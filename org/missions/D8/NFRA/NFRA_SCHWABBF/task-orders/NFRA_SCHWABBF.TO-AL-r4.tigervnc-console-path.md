# TO NFRA_SCHWABBF.TO-AL-r4 -- a TigerVNC console path on the Alongside Schwab Box for Andrew's sign-in (server bound to localhost, reached by the SSM port forward; RDP stays the fallback)

<to_id>NFRA_SCHWABBF.TO-AL-r4</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~SA</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>alongside-vnc</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `AL-r-4` (`decompositions/NFRA_SCHWABBF_DECOMP_AL1.md`) | **outcome_ref:** FWD-8 |
**depends_on:** `TO-AL-r1` (complete). **PRIORITY: this order goes BEFORE `TO-AL-r3` if r3 has not started its apply** (Andrew is waiting to sign in; r3 only prepares the run records). It touches no Terraform and no IAM; if r3 is already running, finish r3's current step, then do this; never run both on the box in the same minute.

---

## WORKER FACE

### GO

GO -- written by 2.0.0_SA_COO~SA 2026-10-20 ~21:2xZ on Andrew-direct ~20:5xZ relayed by `1.0.0_SA_CTO` msg 110025 (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/` @a7852b5b44). Andrew, verbatim: "Can do this any time" and "I recommend Tiger VNC for the port". The CTO asked for: a TigerVNC server on the box bound to localhost only with no ingress, reached by the same SSM port forward (portNumber 5900), the TigerVNC viewer on his side, RDP kept as the fallback, the runbook updated, and a message when the box has the server. The security group stays at ZERO ingress rules (this order changes no Terraform and no security group). The four rules stay DISABLED; no Schwab call.

### THE CELL

`AL-r-4`. Andrew signs the SI2 app in on the box. TigerVNC attaches to the CONSOLE session directly, so he has no RDP disconnect and re-attach to manage (the box's `SchwabKeepConsole` task, which re-attaches a disconnected Administrator session to the console every 5 minutes, stays as a backstop). The box is `i-0825aa0ed88342d67` (Windows Server 2022, Administrator on the `console` session by auto-logon; SSM Online; AWS CLI v2 installed). You install the TigerVNC Windows server from the official release, configure it, prove it works from this laptop, add an install script and a runbook section to the repo, and report. Your lane admits an AE seat to `infra/aws/ec2/`, so you author the script yourself and iterate on the live box with measurements; the box holds NO Schwab session yet, so a failed experiment costs nothing but you must leave it as you found it if a check fails.

**What the issuer measured (2026-10-20 ~21:2xZ, read-only, from this laptop):** the latest TigerVNC release is `v1.16.2` (2026-03-26). Its Windows binaries are on SourceForge, folder `https://sourceforge.net/projects/tigervnc/files/stable/1.16.2/`: the server installer is `tigervnc64-winvnc-1.16.2.exe` (the same folder holds `tigervnc64-1.16.2.exe`, `vncviewer64-1.16.2.exe`, `vncviewer-1.16.2.exe`). The GitHub release page only points at SourceForge. The SourceForge folder's RSS (`https://sourceforge.net/projects/tigervnc/rss?path=/stable/1.16.2`) lists the files and carries their hashes. **UNMEASURED, so you measure it and write what you find:** the installer's silent switches (TigerVNC's Windows installers are Inno Setup builds, whose switches are `/VERYSILENT /SUPPRESSMSGBOXES /NORESTART /SP-`; check with `/?` or the file's version info before relying on it), the server's service name, its registry settings key (expected `HKLM:\\SOFTWARE\\TigerVNC\\WinVNC4`; expected values `LocalHost` DWORD 1 and `SecurityTypes` String `None`; confirm against the documentation shipped in the install folder or the server's behavior), and whether service mode attaches to the console session (it must show the Administrator desktop, not only a logon screen).

**Design (the issuer's rulings inside this order):**
1. **Authentication.** No VNC password: `SecurityTypes = None` with the server bound to 127.0.0.1 only. The gate is the IAM-authenticated SSM port forward (only a principal allowed `ssm:StartSession` on this instance reaches the port), the same principals that can already run SSM commands as SYSTEM on the box. State this plainly in the runbook; it is weaker than RDP's password prompt for anyone holding SSM rights, no weaker than they already are. If you find the server refuses `None` or a password is mandatory, STOP and report; do not invent a password store.
2. **Fail closed.** After configuring, the listening socket must be `127.0.0.1:5900` ONLY (`Get-NetTCPConnection -LocalPort 5900 -State Listen`); a listener on `0.0.0.0` or `::` means the setting did not take: stop the service, report, leave the box without a VNC service running.
3. **Code from S3, not inline** (the archetype's rule 12): the installer and your script are uploaded to `s3://opal-data-assets/code/alongside-schwab-si2/` (the box role reads that prefix) and fetched by the box; do not paste the script into an SSM command.

### DO, IN THIS ORDER (on the laptop; the pinned worktree is for your repo edits)

0. DISK: `df` on `C:` at least 5 GB free, else stop and report the figure.
1. Pinned worktree at the current trunk HEAD (`git worktree add --detach <scratch outside every other worktree> HEAD`), sparse checkout of `.tools`, `lib`, `infra/aws/ec2/alongside-schwab-si2`, `org/critical_paths`, and this project folder. Your repo edits (script, runbook) are made in YOUR worktree and committed with `safe-commit.sh` paths-only.
2. Fetch and verify the installer on THIS laptop first: read the SourceForge RSS for `tigervnc64-winvnc-1.16.2.exe` and its published md5; download it to a scratch folder with `curl -L` (follow the redirect; SourceForge sends an HTML page to some clients, so check the result is a PE file: the first two bytes are `MZ` and the size is in megabytes, not kilobytes); compute md5 and SHA-256; the md5 MUST equal the published one, else stop. Record the URL, size, md5 and SHA-256 in `.../deliverables/0.7.0_AE_CloudOps~NFRA1/r4/installer.txt`.
3. Author `infra/aws/ec2/alongside-schwab-si2/install-tigervnc.ps1` (ASCII only; Windows PowerShell 5.1; `OK:`/`ERROR:` lines; every step checked; `throw` on failure; idempotent): parameter `-Installer` (path); skip the install if the TigerVNC service and files are already present (print `OK: present`); otherwise run the installer silently with the switches you MEASURED, require exit 0; write the registry settings of design 1; set the service to Automatic and (re)start it; check design 2 (fail closed: on a wrong listener it stops the service and exits 1); print the service name, the install folder, and the listening socket. Parse it with the PowerShell parser (`[System.Management.Automation.Language.Parser]::ParseFile`) before upload.
4. Upload `tigervnc64-winvnc-1.16.2.exe` and `install-tigervnc.ps1` to `s3://opal-data-assets/code/alongside-schwab-si2/` with `aws s3 cp ... --sse AES256 --only-show-errors`.
5. Install on the box over SSM (`AWS-RunPowerShellScript` as SYSTEM, a `commands` JSON from a NON-SHELL writer, forward slashes in on-box paths): fetch both files to `C:/schwab-sdd/` with `& 'C:/Program Files/Amazon/AWSCLIV2/aws.exe' s3 cp ...`, check the installer's SHA-256 on the box equals step 2's, then `powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:/schwab-sdd/install-tigervnc.ps1 -Installer C:/schwab-sdd/tigervnc64-winvnc-1.16.2.exe`. Read the output: every line `OK:`, invocation `Success`. Save to `.../r4/install_invocation.json`. If the script fails, do ONE diagnosis pass with read-only SSM probes, fix the script in your worktree, re-upload and re-run; after a second failure stop, uninstall what you installed (state exactly what you removed) and report.
6. Prove it from THIS laptop through the forward: `aws ssm start-session --target i-0825aa0ed88342d67 --document-name AWS-StartPortForwardingSession --parameters "portNumber=5900,localPortNumber=15900"` in the background; then a short Python script (stdlib `socket`) that connects to `127.0.0.1:15900`, reads the 12-byte banner (`RFB 003.008` or similar), replies with the same version, reads the security-type list (it must offer type 1 = None), selects it, sends ClientInit (shared flag 1), and reads ServerInit (width, height, pixel format, desktop name); print them. Then end the session with `aws ssm terminate-session` and confirm no active session remains to the target (`aws ssm describe-sessions --state Active --filters key=Target,value=i-0825aa0ed88342d67`). The width and height must be a real desktop size (not 0). Also re-test the RDP forward still connects (port 3389 to local 13389, TCP connect only), then end it. Save the outputs and the Python script to `.../r4/`.
7. Confirm nothing else moved: `quser` over SSM still lists `administrator` on `console` `Active`; the security group still has ZERO ingress rules (`aws ec2 describe-security-groups`); the four rules are still DISABLED. Save to `.../r4/after.txt`.
8. Runbook: edit `infra/aws/ec2/alongside-schwab-si2/RUNBOOK_ALONGSIDE_SITTING.md` (you may edit this one file; keep every existing section, including RDP as the fallback): ADD a section "Console via TigerVNC (preferred for the first sign-in)" BEFORE the RDP steps: (a) get the viewer on Andrew's side: the official portable viewer `vncviewer64-1.16.2.exe` from `https://sourceforge.net/projects/tigervnc/files/stable/1.16.2/` (no installer, no admin); (b) open the forward: `aws ssm start-session --target i-0825aa0ed88342d67 --document-name AWS-StartPortForwardingSession --parameters "portNumber=5900,localPortNumber=15900"` and leave that window open; (c) in the viewer connect to `localhost::15900` (two colons = a TCP port, not a display number; state that you verified or did not verify this form against the viewer); (d) he lands on the Administrator desktop that is already logged on by auto-logon (no password prompt); (e) the SI2 install and sign-in steps are the same as the RDP section's; (f) when finished close the viewer: nothing to disconnect, the session stays logged on, and the keep-console task is only a backstop; (g) the security note of design 1; (h) how to remove it: the exact uninstall command you measured. Say in one sentence what you could not verify (a person watching the desktop in a real viewer is the first full proof). Add the install script to the "What carries over" or a short "Files" list if the runbook has one.
9. Commit (repo edits, evidence) with `safe-commit.sh` paths-only, remove the pinned worktree if clean, and report to `2.0.0_SA_COO~SA`: **VNC READY** only if steps 5-7 passed, with the service name, the listening socket line, the RFB banner and ServerInit line, the installer's md5/SHA-256, the commit hash; otherwise the first failed step and its output.

### ACCEPTANCE (read by the issuer from your committed files)

<criterion id="AL2-r4-AC1" cell_refs="AL-r-4"><invocation>python .tools/proof-of-spec-check.py org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_SCHWABBF.TO-AL-r4.tigervnc-console-path.proof_of_spec.json AL2-r4-AC1</invocation><expect>VALID</expect></criterion>
`AL2-r4-AC1` -- the proof instance records the installer md5 against the published one, the install verdict lines, the listening socket, the RFB handshake and ServerInit from the laptop, and the unchanged quser / zero-ingress / DISABLED reads as artifact rows.

<expected_criteria>AL2-r4-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. No Terraform, no IAM, no security-group change, no fence, no registry.
- **Never:** opening any inbound port; a VNC service listening on anything but 127.0.0.1; `get-secret-value` on any Alongside secret; enabling a rule; running the SI2 app, the puller, the entitlement script or any Schwab call; stopping or terminating the instance; rebooting it (not needed); editing `bootstrap.ps1` or any other box script.
- **A surprise row you file is committed AT ONCE** with `bash .tools/safe-commit.sh ... -- <the investigations file and your r4/ files>` (paths only) and its hash sent to `2.0.0_SA_COO~SA`.
- **Refusal clause.** If a step cannot be met as written, stop, leave the box as you found it (uninstall anything you installed and say what), write the reason and output in your report and a surprise row, and do not improvise a weaker control.

<paths>
infra/aws/ec2/alongside-schwab-si2/install-tigervnc.ps1
infra/aws/ec2/alongside-schwab-si2/RUNBOOK_ALONGSIDE_SITTING.md
org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_AL1.md</decomp_doc> (Alongside workstream, enrichment), cell `AL-r-4`.
<owned_cells>AL-r-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AL2-r4-AC1. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_SCHWABBF.TO-AL-r4.tigervnc-console-path.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> AL2-r4-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message and a message to `2.0.0_SA_COO~SA`):** as step 9.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; the rules stay DISABLED.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the box role's existing read of the code-home prefix fetches the two files.
comp-adversary: DECLARED-NOT-APPLICABLE -- finding: the installer comes from SourceForge, so its md5 is checked against the published value and its SHA-256 is carried to the box; the weaker control (no VNC password, localhost bind, SSM-authenticated forward) is stated, not hidden.
lane: the <paths> block IS the grant; CloudOps seats act on box software under a task order (rule 34).
</preflight>

Source: Andrew-direct ~20:5xZ 2026-10-20 via CTO msg 110025; PRD v1.0 C-ALONGSIDE ("The first sign-in is a person's act"); `TO-AL-r1` evidence; decomposition cell AL-r-4.
