# AMGT_RESAPP task order -- `AMGT-cc-6` -- THE ADAPTER CELL: EVERY HOOKUP OF THE ROUND, AND THE ONLY WRITER OF THE ADAPTER FILE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-cc-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~313</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only what the function or the hand-run tool already reads; no new read path is granted by this cell.
comp-adversary: RUN at the cut by the issuer's drafting read (GROUP_D_NOTES.md) -- At the base 12 of 12 clauses of the adapter check fail, the three served keys being absent; last round's hookups read YES 6 of 6; the two test folders read 1 failed, 860 passed. Not seen: the page, and the deployed function's imports. Every build criterion FAILS at the base and every bound criterion PASSES there; the literal outputs are in that file.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r79-313` (branch `wk-AMGT_RESAPP-313`, cut from the issuance commit with `--portal-ref d1b21c97`, the portal DEV head at the cut, and no package install). Work and commit only there. Start every shell call with `cd /c/tmp/r79-313`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-cc-6` (round 79, decomposition s.87)

Three cells of this round each built a new module and named a hookup. You make every hookup. You are the ONLY writer of
`lib/research/api/scoped_amgt.py` this round. The three modules are already merged into your worktree's base: read each one
and its tests, whole, before you call it:
`lib/research/api/segment_served.py`, `lib/research/api/dossier_sections.py`, `lib/research/freshness/collector_read.py`.
Each hookup below names the function to find, the place by line number AS MEASURED AT THE CUT, the exact call, and the effect.
Line numbers may have moved by a few lines: find the named function and the quoted line, never the number alone.

1. **The Bloomberg segment table on the thesis route.** In `read_thesis_bundle` (defined at `:3629`), find the line
   `bundle["segment_breakdown"] = read_segment_breakdown(resolved_key or security_key)` (`:3739`). Directly after it, and
   before the line `from lib.research.filings import section_coverage`, add these two lines, the import INSIDE the function:

       from lib.research.api import segment_served
       bundle["segment_table"] = segment_served.serve_segment_table(resolved_key or security_key, fiscal_year_figures, header_figures, client=_pool_client())

   `fiscal_year_figures` (`:3659`) and `header_figures` (`:3650`) are the names already in the function. Pass that
   `header_figures`, the stored list, not the plain-country copy the bundle serves. Effect: ONE new key, `segment_table`,
   beside `segment_breakdown`. Do not change `segment_breakdown` or anything that reads it.

2. **The five research-note sections on the thesis route.**
   (a) Beside the imports at `:134` to `:137`, add: `from lib.research.api import dossier_sections`
   (b) In `read_thesis_bundle`, inside the `bundle = {` literal, directly after the line
   `"dossier_fields": _dossier_fields(dossier_read),` (`:3692`), add this one line:

       "dossier_sections": dossier_sections.dossier_sections(dossier_read[0], read_failed=dossier_read[0] is None and str(dossier_read[1] or "").startswith("dossier read failed")),

   `dossier_read` is the pair already set at `:3655`. Make NO second read of the notes. Give no variable the name
   `dossier_sections`. Effect: ONE new key, `dossier_sections`, a list of five.

