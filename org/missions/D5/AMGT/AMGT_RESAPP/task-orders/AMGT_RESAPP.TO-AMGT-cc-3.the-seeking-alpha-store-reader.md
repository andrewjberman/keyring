# AMGT_RESAPP task order -- `AMGT-cc-3` -- THE STORE READER OF THE SEEKING ALPHA COLLECTOR'S JOB RECORDS, ONE LISTING PER SNAPSHOT REFRESH (ROW Z-S367, RULING R1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-cc-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~310</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only what the function or the hand-run tool already reads; no new read path is granted by this cell.
comp-adversary: RUN at the cut by the issuer's drafting read (GROUP_B_NOTES.md) -- 105 job records in 104 folders, 105 of 105 parse; 23 of 95 covered names hold one: read 11, checked 12, no record 72. Every build criterion FAILS at the base and every bound criterion PASSES there; the literal outputs are in that file.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r79-310` (branch `wk-AMGT_RESAPP-310`, cut from the issuance commit with `--portal-ref d1b21c97`, the portal DEV head at the cut, and no package install). Work and commit only there. Start every shell call with `cd /c/tmp/r79-310`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-cc-3` (round 79, decomposition s.87)

The freshness page's "Seeking Alpha last read" column is wrong for every covered company. The collector now writes one small
JSON record per finished job, and a pure reader of those records already exists
(`lib/research/freshness/collector_record.py`: `parse_record`, `partition_for`, `seeking_alpha_state`). Nothing reads the
records from the store yet. Build that one store-reading module. Another cell connects it to the page; you connect nothing.

Read first, whole: `lib/research/freshness/collector_record.py`, `lib/research/freshness/seeking_alpha_job_record.schema.json`
(its `x-address` and `x-reader-rules`), and `lib/research/freshness/snapshot.py` (how this package asks the address builder).

Create `lib/research/freshness/collector_read.py`. Standard library only at the top of the file, plus
`from lib.research.freshness import collector_record`. Import `boto3` and `lib.opal_naming` INSIDE the functions that use them.
**Never import `lib.research.harvest.store` or `pyarrow`**: the deployed function does not carry `pyarrow`.

It exports exactly these names:

`READ_WIDTH = 16`, `MAX_RECORDS_PER_COMPANY = 5`,
`UNREADABLE_SENTENCE = "The Seeking Alpha collection record could not be read just now."`

`job_record_location()` returns `(bucket, prefix)`.
1. Call `lib.opal_naming.address("seeking-alpha", lib.opal_naming.lookup("harvest")["long"], "state", "job_record", "date=1970-01-01")`.
   It returns `s3://<bucket>/<key>`. The bucket is the text between `s3://` and the first `/`. The prefix is the key with its
   last segment cut, ending in `/`. Type no bucket name and no prefix anywhere in the module or its tests.

`compact_stamp(last_read)` returns text or `None`.
2. For text shaped `YYYY-MM-DDTHH:MM:SSZ` return `YYYYMMDDTHHMMSSZ` (`2026-10-07T01:32:41Z` gives `20261007T013241Z`).
   For `None` or anything else return `None`. It never raises.

`seeking_alpha_by_security(covered_keys, client=None)` returns a dict with exactly two keys, `"by_security"` and `"read"`.
It NEVER raises, whatever the store does.
3. `covered_keys` is a list of company keys such as `BA_US_Equity` or `BP/_LN_Equity`. Keep the first of any repeated key.
   `"by_security"` holds one entry for EVERY key given, and no other key.
4. `client` is a store client with `get_paginator("list_objects_v2").paginate(Bucket=..., Prefix=...)` and
   `get_object(Bucket=..., Key=...)`. When it is `None`, make `boto3.client("s3", region_name="us-east-1")` inside the function.
   Call no other method of the client. Never write, copy or delete.
5. **ONE listing per call.** Paginate the prefix from rule 1 once and read every page's `Contents`. Do not pass `Delimiter`.
   Count every listed object in `read["objects_listed"]`.
6. A listed key counts only when, after the prefix, it is exactly `<folder>/<name>` with the folder starting `security_key=`
   and the name ending `.json`. Any other key is counted in `read["ignored"]` and never fetched.
7. A company's folder is `collector_record.partition_for(<key>)`. Fetch bodies ONLY for folders of the keys given. An object in
   any other folder is never fetched.
8. For one company, sort its object keys from greatest to least and keep the first `MAX_RECORDS_PER_COMPANY`. When it held
   more, add the company's key to the list `read["capped"]`. (The object name is the job's end time, so the greatest names are
   the newest jobs; each record already carries the newest article time held up to that job.)
9. Fetch each kept object with `get_object`, read its `Body`, decode UTF-8 and parse JSON. Use a
   `concurrent.futures.ThreadPoolExecutor` of `min(READ_WIDTH, <objects to fetch>)` workers when there is more than one.
   Fetch no object twice.
