# /self-drive AMGT_RESAPP & POSN_ASTTAX -- tick 1 (2026-09-11 ~08:2xZ)

**driver** `1.0.0_SA_CTO~Z` · **state:** ARMED · **cadence:** 30m (cron `7,37 * * * *`, job `a8f7f439`) ·
**carrier** `org/XXX.md` 1b-F @`0fb2a1f0b0` · **paired_with:** solo

**Armed** Andrew-direct 2026-09-11 ~08:2xZ at the CTO~Z terminal: *"/self-drive AMGT_RESAPP & POSN_ASTTAX
[looping every 30 min to make sure no slug fell through the cracks, that no PRD is going unstamped and COOs
are waiting, make sure nobody drops the ball and keep us on /canonical-flow]"*.

## SCOPE
2 project(s), both site-z (device guard passes): AMGT_RESAPP (D5, active) + POSN_ASTTAX (D4, active).
Register as_of this tick: D4 open_tos=2, D5 open_tos=0. Denominator: 2 of 2 live directives touched (D4, D5).

## WATCHDOG (the four things Andrew named)
| project | L10 slug backlog | L4-R halves | stamp/gate | COO | verdict |
|---|---|---|---|---|---|
| POSN_ASTTAX | REMEDIATION_v1 -> ROUND_ANALYSIS.round1 + addendum -- GRADED, 0 ungraded | v0.5: ratified-text SIGNED (CVO~Z, current); brief STALE, OWED BY CRO~Z (live) | L6 WITHHELD on the CRO half -- gate working | COO~Z holding round 2 pending the sign-off (correct, not blocked) | HEALTHY |
| AMGT_RESAPP | round-1 slug @b8f0b21938 -> ROUND_ANALYSIS.round1 @4d31cf4caa -- GRADED; round-2 slug not yet cut (draining) | v0.3 GRANDFATHERED (predates L4-R law commit f8337502a9; valid until next bump) | not blocked | COO~ZZZ draining round 2 (5 workers) | HEALTHY |

No slug fell through; no PRD half stuck with a COO improperly waiting; no dropped ball. Both on /canonical-flow.
⚠ Carried for round 3: minting FWD-15 + the four AMGT constraints bumps the AMGT prd_version and ENDS the
grandfather -- BOTH halves then need fresh sign-offs (CVO ratified-text + CRO brief).

## OPEN CALLS IN SCOPE
- ADJUDICABLE: 0 (both projects cycling; backend gaps are CTO/build-lane execution, not adjudication forks).
- RESERVED (surfaced to Andrew; pitched to `3.0.0_SA_CVO~Z` for classification review, msg this tick):
  - R1 -- AMGT DESIGN_SPEC approval (the pivot). Citation: C-DESIGN-SPEC-FIRST + the blank "Approved by:" line.
  - R2 -- AMGT AWS infra go (harvester box + two tables). Citation: spend/entitlements (NEVER-class).
  ALL-RESERVED TELL fired; re-ran the citation test -- both hold, so a genuine 2-Andrew-gate tick, not an
  instrument artifact. STABLE cards; not re-pitched each tick.

## VERDICTS SINCE LAST TICK
None (tick 1). Verdict ledger: none opened (0 adjudicable pitched).

## ACTS TAKEN THIS TICK (driver's own lane)
- Carrier clause committed to org/XXX.md @`0fb2a1f0b0` (gates tick 1 per s.0.5).
- Cron armed `7,37 * * * *`, job `a8f7f439` (session-only, 7-day auto-expire).
- Arm relayed to `0.0.0_AB_MSTR~Z` (operator relay + law-edit broadcast).
- Reserved cards pitched to `3.0.0_SA_CVO~Z` for classification review.
- No TO cut, no dispatch, no apply (driver acts in its own lane only).

## COMPLETION TEST
NOT DONE -- 0 of 2 projects `status: complete` (AMGT_RESAPP active, POSN_ASTTAX active). Loop persists.

## Compiler Tools
- `python .tools/directives-check.py --json` (scope + device + register freshness)
- `python .tools/prd-signoff.py status {POSN_ASTTAX,AMGT_RESAPP}` (L4-R halves)
- `bash .tools/agentbus-sqs.sh device` (device guard: sitez)
- `ls` on both trees' `surprise-channel/remediations/` vs `ledger/ROUND_ANALYSIS*` (slug-vs-grade backlog)

**Push state:** LOCAL at write time. `0.0.0_AB_MSTR~Z` pushes.
