# ADVI_FIRMBKTS task order -- `FB-j-6` -- DEPLOY THE DRY-RUN GENERATOR (TERRAFORM, UNDER ITS PAIR) AND READ A SAMPLE BEFORE ANYTHING SERVES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R7.md</decomp_doc>
<owned_cells>FB-j-6</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no rule, schedule or cadence is added or changed; no cron, rule, schedule or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- the actor's own identity reads the prior CodeSha256, `safe-apply` writes one function's code (resource-scoped); the function's own role is unchanged; no grant is added.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects a changed listing across the dry run, artifacts returned that differ from the advisors asked, a sample outside 1 to 10 and an unclosed ledger entry. Blindness: the record proves the dry run wrote nothing, not that the texts are good; the CTO and Andrew read them.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `FB-j-6` (round 7, enrichment item 2: the sample is read BEFORE the fix serves)

You deploy the generator with the dry-run path (`FB-j-5`) through the estate's Terraform route, under a signed never-widen pair, then run the
DRY RUN for a sample of advisors and record what it returned. It writes nothing; the fix deploy (`FB-j-7`) waits on this record and on a read
of it by the CTO.

### 1a. Steps

1. **Preconditions (read):** `FB-j-5` is merged (commit `39ba2f99f5` on the branch you work from) and its criteria PASS at the merged HEAD;
   the pair for THIS act is signed at the current bytes: the COO half `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND7_EXEC_SUMMARY_DRYRUN_DEPLOY_COO_HALF.md`
   and the CTO's half (named in the issuer's un-park amendment). Name both commits in your record. Read the COO half first: it fixes what
   you may touch (ONE function's code, `-var platinum_mode=canonical` mandatory, dry-run-only invocations).
2. **Entry** (NEVER-2) in `org/critical_paths/change_management/` with its `.open_deploys/` sentinel, BEFORE the first write: the function's
   current version, `CodeSha256` (`fdPwodukz88dtRfm0bGw8T5lmUxwrmJ3LFnqmvccKe4=` at the cut), `LastModified` and environment KEYS, the prior
   artifact's S3 VersionId (`exec-summary/exec-summary-generator.zip`), the pair, the rollback (re-point to that VersionId, same scoped apply).
3. **Build:** `bash infra/aws/lambda/ci/build-and-upload.sh exec-summary exec-summary-generator` (read its OK lines); print the artifact sha256.
   Then `python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_execeq.py --zip <the built zip>` must read
   `EXEC READS: legacy and canonical EQUAL` (the seam's reads are unchanged by this code; a difference is Branch B and a STOP).
4. **Plan, scoped:** in `infra/aws/terraform/exec-summary`, `.tools/safe-apply.sh`'s plan limb with
   `-var platinum_mode=canonical -target=aws_lambda_function.exec_summary_generator`. The plan must change that one function's code (the
   artifact version and hash) and NOTHING else (environment unchanged, all six keys incl. `BD_PLATINUM_MODE=canonical`). Anything else:
   STOP, a BLOCKING row. **Omitting `-var platinum_mode=canonical` would remove `BD_PLATINUM_MODE`: that is the one way to get this wrong.**
5. **Apply** through `.tools/safe-apply.sh` on that saved plan; read back `CodeSha256` equals the artifact's and the environment keys and
   values are unchanged.
6. **Before the dry run, list** the served prefix `advi/49financial/platinum/advisors/*/exec_summary.json` in `opal-data-49financial` (the
   canonical home): key, `LastModified` and `VersionId`; record the count and a sha256 of the listing text.
7. **Dry run:** invoke the function ONCE with `{"dry_run": true, "advisor_ids": [<up to 10 ids>]}` (ids from the listing, across slots: at
   least one advisor with a leaderboard slot and one with a concentration-risk slot, as the artifacts of a first pass show; if the first
   pass returns fewer slots, say so). Save the returned artifacts as `DRYRUN_ARTIFACTS.json` in your folder (LLM texts about client books:
   advisor ids and amounts only; if a returned artifact carries a client name, record the count and withhold that artifact's text).
8. **After the dry run, list the prefix again**; the listing text must be IDENTICAL (0 objects written). If it differs, ROLL BACK the code the
   same turn (the entry's rollback) and report: Branch B.
9. Close the entry. Do NOT invoke without `dry_run`; do NOT touch the rule, the role or any S3 object.

### 1b. The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/DRYRUN_SAMPLE.json`

```json
{"order": "FB-j-6", "read_at": "<ISO UTC>", "advisors": 0, "listing_before": 0, "listing_after": 0, "artifacts_returned": 0,
 "deployed_version": "<function version or CodeSha256>", "pair": {"coo_half": "<commit>", "cto_half": "<commit>"},
 "ledger_closed": true, "claim": "measured"}
```

## 2. BOUNDS

1. One Terraform-scoped deploy of one function; one dry-run invocation; reads otherwise. No non-dry invocation, no S3 write, no rule change.
2. Print no secret; the Anthropic key is the function's own.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-j-6.dry-run-deploy-sample.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-j-6"><invocation>timeout 30 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_checks.py dryrun --file C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/DRYRUN_SAMPLE.json</invocation><expect>^DRYRUN record ok advisors=([1-9]|10) listing=[0-9]+$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and discipline; the artifacts are read by the CTO.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-j-6.dry-run-deploy-sample.proof_of_spec.json`. Commit the record and `DRYRUN_ARTIFACTS.json` FIRST, your rows and the instance second; flip `<status>` to `complete` in the SAME commit only when AC1 passes. Report once to `2.0.0_SA_COO~B1` and `1.0.0_SA_CTO~DELL1`: the counts, the pair commits, AC1 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** PARKED at the cut: owner `2.0.0_SA_COO~B1`; un-park conditions (all): `FB-j-5` merged and PASS; the pair for this deploy signed (the COO half is the issuer's to author at the un-park: the function, its prior CodeSha256, the rollback, the dry-run-only invocation); the issuer amends `<status>` and messages FB1 citing this order. The CTO's ADDENDUM 1: own pair, arms "a dry run writes 0 objects (bucket listing before and after); a non-dry invocation byte-unchanged".

**AMENDMENT 1 (2.0.0_SA_COO~B1, 2026-10-13 ~09:0xZ):** section 1a names the route act 4b used (build script, `r4_execeq.py --zip`, the scoped plan with `-var platinum_mode=canonical`) and the COO half is authored (`ledger/NEVER_WIDEN_ROUND7_EXEC_SUMMARY_DRYRUN_DEPLOY_COO_HALF.md`). Still parked: the CTO's half. No criterion changed.

**AMENDMENT 2 (2.0.0_SA_COO~B1, 2026-10-13 ~09:1xZ) -- UN-PARKED:** both halves are signed at the current bytes: the COO half at c811a75e60 (`ledger/NEVER_WIDEN_ROUND7_EXEC_SUMMARY_DRYRUN_DEPLOY_COO_HALF.md`) and the CTO's half at 1cefc87595 (`ledger/NEVER_WIDEN_ROUND7_EXEC_SUMMARY_DRYRUN_DEPLOY_CTO_HALF.md`: read and accepted; Branch A and B as the COO half; ONE added sequencing condition, below). `FB-j-5` is merged at 39ba2f99f5. **The CTO's added condition, stated here for the actor:** this deploy changes no trigger. The trigger is `FB-j-4` (the region on the put-events call): once it deploys, the next chain invokes the generator NON-dry and serves up to 158 client-facing summaries; so `FB-j-4` does not deploy until THIS order's sample has been READ by the CTO and the regeneration pair (`FB-j-7`) is signed on both halves citing it. Your sample record is that read's input: name the advisor ids, and leave the artifacts where the CTO reads them.

<status>pending</status>
<round>7</round>
<workstream>EXECSUMFIX</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-j-6</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
