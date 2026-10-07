# TO NFRA_CTLPLN.TO-CT-d-1 -- round 4 CT-d-1: the fence census -- which firm buckets admit which Dell user, N of N, and the placement map

<to_id>NFRA_CTLPLN.TO-CT-d-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~6</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>in_progress</status>
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

<expected_criteria>CT4d1-AC1,CT4d1-AC2,CT4d1-AC3</expected_criteria>

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

## AMENDMENT (2.0.0_SA_COO~C, 2026-10-07 ~19:4xZ) -- REOPENED: the census reads a SCOPED admission as what it is

The issuer reopens its own order (`complete` -> `in_progress`); the slot is re-seated in a fresh worktree; the earlier commits are
inherited state on the trunk. Since this census was built the fences gained scoped rows: a registry row carrying `actions` and
`prefix` admits its principal through the fence and confines it, by three Deny statements, to get, list and bucket-location under
one prefix (cell CT-d-2, applied today for the dell1 user on three buckets, order NFRA_CTLPLN.TO-APPLY-8). The census grades
agreement between "the policy admits this principal" and "the evaluator lets it read an object in the bucket"; for a scoped
admission those two differ BY DESIGN, so the live census now reads (issuer's run, ~19:2xZ):
`FENCE-CENSUS buckets=24 read=24 unreadable=0 fenced=3 no_policy=11 no_fence=10 dell1_admitted=24/24 dell2_admitted=24/24 disagree=3 undeclared=2 gap_dell1=1 gap_dell2=0 ok=False`
with three `DISAGREE ... dell1 reading=ADMITTED evaluator=explicitDeny` rows. The applier reported it unsmoothed (msg 106522);
the CTO had already asked for a cell "to make the census print scope" (msg 106482). Note also `gap_dell1=1` beside
`dell1_admitted=24/24`: read what `gap` counts and say whether it is now stale. Gate limb: none graded this modification.

1. FIRST, read `dell_fence_census.py` and write, in a short section at the top of your report, exactly what `reading`,
   `evaluator`, `disagree`, `gap_*`, `undeclared` and `ok` each mean in the code today, and which of them a scoped admission
   breaks. Decide for each whether the disagreement is the instrument's assumption or a real fault; if you find a real fault in
   a live policy (for example a scoped principal allowed OUTSIDE its prefix), STOP, change nothing, file a BLOCKING row and report.
2. THE REPAIR, all derived from the registry (`infra/logic/registry/exemptions.json`), nothing typed: a principal whose row for a
   bucket carries `actions` and `prefix` is read as `SCOPED`, a third value beside ADMITTED and not admitted. For a SCOPED pair the
   evaluator arms are: get UNDER the row's prefix -> allowed; get OUTSIDE it -> explicitDeny; put under it -> explicitDeny. It
   AGREES only when all three read so; any other result is a `DISAGREE` row naming the arm that differed (so a scoped principal
   that can write, or read outside its prefix, makes the census fail, which is the point of having it). An unscoped pair keeps
   today's meaning exactly. A registry row that says scoped where the LIVE policy holds no `DenyScopedExemption` statement for
   that principal is a `DISAGREE` (declared scoped, admitted whole).
   The last line gains `dell1_scoped=<n> dell2_scoped=<n>` and `dellN_admitted` counts FULL admission only, so today it reads
   `dell1_admitted=21/24 dell1_scoped=3`. `gap_*` is recomputed on that basis; say what it then reads and why.
3. `--from-file` must still read the committed `dell_fence_census.json`; re-take that file `--live` so it holds the three buckets'
   CURRENT policies (it is the saved copy other checks simulate against), and say in your report that you re-took it and what
   changed in it (statement counts per bucket). The `--control` arm must still pass.
4. Negative controls in a new `--selftest` verb, on scratch copies in memory (no AWS write): a scoped row whose live policy lacks
   the three statements -> DISAGREE; a policy whose scoped Deny omits the put arm -> DISAGREE naming put; an unscoped admitted
   principal -> unchanged reading. LAST line `FENCE-CENSUS-SELFTEST cases=<k>/<n> ok=<True|False>`.

**ACCEPTANCE.** CT4d1-AC1 and CT4d1-AC2 are unchanged and must still pass. One criterion is ADDED:

<criterion id="CT4d1-AC3" cell_refs="CT-d-1"><invocation>python infra/aws/terraform/shared-infra/tests/dell_fence_census.py --selftest</invocation><expect>FENCE-CENSUS-SELFTEST cases=</expect></criterion>
`CT4d1-AC3` -- the same line must read `ok=True`. In the proof row's evidence also give the `--live` last line after the
repair; it is expected to read `disagree=0 ... ok=True` with `dell1_scoped=3`, and if it does not, report what it reads and why.

**BOUNDS.** Read-only AWS (`s3api get-bucket-policy`, `list-buckets`, `iam simulate-*`, `sts get-caller-identity`), as the cell had.
No object read, no object listing in any firm bucket, no apply, no registry edit.
