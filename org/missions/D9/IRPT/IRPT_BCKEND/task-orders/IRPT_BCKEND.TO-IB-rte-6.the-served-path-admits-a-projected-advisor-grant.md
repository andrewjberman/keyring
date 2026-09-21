# TO IRPT_BCKEND.TO-IB-rte-6 -- THE SERVED PATH ADMITS A PROJECTED ADVISOR GRANT: today every live FIRM_ADVISOR request is refused `UNPROJECTED_GRANT` because 0 of 13 entry points pass `id_projection` to the Enforcer and 0 of 22,646 ownership grants join the directory even when the projection is applied by hand (row W1-S22, the finding that the test principal alone unblocks nothing); the wiring is fixed at every entry point, the 49 Financial projection resolves custodian keys through `dim_identity_crosswalk` to the directory's id space (the issuer's REC, pending the CTO's L4 ruling, MEASURED as a join rate), deployed under ledger, and proven on the live routes

<to_id>IRPT_BCKEND.TO-IB-rte-6</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~1</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-18</issued_date>
<status>superseded -- CLOSED for round 5 by 2.0.0_SA_COO~B at 2026-09-19T03:4xZ: its FAIL arm (d) is the entitlement policy the CTO ruled at L4 @61627f39f9 and is re-cut as IB-rtf-2 (round 6); the wiring and the seam stand at HEAD. Was: pending -- HANDED by 2.0.0_SA_COO~B at 2026-09-18T22:0xZ to slot ~1 (cold start) mid-round on row W1-S22 (IB-rte-1 @01ba67fe65): the issuer's ruling -- the WIRING half is ADJUDICABLE at L5/L6 and cut here; the ID-SPACE half is pitched to 1.0.0_SA_CTO with REC (a) the same tick and carried on this face as arm (b), a MEASUREMENT the CTO's ruling confirms or re-cuts. IB-rte-2 is gated on this order's merge.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 5 (the CTO's round-4 analysis @561d6e1cc9, msg 98036) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.14 @b8e98d5a4d (no addendum at round 4) | **Round-4 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND4_ANALYSIS.md` @561d6e1cc9 | **Andrew-direct:** 2026-09-18 ~17:3xZ "Approved" (record `org/tier1_exec/2.0.0_SA_COO~B/deliverables/ANDREW_DIRECT_20260918_173xZ_TWO_OPEN_CALLS_APPROVED_IRPT_BCKEND.md` @af794c77e3) | **Rulings carried:** R-40, R-42, R-44, R-45 @57bc083d45; the forward-looking-criterion bar; Rule 30 | **Decomp cell:** `IB-rte-6` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.5, s.R5) | **outcome_ref:** FWD-1, FWD-2, FWD-5 (the served path)

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~1`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~1;`.
- **Worktree:** `/c/tmp/wk-irpt-5-1b` on branch `wk-irpt_bckend-5-1b`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree; make a path absolute by prefixing `/c/tmp/wk-irpt-5-1b/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~1 <0.9.0_WK_IRPT_BCKEND~1@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/` (granted by the tree convention). Batteries are named `battery_<cell>.py`, the cell id lower-cased with underscores.
- **Python:** `py -3.12`. AWS through `.tools/aws`. `.tools/terraform.exe` is provisioned by the issuer. A recursive `grep`/`find` in Bash is DENIED by a rail hook and a denial aborts the WHOLE call; use the Read/Grep tools and keep a gated read in its own call. Capture `safe-commit.sh` output to a file, never pipe it to `tail`, never pair it with `$( )`.

---

## THE CELL

**The finding (row IRPT_BCKEND-W1-S22, `0.9.0_WK_IRPT_BCKEND~1`, ARMED):** the real `infra/aws/lambda/investor-reporting/_authz/enforce.py` `Enforcer`, wired exactly as `directory/entry.py` wires it in production (`deps=_loaders.deps`, `id_projection` NOT passed), refuses a real request for advisor `abby_horton` / `49financial` against the LIVE directory + LIVE ownership map: `code=UNPROJECTED_GRANT`, *"43 of 43 ownership grants carry ids in a key space this directory cannot be joined on"*. Firm-wide: **0 of 22,646** ownership-map account grants (179 advisors) join the live directory even WITH `_ids.projection_for('49financial')` applied by hand -- the ownership map's raw custodian keys (`z0819594401`-shaped) are not the raw key `_ids/raw_keys.json` declares the 49financial directory mints from (*"the crosswalk's account id, zero-padded to 10 digits"*). A census of every `entry.py` / `handler.py` / `dispatch.py` under `infra/aws/lambda/investor-reporting/` (13 files) shows **0 of 13** pass `id_projection` to `Enforcer`/`Entry`. So the refusal fires for EVERY live FIRM_ADVISOR request today, and FWD-1/2/5's SERVED path has never been reachable.

**The issuer's ruling and its limit:** the WIRING (arm a) is a code defect under the PRD's B1/B2 and is this order's to fix. The ID SPACE (arm b) -- which raw key the ownership map and the directory must share -- is L4's; the issuer's REC (a), pitched to `1.0.0_SA_CTO` this tick, is that the 49financial projection resolves custodian keys THROUGH `dim_identity_crosswalk` (the dimension the K2 grant already lets the 49f principal read) to the crosswalk account id. This order BUILDS (a) and MEASURES its join rate; the CTO's ruling either confirms it or re-cuts it, and arm (a) stands either way.

- (a) THE WIRING: every entry point that constructs an `Enforcer`/`Entry` passes the firm's `id_projection` (`_ids.projection_for(firm)`, resolved from the request's verified firm -- never from a request-controlled token, bound 13); the census `13 of 13` (or the true denominator, printed) after the change reads `13 of 13` wired; a unit test asserts it by AST over the same population so a new entry point cannot regress silently; the refusal path for a grant that STILL does not join keeps its reason and never echoes the refused value.
- (b) THE PROJECTION FOR 49 FINANCIAL, per REC (a): custodian account key -> crosswalk account id via `dim_identity_crosswalk` (read through the assumed 49f principal on the host, or through the projection's existing read path -- name which, cite `file:line @commit`), zero-padded exactly as `_ids/raw_keys.json` declares; the join rate MEASURED before and after over the live ownership map (`n of 22,646`, printed) and per advisor for `abby_horton` (`k of 43`); unmatched grants are counted and named by KIND, never silently dropped. If the crosswalk cannot resolve a class of keys, that class is a row, and the number is the measurement.
- (c) DEPLOY every function that packages the changed modules under a change-management ledger entry (`0 to destroy`; served `CodeSha256 == built`; `lambda-source-map.json` re-pointed); no IAM, no env change.
- (d) PROVEN ON THE LIVE ROUTES: the SAME real request that read `UNPROJECTED_GRANT` in IB-rte-1's arm (a) (advisor `abby_horton` / `49financial`, the real signed request per round 1's harness with the identity IB-rte-1's packet names -- if no live advisor session exists yet, the Enforcer run LIVE against the deployed bytes with the real directory and ownership map, said so) now returns a projected scope: the refusal code is GONE and the served response names `k` permitted accounts (or the truthful smaller number with the unmatched kinds), and a swap to another firm's advisor id is still REFUSED. Negative control: the pre-fix bytes (the prior `CodeSha256`) on the same request read `UNPROJECTED_GRANT`.

---

## DELIVERABLE

The entry-point edits + the projection + tests; the ledger entry; `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_rte_6.py`, `IB-rte-6_R56-AC1_battery_output.txt`, `the-served-path-admits-a-projected-grant.result.md`; the proof instance.

---

## BOUNDS

- The ONLY code touched: the entry points' `Enforcer`/`Entry` construction, `_ids/` projection for 49financial, and their tests; no contract edit; no ownership-map write (the map is READ, a producer outside this project); no directory write; no IAM; no principal created (IB-rte-2's). The CTO's L4 ruling on the id space, if it arrives mid-cell and differs from REC (a), is a STOP on arm (b) only -- record its message id and the ruling, keep arm (a).
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

<criterion id="R56-AC1" cell_refs="IB-rte-6"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_rte_6.py</invocation><expect>IBR56-SERVED-PATH-ADMITS-PROJECTED-GRANT</expect></criterion>
**`R56-AC1` -- PASSES BY OUTPUT:** (a) `13 of 13` entry points wired (denominator printed) with the AST test passing and its mutant (one unwired entry) failing; (b) the join rate before -> after over the live ownership map printed as `n of 22,646` with the unmatched kinds named, and `abby_horton` `k of 43`, `k >= 1`; (c) `N of N` functions deployed under ledger with `CodeSha256 == built`; (d) the live request no longer reads `UNPROJECTED_GRANT` and names `k` permitted accounts, the cross-firm swap still REFUSED, the pre-fix bytes reading `UNPROJECTED_GRANT` as the negative control. The token prints only when every arm holds; the battery re-derives every count from the real world each run.

<criterion id="R56-AC2" cell_refs="IB-rte-6" judgment="true"/>
**`R56-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: what fraction of the firm's grants the crosswalk projection resolves and what the unmatched kinds are (is REC (a) sufficient or does the ownership map's producer need re-keying -- alternative (b)); whether inflection and cottonwood need their own projections (measure their join rates too, `n of M` each, no fix); and whether FWD-1/2/5's served path is now reachable for a real advisor or only for the projected subset. No verdict. Every line citation carries `@<commit-ish>`.

