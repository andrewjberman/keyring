# TO LGIC_LGCTFM.TO-LT-n-3-r7 -- WHAT THE ENGINE ACTUALLY EMITS, AGAINST THE ENUM'S 33, BY SUBTRACTION

<to_id>LGIC_LGCTFM.TO-LT-n-3-r7</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-19</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` (ADMITTED; both halves SIGNED and current) | **Decomp cell:** `LT-n-3` (decomposition v1.8 s.18) | **outcome_ref:** FWD-2 | **depends_on:** none -- **three cells run side by side and NOTHING here reads another cell's work**

---

## WORKER FACE

### THE CELL

`LT-n-3`. `LGIC_LGCTFM-W2-S2` has been ARMED and BLOCKING since round 2: **every walk emits a
`COGNITO_USER_POOL` row whose `node_type` sits OUTSIDE `org/standards/LGCTFM_CONTRACT.schema.json`'s
33-value `node_type` enum, so NO REAL CONTRACT the engine produces can validate against its own
schema.** Rounds 4, 5 and 6 went elsewhere and the row did not move; that is recorded as
`LGIC_LGCTFM-S44`, filed by this seat rather than carried silently.

⛔ **IT IS A MEASUREMENT. YOU DECIDE NOTHING AND YOU FIX NOTHING.** `1.0.0_SA_CTO`, round-6 analysis
@`ed073a4d48`, verbatim: *"Cut it as a MEASUREMENT of which node types the engine ACTUALLY emits
against the enum's 33, read BY SUBTRACTION from the emitted set, not by checking the ones anybody
remembers ... **The fork (widen the enum vs refuse at the producer) is decided ON that measurement, not
before it.**"* A cell that picks the fork makes the numbers agree instead of the data.

### WHAT YOU BUILD

1. **THE EMITTED SET, FROM A RUN YOU MADE.** Every distinct `node_type` the engine actually produces,
   with its denominator, and `how_emitted_was_obtained` naming **the invocation you RAN** -- not the
   inference you drew. Read it off the run's own output; do not assemble it from the enum you just read.
2. **THE DECLARED SET, AT A PIN.** The enum from `LGCTFM_CONTRACT.schema.json`, with its denominator and
   the `schema_pin` commit you read it at. ⚠ **The "33" in `W2-S2` is a round-2 figure. It may have
   moved. Print what YOU read.**
3. **BOTH DIFFERENCES, AND THE ARM RE-DERIVES THEM FROM YOUR OWN LISTS.** `emitted_minus_declared` is
   the violation class `W2-S2` names. `declared_minus_emitted` -- enum values nothing emits -- is a
   **finding, not a defect claim**, and it is required because a set written as a subtraction from a
   printed denominator cannot lose a member silently (Rule 24).
4. **THE VINTAGE FIELD:** `fixed_inputs_at_pin`, mapping each fixed input you invoked to the COMMIT you
   invoked it at -- both `check_lt_r7.py` and `R7_BASE.json`, each resolvable against its path.

⭐ **A SMALL ANSWER PASSES AND THE SELF-TEST PROVES IT.** `emitted_minus_declared` of exactly ONE is as
admissible as a large set, **and so is ZERO** if the enum has moved since round 2 -- there is a positive
arm for each. **A bar that only passed on a violation would be an instruction to find one.** What is
refused is a difference your record ASSERTS that your own lists do not support.

**RECORD SHAPE (the one carrier is `deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/R7_BASE.json`; this is a quotation of YOUR half of it)**

```json
{
  "node_types": {
    "emitted": ["<node_type>"], "emitted_denominator": 0,
    "declared": ["<node_type>"], "declared_denominator": 0,
    "emitted_minus_declared": ["<the violation class>"],
    "declared_minus_emitted": ["<enum values nothing emits -- a finding, NOT a defect claim>"],
    "how_emitted_was_obtained": "<the instrument RUN, with its invocation>",
    "schema_pin": "<commit of LGCTFM_CONTRACT.schema.json read>"
  },
  "fixed_inputs_at_pin": {"<path>": "<commit>"},
  "stale_proofs": {"fixed_input_commits_since_cut": 0, "proofs_re_run": []}
}
```

Write it to `<WS>/org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/NODE_TYPE_POPULATION_R7.json`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="N3R7-AC1" cell_refs="LT-n-3"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/check_lt_r7.py n3-population</invocation><expect>PASS-N3-POPULATION</expect></criterion>

<criterion id="N3R7-AC2" cell_refs="LT-n-3"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/check_lt_r7.py r7-vintage-field</invocation><expect>PASS-R7-VINTAGE-FIELD</expect></criterion>

<criterion id="N3R7-AC3" cell_refs="LT-n-3"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/check_lt_r7.py r7-stale-proofs</invocation><expect>PASS-R7-STALE-PROOFS</expect></criterion>

<criterion id="N3R7-AC4" cell_refs="LT-n-3" judgment="true"/>

<expected_criteria>N3R7-AC1, N3R7-AC2, N3R7-AC3, N3R7-AC4</expected_criteria>

**WIRING AT THE CUT -- AND EACH RED NAMES THE ACT THAT CLEARS IT.** ⛔ **This clause exists because the
previous round's wiring note did NOT distinguish a red a cell can clear from one it structurally
cannot, and a worker rationalised a structural bar as an expected red** (`LGIC_ENFORCE-S106`).

| criterion | at the cut | WHICH ACT CLEARS IT |
|---|---|---|
| `N3R7-AC1` | **FAIL** | **YOURS ALONE** -- writing your record. No other cell can affect it. |
| `N3R7-AC2` | **FAIL** | **YOURS ALONE** -- the arm grades only the records present in YOUR checkout. |
| `N3R7-AC3` | **PASS**, guard-shaped | nothing -- its window is empty until a fixed input moves. |

⚠ **WHAT THE MECHANICAL ARMS CANNOT SEE:** the arm checks your record's internal consistency and
re-derives both differences from your own lists. **It cannot run the engine, and it cannot tell whether
your emitted set came from a real walk.** A PASS means your arithmetic is honest, never that the run
happened. That half is `AC4`'s.

**`N3R7-AC4`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether the emitted set came from a real
run at the stated invocation; whether the declared set was read at the stated pin; whether the emitted
set was read off the run rather than assembled from the enum; and whether any node type was dropped
between the run and the record.

⭐ **THE BAR, and you may hold me to it:** every criterion was checked against a HAND-BUILT CORRECT
RECORD before this order shipped, driven in the self-test as a POSITIVE-SATISFIABILITY arm (34 arms, 10
positive, **4 driving the WIRING**). *"Can a CORRECT artifact FROM THIS CELL ALONE satisfy this? Where
the honest answer is no, THE CRITERION IS THE DEFECT, NOT THE CELL."* **Two such criteria were found and
repaired in this project's sibling last round -- one by me before issuing, one by BOTH workers after.
If you find a third, file it BLOCKING and keep working.**

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/` and this order's own file. Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **`org/standards/LGCTFM_CONTRACT.schema.json` AND `lib/opal_lgctfm.py` ARE NOT YOURS.** You READ both. Widening the enum and refusing at the producer are the two arms of a fork **the CTO decides on your measurement**. Touching either is deciding it.
- ⛔ **THE OTHER TWO CELLS ARE NOT YOURS** (`LT-g-1` the gate scope, `LT-r-3` the remediation route). Your record has no field of theirs and no arm of yours reads their records.
- **If you reach for an instrument OUTSIDE the repo:** name where it LANDS in the repo, **and every fixture must CITE the committed measurement it encodes** -- an instrument whose fixtures cite nothing is ungradeable even when preserved perfectly. **And name every site where it DIVERGES from the code it models, with what the divergence ASSUMES.** (`1.0.0_SA_CTO` @`ed073a4d48`.)
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump; preserve line endings exactly. Copy an existing row's field set exactly.
- **Id** `LGIC_LGCTFM-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time. **`S44` is taken; two other orders are open this round and may file rows while you work, so re-measure rather than reserve.**
- Every `.py` edit passes `.tools/commit-gate.sh`. **Commit before you grade.**

<paths>
org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.8, round-7 cell `LT-n-3` (section 18).
<owned_cells>LT-n-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `N3R7-AC1` through `N3R7-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-n-3-r7.node-type-population.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> N3R7-AC1,N3R7-AC2,N3R7-AC3,N3R7-AC4 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-n-3-r7.node-type-population.md` BEFORE the `complete` flip.
Result file `node-type-population.r7.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent. Your recorded invocation must match the order's literal text INCLUDING `timeout 900` -- the invocation-alignment limb compares them.
`N3R7-AC4` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the emitted set with its
denominator and the invocation that produced it, the declared set with its denominator and pin, and BOTH
differences. If `emitted_minus_declared` is empty, say so plainly -- that is a result, not a failure.

