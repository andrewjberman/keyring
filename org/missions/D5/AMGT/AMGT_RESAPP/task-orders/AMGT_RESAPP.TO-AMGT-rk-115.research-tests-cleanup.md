# AMGT_RESAPP task order -- `AMGT-rk-115` -- round 29 test-rot cleanup: `test_fye_join` reads committed FIXTURES instead of a retired bucket (Z-S222), `test_latest_stamp_raw_pair`'s discriminating arm pins the PRE-rk-70 code by content (Z-S223), the two consumer tests import the CURRENT served overlay consumer (Z-S224), and `test_stage_derive_fye`'s December strip asserts it removed EXACTLY ONE entry (W112-S4); CODE ONLY, test files and fixtures only

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-115</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~115</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- edits five test files and adds four fixture files; arms nothing; runs no pull.
comp-iam: DECLARED-NOT-APPLICABLE -- the ONE live AWS act is AC0's READ-ONLY capture of four bronze objects (GET, sha256
  checked against the hashes in section 1) into fixture files; after this cell NO test in the directory touches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~115`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. Your first act
prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel` and tests that `org/`, `.tools/` and the
existing paths in section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~115;`. **NEVER RUN AN INSTALL. NEVER CALL BLOOMBERG. NO S3 WRITE.** Never
read, show, diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50`.

## 1. THE CELL, inlined in full -- `AMGT-rk-115` (round 29)

**The governing text, verbatim** (1.0.0_SA_CTO~Z msg 24307, 2026-09-22 15:54Z, the round-28 analysis):

> 2. Cleanup, code only:
>    - Z-S222: test_fye_join, 3 failures.
>    - Z-S223: test_latest_stamp_raw_pair, 1 failure.
>    - Z-S224: integrations/bloomberg/research/tests does not collect.
>    - W112-S4's count == 1 assert.

**THE MEASURED STATE at SITEZ `98041e1890` (the issuer ran each file alone; RE-READ at your branch HEAD before editing):**

- **Directory baseline:** `python -m pytest integrations/bloomberg/research/tests -q --continue-on-collection-errors`
  reads **4 failed, 50 passed, 2 errors** over 13 test files. Without the flag, collection STOPS on the 2 errors.

- **Z-S222, `test_fye_join.py` (3 failed, 2 passed).** Cause: the file hardcodes `BUCKET = "opal-data-research"` (`:55`),
  a RETIRED bucket (`NoSuchBucket`). The three failing tests read live S3 through `_baba_hist_rows` (`:72-84`),
  `_baba_daily_px_rows` (`:87-97`) and the inline `_landed_hist` (`:192-197`). The data they need is still landed,
  unchanged, in `opal-data-harvest` under the SAME prefixes `model_block_pull._bronze_prefix` builds (the rk-90 M1 move):

  | fixture | source key in `opal-data-harvest` | sha256 | bytes |
  |---|---|---|---|
  | `histdata_BABA_US_Equity.json` | `bloomberg/harvest/bronze/histdata/security_key=BABA_US_Equity/20260916T201821Z.json` | `4dc12dbb545aae4d580a7531d833096ae4b119c0121d7966bc0b65fa0f7b26f6` | 6728 |
  | `histdata_SAP_GY_Equity.json` | `bloomberg/harvest/bronze/histdata/security_key=SAP_GY_Equity/20260916T201948Z.json` | `f45823e82699c7e4b22462adfdd6e02301d6144ba782b069173e8859d7e37fa6` | 6595 |
  | `histdata_BA_US_Equity.json` | `bloomberg/harvest/bronze/histdata/security_key=BA_US_Equity/20260916T201824Z.json` | `5d9e1e46f4b04eff28c3850c10f5ffee74c590ce0fae33a907b4dfd8d3279323` | 5833 |
  | `histdata_daily_px_BABA_US_Equity.json` | `bloomberg/harvest/bronze/histdata_daily_px/security_key=BABA_US_Equity/20260911T073221Z.json` | `6edff15e6e7d61ef848e0a3978195ca3bf4e75c39166a6c0a7c3d00c7a9aa4d6` | 162269 |

  Each histdata object carries 10 fundamentals rows and 10 `PX_LAST` rows (measured); the daily series carries 2514
  rows. What the three tests PROVE, which stays proven: (1) the calendar-year join mispairs a non-December filer by
  more than 180 days; (2) the fiscal-period join pairs within 45 days; (4) every resolved pairing is on or before its
  period end, across three securities. Tests 3 and the companion arm are synthetic and already pass.

