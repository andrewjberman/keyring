# AMGT_RESAPP task order -- `AMGT-bb-16` -- THE SEEKING ALPHA LAST-READ READER OVER THE COLLECTOR'S JOB RECORDS (ROW Z-S367)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bb-16</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~301</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only what the function or the hand-run tool already reads; no new read path is granted by this cell.
comp-adversary: RUN at the cut by the issuer's drafting read (GROUP_D_NOTES.md) -- The served reader takes the date from four tables holding 3 pilot partitions of 2026-09-11: 95 of 95 names read wrong. Every build criterion FAILS at the base and every bound criterion PASSES there; the literal outputs are in that file.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r78-301` (branch `wk-AMGT_RESAPP-301`, cut from the issuance commit with `--portal-ref ba391aff`, the portal DEV head at the cut, and no package install). Work and commit only there. Start every shell call with `cd /c/tmp/r78-301`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-bb-16` (round 78, decomposition s.86)

The freshness page's "Seeking Alpha last read" is wrong for every covered company: it reads tables the collector stopped writing
in September. The collector will write one small record per finished job. Build the reader of those records. It is a pure
module: it reads no store. Another cell connects it to the page.

Read `lib/research/freshness/seeking_alpha_job_record.schema.json` first. It is the ONE contract, shared with the team that
writes the records. Do not edit it.

Create `lib/research/freshness/collector_record.py` (standard library only) exporting:

`REQUIRED_FIELDS`: a tuple equal to the schema's `required` list.

`parse_record(obj)` returns a clean dict of the record's fields, or `None` when `obj` does not match the contract.
1. It matches when every required field is present, `schema_version` is 1, `security_key` is text ending `_Equity`,
   `finished_at` is text shaped `YYYY-MM-DDTHH:MM:SSZ`, `status` is non-empty text, `stored` is a whole number of 0 or more
   (a true/false value is not a number), and `newest_article_stored_at` is either `None` or text of the same time shape.
2. Extra keys are allowed and are dropped from the returned dict, except `run_id`, which is kept when it is text.

`partition_for(security_key)` returns the folder name the records of that company sit under.
3. Use `lib.research.identity.crosswalk.security_key_partition`, the same function the freshness view already uses, so a name
   with a slash in it (`BP/_LN_Equity`) gets the slash-safe folder (`security_key=BP-SLASH-_LN_Equity`).

`seeking_alpha_state(records, pilot_stamp=None)` returns
`{"state", "last_read", "newest_job_finished_at", "newest_job_status", "stored_by_newest_job", "records", "rejected", "sentence"}`.
`records` is a list of objects as read from the store (dicts); `pilot_stamp` is the September pilot object's stamp when the
caller has one.
4. Run every object through `parse_record`. `records` is the count that parsed, `rejected` the count that did not.
5. The newest job is the parsed record with the greatest `finished_at`: its end time, status and stored count fill
   `newest_job_finished_at`, `newest_job_status`, `stored_by_newest_job`.
6. `last_read` is the greatest `newest_article_stored_at` across the parsed records, ignoring `None`.
7. `state` is `"read"` when `last_read` is set. `sentence`: "Seeking Alpha last read <date>." with the date as YYYY-MM-DD.
8. `state` is `"checked"` when one or more records parsed and none holds an article time. `sentence`: "Seeking Alpha was
   checked on <date of the newest job> and no article is held for this company." `last_read` stays `None`.
9. `state` is `"no_record"` when no record parsed. `sentence`: "No Seeking Alpha collection record is held for this company
   yet." `last_read` stays `None`.
10. **`pilot_stamp` never becomes a date and never changes the state.** It is accepted so the caller can hand it in; the
    function ignores it. The words "not collected" appear in no sentence this function returns: an empty folder is not
    evidence that nothing was collected.
11. No sentence uses: identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input
    ledger, bronze.
12. The function does not change its arguments.

Plant tests in `lib/research/freshness/tests/test_collector_record.py`: one case per rule 1 clause, rules 5 to 10, and the two
examples inside the schema file.

You do NOT edit `lib/research/api/scoped_amgt.py`, `lib/research/freshness/build_view.py` or the schema file. Your report
names the hookup: where the served freshness reader would list the records (one listing of the records' prefix, grouped by
folder) and call `seeking_alpha_state`, and which served fields it would replace.

Run the test folder your module sits in before your commit and report its last line. If a test fails only because it reads a portal file absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W301-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. `lib/research/api/scoped_amgt.py` is READ, never edited.
3. `lib/research/freshness/seeking_alpha_job_record.schema.json` and `lib/research/freshness/build_view.py` are READ, never edited.
4. Any sentence you serve to a user is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input ledger or bronze.
5. No `bun` command of any kind in this worktree (site Z interim rule: a worktree never installs packages).
6. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/freshness/collector_record.py
lib/research/freshness/tests/test_collector_record.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~301/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bb-16"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb16.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>a record with a stored article reads as read and is dated by its newest article; two records give the greatest article time and the greatest end time; records with no article read as checked with no date; no record reads no_record and never not collected; an object off the contract is counted and not used; the pilot stamp is not a date; C1-C6 PASS; R78 BB16 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bb-16"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb16.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>the module's required fields equal the schema's; both schema examples parse (2 of 2); a slash name's folder is the slash-safe one; S1-S3 PASS; R78 BB16 AC2 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~301 <0.9.0_WK_AMGT_RESAPP~301@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~301/AMGT_RESAPP.TO-AMGT-bb-16.the-seeking-alpha-collector-record-reader.proof_of_spec.json`.
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

**ISSUER NOTES:** CTO msg 31060 and rulings file @f97be3fd6f (C2: serve only when the collector's records exist), row Z-S367. Drafted in `deliverables/2.0.0_SA_COO~Z/round78/GROUP_D_NOTES.md` (cell D1), committed in the issuance commit's parent. Checks dry-run at the base: AC1 base: run at the cut, result in the group notes; AC2 base: run at the cut, result in the group notes.

<status>pending</status>
<round>78</round>
<slot>0.9.0_WK_AMGT_RESAPP~301</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
