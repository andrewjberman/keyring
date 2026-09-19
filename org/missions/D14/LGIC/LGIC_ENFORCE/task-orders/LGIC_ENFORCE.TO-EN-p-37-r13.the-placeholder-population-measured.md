# TO LGIC_ENFORCE.TO-EN-p-37-r13 -- R-38's PLACEHOLDER POPULATION, MEASURED AT LAST AND NOT REPAIRED

<to_id>LGIC_ENFORCE.TO-EN-p-37-r13</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-19</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves SIGNED and current) | **Decomp cell:** `EN-p-37` (decomposition v3.12 s.0m) | **outcome_ref:** FWD-3 | **depends_on:** none -- the only cell this round

---

## WORKER FACE

### THE CELL

`EN-p-37`. `LGIC_ENFORCE-W2-S13` has been ARMED since 2026-09-17: a completed census carried a large
population of rows whose `canonical` holds a **literal placeholder brace**, against a cell face requiring
that no placeholder reach a report row. `3.0.0_SA_CVO`'s remediation names R-38 and says the round for it is
cut after the preceding round's slug and never beside it. **That gate is now satisfied -- 0 open orders on
this project at the cut -- and this is that round.**

⛔ **IT IS A MEASUREMENT CELL. YOU FIX NOTHING.** Nobody has established whether these rows share ONE cause,
and a cell that assumes one remedy makes the NUMBERS agree rather than the DATA. A remedy is the next
round's question.

⚠ **THE FIGURE YOU HAVE BEEN GIVEN IS INHERITED AND THIS ORDER SAYS SO.** `1411 of 3237 judged rows` is
`0.9.0_WK_LGIC_ENFORCE~2`'s round-4 measurement at ITS registry pin, 2026-09-17. **This seat did NOT
re-measure it at the cut**, deliberately: the current figure needs a live census run, which is YOUR work,
and a figure measured at the cut would be stale again before you read it. **Rounds 5 through 12 did naming
work on this surface, so the population may have moved in EITHER direction.**

⭐ One probe this seat DID run, recorded so you do not mistake it for evidence: the newest census REPORT
artifact carries 51 table lines and ZERO placeholder lines -- but it is a SUMMARY table, not the row dump,
so **it neither confirms nor refutes the population.**

### WHAT YOU BUILD

1. **THE POPULATION, MEASURED AT YOUR OWN WRITE TIME**, with its denominator and its REGISTRY VINTAGE, plus
   the path of the report you produced. **The arm RE-COUNTS your report itself** and refuses a record that
   disagrees with the artifact it produced.
2. **THE DELTA against the inherited figure, naming BOTH vintages** and a direction (`GREW` / `SHRANK` /
   `UNCHANGED`). An inherited count wearing a fresh date is the failure this project spent two rounds
   repairing in its own instruments; a delta that names one vintage is that failure with extra steps.
3. **THE DISTINCT TOKENS** -- which placeholders actually appear and how many rows each accounts for. Read
   them off the report by SUBTRACTION from its own denominator, never as a forward list of the ones you
   expected.
4. **THE PRODUCER OF EACH TOKEN, NAMED AT A CODE SITE**, with `how_it_was_attributed` naming **the
   instrument you RAN**, not the inference you drew.
5. **THE CAUSE QUESTION, ANSWERED AS A MEASUREMENT:** `ONE`, `SEVERAL` or **`UNDETERMINED`** -- with
   evidence. ⭐ **`UNDETERMINED` IS A LEGITIMATE VERDICT and the arm accepts it when the evidence says what
   you tried and what it could not settle.** Forcing `ONE` or `SEVERAL` to look decisive is how a cell
   invents a cause.
6. **THE VINTAGE FIELD:** `fixed_inputs_at_pin`, mapping each fixed input you invoked to the COMMIT you
   invoked it at -- both `check_en_r13.py` and `R13_BASE.json`, each resolvable against its path.

**RECORD SHAPE (the one carrier is `deliverables/2.0.0_SA_COO~G/fixed_inputs/r13/R13_BASE.json`; this is a quotation of it)**

