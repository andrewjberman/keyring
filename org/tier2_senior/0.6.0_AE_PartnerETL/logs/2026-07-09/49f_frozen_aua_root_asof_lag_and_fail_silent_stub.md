# 49F frozen-AUA ROOT: asOfDate==today-UTC + the fail-silent empty-stub write

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, DEPLOY, VALIDATE
**serial:** 0.6.0_AE_PartnerETL | **date:** 2026-07-09 | **window:** ~08:30Z -> ~09:30Z (respawned lane; CTO GO 080527Z + 083650Z)

## Objective

Ground the empty-root of the 49F portal's frozen AUA (ADVI_BDAPIMIG REST-pull writing EMPTY stubs
07-05..07-09, fail-silent), fix the fail-silent empty-stub write, and route CTO the grounding + fix
plan. Coordinate 0.7.0~A on the auth-quality angle.

## Compiler Tools

| run | result | note |
|---|---|---|
| `comp-which "where is the 49F BD REST pull..."` | near-tie, no fit | routed to comp-dups/comp-routes; neither fits a bronze REST pull. Ran the on-rails `comp-grep`/`comp-glob` instead, as designed (never dead-ends). |
| `comp-glob` x4 | PASS | located `cot_bronze_ingest.py`, `bd-49f-runner/lambda_function.py`, `merge-daily-incremental.py`. |
| `comp-grep` x4 | PASS | importers of the shared script, `_BRONZE_COMPLETE` consumers, `ALLOCATIONS_DAILY` producer. Carried systems-context on each hit. |
| `comp-pipescript io cot_bronze_ingest.py` | **NOT-FOUND** | "Script not found" -- the bronze REST script is not in the pipescript map. |
| `comp-pipescript deployed cot_bronze_ingest.py` | **NO MATCH** | "No scripts matched filter" -> could not verify deploy state; fell back to raw `head-object` ETag-vs-local-md5 (rail-checked). |
| `comp-blast download_export / emit_bronze_sentinel / ingest_table` | **NOT-FOUND x3** | explicitly "not a nothing-breaks clear". Blast radius grounded manually via comp-grep + reading consumers. |
| `comp-freshness chain bd` | **PASS -- and the PASS is the finding** | returned PASS on `bd_silver_allocations` while all 7 recent partitions were 0-row stubs mid-freeze. Elevated by CTO as the freshness-integrity reference case. |
| `comp-surface-check` (via safe-commit) | PASS | no critical surface touched on any of the 4 commits. |
| `comp-to ADVI_BDAPIMIG.P1` | OK | race-free per-session TO_ID. |

**What worked:** `comp-grep`'s systems-context pointed straight at the silver-merge seam.
**What failed / GAP (repeat of my 2026-06-30 finding, still open):** the BD-DataMining REST pull class
has NO comp-tool coverage -- `comp-pipescript io/deployed` and `comp-blast` all return NOT-FOUND for
`cot_bronze_ingest.py` and its functions, so a CLAUDE.md-Rule-20 dependency check before a
client-facing change had to be done by hand. This script feeds two firms' silver. It is the single
highest-value uncovered producer in the estate.
**New GAP found:** `comp-freshness` is bound to object mtime, so it greenlights 0-row stubs (brief filed).

## Deployment Sequence

| # | leg | action | proof |
|---|---|---|---|
| L1 | git | commit + push CLOUD | `9d44d6af5`, `7a229eaaf` (+ later `463238356`, `d37ae51b6`) |
| L2 | s3-prefix | shared `cot_bronze_ingest.py` -> both firm planes | md5 `fa9fd5a9652e7c7aea60776ed469c773` == bd ETag == cot ETag |
| L3 | tf-lambda | `build-and-upload.sh bd-pipeline bd-49f-runner` -> `safe-apply` (HALTGT) | "0 added, 1 changed, 0 destroyed"; replan "No changes"; APPLIED live `CodeSha256=q37ovM/...` + `BD_SNAPSHOT_ASOF_LAG_BDAYS=1` |
| L4 | verify | non-mutating live exercise of lag + reject | CW `[$LATEST]13719c00d6ab4ced9877b85c94dd2505`: as_of resolved 07-09, `REJECT ... 0 DATA ROWS`, ZERO writes |
| L5 | repair | CTO-GO'd re-pull of as_of 2026-07-08 (allocations + unrealized) | bronze 12,935,870B / 38,647,736B + sidecars `has_data_rows:1` |
| L6 | verify | served end-state | **HELD-external (gold gate ~04:00Z 07-10)** |

