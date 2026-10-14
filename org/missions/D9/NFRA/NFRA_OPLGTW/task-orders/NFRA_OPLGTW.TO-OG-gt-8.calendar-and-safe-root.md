# NFRA_OPLGTW task order -- `OG-gt-8` -- the gateway modules import on the host and find the trading calendar staged in the artifact

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gt-8</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-gt-8</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~87</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code, a deploy-script edit and tests only; nothing is deployed here. The release is NFRA_OPLGTW.TO-OG-ap-18 (re-cut on this cell).
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call is added or changed; no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- a defect fix measured by the issuer (addendum R3-T.53) and confirmed by 0.7.0_AE_CloudOps~Z (row Z-S126, msg 34210).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-gt-8` (decomposition addendum R3-T.53, workstream G1-FIX, FWD-22)

All paths are relative to the repo root; the gateway is `infra/aws/ec2/opal-gateway` (call it `GW`).

**The defect.** `GW/app/harvest_identity.py` line 86 and `GW/app/news_typed.py` line 24 each set
`_REPO_ROOT = Path(__file__).resolve().parents[5]`. On the host the file is `/opt/opal-gateway/app/<module>.py`, which has only 4 parents,
so the line raises `IndexError` AT IMPORT and the gateway service would not start. The same line is why `lib/trading_calendar.py` never reaches the
modules: `/opt/opal-gateway` carries no `lib/` (the deploy tars only `app deploy requirements.txt identity_tool_allowlist.txt` and the dashboard bundle).

**What to build, three parts.**

1. **A safe calendar root in both modules.** Delete the `_REPO_ROOT` line (and its use) in each. In each module's existing `_calendar()`:
   try the artifact root first (the parent directory of the `app` directory, where the deploy stages `lib/`), then every ancestor of the module file
   in turn (iterate `Path(__file__).resolve().parents`; NEVER index a fixed depth). The first directory that holds `lib/trading_calendar.py` is appended to
   `sys.path` (if absent) and `from lib import trading_calendar` is returned. None found, or an ImportError, returns `None`. Do not change the text of the
   existing absent-reason strings or any other behaviour. `lib/` has no `__init__.py` and must not get one (a namespace package works).
2. **Stage the calendar in the artifact.** In `GW/deploy-to-ec2.sh`, in the packaging block just before `tar -czf "$TMP/$ART"`: create `$TMP/bundle/lib`,
   copy `"$WORKSPACE_ROOT/lib/trading_calendar.py"` into it (one `cp` line containing `lib/trading_calendar.py` and `$TMP/bundle/lib`; if the source file is
   missing, print an `ERROR:` line to stderr and `exit 1` BEFORE any upload), and add `lib` to the tar's bundle list so the line reads
   `-C "$TMP/bundle" "$DASHBOARD_BUNDLE_DIR" lib`. Edit nothing else in the script. Do NOT copy the calendar into `GW`.
3. **A test file `GW/tests/test_og_gt8.py`** with at least two tests, `test_oggt8_ac01` (a host-shaped copy of `app/` at a shallow path with `lib/trading_calendar.py`
   staged beside it imports both modules in a subprocess and `_calendar()` is not None and `_t1(cal)` is a date for `harvest_identity`) and `test_oggt8_ac02`
   (the same copy WITHOUT `lib/`: both modules still import and `_calendar()` is None, so the degradation stays reported, never raised). Use a temp dir directly under
   `C:/tmp` or `/tmp` so the path is shallow; clean it up.

## 2. BOUNDS

- Code, one deploy-script edit and tests only. No release, no deploy, no IAM or Terraform, no write to any bucket.
- Edit only the files in `<paths>`. Do not touch `tools.py`, `data_entitlement.py`, `destructive_ops.py`, `harvest_press.py` (another cell's) or any registration.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a person's name or a full email address; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/harvest_identity.py
infra/aws/ec2/opal-gateway/app/news_typed.py
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
infra/aws/ec2/opal-gateway/tests/test_og_gt8.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~87/`. Rows: id `NFRA_OPLGTW-Z-W87-S<k>`, fabric `site-z`,
disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gt-8"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt8.AC1.sh; echo "exit=$?"</invocation><expect>(?s)host-shaped import: harvest_identity OK, news_typed OK; calendar importable yes; T-1 computable yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-gt-8"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt8.AC2.sh; echo "exit=$?"</invocation><expect>(?s)bash -n rc 0; stage line 1 \(want 1\); tar names lib [1-9]\d* \(want 1\+\); a second copy of the calendar under the gateway dir 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-gt-8"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt8.AC3.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; tests defined in test_og_gt8.py [2-9]\d* \(want 2\+\); failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: both modules import from a host-shaped path and find the staged calendar. `AC2`: the deploy script stages and tars `lib/`. `AC3`: your tests and the suites of the two modules pass.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-gt-8.calendar-and-safe-root.proof_of_spec.json`. Validate it after your last commit with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all PASS,
and report once. Your report states the commit, the two modules' new `_calendar()` order of search, and anything in the deploy script you saw that may
also drop `lib/` on the host (the md5 read-back in the script names only `app/`, `deploy/` and `dashboard/`; do not edit it, report it).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G1-FIX (addendum R3-T.53). Found by the issuer at the OG-ap-18 Phase B GO; confirmed by `~Z` (Z-S126, msg 34210): exactly one such line in the ap-18 shipped code, a second in `news_typed.py` (ap-19). It is also row Z-S125's cause. The Phase B GO was held before any act.
- Pre-cut (base): gt8.AC1 FAIL (IndexError on both modules, reproduced), gt8.AC2 FAIL (no stage line), gt8.AC3 FAIL (no test file).
- The gateway app files are in lane CLOUD_OPS_OR_ETL, which the COO cannot commit: a worker order grants them.

<status>pending</status>
<round>37</round>
<workstream>G1-FIX</workstream>
<slot>~87</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
