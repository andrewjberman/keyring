# NFRA_GATSCP -- GitOps gates scoped to the act: a gate refuses only what the act itself breaks

```json
{
 "project": "NFRA_GATSCP",
 "directive": "D0",
 "fabric": "dell1",
 "prd_version": "v0.2",
 "step": 4,
 "brief_ref": "docs/briefs/gitops-gates-scoped-to-the-act-brief-20261009.md@4c795d29a4",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7"],
 "status": "DRAFT"
}
```

**Owner:** 1.0.0_SA_CTO. **Brief:** `docs/briefs/gitops-gates-scoped-to-the-act-brief-20261009.md` @4c795d29a4 (4.0.0_SA_CRO~A).
**Andrew's word:** "both recs approved" (~06:3xZ 2026-10-09,
`org/tier1_exec/4.0.0_SA_CRO~A/deliverables/ANDREW_DIRECT_20261009_063xZ_GITOPS_STRATEGY_RECS_APPROVED.md`): rule P1 (a gate refuses only
a defect the act introduces; a standing defect elsewhere is printed and routed to its owner), rule P2 (the commit that changes a generated
file's source regenerates it in the same commit), and one project through the canonical flow. P1 and P2 bind this project; they are not
CLAUDE.md law until Andrew orders it. Each outcome's ACCEPT below carries its negative arm: narrowing who a gate refuses never loosens
what it refuses in the act's own files.

**v0.2 (1.0.0_SA_CTO, 2026-10-09 ~06:5xZ), on `3.0.0_SA_CVO`'s refusal @fc4e314af0, option (a):** FWD-7 reads "no one passing it along
by hand", and C-DELIVER sends the bus line by the sending box's manager's automated path, as NFRA_CTLPLN FWD-3 requires; the note on
negative arms moved here from the ENDPOINT section.

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  On one box, a worker's finished work and that box's sync both land while another project
         holds a fresh error and another project's register is out of step, and nobody on the box
         fixes anything by hand
         DONE WHEN  EXERCISED -- one real drain and one real box sync, both landed, both errors printed
         ACCEPT     a box carries a fresh error in another project's issue log and a register entry of
                    another project that no longer matches its project; a worker's finished work is
                    merged and the box then syncs; both land, both errors are printed and named to their
                    owners, and the box's manager repairs nothing. The two errors may be placed there on
                    purpose for the test; the project work merged must be real, not a practice round
         SOURCE     brief PART I, the candidate thread (site Z, the night of 2026-10-09)

  FWD-2  A seat records its own issue rows while another project's issue log holds a fresh error
         DONE WHEN  EXERCISED -- one commit landing beside another project's error, one refused on its own
         ACCEPT     a seat's issue rows land while a different project's log holds a new error, and that
                    error is printed as standing; a new error in the seat's own rows is refused exactly
                    as today; deliberately resetting the known-errors list stays a refusal
         SOURCE     brief O1

  FWD-3  A seat commits to its own project while another project's register is out of step
         DONE WHEN  EXERCISED -- one commit landing beside another project's mismatch, one refused on its own
         ACCEPT     a commit to one project lands while a different project's register entry does not
                    match it, and the mismatch is printed as standing; a mismatch in a project the
                    commit touches is refused exactly as today
         SOURCE     brief O2

  FWD-4  When a project's record changes, its summary entry changes in the same commit, with no
         second step
         DONE WHEN  EXERCISED -- one real change of a project's stage, committed once, both files in it
         ACCEPT     someone changes a project's stage or another summarised field and commits once; the
                    summary entry is updated in that same commit without anyone running anything else;
                    if the update cannot be made, the commit is refused and says why
         SOURCE     brief O3; rule P2

  FWD-5  The owner of a standing error finds it where they already look, without having been the one
         refused
         DONE WHEN  EXERCISED -- one standing error printed by someone else's act and found by its owner
         ACCEPT     an error printed as standing names its project, and its owner finds it in that
                    project's issue log, on the box's list of open calls, or in its own inbox; no new
                    alert, monitor or notice is built for this
         SOURCE     brief O4; CLAUDE.md section 5 (the standing moratorium)

  FWD-6  A box's merge, and a commit from the shared folder, are judged on what they actually contain
         DONE WHEN  EXERCISED -- one merge and one shared-folder commit, each judged on its own contents
         ACCEPT     the checks read what the merge or the commit actually carries; another seat's unsaved
                    edit in the shared folder is never judged as part of someone else's commit, and a
                    file the merge changes is judged as merged, not as it was before
         SOURCE     brief O5

  FWD-7  An order sent to a seat on another box, or to a Codex seat, arrives without anyone passing it
         along by hand
         DONE WHEN  EXERCISED -- one order to a seat on another box and one to a Codex seat, each found in
                    the receiver's inbox
         ACCEPT     when an order is issued to a seat on another box or a Codex seat, that seat finds it in
                    its inbox with no one passing it along by hand; the notice still travels only between
                    the two boxes' managers, sent by the sending box's manager automatically; it cannot go
                    out before the order itself can be fetched by the receiving box; every time it shows is
                    in UTC
         SOURCE     brief O6
```

## CONTRACTS

- **C-SCOPE (P1).** A gate in scope (the corpus pass inside the surprise-row gate; the missions-tree check) grades the ACT's file set:
  the staged paths at a commit, or the merge's changed paths under box-sync. A finding outside that set prints as `STANDING <owner>` and
  never refuses. Inside it, the gate is exactly as strict as today. A RESOLVED baseline tuple stays a refusal (a CVO re-baseline act).
- **C-REGEN (P2).** A commit that stages a tree `project.json` also stages its regenerated `org/projects/<CODE>.json`, produced by
  `missions-tree-index.py` inside the commit act, within the committing seat's lane. A regeneration that cannot run refuses the commit
  with its reason.
- **C-BYTES.** Every gate in scope reads the staged or merged bytes (the index blob), never the working tree.
- **C-OWNER.** "Owner" resolves from data already present: the channel document's project folder, the tree row's project folder. The
  carrier is one the owner already reads: its surprise channel, the box open-calls list, or its inbox. No new alert, monitor or
  notifier (CLAUDE.md section 5).
- **C-DELIVER.** The task-order issuance act opens the cross-box file (`crossbox-call.py`, owned by NFRA_CTLPLN's SEATS workstream,
  extended here, not redesigned) for an addressee on another box or a Codex seat, and hands the line to the sending box's manager's
  automated path, which puts it on the bus: only the managers talk across boxes (NFRA_CTLPLN FWD-3; Andrew-direct 2026-10-06 ~14:0xZ,
  "only the MSTR agents are the ones that communicate between boxes"). That path refuses to send while the order's commit is not on
  origin, and every time it reads or writes is UTC.
- **C-NO-FRICTION.** No new gate, switch, approval step or override is added; these are refusal-scope changes to existing gates.
- **Out of scope:** a worktree per seat by default (Andrew: "later"); the agent-bus consumer's 30-minute expiry; any CLAUDE.md law edit.

## SURFACE MANIFEST (step 4 -> step 5)

`claim`: `measured` = read by the brief's author on 2026-10-09; `held` = stated by the brief, not re-read by this seat.

| id | outcome_ref | surface | claim | evidence | verb | depends_on | bound |
|---|---|---|---|---|---|---|---|
| S01 | FWD-2, FWD-6 | `.tools/surprise-corpus-validate.py` (the corpus pass) | measured | brief F1; 086b594d5e reads the index | build | -- | refusal scope only; the baseline is the CVO's |
| S02 | FWD-2 | `.tools/surprise-row-gate.py` (its caller) | held | brief F1 | wire | S01 | passes the act's paths |
| S03 | FWD-3, FWD-6 | `.tools/git-hooks/missions-tree-check.sh`, `.tools/missions-tree-index.py check` | measured | brief F2, F3 | build | -- | scope and staged input; the contract's rules unchanged |
| S04 | FWD-4 | `.tools/safe-commit.sh` with `missions-tree-index.py derive --write` | measured | brief F4 | build | S03 | inside the committing seat's lane |
| S05 | FWD-1, FWD-6 | `.tools/box-sync.sh`, `.tools/safe-merge.sh` (callers) | held | brief Part II | wire | S01, S03 | touched only where a gate's input changes |
| S06 | FWD-5 | the surprise channel, `open-calls.py`, the inbox (existing carriers) | held | brief O4 | wire | S01, S03 | no new notifier |
| S07 | FWD-7 | `.tools/crossbox-call.py` send path; the issuance act (`/dispatch`, the TO gate) | measured | brief F5 | build | -- | extends NFRA_CTLPLN's tool; no protocol redesign |
