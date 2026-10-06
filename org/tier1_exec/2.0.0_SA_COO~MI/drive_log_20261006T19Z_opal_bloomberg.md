# /canonical-drive NFRA_MCPINDEX -- 2.0.0_SA_COO~MI -- 2026-10-06 19Z -> 20Z (host opal_bloomberg)

**archetype:** COORDINATE

Lease FULL. Round 7 at L7: 3 of 7 orders terminal.

## Decisions closed

- **Ticks 1-2 (19:1xZ, 19:21Z): NO-OP.** The CTO half for MX-s-17/s-18 was HELD @ba005db3b0 pending Andrew's scope word.
- **Andrew-direct ~19:4xZ, at this terminal:** "Yes we can consolidate writers. I need you to investigate first ..."
  - Record: `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261006_194xZ_BD_CONSOLIDATE_WRITERS_INVESTIGATE_SHAPE_FIRST_SEAT_AE_MI.md`
    @89ef943035.
  - Pointer sent to 1.0.0_SA_CTO~O.
- **MX-a-1 issued @89ef943035** to `0.7.0_AE_CloudOps~MI`: workstream BDOPS, read-only, risk SERVED.
  - Scope: the BD morning REST run's shape (transport, fields, BD-side as-of provenance) against the evening SSM
    documents, plus a verdict on whether the evening run is extraneous.
  - The one-issuance-per-round limb refused a second issuance and reads no override. The `<workstream>` element is
    its lawful route.
- **Issuer read before the cut:** the evening documents' repo JSON fetches nothing from BD. The Playwright download
  was removed after MFA (MX-s-14). They re-merge the morning bronze with `scripts/merge-daily-incremental.py`.
- **AE~MI seated.** Pre-flight: 0 claude.exe hits, 0 markers, 0 open orders, 14 of 20 windows. Launched 19:56Z and
  REGISTERED after ~55s. The GO pointer (msg 30259) was READ by the seat at 20:01Z.
- **Tick 4 (20:21Z): NO-OP.** The seat is 20 minutes into the read, with no commit yet.

## Open (each with its condition)

- **MX-a-1 verdict:** on the seat's report. Then the issuer rules MX-s-17 (likely superseded) and re-addresses the
  MX-s-18 deploy and the evening decommission (MX-s-19) under never-widen halves.
- **Decommission precondition:** the Mon/Tue gap closed first (MX-s-18 live).

## Compiler Tools

`safe-commit.sh`, `to-pipeline-gate.py` (one refusal, resolved by `<workstream>`), `to-check.py --all --assignee`,
`spawn-agent.ps1`, `get_delivery_state`.
