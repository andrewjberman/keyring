# 1.0.0_SA_CTO -- canonical loop: the 10-to-2 re-entry built, and the fourth gate limb landed

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE, VALIDATE
**window:** 2026-09-01 19:52Z -> 20:35Z (since `self_drive_D2_tick127.md` @47a747cde4)
**seat:** `1.0.0_SA_CTO` (base, laptop fabric)

---

## What this window did

Closed the last structural break in the canonical fabric loop, in both directions, with
`3.0.0_SA_CVO` holding the other end.

### 1. Seam 10-to-2 was BROKEN and is now closed on both sides

Step 10 routes a `SCOPE_CHANGE` remediation row to `loop_target: 2`. Step 2 is
`/endpoint --forward`, which I built earlier today -- and it REFUSED without a fresh brief and
REFUSED to read the register. A correctly-routed finding therefore terminated in a skill that
refused its caller.

- `3.0.0_SA_CVO` sent the exact arriving shape at committed bytes (`remediation_row.schema.json`
  @6a1987cc73) BEFORE I designed anything against it. I asked for the shape rather than inventing
  a contract that seat would then have to satisfy.
- It named the real gap as MINE: a row could not cite WHICH outcome was contradicted, and adding
  `outcome_ref` required my numbering to be STABLE first. It was not.
- Landed the permanence contract, then that seat cut `outcome_ref` @c6c3627269 with 5 green
  controls and genuine scoping (a SPEC_ERROR row without the field still passes).
- My half: Step F0 @2eaaee3654, carrying that shape verbatim.

**The payload is `spec_asserts` + `world_is`** -- what the task order said, and what the world
turned out to be. Everything else on the row is addressing.

**Three design calls inside F0:**
- Re-entry reads the NAMED outcome only. A scope change contests ONE outcome; re-running Phase 0
  over the whole endpoint silently re-litigates outcomes nobody questioned.
- `ACCEPT` is re-tested, never inherited. If the world contradicted the outcome, the acceptance
  line that let it read as met is the thing that failed.
- **The guard: re-entry must NEVER silently shrink the endpoint.** Retiring the contested outcome
  is always the cheapest way to make a scope change go away, and the seat doing the retiring is
  the seat the finding was against. A retirement must state what capability the project no longer
  promises -- if that sentence is uncomfortable to write, the outcome was not obsolete.

### 2. Two self-caught defects in my own build

- **F1 still refused unconditionally** (`NO BRIEF, NO PHASE 0`), contradicting F0 inside the same
  file. A reader hitting F1 first would have refused the caller anyway -- the exact bug I had just
  fixed. Scoped to the greenfield path.
- **F0 was labelled as running first and positioned LAST**, after F1-F4. I had added a
  cross-reference in F1; moved the block instead @659cebf864. ORDERING catches every reader, a
  cross-reference catches a careful one.

### 3. Gate limb 4 -- routed, not built by me

Andrew authorized it earlier ("yes endpoint section is mandatory"); I held the build pending the
design workshop, and the workshop settled the shape. `git log` says `.tools/to-pipeline-gate.py` is
`3.0.0_SA_CVO`'s build, and that seat had just cut `outcome_ref` on MY word -- so the symmetric act
was to relay rather than edit another seat's file. That seat cut LIMB 4 @0df5edf606.

**Found while writing the routing, and it raised the urgency:** the gate now refuses a
`SCOPE_CHANGE` row without a usable `outcome_ref`, and that field must match `FWD-n`. A PRD with no
ENDPOINT section has NO FWD ids at all -- so a genuine scope change becomes UNFILEABLE. Worse than
the silent collapse the limb was meant to prevent, and a consequence of the two things landed
tonight interacting.

**Stated in the routing so it is never overclaimed:** the limb checks the section EXISTS and is
NON-EMPTY. It cannot check the outcomes are good, that an arc is present, that acceptance lines are
plain English, or that Andrew ever ratified the endpoint. It closes a ROUTING hole, not a QUALITY
one.

### 4. Gap forecast delivered to Andrew, with three measurements

He asked for next steps plus a per-step slip forecast. Turned three assertions into measurements:

```
  step 7 worker trigger in a TO template?   14 hits, ALL logs/inbox. ZERO templates, ZERO TOs.
  step 8 monitor running?                   2 processes -- RUNNING
  step 6 fabric refusal teaches?            YES -- names the enum and the step-3 call
```

**The finding: the step-7 trigger has NO CARRIER.** The spec says give it to workers verbatim in
every TO; nothing puts it there. Its failure mode is the worst available -- a worker who never got
the line does not report, and nothing records that a surprise went unreported. Steps 8/9/10 then
read a channel that silently under-fills, and a QUIET channel reads as a CALM project.

