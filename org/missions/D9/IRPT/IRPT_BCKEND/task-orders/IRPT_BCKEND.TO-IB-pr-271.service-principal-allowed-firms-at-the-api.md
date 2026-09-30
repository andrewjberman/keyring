# TO IRPT_BCKEND.TO-IB-pr-271 -- The served boundary refuses a service principal's selected firm outside its allowedFirmIds, in every bundle that ships it

<to_id>IRPT_BCKEND.TO-IB-pr-271</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~98</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-30</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>27</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO RULING 103318 (row S238) and ROUND-26 ~P ANALYSIS ruling 6
(`org/missions/D9/IRPT/IRPT_BCKEND/ledger/ROUND_ANALYSIS.round26P.md` @7c9ed807bb); issuer rule CTO 103370 (deployed-layout criterion);
2.0.0_SA_COO~Y's patch candidate `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/API_ALLOWED_FIRMS_PATCH_CANDIDATE_FOR_P_20260930.md`
@4a3cabe67d | **Decomp cell:** `IB-pr-271` (decomposition section 25) | **outcome_ref:** FWD-3 CONSTRAINT (an account outside the
permitted population is never silently granted) | **depends_on:** none

---

## WORKER FACE

**The cell.** In `infra/aws/lambda/investor-reporting/_authz/served.py`, `Entry.handle` step 2 (about lines 924-960) lets an INTERNAL
subject select ANY registry firm: `selected != verified` -> `bucket_for(selected)` -> `verified = selected`. The durable service
principal `svc-irpt-analysis` (profile row `userType service`, `allowedFirmIds "cottonwood"`) is internal (firm `opal-capital`), so on
2026-09-30 16:2xZ it was served an Inflection directory entry (row S238). Add ONE refusal to that branch: a SERVICE subject whose
profile row restricts `allowedFirmIds` is refused `FIRM_BINDING` for any selected firm outside the list. Nothing else changes.

