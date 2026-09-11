# TO IRPT_BCKEND.TO-IB-rt-3 -- ONE OPAQUE-ID NORMALIZER: directory, holdings, performance and the ownership projection through one admitted transformation, no raw upstream suffix in any id, and the account-only versus relationship grain agreed across schema, projection and payload

<to_id>IRPT_BCKEND.TO-IB-rt-3</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~1</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-11</issued_date>
<status>pending -- GO paired at the round-2 issuance (the hand-off is the GO). First order of slot ~1.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 2 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.13 @e6ba5d9878 (ADMITTED, both L4-R halves SIGNED) | **Round-1 analysis:** `../ledger/ROUND_ANALYSIS.round1.md` @0d57ceb2f9, ruling 4 (ids and grain) | **Slug rows this cell closes:** W1-S7, W1-S9, W2-S11, W2-S2 | **Decomp cell:** `IB-rt-3` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.2, s.1 + s.2) | **outcome_ref:** FWD-1, FWD-2, FWD-5 (contrib) | **PRD candidate:** B2

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~1` (the same subagent as round 1, continued with its context intact). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~1;`.
- **Worktree:** `/c/tmp/wk-irpt-2-1` on branch `wk-irpt_bckend-2-1`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-2-1/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~1 <0.9.0_WK_IRPT_BCKEND~1@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/` (granted by the tree convention; no `<paths>` entry needed). Round-2 batteries are named `battery_<cell>.py` with the cell id lower-cased and hyphens as underscores.
- **Queue:** first in slot ~1, the same subagent that built the core root, the holdings snapshot and the ops cell; nothing before it. IB-rt-6 (slot ~2) and IB-rt-7 (this slot) consume this cell's normalizer.

---

## THE CELL

**The PRD row, verbatim at @e6ba5d9878 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B2 identity resolution + permitted account set (`ResolvedScope`); **(v0.10) the Generate resolver: builds the `resolved` half of the job envelope (scope, client/account binding, the immutable holdings snapshot, controlled profile, the AUTHORIZED comparison catalog) from authenticated server context -- the browser can never submit or overwrite it; client autosuggest does not authorize Generate; membership and comparison entitlement are re-validated at job acceptance AND at result release**
- **serves:** FWD-1 (contrib), FWD-2 (own), FWD-11 (contrib), FWD-4 (contrib, v0.10)
- **brief sections consumed:** O1; O8; IV.2 auth-validator paragraph, Global/scoped integration sources; **SUPP VI.6 / UI_CONTRACT.md "UI variables and their source", "Internal job envelope"**
- **contracts (P=produces, C=consumes):** P `ResolvedScope`; P `AnalysisRequest.resolved` (server-only)
- **paths: reuse:** `infra/aws/lambda-edge/auth-validator-edge/index.mjs`; partner `roles.ts` x3 (vocabulary only, never grants)
- **paths: new home:** `infra/aws/lambda/investor-reporting/` (scope resolver)
- **fixtures / evidence:** 49F 201-group overlap fixture (no double-count, no manufactured primary credit); INF 79-unmapped-accounts reason list
- **acceptance clause draft:** a partly permitted relationship resolves to the exact allowed subset or an explicit unsupported scope, never the whole with rows hidden after; fingerprint identical on every downstream call

**The CTO's ruling this cell executes (ROUND_ANALYSIS.round1.md @0d57ceb2f9, verbatim):** ONE OPAQUE-ID NORMALIZER. Directory, holdings and performance ids through one admitted transformation (W1-S7, W1-S9, W2-S11); account-only vs relationship grain agreed across schema, projection and payload (W2-S2).

**What L5 adds (decomposition v0.2 s.2, s.6, s.9):**

- ONE module, `infra/aws/lambda/investor-reporting/_ids/ids.py` (a new home admitted under the lambda tree; the gold runners import it by a documented path -- the shared layer `irpt-common` carries it so a Lambda and a runner read one file), with ONE function per id kind: `opaque_account(firm, raw) -> acc_...`, `opaque_relationship`, `opaque_client`, `opaque_firm`, each deterministic, salted per the existing `directory_runner.opaque_id` grammar (this cell MOVES that function here and the runner imports it -- no second definition anywhere; a census of `sha256(` + `[:24]` outside `_ids/` reads 0). NO NAMESPACE PREFIX in an id (W2-S11): the `<firm>:acct:` prefix is removed at its three mint sites in `holdings_snapshot.py` and the firm is a separate typed field.
- THE RAW KEY PER FIRM IS DECLARED, NOT DISCOVERED: `_ids/raw_keys.json` names, per firm and per id kind, the upstream field the opaque id is minted from (49F: the crosswalk's account id; INF: `accounts_v2.account_id`; COT: `fact_model_assignment.external_id` -- IB-s-4's traced facts at row S10/W2-S11 are the starting point; if the directory used a different key for INF or COT, THIS cell changes the directory to the declared key and rebuilds the artifacts in the worktree under QA prefixes). Proof: directory, holdings and performance ids for the same account are EQUAL for all three firms (join `N of N` per firm, denominators printed), and a raw-id or a swapped-firm input to the normalizer REFUSES (typed ids at the boundary, s.8 bound 13).
- THE GRAIN (W2-S2): `DirectoryEntry.ids.relationship_id` nullable stays; the projection and the payloads agree that an account-only entry is a scope of ONE account with `relationship_id: null`, a multi-relationship account lists each relationship, and the permitted account set is NEVER widened by a relationship the viewer does not hold -- three fixtures, one per case, run through `_scope.resolve` and the directory handler in-process.
- The ownership-map `id_projection` (W2-S7) is the same normalizer, so a granted custodian id resolves to the directory's opaque id with no second strip.

---

## WHAT ROUND 1 DELIVERED THAT THIS CELL BUILDS ON (not rebuilt)

`directory_runner.opaque_id` (IB-s-1); the holdings snapshot with its three mint sites (IB-s-12, `holdings_snapshot.py:370/486/638`); IB-s-4's traced facts (49F 7,431 of 7,453 resolve; INF 0 of 790; COT 0 of 946; the prefix difference on top); `_scope.resolve` with `id_projection` and `unmatched_reasons` (IB-s-2); the shared layer `irpt-common` (IB-s-13).

---

## DELIVERABLE

`infra/aws/lambda/investor-reporting/_ids/{ids.py,raw_keys.json,tests/}`; the runner and handler call sites moved onto it (`data/assets/scripts/gold/investor_reporting/{directory_runner.py,holdings_snapshot.py}`, `directory/`, `performance/`, `_scope/`); the layer rebuilt to carry `_ids` (its root re-applied under a ledger entry, `irpt-common:3`); QA-prefix rebuilt artifacts for the three firms; the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_rt_3.py` and `.result.md`.

---

## BOUNDS

- **One definition.** A second hash of the same grammar anywhere is a FAIL of arm (a).
- **No production artifact is overwritten by this cell**: rebuilt directory/holdings artifacts land under QA prefixes (`investor-reporting/qa/...`) in the firm buckets; the production build rides IB-rt-6 after the first-mint.
- **The raw keys are declared in a file with a per-firm source citation** (file:line of the upstream table's schema), never inferred at runtime.

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

<criterion id="RT3-AC1" cell_refs="IB-rt-3"><invocation>timeout 900 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_rt_3.py</invocation><expect>IBRT3-ONE-ID-SPACE</expect></criterion>
**`RT3-AC1` -- PASSES BY OUTPUT -- one definition, equal ids across three producers for three firms, typed refusals, the grain agreed.**
**(a) ONE DEFINITION.** Census of `sha256(` with `[:24]` (or the grammar's equivalent) across `infra/aws/lambda/investor-reporting/` and `data/assets/scripts/gold/investor_reporting/`: 0 outside `_ids/` (denominator printed); the layer zip carries `_ids/ids.py` byte-equal to the repo file.
**(b) THREE PRODUCERS, THREE FIRMS, EQUAL.** For each firm, the account ids minted by the directory build, the holdings build and the performance adapter's scope for the same raw accounts are pairwise equal: `N of N` per firm with N >= the round-1 populations (7,453 / 790 / 946), 0 raw-suffix ids (regex census `:acct:` = 0).
**(c) TYPED REFUSALS.** A raw upstream key, a display name, an e-mail and a swapped-firm input to each normalizer function REFUSE without echoing the input (byte census); `4 of 4` per function.
**(d) THE GRAIN, THREE FIXTURES.** Account-only (`relationship_id: null`, one account), multi-relationship, and a relationship carrying an account outside the viewer's population: through `_scope.resolve` and the directory handler in-process, the permitted set is exactly the expected set (`3 of 3`), never widened.
**(e) THE PROJECTION RESOLVES.** With the ownership-map fixture for each firm, `id_projection` through the normalizer resolves `N of N` granted ids with 0 `UNPROJECTED-ID`.
**(f) THE LAYER LANDED.** `get-layer-version` on `irpt-common` prints the new version; the performance and narrative functions reference it (2 of 2); the ledger CLOSED, sentinel committed (hash); the performance and narrative roots plan clean.

<criterion id="RT3-AC2" cell_refs="IB-rt-3" judgment="true"/>
**`RT3-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: for INF and COT, which raw key the directory USED in round 1 versus the one declared now, and what that means for any artifact a consumer read in round 1; whether the salt/grammar choice makes an id re-identifiable from a public key space; and what the equal-ids proof cannot show about a client that exists in one source and not another. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>RT3-AC1, RT3-AC2</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rt-3.one-opaque-id-normalizer-and-the-grain.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/_ids/
infra/aws/lambda/investor-reporting/_scope/
infra/aws/lambda/investor-reporting/directory/
infra/aws/lambda/investor-reporting/performance/
infra/aws/lambda/layers/irpt-common/
infra/aws/lambda/ci/lambda-layer-map.json
infra/aws/terraform/investor-reporting/performance/
infra/aws/terraform/investor-reporting/narrative/
data/assets/scripts/gold/investor_reporting/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-bckend-rt3.json
infra/aws/lambda/ci/lambda-source-map.json
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.2, cell `IB-rt-3` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-rt-3</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell creates, changes and fires no schedule, rule or trigger. BLIND SPOT, stated: the round-1 cut-time run (5 of 5 carriers, 0 gates naming this project) is inherited, not re-run here.
comp-iam: RUN at the round-1 cut (191 roles parsed, 307 gaps estate-wide) and the round-1 roles now exist on the DESIRED and APPLIED planes; this cell's change to `irpt-performance-adapter, irpt-narrative` is re-graded by the assignee at Phase 1 by `comp-iam service irpt-performance-adapter, irpt-narrative` and at Phase 2 by `comp-iam gaps` -- both recorded in the instance. BLIND SPOT: DESIRED plane only; a GRANTED-BROAD wildcard cannot be falsified by a resource check.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `docs/contracts/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL or its documentation lane at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: RT3-AC1, RT3-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-rt-3.one-opaque-id-normalizer-and-the-grain.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-rt-3.one-opaque-id-normalizer-and-the-grain.proof_of_spec.json RT3-AC1,RT3-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it. The PENDING-THIS-COMMIT sentinel is one-shot: pin artifact rows to the commit that carries them.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
