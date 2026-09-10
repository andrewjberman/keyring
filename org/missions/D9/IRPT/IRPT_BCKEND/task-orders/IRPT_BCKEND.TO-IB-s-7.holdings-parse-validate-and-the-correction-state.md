# TO IRPT_BCKEND.TO-IB-s-7 -- HOLDINGS PARSE AND THE CORRECTION STATE: deterministic CSV/XLSX parsing that keeps units, cells, totals and cash, never discards an unmatched holding, and sends uncertainty to a correction state

<to_id>IRPT_BCKEND.TO-IB-s-7</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~3</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-10</issued_date>
<status>staged -- assigned to slot ~3; becomes pending when the COO hands it over after IB-s-6 is terminal and merged.</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.4 @62301f71e0 | **Decomp cell:** `IB-s-7` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.1.1, s.1 + s.2) | **outcome_ref:** FWD-9 (own), FWD-4 (contrib) | **PRD candidate:** B7

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~3`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~3;`.
- **Worktree:** `/c/tmp/wk-irpt-1-3` on branch `wk-irpt_bckend-1-3`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-1-3/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~3 <0.9.0_WK_IRPT_BCKEND~3@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/` (granted by the tree convention; no `<paths>` entry needed).
- **Queue:** third in slot ~3, after IB-s-6.

---

## THE CELL

**The PRD row, verbatim at @62301f71e0 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B7 holdings parse + validate + correction state
- **serves:** FWD-9 (own), FWD-4 (contrib)
- **brief sections consumed:** O3 parse paragraph; IV.4 parse paragraph
- **contracts (P=produces, C=consumes):** P `AnalysisRequest.normalized holdings / findings / corrections`; P `StatusEnvelope.needs-correction`
- **paths: reuse:** --
- **paths: new home:** `infra/aws/lambda/investor-reporting/` (parser)
- **fixtures / evidence:** supported CSV/XLSX specimens; `$:CASH`; share-class mapping cases
- **acceptance clause draft:** deterministic parse keeps units, source cells, totals, grouping and cash; unmatched holdings are never discarded or silently substituted; approved substitutions captured explicitly; uncertain items enter the correction state; `management_fee=0.003` is the recorded current setting

**What L5 adds (decomposition v0.1.1 s.2, s.6, s.9):**

- `infra/aws/lambda/investor-reporting/intake/parse.py`: deterministic parsing of the supported CSV/XLSX shapes (synthetic specimens shaped per S8, since real ones are a named gap) retaining units, source cells, totals, security/share-class mapping, grouping and cash (`$:CASH`); field-level provenance to the attachment; findings for anything not read; the correction state (`needs-correction`) on the `AnalysisRequest` revision with the `StatusEnvelope` value `needs-correction`; an analyzer PROPOSES (never applies) substitutions, and an approved substitution is captured explicitly on the next revision.
- Recorded settings as data, not code constants: annual `management_fee=0.003` (July's 0.01 is historical), quarterly rebalancing, dividends false, oldest start, prior close, non-qualified, `^SPXTR` -- declared in `settings.json` with their source, verified after creation by IB-s-9.
- Revisions are immutable: a correction produces revision r+1; r is never rewritten.

---

## DELIVERABLE

`infra/aws/lambda/investor-reporting/intake/parse.py`, `corrections.py`, `settings.json` + `tests/` + `fixtures/holdings/`; the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/battery_ib_s_7.py` and `.result.md`.

---

## BOUNDS

- **An unmatched holding is never dropped and never silently substituted with an ETF** -- arm (b) is the difference control.
- **No deploy in this cell** (the intake Lambda's next build in this slot carries it).
- **A default tax setting is not client tax status; a No Benchmark template does not remove the calculation benchmark** -- both recorded in `settings.json` as facts, not defaults applied to a client.

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

<criterion id="S7-AC1" cell_refs="IB-s-7"><invocation>timeout 300 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/battery_ib_s_7.py</invocation><expect>IBS7-PARSE-DETERMINISTIC</expect></criterion>
**`S7-AC1` -- PASSES BY OUTPUT -- deterministic, lossless, correctable.**
**(a) DETERMINISTIC.** The same specimen parsed twice yields byte-identical normalized holdings; printed.
**(b) NOTHING DROPPED -- THE DIFFERENCE CONTROL.** A specimen with one unresolvable ticker: the output carries it as a finding with its source cell; a deliberately broken parser build that drops it FAILS the same arm. Both printed.
**(c) UNITS, CELLS, TOTALS, CASH.** Every normalized row carries units and its source cell; the sum of rows equals the specimen's stated total (or a finding names the difference); `$:CASH` is preserved as cash. Printed with denominators.
**(d) THE CORRECTION STATE.** Uncertain items enter `needs-correction`; a correction produces revision r+1 and leaves r untouched (hashes printed); an approved substitution is explicit on r+1.
**(e) SETTINGS ARE DATA.** `settings.json` carries the seven recorded settings with sources; `management_fee == 0.003`. Printed.

<criterion id="S7-AC2" cell_refs="IB-s-7" judgment="true"/>
**`S7-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: which holdings shapes your synthetic specimens cannot represent (multi-sheet workbooks, merged cells, non-USD), and how a real specimen would change the parser; and where 'programmatic by default, review the exception' could quietly become 'review everything'. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>S7-AC1, S7-AC2</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-7.holdings-parse-validate-and-the-correction-state.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/intake/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.1.1, cell `IB-s-7` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-s-7</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell creates, changes and fires no schedule, rule or trigger; it builds a library and runs a local battery. BLIND SPOT, stated: the cut-time run (5 of 5 carriers, 0 gates naming this project) is inherited from the issuance, not re-run here.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted and nothing applied by this cell; no policy, role or trust document is written. BLIND SPOT: the reads this cell makes run under the launching seat's credentials, which is stated, not measured.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable (a fresh cut has no prior artifact for it to read).
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: S7-AC1, S7-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/IRPT_BCKEND.TO-IB-s-7.holdings-parse-validate-and-the-correction-state.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/IRPT_BCKEND.TO-IB-s-7.holdings-parse-validate-and-the-correction-state.proof_of_spec.json S7-AC1,S7-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
