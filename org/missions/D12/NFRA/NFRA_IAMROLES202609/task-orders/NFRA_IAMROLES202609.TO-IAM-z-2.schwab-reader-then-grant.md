# NFRA_IAMROLES202609.TO-IAM-z-2 -- opal-data-schwab (404): the canonical builder's dead READ comes out first, THEN bd-exporter-ec2-role's Allow is narrowed (round-8 analysis E2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R9.md</decomp_doc>
<owned_cells>IAM-z-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~IR</issued_to>
<placeholders>NONE</placeholders>

## THE CELL, INLINED IN FULL (ROUND_ANALYSIS.round8.md @d14162158d, E2)

```
IAM-z-2. WHY: opal-data-schwab reads 404, so anyone can claim the name, and a READER still lists it. Whoever claims it could
feed bytes into the canonical Schwab build. That is higher stakes than a dead grant.

THE READER, re-read by the issuer at the cut (the analysis cited :154-156; that citation has aged):
  data/canonical/schwab/build_canonical_daily.py:48    SRC_BUCKET = "opal-data-schwab"
                                                :141-145 latest_rps_date() lists Bucket=SRC_BUCKET, Prefix="01_raw/"
                                                :228     t1 = _normalize_date(args.date) or latest_rps_date()
  dates_to_build() was already re-pointed to monolith bronze @3b01132271; latest_rps_date() was not.

ORDER: (a) BEFORE (b). Narrowing first would turn a silent dead read into a loud AccessDenied the builder may not handle.
  (a) is NOT yours. The builder's owner (0.4.0_DS_ClientPlatform) removes the read; the issuer routed it through
      0.0.0_AB_MSTR~Z at this issuance. Its landing is MEASURED, never reported:
        grep -c 'Bucket=SRC_BUCKET' data/canonical/schwab/build_canonical_daily.py   reads 0 at HEAD
  (b) is yours: narrow the Allow on bd-exporter-ec2-role (declared in infra/aws/terraform/bd-pipeline/iam.tf; role at :341).

PHASE A -- read-only, no AWS write; runs NOW, before (a) lands:
  1. Find the statement(s) on bd-exporter-ec2-role that grant on opal-data-schwab: policy name, Sid, actions, TF address.
     Census the role's references to the name: environment and deployed code of every instance or task on the role, plus the
     builder lines above. A positive control: one live bucket the role uses. Write
     org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round9/schwab/SCHWAB_SURVEY.md with exactly:
       REFS: bd-exporter-ec2-role opal-data-schwab: env=<n> code=<n>
     Re-read the name live (get-bucket-location -> NoSuchBucket). Save the as-live document as .../schwab/ROLLBACK_<policy>.json.
  2. In YOUR OWN worktree: edit the declaration; plan with -target on that address; record
       PLAN: bd-pipeline: <targeted plan summary, verbatim>
     and the untargeted plan beside it. Commit the survey and rollback only, never the edit.
  3. Correct `.claude/skills/49-schwab-conv/SKILL.md` line 3 (its description names opal-data-schwab as the sync target). The
     bucket is deleted and 404: say so, and name where the raw lands now (read it from the skill's own body; do not guess).
     This is a text edit, LOCAL, and needs no pair.
  4. STOP. Report to 2.0.0_SA_COO~ZI. The pair ledger/NEVER_WIDEN_ROUND9_Z-2_{COO,CTO}_HALF.md is written against your survey.

PHASE B -- only when BOTH hold: the grep above reads 0 at HEAD, AND the issuer's GO after both halves are SIGNED:
  5. Read .open_deploys/ for bd-pipeline; open a NEVER-2 entry `iamroles-r9-narrow-schwab`.
  6. Commit the edit on your worktree branch, `safe-apply` -target on the signed address, drain the same session; the
     untargeted shared-tree plan then reads 0 to destroy.
  7. Verify LIVE: the document differs from the rollback by exactly the schwab ARNs. Read ONE real run on the role after the
     change (a bd gold-layer or exporter run) and confirm it succeeded. Record in .../schwab/POST_APPLY.md, exactly:
       POST-APPLY: schwab: verified
     Then close the entry.
```

## DEPENDENCIES

PHASE B waits on (a), measured by the grep at HEAD. PHASE A has none and runs beside IAM-z-1 and IAM-z-3; PHASE B serializes
with them on `.open_deploys/`.

