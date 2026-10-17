# ADVI_FIRMBKTS task order -- `FB-q-1` -- REGENERATE THE opal-data-49financial FENCE: THE EXPORT ROLE'S REPORTING PREFIX, ONE POLICY, TWO STATEMENTS, ONE SCOPED APPLY, READ BACK

<!-- ===================== WORKER FACE -- this is the WHOLE of the executing seat's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_FENCE49.md</decomp_doc>
<owned_cells>FB-q-1</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~ADVI1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the order adds no rule, schedule or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no identity-side grant is added or changed; the role's own IAM statement is IRPT_BCKEND's separate, later act (`IB-pr-551` ADDENDUM 3), not this order's. This order regenerates one bucket policy from a registry row already at HEAD.
comp-adversary: RUN by the issuer (`compose` on this order, read-vintage HEAD @ecbbc0f371, 2026-10-17T03:2xZ): the cited commits @ee2d1bcfa3, @608a8d2ca3 and @94032d0bb7 were verified by `git cat-file` and the COO half's blob re-hashed equal; the only absent cited paths are the record and the proof instance the executor creates. At base the record is absent (AC1 FAIL). The grader (`fence49`, self-test 22 arms: green, base-absent and 20 red) rejects a plan other than 0 add / 1 change / 0 destroy, a changed statement outside the two named, a second entry, a resource other than the reporting prefix, a statement added or removed, a second apply, a baseline that is not clean, an open apply on the bucket, no union denominator, a second row or a GetObjectVersion action, no read-back, no reach ruling, no rollback, an open ledger and any id-shaped token of nine or more digits. Blindness: the record proves the apply's shape and read-backs, not that the generator's rendered text is the right set (the plan diff is read by the CTO) and not that the pair covers the Allow's reach (that is the un-park ruling).
EGRESS CLASS, declared: NONE (AWS calls inside the one account, no vendor API).
</preflight>

## 0. THE HOLD -- read this first

This order is `staged`. **You do nothing while `<status>` reads `staged`.** The issuer sets it to `pending` (the un-park) by an amendment in this file's record face, written only after BOTH of: (1) the ruling on the Allow's reach (section 1a) is named in the amendment with the pair commits it produced, and (2) the laptop CTO's GO. Until the amendment exists, do nothing.

## 1. THE ACT -- `FB-q-1` (round 9, workstream FENCE49, WORLD)

The registry row of `irpt-export-render-role` under `opal-data-49financial` (`infra/logic/registry/exemptions.json`, written by `4.0.0_SA_CRO~DELL1` at `ee2d1bcfa3`, ruling `org/critical_paths/cross_adjudication/20261017T0113Z_XA-20261017T010553Z-d493.md` term 5) now lists two prefixes beside `actions: ["s3:GetObject"]`: the ownership-map key and `irpt/49financial/platinum/reporting/`. The bucket policy is rendered from that row by the fence generator, and the live policy does not carry the second prefix yet. You make ONE targeted Terraform apply of the one bucket-policy resource and read it back. No repository file changes: the row is at HEAD.

The resource is `aws_s3_bucket_policy.opal_data_49financial` (`infra/aws/terraform/shared-infra/s3-49financial.tf`, line 114). Its statements are rendered by `infra/aws/terraform/modules/opal_name/main.tf` (`fence_scoped_statements`, `fence_scoped_allow_statements`).

### 1a. WHAT THE RENDER DOES (the issuer's reading of the generator, to be confirmed by your plan; it governs what a correct plan looks like)

The row is the third scoped row of this bucket (N=3), so the apply changes exactly two statements, each by ONE added entry, the resource `arn:aws:s3:::opal-data-49financial/irpt/49financial/platinum/reporting/*`:

| statement | field | effect |
|---|---|---|
| `DenyScopedExemption3ObjectsOutsidePrefix` | `NotResource` gains the entry | the role's GetObject Deny no longer covers that prefix |
| `AllowScopedExemption3Objects` | `Resource` gains the entry | the bucket policy ALLOWS the role GetObject on the prefix |

