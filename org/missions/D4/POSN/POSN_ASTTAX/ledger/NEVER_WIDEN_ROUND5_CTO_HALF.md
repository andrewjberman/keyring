# NEVER-WIDEN SIGN-OFF -- CTO HALF -- POSN_ASTTAX round 5: B1, B2, R1 (B4 non-application; B5 separate)

**Signer:** `1.0.0_SA_CTO~Z` (L2/L4 owner, gate over the POSN served planes). **Counterpart:** `2.0.0_SA_COO~Z`'s COO half,
`ledger/NEVER_WIDEN_ROUND5_COO_HALF.md`, whose write set is stated in msg 22883 and is the set this half covers.
**Basis:** PRD v0.7 @`99cc431075` (ADMITTED), `ROUND_ANALYSIS.round4` @`221ed89911`, breakdown v0.5 @`0949f2d53d`.
**Rule:** CLAUDE.md NEVER#1 -- the half names the act's BLAST RADIUS and rollback per key, counts the writers of each named
property and prints N, and covers BOTH branches of every expected outcome. **2026-09-14 ~17:5xZ.**

> **SIGNED, for the acts below exactly as bounded. Anything a plan, a diff or a served read shows outside these bounds is
> NOT SIGNED: the cell STOPs before the deploy/write and re-arms a row with the observation verbatim.**

---

## B1 -- deploy the positioning generator at HEAD + the labelled-zero benchmark code

**What the act MAY touch, key by key:**

| key (bucket `opal-data-portal-v2`) | writer | change | rollback |
|---|---|---|---|
| `json/positioning/positioning_data.json` | `yang-generate-positioning` (`put_object` at `lambda_function.py:2459` and `:2581`) | the deployed code moves from the 2026-08-18 build (last source commit before `LastModified 2026-08-18T18:34:43Z`: `69b867c4eb`) to HEAD. **Four source commits ride it:** `7f247caae0` (S6 harden: an unexpected class no longer raises), `c34eab85dc` (S1: an unrecognised security is not silently equity), `07c046fa63` (T1: five classes carried through), and `b0e1f33471` (ETFS_INGEST TO-9-DS: ETFClassifier display-name beautification -- NOT a POSN commit, and it ships with this deploy). Plus B1's own labelled-zero benchmark rows for Structured / Commodities / Alternatives | redeploy the `69b867c4eb` build through Terraform (`safe-apply`) and re-run the generator; the prior S3 object version where the bucket versions (not measured by this seat) |
| `json/positioning/allocation_summary.json` | `yang-generate-allocation-summary` (`OUTPUT_KEY :34`, `put_object :368`) | B1's new code: `BENCHMARK_ALLOCATIONS` (`:46`, read `:262-267`) carries an explicit zero, labelled "no benchmark", for the three new classes. Live bytes `LastModified 2026-08-04`; last source commit `89a3cca5ed` | redeploy the `89a3cca5ed` build and re-run |
| anything else | -- | **NOT SIGNED** | -- |

**Writers of the named property -- "holding-class value on the served positioning plane": N = 4, printed.**
`yang-generate-positioning` (positioning_data.json), `yang-generate-allocation-summary` (allocation_summary.json, reads
`holdings_attribution_data.json :154`), `yang-generate-holdings-attribution` (holdings_attribution_data.json; untouched by B1,
re-reads the registry on its own fire), and `data/etfs/scripts/gold/etf_positioning_publisher.py` (`platinum/etfs/positioning_data.json`,
out of POSN write scope, disclosed per `Z-C-S55`). Census: `2.0.0_SA_COO~Z` by file:line (22883); re-read by this seat with a
different instrument (`comp-find` literal-key census over the corpus + `comp-read --enumerate` of each lambda's `put_object`
sites). The two agree. `Z-S43`'s floor of three is exceeded by one.

**Expected outcome, read from the producers' rules -- BOTH branches, BEFORE any retag:**
- **Branch A -- the served class vocabulary today is unchanged by the code** (the stored values are `equity`, `fixed_income`,
  `hedge`, `cash`; S6/T1 only change what happens to a value outside that set, and S1 only changes a security the registry does
  not recognise). Expected served delta on `positioning_data.json`: display names per `b0e1f33471`, any holding the registry does
  not recognise moving from Equity to its unknown label, and the benchmark rows gaining labelled zeros. **The cell prints the
  DELTA before `safe-apply`**: the generator at `69b867c4eb` and at HEAD run locally against the SAME live input, diffed per key
  and per book, with the count of changed rows by change class.
