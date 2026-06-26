# comp-tools Health Campaign -- Summary (Andrew-directed)

**Owner:** 3.0.0_SA_CVO | **Date:** 2026-06-26 | **Gate:** CTO arch-gate on graph-module / cot-freshness surfaces
**Mandate (Andrew-direct):** "review the comp-tools registry and make sure all are properly mapped, then
go through and stress test all of them and make sure they work under duress, then identify if there are
any obvious holes or improvements, incorporate those, and stress test and validate." Authorship: CVO
authors directly (Andrew-direct).

## Method (P1-P5)
1. **Map** -- audited the registry (`graph-call-manifest.yaml` tools_index + entries + excluded list) vs the
   ~38 `.tools/comp-*` on disk.
2. **Stress under duress** -- ran every tool with bogus/garbage/nonexistent input + timeout guard; classified
   HANG / TRACEBACK / silent-rc0 / fail-loud.
3. **Holes** -- consolidated; ranked by blast radius (which are change-safety / Rule-20 gates).
4. **Fix** -- authored directly, each WITH an adversarial regression test (reproduces-then-resolves).
5. **Re-validate** -- consolidated sweep: 58 regression tests + comp-which 29/3/20 + re-stress of fixed tools,
   all green.

## The unifying lens: verdict-above-grounding
Every hole was the **same shape** -- a tool returning a verdict ABOVE its actual grounding: a FALSE-CLEAR
(rc0 on a not-found target), a FALSE-GREEN (a test that only exercises canonical inputs), or a FALSE-FRESH /
FALSE-RED (mtime standing in for content). CTO named the standing acceptance criterion mid-campaign: **"a test
that exercises only CANONICAL/happy-path inputs is a false-green."** So every fix ships a test that exercises
ADVERSARIAL inputs, not just the golden phrasing.

## 6 false-signal classes CLOSED (CVO-authored)

| # | Tool | False-signal class | Fix | Proof | Commit |
|---|------|-------------------|-----|-------|--------|
| 1 | comp-trace / comp-blast / comp-xref | **FALSE-CLEAR**: a typo'd / not-found target exited rc0 -- on these Rule-20 change-safety gates a typo read identically to a verified "nothing breaks / no consumers" clear | not-found -> rc=3 + NOT-FOUND marker; a real match with zero results still rc0 | regression: garbage->rc3 AND live-pulled real node->rc0 (6/6) | `ded7a6d0f` |
| 2 | comp-build | **silent-do-work-on-garbage**: a garbage arg silently triggered a full graph REBUILD (rc0), and `--check` (verify-freshness-without-rebuild) was UNREACHABLE -- the wrapper dropped `$@` | forward `"$@"` like every sibling wrapper | `--check`->rc0 (no rebuild), garbage->rc2 (loud), bare->rebuild | `61f67b214` |
| 3 | comp-which | **FALSE-GREEN on the RAIL** (Rule 21 default): the 29/29 "self-routing" test was near-tautological (fed each tool its own use_case sentence -- the very text the backstop scores against). Real-NL paraphrases routed only **15/20** | added general real-NL vocabulary to 5 rules + a distinct comp-graph rule; locked a **20-case diverse-paraphrase TEST 3** into the standing guard | 29/29 self + 3/3 audit + **20/20** paraphrase | `71a41a3d2` |
| 4 | comp-iam | **scan-scope coverage hole**: globbed only `infra/aws/terraform/**` -> multi-account/ + ec2/*/terraform roles got NO gap-check on a Rule-20 deploy gate | scan all 3 roots (dedup-by-resolved-path, skip .terraform caches); loud-skip unresolved-var module templates | 8 newly-in-scope roles parsed w/ correct source; collision regression 3/3 + scan-scope 3/3 | `814296969` |
| 5 | registry | **completeness gap**: comp-grep/comp-glob (the on-rails search primitives comp-which RUNS) were in NO registry category -> invisible to a registry audit | accounted them in `excluded_not_graph_use_cases` w/ reason | all 38 `.tools/comp-*` accounted; 0 unaccounted | `4be425bab` |
| 6 | comp-freshness | **FALSE-FRESH**: keyed on S3 mtime -- a re-uploaded-but-stale artifact gets a fresh LastModified while its internal as-of stays old (the cot freeze: mtime moved, data_as_of stuck). mtime-only -> wrongly FRESH | **content-mode**: when `as_of_field` is declared, the object's internal as-of is AUTHORITATIVE; mtime demotes to secondary. UNCHECKED is LOUD (never a silent fallback). + cot pipeline wired (was bd/inf-only) + a load-filter (skip partition-key entries -> no false-RED) + cadence tuned to the T+1 frontier | LIVE on cot served (mtime 0.8h would PASS, content 40h WARN-then-PASS at frontier-correct 96h); 16/16 incl. load-filter adversarial test; mtime-only control proves content-mode flips it | `ab3eab2e6` + `5666cbd84` + `01d3126dc` |

**Plus independently VERIFIED (0.5.0-authored, CVO-verified):** comp-iam cross-module TF role-label COLLISION
(false-MISSING / mis-attribution). Re-ran all points on my side, no divergence; the exact false-MISSING action
(`ec2:Start/StopInstances`) now GRANTED; regression 3/3. `d7ccc029e` + test `e26eb5540`.

## 2 tracked follow-ons (non-blocking)
- **opt-B: partition-key convergence** -- teach comp-freshness `as_of_source: silver-partition-key` so it and
  `freshness_manifest_gen.py` share ONE freshness engine (today the load-filter cleanly separates them).
- **Frontier-aware cadence** -- the interim flat 96h threshold on cot served trades off (passes the normal
  Monday but MISSES a 1-trading-day-behind freeze, and would false-warn a post-holiday Tuesday). The proper fix
  is a trading-day/frontier-aware threshold **sharing COO's `bd-cot-served-aua-stale` cadence model** (one
  definition, two consumers: the alarm + comp-freshness). Converge with COO/0.6.0. CTO flagged the tradeoff;
  the interim is a fine stopgap because the alarm is the primary freeze detector and comp-freshness is the
  diagnostic surface.

## Meta-finding (the durable win)
The campaign's own lens turned inward: **a tool's test can itself be a false-green.** comp-which proved 29/29 on a
tautological corpus; the real number was 15/20. Two of the agent's own intermediate verdicts were also false
(an A11 classifier matched a footer mention, not an instance). The standing fix is the acceptance criterion now
applied across the suite: **canonical-only coverage = UNVALIDATED, regardless of a green suite.** Every fix above
ships an adversarial / reproduces-then-resolves test so the next edit is measured honestly.

## Validation (consolidated P5, all green)
- 58 regression tests (iam collision + scan-scope + false-clear + comp-freshness content-mode/filter): PASS
- comp-which routing guard: 29 self + 3 audit + 20 paraphrase: PASS
- fixed-tool re-stress: not-found->rc3, garbage->rc2, --check->rc0
- registry completeness: 0 unaccounted
