# Deploy Completion Record
**Date opened:** 2026-10-20T23:07:38.399180+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R34O: release r34o of the resident host (FWD-10 comparison, audit wiring, Overview price pages), root /opt/irpt-resident/0485393f3a-r34o, three S3 objects, V2 in the service environment
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | pre-read on the host: running root r34n, r34o root absent, queue 0 0 | P1 STOP-READ-0 PASS |  | OPEN |
| D1 | s3-prefix | three r34o objects uploaded under ec2/investor-reporting-ycharts/resident/ and read back equal | three VersionIds |  | OPEN |
| D2 | activation | signed install on the resident host as root, running root r34o | install rc 0, running root r34o |  | OPEN |
| V1 | verify | after-reads: members, sums, census, bindings, imports, pool, queue | V1 lines |  | OPEN |
| V2 | verify | V2 script inside the service environment | V2S OK SPY KEPT and ZQXWVK NOT_KEPT |  | OPEN |

## Log

- 20261020T230738Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
