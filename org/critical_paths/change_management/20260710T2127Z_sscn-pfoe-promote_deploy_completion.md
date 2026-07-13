# Deploy Completion Record
**Date opened:** 2026-07-10T21:27:13.370943+00:00
**Status:** CLOSED
**Deploy:** Portal DEV->PROD promote: SSCN_PFOE 7db8f6b5 -> v2.1.134 (opalinvest.dev). PFOE 16-factor Security Scanner preset + DIVZ relabel. FE-only, single file constants.ts. Rollback base 86ebd471 (v2.1.133). Andrew-direct via COO~C GO; CTO~C arch-gate PASS.
**Authored by:** 0.3.0_DT_TradingOperations
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | origin/PROD merge --no-ff origin/DEV(7db8f6b5) pushed | PROD merge SHA pushed |  | OPEN |
| L2 | activation | CI deploy.yml -> opalinvest.dev server + annotated tag portal-v2.1.134 | gh run conclusion=success + tag exists |  | OPEN |
| L3 | verify | CI conclusion success + peeled tag == PROD head + live site | gh run view --json conclusion + git rev-parse tag^{commit} |  | OPEN |
| L4 | git | workspace gitlink bump on CLOUD pushed | CLOUD commit hash pushed |  | OPEN |

## Log

- 20260710T212713Z OPENED by 0.3.0_DT_TradingOperations with 4 leg(s)

---

## CLOSED 2026-07-13T07:20Z -- by 2.0.0_SA_COO (NEVER#6 gate owner). VERIFIED AGAINST LIVE STATE, not the record.

**This ledger was OPEN + UNINDEXED for ~3 days and was STRUCTURALLY INVISIBLE to `deploy_ledger.py check --red`**
(a hand-authored markdown ledger carries no `.open_deploys/*.json` sentinel, so the sentinel-only scan cannot see
it). The new gate-bypass scan surfaced it 20260713T0715Z. **The gate reported `0 stranded` the whole time.**

**THE DEPLOY ITSELF LANDED. This was stale PAPERWORK, not a stranded deploy** -- NEVER#6 binds on APPLIED legs,
and every applied leg is proven below. Verified by COO against live git/PROD, NOT from the author's report:

| leg | proof (COO-verified, live) |
|---|---|
| L1 | `7db8f6b5` **is an ancestor of `origin/PROD`** (`git merge-base --is-ancestor` -> true). The code IS on PROD. |
| L2 | annotated tag **`portal-v2.1.134` EXISTS**; peeled `5337b8159a7c`. |
| L3 | `origin/PROD` has since advanced to **`portal-v2.1.135`** -- the promote landed AND the pipeline kept working after it. |
| L4 | gitlink bump on CLOUD: **`8566967f6`** (0.3.0_DT) -- "live PROD=5337b8159 tag portal-v2.1.134 ... CI run 29125030758 SUCCESS". |

**Author `0.3.0_DT_TradingOperations` is not currently live; closed by the gate owner on evidence rather than left
to rot.** No leg is closed on a self-report; each cites a live primitive.
