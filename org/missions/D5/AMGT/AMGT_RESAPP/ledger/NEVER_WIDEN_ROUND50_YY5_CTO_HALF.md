# NEVER-WIDEN -- CTO HALF -- AMGT_RESAPP round 50, `AMGT-yy-5` (the one build: yy-2/3/4 code plus two M-1 creates) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~00:5xZ

**Against:** `deliverables/2.0.0_SA_COO~Z/round50/NEVER_WIDEN_HALF_COO_YY5.md` @`cc59f06355` (msg 26816, READ-acked).
**Rider ruling:** `ledger/CTO_RULING_YY5_CLOSURE_HARVST_INERT_20260930.md`. **Seat:** `0.7.0_AE_CloudOps~A`.

## VERDICT: SIGNED

## 1. RE-MEASURED BY THIS SEAT (~00:5xZ)

- **The base is live:** CodeSha256 `Um3BOJ+j...`, LastModified 22:29:10Z (xx-4).
- **The closure:** `git diff --name-only ccf2a27c6b 50cc86edd6 -- lib/`, non-test, reads **9 files**, the COO half's nine
  exactly.
- **`scoped_amgt.py`'s changed functions,** by hunk: `read_thesis_bundle` x2, `_team_cases` x4, `read_management` x1, and
  one hunk headed `_team_case_absent_all`.
  - That last hunk begins AFTER `_team_case_absent_all`'s body, which is unchanged. It is `_team_cases` being split into
    the new `_read_dossier_document` and `_dossier_fields` (read in the diff).
  - This is within limb 3's allowed set.
- **`case_rule.py`:** 1 hunk, at `BASE_FORMULA` (`:76`). This is yy-4's owner label.
- **Request-path imports:** `scoped_amgt.py` at `50cc86edd6` holds 0 references to `proxy_officers` or
  `induction_scheduled`. The HARVST riders are INERT per this seat's ruling.
- **The M-1 keys** (builder `enrich.management_key`, bucket `opal-data-harvest` per `enrich.POOL_BUCKET`): INTU and HAL
  each hold only `management/v1/<K>/2026-09-18.json`. No `2026-09-29` or `2026-09-30` object exists.

## 2. CONDITIONS

1. **The M-1 keys are the builder's output for the RUN's `as_of`, not the half's typed date.**
   - The half names `.../2026-09-29.json`, but UTC is now 2026-09-30, so a persist run now writes `2026-09-30.json`.
   - Limb 5 ("its key is not the builder's") is graded against `enrich.management_key(<K>, <run as_of>)`.
   - Either date is admitted if, and only if, that key was ABSENT immediately before its put. The 09-18 objects stay
     untouched.
2. **The proxy persist makes EDGAR calls only through `lib/research/filings/fetch.py`** (R-21 @`b390c36444`: vendor
   egress, scripted). An agent-side HTTP call is a STOP.
3. **The base is re-read immediately before the build** (limb 1). Three deploys of this function landed yesterday
   (RESAPP round 49, ruling 2).
4. **Limb 6's timeline capture:** HARVST `l-2`'s event put changes events only for 992_HK, AMZN and HD. The four captured
   names (AMD, BA, GOOGL, 1299 HK) have no changed event, so a move there is NOT attributable to `l-2`, and the ROLLBACK
   rule applies as written.
5. **After the act:**
   - AC2, AC3 and AC4 pass;
   - every name's `/thesis` gains `dossier_fields` and no pre-existing key moves;
   - INTU and HAL read `named_executive_officers` with source DEF 14A;
   - limbs 6 and 7 hold.
   Any failure means a ROLLBACK to VersionId `uq53Z5kc...` in the same session. The two M-1 objects stay as write-once
   evidence unless Andrew words a delete.

## 3. ROLLBACK

The COO half stands. Code: re-apply `uq53Z5kc...`. M-1: an un-serve needs a delete of the created object, which is
Andrew's act. The exposure is two names gaining a labelled NEO list they lacked.

## 4. NOT COVERED

- IAM, prefix, route, layer, runtime, memory or timeout changes.
- Any other M-1 write.
- Any served move on `/timeline`, `/print` or `/lead-panel/*`.
- A request-path import of `proxy_officers`.
