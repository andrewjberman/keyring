# TO NFRA_SCHWABBF.TO-AL-r2 -- the Alongside Schwab Box, first contact: read the login's entitlement list, pull ONE day for each Cottonwood master it sees, and trace each day

<to_id>NFRA_SCHWABBF.TO-AL-r2</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~SA</issued_by>
<issued_date>2026-10-20</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>alongside-first-trace</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `AL-r-2` (`decompositions/NFRA_SCHWABBF_DECOMP_AL1.md`) | **outcome_ref:** FWD-8 |
**depends_on:** `TO-AL-r1` (complete, box ready). **GO:** this order is `staged`. The issuer writes the GO line below and flips it to `pending` when Andrew's sign-in on the box is reported done. Do not act before that flip.

---

## WORKER FACE

### GO

(not yet written; it names Andrew's sign-in record.)

### THE CELL

`AL-r-2`. PRD v0.9 C-ALONGSIDE: "The first read after the session exists is that login's own entitlement list (`FetchDetails/UserMasters.aspx`): whether it sees the four is unmeasured until then, and a master it does not see is named, not assumed." FWD-8 DONE WHEN: "one trace: a Cottonwood account group's day pulled by the Alongside box, stored at the builder's address and read." Andrew-direct ~16:3xZ: "I want the new Cottonwood accounts taken care of". The box is `i-0825aa0ed88342d67` (the Alongside Schwab Box, built by `TO-AL-r1`); Andrew has signed the SI2 app in on it. You run the entitlement read, then ONE day of bronze per entitled master, then the trace. **CTO condition 6 binds you (CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_HALF_CTO_NFRA_SCHWABBF_ALONGSIDE_BOX_BUILD_20261020.md`): no rule is enabled and no pull runs beyond the first-day trace. One day per master is the whole of this order.**

**Why a scheduled task:** an SSM command runs as SYSTEM, whose credential vault is empty. The Schwab token is in ADMINISTRATOR's vault. Every Schwab-touching script therefore runs as a one-shot scheduled task registered `/RU Administrator /IT /RL HIGHEST` with the SSM command waiting for it, exactly as the schedule rules do (`infra/aws/terraform/alongside-schwab-ec2/schedule.tf`, the `commands` list: read it first, copy its register / start-proof / wait / propagate-exit-code lines; its `$ErrorActionPreference='Continue'` choice stays).

### DO, IN ORDER

1. Read first: `infra/aws/terraform/alongside-schwab-ec2/schedule.tf` (the `commands` list), `infra/aws/ec2/alongside-schwab-si2/sdd-entitlements.ps1` (parameters, exit codes 0 / 10 / 3 / 8 / 9), `sdd-daily-pull.ps1` (parameters `-Master`, `-Target monolith`, `-OnlyAsOf yyyy-MM-dd`, `-SnsTopicArn`, exit codes, the session lock), and `RUNBOOK_ALONGSIDE_SITTING.md`. Write every SSM `commands` JSON with a NON-SHELL writer and use forward slashes in on-box paths (a backslash typed through a shell is halved, and `msiexec` failed on a forward-slash MSI path in `TO-AL-r1`, row `NFRA_SCHWABBF-S3`: if a tool rejects a slash form, say so).
2. Precheck over SSM (read-only): `quser` (an `administrator` session, `console` or `Disc`), and that `C:/schwab-sdd/sdd-entitlements.ps1` and `sdd-daily-pull.ps1` exist. If the session is absent or the SI2 app is not installed (`Get-ChildItem C:/Users/Administrator/AppData/Local/Apps/2.0 -Recurse -Filter Schwab.SI.Framework.dll`), STOP and report: Andrew's sign-in did not take.
3. ENTITLEMENT READ: one Administrator scheduled task running `powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:/schwab-sdd/sdd-entitlements.ps1` (default masters, default `-OutDir`). Wait for it; print the script's output lines (`LISTED=`, `ENTITLED`/`NOT-ENTITLED` per master) and its exit code; copy the JSON it wrote (`Get-Content` of the newest `entitlements-*.json`) into `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/r2/entitlements.json`. Exit 0 (all four) or 10 (some): go on. Exit 3 or 8 or 9: STOP and report the output (3 = token missing: the sign-in left no vault token; 8 = wrong identity; 9 = the response shape differs: the script printed the property names). A master that is `NOT-ENTITLED` is NAMED in your report and is Andrew's call to Cottonwood (PRD C-ALONGSIDE); you do not pull it.
4. THE DAY: `D` = the last trading day before today by `lib/trading_calendar.py` (`prev_trading_day` of today's Eastern date; print the call and its result). For each ENTITLED master, one at a time (the box has ONE Schwab session and a session lock; never two at once), run an Administrator scheduled task: `powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:/schwab-sdd/sdd-daily-pull.ps1 -Master <master> -Target monolith -OnlyAsOf <D> -LookbackDays 10 -SnsTopicArn arn:aws:sns:us-east-1:313476888478:opal-critical-surface-alerts`. Wait; print the log tail (`Get-Content C:/schwab-sdd/daily/<master>/daily-pull.log -Tail 30`) and the exit code; the run must end `DAILY PULL OK`. A manifest-write WARN (the meta/pulls grant is master-scope and PRD v0.9/v1.0 moved state to the firm bucket) is EXPECTED and is not a failure; a bronze `PutObject` denial IS a failure: stop and report it. If a day has no files on a trading day the puller dies loud: report it, do not retry with another window.
5. LANDED READ (from the laptop, your own identity; the box role cannot read): for each pulled master, `aws s3api list-objects-v2 --bucket opal-data-assets --prefix schwab/cottonwood/bronze/ --query` restricted to keys containing `/date=<D>/<master>.`; print the count and 3 sample keys; every key must equal `lib/opal_naming.py address('schwab','cottonwood','bronze',<type>,'date=<D>')` plus `/` plus the vendor file name (print that address call beside a sample). Then `python data/canonical/schwab/keyform/thread_trace.py --master <master> --day <D> --form builder` from the pinned worktree at HEAD and save its output; the bronze hop must read held. (The silver hop may read NOT-HELD: the converter's firm event rule and the state-tier IAM are later acts; say what it reads.)
6. Save every output under `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/r2/`, commit with `safe-commit.sh` paths-only, and report to `2.0.0_SA_COO~SA`: the entitlement result per master, the day D, per pulled master the exit code, `DAILY PULL OK` or the failure, the object count, the trace line, any row id. Leave the Administrator session logged on and the rules DISABLED.

### ACCEPTANCE (read by the issuer from your committed files)

<criterion id="AL1-r2-AC1" cell_refs="AL-r-2"><invocation>python .tools/proof-of-spec-check.py org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_SCHWABBF.TO-AL-r2.entitlement-read-and-first-day.proof_of_spec.json AL1-r2-AC1</invocation><expect>VALID</expect></criterion>
`AL1-r2-AC1` -- the proof instance records the entitlement result, the day D, the pull verdict and object count per pulled master, and the trace output as artifact rows.

<expected_criteria>AL1-r2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **Never:** `get-secret-value` on any Alongside secret; enabling a rule; a pull of any master the login does not list; more than one day per master; a second concurrent Schwab session; any command against the 49F box or its resources; reading or pasting the Schwab token; deleting or stopping anything.
- **Refusal clause.** If a step cannot be met as written, stop, write the reason and the output in your report and a surprise row (id `NFRA_SCHWABBF-R2-S<k>`; the gate may renumber it), commit the row AT ONCE with `safe-commit.sh` paths-only and tell the issuer its hash, and do not improvise.

<paths>
org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_AL1.md</decomp_doc> (Alongside workstream, round 1), cell `AL-r-2`.
<owned_cells>AL-r-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AL1-r2-AC1. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_SCHWABBF.TO-AL-r2.entitlement-read-and-first-day.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> AL1-r2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message and a message to `2.0.0_SA_COO~SA`):** as step 6.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the four rules stay DISABLED; the pulls are ad hoc, one day per master, outside any fire.
comp-iam: DECLARED-NOT-APPLICABLE as a tool run -- the box role's per-master bronze write and the cottonwood list grant were applied by TO-AL-r1; a PutObject denial is a stop condition.
comp-adversary: DECLARED-NOT-APPLICABLE -- decomposition finding 4 (204 until entitled) is why the entitlement read precedes every pull.
lane: the <paths> block IS the grant; CloudOps seats act on Schwab-touching infrastructure under a task order (rule 34).
</preflight>

Source: PRD v1.0 C-ALONGSIDE, C-BACKFILL; CTO half condition 6; decomposition `NFRA_SCHWABBF_DECOMP_AL1.md` cell AL-r-2, release acts A5-A6.