3. **The Seeking Alpha column, read from the collector's records.** All of this is in `read_coverage_freshness` (`:5787`).
   (a) Beside the import on the function's first line (`:5794`), add, INSIDE the function:
       `from lib.research.freshness import collector_read`
   (b) Delete the line `seeking_alpha_bronze_keys, seeking_alpha_bronze_record = _pool_keys(SEEKING_ALPHA_BRONZE_PREFIX)`
       (`:5802`) and, in the `per_vendor = {` literal, the line `"seekingalpha": _seeking_alpha_bronze_stamps(seeking_alpha_bronze_keys),`
       (`:5807`).
   (c) Directly after the line `covered_set = set(covered_keys)` (`:5824`), OUTSIDE every loop, add:

       seeking_alpha_read = collector_read.seeking_alpha_by_security(covered_keys, client=_pool_client())
       seeking_alpha_by_key = seeking_alpha_read["by_security"]
       seeking_alpha_stamps: Dict[str, str] = {}
       for covered_key, entry in seeking_alpha_by_key.items():
           stamp = collector_read.compact_stamp(entry.get("last_read")) if entry.get("state") == "read" else None
           if stamp:
               seeking_alpha_stamps[covered_key] = stamp
       per_vendor["seekingalpha"] = seeking_alpha_stamps
       seeking_alpha_states = {"read": 0, "checked": 0, "no_record": 0, "unreadable": 0}

       Call the reader by that dotted name, `collector_read.seeking_alpha_by_security`, exactly ONCE in the function. The
       stamp MUST be the compact form (`20261007T013241Z`): `last_refreshed` is a text `max` over stamps of that form.
   (d) In the row loop, after `security_key_value` is known, add:

       seeking_alpha_entry = seeking_alpha_by_key.get(security_key_value) if security_key_value in covered_set else None
       if seeking_alpha_entry is not None and seeking_alpha_entry.get("state") in seeking_alpha_states:
           seeking_alpha_states[seeking_alpha_entry["state"]] += 1

       and in the row dictionary (`rows.append({...})`, `:5863`), after the `"pack"` entry, add ONE key:

       "seeking_alpha": None if seeking_alpha_entry is None else {name: seeking_alpha_entry.get(name) for name in ("state", "sentence", "last_read", "newest_job_finished_at", "newest_job_status")},

       Change nothing else in the loop: the per-input copy and `last_refreshed` keep their code and now read the value of (c).
   (e) In the returned `"denominators"`: delete the `"seeking_alpha_bronze_objects_listed"` line (`:5891`) and add
       `"seeking_alpha_job_record_objects_listed": seeking_alpha_read["read"].get("objects_listed", 0),` and
       `"seeking_alpha_states": seeking_alpha_states,`
   (f) In the returned `"reads"`: delete the `"seeking_alpha_bronze"` line (`:5900`) and add
       `"seeking_alpha_job_record": seeking_alpha_read["read"],`
   (g) Leave `_seeking_alpha_bronze_stamps` (`:5670`), `_SEEKING_ALPHA_BRONZE_TABLES` and `SEEKING_ALPHA_BRONZE_PREFIX`
       where they are; they now have no caller in this file. Add one comment line above `_seeking_alpha_bronze_stamps` saying
       so and naming this cell. Deleting them is not this cell's.
   What this hookup must and must not do:
   - ONE listing of the records per build of the view. The view is built by the scheduled snapshot refresh
     (`refresh_freshness_snapshot`, `:5951`). The page's request (`serve_coverage_freshness`, `:5923`, and the route at
     `:7023`) reads the stored snapshot with one GET and lists nothing; do not add a call of the reader there, in the route,
     or anywhere outside `read_coverage_freshness`.
   - A failed read never writes a snapshot. You add NO code for that: `_freshness_complete` (`:5912`) already refuses a view
     whose `reads` holds a record with `read_completed` false, and (f) puts the reader's own record there. Do not edit
     `_freshness_complete`, `serve_coverage_freshness`, `refresh_freshness_snapshot`, `lib/research/freshness/snapshot.py` or
     `lib/research/freshness/stale_rule.py`.
   - The three states stay apart: a row whose state is `checked`, `no_record` or `unreadable` gets NO stamp (so it reads
     `NEVER` and is never flagged stale), and keeps its own `state` and `sentence` in `seeking_alpha`.

4. **The page view carries the new field.** In `lib/research/freshness/page_body.py` line 10, `PAGE_ROW_FIELDS` gains
   `"seeking_alpha"` as its LAST entry. Nothing else in that file changes.

5. **One phrase that would name the wrong block.** In `lib/research/api/inputs_statement.py` line 33, change
   `out.append("the segment table")` to `out.append("the segment breakdown")`. That line speaks of the breakdown read from
   the company filing (the key `segment_breakdown`); from this round `segment_table` is Bloomberg's table. Change that one
   string and nothing else in the file: the statement of inputs gains no row and no other word.

