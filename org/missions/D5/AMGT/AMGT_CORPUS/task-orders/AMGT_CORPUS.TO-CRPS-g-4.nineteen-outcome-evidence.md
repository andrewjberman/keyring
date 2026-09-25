# AMGT_CORPUS task order -- `CRPS-g-4` -- ROUND 5: one evidence row for EACH of the 19 endpoint outcomes -- the fence's own DONE-WHEN quoted verbatim, the instrument run at HEAD against served state, its output, and a state; no grade (grading is L9's and L10's)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-g-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~4</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates (G-3 CTO, G-7 POD4), 0 on these surfaces; no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell only READS S3 and writes two files in its own deliverables.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~4`**, slot `~4` of round 5. Serves **FWD-1..FWD-19**: the project's endpoint has 19
outcomes and only 2 have ever been graded.

## 1. THE CELL -- `CRPS-g-4`

**Where this came from.** The PRD `org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md` declares 19 outcomes, FWD-1..FWD-19
(its `endpoint_outcomes` header list; FWD-1..FWD-9 in the main ENDPOINT section, FWD-10..FWD-19 in ADDENDUM A). Each outcome has
a fence with a DONE-WHEN clause. Rounds so far graded only FWD-12 and FWD-19.

**RULED -- what you build:** two files in your deliverables, nothing else.
- `FWD_EVIDENCE_ROUND5.json`: `{"prd": "<path>@<commit>", "run_at": "<UTC>", "outcomes": [ ... 19 rows ... ]}`, each row:
  `{"id": "FWD-<n>", "fence_quote": "<the DONE-WHEN clause, VERBATIM from the PRD>", "instrument": "<the exact command or read you
  ran>", "output_excerpt": "<what it printed, the lines that answer the clause>", "state": "met" | "unmet" | "unmeasurable",
  "reason": "<required when unmeasurable: why no instrument can answer it now>", "notes": "<optional>"}`.
- `FWD_EVIDENCE_ROUND5.md`: the same 19 rows as a readable table.
- Measure against the SERVED and STORED state at HEAD, with read-only instruments only: S3 reads and listings, the project's own
  read-only CLI modes (`--census`, `--folder`, `--read-latest`, `--duplicates`, probes), the served reader in
  `lib/research/api/scoped_amgt.py` called as a library, git reads. When the fence names a population, print the denominator.
  `state` is YOUR measurement of the DONE-WHEN clause as written, not a grade of the outcome.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~4/FWD_EVIDENCE_ROUND5.json
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~4/FWD_EVIDENCE_ROUND5.md
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-g-4.nineteen-outcome-evidence.md
</paths>

READ-ONLY: the whole repository and every S3 object. Scratch `.scratch/g4/`.

## 4. BOUNDS
- NO write anywhere but your two files (and a channel row if you file one). NO vendor call, NO `--write`/`--coverage`/`pull`/
  `derive`/`fire`, NO S3 write. Pure ASCII.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W4-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-g-4"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round5/g4_AC1.sh</invocation><expect>(?m)^VALID$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-g-4"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round5/g4_AC2.sh</invocation><expect>fence_quotes_verbatim 19 of 19</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-g-4"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round5/g4_AC3.sh</invocation><expect>(?m)^paths_outside_grant 0$</expect></criterion>
</proof_of_spec>

- AC1 the evidence file's shape: 19 of 19 outcomes, every row complete, unmeasurable rows with a reason; AC2 every fence quote
  appears verbatim in the PRD; AC3 the bound: your branch changed nothing outside your grant.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~4/AMGT_CORPUS.TO-CRPS-g-4.nineteen-outcome-evidence.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: the count of met / unmet / unmeasurable.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-4 analysis s.7 and s.8 item 4, rule R-4 @`2f9b10b7d3`. The evidence is laid out for the CVO at L8/L9;
the grades are theirs. Checks dry-run at the base: AC1 FAIL (MISSING), AC2 FAIL (MISSING), AC3 bound PASS (no branch changes yet).

<risk>LOCAL</risk>
<status>pending</status>
<round>5</round>
<slot>~4</slot>
<fabric>site-z</fabric>
