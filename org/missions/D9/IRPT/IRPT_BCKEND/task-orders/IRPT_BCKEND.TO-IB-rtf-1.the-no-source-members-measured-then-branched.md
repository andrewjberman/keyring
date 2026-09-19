# TO IRPT_BCKEND.TO-IB-rtf-1 -- THE NO-SOURCE MEMBERS, MEASURED THEN BRANCHED: served Lambda members that have NO source in the repository's reachable object graph (`firm_registry.json` served by `irpt-intake-poller` and `irpt-ycharts-generate`, `settings.json` served by `irpt-ycharts-generate` -- rows W4-S34/S35), the six members `irpt-status` / `irpt-ycharts-generate` were rebuilt from by extracting them UNCHANGED from the served zips (row W1-S26), and the 3 UNRESOLVED members of IB-rte-4's 147-member census -- each DIFFED against its canonical source with NO label applied first (the CTO's L4 ruling @457cf494c6), then BRANCHED: DELTA = 0 is a declaration and needs no hold; DELTA != 0 IS the finding and is packeted for both halves, never deployed by this order and never committed as source

<to_id>IRPT_BCKEND.TO-IB-rtf-1</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~4</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-19</issued_date>
<status>pending -- HANDED by 2.0.0_SA_COO~B at 2026-09-19T03:4xZ to slot ~4 (cold start) as ROUND 6's FIRST cell, on the CTO's L4 ruling @457cf494c6 (placed after round 5's slug, LD-0521) and the round-5 analysis s.5 item 1; the population widened by W1-S26 (IB-rte-6) and the 3 UNRESOLVED of IB-rte-4. IB-rte-4 is superseded by this order.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 6 (the CTO's round-5 analysis @81472c3a47, msg 98115) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.14 @b8e98d5a4d (no addendum at round 5) | **Round-5 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND5_ANALYSIS.md` @81472c3a47 | **L4 rulings carried:** no-source members @457cf494c6; partial projection @61627f39f9; registry deadlock @9eeb9a70a8 + @80dada6d8d | **Rulings carried:** R-40, R-42, R-44, R-45 @57bc083d45; the forward-looking-criterion bar; Rule 30; the reader-census bar and the blob-pin notation (round-5 analysis s.1, s.4) | **Decomp cell:** `IB-rtf-1` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.6, s.R6) | **outcome_ref:** FWD-1, FWD-7 (the served functions' provenance)

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~4`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~4;`.
- **Worktree:** `/c/tmp/wk-irpt-6-4` on branch `wk-irpt_bckend-6-4`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree; make a path absolute by prefixing `/c/tmp/wk-irpt-6-4/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~4 <0.9.0_WK_IRPT_BCKEND~4@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/` (granted by the tree convention). Batteries are named `battery_<cell>.py`, the cell id lower-cased with underscores.
- **Python:** `py -3.12`. AWS through `.tools/aws`. `.tools/terraform.exe` is provisioned by the issuer. A recursive `grep`/`find` in Bash is DENIED by a rail hook and a denial aborts the WHOLE call; use the Read/Grep tools and keep a gated read in its own call. Capture `safe-commit.sh` output to a file, never pipe it to `tail`, never pair it with `$( )`.

---

## THE CELL

**The ruling (@457cf494c6, verbatim where it binds):** *"The direction is (a): the canonical generated view is the intended source of truth, not the served bytes ... BUT REC (a) AS WRITTEN LABELS THE SERVED BYTES 'STALE' BEFORE THE DIFF HAS RUN, AND THAT IS THE ONE THING THE CELL MUST NOT DO ... A NON-EMPTY DIFF DOES NOT MEAN 'SERVED IS STALE.' IT IS EQUALLY CONSISTENT WITH 'CANONICAL IS INCOMPLETE.' ... Deploying canonical over it would then be a silent removal of live configuration, and it would arrive wearing the word 'remediation.'"* *"WHAT IS REFUSED OUTRIGHT: committing the served bytes as source 'for now' while the semantic question waits."* The grounding for the canonical side: `loaders.py`'s own docstring (the firm map *"is derived from data/firm_registry.json -- the ONE firm enumeration"*), the registry under `infra/logic/registry/`, Rule 30.

**THE POPULATION, BY SUBTRACTION FROM A PRINTED DENOMINATOR, NEVER BY RECALL:** re-run IB-rte-4's served-zip census (`the-served-members-declared.result.md` @162b657207 names the 147 members and their classes; `battery_ib_rte_4.py` re-derives it) over every function in the investor-reporting family at its CURRENT served `CodeSha256` (IB-rte-6 redeployed 7 functions @be2fa1dd19 -- the population may have moved), and take every member NOT classed TRACKED-AT-PATH-EQUAL or declared through a verified `staged_from`. Known at the cut: (i) `firm_registry.json` -- `irpt-intake-poller`, `irpt-ycharts-generate` (W4-S34: no source anywhere in `rev-list --objects --all`); (ii) `settings.json` -- `irpt-ycharts-generate` (W4-S35: its embedded `_meta.artifact` claims `intake/settings.json`, a tracked path whose content at EVERY commit is sha256 `c493ea6e...` or `23c649d2...`, never the served `a05bcea4...`); (iii) W1-S26: `irpt-status` `handler.py`, `checkpoint.py`; `irpt-ycharts-generate` `gate.py`, `firm_destination_policy.json` (+ the two above) -- extracted UNCHANGED from the served zips by IB-rte-6's packager for its build and never committed; (iv) the 3 UNRESOLVED of the 147. Print `N of M` members across `F` functions with each member's class; a member the census finds that this list does not name is IN the population and a row.

- (a) THE CANONICAL SOURCE, per member, NAMED BEFORE ANY DIFF: a tracked path at HEAD (cite `path @<commit>` and `blob <hash>`), a builder output (`lib/opal_naming.py` / the registry -- print the call), or ABSENT (no canonical source exists -- that member goes to arm (b) as CANONICAL-ABSENT and is itself the finding; nothing is invented). For code members (W1-S26's `.py` files), the canonical source is the tracked file the served bytes descend from (TRACKED-ELSEWHERE in rte-4's grammar), found by content and by history, never by name alone.
- (b) ARM 1 -- THE DIFF, PRINTED WITH DENOMINATORS, NO LABEL: served bytes vs canonical, key by key for json (`present-only-in-served`, `present-only-in-canonical`, `differing-value`, each `n of K`), line by line for code; both directions; `DELTA` per member is the sum. No word like stale, rot or drift appears in the output before this arm reports.
- (c) ARM 2 -- THE BRANCH, STATED IN ADVANCE: **DELTA = 0** -> declaration only: `staged_from` pins the canonical source's blob in `lambda-source-map.json` (`build-and-upload.sh`'s pinned-blob mechanism @162b657207), the function rebuilds from a CLEAN checkout equal to the served zip member-for-member, no hold, the member's rows close on the declaration. **DELTA != 0 (or CANONICAL-ABSENT)** -> the difference IS the finding: each differing key named with its direction; this order writes the NEVER-WIDEN PACKET for that member (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtf-1.md`: the printed diff as the blast radius, rollback per key = the served bytes' `blob <hash>`, and the WRITERS of each differing key censused -- `N` printed -- before any half can sign), files ONE row per member (`IRPT_BCKEND-W4-S<k>`, ARMED, disarm_owner `2.0.0_SA_COO~B`), and DOES NOT DEPLOY and DOES NOT COMMIT SERVED BYTES AS SOURCE. The deploy of a DELTA != 0 member is a served-behaviour change on a live function and is a LATER hand-off under both halves and a ledger entry; this order's job on that branch is finished when the packet and the row exist.
- (d) ARM 3 -- for every DELTA = 0 member, `staged_from` declares the chosen source and the clean-checkout build equals the served zip member-for-member (`k of k`, sha256 per member); the mutant (the declaration removed in scratch) fails the build; IB-rte-4's census re-run reads every DELTA = 0 member as DECLARED-AND-VERIFIED (`k of N`) and every DELTA != 0 / ABSENT member as PACKETED (`j of N`), `k + j = N`.