- **Z-S223, `test_latest_stamp_raw_pair.py` (1 failed, 5 passed): the CODE IS RIGHT; the TEST's discriminator is
  stale.** `test_head_copy_returns_the_incomplete_stamp` (`:62-110`) loads "HEAD's copy" of `model_block_pull.py` via
  `git merge-base HEAD SITEZ` (`:69-71`), on the premise its docstring states: "this move has not landed there yet".
  The move HAS landed (rk-90 M1, `e61604dffa`), so that copy is now the NEW-grammar code. It raises `RuntimeError: no
  bronze stamp found for 'raw/bloomberg/EXAMPLE US Equity/'` on the old-grammar stub. The arm's PROPERTY is "the
  pair rule discriminates: an implementation WITHOUT it returns the identity-only newest stamp `20260919T011821Z`".
  The last commit WITHOUT the pair rule is **`87ce2e5971`**, the parent of rk-70's `06296daccd`. Its `_latest_stamp(s3,
  prefix)` returns `sorted(stamps)[-1]` (measured at `87ce2e5971:integrations/bloomberg/research/model_block_pull.py:344-352`).
  Pinning the arm to that commit BY CONTENT restores the discriminator. (Note: `e803978fc3`, the pre-M1 parent,
  ALREADY carries the pair rule and would NOT discriminate.)

- **Z-S224, the directory does not collect (2 errors).** `test_consumer_wiring.py:24` and
  `test_unresolved_overlay_renders_marked.py:36` import `lib.research.print.render_pack.load_model_block`, REMOVED at
  `8fcb2e0e26` (rk-6, the print pack moved to the pool). The old function (`8fcb2e0e26^:lib/research/print/render_pack.py:97-106`)
  read `DELIVERABLES/model_block_<key>.json` and applied `render_print.load_corrected_price_overlay` +
  `apply_corrected_price_overlay`. The CURRENT served consumer of that same overlay is
  **`lib.research.api.scoped_amgt._apply_corrected_overlay(model_block, security_key)`** (`scoped_amgt.py:1087-1102`),
  whose root is `AMGT_MODEL_BLOCK_ROOT`, read at CALL time (`:160-161`). The issuer proved the composition reproduces
  the old result: with `AMGT_MODEL_BLOCK_ROOT` set to the `~1` deliverables folder, BABA FY2025 `PX_LAST` reads
  **132.23, RESOLVED, observation_date 2025-03-31**. The two files carry 5 and 4 test functions (9 in total).
  - Hazard, pre-existing: `test_unresolved_overlay_renders_marked._write_fixtures` (`:65-...`) WRITES into the tracked
    folder `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/`. It must leave those files
    BYTE-EQUAL to HEAD (AC4 checks).

- **W112-S4, `test_stage_derive_fye.py`:** `test_december_name_byte_identical_to_pin` strips `unresolved` entries whose
  mnemonic is `EQY_FUND_CRNCY`, with no count check, so a widened strip would pass silently.

- **Other baselines:** `test_stage_derive_fye` 4 passed; `test_vintage_derivation_identity` 4 passed;
  `lib/research/api/tests` 204 passed.

**RULED, what you build:**

1. **Z-S222.** Create `integrations/bloomberg/research/tests/fixtures/fye_join/` holding the four files above. Write each
   by a READ-ONLY `get_object` of its source key, VERBATIM bytes, and verify its sha256 equals the table's before
   writing (AC0's `capture.py`). In `test_fye_join.py`:
   - replace the three S3 readers with one local `_fixture(name)` loader;
   - remove `import boto3` and `BUCKET`;
   - change NO assertion, threshold or security list.
   The docstring gains one line: the data is the landed bronze captured as fixtures at the stated hashes.
2. **Z-S223.** In `test_head_copy_returns_the_incomplete_stamp`, replace the `git merge-base HEAD SITEZ` lookup with the
   fixed content pin `87ce2e5971`, and update the docstring to say why that commit ("the last commit before rk-70's
   pair rule"). Add ONE assert that the loaded copy's `_latest_stamp` source does NOT contain `_stamps_with_raw_pair`,
   so the discriminator can never silently re-pin to code that already carries the fix. Every other arm is unchanged.
3. **Z-S224.** In both consumer files, replace the removed import with a test-local helper:
   - `load_model_block(sec_key)` reads `DELIVERABLES / f"model_block_{sec_key}.json"`;
   - with `AMGT_MODEL_BLOCK_ROOT` set to `str(DELIVERABLES)` (restore the prior value afterwards), it returns
     `lib.research.api.scoped_amgt._apply_corrected_overlay(mb, sec_key)`.
   Update each docstring's "NAMES the consumer" sentence to the current served consumer. NO assertion changes.
4. **W112-S4.** In `test_december_name_byte_identical_to_pin`, count the `unresolved` entries with mnemonic
   `EQY_FUND_CRNCY` BEFORE stripping and `assert == 1`. Every other line is unchanged.

**What this cell does NOT change:** any production module (`lib/`, `integrations/**/*.py` outside `tests/`), any other
test file, any S3 object, the tracked deliverables folder `~1`.

## 2. WHERE THIS CAME FROM

**ROUND 29**, decomposition s.37 (cut by `2.0.0_SA_COO~Z`), on the CTO's round-28 analysis msg 24307, alongside L-ID
(rk-113) and its precursor rk-114. Rows Z-S222, Z-S223 and Z-S224 (@`d8996f575f`) and W112-S4.

## 3. SURFACES -- what you may read and write

<paths>
integrations/bloomberg/research/tests/test_fye_join.py
integrations/bloomberg/research/tests/test_latest_stamp_raw_pair.py
integrations/bloomberg/research/tests/test_consumer_wiring.py
integrations/bloomberg/research/tests/test_unresolved_overlay_renders_marked.py
integrations/bloomberg/research/tests/test_stage_derive_fye.py
integrations/bloomberg/research/tests/fixtures/fye_join/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~115/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-115.research-tests-cleanup.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL**, including every production module and the `~1` deliverables folder.
  Scratch is `<your worktree>/.scratch/r115/`.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~115 <0.9.0_WK_AMGT_RESAPP~115@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS

- **CODE ONLY.** The ONE live act is AC0's read-only capture. NO S3 write, no Bloomberg, no vendor call.
- **If a failure proves a PRODUCTION defect** (the code, not the test, is wrong): STOP with a BLOCKING row naming it.
  That is a scope change for the CTO.
- **Test files and directories each in their own pytest call.** **A script that carries a backslash is a FILE.**
- **THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row, never
  repaired by deleting an assertion or by editing a WALL.
- **SURPRISE ROWS:** `AMGT_RESAPP-Z-W115-S<k>`, with `disarm_owner` `2.0.0_SA_COO~Z`.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 600)

`.scratch/r115/capture.py`:
```
import boto3, hashlib, os
B = "opal-data-harvest"
D = "integrations/bloomberg/research/tests/fixtures/fye_join"
SRC = {
    "histdata_BABA_US_Equity.json": ("bloomberg/harvest/bronze/histdata/security_key=BABA_US_Equity/20260916T201821Z.json", "4dc12dbb545aae4d580a7531d833096ae4b119c0121d7966bc0b65fa0f7b26f6"),
    "histdata_SAP_GY_Equity.json": ("bloomberg/harvest/bronze/histdata/security_key=SAP_GY_Equity/20260916T201948Z.json", "f45823e82699c7e4b22462adfdd6e02301d6144ba782b069173e8859d7e37fa6"),
    "histdata_BA_US_Equity.json": ("bloomberg/harvest/bronze/histdata/security_key=BA_US_Equity/20260916T201824Z.json", "5d9e1e46f4b04eff28c3850c10f5ffee74c590ce0fae33a907b4dfd8d3279323"),
    "histdata_daily_px_BABA_US_Equity.json": ("bloomberg/harvest/bronze/histdata_daily_px/security_key=BABA_US_Equity/20260911T073221Z.json", "6edff15e6e7d61ef848e0a3978195ca3bf4e75c39166a6c0a7c3d00c7a9aa4d6"),
}
s3 = boto3.client("s3", region_name="us-east-1")
os.makedirs(D, exist_ok=True)
for name, (key, want) in sorted(SRC.items()):
    body = s3.get_object(Bucket=B, Key=key)["Body"].read()
    got = hashlib.sha256(body).hexdigest()
    print(name, "sha_match", got == want, "bytes", len(body))
    if got == want:
        open(os.path.join(D, name), "wb").write(body)
