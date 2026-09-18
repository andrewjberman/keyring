# TO IRPT_BCKEND.TO-IB-rte-1 -- THE BOUNDED TEST PRINCIPAL DECLARED AND ITS SIGN-OFF PACKET: Andrew approved (17:3xZ) ONE firm-scoped test advisor identity with terminated-client visibility, created under both never-widen halves and deleted at round close; this cell names the identity plane the scoped API actually trusts, every object the principal needs to exist, every route it can reach, the blast radius per key, the deletion as rollback, and the exercise plan that makes FWD-1/2/5/11 EXERCISED by artifact hash -- it DECLARES and creates NOTHING

<to_id>IRPT_BCKEND.TO-IB-rte-1</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~1</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-18</issued_date>
<status>complete -- 0.9.0_WK_IRPT_BCKEND~1, 2026-09-18. R51-AC1 PASSES BY OUTPUT (battery token IBR51-TEST-PRINCIPAL-DECLARED-AND-PACKETED, rc=0, re-run twice identical); R51-AC2 RECORDED for 3.0.0_SA_CVO at L9, no verdict. NEVER_WIDEN_SIGNOFF_PACKET_IB-rte-1.md written for 1.0.0_SA_CTO + 2.0.0_SA_COO~B; nothing created on any live plane. Four rows filed (IRPT_BCKEND-W1-S21..S24), the most consequential being W1-S22: 0 of 13 live entry points wire id_projection, so the bounded principal alone does not make FWD-1/2/5's SERVED path exercisable against live 49financial data -- named for IB-rte-2 and for L9 rather than fixed. proof-of-spec-check.py rc=0.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 5 (the CTO's round-4 analysis @561d6e1cc9, msg 98036) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.14 @b8e98d5a4d (no addendum at round 4) | **Round-4 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND4_ANALYSIS.md` @561d6e1cc9 | **Andrew-direct:** 2026-09-18 ~17:3xZ "Approved" (record `org/tier1_exec/2.0.0_SA_COO~B/deliverables/ANDREW_DIRECT_20260918_173xZ_TWO_OPEN_CALLS_APPROVED_IRPT_BCKEND.md` @af794c77e3) | **Rulings carried:** R-40, R-42, R-44, R-45 @57bc083d45; the forward-looking-criterion bar; Rule 30 | **Decomp cell:** `IB-rte-1` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.5, s.R5) | **outcome_ref:** FWD-1, FWD-2, FWD-5, FWD-11

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~1`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~1;`.
- **Worktree:** `/c/tmp/wk-irpt-5-1` on branch `wk-irpt_bckend-5-1`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree; make a path absolute by prefixing `/c/tmp/wk-irpt-5-1/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~1 <0.9.0_WK_IRPT_BCKEND~1@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/` (granted by the tree convention). Batteries are named `battery_<cell>.py`, the cell id lower-cased with underscores.
- **Python:** `py -3.12`. AWS through `.tools/aws`. `.tools/terraform.exe` is provisioned by the issuer. A recursive `grep`/`find` in Bash is DENIED by a rail hook and a denial aborts the WHOLE call; use the Read/Grep tools and keep a gated read in its own call. Capture `safe-commit.sh` output to a file, never pipe it to `tail`, never pair it with `$( )`.

---

## THE CELL

**The word and its scope (record @af794c77e3, verbatim REC adopted):** *"one firm-scoped test advisor identity with terminated-client visibility, created under a never-widen sign-off (CTO+COO) and deleted at round close ... never a standing account."* The CTO's placement (analysis s.6/s.8): round 5's highest-value cell -- it gates FWD-1, FWD-2, FWD-5 and FWD-11, none of which has ever been exercised at a live session because there has never been a principal to exercise them with.

- (a) THE IDENTITY PLANE, MEASURED NOT ASSUMED: how a live request to the 11 scoped routes resolves its `principal_class` (`FIRM_ADVISOR` / `FIRM_OPERATIONS` / `OPAL_GLOBAL`) and its firm -- read `infra/aws/lambda/investor-reporting/_authz/enforce.py` (`resolve_now`, the header/claims it trusts, cited `file:line @commit`), the API's authorizer in `infra/aws/terraform/investor-reporting/` (Cognito user pool? JWT authorizer? which issuer, which claims), the round-1 harness this project used for real signed requests (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/` round-1 results and `_authz/tests/fixtures.py`, which names the credential bound 6 forbids in a fixture). State the ONE object that makes a principal a FIRM_ADVISOR of ONE firm, and every object the enforcer's dependency triple reads for it (`loaders.py`: the directory, `platinum/{firm}/ownership_map.json`, the policy) -- `N of N` objects named with their current bytes' hashes.
- (b) THE PRINCIPAL, SHAPED: firm = the one whose directory carries a TERMINATED client entry today (read the three landed directories under `s3://opal-data-bd/investor-reporting/directory/2026-09-16/` -- terminated count per firm, printed; pick the firm with >= 1, say which); the advisor id it maps to (an ISSUED opaque id per bound 13, minted by the same instrument the directory uses, never a display name); its entitlement set (the permitted accounts FWD-1 names; the terminated client VISIBLE with the capability gap per FWD-1's CONSTRAINT); what it can NOT reach (any other firm; any route outside `api/scoped/`; every export/global path FWD-2/FWD-11 fence). Name each object the creation writes (the identity-provider user, the ownership map row, any directory annotation) as a KEY K1..Kn with its rollback (the deletion / the row removal), in the shape of `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtc-6.md`.
- (c) THE EXERCISE PLAN, per outcome, as the bar IB-rte-2 will run: FWD-1 (search -> select -> relationship + permitted accounts + the directory's as-of; vendor request count ZERO; the terminated client visible with the gap), FWD-2 (every tab and export ONLY within the permitted set; a swap to another firm's id REFUSED without echoing it), FWD-5 (current custody holdings + model percentages for a permitted account), FWD-11 (an OPAL_GLOBAL viewer across every firm -- state whether the SAME principal can carry both classes or a second bounded identity is needed, and cost it). Each arm names the route, the real signed request, the artifact it produces and the hash the instance will bind (R-40), and its NEGATIVE control.
- (d) THE PACKET `NEVER_WIDEN_SIGNOFF_PACKET_IB-rte-1.md` under your deliverables home: keys, blast radius per key (who else could use this identity; what data it can read; what the fence denies it), rollback per key (deletion, verified by a read that then FAILS), writers/readers census of the identity plane (the census instrument IB-rtc-6 used, adapted; `n of M` principals that could create or modify such an identity), the lifetime bound (deleted at round close by IB-rte-2's own last arm, or earlier on any STOP), and the negative controls. For `1.0.0_SA_CTO` + `2.0.0_SA_COO~B`. Nothing created.

---

## DELIVERABLE

`battery_ib_rte_1.py`, `IB-rte-1_R51-AC1_battery_output.txt`, `the-test-principal-declared.result.md`, `NEVER_WIDEN_SIGNOFF_PACKET_IB-rte-1.md`; the proof instance.

---

## BOUNDS

- READ-ONLY on every live plane: no identity created, no ownership map written, no directory annotated, no policy changed, no apply. No credential of any kind in any artifact (bound 6): the packet names objects and mechanisms, never a secret value; `describe-secret` prints version state only.
- **THE FORWARD-LOOKING-CRITERION BAR (round-3 analysis s.4, ADOPTED; R-68's shape):** no criterion on this face certifies what a future event WILL find or load; every claim about a run or a served artifact is bound to that artifact's CONTENT HASH (`VersionId`/`ETag`/`sha256`/`CodeSha256`/`git hash-object`) READ AT THE EVENT -- a prediction made before the event is not evidence and a battery that prints one is refused at the drain.
- **S56 (ARMED, the CVO's): EVERY line citation in this order's JUDGMENT RECORD and result carries a vintage -- `path:line @ <commit-ish>` -- a bare `:NNN` is a defect the issuer greps for at the drain (`0 of N` bare citations is the bar).** CLAUDE.md Rule 22: a citation without a vintage is not a citation.
- **S73 (the `comp-iam roles` snapshot with no vintage) is an ESTATE-INSTRUMENT defect routed elsewhere and does NOT ride this order:** a live-plane IAM read here uses `comp-iam live` or `.tools/aws iam get-role`, never `comp-iam roles`.
- **R-40 (standing bar, `1.0.0_SA_CTO` @233f5fd5e4):** every criterion whose subject is a RUN or a PRODUCED ARTIFACT records that artifact's CONTENT HASH (`git hash-object`, `sha256sum`, or the service's own digest such as `ETag`/`CodeSha256`) beside its run id in the instance, and is graded against the hash; a label, a path or a timestamp ordering is not an identity.
- **Surprises:** ONE row per premise that does not hold, path that is not where this face says, result the invocation does not produce, or capability you lack -- at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W1-S<k>` with k continuing that coordinate's numbering (read the file's highest `W1-S<k>` first; the file now holds SEVERAL fenced json blocks -- append your object INSIDE THE FIRST fence's array at its end, LF line endings, UTF-8 written explicitly, no json fence marker inside any row's text, `surfaced_at` a full ISO timestamp, omit `disarm_owner` on an INERT row and name a SEAT SERIAL, never a cell, when ARMED (R-42)); then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.

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

<criterion id="R51-AC1" cell_refs="IB-rte-1"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_rte_1.py</invocation><expect>IBR51-TEST-PRINCIPAL-DECLARED-AND-PACKETED</expect></criterion>
**`R51-AC1` -- PASSES BY OUTPUT:** (a) the identity plane cited `file:line @commit` with the `N of N` dependency objects and their hashes; (b) the firm chosen by its measured terminated-client count, the advisor id shape as an ISSUED id, keys K1..Kn each with a rollback; (c) four outcome arms each with route, request, artifact, hash binding and negative control; (d) the packet written with blast radius, rollback, the identity-plane census `n of M`, and the lifetime bound. The token prints only when every arm holds; the battery re-derives every count from the real world each run and never reads its own earlier output.

<criterion id="R51-AC2" cell_refs="IB-rte-1" judgment="true"/>
**`R51-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: whether one bounded identity can serve all four outcomes or FWD-11 needs a second (and what that costs); whether the identity plane the API trusts is the one the PRD's B1/B2 (identity, tenant scoping) describe or has drifted; and what remains unexercisable even with the principal (name it). No verdict. Every line citation carries `@<commit-ish>`.

<expected_criteria>R51-AC1, R51-AC2</expected_criteria>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rte-1.the-bounded-test-principal-declared-and-its-sign-off-packet.md
infra/aws/terraform/investor-reporting/
infra/aws/lambda/investor-reporting/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.5, cell `IB-rte-1` (s.R5 -- the round-5 rectangle, edges, seating and bounds).
<owned_cells>IB-rte-1</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired; a declaration.
comp-iam: DECLARED-NOT-APPLICABLE at the cut (read-only); the packet's identity-plane census is arm (d), with the census instrument's blind spot (identity policies only; an identity provider's own admin surface is not IAM) stated there.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `.tools/**`, `data/**` and `lib/**` path resolves to its own lane at HEAD and is admitted ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: R51-AC1, R51-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-rte-1.the-bounded-test-principal-declared-and-its-sign-off-packet.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and -- R-40 -- the content hash of every produced or served artifact the row grades, EACH PINNED TO THE COMMIT THAT CARRIED IT (commit the battery, its output and the result BEFORE the instance); a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-rte-1.the-bounded-test-principal-declared-and-its-sign-off-packet.proof_of_spec.json --governing-order org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rte-1.the-bounded-test-principal-declared-and-its-sign-off-packet.md` BEFORE the complete flip; rc 0 AND R51-AC1 PASS-by-output, then flip this order's `<status>` to `complete` and commit instance and flip together. A FAIL row leaves the order open and is your final report on it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
