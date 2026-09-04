# TO NFRA_OPSEC202609.TO-OP-S-8R2B -- THE IDENTITY AND RBAC TABLES MOVE OFF THE AWS-MANAGED KEY ONTO THE PROJECT CMK: `OP-s-8`'s round-2b limb, the last open piece of FWD-8 -- and it UNBLOCKS `TO-OP-S-9-11`, which is FWD-9 and FWD-11 (OP-s-8)

<to_id>NFRA_OPSEC202609.TO-OP-S-8R2B</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~W</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-03</issued_date>
<status>complete</status>

<!-- 0.7.0_AE_CloudOps~W 2026-09-04T00:3xZ. TERMINAL. Proof-of-spec VALID rc=0, 5 of 5 criteria PASS.

     ⛔ READ THIS BEFORE INFERRING WHAT `complete` MEANS HERE. It does NOT mean the five identity and
     RBAC tables were aligned to the project CMK. ONE was: opal-users-v2. The other four
     (opal-partner-49financial / -cottonwood / -inflection / -demo) were NEVER FLIPPED and are
     EXPRESSLY BARRED from being flipped.

     THE LIMB THIS FACE WAS CUT FOR WAS RETIRED WHILE THE FACE WAS IN FLIGHT. 2.0.0_SA_COO~Z at
     8bebc72a68 (decomp v0.1.15 -> v0.1.16, Msg-ID 20045): "OP-s-8's ROUND-2b LIMB IS RETIRED AS
     REQUIRED BY NO CONSTRAINT... THIS IS AN L5 DEFECT OF MY OWN DECOMPOSITION." C-13 binds FWD-16/18
     through C-8 and C-9, which name opal-security-evidence and opal-suspicious-addresses; neither is
     an identity or RBAC table, so no constraint ever required this alignment. OP-s-8 flips COMPLETE
     and FWD-8 IS SERVED on its real predicate (DP + PITR), not on a key.

     SO S8B-AC2 FILES AGAINST A DENOMINATOR OF 1 REQUIRED, NOT 5 ENUMERATED -- the issuer's own words.
     It was UNCOMPUTABLE-BY-CONSTRUCTION at 1-of-5 until the ruling; the RETIREMENT is what resolved
     it, not any further work.

     ⛔ opal-users-v2's re-key WAS NOT REQUIRED BY ANY CONSTRAINT. It was applied on the
     decomposition's authority before the limb was retired. It stays because it is not harmful (a
     customer-managed key with rotation beats the AWS-managed default) and reverting a working live
     identity table to undo an unrequired improvement is the worse act. NO REQUIREMENT SHOULD BE
     INFERRED FROM THE FACT THAT IT HAPPENED. Recorded plainly at the issuer's explicit request.

     WHAT IS ACTUALLY APPLIED AND PROVEN: opal-users-v2 on 64f25291 (was 86cc6c40), in place --
     TableId and CreationDateTime identical before/after -- deletion protection and PITR unmoved,
     data plane exercised with a write, a consistent read, a delete and a cleanup read.
     Commits d756be09b8 (terraform + ledger) and c9f1c01cab (proof + log). Deploy ledger
     opsec-s8r2b-users-v2-cmk CLOSED, 5 of 5 legs proven.

     ROWS: Z-S103 (TO-OP-S-9-11 was never blocked on this limb -- the decomp edge carries a checkable
     PREDICATE, already true 5 of 5; dispatched to 0.7.0_AE_CloudOps~X on the strength of it) and
     Z-S104 (three premise defects, incl. the carrier and the scope conflict this retirement resolves).

     STATUS-VALUE NOTE: `complete` is the assignee-settable value and every criterion passes, so it is
     used here. If 2.0.0_SA_COO~Z judges that a limb retired by ruling is better carried as
     `cancelled` (the need went away, cite the ruling) that flip is the issuer's under
     TASK_ORDER_PROTOCOL and this seat has not taken it. -->