6. **The statement of inputs reads the new read record.** In `lib/research/api/top_band.py` line 34, in `INPUT_SOURCES`, the
   second item of the `"seekingalpha"` entry changes from `"seeking_alpha_bronze"` to `"seeking_alpha_job_record"`. The first
   item (the plain sentence) does not change.

7. **Tests** (in `lib/research/api/tests/` and `lib/research/freshness/tests/`):
   - `test_freshness_harvest_stamps.py`: rewrite `test_seekingalpha_reads_new_grammar_key_names_never_article_never_getobject`
     for the new source. Put collector records in the fake store under the address the module builds
     (`collector_read.job_record_location()`; type no bucket or prefix), make the two names covered (patch
     `covered_security_keys` the way `test_freshness_covered.py` does), and assert: the stamp is the compact form of the
     record's newest article time; the pilot-table key names no longer make a stamp; the new denominator equals the records
     listed. Keep the other two tests of the file as they are.
   - `test_freshness_covered.py`: the two tests that plant a pilot-table key (lines 29 to 41) plant a collector record instead
     and assert its compact stamp.
   - `test_page_body.py`: give the fixture's rows a `seeking_alpha` value so the key-set assertion at line 23 holds.
   - `test_inputs_statement.py` line 38: the expected phrase becomes `"the segment breakdown"`.
   - ADD plant tests, no network: (i) the thesis bundle carries `segment_table` and `dossier_sections` (patch the two module
     functions with recorders: each called once, with the arguments named above); (ii) the reader is called exactly once per
     `read_coverage_freshness`; (iii) a covered row of each of the four states carries `seeking_alpha` with the five keys, and
     only the `read` row carries a stamp; a row that is not covered carries `seeking_alpha` None; (iv) with the reader
     returning `read_completed` false, `_freshness_complete(view)` is false; (v) in `test_top_band_provenance.py`, a view whose
     `reads.seeking_alpha_job_record.read_completed` is false and whose row reads `NEVER` gives the outcome `failed`.

**What must NOT change.**
- On `/overlay` and `/thesis`: every key served today keeps its name and its value. You ADD two keys on `/thesis`
  (`segment_table`, `dossier_sections`) and none on `/overlay`. The two exceptions are named and are the whole list: the one
  phrase of hookup 5, and the Seeking Alpha row of the statement of inputs, which copies the freshness row.
- The round-78 hookups (the coverage marker, the plain country, the one statement of inputs, the officer rank, the source
  names, the peer price listing): untouched. Criterion AC2 reads them.
- The default `/freshness` body: every other field keeps its name and meaning. The whole change is: two keys retired
  (`denominators.seeking_alpha_bronze_objects_listed`, `reads.seeking_alpha_bronze`), three added
  (`denominators.seeking_alpha_job_record_objects_listed`, `denominators.seeking_alpha_states`,
  `reads.seeking_alpha_job_record`), one key added per row (`seeking_alpha`), and the SOURCE of `per_input.seekingalpha`.
- No `.tf` file. The function's permission to read the collector's records is another cell's. You deploy nothing, write to no
  store, send no scheduled event, and call no vendor, web or model service.
- You do not edit the three sibling modules, `segment_table.py`, `segment_period.py`, `collector_record.py`,
  `lib/research/freshness/build_view.py` or `lib/research/corpus/dossier.py`.

Run both test folders before your commit and report the last line. Report also: the seconds one `/thesis` took before and
after on `AMD_US_Equity`; the state counts criterion AC1 prints; and anything the three modules did that this text did not
foresee (file a surprise row for it and keep working; do not bend a hookup to fit).

