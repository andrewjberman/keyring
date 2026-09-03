# ANDREW-DIRECT 2026-09-03 ~03:5xZ -- workers commit freely under their project's tree path; a task order's status flip is the worker's act

**Channel:** Andrew, in person, at the `0.0.0_AB_MSTR` terminal, mid-turn. **Recorded by:** `0.0.0_AB_MSTR`
(carrier; adjudicates nothing). **Routed to:** `2.0.0_SA_COO` as registry grantor (`.owned-paths.yaml` is
`ANY_EXEC_OR_AE`); `1.0.0_SA_CTO` and `3.0.0_SA_CVO` copied. **Ledger:** LD-0521 Amendment 2.

## VERBATIM, entire

> also i dont think this is good design, worker agents should be able to commit freely to the directives folder
> path as thats where their work is:
> The one loose end: the task order's own status field lives in a directory I'm not permitted to commit to (by
> the repo's own access rules), so I left that edit in the working tree with the exact text for the owning seat
> to commit — noted clearly in my report.

*(The second paragraph is the worker's report he was quoting -- `0.8.0_AE_CloudComp`'s completion report on
`NFRA_COMPEFFICACY.TO-CE-T-1`; the first sentence is his ruling on it.)*

## What it binds, read plainly and marked as this seat's reading

- **The design defect he names:** under the project tree, `org/missions/*/*/*/task-orders/**` is lane `TREE_COO`
  (permitted: `2.0.0_SA_COO` only). The worker that completes a task order therefore cannot commit the
  `<status>complete</status>` flip on its own TO, and the flip -- which the canonical loop makes ONE atomic act
  with the proof-of-spec instance, by the acting seat, in the same turn -- was left uncommitted in the shared
  worktree. Measured at 03:57Z: the worker's completion commit `6d04680f2b` (03:51Z) carries the proof instance
  and the deliverable; the TO's status flip landed six minutes later under the ISSUER's author line
  (`2.0.0_SA_COO`, `fc5ec7106c`, 03:55Z), and the worktree under the project is clean. The workaround closed
  this instance; the design defect he names is the lane, and it stands until the grant lands.
- **The ruling:** a worker commits freely to its project's tree path, because that is where its work is. The
  controls on those paths are the GATES, not the lane: issuance is refused by `to-pipeline-gate.py` +
  `to-proof-of-spec-check.sh` (a worker cannot mint a TO that passes them without a decomp ref, a proof block
  and the preflight evidence); a terminal status flip is refused by `to-pipeline-gate.py check_complete_flip`
  unless the proof instance is VALID (now including the surprises limb); a row is refused by
  `surprise-row-gate.py`. This is the same reasoning he applied on 2026-09-02 to `investigations/` and `cards/`
  ("the row gate is the control") and that `2.0.0_SA_COO` applied at `bfec7d99b5` to the flat channel.
- **The act, at the grantor:** `2.0.0_SA_COO` widens the tree lanes so a Tier-2 worker may commit under
  `org/missions/D*/<MACRO>/<CODE>/` for its own work -- at minimum `task-orders/**` (the status flip on a TO the
  worker holds) alongside the already-open `deliverables/<serial>/**`, `surprise-channel/investigations/**` and
  `cards/**`. Whether that is lane `ANY` on `task-orders/**` (the gates as control) or a narrower grant keyed to
  `<issued_to>` is the grantor's design; his words are "commit freely", and a narrower grant must not re-create
  the loose end. `prd/**` and `decompositions/**` stay with their L4/L5 owners (nothing in his word touches them).
- **The immediate residue:** none for T-1 (the issuer committed the flip at `fc5ec7106c`). For every later task
  order the worker's own flip is the worker's own commit; an issuer committing a worker's status is the
  workaround this ruling retires, not the pattern.
- **Law surfaces touched by the grant:** `.owned-paths.yaml` is a law edit (commit + same-turn broadcast + push
  state); the spine's L6/L7 text states that a worker commits its own status flip.

## NOT read into it

- No change to who ISSUES a task order (L6, `2.0.0_SA_COO` only) or to the gates that refuse a malformed one.
- No change to `prd/**` (`1.0.0_SA_CTO`) or `decompositions/**` (`2.0.0_SA_COO`).
- No change to remediation rows (`3.0.0_SA_CVO`, L9).
