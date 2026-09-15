# POSN_AGGFIX -- L5 DECOMPOSITION (round 1)

**archetype:** IMPLEMENT (producer re-point + a new Opal-only key + an edge refusal + the restored Models-mode aggregate UI)
**Owner (L5-L6):** `2.0.0_SA_COO~Z` - **Date:** 2026-09-15 ~18:4xZ - **Directive:** D4 - **Macro:** POSN - **Fabric:** site-z
**PRD:** `org/missions/D4/POSN/POSN_AGGFIX/prd/POSN_AGGFIX_PRD.md` **v0.2** @`cbd85e5cff`, read IN FULL (381 lines). L4-R ADMITTED:
ratified-text half SIGNED `3.0.0_SA_CVO~Z` @`57438abd0e`, brief half SIGNED `4.0.0_SA_CRO~Z` @`b523c21086` (both current at
18:03Z by `prd-signoff.py status`). **Model set:** `org/standards/POSN_AGGREGATE_MODEL_SET.json` v1.0.
**Endpoint outcomes (denominator 8):** FWD-1, FWD-2, FWD-3, FWD-4, FWD-6, FWD-7, FWD-8, FWD-9 (FWD-5 RETIRED, id vacant).

---

## 0. COVERAGE BY SUBTRACTION

```
PRD s.7 SURFACE MANIFEST rows (DENOMINATOR) ...... 17   S1..S17
cells cut, one per row, id AF1-s-<n> = S<n> ...... 17
rows MINUS cells ................................. 0    uncovered {}
cells MINUS rows ................................. 0    invented {}
endpoint outcomes (DENOMINATOR) .................. 8
outcomes with >= 1 cell (s.2 column FWD) ......... 8    FWD-1 s-12 s-14 | FWD-2 s-3 s-4 s-11 s-13 s-15 | FWD-3 s-14
                                                        FWD-4 s-5 s-6 s-9 s-10 | FWD-6 s-1 s-6 s-7 s-10 s-17
                                                        FWD-7 s-2 s-4 s-8 s-9 s-10 s-11 s-12 s-16 | FWD-8 s-2 s-8 s-10 s-16
                                                        FWD-9 s-3 s-13 s-14 s-15
task orders .................................. 7    TO-A1-1 TO-A2-1 TO-A3-1 (slot ~1) | TO-C1-1 (slot ~2) | TO-B1-1 TO-B2-1 TO-B3-1 (slot ~3)
union of <owned_cells> across the 7 orders ....... 17 of 17
```

S4 was added to FWD-2 above because the edge refusal is what makes a remembered or hand-edited aggregate choice unable to fetch
anything; the PRD maps S4 to FWD-7 only. That is an assignment, not a new outcome.

## 1. DESIGN FACTS FIXED AT L5 (each is a measurement or a routine judgment the cells are cut against)

### 1.1 The Opal-only key and its contract (C-OPAL-ONLY-DATA, T3; the PRD left the home to L5)

- **Key:** `s3://opal-data-portal-v2/json/positioning/opal_aggregate.json`, written by the producer beside `OUTPUT_KEY`
  (`lambda_function.py:2529`), with the same put shape (`:2627-2634`: gzip body, `ContentType application/json`,
  `ContentEncoding gzip`, `CacheControl no-cache`).
- **URL:** `/api/general/positioning/opal_aggregate.json`. MEASURED at SITEZ HEAD: `infra/aws/lambda-edge/public-data-router/index.mjs`
  (71 lines) rewrites `/api/general/json/*` -> `/json/*` (:45-48) and `/api/general/*` -> `/json/*` (:63-66) with NO tier branch, so
  BOTH `/api/general/positioning/opal_aggregate.json` and `/api/general/json/positioning/opal_aggregate.json` resolve to the key.
  Both forms are refused by the gate (1.2).