- **Branch B -- the DELTA shows any change outside those three classes** (a weight, a subtotal, a holding appearing or vanishing,
  a class other than via the unknown label): **NOT COVERED.** STOP, no deploy, row re-armed with the diff verbatim.

## B2 -- re-deploy `cot-satellites-registry-producer` with the new `holdings.json` output

| key (bucket `opal-data-cot`) | writer | change | rollback |
|---|---|---|---|
| `platinum/satellites/registry.json` | ONE: `data/assets/scripts/gold/build_satellites_registry.py` via the `cot-satellites-registry-producer` trigger. Independent read: the only role holding a PutObject grant PINNED to this key is `cot-satellites-registry-producer-role` (`infra/aws/terraform/cot-pipeline/satellites-registry-producer.tf`, Sid `WriteSatellitesRegistry`); roles with bucket-wide grants on `opal-data-cot` were not censused by this seat | the producer is re-deployed; **registry.json is expected BYTE-IDENTICAL in content** for the same input (B2 adds an output, it does not change this one) | redeploy the prior producer artifact and re-run |
| `platinum/satellites/holdings.json` | NEW key, zero writers today | one total weight per ticker per satellite from Black Diamond, summed across sleeves, with per-sleeve breakdown and both class labels (`C-SATELLITE-SOURCE`) | **no reader until F3 + B5 are deployed**, so the key is inert if B2 is rolled back; it is left in place, not deleted (an S3 delete is Andrew's) |
| IAM in `satellites-registry-producer.tf` | Terraform | a second PutObject key pinned to `holdings.json`; a DynamoDB read on `etf-classifications`. No bucket-wide grant, no list, no cross-firm read | revert the `.tf` and re-apply |
| anything else | -- | **NOT SIGNED** | -- |

**Expected outcome, both branches:** A -- the re-run registry.json's content equals the pre-deploy registry.json for the same
partition (compared ignoring any generated-at timestamp), and holdings.json appears. B -- registry.json content differs in any
member, book or constituent: **NOT COVERED**, STOP and row.

## B4 -- the additional characteristics lambda: NEVER#1 NON-APPLICATION, stated

A new function writing ONE new pinned key (`platinum/satellites/characteristics.json`), zero writers and zero readers today
until F3 + B5. No existing served output moves, which is NEVER#1's stated non-application ("an act whose write set is a
literal key list the actor controls"). Still binding: its own change-management ledger entry, `safe-apply`, `comp-iam gaps`,
and the cross-firm enumeration read at the cut. Agreed with `2.0.0_SA_COO~Z` (22883).

## R1 -- THE RETAG: the served-output move this project exists for

**What the act MAY touch:** the DynamoDB table `etf-classifications` -- exactly these 12 rows, the fields `asset_class` and
`sub_asset_class`, plus `management_style` on VNQ -- and the same 12 entries in `ETF_CLASSIFICATIONS`. **Nothing else. BIPC is
NOT touched.**

**Prior values (the rollback), point-read by this seat at 2026-09-14T17:53:44Z** (`dynamodb batch-get-item`, 13 of 13 keys
returned, `UnprocessedKeys {}`, negative control `ZZZ_NO_SUCH_TICKER` not returned -- a different instrument from the scans
`2.0.0_SA_COO~Z` and U4 used):

| ticker | asset_class NOW -> TARGET | sub_asset_class NOW -> TARGET | management_style |
|---|---|---|---|
| DBC | hedge -> Commodities | Commodities -> (unchanged) | passive |
| GLD | hedge -> Commodities | Gold -> Metals | passive |
| GSG | hedge -> Commodities | Commodities -> (unchanged) | passive |
| IAU | hedge -> Commodities | Gold -> Metals | passive |
| SLV | hedge -> Commodities | Silver -> Metals | passive |
| USO | hedge -> Commodities | Oil -> (unchanged) | passive |
| PDBC | equity -> Commodities | Commodities -> (unchanged) | active |
| VXX | equity -> Structured | Volatility -> Hedge | passive |
| VIXY | hedge -> Structured | Volatility -> Hedge | passive |
| UVXY | equity -> Structured | Volatility -> Hedge | passive |
| QBER | fixed_income -> Structured | Volatility -> Hedge | active |
| VNQ | equity -> Alternatives | US Large Cap -> Real Estate | **unknown -> set to its factual value BEFORE the class write** (`C-RETAG-SAFETY` step 1) |

Stored-value encoding of the targets (e.g. `commodities` vs `Commodities`) follows whatever the served table's vocabulary
extension in R1 establishes; the TARGET column is the ratified label, and R1's bar compares per ticker per level.

**Writers that re-read the retagged property on their next scheduled fires, N printed = 6:** the four B1 writers above, the B2
producer (`holdings.json` labels), and B4 (through `holdings.json`). **Accepted, not a defect:** Attribution stays two-class, so a
retagged ticker Yang's models hold (VXX) drops out of its per-class groups while its weight stays in its totals (Andrew ~17:3xZ).

**Expected outcome, both branches:**
- **A -- preconditions met** (B1, B2, B4, B5 deployed; B3 landed; F1-F3 built): on the local build over all 9 satellites and the
  Models and ETFs modes, every one of the 12 serves its TARGET at both levels, its label-grouped weight equals its pre-retag
  weight, served rows equal rendered rows, and class subtotals equal the total. The ETF publisher's candidate-member count is
  re-measured and printed.
- **B -- any precondition unmet, or any bar clause fails after the write:** before the write, **NOT COVERED** -- no write. After
  the write, the prior values above are written back to BOTH stores the same turn, and the row is filed with the failing clause.

### R1 AMENDMENT 2026-09-14 ~20:0xZ -- the served refresh after the retag is DRIVEN, not waited on

**Why:** `TO-V8-1` as cut leaves the served refresh to the producers' next scheduled fires (07:00Z / 07:20Z / the Yang
pipeline ~11:0xZ) and warns its render may show pre-retag labels "until then". Rule 27: no forward outcome is a wait. The
mechanism is driven on demand, and the scheduled fire stays as the organic confirmation leg.

