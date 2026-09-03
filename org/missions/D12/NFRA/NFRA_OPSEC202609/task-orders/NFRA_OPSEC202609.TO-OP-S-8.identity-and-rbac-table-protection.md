# TO NFRA_OPSEC202609.TO-OP-S-8 -- THE TABLES HOLDING LOGINS AND PARTNER ROLES CANNOT BE DELETED BY ACCIDENT AND CAN BE REWOUND: PITR + deletion protection on the four real tables, the demo table aligned to the estate CMK

<to_id>NFRA_OPSEC202609.TO-OP-S-8</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~S</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-03</issued_date>
<status>complete</status>

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` v0.4 @43b75ffbd6 (ENDPOINT FWD-8, property 7; brief F6 the table-by-table posture) - **Decomp cell:** `OP-s-8` (v0.1 @bff1f8d012, s.1a; ROUND 1: "table protections; no dependencies"; OP-s-9 and OP-s-11 depend on THIS) - **Lane:** `infra/aws/terraform/portal-auth/dynamodb.tf`, `infra/aws/terraform/modules/partner-firm-table/main.tf` and the module's instantiations under `infra/aws/terraform/partners-api/**` (AE lane) - **Round:** 1 of NFRA_OPSEC202609, SECOND on this seat after TO-OP-S-17-16.

---

## THE CELL -- what the brief measured and what this cell changes

Brief F6 :144-167 (APPLIED 2026-09-02), the identity and RBAC posture table by table:

```
  opal-users-v2            (48 profiles + firm rows)   CMK 86cc6c40..., rotation ON   PITR ON    deletion protection OFF   <- credentials + MFA state
  opal-partner-49financial (11)                         CMK                            PITR OFF   DP OFF                    <- RBAC: plaintext email, firmRole
  opal-partner-cottonwood  (4)                          CMK                            PITR OFF   DP OFF
  opal-partner-inflection  (7)                          CMK                            PITR OFF   DP OFF
  opal-partner-demo        (1)                          AWS-owned key                  PITR OFF   DP ON                     <- inverted relative to the real firms
  opal-portal-auth-mfa / -throttle                      AWS-owned key                  ephemeral, TTL-reaped -- FINE, untouched
```

FWD-8 DONE WHEN is APPLIED: "the protections are switched on for every such table"; ACCEPT: "every table that holds a login or a partner's role refuses to be deleted, and can be restored to how it looked at any moment in the recent past". **This cell moves five settings on five tables and nothing else**: PITR ON and deletion protection ON on `opal-users-v2` and the three real partner tables; the demo table's encryption moved from the AWS-owned key to the estate CMK (so the four partner tables read alike) with PITR ON. The MFA and throttle tables are ephemeral and are NOT touched (the manifest says so; S8-AC4 proves it). OP-s-9 (retire the legacy `opal-users`) and OP-s-11 (the refresh-token binding) depend on this cell being DONE (s.9 item 5) -- they are the next cells on this seat's queue, not this TO.

## DELIVERABLE -- Terraform on the existing declarations, one apply, nothing new

1. **`opal-users-v2`** (`portal-auth/dynamodb.tf`): `deletion_protection_enabled = true`; PITR already ON -- confirm in Terraform (declare it if the resource block lacks it, so DESIRED and APPLIED agree).
2. **The three real partner tables** (`modules/partner-firm-table/main.tf`, instantiated per firm under `partners-api/`): `point_in_time_recovery { enabled = true }` and `deletion_protection_enabled = true` -- in the MODULE so every instantiation inherits it; if the module has a variable for either, set the default to ON and remove any per-firm override that turns it off.
3. **`opal-partner-demo`**: server-side encryption switched to the estate CMK (`server_side_encryption { enabled = true, kms_key_arn = <the CMK ARN read from portal-auth/dynamodb.tf> }`), PITR ON, deletion protection stays ON. An SSE change is an in-place `UpdateTable` -- **a plan that shows the table being REPLACED is a STOP, not a detail** (S8-AC5).
4. **Not built, stated:** hashing `email` in the partner tables is a brief suggestion, not an outcome -- if you judge it worth a row, file one; do not build it.
5. **The proof-of-spec instance** at `../deliverables/0.7.0_AE_CloudOps~S/NFRA_OPSEC202609.TO-OP-S-8.identity-and-rbac-table-protection.proof_of_spec.json`, VALID before the complete flip.
6. **A deploy-ledger entry** for the apply (`safe-apply`; never bare `terraform apply`).

## ACCEPTANCE -- criterion ids minted at cut; the assignee files the instance

<criterion id="S8-AC1" cell_refs="OP-s-8"/> `S8-AC1` -- PITR ON, FIVE OF FIVE: `aws dynamodb describe-continuous-backups --table-name <t>` for `opal-users-v2`, `opal-partner-49financial`, `opal-partner-cottonwood`, `opal-partner-inflection`, `opal-partner-demo` reads `PointInTimeRecoveryStatus: ENABLED` on each, with `EarliestRestorableDateTime` present -- five reads pasted, denominator 5 of 5.
<criterion id="S8-AC2" cell_refs="OP-s-8"/> `S8-AC2` -- DELETION PROTECTION ON, FIVE OF FIVE: `describe-table` reads `DeletionProtectionEnabled: true` on the same five -- five reads pasted, denominator 5 of 5.
<criterion id="S8-AC3" cell_refs="OP-s-8"/> `S8-AC3` -- THE DEMO TABLE READS LIKE THE REAL ONES: `describe-table opal-partner-demo` `SSEDescription` shows `SSEType: KMS` with `KMSMasterKeyArn` = the estate CMK (the same ARN `opal-users-v2` reports), and the table was UPDATED not replaced (`TableId` / `CreationDateTime` identical before and after -- the pair pasted).
<criterion id="S8-AC4" cell_refs="OP-s-8"/> `S8-AC4` -- THE EPHEMERAL TABLES ARE UNTOUCHED: `describe-table` on `opal-portal-auth-mfa` and `opal-portal-auth-throttle` before and after, the SSE / PITR / DP / TTL fields identical (2 of 2 pairs pasted); the plan showed no change on either.
<criterion id="S8-AC5" cell_refs="OP-s-8"/> `S8-AC5` -- NO TABLE REPLACED, 0-DIFF AFTER, LEDGER CLOSED, PUSH STATE MEASURED: the plan's summary line shows 0 to destroy and 0 to replace (quoted); the re-plan after apply reads 0-diff on `portal-auth` and every `partners-api` module touched; the deploy-ledger entry CLOSED with its proof; push state read by ls-remote + is-ancestor (LOCAL expected).

<expected_criteria>S8-AC1, S8-AC2, S8-AC3, S8-AC4, S8-AC5</expected_criteria>

## SURFACES (the brief's reads at @32daebf403; RE-GROUND AT YOUR OWN VINTAGE FIRST -- a setting may have moved since 2026-09-02)

`infra/aws/terraform/portal-auth/dynamodb.tf` (`opal-users-v2`, the CMK ARN, the MFA and throttle tables) - `infra/aws/terraform/modules/partner-firm-table/main.tf` - `infra/aws/terraform/partners-api/*.tf` (the per-firm instantiations; `comp-find 'partner-firm-table' --files infra/aws/terraform` for the denominator) - `infra/aws/terraform/shared-infra/dynamo.tf` (read to confirm none of the five tables is ALSO declared there -- a table declared twice is a row) - brief F6 :144-167.

## BOUNDS

- **Five tables, five settings.** No schema change, no attribute, no GSI, no hashing of `email` (a suggestion, not an outcome), no touch on the MFA / throttle tables, no touch on the legacy `opal-users` (that is OP-s-9's cell and follows this one on this seat).
- **In place, never replaced.** A plan that would replace any table is a STOP: surface it as a row and to the issuer before any apply. Deletion protection ON is itself the guard against the next accidental replace.
- **`safe-apply` only; a ledger entry open for the apply; never-widen; nothing else rides the apply** (the partners-api module instantiations must show ONLY the two settings changing).
- **The estate CMK, read from Terraform, never retyped.**
- **A spec-vs-world divergence is a ROW** at `../surprise-channel/investigations/INVESTIGATION_v1.md` (lane ANY; ids `NFRA_OPSEC202609-Z-S<n>`; `project`, `fabric`, `spec_asserts`, `world_is`), then keep working; never a message.
- **One project per instance (Rule 27):** this seat holds NFRA_OPSEC202609 ONLY.
- **Commit under your own serial** via `.tools/safe-commit.sh --author "0.7.0_AE_CloudOps~S <0.7.0_AE_CloudOps~S@opal.agent>" -F <msgfile>`; push is the integrator's.

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc> @bff1f8d012 (v0.1), cell OP-s-8 (s.1a; manifest row S8; ROUND 1 "table protections; no dependencies").
<owned_cells>OP-s-8</owned_cells>
Read-dependencies, NOT claimed: OP-s-9 and OP-s-11 (depend on THIS cell being DONE; the next TOs on this seat).
</decomp_ref>

<preflight>
comp-schedule: RUN -- 20 gates armed over 5 carriers (C1 21 -> 5, C2 3 -> 3, C3 12 -> 12, C4 20 SEMI-DECIDABLE -> 0, C5 337 NOT-DECIDABLE -> 0); 0 gates name NFRA_OPSEC202609, opal-users-v2 or the partner tables; read 2026-09-03 06:5xZ at the issuer's seat.
comp-iam: RUN -- DESIRED plane (401 .tf files, 369 attached / 24 NOT ATTACHED / 2 Deny unparsed); this cell changes NO grant -- the auth handler's and the partners-data Lambda's table grants are untouched (the brief: the auth handler's grant is correctly scoped by named table; the partners-data Lambda takes allowedFirmIds from the authorizer context) -- so the lens has an empty population of NEW rows; the demo table's KMS switch needs the CMK's key policy to admit the DynamoDB via-service grant, which the brief says is the standard shape (`Principal AWS:*` conditioned on the DynamoDB service) -- read it live (`get-key-policy`) before the apply, never assume it.
comp-adversary: RUN -- rc 0 at read-vintage @e10633f8b7 (2026-09-03T07:34:07Z); 3 commits, 5 repo paths, 0 file:line cites, 8 tool mentions; cited commits 3 attempted / 3 verified / 0 UNVERIFIABLE; cited paths 5 attempted / 4 stable / 1 flagged (the one flagged path is the proof instance this TO CREATES -- GONE at read-vintage, expected).
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S8-AC1`..`S8-AC5`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~S/NFRA_OPSEC202609.TO-OP-S-8.identity-and-rbac-table-protection.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py` BEFORE the complete flip, which the assignee commits itself. S8-AC3's TableId pair and S8-AC5's "0 to replace" plan line are the controls that must be able to FAIL. Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before write">
    <step><run>comp-read infra/aws/terraform/modules/partner-firm-table/main.tf --for "whether point_in_time_recovery, deletion_protection_enabled and server_side_encryption are declared, variable-driven or absent, and what each instantiation overrides"</run><expect>each of the three settings located or its absence stated; the per-firm overrides enumerated</expect><if_mismatch>STOP; an override that turns a protection OFF on purpose carries a reason -- read it, then row</if_mismatch></step>
    <step><run>comp-find 'partner-firm-table' --files infra/aws/terraform</run><expect>the instantiation count printed (the brief names 4 partner tables incl. demo; the count should agree)</expect><if_mismatch>a fifth instantiation is a row and a question to the issuer before the apply</if_mismatch></step>
    <step><run>comp-blast opal-partner-49financial; comp-blast opal-users-v2</run><expect>the consumers listed; a PITR/DP/SSE change touches no consumer's contract</expect><if_mismatch>surface as a row</if_mismatch></step>
    <step><run>aws kms get-key-policy --key-id <estate CMK> --policy-name default</run><expect>the DynamoDB via-service grant present (the brief's shape), so the demo table's switch cannot fail on key policy</expect><if_mismatch>STOP; a key-policy edit is NOT this cell's -- row + issuer</if_mismatch></step>
  </phase>
  <phase id="2" when="before commit">
    <step><run>.tools/commit-gate.sh on every .tf touched; terraform plan via the estate wrapper on portal-auth AND partners-api</run><expect>plan summary: N to change (the five tables' settings), 0 to add, 0 to destroy, 0 to replace -- quoted</expect><if_mismatch>STOP on any add/destroy/replace</if_mismatch></step>
  </phase>
  <phase id="3" when="after commit">
    <step><run>the five describe-continuous-backups + seven describe-table reads named in the criteria; terraform plan re-run</run><expect>5 of 5 PITR ENABLED; 5 of 5 DP true; demo SSE = the CMK with the same TableId; MFA/throttle identical; 0-diff</expect><if_mismatch>ROLL BACK inside the ledger entry and escalate loud (NEVER-2)</if_mismatch></step>
  </phase>
</compiler_tools_mandate>

**DELIVERABLE REPORT:** to `2.0.0_SA_COO~Z` with per-criterion evidence (the twelve reads pasted), the plan summary line, the ledger entry id, and push state as MEASURED. GO = this TO + the dispatch message; this TO ACTIVATES when TO-OP-S-17-16's complete flip is committed by this seat (sequential on one seat; the GO is carried by the same dispatch message and is conditional on that flip).
