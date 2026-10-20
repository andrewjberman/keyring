# TO NFRA_SCHWABBF.TO-AL-e1 -- the Alongside Schwab Box scripts: bootstrap, keep-console, the entitlement read, and the sitting runbook (nothing run)

<to_id>NFRA_SCHWABBF.TO-AL-e1</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~12</issued_to>
<issued_by>2.0.0_SA_COO~SA</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>alongside</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `AL-e-1` (`decompositions/NFRA_SCHWABBF_DECOMP_AL1.md`) |
**outcome_ref:** FWD-8 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`AL-e-1`, the on-box half of PRD v0.5 C-ALONGSIDE. Andrew-direct 2026-10-20 ~13:5xZ: "it should be exact same setup and logic as already exists with the 49 schwab box. this one should explicitly be labeled as an alongside box"; "I will need to RDP into the EC2 box most likely to get that done". The Alongside Schwab Box is a new Windows Server 2022 EC2 (another cell writes its Terraform). This cell writes the PowerShell and the runbook that make it behave like the 49F box, in a NEW folder `infra/aws/ec2/alongside-schwab-si2/`. You run none of them: they need a Windows box, the Schwab app and AWS. WORLD only because the files sit under `infra/`.

**Read first (read-only; edit nothing there):** `infra/aws/ec2/canonical-schwab-si2/bootstrap.ps1` (the style of an SSM-run, idempotent, ASCII bootstrap that calls `C:\Program Files\Amazon\AWSCLIV2\aws.exe` by full path), `sdd-harness.ps1` (the whole file, 5.8 KB: it reads the token and POSTs a `DownloadUserMastersRequest` to `https://si2.schwabinstitutional.com/fileservices/SDDServices/FetchDetails/UserMasters.aspx`, a READ that never rotates the token), and `sdd-daily-pull.ps1` lines ~329-423 (the `CredRead SDDSecure` P/Invoke, the identity check that dies with exit 8 when run as SYSTEM, the loading of the app's `Schwab.SI.*.dll` from `C:\Users\Administrator\AppData\Local\Apps\2.0`, `Get-TypesSafe`, `Invoke-Sdd`), and `infra/aws/terraform/canonical-schwab-ec2/monolith-daily-schedule.tf` lines 82-116 (why the pull must run as Administrator).

**Measured facts about the 49F box that the Alongside copy reproduces (read by the issuer on 2026-10-20 over SSM, read-only):**
- `AutoAdminLogon=1`, `DefaultUserName=Administrator` and a `DefaultPassword` live in `HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon`; the Administrator session is `console`.
- A SYSTEM task `SchwabKeepConsole` (every 5 minutes, `powershell.exe -NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File C:\SchwabData\keep-console.ps1`) re-attaches a DISCONNECTED Administrator session to the console. The script is these two lines, verbatim:
  `$line = (query session 2>$null | Select-String -Pattern 'administrator' | Select-Object -First 1)`
  `if($line -and ($line -match 'Disc')){ if($line -match '\s(\d+)\s+Disc'){ tscon $matches[1] /dest:console 2>$null } }`
- The SI2 app ("Schwab Data Delivery") is a ClickOnce install from `https://si2.schwabinstitutional.com/sdd/Schwab.SI.SI2Desktop.Container.application` (the shortcut `Schwab Data Delivery.appref-ms` carries that URL). The pull code lives in `C:\schwab-sdd\`, data work dirs under `C:\schwab-sdd\daily\<master>`.

**New files, all in `infra/aws/ec2/alongside-schwab-si2/` (create the folder). ASCII ONLY in every file (CLAUDE.md: no non-ASCII in production code; use `OK:`/`WARN:`/`ERROR:`/`SKIP:`).**

1. `keep-console.ps1`: the two lines above, verbatim (a header comment line may precede them; the two lines stay byte-identical).
2. `bootstrap.ps1` (runs once via SSM as SYSTEM on the new instance; idempotent; Windows PowerShell 5.1; `$ErrorActionPreference = 'Continue'`, every step checked and `throw`ing on failure):
   - creates `C:\schwab-sdd` and `C:\SchwabData`; resolves `aws.exe` by full path and throws if absent;
   - IF `C:\SchwabData\bootstrap.done` is absent (or the parameter `-RotatePassword` is passed): generates a 24-character random password with `System.Security.Cryptography.RandomNumberGenerator` (letters and digits only), sets it with `net user Administrator <pw>`, writes `{"username":"Administrator","password":"<pw>"}` to the secret named exactly `schwab/alongside/ec2-credentials` with `aws secretsmanager put-secret-value --secret-id schwab/alongside/ec2-credentials --secret-string file://<temp file>` (a temp file that is deleted in a `finally`; the password is NEVER written to the console, a log or any other secret), then sets the Winlogon values `AutoAdminLogon=1`, `DefaultUserName=Administrator`, `DefaultPassword=<pw>` (the carried 49F property; say so in a comment), then writes the marker file;
   - writes `C:\SchwabData\keep-console.ps1` from the repo copy (fetch it from `s3://opal-data-assets/code/alongside-schwab-si2/keep-console.ps1` with `aws s3 cp`; the box role reads that prefix) and registers the SYSTEM task `SchwabKeepConsole` every 5 minutes with `schtasks`, same action line as above;
   - pulls `sdd-daily-pull.ps1` and `sdd-entitlements.ps1` from the same S3 prefix into `C:\schwab-sdd\`;
   - prints one verdict line per step (`OK: ...` / `ERROR: ...`) and exits 0 only if every step passed.
3. `sdd-entitlements.ps1` (READ-ONLY; runs as Administrator on the box, as a one-shot scheduled task the way the daily pull does): parameters `-Masters` (string array, default the four `08719286`, `08134043`, `08165601`, `08480305`) and `-OutDir` (default `C:\schwab-sdd\entitlements`). It does what `sdd-harness.ps1` does for `UserMasters.aspx`, but: refuses to run as any identity but the one whose vault holds `SDDSecure` (same exit 8 / exit 3 distinction as the daily pull, copied, not reworded); never prints the token; prints the denominator `LISTED=<n> masters in the login's entitlement list`, then one line per requested master `ENTITLED <master>` or `NOT-ENTITLED <master>`; writes a JSON file `entitlements-<UTC yyyyMMddTHHmmssZ>.json` (listed count, requested masters, entitled and not-entitled arrays) into `-OutDir`; exits 0 when every requested master is entitled, 10 when at least one is not (a named, expected outcome, not a crash), 3 or 8 on the credential failures. It writes nothing to S3 and does not touch the SDD session lock files.
4. `RUNBOOK_ALONGSIDE_SITTING.md`: the ordered steps of Andrew's one-time sitting, each with who does it, the command, the expected output and what to do if it differs. It states these in order: (a) prerequisite, the box exists and `bootstrap.ps1` has run (CloudOps); (b) read the Administrator password from the secret `schwab/alongside/ec2-credentials` (value is shown only to Andrew, never pasted into chat or git); (c) RDP WITHOUT a standing ingress rule, by SSM port forwarding: `aws ssm start-session --target <instance-id> --document-name AWS-StartPortForwardingSession --parameters "portNumber=3389,localPortNumber=13389"` then `mstsc /v:localhost:13389`, with the fallback "ask the NFRA CloudOps lane to add ONE temporary TCP 3389 ingress rule from your /32 for the sitting and remove it after"; (d) install the SI2 app: in the Administrator session run `rundll32.exe dfshim.dll,ShOpenVerbApplication https://si2.schwabinstitutional.com/sdd/Schwab.SI.SI2Desktop.Container.application` (state plainly that this exact command is UNVERIFIED on a fresh Server 2022 host and name the fallback, opening the URL in Microsoft Edge in IE mode); (e) sign in with Alongside's Schwab login (the username and password are in the secret `schwab/alongside/sdd-credentials`; Schwab may ask for a security code sent to the registered contact, which Andrew enters); (f) leave the session logged on: DISCONNECT the RDP window, never sign out (the 5-minute keep-console task re-attaches it to the console); (g) tell the COO "signed in"; (h) the COO or CloudOps runs the entitlement read as an Administrator scheduled task and reports which of the four masters the login sees. It ends with a short section "What carries over from the 49F box" (auto-logon with the password in the Winlogon key, the keep-console task, the interactive console session as a single point of failure) and a section "Not in this runbook" (backfill, enabling the schedule).
5. Test `data/canonical/schwab/tests/test_alongside_box_scripts.py` (reads the files as text; runs no script):
   - SYNTAX (name contains `syntax`): for each of the three `.ps1` files, parse with the PowerShell parser through `subprocess` (`powershell.exe -NoProfile -Command` calling `[System.Management.Automation.Language.Parser]::ParseFile`) and require zero parse errors; if `powershell.exe` is not on PATH print `SKIP: powershell.exe not on PATH` and pass. Also: every file in the folder is pure ASCII.
   - BOOTSTRAP (name contains `bootstrap`): the secret id string `schwab/alongside/ec2-credentials` appears and no other `put-secret-value` secret id does; the password variable is never passed to `Write-Output`, `Write-Host` or `Out-File`; `AutoAdminLogon`, `DefaultUserName`, `DefaultPassword`, `bootstrap.done`, `SchwabKeepConsole` appear; `keep-console.ps1` contains the two verbatim lines.
   - ENTITLEMENTS (name contains `entitlements`): the four default masters appear exactly once each in the default; the URL `FetchDetails/UserMasters.aspx`, `SDDSecure`, `NOT-ENTITLED`, `LISTED=` appear; the token variable is never printed; no `aws` S3 write command appears.
   - RUNBOOK (name contains `runbook`): the file contains `AWS-StartPortForwardingSession`, the ClickOnce URL, `schwab/alongside/sdd-credentials`, `schwab/alongside/ec2-credentials`, the words `DISCONNECT` and `UNVERIFIED`, and contains no password-like value (no string after `password` that is 12 or more characters of letters and digits).

### ACCEPTANCE

<criterion id="AL1-e1-AC1" cell_refs="AL-e-1"><invocation>python -m pytest data/canonical/schwab/tests/test_alongside_box_scripts.py -q -p no:cacheprovider --color=no -k "syntax or bootstrap"</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`AL1-e1-AC1` -- the three scripts parse, are ASCII, and the bootstrap writes only its own secret and never prints the password.

<criterion id="AL1-e1-AC2" cell_refs="AL-e-1"><invocation>python -m pytest data/canonical/schwab/tests/test_alongside_box_scripts.py -q -p no:cacheprovider --color=no -k "entitlements"</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`AL1-e1-AC2` -- the entitlement read is read-only, names the four masters, and reports the denominator.

<criterion id="AL1-e1-AC3" cell_refs="AL-e-1"><invocation>python -m pytest data/canonical/schwab/tests/test_alongside_box_scripts.py -q -p no:cacheprovider --color=no -k "runbook"</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`AL1-e1-AC3` -- the sitting runbook has the no-ingress path, the install URL, both secrets by name and no secret value.

<expected_criteria>AL1-e1-AC1,AL1-e1-AC2,AL1-e1-AC3</expected_criteria>

Dry-run at the base 2026-10-20 (the test file does not exist): all three, "file or directory not found" (rc 4) -- FAIL as expected. Write the test first, watch it fail, then build.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit (`canonical-schwab-si2/`, `canonical-schwab-ec2/`, the Terraform).
- **WORLD floor, nothing run.** You do not execute any of these scripts, call AWS or Schwab, upload to S3, or read any secret. The runbook names secrets; it never holds a value.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W12-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test to pass.

<paths>
infra/aws/ec2/alongside-schwab-si2/keep-console.ps1
infra/aws/ec2/alongside-schwab-si2/bootstrap.ps1
infra/aws/ec2/alongside-schwab-si2/sdd-entitlements.ps1
infra/aws/ec2/alongside-schwab-si2/RUNBOOK_ALONGSIDE_SITTING.md
data/canonical/schwab/tests/test_alongside_box_scripts.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_AL1.md</decomp_doc> (Alongside workstream, round 1), cell `AL-e-1`.
<owned_cells>AL-e-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AL1-e1-AC1, AL1-e1-AC2, AL1-e1-AC3. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~12/NFRA_SCHWABBF.TO-AL-e1.alongside-box-scripts-and-runbook.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> AL1-e1-AC1,AL1-e1-AC2,AL1-e1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** each file with its line count, the pytest summary lines, whether the PowerShell parse arm ran or skipped, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule in this cell.
comp-iam: DECLARED-NOT-APPLICABLE as a tool run -- the scripts use the box role AL-a-1 writes (code read, one secret put); BLIND: the live IAM plane.
comp-adversary: DECLARED-NOT-APPLICABLE -- decomposition findings 3 (the ClickOnce install is the person's act) and 4 (204 until entitled: the entitlement read precedes any pull) are inlined above.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.5 C-ALONGSIDE ("The first sign-in is a person's act"); decomposition `NFRA_SCHWABBF_DECOMP_AL1.md` cell AL-e-1, rulings 3, 7, 8; the issuer's 2026-10-20 read-only SSM reads of the 49F box (command ids 6c50525b, 5473d437, 5da3f267).
