# CVO 2026-09-01 ~18:12Z - 21:15Z -- nine commits, two new gates, and a vocabulary error in my own gate that concealed the violations matching it

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE

Delta since `work_1812Z_the_admissibility_gate_was_run...` @`0316d5bd19`. **Nine commits, all
LOCAL.** Andrew answered two `/open-calls` slates and authorized a fourth gate limb in the window.

---

## 1. THE ONE TO READ IF YOU READ NOTHING ELSE

**My own gate carried an UNRATIFIED `dep_stage` value, and the wrong vocabulary hid the violations
that matched it.** The ratified enum is SIX (`DEP_STAGE_ENUM_RULE24_RECORD_20260821.md:41-46`);
mine accepted SEVEN, carrying `TOS_CUT`, which I took from the ten-step map's step 6 instead of from
the enum's authority. Rule 24 binds any schema an agent **authors OR ADOPTS** -- a bad adoption, by
the seat that mandated the rule, inside the gate that enforces it.

>> **`--sweep` reported `BRIEF x2` as off-enum and said NOTHING about `TOS_CUT x2`, which is equally
off-enum, BECAUSE THE TUPLE HAD BEEN WIDENED TO ADMIT IT. A GATE WHOSE VOCABULARY IS WRONG CANNOT
SEE THE VIOLATIONS THAT MATCH ITS OWN ERROR, AND REPORTS CLEAN ON EXACTLY THOSE.** <<

```
  before   off-enum surfaced: BRIEF x2                 (2 of 33 populated)
  after    off-enum surfaced: BRIEF x2 + TOS_CUT x2    (4 of 33 populated)
```
**A one-line correction DOUBLED the count, on a population I had swept and reported CLEAN on that
axis twice the same day.** Blast radius disclosed rather than patched: the bad value printed in
every refusal this gate issued and rode TWO fabric broadcasts to nine seats.
⭐ **Found only because `1.0.0_SA_CTO` declined to assume which of two framings superseded** (five
stages vs ten steps) and said so. **Reconciling a divergence someone refused to paper over is what
exposed it.** Neither framing supersedes -- they are different grains and they nest.

## 2. TWO GATES BUILT, BOTH ON EXPLICIT ANDREW WORD

| commit | what |
|---|---|
| `6a1987cc73` | **step-7/10 ROW VALIDATORS** -- schemas first, then `.tools/surprise-row-gate.py` |
| `c6c3627269` | **`outcome_ref`** -- the 10-to-2 seam now names WHICH outcome was contradicted |
| `0df5edf606` | **LIMB 4** -- the ENDPOINT section is mandatory (Andrew via 92478) |

**THE CENSUS CHANGED THE BUILD ORDER and that was the whole game.** Both schemas are
`additionalProperties: false` and NEITHER carried the mandated fields. **Gate-first would have
DEADLOCKED the channel** -- every gate-compliant row failing schema validation, every schema-valid
row failing the gate.

**PROSPECTIVE BY CONSTRUCTION:** the row gate diffs row IDS between HEAD and the staged blob and
grades only ids NEW in this commit, so ~190 legacy rows across 18 files are never re-graded.
Exercised end-to-end through `safe-commit` against the REAL 408 KB file: BLOCKED, unstaged,
**"1 new row(s) of 19 total checked (18 pre-existing, NOT re-graded)"**.

⛔ **AND THE TWO GATES ALMOST COMPOSED INTO A DEAD END.** `surprise-row-gate` refuses
`route=SCOPE_CHANGE` without an `outcome_ref` matching `FWD-n`; FWD ids exist ONLY in an ENDPOINT
section. **A PRD without one makes a genuine scope change UNFILEABLE** -- the row cannot be written
and the finding has nowhere to go. Limb 4 is what stops it. **Neither author would have seen that
alone; it surfaced in the CTO sync Andrew instructed.**

## 3. WHERE I REFUSED TO WIDEN AN AUTHORIZATION

Andrew: *"yes endpoint section is mandatory and it is written by running endpoint --forward skill
process."* **That is a word about the SECTION.** It is not a word about a project that names no PRD
at all (**21 of 349**), so that case WARNs loudly and PASSES. `dep_stage=REGISTERED` is exempt too --
the ratifying record defines that stage as *"no purpose-level PRD yet"*, and demanding an endpoint
there would refuse a project for being at the stage the enum calls pre-PRD.
**Converting an authorization into a refusal he did not give is the inferred-gate prohibition.**

## 4. A CARD CLOSED SILENTLY AND IT WAS MY FAULT

`1.0.0_SA_CTO` (92434) established that finding `4022ebae4a` had **TWO limbs**; **my `/open-calls`
card carried ONE, and so did my handoff before it.** Andrew answered exactly the question I put in
front of him and it was the wrong half. That seat generously called it a label collision (the
ruling's "(b)-unnarrowed" = BRANCH (b); the card's limb (b) = per-family-vs-per-set). **The
collision is real and it is not the root: the limb was gone before Andrew ever saw the card.**
⭐ **I adopted its wider generalisation over my own:** I had written *"the card with the least
content is most likely to be silently treated as decided."* Theirs: **a card closes silently
whenever the ruling's text CAN BE READ as covering it, whatever makes that reading available.**
Least content is one mechanism; ambiguous labelling a second; **a lossy transcription onto another
seat's slate a third, and that one is mine.**

## 5. A MEASUREMENT THAT REVERSED MY OWN RECOMMENDATION

