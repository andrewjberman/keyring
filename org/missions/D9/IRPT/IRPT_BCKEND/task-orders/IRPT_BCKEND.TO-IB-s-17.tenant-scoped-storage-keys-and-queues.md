# TO IRPT_BCKEND.TO-IB-s-17 -- TENANT-SCOPED STORAGE, KEYS AND QUEUES: the core root applied once -- KMS, the per-firm bucket layout with a quarantine, the tables, the queues, and the key grammar that refuses a client name

<to_id>IRPT_BCKEND.TO-IB-s-17</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~1</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-10</issued_date>
<status>pending -- handed by 2.0.0_SA_COO~B at the IB-s-18 drain</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.4 @62301f71e0 | **Decomp cell:** `IB-s-17` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.1.1, s.1 + s.2) | **outcome_ref:** FWD-10 (own), FWD-2 (own), FWD-9 | **PRD candidate:** B17

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~1`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~1;`.
- **Worktree:** `/c/tmp/wk-irpt-1-1` on branch `wk-irpt_bckend-1-1`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-1-1/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~1 <0.9.0_WK_IRPT_BCKEND~1@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/` (granted by the tree convention; no `<paths>` entry needed).
- **Queue:** second in slot ~1, after IB-s-18. Fourteen cells hang off this one; it is the ONLY cell that applies `core/` until IB-s-5 adds the policy conditions to the same root in the same slot.

---

## THE CELL

**The PRD row, verbatim at @62301f71e0 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B17 tenant-scoped storage and keys: DynamoDB tenant/request keys, immutable revisions, S3 evidence layout, cache/idempotency keys
- **serves:** FWD-10 (own), FWD-2 (own), FWD-9
- **brief sections consumed:** IV.4 records + DynamoDB paragraphs; II.3 keys paragraph
- **contracts (P=produces, C=consumes):** --
- **paths: reuse:** --
- **paths: new home:** proposed `opal-data-ycharts` SSE-KMS bucket (absent at inspection) with `firms/{firm_id}/intake|requests|generations/...` under enumerated prefixes
- **fixtures / evidence:** --
- **acceptance clause draft:** queues carry ids not attachments; S3 holds immutable evidence, never locks; keys include tenant, account-set fingerprint, source/schema/config revisions and operation parameters; once bound the firm is immutable

**What L5 adds (decomposition v0.1.1 s.2, s.6, s.9):**

- ONE root, ONE state: `infra/aws/terraform/investor-reporting/core/` (key `investor-reporting/core/tfstate`). Resources: a customer-managed KMS key + alias `alias/investor-reporting`; bucket `opal-data-ycharts` (ABSENT at the cut: HeadBucket 404 at 20:1xZ) with SSE-KMS default encryption, Block Public Access all four, versioning on, and the prefix layout `firms/{firm_id}/intake/YYYY/MM/DD/{id}/...`, `firms/{firm_id}/requests/{id}/revisions/{r}/...`, `firms/{firm_id}/generations/{id}/attempts/{a}/{vendor/report.pdf|sections/report.json|exports/{revision}/report.pdf}` and a separately enumerated `quarantine/` prefix -- prefixes are DECLARED in a `layout.json` the policy cell binds to, not created as empty objects; DynamoDB tables `irpt-requests` (pk tenant, sk request#revision), `irpt-jobs` (pk tenant, sk job; lease fields), `irpt-outbox` (pk tenant, sk seq), `irpt-checkpoints` (pk source, sk cursor), all PAY_PER_REQUEST, SSE with the same key, point-in-time recovery on; SQS queues `irpt-intake`, `irpt-generation`, `irpt-export` each with a DLQ, KMS-encrypted, carrying IDS ONLY. Firm ids come from `data/firm_registry.json` (`firm_id`: `49financial`, `inflection`, `cottonwood`; kind=client, enabled) -- never a hand-typed list.
- `infra/aws/lambda/investor-reporting/_keys/keys.py`: the key grammar per II.3 -- every cache/idempotency key is built from tenant + authorized account-set fingerprint + source/schema/config revisions + operation parameters; a component that looks like a client name is REFUSED at construction; S3 holds immutable evidence, never a lock.
- Applied through `.tools/safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/core apply` under a ledger entry (`deploy_ledger.py open --slug irpt-bckend-s17 ...`), the sentinel committed.

---

## DELIVERABLE

The `core/` root (`main.tf` completed, `kms.tf`, `s3.tf`, `dynamodb.tf`, `sqs.tf`, `layout.json`, `outputs.tf`); `infra/aws/lambda/investor-reporting/_keys/keys.py` + `tests/test_keys.py`; the ledger entry and its committed sentinel; the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_s_17.py` and `.result.md`.

