# DELL1 self-drive box -- ticks 248-249, 2026-10-21 ~16:53-17:19Z (delta: J123 closed on every leg; the Schwab-household word routed; the walk past half)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 17:19Z. Acked since tick 247: 9167, 9168, 9175, 9178, 9180, 9182, 9186.
- open_calls.json: 167 rows, 5 OPEN act rows: 89c9, ea86, 3bc7, 5013, 764b. CLOSED this span: 5956 (the name came from a legal
  read), f88e (the send went on Andrew's word).

## Acts and rulings
- **J123 (Jai's Opal dashboard login), CLOSED on every leg.** ADVI1 9167 and CRO 9168: the surname "Jai Mukraj" found in the Opal-tenant
  calendar invite (OCIO IC 2026-10-20 14:00Z) on the exact username; RULED: a legal gateway read of Opal's own records satisfies J1
  (order amended @f83e33639e; 5956 closed). CRO 9175: insert rc=0 17:00:49Z (opal-capital, internal, user, must-change, --no-ses),
  draft to Yang Liu 17:01:03Z unsent. ADVI1 9178: receipt, email-index Count 0 -> 1 at 17:01:10Z, proof VALID. **Andrew-direct at the
  CRO's terminal** ("confirm the login URL from the portal route config + once we know the account is good to go send the draft to
  yang"): routes /login and /forgot-password 200, rows live, email SENT 17:07:54Z (CRO 9182, record @2d614e8d18); J3 amended to
  record the authorized send @0dbb0b7cb4; f88e closed; ADVI1's receipt corrected (9186, @6e4afe17de). Unexercised: Jai's first
  sign-in through forgot-password. The 17:01Z draft stays in Drafts, unsent.
- **Andrew-direct via the CRO (9180, @4344f25452):** COO~P1 investigates read-only how households exist on the Schwab side (no
  household table in Schwab silver or bronze; Fidelity has 58 Groups): master->sub structure, the tcf/tcfx/tnn types, synthesis,
  reconciliation with Fidelity's Groups. Routed as the FIDSLVR attribution cell's input at L5; no PRD edit while 764b pends.
- **NFRA_FIDUPL:** FW-s-1 (api_walk.py) COMPLETE after REPAIR 1 (@ee0ce1136e, drained @9e1b18a592f); FW-s-2 released
  (@3fe25e5322). The Historical walk: position 56, prices 54, position_balance_fl 48 dates; runs 133 (past half way to the June floor).
- Push: HEAD 6e4afe17de on origin box/dell1 (ls-remote 17:18Z).

## Scope state
- **NFRA_FIDUPL:** FT-s-8, FU-s-11, FU-x-1, FV-s-3, FW-s-2 pending; rules ENABLED; the SPLIT unreachable until Groups exist.
- **NFRA_FIDSLVR:** PRD v0.3, L4-R WITHHELD on 764b. **ADVI_COTBOOKS:** PRD v0.5, L4-R on ea86. **AMGT_HARVST / MDPF_DEMQUE:**
  parked on Andrew's 14:5xZ word.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **764b:** confirm the four re-cut NFRA_FIDSLVR lines FWD-1..4 (spine :120-121; REC confirm as written).
- **ea86:** confirm ADVI_COTBOOKS v2's eight lines; a yes to REC 2 is a one-time exception to his no-BD rule for FWD-5/6.
- **Per-firm account Groups in Wealthscape** (ruling @4c536cb554). **89c9:** SOC2_MSLOGS re-derive (MFA).
- Housekeeping, not an act: the unsent 17:01Z draft to Yang Liu in his Drafts.

## Compiler Tools
- `list-objects-v2`; `prd-signoff.py status`; `open-calls.py close/list`; `git log`/`ls-remote`.
