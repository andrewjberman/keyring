# L4-R review, NFRA_OPLGTW PRD v3.15 (FWD-23, the full Schwab silver), ratified-text half -- REFUSE, one cure (3.0.0_SA_CVO~Z, 2026-10-21 ~14:0xZ)

**Asked by** `1.0.0_SA_CTO~Z` msgs 36278 and 36280, read. They are not acked: this seat's broker tools are disconnected, and
the ack lands when they reconnect.

**Bytes reviewed:**
- `git show 866ccad604` on the PRD (+69 -2), read whole: the FWD-23 ENDPOINT block and the v3.15 addendum (C2, C3, grants,
  rules that do not move). The PRD at HEAD equals the pin.
- `prd-signoff status`: the ratified-text half is STALE against ENDPOINT hash `18622a31f500`.
- My last stamp was at v3.1 (`95d985d1a5`). Everything between was CONTRACTS-side per its own commits, and the ENDPOINT moves
  only here.

## Sources read

- **Andrew-direct 2026-10-21:** `ANDREW_DIRECT_20261021_13xxZ_MENACHEM_ENTITLEMENTS_ALL_INDICES_ASSETS_AND_SCHWAB_CONFIRM_LIVENESS.md`,
  read whole.
  - The three quotations in FWD-23's SOURCE are verbatim.
  - Menachem as an `account_identity` holder rests on his words about Menachem: "it should have full table access for all
    schwab account silver tables". v2.0 item 1 requires exactly that, his own word for any principal beyond Andrew and
    Alyssa.
- **PRD v2.0 item 1:** `:810-819`, including `:815`, "A column whose class is not decided is forbidden."
- **The converter's pinned schema:** `data/assets/scripts/silver/schwab_schemas.py`. It carries:
  - `ssn_tin_number` (`:144`);
  - `mailing_address_line_1..3` (`:91-93`);
  - `email_address` (`:98`);
  - `phone_nbr` (`:99`) and `mobile_phone_number` (`:161`);
  - `date_of_birth` (`:155`).

## What is right

- His words are carried: every fact table, `fact_acc` and `fact_trn` named, find accounts by name and number, and list
  transactions by trade date.
- Fields are generated from the converter's pinned schemas, never typed.
- The proof is exercised per master and per table, with a direct-read row-count equality and a 0-read negative arm.
- One master per call, the A14 caps, C3 closure and the counts-only audit stay put.
- The reader IAM is named as its own never-widen act.

## Verdict: REFUSE

There is one cure, text-only.

### V1 (blocking): v3.15 drops v2.0's fail-closed rule for an unclassed column, and the silver carries a known instance

**What the text says now.**
- v2.0 item 1 (`:815`): "A column whose class is not decided is forbidden."
- v3.15 C2: "a column the print cannot class is shown to this seat before it ships."
- C1: "an undocumented column is SERVED". That is right for MEANING, but it now sits beside a class rule that no longer
  forbids.

**The known instance.**
- `date_of_birth` (`schwab_schemas.py:155`) is not a name or title field, so it is not `account_identity` as v2.0 defines
  it.
- It is not in the four forbidden classes either.
- Read as written, it is "shown to this seat" and then ships to three principals. Whether a client's date of birth is
  served is a personal-data call that is Andrew's. It is not this seat's, and it is not settled by "shown before it ships".

**The cure.**
1. **Keep v2.0's rule:** a column whose CLASS is not decided is FORBIDDEN, and its MEANING may still be undocumented.
2. **Name the build's class print as the gate.** It prints every silver column's class. An unclassed column is listed to
   this seat and to the CTO, and it stays forbidden until classed.
3. **Name `date_of_birth` as the known undecided column, and put it to Andrew as ONE open call.** He has said "full data";
   his 10-08 answer named only four exclusions.
4. **State that `mobile_phone_number` classes as `phone_number`,** beside `phone_nbr`, so both phone columns stay
   forbidden.

## Noted, not grounds

- **The four forbidden classes stand "until Andrew's word moves them".** His new words, "full data" and "the entire point",
  are general. His 10-08 answer named these four exclusions, so keeping them is faithful. If the CTO reads "full data" as
  plausibly wider, the same open call can carry the question.

## Not graded here

- The reader IAM (its own never-widen act).
- The per-firm client grant shape.
- Round 48's decomposition.

-- 3.0.0_SA_CVO~Z
