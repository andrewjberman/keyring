# The brief-to-cut chain: where a v3 round spends its cost -- L1 brief

**Author:** `4.0.0_SA_CRO`. **Date:** 2026-09-05, measured 13:3xZ-14:0xZ. **Mode:** NEW.
**Commission:** Andrew-direct ~13:3xZ at this terminal, *"recs approved"* on `/open-calls` CALL 1 (*"Commission a brief
on the brief-to-cut chain -- yes / no?"* REC yes), record @`8e89f1127f`. Two rounds said the same thing independently:
`NFRA_OUTSET` round 1 (this seat's check-out, the COO's drain-end read 94341 and L8 94372) and `ETFS_GUARDRAIL` round 1
(the CTO's L10 @`0557afa38a`: *"The round's cost went into the CUT, not the work"*).

**HOW TO READ THIS.** Part I is the territory `/endpoint --forward` cuts outcomes from -- seven things a person can do.
Part II says what this owns against the spine, the gate and `/dispatch`. Part III the bar. Part IV what happened,
measured, with the one sentence per finding that changes what the PRD buys. Part V preconditions, unsequenced. Part VI
status with its clock, NOT outcome-bearing. Part VII what this brief did not check. The brief is about the CHAIN from a
ratified decomposition to a worker's first commit; it is not about any one issuer's night.

---

## PART I -- THE OUTCOME TERRITORY

### O1. An issuer learns at the cut, not at a worker's first commit, that a face's grant does not cover what its commits will trip
Before the issuance commit lands, the issuer can see that a face grants a tool but not the precondition of a gate that
tool's edit fires (the comp-system pair; `task-orders/` for the flip), and the issuance is refused for it in the gate's
own voice. Today nine of seventeen faces shipped that way and each would have walled its assignee at its first commit
(Part IV F2); the one that surfaced it cost a worker a row and the issuer an amendment on nine faces.

### O2. An issuer knows a criterion is satisfiable by an honest implementation before it ships
A mechanical criterion whose `<expect>` cannot be met by a correct implementation on the issuer's own tree -- only by a
dishonest one -- is caught before a worker is asked to meet it. Today O1-AC2 demanded `WITHIN BUDGET` at 5 s from a
tool whose unavoidable git walk measures 6-12 s (Part IV F3); the only way to pass it as written was to wire the budget
to lie, and the worker correctly failed it and filed a row instead.

### O3. The face-level facts every face shares are computed once, never typed per face
The proof-of-spec stem the gate globs, the form an invocation takes for a bash forwarder, the artifact name a criterion
cites -- the properties that were right on one face and wrong on sixteen (Part IV F4) -- come from one derivation the
issuer runs, so a face cannot be individually wrong about a fact the gate decides for all of them.

### O4. A row filed against one face is graded against the population before it closes
When an assignee's row names a defect in its face, the issuer's repair is read against every face that shares the
trigger, and the row closes only when the population is clean -- the habit the OUTSET issuer arrived at by the third
defect ("found by GENERALISING a row instead of closing it") becomes the drain's ordinary step. Today three of five
defects were repaired on the member and left standing on the population (Part IV F5).

### O5. An issuer seats and re-seats slots without amending faces
`<issued_to>` binds a face to a worker slot at spawn, not at the cut, so a fan-out re-sized by file contention or a
slot re-handed after a drain does not cost an amendment on HEAD plus a carry onto every live worktree. Today eight of
the thirteen issuance repairs were addressing churn of exactly that shape (Part IV F6).

### O6. A reader of a round can see where its cost went from one census
Anyone can read, for a closed round, the split of commits and hours between the cut (issuance and its repairs), the
work (worker and lane commits) and the drain, with the issuance repairs listed by cause -- so "the round's cost went
into the cut" is a number with a denominator rather than two seats' impression (Part IV F1 is that census, run by hand).

### O7. A worker's first wall is the issuer's, and it is found before the worker exists
The issuer can run, on its own tree and before any spawn, the same checks a worker's first commit will meet -- the
grant against the paths the invocations touch, the gates those paths trip, the proof stem the gate will glob, the flip
the drain will need -- and reads the refusals in the issuer's own name. Today every one of those was first read by an
assignee, in the assignee's name, at the most expensive moment (Part IV F5: "the gate's message points at the
ASSIGNEE, and the defect is in the ISSUER's face").

---

## PART II -- WHERE THE BOUNDARY SITS

**This work OWNS:** the CUT-TIME checks between a ratified decomposition and the issuance commit -- the face-vs-gate
precondition read (O1, O7), the satisfiability read of a mechanical criterion on the issuer's tree (O2), the derivation
of shared face facts from one source (O3), the population step at a row's close (O4), the binding of `<issued_to>` at
spawn (O5), and the round census as an instrument (O6). Where these land -- as limbs of `.tools/to-pipeline-gate.py`,
as steps of `/dispatch` Step 2-4, or as a derivation `/dispatch` runs -- is L4/L5's call, not this brief's; the brief
names the properties, not the carriers.

**This work RELIES ON, and does not move:** spine v3 as it stands (one issuance, the two faces, one clause per
criterion, the task order as the worker's grant, the drain through `safe-merge.sh`); RULING 1's `<paths>` grammar
(`owned-paths-validate.py`, `to-pipeline-gate.py` GATE (v)); the L6 gate's existing limbs (tier, committer, non-empty
grant, coverage at DECOMP, criterion grammar, the EXECUTING limb the CTO is building on 94335); the surprise channel and
the coordinate grammar; the gates the faces trip (comp-system's stale-state block, the commit gate, the lane hook) --
consumed as facts about what a commit will meet, never edited here; the CTO's round analyses and the CVO's L9, which
are where the two rounds' findings already live.

**Siblings named:** `NFRA_OUTSET` (round 1; the measured specimen), `ETFS_GUARDRAIL` (round 1; the independent one),
`NFRA_CLDGRPH` (round 4; ten post-issuance L6 commits not classified here -- Part VII), `NFRA_COMPEFFICACY` (the
PRD s.4 result schema every face inherits), the `/dispatch` skill (the COO's cut procedure), the L6 gate (the CTO's).

---

## PART III -- THE QUALITATIVE BAR

- **B1.** An assignee's first commit on a fresh v3 round meets no refusal the issuer could have read on its own tree
  before the spawn; when one occurs, the refusal names the issuer's face, not the assignee's commit.
- **B2.** A criterion a worker fails is contested on the worker's implementation, never on whether an honest
  implementation could have passed it.
- **B3.** The same face-level fact is not wrong on two faces of one issuance; a defect in a shared fact is one repair,
  not sixteen.
- **B4.** A row against one face closes with a sentence about the population it was checked against.
- **B5.** A round's drain-end read states the cut / work / drain split with its denominator, and the next round's is
  comparable to it.
- **B6.** Re-seating a slot changes a worker's prompt and nothing on HEAD.

---

## PART IV -- THE SUBSTRATE: what happened, measured

### F1. The census: 13 of 93 commits on NFRA_OUTSET were issuance repairs
POPULATION AND CLOCK, stated because the number moves with both: `git log` (merges included) over
`org/missions/D11/NFRA/NFRA_OUTSET/` since 2026-09-04 15:00Z -- the register row, so the pre-issuance L3/L4/L5 commits
are in the denominator -- read at 2026-09-05 14:0xZ, classified by subject prefix at this seat. 93 commits: 44 work
(worker + lane), 15 drains, 13 issuance repairs (`amend` / `carry` / `re-address` / `L6 AMENDMENT`), 9 surprise, 3 L5,
2 L4, 2 adjudication, 1 L8, 1 L3, 2 issuance, 1 other -- eleven classes, and they sum to 93. A later read gives a
larger total (the round keeps committing) and a `--no-merges` read gives 12 repairs, not 13: the thirteenth
(`2ad5fe800f`) is carried by a merge (parents `ea4a3f99f6` / `ddff1d8eeb`) -- the issuer verified both facts on its
own tree (94424). -- One commit in seven was the cut being repaired after the fact; the PRD buys the cut-time checks
that move that to zero before the spawn.

### F2. The grant covered the tool and not the gate the tool's edit fires -- on 9 of 17 faces
`safe-commit.sh` fires `comp-system --gate --changed` on any path matching `.tools/comp-`, `org/modules/graph/` or the
DS tree and BLOCKS when `infra/system/06_current_state.{json,md}` is stale; ten faces granted a path that trips it; one
(OS-s-1, only because a worker hit the wall and filed W1-S5) granted the pair; nine did not (@`b000632f27`). Under
RULING 1 an ungranted surface is a boundary, so each of the nine would have been walled at its first commit. -- The
check is mechanical: for every `<paths>` entry, the gates it trips and their preconditions are readable from the
gate's own regexes.

### F3. A criterion only a dishonest implementation could pass
O1-AC2 as cut: `.tools/comp-heat freshness .tools --budget 5` must print `WITHIN BUDGET`. comp-heat's freshness had no
path-scoped git call (OS-s-2's own unbuilt cell), so every run paid the whole-repo walk, measured 6.2-11.7 s by the
worker; an honest 5 s ceiling reaches BUDGET REACHED every time (@`ddff1d8eeb`, W1-S1). The worker failed the criterion,
did not flip, filed five rows. A second criterion, O3-AC3, was unsatisfiable on two independent limbs (@`df14ecd5f1`).
-- A satisfiability read is one run of the invocation on the issuer's tree before the cut; its cost is the invocation's
own budget.

### F4. Right on one face, wrong on sixteen: the facts every face shares were typed per face
`to-pipeline-gate.py:1261-1270` builds the proof-of-spec instance name from the FULL file stem (slug included) and globs
`deliverables/*/<full-stem>.proof_of_spec.json`; sixteen faces named the SHORT stem (S4, @`8d13fc6b80`). A worker writing
the instance at exactly the path its order named would have been refused at its complete flip with "NO proof-of-spec
instance was found beside it". The same commit fixed an invocation naming a bash forwarder through `python` (S1). --
Properties the gate decides for every face are one derivation, not seventeen hand-typed lines.

### F5. Three of five defects were repaired on the member and left on the population; none was found by the issuer
The COO's own account (94341): S4 correct on 1 face, wrong on 16; W1-S5 correct on 1, wrong on 9; the EXECUTING flip
wrong on the only row; two found by assignees at a wall, one by this seat's check-out, one by asking "what else did I
fix in exactly one place". The gate's refusal text points at the assignee's commit while the defect is in the issuer's
face -- "sixteen misdirected debugging sessions" had the round not caught it. -- O4 and O7 are the two mechanisms this
finding asks for; CLAUDE.md Rule 22's members-limb names the class.

### F6. Eight of the thirteen repairs were addressing churn, not content
`<issued_to>` was bound to slots at the cut; every re-size of the fan-out by file contention (four of five released cells
write `.tools/comp-heat`, so width 5 became 1+1+1) and every re-hand after a drain cost an `amend` on HEAD plus a
`carry` onto the live worktree, because the grant is read from HEAD and a worktree does not see it until the amendment
is brought over (@`b630052d6a`, `26a8bc43f8`, `afa659557d`, `c3449745ec`, `8c231d47bf`, `f6c7c50a8b`, `7771968abd`,
`d9bd63b35a`). The COO named it: "a FAN-OUT WIDENING IS ALSO AN ADDRESSING ACT". -- The grant needs the ORDER and the
PROJECT; whether it needs the SLOT at cut time is the design question O5 puts to the PRD.

### F7. What the L6 gate grades today, and the six things it does not
At HEAD, `to-pipeline-gate.py` grades GATE (i) the assignee's tier, GATE (iv) the committer, GATE (v) a non-empty
`<paths>` block with path grammar, issuance coverage at DECOMP, one clause per criterion and the judgment form, presence
of `<decomp_ref>` / `<preflight>` / `<proof_of_spec>`, and -- being built on 94335 -- the EXECUTING flip. It does not
grade: a grant against the gates its paths trip (F2); a criterion's satisfiability (F3); the proof stem against what
the gate itself globs (F4); an invocation's form against the file it names (F4); a BUILD cell with no write surface
(OS-s-17, @`ed5c4e2b5b`); `<issued_to>` against a seated slot (F6). -- Every one of the six is readable from artifacts
the gate already has open.

### F8. The channel carried the cost visibly, which is why it is measurable at all
NFRA_OUTSET's channel at 14:0xZ: 89 rows (worker-form and seat-form), of which 26 name the cut, a face, the issuer, a
grant or a precondition -- 17 filed by workers, 9 by seats. Workers filed rows and kept working in every case recorded
(94341: "declining a permission it had just proved it held, and saying so"); no defect was worked around. -- The spine's
row mechanism did its job; the finding is upstream of it.

### F9. The second round said the same thing without reading the first
ETFS_GUARDRAIL round 1 (the CTO's L10 @`0557afa38a`; analysis at `org/missions/D8/ETFS/ETFS_GUARDRAIL/ledger/
ROUND_ANALYSIS.round1.md` s.4): "three issuance amendments in two hours, all three the issuer's own cut defects, while
the worker filed rows and kept working" -- and there the issuer repaired on the POPULATION (W1-S2, W1-S3), "the shape
the NFRA_OUTSET issuer named on its own round, applied correctly here. That is a lesson travelling between projects
under its own power." -- Two issuers, two projects, one shape: the property is the chain's, not a seat's.

### F10. The face a worker receives, for scale
`NFRA_OUTSET.TO-OS-s-1` at HEAD: 89 lines, 11,953 bytes, 5 `<paths>` entries, 6 criteria, `<decomp_ref>`, `<preflight>`,
`<proof_of_spec>`, `<expected_criteria>`; the record face's status line now carries the drain's own account of why the
worker could not flip it. -- The face is small enough to be checked whole by a program before it ships.

---

## PART V -- WHAT MUST BE TRUE, without scoping it now

- **P1.** The gates a commit trips are enumerable from the gates' own code (`safe-commit.sh`'s regexes, the lane hook,
  the commit gate) -- a cut-time check reads them, never re-implements them.
- **P2.** A satisfiability run of an invocation on the issuer's tree is bounded by the invocation's own Rule T budget
  and never writes; a criterion whose invocation cannot run on the issuer's tree is declared so in the face.
- **P3.** The proof-of-spec stem, the artifact names and the invocation form have ONE source the gate and the cut both
  read (today the gate's glob and the face's text are two).
- **P4.** RULING 1's grammar stays: the order is the grant; the question is only when `<issued_to>` binds.
- **P5.** The population step at a row's close has a carrier the drain already runs (the drain reads every row the
  branch carries -- `/dispatch` Step 5).
- **P6.** The round census (O6) is derivable from git alone, so it is comparable across projects and fabrics.
- **P7.** Nothing here adds an approval or a message to any limb; every check is a refusal in a gate's or a skill's
  own voice, before a spawn.
- **P8.** A spawn-time binding of `<issued_to>` (O5) cannot be VERIFIED by commit ancestry: the carry a worker makes
  of an issuer's amendment is a path-scoped checkout that copies content without history, so the worktree's commits
  are not descendants of the amendment (measured with a positive control by `0.0.0_AB_MSTR` 94397, confirmed by
  `1.0.0_SA_CTO` 94393, relayed by the issuer 94424). Whatever verifies the binding reads content or a recorded
  vintage, never `merge-base --is-ancestor`.

---

## PART VI -- STATUS, NOT OUTCOME-BEARING

Measured at this seat 2026-09-05 13:3xZ-14:0xZ at HEAD (LOCAL; origin/CLOUD @`cb82020ab1` by ls-remote at 10:4xZ).

| what | state | clock |
|---|---|---|
| NFRA_OUTSET round 1 | 17/17 terminal, 17/17 proofs VALID, L8 @`a483609584`; CVO L9 in flight (C-S2, C-S3, C-S5 rows) | 13:3xZ |
| its commit census | 93 since issuance: 44 work / 15 drain / 13 issuance repair / 9 surprise / rest L3-L8 | 14:0xZ |
| its channel | 89 rows; 26 name the cut; 17 of those by workers | 14:0xZ |
| ETFS_GUARDRAIL round 1 | ROUND_CLOSE @`0557afa38a`; 3 amendments in 2 h; repaired on the population | record |
| NFRA_CLDGRPH round 4 | 97 commits since 07:00Z 09-04; 10 L6-labelled post-issuance commits, unclassified here | 14:0xZ |
| L6 gate limbs | (i), (iv), (v), coverage, grammar, presence; EXECUTING limb being built (CTO 94335) | HEAD |
| /dispatch | Step 2 states the face contract; Step 4 the `<paths>` census; no satisfiability or gate-precondition step | HEAD |

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- It classified commits by subject prefix; a subject can mislabel its act. The 13 repairs were each read by hand; the
  44 / 15 split was not. The total is a function of the population (the project path, merges included, since the
  register row) and the clock (14:0xZ) named in F1; four other scopings the issuer ran at 18:5xZ read 71, 71, 86 and
  114, none of them wrong -- a census without its population and clock beside it is not comparable to anything.
- It did not classify CLDGRPH round 4's ten post-issuance L6 commits (re-cuts and reopens under a different issuer);
  a third project may agree or disagree with the two.
- It did not measure hours per defect or the time from spawn to first wall; "the most expensive moment" is the COO's
  and CTO's reading, consistent with the record, not a clock this seat took.
- It did not decide where the checks land (gate limb vs `/dispatch` step vs a derivation) or whether `<issued_to>`
  should bind at spawn -- both are L4/L5's.
- It did not read the CVO's L9 on OUTSET, which is in flight and may re-grade some of the 26 rows as records rather
  than items.
- It deliberately does not fold in the two other things this round surfaced -- the unowned deploy (the CTO's at L10)
  and the worker credential posture (Andrew's CALL 2, accepted) -- both are named in the record @`8e89f1127f`.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/the-brief-to-cut-chain-where-a-v3-round-spends-its-cost-brief-20260905.md
  PROJECT           NONE-YET
  EXISTING PRD      NONE (the chain's law is the spine v3 + /dispatch; the L6 gate is the refuser)
  SIBLING PROJECTS  NFRA_OUTSET, ETFS_GUARDRAIL, NFRA_CLDGRPH, NFRA_COMPEFFICACY; the /dispatch skill; the L6 gate
  PRIOR ART         .tools/to-pipeline-gate.py (limbs at :86, :111, :151, :546, :633, :654, :1261-1275);
                    .claude/skills/dispatch/SKILL.md (Step 2-5); .tools/owned-paths-validate.py (RULING 1 grammar);
                    .tools/safe-commit.sh:789/:837 (the comp-system trigger and block); the OUTSET amendments
                    @ddff1d8eeb @8d13fc6b80 @b000632f27 @df14ecd5f1 @ed5c4e2b5b and the addressing set (F6)
  RECORDS           2.0.0_SA_COO 94341 (drain-end read) and 94372 (L8); 1.0.0_SA_CTO 94335 (EXECUTING limb ruling) and
                    the ETFS_GUARDRAIL L10 @0557afa38a; this seat's check-outs 94330/94331; Andrew-direct @8e89f1127f
  MEASURED AT       2026-09-05 13:3xZ-14:0xZ (every Part VI row carries its own clock)
```
