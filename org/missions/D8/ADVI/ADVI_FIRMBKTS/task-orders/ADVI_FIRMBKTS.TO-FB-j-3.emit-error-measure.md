# ADVI_FIRMBKTS task order -- `FB-j-3` -- DEPLOY THE TEXT-ONLY DISPATCHER AND READ THE NEXT CHAIN'S WARN (THE MEASUREMENT)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R7.md</decomp_doc>
<owned_cells>FB-j-3</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no rule, schedule or cadence is added or changed; no cron, rule, schedule or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- one `s3:PutObject` of one key the runner role already syncs, by the actor's own identity (read at the act); no grant.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects an unclosed ledger, a deployed object that does not equal the repo, a named cause with no verbatim text, a text over 300 characters and a write other than the one copy.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `FB-j-3` (round 7, enrichment item 2, step 1: the measurement)

`FB-j-2` changes the dispatcher's WARN to carry the CLI's error text (300 characters) and nothing else. You deploy that one file to the
runner's code prefix and read the next chain's WARN. No served output moves; the point is to turn "REGION_UNSET (inferred)" into a
measured error text, or to refute it.

### 1a. Steps

1. **Preconditions (read):** `FB-j-2` is merged (its commit is on the branch you work from) and its three criteria read PASS at the merged
   HEAD; `git show HEAD:data/black_diamond/scripts/gold/gold_dispatch.sh` carries the new WARN. Record the sha256 of that file.
2. **Ledger:** open an entry in `org/critical_paths/change_management/` (NEVER-2): the object, its prior ETag and VersionId (bucket
   `opal-data-bd`, key `code/gold/gold_dispatch.sh`), the rollback (copy the prior VersionId back). Name every consumer of the key (the
   runner syncs `code/gold/` at chain start and self-fetches the dispatcher; `bd-gold-qa-runner` shares it).
3. **Deploy:** `aws s3 cp <repo file> s3://opal-data-bd/code/gold/gold_dispatch.sh --sse AES256`, read it back (`get-object`, sha256 equals the
   repository file). The push hook never ships `.sh`; this copy is the deploy. No other object is written.
4. **Read the next chain:** the first chain that closes after the deploy (the nightly fallback `cron(0 23 ? * MON-SAT *)` or an S3-triggered
   run). Read its log (`gold/logs/` and the runner's cumulative log `logs/gold-layer/gold_incremental_*.log`) for the WARN line. Record the
   WARN's `rc=` and text VERBATIM (it is at most 300 characters of CLI output; it holds no secret). Classify: `NO_REGION` (a "must specify a
   region" class text), `CREDENTIALS`, `OTHER_NAMED` (any other text, verbatim), or `NOT_OBSERVED` (the chain did not reach the emit, or it
   emitted successfully: say which).
5. **Close the ledger entry** when the read is recorded. If the chain has not run when your window ends, the order stays open: say so.

### 1b. The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/EMIT_ERROR_TEXT.json`

```json
{"order": "FB-j-3", "read_at": "<ISO UTC>", "calls": ["aws s3api get-object ...", "..."],
 "deployed": {"key": "code/gold/gold_dispatch.sh", "sha256": "<64 hex>", "equals_repo": true, "prior_version_id": "..."},
 "ledger": {"entry": "<path>", "closed": true},
 "next_chain": {"label": "...", "started_at": "<ISO UTC>"},
 "warn_text": "<the verbatim text, at most 300 characters, or null when NOT_OBSERVED>",
 "cause_class": "NO_REGION | CREDENTIALS | OTHER_NAMED | NOT_OBSERVED",
 "claim": "measured"}
```

## 2. BOUNDS

1. ONE object is written (the dispatcher). No other write, no instance start or stop, no SSM command (the manifest bars it), no `put-events`.
2. Print no secret. If the deploy cannot be read back equal, restore the prior VersionId the same turn and report.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-j-3.emit-error-measure.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-j-3"><invocation>timeout 30 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_checks.py emiterr --file C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/EMIT_ERROR_TEXT.json</invocation><expect>^EMITERR record ok cause_class=(NO_REGION|CREDENTIALS|OTHER_NAMED|NOT_OBSERVED)$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and discipline. The text's truth is read by the issuer from the cited log.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-j-3.emit-error-measure.proof_of_spec.json`. Commit the record FIRST, your rows and the instance second; flip `<status>` to `complete` in the SAME commit only when AC1 passes. Row ids `ADVI_FIRMBKTS-D1-S<k>`. Report once to `2.0.0_SA_COO~B1`: the cause class, the verbatim text, AC1 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** PARKED at the cut: owner `2.0.0_SA_COO~B1`; un-park condition: `FB-j-2` merged and its criteria PASS at the merged HEAD (the issuer amends `<status>` to `pending` and messages FB1 citing this order). The measurement is a code deploy with no served effect: no never-widen pair; NEVER-2 ledger applies. The CTO's round-6 section 2 item 1 asked for it on the runner host; the manifest bars SSM there, so the dispatcher itself carries the text out in the chain log.

**AMENDMENT 1 (2.0.0_SA_COO~B1, 2026-10-13 ~09:0xZ) -- UN-PARKED:** `FB-j-2` is merged at e33708f50b (worker commit f313505d5c; its three criteria PASS at the merged HEAD: `r7_emit_test.sh` 3 of 3, `awsdiff` OK, scope OK; instance VALID). Precondition 1 of section 1a is met: `git show HEAD:data/black_diamond/scripts/gold/gold_dispatch.sh` carries the new WARN (the diff is two hunks inside `emit_chain_complete`: the output captured in a variable, the WARN printing `rc=<rc>` and the first 300 printable characters). Work from the main checkout's `box/dell1` at or after e33708f50b. No criterion changed.

<status>complete</status>
<round>7</round>
<workstream>EXECSUMFIX</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-j-3</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
