# AMGT_RESAPP task order -- `AMGT-rk-111` -- L-0g (Z-S219): the SA forecast-fallback identity check compares our company name against SA's `attributes.companyName`, not `attributes.name` (the ticker); CODE ONLY, stub SA replies, no SA call

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-111</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~111</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- edits one module and adds one test file; arms nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; no SA or Bright Data call; every SA reply is a STUB.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~111`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. Your first act
prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel` and tests that `org/`, `.tools/` and the
existing paths in section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~111;`. **NEVER RUN AN INSTALL. NEVER CALL SEEKING ALPHA OR BRIGHT DATA.**
Never read, show, diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50`.

## 1. THE CELL, inlined in full -- `AMGT-rk-111` (round 28, the Lenovo trial's wave 0)

**The governing text, verbatim** (row `AMGT_RESAPP-Z-S219`):
- `one_line`: *"The SA forecast-fallback identity check compares our company name against SA's attributes.name, which is
  the TICKER; the company name is attributes.companyName. BA is wrongly refused; COST and BABA pass only by substring."*
- `spec_asserts`: *"The SA identity check confirms SA returned the same company before any SA value is used (forecast
  fallback; C-PEER-SET-SA's planned identity check)."*

**THE MEASURED STATE at SITEZ `96cc4dae9d` (re-read at your branch HEAD):**
- `integrations/bloomberg/research/sa_forecast_fallback.py:239`:
  `sa_name = sa_attrs.get("name") or sa_attrs.get("companyName") or ""`. It prefers the TICKER.
- `:242` then calls `entity_test(block_name or "", sa_name)`. `entity_test` (`:66-80`) is a symmetric jaccard of at least
  0.5 over distinctive words, OR a containment of the concatenated folded forms. The containment arm is what lets a
  ticker such as "cat" pass inside "caterpillar".
- Tests: `integrations/bloomberg/research/tests/test_forecast_fallback.py` **13 passed**. Its stub symbol replies put the
  COMPANY name into `attributes.name` (`:163`, `:194`, `:213`, `:233`, `:296`), with no `companyName`. The directory does
  not collect (2 pre-existing collection errors), so bars are per FILE.

**RULED, what you build:**
1. `:239` becomes: `sa_name = sa_attrs.get("companyName") or sa_attrs.get("name") or ""`. It PREFERS `companyName`, and
   falls back to `name` only when `companyName` is absent (the existing stub shape).
2. The fallback record gains `"sa_name_field": "companyName" | "name" | None`, naming which attribute was compared, so a
   ticker-fallback pass is visible.
3. New test `integrations/bloomberg/research/tests/test_sa_identity_company_name.py`, driving `run_fallback` with the same
   stub pattern `test_forecast_fallback.py` uses, with arms:
   - `test_companyname_preferred_over_ticker`: `{name: "BA", companyName: "The Boeing Company"}` against the block name
     "BOEING CO/THE" PASSES, and `sa_name_field == "companyName"`.
   - `test_lenovo_adr_line`: `{name: "LNVGY", companyName: "Lenovo Group Limited"}` against the block name
     "LENOVO GROUP LTD". Record the ACTUAL result. If it REFUSES, the arm asserts the refusal and a row is filed naming
     why (for example, "ltd"/"limited" token handling). The entity rule is NOT widened here.
   - `test_mismatched_company_still_refuses`: `{name: "ROG", companyName: "Rogers Corporation"}` against
     "Roche Holding AG" REFUSES.
   - `test_name_only_reply_falls_back_and_says_so`: `sa_name_field == "name"`.

**What this cell does NOT change:**
- `entity_test` itself;
- the SA field map;
- `rest_fetch.py`;
- any S3 object.

## 2. WHERE THIS CAME FROM

**ROUND 28**, decomposition s.36: the Lenovo trial's wave 0, ahead of L-SA (the ADR-line SA run, a later worded cell).

## 3. SURFACES -- what you may read and write

<paths>
integrations/bloomberg/research/sa_forecast_fallback.py
integrations/bloomberg/research/tests/test_sa_identity_company_name.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~111/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-111.sa-identity-company-name.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Scratch is `<your worktree>/.scratch/r111/`.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~111 <0.9.0_WK_AMGT_RESAPP~111@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS

- **CODE ONLY.** **Test FILES are run one pytest call each** (the directory does not collect).
- **A script that carries a backslash is a FILE.**
- **The pin is `96cc4dae9d`.**
- **THE REFUSAL CLAUSE** applies. `entity_test` is a WALL for this cell.
- **SURPRISE ROWS:** `AMGT_RESAPP-Z-W111-S<k>`, with `disarm_owner` `2.0.0_SA_COO~Z`.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 600)

`.scratch/r111/ac4.py`:
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
  <criterion id="AC0" cell_refs="AMGT-rk-111"><invocation>cd "$(git rev-parse --show-toplevel)" && sed -n '239p' integrations/bloomberg/research/sa_forecast_fallback.py && python -m pytest integrations/bloomberg/research/tests/test_forecast_fallback.py -q --color=no -p no:cacheprovider 2>&1 | tail -1</invocation><expect>BEFORE any edit: the line preferring attributes "name"; then S0 (13 passed). Record S0</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-111"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest integrations/bloomberg/research/tests/test_sa_identity_company_name.py -v --color=no -p no:cacheprovider 2>&1 | tail -7</invocation><expect>"4 passed" and 0 failed, with the four named arms PASSED (test_lenovo_adr_line asserting whichever result the entity rule actually gives, with a row filed if it refuses)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-111"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest integrations/bloomberg/research/tests/test_forecast_fallback.py -q --color=no -p no:cacheprovider 2>&1 | tail -1</invocation><expect>"S0 passed" and 0 failed: every existing fallback arm is unchanged</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-111"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r111/ac4.py</invocation><expect>"changed_code_files" lists EXACTLY integrations/bloomberg/research/sa_forecast_fallback.py and integrations/bloomberg/research/tests/test_sa_identity_company_name.py; each "compiles True crlf 0" and non_ascii_chars equal to the value at the pin</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE

Write the instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~111/AMGT_RESAPP.TO-AMGT-rk-111.sa-identity-company-name.proof_of_spec.json`.
Grade it with `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3` (rc 0), flip to `complete` only if every
criterion passes, commit with `--only`, and report once.

**MUTATION DISCIPLINE:** snapshot first. Never `git checkout --`, `stash` or `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5):**
1. The `name` fallback is kept so the 5 existing stub shapes stay green. The live SA symbol reply carries `companyName`
   (per Z-S219's measurement). `sa_name_field` makes any ticker-fallback pass visible.
2. The Lenovo ADR arm records reality rather than forcing a pass. A "Ltd" vs "Limited" refusal would be a trial finding
   for the entity rule, which is a separate cell.
3. No new security_key dependency.

<status>pending</status>
<round>28</round>
<slot>~111</slot>
<fabric>site-z</fabric>
