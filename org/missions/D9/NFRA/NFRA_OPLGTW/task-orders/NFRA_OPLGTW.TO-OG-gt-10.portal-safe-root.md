# NFRA_OPLGTW task order -- `OG-gt-10` -- the gateway modules import on the host and find the trading calendar staged in the artifact

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gt-10</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-gt-10</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~90</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests only; nothing is deployed here. The release is NFRA_OPLGTW.TO-OG-ap-19 (the G3 and G6 release).
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call is added or changed; no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- a defect fix measured by the issuer (addendum R3-T.53) and confirmed by 0.7.0_AE_CloudOps~Z (row Z-S126, msg 34210).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-gt-10` (decomposition addendum R3-T.55, workstream G1-FIX, FWD-22; worker row Z-W90-S1)

All paths relative to the repo root; the gateway is `infra/aws/ec2/opal-gateway` (`GW`).

**The defect, found by the worker of OG-gt-10 (row NFRA_OPLGTW-Z-W90-S1) and re-measured by the issuer.** `GW/app/portal_models.py` line 39 and `GW/app/portal_macro.py` line 55 each set
`_REPO_ROOT = Path(__file__).resolve().parents[5]`. On the host the file is `/opt/opal-gateway/app/<module>.py`, which has 4 parents (indices 0-3), so the line raises `IndexError` AT IMPORT. Both modules are
registered by the G3 hookup (OG-pt-4, merged), so a release carrying them would not start. OG-gt-8 fixed the same line in `harvest_identity.py` and `news_typed.py` (merged on your HEAD: read `_calendar()` in
`GW/app/harvest_identity.py` and copy its shape).

**What to build.**

1. In `portal_models.py` and `portal_macro.py`: delete the `_REPO_ROOT` line and, in each module's existing `_calendar()`, search for `lib/trading_calendar.py` the way `harvest_identity._calendar()` does on your HEAD:
   the artifact root first (`Path(__file__).resolve().parent.parent`), then each ancestor from `Path(__file__).resolve().parents` in turn (iterate; never index a fixed depth); the first directory holding
   `lib/trading_calendar.py` is appended to `sys.path` and `from lib import trading_calendar` returned; none found or an ImportError returns `None`. Change nothing else (absent-reason text, `_t1_date`, `_lag`, every tool).
2. A test file `GW/tests/test_og_gt10.py` with at least two tests, `test_oggt10_ac01` (a host-shaped copy of `app/` at a shallow path under `C:/tmp` or `/tmp` with `lib/trading_calendar.py` staged beside it imports both
   modules in a subprocess; `portal_models._t1_date()` is a date and `portal_macro._calendar()` is not None) and `test_oggt10_ac02` (the same copy WITHOUT `lib/`: both modules still import and `_calendar()` is None in each).
3. Report, without editing, every other `Path(...).parents[N]` with N of 3 or more that you see in `GW/app/*.py` or `GW/ops/*.py` (the issuer's AC2 scans `app/` only; `app/gen_rivalfunds_location.py` is a by-hand generator and is exempt).

## 2. BOUNDS

- Code and tests only. No release, no deploy, no IAM or Terraform, no write to any bucket.
- Edit only the files in `<paths>`. Do not touch `tools.py`, `data_entitlement.py`, `destructive_ops.py`, `deploy-to-ec2.sh`, `harvest_press.py` or any registration.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a person's name or a full email address; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/portal_models.py
infra/aws/ec2/opal-gateway/app/portal_macro.py
infra/aws/ec2/opal-gateway/tests/test_og_gt10.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~90/`. Rows: id `NFRA_OPLGTW-Z-W90-S<k>`, fabric `site-z`,
disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gt-10"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt10.AC1.sh; echo "exit=$?"</invocation><expect>(?s)host-shaped import: portal_models OK, portal_macro OK; calendar importable yes; T-1 computable yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-gt-10"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt10.AC2.sh; echo "exit=$?"</invocation><expect>(?s)parents\[N.=3\] in shipped app modules: 0 of \d+ file\(s\) scanned \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-gt-10"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt10.AC3.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; tests defined in test_og_gt10.py [2-9]\d* \(want 2\+\); failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: both portal modules import from a host-shaped path and find the staged calendar. `AC2`: no shipped app module indexes `parents` at a depth the host lacks. `AC3`: your tests and the suites of the two modules pass.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-gt-10.portal-safe-root.proof_of_spec.json`. Validate it after your last commit with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all PASS,
and report once. Your report states the commit, the two modules' new `_calendar()` order of search, and the step-3 list of other `parents[N]` (N of 3 or more).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G1-FIX2 (addendum R3-T.55). Found by the worker of OG-gt-8 (row Z-W87-S1), re-measured by the issuer (gt10.AC2 base: 2 of 69 files). The G3 modules ride `OG-ap-19`; this fix must be merged before that release is cut.
- Pre-cut: gt10.AC1 FAIL (IndexError on both portal modules), gt10.AC2 FAIL (2 of 69), gt10.AC3 FAIL (no test file).

<status>complete</status>
<round>37</round>
<workstream>G1-FIX2</workstream>
<slot>~90</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
