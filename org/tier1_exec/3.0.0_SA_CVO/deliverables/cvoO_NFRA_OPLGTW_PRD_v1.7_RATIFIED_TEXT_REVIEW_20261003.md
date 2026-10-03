# NFRA_OPLGTW PRD v1.7 -- ratified-text review (3.0.0_SA_CVO~O, 2026-10-03 ~20:0xZ) -- SIGNED

**Asked:** `1.0.0_SA_CTO~O` msg 28977. PRD at `4cd951117f` (equal to HEAD): the v1.7 addendum, "C3 records the fourth
dataset, `dim_transaction`", written on this seat's finding in the OG-gw-2 half (@0cfe31652e).

**VERDICT: SIGNED.** The ratified ENDPOINT and CONTRACTS text, read together with the v1.7 addendum, is one consistent
text. Stamped at the ratified-text half hash `19fdaba050a3...`.

## What was checked

- **The 15 columns** the addendum names equal `fields.dim_transaction` in `org/standards/NFRA_OPLGTW_CONTRACT.json` at
  `af2d762970`, by a JSON-normalized diff against the deployed `c2f5d5a071`. Order and spelling agree, including
  `settlmnt_date` and `tran_srcde`.
- **The four data-readable prefixes** match the contract's `datasets` at `af2d762970`.
- **:37 and :309** are carried by the addendum exactly as it says. `:37` reads four from v1.7. `:309`, Menachem's
  proposal, stays at three, and adding the fourth to it is its own act.
- **Grants.** The addendum's "capability is not authorization" paragraph matches the OG-gw-2 half's W1 verbatim scope:
  ONE existing principal's grant under Andrew's 2026-09-30 word, "no other grant change". Every other
  `dim_transaction` grant needs his word.
  - The CTO's G1 (no round-15 cell writes a `dim_transaction` grant) is consistent with it.
  - FWD-9 stays DEFERRED.
- **ENDPOINT is unchanged**, which agrees with `prd-signoff status`.

## Finding -- an addendum's contract change does not move this half's hash

- `prd_signoff_lib.half_of_section` maps `## Canonical handoff` to the BRIEF half. Every addendum, v1.2 through v1.7,
  is a `###` subsection under that heading.
- So the ratified-text half hash is byte-identical across v1.6 -> v1.7 (`19fdaba050...` both), and `prd-signoff status`
  reads this half "current". The v1.7 change to C3 re-opened only the brief half (CRO, "text CHANGED since signed").
- Effect: a CONTRACTS change written as an addendum re-opens the ratified-text half only by human discipline, as the
  CTO did here by asking. The mechanism does not do it.
- Remedy, the CTO's choice (the PRD is that seat's, the library its owner's): write a contract-changing addendum into
  the CONTRACTS section in place, or map addendum subsections whose title names a C-clause to the ratified-text half.

-- 3.0.0_SA_CVO~O
