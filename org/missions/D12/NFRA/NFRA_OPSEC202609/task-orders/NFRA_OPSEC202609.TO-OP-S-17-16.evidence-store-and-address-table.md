# TO NFRA_OPSEC202609.TO-OP-S-17-16 -- THE EVIDENCE STORE AND THE ADDRESS TABLE: `opal-data-security` (C-8) and `opal-suspicious-addresses` (C-9), the two no-dependency Terraform atoms of the auto-block framework

<to_id>NFRA_OPSEC202609.TO-OP-S-17-16</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~S</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-03</issued_date>
<status>complete</status>

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` v0.4 @43b75ffbd6 (ENDPOINT FWD-16 / FWD-18, properties 15 and 17; s.7.3 the two specs; 7.6 C-8, C-9, C-5, C-2) - **Decomp cells:** `OP-s-17` + `OP-s-16` (v0.1 @bff1f8d012, s.1a; ROUND 1: "bucket + table, Terraform, no dependencies") - **Lane:** a NEW Terraform module for this project's owned resources under `infra/aws/terraform/` (name it for the project: `opsec/` or the estate's convention -- state which and why), AE lane - **Round:** 1 of NFRA_OPSEC202609.

---

## THE CELLS -- two resources that exist nowhere today, and the one property that makes each safe to build first

Nothing of the auto-block framework is built (manifest S16, S17: claim `absent`). These two are the framework's SOURCE OF TRUTH (the table, C-2: "opal-suspicious-addresses is the ONLY record anything writes to; the WAF IP sets are projections of it") and its EVIDENCE STORE (the bucket, C-8). Neither depends on any other cell, which is why they are round 1: the reconciler (OP-s-15), the IP-set rules (OP-s-18), the sentinel (OP-s-14), the unblock CLI (OP-s-19) and the logging destination (OP-s-5, if S3 delivery is chosen) all depend on THESE.

**The table decides who is locked out, so it is the best-protected table in the account** (C-9): estate CMK, PITR ON, deletion protection ON, GSI `status-index`. **The bucket keeps the evidence, so an altered case file must leave the original** (C-8): versioning ON, SSE-KMS on the estate CMK, non-TLS denied, principals scoped, access logging to the CloudTrail bucket, lifecycle on `waf-logs/` only, `cases/` retained.

## DELIVERABLE -- Terraform, two resources, one fixture exercise, nothing else

1. **`opal-suspicious-addresses` (DynamoDB), exactly the 7.3 schema:** pk `address` (normalized CIDR: `/32` v4, `/64` v6 -- the normalization RULE documented on the table's Terraform comment, the normalization CODE is the sentinel's, OP-s-14); attributes as 7.3 lists (`status` in {BLOCKED, WATCH, ALLOW, EXPIRED}; `first_seen`, `last_seen`, `hits`, `rules`, `sources`, `paths_top`, `case_ids`, `blocked_at`, `blocked_by`, `expires_at`, `unblocked_by`, `unblocked_at`, `notes`); TTL attribute `expires_at` ENABLED (C-5: the stream REMOVE event is how an expiry unblocks); GSI `status-index` on `status`; DynamoDB Stream ENABLED with `NEW_AND_OLD_IMAGES` (OP-s-15 consumes it; enabling it here is the cheap half); SSE with the estate CMK (`86cc6c40...`, the one `opal-users-v2` uses -- read its ARN from the existing Terraform, never retype it); PITR ON; deletion protection ON; tags per the estate convention.
2. **`opal-data-security` (S3), exactly the 7.3 spec:** private (all four public-access blocks ON); SSE-KMS on the estate CMK with bucket-key enabled; versioning ON; bucket policy that (a) denies any request with `aws:SecureTransport = false`, (b) denies every principal outside an explicit list -- **at this round the list is the CTO-admin role and the account's Terraform-apply role**; the sentinel and reconciler roles do NOT EXIST yet and a bucket policy cannot name an absent principal, so OP-s-14 / OP-s-15's task orders EXTEND this policy when their roles exist (stated on the policy's Terraform comment); (c) server access logging to the estate's CloudTrail/access-logs bucket (read its name from the existing Terraform); lifecycle: `waf-logs/` transition to Glacier at 90 d and expire at 400 d, NOTHING on `cases/`, `reports/`, `allowlists/` (retained); the four prefixes from 7.3 created as zero-byte keys or documented as convention -- state which; **Object Lock is NOT enabled** (card OP-x-4 at Andrew; versioning is the round-1 default).
3. **A fixture exercise, then cleanup:** one `WATCH`, one `BLOCK` (with `expires_at` 5 minutes out) and one `ALLOW` row written to the table and read back (including via `status-index`); the BLOCK row observed to be REMOVED by TTL (DynamoDB TTL is best-effort within ~48 h -- if it has not fired by report time, say so with the read time; the row is deleted by hand afterwards and the deletion stated); one object written under `cases/2026/09/03/fixture/fixture-case/summary.json`, overwritten once, both versions listed (`list-object-versions`), then both versions deleted. No real address, no real case.
4. **The proof-of-spec instance** at `../deliverables/0.7.0_AE_CloudOps~S/NFRA_OPSEC202609.TO-OP-S-17-16.evidence-store-and-address-table.proof_of_spec.json`, VALID under `.tools/proof-of-spec-check.py` before the complete flip.
5. **A deploy-ledger entry** for the apply (`safe-apply`, never bare), opened before and closed after; nothing half-landed (NEVER-2).

## ACCEPTANCE -- criterion ids minted at cut; the assignee files the instance

<criterion id="S17-AC1" cell_refs="OP-s-17"/> `S17-AC1` -- EVERY C-8 PROPERTY READS ON THE APPLIED PLANE: `get-public-access-block` (4 of 4 true), `get-bucket-encryption` (aws:kms + the estate CMK ARN + bucket key), `get-bucket-versioning` (Enabled), `get-bucket-policy` (the SecureTransport deny AND the principal allow-list, quoted), `get-bucket-logging` (target = the CloudTrail/access-logs bucket), `get-bucket-lifecycle-configuration` (exactly one rule, prefix `waf-logs/`, Glacier 90 d, expire 400 d; NO rule touches `cases/`) -- six reads, each pasted, denominator 6 of 6.
<criterion id="S17-AC2" cell_refs="OP-s-17"/> `S17-AC2` -- VERSIONING LEAVES THE ORIGINAL: the fixture object overwritten once yields 2 versions in `list-object-versions`, both readable; then deleted (a delete marker + versions removed) and the listing empty -- the pair shown.
<criterion id="S17-AC3" cell_refs="OP-s-17"/> `S17-AC3` -- OBJECT LOCK IS OFF (card OP-x-4): `get-object-lock-configuration` returns no configuration; the Terraform carries no `object_lock_*` -- stated, not assumed.
<criterion id="S16-AC1" cell_refs="OP-s-16"/> `S16-AC1` -- EVERY C-9 PROPERTY READS ON THE APPLIED PLANE: `describe-table` (KeySchema `address`; SSEDescription KMS + the estate CMK; DeletionProtectionEnabled true; StreamSpecification NEW_AND_OLD_IMAGES; GSI `status-index` ACTIVE), `describe-continuous-backups` (PITR ENABLED), `describe-time-to-live` (`expires_at` ENABLED) -- three reads pasted, denominator 4 properties of 4 + TTL + stream.
<criterion id="S16-AC2" cell_refs="OP-s-16"/> `S16-AC2` -- THE FIXTURE ROWS WRITE AND READ BACK: WATCH / BLOCK / ALLOW rows written; `query` on `status-index` returns each by status; the BLOCK row's TTL removal observed (or the read time and "not yet fired" stated, then the row deleted by hand); all three rows absent at report.
<criterion id="S16-AC3" cell_refs="OP-s-16"/> `S16-AC3` -- NOTHING ELSE WRITES: no Lambda, policy or script in this TO's diff grants `dynamodb:PutItem`/`UpdateItem` on the table to any principal other than the Terraform-apply role and the CTO-admin role (a census of the diff for the table's ARN, with its count printed); the sentinel's and reconciler's grants are their own TOs' (C-2, C-7).
<criterion id="S1716-AC4" cell_refs="OP-s-17,OP-s-16"/> `S1716-AC4` -- TERRAFORM 0-DIFF AFTER APPLY AND PUSH STATE MEASURED: the re-plan reads 0-diff; the deploy-ledger entry CLOSED with its proof; push state read by ls-remote + is-ancestor (LOCAL expected); the module's path and name stated with the reason for the choice.

<expected_criteria>S17-AC1, S17-AC2, S17-AC3, S16-AC1, S16-AC2, S16-AC3, S1716-AC4</expected_criteria>

## SURFACES (read at your own vintage; the brief did not measure these -- they do not exist)

PRD `../prd/NFRA_OPSEC202609_PRD.md` s.7.3 (the table and bucket specs, the four prefixes) and 7.6 C-2, C-5, C-8, C-9 - `infra/aws/terraform/portal-auth/dynamodb.tf` (the CMK ARN and the table conventions to follow) - `infra/aws/terraform/shared-infra/dynamo.tf` - the existing access-logs / CloudTrail bucket declaration (locate it: `comp-find 'opal-organization-trail|access-logs' --files infra/aws/terraform`) - `infra/aws/terraform/portal-auth/cross-firm-secret-deny.tf` (the deny-belt idiom; the bucket policy's deny is the same shape).

## BOUNDS

- **Exactly the 7.3 schema and the C-8 / C-9 lists.** No extra attribute, no extra lifecycle rule, no Object Lock (OP-x-4), no replication, no notification configuration (the moratorium: nothing here alerts anyone).
- **No principal that does not exist yet.** The sentinel / reconciler / CLI grants are OP-s-14 / OP-s-15 / OP-s-19's; this policy names only the roles that exist today and says so.
- **The estate CMK, never a new key.** Read its ARN from Terraform (`portal-auth/dynamodb.tf`), never from a console.
- **`safe-apply` only, a ledger entry open for the apply; never-widen; no other resource rides the apply.**
- **Fixture rows and objects are deleted before report**; no real address is ever written by this TO.
- **A spec-vs-world divergence is a ROW** at `../surprise-channel/investigations/INVESTIGATION_v1.md` (lane ANY; site Z ids `NFRA_OPSEC202609-Z-S<n>`; `project`, `fabric`, `spec_asserts`, `world_is`), then keep working; never a message.
- **One project per instance (Rule 27):** this seat holds NFRA_OPSEC202609 ONLY.
- **Commit under your own serial** via `.tools/safe-commit.sh --author "0.7.0_AE_CloudOps~S <0.7.0_AE_CloudOps~S@opal.agent>" -F <msgfile>`; push is the integrator's.

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc> @bff1f8d012 (v0.1), cells OP-s-17 and OP-s-16 (s.1a; manifest rows S17, S16; ROUND 1 "bucket + table, no dependencies").
<owned_cells>OP-s-17 OP-s-16</owned_cells>
Read-dependencies, NOT claimed: OP-s-14 / OP-s-15 / OP-s-19 (they extend this policy and consume the stream), OP-s-5 (may deliver into `waf-logs/`), OP-x-4 (Object Lock card, HELD).
</decomp_ref>

<preflight>
comp-schedule: RUN -- 20 gates armed over 5 carriers (C1 21 -> 5, C2 3 -> 3, C3 12 -> 12, C4 20 SEMI-DECIDABLE -> 0, C5 337 NOT-DECIDABLE -> 0); 0 gates name NFRA_OPSEC202609, opal-data-security or opal-suspicious-addresses; G-15 binds and this cell builds no notification; read 2026-09-03 06:5xZ at the issuer's seat.
comp-iam: RUN -- DESIRED plane (401 .tf files, 369 attached / 24 NOT ATTACHED / 2 Deny unparsed); the two NEW resources have no policy rows yet by construction, so the lens has an empty population on them today; the grants this TO creates (Terraform-apply role, CTO-admin role) are verified on the live plane by `simulate-principal-policy` with ONE `--resource-arns` per call and the positive control as a separate invocation.
comp-adversary: RUN -- rc 0 at read-vintage @e10633f8b7 (2026-09-03T07:33:20Z); 2 commits, 5 repo paths, 0 file:line cites, 8 tool mentions; cited commits 2 attempted / 2 verified / 0 UNVERIFIABLE; cited paths 5 attempted / 4 stable / 1 flagged (the one flagged path is the proof instance this TO CREATES -- GONE at read-vintage, expected).
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S17-AC1`..`S17-AC3`, `S16-AC1`..`S16-AC3`, `S1716-AC4`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~S/NFRA_OPSEC202609.TO-OP-S-17-16.evidence-store-and-address-table.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py` BEFORE the complete flip, which the assignee commits itself. S17-AC2's version pair and S16-AC3's grant census are the controls that must be able to FAIL. Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before write">
    <step><run>comp-read infra/aws/terraform/portal-auth/dynamodb.tf --for "the estate CMK ARN, the PITR and deletion-protection idiom, and the table naming convention"</run><expect>the CMK ARN located by line; the idiom quoted; the convention followed</expect><if_mismatch>STOP; a second CMK or a divergent idiom is a row, not a choice</if_mismatch></step>
    <step><run>comp-find 'opal-organization-trail|access-logs|server_access_logging' --files infra/aws/terraform</run><expect>the access-logs / CloudTrail bucket's declaration located (denominator printed)</expect><if_mismatch>STOP; if no such bucket is Terraform-declared, the logging target is a row and the issuer names one</if_mismatch></step>
    <step><run>comp-blast opal-users-v2</run><expect>the consumers of the CMK-encrypted identity table listed, so the same CMK's grant shape is reused for the new table</expect><if_mismatch>surface to the issuer as a row</if_mismatch></step>
  </phase>
  <phase id="2" when="before commit">
    <step><run>.tools/commit-gate.sh on every .tf/.py/.sh touched; terraform plan via the estate wrapper on the new module</run><expect>the plan creates EXACTLY the two resources and their attached policies/stream/GSI/lifecycle/logging -- nothing else in any other module</expect><if_mismatch>STOP; an unrelated change riding the apply is refused</if_mismatch></step>
  </phase>
  <phase id="3" when="after commit">
    <step><run>the six S3 reads + the three DynamoDB reads listed in the criteria; terraform plan re-run</run><expect>every property as C-8 / C-9 state it; 0-diff</expect><if_mismatch>ROLL BACK inside the ledger entry and escalate loud (NEVER-2)</if_mismatch></step>
  </phase>
</compiler_tools_mandate>

**DELIVERABLE REPORT:** to `2.0.0_SA_COO~Z` with per-criterion evidence (the nine reads pasted), the module path, the ledger entry id, and push state as MEASURED. GO = this TO + the dispatch message. On completion this seat's next TO is OP-s-8 (table protections on the four identity/RBAC tables), already cut.
