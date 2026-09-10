# TO IRPT_BCKEND.TO-IB-s-18 -- THE FOUNDATION: eleven contract schemas from one table, the three code homes, the path/owner manifest, the nine Terraform roots -- deploys nothing, everything hangs off it

<to_id>IRPT_BCKEND.TO-IB-s-18</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~1</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-10</issued_date>
<status>complete -- S18-AC1 PASS-by-output (rc=0, IBS18-FOUNDATION-COMPLETE, 5 of 5 arms); S18-AC2 RECORDED for 3.0.0_SA_CVO at L9, no worker verdict; proof-of-spec-check rc=0; rows IRPT_BCKEND-W1-S1 and W1-S2 filed. Nothing deployed.</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.4 @62301f71e0 | **Decomp cell:** `IB-s-18` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.1.1, s.1 + s.2) | **outcome_ref:** all ten (FWD-1, 2, 3, 4, 5, 7, 8, 9, 10, 11) | **PRD candidate:** B18

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~1`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~1;`.
- **Worktree:** `/c/tmp/wk-irpt-1-1` on branch `wk-irpt_bckend-1-1`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-1-1/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~1 <0.9.0_WK_IRPT_BCKEND~1@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/` (granted by the tree convention; no `<paths>` entry needed).
- **Queue:** first in slot ~1; nothing before it. Three other slots wait on THIS cell's merge, so it is small by design: schemas, homes, manifest, roots, register. No apply.

---

## THE CELL

**The PRD row, verbatim at @62301f71e0 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B18 infrastructure homes, IAM/KMS/secrets, release manifests
- **serves:** all
- **brief sections consumed:** IV.7 proposed homes paragraph; V
- **contracts (P=produces, C=consumes):** --
- **paths: reuse:** existing protected transport/publisher infrastructure where its contract fits
- **paths: new home:** `infra/aws/lambda/investor-reporting/`, `infra/aws/terraform/investor-reporting/`, `data/assets/scripts/gold/investor_reporting/`
- **fixtures / evidence:** --
- **acceptance clause draft:** every concrete read/write path and owner registered during implementation; no silent dependency on another page's Gold output; reusing a helper never widens its deployment or IAM role; `safe-apply` only; no `aws lambda update-function-code`

**What L5 adds (decomposition v0.1.1 s.2, s.6, s.9):**

- The eleven contract schemas (`DirectoryEntry`, `ResolvedScope`, `PerformanceReport`, `AnalysisRequest`, `AnalysisReport`, `HoldingsSnapshot`, `NarrativePacket`, `ExportBundle`, `ExportReceipt`, `StatusEnvelope`, `RenderPackage`) are GENERATED from the PRD's CONTRACTS table at @62301f71e0 -- every 'required meaning / fields' item becomes a named property with a `description` quoting the table -- so this project's producers and the counterpart's typed client (built from the same table at the same pin) validate against one carrier. Each schema ships with a fixture pair (a valid instance and an invalid one).
- `infra/aws/lambda/investor-reporting/PATH_MANIFEST.json`: every PRD PATHS row (27 reuse rows expanded to their files, 5 new homes) as an entry `{path, kind: reuse|new, cell, owner, use}`; every later cell APPENDS its concrete read/write paths here. The dependency register `infra/aws/lambda/investor-reporting/DEPENDENCY_REGISTER.md` carries the PRD's BRIEF COVERAGE entry 25 (Part V) items, one row each with an owner.
- The nine Terraform roots under `infra/aws/terraform/investor-reporting/` (`core`, `directory`, `intake`, `ycharts`, `performance`, `narrative`, `export`, `ops`, `api`) each get a `main.tf` skeleton with the `s3` backend at bucket `opal-313476888478-terraform-state`, key `investor-reporting/<root>/tfstate`, region `us-east-1`, provider `aws ~> 5.0`, default tags `Project=OpalPortal ManagedBy=Terraform System=InvestorReporting` -- copied from the shape at `infra/aws/terraform/partners-api/main.tf`. NO `init`, NO `plan`, NO `apply` in this cell.
- `data/assets/scripts/gold/investor_reporting/README.md` names the two runners the tree will hold and the rule-13 lane they fall under.
- The supervision/billing cohort semantics paragraph (PRD v0.2, under CONTRACTS) lands as explicit enum properties on `DirectoryEntry` (cohort/capability) and `HoldingsSnapshot` (classification partitions), each with an explicit UNKNOWN value that is never false and never Client.

---

## DELIVERABLE

`infra/aws/lambda/investor-reporting/_contracts/<Contract>.schema.json` x11 with `fixtures/<Contract>.valid.json` and `fixtures/<Contract>.invalid.json` x11; `infra/aws/lambda/investor-reporting/README.md`, `PATH_MANIFEST.json`, `DEPENDENCY_REGISTER.md`; `infra/aws/terraform/investor-reporting/README.md` + nine `<root>/main.tf` skeletons; `data/assets/scripts/gold/investor_reporting/README.md`; the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_s_18.py` and its `.result.md`.

