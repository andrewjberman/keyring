# TO LGIC_LGCTFM.TO-LT-r-2-r3 -- NO BARE "(none)": an empty column is a statement about the INSTRUMENT, never about the subject

<to_id>LGIC_LGCTFM.TO-LT-r-2-r3</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-18</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` v1.4 (ADMITTED; both halves SIGNED and current) | **Decomp cell:** `LT-r-2` (decomposition v1.4 s.13) | **outcome_ref:** FWD-1 | **depends_on:** none -- the only order on slot `~2`

---

## WORKER FACE

### THE CELL

`LT-r-2`. The graded 49F run's `flow.current.md` renders its COMPUTE column as:

```
   -- COMPUTE --
  (none)
```

while the live plane carries **9 Lambdas and 1 EC2 instance** under the subject's own token. Ruling R-79
(@`0e9027c6dc`): *"a blank that does NOT say it is a gap -- it reads as 'this subject has no compute' rather
than 'this instrument cannot see compute'. THE CONTRACT COMMITS THE EXACT FAILURE MODE ITS OWN BAR NAMES BY
NAME."* FWD-1's ACCEPT forbids *"a gap the contract left blank WITHOUT SAYING SO"*.

The line comes from `lib/lgctfm_render.py` `_columns_block()`, which writes `"  (none)"` for an empty column.
Measured at the cut: **10 bare "(none)" lines across 5 of 5 runs** under `workflows/legacy_transform/`.

### WHAT YOU BUILD

Every column section in `flow.current.md` states its COVERAGE, in one of two forms:

1. **The contract carries a `coverage` block** (a new run, after `LT-e-5`): each column prints a line
   containing **`<R> row(s) of <I> involved`**, where R and I are the SUMS of `rows` and `involved` over the
   node_types the renderer's own `NODE_TYPE_COLUMN` assigns to that column. Add whatever else helps a reader
   (not_covered names, the instrument) -- the arm checks for that phrase and those numbers.
2. **The contract carries no coverage block** (every run before this round): **EVERY column** prints a line
   containing **`NOT MEASURED`** -- including the NON-EMPTY columns, because a column with rows but no
   coverage figure can still be incomplete without saying so.

And **no rendered line in `flow.current.md` or `flow.desired.md` is exactly `(none)`** once stripped.

The coverage block's shape is fixed by `LT-e-5`'s cell and carried ONLY in the fixed input. You render it;
you never define it:

**COVERAGE BLOCK SHAPE (the one carrier is R3_BASE.json; this is a quotation of it)**

```json
{
  "coverage": {
    "instrument": "<the cell's 'involved' definition, in words>",
    "legs": ["token", "trigger_target", "iam_grant", "source_text"],
    "vintage": "<the graph's own 'Built from the estate as of ...' line>",
    "token_floor": {"pattern": "<regex>", "hits": 0, "scanned": 0},
    "by_node_type": {
      "LAMBDA": {
        "involved": 0,
        "rows": 0,
        "excluded": [{"name": "<a floor node judged NOT involved>", "reason": "<why>"}],
        "not_covered": [{"name": "<an involved node with no row>", "reason": "<why the instrument cannot row it>"}]
      }
    }
  }
}
```

⛔ **FWD-5 MUST STAY WHOLE.** Its ACCEPT is regeneration fidelity -- the same contract renders the same
picture, and changing a row changes it. `r2-regen` guards that and READS PASS AT THE CUT; it must still read
PASS after your change.

⛔ **THE RUN DIRECTORIES ARE FROZEN (R-43).** You re-render contracts into SCRATCH to prove the change; you
NEVER rewrite a `flow.*.md` inside `workflows/legacy_transform/`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="R2R3-AC1" cell_refs="LT-r-2"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_lt_r3.py r2-no-bare-none</invocation><expect>PASS-R2-NO-BARE-NONE</expect></criterion>

<criterion id="R2R3-AC2" cell_refs="LT-r-2"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_lt_r3.py r2-coverage-lines</invocation><expect>PASS-R2-COVERAGE-LINES</expect></criterion>

<criterion id="R2R3-AC3" cell_refs="LT-r-2"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_lt_r3.py r2-regen</invocation><expect>PASS-R2-REGEN</expect></criterion>

<criterion id="R2R3-AC4" cell_refs="LT-r-2" judgment="true"/>

<expected_criteria>R2R3-AC1, R2R3-AC2, R2R3-AC3, R2R3-AC4</expected_criteria>

**AC1 and AC2 READ FAIL AT THE CUT.** ⚠ **AC3 (`r2-regen`) IS GUARD-SHAPED AND READS PASS AT THE CUT** -- it
protects FWD-5, which works today; it measures nothing you build and is disclosed so its green is not read as
progress. `r2-coverage-lines` renders a contract the checker BUILDS from R3_BASE.json's shape, so your
renderer is graded against the same block `LT-e-5` writes.

**`R2R3-AC4`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether a reader of the new COMPUTE column
would learn, without opening the contract, that an empty or short column is the instrument's limit rather
than the subject's shape.

**THE CHECKER'S CONTROLS:** run `... check_lt_r3.py selftest-arms` FIRST; expect `PASS-ARMS-DISCRIMINATE`.
An arm a CORRECT renderer cannot satisfy is a BLOCKING surprise row quoting the arm and its output.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/` and this order's own file. Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **YOU DO NOT EDIT `lib/opal_lgctfm.py`** -- it has one writer this round, on slot `~1`. The renderer reads the contract; it does not change how one is produced.
- ⛔ **NOTHING UNDER `workflows/legacy_transform/` IS WRITTEN.** Render into scratch.
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump the array; assert the non-ASCII CHARACTER count and backslash-u count unchanged.
- **Id** `LGIC_LGCTFM-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time. **One other order is open this round.**
- Every `.py` edit passes `.tools/commit-gate.sh`. **Commit before you grade.**

<paths>
lib/lgctfm_render.py
org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.4, round-3 cell `LT-r-2` (section 13).
<owned_cells>LT-r-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `R2R3-AC1` through `R2R3-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/LGIC_LGCTFM.TO-LT-r-2-r3.no-bare-none.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> R2R3-AC1,R2R3-AC2,R2R3-AC3,R2R3-AC4 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-r-2-r3.no-bare-none.md` BEFORE the `complete` flip.
Result file `no-bare-none.r3.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent.
`R2R3-AC4` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the rendered COMPUTE section of the graded run before and after, the count of bare "(none)" lines across every run (before 10), and the exact coverage line format you chose.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-3 cut: no schedule is created or read.
comp-iam: RUN at the round-3 cut: no grant moves; the cell reads no AWS surface at all.
comp-adversary: RUN at the round-3 cut: the adversarial control is r2-no-bare-none's second half. The cheapest satisfying move is to replace '(none)' with '(no rows)' on EMPTY columns only, which removes the literal and keeps the lie on every partially-covered column; the arm requires NOT MEASURED in EVERY column of a no-coverage contract, including the non-empty ones. r2-regen is guard-shaped and disclosed on the worker face.
lane: <paths> is the grant; deliverables/0.9.0_WK_LGIC_LGCTFM~2/ is granted by the tree convention.
contention: the channel is shared with slot ~1 -- append-only, 14b's inversion applies. lib/lgctfm_render.py has no other writer this round.
</preflight>

Seating: slot `~2`, level 0, the only order on its slot. Round 3 of LGIC_LGCTFM, issued by `2.0.0_SA_COO~G` on decomposition v1.4 s.13, from R-79 (c). Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/`. Rulings carried: R-79, R-43, LGIC_ENFORCE-S85.
