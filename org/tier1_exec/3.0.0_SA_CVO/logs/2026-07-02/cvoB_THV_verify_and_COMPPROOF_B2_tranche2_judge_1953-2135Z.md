# CVO~B session -- NFRA_TOOLHEALTH TH-V verify + NFRA_COMPPROOF B2 tranche-2 judge

**archetype:** VALIDATE
**serial:** 3.0.0_SA_CVO~B | **window:** 2026-07-02 ~1953Z -> ~2135Z | **spawned-by:** MSTR (for TH-V + B2)

## Summary
Two independent CVO verification threads, both DELIVERED + ACCEPTED this session:
1. **NFRA_TOOLHEALTH.TH-V (Phase-1 honesty verify)** of the TH-B skeleton (`comp_tool_health.py` @ 64c89d675) ->
   verdict **VALIDATED_WITH_GAPS**, accepted by COO~B. commit `116864534`.
2. **NFRA_COMPPROOF.B2 (tranche-2 judge)** of the 12 banked blind-solves B-09..B-20 -> **7 SOLVED / 8 MISS /
   2 false-VOID / 3 held** (46.7% as-runs; 52.9% E-fixed VERIFIED; 55.6% merits full-corpus). Accepted + complete
   by COO~B. commits `a09e4b47c` (judge_axes + report) + `e43e20012` (methodology caveats).

## Thread 1 -- TH-V (VALIDATED_WITH_GAPS)
Method (Art. XIV): wrote a STANDALONE re-derivation (`scratchpad/indep_rederive.py`) importing NONE of the subject's
modules -- own parser, own `result_class`, own taxonomy over the raw substrate (`org/compiler-tools-log.md` +
`comproute-routing.jsonl`). Results:
- **Value-anchored, ZERO usage-Goodhart: VALIDATED.** 50/50 verdicts re-derive; `mean_outcome` exact to 3dp on every
  outcome-bearing tool. Non-monotonic-in-usage proven: comp-drift (usage rank 18, 85 events, ~50% raw FAIL) -> FIX;
  low-usage tools -> KEEP. --self-test 13/13 (COO summary "12/12" was a summary count-drift, not the tool).
- **RETIRE reproduces: VALIDATED.** comp-secrets = manifested-but-dead node (0 rolling-log tool-column invocations;
  3 mentions all non-tool; 7 manifest hits). comp-depth/dispatch/dups all 0 rolling invocations.
- **2 advisory gaps to TH-B (no REWORK):** (E1) `--goodhart-audit` `by_use[:15]` excludes comp-drift@rank18 -> its
  high-usage arm reads empty though the property holds; (E2) value_unknown KEEPs (comp-tool, comp-which-rail) carry a
  basis string that over-claims value+rail. EFFECTIVE-honesty (isolation + used-but-ineffective FIX + TH-C D1) correctly
  deferred to Phase-2 (gated on TH-A/TH-C). Deliverable: `deliverables/NFRA_TOOLHEALTH_TH-V_independent_honesty_verdict_20260702.md`.

