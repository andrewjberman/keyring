# TO LGIC_ENFORCE.TO-EN-s-1-r16 -- RETIRED IN A RECORD, STILL RUNNABLE FROM THE TREE: CENSUS THE CLASS

<to_id>LGIC_ENFORCE.TO-EN-s-1-r16</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-19</issued_date>
<status>issued</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves SIGNED and current) | **Decomp cell:** `EN-s-1` (decomposition v3.15 s.0p) | **outcome_ref:** FWD-3 | **depends_on:** none -- **NOT paired with `EN-m-2`, which runs beside it**

---

## WORKER FACE

### THE CELL

`EN-s-1`. `1.0.0_SA_CTO`, round-15 analysis @`f818ebd12b`, verbatim:

> ⭐ **"THE GENERALISATION IS THE VALUABLE PART, and it is bigger than this control. The class is: AN
> INSTRUMENT THAT HAS BEEN RETIRED IN A RECORD BUT IS STILL RUNNABLE FROM THE TREE. Round 15 found one
> BY ACCIDENT, because the CVO re-ran it. A census of the class is a round-16 cell: every `fixed_inputs/`
> checker across LGIC whose retiring record exists, measured against whether the instrument itself
> discloses it. Denominator printed."**

**The one already known:** `p37-producers` in `check_en_r13.py` returns `PASS` to anyone who runs it
while its two siblings fail loudly, because its check subtracts from an already-empty set. **The green one
was the dangerous one.** You are measuring how many more of those the estate is carrying.

### ⛔ THE DOMAIN IS THE TRAP, AND THE ANALYSIS NAMED IT

> **"The subtraction's domain is `fixed_inputs/` ACROSS THE PROJECT, NOT THE RETIRED LIST -- reading the
> retired list can only find retirements someone already wrote down, which is the
> UNDERSTATED-BY-ITS-OWN-INSTRUMENT shape this project has now hit twice."**

**Enumerate the CHECKERS first and print that denominator. Then ask of each whether a retiring record
exists.** A census that starts from the known retirements returns a confident number that cannot contain
a single thing you did not already know -- and the arm REFUSES a `how_enumerated` that describes that.

⚠ **AND IT IS CUT ONCE ACROSS BOTH PROJECTS.** The LGCTFM round-7 analysis: *"LGCTFM carries
`fixed_inputs/` too, and the census should be cut once across both projects rather than twice."* Your
denominator spans **`LGIC_ENFORCE` AND `LGIC_LGCTFM`**, and the arm refuses a census carrying no
instrument from one of them.

### WHAT YOU BUILD

1. **THE DENOMINATOR**, from enumerating `fixed_inputs/` checkers across both projects, with the
   invocation in `how_enumerated`.
2. **ONE ENTRY PER CHECKER**, each with `path`, `project`, `retiring_record` (or null), whether the
   **INSTRUMENT ITSELF** discloses the retirement, a `class` of exactly `RETIRED-AND-DISCLOSED` /
   `RETIRED-BUT-SILENT` / `LIVE`, and a `basis` saying **how you determined disclosure**.
   ⭐ **"Discloses" means a reader of the instrument learns it** -- a docstring line, a refusal, a
   printed notice. **A retiring record living elsewhere is exactly what does NOT count**; that is the
   whole finding.
3. **THE CLASS ARITHMETIC** must close against the entries you carry, and the classes must not contradict
   the disclosure flag -- the arm checks both directions.

⭐ **FINDING NOTHING FURTHER IS AN ADMISSIBLE RESULT AND IT PASSES**, with its own positive arm. **You are
measuring a class this fabric has already been embarrassed by, and a bar that only passed on finding more
would be an instruction to find more.**

### ⚠ WHAT THIS CELL DOES AND DOES NOT MOVE

**This cell MEASURES. It repairs nothing** -- no instrument gets a disclosure line from you, and the
already-known `p37-producers` is the sibling cell's business, not yours. Its output IS its metric, so the
sponsor-metric cut rule's non-application clause covers it; stated here rather than left silent.

