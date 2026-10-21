# TO NFRA_FIDUPL.TO-FT-s-10 -- the G-scoped export probe (read-only, counts and hashes only)

<to_id>NFRA_FIDUPL.TO-FT-s-10</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~6</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-21</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>fidelity-r3-gexport</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FT-s-10` (`decompositions/NFRA_FIDUPL_DECOMP_R3.md` section 9) | **outcome_ref:** FWD-9 |
**depends_on:** FR-s-6, FT-s-9 (merged)

---

## WORKER FACE

### THE CELL

**FT-s-10** -- The live account list does not change when the G number is switched (31 switches, `available` 5204 every time). The CTO's ruling (msg 8990): the G number scopes the DOWNLOADS. This cell builds ONE module that proves or refutes it in one signed-in session: for the starting G and up to three other ordinals, switch, read the Export Status list for the business day, and download `account.txt` only, then print COUNTS AND HASHES ONLY so the issuer can compare them with the 5009-row file already landed. It makes read requests only and writes nothing to disk or S3.

**Read first:** `fetch.py` (`STATUS_PATH`, `DOWNLOAD_PATH`, `SIX`, `_select_rows`, `PlaywrightSession`: its `xsrf_token`, `post_json(path, body, headers)` and `get_bytes(path, params, headers)`), `gswitch.py` (`GSwitcher`: `read_form`, `switch`, `restore`), `box/paging_probe.py` (its `main()` shape: config, `run.check_pointers`, `run._real_deps`, sign-in, a `finally` that closes the session; copy that shape, do not import it), `box/run.py` (`new_york_day`, `DEFAULT_CONFIG`), `adapters.py` (`ContextRequest`).

### WHAT TO BUILD

`box/g_export_probe.py` (new, Python 3.9, ASCII) and `tests/test_g_export_probe.py` (new, fakes only):
1. `main(argv=None, deps=None)`: as `paging_probe.main` (config path argument or `run.DEFAULT_CONFIG`; `run.check_pointers`; `deps = run._real_deps(config)` when not injected; `creds = deps["read_secret"](config["wealthscape_secret_id"])`; `session = deps["open_session"](config, creds)`; `probe(...)` inside a `try`; `session.close()` in the `finally`, a close failure prints `ERROR: session close did not finish`). `day` = `run.new_york_day(datetime.datetime.now(datetime.timezone.utc))` (the day the box fetches today). Return 0 when at least one ordinal's account.txt was read, else 1. A failure prints `ERROR: probe <class name>` only.
2. `probe(context, switcher, emit, day, wanted=(0, 1, 15))`; `emit` is a one-argument print function (injectable).
   - `form = switcher.read_form()`; `start = form.current`; `options = form.options`; `start_ordinal` = the index of the option whose value equals `start` (or None). Emit `PROBE gexp count=<len(options)> start_ordinal=<int|null> day=<day>`.
   - The ordinals to test, in this order, unique and `< len(options)`: the start ordinal first (when not None), then each of `wanted`. At most four.
   - `fsession = fetch.PlaywrightSession(context)`; `headers = {"x-xsrf-token": fsession.xsrf_token()}`. For each ordinal `i`: `switcher.switch(options[i][0])` (an error emits `PROBE gexp ordinal=<i> switched=error=<class name>` and goes to the next ordinal); then post the status body exactly as `fetch.fetch_day` does (`{"iEtype": "E", "dateString": day, "startPage": "1", "pageLength": 300}` to `fetch.STATUS_PATH`); emit `PROBE gexp ordinal=<i> status=<s> elements=<n> completed_six=<how many of fetch.SIX have a COMPLETED row via fetch._select_rows> profiles=<distinct profileId count> requests=<distinct requestId count> ids_sha8=<first 8 hex of sha1 of the sorted requestIds joined by ",">`; if the `account.txt` row is among the chosen rows, `fsession.get_bytes(fetch.DOWNLOAD_PATH, {"fileName": "account.txt", "fileType": row.get("fileType"), "profileId": row.get("profileId"), "requestId": row.get("requestId")}, headers=headers)` and emit `PROBE gexp ordinal=<i> account status=<s> bytes=<n> rows=<number of non-empty lines> sha8=<first 8 hex of sha256 of the bytes> line1_sha8=<first 8 hex of sha256 of the first line's bytes>`; when it is not chosen emit `PROBE gexp ordinal=<i> account absent`. Drop the bytes right after hashing; nothing is written to disk.
   - A status 401 or 403 on ANY request emits `PROBE stop: HTTP <s>` and ends the probe at once; the `finally` then must NOT send the restore switch and emits `PROBE gexp restore=skipped`. Otherwise the `finally` calls `switcher.restore(start)` and emits `PROBE gexp restore=ok` or `restore=failed`. End with `PROBE gexp done requests=<n>`. At most 60 requests in all.
