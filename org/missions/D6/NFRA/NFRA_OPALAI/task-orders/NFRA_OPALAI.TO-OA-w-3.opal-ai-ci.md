# NFRA_OPALAI task order -- `OA-w-3` -- S4: opal_ai checks itself, standalone and on every push

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-w-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~6</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- CI on push is an event trigger inside the product repo, not a cron, alarm or monitor.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OA-w-3` (round 1, decomposition s.2/s.3)

PRD FWD-13: someone holding ONLY the `opal_ai` repository can run its checks and they pass, and the checks also run on
every change to it (Andrew: CI lives in `opal_ai`). Build, in the nested repo:
1. **`opal/checks/run_checks.sh`**: needs nothing from the workspace, only bash, python and ruff on PATH. It runs over
   the repo it lives in, and prints one line per check with its denominator:
   - `py_compile` over every `*.py` under `opal/` (denominator: files compiled);
   - `ruff check --target-version py39` over `opal/`;
   - an ASCII rule: no non-ASCII byte in any `*.py`, `*.sh`, `*.ps1` or `*.json` under `opal/`;
   - a no-device-path rule: no `C:\Users\` / `/c/Users/` / `ajb_workspace` literal in product code under `opal/`,
     outside `*.example*` config;
   - `pytest` over any `test_*.py` under `opal/`, if present.
   Its last line is exactly `CHECKS: PASS` (exit 0) or `CHECKS: FAIL` (exit 1), naming each failing check. It finds its
   own repo root from its own location, never from a workspace path.
2. **`.github/workflows/ci.yml`**: `on: push` (all branches) and `pull_request`, one job that installs python + ruff and
   runs `bash opal/checks/run_checks.sh`. Its first real run is on the first push (G-PUSH), not here.

The repo holds a README and your files at your base. Sibling cells add product files this round; your checks must pass on
what is there and fail on a planted defect.

## 2. BOUNDS

1. **`opal_ai` is a nested repository** at `<worktree>/opal_ai`, on branch `<your worktree branch>-opal_ai`. It has no
   hooks yet. Commit your nested files with `git -C opal_ai commit --author "0.9.0_WK_NFRA_OPALAI~6
   <0.9.0_WK_NFRA_OPALAI~6@opal.agent>" -F <msgfile> -- <nested paths>`, where the msgfile is written with the Write
   tool.
2. Standing: no push, no install, no vendor call, no AWS. REFUSE a criterion you cannot meet as written, and report the
   refusal with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
opal_ai/opal/checks/run_checks.sh
opal_ai/.github/workflows/ci.yml
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~6/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_OPALAI-Z-W6-S<k>`.

## 4. PROOF OF SPEC (literal; run from your worktree root, after the nested commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-w-3"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/w3.AC1.sh; echo "exit=$?"</invocation><expect>the standalone clone's run_checks.sh prints its denominators and CHECKS: PASS -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-w-3"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/w3.AC2.sh; echo "exit=$?"</invocation><expect>rc!=0; CHECKS: FAIL; py_compile named>=1; ascii named>=1 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OA-w-3"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/w3.AC3.sh; echo "exit=$?"</invocation><expect>push=True steps_invoking_run_checks>=1 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~6/NFRA_OPALAI.TO-OA-w-3.opal-ai-ci.proof_of_spec.json`. Report once: what you changed and where, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** S4 / FWD-13. The issuer re-runs `run_checks.sh` on the merged opal_ai DEV at the cutover (the sibling
cells' files must pass it too); CI green on a real push is A13 at G-PUSH.

<status>pending</status>
<round>1</round>
<slot>~6</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
