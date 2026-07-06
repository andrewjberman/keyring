# BD un-freeze P0: account_is_open str-dtype class -- source-gate + all-consumer fix + Andrew-direct incremental-vs-full sweep -- 0.4.0_DS_ClientPlatform

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, DEPLOY, COORDINATE

**Date:** 2026-07-06
**Task Order:** ad-hoc P0 (0.6.0_AE BD un-freeze blocker + Andrew-direct incremental-vs-full sweep, COO-driven)
**Status:** IN PROGRESS (all durable fixes landed+deployed; P0 served flip pending on 0.6.0's mode=full re-dispatch)

---

## Objective

Un-block the Andrew-watched 49F served flip (07-01 -> 07-02), which crashed the BD gold chain, and run Andrew's directed incremental-vs-full parity sweep to end the crash class systemically. Root turned out to be ONE bug (A_00 incremental writes account_is_open as str not bool) surfacing at MULTIPLE consumers.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| ds-commit-gate.sh | on B_00, A_00 (x3), C_07, B_02 | PASS | py_compile+ruff+AST; caught A_00/C_07 legacy migrations (future-import, F401, E701) |
| comp-pipescript consumers | consumers A_00.accounts_dimension | PASS | confirmed A_00 fan-out (A_01/A_04/B_00-02/C_00-02+) = broad blast for the dtype |
| comp-grep | "data_as_of_date" / account_is_open ops | PASS | consumer-inventory scan (fragile ops == True/.eq()/~) across A/B/C/D |
| Grep (native) | --incremental / merge_incremental / select_dtypes | PASS | triaged the 8 true-incremental scripts + confirmed the blanket-cast + preserve_cols mechanisms are A_00-UNIQUE |
| aws s3api/cp (verify) | ETag-MATCH on every deploy; head-object checkpoints/served | PASS | Rule-22a applied-state verification (deploys + chain progress + served vintage) |

**What worked:** comp-pipescript consumers + the whole-dir grep for the F1/F2 mechanisms let me conclude "A_00-unique" efficiently; ETag/head-object grounded every deploy + the chain progress (caught the stale `aws s3 ls` timestamps -- head-object is authoritative).
**What failed:** none (comp-validate has no addressable config for the served leaderboard -- known, flagged prior log).
**Gap found:** none new.

---

## Work Completed

### 1. P0 root: account_is_open str-dtype (ONE bug, MULTIPLE consumers)
A_00.save_dimension blanket-casts all object cols to 'string' (L602-608); the incremental merge (prior-parquet round-trip + concat) collapses bool account_is_open to object -> str-ified. The FULL path keeps it bool. Downstream consumers of the str dim crash/mis-behave DIFFERENTLY:
- B_00.load_account_closures `~df['account_is_open']` -> TypeError (LOUD crash) -- the 1st crash.
- C_07.advisor_attribution L338 `acct_dim['account_is_open'] == True` -> 0 rows -> empty open_acct -> empty funded -> resolve_architect returns column-less -> KeyError 'arch_tier' (2nd crash, DIFFERENT symptom, SAME root). arch_tier is C_07-INTERNAL (T1/T2/T3), NOT an A_00 column -- disproved 0.6.0+COO's "A_00 drops arch_tier" inference (Rule-22).
- B_02.canonical_lots L795+L919 `.eq(False)` -> 0 rows -> empty closed-set -> SILENTLY drops closed-account realized-lot tax handling (SILENT-wrong, high-blast, never served since chain crashed first).

### 2. Fixes (all deployed+ETag-MATCH)
- B_00 defensive coerce (04c733de5) -- load-bearing: handled the EXISTING str parquet so B_00 cleared without an A_00 re-run (verified prod B_00.done 16:13Z).
- A_00 write-boundary: bool coercion -> generalized into a producer-side DTYPE-PARITY GATE (d705604f7: contract-driven coerce+WARN on bool+datetime cols before the string cast) -> WARN-DELIVERY (2ab432850: CloudWatch metric Opal/DataQuality::AccountsDimensionDtypeCoercion + [DTYPE-DIVERGENCE] marker, best-effort, per CTO item-3).
- C_07 (d8b27a78a) + B_02 (94383024e) consumer-side coerces (robustness contract).

### 3. Andrew-direct incremental-vs-full sweep (accepted)
- Root mechanism named (merge round-trip + concat -> object -> blanket string-cast; preserve_cols semantic asymmetries). ACCEPTED as "the class engine."
- Mechanisms A_00-UNIQUE (grep-confirmed): only A_00 has the blanket object->string cast + merge-outputs preserve_cols. Other 7 incremental scripts (A_01/A_02/A_03/B_01/B_02/B_03/C_06) use safer architectures (A_01/A_02 feed the same builder = parity by construction; A_02 self-documents byte-identical; A_03 already coerces account_is_open).
- F2 RETRACTED (self-caught Rule-22 miss): I asserted the full path drops advisors from L461 alone; grounding the fix I found load_accounts_from_transactions L252-286 ALREADY does per-role last-non-blank carry-forward (the CTO spec, pre-existing). Cost a CTO ruling+Andrew confirm cycle; caught before shipping a wrong fix to correct code. COO: "the discipline working."
- account_is_open consumer inventory COMPLETE: 3 op-fragile (B_00 ~, C_07 ==True, B_02 .eq(False)) all coerced; A_03 guarded; D_00/D_00b/B_01 column-read-only (dtype-agnostic). ONE source fix (A_00 bool) + consumer-coerces = whack-a-mole ended.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| GO mode=FULL (grounded) over incremental whack-a-mole | Full re-runs A_00 with my deployed dtype-gate -> bool dim -> ALL consumers correct + no crash; grounded on the SAME account_is_open root (not the inferred arch_tier-drop). Held 0.6.0's trigger until source-confirmed (post-F2 discipline). |
| dtype-gate = coerce+WARN (not raise) | A dtype divergence is recoverable (coerce keeps pipeline flowing + surfaces WARN); unlike an unrecoverable row-drop -> fail-loud. CTO RATIFIED coerce+WARN+DELIVER. |
| Retract F2 immediately | A causal claim is a hypothesis until source-confirmed; the full path already complied -> no fix, stop before shipping to correct code. |

---

## Files Modified

See commit messages: `04c733de5` (B_00+A_00 bool), `d705604f7` (A_00 dtype-gate), `d8b27a78a` (C_07), `94383024e` (B_02), `2ab432850` (A_00 WARN-deliver). All bd-gold, all deployed to opal-data-bd/code/gold/ + ETag-MATCH verified.

---

## Briefs Written

None -- P0 fixes + sweep; no new brief/data-contract.

---

## Blockers

None (mine). P0 served flip is gated on 0.6.0's mode=full re-dispatch (fired 17:04Z, ETA ~40-60min) -- a real external gate (AE-owned trigger + running gold chain), not a DS block. Consumer path confirmed CLEAN (won't hit a 3rd mid-chain crash).