<expected_criteria>R56-AC1, R56-AC2</expected_criteria>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rte-6.the-served-path-admits-a-projected-advisor-grant.md
infra/aws/lambda/investor-reporting/
infra/aws/terraform/investor-reporting/
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.5, cell `IB-rte-6` (s.R5.5 -- the mid-round addition on row W1-S22).
<owned_cells>IB-rte-6</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired; requests are driven.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant changes; the crosswalk read runs under the grant IB-rtc-7 applied (K2, `dim_identity_crosswalk`) or the functions' existing roles; a read this order needs that no existing grant covers is a BLOCKING row, never a widening.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). A path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: R56-AC1, R56-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-rte-6.the-served-path-admits-a-projected-advisor-grant.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and -- R-40 -- the content hash of every produced or served artifact the row grades, EACH PINNED TO THE COMMIT THAT CARRIED IT (commit the battery, its output and the result BEFORE the instance); a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-rte-6.the-served-path-admits-a-projected-advisor-grant.proof_of_spec.json --governing-order org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rte-6.the-served-path-admits-a-projected-advisor-grant.md` BEFORE the complete flip; rc 0 AND R56-AC1 PASS-by-output, then flip this order's `<status>` to `complete` and commit instance and flip together. A FAIL row leaves the order open and is your final report on it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
