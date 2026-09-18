# TO LGIC_ENFORCE.TO-EN-b-42-r9 -- THE STALE REMEDIATION BACKLOG GETS A NAMED OWNER PER ROW, NEVER A CATEGORY

<to_id>LGIC_ENFORCE.TO-EN-b-42-r9</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-18</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves current) | **Decomp cell:** `EN-b-42` (decomposition v3.8 s.0i) | **outcome_ref:** FWD-4 | **depends_on:** none -- the only order on slot `~3`

---

## WORKER FACE

### THE CELL

`EN-b-42`. Round 8 built the staleness limb (`_stale_open_row`, `STALE_OPEN_ROW_N_ROUNDS = 2`) and
`7f82f66f93` made it **DISCLOSE rather than REFUSE**, for a stated reason:

> a gate refuses an act only when that act can REMEDY the gate's condition.

A slug cannot clear a backlog, so refusing the slug would have deadlocked every future L10 on work no L10
can do. **A REFUSAL FORM IS ONLY REACHABLE ONCE THE BACKLOG HAS AN OWNER -- AND THAT IS THIS CELL.**

⛔ **AND THIS IS THE FOURTH TIME THIS PROJECT HAS BEEN BITTEN BY A CATEGORY WHERE A NAME BELONGS.** R-70:
an owner that is a category decays exactly like NO owner. "the clean-up projects" cost four rounds. `(b)`
this round is HELD OFF THE CUT for precisely that reason. **So: one NAMED owner per row. A category is a
REFUSAL, not an answer.**

### THE NUMBER HAS ALREADY MOVED AND THAT IS THE FIRST ARM

```
  remediation rows                113
  stale at ROUND 8 (the register) 91
  stale at ROUND 9 (this cut)     94
```

Three rows aged past N between round 8's L10 and this cut. **THE SET GROWS WITH THE ROUND NUMBER BY
CONSTRUCTION.** `b42-remeasured` requires you to call the limb YOURSELF at YOUR write time and print the
denominator; **a plan written against 91 is already wrong when it lands, and a plan written against my 94
will be too if you take it on faith.** Call:

```
  srg._stale_open_row(srg._remediation_rows_for_project(<root>, "LGIC_ENFORCE"),
                      <current_round>, srg.STALE_OPEN_ROW_N_ROUNDS)
```

⛔ **`_remediation_ids_for_project` RETURNS A TUPLE `(ids, note)`.** Unpacking it as a bare list produced a
perfectly plausible `109 rowless of 109` earlier in this project, caught only because an INTERMEDIATE
denominator printed `2` on a population known to be 102. **PRINT YOUR INTERMEDIATE DENOMINATORS.** A crash is
the lucky failure; a plausible number is the unlucky one.

### WHAT AN OWNER IS

```
  ACCEPTED   a SERIAL (0.x/1.x/2.x/3.x/4.x) or a PROJECT CODE that exists on the register
  REFUSED    "the clean-up projects", "whoever owns naming", "TBD", "the estate", "a future round",
             any noun phrase that is a class rather than an addressable party
```

`b42-no-category-owners` refuses the record if ANY row's owner is a category. It is a positive
denominator check, not a blacklist grep: **every one of the N rows must carry an owner that resolves.**

### DEFERRAL IS LEGAL AND IT IS NOT FREE

A row you cannot assign is `DEFERRED` **with a REASON and a CONDITION that un-defers it** -- exactly the
"park it on its own carrier with an OWNER and the CONDITION" shape. `b42-deferred-reasons` requires every
DEFERRED row to carry both. ⛔ **A DEFERRED ROW WITH NO CONDITION IS A CATEGORY OWNER WEARING A DIFFERENT
FIELD NAME.**

### WHAT YOU DO NOT DO

⛔ **YOU DO NOT REMEDIATE THE ROWS AND YOU DO NOT CLOSE THEM.** 94 rows is not a round's work and pretending
otherwise produces 94 shallow closures. You are SEATING OWNERSHIP.
⛔ **YOU DO NOT TURN THE LIMB BACK INTO A REFUSAL.** Explicitly not this round -- `R9_BASE.json`
`not_in_this_round_and_why`. The refusal form becomes reachable AFTER ownership exists, as its own deliberate
cut, and never as a condition on a slug.
⛔ **YOU DO NOT EDIT `.tools/surprise-row-gate.py`.** You CALL it.

### WHERE YOUR RECORD GOES

`<WS>/org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/STALE_BACKLOG_R9.json`

```
  {"measured_at_write_time": {"instrument": "srg._stale_open_row(...)", "current_round": <int>,
                              "N_ROUNDS": <int>, "remediation_rows": <int>, "stale": <int>,
                              "intermediate_denominators": {"ids_from_tuple": <int>, "rows": <int>}},
   "assignments": [{"row": "LGIC_ENFORCE-W<n>-S<k>", "owner": "<serial|PROJECT_CODE>",
                    "basis": "..."} ...],
   "deferred":    [{"row": "...", "reason": "...", "uncondition": "..."} ...],
   "coverage": {"stale": <int>, "assigned": <int>, "deferred": <int>,
                "assertion": "assigned + deferred == stale, asserted AFTER the write"}}
```

⛔ **RUN THE COVERAGE ASSERTION AFTER THE WRITE, NOT BEFORE** -- a row can disposition itself out of your
population while you work, and an assertion taken before the write never sees it.

Every instrument you cite goes in that same folder and is **COMMITTED** (row `LGIC_ENFORCE-S69`).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="B42R9-AC1" cell_refs="EN-b-42"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r9/check_en_r9.py b42-remeasured</invocation><expect>PASS-B42-REMEASURED</expect></criterion>

