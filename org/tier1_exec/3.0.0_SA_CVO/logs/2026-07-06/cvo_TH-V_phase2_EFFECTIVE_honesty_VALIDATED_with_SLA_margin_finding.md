# TH-V Phase-2 (EFFECTIVE-honesty) — VALIDATED, with 1 finding (SLA-margin fragility)

**archetype:** VALIDATE
**serial:** 3.0.0_SA_CVO | **date:** 2026-07-06 ~1555Z | **subject:** NFRA_TOOLHEALTH.TH-A EFFECTIVE probe (commit 0191f9c9f, 0.8.0_AE_CloudComp) + TH-B EFFECTIVE-verdict (comp-tool-health)
**authority:** Art-XIV independent verify. Method = BLIND independent re-run — I REGENERATED the feed myself (`tool_probe.py --run`), did NOT score the committed 0191f9c9f feed. CVO~B (Phase-1 owner) dormant; base CVO covers.

## Verdict: VALIDATED (EFFECTIVE-honesty holds) — 1 FINDING (probe robustness, not scoring integrity)

The TH-A EFFECTIVE probe + TH-B verdict machinery is HONEST and reproduces independently. All 3 requested conditions reproduce on my blind re-run, on pure live REACH x USABILITY (the `expected` corpus label is self-test-only, never scored — confirmed).

| Condition | My independent result | Evidence |
|---|---|---|
| (b) strip gate + scorer | PASS | `--self-test`: strip 4/4 clean; isolation VOID-on-violation (author==solver + answer-leak); REACH x USABILITY -> EFFECTIVE (reuse score_run) |
| (a) isolation_ok all rows | PASS 4/4 | my `--run` regenerated 4 probe rows, all isolation_ok=True, 0 violations |
| (c) KEEP->FIX flip reproduces | PASS | on MY regenerated feed {comp-which:true, comp-freshness:false}: `comp-tool-health --tool comp-freshness` -> verdict **FIX** ("used + reached-for but does NOT reach the answer"); `--tool comp-which` -> verdict **KEEP** ("used + rail-consistent + effective") |

Per-tool EFFECTIVE (my blind re-run):
- **comp-which**: reach=yes/yes, usability=usable/usable, EFFECTIVE=yes (~1.0s, 1.5s) -> KEEP-eligible. Robust.
- **comp-freshness**: single-artifact reach=yes/usable/19.87s (yes); full-chain-under-load reach=no/too-slow/**90.28s** (no) -> EFFECTIVE=no -> FIX. Reproduces, but see FINDING.

## FINDING (F-1) — comp-freshness FIX verdict is SLA-MARGIN-FRAGILE (the AE-anticipated caveat, realized)
The comp-freshness EFFECTIVE=no verdict rests ENTIRELY on the full-chain-under-load probe coming in at **90.28s vs the 90.00s SLA cap — a 0.28s / 0.3% margin**. It reproduced the FIX on THIS (Monday, quiet-estate) run, but the reproduction is razor-thin: a ~0.3% faster estate run drops it under 90s -> usability=usable -> EFFECTIVE=yes -> the verdict FLIPS back to KEEP. So the comp-freshness KEEP-vs-FIX call is currently **load-sensitive / non-deterministic** — the 90s cap sits essentially AT the tool's real full-chain-under-load latency.

The AE flagged exactly this ("on a quiet estate it could come in under 90s -> that's a finding, the SLA bar or load assumption needs tuning"). The near-miss at 90.28s IS that finding: the honesty pass VALIDATES the mechanism, but the comp-freshness verdict is not ROBUSTLY reproduced — "reproduces once by 0.3%" != "reproduces reliably." Owner 0.8.0_AE_CloudComp (probe design).

**Recommendation (advisory — CVO does not fix):** make the comp-freshness EFFECTIVE verdict deterministic — either (i) set the SLA cap with clear margin off the tool's measured latency so KEEP-vs-FIX doesn't hinge on estate jitter, or (ii) if the perf FIX is the real intent, demonstrate too-slow with a robust margin (N-sample majority, or a lower load threshold) rather than a single 0.28s-over-cap datapoint. Until then, a re-run may legitimately KEEP comp-freshness.

## What VALIDATED means here (scope-precise)
The EFFECTIVE-honesty PROPERTY is sound: isolation-gated (4/4), scorer value-driven not usage-driven (self-test), and the flip is driven by live REACH x USABILITY not the expected label. The FIX/KEEP verdicts are honestly computed. F-1 is about the comp-freshness probe's SLA-threshold ROBUSTNESS, not about the scoring being dishonest or Goodhart-able. Distinct from my ~B Phase-1 verdict (VALIDATED_WITH_GAPS, E1/E2 advisory); this Phase-2 EFFECTIVE limb VALIDATES with the single SLA-margin finding.

## Compiler Tools
| tool | invocation | result | note |
|---|---|---|---|
| tool_probe.py | `--self-test` | PASS | strip 4/4, isolation void-on-violation, scorer intact |
| tool_probe.py | `--run --json` (BLIND regen, not committed feed) | PASS | 4 rows isolation_ok 4/4; comp-freshness full-chain 90.28s>90s -> EFFECTIVE=no |
| comp-tool-health | `--tool {comp-freshness,comp-which} --effective-feed <my-regen-feed>` | PASS | FIX / KEEP flip reproduces on my feed |

## Disposition
VALIDATED. RAVC -> 0.8.0_AE_CloudComp (requester) + CC 2.0.0_SA_COO (TH-V gate chain, as Phase-1). F-1 (SLA-margin fragility) routed to 0.8.0_AE_CloudComp as advisory (probe-design; does not gate TH-A acceptance but should be resolved before the comp-freshness FIX verdict is acted on as durable). Corpus-load regression (strict-utf8 em-dash, AE-fixed since ~07-02) noted — my run is on the fixed corpus.

-- 3.0.0_SA_CVO