Censused the container swap I had recommended (`0c7853c17f`). **`DEF=1`** -- across 841 hits in
103,138 files, exactly ONE piece of code defines a path into the channel. **Machine benefit of the
swap: ZERO**, because that one reader already parses the rows as JSON. And the argument I did not
have when I recommended it: `comp-surprise.py:40` is `re.finditer`, so it reads EVERY fenced block --
**a pure-JSON file holds exactly one array**, and the loss would be invisible today and discovered
by whoever first needed to append rather than rewrite 408 KB. **Declined the swap; mandated schema
validity instead.** Then USED the multi-block capability to file S18, exercising the claim rather
than asserting it.

## 6. Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| `comp-find` | 6 | PARTIAL | 2 returned `0 across 0` -- OUT-OF-CORPUS, **not reported as absence** |
| `comp-surprise` | 3 | PASS | `defects=0 malformed=0`; parsed BOTH fenced blocks |
| `comp-read --enumerate` | 1 | PASS | exercised as the PRECONDITION for the law edit, not after |
| gate control harness | 12+8+24+12+6 | PASS | 62 controls; **2 caught real bugs** |
| `bash -n` / `ast.parse` | 9 | PASS | every edit |
| `safe-commit` end-to-end | 1 | PASS | deliberate refusal against the real file, then restored |
| `surprise-watch.sh` | 4 | PASS | armed as Monitor `bcrmh5rfd`; **fired on its own first append** |

**What worked:** censusing before building, three times. It set the schema-before-gate order, caught
the `prds` shape trap (**LIST in 327 / ABSENT in 21 / bare STRING in 1** -- a naive resolver would
have thrown INSIDE a gate), and reversed the container recommendation.
**What failed, both mine, both caught by controls not by reading:**
- **`grep -c` PRINTS "0" AND RETURNS rc=1** on zero matches, so `grep -c ... || echo 0` emits BOTH;
  the count became `"0\n0"` and every downstream `$(( ))` threw. Broke the zero-row case.
- **`$COMMIT_MSG_BODY` DOES NOT EXIST** anywhere in `safe-commit.sh`. Under `set -euo pipefail` that
  ABORTS -- and only on the refusal path, i.e. exactly when the gate matters. **A new reference to
  an existing-LOOKING variable is a claim and needs checking like any other.**
**Gap found:** `comp-similar` emits no vintage/denominator while its sibling prints a full header
over the same kuzu corpus -> `0.8.0_AE_CloudComp`.

## 7. Blockers

**No CVO-owned blocker.** All nine commits LOCAL; push is integrator-only (LD-0367).
- `comp-similar` provenance header -> `0.8.0_AE_CloudComp`.
- Seam 4-to-5 (does a decomp need what a conformant PRD is not required to write?) -> mine, agreed
  with `1.0.0_SA_CTO` as NOT tonight.
- **AT ANDREW: nothing.** Both slates answered; `4022ebae4a` closed on both limbs.

## 8. Current State -- for a reader with ZERO context

- **PUSH STATE, MEASURED** (`ls-remote`; negative control `feedfacedead` refused correctly):
  `origin/CLOUD = 6f9bf277f1`, local HEAD `0df5edf606`, **50 ahead. ALL LOCAL.**
- **`.tools/to-pipeline-gate.py` now refuses FOUR things** on a newly-added
  `org/**/task_orders/*.md`: a registered project JSON; a `dep_stage` in the **six**-value ratified
  enum; a `fabric` in `laptop|site-z`; a `<preflight>` whose every RUN carries a denominator or a
  BLIND word on its own line; and limb 4, a non-empty `## ENDPOINT (step 2, /endpoint --forward)`
  section in a named PRD. Override `# pipeline-override: <reason>`, audited.
- **`.tools/surprise-row-gate.py`** refuses a NEW investigation row without `spec_asserts` +
  `world_is`, and a NEW remediation row without `route` + `loop_target` satisfying
  `SPEC_ERROR->6 | DECOMP_INVALIDATING->5 | SCOPE_CHANGE->2`, plus `outcome_ref` (`^FWD-[0-9]+$`) on
  SCOPE_CHANGE only. Wired in `safe-commit.sh` (keyed on **PATHSPEC**, not IN_SCOPE -- channel files
  are `.md`) AND `.git/hooks/pre-commit` via `install-surprise-row-gate.sh`.
- **`--sweep` reads:** `dep_stage` 316/349 ABSENT, `BRIEF x2` + `TOS_CUT x2` off-enum (owner
  unclaimed); `fabric` **349/349 ABSENT** -- every project acquires it at its next TO by Andrew's
  ruling "every project at next TO".
- **The step-8 notifier is ARMED**, Monitor `bcrmh5rfd`, baseline 18 files / 190 rows / 17 projects.
- **`ADVI_PERFRP-S18` filed** @`3eb00f5905`: both step-5 lenses are blind or absent on
  `perfrp_emit_core.py`. ARMED, disarm owner `2.0.0_SA_COO`.
- **CLAUDE.md Rule 21 limb (i) is DISCHARGED** -- `comp-read --enumerate` certified.

## 9. Next Steps

1. **[3.0.0_SA_CVO]** The vocabulary sweep I owe: every copied enum in my files must cite its
   ratifying authority BESIDE the value. Done for `DEP_STAGE_ENUM`; **not done elsewhere, and I
   recorded the debt rather than claiming the discipline.**
2. **[3.0.0_SA_CVO]** Seam 4-to-5: read `docs/architecture/_PRD_TEMPLATE.md` against my step-5
   requirements, emit a DELTA or a clean bill **with the denominator**.
3. **[3.0.0_SA_CVO]** Continue the ADVI_PERFRP backfill. `0.7.0_AE_CloudOps~M`'s three measurements
   still need that seat's own evidence lines before they can be filed as GROUNDED.
4. **[0.8.0_AE_CloudComp]** `comp-similar` provenance header; `comp-pipescript` E-arms still RED.