**NEVER#1 names the new state this creates:** a scheduled producer run off its own clock is a new reachable state, and a
sign-off must cover it. **This half now covers it:**

- **The act:** immediately after R1's writes succeed in BOTH stores, the cell invokes, once each and in dependency order,
  the writers of the retagged property that feed the Positioning page:
  1. `yang-generate-positioning`
  2. `yang-generate-holdings-attribution`
  3. `yang-generate-allocation-summary` (it reads holdings_attribution_data.json)
  4. `cot-satellites-registry-producer` (registry.json content-identical, holdings.json relabelled)
  5. `cot-satellites-characteristics-producer`
- **The keys:** exactly the served keys listed above for B1 and B2, plus `platinum/satellites/characteristics.json`.
  Nothing else. The ETF publisher (`etf_positioning_publisher.py`) is NOT invoked; it stays disclosed, on its own schedule.
- **Expected outcome, both branches.**
  - **A:** each invocation returns success, and each served key's `generated`/`as_of` stamp moves past the retag
    time. The per-ticker per-level target comparison then reads the refreshed artifacts. The next scheduled fire is
    recorded as the organic leg in the ledger, not waited on.
  - **B:** any invocation fails, or a key's content differs beyond the retagged labels and the weights they
    regroup. STOP. Write the 12 prior values back to both stores, re-invoke the same producers so the served keys
    return to pre-retag labels, then file the row.
- **Rollback per key:** the prior values table above, re-written, then the same invocations. Where the bucket versions a
  key, the prior object version.

## WHAT THIS HALF DOES NOT COVER

- B5 (the edge router leaf allowlist): its own pair of halves once it exists as a cell and Andrew has approved it.
- Any portal promote, DEV/PROD push or gitlink move (Andrew's separate word).
- `bd-securities`, the Attribution page, Philosophy/CMA, AdvisorIntelligence (out by Andrew's word).
- The Bloomberg pull edit (`ac3e03a317`, its own ledger `posn-bbg-etf-pull-gld-vxx`).

Push state: LOCAL (this seat never pushes; site-Z pushes are held by `0.0.0_AB_MSTR~Z` on Andrew's word).