**The shape (read ~Y's candidate first; this face fixes two points it leaves open):**
- Insert, between `bucket_for(selected)` and `verified = selected`:
  `if trusted.get("x-user-type", "").strip().lower() == "service":` -> `allowed = self._service_allowed_firms(trusted.get("x-user-email", ""))`
  -> `if allowed is not None and selected not in allowed: return refuse(operation or self.function_name, None, "FIRM_BINDING")`.
- `Entry.__init__` gains the keyword `load_service_profile=None` (callable `email -> row dict | None`, may raise). `_service_allowed_firms`
  uses it when given; when `None` (production) it reads the maintained profile row with
  `from canonical_profile_reads import CanonicalProfileReaders` (lazy, inside the method) and `CanonicalProfileReaders(<a DynamoDB client>).get_user(email)`
  -- read `infra/aws/lambda/investor-reporting/_scope/canonical_profile_reads.py` for the constructor and `get_user`, and
  `infra/aws/lambda/investor-reporting/ycharts/generate/current_authority.py` `allowed_firm_ids` for the parsing it must mirror exactly.
  Returns `None` when the attribute is absent or `"ALL"` (unrestricted), the stripped list otherwise (string with commas or a list),
  and `[]` when the read raises (fail closed, which the caller turns into `FIRM_BINDING`).
- **THE DEPLOYED-LAYOUT TRAP (why this order exists as written).** Seven Lambda bundles ship `served.py` (`infra/aws/lambda/ci/lambda-source-map.json`
  `files`): irpt-performance-adapter, irpt-directory-search, irpt-narrative, irpt-ycharts-generate, irpt-export-render, irpt-holdings,
  irpt-status. Only the first and the fourth ship `canonical_profile_reads.py` today. The lazy import is exempt from
  `import-closure-check.py` by design, and the catch-all makes a missing module read as "restricted to nothing" -- so ~Y's patch as
  written would refuse EVERY service principal on every firm in the other five bundles, including directory-search (the S238 route),
  and no gate would say so (measured at the cut: a scratch copy with the patch and the map unchanged fails exactly those five). So in
  `lambda-source-map.json`, for every function whose `files` ships `served.py`, add `canonical_profile_reads.py` and its top-level
  closure (`maintained_sources.py`, `ids.py`) to `files` where absent, with `staged_from` rows mirroring the irpt-performance-adapter
  entry's rows for the same three files (`repo_path`, `packaged_as`, `pin` = the commit that carries the bytes, `sha256` of those bytes).
- A unit test beside the others, `infra/aws/lambda/investor-reporting/_authz/tests/test_service_allowed_firms.py`, with the four arms of
  ~Y's candidate (hygiene at the drain; the criteria below are the grade).
- **No build, no upload, no apply.** The served move of the seven functions is the issuer's, under a packet and both halves.

<criterion id="P27-1-AC1" cell_refs="IB-pr-271"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r27/p27_1_ac1_service_allowed_firms.py" .</invocation><expect>P27-1-AC1 PASS</expect></criterion>
`P27-1-AC1` -- drives the real `Entry.handle` with `load_service_profile` injected: two harness controls (a non-internal subject is
refused; an internal user subject reaches `deps(<selected>)`), then six arms: allowed firm admitted; foreign firm FIRM_BINDING;
attribute absent admitted; `"ALL"` admitted; profile read raising FIRM_BINDING; a list admitting its second firm. "Admitted" means the
boundary called `deps(<selected>)`. Base: FAIL (Entry does not accept load_service_profile), controls passing; a scratch copy with a
minimal patch PASSES (measured at the cut).

<criterion id="P27-1-AC2" cell_refs="IB-pr-271"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r27/p27_1_ac2_deployed_layout.py" .</invocation><expect>P27-1-AC2 PASS</expect></criterion>
`P27-1-AC2` -- the deployed-layout criterion (CTO 103370): for every bundle in the source map that ships `served.py`, the bundle's own
file list is materialized into a clean directory and a fresh isolated interpreter imports `served` and every module the new branch
imports. Base: FAIL (no service-profile reader); patch alone: FAIL on 5 of 7 bundles; patch plus the closure in every bundle: PASS
(both measured at the cut on a scratch copy).

<expected_criteria>P27-1-AC1,P27-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Every other `_authz`, `_scope` and
  `_ids` module is READ only.
- **No AWS write of any kind.** No build-and-upload, no Terraform.
- **Refusal clause.** If a bundle cannot carry the closure without editing a file outside the grant, stop on that bundle, write the
  reason in a surprise row (`IRPT_BCKEND-W98-S<k>`), and do not weaken a check.

<paths>
infra/aws/lambda/investor-reporting/_authz/served.py
infra/aws/lambda/investor-reporting/_authz/tests/test_service_allowed_firms.py
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r27/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 25 (round 27, workstream ~P), cell `IB-pr-271`.
<owned_cells>IB-pr-271</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: P27-1-AC1, P27-1-AC2. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~98/IRPT_BCKEND.TO-IB-pr-271.service-principal-allowed-firms-at-the-api.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> P27-1-AC1,P27-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hashes, each criterion's last line, the seven bundles' import lines from P27-1-AC2, and any
surprise row id (`IRPT_BCKEND-W98-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule, trigger or cron is created or moved; the cell edits one boundary module, one test and the build map.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: 0 roles touched; the profile read uses the grant irpt-ycharts-generate and irpt-performance-adapter already exercise, and the five other functions' roles are read at the served move (the packet names each function's profile-table grant).
comp-blast: RUN -- denominator: 7 of 7 functions whose source-map files ship served.py; the change refuses only a service subject selecting outside its list; non-service internal subjects, non-internal subjects and service rows without the attribute are unchanged (arms C, D, H2).
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route added, removed or re-pointed; the refusal is inside every existing route's boundary.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface.
comp-adversary: RUN -- P27-1-AC1 base FAIL with both harness controls passing; minimal-patch scratch copy PASS (6 arms). P27-1-AC2 base FAIL; patch-only scratch FAIL on 5 of 7 bundles (directory-search, export-render, holdings, narrative, status); patch + closure PASS 7 of 7.
lane: the <paths> block IS the grant.
</preflight>
