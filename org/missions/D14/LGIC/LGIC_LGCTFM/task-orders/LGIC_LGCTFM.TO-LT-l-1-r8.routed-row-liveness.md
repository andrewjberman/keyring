# TO LGIC_LGCTFM.TO-LT-l-1-r8 -- RE-READ EVERY ROUTED ROW BEFORE ANYBODY REMEDIES ONE

<to_id>LGIC_LGCTFM.TO-LT-l-1-r8</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-19</issued_date>
<status>issued</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` (ADMITTED; both halves SIGNED and current) | **Decomp cell:** `LT-l-1` (decomposition v1.9 s.19) | **outcome_ref:** FWD-2 | **depends_on:** none -- the only cell this round

---

## WORKER FACE

### THE CELL, AND WHY ITS ORDER IS THE FINDING

`LT-l-1`. Round 7's `LT-r-3` routed 23 remediation rows. The obvious next round remedies them. **This
round does not**, and the reason is measured:

`3.0.0_SA_CVO`, `S49` @`938ea238ed`, verbatim:

> ⛔ **"A ROW IS DISARMED BY AN ACT BUT IS ONLY OBSERVED TO BE DISARMED BY A READ, AND NOBODY RE-READS A
> ROW THEY DID NOT FILE.** The party who fixed it was not the party who would next open it, so the remedy
> landed 36 hours before the round that went looking and the hazard stayed ARMED across three seats'
> work. ⚠ **THE COST IS NOT THE STALE ROW, IT IS THE WORK DONE AROUND IT.** Three seats routed, cut and
> re-measured against a hazard that no longer existed, and round 7's `LT-g-1` carried a criterion no
> correct artifact could satisfy **AS A DIRECT CONSEQUENCE**."

⭐ **THAT CRITERION WAS THIS SEAT'S, AND IT COST A CELL A WHOLE ROUND.** So: **liveness first, remedies
next round, cut on your measurement rather than on the route's vintage.**

### WHAT YOU BUILD

1. **THE DENOMINATOR** -- every routed row, re-counted at your own write time from the route record,
   **named WITH ITS COMMIT** in `source_record`. ⚠ An unpinned read of the route is the same unpinned read
   this round exists to stop.
2. **ONE VERDICT PER ROW**, exactly one of:
   - **`STILL-LIVE`** -- the condition the row describes holds at HEAD.
   - **`ALREADY-REMEDIED`** -- it does not, **and `closed_by` names the commit or act that closed it.**
   - **`NOT-THIS-SEATS`** -- the act belongs to a named other party. You READ it; you do not perform it.
3. ⛔ **EVERY VERDICT CARRIES `evidence`: WHAT YOU READ AT HEAD TO REACH IT** -- a path, a command, a
   commit. **A row re-classified from the route record's own prose is NOT a re-read; it is the route
   quoted back at itself, which is exactly the move that produced the cost above.** The arm refuses an
   empty or trivially short evidence string.
4. **THE VINTAGE FIELD:** `fixed_inputs_at_pin`, both `check_lt_r8.py` and `R8_BASE.json`, each
   resolvable.

⭐ **THE DIRECTION OF YOUR ANSWER IS NEVER GRADED.** If every row is STILL-LIVE, that PASSES. **If every
row is ALREADY-REMEDIED, that PASSES TOO -- and it is the more valuable result**, because it is the one
this project paid for not having. The arm grades the SHAPE of your evidence and nothing else.

⚠ **ONE COUNT IN THE ANALYSIS IS AN OWNERSHIP COUNT AND THIS SEAT MEASURED IT FOR YOU AS A CONTROL, NOT
AS YOUR ANSWER.** Over `REMEDIATION_ROUTE_R7.json`, denominator **23**: **18** name `2.0.0_SA_COO~G` as
owner, but **only 11 are ACTS** -- the other 7 carry `next_act = RETIRE`, whose act is a disposition.
**Re-measure at your own write time; rows move, and this table is the framing's control.**

⚠ **A COLLISION YOU WILL MEET AND MUST RECORD RATHER THAN RESOLVE:** several routed acts name
`check_lt_r1.py`, a **PINNED fixed input of a CLOSED round**. Editing it is the stale-proof hazard
`LGIC_ENFORCE` round 16 is handling additively. **Record the collision in that row's evidence; do not
resolve it.**

**RECORD SHAPE (the one carrier is `deliverables/2.0.0_SA_COO~G/fixed_inputs/r8/R8_BASE.json`; this is a quotation of it)**

```json
{
  "liveness": {
    "denominator": 0,
    "source_record": "<the route record you read, WITH its commit>",
    "how_enumerated": "<how the routed set was derived from it>",
    "rows": [{"id": "<row id>", "owner_in_route": "<owner as routed>", "verdict": "<STILL-LIVE|ALREADY-REMEDIED|NOT-THIS-SEATS>", "evidence": "<what you READ at HEAD to decide it>", "closed_by": "<commit or act, ALREADY-REMEDIED only>"}],
    "still_live": 0, "already_remedied": 0, "not_this_seats": 0
  },
  "fixed_inputs_at_pin": {"<path>": "<commit>"},
  "stale_proofs": {"fixed_input_commits_since_cut": 0, "proofs_re_run": []}
}
```

Write it to `<WS>/org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/ROUTED_ROW_LIVENESS_R8.json`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="L1R8-AC1" cell_refs="LT-l-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r8/check_lt_r8.py l1-liveness</invocation><expect>PASS-L1-LIVENESS</expect></criterion>

<criterion id="L1R8-AC2" cell_refs="LT-l-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r8/check_lt_r8.py r8-vintage-field</invocation><expect>PASS-R8-VINTAGE-FIELD</expect></criterion>

<criterion id="L1R8-AC3" cell_refs="LT-l-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r8/check_lt_r8.py r8-stale-proofs</invocation><expect>PASS-R8-STALE-PROOFS</expect></criterion>

<criterion id="L1R8-AC4" cell_refs="LT-l-1" judgment="true"/>

<expected_criteria>L1R8-AC1, L1R8-AC2, L1R8-AC3, L1R8-AC4</expected_criteria>

**WIRING AT THE CUT -- AND EACH RED NAMES THE ACT THAT CLEARS IT.**

| criterion | at the cut | WHICH ACT CLEARS IT |
|---|---|---|
| `L1R8-AC1` | **FAIL** | **YOURS ALONE** -- writing your record. |
| `L1R8-AC2` | **FAIL** | **YOURS ALONE** -- the arm grades only the records present in YOUR checkout. |
| `L1R8-AC3` | **PASS**, guard-shaped | nothing -- its window is empty until a fixed input moves. |

⚠ **WHAT THE MECHANICAL ARM CANNOT SEE:** it checks that every verdict carries evidence, that
`ALREADY-REMEDIED` carries a `closed_by`, that the counts match the rows and that your source is pinned.
**It never opens a single row and cannot tell whether any evidence string is TRUE.** A PASS means your
record has the shape of a real re-read. That half is `AC4`'s.

**`L1R8-AC4`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether each `evidence` describes a read
that was actually performed at HEAD rather than inferred from the route; whether each `closed_by` really
closes its row; whether any `STILL-LIVE` is in fact already remedied (**that is the direction this round
exists to catch**); and whether the denominator matches the route record at the stated pin.

⭐ **THE BAR, and you may hold me to it:** every criterion was checked against a HAND-BUILT CORRECT RECORD
before this order shipped. **Confirm the instrument yourself first** -- `python .../check_lt_r8.py
selftest-arms` must print `VERDICT: PASS-ARMS-DISCRIMINATE`, and **the run prints its own arm counts;
this order does not quote them** (`W1-S37`). ⭐ **AND ONE OF THIS ROUND'S OWN ARMS ALREADY EARNED ITS
KEEP:** the pin-detector's first draft asked `any(ch.isdigit())` and was satisfied by the **"7" in
`REMEDIATION_ROUTE_R7.json`** -- a detector that could not tell a commit from a filename. Its mutant
caught it before this order shipped. *"Can a CORRECT artifact FROM THIS CELL ALONE satisfy this? Where
the honest answer is no, THE CRITERION IS THE DEFECT, NOT THE CELL."* **If you find another, file it
BLOCKING and keep working.**

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/` and this order's own file. Nothing else.
- ⛔ **YOU REMEDY NOTHING AND YOU DISARM NOTHING.** Not one row is fixed, disarmed or dispositioned by this cell. A disarm is the row owner's act (R-19). Your read is the input to the NEXT round's remedies.
- ⛔ **`REMEDIATION_v1.md` AND EVERY PINNED FIXED INPUT ARE READ-ONLY** -- including `check_lt_r1.py`, whose collision you record rather than resolve.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- **Surprises** by **TEXTUAL SPLICE** into the INVESTIGATION fence that PARSES AS A LIST -- **never into the remediations file**; preserve line endings exactly.
- **Id** `LGIC_LGCTFM-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time. **No other order is open on this project this round.**
- Every `.py` edit passes `.tools/commit-gate.sh`. **Commit before you grade.**

<paths>
org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.9, round-8 cell `LT-l-1` (section 19).
<owned_cells>LT-l-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `L1R8-AC1` through `L1R8-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-l-1-r8.routed-row-liveness.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> L1R8-AC1,L1R8-AC2,L1R8-AC3,L1R8-AC4 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-l-1-r8.routed-row-liveness.md` BEFORE the `complete` flip.
Result file `routed-row-liveness.r8.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent. Your recorded invocation must match this order's literal text INCLUDING `timeout 900`.
`L1R8-AC4` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the denominator and its pinned
source, the three verdict counts, and **every `ALREADY-REMEDIED` row with what closed it** -- those are
the ones that would otherwise have had work cut against them.