<criterion id="B42R9-AC2" cell_refs="EN-b-42"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r9/check_en_r9.py b42-every-row-owned</invocation><expect>PASS-B42-EVERY-ROW-OWNED</expect></criterion>

<criterion id="B42R9-AC3" cell_refs="EN-b-42"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r9/check_en_r9.py b42-no-category-owners</invocation><expect>PASS-B42-NO-CATEGORY-OWNERS</expect></criterion>

<criterion id="B42R9-AC4" cell_refs="EN-b-42"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r9/check_en_r9.py b42-deferred-reasons</invocation><expect>PASS-B42-DEFERRED-REASONS</expect></criterion>

<criterion id="B42R9-AC5" cell_refs="EN-b-42" judgment="true"/>

**ALL FOUR MECHANICAL CRITERIA READ FAIL AT THE CUT**, MEASURED by the issuer.

⚠ **`B42R9-AC4` IS VACUOUS ON AN EMPTY `deferred` ARRAY** -- "every deferred row carries a reason and an
uncondition" is TRUE of zero rows. A record that defers nothing passes it without the arm ever exercising.
That is CORRECT behaviour and it is disclosed so nobody reads its green as evidence that deferrals were
examined; `B42R9-AC5` is where a human reads whether the assignments are real.

<expected_criteria>B42R9-AC1, B42R9-AC2, B42R9-AC3, B42R9-AC4, B42R9-AC5</expected_criteria>

**`B42R9-AC5`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether each named owner is a party that can
actually act on that row -- an owner assigned to make an arm go green is a category with a serial typed over
it -- and whether the DEFERRED set is honest rather than a dumping ground.

**THE CHECKER'S CONTROLS:** `selftest-arms` drives **27 arms, 13 POSITIVE-SATISFIABILITY**. Run it first. An
arm a CORRECT record cannot satisfy is a BLOCKING surprise row quoting the arm and its output.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/` and this order's own file. Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **YOU DO NOT EDIT `.tools/surprise-row-gate.py`, ANY GATE, OR ANY THRESHOLD.** `STALE_OPEN_ROW_N_ROUNDS` is read, never written. Its N-sweep is a CLIFF (91/86/86/83/0) and moving it would clear the backlog by arithmetic.
- ⛔ **YOU DO NOT CLOSE, DISARM, GRADUATE OR REMEDIATE ANY ROW.** Ownership only.
- ⛔ **YOU DO NOT EDIT `org/standards/NAMING_SCHEMA.json`** -- that is `EN-s-41`'s this round.
- ⛔ **NOTHING LIVE MOVES.** Every AWS read is read-only through the `.tools/aws` shim.
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump the array; assert the non-ASCII CHARACTER count and the backslash-u count unchanged. `len(b)-len(b.decode())` is a BYTE DELTA, not a character count; for a count use `sum(1 for ch in text if ord(ch) > 127)`.
- **Id** `LGIC_ENFORCE-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time. **Two other orders are open this round, and this cell READS that channel -- an id minted from a stale read COLLIDES SILENTLY.**
- **Commit before you grade.**

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.8, round-9 cell `EN-b-42` (section 0i).
<owned_cells>EN-b-42</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `B42R9-AC1` through `B42R9-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/LGIC_ENFORCE.TO-EN-b-42-r9.stale-backlog-owners.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> B42R9-AC1,B42R9-AC2,B42R9-AC3,B42R9-AC4,B42R9-AC5 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-b-42-r9.stale-backlog-owners.md` BEFORE the `complete` flip.
Result file `stale-backlog-owners.r9.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** The instance's `controls` block admits only `mutant`/`determinism`; fold positive-control evidence into `mutant`. `introduces` entries must be LITERAL tokens present at the pin and absent at its parent, not prose.
`B42R9-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the stale count YOU measured with its round number and denominator, `assigned + deferred == stale` asserted AFTER your write, and the distinct owners you named.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-9 cut: no schedule is created or read by this cell. The staleness limb's clock is the ROUND NUMBER, not wall time, so no cadence surface is touched.
comp-iam: RUN at the round-9 cut: no grant moves. The cell reads a repo channel and a repo gate module; no live policy, role or key is read or written.
comp-adversary: RUN at the round-9 cut: the adversarial control is b42-remeasured paired with b42-no-category-owners. The two cheap satisfying moves are (1) to take the register's 91 rather than measuring, which writes a plan that is wrong on arrival and reproduces the exact stale-figure failure that cost this project four rounds on W7-S4, and (2) to assign every row to a plausible-sounding class. The first arm forbids inheriting the figure, the second forbids the class. ⚠ b42-deferred-reasons is VACUOUS on an empty deferred array -- disclosed on the worker face and carried to L9.
lane: <paths> is the grant; deliverables/0.9.0_WK_LGIC_ENFORCE~3/ is granted by the tree convention. .tools/surprise-row-gate.py is IMPORTED and never written -- a read-only dependency the <paths> block cannot express, stated here.
contention: the channel is written by two other open orders this round AND READ BY THIS ONE -- the sharpest id-collision exposure in the round, called out on the worker face. 14b's append-only inversion applies and no slot isolates there.
</preflight>

Seating: slot `~3`, level 0, the only order on its slot. Round 9 of LGIC_ENFORCE, issued by `2.0.0_SA_COO~G` on decomposition v3.8 s.0i, from the REGISTER's WHAT ROUND 9 OWES `(d)`, read at HEAD. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r9/` (`check_en_r9.py`, 12 real arms and a 27-arm self-test with 13 positive-satisfiability arms; `R9_BASE.json` pinning `d9cdb39063`). Rulings carried: R-66, R-70, S82, the 7f82f66f93 disclose-not-refuse reasoning.
