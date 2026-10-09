# BRIEF -- GitOps gates scoped to the act

**L1 brief, mode NEW.** Author: `4.0.0_SA_CRO~A`, 2026-10-09 ~06:4xZ. Consumer: `1.0.0_SA_CTO` `/endpoint --forward`.
**Andrew's word:** "both recs approved" (~06:3xZ, at the `4.0.0_SA_CRO~A` terminal). It approves rules P1 and P2 and a
single project through the canonical flow. Record:
`org/tier1_exec/4.0.0_SA_CRO~A/deliverables/ANDREW_DIRECT_20261009_063xZ_GITOPS_STRATEGY_RECS_APPROVED.md`. This
continues his site Z order, "they and I can come up with a strategy on how to industrialize a fix", recorded in the
site Z brief (Refs).

**The two rules this brief serves (approved, not yet law in CLAUDE.md):**
- **P1, delta-scoped refusal.** A gate refuses only a defect the act it grades introduces. A standing defect elsewhere on
  the box is printed and routed to its owner; it never refuses a bystander.
- **P2, the writer writes the derived file.** The commit that changes a generated file's source regenerates that file in
  the same commit, so drift cannot be committed and nobody has to remember.

---

## PART I -- THE OUTCOME TERRITORY

### Candidate thread (becomes FWD-1)

**A worker's drain lands on a box that holds other projects' defects.** Take one box, one COO and one worker drain
(`.tools/safe-merge.sh`), followed by that box's `box-sync.sh` pass. The box holds a surprise-channel row with a NEW schema
failure in another project's channel, and a tree-index drift in another project. The drain and the box pass both land.
The two standing defects are printed in the gate output and reach their owners. The box manager does no hand repair. This is
the night of 2026-10-09 at site Z with the choke removed: three OPLGTW drains were refused on rows that were not theirs.

### O1 -- A seat lands its surprise-channel rows while another project's channel holds a failure

A COO or worker commits or drains channel rows. When a NEW schema failure sits in a channel document that the act does not
change, the act lands and the failure prints as STANDING. When the act's OWN documents carry a NEW failure, the act is
refused, as today. A RESOLVED baseline tuple is a deliberate re-baseline act and stays a refusal.
(Gate: `.tools/surprise-corpus-validate.py`, run inside `.tools/surprise-row-gate.py`.)

### O2 -- A seat commits to its own project while another project's tree is out of step with its index

A seat stages paths under `org/missions/D*/<MACRO>/<CODE>/` or `org/projects/<CODE>.json`. The commit lands unless the
violation is in a project the commit touches. A violation in an untouched project prints as STANDING.
(Gate: `.tools/git-hooks/missions-tree-check.sh` -> `.tools/missions-tree-index.py check`.)

### O3 -- An issuer moves a project's tree row and the generated index travels with it

An issuer (COO, CTO, MSTR) changes `dep_stage` or any indexed field in `org/missions/D*/*/<CODE>/project.json`. The same
commit carries the regenerated `org/projects/<CODE>.json`, with no second command to remember. If regeneration cannot
run, the commit is refused with that reason. Today it is refused for the drift.

### O4 -- The owner of a standing defect learns of it from the gate, not from a bystander's refusal

When O1 or O2 prints a STANDING defect, it names the owning project, and the owner finds it on a carrier it already reads.
**Bound:** this is an existing carrier: the project's surprise channel, the box open-calls list, or the owning seat's
inbox. It is NOT a new alert, monitor or notifier (standing moratorium, CLAUDE.md section 5,
`docs/architecture/MDPF_DEBTCLEAN_PRD.md` sections 11-12).

### O5 -- The box manager's merge is graded on the merged bytes, not the shared working tree

When `box-sync.sh` grades a merge under GIT_INDEX_FILE, or a seat commits from the shared tree, every gate in this brief
reads the merged or staged bytes. Another seat's unstaged edit is never graded inside someone else's act. The surprise-
channel pass already does this (086b594d5e; see Part IV F1). The tree check does not (F3).

### O6 -- An issuer hands an order to a seat on another box, or to a Codex seat, and it arrives

An issuer cuts a task order whose `<issued_to>` lives on another box or is a Codex seat. The issuing act opens the
cross-box delivery itself. The bus line cannot go out until the commit carrying the order and its body is on origin,
and every time the tool reads is UTC. The receiving seat finds the order in its inbox with no manager relay.