3. Never print, log or return a G number, a label, an account number, a requestId, a profileId, a cookie, a token or any response text: counts, statuses, ordinals and hashes only.
4. Tests in the NEW `tests/test_g_export_probe.py` (fakes; synthetic bytes such as `b"SYN-0001,x"` followed by a second line `SYN-0002,y`; a fake switcher and a fake context in the style of `tests/test_paging_probe.py`): `test_g_export_probe_prints_counts_and_hashes_per_ordinal_without_values` (three ordinals whose fake downloads differ show differing sha8 and rows, and the output holds no `SYN-`, no G value and no requestId), `test_g_export_probe_includes_the_start_ordinal_and_dedupes` (start ordinal 2 with wanted (0, 1, 15) tests 2, 0, 1 only when the fake has 3 options, and never one ordinal twice), `test_g_export_probe_stops_on_auth_refusal_and_skips_restore` (a 403 on the second ordinal's status post: `PROBE stop: HTTP 403`, `restore=skipped`, no restore POST), `test_g_export_probe_closes_session_and_restores_start_g` (`main` with injected fakes: `close()` once, `restore=ok`, and the start G is switched back last).

### ACCEPTANCE

<criterion id="FT-s-10-AC1" cell_refs="FT-s-10"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft10</invocation><expect>R1-FT10-OK passed=\d+</expect></criterion>
`FT-s-10-AC1` -- the four named probe tests exist and pass.

<criterion id="FT-s-10-AC2" cell_refs="FT-s-10"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fr4</invocation><expect>R1-FR4-OK passed=\d+</expect></criterion>
`FT-s-10-AC2` -- the daily-orchestration tests still pass (a regression guard: this cell must not touch `box/run.py` or `box/daily.py`).

<expected_criteria>FT-s-10-AC1,FT-s-10-AC2</expected_criteria>

Dry-run at the base: `FT-s-10-AC1` base: FAIL as expected; `FT-s-10-AC2` base: PASS as expected.

## BOUNDS

- **Grant.** The `<paths>` block below, this order's file and your deliverables folder.
- **Fakes only.** No network, no AWS, no live call from your tests. No G number, account number or firm label in any output.
- **Do not edit** `fetch.py`, `gswitch.py`, `adapters.py`, `box/run.py`, `box/daily.py` or `box/paging_probe.py`: import from them. Another worker is editing `box/paging_probe.py` and `tests/test_paging_probe.py` at the same time.
- **Refusal clause.** A premise that fails is a surprise row (`NFRA_FIDUPL-D1-W6-S<k>`, next unused), never a guess.
- **ASCII and Python 3.9 syntax** in every file. The whole module suite must have no failure: its last line goes in your report.

<paths>
infra/aws/ec2/canonical-fidelity/box/g_export_probe.py
infra/aws/ec2/canonical-fidelity/tests/test_g_export_probe.py
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R3.md</decomp_doc> (round 3, section 9 addendum), cell `FT-s-10`.
<owned_cells>FT-s-10</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FT-s-10-AC1, FT-s-10-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~6/NFRA_FIDUPL.TO-FT-s-10.g-export-probe.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FT-s-10-AC1,FT-s-10-AC2` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** what was built and where, the test names, each check line verbatim, the module suite's last line, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched; denominator 0 schedules changed.
comp-iam: DECLARED-NOT-APPLICABLE -- fakes only; denominator 0 IAM statements changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- build on fakes; the live run is ordered separately (TO-FT-s-8, amended) under the CTO's go (msg 8990), one sign-in.
lane: the paths block.
</preflight>

Source: CTO msg 8990; CloudOps row D1-S13 and the step 2P-v2 probe record; fetch.py as merged.
