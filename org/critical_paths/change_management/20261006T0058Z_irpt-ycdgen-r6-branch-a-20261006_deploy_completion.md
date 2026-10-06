# Deploy Completion Record
**Date opened:** 2026-10-06T00:58:36.301910+00:00
**Status:** OPEN
**Deploy:** IRPT_YCDGEN round 6 branch A: resident package 3d705e700f-st22 (st21 plus the 14 round-6 members), allow list on its placeholder; CTO half 105445, COO half 20261006
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U2 | s3-prefix | irpt-resident-3d705e700f-st22.tar.gz and resident_host_install_3d705e700f-st22.sh at ec2/investor-reporting-ycharts/resident/ | both keys 404 before; read back by version, sha256 equal to the gate's |  | OPEN |
| R1 | verify | CTO step 1: the NEW package's retention module and the RUNNING package's module validate the live v1 retention rows read-only on the host; counts per firm and family; verdicts compared row by row | zero new refusals; zero writes |  | OPEN |
| D2 | activation | resident install via SSM (root 3d705e700f-st22), after R1 passes and the queue reads 0 0 | running root, member digests, unit active, polls, queue 0 0 |  | OPEN |
| V1 | verify | CTO step 2: one READY status read and one retained-artifact read equal to their pre-install answers | equal, or rolled back the same session |  | OPEN |
| A1 | git | irpt-ycdgen-research-v1 ACTIVE with enforcement_ref the full hash of d2b625e697 by rev-parse, after V1 | commit hash |  | OPEN |

## Log

- 20261006T005836Z OPENED by 2.0.0_SA_COO~Y with 5 leg(s)
