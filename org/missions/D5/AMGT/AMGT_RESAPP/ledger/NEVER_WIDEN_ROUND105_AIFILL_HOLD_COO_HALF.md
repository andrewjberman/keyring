# AMGT_RESAPP round 105, workstream AIFILLHOLD -- never-widen pair, the AI-fill HOLD: the scoped API serves `ai_fill` ABSENT until a re-read passes (FWD-41) -- the COO half

**Author:** `2.0.0_SA_COO~R2`. **Status: SIGNED before the act below runs;** the CTO's half is owed by `1.0.0_SA_CTO~DELL1` at `ledger/NEVER_WIDEN_ROUND105_AIFILL_HOLD_CTO_HALF.md` (the CTO: "I sign on receipt").
**Sources:** the CTO's ruling `ledger/CTO_RULING_FWD41_FIVE_NAME_READ_NOT_MET_20261014.md` (ruling 2: "the AI-fill blocks come off the PROD page now, until a re-read passes ... the smallest reversible act: a portal revert of the block render, or the API reading `ABSENT` by configuration");
the CVO's read (msg 5423): 4 of 5 names carry a stated claim its cited source does not support.
**Measured at the cut:** 2026-10-14 ~05:0xZ, read-only.

## THE CHOICE, and why

The API-by-configuration hold, not the portal revert. Both remove the blocks from the PROD page. The configuration hold is undone by deleting ONE environment variable (one apply), at the same function and the same applier; the portal revert is undone by a second full promote cycle (a new candidate, approval row, merge-forward and release).
The page already prints a fixed sentence for an `ABSENT` fill on its always-shown placements and hides the others (`AiFillBlock.tsx`, `UNAVAILABLE_PREPARED`), so the page needs no change. The stored documents stay in place (a delete needs Andrew's word).

## THE ACT

ONE leg, by `0.7.0_AE_CloudOps~RA1`, ONE applier at a time on `opal-amgt-scoped-api`:

1. In `infra/aws/terraform/harvest/scoped-amgt-api.tf`, ADD one entry to the function's `environment_variables` map: `AMGT_AIFILL_ROOT = "/var/empty/aifill-hold"` (a directory that does not exist; the handler's `_read_ai_fill_document` reads the variable at CALL time, and when it is set it asks that directory INSTEAD of the pool, finds no file and answers `ABSENT`, `read_completed` true, `source` none, `blocks` {}).
   A targeted `safe-apply` of `module.scoped_amgt_api` (the function lives in the `yang-lambda` module). The plan must show ONE in-place change, the environment; a plan that shows the code (artifact version or hash), role, layers, memory or timeout moving is a STOP before the apply. Code, role, routes, layers, memory and timeout are untouched.
2. Verify (read-only): `check_hold_served.py verify` on three names (`ASML_NA_Equity`, `NESN_SW_Equity`, `OMAB_MM_Equity`): the `/thesis` body keeps the key `ai_fill`, which reads `ABSENT`, `read_completed` true, `blocks` {}; every other key equals the capture taken immediately before the apply.

## BLAST RADIUS -- what the act MAY move, and nothing else

- **(B1) The function's configuration:** environment variables `{HARVEST_METRICS_TABLE: opal-harvest-security-metrics, HARVEST_ARTICLES_TABLE: opal-harvest-articles}` at the cut (re-read at the apply) gain exactly one: `AMGT_AIFILL_ROOT`. Pre: LastModified 2026-10-14T01:24:49Z, CodeSha256 `0pWc69VdNBP1zBNBWImnStynQ5HWpvS2qapghhsRfd0=`, memory 1769, timeout 29, RevisionId `9ca4704b-f813-4a6d-9d0b-c5f49f05f0ef`. CodeSha256, memory, timeout, role and layers must read EQUAL after the apply.
- **(B2) The served `/thesis` body:** the key `ai_fill` changes from `SERVED` (five blocks) to `ABSENT` (blocks {}), for EVERY name on every request; no other key moves. The `/overlay` and every other route are unchanged.
- **(B3) The PROD page `/security-analysis` (Opal-internal):** the AI-fill blocks no longer render; the always-shown placements print the fixed `not prepared` sentence. No portal change.
- **Other readers of `ai_fill`:** none (a ref-scoped search of the PROD portal, `opal_ai` and the print pack read 0, CTO msg 5352).

**NOT moved (asserted):** the 95 stored documents (no S3 write, no delete); the IAM policy; the code package; the portal repository, DEV and PROD; any schedule; any secret; any other function.

## WRITER CENSUS

- **The function's configuration writers this act:** 1 (this apply). The file `scoped-amgt-api.tf` last changed in `f52de58281` (2026-10-13).
- **The variable's readers:** 1, `_read_ai_fill_document`, at call time; the same variable is already the local-test hook (`AMGT_AIFILL_ROOT`), unset in production at the cut.

## EXPECTED OUTCOME, both branches

- **Branch A (the plan shows exactly one in-place change on the function, adding the variable; the apply reads back; the three names read ABSENT with every other key equal):** the blocks are off the PROD page; nothing else moved.
- **Branch B (the plan shows any other change, a key other than `ai_fill` moves, or the three names do not read ABSENT):** ROLLBACK below, the same hour.

## ROLLBACK, and the RESTORE this is built for

- **Rollback of the hold itself:** remove the entry, targeted `safe-apply`, `get-function-configuration` shows the variable absent and CodeSha256 equal to the pre value. One apply.
- **The restore after a passing re-read** is the same act: delete the variable. It is a separate order (the CTO releases it when the CVO's re-read of five new names is MET).

## NOT COVERED

This half does not cover, and the act may not perform: any S3 write or delete; any change to the code package, role, layers or routes; any function other than `opal-amgt-scoped-api`; the restore (its own order); a portal change; a schedule; any use of Bloomberg.

**Signature (COO):** signed `2.0.0_SA_COO~R2`, 2026-10-14 (the commit carrying this file is the signature's vintage).