```

`.scratch/r115/ac4.py`:
```
import subprocess
base = subprocess.run(["git", "merge-base", "HEAD", "SITEZ"], capture_output=True, text=True).stdout.strip()
print("base", base[:10])
out = subprocess.run(["git", "diff", "--name-only", base, "HEAD", "--", "lib", "integrations", "infra", ".tools", "portal"], capture_output=True, text=True).stdout.split()
print("changed_code_files", sorted(out))
print("deliverables_1_dirty", subprocess.run(["git", "status", "--short", "--", "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/"], capture_output=True, text=True).stdout.strip() or "none")
tests = [f for f in sorted(out) if f.endswith(".py")]
for f in tests:
    src = open(f, "rb").read().decode("utf-8")
    compile(src, f, "exec")
    print(f, "compiles True boto3_import", "import boto3" in src)
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-115"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest integrations/bloomberg/research/tests -q -p no:cacheprovider --continue-on-collection-errors --color=no 2>&1 | tail -1 && python .scratch/r115/capture.py</invocation><expect>BEFORE any test edit: the directory baseline line D0 (measured "4 failed, 50 passed, 2 errors" at the cut); then four capture lines, each "sha_match True" with its byte count (6728, 6595, 5833, 162269). A False sha_match is a STOP and a row: the landed data moved, so the fixtures would not be the data the tests were written against</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-115"><invocation>cd "$(git rev-parse --show-toplevel)" && for t in test_fye_join test_latest_stamp_raw_pair test_consumer_wiring test_unresolved_overlay_renders_marked test_stage_derive_fye; do echo "$t $(python -m pytest integrations/bloomberg/research/tests/$t.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)"; done</invocation><expect>"test_fye_join 5 passed"; "test_latest_stamp_raw_pair 6 passed"; "test_consumer_wiring 5 passed"; "test_unresolved_overlay_renders_marked 4 passed"; "test_stage_derive_fye 4 passed" -- each 0 failed and 0 errors</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-115"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest integrations/bloomberg/research/tests -q -p no:cacheprovider --color=no 2>&1 | tail -1</invocation><expect>the directory now COLLECTS without the flag: "N passed" with N = D0's passed + D0's failed + 9 (the two files' 9 functions now collecting) -- measured 50 + 4 + 9 = 63 at the cut -- and NO "failed" and NO "error" in the line</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-115"><invocation>cd "$(git rev-parse --show-toplevel)" && env AWS_ACCESS_KEY_ID=invalid AWS_SECRET_ACCESS_KEY=invalid AWS_SESSION_TOKEN=invalid AWS_PROFILE= python -m pytest integrations/bloomberg/research/tests -q -p no:cacheprovider --color=no 2>&1 | tail -1</invocation><expect>the SAME line as AC2 -- with INVALID AWS credentials the directory still passes in full, proving no test in it touches AWS any more</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-115"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r115/ac4.py && python -m pytest lib/research/api/tests -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>"base" is your worktree's fork point from SITEZ (the round-29 issuance commit); "changed_code_files" lists ONLY files under integrations/bloomberg/research/tests/ (the five named test files and the four fixtures) -- no production module; "deliverables_1_dirty none" (the fixture-writing test left the tracked ~1 folder byte-equal); every changed .py "compiles True", and test_fye_join.py "boto3_import False"; then lib/research/api/tests "A0 passed" unchanged (measured 204)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write the instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~115/AMGT_RESAPP.TO-AMGT-rk-115.research-tests-cleanup.proof_of_spec.json`,
grade it with your worktree's `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4` (rc 0), flip the record
face's status to `complete` only if every criterion passes, commit, and report once with each file's before/after count
and the directory line. **MUTATION DISCIPLINE:** snapshot working-tree bytes before editing; never `git checkout --`,
`git stash` or `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
1. **Z-S223 is a test defect, not a code defect.** `_latest_stamp` at HEAD is right. The discriminating arm's pin rotted
   when the M1 move landed, because it used `merge-base HEAD SITEZ` as a proxy for "pre-move". The chosen pin is the
   pre-rk-70 commit, because the pre-M1 parent `e803978fc3` ALREADY carries the pair rule and would not discriminate
   (measured).
2. **Z-S224's consumer is re-pointed, not stubbed.** The served overlay consumer is now
   `scoped_amgt._apply_corrected_overlay`, so the two tests exercise the path that actually serves, which is stronger
   than a local re-composition of the two `render_print` functions.
3. **AC3 is the discriminator for "no live S3 in tests":** invalid credentials, the same pass line.
4. **Pre-existing hazard, NOT fixed here** (it is outside the ruling): `_write_fixtures` writes into the tracked `~1`
   folder on every run. AC4 bars it to byte-equal. A move to `tmp_path` is a later cell, if wanted.
5. **Disjointness:** rk-113 writes `lib/research/identity/registrations.json` plus org paths; rk-114 writes
   `lib/research/identity/{crosswalk.py,add_security.py,tests/test_crosswalk_enrich_coverage.py}` plus org paths; rk-115
   writes only `integrations/bloomberg/research/tests/**`. No file is shared, apart from the append-only channel.

<status>complete</status>
<round>29</round>
<slot>~115</slot>
<fabric>site-z</fabric>
