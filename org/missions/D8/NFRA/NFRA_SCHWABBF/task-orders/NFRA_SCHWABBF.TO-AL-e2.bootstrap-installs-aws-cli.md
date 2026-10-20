# TO NFRA_SCHWABBF.TO-AL-e2 -- bootstrap.ps1 installs the AWS CLI v2 itself (a rebuild reproduces without a manual step)

<to_id>NFRA_SCHWABBF.TO-AL-e2</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~17</issued_to>
<issued_by>2.0.0_SA_COO~SA</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>alongside-state</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `AL-e-2` (`decompositions/NFRA_SCHWABBF_DECOMP_AL1.md`) |
**outcome_ref:** FWD-8 | **depends_on:** `AL-e-1` (merged)

---

## WORKER FACE

### THE CELL

`AL-e-2`. The Alongside Schwab Box was built on a stock Windows Server 2022 image. It carries AWS Tools for PowerShell but NOT the AWS CLI v2, so `bootstrap.ps1` (which calls `C:\Program Files\Amazon\AWSCLIV2\aws.exe` and throws at its own line ~21 if absent) failed on 2026-10-20 (row `NFRA_SCHWABBF-S2`). The issuer's order for the live build added a manual SSM step that installed the CLI from AWS's official MSI. This cell moves that step INTO `bootstrap.ps1`, so a rebuilt box needs no manual step. Nothing is run: WORLD only because the file sits under `infra/`.

**The measured facts you build on** (CloudOps `0.7.0_AE_CloudOps~NFRA1`, 2026-10-20 ~18:4xZ, evidence in `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/r1/step9a_*_invocation.json`, read them): the working install was `Invoke-WebRequest -UseBasicParsing https://awscli.amazonaws.com/AWSCLIV2.msi -OutFile <msi>` then `Start-Process msiexec.exe -ArgumentList '/i',<msi>,'/qn','/norestart' -Wait -PassThru`, exit code 0, then `aws.exe --version` printed `aws-cli/2.38.2`. **`msiexec` returned 1619 on a FORWARD-SLASH msi path and 0 on a BACKSLASH path** (row `NFRA_SCHWABBF-S3`): build the msi path with `Join-Path` or a backslash literal inside the script, never a forward-slash string.

**Build (edit only `infra/aws/ec2/alongside-schwab-si2/bootstrap.ps1` and its test).**
1. Read the current `bootstrap.ps1` first. Its comment at lines ~19-21 says the CLI is installed for the box user and it throws if `aws.exe` is missing. Replace that throw with an `Ensure-AwsCli` step that runs FIRST (before anything that calls aws): if `C:\Program Files\Amazon\AWSCLIV2\aws.exe` is absent: set TLS 1.2, create `C:\schwab-sdd`, download the MSI to `C:\schwab-sdd\AWSCLIV2.msi` (backslash path), run `msiexec` as above and require exit code 0 or 3010, require `aws.exe --version` to print `aws-cli/2.`, delete the MSI, and print `OK: aws cli v2 installed (<version line>)`; if it is already present print `OK: aws cli v2 present (<version line>)`; any failure prints `ERROR: ...` and `throw`s. Everything after it is unchanged, byte for byte. ASCII only.
2. A chicken-and-egg note in a comment: the script is itself fetched with the CLI, so a fresh box's FIRST fetch of `bootstrap.ps1` uses `Read-S3Object` from AWS Tools for PowerShell (present on the stock image) via the instance profile; say that one sentence in the header comment and put the exact one-line command in `RUNBOOK_ALONGSIDE_SITTING.md`'s "Not in this runbook" neighbour section "Rebuilding the box" (ADD that short section; edit nothing else in the runbook): `Import-Module AWSPowerShell; Read-S3Object -BucketName opal-data-assets -Key code/alongside-schwab-si2/bootstrap.ps1 -File C:\schwab-sdd\bootstrap.ps1`, then `powershell -ExecutionPolicy Bypass -File C:\schwab-sdd\bootstrap.ps1`.
3. Tests in `data/canonical/schwab/tests/test_alongside_box_scripts.py` (keep every existing test green; the old BOOTSTRAP test that pins "throws when aws.exe is missing" must be changed to pin the new behavior): ADD a test whose name contains `ensure_awscli`: `bootstrap.ps1` contains the official MSI URL `https://awscli.amazonaws.com/AWSCLIV2.msi`, `msiexec`, the `/qn` and `/norestart` switches, the accepted exit codes 0 and 3010, the `aws-cli/2.` check, and builds the MSI path with a backslash (no forward-slash MSI path string appears in the script); the `Ensure-AwsCli` call precedes the first use of `$AWS` / `aws.exe` for anything else; the file parses with the PowerShell parser and is ASCII.

### ACCEPTANCE

<criterion id="AL2-e2-AC1" cell_refs="AL-e-2"><invocation>python -m pytest data/canonical/schwab/tests/test_alongside_box_scripts.py -q -p no:cacheprovider --color=no -k "ensure_awscli"</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`AL2-e2-AC1` -- the bootstrap installs the CLI itself, with the backslash msi path and the accepted exit codes, before it needs the CLI.

<criterion id="AL2-e2-AC2" cell_refs="AL-e-2"><invocation>python -m pytest data/canonical/schwab/tests/test_alongside_box_scripts.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`AL2-e2-AC2` -- the whole box-scripts test file stays green with the edit.

<expected_criteria>AL2-e2-AC1,AL2-e2-AC2</expected_criteria>

Dry-run at the base 2026-10-20: AC1 has no `ensure_awscli` test (0 selected) -- FAIL as expected; AC2 passes (13 passed) -- a CONTROL; it grades the edited BOOTSTRAP test after your change. Write the `ensure_awscli` test first and watch it fail.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit (the other scripts in the folder, the Terraform).
- **WORLD floor, nothing run.** You run no script, no AWS command, no download.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W17-S<k>`, `surfaced_at` = `date -u +%FT%TZ`), and do not weaken a test.

<paths>
infra/aws/ec2/alongside-schwab-si2/bootstrap.ps1
infra/aws/ec2/alongside-schwab-si2/RUNBOOK_ALONGSIDE_SITTING.md
data/canonical/schwab/tests/test_alongside_box_scripts.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_AL1.md</decomp_doc> (Alongside workstream, enrichment), cell `AL-e-2`.
<owned_cells>AL-e-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AL2-e2-AC1, AL2-e2-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~17/NFRA_SCHWABBF.TO-AL-e2.bootstrap-installs-aws-cli.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> AL2-e2-AC1,AL2-e2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the changed regions of `bootstrap.ps1` with line numbers, the pytest summary lines, whether the PowerShell parse arm ran, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule edit.
comp-iam: DECLARED-NOT-APPLICABLE -- the MSI comes from AWS over HTTPS; no S3 grant is involved.
comp-adversary: DECLARED-NOT-APPLICABLE -- the finding (a stock image lacks the CLI; the msi path form matters) is measured by CloudOps and inlined above.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v1.0 C-ALONGSIDE; rows `NFRA_SCHWABBF-S2` and `NFRA_SCHWABBF-S3`; decomposition `NFRA_SCHWABBF_DECOMP_AL1.md` cell AL-e-2.
