# ETFS_RIVALS -- ROUND 4 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-01 ~23:0xZ

**Input:**
- the CVO slug, msg 28074, `REMEDIATION_v4.Z.md` @7256e90b67 (3 new; 14 open across v1-v4, all owned by this seat);
- the review `org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R4_REVIEW_20261001.md`;
- the drain-end packet @550af8d320 (6 of 6 terminal).

**Already ruled for round 5, and carried here as inputs:**
- the hop-9 rulings a, b and d (@4baf852611);
- PRD v0.8 (@fe946c1366, CVO-signed): IDVZ and PFOE on the Bloomberg leg, and the ACWI and IWM controls with the style-read
  preview first.

## 1. WHAT THE ROUND DELIVERED

- **The round-4 live join landed:**
  - d-5 and addendum 1;
  - five Lambdas in place, at 21:55Z;
  - the page for 2026-10-01 serves 13 funds, 12 updated. GQGU is not-updated on freshness only.
- **The GQGU issuer route serves 305 archived days.**
- **G2 now attributes each issuer capture to its own fund** (W4-S13).
- **Each fund pairs with its own previous report** (W1-S27): TSEL has 101 windows and WCMG 42, with 0 mismatched.
- **The package passes:** 306 tests, 2 skipped, 0 failed.
- **Every round-3 product item is closed**, and the CVO read each fix at HEAD.

**Round 4 is CLOSED.**

## 2. FWD GRADES

- **FWD-1 (the two-group live read):** NOT YET. The signed-in /rivalfunds read is Andrew's.
- **FWD-2/3/5:** served for 13 funds. GQGU 2026-09-29 and 09-30 are a permanent gap, read ABSENT with its cause.
- **FWD-9:** see ruling 9.
- **FWD-10:** waits on the ACWI and IWM controls (v0.8).
- **FWD-13..20:** PROPOSED, awaiting Andrew.

## 3. RULINGS ON THE 14 OPEN ITEMS

### Product -- round-5 cells

| # | item | ruling |
|---|---|---|
| 1 | **W4-S9 (ARMED)**: G1 times out above about 45 dates | **Code bound, FIRST in round 5.** A marker-driven G1 run is windowed by date and continues across invocations from a cursor, so any batch size completes. Proof: one batch above 45 dates completes with no timeout. The disarm stays with COO~RV: no bulk batch runs until the bound ships. **It gates every backfill v0.8 asks for** (IDVZ and PFOE to launch, ACWI and IWM history). |
| 2 | **W5-S21**: the collector's dedup is quadratic | **Round 5, with ruling 1.** The sidecar index is memoised in the product sink, or the dedup is keyed on the sha. It shares a cause with W4-S9: both bite on the first bulk run. |
| 3 | **The per-fund issuer floor** (no carrier row) | **Round 5.** `resolved_floor()` gains per-fund entries under `issuer`, so BASG's floor is set from BASG's own resolution. COO~RV files the carrier row this turn. |
| 4 | **W3-S15**: G4 is an as-of pull written under an old date | **Round 5.** The G4 producer refuses or labels a pull whose run date is not its partition date, and uses a historical request for past dates. FWD-14's daily return series needs this anyway. |
| 5 | **W3-S11**: dividend currency | **Round 6.** DVD_CRNCY is added to the enrichment request, inside the rivalfunds Bloomberg pull Andrew already worded. G5 drops the suffix heuristic. |
| 6 | **W3-S12**: the child identity for a spinoff, rights issue or warrant | **Round 6.** First a probe of whether a Bloomberg field names the child. Failing that, a maintained map. Until then the child line keeps its label as an entry. |
| 7 | **The page headline** reads `not-updated` when 1 of 13 lags | **Round 5, a small cell.** The top-level word means **"page published"**. The headline then states the count, e.g. "12 of 13 funds current", and names each lagging fund with its reason. Failed figures still never publish (FWD-9). |

### Fabric and instrument -- ruled here, no ETFS_RIVALS cell

| # | item | ruling |
|---|---|---|
| 8 | **W4-S7**: the device identity is AdministratorAccess | **Halves name the STAGE ROLES as the subject of a negative control.** An identity-level control on the admin device identity is vacuous and is no longer written. A scoped device role is an IAM change for `/cloud-ops` to propose, outside this project. |
| 9 | **W4-S14**: a check's runtime exceeds the runner's bound | **A task order states its own time bound for any check that reads a whole window** (timeout 600). Otherwise the check samples or reads in parallel. rc 124 is never graded as FAIL. |
| 10 | **W5-S12**: deploy-only refs | **Standing rule:** the issuer commits and deploys a deploy-only ref at its own seat. A worker never holds one. |
| 11 | **W5-S15**: untagged rollback refs | **Tag both refs now** (`288fa78c93`, `093fc247c6`; COO~RV, local tags), and tag the deployed commit in every deploy-only release. |
| 12 | **S2**: no mutual exclusion on gateway deploys | **Until the gateway owner builds a lease, the open change-management entry is the lock.** Before a gateway deploy, read every live worktree's `.open_deploys/` for an open gateway entry (the NEVER-2 union read), and diff the served routes before and after. A missing route STOPs. |
| 13 | **W5-S3** (gateway not reproducible from a fresh tree), **W5-S7** (naming-gate carve-out), **W5-S14** (jq mojibake in the manifest), **S7** (the seating-lint resolver truncates at the first underscore) | **Routed to their owners via `0.0.0_AB_MSTR~Z`'s register.** These are outside this project's write surface. Interim: W5-S14 edits only the one service entry; S7 must be fixed before the seating limb enforces. |

### Tomorrow's first organic morning -- read as three legs, in order

COO~RV reads and records, in this order:
1. the 07:00 ET issuer fetch markers, which test W4-S13 and W4-S10;
2. the 08:03 ET vehicle log's two exit lines (enrichment on schedule for the first time);
3. the 09:00 ET sweep's `waiting` and `unresolved`.

Only then is the page read. If the page reads wrong, the first failing leg is the suspect. This is the CVO's unasked question,
adopted.

## 4. THE ENRICHMENT LIST -- round 5, `2.0.0_SA_COO~RV`, ONE issuance (fan-out cap 8)

1. The W4-S9 code bound (G1 windowed and continued), proved above 45 dates.
2. The W5-S21 dedup memo in the product sink.
3. Hop-9 (a): an ID-CHANGE needs an identifier relation, with the CUSIP zero-pad at silver.
4. Hop-9 (b): implausible flow-factor windows are REFUSED, with the floors in `guardrails_config`, and the replay runs the
   page guardrails.
5. Hop-9 (d): `key_resolution` becomes its own G5 column.
6. The per-fund issuer floor (ruling 3), together with the page headline (ruling 7).
7. The v0.8 Bloomberg leg, daily from now. IDVZ, PFOE, ACWI and IWM join the queue after the request-cost measurement, and
   the ACWI and IWM G9 preview runs first.
8. The W3-S15 G4 as-of guard, with a historical request for past dates.

**Round 6:**
- the backfills to launch (IDVZ, PFOE, ACWI, IWM), which need item 1;
- the G5/G6 replay under a pair;
- W3-S11 and W3-S12;
- Addendum B, once Andrew confirms it.

## 5. ACTS ONLY ANDREW CAN DO (cited)

1. **The FWD-1 signed-in read of /rivalfunds** (his login; PRD FWD-1).
2. **Confirm Addendum B, FWD-13..20** (the ENDPOINT is his to confirm, as FWD-1..12 were). The two answers owed are the
   FWD-14 measure and the meaning of "concentration".
3. **Web search for the AI, if wanted** (vendor per-use word).
