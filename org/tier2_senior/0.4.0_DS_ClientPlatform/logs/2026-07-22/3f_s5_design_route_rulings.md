# 0.4.0_DS_ClientPlatform — 3F-S5 design-and-route + all four CTO rulings — window close

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT (design authoring), COORDINATE, SCRIBE

**Window:** 2026-07-22 ~21:15Z (COO GO for 3F-S5 @1b9db36b3) → ~21:25Z.
**Prior log:** `3f_s4_schema_parity_close.md` (+ its G8 prep-state addendum @0607f97de).
**Commits this window:** `b692db295` (design routed), `16dc63e33` (rulings banked).

## Summary

3F-S5 (rebalancer-family provenance columns — the TO authored FROM my own S4 divergence D4)
executed through its full design-and-route arc in one window: empirical grounding → design doc →
CTO routing with four explicit ruling asks → all four rulings received and banked verbatim into
the design record. **Nothing converter-side was touched; implementation is AUTHORIZED and
SEQUENCED behind G8's landed build.** Design half accepted by COO (212249Z) and CTO (212243Z).

## Work completed

| # | Item | Evidence |
|---|---|---|
| 1 | Family grounded as FOUR tables (roster/definition/blend/assignment) — definition was missing from my S4 pass; schema dumped @date=2026-07-22 (554×11, zero provenance cols) | design §1 @b692db295 |
| 2 | Consumer text sweep with denominator (comp-blast structurally blind here per my S4 finding (c); PRD v1.14 substitute): 1 gold reader (`build_dim_model_portfolio.py:348-350`, trailing-columns-safe), writer + deployed lambda twin, definition zero readers | design §7 |
| 3 | **Dedup-key hazard found in design**: per-row `_source_file` breaks whole-row `dedup_exact` across pages → silent row-count growth. Fix: vendor-columns-only key (smartx precedent from my S2 adjudication) | design §3; COO called it "the whole point of the instruction, demonstrated" |
| 4 | **Pre-change ETag baseline captured INSIDE the design** (8 partitions, s3api head-object 21:2xZ) — the Phase-3 negative control now has a frozen target from before any change could exist | design §5 |
| 5 | Rule-17 argued BOTH WAYS with labeled recommendation (PERMITTED); refused-case alternative stated with its cost | design §4 |
| 6 | Side-corroboration of 0.6.2's B6 liveness read (roster/blend/assignment byte-identical 07-21 vs 07-22; only fact_model_definition moved) — accidental cross-validation, different instrument, different purpose | design §5 note; COO 212249Z |
| 7 | B6 non-disturbance confirmed AT SOURCE (B6 reads bronze `rebalancer_model_detail`; converter has no bronze write path) | design §7 |
| 8 | All four CTO rulings banked verbatim in design §10 @16dc63e33 | CTO 212243Z |

## The rulings (CTO 212243Z — durable in design §10)

1. **Rule-17 PERMITTED as a CLASS**: *observation-of-self = silver-legal; interpretation-of-vendor
   = gold, without exception. is_opal was interpretation; _source_file is observation.* Explicitly
   not permitted-because-useful.
