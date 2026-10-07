# AMGT_RESAPP task order -- `AMGT-bb-2` -- ONE STATEMENT OF INPUTS, WITH A FILINGS ROW THAT SAYS WHAT THE PAGE USED (RULING 4, FWD-12; ROW Z-W286-S2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bb-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~290</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only what the function or the hand-run tool already reads; no new read path is granted by this cell.
comp-adversary: RUN at the cut by the issuer's drafting read (GROUP_B_NOTES.md) -- 95 of 95 covered names serve input_provenance with no filings row; the overlay's provenance says no filings run is recorded on 95 of 95 while 12 theses cite a filing. Every build criterion FAILS at the base and every bound criterion PASSES there; the literal outputs are in that file.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r78-290` (branch `wk-AMGT_RESAPP-290`, cut from the issuance commit with `--portal-ref ba391aff`, the portal DEV head at the cut, and no package install). Work and commit only there. Start every shell call with `cd /c/tmp/r78-290`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-bb-2` (round 78, decomposition s.86)

Today the page states where its inputs came from in more than one place and the statements disagree: one says
"Filings: has not run yet" on a name whose thesis quotes its 10-K. Build the ONE statement both places will read.

Create `lib/research/api/inputs_statement.py` (standard library only: it rides the deployed package with no build
edit) exporting ONE function:

`statement(input_provenance, thesis)` returns a list of rows.
- `input_provenance` is the list the overlay serves today: four dicts `{input, source, last_run, outcome, reason}`
  for `bloomberg`, `seekingalpha`, `serp`, `pack`.
- `thesis` is the `/thesis` body for the same name (a dict), or `None` when the caller could not read it.

Rules:
1. Every row of `input_provenance` is returned unchanged, in the same order. Do not copy-edit them.
2. Add exactly ONE row with `input: "filings"`, placed immediately before the `pack` row (last when there is no
   `pack` row). Its keys: `input`, `source`, `last_run`, `outcome`, `reason`, `form`, `filing_date`, `used_for`.
   `source` is "company filings read for this name".
3. The page uses a filing when any of these five is true in `thesis`, and `used_for` lists the true ones in this
   order and these words:
   - `passage_coverage.sections` has one or more entries -> "the filing passages"
   - `drafting_provenance.accession` is set and `drafted_sections` is non-empty -> "the written sections"
   - `segment_breakdown.rows` is non-empty and `segment_breakdown.source.form` is set -> "the segment table"
   - `thesis_driver_chart.source == "filing"` with one or more `points` -> "the driver chart"
   - one or more of `management.officers` has `source == "filing"` -> "the officer list"
4. When one or more is true: `outcome: "landed"`; `form` and `filing_date` from the newest `filing_date` among
   `passage_coverage.source`, `drafting_provenance` and `segment_breakdown.source`; `last_run` equal to `filing_date`;
   `reason` one sentence naming the form, the date and the uses, for example "This page uses the 10-K filed 2026-01-30
   for the filing passages, the written sections and the officer list."
5. When none is true: `outcome: "never read"`, `last_run`, `form`, `filing_date` all `None`, `used_for: []`, `reason`
   "No company filing has been read for this name yet, so nothing on this page comes from one."
6. When `thesis` is `None`: `outcome: "failed"`, `reason` "What this page took from company filings could not be read
   just now." A failed read must never read as "never read".
7. `outcome` uses only the three values the other rows already use: "landed", "never read", "failed".
8. No sentence you write (`reason`, `source`, `used_for`) uses: identity, unresolved, security key, crosswalk,
   dossier, landed, model block, estate, stage, input ledger, bronze. (`"landed"` is allowed as the `outcome` value
   only; it is an existing code, not a sentence.)
9. The function reads no store, calls nothing and does not change its arguments.

Plant tests in `lib/research/api/tests/test_inputs_statement.py`: all five uses; one use; none; `thesis` None; no
`pack` row; arguments unchanged.

You do NOT edit `lib/research/api/scoped_amgt.py`, `lib/research/api/top_band.py` or any portal file. Your report
names the hookup below and anything about it you found different.

**The hookup the adapter cell makes (named, not built here):**
- `read_thesis_bundle`, after `passage_coverage` is set (`scoped_amgt.py:3700-3701`, before `return bundle` at
  `:3702`): `bundle["input_provenance"] = inputs_statement.statement(_overlay_input_provenance(resolved_key), bundle)`.
  The thesis body already holds all five parts, so this costs one cached freshness read and no new store read.
- `read_security_overlay`, `:3495`: the same statement under the same key `input_provenance`. The overlay does not
  hold the thesis parts, so the adapter supplies them (issuer question 1 below).
- The six-class ledger is replaced by this statement: the Model tab reads `input_provenance` (five rows) and stops
  calling `/ledger`. The `/ledger` route and the overlay's `provenance` block then have no reader on the page; whether
  they are removed or left unread is the adapter cell's and the page cell's, not this one's.

Run the test folder your module sits in before your commit and report its last line. If a test fails only because it reads a portal file absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W290-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. `lib/research/api/scoped_amgt.py` is READ, never edited: the round's adapter cell, AMGT-bb-17, makes every hookup. Name yours in your report.
3. The /ledger route is not retired by this cell and is not edited.
4. Any sentence you serve to a user is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input ledger or bronze.
5. No `bun` command of any kind in this worktree (site Z interim rule: a worktree never installs packages).
6. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/inputs_statement.py
lib/research/api/tests/test_inputs_statement.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~290/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bb-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb2.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>the four rows come back unchanged with ONE filings row before the pack row; a page that uses a filing reads "landed" with its form, date and five uses; a page that uses none reads "never read"; unread parts read "failed"; no served sentence carries a system word; C1-C4 PASS; R78 BB2 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bb-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb2.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>on the real overlay and thesis of BA_US_Equity the filings row reads "landed" with a form and a date; on AMD_US_Equity it reads "never read"; the four existing rows are unchanged on both; C1-C3 PASS; R78 BB2 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bb-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb2.py" --crit AC3 --where local; echo "exit=$?"</invocation><expect>the existing four-row builder's tests still pass; R78 BB2 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~290 <0.9.0_WK_AMGT_RESAPP~290@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~290/AMGT_RESAPP.TO-AMGT-bb-2.one-statement-of-inputs.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the test folder's last line;
- the hookup another cell must make for your work to be served, or that none is needed;
- anything your read of the code found that this order did not say;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-77 ruling 4. The page half is DSGN_AMGTV1's. Drafted in `deliverables/2.0.0_SA_COO~Z/round78/GROUP_B_NOTES.md` (cell B1), committed @643863854d before the cut. Checks dry-run at the base: AC1 base: run at the cut, result in the group notes; AC2 base: run at the cut, result in the group notes; AC3 base: run at the cut, result in the group notes.

<status>pending</status>
<round>78</round>
<slot>0.9.0_WK_AMGT_RESAPP~290</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>complete -- drained @025cab3f95; proof VALID rc=0 on the worker's checker; every criterion re-run by the issuer on the shared tree reads SERVED: YES; served only after the adapter cell bb-17</status>