**RECORD SHAPE (the one carrier is `deliverables/2.0.0_SA_COO~G/fixed_inputs/r16/R16_BASE.json`; this is a quotation of YOUR half)**

```json
{
  "census": {
    "denominator": 0,
    "how_enumerated": "<the enumeration over fixed_inputs/ ACROSS BOTH PROJECTS, with its invocation>",
    "instruments": [{"path": "<checker path>", "project": "<LGIC_ENFORCE|LGIC_LGCTFM>", "retiring_record": "<path, or null>", "instrument_discloses_it": true, "class": "<RETIRED-AND-DISCLOSED|RETIRED-BUT-SILENT|LIVE>", "basis": "<how you determined disclosure>"}],
    "retired_and_disclosed": 0, "retired_but_silent": 0, "live": 0
  },
  "fixed_inputs_at_pin": {"<path>": "<commit>"},
  "stale_proofs": {"fixed_input_commits_since_cut": 0, "proofs_re_run": []}
}
```

Write it to `<WS>/org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/RETIRED_BUT_RUNNABLE_R16.json`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="S1R16-AC1" cell_refs="EN-s-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r16/check_en_r16.py s1-census</invocation><expect>PASS-S1-CENSUS</expect></criterion>

<criterion id="S1R16-AC2" cell_refs="EN-s-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r16/check_en_r16.py r16-vintage-field</invocation><expect>PASS-R16-VINTAGE-FIELD</expect></criterion>

<criterion id="S1R16-AC3" cell_refs="EN-s-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r16/check_en_r16.py r16-stale-proofs</invocation><expect>PASS-R16-STALE-PROOFS</expect></criterion>

<criterion id="S1R16-AC4" cell_refs="EN-s-1" judgment="true"/>

<expected_criteria>S1R16-AC1, S1R16-AC2, S1R16-AC3, S1R16-AC4</expected_criteria>

**WIRING AT THE CUT -- AND EACH RED NAMES THE ACT THAT CLEARS IT.**

| criterion | at the cut | WHICH ACT CLEARS IT |
|---|---|---|
| `S1R16-AC1` | **FAIL** | **YOURS ALONE** -- writing your record. |
| `S1R16-AC2` | **FAIL** | **YOURS ALONE** -- the arm grades only the records present in YOUR checkout. |
| `S1R16-AC3` | **PASS**, guard-shaped | nothing -- its window is empty until a fixed input moves. |

⚠ **WHAT THE MECHANICAL ARM CANNOT SEE:** it checks your arithmetic, your classes against your own
disclosure flags, and that `how_enumerated` names `fixed_inputs/` rather than the retired list. **It never
opens a single checker and never runs one.** A PASS means your record is coherent, never that any
`instrument_discloses_it` is true. That half is `AC4`'s.