- **Payload (the one contract three chains share):**
  ```
  { "status": "OK" | "UNAVAILABLE",
    "reason": null | "<one line>",
    "generated_at": "<ISO Z>", "data_as_of": "<YYYY-MM-DD>",
    "current_holdings": { "AGG": { "holdings": [ <exactly today's AGG holding shape> ], "total_aum": <float> } },
    "weights": { "UST": w, "ST": w, "INT": w, "LT": w, "ULT": w },
    "weights_source": { "key": "platinum/mdpf/global/aum-metrics.json", "version_id": "<VersionId read>", "period": "<file period>" },
    "members": { "UST": aum, ..., "ULT": aum, "blends": [ { "model_name": ..., "aum": ..., "constituents": {...} } ] },
    "left_out": [ { "model_name": ..., "aum": ... } ],
    "reconciliation": { "five_primary_sum": x, "members_sum": y, "file_total_model_aum": z, "gap": z - y,
                        "gap_explanation_ref": "<path of AF1-s-1's note>" } }
  ```
  `status UNAVAILABLE` carries `current_holdings.AGG.holdings = []` and a `reason`; the page offers NO aggregate entry unless
  `status == "OK"` and the holdings are non-empty (C-NO-SILENT-EMPTY on the page side).
- **Which total the aggregate carries (4.0.0_SA_CRO~Z msg 23200, the non-blocking note, decided here):** `current_holdings.AGG.total_aum`
  is `members_sum`, the denominator the weights are computed over (five primary rows plus the blends folded). It is NOT the five
  books' `aum` summed and NOT the file's `total.model_aum`; both of those ride beside it in `reconciliation`, so a reader of the
  file sees all three with the gap. The page shows no total today (the removal diff `d53049a0` carried none for the served AGG),
  so nothing on screen implies one; FWD-5 is retired.
- **The shared file** `json/positioning/positioning_data.json` loses `current_holdings.AGG` entirely. Its five books keep every
  byte except each book's `aum`, which becomes that model's OWN `by_model` row (C-FIVE-BOOKS-UNCHANGED, PRD v0.2 s.0).

### 1.2 The edge refusal (S4 -> S11; the PRD left the home to L5 "after S4")

