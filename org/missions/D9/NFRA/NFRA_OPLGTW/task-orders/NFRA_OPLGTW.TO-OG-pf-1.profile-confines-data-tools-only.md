# NFRA_OPLGTW task order -- `OG-pf-1` -- a profile confines only the data-grant tools (CTO ruling msg 32383; Andrew's 13 months, the Bloomberg mirror)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-pf-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-pf-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~45</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change with tests; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS surface is read or written; the state store is faked in the tests.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is 1.0.0_SA_CTO~O's ruling msg 32383 (2026-10-09 ~04:2xZ) under PRD v2.3 (org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md @4fb7326f67), item 2's any-account grant for the connected principals.
EGRESS CLASS, declared: NONE. No network request of any kind.
</preflight>

## 1. THE CELL -- `OG-pf-1` (round 33, workstream ENTITLE-R33; ships in r30)

Today, `infra/aws/ec2/opal-gateway/app/data_entitlement.py` `decide()` (line ~427) treats a principal with a RESTRICTED
profile as confined to exactly the tools its grant names: every other tool, data or not, is `entitlement_denied`
(`tests/test_data_entitlement_guard.py` `test_ogz1_ac07` pins that: 52 of 52 non-data tools denied). Only Alyssa holds a
profile today. Andrew holds none, so to give him the 13-month window a profile must be created, and under today's rule
that profile would cut him off from every non-data tool and REST route.

The CTO's ruling (msg 32383), verbatim in substance: "Unprofiled = full" is REFUSED (unknown users must still see no Schwab
tools, C2 fail-closed). Instead, `decide()` confines a profiled principal ONLY on the DATA-GRANT tool family: the five
`schwab_*` tools (`data_entitlement.py:87-94`) and the Black Diamond data tools (find them by their classification in the
same module or in `app/integrations/blackdiamond/`). Non-data tools and REST routes are never confined by a profile.

Do:
1. Name the data-grant family in ONE place in `data_entitlement.py` (the five `schwab_*` tools plus the Black Diamond data
   tools; list each by name in a frozenset with a comment).
2. Change `decide()` (and `route_denial()` if it applies the same confinement to REST routes) so that a restricted
   profile confines ONLY tools in that family: a family tool not in the grant is denied as today; a non-family tool is
   NOT denied by the profile (it proceeds to the existing gates). An UNPROFILED principal is still denied every family
   tool (unchanged). An unclassified tool is still `tool_unclassified` for everyone (unchanged).
3. **Alyssa.** Her DATA reach (the family tools, datasets, masters, operations and window her grant names) is unchanged,
   tool for tool. Under the ruling her profile no longer confines her NON-data tools; that is the ruling's consequence,
   and your report names it.
4. Update the module docstring and `decide()`'s docstring to state the new rule.
5. **Tests**, offline, new file `infra/aws/ec2/opal-gateway/tests/test_data_entitlement_family.py`, named EXACTLY
   `test_ogpf1_ac01` .. `test_ogpf1_ac04` as the header of
   `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/pf1.AC1.sh` lists them; reuse the fakes of
   `tests/test_data_entitlement_guard.py`.
6. **The pinned test.** `test_ogz1_ac07` asserts the old rule. Change ONLY its expectation for the non-data tools (now
   allowed past the profile; the family tools outside the grant still denied), and name each line. `test_ogz1_ac08`
   fails at the base already: leave it as it is and do not count it.
7. Run, each in its own process, and state totals: the new file, `test_data_entitlement_guard.py`,
   `test_schwab_query.py`, `test_admin_grants.py`, `test_entitlement_admin.py`, `test_portal_grant.py`.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~45/`.

## 2. BOUNDS

- No release, no deploy, no grant write (Andrew's profile and the Bloomberg mirror are written at r30, under halves), no
  AWS call. BUILT and HELD on your branch.
- No change to what an unprofiled principal can reach; no new tool, route or bearer.
- Fetch nothing from the internet. Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/tests/test_data_entitlement_family.py
infra/aws/ec2/opal-gateway/tests/test_data_entitlement_guard.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~45/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W45-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-pf-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/pf1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 4 of 4; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-pf-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/pf1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)test_schwab_query\.py: pytest rc=0 .*removed or renamed 0.*test_admin_grants\.py: pytest rc=0 .*removed or renamed 0.*test_entitlement_admin\.py: pytest rc=0 .*removed or renamed 0.*failures beyond the base's test_ogz1_ac08: 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the new rule's four arms (profiled keeps non-data tools; unprofiled denied data; Alyssa's data reach unchanged; one family).
- `AC2`: the query, grant and admin suites pass whole; the guard suite fails nothing new.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-pf-1.profile-confines-data-tools-only.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If both criteria PASS, edit the ONE `<status>` tag of this order IN PLACE to `complete`.
4. Report once: literal AC outputs; the diff of `data_entitlement.py`; the family's members; each pinned expectation moved,
   with its line; Alyssa's non-data consequence; every test file run with its totals; commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 33, workstream ENTITLE-R33, cut ahead of the round-32 analysis on the CTO's explicit ruling msg 32383 ("Cut it as a
  round-33 cell with tests"). The workstream tag keeps round 33's main issuance open for the analysis.
- r30 then carries this cell, OG-tg-1 (the Opal-users gate and the concierge's unscoping), and the grant writes: Andrew's
  profile at v2.2 width with 13 months, and the concierge's mirror of it.
- Pre-cut: pf1.AC1 base FAIL as expected (test file absent); pf1.AC2 base PASS as expected (query 27, admin_grants 5,
  entitlement_admin 9, none removed; guard 1 failed = test_ogz1_ac08 only).

<status>pending</status>
<round>33</round>
<workstream>ENTITLE-R33</workstream>
<slot>~45</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
