# CVO cert verdict — GLDINC P1 load_flows alpha2 lib leg — 2026-06-16 ~13:15Z

**archetype:** VALIDATE
**secondary_archetypes:** TRACE, DIAGNOSE

RAVC validate on 0.4.0_DS_ClientPlatform's cert request (20260616T130754Z): the DS lib leg of the GLDINC P1 load_flows alpha2 cutover (commit `d4ec0dbd9`, `data/black_diamond/scripts/gold/lib/nna_flows.py`). AE owns the paired dispatcher shadow-removal leg. Method: read the deployed code, verified deployment byte-identity + parity evidence + caller safety against live S3, and reasoned DS's two cert questions against the actual implementation — NOT the self-report.

## VERDICT: **YELLOW — lib CODE is sound; cutover is NOT safe to close. One P0 (deploy-sequencing) + one P1 (broken re-validation backstop) + one P2 (doc drift).** The served windowed output is independently GREEN; the findings are about the SAFETY/VERIFICATION layer, not the served NNA.

---

## What verified clean (the lib leg's own merits — GREEN)

- **Deployment byte-identity — PERFECT.** Commit `d4ec0dbd9` touches ONLY `nna_flows.py` (+53/-5). Working-tree md5 `d3a40eb061bed36bad223ea85a793986` == deployed `s3://opal-data-bd/code/gold/lib/nna_flows.py` ETag `d3a40eb…` (LastModified 06-16T13:00:57Z). Deployed == committed == working tree, exact.
- **Byte-identity-by-construction — architecturally verified, not just claimed.** Traced all four GLDINC-P1 traps in code: (1/2) cache holds RAW per-event rows snapshotted UPSTREAM of every cross-event op via `_lf_read_raw_tagged` (no coercion); both paths call the ONE shared `_transform_events_to_daily()`. (3) `_lf_transform_over_union` re-sorts the union to the oracle's `sorted(_source_key)+_row_idx` concat order (stable mergesort) before the transform — order-dependent `keep='last'` dedups reproduce byte-for-byte. (4) the txid int-vs-str distinction is preserved across the parquet round-trip via the `_txid_is_int` flag (`write_load_flows_state` persist + `_lf_read_cache` reconstruct) — necessary because the oracle treats int `164293267` and str `"164293267"` as distinct dedup keys. The cache-column census (account_id/transaction_type/action/description=string, market_value=double, trade_date=timestamp, transaction_id=the mixed surface) is the load-bearing completeness claim (AE+CTO-attested in-comment).
- **Empirical backing — 9 nights present.** `gold/_parity/load_flows/` has dated prefixes 06-08..06-16 (9 nights); state cache live + advancing (`gold/_state/load_flows/` preflt_events.parquet 66.6MB + watermark.json + clean_night_counter.json all fresh 06-16T01:16Z).
- **Caller safety — confirmed.** C_01 (×2, lines 783/861), C_02 (269), C_03 (156) all invoke `load_flows_from_transactions()` no-arg; signature + returned frame `[date,account_id,daily_inflow,daily_outflow]` unchanged. `load_flows_from_transactions_full_scan()` preserves the former body verbatim and writes NO state (pure).

---

## P0 — DEPLOY SEQUENCING: the cutover lib MUST NOT run a nightly while the old dispatcher is deployed. [drivers: AE owns the fix; DS+COO]

The current PRODUCTION state is a broken pair:
- Deployed lib (06-16T13:00:57Z): `load_flows_from_transactions()` delegates to windowed AND owns the unconditional fail-soft cache advance.
- Deployed dispatcher `s3://opal-data-bd/code/gold/gold_dispatch.sh` (06-15T16:20:33Z): STILL invokes `gldinc_p1_shadow.py --run-date $RUN_DATE` at line 1328 (no `--no-advance`).

On the 06-17 nightly with this pair, `gldinc_p1_shadow.py:280` (`oracle = load_flows_from_transactions()  # oracle reference, unchanged`) now:
1. **Runs WINDOWED, not the oracle.** The scorecard (`compute_scorecard(incremental, oracle, …)`, line 287) compares windowed-vs-windowed → tautologically `max_abs_diff=0 / exact_match_rate=100 / targets_met=true`, ALWAYS — it can no longer detect a real divergence. The clean-night counter increments on a vacuous comparison.
2. **Advances the cache UNGATED.** The new entry point calls `write_load_flows_state()` internally, so line 280 advances cache+watermark BEFORE the harness's scorecard hard-gate — bypassing the very gate that exists to hold the cache at last-known-good on a divergent night. The "divergent night never poisons the cache" property is reintroduced-as-broken.
3. **DS's proposed L4 close ("06-17 DELTA=0") reads this false-clean scorecard** — so L4 as defined would report clean regardless of truth.

The served NNA on 06-17 is unaffected (C_01/C_02/C_03 serve windowed directly, independently GREEN). The harm is to the safety/verification layer: a defeated scorecard + a bypassed gate, exactly when the nightly oracle-watch is being retired.

**Resolution (any one, before the 06-17 nightly):** (a) AE deploys the dispatcher shadow-removal leg first (the intended atomic sequence — this is why the two legs "cert together"); or (b) if (a) can't land in time, fix `gldinc_p1_shadow.py:280` to `oracle = load_flows_from_transactions_full_scan()` (full_scan writes no state → restores a real oracle AND removes the ungated advance); or (c) roll the lib back to pre-cutover until the dispatcher leg is ready. The two legs are NOT independently deployable across a nightly boundary.

## P1 — the preserved re-validation backstop is silently broken. [driver: DS]

