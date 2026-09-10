# AMGT_RESAPP.TO-AMGT-s-6 -- THE VERSION STORE: opal-data-research, created through the ledger and safe-apply, versioned, raw before derived

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-s-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~7</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-6; manifest row S6)

```
AMGT-s-6. THE VERSION STORE -- `opal-data-research`, MEASURED ABSENT at two vintages (section 1a),
created by Terraform through `safe-apply` under a change-management entry opened BEFORE the act;
snapshots ACCUMULATE, never overwrite; raw before derived.

FWD-6's bar, verbatim: "An analyst returning to a company can say what changed. DONE WHEN EXERCISED
-- someone has actually compared two versions." This cell builds the store that makes two versions
exist; the EXERCISED bar is served later by the page and is not claimed here.

MEASURED ABSENT, twice: comp-find 'opal-data-research' --corpus aws -> 0 of 2382 graph nodes at
2026-09-10 12:24:50Z; the L1 brief's PART V measured it absent on the LIVE plane 13:30-16:00Z the
same day. Two instruments, two vintages, one answer. Your first act re-measures it on the live plane
(AC1) so the create is not a duplicate.

WHAT TO PRODUCE:

  (a) THE TERRAFORM  infra/aws/terraform/research/  (a NEW module; mirror the estate's existing bucket
      declarations -- the opal-data-assets site is declared under infra/aws/terraform/opal-assets/,
      read it for the provider block, tags and the versioning/public-access/encryption resources the
      estate uses):
        - aws_s3_bucket            opal-data-research
        - aws_s3_bucket_versioning Enabled   (snapshots ACCUMULATE; an overwrite becomes a version)
        - aws_s3_bucket_public_access_block  all four true
        - server-side encryption   the estate's default
        - NO lifecycle expiration, NO replication, NO notification, NO event rule (G-20).
        - tags: project=AMGT_RESAPP, directive=D5, owner=2.0.0_SA_COO (a tag is not a lane)

  (b) THE KEY GRAMMAR, as a data contract in the deliverable  .../deliverables/0.9.0_WK_AMGT_RESAPP~7/STORE_CONTRACT.md
      Raw before derived, and every stage persists its own output:
        raw/<vendor>/<security_key>/<YYYYMMDDTHHMMSSZ>/<artifact>        vendor bytes, untouched
        derived/<engine>/<security_key>/<YYYYMMDDTHHMMSSZ>/<artifact>    what an engine computed from raw
        packs/<security_key>/<YYYYMMDDTHHMMSSZ>/pack.json                the assembled pack object
      where <security_key> is the identity layer's key (the Bloomberg ticker with spaces replaced by
      underscores until AMGT-s-12 states otherwise) and the stamp is UTC. State in the contract that a
      consumer reads the LATEST stamp under a prefix and that nothing is ever written to a path that
      already exists (the versioning is the safety net, not the rule).

  (c) THE LEDGER, BEFORE THE ACT (CLAUDE.md NEVER-2; G-16): open a change-management entry at
        org/critical_paths/change_management/<UTCSTAMP>_amgt-resapp-opal-data-research-bucket_deploy_completion.md
      with its sentinel
        org/critical_paths/.open_deploys/amgt-resapp-opal-data-research-bucket.json
      BEFORE `safe-apply`, and CLOSE and COMMIT it BEFORE you take the reads that grade the apply
      (AC2-AC5). Use the estate's ledger tool; locate it with ONE call:
        comp-which "open a change-management deploy ledger entry"
      A death between the apply and the commit leaves the world changed and the record silent -- that
      is the expensive shape, and the ordering above is the rule, not a preference.

  (d) THE APPLY, through the wrapper only:  bash .tools/safe-apply.sh  (never bare `terraform apply`; G-22).
      Plan first, read the plan, apply once. Then re-plan: it must read "No changes." (AC5).
```

## DEPENDENCIES

