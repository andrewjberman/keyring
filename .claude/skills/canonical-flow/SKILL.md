---
name: canonical-flow
description: Pick up a project already in flight or in limbo at the limb the invoking seat owns: `/canonical-flow <PROJECT_CODE>` locates it on both roots, measures its limb from artifacts (never status prose), names its limbo class, and either proceeds through the normal gates or hands off to the limb's owner. Covers the dirty-tree and unfinished-edits read after a crash. `--report-only` measures without acting. Never for a new project (those enter via /brief-create). Tier-1 seats; MSTR reports and routes; a worker subagent never runs it.
---

# /canonical-flow -- pick up an in-flight or limbo project at your limb

**Purpose (Andrew-direct, 2026-09-03 ~05:0xZ, MSTR terminal, verbatim):** *"I think we should make
/canonical-flow skill which is basically just a reference to the doc with the instruction that the agent to
whom its sent (which will invariably be a tier1) pick up the project based on their role and current status.
[...] This skill is basically for projects that are already in some kind of limbo state, if they were totally
new we'd just be running it from the initial /brief-create or /endpoint --forward."* And: *"Don't overfit to
one case, it should be for any in limbo project."*

**The failure it is hardened against (Andrew-direct, 2026-09-03 ~20:0xZ, MSTR terminal, LD-0532, verbatim):**
*"this morning there was an outage with the LLM providers so a lot of agents were unable to reach the server and
dying with unfinished work [...] 1.0.0_SA_CTO is going to be tasked with making a much more robust workflow and
operational structure for /canonical-flow."* A seat that dies mid-work leaves three kinds of residue and this
skill reads all three: work committed at HEAD (durable; the proof instance says whether it is terminal), work on
a worktree branch (durable, isolated; v3 workers only), and uncommitted or untracked edits in the shared tree (the
hazard; v2 seats only, and the only residue that can be lost or silently shipped). Nothing here recovers a
session; everything here recovers the WORK from the artifacts a dead session could not take with it.

**The reference is the spine: `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md`.** This skill restates none of
it. It does three things the spine does not: it MEASURES where a given project actually is, it names WHY it
is stuck from a closed set, and it tells THIS seat which limb is its to pick up and which are not.

**Two generations of project are in flight and this skill measures both.** A project issued under spine v2 has
broker-registered Tier-2 seats in `<issued_to>` and GO messages on the broker; a project issued under spine v3
has worker subagents (`0.9.0_WK_<CODE>~<n>`) in `<issued_to>`, one issuance commit carrying a `fanout:` line, and
worktree branches instead of seats. The spine's transition rule: a round open at the amendment finishes under the
task orders already cut; the next issuance is v3. The artifact grammar below covers both without a mode switch.

## Invocation

| Form | Behavior |
|---|---|
| `/canonical-flow <PROJECT_CODE>` | locate, measure, classify, then PICK UP at your limb (or hand off) -- an execution entry point |
| `/canonical-flow <PROJECT_CODE> --report-only` | locate, measure, classify, report; no act |

**Who runs it:** the Tier-1 seat it is sent to (`4.0.0_SA_CRO`, `1.0.0_SA_CTO`, `2.0.0_SA_COO`, `3.0.0_SA_CVO`, or a
`~lane` of one). `0.0.0_AB_MSTR` owns no limb: it measures, reports and routes to the owner.

