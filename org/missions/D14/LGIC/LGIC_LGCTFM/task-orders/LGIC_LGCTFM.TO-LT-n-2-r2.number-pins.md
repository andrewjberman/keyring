# TO LGIC_LGCTFM.TO-LT-n-2-r2 -- RUN IDS AND CONTENT HASHES ON EVERY NUMBER, with E3 EXCLUDED BY NAME

<to_id>LGIC_LGCTFM.TO-LT-n-2-r2</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-18</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` (ADMITTED; both halves current) | **Decomp cell:** `LT-n-2` (decomposition v1.3 s.12) | **outcome_ref:** FWD-3 | **depends_on:** none -- sole cell of slot ~2

---

## WORKER FACE

### THE CELL

`LT-n-2`. **Every number a round-1 judgment record cites gets bound to the RUN it was measured on and to
that run's CONTENT HASH.** Row `LGIC_LGCTFM-S11` measured the defect: three numbers in round 1's judgment
records name no run, and two of them cannot both be true of one plan -- `P1R1-AC6` cites 1626 packages,
`X1R1-AC6` cites 1074. `E3R1-AC6` grades 271 tensions where the contract now carries 179, so that
population no longer exists anywhere.

**S11's own remedy is the sentence to obey: "No grade moves ... nothing is owed to the cells; what is owed
is the CONVENTION."** You are building the convention's first record, not re-grading anyone.

### THE SET IS A SUBTRACTION, NEVER A FORWARD LIST

⛔ **Rule 24(i), and this is the arm most likely to catch a good-faith record.** Do NOT write down the
numbers you can think of. **Enumerate a DENOMINATOR** -- every number cited in round 1's judgment evidence,
read from the fourteen proof instances and their evidence strings -- **print it, and then subtract what you
exclude.** A forward list covers what its author had in mind and omits silently; the same set written as a
subtraction from a printed denominator cannot lose a member without the count disagreeing.

Your record carries `denominator`, `denominator_source` (the instrument, in words), `numbers_found`,
`pinned`, and `excluded`. **The arm requires `numbers_found == pinned + excluded`.**

### E3 IS EXCLUDED BY NAME AND ITS REASON IS STATED

`1.0.0_SA_CTO`'s round-1 analysis, item 2, verbatim: *"`S11`'s run-ids on every number; `E3` is NOT
re-graded against R-40."*

⛔ **A SILENT OMISSION AND A STATED EXCLUSION ARE DIFFERENT STATES** and the arm grades the difference.
`E3R1-AC6`'s judgment was SOUND AT ITS OWN VINTAGE -- it ran before `LT-e-4` made the untypeable plant
opt-in, which is what moved the population from 271 tensions to 179. **Re-grading it would falsify a
correct grade.** Put it in `excluded` with that reason.

### EVERY HASH CARRIES ITS INSTRUMENT, AND THIS IS NOT PEDANTRY

⛔ **A HASH WITHOUT ITS INSTRUMENT IS TWO NUMBERS.** `git hash-object` prefixes `blob <len>` and a NUL byte
before hashing, so a plain `sha1` of the same bytes disagrees. Measured on this project's own
`contract.json`: **`33204e29839de89af81fb293317cce3ccdf2266d`** by `git hash-object`, and
**`9c5cdb873f00a599bb00166831a91646fea97990`** by plain sha1 -- same file, same moment. The issuing seat
computed the plain one FIRST and briefly read it as a MISMATCH against a hash it had already published in a
row and in two messages. One more step and a CORRECT number would have been "corrected".

So every entry in `pinned` carries `number`, `run_id`, `content_hash` **and `hash_instrument`**, and the arm
refuses a hash with no instrument.

**Read:** row `LGIC_LGCTFM-S11` whole; `R2_BASE.json`'s `graded_run_round_1` and `excluded_by_name`; the
fourteen round-1 proof instances; `R-40` in `SELF_DRIVE_LGIC_RULINGS_20260917.md`.

### WHERE YOUR RECORD GOES

`<WS>/org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/NUMBER_PINS_R2.json`

Any script you cite as an instrument goes in that same folder and is COMMITTED -- row `LGIC_ENFORCE-S69`:
a record citing an untracked instrument has an unverifiable claim at its centre and the drain deletes the
evidence as routine hygiene.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="N2R2-AC1" cell_refs="LT-n-2"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_lt_r2.py n2-subtraction</invocation><expect>PASS-N2-SET-IS-A-SUBTRACTION</expect></criterion>

<criterion id="N2R2-AC2" cell_refs="LT-n-2"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_lt_r2.py n2-e3</invocation><expect>PASS-N2-E3-EXCLUDED-BY-NAME</expect></criterion>

<criterion id="N2R2-AC3" cell_refs="LT-n-2"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_lt_r2.py n2-pins</invocation><expect>PASS-N2-EVERY-NUMBER-CARRIES-ITS-RUN</expect></criterion>

<criterion id="N2R2-AC4" cell_refs="LT-n-2"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_lt_r2.py n2-hash-instrument</invocation><expect>PASS-N2-EVERY-HASH-NAMES-ITS-INSTRUMENT</expect></criterion>

<criterion id="N2R2-AC5" cell_refs="LT-n-2" judgment="true"/>

<expected_criteria>N2R2-AC1, N2R2-AC2, N2R2-AC3, N2R2-AC4, N2R2-AC5</expected_criteria>

**ALL FOUR MECHANICAL CRITERIA READ FAIL AT THE CUT**, each because your record does not exist yet --
MEASURED by the issuer, not assumed. There is no guard-shaped criterion in this cell.

**`N2R2-AC5`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether the denominator is genuinely an
enumeration of the round's judgment numbers rather than a count of what the cell happened to pin, and
whether each `content_hash` was COMPUTED from the named run rather than copied from another record. The
arms can only check that the fields are present and that the arithmetic closes.

**THE CHECKER'S CONTROLS:** `selftest-arms` drives 28 arms, **10 POSITIVE-SATISFIABILITY** against
simulated correct records. Run it first. A mutant proves an arm CAN fail; only the positive arm proves it
can pass for the right reason. An arm a correct record cannot satisfy is a BLOCKING surprise row quoting
the arm and its output -- never a workaround, never an edit to a fixed input.

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/` and this order's own file. Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **EVERY ROUND-1 FIXED INPUT AND EVERY ROUND-1 PROOF INSTANCE IS READ-ONLY.** You cite them; you do not touch them. An issuer re-grade has no home inside a worker's instance and neither does yours.
- ⛔ **NO GRADE MOVES.** If you find a number that is WRONG rather than merely unpinned, that is a surprise ROW with its measurement, not a correction to a closed round.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md`, appended by **TEXTUAL SPLICE** to the fence that PARSES AS A LIST. ⛔ **NEVER RE-DUMP THE ARRAY.** Id `LGIC_LGCTFM-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time -- another cell is appending to this same file CONCURRENTLY, so a stale read collides.
- **Commit before you grade.**
- **Nothing live moves.** No apply, no AWS write, no deploy.

