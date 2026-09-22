# AMGT_RESAPP task order -- `AMGT-rk-114` -- the crosswalk ENRICHES an existing coverage record with a registration's identity (instead of appending a colliding second record), and `add_security` writes `registrations.json` only AFTER the crosswalk builds; CODE ONLY, the precursor to L-ID (rk-113)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-114</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~114</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- two library modules and one new test file; no cron, alarm or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act at all; every test builds the crosswalk from fixtures or local files and
  stubs the Bloomberg client and S3.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification; the declaration applies to the worker's deliverable.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~114`.** Work ONLY in the worktree named in your spawn prompt. First act: print
`git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and test that `org/`, `.tools/` and the paths in
section 3 exist (the new test file excepted); if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~114;`. **NEVER RUN AN INSTALL.** Never read, show, diff or check out branch
`wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50`.

## 1. THE CELL -- `AMGT-rk-114` (round 29, wave 1 precursor to L-ID)

**The governing text, verbatim** (PRD v0.23 s.12, preconditions): *"Identity first. Stage 1 runs before every other
stage. The working key (composite FIGI) is RECORDED on the crosswalk record as an attribute. `security_key` stays the
partition and page key until the key design is ruled."*

**THE MEASURED STATE at SITEZ `0972b8631c` (re-read at your HEAD before editing):**
- `crosswalk.build_crosswalk` (`lib/research/identity/crosswalk.py:637-704`) builds `records = coverage records +
  registered records` (`:664-667`) and REFUSES any `security_key` collision (`:673-679`).
- A registration record carries an `identity` object (`_record_for_registration`, `:487-636`, `identity` at `:560`); a
  COVERAGE record (`_record_for`, `:357-486`) carries none.
- **Lenovo `992_HK_Equity` is a COVERAGE record** in the served `crosswalk/v1/2026-09-19.json` (96 records, 89 coverage +
  7 registered), with `source_row.folder = "Lenovo 992 HK"` and NO `identity`.
- `add_security.main` (`lib/research/identity/add_security.py:337-458`): the collision pre-check (`:387-398`) PASSES when
  the existing record's folder equals `--folder`. It then makes the Bloomberg call (`:402`), lands raw bronze (`:423`),
  and `_persist_registration_and_pool` (`:168-194`) WRITES `registrations.json` FIRST (`:170`) and only then calls
  `build_crosswalk`, which RAISES on the duplicate `992_HK_Equity`. **So an L-ID run today spends the call, lands the
  bronze, dirties `registrations.json`, and writes no crosswalk -- and every later crosswalk build raises.**
- A local `build_crosswalk("2026-09-19")` at `0972b8631c` is BYTE-IDENTICAL to the served 09-19 object (96 of 96
  records equal).
- Production readers of a crosswalk record's `identity`: **0** (`lib/` and `integrations/` census; only tests read it).
  `crosswalk.resolve()` (`:833-885`) does not return `identity`.
- `lib/research/identity/tests`: **60 passed** at the cut.

**RULED, what you build:**
1. `crosswalk.py`:
   - A registrations row MAY carry `"mode": "ENRICH"`. In `build_crosswalk`, an ENRICH row whose `security_key` equals a
     COVERAGE record's `security_key` attaches the row's `identity` object to THAT record as its `identity` key, and
     adds ONE provenance line `provenance["identity"]` naming the registration (`registered_at`, `raw_source`). The row
     is NOT appended as a record.
   - An ENRICH row whose `security_key` matches NO coverage record RAISES `ValueError` naming it (never appended, never
     guessed). A second ENRICH row for the same key RAISES.
   - Rows WITHOUT `mode` behave exactly as today.
   - `denominators` gains `"enriched": <n>`. `registered` keeps counting APPENDED registrations only. Every other
     denominator is unchanged. **When there are no ENRICH rows, the serialised document is byte-identical to today's**
     (the `enriched` key is added ONLY when n > 0).
2. `add_security.py`:
   - When the pre-check finds `security_key` already on a COVERAGE record with the SAME folder, and no registrations row
     exists for it, the registration row it writes carries `"mode": "ENRICH"`. Every other path is unchanged.
   - `_persist_registration_and_pool` builds the crosswalk IN MEMORY from `rows` FIRST (`build_crosswalk(as_of,
     registrations=rows, registrations_source=reg_path)`), and writes `registrations.json` only AFTER that build
     succeeds, then the pool. **A build that raises leaves `registrations.json` byte-unchanged.**
3. New test `lib/research/identity/tests/test_crosswalk_enrich_coverage.py`, arms:
   - `test_enrich_attaches_identity_no_new_record` -- a fixture coverage doc of 3 names plus one ENRICH row for name 2:
     3 records, record 2 carries the identity, records 1 and 3 byte-equal to the build without the row.
   - `test_enrich_without_coverage_record_refuses`.
   - `test_duplicate_enrich_refuses`.
   - `test_no_enrich_rows_byte_identical` -- the real local build at `as_of="2026-09-19"` serialises to the same bytes
     as the PINNED module's build (load `crosswalk.py` from `git show 0972b8631c:...`).
   - `test_add_security_enrich_row_one_call` -- `add_security.main` with `--folder` of an existing coverage name, a
     stubbed `blp` (counting calls) and stubbed S3: exactly 1 Bloomberg call, the row carries `mode: ENRICH`, and the
     in-memory crosswalk carries the identity with the record count unchanged.
   - `test_build_failure_leaves_registrations_unchanged` -- force `build_crosswalk` to raise: `registrations.json`
     bytes (a temp copy) are unchanged.

