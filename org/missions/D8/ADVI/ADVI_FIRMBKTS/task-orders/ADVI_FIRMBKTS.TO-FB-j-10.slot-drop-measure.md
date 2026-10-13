# ADVI_FIRMBKTS task order -- `FB-j-10` -- DEPLOY THE SLOT-DROP LOGGING (SCOPED, UNDER ITS PAIR ADDENDUM) AND READ WHY EVERY SLOT IS DROPPED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R7.md</decomp_doc>
<owned_cells>FB-j-10</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no rule, schedule or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- the actor's own identity reads and runs `safe-apply` scoped to one function's code; one `lambda:InvokeFunction` with `dry_run: true`; no grant is added.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects a changed listing across the dry run, a record with no drops, a cause class outside the closed set, a message over 200 characters and an unclosed ledger entry. Blindness: the record proves what the log held, not that the fix is right.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `FB-j-10` (round 7; the CTO's ruling on `D1-S48`, ROUND_ANALYSIS.round3.md ADDENDUM 14)

`FB-j-9` makes every dropped slot print `[SLOT_DROPPED] slot=<s> exc=<Class> msg=<text>` (the class, and at most 200 characters of message,
`redacted` for PII, schema and URL errors). You deploy that code and read the cause: ONE dry run for TEN pre-screened advisors, then
the function's own log and the returned bullets. No served object is written.

### 1a. Steps

1. **Preconditions (read, each recorded):** `FB-j-9` is merged and its criteria PASS at the merged HEAD; the pair covers a SECOND apply of this
   function's code: the COO half `ledger/NEVER_WIDEN_ROUND7_EXEC_SUMMARY_DRYRUN_DEPLOY_COO_HALF.md` ADDENDUM 1 and the CTO's matching
   addendum, both signed at the current bytes (name both commits). Read the addendum first: it fixes what you may touch.
2. **Entry** (NEVER-2) with its `.open_deploys/` sentinel BEFORE the first write: current `CodeSha256` (the FB-j-6 artifact,
   `qVCUzRtwZxKSrql+JapMKH4wwoAd2+aSB0FyZ470ZkU=`), prior artifact VersionId, the pair, the rollback.
3. **Build:** `bash infra/aws/lambda/ci/build-and-upload.sh exec-summary exec-summary-generator`; print the sha256. Then
   `python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_execeq2.py --zip-prior <deployed.zip> --zip-new <built.zip>` must read `EXEC READS: prior and new canonical EQUAL`.
4. **Plan, scoped:** in `infra/aws/terraform/exec-summary`, `.tools/safe-apply.sh`'s plan limb with
   `-var platinum_mode=canonical -target=aws_lambda_function.exec_summary_generator`: `0 to add, 1 to change, 0 to destroy`, the code hash the
   only diff, environment unchanged. Anything else: STOP, a BLOCKING row.
5. **Apply** on that saved plan; read back `CodeSha256` equals the artifact's and the environment unchanged.
6. **List** the served prefix `advi/49financial/platinum/advisors/*/exec_summary.json` (key, LastModified, VersionId; count and a sha256 of the text).
7. **ONE dry run:** `{"dry_run": true, "advisor_ids": [<10 ids from SLOT_PRESCREEN.json targeted_ids, spread over the slots that fire>]}`. The CTO requires the bullets to be NON-EMPTY. Read the function's log group for that
   invocation's `[SLOT_DROPPED]` lines (CloudWatch `filter-log-events`, the invocation's request id). Count drops per exception class and keep up to
   five distinct `msg=` texts verbatim (each at most 200 characters; they carry no advisor content by construction).
8. **List again**: identical (0 objects written), else ROLL BACK to the prior artifact the same turn and report.
9. **The sample for reading (the CTO reads it and it goes to Andrew):** write `DRYRUN10_ARTIFACTS.json` (the returned artifacts, per advisor id) and
   `DRYRUN10_FIGURES.json`: for EACH returned bullet, the slot, its `headline` and `detail` text verbatim, and the FIGURES it rests on, read
   from the objects its `evidence_keys` name in the canonical home (for a position slot: the ticker, the percentage or amount fields the
   text cites; for a leaderboard or NNA slot: the ranks or flow figures). One row per bullet, so a reader can lay text beside figure. If
   an artifact carries a client name, record the count and withhold that text. Do not judge the text: the CTO does.
10. Close the entry. Do NOT invoke without `dry_run`.

### 1b. The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/SLOT_DROP_CAUSE.json`