---

## BOUNDS

- **DO NOT `terraform init`, `plan` or `apply` anything.** This cell has no state and no ledger entry; a root that has been initialised here would pin a backend before its owning cell exists.
- **DO NOT invent a field.** A property with no source line in the PRD CONTRACTS table (or the v0.2 semantics paragraph) is a fabrication; cite the table row in each property's `description`.
- **Schemas are draft 2020-12 JSON Schema, `additionalProperties: false` at the top level**, so a producer that adds a field the counterpart never agreed to fails validation on both sides.

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

<criterion id="S18-AC1" cell_refs="IB-s-18"><invocation>timeout 300 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_s_18.py</invocation><expect>IBS18-FOUNDATION-COMPLETE</expect></criterion>
**`S18-AC1` -- PASSES BY OUTPUT -- one battery, every number beside its denominator, the token only when all five arms hold.**
**(a) ELEVEN OF ELEVEN, FROM THE TABLE.** Parse the PRD CONTRACTS table at the pin (`git show 62301f71e0:org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`), print the denominator of contract rows found (expect 11), and for each show that every 'required meaning / fields' item has a property whose `description` quotes it; print `N of N` per contract.
**(b) EVERY FIXTURE PAIR DISCRIMINATES -- THE DIFFERENCE CONTROL.** For each of the 11 schemas the `.valid.json` fixture validates and the `.invalid.json` fixture is REFUSED (`jsonschema`), 11 of 11 each way; a schema whose invalid fixture passes fails the arm.
**(c) THE MANIFEST COVERS THE PRD'S PATHS TABLE.** Parse the PRD PATHS table at the pin, expand each row to its files, and show `PATH_MANIFEST.json` carries every one with `kind`, `cell` and `owner` (print `N of N`, and the 3 `new` homes as ABSENT-BY-DESIGN at HEAD).
**(d) NINE ROOTS, NINE DISTINCT STATE KEYS, ZERO STATE.** Read the nine `main.tf` skeletons, print the nine backend keys and assert they are pairwise distinct and all under `investor-reporting/`; assert no `.terraform/` directory and no `terraform.tfstate*` exists under any root.
**(e) THE REGISTER CARRIES PART V.** Print the dependency register's rows (expect the seven Part V items) each with a non-empty owner.

<criterion id="S18-AC2" cell_refs="IB-s-18" judgment="true"/>
**`S18-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: whether any II.3 meaning was LOST in the schema translation (name the contract and the sentence); whether any manifest entry names the wrong owner; and which schema properties you had to shape by judgment because the table's wording admits two readings. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>S18-AC1, S18-AC2</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-18.the-foundation-contracts-homes-manifest-roots.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/
infra/aws/terraform/investor-reporting/
data/assets/scripts/gold/investor_reporting/
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.1.1, cell `IB-s-18` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-s-18</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell creates, changes and fires no schedule, rule or trigger; it builds a library and runs a local battery. BLIND SPOT, stated: the cut-time run (5 of 5 carriers, 0 gates naming this project) is inherited from the issuance, not re-run here.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted and nothing applied by this cell; no policy, role or trust document is written. BLIND SPOT: the reads this cell makes run under the launching seat's credentials, which is stated, not measured.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable (a fresh cut has no prior artifact for it to read).
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: S18-AC1, S18-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-s-18.the-foundation-contracts-homes-manifest-roots.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-s-18.the-foundation-contracts-homes-manifest-roots.proof_of_spec.json S18-AC1,S18-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