---

## Current State

The 49F served flip is blocked ONLY on 0.6.0's mode=FULL bd-gold re-dispatch completing (fired 17:04:19Z; chain verified progressing B_00 16:13 -> C-group; D/platinum ahead). ROOT was ONE bug: A_00's incremental path wrote gold/dimensions/accounts_dimension_latest.parquet account_is_open as str ('True'/'False') via save_dimension's blanket object->string cast; it crashed B_00 (`~`, loud) then C_07 (`== True`, KeyError arch_tier) and would have silently broken B_02 (`.eq(False)`, empty closed-set). ALL fixed: source (A_00 dtype-parity gate d705604f7 writes bool + WARN-delivers on any future divergence 2ab432850) + every op-fragile consumer coerces (B_00/C_07/B_02). mode=full regenerates a bool dimension so all consumers are correct this run. When platinum flips data_as_of->07-02, I independently verify the served vintage + joint-RAVC COO with 0.6.0 (they own AUA no-widen + bd-0702 ledger close).

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] verify + joint-RAVC the served flip** -- on platinum data_as_of=07-02, confirm served vintage + co-RAVC COO with 0.6.0; close bd-0702 P0.
2. **[0.6.0_AE_PartnerETL] infra half of WARN-delivery** -- confirm bd-gold runner has cloudwatch:PutMetricData + wire an alarm on Opal/DataQuality::AccountsDimensionDtypeCoercion>=1 -> SNS subscriber (DS emit is landed).
3. **[1.0.0_SA_CTO] ratify** the dtype-gate coerce-vs-raise (done: coerce+WARN+DELIVER) + shared-helper (deferred to 3rd grounded axis) + the robustness contract (consumers boolean-op'ing a dim col should coerce dtype).
4. **[0.4.0_DS_ClientPlatform] (banked)** restatement-window-completeness residual (incremental carry-forward looks back only across the re-read window) -- flag only if out-of-window restatements are a real concern; D_00 net_flows_ttm today-anchor (from earlier session).