Ledger: `org/critical_paths/change_management/20260709T0855Z_bd-49f-empty-stub-asof-lag-root-fix_deploy_completion.md`

## Verification

- **Root (source+live+exercised).** `bd-49f-runner` fires 00:00:19Z off `bd-49f-session-daily` (the
  `bd-49f-runner-daily` cron(0 2) rule is DISABLED). `run_date=_today_utc()` -> `asOfDate` = today-UTC,
  which at 00:00Z is the prior EVENING in ET. BD answers a point-in-time SNAPSHOT query for a
  non-existent date with a header-only ~4,592B xlsx. PERIOD tables (transactions/realized) span a 14d
  window and are unaffected -> the exact 2-of-4 split observed nightly.
- **Auth REFUTED (decisive).** One invocation, one re-minted bearer: allocations(491479)=4,592B,
  realized(491480)=993,387B. A reduced-scope session cannot do that. 0.7.0~A stood down.
- **Exercised, read-only, no S3 write:** asOfDate 2026-07-09 -> 4,595B / 0 rows; 2026-07-08 ->
  12,898,345B / 32,726 rows. Same cookie, same token, date the only variable.
- **Repair verified by ROW COUNT, not existence:** `silver/allocations/2026-07-08` 6,870 rows /
  $1,840,781,732.39 (was 46,277B / 0 rows); `silver/unrealized/2026-07-08` 103,490 rows (was 8,016B / 0).
- **S5 falsifiable prediction, written before the run:** gold lags run_date by 2 days, so the ~04:00Z
  07-10 gold should certify off data_date 2026-07-08 with `certified_aua = $1,844,022,461.17`
  (+/- drift), != the frozen $1,837,159,865.68.

## Decisions Made

1. **Parameterized, default-OFF as-of lag** (`BD_SNAPSHOT_ASOF_LAG_BDAYS`) rather than changing the
   date semantics globally -- the firm-safety shape CTO already blessed for `BD_TXN_CHUNK_DAYS`. cot's
   windows stay byte-identical; only `bd-49f-runner` opts in.
2. **Rejected the byte-threshold "fix".** Raising `download_export`'s `<100` check would swap one
   arbitrary existence proxy for another. Bound the guard to row count instead, pre-write.
3. **Did NOT delete the 07-09 stubs.** Destructive, needs Andrew, and buys nothing: the absent sidecar
   makes `_table_complete` read the stub as not-landed, so tonight's run re-pulls and self-heals it.
4. **Did NOT run an ad-hoc gold** to un-freeze ~19h sooner. CTO-ruled disproportionate; DS lane; NEVER#2.
5. **Did NOT roll back cot's auto-deployed copy.** A Model-B shared script cannot be staged to one firm
   plane -- the pre-push `safe-deploy` hook deploys `data/cot/scripts/bronze/*.py` to `opal-data-cot`.
   Reverting the object would desync cot's runtime from the repo, a worse state. Surfaced to DS + CTO.
