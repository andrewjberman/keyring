# TO NFRA_CTLPLN.TO-CT-d-1 -- round 4 CT-d-1: the fence census -- which firm buckets admit which Dell user, N of N, and the placement map

<to_id>NFRA_CTLPLN.TO-CT-d-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~6</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~C</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-d-1` (`decompositions/NFRA_CTLPLN_DECOMP.round4.md`) | **outcome_ref:** FWD-10 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CT-d-1`, the CTO's round-4 first cell (msg 106061): "a census, read-only, of every opal-data-* bucket policy for whether each Dell user
is admitted, N of N printed". Reported on dell2 (row IRPT_BCKEND-S347): the `opal-data-inflection` bucket policy explicitly denies
`cloudops-dell2-agent-user`; "the fence admits a listed set of principals and the two Dell users are not in it, so a Dell seat cannot read
the firm data its own projects are placed on". You measure that for every bucket, and you derive which firm's bucket each Dell-placed
project uses. You change NOTHING in AWS and nothing in any `.tf` file.

The two Dell users: `arn:aws:iam::313476888478:user/cloudops-dell1-agent-user`, `...user/cloudops-dell2-agent-user`.

**Build** `infra/aws/terraform/shared-infra/tests/dell_fence_census.py`, with `--live` (default) and `--from-file <json>`:

1. **Buckets.** `s3api list-buckets` through the repo's `.tools/aws` shim; keep every bucket whose name starts `opal-data-`. Print the
   count. That count is N.
2. **Per bucket:** `s3api get-bucket-policy`. `NoSuchBucketPolicy` is the value `NO-POLICY` (no fence); any other error is
   `UNREADABLE <code>` and is counted, never treated as no fence. For a policy, find every statement with Effect `Deny` that excludes
   principals by a list (a `NotPrincipal`, or a Condition such as `ArnNotLike` / `ArnNotEquals` / `StringNotLike` / `StringNotEquals`
   on `aws:PrincipalArn` or `aws:userid`); print the admitted list's length and, for EACH Dell user, `ADMITTED` or `DENIED` by that
   statement (pattern matching as IAM does it: `*` and `?`). A bucket with a policy and no such statement is `NO-FENCE`.
3. **Cross-check by the cloud's own evaluator** for each bucket and each Dell user: `iam simulate-principal-policy` with
   `--policy-source-arn <the user>`, `--action-names s3:GetObject`, `--resource-arns arn:aws:s3:::<bucket>/x`,
   `--resource-policy <the bucket policy document>` (omit it for `NO-POLICY`); record `allowed`, `explicitDeny` or `implicitDeny`.
   Where your own reading of the fence and the evaluator disagree, print `DISAGREE <bucket> <user>` and count it.
4. **Where each fence is declared:** for each bucket, the `.tf` file and line under `infra/aws/terraform/` that declares its bucket
   policy (search for the bucket name and for the resource that builds it), or `UNDECLARED`.
5. **The placement map.** Dell-placed projects: every `org/missions/D*/*/*/project.json` with `placement` `DELL1` or `DELL2` and
   `status` not `closed`. For each, the set of `opal-data-<firm>` bucket names cited anywhere in that project's `task-orders/`,
   `prd/` and `decompositions/` files, with the count of citing files per bucket. Print one line per project: its Dell, its buckets and
   counts, or `no-bucket-cited`. Then, per Dell, the union: the buckets its projects use.
6. **The gap:** per Dell, each bucket in its union where that Dell's user is `DENIED` or the evaluator says not `allowed`. That list is
   what CT-d-2 joins.