```json
{"order": "FB-j-10", "read_at": "<ISO UTC>", "calls": ["aws lambda invoke ...", "..."],
 "deployed_version": "CodeSha256 ...", "pair": {"coo_half_addendum": "<commit>", "cto_half_addendum": "<commit>"},
 "ledger_closed": true, "advisors": 3, "listing_before": 158, "listing_after": 158,
 "drops": 0, "classes": {"TypeError": 0}, "messages": ["<verbatim, at most 200 characters>"],
 "bullets_returned": 0, "cause_class": "CONFIG | PRODUCT | NOT_KNOWN", "cause_reason": "<two sentences>", "claim": "measured"}
```

`cause_class`: `CONFIG` for a model id, key, quota or SDK-usage cause (the CTO fixes those here under a pair); `PRODUCT` for a cause in
the product's own logic or content rules (a CRO brief); `NOT_KNOWN` only when the log holds no `[SLOT_DROPPED]` line at all.

## 2. BOUNDS

1. One scoped apply of one function's code; ONE dry-run invocation; reads otherwise. No non-dry invocation, no S3 write, no env change.
2. Print no secret and no client name; advisor ids and counts only.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-j-10.slot-drop-measure.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-j-10"><invocation>timeout 30 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_checks.py slotcause --file C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/SLOT_DROP_CAUSE.json</invocation><expect>^SLOTCAUSE record ok drops=[0-9]+ classes=[0-9]+ bullets=[1-9][0-9]*$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and discipline.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-j-10.slot-drop-measure.proof_of_spec.json`. Commit the record FIRST, your rows and the instance second; flip `<status>` to `complete` in the SAME commit only when AC1
passes. Row ids `ADVI_FIRMBKTS-D1-S<k>`. Report once to `2.0.0_SA_COO~B1` and `1.0.0_SA_CTO~DELL1`: the classes with counts, the verbatim
messages, the cause class, AC1 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** PARKED at the cut: owner `2.0.0_SA_COO~B1`; un-park conditions (all): `FB-j-9` merged and PASS; the pair ADDENDUM signed by both
halves (the COO addendum authored by the issuer now; the CTO's addendum asked); the issuer amends `<status>` and messages FB1 citing this order.
The CTO's ADDENDUM 14 shape: "deploy under FB-j-6's shape (0/1/0, platinum_mode=canonical, listing unchanged), then one dry run on three or
more pre-screened advisors". A cause of class CONFIG is fixed in a later cell under its own pair and must prove non-empty bullets; PRODUCT goes
to a CRO brief. The pre-screened ids are `SLOT_PRESCREEN.json`'s `targeted_ids` (FB1's own record of FB-j-8).

**AMENDMENT 1 (2.0.0_SA_COO~B1, 2026-10-13 ~10:2xZ):** the pair addendum is signed on both sides: the COO addendum 1 at 78a9c61182 (`ledger/NEVER_WIDEN_ROUND7_EXEC_SUMMARY_DRYRUN_DEPLOY_COO_HALF_ADDENDUM_1.md`) and the CTO's ADDENDUM 3 of his FB-j-6 half at f6ded5f20a ("same shape as FB-j-6, carrying FB-j-9's merge; Branch A: non-empty bullets from 10 pre-screened advisors; Branch B: empty again, but the drop log names the cause, and the deploy stands"). Step 9 added: the bullet texts and the figures they rest on go to the CTO, who reads them, and to Andrew, BEFORE `FB-j-7` and `FB-j-4` are cut or un-parked. Still parked on `FB-j-9` merged and PASS only.

**AMENDMENT 2 (2.0.0_SA_COO~B1, 2026-10-13 ~10:4xZ) -- UN-PARKED:** `FB-j-9` is merged at 8fcbf07d7d (worker commit 2deaa9165e; its four arms PASS at the merged HEAD together with `FB-j-5`'s three: 7 passed; the `betas` mutant fails arm 4, the helper-call mutant fails arm 1; instance VALID). The diff you deploy: `betas=[...]` removed from the `client.messages.create(...)` call; `_log_slot_drop` and its two call sites (message `redacted` for PII, schema and URL classes; ASCII only). The pair addendum is signed on both sides (COO 78a9c61182, CTO f6ded5f20a). Build from the main checkout at or after 8fcbf07d7d. Status pending. No criterion changed.

<status>complete</status>
<round>7</round>
<workstream>SLOTDROPLOG</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-j-10</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
