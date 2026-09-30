# Andrew-direct 2026-09-29 ~21:4xZ to 2.0.0_SA_COO~M -- the canonical table is not overwritten from bd-securities

Said at the 2.0.0_SA_COO~M terminal while ~M cut MDPF_SECCLASS round 1, verbatim:

> "Are we currently using bd-securities for all this? If so, and we are summarily going to be bringing everything into
> the canonical table, then something I want to make sure is clear, is that the canonical table should not be
> overwritten by anything in bd-securities."

## ~M's answer at the terminal

- Yes. The Black Diamond classifier (`data/black_diamond/scripts/gold/lib/etf_classifier.py`) scans `bd-securities`, and
  five BD scripts read through it. The IR Holdings producer does too until IRPT_BCKEND IB-mr-251 lands.
- The PRD's C-WRITER already binds the same way. Only the seed path and FWD-7's scheduled classification write
  `etf-classifications`. The scheduled write is conditional on the row's absence, so it cannot replace an existing row.
  `bd-securities` is read once as input and is never a writer.

## How it binds (scope: ~M's MDPF_SECCLASS cuts; relayed verbatim, not widened)

1. No value read from `bd-securities` replaces or edits an existing `etf-classifications` row, including GLD, PHYS and
   VXX. Mechanism: every scheduled write is a conditional put on the ticker's absence.
2. A `bd-securities` value enters the table only as a NEW row for a ticker the table lacks. It is listed per ticker in
   the backfill census for review before any write, and the first write rides a signed half.
3. Every round-1 order that writes, or builds a writer, carries a test that tries to overwrite GLD with the
   `bd-securities` value and must be refused.

~M asked Andrew at the terminal whether he meant something stricter (no `bd-securities` value entering the table at all,
even for an absent ticker). That reading is open until he answers, and the first write waits on it.

## Andrew's answer, 2026-09-30 ~02:2xZ, verbatim

> "yes, bd-securities values can seed new rows. THey just don't overwrite existing rows."

The open reading is closed. A `bd-securities` value may seed a NEW `etf-classifications` row for a ticker the table
lacks, and it never overwrites an existing row: the conditional put on absence, as built in TO-SC-k1. The backfill
write (MDPF_SECCLASS release step 2) is no longer held on this question. It proceeds under its never-widen halves.
