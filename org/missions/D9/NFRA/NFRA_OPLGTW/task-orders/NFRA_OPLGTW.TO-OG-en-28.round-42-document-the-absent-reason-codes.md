# NFRA_OPLGTW task order -- `OG-en-28` -- document the `absent_reason` codes in the client tools' notes, one line each saying what the code means and what a caller does next (round 42; CTO round-41 analysis item 3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-28</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-28</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~143</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- docstring text and one record file; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-41 analysis item 3 ("a consumer that cannot tell `window_read_busy` from `no_partition_at_as_of` re-creates Z-S372 on its own side").
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-28` (decomposition addendum R3-T.119, round 42, workstream ENRICH-R42-A)

THE GAP. Since `OG-en-24` the 49F adapter's reason words reach the caller in the field `absent_reason` (before, `client_core._answer` nulled them). A caller that reads `window_read_busy` (retry later), `no_partition_at_as_of` (no data on that date), `account_not_in_partition`, `no_candidate_for_last4`, `no_model_assignment_49f`, `no_fee_rows_in_window` and the core's refusal words can only tell them apart if the tool says what each means. The tool notes a caller reads are the DOCSTRINGS of the `client_*` functions in `infra/aws/ec2/opal-gateway/app/tools.py` (the five client tools: `client_resolve_account`, `client_get_holdings`, `client_get_transactions`, `client_get_allocation`, `client_get_fees`; they are served as the tool descriptions).

THE EDIT (documentation only; no behaviour changes):
1. ENUMERATE the codes. Read `app/client_adapter_bd49f.py` (every `_absent(as_of, "<code>", ...)` call, every `"absent_reason":` value, and the `window_read_busy` answer) and `app/client_core.py` (the `REFUSALS` table: the codes the core raises, each already explained there). Write `W/ABSENT_CODES.json` = `{"codes": [{"code": "<word>", "where": "<file>:<line>", "means": "<one line>", "caller_does": "<one line>"}]}`. A prefix code is written in full (`no_model_assignment_49f`). List AT LEAST EIGHT: every code the adapter can set, plus the core refusals a caller of these five tools can actually receive. A code you list must be a code the sources can set (the check reads both files; an invented word fails).
2. In the docstring of the tool(s) that can return each code, add ONE line per code in the form `<code>: <what it means; what the caller does next>` (the explanation after the code is at least 20 characters). Keep it short: tool descriptions are served to every caller on every `tools/list`, so write the shared codes ONCE, in the docstring of the tool that returns them most (for the windowed pair `client_get_transactions`, `client_get_fees` the busy word), and do not repeat a table five times.
3. THE LINE-COUNT RULE. `app/tools.py` is cited by LINE NUMBER in `app/refs/DATA_CATALOG.yaml` (`definition: app/tools.py:<line>`), so the edit must not move any line: ADD NO LINES to the file and DELETE NO LINES. Lengthen EXISTING docstring lines or replace existing lines of comment/docstring text with the code lines (the check requires lines added equal lines deleted in your commits on `tools.py`, and above 0). If a code needs a line the docstring does not have, replace a redundant line; if you cannot meet the rule without moving a line, file a BLOCKING row and keep working.
4. Do not touch any other file than the two in `<paths>` and the channel.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no behaviour change, no IAM, no env key, no catalog edit.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a secret or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/tools.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `app/tools.py` (docstring lines only) and `W/ABSENT_CODES.json` (the tree convention grants `W`); the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~143/`. Rows: id `NFRA_OPLGTW-Z-W143-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-28"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r42/checks/en28.AC1.sh; echo "exit=$?"</invocation><expect>(?s)codes listed (\d+) distinct \(want 8 or more\) of the \d+ the adapter and the core's REFUSALS table can set; adapter codes missing from the record 0 \(want 0\); codes outside both sets 0 \(want 0\); listed codes with no documenting line in a client_\* docstring 0 \(want 0\); tools\.py lines added ([1-9]\d*), deleted \2 .*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-28"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~143 '^infra/aws/ec2/opal-gateway/app/tools\.py$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~143: files touched [1-9]\d*; product files 1; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-en-28"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh en28set tests/test_og_en9.py tests/test_og_sv1.py tests/test_og_sv2.py tests/test_og_cl2.py tests/test_og_en24.py; echo "exit=$?"</invocation><expect>(?s)en28set forward: passed (\d+); failed 0.*en28set reverse: passed \1; failed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the record lists at least eight real codes including every adapter code, each is documented by a line in a `client_*` docstring, and `tools.py` kept its line count. `AC2`: your commits touch only `tools.py` (plus the record and channel). `AC3`: the five catalog, tool and client test files pass together in both orders with the same count.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-28.round-42-document-the-absent-reason-codes.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (commit hash, the AC lines, the list of codes).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 42, workstream ENRICH-R42-A (decomposition addendum R3-T.119). The CTO named "the gateway catalog's tool notes"; the issuer rules (inside its own decomposition) that the notes a caller reads are the `client_*` docstrings in `app/tools.py` (served as tool descriptions), not `DATA_CATALOG.yaml` (which carries sources and line citations, not prose). The line-count rule protects the catalog's `definition:` citations. The check derives the adapter's six literal codes from its source, and the core's `REFUSALS` table, so the universe is measured, not typed.
- A cell of the batched release `OG-ap-39`: `tools/list` descriptions change, names and count (103) do not.
- Pre-cut: `AC1` base FAIL as expected (the record is absent); `AC3` base: the five files pass.

<status>staged</status>
<round>42</round>
<workstream>ENRICH-R42-A</workstream>
<slot>~143</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
