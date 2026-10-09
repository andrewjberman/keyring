# MDPF_CANON task order -- `CN-b-4` -- THE COMPOSITE GRANT TAKES ITS BUCKET FROM THE BUILDER (W1-S1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-b-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~7</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed.
comp-iam: RUN -- comp-iam role mdpf-gold-lambda-role and the live mdpf-gold-writer-assume-policy read at round 1 (CloudOps @1785cdcddf): the composite Put/Get and ListBucket name ${local.mdpf_bucket} (= opal-data-mdpf). This cell re-points the same grants to builder output; their effect is unchanged.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 at box/dell1 -- r2_checks.py builder 0 of 3 at base (5 ARNs on ${local.mdpf_bucket}: the 4 Put/Get plus the AMENDMENT 4 ListBucket)
EGRESS CLASS, declared: NONE (the worker writes no AWS).
</preflight>

## 1. THE CELL -- `CN-b-4` (round 2, decomposition v2)

Read `org/missions/D8/MDPF/MDPF_CANON/ledger/ROUND_ANALYSIS.round1.md` section 3 and `org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md` (v2.9) CONTRACTS and the DECISIONS first.

The CTO ruled row W1-S1 at `org/missions/D8/MDPF/MDPF_CANON/ledger/ROUND_ANALYSIS.round1.md` section 2: under rule 30 the grant takes its bucket from the builder, not from a hand-kept local.

1. In `infra/aws/terraform/mdpf-pipeline/iam.tf`, `aws_iam_role_policy.mdpf_gold_writers`: every S3 ARN that names
   `${local.mdpf_bucket}` (the four composite Put/Get prefixes and the composite ListBucket) takes its bucket from an `opal_name`
   module output instead. Use `module.<m>.scope_bucket["<key>"]`, where the generated map's value for `<key>` equals the bucket
   `address("mdpf", "global", "gold", ...)` returns (`opal-data-mdpf`).
2. The generated map already carries `"mdpf" = "opal-data-mdpf"` (`modules/opal_name/generated_locals.tf`, from `scopes.json`).
   - If that entry IS the builder's product-bucket mapping for the source `mdpf`, use it and say so: no registry row is needed.
   - If it is not, add the missing registry row in `infra/logic/registry/scopes.json` (the grammar rule 30 names) and regenerate the
     locals with the builder's own command (the header of `generated_locals.tf`). File a row naming which it was. The registry and
     the generated locals are then in your paths.
3. The effect is unchanged: the same actions on the same prefixes. AC2 is round 1's `r1_iam.py`, which must still read 6 of 6.

## 2. BOUNDS

1. **No AWS write of any kind**: no apply, no deploy, no invoke, no `s3 cp`/`put`/`rm`, no IAM call, not even from a test (round 1's
   row D1-S4 is what a test write into a live bucket costs). A read-only `get`/`describe`/`head`/`list` is allowed. No install, no push.
   The issuer has CloudOps apply after the drain. REFUSE, do not rescue.
2. Only the files in section 3 change (plus your deliverables and the surprise channel).
3. **Every NEW address and name comes from the builders**: `lib/opal_naming.py` `address()`/`key()`/`name()` and the `../modules/opal_name`
   Terraform module, never a typed bucket, key or role name (PRD CONTRACTS; DEC-15; CLAUDE.md rule 30). A builder REFUSAL is a row.
4. **Never** (PRD DEC-14):
   - change the conformant compute chain's schedules or platinum's shape;
   - move `platinum/mdpf/global/`;
   - touch `opal-data-mdpf/code/scripts/gold/`;
   - add a second writer, a shadow prefix or a standing comparator;
   - move a served key.
5. **CLIENT DATA:** never print a client figure or account id.
6. Keep each file's line endings as you find them (read them first). No non-ASCII. Use the Edit tool for existing files.
7. If an item cannot be met within your paths, file a row and stop on that criterion.

## 3. SURFACES

<paths>
infra/aws/terraform/mdpf-pipeline/iam.tf
infra/logic/registry/scopes.json
infra/aws/terraform/modules/opal_name/generated_locals.tf
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~7/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `lib/opal_naming.py`, `infra/aws/terraform/modules/opal_name/`, `infra/logic/registry/`. The issuer's check `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round2/checks/r2_checks.py` is also read-only (never edit it).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-b-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round2/checks/r2_checks.py" builder; echo "exit=$?"</invocation><expect>ROUND 2 BUILDER: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-b-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round1/checks/r1_iam.py"; echo "exit=$?"</invocation><expect>ROUND 1 GOLD WRITERS: 6 of 6 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-b-4" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded at the round-2 close (never self-graded): after CloudOps applies, a targeted plan on aws_iam_role_policy.mdpf_gold_writers reads 0 to add, 0 to change (the rendered policy is identical), or a change whose rendered JSON is byte-identical.

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~7/MDPF_CANON.TO-CN-b-4.proof_of_spec.json`, with AC3
UNVERIFIABLE-BY-INSTRUMENT and status_reason "graded at the round-2 close". **Flip this order's `<status>` to `complete` in the SAME
commit as your proof instance**, and only when every mechanical criterion passes.

A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W7-S<k>`, with `surfaced_at` taken from `date -u +%FT%TZ` at
filing. Report once: the diff (one line per file), the output line of every criterion, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 2 = `org/missions/D8/MDPF/MDPF_CANON/ledger/ROUND_ANALYSIS.round1.md` @409182ae5a section 3, items 2-4 (item 1 and item 5 are the issuer's read of the 2026-10-10 13:30Z
daily write, not cells). Base box/dell1. LF only.

<status>pending</status>
<round>2</round>
<to_id>MDPF_CANON.TO-CN-b-4</to_id>
<slot>~7</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
