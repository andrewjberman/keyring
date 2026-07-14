# A_00 review fix + A-FAMILY APPROVAL COMPLETE (10:44-11:12Z)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

**Date:** 2026-07-14 (window since v28_converters_wave12_d1a.md @ 83d65033f, ~10:44Z)
**Task Orders:** CTO Wave-2 dispatch (093752Z) -- review-fix leg
**Status:** A-FAMILY APPROVAL COMPLETE (CTO 110236Z, 90f652d07 verified at source). Wave-2
authoring CLOSED. Event-driven idle on gates.

---

## Objective

Close CTO's A-family review items (104349Z: one required change + one contract item) and
complete the approval.

## Work Completed

1. **A_00 provenance-truth fix** @ 90f652d07: provenance now stamps TODAY'S rows BEFORE the
   absent-carry concat -- a carried row keeps its TRUE acc_as_of (last-seen partition) and its
   prior joindim vintages ride through from prev_dim. The review's core line ("a field that
   means the build's vintage on some rows and this row's data vintage on others is two numbers
   with one name") is the in-code comment on the stamp order.
2. **TTL-age surfacing implemented** at CTO's named home: `BuildReport.absent_over_ttl`
   (distinct field; D-group + C_04 summary read it) -- absences older than
   ABSENCE_TTL_TRADING_DAYS=5 surface with {account_id, absent_since, trading_days_absent},
   age via `lib/trading_calendar.trading_days_behind` (TRADING days, never wall-clock).
3. **Both ordered fixtures added, SHARP**: carried-row acc_as_of asserted == last-seen date
   and != build date; TTL ladder 07-07 latch -> 07-14 = 5 trading days across the weekend
   (exactly-at-TTL does NOT surface) -> 07-15 = 6 SURFACES exactly. Honesty note on the
   record: the first fixture draft carried unfalsifiable or-clauses (the
   instrument-that-cannot-fail class) -- self-caught and sharpened pre-commit. Suite 18/18.
4. **CTO verified at source and closed the approval** (110236Z): A_00 + A_01 + C_04 reviewed,
   fixed, 18/18; live runs stay on their stated gates (0.6.2 fact_acc + join dims) -- the
   design working, not a delay.

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| pytest (runners_49f fixtures) | 18 tests | PASS | incl. the two ordered review fixtures |
| commit-gate.sh (auto) | 90f652d07 | PASS | universal gate on the fix commit |

No comp-* graph runs: single-module fix inside a new (not-yet-consumed) gold script; the only
cross-module addition was lib/trading_calendar, the ONE ruled frontier definition (CLAUDE.md
NEVER#1), consumed read-only.

## MCP Traffic

2 in / 1 out significant: CTO A-family review (104349Z, in) -> re-flag w/ fix evidence
(110016Z, out) -> CTO APPROVAL COMPLETE (110236Z, in). Broker re-surfaces of already-handled
messages not counted (speed contract).

## Blockers

NONE self-actionable. All open threads externally gated: V2-8 artifact swap (0.7.0, on CTO
AC-3 signoff of my 101619Z expectation reports; 13:45Z fallback); Wave-2 live runs (0.6.2
fact_acc + join dims); D1 vehicle plan (0.7.0 drafting for CTO's gate).

## Current State (zero-context handoff)

Wave-2 A-group: data/assets/scripts/gold/runners_49f/{a00_dim_account,a01_dim_relationship,
c04_recon_guard}.py @ 90f652d07 -- reviewed, APPROVED-COMPLETE, 18/18, live-run-gated.
V2-8 mirror converters @ 8ed378e53+8e46370bf -- review-PASSED, awaiting 0.7.0's artifact swap.
Contract @ v1.2.1 (8ca0e0c59). Cert prep: orion/cottonwood/0824-ligament closed. Monitor
bvtqozoxc live. No crons.

## Next Steps

- [0.7.0_AE_CloudOps] artifact swap on CTO signoff; then joint read of 14:15Z/16:00Z landed
  silver vs my stated AC-3 expectations (LOCAL-vs-UTC listing discipline).
- MINE time-gated: 13:22Z AoR 164-movers re-measure (read the scheduled artifact, NEVER
  trigger one); 22:00Z ETF first bytes -> contract rules 6-9 + V2-5 etf rows + ETF converter
  authoring (ruling 26: schemas ground on landed bytes only).
- [0.6.2_AE_PartnerETL] fact_acc converter landing unlocks Wave-2 live runs; FAM/SLM reader
  diff same-day review when it comes.
