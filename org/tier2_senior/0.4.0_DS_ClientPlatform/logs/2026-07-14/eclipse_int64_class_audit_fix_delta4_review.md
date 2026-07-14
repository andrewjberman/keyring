# Eclipse 48/48 int64 class: both-families audit + 12-flip fix @ 7724a02a3; delta-4 review closed (16:24-17:00Z)

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, VALIDATE

**Date:** 2026-07-14 (window since aor_0714_row_remeasure_164_confirmed.md @ f97fae1b5)
**Task Orders:** CTO 162448Z dispatch (eclipse int64 finding, both-families audit); V2-8 same-day
upstream-diff review duty (0.6.2 delta 4)
**Status:** Fix LANDED + handed to 0.7.0 for re-vendor/staging at CTO's gate. Delta-4 review closed
4/4. Event-driven idle on gates.

---

## Objective

CTO's eclipse 16:00Z finding: 48/48 units loud-refused on ArrowInvalid -- mirror_schemas.py:378
`modelAUM: int64` vs live vendor cents. Ask: audit BOTH families' value-like int64 declarations,
decide at source (Rule 17 dtype standardization), patch, suite, package for the V2-8 swap path.
0.7.0 convergent-flagged bd/allocations 'Flat Fee' + 'Account - Billing Discount Percentage'
pre-05:00Z (BD first real conversion). CTO posture 163047Z: land clean tonight if it lands,
else LET IT REFUSE -- audit uncompressed.

## Work Completed

1. **Full-vintage read-only audit** (scratchpad int64_audit.py, estate's own raw_json_reader --
   no second parse path): 576 eclipse files/ALL 48 date-dirs, ALL 254 BD xlsx (~4.1M rows),
   orion newest vintage per feed (1.39M txn rows; assets additionally exercised by 359 clean
   conversions). 88 int64 columns measured, 0 unmeasured, 0 container-in-scalar drift.
   FRACTIONAL: modelAUM 334/432, portfolios_full.contribution 63/40,899,
   portfolios_full.pendingValuePercent 4/40,899. Everything else integral -- including every
   semantically value-like candidate, which is exactly the state modelAUM was in on the 07-10
   generation census.
2. **12 declarations flipped int64->float64** @ 7724a02a3 (pushed): 3 evidence-forced + 9 by
   class (eclipse reserveCashTarget/Actual, cashOverage/+Percent, cashUnderage/+Percent;
   bd 'Flat Fee', 'Account - Billing Discount Percentage', 'Bond Duration'). Orion: zero
   value-like int64 (12 id/enum cols enumerated). TYPE LAW docstring amended: VALUE-SEMANTICS
   OVERRIDE -- whole-valued-on-a-vintage is not integer evidence; int64 = ids/codes/counts/flags
   ONLY.
3. **Regression test added** (test_no_value_like_column_declared_int64): token-wise value-like
   name match vs int64, allowlist for the 3 has* flags + allowlist-hygiene twin test. Its own
   first run false-positived on isComm*unit*yModel via raw substring match -- the INSTRUMENT was
   wrong and was fixed (token split), on the record.
4. **Suite 161/161 with ZERO skips**: rebuilt MIRROR_SAMPLES from landed monolith bytes
   (allocations 06-18 / unrealized 06-17 = the data-bearing vintages; 07-10 for the rest) so the
   real-bytes integration tier RAN: the live-refused 2026-07-10 eclipse date-unit now converts
   SIDECAR_RECONCILED all 4 feeds; orion assets + BD 5/5 no regression.
5. **Handoff**: 0.7.0 signaled (165821Z) -- re-vendor mirror_schemas.py x3 (verified all 3
   lambda copies byte-identical to OLD source pre-fix), refresh BUILD_MANIFESTs, stage the ONE
   both-families swap plan at CTO's gate; CTO closed-looped (165834Z). Path (a) tonight or (b)
   05:00Z loud-refuse fallback -- both CTO-accepted.
6. **Delta-4 same-day review ACCEPTED** (c36710809 + a58c19bfb rider; 0.6.2 wound down pre-send,
   reviewed proactively off the commit): runtime read whole (never-summed lane grouping,
   single-writer by construction, record-then-manifest-then-raise, RLD day-grain, loud shapeless
   refusal, unquote_plus); scope_from_key both-shapes-at-the-parser correct; vendored copy
   byte-identical by diff; 8 runtime tests ran green inside my 161 run. Closes my V2-8 review
   set 4/4. Also ACKed 0.6.2's rl* 2025-07-18 APPENDED pin finding (delta-5) + rld 2025-01-09
   shell design cell -- both CTO-gated; contract edit ready same-day on his word.

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| comp-pulse diff (auto, safe-commit) | 2 commits | REFLEX CLEAN x2 | measured, 1239 danger nodes |
| commit-gate.sh | mirror_schemas.py + test file | PASS (1 ruff E402 caught, fixed) | universal gate |
| pytest (full silver suite) | 161 tests + real bytes | PASS, 0 skips | integration tier live via rebuilt samples |

No comp-* graph runs beyond the auto hooks: the window's searches were single-known-file constant
reads (rail-checked inline) and operational S3 listing/head/download of measured artifacts; the
one estate search needed (fold locate, prior window) was comp-grep.

## MCP Traffic

4 in / 5 out significant: CTO dispatch + deadline posture (in) -> ACK + audit-complete close
(out); 0.7.0 BD flag (in) -> convergent ACK + package-ready handoff (out); 0.6.2 rl* FYI (in) ->
combined delta-4 ACCEPT + FYI ack (out); COO AoR ACK (in, prior thread, closed).

## Blockers

NONE self-actionable. Swap staging + gate = 0.7.0 + CTO; delta-5/shell ruling = CTO.

## Current State (zero-context handoff)

mirror_schemas.py @ 7724a02a3 (12 flips + override law + regression tests), pushed CLOUD. Vendored
lambda copies NOT yet re-vendored (0.7.0's leg, in flight). Eclipse backlog 48 date-dirs + BD
first fire 05:00Z convert on next sweep after swap. AoR trigger CONSUMED (prior log). V2-8 review
set 4/4 closed. Monitor bmremqr3j live; no crons.

## Next Steps

- MINE time-gated: **22:00Z ETF first bytes** -> contract rules 6-9 + V2-5 etf rows + ETF
  converter authoring. LAPTOP STAYS ON.
- [0.7.0_AE_CloudOps] re-vendor x3 + BUILD_MANIFEST refresh + ONE swap plan -> CTO gate;
  post-swap eclipse sweep = first live test of the other 3 feeds (pre-cleared by audit).
- [1.0.0_SA_CTO] swap gate; delta-5 rl* pin ruling + rld shell design cell (contract edit ready
  same-day on his word).
- [EVENT] joint AC-3 landed-silver reads with 0.7.0 when mirror fires convert for real.
