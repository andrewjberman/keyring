# MDPF_CANON task order -- `CN-b-3` -- THE PUBLISHER CAN READ PARQUET (M5 capability; no switch)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-b-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~6</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE the publisher's role is unchanged; the cell changes its runtime and layers only.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 at box/dell1 -- r2_checks.py publisher 1 of 3 at base (RUNTIME python3.12 and no LAYER fail as expected; NO SWITCH passes as the guard)
EGRESS CLASS, declared: NONE (the worker writes no AWS).
</preflight>

## 1. THE CELL -- `CN-b-3` (round 2, decomposition v2)

Read `org/missions/D8/MDPF/MDPF_CANON/ledger/ROUND_ANALYSIS.round1.md` section 3 and `org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md` (v2.9) CONTRACTS and the DECISIONS first.

The publisher (`infra/aws/terraform/opal-assets/mdpf_portal_publisher.tf`, `module "mdpf_publisher"`, `../modules/yang-lambda`,
which accepts `layers`) runs python3.12 with no layers, so it cannot read parquet (L5_FACTS section 4). The estate's existing heavy layer
`pandas-pyarrow-requests-layer` is py3.11 (`infra/aws/terraform/mdpf-pipeline/gold-lambda.tf:67-71`).

**Ruled (build ladder: reuse first):** give the publisher that layer.
1. Add a `data "aws_lambda_layer_version"` with `layer_name = "pandas-pyarrow-requests-layer"` in the opal-assets stack (in this file).
2. Set the module's `runtime = "python3.11"` and `layers = [data.aws_lambda_layer_version.<that>.arn]`.
3. Confirm the publisher source `infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher/lambda_function.py` is python3.11-clean:
   `python -m py_compile` under a 3.11 interpreter if one is installed, else a read for 3.12-only syntax. Say which.

**Nothing it reads or writes moves:** `GOLD_BUCKET`, `GOLD_ROOT`, `SERVE_BUCKET` and `SERVE_ROOT` are byte-identical. The read source moves
in the publisher's own later round, LAST (DEC-4). Do not touch the publisher's code.

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
infra/aws/terraform/opal-assets/mdpf_portal_publisher.tf
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~6/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `infra/aws/terraform/modules/yang-lambda/`, `infra/aws/terraform/mdpf-pipeline/gold-lambda.tf`. The issuer's check `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round2/checks/r2_checks.py` is also read-only (never edit it).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-b-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round2/checks/r2_checks.py" publisher; echo "exit=$?"</invocation><expect>ROUND 2 PUBLISHER: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-b-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; terraform -chdir=infra/aws/terraform/opal-assets fmt -check mdpf_portal_publisher.tf; echo "exit=$?"</invocation><expect>exit=0 with no file listed -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-b-3" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded at the round-2 close (never self-graded): after CloudOps applies, one publisher run on python3.11 serves leaves whose data-bearing values are byte-identical to the run before (`_provenance.written_at` excluded).

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~6/MDPF_CANON.TO-CN-b-3.proof_of_spec.json`, with AC3
UNVERIFIABLE-BY-INSTRUMENT and status_reason "graded at the round-2 close". **Flip this order's `<status>` to `complete` in the SAME
commit as your proof instance**, and only when every mechanical criterion passes.

A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W6-S<k>`, with `surfaced_at` taken from `date -u +%FT%TZ` at
filing. Report once: the diff (one line per file), the output line of every criterion, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 2 = `org/missions/D8/MDPF/MDPF_CANON/ledger/ROUND_ANALYSIS.round1.md` @409182ae5a section 3, items 2-4 (item 1 and item 5 are the issuer's read of the 2026-10-10 13:30Z
daily write, not cells). Base box/dell1. LF only.

<status>complete</status>
<round>2</round>
<to_id>MDPF_CANON.TO-CN-b-3</to_id>
<slot>~6</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
