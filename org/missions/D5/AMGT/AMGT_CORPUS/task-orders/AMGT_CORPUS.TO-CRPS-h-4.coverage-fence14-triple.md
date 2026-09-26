# AMGT_CORPUS task order -- `CRPS-h-4` -- ROUND 6: the coverage census prints FWD-14's three counts in FWD-14's own names, with any folder outside them counted as a disclosed remainder

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-h-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~4</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 1 drift candidate, on data/black_diamond; 0 on these surfaces; no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- the dry run writes nothing; the census write is the issuer's drain act.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~4`**, slot `~4` of round 6. Serves **FWD-14**: "the three counts (resolved / ambiguous /
empty-or-workbook-only) SUM TO THE FOLDER COUNT every time".

## 1. THE CELL -- `CRPS-h-4`

**Where this came from.** `lib/research/corpus/backlog.py`'s coverage census (`--coverage`, and its read-only twin
`--coverage-dry-run`) prints its own classes and the FWD-19 fence line (`fence dossier-served <a> resolved-but-no-prose <b>
unresolved-with-reason <c> sum <s> folders_read <n>`). It already MEASURES, per folder, the identity state (`RESOLVED`,
`UNRESOLVED`, `AMBIGUOUS`; `STATE_*` constants) and `never_prose_reason` (`'empty'` / `'workbook-only'` / None;
`NEVER_PROSE_REASONS`, `backlog.py:142`). No line uses FWD-14's three names, and those names overlap on the census's own axes
(a workbook-only folder is also identity-resolved), so they sum to the folder count only under a stated precedence.

**RULED -- what you build:**
- Every coverage totals print (`--coverage` and `--coverage-dry-run`) gains ONE line, after the existing `fence` line:
  `fence14 resolved <a> ambiguous <b> empty-or-workbook-only <c> sum <a+b+c> outside-fence <d> folders_read <n>`,
  classifying each folder ONCE by this precedence: `never_prose_reason in NEVER_PROSE_REASONS` -> empty-or-workbook-only; else
  identity AMBIGUOUS -> ambiguous; else identity RESOLVED -> resolved; else -> outside-fence. So `a+b+c+d == n` always, and the
  fence holds exactly when `d == 0`. Every outside-fence folder prints one line `fence14_outside <folder> <state> <reason>`.
- The existing lines stay as they are.
- `lib/research/corpus/tests/test_backlog_fence14.py` (new): the precedence (a workbook-only resolved folder counts once, as
  empty-or-workbook-only), the sum, an unresolved non-ambiguous folder landing in `outside-fence` with its line, and that the
  dry run writes nothing.

## 3. SURFACES

<paths>
lib/research/corpus/backlog.py
lib/research/corpus/tests/test_backlog_fence14.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-h-4.coverage-fence14-triple.md
</paths>

READ-ONLY: every other `lib/research/corpus/` module. Scratch `.scratch/h4/`.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible. NO S3 write (never run `--coverage` or `--write` for real), NO change to any
  disposition or existing total.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W4-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-h-4"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round6/h4_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-h-4"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round6/h4_AC2.sh</invocation><expect>fence14 resolved \d+ ambiguous \d+ empty-or-workbook-only \d+ sum (\d+) outside-fence 0 folders_read \1\b</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-h-4"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round6/h4_AC3.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe: the live dry run prints the fence14 line summing to the live folder count with
  nothing outside; AC3 the bound: the corpus suite still passes.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~4/AMGT_CORPUS.TO-CRPS-h-4.coverage-fence14-triple.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: AC2's fence14 line.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-5 analysis s.5 item 5 @`37217d8053` ("g-3 closed this class for FWD-19's triple, not this one"). The
precedence is the issuer's ruling (decomposition s.2 and s.8). Expected live: resolved 83, ambiguous 0,
empty-or-workbook-only 12, outside-fence 0, sum 95 (from the FWD-19 line's 83 / 12 / 0). Checks dry-run at the base: AC1 FAIL
(no such file), AC2 FAIL (no fence14 line), AC3 bound.

<risk>LOCAL</risk>
<status>pending</status>
<round>6</round>
<slot>~4</slot>
<fabric>site-z</fabric>

**WORKER CLOSE (`0.9.0_WK_AMGT_CORPUS~4`):** AC1 PASS (6 passed in test_backlog_fence14.py); AC2 PASS (live --coverage-dry-run: `fence14 resolved 83 ambiguous 0 empty-or-workbook-only 12 sum 95 outside-fence 0 folders_read 95`); AC3 PASS (314 passed in lib/research/corpus/tests).

<status>complete</status>
