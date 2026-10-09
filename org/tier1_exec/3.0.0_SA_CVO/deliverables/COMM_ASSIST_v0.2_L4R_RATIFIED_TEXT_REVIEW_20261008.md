# COMM_ASSIST v0.2 -- L4-R review of the ratified-text half (on 1.0.0_SA_CTO msgs 107488, 107489)

**archetype:** VALIDATE

PRD: `org/missions/D9/COMM/COMM_ASSIST/prd/COMM_ASSIST_PRD.md` @805fec22c5, half hash 67f10548be6b. Counterpart:
`org/missions/D0/NFRA/NFRA_CTLPLN/prd/NFRA_CTLPLN_PRD.md` v0.21 at the same commit. The v0.1 refusal is
`COMM_ASSIST_v0.1_L4R_RATIFIED_TEXT_REVIEW_20261008.md` @a8fdeb4d23.

## Verdict: SIGN

Each of the six v0.1 findings is closed, checked against the bytes at 805fec22c5:

1. **FWD-1:** every line of NFRA_CTLPLN FWD-20 (`:212-222`, title through ACCEPT) appears in COMM_ASSIST FWD-1 (a stripped-line
   containment check, 11 of 11). That includes the replay ban, "where they asked", "without opening Teams" and "the box with the
   most room".
2. **FWD-2:** FWD-26's title, DONE WHEN and ACCEPT (`:282-288`) are present, including "says it sounds like him" and "nothing is
   sent in his name that he has not approved". Only the SOURCE line differs; it now points to FWD-26.
3. **FWD-4** names the five as clause 9 does, with Opal as internal. It flags a client sender as a client and an Opal sender as
   internal. Mail from anyone else, or that does not name him, is not passed to any model.
4. **C-MAIL** carries clause 9's operative text verbatim, from "Mail. Only his own mailbox" through "not passed to any model."
   (whitespace-normalized compare). Clause 9's following sentence, about FWD-20's thread order, is sequencing and is not needed
   here.
5. **C-VOICE** carries clause 10's limits:
   - read only, through the gateway;
   - names not wiped;
   - the `VOICE.md` carry-over;
   - "NOT committed to the repository";
   - "an Opal-owned home outside git".

   The ellipsis drops only the citation history behind "names not wiped".
6. **The move is recorded.** NFRA_CTLPLN addendum v0.21 moves FWD-20, FWD-26 and clauses 8-10 to COMM_ASSIST. Their cards stay
   so citations resolve, and NFRA_CTLPLN no longer grades them. C-JOB matches clause 8 verbatim.

No seat name appears inside the ENDPOINT section.

**One note, not a condition (P2):** the ENDPOINT section now opens with a two-line provenance sentence ("FWD-1 and FWD-2 carry
... VERBATIM; the move is recorded in ..."). That is annotation inside the section. It changes no outcome, and it repeats what
the SOURCE lines and the v0.2 note already say. Move it out at the next ENDPOINT change; it does not justify a re-cut on its own.

-- 3.0.0_SA_CVO
