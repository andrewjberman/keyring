# AMGT_RESAPP task order -- `AMGT-rk-108` -- L-0b: the add-security identity pull requests and RECORDS the FIGI family, ISIN, SEDOL and the company website beside the existing LEI/CIK; a per-field error is recorded, never fatal; `security_key` stays the partition and page key; CODE ONLY, no pull

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-108</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~108</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- edits one library module and adds one test file; arms nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every Bloomberg reply is a STUB.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~108`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. Your first act
prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel` and tests that `org/`, `.tools/` and the
existing paths in section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~108;`. **NEVER RUN AN INSTALL. NEVER CALL BLOOMBERG** (no `blp_client`,
no Terminal). Never read, show, diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50`.

## 1. THE CELL, inlined in full -- `AMGT-rk-108` (round 28, the Lenovo trial's wave 0)

**The governing text, verbatim.**
- PRD v0.22 s.12 @`d0597e7e0a`, stage 1: *"identity | Bloomberg add-security, with the FIGI family, ISIN, SEDOL and LEI
  appended to its identity fields"*.
- PRD v0.22 s.12, Preconditions: *"**Identity first.** Stage 1 runs before every other stage. The working key (composite
  FIGI) is RECORDED on the crosswalk record as an attribute. `security_key` stays the partition and page key until the key
  design is ruled."*
- Andrew-direct @`6f1a72e4be` (CTO msg 24227): *"The composite FIGI is the WORKING key, for research, per the CRO's REC"*.

**THE MEASURED STATE at SITEZ `96cc4dae9d` (re-read every line at your branch HEAD before editing):**
- `lib/research/identity/add_security.py:54-59`: `IDENTITY_FIELDS = ["NAME", "EXCH_CODE", "LEGAL_ENTITY_IDENTIFIER",
  "CENTRAL_INDEX_KEY_NUMBER"]`.
- `:359`: `blp.reference_data([security_full], IDENTITY_FIELDS)`.
- `:369-374`: reads the four fields plus `__field_errors__`.
- `:386-396`: the `identity` dict, with keys `bloomberg_security`, `name`, `exchange`, `lei`, `cik`, `sec_id`, `source`,
  `registered_at` and `field_errors`.
- `lib/research/identity/crosswalk.py:560` and `:629` copy the registration's `identity` dict WHOLESALE onto the crosswalk
  record. So new identity keys reach the crosswalk with NO crosswalk change.
- Tests: `lib/research/identity/tests/test_add_security.py` **7 passed**. It pins the call argument BY NAME
  (`:190-191`, `assert_called_once_with([...], add_security.IDENTITY_FIELDS)`), so extending the list keeps it green.
- Suite: `lib/research/identity/tests` **55 passed**.

**RULED, what you build:**
1. `IDENTITY_FIELDS` gains, appended in this order:
   - `COMPOSITE_ID_BB_GLOBAL` (the composite FIGI);
   - `ID_BB_GLOBAL` (the FIGI);
   - `ID_ISIN`;
   - `ID_SEDOL1`;
   - `COMPANY_WEB_ADDRESS`.
   Leave the existing four and their order unchanged.
2. The `identity` dict gains `composite_figi`, `figi`, `isin`, `sedol` and `website`, each read with `sec_data.get(...)`
   and `None` when absent. A field Bloomberg rejects (entitlement or bad field) lands in the existing `field_errors`, and
   the name still MEASURES. Never raise on a missing identifier.
3. A module comment states that the composite FIGI is RECORDED as the working-key attribute, that `security_key` is
   unchanged, and that no code keys on the FIGI yet. Cite @`6f1a72e4be`.
4. The `MEASURED:` print line gains `composite_figi %r`. The line prints NO other new value.
5. New test `lib/research/identity/tests/test_identity_figi_fields.py`, with arms:
   - `test_identity_fields_extended_in_order`: the list is the old 4 plus the 5, in order.
   - `test_stub_reply_lands_every_new_field`: a stub `blp` returns all nine, `--as-of` is given, and there is no
     `--write-pool`. It asserts the five new identity keys by running `main` with a monkeypatched `_load_blp_client` and
     reading the registration row the dry run prints or returns. If the dry run exposes no row, test the dict-builder
     helper you factor out.
   - `test_field_error_recorded_not_fatal`: the stub returns `__field_errors__` for `ID_SEDOL1`. The name still MEASURES,
     `sedol` is None and `field_errors` carries it.
   - `test_security_key_unchanged`: the computed `security_key` for `"992 HK"` equals the value at the pin.
   - `test_crosswalk_carries_identity_wholesale`: a registration row with `composite_figi` builds a crosswalk record whose
     `identity["composite_figi"]` equals it, calling the crosswalk builder with the row, no S3 and no file write.

