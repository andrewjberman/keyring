# TO LGIC_LGCTFM.TO-LT-g-1-r7 -- WHAT THE NAMING GATE REFUSES, ON WHAT BASIS, WITH A PATH IT ADMITS

<to_id>LGIC_LGCTFM.TO-LT-g-1-r7</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-19</issued_date>
<status>issued</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` (ADMITTED; both halves SIGNED and current) | **Decomp cell:** `LT-g-1` (decomposition v1.8 s.18) | **outcome_ref:** FWD-2 | **depends_on:** none -- **three cells run side by side and NOTHING here reads another cell's work**

---

## WORKER FACE

### THE CELL

`LT-g-1`. `LGIC_LGCTFM-W2-S1` has been ARMED and BLOCKING since round 2, **and its disarm owner is
`1.0.0_SA_CTO`, not this fabric's COO**: `DEC-9`'s MARK COMMIT AND THE ENGINE'S OWN RUN ARTIFACTS ARE
NOT COMMITTABLE AT `DEC-12`'s RUN HOME -- `.tools/naming-gate.py` in ENFORCE mode refuses
`contract.json`, `plan.json`, `PLANT.json`, `PLANT_UNTYPEABLE.json` and `MARK.json` wholesale.

⛔ **IT IS A MEASUREMENT AND YOU PROPOSE NO GATE EDIT.** The gate is `1.0.0_SA_CTO`'s artifact and that
seat holds the row's clock. Your job is to make the refusal **legible enough to act on**: which paths,
by which predicate, on what basis -- and to prove the guard is SCOPED rather than broken.

### WHAT YOU BUILD

1. **THE REFUSED SET, WITH THE GATE'S OWN OUTPUT LINE PER PATH.** Not your paraphrase -- the line the
   gate printed. With a denominator: how many paths you put through it.
2. **THE REFUSING PREDICATE, NAMED AT `file:line`.** The code that actually refuses, read at a pin.
   `gate_pin` records the commit you read the gate at -- **it is another seat's live artifact and it
   moves.**
3. **THE REFUSAL BASIS: `FILENAME`, `PATH` or `CONTENT`** -- exactly one. ⭐ **This is the field that
   decides whether a RENAME lapses the guard silently**, and it is the difference between a remedy that
   renames the artifacts and one that widens the gate. Read it off the predicate, not off the symptom.
4. **AN ADMITTING CONTROL.** A path the gate **ADMITS**, through the same invocation, with its output
   line. ⛔ **Without it a scoped guard and a gate that refuses everything read IDENTICALLY**, and the
   arm refuses a record whose "admitting" path also appears in the refused list.
5. **THE VINTAGE FIELD:** `fixed_inputs_at_pin`, mapping each fixed input you invoked to the COMMIT you
   invoked it at -- both `check_lt_r7.py` and `R7_BASE.json`, each resolvable against its path.

⚠ **IF THE GATE NO LONGER REFUSES THESE PATHS, THAT IS THE RESULT** -- and it is what happened.

⛔ **THE RESIDUAL THIS ORDER DISCLOSED AT THE CUT FIRED, AND THE ARM IS REPAIRED.** The first cut
required a NON-EMPTY refused set, so a genuinely-empty one could not be satisfied by any correct
artifact. `0.9.0_WK_LGIC_LGCTFM~2` measured **0 of 5** refused, filed `LGIC_LGCTFM-W2-S45` BLOCKING
**rather than manufacturing a refusal**, and did not flip its order. That was exactly right, and the
defect was mine. **`W2-S1` IS ALREADY REMEDIED**: `1.0.0_SA_CTO`'s R-35 fix @`5fd4251792` is an ancestor
of this round's cut pin -- it landed BEFORE the round was cut, and nobody had noticed, which is the
`S44` class again.

**SO THE ARM NOW ADMITS TWO SHAPES:**

- **(A) THE GATE STILL REFUSES** -- a refused set, a predicate at `file:line`, a `refusal_basis` from
  the enum, and an ADMITTING control.
- **(B) THE GATE NO LONGER REFUSES** -- an EMPTY refused set, with `why_zero`, the EXCLUDING predicate
  at `file:line`, and a **`scoping_control`**: a path in the SAME tree the gate **DOES** refuse,
  `refused: true`, with its output line.

⭐ **THE DISCRIMINATOR IS PRESERVED EXACTLY WHERE IT MATTERS.** Branch (B) is not a weakening: without
the scoping control, **a scoped carve-out and a gate that has gone silent everywhere read identically**
-- and that is the whole question this cell exists to answer.

**RECORD SHAPE (the one carrier is `deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/R7_BASE.json`; this is a quotation of YOUR half of it)**

```json
{
  "gate_scope": {
    "refused": [{"path": "<path>", "verdict": "<the gate's own output line>"}],
    "refused_denominator": 0,
    "refusing_predicate": "<file:line of the code that REFUSES (branch A) or EXCLUDES (branch B)>",
    "refusal_basis": "<FILENAME|PATH|CONTENT -- branch A only; empty on branch B>",
    "admitting_control": {"path": "<a path the gate ADMITS>", "verdict": "<its output line>"},
    "why_zero": "<branch B only: what produced the empty refused set>",
    "scoping_control": {"path": "<branch B only: a path in the SAME tree the gate DOES refuse>", "verdict": "<its output line>", "refused": true},
    "gate_pin": "<commit of .tools/naming-gate.py read>"
  },
  "fixed_inputs_at_pin": {"<path>": "<commit>"},
  "stale_proofs": {"fixed_input_commits_since_cut": 0, "proofs_re_run": []}
}
```

⚠ **Any other field you find useful is welcome and the arm ignores it** -- the first pass of this cell
carried `measured_paths`, `invocation`, `gate_output_verbatim`, `rc` and a corroboration field, and all
of them made the record better. **The named fields above are the floor, not the ceiling.**

Write it to `<WS>/org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/GATE_SCOPE_R7.json`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="G1R7-AC1" cell_refs="LT-g-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/check_lt_r7.py g1-scope</invocation><expect>PASS-G1-SCOPE</expect></criterion>

<criterion id="G1R7-AC2" cell_refs="LT-g-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/check_lt_r7.py r7-vintage-field</invocation><expect>PASS-R7-VINTAGE-FIELD</expect></criterion>

<criterion id="G1R7-AC3" cell_refs="LT-g-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/check_lt_r7.py r7-stale-proofs</invocation><expect>PASS-R7-STALE-PROOFS</expect></criterion>

<criterion id="G1R7-AC4" cell_refs="LT-g-1" judgment="true"/>

<expected_criteria>G1R7-AC1, G1R7-AC2, G1R7-AC3, G1R7-AC4</expected_criteria>

**WIRING AT THE CUT -- AND EACH RED NAMES THE ACT THAT CLEARS IT.** ⛔ **This clause exists because the
previous round's wiring note did NOT distinguish a red a cell can clear from one it structurally
cannot, and a worker rationalised a structural bar as an expected red** (`LGIC_ENFORCE-S106`).

| criterion | at the cut | WHICH ACT CLEARS IT |
|---|---|---|
| `G1R7-AC1` | **FAIL** | **YOURS ALONE** -- writing your record. No other cell can affect it. |
| `G1R7-AC2` | **FAIL** | **YOURS ALONE** -- the arm grades only the records present in YOUR checkout. |
| `G1R7-AC3` | **PASS**, guard-shaped | nothing -- its window is empty until a fixed input moves. |

⚠ **WHAT THE MECHANICAL ARMS CANNOT SEE:** the arm checks that you recorded a refusal, a predicate at a
site, a basis from the enum and a distinct admitting control. **It never runs the gate.** A PASS means
your record is structurally sound, never that the gate said what you wrote. That half is `AC4`'s.

**`G1R7-AC4`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether each verdict line is the gate's
actual output at the stated pin; whether the predicate at `file:line` is the code that truly refuses
rather than a plausible neighbour; whether the basis is read off the predicate rather than inferred from
the filenames; and whether the admitting control went through the SAME invocation.

⭐ **THE BAR, and you may hold me to it:** every criterion was checked against a HAND-BUILT CORRECT
RECORD before this order shipped, driven in the self-test as a POSITIVE-SATISFIABILITY arm (34 arms, 10
positive, **4 driving the WIRING**). *"Can a CORRECT artifact FROM THIS CELL ALONE satisfy this? Where
the honest answer is no, THE CRITERION IS THE DEFECT, NOT THE CELL."* **Two such criteria were found and
repaired in this project's sibling last round -- one by me before issuing, one by BOTH workers after.
If you find a third, file it BLOCKING and keep working.**

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/` and this order's own file. Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **`.tools/naming-gate.py` IS NOT YOURS AND IS NOT THIS ROUND'S EDIT.** It is `1.0.0_SA_CTO`'s artifact and that seat holds `W2-S1`'s clock. Read it, run it, pin it. Do not change it and do not propose the change in your record -- the record carries the MEASUREMENT.
- ⛔ **THE OTHER TWO CELLS ARE NOT YOURS** (`LT-n-3` the node-type population, `LT-r-3` the remediation route). Your record has no field of theirs and no arm of yours reads their records.
- **Running the gate on scratch paths is expected.** Put them outside the repo or under your own deliverables directory; do not commit artifacts you created only to feed the gate, beyond what your record cites.
- **If you reach for an instrument OUTSIDE the repo:** name where it LANDS in the repo, **and every fixture must CITE the committed measurement it encodes.** **And name every site where it DIVERGES from the code it models, with what the divergence ASSUMES.** (`1.0.0_SA_CTO` @`ed073a4d48`.)
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump; preserve line endings exactly.
- **Id** `LGIC_LGCTFM-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time. **`S44` is taken; two other orders are open this round and may file rows while you work.**
- Every `.py` edit passes `.tools/commit-gate.sh`. **Commit before you grade.**

<paths>
org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.8, round-7 cell `LT-g-1` (section 18).
<owned_cells>LT-g-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `G1R7-AC1` through `G1R7-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/LGIC_LGCTFM.TO-LT-g-1-r7.gate-scope.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> G1R7-AC1,G1R7-AC2,G1R7-AC3,G1R7-AC4 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-g-1-r7.gate-scope.md` BEFORE the `complete` flip.
Result file `gate-scope.r7.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent. Your recorded invocation must match the order's literal text INCLUDING `timeout 900`.
`G1R7-AC4` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT every refused path with the
gate's own line, the predicate at `file:line`, the basis and why the predicate implies it, and the
admitting control with its line. If the gate no longer refuses, print that instead -- and say what you
ran.

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
comp-adversary: RUN at the round-7 cut: the cheapest satisfying move is to record a refusal from the ROW's round-2 text rather than from a run, which is why every refused entry carries the gate's OWN output line and the record carries a gate_pin; the second-cheapest is an "admitting" control that is not actually admitted, so the arm refuses a control whose path also appears in the refused list. What no mechanical arm here can see is whether the gate was run at all -- stated on the order and routed to AC4. RESIDUAL DISCLOSED AT THE CUT, AND IT FIRED: the first cut of the arm required a NON-EMPTY refused set, so a genuinely-empty one could not be satisfied by any correct artifact. 0.9.0_WK_LGIC_LGCTFM~2 measured 0 of 5, filed LGIC_LGCTFM-W2-S45 BLOCKING rather than manufacturing a refusal, and did not flip its order. The arm is REPAIRED to admit branch (B) -- an empty refused set WITH why_zero, the excluding predicate at file:line, and a scoping control proving the gate still refuses something in the same tree. The discriminator is preserved: without that control a scoped carve-out and a gate gone silent everywhere read identically. Disclosing the residual at the cut is what made the worker file it instead of working around it.
lane: <paths> is the grant; deliverables/0.9.0_WK_LGIC_LGCTFM~2/ by the tree convention. .tools/naming-gate.py has NO writer this round.
contention: the channel is shared -- append-only, 14b's inversion applies. Three cells write three disjoint deliverable directories.
</preflight>

Seating: slot `~2`, level 0, one of THREE orders this round. Round 7 of LGIC_LGCTFM, issued by
`2.0.0_SA_COO~G` on decomposition v1.8 s.18, from `1.0.0_SA_CTO`'s round-6 analysis @`ed073a4d48` and
`W2-S1`. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/` (`check_lt_r7.py`, `R7_BASE.json`
pinning `ed073a4d48`). Rulings carried: S85's ONE CARRIER, the cut-time criterion bar, S106's
criterion-level non-pairing, ADDENDUM 3's vintage field, LD-0521.