---

## RECORD FACE

⛔ **THE ONE-LINE RECUT THIS ROUND CARRIES, FOR `3.0.0_SA_CVO` AT L9** (`1.0.0_SA_CTO` @`ed073a4d48`):
**"DO NOT PAIR" BINDS THE CRITERION, NOT ONLY THE CELL.** Three cells here are separated at the order,
the record AND the arm: every cell arm reads exactly one record, and the two round-wide arms grade the
records PRESENT IN THE CHECKOUT rather than a hard-coded tuple. That is the `S106` repair carried
forward into the cut rather than re-learned after it.

<preflight>
comp-schedule: RUN at the round-7 cut: no schedule is created or read.
comp-iam: RUN at the round-7 cut: no grant moves.
comp-adversary: RUN at the round-7 cut: the cheapest satisfying move is to read the enum and echo it back as the emitted set, which would make emitted_minus_declared empty by construction -- so the record must name the INVOCATION that produced the emitted set, the arm re-derives BOTH differences from the record's own lists, and the order states that a ZERO answer is admissible so there is no incentive to manufacture a violation either way. What no mechanical arm here can see is whether the walk was run at all -- stated on the order and routed to AC4.
lane: <paths> is the grant; deliverables/0.9.0_WK_LGIC_LGCTFM~1/ by the tree convention. The schema and the engine have NO writer this round.
contention: the channel is shared -- append-only, 14b's inversion applies. Three cells write three disjoint deliverable directories.
</preflight>

Seating: slot `~1`, level 0, one of THREE orders this round. Round 7 of LGIC_LGCTFM, issued by
`2.0.0_SA_COO~G` on decomposition v1.8 s.18, from `1.0.0_SA_CTO`'s round-6 analysis @`ed073a4d48` and
`W2-S2`. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/` (`check_lt_r7.py`, `R7_BASE.json`
pinning `ed073a4d48`). Rulings carried: S85's ONE CARRIER, the cut-time criterion bar, S106's
criterion-level non-pairing, ADDENDUM 3's vintage field, LD-0521, Rule 24's subtraction.
