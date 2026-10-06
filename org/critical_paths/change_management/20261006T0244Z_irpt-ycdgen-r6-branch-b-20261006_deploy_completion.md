# Deploy Completion Record
**Date opened:** 2026-10-06T02:44:56.424584+00:00
**Status:** OPEN
**Deploy:** IRPT_YCDGEN round 6 branch B: resident package 09139ee34d-st23 (st22 plus the 11 named files, the Overview map and the opal_map binding), Andrew's sign-in on the Opal allow list; CTO half 105481, COO half in the packet
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U2 | s3-prefix | irpt-resident-09139ee34d-st23.tar.gz and resident_host_install_09139ee34d-st23.sh at ec2/investor-reporting-ycharts/resident/ | both keys 404 before; read back by version, sha256 equal to the gate's |  | OPEN |
| R1 | verify | the NEW package's retention module and the RUNNING st22 module validate the same live v1 retention rows read-only on the host | 0 verdict differences, 0 new refusals, 0 writes |  | OPEN |
| P1 | verify | pre-install step-2 answers: one READY job and one retained PDF read by version | answers recorded |  | OPEN |
| D2 | activation | resident install via SSM (root 09139ee34d-st23) with the renderer drop-in | running root, member digests, drop-in effective, unit active, queue 0 0 |  | OPEN |
| V1 | verify | post-install step-2 reads equal the pre-install answers; producer and map import smoke | equal, or rolled back the same session |  | OPEN |
| F1 | verify | Andrew submits a Cottonwood Overview as himself on the development build and opens the Opal report; run record, retained PDF hash, report status and clocks read | report opened by Andrew |  | OPEN |
| M1 | git | the allow-list constant (resident_worker.py and its test) lands on CLOUD after F1 | commit hash |  | OPEN |

## Log

- 20261006T024456Z OPENED by 2.0.0_SA_COO~Y with 7 leg(s)
