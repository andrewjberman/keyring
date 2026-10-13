# NFRA_DEVPLN -- ROUND-2 ANALYSIS (1.0.0_SA_CTO, 2026-10-13 ~21:4xZ)

**On:**
- the CVO's L10 slug `surprise-channel/adjudications/ADJUDICATION_v2.md` @ba5474825a (watermark 21:39Z; 5 rows dismissed, 0
  graduate, 0 ARMED; PROD read independently);
- the issuer's drain end `org/tier1_exec/2.0.0_SA_COO~DV/deliverables/NFRA_DEVPLN_ROUND2_DRAIN_END_20261013.md` (3 of 3 orders,
  MAY-CLOSE).

**PRD:** v0.3, unchanged. **Next:** round 3, cut by `2.0.0_SA_COO~DV` in ONE issuance on section 3.

## 1. The thread ran end to end

FWD-1's journey ran for real, hops 3 to 7, on `cand/laptop/contributing-boxes`:
1. Approved by this seat (row 9e8a).
2. Merged forward onto DEV by the integrator as a two-parent merge with both trailers (`24877b67`).
3. Promoted alone by the DT's chosen-set build (PROD `10e7664d`, CI `38466864693` success, tag `portal-v2.1.214`).
4. Read on PROD.

The CVO read independently that PROD gained exactly one file and that none of the 7 unapproved dell2 DEV commits reached PROD.

**Grade reads named for the CVO, not graded here:**
- FWD-1 (the journey);
- FWD-2's approve arm;
- FWD-4 (`portal-dev-approval-read.py` on the real portal);
- FWD-5 (a chosen set shipped and left unapproved work behind).

**FWD-1 caveat:** the feature is a docs file, not a page a client opens. FWD-1's client-facing case is round 3's dell2 feature
(section 3, item 3). FWD-1 is not counted REALIZED until that runs.

## 2. Rulings

- **The nine branches (issuer's change accepted).** My round-1 ruling called five branches "contained in the trunk". The issuer
  measured them as patch-equivalent, not ancestors. It tagged each tip `archive/devpln-20261013/<branch>` on origin, read each
  tag against its tip, then deleted the branch. That is the right act: nothing is lost and each branch restores from its tag. The
  three IRPT branches went to `1.0.0_SA_CTO~DELL2`, and the DSGN_IRPTV1 branch is held.
- **The three dell2 ANLREQ merges on DEV** (call `bb8b`) and **the dell2 feature** (call `7d95`) are ruled
  (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_20261013_213xZ_LAPTOP_E846_7D95_BB8B.md`). IRPT_ANLREQ is not parked. Its
  next page change goes through the route. The three merges are re-registered as approval rows for Andrew, with the DEV-overlap
  refusal waived for those three shas only.
- **The declined row `e89f`** is CLOSED declined (`DECLINE_20261013_213xZ_DEVPLN_CAND_LAPTOP_DECLINED_EXAMPLE.md`).

## 3. ENRICHMENT LIST for round 3 (thread-breaking first)

1. **S03, the gate edit, by this seat** (`.tools/hooks/never-rules-gate.sh` portal DEV and PROD limbs). It lands before the round-3
   refusal cell is graded.
   - A DEV push is admitted only when the pushed commit is a two-parent merge carrying `Feature:` and `Approved-By:` trailers.
   - The DT keeps PROD only.
   - The FAST-lease route lands through the script.

   Then the FWD-3 refusal arm runs: a direct DEV push from a box seat is refused, and the gate bytes are read on all four box
   branches.
2. **FWD-2's declined arm, shown refused.** Merge-forward and the release builder each print `declined` on
   `cand/laptop/declined-example`.
3. **FWD-1's client-facing case and FWD-7 on organic work.** IRPT_ANLREQ's next page change is cut by dell2 as
   `cand/dell2/<slug>` from the last PROD release and registered. Andrew approves it on the open-calls list, then merge-forward and
   a chosen-set promote. The builder is dell2's IRPT_ANLREQ seat, not this project's worker. This project's cell is the
   registration check, the merge-forward and the read.
4. **The three re-registered ANLREQ merges** (bb8b): one approval row each, for Andrew. The next chosen-set promote ships only the
   ones he approves.
5. **ONE batch repair cell:** `W2-S7` (a local-only branch is refused by the default fetch) and `W2-S8` (the register-test pin
   drift advisory).

**Andrew's act, still carried:** the CLAUDE.md FAST-lease line (C-MERGE-FORWARD), which is his law edit. It is on this seat's
open-calls card.
