# AMGT_RESAPP task order -- `AMGT-bb-1` -- THE SEGMENTS READER: A SEGMENT TABLE FROM THE STORED BLOOMBERG SEGMENTS OBJECT (RULING 3, FWD-1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bb-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~289</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only what the function or the hand-run tool already reads; no new read path is granted by this cell.
comp-adversary: RUN at the cut by the issuer's drafting read (GROUP_A_NOTES.md) -- 85 stored partitions read at the cut: 76 names carry revenue rows, 9 none, 50 operating income; the object carries no fiscal period and no currency. Every build criterion FAILS at the base and every bound criterion PASSES there; the literal outputs are in that file.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r78-289` (branch `wk-AMGT_RESAPP-289`, cut from the issuance commit with `--portal-ref ba391aff`, the portal DEV head at the cut, and no package install). Work and commit only there. Start every shell call with `cd /c/tmp/r78-289`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-bb-1` (round 78, decomposition s.86)

Build a reader of the stored Bloomberg segment table as a NEW module, `lib/research/api/segment_table.py`, exporting ONE function:

`read_segment_table(security_key, client=None)` returns a dict with exactly these keys:
`status` ("served" or "none"), `rows`, `operating_income_rows`, `periods`, `period_note`, `currency`, `currency_note`, `reason`, `source`.
A row is `{"segment": str, "level": int, "values": [five entries, each a float or None]}`.

1. **Where it reads.** One folder per name in bucket `opal-data-harvest`: `bloomberg/harvest/bronze/segments/` +
   `lib.research.harvest.store.entity_partition("security_key", security_key)` + `/`, objects named `<stamp>.json`. Build the
   folder ONLY through `entity_partition`: two stored names carry a slash and their folders are `security_key=BP-SLASH-_LN_Equity`
   and `security_key=NG-SLASH-_LN_Equity`. `security_key` arrives in the underscore form (`AMD_US_Equity`, `BP/_LN_Equity`).
   `client` is an S3 client; when None, build `boto3.client("s3", region_name="us-east-1")` inside the function. Use only
   `client.get_paginator("list_objects_v2").paginate(Bucket=..., Prefix=...)` and `client.get_object(Bucket=..., Key=...)`: the
   check and the adapter both pass a client that offers just those two.
2. **Which object.** Sort the folder's `.json` keys newest first (the stamp sorts as text). Take the first USABLE one, reading
   at most five. The body is `{"security", "pulled_at", "response"}`. An object is usable when `response["__field_errors__"]`
   has no entry for `PG_REVENUE` AND (the response carries `PG_REVENUE` or `PG_OPERATING_INCOME`, or it has no field errors
   at all). An object that holds only refused fields (a field probe) is skipped, even when it is the newest.
   **AMENDMENT 1 (issuer, 2026-10-07, on row AMGT_RESAPP-Z-W289-S1).** Read the five newest objects, then choose in two
   passes. FIRST: the newest of them that has no `PG_REVENUE` field error AND carries `PG_REVENUE` or `PG_OPERATING_INCOME`.
   ONLY IF none of the five does: the newest usable one by the rule above. So a later pull of other fields into the same folder
   (AMD US holds one, stamped 20261007T145856Z, with no segment list and no errors) never hides a stored table. Add one plant
   test for exactly that case: a newer error-free object with no segment list above an older one with a table serves the table.
   The check was amended to the same rule on the issuer's tree; run it from there against YOUR worktree's code:
   `cd /c/tmp/r78-289 && PYTHONPATH="$(pwd)" python "/c/Users/Opal Bloomberg/Desktop/ajb_workspace/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb1.py" --crit AC1 --where local; echo "exit=$?"`
   (and the same line with AC2 and AC3). Row Z-W289-S1 is disarmed by this amendment; do not edit it.
3. **Rows.** `response["PG_REVENUE"]` and `response["PG_OPERATING_INCOME"]` are lists of
   `{"Metric Name", "Period 1 Value" .. "Period 5 Value", "Product Geographic Hierarchy Level"}`. For each row:
   `segment` is the metric name with every non-breaking space (`chr(160)`) turned into a space, runs of space collapsed, ends
   stripped; change no other character. `level` is the hierarchy level as stored (1 is a top line; 2 to 5 are lines beneath
   it). `values` are periods 1 to 5 in order: None when the stored value is missing, is not a number, or is non-zero and
   smaller than 1e-9 in size (Bloomberg writes a missing period as about -2.4e-14); an exact 0.0 stays 0.0. Keep the stored
   row order. `rows` come from `PG_REVENUE`, `operating_income_rows` from `PG_OPERATING_INCOME`. Do NOT join the two tables by name.
