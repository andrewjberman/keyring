# NFRA_TRNSPT -- ruling: Alyssa's PRD-001 commentary work as a second source

Author `1.0.0_SA_CTO~DELL2`, 2026-10-07 ~15:3xZ. A design call, ruled after the CRO's research.

**Input:**
- Andrew-direct ~15:05Z (record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261007_151xZ_PRODUCT_ALYSSA_RECON_CIO_HUNT_COMMENTARY_SUBSTRATE_TOP3_AUTOMATION.md` @03f59dbbf4):
  "materials here which we are going to want to use, like the investment commentary database ... substrate that COO~T2 is going to
  need for their commentary work".
- The CRO's shape file `org/tier1_exec/4.0.0_SA_CRO/deliverables/PRD001_COMMENTARY_SHAPE_FOR_NFRA_TRNSPT_20261007.md` @6ec89a3194
  (msg 752).

## What exists (the CRO's measurement)

No commentary database has been built: 0 records. What exists is:
- a finder (`classify.py`, scored 170 of 183 on its own build set);
- a schema;
- one mock record;
- a labelled corpus of 183 emails (70 real commentaries, March-September 2026). It sits on Alyssa's laptop only, and it holds client
  PII by her statement.

## Ruling

1. **What Andrew's word is served by: the labelled corpus and the finder rules, as ground truth for C-CRITERION's precision.**
   - FWD-7's criterion is graded today on Andrew's mailbox alone (6 confirmed and about 13 probable of 18).
   - 70 positive and 113 negative labelled examples measure its precision and recall on a second population.
   - The corpus enters Opal only by Alyssa's act, on Andrew's word. It lands in bronze under C-READERS (two named readers) and passes
     the wipe before any silver use, like every other mail row. Until then the finder's RULES are read from SharePoint (no PII) and
     compared with C-CRITERION's tests.
2. **C-GOLD-FIELDS stands; no field is added now.**
   - **`approved`:** in PRD-001 this is Manav's no-edit reply to Alyssa's draft. That reply is an internal thread, outside
     C-CRITERION's scan of Manav's sent client mail. Adding the field means widening the scan, which is a new outcome on Andrew's
     word, not a field edit.
   - **`mention_rate` and `model_as_of`:** derivations the drafter may want. C-SLICE ranks on neither, so both wait for the FWD-10
     drafter round and are decided there against a real draft (build ladder rung 1).
3. **The hold-back rule** (the PDF goes to the client at once; the commentary follows only after Alyssa signs off) agrees with FWD-10
   ("the draft never reaches an advisor unless a person sends it"). No change.

## Placed

- `2.0.0_SA_COO~T2`:
  - item 1's finder-rules comparison may ride round 4 as a LOCAL cell at the issuer's choice;
  - the corpus landing waits on the act below.
- **For Andrew (an act only he can authorize; cross-person data movement of client PII):** his word for Alyssa to place her labelled
  corpus into the transcripts bronze tier.

-- 1.0.0_SA_CTO~DELL2
