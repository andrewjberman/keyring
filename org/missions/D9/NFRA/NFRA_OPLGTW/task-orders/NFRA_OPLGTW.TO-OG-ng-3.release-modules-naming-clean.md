# NFRA_OPLGTW task order -- `OG-ng-3` -- three lines in two release modules the commit-time naming gate still refuses (row NFRA_OPLGTW-Z-S161)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ng-3</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ng-3</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~111</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code, one registry data row and offline tests; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the applier's BLOCKING row NFRA_OPLGTW-Z-S161 (the OG-ap-23 release commit REFUSEs in ENFORCE) under the CTO's rulings @d97ea3ae82 section 1 (a name that is a vendor or internal identifier gets a none_owed row; no override, no rename of a vendor's identifier) and the standing naming law (a registered term is read through `lookup()` or not typed).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-ng-3` (decomposition addendum R3-T.85, workstream NAMING-RELEASE-CLEAN, FWD-22)

The release commit of `OG-ap-23` adds `app/portal_served.py` and `app/etfs_silver.py` whole against the live base, and the gate (ENFORCE, now reading `name_rulings.json`) refuses three lines in them. Fix exactly these three, no more:

1. **`infra/aws/ec2/opal-gateway/app/portal_served.py` lines 125 and 126:** `ts.Scope("mdpf", ...)` types `mdpf`, a registered scope token, as a hand-kept carrier. The first argument of `Scope` is only a LABEL used in two refusal messages (`app/typed_scope.py` lines 72 and 75: "the %s scope is served ..."). Do NOT add a `name_rulings.json` row for `mdpf` (a row is keyed by name and type, not by file, so it would admit that token in every file). Instead derive the label as `app/typed_scope.py` line 46 does for its own scope ("the last segment of the bucket name, derived, not typed"): for the found-row case `row["bucket"].rsplit("-", 1)[-1]`; for the row-absent case use the module's `TOOL` constant. Change nothing else in the module. If a test in `tests/test_og_gp1.py` asserts the literal label text `mdpf` in a refusal message, update that one assertion to the derived label (the bucket's last segment, which equals `mdpf` for the real bucket) and say so in your report.
2. **`infra/aws/ec2/opal-gateway/app/etfs_silver.py` line 313:** `_audit_over_cap(tool, "bloomberg_profile")`: the string is an internal AUDIT LABEL for the Bloomberg profile record kind; the gate grades it as `INSTANCE_PROFILE` (NEW and OUT-OF-PATTERN). It names no AWS resource. Add ONE row to `infra/logic/registry/name_rulings.json` (the same shape and indentation as the rows `OG-cl-8` added; read them): `name` `bloomberg_profile`, `type` `INSTANCE_PROFILE`, `none_owed` = "an internal audit label naming the Bloomberg profile record kind inside the etfs silver module; it names no AWS resource and mints no stored name", `evidence` = "naming-gate.py full add of app/etfs_silver.py (read 2026-10-16 by the OG-ap-23 applier, row NFRA_OPLGTW-Z-S161) graded NAMING REFUSE infra/aws/ec2/opal-gateway/app/etfs_silver.py:313 bloomberg_profile as NEW and OUT-OF-PATTERN as INSTANCE_PROFILE; the string is the over-cap audit label for the Bloomberg profile record kind (file:line as measured at HEAD). Rests on the CTO ruling org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_OPLGTW_CL7_NAMING_GATE_AND_MCPINDEX_AI_CLASSIFIED_20261016_Z.md section 1.", `owner` = "the etfs silver module (an internal label)". No `canonical`. Confirm the line number at your HEAD and write the true one in the evidence.
3. Run the full-add gate over every module the release takes whole (`ng3.AC1.sh` builds the list) before and after, keep both outputs as `W/NG3_BEFORE.txt` and `W/NG3_AFTER.txt`: AFTER prints no REFUSE.

## 2. BOUNDS

