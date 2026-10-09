# ANDREW_DIRECT 2026-10-09 ~01:1xZ -- every queued open call carries its context and its recommendation

**Channel:** laptop terminal, in the 4.0.0_SA_CRO~B session. **Recorded by:** 4.0.0_SA_CRO~B, same turn.
**Parent order:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_000xZ_KEEP_WORK_DRIVING_OPEN_CALL_QUEUE_CROSS_ADJUDICATION_AND_NEXT_CALLS_ON_EMPTY_TICK.md`.

## Andrew's words, verbatim

~01:0xZ: > "Are the calls that collect actually have a description/context?"

~01:1xZ, answering the measured reply and its recommendation: > "yes, build the context and rec fields"

## What was measured and recommended

Of 34 queued rows across the four boxes' cluster copies: a one-line `subject` (median 99 characters), a REC only where the
asking seat packed it into the subject, the real context only in the `source` file; 3 of 34 sources were another seat's inbox
message on another box, unreadable from the adjudicating laptop. Built: `open-calls.py add` takes `--context` (2-3 lines: what
created the call, what it gates) and `--rec`, both required for a new `fork` (`--context` for an `act`); a source under
`org/mcp/inbox/` is refused; the scan file and the cluster cards print both. Rows written before the change carry neither and
read as before.