7. Save the full result as `infra/aws/terraform/shared-infra/tests/dell_fence_census.json` (it names firm buckets, so it lives under
   `tests/`, where the repo's naming gate does not grade strings). `--from-file` re-prints from a saved listing without calling AWS.
8. LAST line:
   `FENCE-CENSUS buckets=<N> read=<r> unreadable=<u> fenced=<f> no_policy=<p> no_fence=<q> dell1_admitted=<a>/<N> dell2_admitted=<b>/<N> disagree=<d> undeclared=<x> gap_dell1=<g1> gap_dell2=<g2> ok=<True|False>`
   with `ok=True` only when `r == N`, `u == 0`, `d == 0`, and `f + p + q == N`.

### ACCEPTANCE

<criterion id="CT4d1-AC1" cell_refs="CT-d-1"><invocation>python infra/aws/terraform/shared-infra/tests/dell_fence_census.py --from-file infra/aws/terraform/shared-infra/tests/dell_fence_census.json</invocation><expect>unreadable=0</expect></criterion>
`CT4d1-AC1` -- every `opal-data-*` bucket was read and classified; the same line must read `disagree=0` and `ok=True`, stated in the
proof row. Run `--live` once first to produce the saved file (outside the 120 s bound if the listing needs it; say so).

<criterion id="CT4d1-AC2" cell_refs="CT-d-1"><invocation>python infra/aws/terraform/shared-infra/tests/dell_fence_census.py --from-file infra/aws/terraform/shared-infra/tests/dell_fence_census.json --control</invocation><expect>CONTROL admitted_principal=allowed dell_on_fenced=denied ok=True</expect></criterion>
`CT4d1-AC2` -- the control: on one fenced bucket, a principal the fence DOES admit evaluates `allowed` by the same reading and the same
evaluator call that evaluates the Dell user as denied. (`--control` makes one live `simulate-principal-policy` call for the admitted
principal; if no bucket is fenced, the line reads `CONTROL none-fenced ok=False` and you file a row.)

<expected_criteria>CT4d1-AC1,CT4d1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **Read-only.** AWS calls allowed: `s3api list-buckets`, `s3api get-bucket-policy`, `iam simulate-principal-policy`,
  `sts get-caller-identity`. No write, no object read (you never read a firm's data), no edit to any `.tf` file.
- Firm bucket names appear ONLY in files under a `tests/` directory and in your final report: not in your commit message, not in your
  proof instance, not in a surprise row (write "the fenced firm buckets" and give counts). If the commit gate refuses a string, do not
  override: file a BLOCKING row and stop.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_CTLPLN-W6-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or the
  expected value.

<paths>
infra/aws/terraform/shared-infra/tests/dell_fence_census.py
infra/aws/terraform/shared-infra/tests/dell_fence_census.json
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit: every `.tf` file under `infra/aws/terraform/`, every `project.json`, and the
Dell-placed projects' `task-orders/`, `prd/` and `decompositions/` folders.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round4.md</decomp_doc> (round 4), cell `CT-d-1`.
<owned_cells>CT-d-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CT4d1-AC1, CT4d1-AC2. Instance at `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~6/NFRA_CTLPLN.TO-CT-d-1.dell-fence-census.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CT4d1-AC1,CT4d1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines; the per-bucket table (bucket, class, admitted-list length, dell1, dell2, evaluator decisions, where
declared); the placement map per project and per Dell; the gap list per Dell; every `UNDECLARED` fence; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: RUN at the cut by the evaluator cross-check inside the census (iam simulate-principal-policy with the bucket policy as resource policy); the control criterion CT4d1-AC2 is its positive arm.
comp-adversary: RUN -- a census that reads a failed retrieval as no fence (UNREADABLE counted, never NO-POLICY); a fence form the parser does not know (the evaluator cross-check and the disagree count); a wrong-domain zero (N printed from list-buckets; a bucket not named opal-data-* is out of the declared domain and said so); cross-firm exposure by the census itself (no object read; names only under tests/); BLIND: a fence enforced somewhere other than the bucket policy (an access point, a key policy) -- the live Dell read after CT-d-2's apply is the test.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: CTO msg 106061 (a); row IRPT_BCKEND-S347 @ce0b9df49c; decomposition round 4. Base dry-run at the cut: CT4d1-AC1 and CT4d1-AC2
base FAIL as expected (the script does not exist).
