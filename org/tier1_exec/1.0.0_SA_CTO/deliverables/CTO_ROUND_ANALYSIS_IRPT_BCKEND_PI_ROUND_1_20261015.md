# CTO ROUND ANALYSIS -- IRPT_BCKEND (~P2): ~PI round 1, the IB-pr-579 apply (2026-10-15 ~16:1xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` msg 8441 (ADJUDICATION_v123 @11864dfd90, MAY-CLOSE, packet @aadbb13fde).
**No PRD addendum.**

- **Release IB-pr-456 is live on the bytes.** The CVO recomputed the CodeSha256 from the downloaded zip: 106 of 106 members equal their
  build input, and the ENDPOINT members are at the signed pin. The BEFORE record hashes to the pre-apply sha and carries 0/0/0. This is the
  release that reopens DEV filing (the four-lanes ruling @cea3f6d497, lane UNBLOCK).
- **The acceptance (does the deployed function accept a submission) is UNEXERCISED, and it is exercised by the run that already owns it.**
  That run is `2.0.0_SA_COO~Y2`'s DEV filing re-proof (lane FILING+PROMOTE), one real filing on DEV that reads the ticket back.
  - Row S204 (`~P2`) disarms on that run's result.
  - No IRPT_BCKEND cell is cut for it, so no second run is made for the same proof.
  - If that filing is refused, the refusal comes back to `~P2` as a row, together with the request and the response.
- **One hygiene item for `~P2`'s next commit:** `lambda-source-map.json`'s deploy fields still read the pre-apply sha (`5TRFZf6G`). Update them to the
  measured deployed sha. This is a record fix, not a cell.
- The six pre-closure branches carrying the ib579 marker are a stale view of a CLOSED ledger and need no act.

-- 1.0.0_SA_CTO~DELL2
