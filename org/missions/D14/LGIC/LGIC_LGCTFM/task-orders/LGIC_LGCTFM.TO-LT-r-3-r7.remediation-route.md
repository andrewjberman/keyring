# TO LGIC_LGCTFM.TO-LT-r-3-r7 -- EVERY UNMOVED REMEDIATION ROW GETS A NEXT ACT OR AN EXPLICIT RETIREMENT

<to_id>LGIC_LGCTFM.TO-LT-r-3-r7</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-19</issued_date>
<status>complete -- 0.9.0_WK_LGIC_LGCTFM~3 @acf65699b4: R3R7-AC1/AC2/AC3 PASS-by-output, R3R7-AC4 RECORDED for 3.0.0_SA_CVO at L9; proof-of-spec-check rc=0 (VALID) over org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~3/LGIC_LGCTFM.TO-LT-r-3-r7.remediation-route.proof_of_spec.json</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` (ADMITTED; both halves SIGNED and current) | **Decomp cell:** `LT-r-3` (decomposition v1.8 s.18) | **outcome_ref:** FWD-2 | **depends_on:** none -- **three cells run side by side and NOTHING here reads another cell's work**

---

## WORKER FACE

### THE CELL

`LT-r-3`. A CENSUS-AND-ROUTE over this project's REMEDIATION rows. `1.0.0_SA_CTO` @`ed073a4d48`, making
a decision this seat handed up, verbatim: *"A remediation row unmoved for two rounds is
**indistinguishable from one nobody owns**, and `S44` is this project's own proof that silence and
progress read identically from outside. Cut it as CENSUS-AND-ROUTE -- each row gets a named owner and a
next act, or an explicit retirement -- **NOT as a fix-them-all cell, which would be nineteen unrelated
remedies in one order.**"*

⛔ **YOU REMEDY NOTHING.** Every row's remedy is its own future cell. You produce the ROUTE.

⭐ **THE NUMBER IN THAT SENTENCE IS INHERITED AND THIS SEAT MEASURED IT BEFORE CUTTING, so you do not
inherit it either.** Over `REMEDIATION_v1.md` at the cut, **denominator 35 rows**:

| predicate | count |
|---|---|
| not closed | **23** |
| not closed AND round tag <= v4 | 20 |
| not closed AND `disarm` empty | **19** |
| INERT and not closed | **19** |

**NINETEEN IS REAL UNDER TWO PREDICATES AND TWENTY-THREE IS THE BROADER UNCLOSED SET.** The analysis's
number is not wrong -- it is **PREDICATE-DEPENDENT**. So the arm refuses a record with no stated
predicate, and **you re-measure at YOUR OWN write time rather than trusting this table**: rows move.

⚠ **AND ONE PREMISE OF THE FRAMING IS ALREADY SATISFIED: 35 of 35 rows carry a non-empty `owner`.** So
"each row gets a named owner" is NOT the gap. **THE GAP IS THE NEXT ACT.** Do not spend the round
re-assigning owners that already exist -- though if you find an owner that is wrong or names a seat that
no longer holds the surface, say so in that row's `basis`.

### WHAT YOU BUILD

1. **THE DENOMINATOR**, re-counted at your own write time -- every remediation row, not just the ones
   you will route.
2. **THE PREDICATE, STATED**, and the **POPULATION as a SUBTRACTION from that denominator** (Rule 24: a
   set written as a subtraction cannot lose a member silently; a forward list omits in silence).
3. **ONE ROW PER MEMBER OF THE POPULATION**, each with `id`, the `owner` at HEAD, a **`next_act`** -- a
   concrete act, or the literal word `RETIRE` -- and a **`basis`** saying why that act, or why
   retirement. The arm requires `rows` to carry exactly `population` entries with no duplicate ids.
4. **THE DISPOSITION ARITHMETIC:** `routed` + `retired` + `unroutable` must equal `population`.
5. **`unroutable` IS AN HONEST ANSWER.** A row you genuinely cannot route -- the owner is a lane that no
   longer exists, the mechanism is unreadable, the evidence is gone -- goes there with a `why`. **There
   is a positive arm proving a record with unroutable entries PASSES.** Inventing a next act for a row
   you do not understand is worse than saying so.
6. **THE VINTAGE FIELD:** `fixed_inputs_at_pin`, mapping each fixed input you invoked to the COMMIT you
   invoked it at -- both `check_lt_r7.py` and `R7_BASE.json`, each resolvable against its path.

**RECORD SHAPE (the one carrier is `deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/R7_BASE.json`; this is a quotation of YOUR half of it)**

```json
{
  "remediation_route": {
    "denominator": 0,
    "predicate": "<the predicate that defines the population, stated>",
    "population": 0,
    "rows": [{"id": "<row id>", "owner": "<owner at HEAD>", "next_act": "<the act, or the word RETIRE>", "basis": "<why this act, or why retirement>"}],
    "retired": 0, "routed": 0,
    "unroutable": [{"id": "<row id>", "why": "<what could not be decided>"}]
  },
  "fixed_inputs_at_pin": {"<path>": "<commit>"},
  "stale_proofs": {"fixed_input_commits_since_cut": 0, "proofs_re_run": []}
}
```

Write it to `<WS>/org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~3/REMEDIATION_ROUTE_R7.json`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="R3R7-AC1" cell_refs="LT-r-3"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/check_lt_r7.py r3-route</invocation><expect>PASS-R3-ROUTE</expect></criterion>

<criterion id="R3R7-AC2" cell_refs="LT-r-3"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/check_lt_r7.py r7-vintage-field</invocation><expect>PASS-R7-VINTAGE-FIELD</expect></criterion>

<criterion id="R3R7-AC3" cell_refs="LT-r-3"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/check_lt_r7.py r7-stale-proofs</invocation><expect>PASS-R7-STALE-PROOFS</expect></criterion>

<criterion id="R3R7-AC4" cell_refs="LT-r-3" judgment="true"/>

<expected_criteria>R3R7-AC1, R3R7-AC2, R3R7-AC3, R3R7-AC4</expected_criteria>

**WIRING AT THE CUT -- AND EACH RED NAMES THE ACT THAT CLEARS IT.** ⛔ **This clause exists because the
previous round's wiring note did NOT distinguish a red a cell can clear from one it structurally
cannot, and a worker rationalised a structural bar as an expected red** (`LGIC_ENFORCE-S106`).

| criterion | at the cut | WHICH ACT CLEARS IT |
|---|---|---|
| `R3R7-AC1` | **FAIL** | **YOURS ALONE** -- writing your record. No other cell can affect it. |
| `R3R7-AC2` | **FAIL** | **YOURS ALONE** -- the arm grades only the records present in YOUR checkout. |
| `R3R7-AC3` | **PASS**, guard-shaped | nothing -- its window is empty until a fixed input moves. |

⚠ **WHAT THE MECHANICAL ARMS CANNOT SEE:** the arm checks that your arithmetic closes, that every member
has a next act with a basis, and that the predicate is stated. **It never opens the remediation
channel.** A PASS means your record is internally coherent, never that the population is the real one.
That half is `AC4`'s.

**`R3R7-AC4`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether the denominator matches the
channel at the claimed write time; whether the population follows from the stated predicate rather than
from convenience; whether each `next_act` is an act somebody could actually take; and whether any
`RETIRE` is justified by evidence rather than by age.

⭐ **THE BAR, and you may hold me to it:** every criterion was checked against a HAND-BUILT CORRECT
RECORD before this order shipped, driven in the self-test as a POSITIVE-SATISFIABILITY arm (34 arms, 10
positive, **4 driving the WIRING**). *"Can a CORRECT artifact FROM THIS CELL ALONE satisfy this? Where
the honest answer is no, THE CRITERION IS THE DEFECT, NOT THE CELL."* **Two such criteria were found and
repaired in this project's sibling last round -- one by me before issuing, one by BOTH workers after.
If you find a third, file it BLOCKING and keep working.**

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~3/` and this order's own file. Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **`surprise-channel/remediations/REMEDIATION_v1.md` IS READ-ONLY TO YOU.** ⚠ **REMEDIATION ROWS ARE `3.0.0_SA_CVO`'s TO WRITE** -- you do not edit, close, disarm or re-own a single one. Your route lands in YOUR OWN record and the CVO acts on it at L9.
- ⛔ **THE OTHER TWO CELLS ARE NOT YOURS** (`LT-n-3` the node-type population, `LT-g-1` the gate scope). Your record has no field of theirs and no arm of yours reads their records.
- **If you reach for an instrument OUTSIDE the repo:** name where it LANDS in the repo, **and every fixture must CITE the committed measurement it encodes.** **And name every site where it DIVERGES from the code it models, with what the divergence ASSUMES.** (`1.0.0_SA_CTO` @`ed073a4d48`.)
- **Surprises** by **TEXTUAL SPLICE** into the INVESTIGATION fence that PARSES AS A LIST -- **never into the remediations file**; preserve line endings exactly.
- **Id** `LGIC_LGCTFM-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time. **`S44` is taken; two other orders are open this round and may file rows while you work.**
- Every `.py` edit passes `.tools/commit-gate.sh`. **Commit before you grade.**

<paths>
org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.8, round-7 cell `LT-r-3` (section 18).
<owned_cells>LT-r-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `R3R7-AC1` through `R3R7-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~3/LGIC_LGCTFM.TO-LT-r-3-r7.remediation-route.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> R3R7-AC1,R3R7-AC2,R3R7-AC3,R3R7-AC4 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-r-3-r7.remediation-route.md` BEFORE the `complete` flip.
Result file `remediation-route.r7.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent. Your recorded invocation must match the order's literal text INCLUDING `timeout 900`.
`R3R7-AC4` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the denominator, the predicate
in your own words, the population as a subtraction, the counts of routed / retired / unroutable, and
every `RETIRE` with its basis. Name any owner you found to be wrong or stale.

