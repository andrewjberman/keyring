# TO LGIC_ENFORCE.TO-EN-d-1-r15 -- THE REPAIR RETIRED A DISCRIMINATOR; FIND EVERY INSTRUMENT THAT USED IT

<to_id>LGIC_ENFORCE.TO-EN-d-1-r15</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-19</issued_date>
<status>issued</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves SIGNED and current) | **Decomp cell:** `EN-d-1` (decomposition v3.14 s.0o) | **outcome_ref:** FWD-3 | **depends_on:** none -- the only cell this round

---

## WORKER FACE

### THE CELL

`EN-d-1`. Round 14 repaired the population report: every column now renders through ONE renderer under
ONE rule. The analysis accepted it and it **STANDS**. ⛔ **ITS SIDE EFFECT IS THAT NO COLUMN IS
DISTINGUISHED ANY MORE BY CARRYING BRACE BYTES -- and that is exactly what round 13's arm used to
identify R-38's population.**

`1.0.0_SA_CTO`, round-14 analysis @`7761d31eaf`, verbatim: *"The repair BREAKS ANY INSTRUMENT THAT READS
THE POPULATION OFF THE RENDERED TABLE'S BRACES -- `3.0.0_SA_CVO` named this against its own convenience,
**including the instrument IT used minutes earlier, which would now return a clean denominator-bearing
0.** Cut a cell that enumerates those instruments and re-points or retires each."*

⛔ **THE HAZARD IS A SILENT ZERO.** A broken instrument here does not error and does not warn. It
returns **0**, with a clean denominator, and **it agrees with itself.** That is why this order's
acceptance is a POSITIVE CONTROL and not a pass/fail.

### WHAT YOU BUILD

1. **THE DENOMINATOR, FROM AN UNSCOPED READ.** Every instrument that READS THAT TABLE AT ALL -- not the
   set of files anybody thought to check. Record the invocation in `how_enumerated`. ⛔ **Write the
   swept set as the printed denominator MINUS what you exclude, never as a forward list** (Rule 24: a
   forward list covers what its author had in mind and omits in silence).
   ⚠ **The sweep's subject is the CLAIM'S population.** Choosing the domain is itself a claim: do the
   unscoped read FIRST, print its number, and only then subtract.
2. **ONE ENTRY PER INSTRUMENT**, each with its `path`, whether it `reads_the_rendered_table`, whether it
   `used_the_brace_discriminator`, a `disposition` of exactly `RE-POINTED` / `RETIRED` / `UNAFFECTED`,
   and a `basis`.
3. ⭐ **A POSITIVE CONTROL ON EVERY `RE-POINTED` INSTRUMENT, AND IT IS THE CRITERION:** it must return
   **1303** -- round 13's population -- against the RAW rows, with `on` naming what it now reads and
   `invocation` naming what you RAN. **A control returning 0, or any other number, is REFUSED and the
   arm says why: a clean zero is precisely what a broken instrument reports.**
   ⚠ `1303` is not arbitrary: round 13 measured it and round 14's `EN-p-38` re-derived it from a pinned
   input while reconciling 1449 by-token against it. **Two rounds, two routes, one number.**
4. **AN INSTRUMENT THAT CANNOT RETURN 1303 IS NOT RE-POINTABLE** -- it goes in `RETIRED` with a basis.
   That is an honest outcome and it has its own positive arm.
5. **THE DISPOSITION ARITHMETIC:** `re_pointed` + `retired` + `unaffected` must equal the entries you
   carry, and `re_pointed` must equal the number of passing controls.
6. **THE VINTAGE FIELD:** `fixed_inputs_at_pin`, mapping each fixed input you invoked to the COMMIT you
   invoked it at -- both `check_en_r15.py` and `R15_BASE.json`, each resolvable against its path.

⭐ **FINDING NOTHING IS AN ADMISSIBLE RESULT AND IT PASSES**, with its own positive arm: if no instrument
read the population off the braces, say so and show the denominator. **You are being asked to find
breakage caused by a repair this fabric just accepted -- and a bar that only passed on finding breakage
would be an instruction to find some.**

⚠ **`3.0.0_SA_CVO`'s OWN INSTRUMENT IS IN SCOPE.** The analysis names it explicitly: that seat surfaced
this against its own convenience. A sweep that omits the adjudicator's own instrument has excluded the
one member the analysis actually cited.

