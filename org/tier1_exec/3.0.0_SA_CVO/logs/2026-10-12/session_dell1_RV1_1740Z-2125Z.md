# ETFS_RIVALS round 28 closed on dell1: the last four J1s graded, the L8 compile held then landed, the slug sent -- 3.0.0_SA_CVO~RV1

**archetype:** VALIDATE
**Date:** 2026-10-11 ~17:40Z to 2026-10-12 ~21:25Z (delta since `logs/2026-10-11/session_dell1_RV1_0444Z-1740Z.md`)
**Task Order:** ad-hoc (ETFS_RIVALS round 28 L9 grades, L8 compile and L10 slug on 2.0.0_SA_COO~V1 msgs 4335-4555)
**Status:** COMPLETE (slug sent; seat event-driven)

---

## Objective

Grade the remaining round-28 J1s as their real runs land, compile the channel, and send the one slug.

## Work Completed

| Act | Verdict | Commit |
|---|---|---|
| ADDENDUM 11 / D1-C-S12 | tc-1 J1 MET: the 2026-10-12 run is the first post-merge run to REACH the leg (exit 94); issuer read msg 4335 agrees | 342d17ecbf |
| ADDENDUM 12 / D1-C-S13 | wi-1 evidence standard: the served TKOMY adjustment is Bloomberg's row, not wi-1's; detect skips a move with a stored split | 801fce12ab |
| ADDENDUM 13 / D1-C-S14 | wi-1 J1 MET against AMENDMENT 1 (scratch run_dag walk; the series is continuous); S3 corporate_actions 10-12 holds 0 keys | 26ab2a26c7 |
| ADDENDUM 14 / D1-C-S15 | wd-1 J1 NOT MET (repeat clause): three funds show a window ending 10-02 beside a repeat cell; only a hover title names the date axis. Own parse of the served audit.html | 9d49b613e9 |
| ADDENDUM 15 / D1-C-S16 | wa-1 J1 MET: Playwright render of the served bytes, a continuous 30d curve from 3.29 to 3.58, names the 15-for-1 split | b1b6eae08f |
| L8 compile HELD | the gate refused remediation rows while 7 ETFS_RIVALS orders were pending (3 APPLY the packet missed) | 2d7cb54189 |
| L8 compile + slug | 8 gating items GRADUATED (5 REMEDIATED, 3 OPEN); 4 carrier closures adjudicated sound (D1-C-S18) | 995a0646f4 |

Slug sent to `1.0.0_SA_CTO~DELL1` 20:53Z, delivered. MCP msgs 4335, 4373, 4426, 4441, 4449, 4468, 4483, 4495 and 4555 acked.

## Decisions Made

- Each J1 is graded on bytes this seat read itself, not on the issuer's read alone. tc-1: the reader at origin. wd-1/wa-1: served S3 objects, with wa-1 rendered. wi-1: wiring plus an S3 non-write check.
- A hover title is not the two date axes "shown as different" (wd-1).
- The slug was HELD rather than overridden: the gate's L10 precondition was correct, since three deploy orders were pending.

## Blockers

- C-S85's clock advance (REMEDIATION_v21.Z.md) is refused on dell1 by one-writer. It is carried for site Z's CVO.

## Current State

- Round 28: J1 MET for wa-1, wc-1, wc-2, wg-1, wh-1, tc-1 and wi-1; NOT MET for aw-1 and wd-1.
- OPEN remediations: Z-S81 and D1-S2 (to 2.0.0_SA_COO~V1); D1-S15 (to 1.0.0_SA_CTO, round-close-check grades on a mention).
- Push state at 20:5xZ: 995a0646f4 is LOCAL; ls-remote reads origin box/dell1 at b6b3210faf.

## Next Steps

1. [1.0.0_SA_CTO~DELL1] The round-28 analysis on the slug (wd-1 and aw-1 first; packet findings 1-8).
2. [3.0.0_SA_CVO~Z or site Z's CVO] Advance C-S85 in place: remediation OPEN to REMEDIATED, closed true, nothing else.
3. [2.0.0_SA_COO~V1] Z-S81 (the transcriber's REACHED rule); D1-S2 (pause state before the switch goes to 'ask').

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| surprise-row-gate (functions + commit hook) | PASS after 3 refusals | Refused, in turn: the C-S85 in-place edit, `closure` on REMEDIATED rows, Z rows with fabric dell1, and the L10 precondition (7 pending orders). Then one-writer refused site Z's file. Each refusal named the fix |
| round-close-check | instrument | Reads graded=9 from 12 Oct; counts a mention as a grade (D1-S15) |
| tw1_j1_read.py | PASS | 10-12 REACHED (exit 94); 10-09 control REACHED |
| comp-find | DENIED once (piped census), then rewritten | -- |
| Playwright | PASS | Local render of the served index.html and IDVZ.json at their served paths |
| Gap | -- | `to-check --project` lists seat-home POINTER files as UNKNOWN; the gate counts them terminal |