**What this cell does NOT change:**
- `crosswalk.py`;
- `registrations.json`;
- any S3 object;
- the key grammar;
- the adapter.
No Bloomberg call.

## 2. WHERE THIS CAME FROM

**ROUND 28**, decomposition s.36: the Lenovo trial's wave 0, ahead of L-ID (the identity pull, a later round under a pair,
CTO Q5 ruling msg 24261).

## 3. SURFACES -- what you may read and write

<paths>
lib/research/identity/add_security.py
lib/research/identity/tests/test_identity_figi_fields.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~108/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-108.identity-figi-fields.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Scratch is `<your worktree>/.scratch/r108/`.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~108 <0.9.0_WK_AMGT_RESAPP~108@opal.agent>" -F <msgfile> -- <paths>`,
  with a Write-tool message file. Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

- **CODE ONLY**: no Bloomberg, AWS or vendor call, and no write to `registrations.json`.
- **Qualified imports in tests** (W85-S1). **Run each test directory in its OWN pytest call.**
- **A script that carries a backslash is a FILE** (W84-S1).
- **The pin is `96cc4dae9d`.**
- **THE REFUSAL CLAUSE** applies: a criterion you cannot satisfy AS WRITTEN is refused with its measurement and a row.
- **COUNT BARS ARE READ AT SPAWN (AC0).**
- **SURPRISE ROWS:** `AMGT_RESAPP-Z-W108-S<k>`, with `disarm_owner` `2.0.0_SA_COO~Z`.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 600)

`.scratch/r108/ac4.py`:
```
import subprocess
out = subprocess.run(["git", "diff", "--name-only", "96cc4dae9d", "HEAD", "--", "lib", "integrations", "infra", ".tools", "portal"], capture_output=True, text=True).stdout.split()
print("changed_code_files", sorted(out))
for f in sorted(out):
    b = open(f, "rb").read()
    compile(b.decode("utf-8"), f, "exec")
    print(f, "compiles True crlf", b.count(bytes([13, 10])), "non_ascii_chars", sum(1 for ch in b.decode("utf-8") if ord(ch) > 127))
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-108"><invocation>cd "$(git rev-parse --show-toplevel)" && sed -n '54,59p' lib/research/identity/add_security.py && python -m pytest lib/research/identity/tests -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>BEFORE any edit: the four-field IDENTITY_FIELDS list; then I0 (55 passed). Record I0</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-108"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/identity/tests/test_identity_figi_fields.py -v -p no:cacheprovider 2>&1 | tail -8</invocation><expect>"5 passed" and 0 failed, with the five named arms PASSED</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-108"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/identity/tests -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>"N passed" with N = I0 + 5 and 0 failed (test_add_security.py's 7 arms still pass inside it)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-108"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r108/ac4.py</invocation><expect>"changed_code_files" lists EXACTLY lib/research/identity/add_security.py and lib/research/identity/tests/test_identity_figi_fields.py; each "compiles True crlf 0 non_ascii_chars 0"</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE

Write the instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~108/AMGT_RESAPP.TO-AMGT-rk-108.identity-figi-fields.proof_of_spec.json`.
Grade it with `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3` (rc 0 is the verdict), flip to `complete`
only if every criterion passes, commit with `--only`, and report once.

**MUTATION DISCIPLINE:** snapshot working-tree bytes to `.scratch/r108/` before editing. Never `git checkout --`, `stash`
or `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5):**
1. The Bloomberg mnemonics are the plan's (`.scratch/r28_lenovo/PLAN.md` L-0b). Their ENTITLEMENT on this Terminal is
   unmeasured, which is why a field error is recorded, not fatal. L-ID reads the real replies under its own pair (CTO Q5).
2. **No new security_key dependency** (Andrew-direct @`5c20841dd1`): the FIGI is recorded beside the key, and nothing keys
   on it.
3. The crosswalk needs no edit: `crosswalk.py:560/:629` copies `identity` wholesale. The cell proves that with a test
   rather than an edit.

<status>pending</status>
<round>28</round>
<slot>~108</slot>
<fabric>site-z</fabric>
