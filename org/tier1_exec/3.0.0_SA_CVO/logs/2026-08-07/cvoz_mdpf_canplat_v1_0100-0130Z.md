# CVO~Z session log — MDPF_CANPLAT.V1: ad-hoc chain fired, rendered, re-pinned; routes validated

**archetype:** VALIDATE
**Seat:** `3.0.0_SA_CVO~Z` · **Window:** 2026-08-07 01:00–01:30Z
**TO:** `MDPF_CANPLAT.V1.routes-adhoc-baseline` (GO 01:00:49Z, ACKed 01:01:14Z) · V-PRD @2dedd8f6a

## V-2 (Andrew-direct "ad hoc run issued now") — full detail in `records/V2_ADHOC_CHAIN_RUN_20260807.md`

- Chain fired hop-by-hop in production order: hop-1 DESIGNED DEFERRAL (INF spine gate, trading-calendar
  correct); hop-2 SSM Success `written=0 skipped_existing=14 errors=0`; hop-3 publisher 14/14 published
  from frozen sources (2026-08-03/04). No IAM denial at this seat.
- V6 via my own R7 instrument: 12/12 pairs, 47,119 paths — the ONLY moved path anywhere is
  `_provenance.written_at`. Frozen-gold republish measured end-to-end, pre-ruled expected.
- V7: deployed bundle at opalinvest.dev rendered all four scopes with the VersionId-pinned bodies
  (fixture-fulfilled; the edge correctly 401s a stub session — authed leg COULD-NOT-VERIFY at this
  seat, 401 log = the edge-posture measurement). All four scopes render correctly; data-as-of 08-03
  recorded beside the verdict. Curve-at-global-only observation SURPRISE'd + triaged (today's live
  behavior, V3 not reopened).
- V8: **new pin `baseline_manifest_20260807T011035Z.json`, 14/14 @01:10:35Z** — supersedes 00:07:53Z
  as the R7 before-image per COO~Z's PIN-NOW guidance.

## V-1 — full detail in `records/V1_ROUTES_VALIDATION_20260807.md`

4 entries validated with targets RESOLVED to Active functions; V2 policies exact per principal+source;
V3 DLQ depth 0 + known mis-scope confirmed-as-recorded; V4 dead edge accelerator-only (last fired
07-30); V5 negatives with denominators (0 destinations across 3 mdpf functions of 196; 0 of 10 S3
notification configs touch gold/portal-gold/platinum). Frame delta recorded: V-PRD's "four MDPF
functions" vs 3 existing at 01:24Z (`mdpf-gold-lambda` not yet deployed).

## SURPRISE channel uses this window (all triaged same-hour by COO~Z)

1. 010342Z deferral-record AccessDenied (recorded, no action — dies with cutover).
2. 012053Z holdings curve draws at global only on populated histograms (recorded, V3 not reopened).

## Compiler Tools

| Tool | Call | Result |
|---|---|---|
| comp-which | "enumerate scheduler entries and rules touching mdpf" | routed comp-trigger (near-tie surfaced honestly) |
| comp-trigger | `mdpf` | 4-entry surface confirmed, denominator 139+16 printed, live fired-evidence 07-30 on the dead edge |
| comp-routes | `components` | resolved ModelPortfolios.tsx + its three per-firm API routes (V7 route map) |
| raw aws | invokes (operational) + policy reads (rail-checked, TO-legalized; live=APPLIED per Rule 22a) | chain fired; V2/V3 policies read on the live layer |
| R7 comparator (own instrument) | live vs 000753Z pin | V6 measured as a localised single-path diff per artifact |

Rail note: the HUD gated the first `get-policy` read; re-ran with `# rail-checked:` citing the TO's
explicit legalization — the audit trail carries the why.

## Errors of my own this window, on the record

1. Handed an MSYS-style path into native Python (`pathlib.Path('/c/...')`) — fixture write landed in a
   phantom `C:\c\` tree; caught by the comparator's COULD-NOT-VERIFY (which then also exposed that a
   CNV pair exited rc=0 — hardened to rc=3 in the same commit).
2. Two relative-path reads from a drifted CWD (portal/ residue) — both caught by the frame-check
   discipline banked earlier tonight (pwd + absolute anchors).

## Blockers

None at me. V9–V11 are DS~Z's; V-3 frontend-consumption analysis is routed elsewhere (curve datum
forwarded to CTO~Z by COO~Z for the goal-3 report).

## Next steps

1. **[3.0.0_SA_CVO~Z]** R7 same-data-day runs when P1-1/P1-2 candidates land, against the 011035Z pin.
2. **[3.0.0_SA_CVO~Z]** §B re-derive on any further CONTRACT amendment.

— 3.0.0_SA_CVO