> ⛔ **AND IT IS NOT A STOP ON THE WAY, EITHER — THE CTO RUNS L2 THROUGH THE L5 HANDOFF WITHOUT
> ASKING `0.0.0_AB_MSTR` FOR ANYTHING.** Andrew-direct 2026-09-10 ~20:0xZ/~20:1xZ at the MSTR terminal,
> VERBATIM: *"moving forward, tree landing needs to be a CTO job"* and *"yeah macros.yaml needs to be
> CTO too. anything from L2 up to the L5 handoff to COO for decomp needs to be able to be handled by CTO
> so we dont have this arbitrary mcp'ing which holds up our entire process if you are busy with something
> else. MCPing is really only to be used when necessary, the more efficient we get the less mcping should
> be happening."*
>
> ⭐ **THE GATE ALREADY SAID SO AND THE DOCTRINE DID NOT — measured on the resolver 2026-09-10 ~20:2xZ,
> 7 carriers x 4 agents, with `0.0.0_AB_MSTR` REFUSED on `project.json` in the same run as the live
> discriminator:**
>
> | L2–L5 carrier | lane | `1.0.0_SA_CTO` |
> |---|---|---|
> | `org/missions/*/*/*/project.json` | TREE_PROJECT_ROW | PERMIT |
> | `org/missions/DIRECTIVES.yaml` | TIER0_DIRECTIVES_REGISTER | PERMIT |
> | `org/missions/MACROS.yaml` | TREE_MACROS | PERMIT |
> | `org/projects/<CODE>.json` | ANY_EXEC_OR_AE | PERMIT |
> | `org/missions/*/*/*/prd/**` | ANY_CTO | PERMIT |
>
> **FIVE OF FIVE WERE ALREADY PERMITTED. NOTHING NEEDED A PERMISSION CHANGE.** What held the process up
> was PROSE — `.owned-paths.yaml`'s TREE_MACROS note said *"MSTR registers, CTO co-signs"*, and the same
> shape sits in CLAUDE.md Rule 27, the spine §L3 and `PROJECT_TREE.contract.json`'s `readers`.
> ⛔ **A DOCTRINE LINE THAT ROUTES AN ACT THROUGH A SEAT THE GATE DOES NOT REQUIRE IS WORSE THAN A
> PERMISSION BLOCK, BECAUSE NO REFUSAL TEXT EVER PRINTS.** A blocked seat reads a refusal and asks; an
> obedient seat sends a message and waits, and the wait is invisible to every instrument. Measured the
> same evening: two IRPT projects sat unregistered across four seats' messages while the CTO held PERMIT
> on every path involved.
>
> **SO: at L2, L3 and L4 the CTO writes the row, the register line, the macro enum, the index and the PRD
> ITSELF, in its own commit, and tells `0.0.0_AB_MSTR` afterward if at all.** `0.0.0_AB_MSTR` keeps
> DIRECTIVES.yaml and MACROS.yaml write access as an integrator fallback and holds NO gate over either.
> **L1 is unchanged and is still `4.0.0_SA_CRO`'s** (TREE_CRO refuses the CTO on `brief/**`, measured in
> the same run) — Andrew's range starts at L2. **L5 onward is unchanged and is still the COO's.** A v2 Tier-2 seat
enters a project only through an L6 task order: it measures, reports, and routes to its issuer. A v3 worker
subagent has no seat, no inbox and no skill tool, and never runs this; its whole context is its task order.

## Step 0 -- Read the spine

Read `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` in full at HEAD: section 1 (the limbs, their owners,
instruments and artifacts, the shape of a round and the midstream read), section 2 (role exclusivity), section 3
(limb, owner, `dep_stage`, refuser), section 4 (what binds by reading -- the clauses a live gate still
contradicts). Everything below keys on that file's grammar; where this skill and the spine differ, the spine governs.

## Step 0b -- The project tree: folder structure and key paths

**Normative carrier: `org/standards/PROJECT_TREE.contract.json`** (the tree as DATA; gates and the generator read
it, never prose). Reasoning and the artifact inventory per limb: `org/tier1_exec/2.0.0_SA_COO/deliverables/SPEC_PROJECT_TREE_DIRECTIVE_MACRO_PROJECT_20260902.md`
(sections 1, 3, 5a, 6). Lanes per folder: `.owned-paths.yaml`. What follows is the shape at contract 0.1.1,
restated once so a seat can orient without opening the contract; where they differ, the contract governs.

