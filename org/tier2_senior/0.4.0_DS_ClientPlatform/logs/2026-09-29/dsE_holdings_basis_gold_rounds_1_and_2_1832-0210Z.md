# The holdings-basis gold, built twice: one account YTD, then every 49F account back to inception -- 0.4.0_DS_ClientPlatform~E

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Date:** 2026-09-29
**Task Order:** IRPT_BCKEND.TO-IB-er-201 (round 1), IRPT_BCKEND.TO-IB-er-202 (round 2); IRPT_BCKEND.TO-IB-er-191 (cancelled before any write)
**Status:** COMPLETE

---

## Objective

Move 49 Financial performance off the flow-based TWR form and onto Andrew's call-3 basis: end-of-day
asset holdings only, weight-pro-rated daily security returns, the delta from the previous day, no
inflow/outflow logic (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_222xZ_OPEN_CALLS_1_2_APPROVED_3_HOLDINGS_BASED_PERFORMANCE.md`).
Round 1 proved the method on one account over YTD; round 2 widened it to every 49F account back to
the silver's first computable day, with a manifest that states its own completeness.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-find | `comp-find 'stream_parquet' --limit 20 --band DEF -- lib data` | PASS | MEASURED zero over 1,634 files with 105 binary and 2,794 ephemeral-floor declared unsearched, so the zero was not read as an absence. Found the module at `data/assets/scripts/lib/stream_parquet.py` and reused it for the atomic ETag-verified write instead of a hand-rolled `put_object`. |
| comp-find | `comp-find '08335338' --limit 25 -- infra/logic/registry` | PASS | 5 hits over 7 files; located the MASTER scope row that made the firm derivation possible. |
| comp-pipescript io | `comp-pipescript io holdings_performance.py --pipeline advi` | FAIL (correctly) | `Unknown script in tree [advi]`. The graph is queried, never rebuilt (Rule 20), and its vintage predates this producer. Re-run in round 2 to confirm the state rather than assume it. Recorded as a refusal, never a pass. |
| comp-pipescript deployed | `comp-pipescript deployed` | PARTIAL | `STATE NOT-DECIDABLE (rc=4)`, ANSWER-STATE PARTIAL_OR_BLIND, 90 s budget reached with 0 of 1 `s3_head_object` scanned. Also not applicable on its own terms: the producer ran from the working tree and has no deployed code prefix. |
| comp-pipescript postdeps | `comp-pipescript postdeps holdings_performance.py --firm bd` | FAIL (correctly) | `REFUSED (rc=2)` unknown id, 35 ids searched. No downstream consumer exists to disturb: the prefixes are new and no reader is switched. |
| comp-validate | `comp-validate data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` | FAIL (NO_CONFIG) | Per `org/XXX.md` that means UNVALIDATED, so no SAFE was signalled. Declared as an exclusion in both proof-of-spec instances rather than left looking covered. |
| naming-gate | `python .tools/naming-gate.py --diff <new files>` | WARN then PASS | REFUSE 6 -> REFUSE 4 -> PASS 3 graded 0 REFUSE in round 1; PASS 0 graded in round 2. The middle step is the whole story of row S191. |
| proof-of-spec-check | `python .tools/proof-of-spec-check.py <instance> <ids>` | PASS | INVALID rc=1 with 8 violations on the first round-1 write, then VALID rc=0 for both rounds. |
| pytest | `python -m pytest data/assets/scripts/gold/irpt_holdings_performance/tests/ -q` | PASS | 9 passing in round 1 (2 failed first and each named a real defect), 13 in round 2. |
| pyarrow read_metadata | footer `num_rows` summed over 557 partitions | PASS | 3,188,339 rows, equal to the producer's tally. Used deliberately instead of trusting the EMIT line. |
| ruff / py_compile | `ruff check --target-version py39 <dir>` | PASS | Clean; non-ASCII census 0 bytes and 0 characters, measured as a byte delta and a character count separately. |

**What worked:** `comp-find`'s explicit unsearched-file accounting stopped a zero from reading as an
absence, which is exactly the trap it exists for -- and the module it then found gave me atomicity and
ETag verification for free instead of a hand-rolled write. `proof-of-spec-check` and `naming-gate`
both caught real problems I would otherwise have committed.

**What failed:** nothing silently. Four tools refused the new producer as an unregistered script, and
all four refusals were correct; the risk was reading them as passes, which the proof-of-spec instances
explicitly avoid.

**Gap found:** a brand-new gold producer is invisible to `comp-pipescript` (graph), `gold_pipeline_deps.yaml`
and `gold_validate_config.yaml` at once, so every Rule-20 instrument answers "unknown id" and none of
them can distinguish "new and unregistered" from "wrong id typed". Registration has no home until a
deployed code prefix exists, which is the schedule cell (`IB-er-203`). Named here, not filed as a
surprise row, because it is a known consequence of being round 1 rather than an unexpected state.

## Work Completed

### 1. TO-IB-er-191 received, then cancelled before any write

Issued at 22:50Z to rewrite `c02_twr_engine.py`'s daily return in place; halted at 22:57Z when
Andrew's ~22:4xZ direct widened the basis to all firm channels via one consolidated gold. I had done
read-only surveys only. Verified and reported: `c02_twr_engine.py` byte-identical to HEAD
(`git diff HEAD` empty at ac7792ac50), no commit, no QA run, no S3 write, no ledger opened.

Three measurements from those surveys were delivered to the issuer rather than discarded, since the
CRO's silver-inventory brief was the next act: the rule is applicable at 49F (6,288 of 6,341 accounts
fully priceable on one day pair, 99.2%); `canonical_positions` carries `closing_price` itself; and row
W61-S2's cause is that an all-refusal partition emits no value columns at all.

### 2. TO-IB-er-201 -- the thread: one account, YTD

Built `data/assets/scripts/gold/irpt_holdings_performance/{sources.json, holdings_performance.py}`
plus tests. The declaration is data (PRD v0.19 ruling 1); every address comes from
`lib/opal_naming.address()`; the day axis is `lib/trading_calendar`; the write rides
`lib/stream_parquet`.

The cash columns were named from the data by subtraction against a printed denominator, not from
their names: `money_mkt_funds + net_credit_debit` equals `net_mv_plus_cash - net_mv_positions` for
92,407 of 92,407 account-rows across 14 partitions spanning 2024-07-08..2026-09-16. I rejected
`cash_balance_settled_only` on measurement -- it equals `net_credit_debit` only where the balance is a
credit, so substituting it breaks the identity for 142 of 7,540 rows at 2026-09-24.

E1-AC1 PASS, E1-AC2 PASS (184 of 184 trading days, chained YTD +5.83%), planted mutant fired.

### 3. Row S191 -- the check and the commit gate were jointly unsatisfiable

`E1-AC1` read the declaration as `json[...]["49financial"]`, and the naming limb refuses a bare
registered firm token in a new authored JSON. I narrowed six refusals to one by removing two
redundancies that deserved removing anyway, established that both remaining fixes were outside this
cell's grant (the generated-file route needs a `lib/opal_naming.py` generator target), and escalated
with the measurement. No override taken, no gate edited, no enforce switch touched, no check weakened.

The issuer amended `E1-AC1` @5e273c614f and ruled the entry be re-keyed by custody source. The result
is better than what I had built: the entry is keyed `schwab_08335338`, carries only its `master`, and
the firm comes from `lookup(master)["firm"]` -- so it cannot drift from the registry, and a second
custody channel of the same firm needs no second firm token. Every emitted value is unchanged.

### 4. TO-IB-er-202 -- every 49F account, full history

Vectorized the per-account roll-up (round 1 sliced a frame per account, free for one account over 184
days and not for ~6,300 over 557). Added the manifest completeness triple and a parquet surface beside
the JSON, both projected from one dict. Four new tests.

E2-AC1 PASS (6,341 silver accounts, 7,540 gold rows, 0 missing, 0 duplicated, manifest
6341/6338/3 complete=True), E2-AC2 PASS (557 of 557 trading days). 3,188,339 rows landed.

## Decisions Made

1. **`account_value` is the return DENOMINATOR** (included t-1 holding value + t-1 cash), not the
   whole book. The pair with `excluded_value` reconstructs the book, so the exclusion is visible
   arithmetic rather than a silent shortfall. Stated in the manifest so no consumer has to infer it.
2. **Four-member status vocabulary**, MECE over "why does this account-day carry no return", each
   member named by the remedy that moves it. A pure-cash account is OK at 0.0 (cash earning zero is
   the ruling, not a refusal); an account that held positions and could price none is
   ALL-HOLDINGS-EXCLUDED, because emitting 0.00% there would fabricate a flat day out of a price gap.
3. **The manifest's completeness population is prior-HOLDINGS, not rows.** Counting rows would inflate
   the denominator by every cash-only account (1,199 of 7,540 at 2026-09-25) and make the stated
   identity false.
4. **`complete` reads FALSE on any account-restricted run** -- it is a claim about the partition, and
   round 1's single-account partitions had no business asserting it.
5. **Escalated rather than forced on S191.** The TO's refusal clause says stop and file; the
   alternatives were an override I am not entitled to take or a weakened check.

## Files Modified

See commit messages: 23004aaf98, 9a47906bda, e29adc9fa7, f778b0c741. Rows needing extra context:

| File | Note |
|---|---|
| `data/assets/scripts/gold/irpt_holdings_performance/sources.json` | Re-keyed mid-session from a firm token to `schwab_08335338` on the S191 ruling; `firm_scope` dropped as redundant with the key. |
| `data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` | Two defects found by its own tests before any S3 write: the full-exit branch order (see Briefs Written) and `declared_firms()` treating the declaration's `doc` key as a firm. |
| `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md` | Four rows appended: S189, S190, S191, S192. Appended in the shared tree, never isolated in a worktree (Rule 14b's inversion for append-only shared files). |

## Briefs Written

| Finding | Where | Owner |
|---|---|---|
| The 49F Schwab silver disagrees with itself on the position total: `dim_balance.net_mv_positions` differs from the summed `dim_position` market value for 420 of 92,407 account-rows (0.4545%), worst delta $4,926,000.00, round-million shape suggesting one instrument class rather than float error | row IRPT_BCKEND-S189 | routed via `2.0.0_SA_COO~M` |
| `date=2025-01-09` is not a trading day at all (NYSE closed, 2025 national day of mourning), which is the standing cause of half of row W61-S2; the real shared defect is that an all-refusal partition drops its value columns, so a schema-guarded reader refuses a whole history over a column absence rather than a missing value | row IRPT_BCKEND-S190 | open |
| `E1-AC1` and the naming limb jointly unsatisfiable for the declaration's firm key under this cell's grant | row IRPT_BCKEND-S191 (BLOCKING) | ruled by `2.0.0_SA_COO~P` msg 102514 |
| Dispositions S191 on that ruling | row IRPT_BCKEND-S192 | disarmed same turn |
| The full-exit branch-order defect: with every holding excluded and no cash the base is 0, so both the all-excluded and non-positive-base tests are true; graded on base first, a full exit reports NON-POSITIVE-BASE and sends a reader to the account's value when what is missing is a PRICE | caught by `test_a_full_exit_is_not_minus_one_hundred_percent`, fixed pre-write, documented at the branch | closed in-session |

## Blockers

**None.** S191 was a real blocker for 36 minutes and is closed: the issuer amended the check and ruled
the re-key (msg 102514), both criteria then passed, and row S192 dispositions it. S189 and S190 are
open FINDINGS owned elsewhere, not blockers on this lane -- neither reaches the gold this producer
writes, because the base is built from `dim_position` plus the declared cash columns and never from
`net_mv_positions`.

## Current State

The consolidated holdings-basis gold exists and is complete for 49 Financial.

- **Producer:** `data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` at
  commit e29adc9fa7. Selector is `--source` (a custody-source key); the firm is derived via
  `opal_naming.lookup(master)["firm"]`; the module names no firm at all. `--date` or
  `--start`/`--end`, `--accounts` for a QA thread, `--dry-run`/`--upload`.
- **Declaration:** `sources.json`, one entry `schwab_08335338` reading
  `opal-data-assets/schwab/08335338/silver/{dim_position,dim_balance}/`, cash columns
  `["money_mkt_funds", "net_credit_debit"]` with `cash_columns_basis: measured`.
- **Served-nothing gold on S3:** `s3://opal-data-49financial/irpt/49financial/gold/holdings_performance_daily/date=YYYY-MM-DD/data.parquet`
  and `.../holdings_performance_manifest/date=YYYY-MM-DD/{data.parquet,manifest.json}` -- 557
  partitions each, 2024-07-09..2026-09-25, 3,188,339 rows, 0 empty, every manifest `complete=True`.
  15-column daily schema; 22-column one-row manifest parquet.
- **No reader is switched.** `irpt-performance-adapter`, `c02_twr_engine.py` and every served table
  are untouched. `2.0.0_SA_COO~P`'s adapter switch was gated on this manifest reading complete
  (CTO ruling 102520); that condition is now MET and the switch is ~P's own cell.
- **Commits, all LOCAL:** 23004aaf98, 9a47906bda, e29adc9fa7, f778b0c741. `origin/CLOUD` reads
  fd045338c4 (`git ls-remote`, read at 02:0xZ). Trunk pushes are not this seat's act.
- **Ledgers:** `irpt-holdings-gold-thread-49f-20260928` and `irpt-holdings-gold-all-49f-20260929`,
  both CLOSED with all three legs proven. No open deploy at this lane.
- **Tests:** 13 in `data/assets/scripts/gold/irpt_holdings_performance/tests/`.
- Two untracked files under the project's surprise channel (`ADJUDICATION_v14.md`,
  `REMEDIATION_v10.md`) are `3.0.0_SA_CVO`'s and were left alone.

## Next Steps

1. **[`2.0.0_SA_COO~P`]** The adapter switch: its stated condition (this manifest reads complete) is
   met at every one of the 557 partitions. Nothing on this lane gates it.
2. **[`2.0.0_SA_COO~M`]** Row S189 -- the `dim_balance` vs `dim_position` position-total disagreement.
   It does not reach this gold, but it will surface the moment anyone reconciles the new gold against
   a vendor's official figure at a pre-set period (PRD v0.19 ruling 3).
3. **[`1.0.0_SA_CTO` or the LGIC builders' owner]** Row S190's producer-shape half: the superseded
   engine's all-refusal partitions drop their value columns. The new table cannot repeat it (fixed
   15-column schema on every row including refusals), so this is about `c02_twr_engine.py` until it
   retires under ruling 12.
4. **[whoever holds `IB-er-203`]** The daily schedule. Until it lands, every partition here came from
   an ad-hoc QA run and the producer has no production trigger -- and graph/validate-config
   registration for this script belongs with that cell, since it is where a deployed code prefix
   first exists to census.
5. **[`0.4.0_DS_ClientPlatform~E`]** Inflection and Cottonwood are later rounds (ruling 11); each is a
   new `sources.json` entry keyed by its own custody source, not a code branch.