**RECORD SHAPE (the one carrier is `deliverables/2.0.0_SA_COO~G/fixed_inputs/r15/R15_BASE.json`; this is a quotation of it)**

```json
{
  "sweep": {
    "denominator": 0,
    "how_enumerated": "<the unscoped read that produced the denominator, with its invocation>",
    "instruments": [{"path": "<file or file:line>", "reads_the_rendered_table": true, "used_the_brace_discriminator": true, "disposition": "<RE-POINTED|RETIRED|UNAFFECTED>", "control": {"returns": 0, "on": "<the raw rows source it now reads>", "invocation": "<what was RUN>"}, "basis": "<why this disposition>"}],
    "re_pointed": 0, "retired": 0, "unaffected": 0
  },
  "fixed_inputs_at_pin": {"<path>": "<commit>"},
  "stale_proofs": {"fixed_input_commits_since_cut": 0, "proofs_re_run": []}
}
```

Write it to `<WS>/org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/DISCRIMINATOR_SWEEP_R15.json`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="D1R15-AC1" cell_refs="EN-d-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r15/check_en_r15.py d1-sweep</invocation><expect>PASS-D1-SWEEP</expect></criterion>

<criterion id="D1R15-AC2" cell_refs="EN-d-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r15/check_en_r15.py r15-vintage-field</invocation><expect>PASS-R15-VINTAGE-FIELD</expect></criterion>

<criterion id="D1R15-AC3" cell_refs="EN-d-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r15/check_en_r15.py r15-stale-proofs</invocation><expect>PASS-R15-STALE-PROOFS</expect></criterion>

<criterion id="D1R15-AC4" cell_refs="EN-d-1" judgment="true"/>

<expected_criteria>D1R15-AC1, D1R15-AC2, D1R15-AC3, D1R15-AC4</expected_criteria>

**WIRING AT THE CUT -- AND EACH RED NAMES THE ACT THAT CLEARS IT.**

| criterion | at the cut | WHICH ACT CLEARS IT |
|---|---|---|
| `D1R15-AC1` | **FAIL** | **YOURS ALONE** -- writing your record. |
| `D1R15-AC2` | **FAIL** | **YOURS ALONE** -- the arm grades only the records present in YOUR checkout. |
| `D1R15-AC3` | **PASS**, guard-shaped | nothing -- its window is empty until a fixed input moves. |

⚠ **WHAT THE MECHANICAL ARMS CANNOT SEE:** the arm checks your record -- the arithmetic, the
dispositions, and that every re-pointed control reports 1303. **It never runs your instruments and never
opens the table.** A PASS means your record is internally sound and your controls report the right
number, never that you ran them. That half is `AC4`'s.

**`D1R15-AC4`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether the denominator came from a
genuinely unscoped read; whether each control was actually RUN at the stated invocation rather than
reasoned to; whether any instrument that reads the table was excluded from the swept set; and whether
each `RETIRED` is justified by inability rather than by inconvenience.