```
org/missions/D<n>/<MACRO>/<CODE>/                 three levels, each an enum:
  |                                                 D<n>   in org/missions/DIRECTIVES.yaml (directives.<D>; placement, members)
  |                                                 MACRO  ^[A-Z]{4}$, RATIFIED per directive in org/missions/MACROS.yaml
  |                                                 CODE   ^[A-Z]{4}_[A-Z0-9]{4,12}$
  +-- project.json                                  the register row IN its folder: dep_stage, fabric, directive, leads    (L3; lane TREE_PROJECT_ROW, CTO)
  +-- brief/                                        L1 output                                                                (lane TREE_CRO)
  +-- prd/<CODE>_PRD.md                             L4 output: PRD_HEADER block + ENDPOINT section + surface manifest;
  |                                                   a PRD addendum from L10 is a prd_version bump here                      (lane ANY_CTO)
  +-- decompositions/<CODE>_DECOMP.md               L5 output: the rectangle + four-postulate record + dependency edges;
  |                                                   FROZEN at the cut -- history lives in proof instances + the round-N analysis (lane TREE_COO)
  +-- task-orders/<CODE>.TO-<cell>.<slug>.md         L6 output (hyphen, tree spelling); v3: ONE issuance commit for every cell,
  |                                                   its message carrying `fanout: N of M chains, cap K, reason: ...`;
  |                                                   two faces in one file -- the WORKER face (cell text, paths, bounds,
  |                                                   one clause per criterion) is the subagent's prompt, the RECORD face
  |                                                   (status, authority, preflight narrative) stays for the gates;
  |                                                   a NEW file commits only as COO; a worker commits its own status flip     (lane ANY; gates are the control)
  +-- deliverables/<serial>/                         L7 outputs: <tool>.result.md, <TO>.proof_of_spec.json                   (owner carried by the path)
  +-- surprise-channel/investigations/INVESTIGATION_v{N}.md   L7/L8 WORKER rows, append-only, the seat that sees it appends (lane ANY)
  +-- surprise-channel/adjudications/ADJUDICATION_v{N}.md     L9: the CVO's dispositions, corrections and own observations,
  |                                                   in their own document so L8 reads worker rows only (spine s.4: the
  |                                                   contract folder and the gate census are build acts; until they land
  |                                                   the CVO's rows sit in the investigation file)                          (lane TREE_CVO)
  +-- surprise-channel/remediations/REMEDIATION_v{N}.md       L9 rows; the ONE slug of the round, to the CTO                (lane TREE_CVO)
  +-- ledger/                                        deploy-completion / change-management entries; STEP_LOG.<serial>.round<N>.json;
  |                                                   ROUND_ANALYSIS.round<N>.md (the CTO's answer to the slug);
  |                                                   COMPLETION_REPORT / COMPLETION_GRADES .round<N>.json at the close      (lane TREE_LEDGER)
  +-- cards/                                         substrate cards for what the project builds on                          (lane ANY)

.claude/worktrees/<name>/  +  branches worktree-*  v3 workers' isolated checkouts; a branch with no merged proof instance is a
                                                    worker that died mid-task-order (spine L7 "the drain", the midstream read)
org/projects/<CODE>.json                            the flat index entry, GENERATED from the tree for tree projects (derive --write);
                                                    hand-written for legacy flat projects (never overwritten, refusal R3)
org/projects/REGISTRY.md                            the human register row
docs/architecture/<CODE>_PRD.md                     a legacy flat PRD's home; a tree project's PRD lives at prd/ and this becomes a stub
org/surprise_channel/<CODE>/                        the legacy flat channel (investigations lane ANY; remediations CVO)
```

**Tools of the tree:** `python .tools/missions-tree-index.py check` (tree <-> index <-> DIRECTIVES.yaml; every
denominator printed; refusals R1-R5, ROW-*, INDEX-*), `... derive --write` (refresh the generated index entries),
`--self-test`; the commit-time validator `.tools/git-hooks/missions-tree-check.sh` (installed per device by
`install-missions-tree-check.sh`; fail-closed on any staged tree or register path). **PROSPECTIVE ONLY:** a legacy
flat project enters the tree the first time it is picked up (its L3 under the tree grammar), never by back-fill.

