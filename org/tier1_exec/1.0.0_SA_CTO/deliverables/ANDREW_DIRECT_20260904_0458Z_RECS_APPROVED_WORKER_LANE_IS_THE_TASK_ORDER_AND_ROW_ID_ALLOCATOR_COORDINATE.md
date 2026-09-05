# ANDREW-DIRECT 2026-09-04 ~04:58Z at the 1.0.0_SA_CTO terminal -- "recs approved" on /open-calls (2 cards)

**Verbatim, in full:** `/open-calls` (the skill, run at this seat) -> the two cards below -> **"recs approved"**.

Recorded by `1.0.0_SA_CTO` the same turn; broadcast the same turn to `0.0.0_AB_MSTR`, `2.0.0_SA_COO`,
`3.0.0_SA_CVO`, `4.0.0_SA_CRO`. Push state at record time: LOCAL; origin/CLOUD @351f309e0a (ls-remote read
2026-09-04 ~02:0xZ; pushes on Andrew's word, LD-0522).

Context: spine v3's first real drain (worker `0.9.0_WK_NFRA_COMPEFFICACY~2` on TO-CE-G-2, drain @46ff7f8c8a)
exposed five mechanism gaps (3.0.0_SA_CVO 94007/94010/94021; 4.0.0_SA_CRO 94014/94025). Gaps 2 and 5 closed
@72d05b2642 (CTO), gap 3 as procedure @e6351512fe (COO). The two that needed his word were put to him as cards.

## The frame he approved, verbatim

```
OPEN CALLS AT ANDREW -- 1.0.0_SA_CTO (2 calls, 2026-09-04 04:58Z)

BLOCKING (something waits on the word)

+-- CALL 1 of 2 ---------------------------------------------------+
  **Worker lane membership: (a) admit `0.9.0_WK_*` to every lane a Tier-2
  executor holds, or (c) the TASK ORDER is the grant -- a worker may write
  exactly the paths its order names, nothing else?**
  No lane in .owned-paths.yaml admits a worker serial (0 hits / 2,126 lines);
  worker ~2 committed both real surfaces through the audited override. Gates
  item 3 (NOT PASSED on this limb alone) and every L7 commit under v3.
  Registry act is 0.0.0_AB_MSTR's under SoD; your "the mechanisms right now"
  named spine s.4's eight, and this gap is new -- so it is your word.
  --------------------------------------------------------------------
  **REC -- (c).** The issuance commit already carries the order's <paths>
  under the COO's lane; owned-paths-validate resolves a worker's commit by
  reading its order at HEAD (I build the resolver limb; MSTR lands the rule).
  Only shape where a worker's write surface equals its order, and no lane
  widens fabric-wide.
+---------------------------------------------------------------------+

CARRIED (nothing blocked; answer whenever)

+-- CALL 2 of 2 ---------------------------------------------------+
  **Row-id allocator coordinate: adopt `<CODE>-(Z-)?(W<n>-)?S<k>` (and `C-`
  for the CVO's adjudication rows) -- yes/no?**
  CVO PROPOSAL @ddbbf3ce46 after S34 was minted twice by two worktrees.
  Detection is live (@72d05b2642 refuses a duplicate at the graded index;
  the COO's pre-merge gate is procedure). This removes the race at mint.
  Schema half CVO, three regexes mine, one commit; every existing id stays
  valid, nothing renumbered.
  --------------------------------------------------------------------
  **REC -- yes,** with <n> = the worker's slot number and `C-` for CVO rows.
  A worker's index cannot see the main index, so detection alone leaves the
  race to a procedure step that binds by reading; the coordinate makes the
  collision impossible rather than caught.
+---------------------------------------------------------------------+

Decided at this lane, not calls: subagent telemetry -- a worker's acts are witnessed by its commits
(author = worker serial), its proof instance and its WORKER REPORT, so the L7 step log compiles from git,
not the telemetry stream; spine v3.2 says so. Override-audit carrier (gap 4) -- the log should be written
under `git rev-parse --git-common-dir`, shared by every worktree; a one-line change I'll put to
owned-paths-check's owner.

NOT-MINE: 0.0.0_AB_MSTR holds the push window (LD-0522) and the CLDGRPH L8-L10 team restart
("call b we will wait") -- run /open-calls there.
```

## RULINGS (his "recs approved" = both RECs, as written)

**RULING 1 -- (c). THE TASK ORDER IS THE WORKER'S GRANT.** A worker serial `0.9.0_WK_<CODE>~<n>` is admitted to
exactly the paths that a task order under project `<CODE>`, issued to that serial and non-terminal at HEAD,
names in its `<paths>` block -- and to nothing else. No lane in `.owned-paths.yaml` enumerates a worker.
- `1.0.0_SA_CTO`: the resolver limb in `.tools/owned-paths-validate.py` (the resolver the pre-commit hook runs
  via `owned-paths-check.sh:140`) -- a worker's staged path is admitted iff its order names it at HEAD; a worker
  with no such order, or a path its order does not name, is REFUSED like any lane refusal; the override stays
  audited and singular. Self-tested red/green before it lands.
- `0.0.0_AB_MSTR` (registry grantor, SoD): the registry rule that DECLARES the policy so the registry stays the
  single declaration -- the exact stanza is in the broadcast; nothing else in the file moves.
- `2.0.0_SA_COO`: `/dispatch`'s pre-spawn census (@e6351512fe) reads the same rule -- the order's `<paths>` block
  is the worker's whole write surface, so a path the worker will need and the order does not name is a cut
  defect, not an override.

**RULING 2 -- YES. THE ROW-ID ALLOCATOR COORDINATE.** Grammar `^[A-Z0-9_]+-(Z-)?(W[0-9]+-|C-)?S[0-9]+$`:
a row minted in worker `<n>`'s worktree carries `W<n>` (`<n>` = the worker's SLOT number, the `~<n>` of its
serial); a row the CVO mints in `adjudications/` carries `C-`; a seat's row on the main index carries neither;
the fabric coordinate `Z-` stays and nests first. Every existing id (both S34s included) is valid unchanged;
nothing is renumbered. Uniqueness is by FULL id, so the limb @72d05b2642 keeps refusing a duplicate within a
coordinate.
- `1.0.0_SA_CTO`: the three regexes -- `.tools/surprise-row-gate.py:78 ID_RE` (with the gate's new discipline:
  a worker's NEW row carries `W<n>` equal to its own slot and a seat's row carries no `W`; a `C-` row lives
  only in `adjudications/` and a NEW row in `adjudications/` carries `C-`), `.tools/proof-of-spec-check.py:946
  SURPRISE_ID_RE`, `.tools/surprise-watch.sh:80 ID_RE`; plus `.claude/agents/worker.md` (the minting sentence).
  LANDS FIRST: the gate reads the schema from the staged index, so the regex half is a superset that admits
  the new form before the schema does -- nothing is broken between the two commits.
- `3.0.0_SA_CVO`: the schema half -- `investigation_item.schema.json:18` and `remediation_row.schema.json:20`
  patterns -- in ITS commit, AFTER the regex half is at HEAD.

**DECIDED AT THIS LANE (not calls), stated for the record:** (i) subagent telemetry -- a worker's acts are
witnessed by its commits, its proof instance and its WORKER REPORT; the L7 step log compiles from git (author =
worker serial), not from the telemetry stream; spine v3.2 carries the sentence. (ii) the override-audit carrier
(gap 4) -- the audit line should be written under `git rev-parse --git-common-dir` so every worktree shares one
log; a one-line change put to `owned-paths-check.sh`'s owner (the same SoD as the registry).

## Standing law applied
Verbatim record + same-turn broadcast + push state in the broadcast (CLAUDE.md "Changing this file"; org/XXX.md).
No gate is added on any seat by this record; the two acts it names are the two RECs he approved, in the lanes
that own them.
