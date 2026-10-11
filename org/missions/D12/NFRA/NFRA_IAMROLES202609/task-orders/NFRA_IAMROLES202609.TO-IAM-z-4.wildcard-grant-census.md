# NFRA_IAMROLES202609.TO-IAM-z-4 -- READ-ONLY census of the three S3 wildcard grants (opal*, opal-*, opal-data-*): who holds each, with what actions, and which concrete buckets the holder actually addresses (round-8 analysis E4)

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R9.md</decomp_doc>
<owned_cells>IAM-z-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_IAMROLES202609~14</issued_to>
<placeholders>NONE</placeholders>

## THE CELL, INLINED IN FULL (ROUND_ANALYSIS.round8.md @d14162158d, E4)

```
IAM-z-4. READ-ONLY. NOTHING IS APPLIED, EDITED OR DELETED. No bucket is created.
WHY: an Allow on arn:aws:s3:::opal-data-* grants on every bucket of that prefix, including one an outsider creates later.
A wildcard has no single name to classify, so it is graded by what its holder actually uses. Round 10 replaces each
wildcard with that explicit list.

STEPS (workspace root C:/Users/Opal Bloomberg/Desktop/ajb_workspace; AWS through its .tools/aws shim):
  1. ENUMERATE: `.tools/aws iam get-account-authorization-details --output json` (the CLI auto-paginates; ~36 MB). From
     every role, user and group inline policy and every customer-managed policy's DEFAULT version, find every ALLOW
     statement with an S3 Resource whose bucket part contains a `*` and starts with `opal` (expected patterns: opal*,
     opal-*, opal-data-*; report any other). A grant = one distinct (principal, pattern) pair. Deny is not a grant.
  2. For each grant, record: the actions (write=yes if any of s3:Put*, s3:Delete*, s3:*); the buckets in THIS account
     matching the pattern (`.tools/aws s3api list-buckets`); and the buckets the principal ADDRESSES: environment
     variables of every Lambda function on the role (`lambda list-functions`, filter by Role, then
     get-function-configuration), ECS task definitions or EC2 instance profiles on it where they exist, and bucket names in
     the repo code that deploys to it where you can name that code. Say which of these planes you could read for each
     principal; a plane you could not read is named, never counted as zero.
  3. Write C:/Users/Opal Bloomberg/Desktop/ajb_workspace/org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~14/WILDCARD_CENSUS.md
     with one line per grant, exactly:
       WILDCARD: <pattern> principal=<role|user|group|policy name> write=<yes|no> ours_matching=<n> addressed=<n>
     then, under each, the addressed bucket names; and exactly one line:
       DENOMINATOR: principals=<n> documents=<n> wildcard_grants=<n>
  4. Report in your final message: the grants, which hold write, and every addressed bucket that is NOT in our account
     (that one is URGENT).
```

## DEPENDENCIES

None. Read-only; runs beside IAM-z-1..z-3.

## BOUNDS

```
READ-ONLY: no apply, no policy edit, no bucket created. No deploy ledger. G-21: no alert, monitor or schedule.
G-25: no Access Analyzer.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~14/
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Surprise rows: id `NFRA_IAMROLES202609-Z-S<k>` (next free k), `"fabric": "site-z"`.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-z-4"><invocation>bash -c "f=org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~14/WILDCARD_CENSUS.md; test -f \$f || { echo MISSING:\$f; exit 2; }; echo den=\$(grep -c -E '^DENOMINATOR: principals=[0-9]+ documents=[0-9]+ wildcard_grants=[0-9]+\$' \$f) rows=\$(grep -c -E '^WILDCARD: [a-z0-9*.-]+ principal=[A-Za-z0-9_.+=,@-]+ write=(yes|no) ours_matching=[0-9]+ addressed=[0-9]+\$' \$f) grants=\$(grep -o -E 'wildcard_grants=[0-9]+' \$f | head -1)"</invocation><expect>`den=1`, and `rows` equal to the number after `wildcard_grants=` -- every grant in the denominator has exactly one row</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-z-4" judgment="true"/>
</proof_of_spec>

- **AC4** (JUDGMENT, never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason naming 3.0.0_SA_CVO~Z): is each
  `addressed` list complete enough to replace its wildcard without breaking the holder, and is every unreadable plane named?

Every invocation runs under `timeout 120`.

<!-- ===================== RECORD FACE -- does NOT travel to the assignee ===================== -->

<status>pending</status>
<round>9</round>
<slot>0.9.0_WK_NFRA_IAMROLES202609~14</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZI</issued_by>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<to_id>NFRA_IAMROLES202609.TO-IAM-z-4</to_id>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 9) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @3cadaf52ca (L4-R GRANDFATHERED per `prd-signoff.py status`)
**Authority chain:** round-8 slug (msg 33357) -> `ROUND_ANALYSIS.round8.md` @d14162158d E4 (msg 33361) -> L5 round-9 decomp -> this issuance.
**Risk LOCAL:** read-only reads of IAM, S3 and Lambda configuration; nothing in the world moves.
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- read-only; no deploy ledger.
comp-iam: RUN -- the sweep (DEAD_BUCKET_SWEEP.md section 3) counted 3 distinct wildcard names, 9 occurrences; comp-iam models (action) only, so the cell reads live.
comp-adversary: RUN -- recut taken as GIVEN; denominator of re-derived premises 1 of 1 (a wildcard cannot be classified by head-bucket; it is graded by what its holder addresses).
</preflight>

**Preflight disposition:** checks dry-run at the base: AC1 base FAIL as expected (`MISSING:` the census).