4. **Periods and currency.** The stored object names neither a fiscal year nor a currency. Serve `periods` as
   `["Period 1", "Period 2", "Period 3", "Period 4", "Period 5"]`, `period_note` as one plain sentence saying these are
   Bloomberg's own period numbers and the stored table does not say which fiscal year each one is, `currency` as None, and
   `currency_note` as one plain sentence saying the stored table does not state its currency or its units. Never guess either.
5. **The share-capital and one-heading rule (round-76 ruling 7).** Before serving, hand
   `lib.research.filings.table_class.segment_refusal` the revenue rows as `[{"segment": <segment>, "text": ""}, ...]`. If it
   returns a sentence, serve `rows: []`, `operating_income_rows: []`, `status: "none"` and YOUR OWN reason, because that
   module's sentences say "the filing text kept here" and this table is not a filing: for
   `table_class.SEGMENT_CAPITAL_REASON` say the Bloomberg table lists share capital rather than business lines; for
   `table_class.SEGMENT_ONE_LABEL_REASON` say it repeats one heading rather than separate business lines. `table_class.py` is
   read, never edited. (On today's 76 stored tables it refuses none; your tests plant both cases.)
6. **Nothing to show, each with its own plain reason** (`status: "none"`, `rows: []`):
   no object in the folder ("No Bloomberg segment table has been stored for this name yet."); objects, none usable; a usable
   object with no revenue lines (9 stored names today; when it carries operating income lines, still serve those in
   `operating_income_rows`); no `security_key` given; a read that failed ("... could not be read just now"). The function
   NEVER raises: any exception becomes the read-failed reason.
7. **`source`** when an object was chosen: `{"vendor": "Bloomberg", "label": "Bloomberg product segments", "object": <the key
   read>, "pulled_at": <the body's pulled_at>, "company": <response NAME>}`; None when no object was chosen.
8. Every reason is in plain words. Do not use: identity, unresolved, security key, crosswalk, dossier, landed, model block,
   estate, stage, input ledger, bronze.

Plant tests in `lib/research/api/tests/test_segment_table.py` with a small fake client: a served table, the newer-probe case,
the marker and the true zero, the indent, both refusals, each of the five kinds of nothing, a slash name, a client that raises.

**You do NOT edit `lib/research/api/scoped_amgt.py`, `lib/research/filings/table_class.py` or `lib/research/harvest/store.py`.**
The hookup is the adapter cell's. Name it in your report: `segment_table.read_segment_table(key, client=_pool_client())`, called
where `/thesis` is assembled beside `read_segment_breakdown` (`scoped_amgt.py:3696`), served under a NEW key `segment_table`;
the filing-prose `segment_breakdown` stays as it is.

Run the test folder your module sits in before your commit and report its last line. If a test fails only because it reads a portal file absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W289-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. `lib/research/api/scoped_amgt.py` is READ, never edited.
3. The stored object states no fiscal period and no currency. Serve the vendor's period numbers and a null currency, each with its plain note. Do not guess either.
4. Any sentence you serve to a user is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input ledger or bronze.
5. No `bun` command of any kind in this worktree (site Z interim rule: a worktree never installs packages).
6. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/segment_table.py
lib/research/api/tests/test_segment_table.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~289/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bb-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb1.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>AMD US serves clean revenue rows from the newest stored object that carries the table; BP/ LN serves rows; a stored name with no revenue lines and a never-stored name each read their own plain reason; every stored name reads as its newest usable object says (N of N); periods and currency are stated plainly with currency None; C1-C5 PASS; R78 BB1 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bb-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb1.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>a newer object of refused fields is not chosen; indent stripped, level kept, the marker None, a true zero kept; share-capital lines and one repeated heading refused with a reason that names no filing; a raising store reads a reason; a slash name is found; F1-F5 PASS; R78 BB1 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bb-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb1.py" --crit AC3 --where local; echo "exit=$?"</invocation><expect>every plant case in test_segment_table.py passes; R78 BB1 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~289 <0.9.0_WK_AMGT_RESAPP~289@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~289/AMGT_RESAPP.TO-AMGT-bb-1.the-segments-reader.proof_of_spec.json`.
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

**ISSUER NOTES:** CTO round-77 ruling 3. Issuer default on period and currency: CALLS_AT_THE_CUT_20261007.md section B. Drafted in `deliverables/2.0.0_SA_COO~Z/round78/GROUP_A_NOTES.md` (cell A1), committed @643863854d before the cut. Checks dry-run at the base: AC1 base: run at the cut, result in the group notes; AC2 base: run at the cut, result in the group notes; AC3 base: run at the cut, result in the group notes.

<status>pending</status>
<round>78</round>
<slot>0.9.0_WK_AMGT_RESAPP~289</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
