# TO LGIC_LGCTFM.TO-LT-r-1-r10 -- SPLIT THE FLAT CLASS, THEN TAKE THE RE-ROUTE THAT EXISTS

<to_id>LGIC_LGCTFM.TO-LT-r-1-r10</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-19</issued_date>
<status>complete -- 0.9.0_WK_LGIC_LGCTFM~1 @a1d048eb84 (branch wk-lgic-lgctfm-10-1). R1R10-AC1 PASS-R1-RECLASS, R1R10-AC2 PASS-R1-REROUTE, R1R10-AC3 PASS-R10-VINTAGE-FIELD, R1R10-AC4 PASS-R10-STALE-PROOFS (all rc=0); R1R10-AC5 UNVERIFIABLE-BY-INSTRUMENT (judgment, routed to 3.0.0_SA_CVO at L9). Record c0bf6d3021 (ROUTED_ROW_RECLASS_R10.json + fixed_inputs/r1/DRIFT_CAUSES.md); check_lt_r1.py blob unchanged (8835d6519b67d96bb6bc07b4230c0be81a4590f0 at base and HEAD). proof-of-spec-check: VALID (rc=0), acceptance rows=5, violations=0. No row disarmed; S18/W1-S21 disposition owed to 3.0.0_SA_CVO at L9, disarm to 2.0.0_SA_COO~G under R-19.</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` (ADMITTED; both halves SIGNED and current) | **Decomp cell:** `LT-r-1` (decomposition v1.11 s.21) | **outcome_ref:** FWD-6 | **depends_on:** none -- **the only cell this round**

---

## WORKER FACE

### THE CELL

Round 9 classed two rows `UNEXECUTABLE-AS-ROUTED`. `3.0.0_SA_CVO` graded that PASS **and then found
what the class costs**, and `1.0.0_SA_CTO` turned it into a taxonomy act:

> ⛔ **"THE RECORD FLATTENS A DISTINCTION THAT MATTERS: a future round reading
> `UNEXECUTABLE-AS-ROUTED x2` will treat both as equally blocked when ONE HAS A CHEAP ADDITIVE
> RE-ROUTE AND THE OTHER HAS NONE."**

| row | asks for | conformant alternative |
|---|---|---|
| `S18` | an **ARM** in `check_lt_r1.py` | **NONE** -- an arm is dispatched by the checker's own CMD table and no sibling can add one |
| `W1-S21` | **DOCUMENTATION**, carried *"where a later re-derivation will meet them"* | ⭐ **EXISTS** -- a sibling document in `fixed_inputs/r1/`, the `RETIRED.md` shape |

**The class name was right** -- *"AS ROUTED"* is the operative qualifier. **The RECORD was lossy.**
You fix the record, and you take the re-route that exists.

### THE SPLIT

- **`UNEXECUTABLE-AS-ROUTED-RE-ROUTABLE`** -- the routed form is barred AND a conformant alternative
  EXISTS. **The row NAMES the alternative.**
- **`UNEXECUTABLE-IN-PRINCIPLE`** -- no conformant form exists from any cell so barred. **The row
  NAMES what would have to change for one to exist.**

⛔ **BOTH CLASSES MUST NAME SOMETHING, and the checker enforces it.** `UNEXECUTABLE-IN-PRINCIPLE` is
where a cell could park work it did not want to do, so **a row that says only "blocked" satisfies
neither class.**

⚠ **RE-DERIVE THE POPULATION FROM THE ROUND-9 RECORD**, not from this order's table. The arm reads
`ROUTED_ROW_REMEDY_R9.json` for the rows actually carrying the flat value and compares by SET EQUALITY.
**The record is the authority; this table is a framing control.**

### THE RE-ROUTE YOU PERFORM

**`W1-S21`: add a sibling document in `fixed_inputs/r1/`** carrying the three drift causes, on the
`RETIRED.md` precedent. **Cheap, additive, and it closes a row that has been reading as blocked.**

**It must say, about itself, what it does NOT close:** it adds no arm, does not change
`check_lt_r1.py`'s output, and does not make `x2-flag` or `x3-filed` distinguish an empty window from a
satisfied one. **That is `S18`'s, and `S18` has no conformant form.**

### ⛔ THE ADDITIVITY PROOF IS ANCHORED TO YOUR OWN BASE, NOT TO A ROUND PIN

`LGIC_ENFORCE` round 16 proved additivity against a **round-13 pin**, and that worked because **exactly
one commit had ever touched that file.**

⚠ **`check_lt_r1.py` HAS SIX COMMITS TOUCHING IT** (`ef8197ed07`, `56dbaee026`, `60aac06844`,
`8db9eb1bd9`, `e1ffe52bdf`, `39e6977e95`) -- legitimate repairs **during** round 1, before it closed.
**A blob-vs-round-1-pin comparison would FAIL ON HONEST HISTORY**, and I did not cut one.

**Your record carries `pinned_input_blob_at_base` and `pinned_input_blob_at_head` and they must be
IDENTICAL** -- which proves **YOU** did not touch it, the only thing this round can be responsible for.
⛔ **And the arm separately checks your claimed HEAD blob against the TREE, so you cannot assert
additivity by writing the same string twice.**

### WHAT YOU PRODUCE

A record at
`<WS>/org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/ROUTED_ROW_RECLASS_R10.json`
in exactly the shape `R10_BASE.json` carries (`record_shape`, the ONE carrier -- `S85`): a `reclass`
block (`base_sha`, `source_record`, `how_enumerated`, `population`, `rows[]` each with `id`,
`prior_class`, `new_class`, `base_sha`, `names`, `evidence`, plus the two counts) and a `re_route`
block (`row`, `artifact`, `precedent`, the two blobs, `what_it_does_not_close`). Plus
`fixed_inputs_at_pin` and `stale_proofs` per the base.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="R1R10-AC1" cell_refs="LT-r-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r10/check_lt_r10.py r1-reclass</invocation><expect>PASS-R1-RECLASS</expect></criterion>

<criterion id="R1R10-AC2" cell_refs="LT-r-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r10/check_lt_r10.py r1-reroute</invocation><expect>PASS-R1-REROUTE</expect></criterion>

<criterion id="R1R10-AC3" cell_refs="LT-r-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r10/check_lt_r10.py r10-vintage-field</invocation><expect>PASS-R10-VINTAGE-FIELD</expect></criterion>

<criterion id="R1R10-AC4" cell_refs="LT-r-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r10/check_lt_r10.py r10-stale-proofs</invocation><expect>PASS-R10-STALE-PROOFS</expect></criterion>

<criterion id="R1R10-AC5" cell_refs="LT-r-1" judgment="true"/>

<expected_criteria>R1R10-AC1, R1R10-AC2, R1R10-AC3, R1R10-AC4, R1R10-AC5</expected_criteria>

**WIRING AT THE CUT -- AND EACH RED NAMES THE ACT THAT CLEARS IT.**

| criterion | at the cut | WHICH ACT CLEARS IT |
|---|---|---|
| `R1R10-AC1` | **FAIL** | **YOURS ALONE** -- writing the reclass block. |
| `R1R10-AC2` | **FAIL** | **YOURS ALONE** -- adding the sibling document and recording the blobs. |
| `R1R10-AC3` | **FAIL** | **YOURS ALONE** -- the arm grades only the records present in YOUR checkout. |
| `R1R10-AC4` | **FAIL** | **YOURS ALONE** -- same reason; it refuses an empty population rather than passing it vacuously. |

⚠ **WHAT THE MECHANICAL ARM DOES AND DOES NOT SEE.** It re-derives your population from the round-9
record by SET EQUALITY; it requires a `names` on BOTH classes, a `base_sha` on every row, the sibling
to EXIST and to sit in `fixed_inputs/r1/`, and the two blobs to be identical **and** to agree with the
tree. ⛔ **It never reads the sibling's CONTENT and cannot tell whether the three drift causes are
actually in it, or whether `S18` truly has no conformant form.** That half is `AC5`'s.

**`R1R10-AC5`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether **each row's new class is
right at the bytes -- across BOTH classes** -- and whether the sibling document actually carries the
three drift causes where a later re-derivation will meet them.

⛔ **THAT PHRASING IS THE ROUND-8 PARTITION RULE.** The tempting bucket to police is
`UNEXECUTABLE-IN-PRINCIPLE`. ⭐ **But a row wrongly marked `RE-ROUTABLE` is equally wrong -- it creates
a promise nobody keeps.**

⭐ **THE BAR, and you may hold me to it:** every criterion was checked against a HAND-BUILT CORRECT
RECORD before this order shipped, **and the round-16 additivity arm was NOT copied because measuring
first showed it would have failed on honest history.** **Confirm the instrument yourself** --
`python .../check_lt_r10.py selftest-arms` must print `VERDICT: PASS-ARMS-DISCRIMINATE`, and **the run
prints its own arm counts; this order does not quote them** (`W1-S37`). *"Can a CORRECT artifact FROM
THIS CELL ALONE satisfy this? Where the honest answer is no, THE CRITERION IS THE DEFECT, NOT THE
CELL."* **If you find one, file it BLOCKING and keep working.**

## BOUNDS

- **Grant.** ⛔ **THE `<paths>` BLOCK BELOW IS THE GRANT AND EVERY PATH YOU MAY WRITE IS IN IT.** Nothing is granted in this prose. Note it includes the NEW sibling document by name.
- ⛔ **`check_lt_r1.py` IS READ-ONLY. NOT ONE BYTE.** Your own `AC2` proves it by comparing its blob at your base and at your HEAD. The other `fixed_inputs/r1/` files (`FORK_CONTROLS.json`, `PLANTED_CONTRACT.json`, `SUBJECT_CONTROL.json`) are equally read-only -- you ADD a file to that directory and change none of them.
- ⛔ **DO NOT TRY TO SATISFY `S18`.** It has no conformant form, which is the finding. A cell that found a way to add that arm would have falsified the class rather than satisfied the round -- if you believe one exists, file it BLOCKING and say so; do not perform it.
- ⛔ **YOU DISARM NOTHING.** Both rows name `2.0.0_SA_COO~G`; a disarm is the row owner's act under R-19 and the disposition is `3.0.0_SA_CVO`'s at L9.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump; preserve line endings exactly.
- **Id** `LGIC_LGCTFM-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time. **No other order is open this round.**
- Every `.py` edit passes `.tools/commit-gate.sh`. **Commit before you grade.**

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.11, round-10 cell `LT-r-1` (section 21).
<owned_cells>LT-r-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `R1R10-AC1` through `R1R10-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-r-1-r10.split-and-reroute.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> R1R10-AC1,R1R10-AC2,R1R10-AC3,R1R10-AC4,R1R10-AC5 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-r-1-r10.split-and-reroute.md` BEFORE the `complete` flip.
Result file `split-and-reroute.r10.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent. Your recorded invocation must match this order's literal text INCLUDING `timeout 900`.
`R1R10-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