## Step 1 -- LOCATE the project on both roots, and stop if it is not yours to pick up

Measure each of these; ABSENT is a value, not a guess. Print the table.

| what | where to look |
|---|---|
| tree home | `org/missions/D*/<MACRO>/<CODE>/` -- `project.json` (`dep_stage`, `fabric`, `directive`), `brief/`, `prd/`, `decompositions/`, `task-orders/`, `deliverables/`, `surprise-channel/`, `ledger/` |
| flat register | `org/projects/<CODE>.json` (`dep_stage`, `fabric`, `phase`, `blocking`), the `REGISTRY.md` row, `org/missions/DIRECTIVES.yaml` membership + the directive's `placement` |
| brief | tree `brief/`, or the `brief_ref` the PRD header names, or `docs/briefs/` |
| PRD | tree `prd/<CODE>_PRD.md` (PRD_HEADER block, ENDPOINT section, surface manifest; `prd_version` -- an addendum bumped it) or `docs/architecture/<CODE>_PRD.md` |
| decomposition | tree `decompositions/`, or `workflows/atom_decomposition/runs/<code-ish>/`; its dependency edges (the chains L6 derives fan-out from); its version against the issuance commit (a decomposition that moved after the cut is a finding: it is frozen for the round) |
| task orders | `python .tools/to-check.py --all --project <CODE>` (both roots); the issuance commit and its `fanout:` line (`git log --format=%B -- task-orders/` on the newest issuance); for v2 assignees `python .tools/to-liveness-join.py` |
| proof instances | `deliverables/<serial>/<TO>.proof_of_spec.json` at HEAD, each run through `.tools/proof-of-spec-check.py`; VALID at HEAD is the only terminal read -- a `<status>` field is the stalest carrier in its own document; a criterion the task order flags as judgment is graded only in the CVO's adjudication, never by the instance's own verdict |
| worker branches | `git worktree list` + `git branch --list 'worktree-*'`; each unmerged branch is a worker that died mid-task-order |
| **unfinished edits** | `git status --porcelain -- org/missions/D*/<MACRO>/<CODE>/` AND every path the project's open task orders name in `<paths>` (or cite in their bodies), plus `git stash list`; a modified, staged or untracked file under those paths with no commit is a dead seat's unfinished work -- the outage residue. Print the file list with its denominator; never `git checkout --` or `git clean` anything here |
| surprise channel | `comp-surprise --project <CODE>` (both roots); the latest row citing each item decides its state; the CVO's heartbeat watermark (rows seen / undispositioned / watch pid) against the channel's row count |
| the slug and the CTO's answer | `surprise-channel/remediations/REMEDIATION_v<N>.md` (present = the slug is cut); `ledger/ROUND_ANALYSIS.round<N>.md` or a bumped `prd_version` (present = the CTO has answered it) |
| step logs / compilation | tree `ledger/STEP_LOG.*`; the compiled log's share of acts outside the limbs is the round's own instrument |
| holds | the register `phase` / `blocking` text, the directive's `placement`, any Andrew-direct record the row cites |

**Stop conditions, before anything else:**
- **Not found on either root** -> the project is NEW. Print `NEW: not in the loop -- enter through
  /brief-create or /endpoint --forward` and stop. This skill never registers a project.
- **Placed on the other fabric** (the directive's `placement`, or the project's `fabric`, names the device you
  are not on) -> print the placement and stop; it is that device's MSTR and seats who pick it up.
- **Closed** (`status` complete/cancelled with its closure) -> print it and stop.

## Step 2 -- MEASURE the limb from artifacts, then name the limbo class