**Recommended to Andrew, in order:** build limb 4 (now done); give the trigger a carrier via the
step-6 gate rather than a template (proposal, COO's gate); and RUN THE LOOP ONCE END TO END on
`ADVI_PERFRP`, because everything except steps 3 and 6 has never executed and my whole forecast is
theoretical. Cautioned against building further against forecast gaps -- that is how the
deploy-ledger parser earned four spelling patches.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-find` | `"Did I have to do..." --corpus all --files` | PASS | 14 hits / 142,743 scanned; ZERO templates -- the step-7 carrier gap |
| `comp-read` | `.claude/skills/prd-check/SKILL.md` | PASS | established prd-check is a COVERAGE view, not a quality check |
| `git log` | `-1 --format=%an -- to-pipeline-gate.py` | PASS | ownership measured, not assumed, before routing rather than editing |
| `grep -c` | `"ENDPOINT" to-pipeline-gate.py` | **FAIL as used** | returned 21; a WORD COUNT compatible with the limb landed AND never built |
| `grep -nE` | implementation + call site | PASS | the re-derivation that actually settled it |
| `safe-commit` | 2 commits, pathspec-scoped | PASS | post-commit STATE verified both times, not read from the message |

**What worked:** asking `3.0.0_SA_CVO` for the arriving SHAPE before designing against it. It
returned committed bytes and named a precondition at my end I had not seen.

**What failed:** `grep -ci "ENDPOINT"` as a landed-or-not oracle. 21 hits is equally consistent with
built and not-built. Same class as this morning's `--red` ledger read and the `9 of 11` limb -- a
number correct in its source, used against a question its source cannot answer.

**Gap found:** the step-7 worker trigger has no mechanical carrier. Proposed to route it through the
step-6 gate (COO's), NOT a template -- a template is one more thing to remember, and the gate
already refuses non-conformant TOs on three other limbs.

## Blockers

None. Nothing at this seat is blocked.

## Current State

**The canonical fabric loop is built end to end and has never run once.**

```
  step 1  4.0.0_SA_CRO   /brief-create  @098a5aa28d   BUILT, NEVER RUN
                         CRO's PERFRP brief EXISTS: docs/briefs/advi-perfrp-merge-forward-brief-20260901.md
  step 2  1.0.0_SA_CTO   /endpoint --forward Phase 0   BUILT, NEVER RUN
                         F0 re-entry @2eaaee3654, reordered @659cebf864
  step 3  1.0.0_SA_CTO   fabric key                    ENFORCING; D2 10/10 @a2ff0db2e7; 339 estate-wide absent
  step 4  1.0.0_SA_CTO   docs/architecture/_PRD_TEMPLATE.md   BUILT, NEVER USED
  step 5  2.0.0_SA_COO   decomp + preflight            ENFORCING
  step 6  2.0.0_SA_COO   .tools/to-pipeline-gate.py    ENFORCING, FOUR LIMBS as of @0df5edf606
  step 7  worker         surprise rows                 NO CARRIER FOR THE TRIGGER (the gap above)
  step 8  3.0.0_SA_CVO   surprise-watch.sh             BUILT AND RUNNING; notifier only
  step 9/10 3.0.0_SA_CVO disposition + route           row validators are the NEXT BUILD
```

Memorialised at `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` -- Andrew's word: reference only,
"not needed operationally, but we have one because its good to memorialize."

`/self-drive D2` ARMED, tick 129, completion 2 of 10 READ from the register, ledger 40 rows.
Register `open_tos` 17 remains UNVERIFIED (a mechanical open-count is measured unsound on this
corpus: 30 of 62 status blocks carry BOTH open and closed words).

**PUSH STATE:** all window commits LOCAL. `origin/CLOUD` last read `6f9bf277f1` via a peer's
`ls-remote` -- NOT my own read, and perishable. Push is integrator-only; rides `0.0.0_AB_MSTR`'s
window.

## Next Steps

1. **[1.0.0_SA_CTO]** Run the loop once end to end on `ADVI_PERFRP` -- the brief exists. Highest
   value available; every forecast gap above is theoretical until one real execution.
2. **[2.0.0_SA_COO]** Consider the step-7 trigger limb on the step-6 gate. Proposal only; that gate
   is COO's and Andrew has not ruled on this one.
3. **[3.0.0_SA_CVO]** Seam 4-to-5 check: does a step-5 decomp need anything `_PRD_TEMPLATE.md` does
   not require an author to write? That seat is running it on its own clock; nothing blocked.
4. **[Andrew]** One card open: whether the flow-ingestion defect widens the ruled 22.

## Note against my own recent practice

This log is PLAIN ASCII per `CLAUDE.md` ("No non-ASCII in production code/logs/AWS") and the `/log`
standard. **My `/self-drive` tick logs today used non-ASCII markers throughout, against that rule.**
Recording it rather than silently switching; the tick logs are committed and I am not rewriting
history over it, but the practice was wrong and this is the correction.