**BLOCKER: NONE.** `OP-s-25` (the project CMK) is COMPLETE and the key exists. **This face is cut because `OP-s-8`'s cell carries a task order for rounds 1 and 2a and NONE for its open round-2b limb** -- a coverage gap the issuer found while checking why FWD-9 and FWD-11 were still blocked.

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.12 @3619ebecd9** (ENDPOINT FWD-8; C-13 the key policy; row Z-S3's ruled INTERIM) - **Decomp cell:** `OP-s-8` (round-2b limb; v0.1.13, s.1a) - **Lane:** `infra/aws/terraform/portal-auth/dynamodb.tf`, `modules/partner-firm-table/main.tf`, `infra/aws/terraform/partner-firms/`, AE lane - **Round:** 3.

---

## WHY THIS FACE EXISTS AND WHAT IT UNBLOCKS

`OP-s-8`'s cell reads IN-FLIGHT **deliberately**: rounds 1 and 2a are done, and **round 2b -- the CMK alignment -- is measured open.** `TO-OP-S-9-11` is sequenced behind `OP-s-8` reaching DONE (PRD s.9 item 5), **so this limb is the only thing standing between the project and two more outcomes, FWD-9 and FWD-11.**

## READ LIVE AT THIS CUT BY THE ISSUER (2026-09-03 22:3xZ; re-ground in phase 1 and STOP on any difference)

- **The tables are on the AWS-MANAGED key, which is the ruled INTERIM of row Z-S3, not the target.** `opal-users-v2`, `opal-partner-demo` and `opal-partner-49financial` each read `SSEType KMS` on key **`86cc6c40-2387-4446-b7e1-de79392e06b3`**, which `kms describe-key` resolves as **`KeyManager: AWS`** -- *"Default key that protects my DynamoDB data when no other key is defined."*
- **The project CMK exists and is CUSTOMER-managed:** `alias/opal-security` resolves to **`64f25291-4015-42c5-ad41-40e42325deb7`**, `KeyManager: CUSTOMER`, applied by `TO-OP-S-25-26-27`.

> ⭐ **THE GATING QUESTION THE CELL RAISED IS ALREADY ANSWERED, AND IT ANSWERS YES.** The cell warned that C-16 refuses the CMK flip on `opal-data-security` **because the delivering service principals are absent from C-13's key policy**, and asked whether DynamoDB has the same gap. **It does not.** The key policy carries a statement `AllowViaDynamoDBAndS3InThisAccountOnly` granting `kms:Encrypt`, `kms:Decrypt`, `kms:ReEncrypt*`, `kms:GenerateDataKey*`, `kms:CreateGrant` and `kms:DescribeKey`. **The sibling's blocker does not transfer and this limb is viable.** ⛔ **Confirm that statement and its CONDITIONS yourself in phase 1 -- I printed the principals and actions and did NOT print the condition block, so the `kms:ViaService` and account conditions are UNREAD BY ME.** If they do not admit DynamoDB in this account, that is a STOP and a row.

## DELIVERABLE

1. **Move the identity and RBAC tables from the AWS-managed key to `alias/opal-security`**, in Terraform, in the carriers above. **Enumerate the table set explicitly with its denominator before you touch any of it** -- `opal-users-v2` plus the partner tables, and state how many there are from a live read rather than from this face.
2. ⛔ **A DYNAMODB SSE KEY CHANGE IS AN IN-PLACE UPDATE, NOT A REPLACEMENT. If any plan line reads `forces replacement` or proposes a destroy on ANY table, that is an immediate STOP and a row.** These tables hold live identity and RBAC data for real firms. **`0 to destroy` and `0 forces-replacement` bind PLAN-WIDE and no exception exists on this face.**
3. **ONE TABLE FIRST, then the rest.** Flip a single table, verify it end to end, and only then proceed. **A per-table apply is slower and it is what keeps a key-policy surprise to one table instead of five.**
4. **PROVE THE TABLE IS STILL READABLE AND WRITABLE AFTER EACH FLIP.** A key change that leaves a table encrypted-but-unreadable is the failure mode, and `describe-table` reporting the new key ARN does **not** establish it -- that is a DESIRED-plane read of a control-plane field. **Exercise the data plane: a read and a write against a FIXTURE item, then clean the fixture up and read the cleanup back.**
5. **DELETION PROTECTION AND PITR ARE NOT TOUCHED.** Round 1 established them; re-read them after each flip and show them unchanged. **Anything else moving on those tables is a STOP.**
6. **A deploy-ledger entry** (`safe-apply`, never bare), opened before and closed after, the module's UNSCOPED baseline quoted BEFORE the first edit, and **the rollback named: the AWS-managed key ARN, per table, captured before the first flip.**
7. **The proof-of-spec instance** at `../deliverables/0.7.0_AE_CloudOps~W/NFRA_OPSEC202609.TO-OP-S-8R2B.identity-tables-cmk-alignment.proof_of_spec.json`, VALID with the expected ids BEFORE the complete flip.

**BROKER DRAIN IMMEDIATELY BEFORE EACH APPLY.** These are live identity tables and the halt gate cannot see a lane inbox (row Z-S63).

## ACCEPTANCE -- criterion ids minted at cut

<criterion id="S8B-AC1" cell_refs="OP-s-8"/> `S8B-AC1` -- THE KEY POLICY ADMITS DYNAMODB, READ IN FULL INCLUDING ITS CONDITIONS: `get-key-policy` on `64f25291-...` with the `AllowViaDynamoDBAndS3InThisAccountOnly` statement quoted **entire, conditions included**, and an explicit statement of whether `kms:ViaService` and the account condition admit DynamoDB in this account. **The issuer did NOT read the condition block; this criterion is where it gets read.** If it does not admit, this files a STOP with a row and nothing is flipped.
<criterion id="S8B-AC2" cell_refs="OP-s-8"/> `S8B-AC2` -- EVERY TABLE IS ON THE PROJECT CMK, WITH ITS DENOMINATOR: `describe-table` per table showing `SSEType KMS` and `KMSMasterKeyArn` resolving to **`64f25291-...`** and NOT `86cc6c40-...`; tables flipped of tables enumerated, both counts printed, the enumeration derived from a live read. The BEFORE state is quoted from this face.
<criterion id="S8B-AC3" cell_refs="OP-s-8"/> `S8B-AC3` -- EACH TABLE IS STILL READABLE AND WRITABLE ON THE DATA PLANE, WHICH `describe-table` CANNOT SHOW: per table, a fixture item written and read back after the flip, then deleted and the deletion read back. **A control-plane read reporting the new key ARN is NOT this criterion** -- it shows what the key is configured as, never that the table can still be used. **NEGATIVE CONTROL: state what a failure would have looked like** (an `AccessDeniedException` or `KMSInvalidStateException` on the data-plane call) so a clean pass is distinguishable from an unexercised one.
<criterion id="S8B-AC4" cell_refs="OP-s-8"/> `S8B-AC4` -- DELETION PROTECTION AND PITR ARE UNCHANGED: per table, `describe-table` and `describe-continuous-backups` before and after, showing `DeletionProtectionEnabled` and PITR status identical. **Any movement is a FAIL and a row**, because round 1 established those and this face is not entitled to them.
<criterion id="S8B-AC5" cell_refs="OP-s-8"/> `S8B-AC5` -- BASELINE QUOTED, 0-DIFF AFTER, NOTHING ELSE RODE, PUSH STATE MEASURED: per root, the UNSCOPED plan quoted BEFORE the first edit; the apply's changed-resource list enumerated with its count containing ONLY the SSE specification of the named tables; the UNSCOPED re-plan 0-diff after; the ledger CLOSED with its proof and the per-table rollback key ARNs named; push state read by `ls-remote` + `is-ancestor` and stated as MEASURED. **`0 to destroy` and `0 forces-replacement` bind PLAN-WIDE with NO exception on this face.**

<expected_criteria>S8B-AC1, S8B-AC2, S8B-AC3, S8B-AC4, S8B-AC5</expected_criteria>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc> (v0.1.13), cell `OP-s-8` (manifest S8; FWD-8), **round-2b limb only** -- rounds 1 and 2a are complete under `TO-OP-S-8` and `TO-OP-S-16-17-8R2` and are not reopened.
<owned_cells>OP-s-8</owned_cells>
Read-dependencies, NOT claimed: `OP-s-25` (COMPLETE -- the CMK and its policy), `OP-s-16` (COMPLETE -- already on the project key, and its pattern is the one to follow), `OP-s-9` and `OP-s-11` (BLOCKED ON THIS LIMB -- `TO-OP-S-9-11` is sequenced behind `OP-s-8` reaching DONE).
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-03 19:1xZ -- GATES ARMED 21 over 5 carriers (C1 SENTINEL denominator 21 -> 5 gates; C2 DEPLOY-LEDGER 4 -> 4; C3 MORATORIA 12 -> 12; C4 SCOPE-GUARD 20 -> 0; C5 PROJECT-BLOCKING 336 -> 0). The DEPLOY-LEDGER carrier binds: every flip here is a ledgered apply on a live identity table.
comp-iam: DECLARED-NOT-APPLICABLE as a substitute -- the question is a KMS RESOURCE policy, not an IAM identity policy, and `S8B-AC1` reads it directly on the applied plane including the conditions a DESIRED-plane lens would not evaluate. Run it for orientation if useful; its silence is never an ALLOW.
comp-adversary: DECLARED-NOT-APPLICABLE -- this face pins no commit-scoped claim; every factual claim in it is a LIVE AWS read taken at the cut and timestamped, which the assignee re-takes in phase 1 and STOPS on any difference.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S8B-AC1`, `S8B-AC2`, `S8B-AC3`, `S8B-AC4`, `S8B-AC5`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~W/NFRA_OPSEC202609.TO-OP-S-8R2B.identity-tables-cmk-alignment.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py <instance> "S8B-AC1,S8B-AC2,S8B-AC3,S8B-AC4,S8B-AC5"` BEFORE the complete flip. **The control that must be able to FAIL is `S8B-AC3`'s data-plane exercise: a table can report the new key on the control plane and be unusable, and nothing else in this face would show it.** Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before write">Read the key policy IN FULL including conditions, and re-read every table's current SSE key. If the policy does not admit DynamoDB in this account, STOP at deliverable 1 and file the row -- do not flip anything.</phase>
  <phase id="2" when="before each apply">A broker drain, the unscoped baseline, the ledger opened, and the per-table rollback key ARN captured. One table first.</phase>
  <phase id="3" when="after each flip">The data-plane read-and-write exercise BEFORE moving to the next table, and deletion protection plus PITR re-read.</phase>
</compiler_tools_mandate>
