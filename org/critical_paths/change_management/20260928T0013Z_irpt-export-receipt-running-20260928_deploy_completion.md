# Deploy Completion Record
**Date opened:** 2026-09-28T00:13:20.209640+00:00
**Status:** OPEN
**Deploy:** irpt-export-render Ulim/gmf -> the pending receipt answers RUNNING with no data per R11 (backend 5c0185fee2; CTO 102223/102227/102237); code only; built-zip cold-start smoke; halves pending; apply after the 03:00-05:00Z freeze
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | artifact build + upload + smoke | census vs live Ulim/gmf: ONLY entry.py differs; zip_cold_start_smoke.py PASS on the export route | publish (export/entry.py + test from backend 5c0185fee2; publish copy before == backend parent 9bc79c8a -> new 4944973e); build-and-upload rc 0; S3 investor-reporting/irpt-export-render.zip VersionId O1Vu8CyDp6aKLZHRur_YhlftYjHrX.1B sha BORQ2shbblG4..; census vs live Ulim/gmf: 59 -> 59, differ entry.py ONLY (the export zip packages no response schema; R11 lives in docs/contracts and the backend test validates the envelope against it). Built-zip cold-start smoke (~Y zip_cold_start_smoke.py, route GET /api/scoped/investor-reporting/export/{exportId}, AWS endpoint dead): PASS, answered UNAVAILABLE to an unauthenticated request, no first-party module from outside the zip; control: the live Ulim/gmf zip also PASSes (no broken zip exists for this change -- the smoke guards cold start, not the RUNNING behavior, which the backend test proves: export 121 passed, R11 validation + pre-R11 negative control). | CLOSED 20260928T002147Z |
| D1 | activation | export root safe-apply (after 05:00Z) | both halves at HEAD; live before-read of a pending/unknown receipt; plan 0/1/0; readback CodeSha; cold start; the same read after; replan 0 |  | OPEN |
| A1 | verify | next K8 window | a pending receipt reads RUNNING and the page keeps polling to READY |  | OPEN |

## Log

- 20260928T001320Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260928T002147Z LEG U1 closed: publish (export/entry.py + test from backend 5c0185fee2; publish copy before == backend parent 9bc79c8a -> new 4944973e)
