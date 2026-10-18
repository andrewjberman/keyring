# AMGT_HARVST task order -- `HVST-ch-4` -- ROUND 93, workstream DIVZ-FORM: THE FUND FORM WRITES A FORM FOR EVERY FUND OF THE CLOSED SET, WITH AN ABSENT REASON WHEN NO REPORT HOLDS IT (so no reader resolves the stale version-1 DIVZ form) (CTO ruling @162d5a6934 item 2 and the `cf-5` CTO half condition 2; round-92 analysis item 1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-ch-4.the-fund-form-writes-a-form-for-every-fund-with-an-absent-reason-when-no-report-holds-it</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ch-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~166</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and offline tests, plus READ-ONLY S3 reads of the bucket `opal-data-harvest` in the census step ONLY: the silver prefix `amgt/harvest/silver/research-report/`, the extraction objects each silver row names (`extract_key`) and the stored `amgt/harvest/gold/research-fund-form/` objects, through `lib.research.harvest.store._default_client()`; never `put`, `delete`, `copy`, `sync` or a bare `aws` call. Budget: at most 800 requests and 300 MiB in all, counted in the census's last line. NO `fund_form.write`, `gold_put`, `write_one` or `silver_append` is RUN with a real client, NO deploy, NO edit outside `<paths>`.
comp-adversary: RUN at L5 -- the adversary is a change that alters the IDVZ or PFOE documents (their object names and `content_sha256` must equal the stored version-2 objects), a `fields` shape change for a fund WITH reports (only a zero-report form gains the key), a fund set typed by hand that drifts from the token set `typed` uses, a zero-report form that carries a made-up report or skeleton, and a version bump that is not needed (it would make the stored IDVZ and PFOE forms stale again).
</preflight>

## 0. THE CELL

`lib/research/corpus/fund_form.py::write()` (line 289) writes one `research-fund-form` object per DISTINCT fund of the holding reports (`distinct_funds`). Since `HVST-cf-3`, DIVZ has no holding report, so no version-2 DIVZ form exists, and `substrate._pick_stored` for a security whose fund of record is DIVZ falls back to the STALE version-1 DIVZ object (it counts candidate and misfiled reports) with `current` False; `fund_form.read_latest("DIVZ")` raises `LookupError` and `fund_form --compare` fails on it. **The CTO ruled: DIVZ gets a version-2 form with 0 holding reports and an absent reason, so no reader resolves the stale version-1 form.** This cell changes `fund_form.py` and its tests and runs a read-only census. It writes no object; the one write is a later seat order.

## 1. THE BUILD (LOCAL, about 25 product lines)

Work in your worktree. Change only the files named in `<paths>`.
a. In `lib/research/corpus/fund_form.py`:
   - a module constant `FUNDS = ("DIVZ", "IDVZ", "PFOE")` with a comment: the closed set of fund tokens `typed._FUND_TOKEN_RE` recognises (read that pattern; do not import a private name into a public constant; a drift test holds them equal);
   - in `build(fund, items)`: when the fund is truthy and the number of its reports is 0, the returned `fields` dict gains ONE key `"absent"` with the text `no report whose silver row states fund_relation == holding names <fund>` (the fund token substituted); a fund WITH reports returns exactly the `fields` it returns today (no new key);
   - in `write()`: iterate `sorted(set(distinct_funds(...)) | set(FUNDS))` instead of `distinct_funds(...)` alone, so every fund of the closed set gets an object; everything else in `write()` stays;
   - `METHOD_VERSION` stays `"2"` (the IDVZ and PFOE documents are unchanged, so their object names and hashes are unchanged; a bump would make the stored version-2 forms stale);
   - update the module docstring (two ASCII sentences: `AMENDED round 93 (CTO ruling @162d5a6934): every fund of the closed set FUNDS gets a form; a fund no holding report names gets reports 0 and an absent reason, so no reader resolves a stale form.`) and change nothing else in the file.