<paths>
org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/ROUTED_ROW_RECLASS_R10.json
org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-r-1-r10.split-and-reroute.proof_of_spec.json
org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/split-and-reroute.r10.result.md
org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/DRIFT_CAUSES.md
org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-r-1-r10.split-and-reroute.md
</paths>
<preflight>
lane: <paths> IS the grant and it is exhaustive -- the record, the proof instance, the result narrative, THE NEW SIBLING DOCUMENT (fixed_inputs/r1/DRIFT_CAUSES.md, named explicitly because it sits in the ISSUER's deliverables tree where no convention covers a worker), the shared channel, and this order for the status flip. Nothing is granted in BOUNDS prose. check_lt_r1.py and the other three r1 fixed inputs have NO writer this round.
contention: the channel is shared -- append-only, 14b's inversion applies, so do NOT isolate the channel write. One cell this round, so no sibling races your deliverables directory.
comp-schedule: RUN at the round-10 cut: no schedule is created or read.
comp-iam: RUN at the round-10 cut: no grant moves.
comp-adversary: RUN at the round-10 cut. The cheapest satisfying move is to class both rows IN-PRINCIPLE and write nothing -- so the arm requires BOTH classes to NAME something and requires the re-route artifact to EXIST in fixed_inputs/r1/. The second-cheapest is to copy the two ids from this order's framing table -- so the arm re-derives them from the round-9 record by SET EQUALITY. The third is to assert additivity by writing the same blob string twice -- so the arm checks the claimed HEAD blob against the TREE. What no mechanical arm here can see is whether the sibling actually CARRIES the three drift causes, or whether S18 truly has no conformant form; stated on the order and routed to AC5 over BOTH classes.
</preflight>

Seating: slot `~1`, level 0, the ONLY order this round. Round 10 of LGIC_LGCTFM, issued by
`2.0.0_SA_COO~G` on decomposition v1.11 s.21, from `1.0.0_SA_CTO`'s round-9 analysis @`25bd9cb1fd` and
`3.0.0_SA_CVO`'s L9 @`dbd706fcea`. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r10/`.
Rulings carried: `S85`'s ONE CARRIER, the cut-time criterion bar, `S106`'s criterion-level non-pairing,
the stale-proof arm, the additive-sibling ruling, **the actor's-own-base additivity anchor (new this
round)**, the partition rule for judgment criteria, `W1-S37`, ADDENDUM 3's vintage field, `S108`'s
grant discipline, R-19, R-81 as amended @`80bb078627`, LD-0521.

---

## RECORD FACE

**Cut rationale.** The analysis s.6 names the split and the re-route and says *"Nothing else."*

**The issuer measured before cutting and did NOT copy round 16's arm.** `check_lt_r1.py` has SIX
commits touching it, so the round-16 blob-vs-round-pin proof would have **failed on honest history** --
a criterion no correct artifact could satisfy. ⭐ **The anchor moved to the ACTOR'S OWN BASE**, which
proves the only thing this cell can be responsible for, and the general rule is recorded in s.21.3.

**`S26` is not here.** It CLOSED at `LGIC_LGCTFM-S55` @`d180c2077f` on the R-81 scope ruling
@`80bb078627`, by its owner, this tick -- the clock this seat held and declined to close on its own
reading.
