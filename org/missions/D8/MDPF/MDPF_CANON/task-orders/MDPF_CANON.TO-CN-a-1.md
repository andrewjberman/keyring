# MDPF_CANON task order -- `CN-a-1` -- THE PER-FIRM GOLD WRITERS (IAM)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-a-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~1</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed (the live clock stays as read at L5).
comp-iam: RUN -- comp-iam role mdpf-gold-lambda-role read 2026-10-09 ~18:5xZ: 14 statements, no write on any firm bucket and none on composite gold today (the gap this cell closes). This cell adds three NEW roles from ../modules/opal_name (function gold-writer, kind role), each trusting mdpf-gold-lambda-role, each granted only its firm gold prefix of the four artifacts; the gold Lambda gains sts:AssumeRole on exactly the three and Put/Get on the composite gold of the four artifacts in opal-data-mdpf. Applied by CloudOps after the drain.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 at box/dell1 -- r1_iam.py 2 of 6 (NAMES, GRANT, TRUST, GLOBAL fail as expected; ADMITTED passes LIVE: name() gives mdpf-49f/inf/cot-gold-writer-role and each matches its bucket's DenyForeignFirmPrincipals; PLANTED passes); terraform fmt -check rc=0 at base
EGRESS CLASS, declared: NONE (the worker writes no AWS; the issuer's CloudOps lane applies after the drain).
</preflight>

## 1. THE CELL -- `CN-a-1` (round 1, THE THREAD for FWD-1; decomposition v1)

Read `org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md` (v2.9) CONTRACTS and DEC-2, DEC-14 and DEC-15 first. The L5 fact sheet the issuer cut against is
`org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round1/L5_FACTS.md`. This cell is its own chain (no dependency); its apply precedes the emitter's deploy.

In `infra/aws/terraform/mdpf-pipeline/`, add the per-firm gold writers by copying MDPF_TAXSMA's role pattern in `iam.tf`
(`taxsma_49f` / `taxsma_cot`, about lines 992-1230: the `opal_name` module, the firm long name and the bucket derived from the module's
`scope_short` / `scope_class` / `scope_bucket` maps, the trust on `aws_iam_role.mdpf_gold_lambda.arn`).

1. **Three roles, one per firm** (49financial, inflection, cottonwood). Each has:
   - a `module` block with `source = "../modules/opal_name"`, `system = "mdpf"`, `scope = "<firm>"`, `function = "gold-writer"`,
     `kind = "role"`;
   - an `aws_iam_role` named `module.<that>.name`, trusting `aws_iam_role.mdpf_gold_lambda.arn` only;
   - an `aws_iam_role_policy` (its name from the same module with `kind = "policy"`) granting:
     - `s3:PutObject`, `s3:GetObject` on `arn:aws:s3:::${local.<bucket>}/mdpf/${local.<long>}/gold/<artifact>/*` for EXACTLY the four
       artifacts `account_distribution`, `account_units`, `aggregate_aua_timeseries`, `aum_metrics`;
     - `s3:ListBucket` on the bucket, conditioned on those prefixes.
   - Nothing else: no platinum, no state, no `gold/*`.
   - The bucket and long name are locals derived from the module's maps, never typed.
2. **The gold Lambda side:**
   - an `aws_iam_role_policy` on `aws_iam_role.mdpf_gold_lambda` allowing `sts:AssumeRole` on exactly the three new role ARNs
     (a new policy, or an extension of the existing assume policy; do not touch the TAXSMA grants);
   - the same role gets `s3:PutObject`, `s3:GetObject` on `mdpf/global/gold/<artifact>/*` in the composite bucket for the four
     artifacts (the composite bucket from the module's `scope_bucket` for scope `global`, never typed);
   - in `gold-lambda.tf`'s environment, `GOLD_WRITER_ROLE_ARN_49FINANCIAL`, `GOLD_WRITER_ROLE_ARN_INFLECTION` and
     `GOLD_WRITER_ROLE_ARN_COTTONWOOD`, each `= aws_iam_role.<role>.arn`.
3. **No role name is typed.** The live fence (`DenyForeignFirmPrincipals` on each firm bucket) admits `*-49f-*`, `*-inf-*` and
   `*-cot-*`, and `name()` puts the firm in the scope slot. AC1's arm 5 reads the live policy to show it, and the fence is never edited.

## 2. BOUNDS

1. **No AWS write of any kind**: no apply, no deploy, no invoke, no `s3 cp`/`put`, no IAM call. A read-only `get`/`describe`/`head` is
   allowed. No install, no push. The issuer has CloudOps apply and deploy after the drain. REFUSE, do not rescue.
2. Only the files in section 3 change (plus your deliverables and the surprise channel).
3. **Every NEW address and name comes from the builders**: `lib/opal_naming.py` `address()`/`key()` in Python, and the
   `../modules/opal_name` Terraform module for names, never a typed bucket, key or role name (PRD CONTRACTS; DEC-15; CLAUDE.md rule 30).
   A builder REFUSAL is a row, never a hand-typed workaround.
4. **Never** (PRD DEC-14):
   - change the conformant compute chain's schedules or platinum's shape;
   - move `platinum/mdpf/global/`;
   - touch `opal-data-mdpf/code/scripts/gold/`;
   - add a second writer of the new gold;
   - add a shadow prefix or a standing comparator.
   The existing JSON emits stay exactly as they are this round; the new parquet is ADDED beside them (the readers and the publisher
   move in later rounds, the publisher last).
5. **CLIENT DATA:** never open or print a client figure or account id; fixtures are synthetic. Never read any
   `org/**/W73_S*_EVIDENCE.json`, `W73_S2_RESOLUTION.json`, an IRPT_DASHBD tie-out file or a COTBKF worker manifest.
6. Keep each file's line endings as you find them (read them first); no non-ASCII; Edit tool for existing files. Python edits pass
   `.tools/commit-gate.sh` (safe-commit runs it).
7. If an item cannot be met within your paths, file a row and stop on that criterion.

## 3. SURFACES

<paths>
infra/aws/terraform/mdpf-pipeline/iam.tf
infra/aws/terraform/mdpf-pipeline/gold-lambda.tf
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~1/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `infra/aws/terraform/modules/opal_name/`, and the issuer's checks under `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round1/checks/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-a-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round1/checks/r1_iam.py"; echo "exit=$?"</invocation><expect>ROUND 1 GOLD WRITERS: 6 of 6 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-a-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; terraform -chdir=infra/aws/terraform/mdpf-pipeline fmt -check iam.tf gold-lambda.tf; echo "exit=$?"</invocation><expect>exit=0 with no file listed -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-a-1" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded on the issuer's real run at the round-1 close (never self-graded): after CloudOps applies, `get-role` on each name() role shows the trust on mdpf-gold-lambda-role and the four gold prefixes only, and the gold Lambda's live env carries the three ARNs.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~1/MDPF_CANON.TO-CN-a-1.proof_of_spec.json` (AC3 UNVERIFIABLE-BY-INSTRUMENT,
status_reason "graded at the round-1 close run"). **Flip this order's `<status>` to `complete` in the SAME commit as your proof
instance**, only when AC1 and AC2 pass. A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W1-S<k>`, with
`surfaced_at` from `date -u +%FT%TZ` at filing. Report once: the diff (per file, one line each), the output line of every
criterion, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 1 = THE THREAD (FWD-1) over PRD v2.9 @12adb87963 (ADMITTED; the CVO's L6 condition, msg 3000, is arm 1 and arm
5 of `r1_iam.py`). Base box/dell1. LF only. Checks positive-controlled against a reference tree before the cut.

<status>complete</status>
<round>1</round>
<to_id>MDPF_CANON.TO-CN-a-1</to_id>
<slot>~1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
