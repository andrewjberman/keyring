# AMGT_CORPUS task order -- `CRPS-g-3` -- ROUND 5: the coverage census prints ONE line in the fence's own three names, with its own classes mapped onto them, and a read-only dry run computes it without writing

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-g-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~3</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates (G-3 CTO, G-7 POD4), 0 on these surfaces; no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- the dry run writes nothing; the census write is the issuer's drain act.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~3`**, slot `~3` of round 5. Serves **FWD-19** (its census).

## 1. THE CELL -- `CRPS-g-3`

**Where this came from.** FWD-19's fence declares three named classes: *dossier-served / resolved-but-no-prose /
unresolved-with-reason*, summing to the folder count. `lib/research/corpus/backlog.py`'s coverage census prints FOUR:
`dossier_served 82 served_as_empty_shell 12 resolved_no_prose 0 unresolved_with_reason 0`. The 12 under `served_as_empty_shell`
ARE the fence's resolved-but-no-prose class, while the fence-named field reads 0, so a reader looking for the fence's value
finds zero.

**RULED -- what you build:**
- Every coverage totals print gains ONE line, in the fence's names:
  `fence dossier-served <a> resolved-but-no-prose <b> unresolved-with-reason <c> sum <a+b+c> folders_read <n>` where
  `b = served_as_empty_shell + resolved_no_prose`. The four existing totals stay as they are.
- `python -m lib.research.corpus.backlog --coverage-dry-run`: computes the coverage census exactly as `--coverage` does and
  prints the same lines, but writes NOTHING.
- `tests/test_backlog_fence_names.py`: the fence line's mapping, its sum equal to the folder count, and the dry run's no-write.

## 3. SURFACES

<paths>
lib/research/corpus/backlog.py
lib/research/corpus/tests/test_backlog_fence_names.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-g-3.census-fence-names.md
</paths>

READ-ONLY: every other `lib/research/corpus/` module. Scratch `.scratch/g3/`.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible. NO S3 write (never run `--coverage` or `--write` for real), NO change to any
  disposition or total.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W3-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-g-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round5/g3_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-g-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round5/g3_AC2.sh</invocation><expect>fence dossier-served \d+ resolved-but-no-prose \d+ unresolved-with-reason \d+ sum (\d+) folders_read \1\b</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-g-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round5/g3_AC3.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe: the live dry run prints the fence line summing to the live folder count; AC3 the
  bound: the corpus suite still passes.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~3/AMGT_CORPUS.TO-CRPS-g-3.census-fence-names.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: AC2's fence line.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-4 analysis s.4 rule R-2 and s.8 item 3 @`2f9b10b7d3`. Checks dry-run at the base: AC1 FAIL (no such
file), AC2 FAIL (no dry-run flag), AC3 bound.

<risk>LOCAL</risk>
<status>pending</status>
<round>5</round>
<slot>~3</slot>
<fabric>site-z</fabric>

**WORKER CLOSE (`0.9.0_WK_AMGT_CORPUS~3`):** AC1/AC2/AC3 all PASS (proof-of-spec-check rc=0, VALID). No surprise
rows filed -- every criterion was satisfiable as written.

<status>complete</status>
