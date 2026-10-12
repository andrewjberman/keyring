# L4-R re-read, MDPF_SECCLASS and MDPF_SECHIST ratified-text halves, after Site Z's D2-S83 fix (3.0.0_SA_CVO, dell1, 2026-10-11 ~21:5xZ)

**Ask:** `1.0.0_SA_CTO~DELL1` msg 4131. Site Z's `prd_signoff_lib.py` fix @41b9fa7e01 hashes ENDPOINT/CONTRACT addenda into the
ratified-text half. It is NOT yet on box/dell1 (`merge-base --is-ancestor 41b9fa7e01 HEAD` false at 21:4xZ). Under dell1's library both
halves read SIGNED and current, so a stamp today would bind the OLD hash.

**Instrument:** this seat loaded `git show 41b9fa7e01:.tools/prd_signoff_lib.py` from scratch and hashed both PRDs at box/dell1 HEAD:
- MDPF_SECCLASS v0.16: new-lib ratified-text 8e1045ea9bdb8ea7..., ENDPOINT 8eb619c4748e14ef...
- MDPF_SECHIST v0.3: new-lib ratified-text 084e3a429e89f83a..., ENDPOINT e018e044ae2ac00b...

## MDPF_SECCLASS -- re-read: SIGN when the library lands

The last stamp was at v0.13 (2026-10-07T11:18:39Z). The new library adds three later sections, read whole here:
- **v0.14:** C-BOUND. The sub-class `Cash` belongs to `cash` only, and the canonical CASH row is corrected through its own pair.
- **v0.15:** C-CASH-TOKEN, on Andrew's verbatim word (record @fa8d7d1cf7). The token rule fills the TABLE only, and FWD-13 still binds
  the screens.
- **v0.16:** narrows v0.15's name leg to an allowlist of whole normalized names, on row W47-S1 ("Cash Flow Dividend Fund" is equity).
  The ticker leg is unchanged, neither leg overrides a seed or canonical row, and the test pins three negatives.

All three are contract notes, and each states that the ENDPOINT section is not edited. No outcome is narrowed,
and v0.16 moves in the safer direction (a blank over a wrong class).

## MDPF_SECHIST -- re-read: SIGN when the library lands (formality)

The last stamp was at v0.3 (2026-10-09T16:14:17Z). The only section the new library newly assigns to ratified-text is ADDENDUM v0.2
(Yahoo Finance admitted as a second price source), and it was in the bytes stamped at v0.3. ADDENDUM v0.3 itself reads `brief` under the
new library. Nothing unreviewed moved.

## Parked

OWNER: `3.0.0_SA_CVO`. UN-PARKS ON: 41b9fa7e01 an ancestor of box/dell1 HEAD. THEN: `prd-signoff.py sign <CODE> --half ratified-text
--review <this file>@<pin> --expect-half-hash <the new-lib hash printed by status>` for each, after checking that the hash equals the one
above (or re-reading whatever moved). Nothing is withheld meanwhile (CTO msg 4131).

-- 3.0.0_SA_CVO
