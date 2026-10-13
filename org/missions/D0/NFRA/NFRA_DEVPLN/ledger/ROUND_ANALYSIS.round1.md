# NFRA_DEVPLN -- ROUND-1 ANALYSIS (1.0.0_SA_CTO, 2026-10-13 ~20:5xZ)

**On:** the issuer's drain-end read `org/tier1_exec/2.0.0_SA_COO~DV/deliverables/NFRA_DEVPLN_ROUND1_DRAIN_END_20261013.md`
(@f4539dcc2f; 6 of 6 orders complete, 6 proof instances VALID, round-close-check MAY-CLOSE). **PRD:** v0.2 @d2b7385bee, plus the v0.3
wording addendum below (no ENDPOINT change). **Next:** round 2, cut by `2.0.0_SA_COO~DV` in ONE issuance on section 4.

## 1. Where the thread stands (advance, not a grade; the CVO grades)

The round built every hop of FWD-1's journey as a tool:
- the approval row (DP-b-1, DP-b-5);
- the merge-forward script (DP-b-2);
- the release builder and the `/prod-deploy` chosen-set step (DP-b-3);
- the contributor page (DP-b-4);
- the settlement list (DP-s-1).

The seam was run on the real portal repo with a scratch store and no push. The merge is two-parent with both trailers, and the
release reads `unapproved=0` READY.

Not yet run for real: hops 3 to 7. Those are the row's close, the DEV push through the script, the chosen-set promote by the DT and
the page read.

**Moved since the drain:** the first real row, `laptop-20261013T200117Z-9e8a` (`cand/laptop/contributing-boxes`, Opal-internal, one
docs file), is CLOSED `approved` by this seat (`APPROVAL_20261013_202xZ_DEVPLN_CAND_LAPTOP_CONTRIBUTING_BOXES.md`; DEVPLN rec (b)).
Hop 3 is therefore met in the world, and hops 4 to 7 are round 2's first cell.

**Settlement (FWD-6) moved under the round, by Andrew's act.** The whole-DEV promote `63c4f9e3` (~19:24Z, his ~18:5xZ word) and the
integrator's fast-forward leave DEV = PROD = `63c4f9e3`. Open call `1e0b` is closed SUPERSEDED (ruling @ef92f6af09). C-SETTLE
clauses (1) and (2) are therefore met by that act. Its settlement commit is `63c4f9e3`, and C-PROMOTE's ancestry check binds from
it forward.

## 2. Rulings on the rows owed to this seat

**`NFRA_DEVPLN-W1-S1` (ARMED, disarm owner this seat): the approval close skips the CLOSED-BOTH gate. RULED: intended. The row is
DISARMED.**

The project-scope measurement reads the project's round orders: `.tools`, the portal, and two paths shared with IRPT_BCKEND. Those
are the wrong instrument for one feature's approval. An approval's subject is one branch, and its row lives on the building box's
own list. `approval_read` reads `cand/<box>/...` from that box's file, which has one writer, so only that box's seats can close it.
Its validity is read by `approval-status`: the class, and a closer of the right identity (`approval_class_ok`). That is the whole
gate the PRD asks for (C-CLASS).

Kept as stated: a client-facing approval still reads `valid=no` unless Andrew or a FAST lease closed it, whatever the scope.

A future approval for a project that is not NFRA_DEVPLN takes the same path. No new measurement is needed.

**`NFRA_DEVPLN-S1` (the issuer's two readings): BOTH ACCEPTED.**
- **C-PROMOTE, read first-parent plus a per-feature binding.** The literal walk of every `PROD..release` commit for a trailer would
  refuse every release: a feature's own commits are written before any approval exists, and only the merge commit can carry the
  trailer. Your reading closes the hole the CVO named, a DEV-cut branch carrying DEV beneath it, and it does so at each layer:
  - the first-parent walk of the release finds no untrailed merge;
  - each merged feature's head and commit count equal its approval row;
  - registration refuses a branch with a DEV-only commit (DP-b-5).

  The v0.3 wording addendum states it in the clause.
- **C-MERGE-FORWARD (iii), a lease-written approval row.** This is already the clause's text ("an approval row is still written
  for the record ... closed `approved` with `approved_by: FAST lease <lease file>`"). `approval-lease` is that writer, and the
  script reads one record. No wording change is needed.

## 3. The nine branches (C-SETTLE clause 3)

Measured by the issuer: all nine are PROD-cut and none overlaps DEV-only work.
- **Five hold nothing not already on DEV:** `cand-dell1-secclass-e53-r9`, `cand-dell1-secclass-e59-r10`,
  `q/dell2/wk-IRPT_BCKEND-167-portal/r1`, `irpt-dev-candidate-7-20260924`, `sitez/merge-trial-20260915`. **RULED: delete the remote
  refs.** A ref contained in its trunk loses no commit and is not destructive git (CLAUDE.md, Agent Autonomy). The issuer prints
  the containment read beside each delete.
- **Four hold a unique patch:** `wk-dsgn-irptv1-r25-61-prodcut`, `irpt-dev-candidate-3-20260924`, `irpt-opal-scope-p-portal-20260923`,
  `wk-IRPT_ANLREQ-51-portal-r4`. **RULED: each goes to its owner by name.**
  - The DSGN_IRPTV1 branch is HELD as is, since that project is PARKED by the pivot.
  - The three IRPT branches go to `1.0.0_SA_CTO~DELL2` through `0.0.0_AB_MSTR`.
  - Each owner either re-cuts its branch as a `cand/dell2/<slug>` feature through the route or names it dropped. A dropped branch
    is kept as a tag, never deleted while it holds a unique patch.
- The settlement list's headline counts are re-run after the promote.

## 4. ENRICHMENT LIST for round 2 (the issuer cuts ONE issuance; thread-breaking first)

1. **FWD-1's live run, hops 4 to 7, on row 9e8a.** The merge-forward pushes DEV. Until S03 lands, the integrator `0.0.0_AB_MSTR`
   pushes, which is admission (i). Then the DT runs the chosen-set promote naming only `cand/laptop/contributing-boxes`, and the file
   is read on PROD. This one real journey is the round's spine.
2. **S03 gate edit (DP-g-1), `1.0.0_SA_CTO`.** This seat lands it at its bytes, now that `portal-merge-forward.sh` exists.
   - The gate admits a DEV push only when the pushed commit is a two-parent merge carrying `Feature:` and `Approved-By:` trailers.
   - It ends the DT's DEV admission and keeps its PROD admission.
   - The FAST-lease route lands through the script.

   The refusal arm then runs on every box: a direct DEV push from a box seat is refused (FWD-3).
3. **A dell2 Investor Reporting feature through the route**, the brief's named first case: one real client-facing feature,
   approved by Andrew on the open-calls list.
4. **The nine-branch dispositions** as section 3 rules, with the settlement list re-run.
5. FWD-4's per-commit read; FWD-7's line in the gate and in `CONTRIBUTING-BOXES.md`; FWD-2's declined arm; FWD-5's negative-arm
   promote (a list naming an unapproved branch is refused).
6. **ONE batch repair cell (worker-light):**
   - `test_open_calls.py` red at base (W1-S8);
   - merge-forward never fetches (W2-S2);
   - no merge sha printed without `--push`;
   - the `approval-lease` default `--project` (W1-S7);
   - the `/prod-deploy` Step 8 receipt wording (W3-S3).

**Andrew's act, carried and not cut:** the CLAUDE.md FAST-lease line ("lands product changes on portal DEV itself" ->
"... through the merge-forward"). It is a law edit on his word (C-MERGE-FORWARD). Until he words it, the lease route and the script
coexist.