b. New test `lib/research/corpus/tests/test_fund_form_zero_report.py`, offline; copy the fake client and fixtures from `tests/test_fund_form_holding_only.py` (read it first; change it only as in c). Arms: (1) a population where no holding report names DIVZ: `build("DIVZ", items)["reports"] == 0`, its `fields` has `"absent"` with the DIVZ text, empty `skeleton` and `by_class`; (2) the IDVZ and PFOE `fields` of the same population carry NO `"absent"` key and are equal to what `build` returned before this change (compute the expected dict independently in the test from the fixture); (3) `write()` through the fake client writes THREE objects (DIVZ, IDVZ, PFOE) and the DIVZ document has `inputs == []`, `reports 0`, `method_version "2"`; (4) a stored version-1 DIVZ object with inputs of 2 plus the new DIVZ object (inputs `[]`): `fund_form.read_latest("DIVZ")` returns the new one (its `inputs` equal `current_inputs("DIVZ")`, which is `[]`), and `substrate._pick_stored` for `fund=divz` returns it with `current` True; (5) `FUNDS` equals the set of tokens in `typed._FUND_TOKEN_RE.pattern` (parse the alternation in the test); (6) `METHOD_VERSION == "2"`; (7) **A MUTANT:** with `write()`'s fund set monkeypatched back to `distinct_funds` alone, arm (3) FAILS (assert that it does).
c. In `lib/research/corpus/tests/test_fund_form.py` and `test_fund_form_holding_only.py`, change ONLY what the new behaviour forces (for example a test that counts the objects `write()` puts): change that count and nothing else.
d. **The census (read-only).** Write `ch4_census.py` in your deliverables folder and run it once in the FOREGROUND with `python -u`, stdout to `ch4_census.out`. It reads the silver and the extractions as `fund_form.gather_items` does, builds every fund's document in memory with the changed code (`build_document`, `_inputs_sha16`, no write), reads the stored `research-fund-form/` objects, and prints per fund `FORM <fund> reports=<n> object=<inputs_sha16>.json content_sha256=<first 8 hex> stored=<equal|absent|different>` (`equal` when a stored object of the same name exists and its `content_sha256` equals the built one; `absent` when no stored object has that name; `different` otherwise), then exactly `CENSUS-FORMS forms=<n> idvz=<equal|absent|different> pfoe=<equal|absent|different> divz=<equal|absent|different> divz_reports=<n> gets=<requests> bytes=<bytes>`. **The issuer expects `forms=3 idvz=equal pfoe=equal divz=absent divz_reports=0`** (IDVZ `65a5baab3afd06f0.json` 82 reports and PFOE `57cee6de8b2cd85e.json` 33 reports are the stored version-2 objects). **If a count differs, DO NOT edit the expectation or the code to match: print the actual lines, add a row and report.**
e. Do not run `fund_form.write`, `_run_write`, `--write`, `gold_put` or any gold or silver writer with a real client. A surprise is a row; keep working.

<paths>
lib/research/corpus/fund_form.py
lib/research/corpus/tests/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~166/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ch-4"><invocation>python -m pytest lib/research/corpus/tests/test_fund_form_zero_report.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ch-4"><invocation>python -m pytest lib/research/corpus/tests/test_fund_form.py lib/research/corpus/tests/test_fund_form_holding_only.py lib/research/corpus/tests/test_substrate.py lib/research/corpus/tests/test_typed.py lib/research/corpus/tests/test_fund_relation.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^66 passed in</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-ch-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~166/ch4_census.out</invocation><expect>(?m)^CENSUS-FORMS forms=3 idvz=equal pfoe=equal divz=absent divz_reports=0 gets=\d+ bytes=\d+$</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-18 ~03:5xZ):** AC1 FAIL as expected (the new test file does not exist); AC2 PASS as expected (`66 passed in 0.96s` over the five files); AC3 FAIL as expected (`cat` of a file that does not exist). If your base count differs, say so with both counts and do not weaken the pattern.
- **LINE ENDINGS:** edit so `git diff --stat` reads only the lines you changed; a whole-file diff is a defect. Check `git diff --stat` before you commit.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W166-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~166/AMGT_HARVST.TO-HVST-ch-4.the-fund-form-writes-a-form-for-every-fund-with-an-absent-reason-when-no-report-holds-it.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ch-4.the-fund-form-writes-a-form-for-every-fund-with-an-absent-reason-when-no-report-holds-it` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-ch-4.the-fund-form-writes-a-form-for-every-fund-with-an-absent-reason-when-no-report-holds-it.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: the CTO's `cf-5` half (`ledger/NEVER_WIDEN_CF5_FUND_FORM_V2_CTO_HALF.md` @78b98db60d, condition 2: "DIVZ resolves to a version-2 form with 0 reports and an absent reason, or the substrate stops falling back to a stale form") and his round-92 analysis item 1 (DIVZ with the picker fix). Decomposition section 123.
- **Why the fund set is closed and typed here:** `typed._FUND_TOKEN_RE` is the one place the three funds are named; a drift test holds `FUNDS` equal to it.
- **A side effect named:** with a current DIVZ form, `fund_form.read_latest("DIVZ")` no longer raises, so `fund_form --compare` stops failing on DIVZ (C-8 of the `cf-5` pair, "do NOT run `--compare`", can lift after the DIVZ write).
- **The write is `HVST-ch-5`** (a seat order for `0.7.0_AE_CloudOps~SC1`, one object, under its own pair), after this cell merges. Its stops and expected questions go in the order before the run (CTO msg 7871).
- Slot ~166, worktree `C:/dev/wk-harvst-166`, branch `wk-AMGT_HARVST-166`. Widen the sparse set at provision with `lib/research`, `.claude/agents`, `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_CORPUS_SCAN_20260922` and `infra/aws/ec2/opal-gateway/app` (the AC2 list reads the gateway file).
- **SENT:** with the round-93 issuance.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>93</round>
<workstream>DIVZ-FORM</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
