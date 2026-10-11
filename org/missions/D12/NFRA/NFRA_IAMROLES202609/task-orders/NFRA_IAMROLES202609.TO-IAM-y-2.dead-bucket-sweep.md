# NFRA_IAMROLES202609.TO-IAM-y-2 -- READ-ONLY account-wide sweep: every S3 bucket name an identity policy grants on, classified 404 / 403 / 200; plus market-overview's consumers of market_data_v2

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R8.md</decomp_doc>
<owned_cells>IAM-y-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~IR</issued_to>
<placeholders>NONE</placeholders>

## THE CELL, INLINED IN FULL (round-7 analysis E2; row Z-S39 generalised)

```
IAM-y-2. READ-ONLY. NOTHING IS APPLIED, EDITED OR DELETED.
WHY: round 7 found Allows on non-existent GLOBAL bucket names on three roles (one a 12-function production role with
Put/Delete). Nobody has swept the account for the class. An S3 name is global: a 404 name is claimable by anyone, and a 403
name already belongs to another account that our grant reaches.

STEPS:
  1. ENUMERATE: aws iam get-account-authorization-details (auto-paginated, counted client-side). From every role inline
     policy, user and group inline policy, and customer-managed policy DEFAULT version, collect every distinct S3 bucket name
     appearing in a Resource ARN (arn:aws:s3:::<name> or <name>/...). Skip wildcard-only names ("*", "prefix*") but COUNT
     them separately. Print the denominators: principals read, policy documents read, distinct bucket names, wildcard names
     skipped.
  2. CLASSIFY each distinct name with `aws s3api head-bucket --bucket <name>` and read the ERROR CODE: 404 / NoSuchBucket =
     ABSENT (claimable); 403 = FORBIDDEN (exists, another account's, or ours without access -- resolve which with
     get-bucket-location / our bucket list); 200 = OURS. Carry a control in each class where one exists (a bucket you know is
     ours for 200; a name round 7 proved absent, e.g. opal-data-smartx, for 404).
  3. Write org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round8/DEAD_BUCKET_SWEEP.md with
     one line per distinct name, exactly:
       BUCKET: <name> class=<ABSENT|FOREIGN|OURS|UNRESOLVED> grants=<n principals> write=<yes|no>
     (write=yes if any granting statement holds s3:Put*, s3:Delete* or s3:*), and exactly one line:
       DENOMINATOR: principals=<n> documents=<n> names=<n> wildcard_skipped=<n>
  4. market-overview's `market_data_v2` (deleted out of band; the module would re-create it): name its CONSUMERS -- code,
     environment variables and grants that reference that bucket -- in a section of the same file, ending in exactly:
       MARKET_DATA_V2_CONSUMERS: <n>
  5. Report. Each ABSENT name with write=yes is round 9's narrowing; each FOREIGN name is URGENT.
```

## DEPENDENCIES

None. Read-only, so it may run beside IAM-y-1 (DECOMP_R8 section 4).

## BOUNDS

```
READ-ONLY: no apply, no policy edit, no bucket created (never create a bucket to "test" a name). No deploy ledger.
G-21: no alert, monitor or schedule.  G-25: no Access Analyzer.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round8/
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-y-2.dead-bucket-sweep.md
</paths>

Surprise rows: id `NFRA_IAMROLES202609-Z-S<k>` (next free k), `"fabric": "site-z"`. Commit through `.tools/safe-commit.sh` under
your own author line. At the end, flip this order's LAST `<status>` to `complete` with a proof instance in your deliverables
directory (`to_id` NFRA_IAMROLES202609.TO-IAM-y-2).

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-y-2"><invocation>bash -c "f=org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round8/DEAD_BUCKET_SWEEP.md; test -f \$f || { echo MISSING:\$f; exit 2; }; echo den=\$(grep -c -E '^DENOMINATOR: principals=[0-9]+ documents=[0-9]+ names=[0-9]+ wildcard_skipped=[0-9]+\$' \$f) rows=\$(grep -c -E '^BUCKET: [a-z0-9.-]+ class=(ABSENT|FOREIGN|OURS|UNRESOLVED) grants=[0-9]+ write=(yes|no)\$' \$f) names=\$(grep -o -E 'names=[0-9]+' \$f | head -1)"</invocation><expect>`den=1`, and `rows` equal to the number after `names=` -- every distinct bucket name in the denominator has exactly one classified row</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-y-2"><invocation>grep -c -E '^MARKET_DATA_V2_CONSUMERS: [0-9]+$' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round8/DEAD_BUCKET_SWEEP.md</invocation><expect>exactly 1 -- market_data_v2's consumers are counted, so next round can rule removal vs owner decision</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-y-2" judgment="true"/>
</proof_of_spec>

- **AC4** (JUDGMENT, never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason naming 3.0.0_SA_CVO~Z): does each class
  carry a control, and could an ABSENT or FOREIGN name be hiding behind an UNRESOLVED row?

Every invocation runs under `timeout 120`.

<!-- ===================== RECORD FACE -- does NOT travel to the assignee ===================== -->

<status>complete</status>
<round>8</round>
<slot>0.7.0_AE_CloudOps~IR</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZI</issued_by>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<to_id>NFRA_IAMROLES202609.TO-IAM-y-2</to_id>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 8) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @3cadaf52ca (L4-R GRANDFATHERED per `prd-signoff.py status`)
**Authority chain:** round-7 slug (msg 33310) -> `ROUND_ANALYSIS.round7.md` @fef971046b E2 -> L5 round-8 decomp -> this issuance.
**Risk LOCAL:** read-only reads of IAM and S3; nothing in the world moves.
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- read-only; no deploy ledger.
comp-iam: RUN -- `bash .tools/comp-iam stats` at the round-7 cut (219 roles); comp-iam models (action) only, never (action, resource), so it cannot answer this sweep -- the cell reads get-account-authorization-details live.
comp-adversary: RUN -- recut taken as GIVEN; denominator of re-derived premises 2 of 2 (head-bucket's three classes; a failed read returns a value, so each class carries a control).
</preflight>

**Preflight disposition:** checks dry-run at the base: AC1 base FAIL as expected (`MISSING:`); AC2 base FAIL as expected (file absent).
