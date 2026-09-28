# AMGT_CORPUS task order -- `CRPS-i-5` -- ROUND 7: one evidence row per outcome, FWD-1..FWD-19, measured on the served state after round 7's drains, so the next analysis can restate the REALIZED count

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-i-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~5</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only evidence pass.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~5`**, slot `~5` of round 7. Serves **FWD-1..FWD-19**: the evidence the next analysis grades.

## 1. THE CELL -- `CRPS-i-5`

**Where this came from.** The PRD `org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md` declares 19 outcomes, FWD-1..FWD-19
(its `endpoint_outcomes` header list; FWD-1..FWD-9 in the main ENDPOINT section, FWD-10..FWD-19 in ADDENDUM A). Each has a
fence with a DONE-WHEN clause, and several carry dated ADDENDA and CORRECTIONS beneath them that bind how the fence is read
(read every addendum under an outcome before measuring it). A round-5 pass produced one evidence row per outcome; since then
code and served state have moved. Your worktree was cut AFTER this round's served fixes landed, so the source you read and the
served state you measure are the same vintage.

**RULED -- what you build:** two files in your deliverables, nothing else.
- `FWD_EVIDENCE_ROUND7.json`: `{"prd": "<path>@<commit>", "run_at": "<UTC>", "outcomes": [ ... 19 rows ... ]}`, each row:
  `{"id": "FWD-<n>", "fence_quote": "<the DONE-WHEN clause, VERBATIM from the PRD>", "instrument": "<the exact command or read
  you ran>", "output_excerpt": "<what it printed, the lines that answer the clause>", "state": "met" | "unmet" |
  "unmeasurable", "reason": "<required when unmeasurable: why no instrument can answer it now>", "notes": "<optional; name
  any addendum you applied>"}`.
- `FWD_EVIDENCE_ROUND7.md`: the same 19 rows as a readable table.
- Measure against the SERVED and STORED state with read-only instruments only: S3 reads and listings, the project's own
  read-only CLI modes (`--census`, `--coverage-dry-run`, `--folder`, `--read-latest`, `--duplicates`, `--code-census`,
  `--show-terms`, probes, `cases-report`), the served reader in `lib/research/api/scoped_amgt.py` called as a library, git reads.
  When the fence names a population, print the denominator. A fence whose clause sits on a page render (a DOM, a tab, a
  typography rule) and cannot be answered from this project's data is `unmeasurable` with that reason. `state` is YOUR
  measurement of the clause as written, not a grade of the outcome.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~5/FWD_EVIDENCE_ROUND7.json
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~5/FWD_EVIDENCE_ROUND7.md
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-i-5.nineteen-outcome-evidence-round7.md
</paths>

READ-ONLY: the whole repository and every S3 object. Scratch `.scratch/i5/`.

## 4. BOUNDS
- NO write anywhere but your two files (and a channel row if you file one). NO vendor call, NO `--write` / `--coverage` /
  `pull` / `derive` / `fire`, NO S3 write. Pure ASCII.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W5-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-i-5"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round7/i5_AC1.sh</invocation><expect>(?m)^VALID$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-i-5"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round7/i5_AC2.sh</invocation><expect>fence_quotes_verbatim 19 of 19</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-i-5"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round7/i5_AC3.sh</invocation><expect>(?m)^paths_outside_grant 0$</expect></criterion>
</proof_of_spec>

- AC1 the evidence file's shape: 19 of 19 outcomes, every row complete, unmeasurable rows with a reason; AC2 every fence quote
  appears verbatim in the PRD; AC3 the bound: your branch changed nothing outside your grant.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~5/AMGT_CORPUS.TO-CRPS-i-5.nineteen-outcome-evidence-round7.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: the count of met / unmet / unmeasurable, by id.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-6 analysis s.5 and s.6 item 6 @`1e53f322f3` ("the next 19-outcome pass produces the number"). Issued
with the round, SPAWNED only after the i-1 and i-2 drains land (decomposition v7.0 s.4), its worktree cut from CLOUD at that
moment -- the round-5 g-4 pass read a worktree older than its fixes (the CTO's vintage-hole finding). Checks dry-run at the
base: AC1/AC2 FAIL (MISSING file), AC3 bound.

<risk>LOCAL</risk>
<status>complete</status>
<round>7</round>
<slot>~5</slot>
<fabric>site-z</fabric>