---

## PART II -- WHERE THE BOUNDARY SITS

**Owns:** the refusal scope of the three gates named in O1, O2 and O5; index regeneration at commit (O3); the routing of
a standing defect onto an existing carrier (O4); and the issuance-to-delivery hook for cross-box and Codex addressees,
including origin and UTC correctness (O6).

**Relies on, does not own:**
- **`NFRA_CTLPLN`** (D0/NFRA), workstream SEATS. It owns `.tools/crossbox-call.py` (cell CT-s-6, contract C-SEATS
  clauses 5-6) and the open-calls list. O6 extends that tool's send path; it does not redesign the cross-box file
  protocol. **The CTO decides at L3 whether this is a new project or a workstream of NFRA_CTLPLN.**
- **The surprise channel's content and baseline**, owned by `3.0.0_SA_CVO` (re-baseline is a CVO act). This project
  changes WHICH failures refuse an act, never what counts as a failure or the baseline.
- **The tree contract** (`org/standards/PROJECT_TREE.contract.json`, rules R1-R5). This project changes the check's SCOPE,
  never its rules.
- **`.tools/box-sync.sh` and `.tools/safe-merge.sh`** as callers. They are touched only where a gate's input changes.
- **`/dispatch`** (2.0.0_SA_COO) as the issuance act that O6 hooks into.

**Out of scope, named:**
- A worktree per seat by default (site Z cause 3). Andrew left it CARRIED with the REC "later".
- The 30-minute expiry of the agent-bus consumer (site Z item 5, unacked frames).
- Any law edit to CLAUDE.md that writes P1 or P2 as law. That takes Andrew's express order.

---

## PART III -- THE QUALITATIVE BAR

- A seat that commits on a box never has to read, fix or override a defect that another seat's act made. "Override"
  includes `# surprise-row-override` and `GIT_COMMIT_AUTHOR_OVERRIDE`.
- A box manager's night at merge time is spent merging. Today it goes to hand regeneration of indexes and relays of orders
  the issuing tool should have delivered (site Z brief, item 5).
- A gate stays as strict on the act it grades as it is today. A planted defect in the act's OWN files is refused exactly
  as before. Narrowing the blast radius is not loosening the bar.
- A standing defect is neither lost nor silent. It is printed each time, and its owner can find it without having been
  the one refused.

---

## PART IV -- THE SUBSTRATE (findings, measured 2026-10-09 06:1x-06:4xZ on the laptop)

- **F1, surprise-corpus pass: input fixed, scope not fixed.**
  - 086b594d5e (this lane, CTO-reviewed) reads every channel document from the index blob, so the pass grades merged or
    staged bytes. Proven by a planted index-only mutation: HEAD passed it, the patched code refused it.
  - The pass still refuses on ANY NEW failure in ANY of the 329 documents (9,890 rows). It runs on every channel commit
    (`surprise-row-gate.py` :3975-3992).
  - The per-row limbs of the row gate are already prospective (they grade only what the commit adds or mutates). The
    cross-document id-uniqueness limb was delta-scoped at c1a2ed1b8e. The corpus pass is the remaining whole-box limb.
- **F2, tree check: whole-tree scope.**
  - `missions-tree-check.sh` fires on any staged `org/missions/D*/` or `org/projects/*.json` path, then runs
    `missions-tree-index.py check` over every project (the generator reads 350+ rows, per its own header).
  - Any violation anywhere refuses the commit. That is how one issuer's drift refused every seat's tree commit on the box
    four times on 2026-10-09 (site Z brief, item 3).
- **F3, tree check reads the worktree.** The hook's own header states the bound: "`check` reads the WORKTREE, not the
  staged index ... the generator has no --staged mode. Named here so it is a known hole". It is the same disease 086b594d5e
  cured for the corpus pass.
- **F4, index regeneration exists as a manual verb only.** `missions-tree-index.py derive --write` regenerates the
  index. Nothing runs it at commit: `safe-commit.sh` has no call to it (grep: 0 hits for `missions-tree-index` in
  `safe-commit.sh`).
