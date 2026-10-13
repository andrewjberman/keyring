# ADVI_FIRMBKTS task order -- `FB-j-7` -- THE FIX DEPLOY (EVENTS_REGION) UNDER ITS PAIR, AND THE FIRST CHAIN READ: EMITTED, PUTEVENTS, GENERATOR INVOKED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R7.md</decomp_doc>
<owned_cells>FB-j-7</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no rule, schedule or cadence is added or changed; no cron, rule, schedule or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- one `s3:PutObject` of the dispatcher key by the actor's own identity (the runner role already syncs it); no grant is added; the generator's own role writes the named summary keys.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects a sample that wrote objects or was not read before the deploy, a chain with no emitted line or no PutEvents or no invocation, a regenerated count above the ceiling or above 158, unrecorded prior VersionIds, and an unclosed ledger entry. Blindness: the record proves the first chain's mechanics, not that the texts are right; the dry-run sample and Andrew's optional read are that.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `FB-j-7` (round 7, enrichment item 2: the fix, its first chain, and `D1-W65-S1`'s disarm read)

You deploy the dispatcher with the region variable (`FB-j-4`), under the signed never-widen pair, and read the first chain after the
deploy. When the emit works, `exec-summary-generator` fires at every chain close and regenerates up to 158 client-facing summaries: the
pair bounds that.

### 1a. Steps

1. **Preconditions (read, each recorded):** `FB-j-3`'s measured cause is read and the issuer's amendment of this order names it;
   `FB-j-4` merged and PASS; `FB-j-6`'s `DRYRUN_SAMPLE.json` is read by the CTO (his message cited in your record); the pair for THIS deploy
   (the up-to-158 key set, the sample read, the prior VersionIds) is signed by both halves at the current bytes (name both commits).
2. **Before:** list the 158-or-fewer canonical keys `advi/49financial/platinum/advisors/<id>/exec_summary.json` with their current VersionIds
   (this is the rollback list: `rollback_versions.json`, in your folder) and record the legacy home's count.
3. **Ledger** (NEVER-2): the dispatcher object, prior VersionId, rollback (restore the prior VersionId); consumers named.
4. **Deploy:** `aws s3 cp <repo file> s3://opal-data-bd/code/gold/gold_dispatch.sh --sse AES256`; read back equal. Nothing else is written.
5. **Read the first chain after the deploy:** the log line `EventBridge chain-complete emitted`; CloudTrail `PutEvents` from the runner's
   session (>= 1); `AWS/Lambda` `Invocations` of `exec-summary-generator` (>= 1) and its log for errors; then the regenerated keys: count
   the keys whose newest VersionId is newer than the deploy, confirm the count is at most the named ceiling, and read the sample you took
   (the same advisors as `FB-j-6`) against their dry-run artifacts (record equal or differing, by advisor id, not by text).
5b. **No regression, read PER ADVISOR (the CTO's criterion, FB-j-6 CTO half ADDENDUM 2 item 3):** from `rollback_versions.json` (the prior VersionIds) count the advisors whose PRIOR `exec_summary.json` carried at least one bullet (`advisors_with_bullets_before`), and for each such advisor read the regenerated object: a summary that carried bullets before and carries NONE now is a regression (`bullet_regressions` counts them). Any regression is a roll-back trigger (step 6) for THAT advisor's key at least, and a report.
6. **Roll back** (restore the prior VersionIds from `rollback_versions.json`, and restore the prior dispatcher VersionId) if any regenerated
   key is outside the named set, or the count exceeds the ceiling, or the generator errors on more than 5 percent of advisors, and report.
7. Close the ledger entry.

### 1b. The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/FIRST_CHAIN_READ.json`

```json
{"order": "FB-j-7", "read_at": "<ISO UTC>",
 "pair": {"coo_half": "<commit>", "cto_half": "<commit>"},
 "dry_run_sample": {"advisors": 0, "objects_written": 0, "read_before_deploy": true},
 "deploy": {"key": "code/gold/gold_dispatch.sh", "sha256": "<64 hex>", "ledger_closed": true},
 "chain": {"label": "...", "emitted_line": true, "cloudtrail_putevents": 0, "generator_invocations": 0},
 "keys": {"regenerated": 0, "ceiling": 158, "prior_version_ids_recorded": true,
          "advisors_with_bullets_before": 0, "bullet_regressions": 0},
 "claim": "measured"}
```

## 2. BOUNDS

1. ONE object is written by you (the dispatcher). The generator's writes are the pair's named set; nothing outside it is written by you or
   by the chain. No manual invoke of the generator, no instance start or stop.
2. Print no client name, secret or token; decisions by advisor id only.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-j-7.exec-summary-fix-first-chain.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-j-7"><invocation>timeout 30 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_checks.py firstchain --file C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/FIRST_CHAIN_READ.json</invocation><expect>^FIRSTCHAIN record ok regenerated=[0-9]+ invocations=[1-9][0-9]*$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and discipline.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-j-7.exec-summary-fix-first-chain.proof_of_spec.json`. Commit the record and `rollback_versions.json` FIRST, your rows and the instance second; flip `<status>` to `complete` in the SAME commit only when AC1 passes. Report once to `2.0.0_SA_COO~B1` and `1.0.0_SA_CTO~DELL1`: the chain, the counts, the pair commits, AC1 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** PARKED at the cut: owner `2.0.0_SA_COO~B1`; un-park conditions (all): `FB-j-3` read and its cause named in an amendment of this order; `FB-j-4` merged and PASS; `FB-j-6`'s record read by the CTO; the fix pair signed (COO half authored by the issuer at the un-park: the key set, the rollback per key, writers N = 1: the generator; the CTO's half). The CTO's section 2 item 4: closes on the first chain's emitted line, the CloudTrail PutEvents and the generator invoked; `D1-W65-S1` disarms on that read (disarm owner this seat). A join cell: it waits on both the dispatcher chain and the generator chain.

**AMENDMENT 1 (2.0.0_SA_COO~B1, 2026-10-13 ~09:3xZ):** the CTO's ruling on `D1-S47` adds step 5b and the record fields `advisors_with_bullets_before` and `bullet_regressions` (the grader requires the latter to be 0). A further un-park condition: `FB-j-8`'s record read (it measures whether any advisor fires a slot today; if none does, the regeneration rewrites empty artifacts with empty ones and the pair is to say so). FB-j-4 stays blocked behind this order's pair.

<status>parked</status>
<round>7</round>
<workstream>EXECSUMFIX</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-j-7</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
