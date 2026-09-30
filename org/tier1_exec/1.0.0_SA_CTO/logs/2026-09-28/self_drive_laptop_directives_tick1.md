# /self-drive laptop directives -- tick 1 (2026-09-28 ~23:1xZ)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_230xZ_SELF_DRIVE_LAPTOP_FABRIC.md`
@`9549fd3b32`. Cron `f02c52db` (`13,43 * * * *`, session-only). **state: ARMED**

## Scope

- Device: laptop (agentbus inbound queue `sitez-to-laptop`). 9 of 15 live directives: D0 D2 D3 D8 D9 D10 D11 D13 D14.
- Projects: 43 in scope, 14 complete or closed; 55 open task orders (directives-check, 23:06Z).
- Inbox: 0 unread. Active commitments: 1 line in 24 h (`2.0.0_SA_COO~M` -> ~D, the Holdings shape it will serve).

## Sequence (`org/missions/SEQUENCE.yaml` @55903c6259, TRACK)

- CAPACITY: 4 live COO lanes (~D ~M ~P ~Y) vs cap 3 -- AT CAP; Andrew's "limit doesnt matter" covers the IRPT seating
  only, so no further COO seat is asked. Next slot, in order: MDPF_CANON -> MDPF_TAXSMA -> NFRA_MCPINDEX -> NFRA_OPLGTW
  -> LGIC_ENFORCE -> LGIC_CANON -> LGIC_LGCTFM -> ADVI_FIRMBKTS.
- IRPT_BCKEND (stage 0): EXECUTING, round 19 issued in four workstreams (~M 2, ~P 3, ~Y 2, ~E pending its carrier).
- DRIFT x2: NFRA_MCPINDEX and NFRA_OPLGTW -- the file says laptop, the register row says site-z; both are driven by
  the ~O fabric seats. UNREACHABLE from this driver (never cross a fabric); the file correction is the owning CTO's
  (`1.0.0_SA_CTO~O`).
- LANE-DARK READY-IDLE x5 (MDPF_TAXSMA ~T, LGIC_ENFORCE / LGIC_CANON / LGIC_LGCTFM ~G, MDPF_CANON): wait for a COO slot.

## Acts this tick

- **Fix @`44e3297751`:** `sequence-check.py` read IRPT_BCKEND v0.18 as WITHHELD (brief STALE) while `prd-signoff.py
  status` and the task-order gate read ADMITTED. It called `evaluate()` without the lib's file reader, the coo_lane,
  the designated signer or the CRO-written-brief admission. After the fix: IRPT_BCKEND ADMITTED; MDPF_CANON,
  LGIC_ENFORCE, ADVI_FIRMBKTS unchanged (controls).
- D10 (no members): the member-set gap routed to `0.0.0_AB_MSTR`.

## Open calls in scope

- Decided on REC today (Andrew): calls 1-3 of 22:19Z, and the all-firms holdings-based performance
  (`0b6f598df4`). Next act: the CRO's midstream brief (L1), then this seat's L4 addendum.
- At Andrew, not a decision this seat can close: the Schwab registration-code list for 49F (UIC-16). REC (a),
  the Schwab rep; the contact is his.

## Completion test

NOT DONE -- 14 of 43 projects complete or closed. D10 UNMEASURABLE (no members). REACHABLE from this fabric's seats
today: IRPT_BCKEND, DSGN_IRPTV1. The other open projects wait on a COO slot or on the ~O fabric.

## Compiler Tools

- `directives-check.py --json`: 15 live, 9 laptop. Worked.
- `sequence-check.py`: worked; its PRD reader disagreed with `prd-signoff.py` -- fixed (above).
- `active-commitments.py`: 1 line of 434 in 69 ledgers. Worked.
- Gap: none new.
