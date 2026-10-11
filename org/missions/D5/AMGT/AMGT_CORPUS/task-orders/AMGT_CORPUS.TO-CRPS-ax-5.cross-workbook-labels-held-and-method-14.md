# AMGT_CORPUS task order -- `CRPS-ax-5` -- ROUND 48: a FactSet code's single label across the team's workbooks is served, claim held; the own sheet's measured label wins (FWD-20, lib half; method /14)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ax-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no policy, role or credential changes; tests use an in-memory workbook and a fake client only.
comp-adversary: RUN by the issuer at the cut -- ax5_check.py: `ax5 build 2/3 control 2/2` at the base (only the precedence arm fails), `build 3/3 control 2/2` after the change. Blind spot: the check is a miniature workbook; the 95 stored dossiers are the issuer's /14 write leg.
EGRESS CLASS, declared: NONE. No S3 write, no Bloomberg or vendor call.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, a continued slot `~1` of round 48. Your worktree is the absolute path the issuer gives you; work and commit only there.
Your worktree is cut from the branch after round 47 drained (`lib/research/corpus/team_sheet.py` carries the labels, `template.py` exists, METHOD is `/13`).

## 1. THE CELL -- `CRPS-ax-5`

Outcome FWD-20. The CTO ruled (round-47 analysis ADDENDUM 1, msg 4113): "apply a code's single label across workbooks at any count, claim held, cite source and
'N agree, 0 disagree'; own-sheet measured wins; print the three shares". The issuer's read of the 80 stored workbooks (`checks/round48/ax3_label_read.py`, 372 sheets
walked, 0 raised, a positive control that reads COPA's FF_SALES "Revenue") found nine FactSet codes with exactly ONE label across every workbook that assigns one. They go
into `lib/research/corpus/factset_descriptions.json`, which `team_sheet` already reads (`_factset_entries`, `_row_label`). Today the entries file sits ABOVE the own sheet's
measured label; the ruling reverses that.

**Build:**

1. `lib/research/corpus/factset_descriptions.json`: replace its content with EXACTLY the JSON below (ASCII, the one key `entries`):

```json
{
  "entries": {
    "FF_BPS": {
      "cite": "AMGT_CORPUS round 48 ax-3 read of 80 stored workbooks (the research-report library and the master template), 2026-10-11: 23 workbooks agree, 0 disagree",
      "text": "BVPS"
    },
    "FF_CAPEX": {
      "cite": "AMGT_CORPUS round 48 ax-3 read of 80 stored workbooks (the research-report library and the master template), 2026-10-11: 19 workbooks agree, 0 disagree",
      "text": "Cap Ex"
    },
    "FF_COM_SHS_OUT": {
      "cite": "AMGT_CORPUS round 48 ax-3 read of 80 stored workbooks (the research-report library and the master template), 2026-10-11: 1 workbook agrees, 0 disagree",
      "text": "Diluted shares outstanding"
    },
    "FF_COM_SHS_OUT_EPS_DIL": {
      "cite": "AMGT_CORPUS round 48 ax-3 read of 80 stored workbooks (the research-report library and the master template), 2026-10-11: 23 workbooks agree, 0 disagree",
      "text": "Avg Diluted Shares"
    },
    "FF_EBITDA_OPER": {
      "cite": "AMGT_CORPUS round 48 ax-3 read of 80 stored workbooks (the research-report library and the master template), 2026-10-11: 19 workbooks agree, 0 disagree",
      "text": "EBITDA"
    },
    "FF_EBIT_OPER": {
      "cite": "AMGT_CORPUS round 48 ax-3 read of 80 stored workbooks (the research-report library and the master template), 2026-10-11: 21 workbooks agree, 0 disagree",
      "text": "Operating Income"
    },
    "FF_EPS_DIL_BEF_UNUSUAL": {
      "cite": "AMGT_CORPUS round 48 ax-3 read of 80 stored workbooks (the research-report library and the master template), 2026-10-11: 2 workbooks agree, 0 disagree",
      "text": "EPS"
    },
    "FF_FREE_CF": {
      "cite": "AMGT_CORPUS round 48 ax-3 read of 80 stored workbooks (the research-report library and the master template), 2026-10-11: 21 workbooks agree, 0 disagree",
      "text": "FCF"
    },
    "FF_NET_INC": {
      "cite": "AMGT_CORPUS round 48 ax-3 read of 80 stored workbooks (the research-report library and the master template), 2026-10-11: 1 workbook agrees, 0 disagree",
      "text": "Net Income"
    }
  }
}
```

2. `lib/research/corpus/team_sheet.py`, `_row_label`: the precedence becomes: the Bloomberg field map, held; then the team's own sheet MEASURED (column-B metric name,
   single-row pass-through, as today); then the entries file, held (FactSet codes only; `text` and `cite` AS STORED, `claim` "held", `source` "factset"); then the
   fallback line. Nothing else about a label changes. The measured rule is run for a FactSet code that has an entry (it was skipped before); keep the workbook's
   formula grid read at most once per workbook. Update the module doc's precedence line.
3. `lib/research/corpus/dossier.py`: bump `METHOD_VERSION` from `amgt-corpus-dossier/13` to `amgt-corpus-dossier/14`, add the comment line
   `# /14 (CRPS-ax-5): a FactSet code's single label across the team's workbooks is served held; the own sheet's measured label wins.` above it, and update ONLY that
   literal in the six tests that pin it (listed in `<paths>`), and the occurrences in `test_team_sheet_round47.py` and `test_template_round47.py` if they pin it.