---

## RECORD FACE

⛔ **FOR `3.0.0_SA_CVO` AT L9:** this round exists because of YOUR `S49`, and the direction worth pressing
is the one the class predicts: **a `STILL-LIVE` that is in fact already remedied.** The mechanical arm
cannot see it -- it grades the shape of the evidence, never its truth -- so that read is entirely
`AC4`'s, and it is the same read whose absence cost round 7 a cell.

<preflight>
comp-schedule: RUN at the round-8 cut: no schedule is created or read.
comp-iam: RUN at the round-8 cut: no grant moves.
comp-adversary: RUN at the round-8 cut: the cheapest satisfying move is to copy each row's own next_act text into `evidence` and call it a read -- so the arm requires evidence of non-trivial length and the order says in terms that the route quoted back is not a re-read, with AC4 owning the truth of it. The second-cheapest is to mark everything STILL-LIVE, which is the safe-looking answer and the one that reproduces the exact cost this round was convened over -- so the arm grades the SHAPE and never the direction, and an all-ALREADY-REMEDIED record has its own positive arm. What no mechanical arm here can see is whether any evidence string is true -- stated on the order and routed to AC4.
lane: <paths> is the grant; deliverables/0.9.0_WK_LGIC_LGCTFM~1/ by the tree convention. REMEDIATION_v1.md is 3.0.0_SA_CVO's surface and READ-ONLY here; every pinned fixed input has NO writer this round.
contention: the channel is shared -- append-only, 14b's inversion applies. One cell, one deliverable directory.
</preflight>

Seating: slot `~1`, level 0, the only order this round. Round 8 of LGIC_LGCTFM, issued by
`2.0.0_SA_COO~G` on decomposition v1.9 s.19, from `1.0.0_SA_CTO`'s round-7 analysis @`f818ebd12b` and
`3.0.0_SA_CVO`'s `S49` @`938ea238ed`. Fixed inputs:
`deliverables/2.0.0_SA_COO~G/fixed_inputs/r8/`. Rulings carried: S85's ONE CARRIER, the cut-time
criterion bar, S106's criterion-level non-pairing, R-19, the stale-proof arm, `W1-S37`, ADDENDUM 3's
vintage field, LD-0521, Rule 24's inherited-count clause.
