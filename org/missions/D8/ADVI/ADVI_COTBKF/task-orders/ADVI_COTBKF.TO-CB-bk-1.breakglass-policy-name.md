# TO ADVI_COTBKF.TO-CB-bk-1.breakglass-policy-name -- round 63 CB-bk-1: the break-glass role's inline policy takes the ruled name

<to_id>ADVI_COTBKF.TO-CB-bk-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~89</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>63</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bk-1` (`decompositions/ADVI_COTBKF_DECOMP.round63.md`) |
**outcome_ref:** FWD-7 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_XB_282F_INLINE_POLICY_NAME_AND_GATE_REFUSED_LEDGER_20261011.md` (the laptop CTO's ruling), and `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf` lines 236 to 290.

**The problem.** A targeted apply of FWD-7's break-glass role stopped before any write, because the naming gate refuses a hand-typed
name: the inline policy `aws_iam_role_policy.restricted_breakglass` is named `restricted-prefix-get-put-list` at line 264. The canon's
owner fixed the naming library and RULED the name.

**Your item. You run NO terraform command and make NO AWS call. You do NOT merge your branch.**

1. Change the `name` of `aws_iam_role_policy.restricted_breakglass` to exactly `RestrictedPrefixGetPutList`. That is the ruled name;
   do not derive, shorten or re-spell it, and do NOT use the name the gate itself suggested (it carries another firm's token).
2. Change nothing else in the file: not the role, not the policy document, not the statements, not a comment outside the two lines
   immediately above the `name` line if one of them cites the old name.
3. Do NOT run `python lib/opal_naming.py generate` and do NOT edit any generated file. They are stale for other reasons and are
   another seat's to regenerate.
4. Commit. The commit runs the naming gate on your diff: report its lines verbatim. **If it REFUSES, do not override and do not
   re-spell: stop and report the refusal text.** That would be a finding about the fix, not about you.
5. Run the acceptance invocation.

### ACCEPTANCE

<criterion id="CB63bk1-AC1" cell_refs="CB-bk-1"><invocation>python -c "import re;t=open('infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf',encoding='utf-8').read();i=t.index('resource \"aws_iam_role_policy\" \"restricted_breakglass\"');b=t[i:i+400];m=re.search(r'name\s*=\s*\"([^\"]+)\"',b);print('BREAKGLASS-POLICY-NAME name=%s old_name_hits=%d'%(m.group(1),t.count('restricted-prefix-get-put-list')))"</invocation><expect>BREAKGLASS-POLICY-NAME name=RestrictedPrefixGetPutList old_name_hits=0</expect></criterion>
`CB63bk1-AC1` -- the resource's `name` is the ruled name and the old name appears nowhere in the file.

<expected_criteria>CB63bk1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, your deliverables folder and the file of this order.
- **Do NOT touch:** any other `.tf`, any registry file, any generated carrier, `lib/`.
- **No terraform command, no AWS call, no `generate`, no push, no merge.**
- **No gate override** of any kind and no `--force`.
- **Refusal clause.** If the criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row: the next
  free `ADVI_COTBKF-D2-S<k>` id read from the channel at write time, `"fabric": "dell2"`, `surfaced_at` read from the clock.

<paths>
infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round63.md</decomp_doc> (round 63), cell `CB-bk-1`.
<owned_cells>CB-bk-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB63bk1-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~89/ADVI_COTBKF.TO-CB-bk-1.breakglass-policy-name.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB63bk1-AC1` BEFORE the flip. Mechanical.
</proof_of_spec>

**REPORT:** the exact diff of the file; the `BREAKGLASS-POLICY-NAME` line; the naming gate's lines from your commit, verbatim; commits;
every gate refusal or warning, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE one name in one Terraform file; no schedule reads it.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no change to the policy document; the name of an inline policy grants nothing; BLIND: comp-iam was not run by the issuer.
comp-adversary: RUN -- the check reads the name from the resource block itself and counts the old name across the whole file; the commit-time naming gate grades the diff and a refusal stops the cell; BLIND: the apply-time naming plan limb is exercised only by the next order's plan.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: laptop `1.0.0_SA_CTO` ruling @e1267f773c (crossbox XB-20261011T082334Z-282f); `1.0.0_SA_CTO~DELL2` msgs 4474 and 4516; rows ADVI_COTBKF-D2-S95, D2-S98 and D2-S99; order CB-bj-1.