4. **Tests:** in `test_team_sheet_round47.py` / `test_template_round47.py` the test that asserts "an entries-file entry wins over a measured label" becomes its
   reverse (the measured label wins; the entry serves a code with no own-sheet label); add a test with an in-memory workbook for each of: an entry with no own-sheet
   label (held, cite as stored), an entry AND an own-sheet label (measured wins), neither (fallback). Do not touch `template.py` behaviour.

## 2. BOUNDS

1. Only the files in `<paths>` change. Never edit the issuer's checks. No portal file, no `scoped_amgt.py`.
2. NO S3 write, NO deploy, NO push, NO Bloomberg or vendor call.
3. Write code with the Edit/Write tools, never a shell heredoc, sed or `python -c` rewrite. ASCII only.
4. Rows are `AMGT_CORPUS-D1-W1-S<k>` (next free k across every file under `surprise-channel/`), `disarm_owner 2.0.0_SA_COO~C1`, and `surfaced_at` = `date -u +%FT%TZ` at filing.
5. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~1 <0.9.0_WK_AMGT_CORPUS~1@opal.agent>" -F <msgfile> -- <paths>`. Your proof instance's `to_id` is
   this order's FULL id: `AMGT_CORPUS.TO-CRPS-ax-5.cross-workbook-labels-held-and-method-14`.

## 3. SURFACES

<paths>
lib/research/corpus/team_sheet.py
lib/research/corpus/factset_descriptions.json
lib/research/corpus/dossier.py
lib/research/corpus/tests/test_team_sheet_round47.py
lib/research/corpus/tests/test_template_round47.py
lib/research/corpus/tests/test_team_sheet_round44.py
lib/research/corpus/tests/test_dossier_method_bump.py
lib/research/corpus/tests/test_dossier_case_body.py
lib/research/corpus/tests/test_dossier_case_unit.py
lib/research/corpus/tests/test_dossier_case_positional.py
lib/research/corpus/tests/test_dossier_heading_only_round40.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-ax-5.cross-workbook-labels-held-and-method-14.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ax-5.cross-workbook-labels-held-and-method-14.md
</paths>

Read-only: the whole repository, in particular the issuer's check `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round48/ax5_check.py`.

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ax-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round48/ax5_check.py" 2&gt;&amp;1 | tail -1</invocation><expect>(?m)^ax5 build 3/3 control 2/2$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ax-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m pytest -q -p no:cacheprovider lib/research/corpus/tests/test_template_round47.py lib/research/corpus/tests/test_team_sheet_round47.py lib/research/corpus/tests/test_team_sheet_round46.py lib/research/corpus/tests/test_team_sheet_round44.py lib/research/corpus/tests/test_dossier_method_bump.py lib/research/corpus/tests/test_dossier_case_body.py lib/research/corpus/tests/test_dossier_case_unit.py lib/research/corpus/tests/test_dossier_case_positional.py lib/research/corpus/tests/test_dossier_heading_only_round40.py 2&gt;&amp;1 | tail -1 | sed 's/\x1b\[[0-9;]*m//g'</invocation><expect>(?m)^\d+ passed in [\d.]+s$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-ax-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; grep -c '^METHOD_VERSION = "amgt-corpus-dossier/14"$' lib/research/corpus/dossier.py</invocation><expect>(?m)^1$</expect></criterion>
  <criterion id="AC4" cell_refs="CRPS-ax-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; grep -c '"text":' lib/research/corpus/factset_descriptions.json</invocation><expect>(?m)^9$</expect></criterion>
</proof_of_spec>

- AC1: an entry serves a FactSet code with no own-sheet label (held, cite as stored); the own sheet's measured label wins over an entry; neither gives "FactSet line"; a field-map code keeps its description.
- AC2: your tests, round 47's, 46's and 44's, and the six method-pinning tests pass (every one of them reads `/14`).
- AC3: the method literal is `/14`.
- AC4: the entries file holds the nine entries (a fourth criterion: the data file is its own outcome).

## 5. WHEN YOU ARE DONE

1. Run `python -m lib.research.corpus.team_sheet --census` (read only; if the store is not reachable, say so) and put its labels and row-classes lines in your report.
2. Write the instance at the proof path (genre BUILD), with its mutant control; run `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4 --governing-order <this order>`
   AFTER your final commit; rc 0. WITHHOLD the order's complete tag: the issuer flips it after re-running the criteria.
3. Report ONCE: the change, AC1's to AC4's lines, the census lines, your commit hashes, any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-47 analysis ADDENDUM 1 (msg 4113) on the issuer's ax-3 read (evidence/r48_ax3_label_read_20261011_v2.txt: 80 workbooks, 372 sheets, 0 raised, control OK; 9 unambiguous codes, 252 rows, 1 to 23 workbooks each). The /14 write (its own pair) and the redeploy carrying /14 follow; whether round 98's redeploy carries /13 or /14 is the CTO's (asked). Base at the cut: AC1 FAIL (`build 2/3`), AC2 PASS or FAIL on the pins (the new tests are absent), AC3 FAIL (the literal reads /13; the file holds 0 entries).
<risk>LOCAL</risk>
<status>pending</status>
<round>48</round>
<slot>~1</slot>
<fabric>dell1</fabric>