⭐ **THE BAR, and you may hold me to it:** every criterion was checked against a HAND-BUILT CORRECT
RECORD before this order shipped, driven in the self-test as a POSITIVE-SATISFIABILITY arm. **Confirm
the instrument yourself before you start** -- `python .../check_en_r15.py selftest-arms` must print
`VERDICT: PASS-ARMS-DISCRIMINATE`, and **the run prints its own arm counts; this order deliberately does
not quote them** (`LGIC_LGCTFM-W1-S37`: a number an order quotes about its own instrument is a second
carrier of a fact the instrument already reports, and this seat was measured in breach of that row in
its last three orders). *"Can a CORRECT artifact FROM THIS CELL ALONE satisfy this? Where the honest
answer is no, THE CRITERION IS THE DEFECT, NOT THE CELL."* **Three such criteria have been found in this
project's last two rounds -- one by me before issuing, two by workers who refused to flip their orders.
If you find a fourth, file it BLOCKING and keep working.**

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/` and this order's own file. Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **DO NOT UNDO OR AMEND ROUND 14's REPAIR.** It STANDS, and the analysis found that moving to the raw census JSON was **REQUIRED BY** the repair rather than an optional tidy. Re-pointing an instrument means pointing it at the RAW rows, never restoring the brace discriminator.
- ⛔ **DO NOT RE-MEASURE R-38's POPULATION.** Round 13 measured it, round 14 re-derived it. You USE 1303 as a control value.
- ⛔ **RE-POINTING AN INSTRUMENT YOU DO NOT OWN:** if a re-point would edit another seat's artifact, do NOT edit it -- record it as `RETIRED` or `UNAFFECTED` with a basis naming the owner, or record the re-point as the OWNER's act with what you verified. Say which in the `basis`.
- **Anything the sweep finds that is NOT about the brace discriminator is a ROW, not a fix.**
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump; preserve line endings exactly.
- **Id** `LGIC_ENFORCE-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time. **No other order is open on this project this round.**
- Every `.py` edit passes `.tools/commit-gate.sh`. **Commit before you grade.**

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.14, round-15 cell `EN-d-1` (section 0o).
<owned_cells>EN-d-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `D1R15-AC1` through `D1R15-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-d-1-r15.discriminator-sweep.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> D1R15-AC1,D1R15-AC2,D1R15-AC3,D1R15-AC4 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-d-1-r15.discriminator-sweep.md` BEFORE the `complete` flip.
Result file `discriminator-sweep.r15.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent. Your recorded invocation must match this order's literal text INCLUDING `timeout 900` -- the invocation-alignment limb compares them.
`D1R15-AC4` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the denominator and the
invocation that produced it, every instrument with its disposition and basis, and **every re-pointed
control's returned number beside the 1303 it had to match.** If nothing used the discriminator, print
the denominator that proves you looked.

---

## RECORD FACE

⛔ **THE STANDING BAR THIS ROUND ESTABLISHES, FOR `3.0.0_SA_CVO` AT L9** (`1.0.0_SA_CTO` @`7761d31eaf`):
**a repair that RETIRES a discriminator names the instruments that used it, IN THE SAME RECORD.** COST:
one list. NON-APPLICATION: a repair that ADDS a signal without removing one. This round exists because
round 14's repair did not carry that list -- correctly, since the bar did not exist yet.

⚠ **AND THE GRADING NOTE THAT MATTERS MOST HERE:** the failure mode under test is a CLEAN ZERO. An arm
that accepted "the instrument ran and returned a number" would grade a broken instrument GREEN, so the
criterion demands the NUMBER. At L9 the same applies to the judgment half: a control nobody ran and a
control that returned 1303 look identical in a record.

<preflight>
comp-schedule: RUN at the round-15 cut: no schedule is created or read.
comp-iam: RUN at the round-15 cut: no grant moves.
comp-adversary: RUN at the round-15 cut: the cheapest satisfying move is to enumerate the instruments anybody remembers and report them all UNAFFECTED, which costs nothing and finds nothing -- so `how_enumerated` must name an UNSCOPED read with its denominator, and the order states that the adjudicator's own instrument is in scope and named by the analysis. The second-cheapest is to re-point an instrument and report that it "works" -- so every RE-POINTED entry must carry a control returning exactly 1303, and a clean 0 is called out by the arm as the signature of the very breakage being swept. What no mechanical arm here can see is whether any control was RUN -- stated on the order and routed to AC4.
lane: <paths> is the grant; deliverables/0.9.0_WK_LGIC_ENFORCE~1/ by the tree convention. Round 14's artifacts and 3.0.0_SA_CVO's instruments are READ surfaces; an edit to a foreign artifact is recorded, not made.
contention: the channel is shared -- append-only, 14b's inversion applies. One cell, one deliverable directory.
</preflight>

Seating: slot `~1`, level 0, the only order this round. Round 15 of LGIC_ENFORCE, issued by
`2.0.0_SA_COO~G` on decomposition v3.14 s.0o, from `1.0.0_SA_CTO`'s round-14 analysis @`7761d31eaf`.
Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r15/` (`check_en_r15.py`, `R15_BASE.json`
pinning `3c00f32900`). Rulings carried: S85's ONE CARRIER, the cut-time criterion bar, S106's
criterion-level non-pairing, the retired-discriminator bar, `LGIC_LGCTFM-W1-S37` (no derived totals
quoted in an order), ADDENDUM 3's vintage field, LD-0521, Rule 24's subtraction.
