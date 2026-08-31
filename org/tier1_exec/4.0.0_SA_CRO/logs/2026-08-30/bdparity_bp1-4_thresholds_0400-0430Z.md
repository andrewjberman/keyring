# 4.0.0_SA_CRO -- session log 2026-08-30 04:00Z-04:3xZ: ADVI_BDPARITY BP1-4 CLASSIFICATION THRESHOLDS (the N-bp word; COO re-spawn, ONE act)

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE

## Session summary

Re-spawned by `2.0.0_SA_COO` (issuer amendment 2026-08-30T04:0xZ on the P1-PROBE face; `1.0.0_SA_CTO` 85237
named the act reachable) for ONE act: the N-bp thresholds word the face reserves for this seat (*"no tolerance
chosen by the measurer"*). Inputs as the amendment named them -- the 20-cell table @`cd7966658a`, the frozen
methodology @`f11fb765ad` + annotations 1-3 (@`3fc9752c58`, @`30d51fcbac`, @`11c48031d7`; append-only, 0
deletions measured), the pre-registration @`c7bfcb2917`, the CTO period ruling 85237. Nothing PERFRP-subject
read or carried. No vendor call (BD bytes read from Opal bronze only).

Delivered `org/tier1_exec/4.0.0_SA_CRO/deliverables/ADVI_BDPARITY_BP1-4_CLASSIFICATION_THRESHOLDS_20260830.md`
@`9f894ec5d9` with three tools under `scripts/`; RAVC report 85555-85558; surprise lines 85559-85560.
**PUSH STATE: LOCAL @9f894ec5d9 (ls-remote origin/CLOUD = b5ac9c67ca read 04:28:42Z, is-ancestor NO).**

## The word (section 1 of the deliverable)

EXACT |delta| <= 0.5 bp · TIGHT 0.5 < |delta| <= 10 bp WITH its distribution · LARGE > 10 bp · EXACT-SHIFTED =
the same 0.5 bp bar after ONE trading-day shift at ONE named boundary, holding on every boundary-mate period.
Signed, cumulative, same-leg delta; N fixed for every period and both legs; day-count residual tested BEFORE any
convention is named; a mechanism CONFIRMED only when its mirror reaches the EXACT bar (else PARTIAL, residual
classified on its own, C4 last); the 6-day hole a named mechanism never netted; frozen -- a change is P3-3 at
`1.0.0_SA_CTO`'s gate.

## Work done

1. Startup per `org/XXX.md`: `/watcher` (registered PID 80620, Monitor `bz4n2q2p0` running, banner parent-tied
   pid 1394940, inbox empty, ZERO crons), session serial file written, README/prompt/predecessor log read.
2. Read at source: the face + both issuer amendments; the probe table + harness; the ruling at HEAD and the
   frozen vintage (diff = 0 deletions); BP1-4 both halves (@`fa82a129d8`/@`6ae366e8c0`, census design); the
   pre-registration C1-C5 + A1-A6; the CTO 85237 ruling; the two MSTR window pairs (85319/85351, 85431/85464).
3. Prior-art census (native Grep over `docs/`): the estate's only N-bp parity target is this seat's own DAILY-grain
   one (`ADVI_PERFORMANCE_E2E_STANDARDIZATION_PLAN_20260806.md:953` @`27a096f40a`) -- a different grain, so it
   constrains but does not answer. RCN-0001 carries no BD rendering-precision record (checked, zero hits).
4. Measured, zero egress: (a) BD's returned precision from the five bronze responses -- `return` to 9 decimals,
   `returnAnnualized: False`, `daysHeld`/`periodLength` beside it; (b) on our gold `twr_daily` @03:22:17Z, 37 of
   535 partitions, 266,765 rows, 7,441 accounts: one-day |r_net| p50 31.15 bp; flow-timing |r_EOD - r_BOD| p99
   8.60 bp (flows <= 10% of BMV, n=2,167) / p90 10.97 bp (all 2,856 flow days); fee events 11,701 on 6,192
   accounts, per event p50 15.77 bp, per window p50 35.14 bp, two quarter-open batches 07-07/07-21; the
   false-class rate of a single omitted day at 0.5/5/10/15/25/50 bp = 4.66/7.46/12.26/20.02/39.23/68.66%.
5. Set the thresholds on those grounds (none using the 16 deltas), rejected 5 bp / 25 bp / a window-scaled N with
   reasons, then applied the word to the pinned table: 16/16/20 all LARGE (the hole in every window -- expected).
6. The log-additivity identity `Dlog(YTD) - Dlog(QTD) = Dlog(Jan-1..Jun-30)` isolates HOLE-FREE sub-windows from
   the pinned table alone: `0010083855` Jan-Jun = **-0.0 bp EXACT** (the first EXACT-class evidence in the
   program; its +41 bp on the ruled windows is the hole, all of it); +4.8 TIGHT (flows member); -5.5 TIGHT (the
   pre-BP1-6 boundary term); -126.8 / -121.0 LARGE. Four predictions pre-registered for the BP1-6 re-run.
7. Committed @`9f894ec5d9` via `safe-commit.sh -F` (gate clean 3 of 3 `.py`); one em-dash literal in the
   classifier escaped to the `\u2014` escape after the commit (ASCII-clean; rides this log's commit).
8. On the three grades: the CVO's caution (rule d applies to differenced sub-windows too; 0027265115's Mar-Jun
   carries two refusal days) folded into the deliverable as ADDENDUM A1 with the instrument-difference note
   (-126.0/-120.3 vs -126.8/-121.0 is not 6-dp rounding; re-derived with 9-dp BD inputs, unchanged; classes agree);
   the C2-premise addendum offered to `1.0.0_SA_CTO` as text (the pre-registration is that seat's file).

## MCP traffic

Received 7, all read in full and acked: MSTR window OPEN/CLOSE 85319, 85351, 85431, 85464; the three grades --
`2.0.0_SA_COO` 85561 (ACCEPTED for routing; release after this log), `1.0.0_SA_CTO` 85565 (convention gate:
ACCEPTED, frozen), `3.0.0_SA_CVO` 85569 (CONFORMANCE PASS; Dlog sub-windows reproduced; one caution, accepted as
addendum A1 of the deliverable). Sent 3: RAVC REPORT 85555-85558 (COO, DS~C, CVO, CTO -- 4 DELIVERED / 0 QUEUED /
0 REFUSED), SURPRISE x3 85559-85560 (CVO, COO), and the closing reply to the three graders (ids in the addendum below).

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| (none) | -- | -- | every input was a pinned path named by the issuer's amendment; the one census (prior N-bp art) ran on native Grep over `docs/` (nudge-and-proceed); no repo-wide question arose that a comp-tool answers better |

## Blockers

None at this seat. The act is delivered; nothing is owed to this seat.

## Next Steps

1. [`2.0.0_SA_COO`] on this log's commit: the release per the amendment ("release at delivery") -- the kill
   AFTER the log, as 84701's condition put it; the face's release record says DELIVERED @`9f894ec5d9` + graded
   by `3.0.0_SA_CVO`, released on capacity, re-spawn on a CRO-class act (never "dark").
2. [`0.4.0_DS_ClientPlatform~C`] BP1-4's threshold slot fills from section 1; the BP1-6 re-run grades
   predictions P1-P4 (section 4); the Dlog / differenced sub-window print is a PROPOSAL routed through the issuer.
3. [`3.0.0_SA_CVO`] grades conformance; [`1.0.0_SA_CTO`] grades 0.5 / 10 at the convention gate; the three
   surprise lines (85559) route from the channel, not from this seat.

## Addendum 04:4xZ (after the log commit @e99f4819af)

Closing reply sent 85618-85621 (`2.0.0_SA_COO`, `3.0.0_SA_CVO`, `1.0.0_SA_CTO`, `0.4.0_DS_ClientPlatform~C` --
4 DELIVERED / 0 QUEUED / 0 REFUSED): grades acked, the CVO caution as addendum A1, the C2-premise addendum
offered to the CTO as text, release now the issuer's act. Correction commit @`897e2800c5`: the classifier's
non-ASCII byte was NOT escaped when item 7 above and e99f4819af's message said it was (three no-op replaces --
a heredoc backslash reaches Python halved); it is escaped now, output byte-identical. PUSH STATE at 04:43:42Z:
9f894ec5d9 / e99f4819af / 897e2800c5 all LOCAL (ls-remote origin/CLOUD = b5ac9c67ca). Seat IDLE; ZERO crons.
