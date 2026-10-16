# TO-AR-g-134 -- TRACE every YCharts security-id dependency left in report generation (PRD v0.22 item 3): a read-only record, nothing under infra/ changes

<to_id>IRPT_ANLREQ.TO-AR-g-134</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~266</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>44</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-134` (`decompositions/IRPT_ANLREQ_DECOMP_R44_G.md`) |
**outcome_ref:** FWD-7 ("no YCharts call end to end") | **depends_on:** none. Order: CTO msg 9522, PRD v0.22 item 3: "No step may require a YCharts security id for a holding Yahoo prices."

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~266`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-266` (branch `wk-IRPT_ANLREQ-266`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~266 <0.9.0_WK_IRPT_ANLREQ~266@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W266-S<k>` (take the next free `<k>`; check the channel file for `W266` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- **READ-ONLY on the product.** You change nothing under `infra/`, `lib/` or `reports/`. Your only output is one JSON record in your folder. No network, no AWS call, no push.

### THE CELL (`AR-g-134`, inlined)

Andrew's rule (PRD v0.22): yfinance first, YCharts second, everywhere. The upload door will ask yfinance first, so a holding Yahoo prices will reach report generation with NO YCharts security id. Report generation today builds the portfolio in YCharts by YCharts security id. Your job is to find, by reading the code, EVERY place in report generation where a YCharts security id (or a call to YCharts that needs one) is required, and say for each whether a holding that Yahoo prices (history at T-1) can do without it.

Read, at least: every `.py` file in `infra/aws/lambda/investor-reporting/ycharts/generate/` (not the `tests/` folder), `infra/aws/lambda/investor-reporting/ycharts/research/price_source.py` (the price chain `estate, yfinance, ycharts`), `infra/aws/lambda/investor-reporting/reports/build_resident_package.py` (the build flag `opal_pricing`, line about 119), and whatever those call to turn a holding into a YCharts portfolio, a time series, a risk or return figure or a chart. Search for the terms `security_id`, `YCHARTS_SECURITY_ID`, `securities_info`, `ycharts` and `portfolio` with the Grep tool, then read each hit's surroundings. A dependency is a line where a holding's YCharts id is read, required, sent to YCharts or used as a key, or a function that raises or skips a holding when the id is missing.

Write ONE file: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~266/YCHARTS_ID_TRACE.json` (create the folder). Shape (a JSON object):
- `entry_points_read`: list of the repo-relative paths you read as the starting points (each must be a file that exists).
- `dependencies`: list of rows, one per dependency, each with: `site` ("repo-relative/path.py:LINE"), `line_text` (that exact line, stripped), `what` (one sentence: what the line does with the id), `needs_ycharts_id_for_yahoo_priced_holding` ("YES" if a Yahoo-priced holding with no YCharts id would fail, be skipped or lose data here; "NO" if it would not), `id_source` (REQUIRED when YES: where the id comes from, for example the door's `securities_info` answer, or the swap pass), `removal` (one sentence: what would remove the need, or why it cannot be removed), `claim` ("MEASURED" if you read the line and followed what it calls; "INFERRED" if you reasoned past what you read).
- `summary`: `{"dependencies": <number of rows>, "needs_yes": <number of rows with YES>}`.
- `remaining_ycharts_calls`: list of strings naming each YCharts call that stays even after the YES rows are removed (the data YCharts alone supplies), each with how many calls one report makes if you can read it; an empty list if none.
If you find a place you cannot follow, add a row for it with `claim` INFERRED and say so in `what`. Do not guess a line number: copy it from a Read or Grep result.

1. Run the two criteria. Commit the record, then the proof and the status flip, as separate commits (record first).
2. **Report** the commit hashes, the summary counts, the YES rows' sites, the `remaining_ycharts_calls` list and both criterion outputs.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR134-g-AC1" cell_refs="AR-g-134"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g134_checks.py verify org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~266/YCHARTS_ID_TRACE.json</invocation><expect>^AR-G134-OK</expect></criterion>

<criterion id="AR134-g-AC2" cell_refs="AR-g-134"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g134_checks.py scope box/dell2 org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~266 org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-134.trace-ycharts-id-dependencies.md</invocation><expect>^AR-G134-SCOPE-OK</expect></criterion>

<expected_criteria>AR134-g-AC1,AR134-g-AC2</expected_criteria>

- AC1 checks the record is well formed and every citation is real: each `site` exists at that line and its `line_text` equals the file's line; every row says YES or NO, a claim word, what and removal; a YES row names its id source; the summary equals the rows. At base (no record) it FAILs. It does not grade whether the trace is complete: the issuer reads the content.
- AC2 checks (against the merge-base with `box/dell2`) that your branch changed nothing outside your own folder, your order, the channel file and the issuer's issuance files. At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. READ-ONLY on the product.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~266/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-134.trace-ycharts-id-dependencies.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R44_G.md</decomp_doc> round 44, workstream ~G, cell `AR-g-134`.
<owned_cells>AR-g-134</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR134-g-AC1, AR134-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~266/IRPT_ANLREQ.TO-AR-g-134.trace-ycharts-id-dependencies.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-134`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the record first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR134-g-AC1,AR134-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** as step 2.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- a read-only trace; the only write is one JSON record and the proof in the worker's folder. Nothing deployed, no AWS call, no network.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call. comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. 
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; a read-only trace.
comp-adversary: RUN -- the issuer's verifier `ar_g134_checks.py` was dry-run on a good record and on five bad ones (a wrong line_text, a YES row with no id_source, a summary that does not equal the rows, a line past the end of the file, a missing file): the good one passes, each bad one fails. Traps: a cited line that does not hold the quoted text; a YES row with no id source; a trace that lists only the first hit of each term; a dependency named with an invented line number. NOT seen (blind): whether the trace is COMPLETE (the verifier checks citations, not coverage; the issuer reads the content and the CTO reads the removal cell it produces); denominator: the files under `ycharts/generate/` (non-test) plus `price_source.py` and `build_resident_package.py`.
</preflight>

- Cut on the CTO's rule (msg 9522, PRD v0.22 item 3) by the issuer inside its own decomposition. Risk LOCAL (a record). Base: AR134-g-AC1 FAILs (no record), AR134-g-AC2 PASSes (in the worker's worktree).