**NONE.** No cell precedes it. Two cells wait on it (AMGT-s-7 the freshness view, AMGT-s-14 the input
ledger), and AMGT-s-1's RAW LANDING needs this bucket to exist even though the manifest draws no edge
(the decomposition's investigation row AMGT_RESAPP-Z-S1 records that). Land it early in the round.

## BOUNDS -- what this cell may not cross

```
⛔ G-16 (NEVER-2): the ledger entry is opened BEFORE the apply and closed + committed BEFORE the grading
reads. A confirmed deploy is never left half-landed: finish in-session or roll back and say so.

⛔ G-22 (NEVER-9): safe-apply, never bare terraform apply; safe-commit, never bare git commit.

⛔ G-19: ONE bucket, ONE output path grammar. No second bucket, no "staging" bucket, no parallel prefix
that duplicates raw/ under another name.

⛔ G-20: no lifecycle notification, no event rule, no SNS topic, no alarm on this bucket. A version
store is a store.

⛔ G-23: no cross-firm data touches this bucket and no other firm's bucket or key prefix is referenced
by this module. This is research on public securities, not client data.

⛔ NO IAM CHANGE IN THIS CELL. Which principal writes to the bucket is AMGT-s-1's and AMGT-s-2's to
establish when they land bytes; do not attach a bucket policy or create a role here. If the apply
REQUIRES an IAM change to succeed, that is a BLOCKING row, not an edit.

⛔ NOTHING IS DELETED, RENAMED OR RE-POINTED. This module creates. comp-blast is owed the moment the
plan shows a change to any resource that already exists -- and that plan is NOT applied.

⚠ BOUND EVERY AWS CALL. Each invocation runs under `timeout 120`; a timeout is the recorded output.
terraform init on a fresh module can exceed that on a cold provider cache -- run init FIRST as its own
step, outside a criterion, and record its rc.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-find --corpus aws (vintage 2026-09-10 12:24:50 UTC): 'opal-data-research' -> 0 hit(s) across 2382
    aws node(s). S3 keys ARE modelled in that graph (the S3Key band is populated elsewhere), so the zero
    is a measured absence in the graph; AC1 re-measures on the live plane.

comp-iam stats (RUN at the L5 vintage): 195 TF roles / 188 services / 1084 operations / 304 gaps. No
    IAM is touched here; the writer principal is a later cell's.

comp-schedule (RUN to completion, --budget 500, 5 of 5 carriers): 25 gates armed, none this project's.
    G-16, G-19, G-20, G-22, G-23 bind this cell and are in BOUNDS. Two open deploy-ledger entries
    exist on this fabric for OTHER projects (G-8..G-13); yours is a NEW entry with its own slug.

The estate's Terraform for buckets: infra/aws/terraform/opal-assets/ declares the opal-data-assets
    site (advi_stitch_landing.tf and siblings). Mirror its provider, backend and tag conventions;
    do not copy its IAM.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
infra/aws/terraform/research/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-s-6.version-store-opal-data-research.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~7/`, inside the granted prefix. AWS acts
(terraform init/plan, safe-apply, s3api reads) are operational and are not path-gated.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
⛔ REFUSE a criterion you cannot satisfy as written and report the refusal with its measurement; never
repair the criterion, widen it, or satisfy it by a route this order did not name. If you need a
surface that is not listed, file a surprise ROW in the investigation file above and STOP on that
criterion. Your surprise row id is `AMGT_RESAPP-Z-W7-S<k>`, `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`,
inside the file's fenced json array; a BLOCKING row is read by the COO in your final report; an
OBSERVATION never interrupts.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-s-6"><invocation>aws s3api head-bucket --bucket opal-data-research 2>&amp;1 | grep -c -E 'Not Found|404|NoSuchBucket'</invocation><expect>exactly "1" BEFORE the apply -- the bucket is ABSENT on the live plane at your vintage (the pre-act re-measure that makes the create a create and not a duplicate); record this output with its UTC time in the deliverable BEFORE running safe-apply; a "0" here means the bucket exists and the create is a BLOCKING row, not an apply</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-s-6"><invocation>aws s3api get-bucket-versioning --bucket opal-data-research --query Status --output text</invocation><expect>exactly "Enabled" -- snapshots ACCUMULATE; an overwrite becomes a version rather than a loss (FWD-6's precondition)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-s-6"><invocation>aws s3api get-public-access-block --bucket opal-data-research --query 'PublicAccessBlockConfiguration.[BlockPublicAcls,IgnorePublicAcls,BlockPublicPolicy,RestrictPublicBuckets]' --output text</invocation><expect>"True	True	True	True" -- all four public-access blocks on; research packs are internal</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-s-6"><invocation>python -c "import glob,io,importlib.util,pathlib; s=importlib.util.spec_from_file_location('dl','.tools/deploy_ledger.py'); dl=importlib.util.module_from_spec(s); s.loader.exec_module(dl); fs=glob.glob('org/critical_paths/change_management/*amgt-resapp-opal-data-research-bucket_deploy_completion.md'); t=io.open(fs[0],encoding='utf-8').read() if len(fs)==1 else ''; st=dl._md_status(pathlib.Path(fs[0])) if len(fs)==1 else None; print('entries', len(fs), '| names safe-apply', 'safe-apply' in t, '| closed', bool(st) and dl._is_terminal_status(st))"</invocation><expect>"entries 1 | names safe-apply True | closed True" -- exactly one ledger entry for this slug exists, it names the wrapper it used, and it is CLOSED before this read (G-16: the record is committed before the grading reads), where CLOSED is read by the ledger tool's OWN reader (.tools/deploy_ledger.py _md_status + _is_terminal_status, the predicate its RED sweep uses; amendment 1 on row AMGT_RESAPP-Z-W7-S1 -- the original four hand-rolled literals never matched the tool's canonical "**Status:** CLOSED -- nothing stranded -- closed &lt;ts&gt;" rendering); "entries 0", "entries 2", or "closed False" is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-s-6"><invocation>terraform -chdir=infra/aws/terraform/research plan -no-color -input=false 2>&amp;1 | grep -c -E '^No changes\.|Your infrastructure matches the configuration'</invocation><expect>exactly "1" AFTER the apply -- NEGATIVE: the module is idempotent and the world matches the record; a second apply would do nothing. A plan showing changes after the apply means the apply was partial or the module drifts, and that is a BLOCKING row</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-s-6"><invocation>terraform -chdir=infra/aws/terraform/research state list | grep -v -c -E '^aws_s3_bucket'</invocation><expect>exactly "0" -- NEGATIVE and structural: every resource in the module's state is an aws_s3_bucket* resource (the bucket and its versioning, public-access-block and encryption configuration). No IAM, no notification, no lifecycle, no second bucket: the cell created a store and nothing else</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-s-6" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical, the pre-act re-measure): absent on the live plane at your vintage, recorded before the apply. A create against an existing bucket is a collision, never a no-op.
- **AC2**, **AC3** (mechanical): versioning on, public access off -- read from the live plane, never from the plan.
- **AC4** (mechanical): the ledger entry exists once, names the wrapper, and is closed before the grading reads. NEVER-2 in one line.
- **AC5** (mechanical, NEGATIVE): idempotent -- the record and the world agree after the act.
- **AC6** (mechanical, NEGATIVE, structural): the state holds a store and nothing else. The bound that decides whether this cell stayed a store.
- **AC7** (JUDGMENT -- never self-graded; record its output UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): does STORE_CONTRACT.md state the key grammar so that AMGT-s-1 can land raw bytes and AMGT-s-14 can render "last run / outcome / re-run" WITHOUT asking anyone -- raw before derived, a stamp per write, never a write to an existing path, the latest stamp as the read?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output -- run `terraform init` as its own step first.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>1</round>
<slot>~7</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5+L6, round 1) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @f68818832b
**Authority chain:** L1 brief @19ce7d5b4d -> L2 endpoint @3bc8f5f2c4 -> L4 PRD v0.3 @f68818832b -> L5 decomposition v0.2 @ed25feaee5 -> this issuance.
**Chain:** Q7, the root of `AMGT-s-6 -> AMGT-s-7 -> AMGT-s-14`; slot ~7 drains that queue.
**Provenance:** the cell text is the decomposition's row verbatim. The IAM exclusion is this issuer's: a bucket cell that also minted a writer role would be two engines, and the writer principal is only knowable when the landing cell picks its interpreter and credential. The manifest draws no S1 -> S6 edge; the decomposition's row AMGT_RESAPP-Z-S1 records that S1's raw landing needs this bucket, and the issuance sequences S1's spawn after this cell lands rather than adding an edge to a frozen spec.
<preflight>
comp-schedule: RUN -- --budget 500 to completion, 5 of 5 carriers, C1=23 C2=6 C3=12 C4=20 C5=335, 25 gates armed, none this project's; G-16, G-19, G-20, G-22, G-23 bound onto this cell
comp-iam: RUN -- 195 TF roles / 188 services / 167 Lambda / 21 EC2 / 1084 operations / 304 gaps; no IAM touched by this cell by construction (AC6)
comp-adversary: RUN -- on the L5 decomposition v0.2 at read-vintage @d09e26e1b1; 10 of 10 cited pins VERIFIED
comp-routes: RUN -- 28 CloudFront behaviors, DESIRED plane; no distribution touched
comp-cache: RUN -- 118 of 118 useQuery sites; no portal file touched
comp-find --corpus aws: RUN -- 'opal-data-research' 0 of 2382 nodes at 12:24:50Z; AC1 re-measures on the live plane before the act
</preflight>

**Preflight disposition:** mandatory core RUN at the L5 vintage. comp-blast DECLARED-NOT-APPLICABLE at the cut: the module CREATES; the blast radius of a resource that does not exist is empty by construction. It becomes OWED the moment a plan shows a change to an existing resource, and such a plan is not applied under this order.

**Amendment 1 (2026-09-10T21:41Z, 2.0.0_SA_COO~ZZZ, on row AMGT_RESAPP-Z-W7-S1):** AC4's `closed` predicate replaced. The original four literals ('STATUS: CLOSED', 'STATUS: COMPLETE', 'CLOSED AT', 'COMPLETED AT') were written against a hand-authored form this issuer never read; the estate's ledger tool, used exactly as deliverable (c) names it, renders `**Status:** CLOSED -- nothing stranded -- closed <ts>`, which contains none of them -- a criterion no correct use of the named tool could satisfy. The proposition is unchanged (exactly one entry, names safe-apply, CLOSED before the grading reads); what `closed` is measured against is now the tool's own reader (`_md_status` + `_is_terminal_status`), exercised by this issuer in the slot's worktree before the amendment: True on the committed entry, False on 'OPEN -- ...', 'HELD-VERIFY-PENDING -- ...' and a file with no status line. The FAIL recorded against the original text in the instance @71fa0a2264 stands as the measurement of that text; the worker re-runs AC4 as now written and records the result beside it. No other criterion moved.