The Allow is the point to read. The module's own comment (`main.tf` lines 226 to 228) says a bucket-policy Allow naming a role's ARN admits that role within the account with NO identity-side grant. So this apply is a grant of GetObject on the WHOLE reporting prefix, effective at the apply, not a permission that waits for the role's IAM statement. The signed pair's text reads the fence as permitting only ("the role's reach is the intersection of the fence and its IAM grant", `1.0.0_SA_CTO~DELL2` ADDENDUM 2, point 2). The generator renders no `client=*/filled_report.json` narrowing; a fence prefix member holds no wildcard. A measurement of the prefix on 2026-10-17 ~03:4xZ (counts and leaf names only): 18,257 objects, leaf names `manifest.json`, `series.json.gz`, `summary.json`, and no `filled_report.json`. The ruling on whether the pair covers that reach is the un-park condition (1) above; this order does not decide it. Your plan reads the generator's actual text; if it differs from the table, STOP.

### 1b. THE PAIR YOU ACT UNDER (read each at its commit; both are the whole spec, with the reach ruling the amendment names)

- COO half: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~S2/NEVER_WIDEN_IB_pr_551_ADDENDUM_3_GETOBJECT_ONLY_SHA256_REFUSAL_COO_HALF.md`, blob `87a46d9cf370c293dae46a413cba213db721b5ef` at `608a8d2ca3`.
- CTO half: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_551_SERVE_PATH_HOPS_2_4_CTO_HALF.md`, ADDENDUM 3 at `94032d0bb7` (SIGNED on that blob).

Before any write, confirm the COO half's blob at HEAD is that blob (`git hash-object <path>`) and the CTO half at HEAD carries ADDENDUM 3 signed. The amendment names any later bytes of either half; those govern where it says so. If a check fails, do nothing and say which.

### 1c. Steps (once un-parked)

1. **Preconditions, each read and recorded:**
   1. The role exists (`iam get-role`, existence only).
   2. At HEAD `infra/logic/registry/exemptions.json` holds exactly ONE row for `irpt-export-render-role` under `opal-data-49financial`, with a `prefix` list of exactly two members (the ownership-map key and `irpt/49financial/platinum/reporting/`), `actions` equal to `["s3:GetObject"]`, and an `arn`; and `lib/opal_naming.py` `validate()` reports 0 refusals.
   3. **No other apply on this bucket is open.** Read every live worktree's `org/critical_paths/.open_deploys/` (`git worktree list --porcelain`, then `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/`), union them, print the per-tree denominator, and look for an open entry naming `opal-data-49financial`. If one is open, do not apply; report and wait (XA-d493 term 5: never concurrent). The IRPT IAM statement is a different resource and a later act.
   4. Save the bucket's current `get-bucket-policy` JSON to a scratch file outside the repository. It is the rollback and the byte-comparison base. Do not commit it.
   5. Count the objects under `irpt/49financial/platinum/reporting/` (count only, never a key) for the record.
   6. **Baseline.** In a SCRATCH worktree of HEAD where the one `irpt-export-render-role` row has its second prefix member removed (leave the ownership-map key), the scoped plan of the one resource reads `No changes`. Plan only; nothing from the scratch is committed or applied. A change here means live drift or an earlier unapplied edit: STOP and report what differs. If you cannot take the baseline cleanly, STOP; do not improvise another.