10. A body that is fetched but is not UTF-8 JSON becomes `None` in the company's list. A fetched object for which
    `collector_record.parse_record` returns `None` (that includes the `None` just named) has its store key added to the list
    `read["rejected"]`. It is still handed to `seeking_alpha_state`, which counts it and never uses it as a date.
11. The company's entry is `collector_record.seeking_alpha_state(<its list of objects>)`, called with NO `pilot_stamp`. A company
    with no folder gets `seeking_alpha_state([])`, which reads `no_record`. Do not change the dict that function returns.
12. **A fetch that raises.** Add that object's key to the list `read["bodies_failed"]`. The company it belongs to gets the
    UNREADABLE entry of rule 14, even if its other objects were fetched. Every other company is unaffected.
13. **A listing that raises, or the address builder raising.** Every company gets the UNREADABLE entry; nothing is fetched;
    `read["reason"]` says what failed in plain words with the error's type name.
14. The UNREADABLE entry is exactly: `state` `"unreadable"`, `last_read` `None`, `newest_job_finished_at` `None`,
    `newest_job_status` `None`, `stored_by_newest_job` `None`, `records` `0`, `rejected` `0`, `sentence` `UNREADABLE_SENTENCE`.
    It never carries a date.
15. `"read"` is a dict with exactly: `status` (`"served"` or `"read_failed"`), `read_completed` (true only when the listing
    finished AND no fetch raised), `store` (`s3://<bucket>`, or `None` if the builder raised), `prefix`, `objects_listed`,
    `ignored`, `folders` (distinct counted folders listed), `covered_names` (keys given after rule 3), `covered_with_folder`,
    `bodies_read` (objects fetched), `bodies_failed` (sorted list), `rejected` (sorted list), `capped` (list, in the order of
    the keys given), `reason` (`None` when `read_completed` is true).
16. The module never reads `seeking-alpha/harvest/bronze/` or any other prefix. The September pilot objects are not its input.
17. No sentence it returns uses: not collected, identity, unresolved, security key, crosswalk, dossier, landed, model block,
    estate, stage, input ledger, bronze.

Plant tests in `lib/research/freshness/tests/test_collector_read.py` with a fake client of your own (a dict of key to bytes;
no network): one test per rule 2, 3, 5 to 14, and one that the module's source text contains neither `harvest.store` nor
`pyarrow`.

You do NOT edit `lib/research/api/scoped_amgt.py`, `lib/research/freshness/build_view.py`, `lib/research/freshness/page_body.py`,
`lib/research/freshness/stale_rule.py`, `lib/research/freshness/collector_record.py` or the schema file. You deploy nothing and
write nothing to any store. AC2 reads the real store with this device's own credentials (list and GET only). Your report names
anything the hookup cell must know that this order did not say.

Run the test folder your module sits in before your commit and report its last line. If a test fails only because it reads a portal file absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W310-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. `lib/research/api/scoped_amgt.py` is READ, never edited.
3. `lib/research/freshness/collector_record.py`, the schema file and `build_view.py` are READ, never edited.
4. Three states are kept apart: read, checked with nothing new, no record. No record is never a date and never stale (CTO msg 31672).
5. Any sentence you serve to a user is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input ledger or bronze.
6. No `bun` command of any kind in this worktree (site Z interim rule: a worktree never installs packages).
7. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/freshness/collector_read.py
lib/research/freshness/tests/test_collector_read.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~310/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-cc-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round79/checks/r79_cc3.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>on a fake store, two companies read with their newest article date, a no-article record reads checked, no folder reads no_record, a malformed object is counted and named, the slash name is found, a failed listing and a failed body read unreadable with no date, one listing per call, the cap holds; F0-F11 PASS; R79 CC3 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-cc-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round79/checks/r79_cc3.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>on the real store the read finishes, 95 of 95 covered names have a state, each equals the check's own recount (90 or more compared, 0 differ), 23 or more hold a record and 11 or more read a date, no date is 2026-09-11; R1-R6 PASS; R79 CC3 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-cc-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round79/checks/r79_cc3.py" --crit AC3 --where local; echo "exit=$?"</invocation><expect>the freshness test folder passes and collector_record.py and the schema file hold the bytes of the cut; B1-B2 PASS; R79 CC3 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~310 <0.9.0_WK_AMGT_RESAPP~310@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~310/AMGT_RESAPP.TO-AMGT-cc-3.the-seeking-alpha-store-reader.proof_of_spec.json`.
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

**ISSUER NOTES:** CTO round-78 analysis R1 (FWD-7); CTO ruling msg 31672 (serve now, read-only grant, three states). Drafted in `deliverables/2.0.0_SA_COO~Z/round79/GROUP_B_NOTES.md` (cell B1), committed before the cut, in the issuance commit's ancestry. Checks dry-run at the base: AC1 base: run at the cut, result in the group notes; AC2 base: run at the cut, result in the group notes; AC3 base: run at the cut, result in the group notes.

<status>pending</status>
<round>79</round>
<slot>0.9.0_WK_AMGT_RESAPP~310</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
