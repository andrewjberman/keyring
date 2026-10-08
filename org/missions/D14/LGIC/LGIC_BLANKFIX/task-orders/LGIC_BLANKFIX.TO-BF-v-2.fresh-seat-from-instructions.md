# TO LGIC_BLANKFIX.TO-BF-v-2 -- round 7 BF-v-2: FWD-5 exercised again -- a new seat finds the check in the written instructions on a fresh copy and reaches its totals, writing nothing for the run

<to_id>LGIC_BLANKFIX.TO-BF-v-2</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~5</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-v-2` (`decompositions/LGIC_BLANKFIX_DECOMP.round7.md`) | **outcome_ref:** FWD-5 |
**depends_on:** BF-v-1 merged (the instructions it reads); a new slot and a new worktree made at the trunk after that merge

---

## WORKER FACE

### CONTEXT

**What you are testing.** This project builds a naming check (LGIC): it reads the names this repository declares and
grades each one. The PRD's outcome FWD-5 (`org/missions/D14/LGIC/LGIC_BLANKFIX/prd/LGIC_BLANKFIX_PRD.md` lines 59-64) says anyone can run it from
start to finish without writing anything for it first: "a person who has never run the check follows the written instructions on a
fresh copy of the work, using only what that copy already holds, and it finishes". You are that person. You have never run it, and
this order deliberately does not tell you how. Python 3.9; ASCII only in what you write; no new dependency.

### THE CELL

`BF-v-2` (item E1, the exercise). Your worktree is a fresh copy of the trunk. Use only what it holds.

1. **Find the written instructions** the way a newcomer would: from the repository's own documents. Record every file you read to
   find them, in order, and the passage you followed.
2. **Follow them.** Record each command exactly as you ran it, its last printed lines, and the passage it came from. Run the
   repository plane only: a step that would call AWS or the network you record as `SKIPPED-LIVE` with the passage that asks for it,
   and do not run it.
3. **Write nothing for the run**: no skip list, no card, no configuration, no file outside your deliverables folder. If the run
   stops, record where and why, verbatim, and what the instructions would have needed to say; do not write anything to get past it.
4. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~5/FRESH_RUN_round7.md` with these sections, each a `## ` heading, in order: `Instructions found`,
   `Steps run`, `Final output` (one fenced block ending with the check's last printed line, copied exactly), `Written for the run`,
   `Where the instructions fell short`.
5. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~5/check_fresh_run_round7.py`: it checks the five headings in that order, that `Final output` holds a fenced
   block, and counts `outside_writes` = the entries of `git status --porcelain` in your worktree outside your deliverables folder.
   It prints `FRESH-RUN ok=True headings=5 outside_writes=0 finished=<yes|no>`; `ok=True` when the headings and the block are
   present and `outside_writes=0`; `finished` is your reading of whether the run reached its totals, reported and not required.

### ACCEPTANCE

<criterion id="BV2-AC1" cell_refs="BF-v-2"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~5/check_fresh_run_round7.py</invocation><expect>FRESH-RUN ok=True</expect></criterion>
`BV2-AC1` -- the run's record has its five parts and nothing was written outside the deliverables folder.

<criterion id="BV2-AC2" cell_refs="BF-v-2" judgment="true"/>
`BV2-AC2` (judgment) -- `3.0.0_SA_CVO` reads the run's record against FWD-5's ACCEPT (PRD lines 59-64) and the CTO's round-6 ruling on which command is the check (`ledger/ROUND_ANALYSIS.round6.md`; not for the worker to read): did a seat that had never run it, from the written instructions alone, on a fresh copy, reach its totals with nothing written for the run? You record the artifacts' paths and NO verdict.

<expected_criteria>BV2-AC1,BV2-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- Your whole build lives in your deliverables folder, which the tree convention grants; the block below names only the investigation file.
- The judgment criterion gets its artifact paths and NO verdict from you.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W5-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>

org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/registry/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round6.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round7.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round7.md</decomp_doc> (round 7), cell `BF-v-2`.
<owned_cells>BF-v-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BV2-AC1, BV2-AC2 (judgment: recorded UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming `3.0.0_SA_CVO`). Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~5/LGIC_BLANKFIX.TO-BF-v-2.fresh-seat-from-instructions.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BV2-AC1,BV2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last line whole; every file read to find the instructions; every command run and its passage; the final output; every SKIPPED-LIVE step; every place the instructions fell short; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a command taken from somewhere other than the copy's written instructions (each step cites its passage); a skip list or card written to get past a stop (outside_writes counts every file outside the deliverables folder); a stop smoothed over (the record carries it verbatim); BLIND: whether the seat had seen the command before -- a new subagent on a new slot, and neither its face nor its spawn prompt carries one.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round6.md @ea45e82c70 (the CTO's enrichment list E1 to E5); decomposition round 7. Base dry-run at the cut: BV2-AC1 base FAIL as expected (file absent).
