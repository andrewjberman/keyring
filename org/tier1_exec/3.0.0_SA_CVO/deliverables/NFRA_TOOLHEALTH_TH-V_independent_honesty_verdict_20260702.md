# NFRA_TOOLHEALTH.TH-V -- CVO Independent Honesty Verification (Phase-1)

<verifier>3.0.0_SA_CVO~B</verifier>
<subject>org/modules/graph/comp_tool_health.py (637 lines) + .tools/comp-tool-health -- TH-B skeleton, commit 64c89d675</subject>
<issued_by>2.0.0_SA_COO~B (GO 2026-07-02T~19:57Z)</issued_by>
<date>2026-07-02</date>
<constitution>Art. XIV -- VERIFY, do NOT co-author. Sharpest-test-binds; could-not-verify is a finding (Rule 22).</constitution>

## VERDICT: VALIDATED_WITH_GAPS

The two Phase-1 honesty properties in scope both **HOLD under fully independent re-derivation**:
scorer/health verdicts are value-anchored with **zero usage-Goodhart**, and a flagged **RETIRE
reproduces on live** as a genuine dead node. Two named, grounded gaps remain -- both are
**demonstration-robustness advisories to TH-B**, not honesty defects (no false verdict, no real
Goodhart). Neither warrants REWORK of the skeleton. The EFFECTIVE-axis honesty properties are
**correctly out of Phase-1 scope** (gated on TH-A) and recorded as deferred, not failed.

## Independence method (sharpest-test bind)

I did **NOT** re-run the subject's code to check it. I wrote a standalone re-derivation
(`scratchpad/indep_rederive.py`) that imports **none** of the subject's modules
(`comp_tool_health` / `comp_learns_score` / `comp_route` / `tool_activity_emit`) and hand-rolls:
(a) its own pipe/JSONL parsers over the raw substrate, (b) its own `result_class` outcome
weighting (re-implemented from the `comp_route.result_class` PASS/FAIL token spec I read), and
(c) its own `classify_full`/`decide` taxonomy. Raw sources read directly:
- **USED** -- `org/compiler-tools-log.md` (11,389 pipe rows) -- rolling-log ONLY (the subject also
  folds session-log blocks, so my event counts are a deliberate LOWER BOUND).
- **RAIL** -- `org/mcp/comproute-routing.jsonl` (641 route rows), winner = `ranked[0].id`.

## Property A -- scorer/health honesty (value-anchored, zero usage-Goodhart): **VALIDATED**

grounding: `scratchpad/indep_rederive.py` vs `comp-tool-health --json` (50 tools) --
- **50/50 verdicts match**; 0 hard mismatches. The only 4 divergences are `~BOUNDARY`
  (KEEP@3-8ev vs my RETIRE@1-2ev) and are fully explained by session-log rows I intentionally
  excluded pushing a tool across the `MIN_USED_EVENTS>=3` line.
- **`mean_outcome` matches to the 3rd decimal on EVERY outcome-bearing tool** (e.g. comp-drift
  0.494, comp-constants 0.432, comp-iam 0.943, comp-freshness 0.980) despite my lower event
  counts -- proving the VALUE anchor (`outcome_n` mean) is computed purely from raw PASS/FAIL
  RESULT cells, identical `outcome_n`, **never from usage volume**.
- **Non-monotonic in usage (the anti-Goodhart bite, independently reproduced):** the verdict does
  not track usage rank. Highest-usage NON-KEEP is `comp-drift` at **usage rank 18** (85 events ->
  FIX, mean 0.494); also `comp-constants` (rank 31 -> FIX), `comp-tooltip` (rank 34 -> FIX). Low-usage
  KEEPs exist (`comp-learns-score` 3ev, `comp-diff` 9ev). Usage magnitude does NOT drive KEEP.
- **FIX observation reproduced on raw data:** `comp-drift`'s raw RESULT cells are ~50% FAIL
  (41 PASS / 41 FAIL in `org/compiler-tools-log.md`) -- 85 invocations, half failing -> a
  value-grounded FIX. Heavy usage did not protect it.
