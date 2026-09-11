# TO IRPT_BCKEND.TO-IB-s-4 -- DIRECTORY FRESHNESS, DRIVEN: the refresh schedule, the expiry/fallback, and a controlled-clock harness that drives all five arms with no real-calendar wait

<to_id>IRPT_BCKEND.TO-IB-s-4</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~2</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-10</issued_date>
<status>staged -- assigned to slot ~2; becomes pending when the COO hands it over after IB-s-3 is terminal and merged.</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.4 @62301f71e0 | **Decomp cell:** `IB-s-4` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.1.1, s.1 + s.2) | **outcome_ref:** FWD-7 (own) | **PRD candidate:** B4

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~2`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~2;`.
- **Worktree:** `/c/tmp/wk-irpt-1-2` on branch `wk-irpt_bckend-1-2`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-1-2/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~2 <0.9.0_WK_IRPT_BCKEND~2@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/` (granted by the tree convention; no `<paths>` entry needed).
- **Queue:** fourth in slot ~2, after IB-s-3 (it depends on IB-s-1; the slot's order puts the library first so the handler can use it).

---

## THE CELL

**The PRD row, verbatim at @62301f71e0 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B4 directory refresh schedule, expiry/fallback, controlled-clock harness
- **serves:** FWD-7 (own)
- **brief sections consumed:** O1 refresh; O7 clocks/manifests; IV.2 business-date paragraph
- **contracts (P=produces, C=consumes):** P `DirectoryEntry.revision`; P `StatusEnvelope` (stale)
- **paths: reuse:** `lib/trading_calendar.py`; each source's completion manifest
- **paths: new home:** `infra/aws/terraform/investor-reporting/` (scheduler)
- **fixtures / evidence:** source fixtures for the five arms
- **acceptance clause draft:** all five arms driven on a controlled clock: added client, changed eligibility, MISSED trigger, FAILED refresh, OVER-AGE request -- each reads differently; no real-calendar wait

**What L5 adds (decomposition v0.1.1 s.2, s.6, s.9):**

- `infra/aws/lambda/investor-reporting/directory/refresh.py`: the refresh entry (invokes the directory runner's build for a firm on a business date; records a completion manifest with the source dates and a MISSED / FAILED / COMPLETED status distinct in the `StatusEnvelope` it emits), `expiry.py`: the declared refresh window and the over-age behaviour (a request served from a directory older than the schedule's ceiling gets the declared expiry/fallback response, never a silent answer). The oldest directory an advisor can be served is set by the SCHEDULE.
- The schedule: an EventBridge Scheduler rule in `infra/aws/terraform/investor-reporting/directory/schedule.tf` on the trading-day cadence the cell declares (measured from the sources' completion cadence, then declared -- the brief's 09:00 ET is context, not an SLA), ENABLED, targeting the runner's Lambda entry. It fires on Opal-owned sources only (no vendor call), so it may be enabled.
- The harness under `deliverables/`: injects a controlled clock and source fixtures and drives the FIVE arms -- an added client, a changed eligibility, a MISSED trigger, a FAILED refresh, an OVER-AGE request -- each producing a DIFFERENT observable; total harness runtime printed and under 60 s.

**ISSUER AMENDMENT (2.0.0_SA_COO~B, 2026-09-11 ~00:2xZ, before this order was handed -- a cut defect of the issuer, surfaced on a worker's row):**
- **FIRST-MINT IS EXPLICIT, AND THE EXIT CODE IS NOT THE DELIVERY (row `IRPT_BCKEND-W2-S5`).** `.tools/safe-deploy.sh` on a shared home whose prefix carries 0 members emits `SKIP-NOT-MEMBER` and exits rc=0 with `OK: safe-deploy gate PASS` -- a GATE verdict with NOTHING deployed, and the disclaiming lines sit below the OK where a tail-read misses them. The production code deploy of this cell's runner is that FIRST-MINT: read `.tools/safe-deploy.sh`'s own header for the explicit first-mint mechanism it names and use it (never a bare `aws s3 cp`); then verify the ARTIFACT on the served prefix (`head-object` on the landed key: size and ETag/sha printed beside the built file's), never the guard's exit code. If the guard names a lane this serial cannot satisfy for the first-mint, that is a BLOCKING row on the deploying arm, not an override. This cell's schedule targets the runner's PRODUCTION code, so the runner's first-mint to the shared home is THIS cell's act and its verification is arm (h).

---

## DELIVERABLE

`infra/aws/lambda/investor-reporting/directory/refresh.py`, `expiry.py` + tests; `infra/aws/terraform/investor-reporting/directory/schedule.tf`; the ledger entry + sentinel; the harness `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/ib_s_4_controlled_clock.py`; the battery `battery_ib_s_4.py` and `.result.md`.

---

## BOUNDS

- **NO REAL-CALENDAR WAIT ANYWHERE.** Every arm is driven by the injected clock; a `sleep` longer than one second in the harness fails arm (f).
- **This is directory freshness and eligibility only; revocation is FWD-2's** and is not graded here.
- **Terminated clients stay visible under entitlement**: a changed eligibility that ends offering a client must not delete it from the directory.

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

<criterion id="S4-AC1" cell_refs="IB-s-4"><invocation>timeout 300 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_s_4.py</invocation><expect>IBS4-FRESHNESS-DRIVEN</expect></criterion>
**`S4-AC1` -- PASSES BY OUTPUT -- five arms, five different readings, on a controlled clock.**
**(a) ADDED CLIENT** appears within the declared window without anyone asking; **(b) CHANGED ELIGIBILITY** ceases to be offered within the window and stays VISIBLE marked terminated; **(c) MISSED TRIGGER** reads MISSED; **(d) FAILED REFRESH** reads FAILED; **(e) OVER-AGE REQUEST** hits the declared expiry/fallback -- print the five status values and assert they are pairwise distinct (`5 of 5`).
**(f) NO WAIT.** Harness wall-clock printed and < 60 s; no `sleep` > 1 s (source census printed).
**(h) THE RUNNER'S FIRST-MINT LANDED -- THE ARTIFACT, NOT THE EXIT CODE.** `head-object` on the runner's key under the shared home prints size and ETag/sha equal to the built file's; the guard's own SKIP line, if it appeared, is printed beside it as what it is (a gate verdict); a BLOCKED lane is a BLOCKING row.
**(g) THE SCHEDULE IS APPLIED AND ENABLED.** `aws scheduler get-schedule --name irpt-directory-refresh` prints `State: ENABLED` and the declared expression; the ledger CLOSED and the sentinel committed (hash).

<criterion id="S4-AC2" cell_refs="IB-s-4"><invocation>timeout 120 .tools/terraform.exe -chdir=infra/aws/terraform/investor-reporting/directory plan -no-color -input=false -lock=false</invocation><expect>No changes\. Your infrastructure matches the configuration\.</expect></criterion>
**`S4-AC2` -- THE ROOT IS CONVERGED after this cell's apply.**
Run after the apply and after the ledger closes.

<criterion id="S4-AC3" cell_refs="IB-s-4" judgment="true"/>
**`S4-AC3` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: how you measured the cadence you declared (which source completion manifests, over how many days), and what the harness's controlled clock cannot show about the real scheduler (time zones, DST, a missed fire nobody observes). No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>S4-AC1, S4-AC2, S4-AC3</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-4.directory-freshness-driven-on-a-controlled-clock.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/directory/
infra/aws/terraform/investor-reporting/directory/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-bckend-s4.json
infra/aws/lambda/ci/lambda-source-map.json
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.1.1, cell `IB-s-4` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-s-4</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: RUN at the cut (20:2xZ, --budget 150) -- WITHIN BUDGET, denominator 5 of 5 carriers (C1=92 C2=6 C3=12 C4=20 C5=335), 25 gates ARMED, 0 name IRPT or any surface of this cell; the moratoria that bind here are G-20 (no monitor), G-23 (cross-firm), G-24 (vendor egress). BLIND SPOT: a ledger of gates, not prose obligations; 137 prose blocking fields unread. This cell CREATES one schedule (irpt-directory-refresh, ENABLED, Opal-owned sources only).
comp-iam: RUN at the cut -- `comp-iam stats` + `roles`: denominator 191 roles parsed, 188 services, 307 gaps estate-wide; ZERO investor-reporting roles exist on the DESIRED plane, so this cell's role is graded at Phase 1 by `comp-iam service irpt-directory-refresh` once its `.tf` exists and at Phase 2 by `comp-iam gaps` -- both recorded in the instance. BLIND SPOT: DESIRED plane only (the repo's Terraform); a GRANTED-BROAD wildcard cannot be falsified by a resource check.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable (a fresh cut has no prior artifact for it to read).
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: S4-AC1, S4-AC2, S4-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-s-4.directory-freshness-driven-on-a-controlled-clock.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-s-4.directory-freshness-driven-on-a-controlled-clock.proof_of_spec.json S4-AC1,S4-AC2,S4-AC3` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
