# TO IRPT_BCKEND.TO-IB-s-1 -- THE DIRECTORY: a per-firm DirectoryEntry set from Silver and the identity runners, landed in the FIRM's bucket, and a search/resolve handler that makes zero provider calls

<to_id>IRPT_BCKEND.TO-IB-s-1</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~2</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-10</issued_date>
<status>complete -- S1-AC1 PASS-by-output (IBS1-DIRECTORY-SERVED, 6 of 6 arms) and S1-AC2 PASS-by-output (No changes.) re-run by 0.9.0_WK_IRPT_BCKEND~2 on the RESPAWN; S1-AC3 RECORDED as judgment for 3.0.0_SA_CVO at L9. Instance VALID rc=0 (17 artifact rows, 6 of 6 surprise ids resolve, alignment 1/1 cell). The world acts were performed under commits 3654197107 and 4d3d2d10dd by the previous instance of this slot and are read, not re-executed (NEVER-2).</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.4 @62301f71e0 | **Decomp cell:** `IB-s-1` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.1.1, s.1 + s.2) | **outcome_ref:** FWD-1 (contrib), FWD-7 (own) | **PRD candidate:** B1

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~2`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~2;`.
- **Worktree:** `/c/tmp/wk-irpt-1-2` on branch `wk-irpt_bckend-1-2`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-1-2/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~2 <0.9.0_WK_IRPT_BCKEND~2@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/` (granted by the tree convention; no `<paths>` entry needed).
- **Queue:** first in slot ~2. Spawned after IB-s-18 is merged. IB-s-2, IB-s-4, IB-s-12 and IB-s-15 hang off this cell.

---

## THE CELL

**The PRD row, verbatim at @62301f71e0 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B1 directory ingestion + viewer-scoped projection + search service
- **serves:** FWD-1 (contrib), FWD-7 (own)
- **brief sections consumed:** O1; IV.2 identity table, daily-movement paragraph, business-date paragraph
- **contracts (P=produces, C=consumes):** P `DirectoryEntry`
- **paths: reuse:** `data/assets/scripts/silver/silver_registry.py`, `mirror_schemas.py`, `rebalancer_schemas.py`, `bd49f_dim_conversion.py`; `runners_49f/a01_dim_relationship.py`, `a06_dim_identity_crosswalk.py`, `d08_firm_ownership_map.py`, `bd49f_dim_portfolio_group.py`; `runners_inf/a00_dim_account.py`, `a01_dim_relationship.py`, `runner_common.py`; `runners_cot/a01_dim_relationship.py`; `data/firm_registry.json`; `lib/trading_calendar.py`
- **paths: new home:** `data/assets/scripts/gold/investor_reporting/` (directory runner); publisher output in `opal-data-portal-v2`
- **fixtures / evidence:** split evidence manifest; 49F crosswalk `match_method`/`match_as_of`/`in_0833_universe`; INF 874-of-953 identity fixture
- **acceptance clause draft:** duplicate names, account-only entry, multiple relationships, terminated-but-entitled client resolve to the expected authorized set; provider calls during search = 0; as-of and source completion date carried on every entry

**What L5 adds (decomposition v0.1.1 s.2, s.6, s.9):**

- **Destination re-homed (decomposition s.9 finding 1, row `IRPT_BCKEND-S1`):** the directory is NOT published into `opal-data-portal-v2` (an origin with an unauthenticated CloudFront path). It lands in the FIRM's own bucket per `infra/aws/lambda-edge/_shared/firm-config.mjs` FIRM_BUCKET_MAP (49financial -> `opal-data-bd`, and the inflection / cottonwood buckets that map names -- READ it) under `investor-reporting/directory/<as_of>/directory.json` plus a `latest.json` pointer, and is served ONLY through this project's scoped handler after `ResolvedScope`. The QA run writes under `investor-reporting/qa/directory/...` in the same buckets.
- The runner `data/assets/scripts/gold/investor_reporting/directory_runner.py` reads the typed daily sources through `silver_registry.py` and the identity runners the PRD row names (49F: `a01_dim_relationship`, `a06_dim_identity_crosswalk` with `match_method`/`match_as_of`/`in_0833_universe`, `d08_firm_ownership_map`, `bd49f_dim_portfolio_group`; INF: `a00_dim_account`, `a01_dim_relationship`, `runner_common`; COT: `a01_dim_relationship`), selects the completed source set by business date with `lib/trading_calendar.py` (`expected_last_trading_day`, `prev_trading_day`) and each source's completion manifest, and emits `DirectoryEntry` objects that validate against `_contracts/DirectoryEntry.schema.json`: opaque ids, display name + masked discriminator, permitted scope/capabilities, termination indicator SEPARATE from access, cohort/capability facts when authoritative (UNKNOWN otherwise), directory/source revision and as-of. The 201-group overlap must not double-count accounts; the 79 unmapped INF accounts carry a reason each.
- The handler `infra/aws/lambda/investor-reporting/directory/handler.py` (Lambda `irpt-directory-search`, role `irpt-directory-role`, module `yang-lambda`, artifact `investor-reporting/irpt-directory-search.zip`): `search(q)` over the viewer's projection and `resolve(selection)` to the unique permitted account set + fingerprint, consuming `ResolvedScope` (a FIXTURE scope in this cell; IB-s-2 supplies the real resolver next in this slot). It imports NO vendor client; provider calls per keystroke = 0 by construction, censused.
- Applied from `infra/aws/terraform/investor-reporting/directory/` under a ledger entry. The production schedule for the runner is IB-s-4's; this cell runs the runner AD HOC for QA (permitted) and deploys the handler.

---

## DELIVERABLE

`data/assets/scripts/gold/investor_reporting/directory_runner.py` + `tests/`; `infra/aws/lambda/investor-reporting/directory/handler.py` + `tests/`; `infra/aws/terraform/investor-reporting/directory/` (`lambda.tf`, `iam.tf` -- the role's read grant is the firm buckets' `investor-reporting/directory/*` prefixes only); the ledger entry + sentinel; the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_s_1.py` and `.result.md`; the QA directory objects under `investor-reporting/qa/directory/` in each firm bucket.

---

## BOUNDS

- **NO provider call, ever.** The directory is built from Silver and the identity runners; a Black Diamond, Orion or YCharts client import in this cell's code fails arm (d).
- **Fuzzy matching is reconciliation prior art, not an authorization rule** (`build_schwab_bd_account_xref.py`); a name never authorizes.
- **Test/demo firms are excluded** (`firm_registry.json` kind).
- **Do not write outside `investor-reporting/` in the firm buckets**; the QA prefix is `investor-reporting/qa/`. Nothing under `platinum/`, `mdpf/` or any existing prefix is touched.
- **The production code deploy of the runner (`safe-deploy.sh`) is a rule-13 act** (row `IRPT_BCKEND-S4`): attempt it ONCE under the ledger; a refusal for your serial is a BLOCKING row on arm (f), not an override.

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

<criterion id="S1-AC1" cell_refs="IB-s-1"><invocation>timeout 600 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_s_1.py</invocation><expect>IBS1-DIRECTORY-SERVED</expect></criterion>
**`S1-AC1` -- PASSES BY OUTPUT -- the directory built, validated, landed and searchable; provider calls zero by census.**
**(a) THREE FIRMS, THREE DIRECTORIES, EVERY ENTRY VALID.** The QA run builds a directory per registry firm; every entry validates against the schema; print per firm the entry count, the as-of, the source completion date and the business date the calendar selected.
**(b) THE FIXTURE CASES RESOLVE TO THE EXPECTED AUTHORIZED SET.** A fixture directory carrying duplicate names, an account-only entry, multiple relationships, a terminated-but-entitled client and a partly permitted relationship: `search` returns an unambiguous selection for each; `resolve` returns exactly the expected permitted account set (or an explicit unsupported scope for the partly permitted relationship, never the whole with rows hidden); the terminated client is VISIBLE, marked terminated; print `N of N` cases.
**(c) NO DOUBLE COUNT, EVERY GAP REASONED.** The 49F 201-group overlap: unique accounts before == after grouping (printed); INF unmapped accounts each carry a reason (print `79 of 79` or the live count with its denominator).
**(d) ZERO PROVIDER CALLS -- THE CENSUS.** Enumerate the imports of the runner and the handler (denominator printed) and show none resolves to a vendor client module; run `search` over 100 fixture keystrokes with a network stub that RAISES on any outbound call: 0 raised.
**(e) THE DIFFERENCE CONTROL ON SCOPE.** The same `search` with a `ResolvedScope` fixture for advisor A and for advisor B returns disjoint result sets where the fixture says they must; with a revoked fixture it returns nothing. Printed.
**(f) LANDED AND DEPLOYED.** `head-object` on each firm's QA `latest.json`; `get-function-configuration irpt-directory-search` prints `CodeSha256` equal to the sha256 of the built zip; the ledger CLOSED and the sentinel committed (hash). If `safe-deploy.sh` refuses the runner's code deploy for your serial, print the refusal verbatim, file the BLOCKING row, and this arm reads BLOCKED (the battery still prints its other arms and NOT the token).

<criterion id="S1-AC2" cell_refs="IB-s-1"><invocation>timeout 120 .tools/terraform.exe -chdir=infra/aws/terraform/investor-reporting/directory plan -no-color -input=false -lock=false</invocation><expect>No changes\. Your infrastructure matches the configuration\.</expect></criterion>
**`S1-AC2` -- THE ROOT IS CONVERGED after this cell's apply.**
Run after the apply and after the ledger closes.

<criterion id="S1-AC3" cell_refs="IB-s-1" judgment="true"/>
**`S1-AC3` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: which identity inputs you treated as AUTHORITATIVE and which as reconciliation prior art, with the line you read for each; whether the masked discriminator can leak a name; and what an advisor could still be shown that the entitlement half (IB-s-2) must refuse. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>S1-AC1, S1-AC2, S1-AC3</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-1.the-directory-runner-and-the-search-resolve-handler.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
data/assets/scripts/gold/investor_reporting/
infra/aws/lambda/investor-reporting/directory/
infra/aws/terraform/investor-reporting/directory/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-bckend-s1.json
infra/aws/lambda/ci/lambda-source-map.json
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.1.1, cell `IB-s-1` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-s-1</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: RUN at the cut (20:2xZ, --budget 150) -- WITHIN BUDGET, denominator 5 of 5 carriers (C1=92 C2=6 C3=12 C4=20 C5=335), 25 gates ARMED, 0 name IRPT or any surface of this cell; the moratoria that bind here are G-20 (no monitor), G-23 (cross-firm), G-24 (vendor egress). BLIND SPOT: a ledger of gates, not prose obligations; 137 prose blocking fields unread.
comp-iam: RUN at the cut -- `comp-iam stats` + `roles`: denominator 191 roles parsed, 188 services, 307 gaps estate-wide; ZERO investor-reporting roles exist on the DESIRED plane, so this cell's role is graded at Phase 1 by `comp-iam service irpt-directory-search` once its `.tf` exists and at Phase 2 by `comp-iam gaps` -- both recorded in the instance. BLIND SPOT: DESIRED plane only (the repo's Terraform); a GRANTED-BROAD wildcard cannot be falsified by a resource check.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable (a fresh cut has no prior artifact for it to read).
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: S1-AC1, S1-AC2, S1-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-s-1.the-directory-runner-and-the-search-resolve-handler.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-s-1.the-directory-runner-and-the-search-resolve-handler.proof_of_spec.json S1-AC1,S1-AC2,S1-AC3` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
