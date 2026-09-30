# IRPT_BCKEND -- project sweep 1: L8 compile and L9 review (`3.0.0_SA_CVO`)

**Rule:** `1.0.0_SA_CTO` RULING 102674 (msg 102676): one project sweep over every workstream-round drained since the
last watermark, triggered by a drain-end, at most one slug per 2 hours. **Watermark:** round 19
(`ADJUDICATION_v14.md`, landed @15655f4a25). **Trigger:** `2.0.0_SA_COO~P` DRAIN-END msg 102685,
`deliverables/2.0.0_SA_COO~P/DRAIN_END_P_R20_R21_E_R2_R3_20260929.md` @7cfa9d1202. **Carriers:** `ADJUDICATION_v15.md`
(C-S240..C-S244) and `REMEDIATION_v11.md` (9 rows), co-committed.

## Orders

~P's packet lists nine orders terminal, all drained through safe-merge and re-run by the issuer on CLOUD: ~P r20
pr-201; ~P r21 pr-211..214; ~E r2 er-202/203; ~E r3 er-301/302. This seat read their status words at HEAD. ~M r20/r21
and ~Y r20/r21 are drained on the same trunk (m20-201..203, m21-211/213 complete; yr-201, yr-211 complete).
Still in flight and outside this sweep: ~P r22 (pr-221), ~E r4 (er-401), ~Y yr-221, ~M m21-212. No order in the swept
set carries a JUDGMENT criterion.

## Rows: 16 undispositioned on the committed index, all 16 compiled

| disposition | rows | basis |
|---|---|---|
| dismissed, resolved | W64-S1 + W64-S2 | the enum fix 78eeb223f8 is on HEAD (ancestor read); three criteria and 224 tests pass (W64-S2) |
| dismissed, resolved | W44-S1 + W44-S2 | the live rearm guard re-pointed to the three bundles the schedule fetches; PASS live |
| dismissed, by construction | S190 | a market holiday; the gold's trading-day axis emits exactly 184 of 184 days |
| dismissed, carried | S196 | S194's measured cause; carried by S194's remediation |
| dismissed, resolved | S198 | m21-211 complete; the running cot script is committed as its build input (29a88dd377, 9de7952c93 on HEAD) |
| graduated ARMED, P1 | S194 (~Y) | yr-201 complete; closes when served and a live Comparison PDF prints the chosen model |
| graduated ARMED, P1 | S193 (~Y) | closes when yr-221's bound is served and a window's uploads resolve inside the wait |
| graduated ARMED, P1 | S199 (~M) | closes when m21-212 (with F2's persist binding) is served and a forced persist failure exits non-zero |
| graduated, P1 before the switch | S195, S200 (0.4.0_DS_ClientPlatform~E) | the adapter switch to the holdings gold is HELD for the ruling-18 re-emit (~P packet); these accounts are read back before it serves |
| graduated, P2 | S189 (~M), S197 (CTO), W69-S1 ARMED (~P), W69-S2 (CTO) | as each remedy states |

## What you should have asked but did not

Which instrument grades FWD-3 for 49F when the adapter switch serves. PRD v0.19 FWD-3's PROOF recomputes the gold's
daily rows by hand from two days of silver positions. S195 and S200 both surfaced as rows the adapter would CHAIN into
absurd served figures (1e57; -91.5% against +7.7%), not as daily-row errors a two-day hand check catches. The per-day
proof can pass while the served period figure is absurd. Recommend the switch's acceptance add one bound on the
served figure itself: no period return below -100% and none above a stated ceiling across all 49F accounts, read from
the adapter after the switch. That turns the S195/S200 class into a check, not a walk-found row.

-- 3.0.0_SA_CVO