---

## BOUNDS

- **Apply this root and NO other.** The eight sibling roots belong to other cells and slots.
- **No firm-specific data is written.** This cell creates empty resources and a layout declaration; the first object under `firms/` is written by a later cell through the gate.
- **The firm list is READ from `data/firm_registry.json`** (enabled, kind=client); a Terraform variable with three literals is the enumerated ban list CLAUDE.md s.5 warns lapses silently.

### Bounds every order carries (decomposition v0.1.1 s.8, verbatim)

1. **NO LIVE VENDOR CALL.** Endpoint, verbatim: *"NO LIVE VENDOR CALL is authorized by this document -- availability is not authorization; a live YCharts, Black Diamond or Orion call needs Andrew's explicit per-use word."* The same bound covers the mailbox read. A cell that carries a live arm proves its MECHANISM against recorded fixtures through a transport stub with a difference control; the live arm is an express qualification read by the CTO at L10 on Andrew's per-use word, never something this order does.
2. **NO MONITOR, ALARM, SNS OR SES SEND.** Nothing in this project notifies anyone. A scheduler this project creates is the product's own trigger and is applied `DISABLED` where its first fire would be a vendor call.
3. **CROSS-FIRM, both shapes.** Per-firm prefixes + IAM conditions in the shared bucket; the FIRM's own bucket for directory and holdings data; the `FirmDestinationPolicy`; the firm fixed from the sender's domain at ingestion and immutable after; Global GRANTED to an Opal principal, never to a firm one; no new all-firm financial aggregate.
4. **Deploys (NEVER-2, NEVER-9).** `.tools/safe-apply.sh` only, from a root whose state key is this cell's; a change-management entry opened at the start (`python .tools/deploy_ledger.py open ...`) and closed at completion, the sentinel `org/critical_paths/.open_deploys/<slug>.json` COMMITTED; ORDER on any act that changes the world: open the entry, ACT, close the entry and COMMIT it BEFORE taking the reads that grade the act; served bytes verified as `CodeSha256` against the built zip, never by filename; `aws lambda update-function-code` never; `.tools/terraform.exe` is provisioned in your worktree by the issuer -- use it by that path, never a PATH substitute (a substitute re-pins remote state).
5. **Andrew's four fixed constraints are not build choices:** the BDAPI-with-Kimi runner STYLE with NO OTP branch; the firm from the sender's domain at ingestion gated to enumerated destinations; the multitenant `api/scoped/` layout; terminated clients STAY VISIBLE under entitlement. And the endpoint's: units are part of a number's meaning; unsupported positions are never silently removed; no PUT of global YCharts preferences; no vendor call in render or preview; missing history is an answer, not an empty state; the narrative states contemporaneity and never causes; model targets never masquerade as observed holdings.
6. **No credential in any artifact, log, fixture or commit.** Secrets are read by NAME at runtime; a recorded fixture is scrubbed before it is committed; signed URL parameters are never logged; a `describe-secret` prints version state, never a value.
7. **No served output is touched.** The 28 existing CloudFront behaviors, the 14 existing scoped routes and every existing bucket, table and Lambda are read, never edited, except where THIS order's cell says it ADDS a resource.
8. **The spec is FROZEN mid-round.** A premise that does not hold, a path that is not where this face says, a result the invocation does not produce, a capability you lack: ONE row at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W<your slot>-S<k>`, per `org/surprise_channel/schemas/investigation_item.schema.json`, inside the fenced json array, appended never edited; then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.
9. **Every invocation terminates.** You run each named invocation under `timeout`; rc 124 IS the recorded output, retried once at most.
10. **Every `.py` edit passes `.tools/commit-gate.sh`.** Python 3.12 (`Python312` first on PATH; bare `python` may resolve to 3.14 without PyYAML). ASCII only in production code, logs and AWS names (`OK:`/`WARN:`/`ERROR:`/`SKIP:`/`BLOCKED:`).
11. **Scratch** is `<your worktree>/.scratch/` only.

---

## ACCEPTANCE

<criterion id="S17-AC1" cell_refs="IB-s-17"><invocation>timeout 300 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_s_17.py</invocation><expect>IBS17-STORAGE-APPLIED</expect></criterion>
**`S17-AC1` -- PASSES BY OUTPUT -- the applied plane read back, every count beside its denominator.**
**(a) THE BUCKET IS THERE, ENCRYPTED, CLOSED.** `head-bucket` 200; `get-bucket-encryption` names the `alias/investor-reporting` key (aws:kms); `get-public-access-block` all four true; `get-bucket-versioning` Enabled. Print each read.
**(b) THE LAYOUT IS DECLARED FROM THE REGISTRY.** `layout.json` firm ids == `data/firm_registry.json` enabled client firms (print `3 of 3` and the ids); `quarantine/` present; the three prefix families per firm present.
**(c) TABLES AND QUEUES, N OF N.** `describe-table` on 4 of 4 tables: SSE with the key, PITR enabled, PAY_PER_REQUEST; `get-queue-attributes` on 3 of 3 queues + 3 of 3 DLQs: KmsMasterKeyId set, RedrivePolicy names the DLQ. Print names and the denominator.
**(d) THE KEY GRAMMAR REFUSES A CLIENT NAME -- THE DIFFERENCE CONTROL.** `tests/test_keys.py`: a well-formed key carries every II.3 component (assert each); a key built with a client name component RAISES; two calls with the same inputs produce the same key (idempotent) and two different fingerprints produce different keys. Print passed/total.
**(e) THE LEDGER IS CLOSED AND ITS SENTINEL COMMITTED.** `python .tools/deploy_ledger.py check` reads no OPEN entry for this slug; `git log -1 --format=%H -- org/critical_paths/.open_deploys/irpt-bckend-s17.json` prints a hash.

<criterion id="S17-AC2" cell_refs="IB-s-17"><invocation>timeout 120 .tools/terraform.exe -chdir=infra/aws/terraform/investor-reporting/core plan -no-color -input=false -lock=false</invocation><expect>No changes\. Your infrastructure matches the configuration\.</expect></criterion>
**`S17-AC2` -- THE ROOT IS CONVERGED: a plan after the apply reads no changes.**
Run after the apply and after the ledger closes. A plan that still wants to change something means the applied plane and the record disagree; that is a FAIL, not a retry.

<criterion id="S17-AC3" cell_refs="IB-s-17" judgment="true"/>
**`S17-AC3` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: whether the layout's prefix families are sufficient for every later cell's writes (name any a later cell will need that is not declared); whether `firms/{firm_id}/` under ONE bucket with IAM conditions is the right shape here versus per-firm buckets, given both shapes are live in the estate; and what a reader of `layout.json` cannot learn from it. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>S17-AC1, S17-AC2, S17-AC3</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-17.tenant-scoped-storage-keys-and-queues.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/terraform/investor-reporting/core/
infra/aws/lambda/investor-reporting/_keys/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-bckend-s17.json
infra/aws/lambda/ci/lambda-source-map.json
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.1.1, cell `IB-s-17` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-s-17</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: RUN at the cut (20:2xZ, --budget 150) -- WITHIN BUDGET, denominator 5 of 5 carriers (C1=92 C2=6 C3=12 C4=20 C5=335), 25 gates ARMED, 0 name IRPT or any surface of this cell; the moratoria that bind here are G-20 (no monitor), G-23 (cross-firm), G-24 (vendor egress). BLIND SPOT: a ledger of gates, not prose obligations; 137 prose blocking fields unread.
comp-iam: RUN at the cut -- `comp-iam stats` + `roles`: denominator 191 roles parsed, 307 gaps estate-wide; ZERO investor-reporting roles exist; this cell writes bucket, key and queue policies and NO role, so `comp-iam gaps` at Phase 2 is the read that binds (recorded in the instance). BLIND SPOT: DESIRED plane only.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable (a fresh cut has no prior artifact for it to read).
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: S17-AC1, S17-AC2, S17-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-s-17.tenant-scoped-storage-keys-and-queues.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-s-17.tenant-scoped-storage-keys-and-queues.proof_of_spec.json S17-AC1,S17-AC2,S17-AC3` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