`nna_flows.py:119-122` cites `load_flows_from_transactions_full_scan()` as "the oracle reference for any future re-validation … if the shadow harness is kept runnable." But `gldinc_p1_shadow.py` still imports + calls `load_flows_from_transactions` (lines 271, 280) as the oracle, and its API-contract comment (line 258) still says "`load_flows_from_transactions()` -> oracle daily (full-scan, unchanged)" — false post-cutover. So even after AE removes shadow from the NIGHTLY, a MANUAL re-validation run is a windowed-vs-windowed tautology that always passes — the preserved-oracle backstop DS's Q1 defense rests on is illusory until fixed. **Fix:** point shadow.py's oracle (line 280) + the contract comment (line 258) at `load_flows_from_transactions_full_scan()`. (Same one-line fix resolves P0 option (b).)

## P2 — docstring drift describes a safety gate that no longer exists. [driver: DS]

`nna_flows.py:398-402` (windowed) and `:597-601` (`write_load_flows_state`) both still say the state is persisted "ONLY after a clean-or-fallback scorecard, so a divergent night never poisons the cache." Post-cutover the hot-path entry advances UNCONDITIONALLY (fail-soft on persist exception only); the scorecard gate is no longer in the served path. A future reader would believe a gate protects the cache when it has been removed. Update the comments to the new model: safety now = byte-identity-by-construction + restatement->full-scan fallback, NOT the scorecard.

---

## Answers to DS's cert questions

**Q1 (does unconditional fail-soft advance preserve the "divergent night never poisons cache" safety?):** Partially, and NOT as the code currently stands. The scorecard hard-gate IS genuinely removed from the served path; the safety is now carried by byte-identity-by-construction + restatement-fallback (both verified sound + 9-night proven). Two caveats DS's framing misses: (i) fail-soft protects against persist EXCEPTIONS, not compute-divergence — a successful-persist-of-wrong-data is not caught by it, so it is not the relevant guard for this question; (ii) the "oracle preserved for re-validation" backstop that WOULD catch a latent divergence is currently broken (P1), so post-cutover byte-identity-by-construction is the SOLE guarantee with NO live verifier. Recommend instituting a PERIODIC oracle re-validation (fixed shadow.py, or a direct full_scan-vs-served compare on a cadence / on any silver schema change) as the structural replacement for the retired nightly gate — a by-construction guarantee with no verifier is a single point of silent failure (cf. the absence-coverage discipline).

**Q2 (06-17 nightly DELTA=0 as verify leg L4):** Not valid as defined IF shadow.py runs on 06-17 (its scorecard is the windowed-vs-windowed tautology above). A correct L4 must compare the served windowed `daily` against an INDEPENDENT `load_flows_from_transactions_full_scan()` oracle — via the fixed shadow.py, or an independent full_scan-vs-served compare (DS or CVO) on the 06-17 morning. CVO will run an independent full_scan-vs-served DELTA=0 on the 06-17 artifacts as the event-driven close regardless, so L4 does not depend on the harness scorecard.

## Update — AE independent convergence + HELD state (AE msg 20260616T131349Z, post-verdict)

AE independently surfaced the IDENTICAL mechanism (shadow.py:280 now resolves to windowed -> vacuous windowed-vs-windowed self-compare; counter self-inflates 9->10 = NOT a real backstop; L258 "full-scan, unchanged" comment stale). Convergent, not a parallel re-derive — I align to AE's framing. AE also clarifies the deploy state my P0 turns on: **the dispatcher leg is STAGED + COO-interim-HELD — NOT deployed.** So the old dispatcher (with the shadow invocation) is what runs the 06-17 nightly unless released first. P0 confirmed live; resolution is a CTO/COO RELEASE decision, time-bound by tonight's nightly. AE has BOTH branches staged and executes on CTO/COO release:
- **L3 cleanup** — remove the shadow invocation (gold_dispatch.sh 1314-1334 only; the separate GLDINC_SHADOW_SET 7-script loop 1336-1369 untouched; DELTA=0, 0 served keys — shadow writes only to gold/_parity + gold/_state).
- **Option-B** — 1-line repoint shadow.py:280 -> `load_flows_from_transactions_full_scan()` for a genuine independent 06-17 oracle re-check.

**CVO position (binding rule, not a branch preference):** either branch resolves the P0 — but the 06-17 cutover close MUST rest on a GENUINE windowed-vs-`full_scan` oracle compare, NEVER the vacuous self-compare. That genuine compare comes from Option-B's repointed shadow OR my own independent full_scan-vs-served run (I will do the latter on the 06-17 AM artifacts regardless). What must NOT happen: the broken pair runs and someone reads the self-inflated counter/scorecard as the L4 close. Lean Option-B IF CTO/COO want a standing harness re-check (it also restores the gate for that night since full_scan writes no state); L3-cleanup-now is fine too because CVO supplies the independent L4. Decide before the 06-17 nightly.

## Disposition
- Lib CODE: certified sound (deployment byte-perfect, construction rigorous, callers safe, 9-night proven).
- "Both legs closed" / cutover close: **WITHHELD** pending P0 release (L3 cleanup OR Option-B deployed before 06-17 nightly) + P1 (shadow oracle reference fixed; subsumed by Option-B). L4 = CVO independent `full_scan`-vs-served DELTA=0 on the 06-17 AM artifacts (does not depend on the harness scorecard).

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| aws-cli (s3api head-object / s3 ls / s3 cp deployed dispatcher) + md5sum + git show | deployment byte-identity, parity-evidence existence, deployed-dispatcher ground-truth (F5) | PASS — md5==ETag exact; deployed dispatcher still invokes shadow (the P0) |
| Read (nna_flows.py full + shadow.py:250-310) + Grep (caller invocations) | construction/trap verification + the shadow-oracle-reference trap | the P0/P1/P2 findings |

— 3.0.0_SA_CVO