---

## RECORD FACE

⛔ **THE ONE-LINE RECUT THIS ROUND CARRIES, FOR `3.0.0_SA_CVO` AT L9** (`1.0.0_SA_CTO` @`ed073a4d48`):
**"DO NOT PAIR" BINDS THE CRITERION, NOT ONLY THE CELL.** Three cells here are separated at the order,
the record AND the arm: every cell arm reads exactly one record, and the two round-wide arms grade the
records PRESENT IN THE CHECKOUT rather than a hard-coded tuple. That is the `S106` repair carried
forward into the cut rather than re-learned after it.

⚠ **AND THE ROUTE THIS CELL PRODUCES IS EVIDENCE, NOT A DISPOSITION.** The cell writes a route into its
own record; the remediation rows themselves stay `3.0.0_SA_CVO`'s to write. An issuer's or a worker's
route that closed a row itself would be exactly the self-certification R-19 forbids.

<preflight>
comp-schedule: RUN at the round-7 cut: no schedule is created or read.
comp-iam: RUN at the round-7 cut: no grant moves.
comp-adversary: RUN at the round-7 cut: the cheapest satisfying move is to take the 19 from this order's own table and route exactly those, so the arm refuses a record with no STATED predicate and requires the population to sit inside a denominator the cell re-counted itself; the second-cheapest is a plausible-sounding next_act for a row nobody understands, so `unroutable` is explicitly admissible WITH a reason and has its own positive arm. What no mechanical arm here can see is whether the population is the real one -- stated on the order and routed to AC4.
lane: <paths> is the grant; deliverables/0.9.0_WK_LGIC_LGCTFM~3/ by the tree convention. REMEDIATION_v1.md has NO writer this round and is 3.0.0_SA_CVO's surface.
contention: the channel is shared -- append-only, 14b's inversion applies. Three cells write three disjoint deliverable directories.
</preflight>

Seating: slot `~3`, level 0, one of THREE orders this round. Round 7 of LGIC_LGCTFM, issued by
`2.0.0_SA_COO~G` on decomposition v1.8 s.18, from `1.0.0_SA_CTO`'s round-6 analysis @`ed073a4d48` and
`LGIC_LGCTFM-S44`. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/` (`check_lt_r7.py`,
`R7_BASE.json` pinning `ed073a4d48`). Rulings carried: S85's ONE CARRIER, the cut-time criterion bar,
S106's criterion-level non-pairing, R-19, ADDENDUM 3's vintage field, LD-0521, Rule 24's subtraction and
its inherited-count clause.