- The diff is `app/portal_served.py` (two sites, plus at most one assertion in `tests/test_og_gp1.py`) and ONE new row in `name_rulings.json`. Nothing else: no other module, no other row, no gate file, no override, no `# naming-place-override`.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print an account number or a person's name.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/portal_served.py
infra/aws/ec2/opal-gateway/tests/test_og_gp1.py
infra/logic/registry/name_rulings.json
infra/aws/ec2/opal-gateway/app/etfs_silver.py
infra/aws/ec2/opal-gateway/app/typed_scope.py
infra/aws/ec2/opal-gateway/tests/test_og_gf1.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE only `portal_served.py`, `tests/test_og_gp1.py` (one assertion at most), `name_rulings.json` (one row), the files under `W/` and the investigation file (append rows only if you hit a surprise); the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~111/`. Rows: id `NFRA_OPLGTW-Z-W111-S<k>` (continue after your last), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ng-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ng3.AC1.sh; echo "exit=$?"</invocation><expect>(?s)full-add naming gate over 17 release modules in ENFORCE: rc=0; REFUSE verdicts 0 \(want 0\); RULED verdicts \d+; NAMING-GATE: (?:PASS|WARN) \d+ graded.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ng-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ng3.AC2.sh; echo "exit=$?"</invocation><expect>(?s)name_rulings: bloomberg_profile rows 1 of 1; unique per \(name, type\) True; portal_served.py typed Scope\("mdpf"\) sites 0 \(want 0\).*gp1 and gf1 suites: pytest rc=0; passed \d+; failed 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the full-add gate over all release modules prints no REFUSE. `AC2`: the `bloomberg_profile` row exists, no typed `Scope("mdpf"...)` remains, and the two modules' test suites pass.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ng-3.release-modules-naming-clean.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hashes, the two AC lines, the line numbers, whether a test assertion changed).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream NAMING-RELEASE-CLEAN (decomposition addendum R3-T.85). Origin: `~Z`'s Phase A of `OG-ap-23` stopped at its release commit (msg 34745, row Z-S161): 23 lines. Twenty are `app/refs/partner_roster.json` and the rest of the data copies, which the issuer takes out of the release commit (the deploy script stages the roster and the registry copy at bundle time from the repo sources, like `lib/trading_calendar.py`); two are the `mdpf` label; one is `bloomberg_profile`. The `scopes.json` and `admin_gateway_breakdown.py` refusals were an environment effect of the sparse release tree (the live-read client `infra/aws/globgrph/projection_client.py` was not in its cone); the issuer told `~Z` the cone fix.
- After this merges the issuer re-GOes Phase A with a new `trunk_sha`.
- Pre-cut: ng3.AC1 base FAIL as expected (3 REFUSE); ng3.AC2 base FAIL as expected (0 rows, 2 typed sites).

- A1 (issuer, 2026-10-16 ~11:0xZ, round-close-check PROOF-BAD, row Z-W111-S16): the proof instance still carries the worker's AC1 `FAIL` row, an environment effect of its sparse tree (the gate's live-read client was not in the cone); the lane `TREE_DELIVERABLES` gives the instance to its serial alone, so the issuer cannot rewrite it. RE-SEATED slot `~111` (prior commits `a9dd9aff6c` and the worker's proof commit are inherited state): in a worktree whose cone holds `.tools/`, `lib/`, `infra/logic/`, `infra/aws/globgrph/` and `infra/aws/ec2/opal-gateway/app/`, re-run `ng3.AC1.sh` and `ng3.AC2.sh`, rewrite ONLY the AC1 acceptance row of the instance from that run (its output verbatim, the verdict the run reads; keep the former FAIL and its cause in `status_reason`; set the row's recorded `expect` to this order's current AC1 expect, which admits the gate's `WARN` summary token since `06dfc8b95c`), validate with `proof-of-spec-check.py`, flip the order `<status>` back to `complete`. No product file is touched. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>complete</status>
<status_reason>closed by the issuer 2026-10-16: the worker's AC1 FAIL was one line, admin_gateway_breakdown.py:164 (opal-data-bd), an environment effect of its sparse tree (the gate's live-read client infra/aws/globgrph/projection_client.py was not in the cone; row Z-W111-S16). The issuer re-ran ng3.AC1 in the main tree on trunk 396b0690d5: rc=0, REFUSE 0, RULED 11, 13 graded, PASS; ng3.AC2 PASS (worker and issuer).</status_reason>
<round>37</round>
<workstream>NAMING-RELEASE-CLEAN</workstream>
<slot>~111</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
