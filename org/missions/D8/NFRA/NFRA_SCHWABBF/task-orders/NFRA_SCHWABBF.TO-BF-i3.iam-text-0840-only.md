# TO NFRA_SCHWABBF.TO-BF-i3 -- the box role's firm-prefix write entry for 08403355 only (drop 0824 and 0833; Terraform text only)

<to_id>NFRA_SCHWABBF.TO-BF-i3</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~5</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-i-3` (`decompositions/NFRA_SCHWABBF_DECOMP_R3.md`) |
**outcome_ref:** FWD-1, FWD-6 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`BF-i-3`, PRD v0.7 C-SCOPE / C-ONEWRITER / C-ALONGSIDE (IAM shape: "enumerated per master by the vendor file name's master prefix ... one statement entry per master, never a wildcard over the folder"). 0824 and 0833 keep today's keys and write the OLD prefix; only 0840 writes the firm folder `schwab/49financial/bronze/`. Andrew-direct ~16:3xZ: "I dont care about that 0824, I want the new Cottonwood accounts taken care of and the 0840 tax sma account sorted out."
This cell edits Terraform TEXT and a test. It runs no `terraform init`, `plan` or `apply`, no `aws` command.

**What exists (read first).** Round 2 (merged `95b30c139f`) added to `infra/aws/terraform/canonical-schwab-ec2/monolith-iam.tf`: three per-master PutObject entries on the firm prefix in statement `MonolithSchwabWrite` (`schwab/49financial/bronze/*/date=*/{08242234,08335338,08403355}.*`, around lines 94-96) and `schwab/49financial/bronze/*` in the `MonolithSchwabList` prefix list (around line 67), with a comment (around lines 81-86). Entries for 08242234 and 08335338 are not needed (they write the old prefix) and widen the box role for nothing.
Its test is `data/canonical/schwab/tests/test_firm_prefix_grants.py` (12 tests: 6 `iam_grants`, 5 `event_rules`, 1 fmt).

**Build.**
1. In `monolith-iam.tf` REMOVE the two firm-prefix write entries for `08242234` and `08335338`, keeping the `08403355` entry, the old per-master (old-prefix) grants untouched, the list-prefix entry, the write-only invariant (no Get, no Delete), and the comment (update it: only 0840 writes the firm folder under v0.7; the Cottonwood masters belong to the Alongside box's own role).
2. Do not touch `silver.tf` (the two event rules and the converter's firm read stay: 0840 and Cottonwood use the firm prefixes).
3. Rework the `iam_grants` tests of `test_firm_prefix_grants.py`: exactly ONE per-master firm-prefix write resource (`.../schwab/49financial/bronze/*/date=*/08403355.*`); none for 08242234 or 08335338 under the firm prefix; no bare `schwab/49financial/bronze/*` folder wildcard as a write resource; the three old per-master old-prefix write resources still present; no `s3:GetObject` or `s3:DeleteObject` on the box role. Keep the `event_rules` and fmt tests as they are.

### ACCEPTANCE

<criterion id="BF3-i3-AC1" cell_refs="BF-i-3"><invocation>python -m pytest data/canonical/schwab/tests/test_firm_prefix_grants.py -q -p no:cacheprovider --color=no -k iam_grants</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF3-i3-AC1` -- the box role's firm-prefix write entry for 0840 only, the untouched old grants, the absence of a folder wildcard.

<criterion id="BF3-i3-AC2" cell_refs="BF-i-3"><invocation>python -m pytest data/canonical/schwab/tests/test_firm_prefix_grants.py -q -p no:cacheprovider --color=no -k event_rules</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF3-i3-AC2` -- the control: the event rules and the singleton notification are as round 2 left them (5 passed at the base).

<expected_criteria>BF3-i3-AC1,BF3-i3-AC2</expected_criteria>

Dry-run at the base: AC1 `6 passed` against the three-master firm entries (control); AC2 `5 passed` (control). FIRST rewrite the `iam_grants` tests for the one-master rule and run AC1: it must FAIL against the current Terraform (it still has the 0824 and 0833 entries); only then edit.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit.
- **WORLD floor, nothing applied.** No `terraform init`, `plan` or `apply`, no `aws` command, no deploy (`terraform fmt -check` offline, if the test runs it, is fine). The apply is the NFRA CloudOps lane's act under `safe-apply` after the never-widen pair.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W5-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; read `org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md` for the highest `W5-S<k>` and use the next), and do not weaken the test to pass.

<paths>
infra/aws/terraform/canonical-schwab-ec2/monolith-iam.tf
data/canonical/schwab/tests/test_firm_prefix_grants.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R3.md</decomp_doc> (round 3), cell `BF-i-3`.
<owned_cells>BF-i-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF3-i3-AC1, BF3-i3-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~5/NFRA_SCHWABBF.TO-BF-i3.iam-text-0840-only.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF3-i3-AC1,BF3-i3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** each statement entry you removed or kept with file and line, the pytest summary lines, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- Terraform text; no schedule edit.
comp-iam: RUN -- decomposition battery scanned 2 Terraform files (monolith-iam.tf, iam.tf) and 3 enumerated masters before this cell and 1 (08403355) for the firm prefix after it; this cell is a NARROWING of the round-2 IAM edit (no widening, write-only invariant kept); BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- the round-2 entries for 0824 and 0833 widened the box role for masters that stay on the old prefix; removing them is the point.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.7 C-SCOPE, C-ONEWRITER, C-ALONGSIDE (IAM shape); decomposition round 3 cell BF-i-3; round-2 merge `95b30c139f`.
