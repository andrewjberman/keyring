# TO MDPF_SECCLASS.TO-SC-e102 -- round 25 SC-e-102: C_06 writes mix_daily_summary.json with sorted keys (build only, nothing deployed)

<to_id>MDPF_SECCLASS.TO-SC-e102</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~92</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>25</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-102` (`decompositions/MDPF_SECCLASS_DECOMP_R25.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none | **source:** CTO round-24 analysis section 4 item 3, msg 5506; XA-20261014T113939Z-a304

---

## WORKER FACE

### THE CELL

`SC-e-102`. The gold job C_06 (`data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py`) writes `mix_daily_summary.json` with `_write_mix_summary`
(about lines 663-676): `body = json.dumps(payload, separators=(',', ':')).encode('utf-8')`. The payload is `{'firm': firm_daily, 'advisors': advisor_daily,
'restated_through': ...}`. Measured: two C_06 runs on identical inputs produced the SAME parsed JSON but a different byte order under `advisors` (the object's ETag
changed on every run: 9,941,227 bytes each, three different md5s). **The change: add `sort_keys=True` to that one `json.dumps` call, and nothing else in the file.** The
other three `json.dumps` calls in C_06 (`_write_watermark`, `_write_relationship_json`, `_write_relationship_views`) are NOT changed: across the same two runs 15,543 of
15,544 other keys held their ETag, and sorting them would rewrite every relationship key once with no content change.

**What you build:**
1. The one-argument change above in `C_06.client_mix_timeseries.py`.
2. A new test file `data/black_diamond/scripts/gold/tests/test_c06_sorted_keys_r25.py`. Read `test_c06_rolling_rederive_r23.py` in the same folder first: it loads the C_06 module
   without side effects (`_load_c06`) and shows how `s3` is stubbed. Your test calls the real `_write_mix_summary` with a stubbed S3 client that records the `Body` it is
   given. It must show: (a) the same `firm_daily` and `advisor_daily` content built in two different insertion orders (at least three advisors, three dates, the class dicts
   inside each in two different key orders) gives IDENTICAL bytes; (b) the recorded bytes parse (`json.loads`) to a dict equal to the payload; (c) the DIFFERENCE CONTROL: the
   same two insertion orders passed through `json.dumps(payload, separators=(',', ':'))` WITHOUT `sort_keys` give DIFFERENT bytes (this proves the test can tell the two
   apart); (d) `restated_through` passes through unchanged, as `None` and as a date string.
3. Nothing else. Do not touch `lib/`, `D_03`, `D_04` or any other gold script.

**Report (not a criterion):** read the readers of `mix_daily_summary.json` in `data/black_diamond/scripts/gold/` (search for `MIX_DAILY_SUMMARY` and
`mix_daily_summary`; D_03 and D_04 read it) and state, for each reader, whether it depends on the INSERTION order of `advisors` or of `firm` (for example by taking the
first element, or by writing the dict out in iteration order into a served object). Cite file:line. If any reader does, file a surprise row and say which served object's
order would change.

### ACCEPTANCE

<criterion id="SC25-e102-AC1" cell_refs="SC-e-102"><invocation>python -m pytest data/black_diamond/scripts/gold/tests/test_c06_sorted_keys_r25.py -q --tb=short</invocation><expect>passed</expect></criterion>
`SC25-e102-AC1` -- the new test passes, including the difference control (c).

<criterion id="SC25-e102-AC2" cell_refs="SC-e-102"><invocation>bash -c 'python -m pytest data/black_diamond/scripts/gold/tests/test_c06_rolling_rederive_r23.py data/black_diamond/scripts/gold/tests/test_c06_retained_unclassified_r21.py data/black_diamond/scripts/gold/tests/test_c06_retained_dates_six_class.py -q --tb=line; echo PYTEST-RC=$?'</invocation><expect>PYTEST-RC=0</expect></criterion>
`SC25-e102-AC2` -- the three sibling C_06 suites stay green (30 passed at the base, 0.9 s).

<expected_criteria>SC25-e102-AC1, SC25-e102-AC2</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-14 ~12:5xZ): AC1 FAILS as expected (the test file is absent); AC2 PASSES as expected (`30 passed`, `PYTEST-RC=0`), which is
the control that the siblings are green before your change.

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No package install and no download of any kind.** **No AWS call of any kind, read or write**: the test stubs S3. Nothing is deployed. Never push.
- **Never edit** anything outside the `<paths>` block. The ship of this change to the served script is a LATER order to a CloudOps seat under a never-widen pair; you do not
  take it, and you do not run `safe-deploy`.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id `MDPF_SECCLASS-D1-W92-S<k>`,
  `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken the difference control.

<paths>
data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py
data/black_diamond/scripts/gold/tests/test_c06_sorted_keys_r25.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R25.md</decomp_doc> (round 25), cell `SC-e-102`.
<owned_cells>SC-e-102</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC25-e102-AC1, SC25-e102-AC2. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~92/MDPF_SECCLASS.TO-SC-e102.c06-mix-summary-sorted-keys.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC25-e102-AC1,SC25-e102-AC2`.
</proof_of_spec>

**REPORT:** the exact diff of `C_06.client_mix_timeseries.py` (it must be one line), each criterion's output verbatim, the reader survey above with file:line, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE nothing is scheduled; the change ships later.
comp-iam: DECLARED-NOT-APPLICABLE no new AWS call.
comp-adversary: RUN -- a test that passes with or without the change (the difference control (c) must show the unsorted bytes differ); a reader that depends on insertion order (surveyed in the report); a change wider than one line (the issuer reads the diff at the drain). BLIND: how the ETag of every served object downstream of C_06 behaves on the first fire after the ship (the never-widen pair names the objects whose bytes move with no content change; that pair is the issuer's next act).
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-24 analysis section 4 item 3 (msg 5506); XA-20261014T113939Z-a304 follow-up; row D1-S37; DECOMP_R25. D1-S39 (a pair that ships `code/gold/lib/` names the classifier radius):
this change ships one script and no `lib/` file, and the ship pair says so.