**The limb is the highest limb whose OUTPUT artifact exists and conforms** (the spine's section 1 names each
limb's output). Read `dep_stage` too, but as a CLAIM: when the measured limb and `dep_stage` disagree, that
disagreement is a finding of its own (the row is stale; owner `1.0.0_SA_CTO` under the tree, the register
grantor for a flat row) and it goes into the report; it never overrides the measurement.

```
  output present and conforming                                  -> past limb
  brief (citable lines)                                          -> L1
  endpoint section / ratified FWD-n set                          -> L2
  project.json under the tree, macro in the ratified enum,
    fabric + directive set, index derived                        -> L3   (flat-only = NOT past L3 under the tree grammar)
  PRD at the tree home with PRD_HEADER + ENDPOINT + manifest     -> L4
  decomposition with its cells, record and dependency edges      -> L5
  task orders with decomp_ref + proof block; v3: one issuance
    covering every cell with its fanout line; v2: GO paired      -> L6   (in L7 while any is open)
  every TO terminal with a VALID proof instance at HEAD,
    surprises -> rows, no unmerged worker branch,
    no unfinished edit under the project's paths                 -> L7 done
  investigation rows filed; the CVO's watermark not behind       -> L8
  every item dispositioned by its latest citing row              -> L9
  the slug (REMEDIATION_v<N>) cut and sent to the CTO            -> L10 slug     (next = the CTO's read)
  ROUND_ANALYSIS.round<N> or a bumped prd_version                -> L10 answered (next = the COO's recut, or L4 forward)
  the next issuance cut from the analysis                        -> L6 again
  COMPLETION_REPORT + COMPLETION_GRADES, every grade REALIZED    -> CLOSED
```

**Limbo classes -- closed, exhaustive over "what is missing / whose turn / is a hold named":**

| class | meaning | owner of the next act |
|---|---|---|
| `STALLED-AT-OWNER` | the next limb's input exists and conforms; its owner has not acted | the next limb's owner |
| `ARTIFACT-GAP` | the next limb's input is missing or non-conforming (a PRD without an endpoint section or manifest; a decomp without its record or edges; a TO without a proof block or with a compound criterion; an issuance that does not cover every cell) | the limb that should have produced it |
| `PRE-TREE` | exists only in the flat register; no tree home | `1.0.0_SA_CTO` (L3 under the tree, then L4 at the tree home) |
| `DEAD-SEAT` | v2 only: open task orders whose broker-registered assignee is not live | `2.0.0_SA_COO` (re-address, or seat a fresh lane; or recut under v3 at the next issuance) |
| `UNFINISHED-EDITS` | uncommitted, staged or untracked edits under the project's paths, left by a seat that died mid-work; v2 residue -- v3 L7 work lives in worktrees and cannot produce this class | `2.0.0_SA_COO`: finish or discard each touch, one commit per task order it belongs to, with `3.0.0_SA_CVO` validating each finished fix against the task order's own criteria; a touch no open task order explains is a surprise row, not a commit |
| `ORPHAN-WORKTREE` | v3 only: a worker branch with no valid proof instance merged at HEAD | `2.0.0_SA_COO` (merge if its instance is valid, else discard and re-dispatch to a fresh slot) |
| `OPEN-ROUND` | every TO terminal; rows undispositioned, or the CVO's watermark behind the channel, or no slug | `3.0.0_SA_CVO` (L8-L9, the slug); a watermark behind is reported to `1.0.0_SA_CTO`, who re-arms the watcher |
| `SLUG-UNREAD` | the slug is cut and the CTO has written neither a round-N analysis nor an addendum | `1.0.0_SA_CTO` (the L10 read) |
| `ROUND-UNCUT` | the CTO's answer exists and no issuance has been cut from it | `2.0.0_SA_COO` (the recut, one issuance) or, after an addendum, `2.0.0_SA_COO` at L5 on the bumped PRD |
| `SEQUENCED-BEHIND` | a named hold blocks the next limb (a register phase, a directive placement, an Andrew-direct record) | nobody: report the hold's carrier; only Andrew lifts a hold |

A project can carry more than one class; list all, the blocking one first. `UNFINISHED-EDITS` and
`ORPHAN-WORKTREE` are always listed when present, whatever the limb: they are work that exists nowhere durable
and the next act of any seat must not overwrite it.

## Step 3 -- YOUR ROLE maps to exactly one pickup

| your seat | limbs you may pick up | what the pickup is |
|---|---|---|
| `4.0.0_SA_CRO` | L1 | the brief (`/brief-create`, `--midstream` when the project is already in flight) |
| `1.0.0_SA_CTO` | L2, L3, L4; the L10 read; the close | `/endpoint --forward` on the brief; registration under the tree; the PRD at the tree home with header, endpoint and manifest; reading a cut slug into `ROUND_ANALYSIS.round<N>.md` (to the COO with the remediations file) or a PRD addendum (a `prd_version` bump, the L4 notifier fires); the grades and the `CLOSED` flip |
| `2.0.0_SA_COO` | L5, L6, Track A, the recut, the cleaning run | `/atom-decomp` over the manifest and the battery; the one issuance for every cell with its `fanout:` line; the midstream three reads, then re-dispatch of every non-terminal task order to fresh worker slots; merging valid worker branches and discarding orphans; the one-off cleaning run over `UNFINISHED-EDITS` with the CVO validating each fix; the recut from a round-N analysis as one issuance |
| `3.0.0_SA_CVO` | L8, L9, the slug; validation of the cleaning run | rows, dispositions (judgment criteria graded here), the one slug of the round to `1.0.0_SA_CTO` and to no one else; re-arming its watcher from its watermark; validating each fix the COO finishes from `UNFINISHED-EDITS` against the task order's criteria, as a row |
| `0.0.0_AB_MSTR`, any v2 Tier-2 seat | none | report and route |

**Decide, in this order:**
1. If a `SEQUENCED-BEHIND` hold is named -> report it and stop. Do not lift it, do not work around it.
2. If `UNFINISHED-EDITS` or `ORPHAN-WORKTREE` is present and you are not the COO -> report it to the COO first,
   with the file list, and do not touch those files; then continue with your own limb if it does not read or
   write them.
3. If the next limb is YOURS -> pick it up (Step 4).
4. If the next limb is yours but its input has an `ARTIFACT-GAP` owned by an earlier limb -> hand BACK to that
   owner (a decomposition does not proceed on a PRD without a manifest; the COO does not write the manifest).
5. If the next limb is NOT yours -> hand off and stop: the spine's handoff for that limb where one exists (the
   L4 to L5 notifier fires on the PRD commit; a v3 task order's GO is its spawn, a v2 task order carries its own
   GO; the slug and the round-N analysis are each one message), otherwise one message to the owner naming the
   measured limb, the class and the gap. Never do another seat's limb.

