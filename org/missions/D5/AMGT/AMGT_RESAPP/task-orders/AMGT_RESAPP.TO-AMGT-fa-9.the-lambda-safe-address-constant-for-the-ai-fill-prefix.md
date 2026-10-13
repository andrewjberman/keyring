# AMGT_RESAPP task order -- `AMGT-fa-9` -- THE LAMBDA-SAFE ADDRESS CONSTANT `AI_FILL_GOLD_PREFIX` IN THE GENERATED PREFIXES MODULE (FWD-41; A GENERATOR ENTRY)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-fa-9</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~428</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-fa-9.the-lambda-safe-address-constant-for-the-ai-fill-prefix</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled; a library module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, grant, key or policy is touched; the order edits an infrastructure-tree generator script and regenerates a constants module, and applies nothing. The function role's S3 read on the new prefix is read by the issuer with `comp-iam` before any store write (decomposition s.5).
comp-adversary: RUN at the cut -- `check_fa9_prefix.py` is a prepared acceptance check (8 arms: the new constant equals the builder's table prefix, the five existing constants and the registry hash unmoved, the module still GENERATED and import-free, the generator's own `--check`, `compute()` at six entries, the sources tuple unchanged, the neighbouring test pinning the constant); at the base 3 of 8 arms FAIL and the five control arms PASS (5 of 8), the build check failing as expected.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-428` (branch `wk-AMGT_RESAPP-428`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-428`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-fa-9` (round 104, workstream AIFILL, decomposition `org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md`)

FWD-41's serve reads one S3 object per name. CLAUDE.md rule 30: every S3 address is `lib/opal_naming.py address()` output, never typed. The Lambda adapter reads new-grammar prefixes ONLY from the generated module `lib/research/api/_harvest_prefixes.py` (it never imports `lib.opal_naming`: read the header of that module and of `infra/aws/terraform/harvest/gen_harvest_prefixes.py` first). So the address needs ONE new generated constant. You make that one change, the established route, and nothing else; the serve (another cell) will read the constant.

1. In `infra/aws/terraform/harvest/gen_harvest_prefixes.py` add ONE entry to the dict `compute()` returns: `"AI_FILL_GOLD_PREFIX": _table_prefix("amgt", _SCOPE, "gold", "ai_fill"),`. Touch nothing else in the file (`_SOURCES` stays the same four sources; `scoped_registry_hash` stays as it is).
2. Regenerate the module with `python infra/aws/terraform/harvest/gen_harvest_prefixes.py --write` (the file is GENERATED and marked DO NOT EDIT: never edit it by hand). The value it writes is `amgt/harvest/gold/ai_fill/`; the registry hash must stay `fff9a273a59bc232addcd45968cfaca55832266e74e288512d5c61817d7c225e` and the five existing constants must not move (no registry row changes).
3. In `lib/research/api/tests/test_harvest_prefixes.py` add the same constant to the dict `_fresh_constants()` returns: `"AI_FILL_GOLD_PREFIX": _table_root("amgt", "harvest", "gold", "ai_fill"),` (that test re-derives each constant from `lib.opal_naming` and compares it to the committed module).
4. Run the two criteria below.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W428-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS


1. Write ONLY `infra/aws/terraform/harvest/gen_harvest_prefixes.py` (the one `compute()` entry), `lib/research/api/_harvest_prefixes.py` (only by running the generator's `--write`) and `lib/research/api/tests/test_harvest_prefixes.py` (the one `_fresh_constants()` entry). No other file.
2. You never deploy, never `terraform apply`, never run the build-and-upload script, never write S3.
3. Python 3.9 syntax, ASCII-only; run `bash .tools/commit-gate.sh` on the generator and the test before you commit (the generated module is checked by `--check`).

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/gen_harvest_prefixes.py
lib/research/api/_harvest_prefixes.py
lib/research/api/tests/test_harvest_prefixes.py
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-fa-9"><invocation>cd C:/dev/wk-resapp-428 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/checks/check_fa9_prefix.py" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `AIFILL FA-9 ARMS: YES (N of N)` with N equal to 8, no `FAIL` arm line above it; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-fa-9"><invocation>cd C:/dev/wk-resapp-428 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python -m pytest -q --color=no -p no:cacheprovider lib/research/api/tests/test_harvest_prefixes.py | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the last non-empty line before `exit=` reads `N passed` (N at least the count your test module's functions define) with no `failed` and no `error` in the last 3 lines; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~428 <0.9.0_WK_AMGT_RESAPP~428@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~428/AMGT_RESAPP.TO-AMGT-fa-9.the-lambda-safe-address-constant-for-the-ai-fill-prefix.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- each criterion's deciding output line (verbatim) and the arm count;
- the arm lines of AC1 that read FAIL, if any, the pytest summary line, and the generated constant's value.
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** WORLD class because its `<paths>` name an infrastructure-tree script (the L6 gate's inferred floor; the first cut of this change rode inside the serve order at LOCAL and was refused). It applies nothing: the exercised read for the WORLD class is the generator's own `--check` plus the neighbouring test's byte comparison against fresh `lib.opal_naming` output, run by the issuer at the drain, and the CTO's read at the round close. The constant is the rule-30 route for the serve (`AMGT-fa-7`, staged behind this order); the S3 write that fills the address is a separate never-widen act (decomposition s.5).

<status>pending</status>
<status>complete -- 2026-10-13T22:5xZ by the issuer (2.0.0_SA_COO~R2): wk-AMGT_RESAPP-428 @f56dbd91a5 merged @957b04a764, proof instance VALID (rc=0). AC1 PASS (`AIFILL FA-9 ARMS: YES (8 of 8)`, re-run by the issuer in the worker's tree, same line), AC2 PASS (6 passed). Issuer re-read: `gen_harvest_prefixes.py --check` byte for byte, registry hash fff9a273 unmoved, the diff is the three lines the face names (generator entry, regenerated constant `AI_FILL_GOLD_PREFIX = 'amgt/harvest/gold/ai_fill/'`, the test pin). Row W428-S1 is an OBSERVATION (the check prints failure text as detail on two PASS arms; verdict and exit code are right); not graded here.</status>
<round>104</round>
<workstream>AIFILL</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~428</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