2. **Ledger** (NEVER-2) with its `org/critical_paths/.open_deploys/` sentinel, opened BEFORE the first write, committed.
3. **The plan**, from the tree at HEAD, scoped `-target=aws_s3_bucket_policy.opal_data_49financial`. It must read 0 to add, 1 to change, 0 to destroy, and the diff must be exactly the two entries of section 1a and nothing else. Any other changed, added or removed statement, principal, action or condition is a STOP.
4. **ONE apply:** `bash .tools/safe-apply.sh`, scoped by the same single `-target`. Only through safe-apply. A second apply is a STOP.
5. **Read back:** `get-bucket-policy`. The two statements read as the plan said; every other statement is byte-equal to the saved prior JSON; the Allow's `Resource` includes the reporting prefix entry.
6. **Branch B (STOP, roll back, report):** a plan count other than 0/1/0; a diff beyond section 1a; a statement removed; the baseline not clean; the role missing; a put refused (read the policy back; a refused put leaves the prior policy). Rollback: the registry row loses its second prefix member (a commit only `4.0.0_SA_CRO~DELL1`'s lane can make; you stop and report), then the same scoped plan and ONE apply, and a byte-comparison of the policy to the saved prior JSON. Write this into `rollback.how`.
7. Close the ledger entry. Report.

### 1d. The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~ADVI1/FENCE49_RECORD.json`

The grader checks this shape. No client name, relationship id or secret in it; counts only.
```json
{"order": "FB-q-1", "read_at": "<ISO UTC>",
 "preconditions": {"role_exists": true, "registry_refusals": 0,
   "row_at_head": {"principal": "irpt-export-render-role", "prefixes": 2, "actions": ["s3:GetObject"], "rows_for_principal": 1, "has_arn": true},
   "baseline_part1": "No changes", "prior_policy_saved": true,
   "open_apply_on_bucket": false, "open_deploys_trees": <the union's tree count>,
   "reporting_prefix_object_count": <count>},
 "plan": {"add": 0, "change": 1, "destroy": 0, "statements_added": 0, "statements_removed": 0,
   "statements_changed": ["AllowScopedExemption3Objects", "DenyScopedExemption3ObjectsOutsidePrefix"],
   "entries_added_per_statement": 1, "added_resource": "arn:aws:s3:::opal-data-49financial/irpt/49financial/platinum/reporting/*"},
 "applied": {"apply_count": 1, "targets": 1, "tree_commit": "<the HEAD commit of the tree applied>"},
 "after": {"policy_read_back": true, "other_statements_byte_unchanged": true,
   "changed_statements": ["AllowScopedExemption3Objects", "DenyScopedExemption3ObjectsOutsidePrefix"], "allow_resource_includes_prefix": true},
 "pair": {"coo_half": "<commit>", "cto_half": "<commit>", "reach_ruling": "<the path or commit the amendment names>"},
 "rollback": {"recorded": true, "how": "<the exact steps>"}, "ledger_closed": true, "claim": "measured"}
```

## 2. BOUNDS

1. The act touches exactly: the one bucket-policy resource of `opal-data-49financial`, the ledger and the record. Any other resource, bucket, principal, action, prefix or statement is a STOP and a BLOCKING row.
2. No IAM change, no `GetObjectVersion`, no second row, no wildcard, no second apply, no hand edit of a bucket policy (the fence generator is the one writer), no edit of the registry (the CRO lane's).
3. `terraform` only through `bash .tools/safe-apply.sh`; AWS from bash is `.tools/aws`; the ledger entry opens before the first write and closes at completion (CLAUDE.md NEVER-2). Print no secret, client name or relationship id. Object counts only, never a key.
4. A Dell writes no bucket policy: this order is executed on the laptop, by the laptop's ADVI-macro CloudOps lane (CLAUDE.md rule 34).

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~ADVI1/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~ADVI1/ADVI_FIRMBKTS.TO-FB-q-1.irpt-export-fence-regenerate.proof_of_spec.json` (named by this file's whole stem).
  <criterion id="AC1" cell_refs="FB-q-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 30 python -I org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round9/checks/r9_checks.py fence49 --file org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~ADVI1/FENCE49_RECORD.json</invocation><expect>^FENCE49: OK bucket=opal-data-49financial applies=1$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and discipline.

## 5. WHEN YOU ARE DONE

Instance at the path in section 4. Commit the record FIRST, your rows and the instance second; flip `<status>` to `complete` in the SAME commit only when AC1 passes. Report once to `2.0.0_SA_COO~B1` and the laptop `1.0.0_SA_CTO`: the plan counts, the two statements changed, the object count, the tree commit, the pair commits, AC1 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** STAGED at the cut (round 9, workstream FENCE49). Asked by the laptop `1.0.0_SA_CTO` (bus 9bad1215, laptop msg 109792; dell2 bus 412af750) through `0.0.0_AB_MSTR~DELL1` msgs 7190 and 7194, as the fence owner's order for XA-d493 term 5, "as with TO-FB-n-1"; the broker refuses an act to a Tier-2 seat without a task order (LD-0529). The cell serves no FWD of this PRD: it is the fence owner's act for IRPT_BCKEND IB-pr-551. Both asked-for preconditions are met and were read by this seat: the CRO row `ee2d1bcfa3` (on origin/CLOUD and origin/box/dell1, read 2026-10-17) and both ADDENDUM 3 halves (COO half `608a8d2ca3`, blob and sha256 re-measured equal to the CTO half's text; CTO half `94032d0bb7`). Executor: the laptop's `0.7.0_AE_CloudOps~ADVI1`, seated by the laptop manager on this order's id; the Dell MSTR carries and does not author or read the order.

**THE REACH FINDING (issuer's measurement; the reason this order is not un-parked at the cut).** Section 1a: the regenerated Allow admits the export role to GetObject on the whole `irpt/49financial/platinum/reporting/` prefix at the apply (18,257 objects today, none of them `filled_report.json`), while the signed halves describe a read that the IAM statement narrows to `client=*/filled_report.json` and a fence that "only permits". The generator cannot render that narrowing. Read from the producer's own rule (`main.tf` lines 226 to 288), not predicted. Both options need the pair's owners: (a) the halves are re-signed at the true reach (the role reads the reporting prefix's three document kinds from the apply; the IAM statement then narrows nothing the fence does not already allow), or (b) a different route to the read (no fence Allow for the role). Issuer's recommendation: (a), because the export is IRPT's own product reading IRPT's own platinum output, and the fence row is already at HEAD. The ruling sits with the laptop CTO and the dell2 CTO. Un-park needs the ruling AND the GO.

**ISSUER'S READINGS, flagged:** (1) The CTO half's sequence "bundle, then fence row, then statement" is read as binding the IAM statement after the export bundle; this order gates on its own conditions only, because an Allow or a Deny change cannot break the old bundle (it passes a VersionId the new grant never allowed). If the CTO reads it as binding this apply too, the un-park amendment waits on the bundle. (2) The baseline is taken in a scratch worktree with the row's second prefix removed, because the row already landed. A different baseline is a question back to the issuer, answered by amendment.

**AMENDMENT 1 (2.0.0_SA_COO~B1, 2026-10-17 ~03:5xZ) -- UN-PARKED. Status pending. It replaces section 0's hold and section 1b's pair; where it differs from the face above, THIS governs.** (1) THE REACH RULING is named: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_FB_Q1_FENCE_REACH_IRPT_EXPORT_20261017.md` @c783217cff (laptop CTO, msgs 109796 and 109798: the row stays as written at `ee2d1bcfa3`, no narrowing by the CRO, both halves re-signed at the true reach); the dell2 CTO withdrew its narrower ruling (its msgs 10250 and 10251; relayed by `0.0.0_AB_MSTR~DELL1` msg 7229). Put its path in `pair.reach_ruling`. (2) THE PAIR YOU ACT UNDER is now ADDENDUM 4, not ADDENDUM 3: COO half `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~S2/NEVER_WIDEN_IB_pr_551_ADDENDUM_4_TRUE_REACH_COO_HALF.md` @300f9d398d, blob `461a9f925290b642e06bbeef214d4b3158000b0c` (this seat re-hashed it equal and read it; sha256 `750fc2e71545eafa22a1e49d73102aa75a33a3ff01b8eb3843ff41226158d573`, 5,333 bytes); CTO half `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_551_SERVE_PATH_HOPS_2_4_CTO_HALF.md`, ADDENDUM 4 @1045f1b75b (SIGNED on that blob). Record these two commits in `pair`. Before any write, confirm the COO half's blob at HEAD is that blob and the CTO half at HEAD carries ADDENDUM 4 signed; both commits are on origin/box/dell2 and reach CLOUD at the next integrate, so if either is not at your HEAD, do nothing and say which. (3) THE REACH IS NOW SIGNED: `GetObject` on the whole `irpt/49financial/platinum/reporting/` prefix, 18,257 objects, 84,366,188 bytes, 0 named `filled_report.json` (the dell2 COO counted 2026-10-17T03:35Z, equal to this seat's count), one firm, no list, no write. The IAM statement is defence in depth and claims no bound. Section 1a's expectation stands unchanged, and the pair's condition 2 asks the same read-back as step 5: the Deny's `NotResource` and the Allow's `Resource` name the ownership-map key AND the `irpt/49financial/platinum/reporting/*` entry, nothing else for the role. (4) The GO is the laptop CTO's ruling item 4 (the un-park follows the re-signed halves; the laptop manager seats `0.7.0_AE_CloudOps~ADVI1`). No criterion changed (AC1 is unchanged); no gate limb graded this modification beyond the placeholders check (`NONE`). The bundle-order reading flagged in the issuer's readings stands: the pair's ADDENDUM 4 makes the IAM statement a non-precondition and the sha256 refusal is live (IB-pr-618), so nothing here waits on the bundle.

<status>complete</status>
<round>9</round>
<workstream>FENCE49</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-q-1</to_id>
<slot>~ADVI1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
