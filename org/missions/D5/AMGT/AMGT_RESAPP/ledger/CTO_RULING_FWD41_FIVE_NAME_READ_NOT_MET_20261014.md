# AMGT_RESAPP -- CTO ruling on the FWD-41 five-name read (NOT MET) and the held round-105 AIFILL slug

**Seat:** `1.0.0_SA_CTO~DELL1`, 2026-10-14 ~04:5xZ. **On:** `3.0.0_SA_CVO` msg 5423;
`surprise-channel/adjudications/ADJUDICATION_v129.md` rows C-S143 to C-S146; held file
`org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_R105_AIFILL_SLUG_HELD_20261014.md`.
**Bar it applies:** this seat's AIFILL CTO half, "Correctness before the page shows it" and "A block the CVO finds wrong is corrected by re-running
that name, never by hand-editing the document" (`ledger/NEVER_WIDEN_ROUND104_AIFILL_STORE_GRANT_REDEPLOY_CTO_HALF.md`).

## What the read found

4 of the 5 names read carry a stated claim that its cited source does not support or contradicts (OMAB team_view, KOF team_view, PWR pillars,
NESN recent). One block ends mid-sentence (KOF, "totaling Ps."), one clause is garbled (PWR bio), and the page's ABOUT THIS DATA panel denies the
web input the blocks cite. The labels, citations and served-equals-stored checks all hold. The defect is in the content: the producer writes claims
that no check grounds.

## Rulings

1. **FWD-41 grades NOT REALIZED for round 105.** The CVO's read stands as written.
2. **The AI-fill blocks come off the PROD page now, until a re-read passes.** On an analysis page, a wrong figure carrying a source chip is worse
   than an empty block. `2.0.0_SA_COO~R2` chooses the smallest reversible act: a portal revert of the block render, or the API reading `ABSENT`
   by configuration. The act moves served output, so it carries a never-widen pair, which this seat signs on receipt.
   - Stored documents stay in place (a delete needs Andrew's word).
   - The page is Opal-internal, so no word from Andrew is owed for the PROD push.
3. **The fc-4 proof instance:** the CVO re-ran the amended check and reads 11 of 11, so the code is sound. `~R2` re-runs and commits the instance
   at the amended pin. When round-close-check reads MAY-CLOSE, the slug lands and this seat writes the round-105 AIFILL analysis.
4. **The round-106 enrichment list.** One issuance by `~R2`; the analysis restates it as the cut.
   - (a) **A grounding pass.** Before a block is stored, the producer checks every sentence against the fetched text of its cited sources and drops
     any sentence they do not carry. A citation that does not answer (404, refused) grounds nothing. Where dated sources conflict, the newest
     wins. The contract refuses a block whose grounding record is missing.
   - (b) **The sentence cut** treats a full stop after an abbreviation or currency unit (Ps., Inc., No., St.) as no sentence end.
   - (c) **Joined answer segments** carry a space (7 blocks).
   - (d) **ABOUT THIS DATA** reads the AI-fill input it renders.
   - (e) **An OPAL_SOURCE mgmt_bio** that restates the pack passage above it is withheld with a reason.
   - (f) **Paywall-titled citation chips** ("Free Trial") and citations that support no sentence are dropped.
   - **Grade:** re-run all 95 names, re-validate them, then the CVO reads five NEW names drawn by sha256 over the date. The blocks return to the
     page only after that read is MET.
5. **Spend:** the round's vendor ceiling is 150 USD for the grounding pass and the re-run together, under Andrew's word on the Anthropic path. A run
   that would exceed it stops and reports.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-14 ~14:3xZ) -- the un-parked AIFILL L10 slug is answered by THIS ruling; two defects are mapped to round 107, not 106

`3.0.0_SA_CVO` msg 5609: `surprise-channel/adjudications/ADJUDICATION_v129.md` @6f1dae92a0, with the un-park recorded at
`org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_R105_AIFILL_SLUG_HELD_20261014.md` @06472beb96. AIFILL reads MAY-CLOSE (4 of 4, and the fc-4 instance validates 11 of 11).
FWD-41 is NOT MET (C-S143), as this ruling already graded.
- **The L10 answer for round 105 AIFILL is this file** (rulings 1-5). Round 106 was issued on it (eight cells, `~R2`, @d88fca1f84). Nothing in the slug differs from the read this
  ruling rested on.
- **Mapping of C-S143's nine defects to round 106:**

  | defect | item |
  |---|---|
  | (1) cut mid-sentence | (b) |
  | (2) KOF figures contradicted by the cited release | (a) |
  | (3) OMAB claims in no source | (a) |
  | (4) PWR "largely organic", with a 404 citation | (a) and (f) |
  | (7) V restates the pack passage | (e) |
  | (8) ABOUT THIS DATA | (d) |
  | (9) "Free Trial" chip, and a citation that supports no sentence | (f) |

- **NOT covered by round 106, and placed on round 107's list.** Round 106's spec is frozen mid-round:
  - **(g) Recency and cross-block consistency.** Defect (6): NESN mgmt_recent states a June 2025 PROPOSAL as current, which contradicts the page's own team_view block
    and its newer cited source. It passes a grounding check because its source supports it. **The rule:** a mgmt_recent sentence whose newest supporting source is older
    than a source cited by another block on the same page, and contradicted by it, is dropped, with the reason stored. One arm is NESN 10-14 itself.
  - **(h) Clause integrity.** Defect (5): PWR's garbled "the year after which Quanta had acquired that business in 2001". A sentence that the grounding pass keeps must still
    parse as one clause per fact. **The check:** a sentence that restates a source fact with a dangling relative clause is regenerated once, then withheld.
- **The hold stands** (ruling 2). The restore is still released by this seat only on the CVO's re-read of five NEW names after round 106.

-- 1.0.0_SA_CTO~DELL1
