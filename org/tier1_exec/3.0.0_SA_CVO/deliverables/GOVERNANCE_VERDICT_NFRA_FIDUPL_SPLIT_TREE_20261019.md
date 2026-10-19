# Governance verdict -- NFRA_FIDUPL: which tree may run the FWD-9 split

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO~DELL1, 2026-10-19 ~20:0xZ. Answers 1.0.0_SA_CTO~DELL1 msg 8506 (self-drive box tick 155; acked).
**Read:**
- the CRO's split research, `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261019_NFRA_FIDUPL_ACCOUNT_TXT_AND_FIRM_SPLIT.md`
  @8f127b8d2b (whole);
- CLAUDE.md section 5: "NEVER reference another firm's data from a pipeline tree -- BUCKET or KEY-PREFIX", with its gate
  `.tools/ds-precommit-check.py` `_CROSS_FIRM_FOREIGN_*`;
- section 2, on not adjudicating wider (if wider seems plausible, ASK);
- the six `ANDREW_DIRECT_20261019_19*` records on dell1 (tier1 CTO and CRO).

## Verdict: the REC's gate carve-out is REFUSED as a ruling; a no-carve-out path is named first

- **What the REC is.** The splitter would read the Inflection (Orion), Cottonwood (Black Diamond) and 49 Financial (Black Diamond) account
  columns into the `alongside` tree. Account numbers are firm-attributable identifiers, so they are client-confidential under R7 "at ANY
  grain". Three firms' prefixes read from one tree is the act the NEVER names. The proposed "umbrella" entry makes a standing exception
  to a section-5 hard stop.
- **Why it is not a CTO or CVO ruling.** Narrowing that NEVER is wider than any word on record:
  - The quoted words, "Alongside is the RIA under which 49 Financial, Inflection ... sit", are in none of the six Andrew-direct records on
    dell1 today (0 hits).
  - Even if recorded elsewhere, a description of how the firms are organised does not authorize relaxing the cross-firm gate.
  - So this is Andrew's to say (CLAUDE.md section 2: ASK).

## The order this verdict supports

1. **First, the path that needs no carve-out: Fidelity's own attribution.** The research names per-G-number account lists (s.3):
   `accountList.json` under each G number, about 31 calls inside the session the uploader already holds.
   - It attributes every account from the Alongside data itself, so the splitter reads no other firm's tree.
   - It covers the 3,589 accounts the crosswalk cannot reach, including 49 Financial's.
   - Andrew is already checking for a G-number selector. The authorized automated session can read the same thing without exporting.
2. **Only if Fidelity offers no per-G attribution: the crosswalk, on Andrew's word.** Put to him narrowly: may the `alongside` tree read
   the account-number column only (never values) of exactly {inflection, cottonwood, 49financial}? It writes each share only to
   `fidelity/<firm>/bronze`, and no child tree reads a sibling or `fidelity/alongside`. The REC's shape is sound once he says yes.
3. **Round 1 does not wait on either.** FWD-9 allows "any accounts no firm claims listed". Until (1) or (2) lands, the full pull stays
   staged under `fidelity/alongside`, which Andrew authorized at 19:05Z, and the split cell is held. Nothing else moves.

## Surfaced, not ruled

- The research itself already joined Orion and Black Diamond account numbers from three firms' silver to the Alongside staging, on dell1
  (s.2: 1,418 claimed, 0 conflicts). It was a read-only research act outside any pipeline tree, so it is not the NEVER's act. But its
  intermediate join output, wherever it was kept, should not persist as a cross-firm artifact. The CRO should say where it sits and
  delete it once the split is ruled.
- Inflection's Orion lists 980 Fidelity accounts, and 201 of them are missing from the Alongside file (cause unmeasured). The per-G lists
  in (1) would explain them.

-- 3.0.0_SA_CVO~DELL1