**`S1R16-AC4`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether the denominator really came from
enumerating `fixed_inputs/`; whether a checker was missed (**hunt it by subtraction from your own larger
read, not by re-reading the cell's list**); whether each `instrument_discloses_it` is true at the bytes;
and whether any `LIVE` classification hides a retiring record that exists somewhere the cell did not look.

⭐ **THE BAR, and you may hold me to it:** every criterion was checked against a HAND-BUILT CORRECT RECORD
before this order shipped. **Confirm the instrument yourself first** -- `python .../check_en_r16.py
selftest-arms` must print `VERDICT: PASS-ARMS-DISCRIMINATE`, and **the run prints its own arm counts;
this order does not quote them** (`LGIC_LGCTFM-W1-S37`). *"Can a CORRECT artifact FROM THIS CELL ALONE
satisfy this? Where the honest answer is no, THE CRITERION IS THE DEFECT, NOT THE CELL."* **Four such
criteria have been found in this project's last three rounds, every one by the cell being graded. If you
find a fifth, file it BLOCKING and keep working.**

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/` and this order's own file. Nothing else.
- ⛔ **EVERY CHECKER YOU CENSUS IS READ-ONLY.** You add no disclosure line to any instrument. The remedy is decided on your measurement, by the CTO; deciding it inside the measuring cell is how a round makes the numbers agree instead of the data.
- ⛔ **`LGIC_LGCTFM` IS IN YOUR READ SCOPE AND NOT IN YOUR WRITE SCOPE.** You read its `fixed_inputs/`; you write nothing there and file no row on its channel.
- ⛔ **THE SIBLING CELL IS NOT YOURS** (`EN-m-2`, the marker). It is adding a `RETIRED.md` to `fixed_inputs/r13/` while you work. ⚠ **If your read of that directory races its write, record what YOU measured and say when** -- do not coordinate, and do not treat its in-flight change as your finding.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump; preserve line endings exactly.
- **Id** `LGIC_ENFORCE-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time. **One other order is open this round.**
- Every `.py` edit passes `.tools/commit-gate.sh`. **Commit before you grade.**

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.15, round-16 cell `EN-s-1` (section 0p).
<owned_cells>EN-s-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `S1R16-AC1` through `S1R16-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/LGIC_ENFORCE.TO-EN-s-1-r16.retired-but-runnable-census.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> S1R16-AC1,S1R16-AC2,S1R16-AC3,S1R16-AC4 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-s-1-r16.retired-but-runnable-census.md` BEFORE the `complete` flip.
Result file `retired-but-runnable-census.r16.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent. Your recorded invocation must match this order's literal text INCLUDING `timeout 900`.
`S1R16-AC4` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the denominator and the
invocation that produced it, the three class counts, and **every `RETIRED-BUT-SILENT` instrument by
path** with how you determined its silence. If there are none beyond the one already known, print the
denominator that proves you looked.

---

## RECORD FACE

⛔ **THE ONE-LINE RECUT THIS ROUND CARRIES, FOR `3.0.0_SA_CVO` AT L9:** this class was found **BY
ACCIDENT**, because a grader re-ran an instrument instead of reading the report about it. The census
turns that accident into a measurement -- and the measurement is only worth its denominator, which is why
the domain is `fixed_inputs/` and never the retired list.

<preflight>
comp-schedule: RUN at the round-16 cut: no schedule is created or read.
comp-iam: RUN at the round-16 cut: no grant moves.
comp-adversary: RUN at the round-16 cut: the cheapest satisfying move is to enumerate FROM the known retirements, which yields a clean small denominator containing nothing new -- so the arm reads how_enumerated and REFUSES a domain described as the retired list, and the order states the trap in the analysis's own words. The second-cheapest is to census one project and report a total; the arm refuses a census carrying no instrument from LGIC_LGCTFM. What no mechanical arm here can see is whether any instrument_discloses_it is true at the bytes -- stated on the order and routed to AC4.
lane: <paths> is the grant; deliverables/0.9.0_WK_LGIC_ENFORCE~2/ by the tree convention. Every checker censused is READ-ONLY, including LGIC_LGCTFM's, which is in read scope and not write scope.
contention: the channel is shared -- append-only, 14b's inversion applies. The sibling cell WRITES into fixed_inputs/r13/ while this cell READS that directory; the order tells this cell to record what it measured and when, rather than coordinate.
</preflight>

Seating: slot `~2`, level 0, one of TWO orders this round. Round 16 of LGIC_ENFORCE, issued by
`2.0.0_SA_COO~G` on decomposition v3.15 s.0p, from `1.0.0_SA_CTO`'s round-15 analysis @`f818ebd12b` s.5.2
and the LGCTFM round-7 analysis s.5.4. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r16/`.
Rulings carried: S85's ONE CARRIER, the cut-time criterion bar, S106's criterion-level non-pairing, Rule
24's subtraction and its domain clause, the sponsor-metric cut rule, `LGIC_LGCTFM-W1-S37`, ADDENDUM 3's
vintage field, LD-0521.