## Step 4 -- Pick it up, through the gates

This is an execution entry point. After the report, do your limb's act in your own lane and under every
standing law: `safe-commit`, the L6 gate for any task order, the L4 to L5 notifier, record + broadcast for any
Andrew word met on the way, a surprise as a ROW. Where the spine's section 4 names a live gate that contradicts
the v3 clause you are executing, the gate's audited override is the only lawful way through, written into the
commit that uses it, and the report names it. A dead seat's uncommitted edit is neither merged nor discarded
silently: it is finished or discarded by the COO with the CVO validating, one commit per task order, and the
report names each file and what became of it. The pickup ends when your limb's output artifact exists and the
handoff to the next limb has fired; say which artifact and which handoff. Nothing here skips a limb.

## Step 5 -- Output

```
CANONICAL FLOW -- {serial} on {CODE} ({date time})

LOCATE   home: {tree path | flat only}   placement: {laptop | site-z} ({carrier})   status: {..}
         brief {path@vintage | ABSENT}  endpoint {..}  PRD {.. v{prd_version}}  decomp {.. chains M; moved since the cut? y/n}
         TOs {n open / m terminal; issuance {commit | v2 piecemeal}; fanout {N of M, cap K | ABSENT}}
         proof instances {v valid / t total at HEAD}   worker branches {k unmerged}
         unfinished edits {f file(s) under the project's paths | none}   stash {s | none}
         rows {n items, k undispositioned; watermark {ahead | BEHIND by d | ABSENT}}
         slug {REMEDIATION_v<N>@vintage | ABSENT}   answer {ROUND_ANALYSIS.round<N> | addendum v{..} | ABSENT}
         dep_stage (claimed): {..}
MEASURED limb: {Ln} -- highest conforming output: {artifact@vintage}
         claimed vs measured: {AGREE | DISAGREE: dep_stage says X, artifacts say Y -> finding, owner ..}
CLASS    {class} [, {class}]: {one line each, with the missing or stale artifact named; UNFINISHED-EDITS lists every file}
ROLE     {serial} owns {limbs}; next limb {Ln} is {MINE | NOT MINE -> {owner}}
ACT      {what I do now, or: handed off to {owner} by {handoff}; or: HOLD {carrier}, stopped}
```
Then the act itself, or the handoff message, or nothing (report-only).

