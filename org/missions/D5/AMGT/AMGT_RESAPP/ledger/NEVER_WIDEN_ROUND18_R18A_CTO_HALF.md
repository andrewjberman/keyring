# AMGT_RESAPP round 18 -- never-widen pair, R18-A -- the CTO half

**Author:** `1.0.0_SA_CTO~Z`. **Counterpart:** `ledger/NEVER_WIDEN_ROUND18_R18A_COO_HALF.md` (COO, signed at issuance
`c13e1b93df`). **Order:** `task-orders/AMGT_RESAPP.TO-AMGT-rk-74.served-crosswalk-vintage-field.md`.

## `AMGT-rk-74` -- the served crosswalk vintage field

### What this half signs

The act as the COO half names it: one redeploy of `opal-amgt-scoped-api`, with one new artifact version and one
targeted apply whose plan reads `0 to add, 1 to change, 0 to destroy`. The blast radius is B1-B4 and nothing else.
The carry-along is exactly two files: this cell's `scoped_amgt.py` edit, and **`AMGT-rk-68`'s `crosswalk.py` at
`0164b134ac`**, which rk-68's own order bound this redeploy to name. This half adopts the COO half's BLAST RADIUS,
WRITER CENSUS, EXPECTED OUTCOME (branches A/B/C), PER-KEY ROLLBACK and NOT COVERED sections as written. It does not
restate them. Where this half differs, it says so below.

### Independent measurements (this seat, read-only, 2026-09-21 ~17:0xZ -- different instruments from the COO's)

| anchor | read | agrees with the COO half? |
|---|---|---|
| live `CodeSha256` of `opal-amgt-scoped-api` | `QwET8XtX3Z53ylyStMoiX/yaC0Slfrc959+rUGlHGME=`, `LastModified` 2026-09-19T16:22:28Z (the `AMGT-rk-37` redeploy; no redeploy since) | yes |
| keys under `s3://opal-data-harvest/crosswalk/v1/` | 2: `2026-09-15.json`, `2026-09-19.json`; both match `^crosswalk/v1/\d{4}-\d{2}-\d{2}\.json$` | yes, so Branch A is the expected state |
| drift in the two named files since the served source `55e3a56854` | `git log 55e3a56854..HEAD` over both: ONE commit, `0164b134ac` (rk-68, `crosswalk.py`); `scoped_amgt.py` has 0 commits, so this cell's edit is the only change there | yes |

This seat did NOT re-measure the whole 58-path packaged population. The COO half's subtraction is the only reading
of it, and the order's AC3 re-reads it at spawn. That is the instrument this half relies on for "no third file".

### Where this half adds to the COO half

1. **Branch B is the one that matters, and the order already stops on it.** rk-68 turns a non-dated key under
   `crosswalk/v1/` from "ignored by sort" into "every crosswalk-resolved identity goes UNRESOLVED". That is a
   whole-page effect from one stray key. Today's measurement says Branch A. The order's AC4 re-reads before the build
   and STOPs on any non-matching key, and AC6 triggers the rollback if one appears after. This half signs on that
   stop-and-rollback; it does not sign an act that would ship into Branch B.
2. **What the field exposes.** `crosswalk_source` puts an `s3://opal-data-harvest/...` URI into the served JSON.
   Accepted: a bucket and key name is not a secret, the routes are authenticated, and the page is internal (Dev +
   admin today; managers pending Andrew's card). If the page is ever exposed beyond internal staff, this field is
   re-reviewed then.
3. **Timing.** This redeploy lands before the AMGT portal promote Andrew is carded on, and before the manager review.
   Accepted: the change is additive (one key), and the page renders nothing new from it until a portal change reads
   it (NOT COVERED: no portal change in this act).

### Rollback -- confirmed, with the anchors this seat re-read

As the COO half's PER-KEY ROLLBACK: restore the artifact key from its pre-act **VersionId** (the worker's AC4 value)
by `copy-object`, re-run the same targeted `safe-apply`, and confirm `get-function-configuration` prints the pre-act
**CodeSha256** (`QwET8XtX...` at this seat's read) and the 13-route census equals the AC4 baseline. No version is
deleted and no VersionId is handed to Terraform. Triggers are as in the COO half.

**Signature (CTO):** signed `1.0.0_SA_CTO~Z`, 2026-09-21 ~17:0xZ. The pair for `AMGT-rk-74` is complete with this
half.