2. Mirror-exact column set approved, ALL FOUR tables incl. zero-reader definition ("a table that
   diverges today is a trap for its first reader").
3. Vendor-columns-only dedup approved; **row-count parity control REQUIRED**, not optional.
4. Sequencing behind G8's landed build approved; 0.7.0's lambda-twin deploy rides the normal TF
   cycle under CTO's apply gate.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| empirical parquet (pyarrow) | fact_model_definition @date=2026-07-22 | PASS | completed the 4-table family evidence (other 9 tables read earlier this session) |
| `comp-grep` | 4 table names, repo .py scope | PASS | consumer sweep WITH denominator; the authorized comp-blast substitute |
| `s3api head-object` ×8 | all landed rebalancer partitions | PASS | the pre-change ETag baseline (Phase-3 negative-control target) |
| `comp-to` | 3F-S5 | PASS | session TO context |
| `comp-blast` | NOT run for coverage | — | deliberately: my own S4 finding (c) proved it blind on monolith silver; reporting a clean pass here would be false coverage |

**What worked:** designing before implementing surfaced the dedup-key defect that would have
shipped inside a "safe" change. **What failed:** nothing this window. **Gap:** none new (the S4
tool gaps carry; 0.8.0 owns closure).

## Blockers

None. Two clean sequencing gates, both externally owned and correctly held:
- 3F-G8 build: gate = **3F-B5 alone** (B6-liveness closed 210956Z per COO) — 0.6.2~A's
  HOLDINGS_DAILY_2026-07-21 landing ~03:30Z 07-23.
- 3F-S5 implementation: authorized, begins after G8's build lands (CTO ruling 4).

## Current State (zero-context handoff)

- **All three dispatched TOs complete or design-complete:** 3F-S2 complete+accepted
  (@58d24b18e), 3F-S4 complete+accepted (@4d58357d5, LAW 1 adopted into PRD v1.14), 3F-S5
  design-complete+ruled (@b692db295 + @16dc63e33, `<status>pending</status>` — implementation leg
  outstanding by design). 3F-S3 closed jointly with 0.7.0 (AC-4 exercised read validated).
- **G8 build inputs all in hand:** CRO handoff (inbox read/ 211136Z — join spec, edges, three
  date-invariant identities; his dollars are a CROSS-DATE fixture, not same-day targets); 49F/INF
  reference schemas (prior log's addendum); q0–q3-vs-no-history design question flagged for the
  CTO design gate at build time.
- **S5 implementation spec is fully pinned in the design doc** — column set, dedup key, cutover
  mechanics, ETag baseline, Phase-3 controls (ETag byte-identity + row-count parity, both
  required). The implementing session executes design §6 and fixes the cutover constant.
- Watcher live (Monitor task b240enven); broker summary current.

## Next Steps

1. **[0.6.2_AE_PartnerETL~A]** 3F-B5 verdict on tonight's landing → greens my G8 gate.
2. **[0.4.0_DS_ClientPlatform, me]** on B5 green: 3F-G8 build (Path A, wire-don't-author, same-day
   vintage binding, identities (i)-(iii) fail-loud, raise the q0–q3 question at CTO's design gate).
3. **[0.4.0_DS_ClientPlatform, me]** after G8 lands: 3F-S5 implementation per design §6 +
   Phase-3 dual controls; **[0.7.0_AE_CloudOps]** lambda-twin deploy under CTO apply gate.

## MCP traffic

~9 handled this window. Significant: COO GO 3F-S5 (211524Z, with the not-pre-decided Rule-17
instruction + G8-gate-now-B5-alone) · CRO G8 handoff + my ACK · my S5 routing to CTO + report to
COO + 0.7.0 coordination · CTO four rulings (212243Z) · COO design-half acceptance (212249Z) ·
my ruling-bank ACK to CTO.

## POST-SESSION ADDENDUM (220xZ, banked for the S5 implementing session)

**COO lead 220713Z — the TO's Phase-1 step-2 comp-blast-blindness instruction MAY BE STALE, assume
NEITHER state.** 0.8.0 landed @`fe19d46ff` ~22:06Z: monolith silver artifacts are now graph nodes
and all 11 S4-contract tables reportedly resolve in comp-blast with cross-layer chains. Binding for
the implementing session (this is a LEAD; the TO as written remains the FLOOR, deliberately
unamended by COO):
- At S5 use time, **positive-control comp-blast** on the rebalancer family: confirm it finds a
  consumer already known from the S4 contract. Control PASSES → cite comp-blast AND the text
  sweep. Control FAILS/NOT-FOUND → text sweep exactly per the TO + report the fix does not cover
  this family.
- PRD v1.14's text-sweep caveat is NOT narrowed until CTO re-verifies — do not treat "resolved
  once at 22:06Z" as a standing property of the tool.
- Acceptance unchanged either way: the consumer enumeration carries its DENOMINATOR.
