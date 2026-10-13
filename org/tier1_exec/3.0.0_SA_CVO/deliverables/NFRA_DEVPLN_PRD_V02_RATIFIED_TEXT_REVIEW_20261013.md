# NFRA_DEVPLN PRD v0.2 -- ratified-text half (ENDPOINT + CONTRACTS) review

**Reviewer:** `3.0.0_SA_CVO~L` (laptop), on the L4-R delivery 1.0.0_SA_CTO msg 108814 (and msg 108815). 2026-10-13 ~16:5xZ.
**Verdict:** SIGNED.

## What was read

- PRD at d2b7385bee (v0.2), unchanged at HEAD; ratified-text half_hash `3371f72bd76a8b134eb82bc6a9280f6facaac18cbfcab017a0daa87f5369dba5`.
- A section diff from v0.1 (1e49544e05): ENDPOINT is byte-unchanged; C-FEATURE, C-MERGE-FORWARD, C-PROMOTE and C-CLASS are amended;
  the ADDENDUM v0.2 is added.

## Against the v0.1 refusal (review @2b616031b1)

1. **The ancestry hole is closed twice.**
   - C-FEATURE: a feature branch is cut from the last PROD release, never from DEV. A DEV-cut branch is moved onto the release by its
     owner before its approval row exists. That is a private branch, not the forbidden rebase of a shared branch.
   - C-PROMOTE: a release is refused when any `PROD..release` commit lacks an `Approved-By:` trailer, with the count printed beside
     the total.
   FWD-5's ACCEPT is now delivered by the contract. Binding from the settlement commit is correct, because the backlog before it is
   ruled per group by Andrew (C-SETTLE).
2. **The FAST-lease route is reconciled, not removed.** It is kept as law, the live lease is read as the approval, an approval row is
   written for the record, and the lease's seat lands through the one script. The CLAUDE.md wording change is listed as Andrew's
   act, not made here. That is the right owner.
3. **The FWD-7 note is met.** C-CLASS states the read with both denominators, and says what a missing denominator does.

## Notes (not blocking)

- **A second law line is affected.** The CLAUDE.md push law ("PUSHES NEED NO WORD FROM ANDREW -- agents push at will (... portal
  DEV and PROD)") also changes once DEV is written only by the merge-forward script. Andrew's "yes agreed for all of this" and "All
  agreed, proceed" approve the approach, but the law edit list should name this line beside the FAST-lease line, as his act.
- **The DT seat's DEV admission ends** (ii). That is consistent with decision (a)-(e). It is worth one line in Andrew's law-edit
  list too, since `/prod-deploy` is the DT's skill.
