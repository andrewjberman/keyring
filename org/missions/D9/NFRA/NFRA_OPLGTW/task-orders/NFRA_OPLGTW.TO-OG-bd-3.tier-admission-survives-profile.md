# NFRA_OPLGTW task order -- `OG-bd-3` -- master_admin tier admission for `blackdiamond_list_fees` holds on the PROFILED branch too (CTO ruling msg 33941)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-bd-3</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-bd-3</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~67</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and offline tests only; the change reaches the host only through a later gateway release order (cut after this cell drains, behind the r30 release OG-ap-14).
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS or Graph call is added; decide() is an in-process decision and the tier is read from app/tier.py resolve_tier over the deploy-time rosters, as OG-bd-2 already does.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z's ruling msg 33941 (route (a)) on the COO's refusal of OG-mg-1 (deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_HALF_COO_OG-mg-1_20261014.md @e4beda9641).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-bd-3` (decomposition addendum R3-T.49 A2)

`infra/aws/ec2/opal-gateway/app/data_entitlement.py` `decide(tool, access, tier)` admits a `TIER_ADMITTED_TOOLS` member
(today only `blackdiamond_list_fees`) for tier `master_admin` ONLY on the no-profile branch. On the restricted
(profiled) branch, a data-grant tool passes only if the grant names it. So profiling a master_admin silently ends that
tier admission. The CTO's ruling: the `master_admin` tier keeps `TIER_ADMITTED_TOOLS` whatever the caller's profile
state.

1. **The change.** In `decide()`, on the restricted branch, a tool in `TIER_ADMITTED_TOOLS` passes when `tier` is
   `Tier.MASTER_ADMIN`. Everything else on that branch is unchanged:
   - tier admission applies whatever the profile's state, active or not (the CTO's words: "whatever the caller's
     profile state"). An inactive profile is still denied every OTHER tool;
   - every other data-grant tool still needs the grant;
   - add a fourth case to `test_ogbd3_ac01`: an inactive (revoked) profile at tier `master_admin` is allowed the tier
     tool and still denied a non-tier tool.
2. **The callers.** `tool_denial` and `visible_tools` compute the tier only when `not access.restricted` (about lines
   535 and 549). Make them compute it for a restricted caller as well when a `TIER_ADMITTED_TOOLS` member is in play,
   so the decision and the tool listing agree. The tier read stays fail-closed (any error gives None, which admits
   nobody by tier).
3. **Tests,** in `infra/aws/ec2/opal-gateway/tests/test_og_bd3.py`, offline:
   - `test_ogbd3_ac01`: a principal with an ACTIVE restricted profile whose grant does NOT name the tool, tier
     `master_admin`, is ALLOWED `blackdiamond_list_fees` by `decide()` and sees it in `visible_tools`;
   - `test_ogbd3_ac02`: the same principal at tier `standard` (or None) is DENIED it (`entitlement_denied`);
   - `test_ogbd3_ac03`: the unprofiled cases are exactly OG-bd-2's (master_admin admitted; standard or None denied),
     and a Schwab tool for a profiled master_admin still needs the grant.
4. Update `decide()`'s docstring rule list to state the new branch.
5. **(A1) Re-pin ONE assertion of OG-bd-2's suite.** `tests/test_og_bd2.py` `test_ogbd2_ac03` pins exactly the old rule
   the CTO reversed: about line 70, `assert de.tool_denial(BD, profiled_admin.principal, ge.store)["code"] ==
   "entitlement_denied"` (a profiled master_admin DENIED). Change that one line to assert `is None` (ALLOWED). Update
   the comment above it and the test's docstring to cite ruling msg 33941. Change nothing else in that file: the
   unprofiled cases and the narrow-profile `BD` denial (a profiled NON-admin) stay exactly as they are.

## 2. BOUNDS

- `app/data_entitlement.py` and the one new test file only. No release, no deploy, no grant or profile written.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/tests/test_og_bd3.py
infra/aws/ec2/opal-gateway/tests/test_og_bd2.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~67/`. Rows: id `NFRA_OPLGTW-Z-W67-S<k>`, fabric
`site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-bd-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/bd3.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*failing ids not in the baseline: 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: a profiled master_admin keeps the tier tool; a profiled non-admin does not; the unprofiled cases and OG-bd-2's
  tests are unchanged; nothing else regresses.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-bd-3.tier-admission-survives-profile.proof_of_spec.json`. Validate it after
your last commit with `python .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this order>`. Flip the ONE
`<status>` tag to `complete` only if AC1 PASSES, and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- CTO ruling msg 33941 (route (a)). Order: r30 (OG-ap-14), then this cell's release (a gateway apply order cut when this
  cell drains, naming its commit), then OG-mg-1 Phase B. OG-mg-1's halves re-sign on that base.
- Pre-cut: bd3.AC1 base FAIL as expected (`tests/test_og_bd3.py` absent). Its control limbs read OG-bd-2's tests 3 of 3
  and the family + guard suites 0 new failing ids.

- A1 (issuer, 2026-10-14 ~03:0xZ, row Z-W67-S1): `test_ogbd2_ac03` pinned the rule the CTO reversed (msg 33941), and
  `test_og_bd2.py` was missing from `<paths>`. Both are issuer defects at the cut: the cut ran the bd-2 suite as a
  control and never read what it asserted. Step 5 re-pins the one line, and the file joins `<paths>`. AC1 is unchanged:
  its bd2 limb now grades the re-pinned suite.
  Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>pending</status>
<round>37</round>
<workstream>R37-TIER</workstream>
<slot>~67</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
