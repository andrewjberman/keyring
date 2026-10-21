# TO NFRA_SCHWABBF.TO-AL-r5 -- RDP NLA on the Alongside Schwab Box: record the change made at Andrew's sitting, put the known fix in the runbook, and restore NLA after the sitting

<to_id>NFRA_SCHWABBF.TO-AL-r5</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~SA</issued_by>
<issued_date>2026-10-21</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>alongside-rdp</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `AL-r-5` (`decompositions/NFRA_SCHWABBF_DECOMP_AL1.md`) | **outcome_ref:** FWD-8 |
**depends_on:** `TO-AL-r1` (complete). **Step B waits on the issuer's GO** (a message from `2.0.0_SA_COO~SA` citing this order and saying "sitting done"); do step A now and then wait.

---

## WORKER FACE

### THE CELL

`AL-r-5`. Andrew was in his sitting on 2026-10-21 ~13:4xZ with the SSM port forward open; his `mstsc /v:localhost:13389` refused on Network Level Authentication (NLA). With him live, `1.0.0_SA_CTO` ran ONE SSM command on the box (`144a3975-2edc-44ca-82ca-2972536ccc6e`, 13:45:06Z): on `HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp` it changed `UserAuthentication` from `1` to `0` (the command's own output: `BEFORE UserAuthentication=1`, `AFTER UserAuthentication=0`). The issuer read it back at ~13:5xZ: `0`. The security group still has ZERO ingress rules, so RDP is reachable only through the IAM-gated SSM forward; the Windows Administrator password is still required. The CTO's recommendation, which the issuer follows: restore `1` after the sitting. This order records the change as a box change, puts the fix in the runbook, and restores the setting. You contact Schwab for nothing and read no secret.

### DO, IN THIS ORDER

**Step A (now).**
1. Open and close a RETROSPECTIVE ledger entry with `python .tools/deploy_ledger.py` (read its usage; if it cannot open an entry for an act already done, write the same facts into a closed entry by the tool's nearest route and say what you did) named `nfra-schwabbf-alongside-rdp-nla-off-20261021`: the act (SSM command id above, run by `1.0.0_SA_CTO` with Andrew present), the target (the instance `i-0825aa0ed88342d67`, the registry value, before 1, after 0), the reason (mstsc through `localhost:13389` refused NLA), the containment (zero ingress; IAM-gated forward; the Windows password), and the planned reversal (step B). Leave the entry OPEN with one leg "restore NLA=1" until step B is done; commit entry and sentinel.
2. Runbook: edit `infra/aws/ec2/alongside-schwab-si2/RUNBOOK_ALONGSIDE_SITTING.md` (the one file you may edit there; keep every section) and ADD, inside step (c) after item 2, a numbered item "If `mstsc` refuses with an NLA or CredSSP error (measured at the first sitting, 2026-10-21): the box's RDP security layer requires NLA, and a connection through `localhost` fails it. The known fix, run once for the sitting by CloudOps or the COO over SSM, as SYSTEM: `Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -Name UserAuthentication -Value 0` (read it back). Restore after the sitting with `-Value 1`. While it is 0, RDP is still reachable only through the IAM-gated SSM forward and still asks the Administrator password." Also replace the literal `<instance-id>` with `i-0825aa0ed88342d67` everywhere in the runbook (the box exists now; say in the header comment that a rebuild changes it). Commit with `safe-commit.sh` paths-only.
3. Report step A to `2.0.0_SA_COO~SA` in one message (commit hash), then WAIT for the GO of step B.

**Step B (only on the issuer's GO).**
4. Over SSM (`AWS-RunPowerShellScript`, a `commands` JSON from a NON-SHELL writer, forward slashes in registry paths): set `UserAuthentication` to `1` on `RDP-Tcp`, read it back, run `quser` (the `administrator` session must still be listed; the setting affects NEW connections only, so an open session is not dropped), and confirm the security group still has zero ingress rules. Save the output.
5. Close the ledger entry, commit the evidence, remove nothing else, and report to `2.0.0_SA_COO~SA`: the before and after values and the `quser` line.

### ACCEPTANCE (read by the issuer from your committed files)

<criterion id="AL2-r5-AC1" cell_refs="AL-r-5"><invocation>python .tools/proof-of-spec-check.py org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_SCHWABBF.TO-AL-r5.rdp-nla-record-and-restore.proof_of_spec.json AL2-r5-AC1</invocation><expect>VALID</expect></criterion>
`AL2-r5-AC1` -- the proof instance records the retrospective ledger entry, the runbook edit, and (after step B) the restored value read back with the unchanged `quser` and zero-ingress reads.

<expected_criteria>AL2-r5-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder, the ledger folders, and this order's file. No Terraform, no IAM, no security group, no other box setting.
- **Never:** changing any RDP or Windows setting other than `UserAuthentication` on `RDP-Tcp`; touching the Administrator session, the SI2 app or the Schwab credentials; opening any inbound port; rebooting; `get-secret-value` on any Alongside secret; running step B before the issuer's GO.
- **A surprise row you file is committed AT ONCE** with `bash .tools/safe-commit.sh ... -- <the investigations file and your r5/ files>` (paths only) and its hash sent to `2.0.0_SA_COO~SA`.
- **Refusal clause.** If a step cannot be met as written, stop, write the reason and output in your report and a surprise row, and do not improvise.

<paths>
infra/aws/ec2/alongside-schwab-si2/RUNBOOK_ALONGSIDE_SITTING.md
org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_AL1.md</decomp_doc> (Alongside workstream, enrichment), cell `AL-r-5`.
<owned_cells>AL-r-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AL2-r5-AC1. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_SCHWABBF.TO-AL-r5.rdp-nla-record-and-restore.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> AL2-r5-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT (your final messages to `2.0.0_SA_COO~SA`):** after step A, and after step B, as described.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; the rules stay DISABLED.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the finding is the change itself: NLA off weakens the RDP pre-authentication, contained by zero ingress, the IAM-gated forward and the Windows password; it is restored after the sitting.
lane: the <paths> block IS the grant; CloudOps seats act on box settings under a task order (rule 34).
</preflight>

Source: CTO msg 110105 (the change, SSM command 144a3975-2edc-44ca-82ca-2972536ccc6e); decomposition cell AL-r-5.