6. **Relocated a finding rather than force-bypassing** the owned-paths hook (`data/black_diamond/API/
   findings/` is POD4's lane; I am AE).

## Self-caught defect (recorded, not buried)

My first `_export_has_data_rows` counted bare `<row `. BD emits **namespaced** XML (`<x:row`,
`<x:dimension`), so it matched ZERO times in every real export. It passed the real-stub fixture for the
WRONG REASON (0 matches read as "empty") and passed the real-export fixtures only via a `>256KB`
size short-circuit that never exercised the counting path. **A small-but-VALID export would have been
REJECTED as empty** -- the guard written to prevent a freeze inventing a new one. Caught while dumping
raw sheet bytes for the 500K finding, BEFORE running the re-pull on a blind probe. Rebound to
`<dimension ref>` (exact, O(1), namespace-agnostic). `463238356`.

## Corrections issued upward

- **500K cap:** I nearly retracted it as an openpyxl phantom. The landed 07-08 export's `<dimension
  ref="A1:O500001">` = exactly 500,000 rows vs 07-02's arbitrary 488,577 -> the cap is REAL. CTO's
  call stood; my doubt was wrong. Corrected myself before it became a filed retraction.
- **Severity premise:** the "~$185M / 11% OVERSTATED / ~3wk stale" figure is not supported by any
  artifact. Frozen cert @07-02 $1,837,159,865.68 vs true @07-08 basis $1,844,022,461.17 =
  **$6.86M / 0.372% UNDERSTATED, 7 days stale**. CTO owned it (the $185M was a cert-vs-derived-AUA
  comparison -- different quantities) and is correcting Andrew.

## Briefs Written

- `docs/briefs/comp-freshness-is-mtime-bound-greenlit-a-5day-client-facing-freeze-20260709.md`
  (ELEVATED by CTO as the freshness-integrity program's reference case; `bd-49f-freshness-probe`'s
  `SilverAgeHours` rides the same mtime predicate -- source-confirmed `lambda_function.py:17-20` --
  so tool AND alarm were both proxy-bound, which is why a monitored, alarmed pipeline froze silently.)
- `docs/briefs/bd-unrealized-export-500k-row-cap-finding-20260709.md`

## Files Modified

- `data/cot/scripts/bronze/cot_bronze_ingest.py` -- as-of lag, row probe, universal 0-row snapshot
  reject, generalized completeness sidecar, content-bound sentinel.
- `infra/aws/lambda/bd-pipeline/bd-49f-runner/lambda_function.py` -- content-grounded `_already_landed`,
  as-of-keyed idempotency + sentinel, `rejected` in the result.
- `infra/aws/terraform/bd-pipeline/bd-49f-interim.tf` -- `BD_SNAPSHOT_ASOF_LAG_BDAYS = "1"`.
- `infra/aws/lambda/ci/lambda-source-map.json` -- stale `_build_note` corrected (it claimed the runner
  emits no bronze sentinel; it does, and that sentinel was firing silver on stubs).
- `data/cot/scripts/bronze/tests/test_empty_stub_and_asof_lag.py` (new, 35 tests),
  `data/cot/scripts/bronze/tests/test_retry_net.py` (2 mock targets updated for the sidecar rename).
- Task order `ADVI_BDAPIMIG.P1` annotated. 57/57 tests green.

## Blockers

None. L6 (served un-freeze) is a **hard external gate** -- D_00 produces the served AUA only inside
the scheduled ~04:00Z gold; there is no served write between gold runs. CTO ruled no ad-hoc gold. The
remediation has executed; only propagation waits. Ledger HELD-external so it does not read as a
half-landed deploy.

## Current State (handoff)

- Fix live on `bd-49f-runner` (CodeSha256 `q37ovM/...`, `BD_SNAPSHOT_ASOF_LAG_BDAYS=1`), shared script
  on both firm planes (md5 `fa9fd5a9...`).
- `silver/allocations` max NON-degenerate date = 2026-07-08 (6,870 rows). 07-09 remains a 0-row stub,
  intentionally, and is self-healing.
- Tonight 00:00Z: runner re-pulls as_of 07-09 (sidecar absent -> not-landed -> re-pull) and overwrites
  the stub; ETag change forces the merge to replace the silver partition.
- ~04:00Z 07-10 gold: expected cert `2026-07-08.json`, `certified_aua ~= $1,844,022,461.17`.

## Next Steps

1. **[0.6.0, post-gold]** Exercise the SERVED property (cert JSON + `certified_aua` + the portal) and
   RAVC CTO. Close ledger L6. If gold instead advances to 07-09 and the runner failed to land it real,
   the cert will skip again -- check the runner's 00:00Z log first.
2. **[0.4.0_DS]** cot's snapshot tables carry the same latent date bug (holdings retry-net masks it);
   decide whether cot opts into `BD_SNAPSHOT_ASOF_LAG_BDAYS=1`.
3. **[CTO/CVO freshness-integrity program]** bind `comp-freshness` AND `bd-49f-freshness-probe`'s
   `SilverAgeHours` to row-count/content, not mtime.
4. **[owner TBD]** the unrealized 500,000-row cap: read `<dimension>` across consecutive dates; if it
   recurs exactly, paginate or fail loud. Check `transactions` for the same boundary.
5. **[0.7.0~A, registered]** bearer TTL < runner sweep duration (686s run threw two mid-sweep 401s,
   both re-mint-recovered; benign now, fragile on a longer sweep).
6. **[comp-tool coverage]** `cot_bronze_ingest.py` has no `comp-pipescript`/`comp-blast` node -- second
   time this has blocked a Rule-20 pre-change dependency check on a client-facing producer.

---

## Addendum -- freshness-integrity tonight-slice (COO /drive GO 094410Z, CTO-ruled)

**archetype:** IMPLEMENT | **window:** ~09:45Z -> ~10:05Z | used the gold-gated idle capacity.

Closed my own finding: bound `bd-49f-freshness-probe` to CONTENT. Ledger
`20260709T0957Z_bd-49f-freshness-probe-content-assertion` CLOSED, 4/4 legs proven.

**Framing correction (material).** COO dispatched "SilverAgeHours mtime -> content". Source says the
ALARM rides **`TradingDayLag`**, and its `max_as_of` was parsed from the **object KEY NAME**
(`lambda_function.py:209-218`) -- a FILENAME proxy, weaker than mtime. Fixing `SilverAgeHours` alone
would have changed an unalarmed metric and left the alarm exactly as blind. Rollout lesson: read what
the ALARM consumes, not what the docstring says.

**Fix.** Anchor `max_as_of` on the newest partition PROVEN to hold >0 rows; row count from the parquet
footer (thrift-compact `FileMetaData.num_rows`) via ONE suffix-ranged GET (~64KB). No full download,
no new dependency (probe stays pure stdlib+boto3 -- FIRM-SEP forbids growing its surface). Metric
names unchanged, so the alarms needed no TF change; only their input became truthful. Added
`SilverRowCount` / `SilverNewestPartitionDegenerate` / `SilverRowCountUnknown`. Fail-OPEN on an
unparseable footer (unknown != empty), never on a proven-empty one. IAM: `s3:GetObject` on
`opal-data-bd/silver/*` only.

**Cert bar -- exercised on the REAL known-bad artifacts (CTO condition):**
| bar | result |
|---|---|
| real 46,277B 0-row stub | reads **0 rows** |
| repaired 07-08 partition | reads **6,870 rows** |
| pre-repair inventory replay (live stub objects) | OLD filename lag=**0 GREEN** vs NEW content lag=**4 REDS** (threshold 2) -- would have fired on day one |
| repaired estate | no false page (alloc 1, unreal 1, txn 0, realized 0, fees 2) |

LIVE in AWS: `silver/allocations 2026-07-09 -> 0 rows (DEGENERATE stub) -- skipped, not an as_of anchor`.
APPLIED truth off live `get-function-configuration` (CodeSha256 `lIfp0ZeJ...`) + live `get-role-policy`.

**Second self-caught defect this session.** `self.i += self.varint()` in the BINARY skip is wrong --
Python evaluates the left `self.i` BEFORE `varint()` advances it, so the length prefix's own bytes are
never skipped and every later field header lands one byte early. It crashed on the real stub's 15-char
`portfolio_group` column. Both bugs I shipped tonight were in MY probe, not the vendor's data, and both
were surfaced by exercising the real artifact rather than a fixture. Tests 12/12.

**Handed to the daylight program:** (1) `infra/aws/lambda/cot-pipeline/bd-cot-freshness-probe/lambda_function.py:211`
carries the IDENTICAL filename-anchored `max_as_of` -- first rollout target, this code drops straight in
(not touched: cot lane). (2) `comp-freshness` itself is still mtime-bound. (3) `SilverNewestPartitionDegenerate`
is emitted but deliberately NOT alarmed tonight -- allocations' newest partition IS degenerate right now
(the self-healing 07-09 stub) and would page Andrew at ~05:00 ET for a known, remediated condition;
recommend alarming after tonight's runner heals it. (4) Unrelated pre-existing IAM gaps surfaced by the
mandated `comp-iam gaps`: `astn-wsjft-orchestrator` missing `s3:GetObject`+`s3:PutObject`,
`etfs-reports-orchestrator` missing `s3:PutObject` -- routed to COO, not my lane.

Commits `f45e63189`, `e0909399b`. Compiler tools: `comp-iam service bd-49f-freshness-probe` (pre-change,
grounded that the role had ListBucket only), `comp-iam gaps` (post-iam.tf), `comp-glob` (found the cot
sibling). 49F itself remains gold-gated; post-gold served-property RAVC to CTO closes it.
