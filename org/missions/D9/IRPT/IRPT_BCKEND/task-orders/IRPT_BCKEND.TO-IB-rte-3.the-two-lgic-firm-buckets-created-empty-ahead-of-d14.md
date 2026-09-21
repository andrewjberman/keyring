# TO IRPT_BCKEND.TO-IB-rte-3 -- THE TWO LGIC FIRM BUCKETS CREATED, EMPTY, AHEAD OF D14: Andrew approved (17:3xZ) provisioning `opal-data-inflection` and `opal-data-cottonwood` NOW; the CTO placed it as an IRPT_BCKEND round-5 cell under Rule 30 -- CREATION ONLY, names from `lib/opal_naming.py name()`, declared in the same shape as the 49 Financial bucket, applied through `safe-apply` under a change-management entry, the cross-firm gate enumerations REGENERATED from the registry so the new names are fenced; no object moves, no reader cut-over, no legacy retirement

<to_id>IRPT_BCKEND.TO-IB-rte-3</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~3</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-18</issued_date>
<status>superseded -- CLOSED for round 5 by 2.0.0_SA_COO~B at 2026-09-19T03:4xZ: its FAIL arms (b)-(e) are re-handed as IB-rtf-5 (round 6) behind Andrew's step 4; its ledger entry and sentinel stay OPEN RED until IB-rtf-5 closes them. Was: pending -- HANDED by 2.0.0_SA_COO~B at 2026-09-18T19:0xZ to slot ~3 (cold start) on Andrew's 17:3xZ approval (record @af794c77e3) and the CTO's Rule-30 placement (analysis s.6(b)/s.8 item 2). The legacy bd/inf/cot channels stay ACTIVE (Andrew's prior word, not reversed).</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 5 (the CTO's round-4 analysis @561d6e1cc9, msg 98036) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.14 @b8e98d5a4d (no addendum at round 4) | **Round-4 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND4_ANALYSIS.md` @561d6e1cc9 | **Andrew-direct:** 2026-09-18 ~17:3xZ "Approved" (record `org/tier1_exec/2.0.0_SA_COO~B/deliverables/ANDREW_DIRECT_20260918_173xZ_TWO_OPEN_CALLS_APPROVED_IRPT_BCKEND.md` @af794c77e3) | **Rulings carried:** R-40, R-42, R-44, R-45 @57bc083d45; the forward-looking-criterion bar; Rule 30 | **Decomp cell:** `IB-rte-3` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.5, s.R5) | **outcome_ref:** FWD-1, FWD-7, FWD-10 (the firm-bound destination)

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~3`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~3;`.
- **Worktree:** `/c/tmp/wk-irpt-5-3` on branch `wk-irpt_bckend-5-3`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree; make a path absolute by prefixing `/c/tmp/wk-irpt-5-3/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~3 <0.9.0_WK_IRPT_BCKEND~3@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/` (granted by the tree convention). Batteries are named `battery_<cell>.py`, the cell id lower-cased with underscores.
- **Python:** `py -3.12`. AWS through `.tools/aws`. `.tools/terraform.exe` is provisioned by the issuer. A recursive `grep`/`find` in Bash is DENIED by a rail hook and a denial aborts the WHOLE call; use the Read/Grep tools and keep a gated read in its own call. Capture `safe-commit.sh` output to a file, never pipe it to `tail`, never pair it with `$( )`.

---

## THE CELL

**The word (record @af794c77e3, verbatim REC adopted):** *"provision the two buckets now through the LGIC builders (D14's own names, empty, no data moves), so IB-rtd-7's port can be re-cut in round 5 while the legacy prefixes stay live until the readers cut over in one window."* **The CTO's placement (analysis s.6(b)):** an IRPT_BCKEND cell, not a D14 act; *"CREATION ONLY, names from lib/opal_naming.py name(), through safe-apply under a change-management entry; a builder refusal is a registry row to add, never a hand-typed workaround. NO OBJECT MOVES, NO READER CUT-OVER, NO LEGACY-PREFIX RETIREMENT."* IB-rtd-6 (@d6e3fdd085) already built the addresses `s3://opal-data-inflection/irpt/inflection/gold/directory/...` and `s3://opal-data-cottonwood/irpt/cottonwood/gold/directory/...` with 0 registry refusals, and measured both buckets `NoSuchBucket` live.

- (a) THE NAMES, BUILT: call `name()` for each firm's data bucket exactly as the registry scopes it (print the call and the output; IB-rtd-6's result shows the address form); a REFUSAL is a drafted registry row in your result and a STOP, never a typed name. Confirm each name is ABSENT live (`head-bucket` -> 404, printed) before anything is declared.
- (b) THE DECLARATION, in the shape the estate already uses for a firm bucket: read `infra/aws/terraform/shared-infra/s3-49financial.tf` (@HEAD, cite lines) and declare the two buckets beside it with the SAME controls (versioning, public-access block, encryption, the per-firm Deny fence the doctrine's tenancy rules require -- `infra/logic/02_DOCTRINE.md` R5/R7 and the tenancy rule that names the fence, cited with vintage); every property the 49 Financial declaration carries, the new ones carry, `p of p` printed; nothing else in that root changes. Plan: exactly the new resources `to add`, `0 to change`, `0 to destroy` -- print the plan and its resource list; anything else is a STOP.
- (c) THE GATE ENUMERATIONS: `.tools/ds-precommit-check.py`'s `_CROSS_FIRM_FOREIGN_BUCKETS` / `_CROSS_FIRM_FOREIGN_KEY_PREFIXES` are GENERATED from `infra/logic/registry/scopes.json` (`# GENERATED by lib/opal_naming.py ... regenerate with: python lib/opal_naming.py generate --out <dir> --target .tools/ds-precommit-check.py`, `:68-73` and `:112-117` @HEAD). CLAUDE.md NEVER: *"a new firm name is a GATE EDIT, not just an infra act."* Regenerate through the builder (never a hand edit); print the diff of the generated block; if the registry already scopes both firms the diff may be empty -- say so and prove the fence sees the new names by a negative test (a pipeline dir referencing the foreign bucket name is REFUSED by the gate, `2 of 2`).
- (d) THE APPLY under ledger (`.tools/safe-apply.sh` from that root with the vendored binary, `init` first; OPEN sentinel committed before; closed before the grading reads): post-apply `head-bucket` 200 for both, `get-bucket-versioning` Enabled, `get-public-access-block` all four true, `get-bucket-policy` carrying the fence -- `2 of 2` buckets, every control read back, R-40 (policy documents' sha256). The buckets are EMPTY: `list-objects-v2` `0` keys each, printed. The re-plan reads `0/0/0`.
- (e) THE NEGATIVE CONTROL: from the host (`i-02448edb624a7a7cf`, read-only SSM), the host role's attempt to write `opal-data-inflection/irpt/inflection/gold/directory/zz-negative-control` and the 49f principal's attempt to read `opal-data-cottonwood/...` both DENIED (`2 of 2`) -- the fence is live and no grant was widened by creation. NOTHING is written to either bucket by anyone this round.

---

## DELIVERABLE

the two bucket declarations; the regenerated gate block (if changed); the ledger entry; `battery_ib_rte_3.py`, `IB-rte-3_R53-AC1_battery_output.txt`, `the-two-firm-buckets-created.result.md`; the proof instance.

---

## BOUNDS

- CREATION ONLY: no object written or copied to either bucket; no reader, writer, runner, policy or env change anywhere else; no legacy prefix touched; the shared-infra root's other resources untouched (a plan naming any of them is a STOP). A builder refusal is a drafted registry row + STOP, never a typed name. `-target` never on this root.
- **THE FORWARD-LOOKING-CRITERION BAR (round-3 analysis s.4, ADOPTED; R-68's shape):** no criterion on this face certifies what a future event WILL find or load; every claim about a run or a served artifact is bound to that artifact's CONTENT HASH (`VersionId`/`ETag`/`sha256`/`CodeSha256`/`git hash-object`) READ AT THE EVENT -- a prediction made before the event is not evidence and a battery that prints one is refused at the drain.
- **S56 (ARMED, the CVO's): EVERY line citation in this order's JUDGMENT RECORD and result carries a vintage -- `path:line @ <commit-ish>` -- a bare `:NNN` is a defect the issuer greps for at the drain (`0 of N` bare citations is the bar).** CLAUDE.md Rule 22: a citation without a vintage is not a citation.
- **S73 (the `comp-iam roles` snapshot with no vintage) is an ESTATE-INSTRUMENT defect routed elsewhere and does NOT ride this order:** a live-plane IAM read here uses `comp-iam live` or `.tools/aws iam get-role`, never `comp-iam roles`.
- **R-40 (standing bar, `1.0.0_SA_CTO` @233f5fd5e4):** every criterion whose subject is a RUN or a PRODUCED ARTIFACT records that artifact's CONTENT HASH (`git hash-object`, `sha256sum`, or the service's own digest such as `ETag`/`CodeSha256`) beside its run id in the instance, and is graded against the hash; a label, a path or a timestamp ordering is not an identity.
- **Surprises:** ONE row per premise that does not hold, path that is not where this face says, result the invocation does not produce, or capability you lack -- at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W3-S<k>` with k continuing that coordinate's numbering (read the file's highest `W3-S<k>` first; the file now holds SEVERAL fenced json blocks -- append your object INSIDE THE FIRST fence's array at its end, LF line endings, UTF-8 written explicitly, no json fence marker inside any row's text, `surfaced_at` a full ISO timestamp, omit `disarm_owner` on an INERT row and name a SEAT SERIAL, never a cell, when ARMED (R-42)); then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.

### Bounds every order carries (decomposition v0.2 s.8, verbatim)

1. **NO LIVE VENDOR CALL.** Endpoint, verbatim: *"NO LIVE VENDOR CALL is authorized by this document -- availability is not authorization; a live YCharts, Black Diamond or Orion call needs Andrew's explicit per-use word."* The same bound covers the mailbox read and a YCharts login or session capture. A cell that carries a live arm proves its MECHANISM against recorded fixtures through a transport stub with a difference control; the live arm is an express qualification read by the CTO at L10 on Andrew's per-use word, never something this order does.
2. **NO MONITOR, ALARM, SNS OR SES SEND.** Nothing in this project notifies anyone. A scheduler this project creates is the product's own trigger and is applied `DISABLED` where its first fire would be a vendor call.
3. **CROSS-FIRM, both shapes.** Per-firm prefixes + IAM conditions in the shared bucket; the FIRM's own bucket for directory and holdings data; the `FirmDestinationPolicy`; the firm fixed from the sender's domain at ingestion and immutable after; Global GRANTED to an Opal principal, never to a firm one; no new all-firm financial aggregate.
4. **Deploys (NEVER-2, NEVER-9).** `.tools/safe-apply.sh` only, from a root whose state key is this cell's; a change-management entry opened at the start (`python .tools/deploy_ledger.py open ...`) and its OPEN sentinel `org/critical_paths/.open_deploys/<slug>.json` COMMITTED IMMEDIATELY (row W3-S4's rule) before the act; the entry closed at completion and COMMITTED BEFORE the reads that grade the act; served bytes verified as `CodeSha256` against the built zip, never by filename; `aws lambda update-function-code` never; `.tools/terraform.exe` is provisioned in your worktree by the issuer -- use it by that path, never a PATH substitute (a substitute re-pins remote state); every provider cache was purged estate-wide, so `init` each root you plan with the vendored binary.
5. **Andrew's four fixed constraints are not build choices:** the BDAPI-with-Kimi runner STYLE with NO OTP branch; the firm from the sender's domain at ingestion gated to enumerated destinations; the multitenant `api/scoped/` layout; terminated clients STAY VISIBLE under entitlement. And the endpoint's: units are part of a number's meaning; unsupported positions are never silently removed; no PUT of global YCharts preferences; no vendor call in render or preview; missing history is an answer, not an empty state; the narrative states contemporaneity and never causes; model targets never masquerade as observed holdings; THE YCHARTS MECHANISM IS FIXED (v0.9: K3 capture on the dedicated host -> fenced publication -> browserless Lambda REST replay).
6. **No credential in any artifact, log, fixture or commit.** Secrets are read by NAME at runtime; a recorded fixture is scrubbed before it is committed; signed URL parameters are never logged; a `describe-secret` prints version state, never a value.
7. **No served output is touched.** The 28 existing CloudFront behaviors, the 14 pre-existing scoped routes, this project's 11 live routes and every existing bucket, table and Lambda are read, never edited, except where THIS order's cell says it CHANGES or ADDS a resource.
8. **The spec is FROZEN mid-round.** A premise that does not hold, a path that is not where this face says, a result the invocation does not produce, a capability you lack: ONE row at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W<your slot>-S<k>` (a DS lane mints `IRPT_BCKEND-D-S<k>`), per `org/surprise_channel/schemas/investigation_item.schema.json`, inside the fenced json array, appended never edited, k continuing your slot's round-1 numbering; then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.
9. **Every invocation terminates.** You run each named invocation under `timeout`; rc 124 IS the recorded output, retried once at most.
10. **Every `.py` edit passes `.tools/commit-gate.sh`.** Python 3.12 (`Python312` first on PATH; bare `python` may resolve to 3.14 without PyYAML). ASCII only in production code, logs and AWS names (`OK:`/`WARN:`/`ERROR:`/`SKIP:`/`BLOCKED:`).
11. **Scratch** is `<your worktree>/.scratch/` only.
12. **NO SELF-WRAPPING HARNESS AS EVIDENCE (round-1 lesson, rows W1-S10, S24).** An arm's subject is the REAL artifact -- the real route file, the real dispatcher, the deployed function, the served object -- never a copy the battery wraps, patches or re-registers itself. A census reads the real population and prints its denominator; a `0 of 0` is printed as VACUOUS, never as a pass. Every manifest of hashes a cell writes is re-derived by its battery every run (row W3-S9).
13. **TYPED, ISSUED IDENTIFIERS AT EVERY BOUNDARY (round-1 lesson, rows W2-S9/S11, W1-S7, W3-S12).** Firm, client, relationship, account, report, export and job ids cross a function boundary as ISSUED opaque ids of a declared type; a display name, an e-mail address, a raw upstream key or a request-controlled firm token is refused at the boundary, and a refusal never echoes the refused value.

---

## ACCEPTANCE

<criterion id="R53-AC1" cell_refs="IB-rte-3"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/battery_ib_rte_3.py</invocation><expect>IBR53-TWO-FIRM-BUCKETS-CREATED-EMPTY-AND-FENCED</expect></criterion>
**`R53-AC1` -- PASSES BY OUTPUT:** (a) `2 of 2` names built by `name()` with the calls printed, both ABSENT live before; (b) the declaration with `p of p` controls matching the 49 Financial bucket's, the plan exactly the new resources `to add` / `0 to change` / `0 to destroy`; (c) the gate block regenerated through the builder (diff printed) and the fence refusing a foreign reference `2 of 2`; (d) post-apply reads `2 of 2` with every control and `0` keys each, re-plan `0/0/0`; (e) negative control `2 of 2` DENIED from the host. The token prints only when every arm holds; the battery re-derives every count from the real world each run and never reads its own earlier output.

<criterion id="R53-AC2" cell_refs="IB-rte-3" judgment="true"/>
**`R53-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: whether the D14 full-name migration's own plan already names these two buckets (and if so whether this creation pre-empts or conforms to it -- cite the D14 register); what IB-rtd-7's re-cut port now lacks besides the halves and the FNTEND reader cell; and whether the 49 Financial bucket's declaration is itself the canonical shape or carries drift the new ones should not copy. No verdict. Every line citation carries `@<commit-ish>`.

<expected_criteria>R53-AC1, R53-AC2</expected_criteria>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rte-3.the-two-lgic-firm-buckets-created-empty-ahead-of-d14.md
infra/aws/terraform/shared-infra/
.tools/ds-precommit-check.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.5, cell `IB-rte-3` (s.R5 -- the round-5 rectangle, edges, seating and bounds).
<owned_cells>IB-rte-3</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired.
comp-iam: RUN at the cut by the issuer's read of IB-rtd-6's packet -- no principal holds a grant on either new bucket today (they do not exist); the DESIRED plane is the fence declared with the bucket; the APPLIED plane is this cell's post-apply policy reads + the on-host negative control, the discriminator. BLIND SPOT: identity policies only.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `.tools/**`, `data/**` and `lib/**` path resolves to its own lane at HEAD and is admitted ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: R53-AC1, R53-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/IRPT_BCKEND.TO-IB-rte-3.the-two-lgic-firm-buckets-created-empty-ahead-of-d14.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and -- R-40 -- the content hash of every produced or served artifact the row grades, EACH PINNED TO THE COMMIT THAT CARRIED IT (commit the battery, its output and the result BEFORE the instance); a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/IRPT_BCKEND.TO-IB-rte-3.the-two-lgic-firm-buckets-created-empty-ahead-of-d14.proof_of_spec.json --governing-order org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rte-3.the-two-lgic-firm-buckets-created-empty-ahead-of-d14.md` BEFORE the complete flip; rc 0 AND R53-AC1 PASS-by-output, then flip this order's `<status>` to `complete` and commit instance and flip together. A FAIL row leaves the order open and is your final report on it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
