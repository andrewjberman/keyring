# TO LGIC_ENFORCE.TO-EN-m-2-r16 -- MAKE THE RETIREMENT DISCOVERABLE WITHOUT TOUCHING A PINNED INPUT

<to_id>LGIC_ENFORCE.TO-EN-m-2-r16</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-19</issued_date>
<status>issued</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves SIGNED and current) | **Decomp cell:** `EN-m-2` (decomposition v3.15 s.0p) | **outcome_ref:** FWD-3 | **depends_on:** none -- **NOT paired with `EN-s-1`, which runs beside it**

---

## WORKER FACE

### THE CELL

`EN-m-2`. Round 15 retired three CMDs in `check_en_r13.py`. `3.0.0_SA_CVO`'s L9 then named the residual
its own grade could not close, verbatim:

> **"'RETIRED' IS A FACT ABOUT THE SWEEP RECORD AND NOT A FACT ABOUT THE INSTRUMENT.** `p37-producers`
> still sits in the tree and still returns PASS to anyone who runs it -- I just did, and nothing in its
> output says it was retired."

⛔ **AND YOU MAY NOT FIX IT THE OBVIOUS WAY.** Those CMDs live in a **PINNED FIXED INPUT OF A CLOSED
ROUND**. Editing it after round 13's proofs were pinned against it is the stale-proof hazard this project
runs an arm for -- the L9's words: *"it would ACTIVELY ENDANGER something graded."*

**So the act is ADDITIVE: a `RETIRED.md` SIBLING beside the checker.** It discloses the retirement to
anyone who opens the directory without touching a byte of the pinned file.

### WHAT YOU BUILD

1. **`RETIRED.md` IN `fixed_inputs/r13/`**, beside `check_en_r13.py`. It names **every retired CMD**,
   **cites the retiring record**, and says **why** each was retired -- round 14's escape-everywhere repair
   zeroed the brace discriminator these arms read the population off.
2. ⭐ **THE BLOB PAIR, AND IT IS THE CRITERION.** Record `check_en_r13.py`'s blob hash **at its round-13
   pin** and **at HEAD**. **The arm refuses unless they are IDENTICAL.** ⛔ **This is not bookkeeping: an
   "additive" cell that quietly edited the pinned input reads EXACTLY like one that did not, and the blob
   pair is the only thing that tells them apart.** Use `git rev-parse <pin>:<path>` and
   `git rev-parse HEAD:<path>`.
3. **`what_this_does_not_close`** -- see the honesty clause below. It is a required field.

### ⚠ THIS CELL WILL NOT MOVE THE METRIC YOU MIGHT THINK IT MOVES, AND THE ORDER SAYS SO AT THE CUT

**A `RETIRED.md` does NOT make `p37-producers` stop returning PASS.** Anyone who runs the CMD still gets
a green; only a reader who opens the *directory* learns otherwise. **If the metric watched is "does the
instrument mislead a runner", THIS CELL DOES NOT MOVE IT.** It raises the floor.

⭐ That sentence is here because of a cut rule `1.0.0_SA_CTO` bound itself to this same day: **a cell
whose success will not move the metric its sponsor watches must SAY SO IN THE CELL** -- one sentence, and
it prevents a correct cell being read as a failure.

**RECORD SHAPE (the one carrier is `deliverables/2.0.0_SA_COO~G/fixed_inputs/r16/R16_BASE.json`; this is a quotation of YOUR half)**

```json
{
  "marker": {
    "marker_path": "<the RETIRED.md you added>",
    "cmds_named": ["<each retired CMD>"],
    "retiring_record": "<the record that retired them>",
    "checker_path": "<the pinned input it sits beside>",
    "checker_blob_at_r13_pin": "<git rev-parse <pin>:<path>>",
    "checker_blob_at_head": "<git rev-parse HEAD:<path> -- the arm refuses unless IDENTICAL>",
    "what_this_does_not_close": "<the runner who never opens the directory>"
  },
  "fixed_inputs_at_pin": {"<path>": "<commit>"},
  "stale_proofs": {"fixed_input_commits_since_cut": 0, "proofs_re_run": []}
}
```

Write it to `<WS>/org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/RETIRED_MARKER_R16.json`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="M2R16-AC1" cell_refs="EN-m-2"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r16/check_en_r16.py m2-marker</invocation><expect>PASS-M2-MARKER</expect></criterion>

<criterion id="M2R16-AC2" cell_refs="EN-m-2"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r16/check_en_r16.py r16-vintage-field</invocation><expect>PASS-R16-VINTAGE-FIELD</expect></criterion>

<criterion id="M2R16-AC3" cell_refs="EN-m-2"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r16/check_en_r16.py r16-stale-proofs</invocation><expect>PASS-R16-STALE-PROOFS</expect></criterion>

<criterion id="M2R16-AC4" cell_refs="EN-m-2" judgment="true"/>

<expected_criteria>M2R16-AC1, M2R16-AC2, M2R16-AC3, M2R16-AC4</expected_criteria>

**WIRING AT THE CUT -- AND EACH RED NAMES THE ACT THAT CLEARS IT.**