<paths>
org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.3, round-2 cell `LT-n-2` (section 12).
<owned_cells>LT-n-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `N2R2-AC1` through `N2R2-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/LGIC_LGCTFM.TO-LT-n-2-r2.number-pins.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> N2R2-AC1,N2R2-AC2,N2R2-AC3,N2R2-AC4,N2R2-AC5 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-n-2-r2.number-pins.md` BEFORE the `complete` flip.
Result file `number-pins.r2.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`N2R2-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape, and PRINT the denominator with its instrument, the `pinned + excluded == numbers_found` arithmetic, and E3's exclusion reason.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-2 cut: no schedule is created or read by this cell.
comp-iam: RUN at the round-2 cut: no grant moves; the cell reads round-1 records and writes one of its own.
comp-adversary: RUN at the round-2 cut: the adversarial control is the SUBTRACTION arm, which refuses a set that does not close against a printed denominator -- the shape that catches a forward list wearing a count. It exists because a correct subtraction on the WRONG AXIS was ruled against this very seat four hours ago as R-50, arriving looking measured because its denominator was real.
lane: the <paths> block is the grant; deliverables/0.9.0_WK_LGIC_LGCTFM~2/ is granted by the tree convention. Round-1 fixed inputs and proof instances are READ-ONLY by a BOUND, which the grant cannot express.
contention: this cell runs CONCURRENTLY with LT-a-2 on slot ~1 and both append to the same surprise channel. That is DELIBERATE and is this round's stated experiment -- see LT-a-2's contention note for the hypothesis, the 3-of-3 conflicts that argued against it and the 1-of-1 clean union merge that argued for it. BOTH ORDERS MANDATE A TEXTUAL SPLICE AND FORBID A RE-DUMP, and a conflict at the second drain refutes the hypothesis and is recorded rather than forgotten.
</preflight>

Seating: slot `~2`, level 0, SOLE order of that slot. Round 2 of LGIC_LGCTFM, issued by `2.0.0_SA_COO~G` on decomposition v1.3 s.12, from `1.0.0_SA_CTO`'s round-1 analysis item 2. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/` (`check_lt_r2.py`, 11 subcommands and a 28-arm self-test with 10 positive-satisfiability arms; `R2_BASE.json` pinning `d0d4c6065f`). Rulings carried: R-40, R-43.
