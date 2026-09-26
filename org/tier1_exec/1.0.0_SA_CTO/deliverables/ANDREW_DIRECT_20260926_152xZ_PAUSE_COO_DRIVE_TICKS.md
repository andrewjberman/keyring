# ANDREW-DIRECT 2026-09-26 ~15:2xZ -- pause COO drive ticks

**Channel:** the 1.0.0_SA_CTO terminal. **Recorded by:** 1.0.0_SA_CTO, the same turn.

## Verbatim

"i think we may want to have all COOs pause drive ticks while we get to the botom of this, at least COO~P ~M ~D"

## Scope as relayed

- **"all COOs":** the live COO seats on the laptop at 15:2xZ were 2.0.0_SA_COO~D, ~M, ~P and ~Y (`get_live_agents`,
  4 of 4). All four pause. ~P, ~M and ~D are named as the floor; ~Y is included under "all COOs".
- **"this":** the account-level versus client-level Performance design question (record
  `ANDREW_DIRECT_20260926_151xZ_PERFORMANCE_ACCOUNT_LEVEL_FRONTEND_ROUTES_CLOSER_TRACE.md`) and the hop-3 defects,
  while 4.0.0_SA_CRO's `/closer` traces run.

## What a pause means

- **Stops:** each COO stops its drive-tick loop (`/closer-drive` or `/canonical-drive`) and starts no new act.
- **Still done (NEVER #2, no half-landed act):** the in-flight safety closure.
  - 2.0.0_SA_COO~P deletes the window-2 principal and closes its ledger.
  - ~D's K6 read runs only if it is already in progress; otherwise it is skipped.
  - Any open deploy ledger is closed or left with its state stated.
- **Held:** the generate grant apply (CTO 101275) waits for the resume.
- **Unchanged:** the seats stay live and receive mail. The FAST leases stand.
- **Resume:** on Andrew's word, or when the CTO relays it after the traces land.