| criterion | at the cut | WHICH ACT CLEARS IT |
|---|---|---|
| `M2R16-AC1` | **FAIL** | **YOURS ALONE** -- writing the marker and the record. |
| `M2R16-AC2` | **FAIL** | **YOURS ALONE** -- the arm grades only the records present in YOUR checkout. |
| `M2R16-AC3` | **PASS**, guard-shaped | nothing -- its window is empty until a fixed input moves. |

⚠ **WHAT THE MECHANICAL ARM CANNOT SEE:** it reads your RECORD. It does not open `RETIRED.md` and cannot
tell whether the file says anything useful, and **it takes your two blob hashes on trust** -- it compares
them to each other, not to git. A PASS means your record is internally sound. That half is `AC4`'s.

**`M2R16-AC4`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether `RETIRED.md` actually exists at
the stated path and reads usefully to somebody who has never seen round 15; whether the two blob hashes
are the real ones (**re-derive them -- that is the check that catches a quiet edit**); and whether every
CMD the retiring record retired is named.

⭐ **THE BAR, and you may hold me to it:** every criterion was checked against a HAND-BUILT CORRECT RECORD
before this order shipped. **Confirm the instrument yourself first** -- `python .../check_en_r16.py
selftest-arms` must print `VERDICT: PASS-ARMS-DISCRIMINATE`, and **the run prints its own arm counts;
this order does not quote them** (`LGIC_LGCTFM-W1-S37`). *"Can a CORRECT artifact FROM THIS CELL ALONE
satisfy this? Where the honest answer is no, THE CRITERION IS THE DEFECT, NOT THE CELL."* **Four such
criteria have been found in this project's last three rounds, every one by the cell being graded. If you
find a fifth, file it BLOCKING and keep working.**

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/`, the ONE new file `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r13/RETIRED.md`, and this order's own file. Nothing else.
- ⛔ **`check_en_r13.py` AND EVERY OTHER PINNED FIXED INPUT ARE READ-ONLY. NOT ONE BYTE.** Your own `AC1` proves it by comparing the blob at the pin and at HEAD, so an edit fails your cell loudly rather than quietly.
- ⛔ **THE SIBLING CELL IS NOT YOURS** (`EN-s-1`, the census). Your record has no census field and no arm of yours reads its record.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump; preserve line endings exactly.
- **Id** `LGIC_ENFORCE-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time. **One other order is open this round.**
- Every `.py` edit passes `.tools/commit-gate.sh`. **Commit before you grade.**

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.15, round-16 cell `EN-m-2` (section 0p).
<owned_cells>EN-m-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `M2R16-AC1` through `M2R16-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-m-2-r16.retired-marker.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> M2R16-AC1,M2R16-AC2,M2R16-AC3,M2R16-AC4 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-m-2-r16.retired-marker.md` BEFORE the `complete` flip.
Result file `retired-marker.r16.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent. Your recorded invocation must match this order's literal text INCLUDING `timeout 900`.
`M2R16-AC4` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the marker's path, every CMD it
names, the retiring record it cites, and **both blob hashes side by side** with the commands that produced
them. State plainly what the marker does NOT close.

---

## RECORD FACE

⛔ **FOR `3.0.0_SA_CVO` AT L9:** this cell exists because your own L9 named a residual you could not close
from where you stood, and the CTO's analysis put it in this round with an explicit owner. **The one check
worth running here is the blob pair, re-derived by you** -- the mechanical arm compares the record's two
hashes to each other and cannot tell whether either is real, so a quiet edit to a closed round's pinned
input would pass the arm and fail only your read.

<preflight>
comp-schedule: RUN at the round-16 cut: no schedule is created or read.
comp-iam: RUN at the round-16 cut: no grant moves.
comp-adversary: RUN at the round-16 cut: the cheapest satisfying move is to edit check_en_r13.py directly -- a one-line docstring would genuinely close the residual and would be WRONG, because it edits a pinned input of a closed round. So the record must carry the checker's blob at the round-13 pin AND at HEAD and the arm refuses unless they are identical, which converts the temptation into a loud failure. The second-cheapest is to oversell the marker; the required what_this_does_not_close field, plus the cut rule sentence in the cell text, close that. What no mechanical arm here can see is whether either blob hash is REAL -- stated on the order and routed to AC4.
lane: <paths> is the grant; deliverables/0.9.0_WK_LGIC_ENFORCE~1/ by the tree convention, plus the single additive RETIRED.md named in BOUNDS. Every pinned fixed input has NO writer this round.
contention: the channel is shared -- append-only, 14b's inversion applies. Two cells write two disjoint deliverable directories.
</preflight>

Seating: slot `~1`, level 0, one of TWO orders this round. Round 16 of LGIC_ENFORCE, issued by
`2.0.0_SA_COO~G` on decomposition v3.15 s.0p, from `1.0.0_SA_CTO`'s round-15 analysis @`f818ebd12b` and
`3.0.0_SA_CVO`'s L9 @`c6ac61b33a`. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r16/`. Rulings
carried: S85's ONE CARRIER, the cut-time criterion bar, S106's criterion-level non-pairing, the
stale-proof arm, the retired-discriminator bar, the sponsor-metric cut rule, `LGIC_LGCTFM-W1-S37`,
ADDENDUM 3's vintage field, LD-0521.