## Thread 2 -- COMPPROOF B2 tranche-2 judge (B-09..B-20)
Method: graded blind vs the SEALED `true_root_cause`; exercised the objective isolation layer myself
(`harness.isolation_gate` + `assert_live_context_clean` + authoritative `harness.cheat_check`); 12 parallel
grounding-assistant subagents grounded each incident vs live source + tool_log; I applied `score_run` + owned the
verdicts + personally ground the borderline (B-12/B-13/B-17). Verdicts:
- SOLVED: B-10, B-19 (+ B-15/B-16 on merits, false-VOID'd today by FINDING E).
- MISS: B-09, B-11, B-12*, B-14, B-17(trip), B-18(substrate-gap), B-20(trip).  *B-12 = partial-substance (1 of 2 legs).
- HELD-OUT: B-13 (seal defective, FINDING F).
- **Grounding-resilience axis VALIDATED**: caught B-17 + B-20 as TRIPS (confident, source-grounded-looking, WRONG).

### Findings issued (RAVC'd COO~B, CC CTO)
- **E** (harness): context-gate false-VOIDs B-15/B-16 on the generic word "review" (the `code-review` CC slash-command
  colliding with `how_it_was_actually_found`). PROVEN fix: answer-terms from `true_root_cause` only -> void 2->0, no new
  leaks, 52.9%. Owner ~D.
- **F** (corpus, MAJOR): B-13 seal DEFECTIVE. Grounded: contradicts `0.5.0 MDPF_ASSETS.FREEZE-DX_diagnosis.md:9,38-40`
  (bd-fees stall + convergence-gate defer) + causally impossible (`bd-49f-interim.tf:383-411` -- silver-stale alarms only
  email SNS; the gate is "MDPF's real protection"). Solver reached the true cause. **CTO AFFIRMED** on ETL-domain
  authority + endorsed a seal-review gate; routed to ~D. Irony: the seal is itself a B-17 COTETL_SEAL_MISINFERENCE.
- **G**: `run_meta.cheat_check` false-positives persist (6/12; authoritative gate clears all). Mark advisory.
- **H**: binary-reach rubric can't express B-12's reached-1-of-2; recommend reach in {yes,partial,no}.
- **Side-finding**: live `infra/aws/lambda/ci/lambda-source-map.json` has 6 lambda registrations as top-level siblings of
  `functions{}` (invisible to CI drift tooling). **CTO AFFIRMED real** -> routing (inf-gold-trigger into 0.6.1 L7 + 5 as COO fast-fix).

## MCP traffic
~10 messages. Significant: COO~B [GO] TH-V -> my TH-V RAVC -> COO~B ACCEPT; COO~B [DRIVE] B2 -> my B2 RAVC (CC CTO) ->
COO~B RAVC-validate + correction (B2 accepted/complete) + CTO FINDING-F affirmation + side-finding routing. All handled.

## Compiler Tools
| tool | invocation | result | note |
|---|---|---|---|
| comp-tool-health | `--json` / `--self-test` / `--goodhart-audit` (the TH-V SUBJECT, adversarially exercised) | PASS | 13/13 self-test; goodhart-audit high-usage arm empty (E1 gap) |
| blind_run.py + harness | `--solver-results ... --judge-axes ...` (the COMPPROOF scorer, exercised end-to-end) | PASS | 7S/8M/2VOID/3PEND reproduces my judgment; E-fixed re-run -> 9S/8M |
| harness gates | `isolation_gate` + `assert_live_context_clean` + `cheat_check` over B-09..B-20 | PARTIAL | authoritative cheat clears all 12; context-gate false-VOIDs B-15/B-16 (FINDING E) |
| comp-* suite (via 12 grounding subagents) | comp-kuzu/comp-blast/comp-trace/comp-freshness/comp-platinum/comp-pipescript/comp-routes/comp-lambdamap/comp-which | PASS | per-incident live grounding; comp-kuzu graph topology load-bearing for B-12/B-20 |

**What worked:** the standalone re-derivation (zero subject imports) is the sharpest-test independence -- 50/50 + 3dp mean
match is airtight. Exercising the harness end-to-end (not asserting) proved the E-fixed number. **What failed:** n/a (both
verdicts landed). **Gap found:** the harness context-gate + rubric gaps (E/G/H) + a defective corpus seal (F) -- all routed.

## Blockers
None. Both threads DELIVERED + ACCEPTED. Downstream is other-agent lane: ~D (E harness-fix + F seal-correction + re-run ->
55.6% report.json), CTO (seal-review gate + lambda-source-map fix routing), TH-A (unblocks TH-V Phase-2).

## Current State
- TH-V Phase-1: CLOSED, VALIDATED_WITH_GAPS (`116864534`). Deliverable + independent re-derivation script on record.
- COMPPROOF B2 tranche-2: CLOSED, accepted. `judge_axes.json` (B-09..B-20, B-13 omitted=held), `JUDGE_REPORT_TO-B2_CVO-B_tranche2_B09-B20.md`,
  `judge_methodology_caveats.json` all committed (`a09e4b47c`, `e43e20012`). ~D spawning for E+F fixes + re-run; COO~B closes on re-run.
- Scratchpad (verification scripts, reusable): `indep_rederive.py`, `gate_diag.py`, `efixed_aggregate.py`, `incidents/B-*.txt` packets.

## Next Steps
- [2.0.0_SA_COO~B] fire ~D aggregator once E+F land -> merits-correct 55.6% report.json = Andrew-facing COMPPROOF answer + TH-A EFFECTIVE unblock; then close B2.
- [0.8.0_AE_CloudComp~D] apply FINDING E (one-line answer-term narrowing, proven) + FINDING F (B-13 seal correction, CTO-affirmed) + re-run.
- [1.0.0_SA_CTO] seal-review gate on the corpus (endorsed); lambda-source-map 6-key fix (routing in progress).
- [3.0.0_SA_CVO~B] STAND BY for TH-V Phase-2 (EFFECTIVE-honesty: isolation + used-but-ineffective FIX + TH-C D1), gated on TH-A/TH-C landing.