- **F5, crossbox send path.**
  - Prior art: `crossbox-call.py` refuses `line` until the order file is committed LOCALLY (:230-300).
  - On the receiving box, `receive` answers PULL-FIRST when the commit is absent (:352).
  - Nothing refuses the send when the commit is local-only and not on origin, so the line goes out and the receiver sits
    in PULL-FIRST. That is the "7b40 sent before its commit reached origin" case.
  - Nothing links task-order issuance to `crossbox-call.py open`. Site Z's Codex orders were files only, fixed by hand at
    05:5xZ.
  - The tool already formats and parses UTC (`UTC_FMT`, `parse_utc`).

---

## PART V -- WHAT MUST BE TRUE (named, not sequenced)

- A gate must know the ACT's file set: the staged paths at a commit, the merge's changed paths under box-sync. The row gate
  already receives dispatched paths (`_dispatched_from_argv_or_env`). The tree check receives `OWNED_PATHS_STAGED_FILES`
  or `diff --cached`.
- "Owner of a standing defect" must resolve from data already present: the channel document's project path, the tree
  row's project folder.
- `missions-tree-index.py` needs a way to read the staged or merged index (F3) before O2 and O5 can hold for the tree.
- Auto-regeneration in O3 must stay inside the committing seat's owned-paths lane. `org/projects/<CODE>.json` is a
  generated file; the CTO is the L3 writer of the tree carriers (CLAUDE.md rule 27, L3).
- O6 needs the issuance act (`/dispatch`, the TO gate) to know when an addressee is cross-box or Codex. A seat-to-box
  map exists in `lib/devices.py` and the open-calls scope tooling.
- A switch-free rollout. These are refusal-scope changes to existing gates; no new gate, alert or approval step is added
  (CLAUDE.md section 2, "do not manufacture friction").

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

| Clock (UTC) | Measured |
|---|---|
| 06:18Z | `box-sync.sh status --fetch` on the laptop: box/laptop 0 behind CLOUD 2626e2c073; dell2 100 behind; sitez 25 behind |
| ~06:1xZ | per the site Z brief: `missions-tree-index.py check` 0 violations at site Z; site Z winding down for a reboot on Andrew's word |
| 06:3xZ | 086b594d5e (corpus pass reads the index blob) is committed LOCAL on box/laptop; origin box/laptop was 6bcd481ff6 at ls-remote read |

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- I did not measure how often each choke fired across all four boxes. The counts are site Z's, from one night, in its
  brief.
- I did not trace which tool read `--since` as local time ("f12c" in the site Z brief). O6's UTC clause rests on that
  report, not on a reproduction.
- I did not verify that box-sync passes the merge's changed-path set to the row gate. O1 for merges assumes it does,
  because the cross-document limb's fix at c1a2ed1b8e grades "what a merge introduces".
- I did not read the `/dispatch` skill to find where O6's issuance hook would attach.
- I have not checked whether the generated index can be regenerated for one project or only for all of them (O3's cost).
- No numbers in Part III are ratified, because there are none.

---

## REFS

```
  BRIEF PATH        docs/briefs/gitops-gates-scoped-to-the-act-brief-20261009.md
  PROJECT           NONE-YET (CTO at L3: new NFRA project, or a workstream of NFRA_CTLPLN)
  EXISTING PRD      NONE
  SIBLING PROJECTS  NFRA_CTLPLN (SEATS workstream: crossbox-call.py, open-calls)
  PRIOR ART         086b594d5e corpus pass reads the index; c1a2ed1b8e cross-document limb delta-scoped;
                    crossbox-call.py committed-body and PULL-FIRST checks; missions-tree-index.py derive --write
  SOURCES           org/tier0_exec/0.0.0_AB_MSTR~Z/deliverables/BRIEF_20261009_061xZ_SITEZ_FABRIC_CHOKE_GITOPS_GATES.md @19a44d57c0
                    org/tier1_exec/4.0.0_SA_CRO~A/deliverables/GITOPS_INDUSTRIAL_FIX_STRATEGY_20261009.md @e13f7df191
                    org/tier1_exec/4.0.0_SA_CRO~A/deliverables/ANDREW_DIRECT_20261009_063xZ_GITOPS_STRATEGY_RECS_APPROVED.md
  MEASURED AT       2026-10-09 06:18Z-06:4xZ (Part VI)
```
