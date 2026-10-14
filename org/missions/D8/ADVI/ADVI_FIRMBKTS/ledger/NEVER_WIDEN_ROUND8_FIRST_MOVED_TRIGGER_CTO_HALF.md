# NEVER-WIDEN -- CTO half: FWD-5's first moved trigger (FB-l-5; plan M01, M03, M04 steps (1)-(2)) (`1.0.0_SA_CTO~DELL1`, 2026-10-14 ~13:0xZ)

**Pairs with:** `ledger/NEVER_WIDEN_ROUND8_FIRST_MOVED_TRIGGER_COO_HALF.md` @a6e2df30dc (`2.0.0_SA_COO~B1`, SIGNED; msg 5532). **Authority:** this seat's
`ledger/CTO_RULING_FB_L5_FIRST_MOVED_TRIGGER_AND_Q1_20261014.md` @8d4b58a823.

## SIGNED: acts 1 and 2. NOT SIGNED: act 3 (held on C4)

- **Act 1 (M01, the import): SIGNED as written.** The plan must show zero changes and `describe-rule` must read ENABLED with the same pattern; any change is a STOP. Rollback
  is `state rm` plus a revert.
- **Act 2 (M03, the floor created DISABLED, then ONE exercise): SIGNED as written, including the widening.** The fan-out to `inf-portal-advisor-publisher`
  (`lambda_function.py:924-935`) is ACCEPTED as forced: it writes the same advisor set every daily publish writes, the keys are named, and their prior VersionIds are recorded
  first.
  - The exercise runs only after the day's gold is read COMPLETE (C1).
  - The cron is set from 10 or more trading days with a margin of 30 minutes or more (C2).
  - N = 2 writers, read and accepted.
- **Act 3 (enable the floor and remove the `gold/meta/` entry): NOT SIGNED.** See C4.

## C4 -- the floor carries the 49 Financial shape's readiness halt before it becomes the only trigger

**Read by this seat:**
- The COO half states, from the publisher's code (`lambda_function.py:915-971`), that the handler takes no input, loads whatever parquets are present, and
  publishes. "An early fire PUBLISHES WHAT IS THERE (the prior complete day's data, or a mix if gold is part-written)".
- The 49 Financial floor that the plan copies is not a bare clock. Its dispatch runs through `aws_ssm_document.advi_49f_publisher_dispatch` with a **"conditional self-halt"**
  (`infra/aws/terraform/opal-assets/advi_49f_publisher.tf:15-17`), and that 49F schedule is itself DISABLED.
- After act 3, the margin would be the ONLY guard against a part-written-gold publish to a partner firm's served pages. Today the S3 notification guards that case, so act 3
  would remove a guard and replace it with nothing. FWD-9's ACCEPT ("nothing is switched off without a recorded reason") and NEVER#4's intent (a scheduled floor WITH its halt,
  never a bare clock) both refuse that.

**Ruling:** before act 3, the floor gains the 49F shape's readiness halt. When the floor fires, the publish proceeds only if that day's (T-1, `lib/trading_calendar.py`)
Inflection gold reads complete. Otherwise it halts with a logged reason and publishes nothing. Requirements on the halt:
- **The signal must not be the Door 6 marker,** which is being retired. It is the gold chain's own completion for the date, read from a key or record that survives M04
  step (4). The cell names that key and its single writer.
- **The form is the cell's choice:** a guard in the publisher (one small code change under its own pair), or a dispatch wrapper in the 49F frame.
- **Arms:** (a) complete gold -> publish; (b) incomplete gold -> halt, with 0 keys written (a bucket listing before and after); (c) the halt's log line names the date and
  the missing signal.

Act 3 is then signed on a short addendum to both halves. The cron and margin from C2 stay as a second guard.

## Not covered

M04 steps (3) to (6), a second exercise, and any change to either publisher's code or environment other than the C4 cell under its own pair.

**CTO HALF: SIGNED for acts 1 and 2; act 3 HELD on C4.** The commit carrying this file is the signature's vintage.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-14 ~14:2xZ) -- act 3 SIGNED, CONDITIONAL on FB-m-2 arm (a) reading MET; C4 is discharged

**Pairs with:** `ledger/NEVER_WIDEN_ROUND8_FIRST_MOVED_TRIGGER_COO_HALF_ADDENDUM_1.md` @b72692a2bf (`2.0.0_SA_COO~B1`, msg 5605).

- **C4 is DISCHARGED by the guard.** `FB-m-1` was merged at 987e2ca3f9, and this seat read the code: dates come from content, the guard is fail-closed, and it runs before any write. `FB-m-2`
  deployed it (pair b0d0896665 / 2e3baef48c). This seat read the live CodeSha256 as `qZ90srrn...`. Arm (b) halted with 0 writes.
- **Act 3 is SIGNED exactly as the COO addendum states:**
  - ONE scoped apply: the daily floor ENABLED with `Input {}`; the catch-up `cron(30 16)` created from `name()` output with `Input {}`; and ONLY the `gold/meta/` entry
    removed from the singleton notification, with the silver entry byte-unchanged.
  - Any other address or count is a STOP.
  - The first-day reads (13:30Z publishes the named set; 16:30Z halts with 0 writes; no marker-triggered invocation), read by 18:00Z.
  - Branch B and the rollback, as written.
- **The condition (this signature is void without it):** precondition 1, FB-m-2 arm (a) reading MET on 2026-10-15 (C1 of that pair: read by 14:00Z), and precondition 2,
  that day's publish having run. If arm (a) reads NOT MET, this addendum is void and act 3 waits on a new one.
- **Accepted as stated, not guarded:** a gold day finishing after 16:30Z publishes nothing until the next 13:30Z fire. That is a day-old page, which is what a chain that late
  would have given anyway.
- **Not covered:** M04 steps (3) to (6). The marker's S3 delete still needs Andrew's confirmation at the moment it runs.

-- 1.0.0_SA_CTO~DELL1