**What this cell does NOT change:** `resolve()`, `write_pool`, the key grammar, the coverage file, `registrations.json`
itself (tests use temp copies), any S3 object. No Bloomberg call.

## 2. WHERE THIS CAME FROM

ROUND 29, decomposition s.37 (cut by `2.0.0_SA_COO~Z`). Drafting L-ID (rk-113) found that `add_security` cannot
register a name that is already a coverage record: Lenovo is one.

## 3. SURFACES

<paths>
lib/research/identity/crosswalk.py
lib/research/identity/add_security.py
lib/research/identity/tests/test_crosswalk_enrich_coverage.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~114/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-114.crosswalk-enrich-coverage.md
</paths>

- A surface not named in `<paths>` is a WALL (including `registrations.json`). Scratch is `<worktree>/.scratch/r114/`.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~114 <0.9.0_WK_AMGT_RESAPP~114@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS

- **CODE ONLY.** No Bloomberg call, no S3 write; AC0's S3 GET is the one live read.
- **One pytest call per test directory.** **A script that carries a backslash is a FILE.** **Pin: `0972b8631c`.**
- **THE REFUSAL CLAUSE** applies. **SURPRISE ROWS:** `AMGT_RESAPP-Z-W114-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 5. PROOF OF SPEC (literal; timeout 600)

`.scratch/r114/ac0.py`:
```
import json, boto3, sys
sys.path.insert(0, ".")
from lib.research.identity import crosswalk as cw
s3 = boto3.client("s3", region_name="us-east-1")
served = json.loads(s3.get_object(Bucket="opal-data-harvest", Key="crosswalk/v1/2026-09-19.json")["Body"].read())
r = [x for x in served["records"] if x["security_key"] == "992_HK_Equity"]
print("served_records", len(served["records"]), "992_records", len(r), "992_has_identity", bool(r and "identity" in r[0]), "992_folder", r[0]["source_row"]["folder"] if r else None)
print("local_rebuild_byte_equal", cw.serialise(cw.build_crosswalk(served["as_of"])) == cw.serialise(served))
```

`.scratch/r114/ac4.py`:
```
import subprocess
out = subprocess.run(["git", "diff", "--name-only", "0972b8631c", "HEAD", "--", "lib", "integrations", "infra", ".tools", "portal"], capture_output=True, text=True).stdout.split()
print("changed_code_files", sorted(out))
for f in sorted(out):
    b = open(f, "rb").read()
    compile(b.decode("utf-8"), f, "exec")
    print(f, "compiles True crlf", b.count(bytes([13, 10])), "non_ascii_chars", sum(1 for ch in b.decode("utf-8") if ord(ch) > 127))
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-114"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r114/ac0.py && python -m pytest lib/research/identity/tests -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>BEFORE any edit: "served_records 96 992_records 1 992_has_identity False 992_folder Lenovo 992 HK"; "local_rebuild_byte_equal True"; the identity suite "I0 passed" (measured 60 at the cut). Record every value</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-114"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/identity/tests/test_crosswalk_enrich_coverage.py -v -p no:cacheprovider 2>&1 | tail -9</invocation><expect>"6 passed" and 0 failed, the six named arms PASSED</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-114"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/identity/tests -q -p no:cacheprovider 2>&1 | tail -1 && python .scratch/r114/ac0.py</invocation><expect>"N passed" with N = I0 + 6 and 0 failed; then "local_rebuild_byte_equal True" again (no ENRICH row exists in the real registrations.json, so the served-shape build is unchanged)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-114"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r114/ac4.py</invocation><expect>"changed_code_files" EXACTLY lib/research/identity/add_security.py, lib/research/identity/crosswalk.py and lib/research/identity/tests/test_crosswalk_enrich_coverage.py; each "compiles True crlf 0" with non_ascii_chars equal to its value at the pin</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE

Write the instance to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~114/AMGT_RESAPP.TO-AMGT-rk-114.crosswalk-enrich-coverage.proof_of_spec.json`,
grade it with your worktree's `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3` (rc 0), flip the record
face's status to `complete` only if every criterion passes, commit, and report once. **MUTATION DISCIPLINE:** snapshot
working-tree bytes before editing; never `git checkout --`, `git stash` or `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the precursor exists because L-ID as planned would half-land (call spent, bronze landed,
`registrations.json` dirtied, no crosswalk written, every later build raising). Item 2's reorder closes that hazard for
every future registration, not only Lenovo's. `registered` keeps its meaning (appended rows); `enriched` is new and
appears only when n > 0, so the served 09-19 document's bytes are reproducible.

<status>pending</status>
<round>29</round>
<slot>~114</slot>
<fabric>site-z</fabric>