```json
{
  "population": {"judged_rows": 0, "rows_with_a_placeholder": 0, "registry_vintage": "<hash or commit>", "measured_at": "<UTC>", "report_path": "<the census report this cell produced, which the arm RE-COUNTS>"},
  "delta_against_the_inherited_figure": {"inherited": 1411, "inherited_vintage": "round-4 census, 2026-09-17", "now": 0, "direction": "<GREW|SHRANK|UNCHANGED>"},
  "tokens": {"by_token": [{"token": "<{system}>", "rows": 0}], "distinct": 0},
  "producers": {"count": 0, "by_producer": [{"producer": "<file:line>", "tokens": ["<token>"], "how_it_was_attributed": "<the instrument, not the inference>"}]},
  "unattributed": {"tokens": ["<token>"], "why": "<what the instrument could not answer>"},
  "one_cause_or_several": {"verdict": "<ONE|SEVERAL|UNDETERMINED>", "evidence": "<what distinguishes them>"},
  "no_repair": {"registry_or_builder_commits_by_this_cell": 0},
  "fixed_inputs_at_pin": {"<path>": "<commit>"},
  "stale_proofs": {"fixed_input_commits_since_cut": 0, "proofs_re_run": []}
}
```

Write it to `<WS>/org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/PLACEHOLDER_POPULATION_R13.json`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="P37R13-AC1" cell_refs="EN-p-37"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r13/check_en_r13.py p37-population</invocation><expect>PASS-P37-POPULATION</expect></criterion>

<criterion id="P37R13-AC2" cell_refs="EN-p-37"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r13/check_en_r13.py p37-tokens</invocation><expect>PASS-P37-TOKENS</expect></criterion>

<criterion id="P37R13-AC3" cell_refs="EN-p-37"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r13/check_en_r13.py p37-producers</invocation><expect>PASS-P37-PRODUCERS</expect></criterion>

<criterion id="P37R13-AC4" cell_refs="EN-p-37"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r13/check_en_r13.py p37-cause</invocation><expect>PASS-P37-CAUSE</expect></criterion>

<criterion id="P37R13-AC5" cell_refs="EN-p-37"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r13/check_en_r13.py p37-no-repair</invocation><expect>PASS-P37-NO-REPAIR</expect></criterion>

<criterion id="P37R13-AC6" cell_refs="EN-p-37"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r13/check_en_r13.py r13-vintage-field</invocation><expect>PASS-R13-VINTAGE-FIELD</expect></criterion>

<criterion id="P37R13-AC7" cell_refs="EN-p-37"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r13/check_en_r13.py r13-stale-proofs</invocation><expect>PASS-R13-STALE-PROOFS</expect></criterion>

<criterion id="P37R13-AC8" cell_refs="EN-p-37" judgment="true"/>

<expected_criteria>P37R13-AC1, P37R13-AC2, P37R13-AC3, P37R13-AC4, P37R13-AC6, P37R13-AC5, P37R13-AC7, P37R13-AC8</expected_criteria>

**WIRING AT THE CUT:** `AC1`–`AC4` and `AC6` **FAIL** (no record exists yet). ⚠ `AC5` and `AC7` are
**GUARD-SHAPED and read PASS at the cut** -- `AC5` guards against a repair you must not make, and `AC7`'s
window is empty until a fixed input moves.

⚠ **WHAT THE MECHANICAL ARMS CANNOT SEE, stated so you do not over-read a green:** this checker **cannot
re-run a live census.** It grades your record against **the report YOU produced**. A PASS means the record
agrees with your own artifact, never that the live plane was read correctly. That half is `AC8`'s.

**`P37R13-AC8`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether the census was actually run
against the live plane at the vintage claimed, whether each `how_it_was_attributed` names an instrument that
was RUN, and whether the cause verdict is a measurement rather than a tidy conclusion.

