# TO LGIC_CANON.TO-CN-o-5-r4 -- the onboarding checklist's FIRST REAL RUN, on a practice wave, graded on reached + carded

<to_id>LGIC_CANON.TO-CN-o-5-r4</to_id>
<project>LGIC_CANON</project>
<issued_to>0.9.0_WK_LGIC_CANON~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-18</issued_date>
<status>complete -- proof-of-spec VALID (rc=0) against org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~1/LGIC_CANON.TO-CN-o-5-r4.checklist-first-run.proof_of_spec.json, gate run 2026-09-18 by the worker with --governing-order bound; all 7 mechanical criteria (C6R4-AC1..AC7) PASS-by-output, reached 12 + carded 4 = 16 of 16 checklist steps, C6R4-AC8 JUDGMENT left for 3.0.0_SA_CVO at L9</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_CANON_PRD.md` v1.7 (ADMITTED; both halves SIGNED and current) | **Decomp cell:** `CN-o-5` (decomposition v6 s.0f; the PRD calls it C6) | **outcome_ref:** FWD-5 | **depends_on:** LGIC_LGCTFM round 1 terminal -- MET, 14 of 14, and its wave is named below by CONTENT HASH rather than by label

---

## WORKER FACE

### THE CELL

`CN-o-5` -- the PRD's **C6** (DEC-6, cell table row C6). **You take the 49 Financial subject through
`infra/logic/10_ONBOARDING_CHECKLIST.md` end to end on LGIC_LGCTFM's practice wave, and you record the run STEP BY
STEP.** You write no engine code and you move nothing live.

**THIS CELL WAS HELD FOR WEEKS ON TWO GATES THAT ARE BOTH LIFTED**, and the decomposition said otherwise until this
round's re-cut. Read s.0f for the whole correction; the short form is that Andrew lifted G-N himself
(*"...because we don't have a new firm to test and I don't feel like messing around making demo cruft"*) and **R-34**
released the `ADVI_FIRMBKTS` dependency. **No demonstration firm is invented for this run** -- that is why G-N was
lifted rather than satisfied.

### THE BAR, AND IT IS NOT "EVERY STEP COMPLETED"

**R-34, verbatim:** *"The outcome is graded on what the wave reaches plus its carded set -- `reached + carded ==
steps`, denominators printed."*

So **every step is REACHED or CARDED, and nothing else.** A run that stops at the first unreachable step FAILS. A run
that silently skips a step FAILS. A run that CARDS a step with an owner and a reason and keeps going is doing exactly
what the ruling asks.

**The checklist says this about itself, at its own close:** *"It cannot be completed from end to end at this vintage.
Each STOP point names an OWNER, so none of them is blocked."* **R-34's shape is already written into the
instrument** -- your job is to run it and account for every step, not to force it to finish.

### MEASURED AT THE CUT, and re-measure all of it at your own tree

```
  steps the checklist declares .................... 16   (### STEP <n> -- headings)
  steps naming a `rule:` .......................... 16
  steps naming a `builder:` ....................... 16
  **STOP -- blocks ................................  2   owners: ADVI_FIRMBKTS (:295), 1.0.0_SA_CTO (:359, register entry X8)
  steps whose builder does not exist yet .......... 2   (`built: no`, each naming the cell that builds it)
```

**THE SUBJECT, named by CONTENT because a label is not an identity (R-40):** LGIC_LGCTFM's practice wave
`20260918T011619Z-8db9eb1` under `workflows/legacy_transform/blackdiamond-49financial/`, whose `contract.json` hashes
**`33204e29839de89af81fb293317cce3ccdf2266d`**. That hash agreed across three instruments at the cut -- `git
hash-object` on the worktree file, `git rev-parse HEAD:<path>` on the record, and the run's own `HASHES.json`. **If it
does not agree at your tree, STOP and file a BLOCKING row: the wave moved, and that is the issuer's problem, not
something to work around.**

### WHAT YOU WRITE

**`C6_RUN_RECORD.json`** in your own deliverables folder:

```
{"subject": {"run_id": "<the wave's id>", "contract_hash": "<its contract.json hash, measured by you>"},
 "reached": [ {"step": <int>, "rule": "<the checklist's own rule: line for that step, verbatim>",
               "builder": "<its own builder: line, verbatim>", "evidence": "<what you ran and what it printed>"} ],
 "carded":  [ {"step": <int>, "owner": "<serial or directive>", "reason": "<why this step cannot be reached now>"} ],
 "rows_filed": [ "<every surprise row id this run raised; [] if none, printed rather than omitted>" ],
 "served":   {"instrument": "<how you read the served plane>",
              "before": {"routes_sha256": "..."}, "after": {"routes_sha256": "..."}},
 "live_acts": []   <- an EMPTY LIST, present. A missing field is silence; [] is a measurement.
}
```

⛔ **`rule` AND `builder` ARE COPIED FROM THE CHECKLIST, VERBATIM, PER STEP.** The arm compares them to the
checklist's own lines, so a "reached" claim is BOUND TO ITS INSTRUMENT rather than asserted. A paraphrase fails.

**`C6_RUN.md`** beside it -- the prose record a human reads: what happened at each step, what each STOP cost, and what
the carded set means for FWD-5.

**`C6_HASHES.json`** -- the R-40 manifest, written after both files are final, declaring exactly
`C6_RUN_RECORD.json` and `C6_RUN.md` with their `git hash-object` shas.

### ONE KNOWN STALENESS YOU WILL MEET, ALREADY FILED

Row **`LGIC_CANON-S19`**: the checklist's **Step 11** (:314-315) says *"at this vintage the kill switch
`org/mcp/naming-gate.enforce` is absent, so the stage prints `WARN` where it would refuse, and exits 0."* **That file
EXISTS at HEAD and the stage REFUSES.** You will meet a refusal where the step promises a warning.

**CORRECT STEP 11's TEXT** as part of this run -- it is inside your grant and it is the cell that discovered it in
practice. Say what the stage actually does now, and cite the flag's existence. Do not touch any other step's text
unless the run proves it wrong too, and if it does, that is a row AND a correction.

**Read:** the whole checklist; `LGIC_CANON_PRD.md` DEC-6 and its ENDPOINT card for FWD-5; decomposition v6 s.0f;
rows `LGIC_CANON-S19` and the project channel; `infra/logic/02_DOCTRINE.md` for any rule a step cites that you need to
read at its source.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="C6R4-AC1" cell_refs="CN-o-5"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_cn_r4.py c6-steps</invocation><expect>PASS-C6-EVERY-STEP-REACHED-OR-CARDED</expect></criterion>

<criterion id="C6R4-AC2" cell_refs="CN-o-5"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_cn_r4.py c6-carded-owners</invocation><expect>PASS-C6-EVERY-CARDED-STEP-NAMES-AN-OWNER</expect></criterion>

<criterion id="C6R4-AC3" cell_refs="CN-o-5"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_cn_r4.py c6-step-evidence</invocation><expect>PASS-C6-EVERY-REACHED-STEP-BOUND-TO-ITS-INSTRUMENT</expect></criterion>

<criterion id="C6R4-AC4" cell_refs="CN-o-5"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_cn_r4.py c6-nothing-live</invocation><expect>PASS-C6-NOTHING-LIVE-MOVED</expect></criterion>

<criterion id="C6R4-AC5" cell_refs="CN-o-5"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_cn_r4.py c6-rows</invocation><expect>PASS-C6-EVERY-SURPRISE-FILED</expect></criterion>

<criterion id="C6R4-AC6" cell_refs="CN-o-5"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_cn_r4.py c6-subject</invocation><expect>PASS-C6-SUBJECT-IS-THE-HASH-BOUND-WAVE</expect></criterion>

<criterion id="C6R4-AC7" cell_refs="CN-o-5"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_cn_r4.py c6-hashes</invocation><expect>PASS-C6-RECORD-BOUND-TO-ITS-HASHES</expect></criterion>

<criterion id="C6R4-AC8" cell_refs="CN-o-5" judgment="true"/>

<expected_criteria>C6R4-AC1, C6R4-AC2, C6R4-AC3, C6R4-AC4, C6R4-AC5, C6R4-AC6, C6R4-AC7, C6R4-AC8</expected_criteria>

**AT THE CUT ALL SEVEN MECHANICAL CRITERIA READ FAIL**, each because its input does not exist yet -- measured by the
issuer, not assumed. There is no guard-shaped criterion in this cell.

**THE CHECKER WAS BUILT WITH A CONTROL THIS ESTATE ONLY DERIVED LAST NIGHT, and you should know it exists:** every
core is driven against a **SIMULATED CORRECT RUN RECORD** and must PASS, as well as against a doctored one and must
FAIL. Three of this issuer's arms on sibling projects were UNSATISFIABLE BY A CORRECT FIX in one evening -- each
passed its mutant test and still could not be satisfied by the right answer. `selftest-arms` prints 20 arms, 5 of them
that positive-satisfiability check. **If you nonetheless find an arm a correct run cannot satisfy, that is a BLOCKING
row naming the arm and quoting its output, never a workaround.**

**`C6R4-AC8`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether the run is a genuine end-to-end exercise of
the checklist rather than a step-by-step transcription of it -- did anything have to be invented at any step, and does
the carded set name real, closeable gaps? **FWD-5 does not reach EXERCISED on this cell alone:** its DONE-WHEN also
requires *"that firm's people can see their dashboard at the end"*, and that is why the bar is reached-plus-carded.

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_CANON/deliverables/<your serial>/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row, never an override.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only** -- everything under `deliverables/2.0.0_SA_COO~G/fixed_inputs/`.
- ⛔ **NOTHING LIVE MOVES, AND THIS IS THE CELL WHERE THAT MATTERS MOST**, because the checklist's steps describe real acts: **no `safe-apply`, no Terraform apply, no AWS write, no bucket mint, no IAM change, no route change, no promote, no portal write.** Every step is exercised as a READ or as a DRY RUN, and where a step cannot be exercised without a live act, **that step is CARDED with its owner** -- that is precisely what the carded set is for. The served dashboard is READ. `live_acts` is `[]` and the arm refuses a non-empty one.
- **AWS reads are read-only through the `.tools/aws` shim.**
- **Surprises** go to `org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, appended to the fence that PARSES AS A LIST (that channel's investigations file carries one array; other documents under the channel carry their own), keeping every existing row's indentation byte-for-byte. Id `LGIC_CANON-W<n>-S<k>`, `<k>` ONE ABOVE the highest `LGIC_CANON-W<n>-S` in ANY document under that channel directory. Keep working after filing. A row's `disarm_owner` is never a worker serial.
- **Judge from the files this order names and cite them** (`path:line @commit`).
- **Numbers in this order are CONTEXT, measured by the issuer at the cut, never acceptance values.** Re-measure at your own tree.
- **Commit before you grade.** The checker reads the tree it runs in.
- **Disk is tight.** Keep scratch small; delete any temporary worktree you create before you report.

<paths>
infra/logic/10_ONBOARDING_CHECKLIST.md
org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_CANON/decompositions/LGIC_CANON_DECOMP.md</decomp_doc> v6, round-4 cell `CN-o-5` (section 0f).
<owned_cells>CN-o-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `C6R4-AC1` through `C6R4-AC8`. Instance at
`org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~1/LGIC_CANON.TO-CN-o-5-r4.checklist-first-run.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> C6R4-AC1,C6R4-AC2,C6R4-AC3,C6R4-AC4,C6R4-AC5,C6R4-AC6,C6R4-AC7,C6R4-AC8 --governing-order org/missions/D14/LGIC/LGIC_CANON/task-orders/LGIC_CANON.TO-CN-o-5-r4.checklist-first-run.md` BEFORE the `complete` flip.
Result file `checklist-first-run.r4.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`C6R4-AC8` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape, and PRINT THE THREE COUNTS in it -- reached, carded, and the checklist's step total.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-4 cut: the run READS trigger and schedule state where a step names one; no schedule is created.
comp-iam: RUN at the round-4 cut: no grant moves. Steps that would need one (the firm bucket's mint, the IAM fence, the sign-in) are exercised as reads or CARDED with their owner -- that is the cell's whole design, not a limitation of it.
comp-adversary: RUN at the round-4 cut: the checker's own positive-satisfiability arms are the adversarial control -- every core is driven against a SIMULATED CORRECT RECORD and must PASS, because three of this issuer's arms in one night were unsatisfiable by a correct fix and each had passed its mutant test.
lane: the <paths> block is the grant (RULING 1 shape c); deliverables/<serial>/ is granted by the tree convention. infra/logic/10_ONBOARDING_CHECKLIST.md is C5's deliverable and is granted HERE because C6 is the cell that discovers its staleness in practice (row LGIC_CANON-S19) and C5 is complete.
contention: the checklist is written by no other open order in any LGIC project at the cut (censused from every non-terminal order's <paths>: LGIC_ENFORCE's only open order EN-c-28-r5 writes systems.json, resources.json and its own channel; LGIC_LGCTFM has none). LGIC_CANON's channel is append-only and shared, per CLAUDE.md 14b.
</preflight>

Seating: slot `~1`, level 0, the only cell of round 4. Round 4 of LGIC_CANON, issued by `2.0.0_SA_COO~G` on decomposition v6 s.0f, from PRD v1.7 @`1bd1963781` and rulings R-34 and R-43. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/` (`check_cn_r4.py` with 7 subcommands and a 20-arm self-test, `R4_BASE.json` pinning `43ed12c300`). Rulings carried: R-34, R-43, R-40, G-N's lift, DEC-6, DEC-9, DEC-13.
