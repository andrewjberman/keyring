# AMGT_CORPUS task order -- `CRPS-o-1` -- ROUND 13: one evidence row per outcome, FWD-1..FWD-19, measured on an exercise at HEAD, and for every outcome not met the act that would exercise it and its owner

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-o-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only evidence pass.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 13. Serves **FWD-1..FWD-19**: the evidence the next analysis grades.

## 1. THE CELL -- `CRPS-o-1`

**Where this came from.** The PRD `org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md` declares 19 outcomes, FWD-1..FWD-19
(its `endpoint_outcomes` header list; FWD-1..FWD-9 in the main ENDPOINT section, FWD-10..FWD-19 in ADDENDUM A). Each has a fence
with a DONE-WHEN clause, and several carry dated ADDENDA and CORRECTIONS beneath them that bind how the fence is read (read every
addendum under an outcome before measuring it). The last pass is round 7's,
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~5/FWD_EVIDENCE_ROUND7.json`. Since then, code and stored state
have moved: the scenario cases, units, currency, the positional read, and the dossier store's prefix. The store's prefix is now
`amgt/harvest/gold/research_dossier/` (95 objects); `lib/research/corpus/dossier.py` `read_dossier` reads it. Use round 7's
instruments as a STARTING LIST ONLY; carry no grade from it; re-run every instrument at HEAD.

**RULED -- what you build:** two files in your deliverables, nothing else.
- `FWD_EVIDENCE_ROUND13.json`: `{"prd": "<path>@<commit>", "run_at": "<UTC>", "outcomes": [ ... 19 rows ... ]}`, each row:
  `{"id": "FWD-<n>", "fence_quote": "<the DONE-WHEN clause, VERBATIM from the PRD>", "instrument": "<the exact command or read you
  ran>", "output_excerpt": "<what it printed, the lines that answer the clause>", "denominator": "<the population the clause names
  and its size as printed; or 'none: the clause names no population'>", "state": "met" | "unmet" | "unmeasurable", "reason":
  "<required when unmeasurable: why no instrument can answer it now>", "exercising_act": "<required when not met>", "owner":
  "<required when not met>", "notes": "<optional; name any addendum you applied>"}`.
- **For every row not met:** `exercising_act` names the ACT that would exercise the clause, driven on demand by a seat, never an
  organic event waited for (if the clause needs a new report to land, the act is the one that drives a report in, and the rebuild).
  `owner` is exactly one of `AMGT_CORPUS` (this project's data or code), `AMGT_RESAPP` (the served API, including its deployed
  Lambda, which reads the legacy prefix until its own redeploy), or `DSGN_AMGTV1` (the portal page render).
- `FWD_EVIDENCE_ROUND13.md`: the same 19 rows as a readable table.
- Measure with read-only instruments only: S3 reads and listings, the project's read-only CLI modes (`--census`,
  `--coverage-dry-run`, `--folder`, `--read-latest`, `--duplicates`, `--code-census`, `--show-terms`, `--case-census`,
  `--pick-census`, probes, `cases-report`), the served reader `lib/research/api/scoped_amgt.py` called as a library, git reads.
  When the fence names a population, print the denominator. `state` is YOUR measurement of the clause as written, not a grade.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/FWD_EVIDENCE_ROUND13.json
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/FWD_EVIDENCE_ROUND13.md
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-o-1.nineteen-outcome-evidence-round13.md
</paths>

READ-ONLY: the whole repository and every S3 object. Scratch `.scratch/o1/`.

## 4. BOUNDS
- NO write anywhere but your two files (and a channel row if you file one). NO vendor call, NO `--write` / `--coverage` / `pull` /
  `derive` / `fire`, NO S3 write. Pure ASCII.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W1-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-o-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round13/o1_AC1.sh</invocation><expect>(?m)^VALID$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-o-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round13/o1_AC2.sh</invocation><expect>fence_quotes_verbatim 19 of 19</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-o-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round13/o1_AC3.sh</invocation><expect>(?m)^paths_outside_grant 0$</expect></criterion>
</proof_of_spec>

- AC1 the evidence file's shape: 19 of 19 outcomes, every row complete with a denominator, unmeasurable rows with a reason, every
  row not met with an act (never a wait) and an owner; AC2 every fence quote appears verbatim in the PRD; AC3 the bound: your branch
  changed nothing outside your grant.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-o-1.nineteen-outcome-evidence-round13.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: the count of met / unmet / unmeasurable, by id, and each not-met row's owner.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-12 analysis s.4 @`1b4a75ba26` (msg 26583). Checks dry-run at the base: AC1/AC2 FAIL (MISSING file), AC3
PASS (paths_outside_grant 0). Checker controls: the round-7 file INVALID (rows_valid 0), a completed copy VALID, one "wait" act
INVALID (acted 6 of 7).

<risk>LOCAL</risk>
<status>complete</status>
<round>13</round>
<slot>~1</slot>
<fabric>site-z</fabric>