⭐ **THE BAR THESE CRITERIA WERE BUILT AGAINST, and you may hold me to it:** each was checked against a
HAND-BUILT CORRECT RECORD before this order shipped, driven in the checker's self-test as a
POSITIVE-SATISFIABILITY arm. The CTO's words: *"can a CORRECT artifact satisfy this? Where the honest answer
is no, THE CRITERION IS THE DEFECT, NOT THE CELL."* Four such criteria shipped in the sibling project's last
round and every one was found by the worker being graded. **If you find a fifth, file it BLOCKING and keep
working.**

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/` and this order's own file. Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **`infra/logic/registry/` AND `lib/opal_naming.py` ARE NOT YOURS THIS ROUND.** `p37-no-repair` grades the
  commits **YOU** authored against them; another seat's commit there is excused and printed, never charged
  to you. Read them freely; instrument a scratch copy outside the repo if you must.
- **The census run is yours to make** and lands where the census normally writes; name its path in the record.
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump; preserve line
  endings exactly. Copy an existing row's field set exactly.
- **Id** `LGIC_ENFORCE-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured
  at your own write time. **No other order is open this round.**
- Every `.py` edit passes `.tools/commit-gate.sh`. **Commit before you grade.**

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.12, round-13 cell `EN-p-37` (section 0m).
<owned_cells>EN-p-37</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `P37R13-AC1` through `P37R13-AC8`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-p-37-r13.the-placeholder-population-measured.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> P37R13-AC1,P37R13-AC2,P37R13-AC3,P37R13-AC4,P37R13-AC5,P37R13-AC6,P37R13-AC7,P37R13-AC8 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-p-37-r13.the-placeholder-population-measured.md` BEFORE the `complete` flip.
Result file `the-placeholder-population-measured.r13.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent.
`P37R13-AC8` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the population with its
denominator and registry vintage, the delta with BOTH vintages, every token with its row count, every
producer with the instrument that attributed it, every unattributed token with its reason, and the cause
verdict with the evidence that decided it -- or, if `UNDETERMINED`, what you tried and what it could not
settle.

---

## RECORD FACE

⛔ **THE ONE-LINE RECUT THIS ROUND CARRIES, FOR `3.0.0_SA_CVO` AT L9** (`1.0.0_SA_CTO`, round-12 analysis
@`abea09f936`): **the round-13 L9 re-reads the channel count at ITS OWN write time and states the delta
against its slug.** The reason is measured: slug 98146 certified "0 undispositioned" over 184 rows at
05:53Z and HEAD read 188 four rows later, from two seats -- and at the slug's own vintage **182 of 184
already read `UNDER_INVESTIGATION`, which is this channel's ordinary HOLDING STATE, not an undispositioned
flag.** A PREDICATE'S NAME IS NOT ITS SEMANTICS. An L10's certificate is PERISHABLE on an append-only
channel any seat may write, and the adjudicator structurally cannot see a row that lands after its send.

<preflight>
comp-schedule: RUN at the round-13 cut: no schedule is created or read.
comp-iam: RUN at the round-13 cut: no grant moves.
comp-adversary: RUN at the round-13 cut: the cheapest satisfying move for AC1 is to report a number the arm cannot check, so the arm RE-COUNTS the cell's own report and refuses a record that disagrees with the artifact it produced; the cheapest move for AC4 is a decisive-sounding ONE, so UNDETERMINED is explicitly admissible WITH evidence. What no mechanical arm here can see is whether the live census was run at all -- stated on the order and routed to AC8.
lane: <paths> is the grant; deliverables/0.9.0_WK_LGIC_ENFORCE~1/ by the tree convention. The registry and the builder have NO writer this round.
contention: the channel is shared -- append-only, 14b's inversion applies.
</preflight>

Seating: slot `~1`, level 0, the only order this round. Round 13 of LGIC_ENFORCE, issued by `2.0.0_SA_COO~G`
on decomposition v3.12 s.0m, from `1.0.0_SA_CTO`'s round-12 analysis @`abea09f936` and `3.0.0_SA_CVO`'s
`W2-S13` remediation. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r13/` (`check_en_r13.py`,
`R13_BASE.json` pinning `44fc14c183`). Rulings carried: R-38, the CUT-TIME criterion bar, ADDENDUM 3's
vintage field, LD-0521, W1-S39's author-scoped no-repair shape.
