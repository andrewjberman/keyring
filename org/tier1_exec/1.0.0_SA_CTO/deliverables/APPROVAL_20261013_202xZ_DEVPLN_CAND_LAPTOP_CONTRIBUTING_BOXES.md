# APPROVAL 2026-10-13 ~20:2xZ (1.0.0_SA_CTO, laptop box CTO) -- cand/laptop/contributing-boxes APPROVED (opal-internal)

**Row:** `laptop-20261013T200117Z-9e8a` (kind approval, NFRA_DEVPLN, asked by `2.0.0_SA_COO~DV`).
**Authority:** NFRA_DEVPLN recs approved by Andrew ~14:3xZ (record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261013_143xZ_DEVPLN_RECS_APPROVED_AND_COMM_ASSIST_THROUGH_MUSE.md`):
(b) the box CTO approves an Opal-internal feature.

**Read by this seat:**
- `git -C portal log 15c97549..origin/cand/laptop/contributing-boxes` holds one commit, `07f065e6`.
- `git diff --stat` adds one file, `CONTRIBUTING-BOXES.md` (57 lines, a docs file in the repo root). It touches no page a user
  opens, so it is Opal-internal at most.
- The branch is cut from PROD release `15c97549`. Its text matches the DEVPLN rules Andrew approved: one feature per branch, cut
  from PROD, the approval classes, merge-forward only, and the promote taking a list.

**Decision:** APPROVED. It reaches DEV only through `.tools/portal-merge-forward.sh cand/laptop/contributing-boxes`.

**One note for the issuer:** PROD moved to `63c4f9e3` at ~19:24Z (the whole-DEV promote), after this branch was cut. The branch
still carries only its own commit, so the merge-forward stays clean. Re-cutting it is not required.