- Builder proofs exercised + adversarially checked: `--self-test` **13/13 PASS** (all checks
  legitimate; the COO summary's "12/12" is a count-drift in the *summary*, not the tool);
  `--goodhart-audit` returns `is_usage_proxy: false`.

## Property B -- FIX/RETIRE reproduction on LIVE: **VALIDATED (RETIRE)**

grounding: raw `org/compiler-tools-log.md` + `graph-call-manifest.yaml` --
- **`comp-secrets` (RETIRE) reproduces as a genuine dead node:** **0** tool-column invocations in
  the rolling log; its only 3 raw mentions (lines 9022/9031/9071) are non-tool (two are
  `comp-surface-check` runs referencing `.tools/comp-secrets` as a *file* argument; one is a
  session-close note). Yet it is **manifested** (7 hits in the canonical catalog) => a
  manifested-but-dead node, exactly the RETIRE catch the design intends.
- `comp-depth` / `comp-dispatch` / `comp-dups` (the other three RETIREs): **0** rolling-log
  invocations each. All four RETIREs reproduce.
- The used-but-ineffective **FIX-via-EFFECTIVE-probe** flavor is gated on TH-A (Phase-B) -- see
  deferred below. The value-grounded FIX flavor (Property A) is confirmed live.

## GAP-1 (advisory to TH-B) -- `--goodhart-audit` under-demonstrates its high-usage arm

grounding: `comp_tool_health.py:635-638` (`by_use[:15]`) + independent usage-rank table --
The audit's `high_usage_NOT_keep` arm returns **empty** because it inspects only the top 15 by
usage, and the strongest counter-example -- `comp-drift` -- sits at **usage rank 18**, just outside
the window. The "not a usage proxy" conclusion therefore rests solely on the `low_usage_IS_keep`
arm this run. The property is TRUE (independently confirmed), but the builder's own proof
under-shows it. **Fix:** widen the window (`[:20]`+) or explicitly surface high-usage non-KEEP
tools -- then the arm exhibits comp-drift/comp-constants/comp-tooltip. Not a honesty defect.

## GAP-2 (advisory to TH-B) -- `value_unknown` KEEP `basis` string over-claims

grounding: `comp_tool_health.py:467-471` (`_value_anchor.basis`) + live rows --
`comp-tool` and `comp-which-rail` are **KEEP** with `mean_outcome=None` (value_unknown) AND
`rail_quality=no_signal` -- neither a positive value signal nor a rail signal. Their KEEP rests on
`events>=3` (crossed only via session rows) + the "unknown-outcome-treated-as-healthy" convention.
The emitted `basis` string nonetheless asserts *"KEEP rests on value-healthy outcomes + rail
decision-quality, NOT usage count"* -- not literally true for these two. This is **bounded**: the
verdict is provisional (`KEEP?`, pending EFFECTIVE), the convention is documented ("absence of a
RESULT is not evidence of failure"), and TH-A's EFFECTIVE probe resolves it. It is **not**
usage-magnitude Goodhart (4 events). **Fix:** qualify the `basis` string when
`value_unknown and rail_quality==no_signal` (e.g. "provisional KEEP -- no adverse signal; EFFECTIVE
pending"). Not a false verdict.

## Deferred -- out of Phase-1 scope (gated on TH-A; recorded, not failed)

Per the TO's Phase-1 boundary, these follow post-TH-A and are **not** counted against this pass:
- **EFFECTIVE-verdict isolation honesty** (author != solver != judge; not tuned-on-the-eval) --
  TH-A's blind-run probe does not exist yet (EFFECTIVE axis = `pending`); could-not-verify-YET.
- **used-but-ineffective FIX reproduction** (the EFFECTIVE-probe FIX flavor) -- pending TH-A.
- **TH-C close-loop "acted" delta (COMPPROOF-D1)** -- pending TH-C.
Phase-B is a one-line wire; `--self-test` check `phaseB.effective_feed_flips_live_keep_to_fix`
(comp-pipescript: eff=False->FIX / eff=True->KEEP, both final) demonstrates the join seam works on
the live substrate today, so the deferral is a data dependency, not a design gap.

## Disposition
- No REWORK of the TH-B skeleton (64c89d675). Its verdicts are honest and independently
  reproducible; the skeleton is fit to accept for Phase-1.
- GAP-1 + GAP-2 routed as **advisories to the owning TO (TH-B / 0.8.0_AE_CloudComp)** -- fold on
  next touch (they also make the Phase-2 EFFECTIVE-honesty pass cleaner).
- The EFFECTIVE-honesty re-verify (isolation + used-but-ineffective FIX + TH-C D1) is a Phase-2
  TH-V pass, GATED on TH-A/TH-C landing.
