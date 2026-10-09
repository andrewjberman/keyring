# GitOps choke at site Z: strategy for a mechanical fix

**From:** `4.0.0_SA_CRO~A`, 2026-10-09 ~06:3xZ.
**For:** Andrew. This is a proposal for decision; nothing below is implemented except item 0.
**Input:** `org/tier0_exec/0.0.0_AB_MSTR~Z/deliverables/BRIEF_20261009_061xZ_SITEZ_FABRIC_CHOKE_GITOPS_GATES.md`
@19a44d57c0, delivered by 0.0.0_AB_MSTR msg 107777.

## Conclusion

The four chokes share one root cause: **each gate's refusal reaches further than the act it grades.** A gate reads the
whole box (the whole corpus, the whole project index, the shared working tree) and refuses whichever seat happens to
commit next. That seat neither caused the defect nor can fix it. So the box manager repairs by hand, and merging waits.

Two principles would turn the fix into mechanism:

- **P1, delta-scoped refusal.** A gate refuses only on a defect the act itself introduces. A standing defect elsewhere
  is printed and handed to its owner; it does not refuse the act.
- **P2, the writer writes the derived file.** When a commit changes a generated file's source, the same commit
  regenerates it. Nobody has to remember.

## The four causes, mapped

| # | Cause (brief) | Fix | Principle | Owner to build it | Cost |
|---|---|---|---|---|---|
| 0 | The corpus pass graded other seats' UNSTAGED edits in the shared tree (the `NFRA_MCPMSP-Z-S4` refusal) | **DONE** @086b594d5e: every document is read from the index blob, so only what the act stages or merges is graded | P1 | done, 4.0.0_SA_CRO~A | -- |
| 1 | The corpus pass refuses every drain on one committed bad row anywhere | A NEW failure refuses only when it sits in a document the commit or merge changes. NEW failures in untouched documents print as STANDING and the drain goes through. RESOLVED stays a refusal. | P1 | `.tools/surprise-corpus-validate.py` + row gate; this lane | small: one path filter, plus an arm per branch |
| 2 | Generated-index drift (`org/projects/<CODE>.json`) fixed by hand 4 times | (a) When a tree row is staged, `safe-commit.sh` runs `missions-tree-index.py derive --write` and stages the regenerated JSON. (b) `missions-tree-check` refuses only drift in the projects the commit touches. | P2 + P1 | safe-commit + `missions-tree-index.py`; this lane | small to medium |
| 3 | A dirty shared tree, 21-41 edits by about 13 owners | Point 0 already stops other seats' unstaged edits from reaching the corpus gate. What remains: box-sync HOLDS when a dirty edit sits on a path CLOUD changed, and that hold is correct. Fix: the seat launcher opens a worktree per seat by default (rule 14b today binds by reading only), and the shared tree is used for drains only. | P1 | launcher (`spawn-agent.ps1`) + `/mstr-spawn`; 0.0.0_AB_MSTR | medium; changes every seat's start |
| 4 | Cross-box orders to Codex seats were delivered as files only; a line was sent before its commit was on origin; `--since` was read as local time | Issuing an order to a seat on another box or to a Codex seat runs `crossbox-call.py`. It refuses to send until the commit is on origin (ls-remote ancestry), and it parses times as UTC. | P2 | `crossbox-call.py` + `/dispatch`; this lane, with the COO for the dispatch hook | small |

The manager's load (brief item 5) is the sum of items 1 to 4. It needs no fix of its own.

## Recommendation

Run it as one project, "GitOps gates scoped to the act". Brief it with `/brief-create` and enter the canonical
flow, which takes it through endpoint and PRD to dispatch by the COO. Round 1 builds items 1, 2 and 4: each is a
small change in a tool this lane already maintains. Each FWD outcome is provable by planting the defect elsewhere on the
box and showing an unrelated commit pass while the planting commit refuses. Item 3 changes how every seat launches, so
it waits for your separate word.

## What I need from you

1. Do P1 and P2 hold as the rules?
2. Brief it as one project now (recommended), or hand items 1, 2 and 4 straight to this lane as fixes, with no project?
3. Item 3, worktree per seat by default: yes, no, or later?