## Rules

- **Measure, never infer.** A `<status>` field, a `phase` sentence and a `dep_stage` value are claims; the
  artifact at its vintage is the measurement. Cite paths and hashes. A proof-of-spec instance VALID at HEAD is
  the only terminal read for a task order; an unmerged worker branch is the only read for a dead worker; `git
  status` under the project's paths is the only read for a dead seat's unfinished work.
- **Role exclusivity is absolute** (spine section 2). A pickup at a limb you do not own is refused by this
  skill's Step 3 before any gate sees it.
- **No new projects, no holds lifted, no task orders from anyone but the COO, no CVO act before L8, no message
  from the CVO but the slug, no message from the CTO mid-round but the round-N analysis, no message to a worker
  ever, no `git checkout --` or `git clean` on another seat's unfinished edit by anyone.**
- **General by construction.** The classes above are defined by artifact grammar and ownership, not by any
  project, by which generation issued it, or by which outage killed the seat; a case this skill cannot classify
  is a defect in the class set, surfaced as a row, never special-cased in the skill.

## Notes

- Authority + provenance: Andrew-direct 2026-09-03 (verbatim above), recorded at creation in
  `org/tier0/ledger/LD-0524.md`; authored by `0.0.0_AB_MSTR`. A skill is accepted on an observed run: the
  first run is the Tier-1 seat Andrew sends it to, on the project he names.
- Re-keyed to spine v3.0 by `1.0.0_SA_CTO` on Andrew's word at the CTO terminal 2026-09-03 ~20:0xZ
  (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260903_200xZ_CANONICAL_FLOW_V3_RESTRUCTURE_SPINE_SKILL_CLAUDEMD_SINGLEHANDED.md`),
  from the CRO's implementation spec @29bf9265ea and its section 13 @9dc97d860d: the measurement ladder carries
  the issuance, the proof instances at HEAD, worker branches, the slug and the CTO's answer; the classes gain
  `ORPHAN-WORKTREE`, `SLUG-UNREAD` and `ROUND-UNCUT` and lose `ROUTED-UNPICKED` with the route tokens; the
  COO's midstream read of spine L7 is this skill's Step 1 and 2.
- Hardened against seats dying mid-work by `1.0.0_SA_CTO` on Andrew's word at the MSTR terminal 2026-09-03
  ~20:0xZ (LD-0532, relayed as message 93908): the `unfinished edits` read, the `UNFINISHED-EDITS` class owned by
  the COO with the CVO validating, the decide-order step that protects those files from every other seat, and
  the rule that no seat checks out or cleans another's unfinished edit.