Run the test folder your module sits in before your commit and report its last line. If a test fails only because it reads a portal file absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W313-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. You are the ONLY writer of `lib/research/api/scoped_amgt.py` this round. Edit no module another cell built: if one is wrong, file a row and say so in your report.
3. Every existing served key and value is unchanged: ADDED keys, and the Seeking Alpha fields the notes name as replaced.
4. Any sentence you serve to a user is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input ledger or bronze.
5. No `bun` command of any kind in this worktree (site Z interim rule: a worktree never installs packages).
6. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/inputs_statement.py
lib/research/api/top_band.py
lib/research/freshness/page_body.py
lib/research/api/tests/
lib/research/freshness/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~313/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-cc-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round79/checks/r79_cc6.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>the thesis serves the Bloomberg segment table for AMD US with its first column named fiscal year 2025 in USD, serves 8766 JP with its first column unnamed and a note, and reads a plain reason where no table is stored; it serves the five research-note sections for ASML NA in order and five absent entries with reasons for AMD US; every covered freshness row carries a Seeking Alpha state and sentence, no row that is not read carries a date or a stale flag, no date is 2026-09-11; the default freshness body keeps every other field; one build asks the record reader once, a page request answered from a snapshot asks it not at all, and a failed read writes no snapshot; H1-H4, H5a-H5d, K1 and L1-L3 PASS; R79 CC6 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-cc-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round79/checks/r79_cc6.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>the round-78 served shape still reads YES on the tree (its six clauses pass); B1 PASS; R79 CC6 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-cc-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round79/checks/r79_cc6.py" --crit AC3 --where local; echo "exit=$?"</invocation><expect>lib/research/api/tests/ and lib/research/freshness/tests/ show 860 or more passed, no error, and no failure other than the allowed test_harvest_prefixes.py::test_ii_registry_hash_matches, which the check prints; B1 PASS; R79 CC6 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~313 <0.9.0_WK_AMGT_RESAPP~313@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~313/AMGT_RESAPP.TO-AMGT-cc-6.the-adapter-cell.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the test folder's last line;
- the hookup another cell must make for your work to be served, or that none is needed;
- anything your read of the code found that this order did not say;
- any row.

The `<status>` flip is the issuer's.

## AMENDMENT 1 (2026-10-08 ~12:3xZ, by the issuer on CTO ruling msg 31722) -- ONE MORE WORDING, IN A FILE ALREADY IN YOUR PATHS

The team names its own document a "Research Pack", so those two words belong to the team's document alone. The thing this
system BUILDS for a name loses them. In `lib/research/api/top_band.py`, the `INPUT_SOURCES` entry for `"pack"` (line 36 as
measured at the cut) serves its source as `the research pack built for this name`. Change that ONE string to
`the analysis built for this name`. Change nothing else in that entry and no other sentence that says "research pack" anywhere:
the others name the team's document and stay. If a test in your two test folders asserts the old string, amend that assertion to
the new one. Do not edit any file under `org/` outside your own deliverables for this (older rounds' checks keep their text).
In your report, add one line: the served `source` of the `pack` row of `input_provenance` for `AMD_US_Equity`, read through the
handler on your tree.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-78 analysis R1: each hookup is named, and the redeploy's pair lists them. WAVE 1: cut from the drain of cc-1 to cc-5. Drafted in `deliverables/2.0.0_SA_COO~Z/round79/GROUP_D_NOTES.md` (cell D1), committed before the cut, in the issuance commit's ancestry. Checks dry-run at the base: AC1 base: run at the cut, result in the group notes; AC2 base: run at the cut, result in the group notes; AC3 base: run at the cut, result in the group notes.

<status>pending</status>
<round>79</round>
<slot>0.9.0_WK_AMGT_RESAPP~313</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending -- AMENDMENT 1 (CTO msg 31722): the pack row's served source wording, one string in top_band.py, already in paths; wave 0 drained 5 of 5 (cc-1 @0433c23f27, cc-4 @f6b844fadd, cc-5 @646167b6df, cc-3 @beee52785a, cc-2 @bdd1a55638), every criterion re-run YES on the shared tree</status>