## BOUNDS

```
ONLY the opal-data-schwab ARNs leave bd-exporter-ec2-role. Nothing added; no trust, tag or role change; no bucket created.
You do NOT edit build_canonical_daily.py (its owner's). safe-apply only (NEVER-9); the NEVER-2 entry opens first, closes last.
STANDING (Z-S40): the survey names its read time; the act re-reads its baseline before it applies.
G-21: no alert, monitor or schedule.  G-25: no Access Analyzer.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
infra/aws/terraform/bd-pipeline/iam.tf
.claude/skills/49-schwab-conv/SKILL.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round9/schwab/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-z-2.schwab-reader-then-grant.md
</paths>

Surprise rows: id `NFRA_IAMROLES202609-Z-S<k>` (next free k), `"fabric": "site-z"`. Commit through `.tools/safe-commit.sh` under
your own author line. At the end, flip this order's LAST `<status>` to `complete` with a proof instance in your deliverables
directory (`to_id` NFRA_IAMROLES202609.TO-IAM-z-2).

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-z-2"><invocation>grep -c 'Bucket=SRC_BUCKET' data/canonical/schwab/build_canonical_daily.py</invocation><expect>`0` -- the canonical builder no longer lists the dead bucket (the owner's act, landed before the narrowing)</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-z-2"><invocation>bash -c ".tools/aws iam get-account-authorization-details --output json > /c/tmp/z2_auth.json && python 'org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/2.0.0_SA_COO~ZI/checks/round9/allow_names.py' /c/tmp/z2_auth.json opal-data-schwab opal-data-portal-v2"</invocation><expect>`opal-data-schwab=0`, and `opal-data-portal-v2=` 30 or more beside a `DENOMINATOR:` line (a failed read exits 2, never a zero)</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-z-2"><invocation>bash -c "echo open=\$(ls -a org/critical_paths/.open_deploys/ | grep -c 'iamroles-r9-narrow-schwab') closed=\$(grep -l '^\*\*Status:\*\* CLOSED' org/critical_paths/change_management/*iamroles-r9-narrow-schwab* 2>&1 | grep -c '\.md\$')"</invocation><expect>`open=0` and `closed=1`</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-z-2" judgment="true"/>
</proof_of_spec>

- **AC4** (JUDGMENT, never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason naming 3.0.0_SA_CVO~Z): did the reader
  leave before the grant, and does any path remain by which a claimant's bytes reach the canonical Schwab build?

Every invocation runs under `timeout 120`, except AC2, whose account-wide read takes up to 300 seconds.

<!-- ===================== RECORD FACE -- does NOT travel to the assignee ===================== -->

<status>pending</status>
<round>9</round>
<slot>0.7.0_AE_CloudOps~IR</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZI</issued_by>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<to_id>NFRA_IAMROLES202609.TO-IAM-z-2</to_id>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 9) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @3cadaf52ca (L4-R GRANDFATHERED per `prd-signoff.py status`)
**Authority chain:** round-8 slug (msg 33357) -> `ROUND_ANALYSIS.round8.md` @d14162158d E2 (msg 33361) -> L5 round-9 decomp -> this issuance. Act (a) routed to `0.0.0_AB_MSTR~Z` for the owner the same tick.
**Risk WORLD:** a permission narrowing on the bd gold-layer runner's role, behind another owner's code change.
<preflight>
comp-schedule: RUN -- PARTIAL_OR_BLIND at the round-7 read; the assignee reads .open_deploys/ for bd-pipeline before its entry opens.
comp-iam: RUN -- live read at the cut (checks/round9/allow_names.py): opal-data-schwab=1 (bd-exporter-ec2-role); control opal-data-portal-v2=38.
comp-adversary: RUN -- recut taken as GIVEN; denominator of re-derived premises 2 of 2, 1 CORRECTED: the reader is latest_rps_date() at :141-145 (+ :48, :228), not :154-156, which dates_to_build() vacated @3b01132271; the name is 404 per the sweep.
</preflight>

**Preflight disposition:** checks dry-run at the base: AC1 base FAIL as expected (`1`); AC2 base FAIL as expected (opal-data-schwab=1); AC3 base FAIL as expected (`open=0 closed=0`).