- **Home: `infra/aws/lambda-edge/auth-validator-edge/index.mjs`, the viewer-request function.** MEASURED: it verifies the RS256 JWT
  (`verifyWithSlots` :234) on every request of the behaviours it is associated with, holds the claims `firmId` and `userType`
  (header :9-12), and already denies with 401 (not 403: CloudFront's custom error response swallows 403, header :33) after the
  verify (:236-260). Its tier gate covers `/api/scoped/advisor-intelligence/*` only (`tier_policy.mjs:25-26` returns null for
  every other URI). The two other candidates carry no gate for this path: `public-data-router` (above) and `shared-advisor-router`
  (its tier check is for its own scoped prefix).
- **The rule, mirroring the page's own predicate (C-EXISTING-PREDICATE):** MEASURED at portal `edf85ce503`
  `src/contexts/AuthContext.tsx`: `isInternal` = `claims.firmId === 'opal-capital'` (:736-737); `isDev` = `claims.userType === 'Dev'`
  (:750-751); `userType` normalised to `'Dev'` or null (:118-119). So the gate ADMITS a verified payload with
  `firmId === 'opal-capital'` OR `userType === 'Dev'`, and returns 401 for every other verified payload, for BOTH URL forms.
  **It does NOT use `tier === 'internal'`** (the edge's existing ADVI bypass does; the page's comment :756 says "With tier removed,
  internal = firmId opal-capital"). A divergence between the two readings is a row, never a silent choice.
- **Deploy:** portal-auth root. MEASURED: `infra/aws/terraform/portal-auth/lambda-edge.tf:84-127` (`publish = true`,
  `ignore_changes = [source_code_hash]` only -- the qualified_arn pin was DROPPED 2026-09-09, :106-121), the association through
  `cloudfront-distribution.tf:65` `local.auth_validator_edge_arn`; build `bash infra/aws/lambda/ci/build-nodejs-lambda.sh portal-auth
  auth-validator-edge` (`lambda-edge.tf:9`). The post-apply proof is the LIVE distribution's association version (`lambda-edge.tf:42-68`),
  never the re-plan. **Whole-root plan at the cut (this seat, 18:3xZ, `-lock=false`): `Plan: 0 to add, 1 to change, 0 to destroy`,
  the one change `aws_wafv2_web_acl.opal_cloudfront_protection` in place -- PRE-EXISTING DRIFT, not this project's.** The cell's plan is
  `-target`ed to the function and the distribution and the WAF change stays out of it.

### 1.3 The producer (S6-S8, S10)

- **Weights and book `aum`:** MEASURED `lambda_function.py` @SITEZ HEAD (last touch `dbe34de7b0`): `load_aum_data` :1421 reads
  `json/portfolios/aum-metrics.json` :1461 in the Lambda path and returns `{}` on a failed read :1474-1476; `extract_current_holdings`
  :1651 writes each book's `'aum': aum_data.get(model_code, 0)` :1798 and `current_holdings['AGG']` :1811-1814 with `total_aum` =
  `sum(aum_data.values())`; the handler publishes whatever it built :2618-2636. The standard's membership is a MODULE CONSTANT in the
  producer (the Lambda cannot read `org/standards/`), with an exercise criterion proving it equals the standard file.
- **Served today, MEASURED 18:1xZ:** `positioning_data.json` VersionId `aJ7nhwRKko3H_AMRzsNvvwkf1NiO9aou` (11:06:20Z, `data_as_of`
  2026-09-14): books UST 52,360,822.93 / ST 129,227,888.01 / INT 444,315,640.92 / LT 804,605,507.26 / ULT 206,634,320.89, each EQUAL to
  the legacy file's row (5 of 5) and to NONE of the current file's rows (0 of 5); AGG `total_aum` 1,637,144,180.01 = their sum.
- **Yang-pipeline root:** a plan at the cut refused `Backend initialization required` in the shared tree (no `.terraform` there); the
  deploy cell runs `terraform init` in its own worktree first and records it.
- **The one second reader MEASURED at L5:** `data/assets/scripts/gold/build_satellites_characteristics.py` reads the shared file
  (`get_object` :230) and `yang_index` (:391-431) walks EVERY book of `current_holdings` including AGG, first occurrence wins, AGG last
  in insertion order. Removing AGG can move only its `conflicts` list (a ticker whose AGG row disagreed with a model row). AF1-s-2
  censuses; AF1-s-10 exercises the before/after on that function.

### 1.4 The portal (S12-S16)

- **Base:** portal `edf85ce503` (origin/PROD, the tree Andrew checked live). origin/DEV `acdb02e917` is PROD plus ONE CI commit
  (`fix(ci): run project-reference-aware portal typecheck`) and 0 files under `src/pages/Positioning` or `src/api/portal-proxy.ts`
  differ. The round's ONE drain ref is `refs/drains/aggfix-1-portal`, created by this seat at the first portal drain.
  `ledger/PORTAL_REFS.md` is opened with the issuance. NOTHING MOVES A GITLINK; the promote is Andrew's word (C-PORTAL-PROMOTE).
- **The page reads the aggregate as it did before:** the portal fetches the Opal-only file for an internal viewer only and merges its
  `current_holdings.AGG` into the Positioning data object, so `HoldingsTab` keeps reading `positioningData.current_holdings[selectedPortfolio]`.
  An advisor or client never issues the fetch (and the edge refuses it if they do).
- **Fixtures until the key exists:** the served AGG block of VersionId `aJ7nhwRKko3H_AMRzsNvvwkf1NiO9aou` re-keyed into the 1.1 payload.
  AF1-s-16 re-reads on the live key once AF1-s-10 has written it.

## 2. THE RECTANGLE -- 17 cells x {surface, verb, FWD, constraint, depends_on (observed completion), placement, task order, status}

Status vocabulary: `NOT_EVALUATED` (cut, no worker has run it) | `PASS` | `FAIL` | `REFUSED` | `JUDGMENT_RECORDED`. Every cell reads
`NOT_EVALUATED` at the cut. Placement: every cell executes on **site-z** (the ~Z fabric; the push hold stands).

| cell | surface (PRD s.7) | verb | FWD | binds | depends_on | TO / slot | status |
|---|---|---|---|---|---|---|---|
| `AF1-s-1` | S1 the gap in `platinum/mdpf/global/aum-metrics.json` | verify | 6 | C-GAP-EXPLAINED | -- | TO-A1-1 / ~1 | NOT_EVALUATED |
| `AF1-s-2` | S2 writers + readers census | verify | 7, 8 | C-NEVER-WIDEN, C-FIVE-BOOKS-UNCHANGED | -- | TO-A1-1 / ~1 | NOT_EVALUATED |
| `AF1-s-3` | S3 the page predicate | verify | 2, 9 | C-EXISTING-PREDICATE | -- | TO-B1-1 / ~3 | NOT_EVALUATED |
| `AF1-s-4` | S4 viewer-tier enforcement + every URL to the key | verify | 7, 2 | C-OPAL-ONLY-DATA | -- | TO-C1-1 / ~2 | NOT_EVALUATED |
| `AF1-s-5` | S5 deployed producer bytes vs build input | verify | 4 | C-NEVER-WIDEN | -- | TO-A1-1 / ~1 | NOT_EVALUATED |
| `AF1-s-6` | S6 `load_aum_data` re-point + members | port | 4, 6 | C-CURRENT-SOURCE, C-MEMBERS, C-NO-SILENT-EMPTY | s-1, s-5, s-17 | TO-A2-1 / ~1 | NOT_EVALUATED |
| `AF1-s-7` | S7 `calculate_aggregated_holdings` | align | 6 | C-MEMBERS, C-NO-SILENT-EMPTY | s-6 | TO-A2-1 / ~1 | NOT_EVALUATED |
| `AF1-s-8` | S8 the write: shared file vs the Opal-only key | wire | 7, 8 | C-OPAL-ONLY-DATA, C-FIVE-BOOKS-UNCHANGED | s-2, s-7 | TO-A2-1 / ~1 | NOT_EVALUATED |
| `AF1-s-9` | S9 the producer role's grant | verify | 4, 7 | C-NEVER-WIDEN | -- | TO-A1-1 / ~1 | NOT_EVALUATED |
| `AF1-s-10` | S10 the producer deploy | wire | 4, 6, 7, 8 | C-NEVER-WIDEN | s-6, s-7, s-8, s-9 | TO-A3-1 / ~1 | NOT_EVALUATED |
| `AF1-s-11` | S11 the edge refusal, built, deployed, exercised | wire | 7, 2 | C-OPAL-ONLY-DATA, C-NEVER-WIDEN | s-4 | TO-C1-1 / ~2 | NOT_EVALUATED |
| `AF1-s-12` | S12 `getPositioningData` unchanged + the new fetch | wire | 1, 7 | C-OPAL-ONLY-DATA | -- (the 1.1 contract) | TO-B1-1 / ~3 | NOT_EVALUATED |
| `AF1-s-13` | S13 `Positioning.tsx` predicate + mount | wire | 2, 9 | C-EXISTING-PREDICATE, C-DEFAULT-UNLESS-REMEMBERED | s-3, s-12 | TO-B1-1 / ~3 | NOT_EVALUATED |
| `AF1-s-14` | S14 `HoldingsTab.tsx` selector, panels, columns, landing | port | 1, 3, 9 | C-PRIOR-LAYOUT, C-DEFAULT-UNLESS-REMEMBERED | s-13, s-15 | TO-B2-1 / ~3 | NOT_EVALUATED |
| `AF1-s-15` | S15 `bookSet.ts` rationale + remembered choice | align | 2, 9 | C-EXISTING-PREDICATE, C-DEFAULT-UNLESS-REMEMBERED | s-13 | TO-B1-1 / ~3 | NOT_EVALUATED |
| `AF1-s-16` | S16 the five model views before/after as advisor and client | verify | 8, 7 | C-FIVE-BOOKS-UNCHANGED | s-10, s-11, s-14 | TO-B3-1 / ~3 | NOT_EVALUATED |
| `AF1-s-17` | S17 the blend constituents | verify | 6 | C-MEMBERS | -- | TO-A1-1 / ~1 | NOT_EVALUATED |

## 3. THE CELLS (text inlined verbatim into each task order)

### `AF1-s-1` -- the gap between the per-model rows and Opal's own total, explained (S1, C-GAP-EXPLAINED)
Read `data/mdpf/scripts/gold/dim_mdpf_aum_metrics.py` (MEASURED: `total.model_aum` is the fold's own `model_aua` frontier :27-28,
:374, :488, "NOT sum(by_model)" :457; `by_model` is the fold's per-key frontier :501, cohort `model` only :31-32) and the served
`platinum/mdpf/global/aum-metrics.json` (VersionId at read time printed). Reproduce the gap arithmetically from the file
(`total.model_aum - sum(by_model[].aum)`, the 2026-09-14 figure 8,324,465.16) and from the gold fold input the producer reads, and write
ONE explanation note (what the gap is, measured, and whether it is a defect) to the worker's deliverables; the producer's
aggregate file cites it as `reconciliation.gap_explanation_ref`. A defect is a surprise row naming the MDPF producer's owner; this
project edits nothing there.

### `AF1-s-2` -- writers and readers counted (S2, C-NEVER-WIDEN, C-FIVE-BOOKS-UNCHANGED)
Three censuses, each with its denominator printed and a positive control: (a) every WRITER of `json/positioning/positioning_data.json`
and of `current_holdings.AGG` (L5 read: one, the producer :2529/:2627; `build_satellites_characteristics.py:142` is a READER); (b) every
READER of a book's `aum` (`current_holdings.<code>.aum`) and of the shared file outside `portal/src/pages/Positioning`, across the repo
AND the portal at `edf85ce503` (L5 read: 32 portal files at PROD, no book-level `aum` reader, type declarations only at
`portal-proxy.ts:1113-1114`; the per-holding `aum` at `HoldingsTab.tsx:966/:1582` is ETF AUM, a different field); (c) every reader of
`current_holdings.AGG` (L5 read: the satellites `yang_index` walks it). A census uses an instrument different from the L5 read.

### `AF1-s-3` -- what the page's internal check admits (S3, C-EXISTING-PREDICATE)
At the portal base `edf85ce503`: read `isInternal` / `isDev` in `src/contexts/AuthContext.tsx` (L5: :736-737, :750-751, :118-119) and
where `firmId` and `userType` come from (the JWT claims); record which viewers `isDev()` admits beyond Opal staff, if any. The gate in
AF1-s-11 mirrors this reading; a viewer class the two readings treat differently is a BLOCKING row.

### `AF1-s-4` -- where a tier refusal runs, and every URL that reaches the key (S4, C-OPAL-ONLY-DATA)
Read in order `infra/aws/lambda-edge/shared-advisor-router/index.mjs`, `infra/aws/lambda-edge/auth-validator-edge/index.mjs` (the
handler :210 onward whole) and `infra/aws/lambda-edge/public-data-router/index.mjs`; list every CloudFront behaviour whose path pattern and
rewrite can reach `json/positioning/opal_aggregate.json` (`comp-routes behaviors` / `rewrites`, denominator printed) and which of them
associate `auth-validator-edge` at viewer-request; record whether the proxy docstring's "blocks client tier" for
`/api/general/positioning/model.json` (`portal-proxy.ts:1419-1426` @edf85ce503) is true by exercising that URL live with a client token.
A live exposure found elsewhere is a surprise row, not this project's fix.

### `AF1-s-5` -- the running producer against its build input (S5, C-NEVER-WIDEN)
`yang-generate-positioning`'s deployed code (get-function `CodeSha256`, `LastModified`, and the code bundle's `lambda_function.py`
fetched through the function's own code location) diffed against `lambda_function.py` at the commit `lambda-source-map.json` records as
last deployed and against SITEZ HEAD; every commit between the two on that directory listed. That list is what rides AF1-s-10's deploy.

### `AF1-s-6` -- the weights and each book's `aum` come from the current file (S6, C-CURRENT-SOURCE, C-MEMBERS, C-NO-SILENT-EMPTY)
In `lambda_function.py`, the Lambda branch of `load_aum_data` (:1421-1476) reads `platinum/mdpf/global/aum-metrics.json` and
records its VersionId and `period`; the legacy key `json/portfolios/aum-metrics.json` has ZERO occurrences in the file afterwards. A
module constant carries the standard's membership (primary `served_name` -> code; blend `served_name` -> constituents and shares) and is
proved equal to `org/standards/POSN_AGGREGATE_MODEL_SET.json`. The result separates (a) `book_aum`: each primary model's OWN row, no
blend share, for the five books (:1798 keeps `.get(code, 0)`, so a failed read still writes 0 into each book, unchanged); (b)
`member_aum`: each primary row plus each blend's constituent shares; (c) `left_out`: every row that is neither. A failed read, or a
file missing any of the five primary rows, makes the aggregate UNAVAILABLE (never an empty aggregate that reads as current). The
local (non-Lambda) branch :1478-1522 is not the legacy key and is untouched.

### `AF1-s-7` -- the aggregate computed over the members (S7, C-MEMBERS, C-NO-SILENT-EMPTY)
`calculate_aggregated_holdings` (:1525) weights each model by `member_aum[code] / members_sum`; `model_breakdown` keeps today's meaning
(each model's own weight in that ticker); `total_aum` = `members_sum` (1.1). A zero or UNAVAILABLE total returns the UNAVAILABLE
payload rather than `[]` (:1538-1541 today). The exercise re-derives the aggregate weight of three named holdings by hand from the
model books and the member AUM and matches the producer's output to 6 decimals.

### `AF1-s-8` -- the aggregate leaves the shared file for the Opal-only key (S8, C-OPAL-ONLY-DATA, C-FIVE-BOOKS-UNCHANGED)
`extract_current_holdings` stops writing `current_holdings['AGG']` (:1811-1814); the handler writes the 1.1 payload to
`json/positioning/opal_aggregate.json` beside `OUTPUT_KEY` with the same put shape (:2627-2634), on EVERY run (OK or UNAVAILABLE). The
exercise runs the handler at the base commit and at the branch HEAD against the SAME inputs with S3 writes captured (never served) and
proves: the shared file's five books byte-identical in every field except `aum`; each book's `aum` equals its own current `by_model`
row; `current_holdings` carries exactly the five books; every other top-level key byte-identical apart from `generated_at`; the new
key's payload matches 1.1 with `status OK`; and the failure arm (the current file unreadable) yields `status UNAVAILABLE`, books `aum` 0.

### `AF1-s-9` -- the producer role already holds what the re-point and the new key need (S9, C-NEVER-WIDEN)
`yang-pipeline-lambda-role`: `s3:GetObject` on `arn:aws:s3:::opal-data-portal-v2/platinum/mdpf/global/aum-metrics.json` and
`s3:PutObject` on `arn:aws:s3:::opal-data-portal-v2/json/positioning/opal_aggregate.json` both `allowed` by an IAM policy simulation
(a different instrument from the PRD's `comp-iam` read of `iam.tf:34-46`), with a negative control that is `implicitDeny`.

### `AF1-s-10` -- the producer deployed through its module, and the served result read (S10, C-NEVER-WIDEN)
Under `ledger/NEVER_WIDEN_ROUND1_PRODUCER_COO_HALF.md` and `..._CTO_HALF.md` (both at HEAD before any leg moves): the deploy ledger
entry opened first; `build-and-upload.sh yang-pipeline yang-generate-positioning`; `terraform init` then a plan `-target`ed to
`module.generate_positioning` reading exactly one function updated in place; `safe-apply`; a 0-diff re-plan; deployed `CodeSha256`
== the uploaded artifact's; the generator invoked DIRECTLY once with the event the state machine passed it on its last execution
(never a hand-written event, never the state machine) and the pipeline's own invalidation lambda with its recorded event; then the
served reads: the prior and new VersionIds of the shared file printed; the new shared file's five books byte-identical to the prior
version in every field except `aum`; each book's `aum` == its current row; no AGG in the shared file; the new key present, `status OK`,
weights == members / members_sum; the satellites `yang_index` run on the prior and new shared file yields identical `out` and `extra`
maps and a `conflicts` list whose difference is printed; the recorder commit verified by git; the ledger entry closed. **The key's
exposure before AF1-s-11's gate is live equals today's** (every signed-in viewer receives the AGG block in the shared file today),
so no widening occurs in that window; the halves name it.

### `AF1-s-11` -- the edge refuses the aggregate to anyone outside Opal, deployed and exercised live (S11, C-OPAL-ONLY-DATA)
In `infra/aws/lambda-edge/auth-validator-edge/`: ONE new pure module `aggregate_gate.mjs` exporting the URI match (both forms, 1.2) and
the admit predicate (`firmId === 'opal-capital' || userType === 'Dev'`), called from `index.mjs` right after the JWT verify, returning
`unauthorized(...)` with one structured log line `aggregate_denied` (no metric filter, no alarm: the moratorium). A unit harness drives
`handler` with synthetic viewer-request events whose JWT verify is replaced in-process: four viewer classes (Opal staff, Dev, advisor,
client) x the two aggregate URLs x a control URL (`/api/general/positioning/positioning_data.json`). Deployed under
`ledger/NEVER_WIDEN_ROUND1_EDGE_GATE_COO_HALF.md` and `..._CTO_HALF.md`: ledger entry; build; plan `-target`ed to the function and the
distribution; `safe-apply`; re-plan; the LIVE distribution association version equals the newly published version on every behaviour
that associates the function (N of N printed); live arms with short-lived tokens for the four classes on both URLs and the control.

### `AF1-s-12` -- the fetch (S12, C-OPAL-ONLY-DATA)
`portal/src/api/portal-proxy.ts`: `getPositioningData` (:1177) byte-unchanged; ONE new exported fetch for
`/api/general/positioning/opal_aggregate.json` returning the 1.1 payload typed, through the same `apiRequest` helper.

### `AF1-s-13` -- the page hands the predicate down and fetches only for Opal (S13, C-EXISTING-PREDICATE, C-DEFAULT-UNLESS-REMEMBERED)
`portal/src/pages/Positioning/Positioning.tsx`: `internal` (:267) is passed to the `HoldingsTab` mount (:642); the aggregate fetch runs
only when `internal` is true and only in Models mode; on `status OK` with holdings its `current_holdings.AGG` is merged into the
Positioning data object the tab reads; otherwise nothing is merged. Advisor and client code paths issue no request for the key. How the
aggregate behaves while an internal viewer has a partner firm selected is read from the page and recorded (C-ONE-BOOK).

### `AF1-s-14` -- the selector entry, both panels, the per-model columns and the landing (S14, C-PRIOR-LAYOUT, C-DEFAULT-UNLESS-REMEMBERED)
`portal/src/pages/Positioning/tabs/HoldingsTab.tsx`: for an internal viewer with the merged block present, `Aggregate` is the FIRST book
in the Models-mode selector (the removed `AGG_PORTFOLIO` shape, `d53049a0`); Portfolio Composition (:1105) and Holdings Breakdown (:1197)
render `current_holdings.AGG` through the existing path; the Model Breakdown group (UST, ST, INT, LT, ULT from `model_breakdown`) returns
in the position and order the removal took out, labelled as all of Opal, re-authored in today's light-canvas tokens (no `text-white`,
`text-orange-300`, `bg-white/10`, `bg-orange-500/5`); the first-render landing (:841) lands an internal viewer with no remembered
choice on the aggregate, and a remembered choice wins. Advisor and client see no change.

### `AF1-s-15` -- the book set and the remembered choice (S15, C-EXISTING-PREDICATE, C-DEFAULT-UNLESS-REMEMBERED)
`portal/src/pages/Positioning/shared/bookSet.ts`: `capabilitiesFor(mode)` (:299) stays mode-only and gains NO aggregate capability; the
no-aggregate rationale (:238-257, :39-46) is rewritten to cite this project and the viewer-scoped entry; a remembered or hand-edited
`'AGG'` is honoured only when the viewer's own book set contains it and otherwise falls back to the ordinary default, mirroring the
existing `visibleModes` check on remembered mode.

### `AF1-s-16` -- the five model views unchanged, and the aggregate on live bytes (S16, C-FIVE-BOOKS-UNCHANGED)
On the drain ref carrying AF1-s-12..s-15: the page rendered as an advisor and as a client, Models mode, each of the five books, once
with the shared file's PRIOR served version and once with the version AF1-s-10 wrote (VersionIds from AF1-s-10's proof), holdings and
weights text identical per book (a positive control: a one-weight mutation of the fixture differs); and as an Opal user with the LIVE
`opal_aggregate.json` bytes, the aggregate present with both panels and the five breakdown columns.

### `AF1-s-17` -- the blend constituents verified (S17, C-MEMBERS)
Find a DEFINITION of `opal_blend_5050_int_ltc` and `opal_blend_5050_st_int` (a model definition, target-allocation or crosswalk
artifact that states constituents, not a name), census with its denominator, and record CONFIRMED / CONTRADICTED / NO-DEFINITION-FOUND
per blend against the standard. CONTRADICTED is a BLOCKING row (the standard and the PRD bump); NO-DEFINITION-FOUND is recorded with the
census and the standard's `inferred` claim stands for the L9 judgment.

## 4. DEPENDENCY EDGES, CHAINS AND FAN-OUT (keyed to OBSERVED completion: a proof instance VALID and drained at HEAD)

```
TO-A1-1 (s-1 s-2 s-5 s-9 s-17) --> TO-A2-1 (s-6 s-7 s-8) --> TO-A3-1 (s-10) --+
TO-C1-1 (s-4 s-11) -----------------------------------------------------------+--> TO-B3-1 (s-16)
TO-B1-1 (s-3 s-12 s-13 s-15) --> TO-B2-1 (s-14) ------------------------------+
```
Three independent roots (A1, C1, B1); the three chains join only at B3. Maximal paths: 3. Workers: slot `~1` holds A1->A2->A3, slot
`~2` holds C1, slot `~3` holds B1->B2->B3 (B3 handed only after A3 and C1 drain). **fanout: 3 of 3 chains, cap 8, reason: one worker per
independent root; B3 joins the three and rides slot ~3's queue after its two cross-chain dependencies drain.**

## 5. THE BATTERY

| lens | disposition | denominator / blindness |
|---|---|---|
| `comp-schedule --drift` | RUN 18:3xZ | 7 armed gates (G-3 inf never-widen sentinel, G-7 BD calendar guard among them), 0 POSN; 6 open deploy-ledger entries, none POSN; 12 standing NEVER clauses -- those binding here: Terraform only (`safe-apply`), never-widen halves, no `update-function-code`, no monitor/alarm, no push. BLIND: C4 scope guards (21) and C5 project `blocking` prose (334) are a reading list, not gates. |
| `comp-iam` | RUN (producer) / DECLARED-BLIND (edge) | `comp-iam service yang-generate-positioning` (PRD s.9, cited not re-run): role `yang-pipeline-lambda-role`, 7 operations, 1 GRANTED, 6 UNRESOLVABLE-RESOURCE; AF1-s-9 answers the two resources this project needs by simulation. `comp-iam service auth-validator-edge` returned the service listing (no record for the edge function): BLIND on the edge role; AF1-s-11 changes no grant and its S3 read of the ownership map is untouched. |
| `comp-adversary compose` | RUN on this file at the cut | recorded in s.7 below |
| terraform plan (root preflight, memory rule) | RUN 18:3xZ | portal-auth: 0 add / 1 change (WAF drift) / 0 destroy; yang-pipeline: `Backend initialization required` in the shared tree -- the worker inits in its worktree |

## 6. FOUR-POSTULATE RECORD (Rule 24)

(i) **MECE over the declared domain** = the PRD s.7 manifest rows (denominator 17): 17 cells, one per row, subtraction 0 both ways (s.0).
The outcome domain (8) is covered by the FWD column, subtraction 0. (ii) **SAME GRAIN:** one cell = one manifest row = one surface;
the task orders group cells by chain and never split a cell. (iii) **INTENT COHERENCE:** "Opal staff read one current Opal-wide
aggregate that nobody outside Opal can see or fetch, and nothing else a viewer sees moves." (iv) **STATE COHERENCE -- what the cells do
NOT move:** the five books' holdings and weights and every other field of the shared file but `aum`; the MDPF gold producer and its
publisher; the legacy `json/portfolios/aum-metrics.json` object; every Lambda but `yang-generate-positioning` and `auth-validator-edge`;
the WAF drift; the Attribution and Factor Tilts pages; the Satellites and ETFs modes; the portal gitlink, DEV and PROD.

## 7. comp-adversary (the validator-context declaration of this file)

`comp-adversary compose org/missions/D4/POSN/POSN_AGGFIX/decompositions/POSN_AGGFIX_DECOMP.md` (this seat, ~18:5xZ): complement
sources 5 run / 0 deferred / 4 declared-excluded (toolgraph independence, comp-axes unexamined axes, comp-blast neighbourhood expansion,
comp-pulse); 12 digests, 28,224 bytes; every pin READ-VINTAGE. A declaration is never a clean bill.

**NOT covered by this seat, stated so each worker measures it first:**
1. The live tier arms of AF1-s-11 (and AF1-s-4's model-route arm) need short-lived tokens signed by the active key; the issuer has NOT
   read `opal/auth/jwt-private-key` (`infra/aws/terraform/portal-auth/secrets.tf:14-15`) nor exercised minting. If the key is not
   readable through `comp-secrets`, those arms are REFUSED with a row, never replaced by another route.
2. Replacing the JWT verify in-process for AF1-s-11's unit harness is unexercised: `index.mjs` imports `jsonwebtoken` and
   `../../lambda/lib/authkeys/jwtPublicKeys.mjs` (:62-65). The harness mechanism is the worker's to measure and state.
3. The generator's recorded event (the state machine's last execution of `GeneratePositioning`) is unread by the issuer.
4. The yang-pipeline root has not been initialised or planned on this device this session.
5. No blend definition search has run (AF1-s-17 is the first).
6. The advisor and client claim sets for the page renders are not constructed by the issuer; the portal worker builds them from
   `AuthContext.tsx` and records them.
7. The satellites characteristics artifact's served bytes are not re-read by the issuer; AF1-s-10 exercises `yang_index` only.
