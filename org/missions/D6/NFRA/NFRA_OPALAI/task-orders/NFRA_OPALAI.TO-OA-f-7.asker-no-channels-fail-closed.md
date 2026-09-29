# NFRA_OPALAI task order -- `OA-f-7` -- DIRECT ACT, ADDENDUM R2-A5: an asker grant with no portal channels gets no portal catalog (fail closed)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-f-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~22</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS surface is written; AC2 runs the guard suite locally with moto.
comp-adversary: DECLARED-NOT-APPLICABLE -- the two negative arms are the adversary read of the one gate this narrows.
EGRESS CLASS, declared: NONE (moto is already installed at C:/tmp/moto-target; development downloads are covered by
Andrew-direct record @f8d1103a38).
</preflight>

## 1. THE CELL -- `OA-f-7` (decomposition ADDENDUM R2-A5; CTO ruling msg 26343, on the CVO's question under row Z-W2-S1)

The gateway tool `opal_asker_query` answers a colleague's Teams question from the portal catalog, scoped to the ASKER.
`infra/aws/ec2/opal-gateway/app/asker_scope.py:384-397` applies the asker grant's `portal_channels`. But a grant with
NO `portal_channels` "does not narrow": such an asker is served the WHOLE Opal-internal catalog. The ruling: an absent
allowlist fails CLOSED, as every other entitlement axis here does.

Change `handle_asker_query`'s step (d) so that EVERY scope in play must carry a NON-EMPTY `portal_channels`: the asker's,
and in a group chat each member's. When any scope has none (key absent, or an empty list), refuse with the new code
`asker_no_portal_channels` and a plain reason ("this person's data entitlement names no portal channels, so no portal
figure can be served; ask Andrew to add the channels they need"). Audit it through the existing `audit_log`, as the
neighbouring refusals do, and fetch NOTHING. When every scope has channels, the effective set is the intersection, exactly
as today. Update the module docstring lines that say a grant without portal_channels "behaves exactly as before" or
"does not narrow".

**Tests.** Write a NEW file `infra/aws/ec2/opal-gateway/tests/test_asker_nochannels.py`, with fakes only, the same way
`tests/test_asker_binding.py` builds its fake Graph and `acs.AccessState`. It has EXACTLY these three names:
- `test_grant_without_portal_channels_denied`: an active profile whose grant has NO `portal_channels` key is refused
  `asker_no_portal_channels`, and no fetch runs;
- `test_grant_with_empty_portal_channels_denied`: the same with `portal_channels: []`;
- `test_grant_with_channels_served`: the POSITIVE control. A grant with channels, the key in a granted channel, is
  served.
Existing tests that relied on "no portal_channels means everything" (in `tests/test_asker_scope.py`,
`tests/test_asker_binding.py`, `tests/test_portal_grant.py`) get their FIXTURES updated to carry explicit channels. Never
change what an assertion asserts. Alyssa Keith's live grant carries 10 channels and is unaffected.

## 2. BOUNDS

1. Only `asker_scope.py` and the four test files change. No `data_entitlement.py`, `identity_scope.py`, `tools.py` or
   `config.py` edit, and no grant, profile or policy record is written.
2. Nothing is deployed. The release rides OA-e-3's narrow release, a separate order.
3. Standing: no push, no vendor call. REFUSE a criterion you cannot meet as written, and report the refusal with its
   measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/asker_scope.py
infra/aws/ec2/opal-gateway/tests/test_asker_nochannels.py
infra/aws/ec2/opal-gateway/tests/test_asker_scope.py
infra/aws/ec2/opal-gateway/tests/test_asker_binding.py
infra/aws/ec2/opal-gateway/tests/test_portal_grant.py
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~22/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id
`NFRA_OPALAI-Z-W22-S<k>` (none exist at the cut; the first is S1).

## 4. PROOF OF SPEC (literal; run from your worktree root, after your commits)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-f-7"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f7.AC1.sh; echo "exit=$?"</invocation><expect>named arms passed 3 of 3; failed/errored tests 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-f-7"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e1.AC3.sh; echo "exit=$?"</invocation><expect>moto from C:/tmp/moto-target: 5.2.3; passed>=10; failed=[test_ogz1_ac05 test_ogz1_ac08]; new failures=[] -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~22/NFRA_OPALAI.TO-OA-f-7.asker-no-channels-fail-closed.proof_of_spec.json`.
Report once: the changed region with file:line, the code commit hash(es) (OA-e-3's release cherry-picks exactly these),
the three arms' pytest lines, the guard-suite counts, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** a direct act on `1.0.0_SA_CTO~O`'s ruling msg 26343 (the CVO graded OA-r-1 J1 PASS @c180d84b36, which
meets G-SCOPE's condition, and asked whether a grant without channels should see the whole catalog; the CTO ruled
fail-closed). No `<round>` (the R2-A1 precedent). It ships inside OA-e-3's release, amended the same commit. AC2 reuses
the R-5 guard check (e1.AC3.sh) unchanged. Risk: gateway code under infra/, WORLD floor; nothing deploys here.

SPAWN ONLY WHEN: at the cut. Slot `~22`.

Dry-run at base (CLOUD, ~01:1xZ):
- f7.AC1 base: FAIL as expected (`tests/test_asker_nochannels.py absent`).
- e1.AC3 (AC2) base: PASS as expected (control: 10 passed, failed set exactly test_ogz1_ac05 + test_ogz1_ac08).

<status>pending</status>
<direct_act>true</direct_act>
<slot>~22</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