---

## DELIVERABLE

the `lambda-source-map.json` declarations; the packet (if any member branches to DELTA != 0); `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/battery_ib_rtf_1.py`, `IB-rtf-1_R58-AC1_battery_output.txt` (the population table, every diff with denominators), `the-no-source-members-measured.result.md`; the proof instance.

---

## BOUNDS

- NO served bytes are committed as source, on ANY branch; NO deploy by this order (a DELTA != 0 member is packeted, never shipped); the ONLY code paths touched are `infra/aws/lambda/ci/` (the source map, and the builder only if a form it cannot express is needed -- minimal, cited); `BAU_PARITY_SKIP` never set in the graded run; the served functions are not redeployed. A label applied to either side before arm (b) reports is a defect the issuer greps for at the drain.
- **THE FORWARD-LOOKING-CRITERION BAR (round-3 analysis s.4, ADOPTED; R-68's shape):** no criterion on this face certifies what a future event WILL find or load; every claim about a run or a served artifact is bound to that artifact's CONTENT HASH (`VersionId`/`ETag`/`sha256`/`CodeSha256`/`git hash-object`) READ AT THE EVENT -- a prediction made before the event is not evidence and a battery that prints one is refused at the drain.
- **S56 (ARMED, the CVO's): EVERY line citation in this order's JUDGMENT RECORD and result carries a vintage -- `path:line @ <commit-ish>` -- a bare `:NNN` is a defect the issuer greps for at the drain (`0 of N` bare citations is the bar).** CLAUDE.md Rule 22: a citation without a vintage is not a citation.
- **S73 (the `comp-iam roles` snapshot with no vintage) is an ESTATE-INSTRUMENT defect routed elsewhere and does NOT ride this order:** a live-plane IAM read here uses `comp-iam live` or `.tools/aws iam get-role`, never `comp-iam roles`.
- **R-40 (standing bar, `1.0.0_SA_CTO` @233f5fd5e4):** every criterion whose subject is a RUN or a PRODUCED ARTIFACT records that artifact's CONTENT HASH (`git hash-object`, `sha256sum`, or the service's own digest such as `ETag`/`CodeSha256`) beside its run id in the instance, and is graded against the hash; a label, a path or a timestamp ordering is not an identity.
- **Surprises:** ONE row per premise that does not hold, path that is not where this face says, result the invocation does not produce, or capability you lack -- at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W4-S<k>` with k continuing that coordinate's numbering (read the file's highest `W4-S<k>` first; the file now holds SEVERAL fenced json blocks -- append your object INSIDE THE FIRST fence's array at its end, LF line endings, UTF-8 written explicitly, no json fence marker inside any row's text, `surfaced_at` a full ISO timestamp, omit `disarm_owner` on an INERT row and name a SEAT SERIAL, never a cell, when ARMED (R-42)); then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.
- **THE READER-CENSUS BAR (round-5 analysis s.1, the mirror of the never-widen writer census):** FLIPPING A SHARED FLAG OR FIELD NEEDS ITS READER CENSUS -- N readers, N rules read, N printed -- before the flip is called safe; a write asks who else SETS this, a flip asks who else BELIEVES this. NON-APPLICATION: a value with exactly one reader, which the same census proves.
- **BLOB PINS ARE WRITTEN `blob <hash>` (round-5 analysis s.4):** `@<hash>` means commit-ish in this estate; a blob pinned as `@<hash>` reads like a missing file at the grader. No `memory/` path is cited on this face (S78: a fresh worktree cannot resolve one); every rule this face relies on is stated inline.

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

<criterion id="R58-AC1" cell_refs="IB-rtf-1"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/battery_ib_rtf_1.py</invocation><expect>IBR58-NO-SOURCE-MEMBERS-MEASURED-AND-BRANCHED</expect></criterion>
**`R58-AC1` -- PASSES BY OUTPUT:** the population `N of M` printed by subtraction from the re-run census; (a) every member's canonical source NAMED or ABSENT (`N of N`); (b) every member's diff printed both directions with denominators and NO label before it; (c) every member either DECLARED-AND-VERIFIED (`k`) or PACKETED-AND-ROWED (`j`), `k + j = N`, with the packet's writer census `W` printed for each packeted member; (d) the mutant fails and the clean build succeeds for the `k`. A truthful branch outcome on every member is the PASS of this MEASURE cell; the token prints only when every member has reached one of the two terminal states; the battery re-derives every count from the real zips and the real object graph each run.

<criterion id="R58-AC2" cell_refs="IB-rtf-1" judgment="true"/>
**`R58-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: per DELTA != 0 member, whether the evidence reads "served is stale" or "canonical is incomplete" and what would discriminate; whether `firm_registry.json` should be a BUILDER OUTPUT from `infra/logic/registry/` (Rule 30) rather than a tracked file; what W4-S35's `_meta.artifact` claim means for the family's provenance stamps; and whether `_authz/` should be a shared package (IB-rte-4's carried question). No verdict. Every line citation carries `@<commit-ish>`; a blob pin is written `blob <hash>`.

<expected_criteria>R58-AC1, R58-AC2</expected_criteria>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtf-1.the-no-source-members-measured-then-branched.md
infra/aws/lambda/ci/
infra/aws/lambda/investor-reporting/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.6, cell `IB-rtf-1` (s.R6 -- the round-6 rectangle, edges, seating and bounds).
<owned_cells>IB-rtf-1</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant changes; no deploy by this order.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `.tools/**`, `data/**` and `lib/**` path resolves to its own lane at HEAD and is admitted ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: R58-AC1, R58-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/IRPT_BCKEND.TO-IB-rtf-1.the-no-source-members-measured-then-branched.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and -- R-40 -- the content hash of every produced or served artifact the row grades, EACH PINNED TO THE COMMIT THAT CARRIED IT (commit the battery, its output and the result BEFORE the instance; `PENDING-THIS-COMMIT` is a ONE-SHOT sentinel -- a later re-commit of the instance re-pins every such row to the commit that carried the artifact); a blob pin is written `blob <hash>`; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/IRPT_BCKEND.TO-IB-rtf-1.the-no-source-members-measured-then-branched.proof_of_spec.json --governing-order org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtf-1.the-no-source-members-measured-then-branched.md` BEFORE the complete flip; rc 0 AND R58-AC1 PASS-by-output, then flip this order's `<status>` to `complete` and commit instance and flip together. A FAIL row leaves the order open and is your final report on it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
