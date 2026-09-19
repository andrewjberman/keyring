# TO IRPT_BCKEND.TO-IB-rtf-6 -- THE MANIFEST RE-PINNED AFTER THE SHARED-SURFACE DRAINS: IB-rtf-1 pinned the shared `_authz/enforce.py`, `_authz/served.py`, `_authz/loaders.py`, `_ids/ids.py` and the seam file for six functions to their blobs at `c28c728a30`; IB-rtf-2 then changed `enforce.py` (the ordering inversion) and `served.py` (the disclosure field) and deployed all seven functions through `rte6_package_deploy.py`, which resolves shared roots directly and bypasses the pins -- so the DECLARED source and the SERVED bytes now disagree for those members (row W4-S41's class, widened by the drain), and a `build-and-upload.sh` run from HEAD would stage the PRE-inversion bytes and silently regress the L4 ruling by build. Re-pin every stale declaration to the blob the served bytes match (HEAD's, for the shared files), prove the regression on the mutant and its absence on the real manifest, deploy nothing

<to_id>IRPT_BCKEND.TO-IB-rtf-6</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~4</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-19</issued_date>
<status>pending -- HANDED by 2.0.0_SA_COO~B at 2026-09-19T06:4xZ to slot ~4 (cold start; IB-rtf-1's worker is terminal and reported) mid-round on row W4-S41 (IB-rtf-1 @949dc88099) and the issuer's own read after IB-rtf-2's drain @4e6c6738c3: HEAD's `_authz/enforce.py` is `blob 79c9d9dee1` and `_authz/served.py` `blob fd8b189e5c`, while the manifest's `staged_from` entries for those two files on six functions pin `c28c728a30`'s blobs. IB-rtf-3 does not depend on this order (its arms are live requests); IB-rtf-5 does not either. The next BUILD does.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 6 (the CTO's round-5 analysis @81472c3a47, msg 98115) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.14 @b8e98d5a4d (no addendum at round 5) | **Round-5 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND5_ANALYSIS.md` @81472c3a47 | **L4 rulings carried:** no-source members @457cf494c6; partial projection @61627f39f9; registry deadlock @9eeb9a70a8 + @80dada6d8d | **Rulings carried:** R-40, R-42, R-44, R-45 @57bc083d45; the forward-looking-criterion bar; Rule 30; the reader-census bar and the blob-pin notation (round-5 analysis s.1, s.4) | **Decomp cell:** `IB-rtf-6` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.6, s.R6.5) | **outcome_ref:** FWD-1, FWD-2, FWD-5, FWD-7 (the served functions' provenance, and the served path's behaviour surviving the next build)

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~4`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~4;`.
- **Worktree:** `/c/tmp/wk-irpt-6-4b` on branch `wk-irpt_bckend-6-4b`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree; make a path absolute by prefixing `/c/tmp/wk-irpt-6-4b/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~4 <0.9.0_WK_IRPT_BCKEND~4@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/` (granted by the tree convention). Batteries are named `battery_<cell>.py`, the cell id lower-cased with underscores.
- **Python:** `py -3.12`. AWS through `.tools/aws`. `.tools/terraform.exe` is provisioned by the issuer. A recursive `grep`/`find` in Bash is DENIED by a rail hook and a denial aborts the WHOLE call; use the Read/Grep tools and keep a gated read in its own call. Capture `safe-commit.sh` output to a file, never pipe it to `tail`, never pair it with `$( )`.

---

## THE CELL

**The state at the cut, measured by the issuer:** `git rev-parse HEAD:infra/aws/lambda/investor-reporting/_authz/enforce.py` = `79c9d9dee1`, `.../served.py` = `fd8b189e5c` (post-IB-rtf-2). `infra/aws/lambda/ci/lambda-source-map.json` carries 14 `files[]` entries naming `enforce.py`/`served.py` across 7 functions; IB-rtf-1 declared them with `staged_from` pinned to `c28c728a30` -- the commit BEFORE IB-rtf-2's first pass drained (@b6f49d9401) -- so the pinned blobs are the PRE-inversion bytes. IB-rtf-2's deploy (7 of 7, `CodeSha256 == built`) was packaged by `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/rte6_package_deploy.py` (its `SHARED_ROOTS` resolver), which reads the worktree's shared files directly, so the SERVED bytes are the post-inversion ones. **Two mechanisms package the same functions and only one of them reads the manifest.** IB-rtf-1's instrument (`battery_ib_rtf_1.py` @949dc88099) already classes every served member against the manifest and the object graph at the live `Code.Location`; it is the instrument here too.

- (a) THE CENSUS, re-run at the LIVE `Code.Location` bytes for all 9 investor-reporting functions with IB-rtf-1's instrument (cite it; never the build-artifact bucket -- W4-S37's and IB-rtf-1's own trap): per declared member, the DECLARED blob (the `staged_from` pin resolved), the SERVED sha256, and HEAD's blob for the same path; class each as PIN-MATCHES-SERVED / PIN-STALE-HEAD-MATCHES-SERVED / PIN-STALE-SERVED-DIVERGED-FROM-HEAD / PACKETED (IB-rtf-1's 6). Print `n stale of N` with the denominator. The expected members are the 14 `enforce.py`/`served.py` entries; the census decides, not the expectation.
- (b) THE RE-PIN: every PIN-STALE-HEAD-MATCHES-SERVED member is re-pinned to HEAD's blob (the pinned-blob mechanism @162b657207 -- `path@<commit>` resolved by content; print old pin -> new pin per member). A PIN-STALE-SERVED-DIVERGED-FROM-HEAD member (the `irpt-holdings` `holdings/enforce.py` class, W1-S29 -- a local diverged copy the packager's `source_dir`-first resolution ships instead of the shared file) is NOT re-pinned to the served bytes and NOT to HEAD's shared file (either would assert a source that is not what runs): it is classed, rowed (`IRPT_BCKEND-W4-S<k>`, disarm_owner `1.0.0_SA_CTO`, citing W1-S29) and left for the CTO's ruling. PACKETED members stay packeted. No served bytes committed as source; no third copy.
- (c) THE CONTROL, BOTH SIGNS: the MUTANT -- the manifest with the pins reverted to `c28c728a30` (scratch, `BAU_SOURCE_MAP_OVERRIDE`, the real file untouched) -- built from a CLEAN checkout produces an `enforce.py` whose sha256 != the served one and whose bytes carry the OLD refusal order (the `:276` comment and `:283` check the CVO read at L9 -- grep the built member for the pre-inversion text, `1 of 1`): the regression DEMONSTRATED. The REAL re-pinned manifest built from a clean checkout equals the served zips member-for-member for every re-pinned member (`k of k`, sha256 per member) -- so the next `build-and-upload.sh` from HEAD reproduces what is served today. `BAU_PARITY_SKIP` never set.
- (d) NO DEPLOY: served == built for the re-pinned members means `0` functions need a deploy; if a function's clean build differs from its served zip on a member this order did not re-pin, that member is a row, not a deploy.

---

## DELIVERABLE

the re-pinned `lambda-source-map.json`; `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/battery_ib_rtf_6.py`, `IB-rtf-6_R63-AC1_battery_output.txt` (the census table, the pin changes, the mutant's pre-inversion evidence, the clean-build equality), `the-manifest-re-pinned.result.md`; the proof instance.

---

## BOUNDS

- ONLY `infra/aws/lambda/ci/lambda-source-map.json` changes (the builder only if a pin form it cannot express is needed -- minimal, cited); NO deploy; NO served bytes as source; NO third copy; the diverged `holdings/enforce.py` is rowed, never edited, never pinned; `BAU_PARITY_SKIP` never set in the graded run; the packager script is read, never edited (its class is R63-AC2's).
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

<criterion id="R63-AC1" cell_refs="IB-rtf-6"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/battery_ib_rtf_6.py</invocation><expect>IBR63-MANIFEST-RE-PINNED-TO-THE-SERVED-BYTES</expect></criterion>
**`R63-AC1` -- PASSES BY OUTPUT:** (a) the census `n stale of N` at the live bytes, every member classed; (b) every PIN-STALE-HEAD-MATCHES-SERVED member re-pinned (`m of m`, old -> new printed), every diverged member rowed not pinned (`d of d`); (c) the mutant build's `enforce.py` carries the pre-inversion text (`1 of 1`) and differs from served, the real build equals served member-for-member `k of k`; (d) `0` deploys. The token prints only when every arm holds; the battery re-derives every count from the real zips, the real object graph and the real live bytes each run.

<criterion id="R63-AC2" cell_refs="IB-rtf-6" judgment="true"/>
**`R63-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: whether two packaging mechanisms (`build-and-upload.sh`'s declarative `staged_from` and `rte6_package_deploy.py`'s direct resolver) can coexist without this class recurring every round, and which one should be the ONLY one (a shape question for L4, with the W4-S39/S40/S41 and W1-S29 evidence); whether a manifest pin should be a CONTENT hash rather than a commit (a commit pin goes stale on every drain of a shared file; a content pin fails loudly); and what `irpt-holdings`'s diverged `enforce.py` means for FWD-5 today (which refusal order it serves). No verdict. Every line citation carries `@<commit-ish>`; a blob pin is written `blob <hash>`.

<expected_criteria>R63-AC1, R63-AC2</expected_criteria>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtf-6.the-manifest-re-pinned-after-the-shared-surface-drains.md
infra/aws/lambda/ci/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.6, cell `IB-rtf-6` (s.R6.5 -- the mid-round additions on rows W4-S41 / W1-S29 and the Andrew-direct ~06:3xZ).
<owned_cells>IB-rtf-6</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant changes; no deploy.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `.tools/**`, `data/**` and `lib/**` path resolves to its own lane at HEAD and is admitted ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: R63-AC1, R63-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/IRPT_BCKEND.TO-IB-rtf-6.the-manifest-re-pinned-after-the-shared-surface-drains.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and -- R-40 -- the content hash of every produced or served artifact the row grades, EACH PINNED TO THE COMMIT THAT CARRIED IT (commit the battery, its output and the result BEFORE the instance; `PENDING-THIS-COMMIT` is a ONE-SHOT sentinel -- a later re-commit of the instance re-pins every such row); a blob pin is written `blob <hash>`; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/IRPT_BCKEND.TO-IB-rtf-6.the-manifest-re-pinned-after-the-shared-surface-drains.proof_of_spec.json --governing-order org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtf-6.the-manifest-re-pinned-after-the-shared-surface-drains.md` BEFORE the complete flip; rc 0 AND R63-AC1 PASS-by-output, then flip this order's `<status>` to `complete` and commit instance and flip together. A FAIL row leaves the order open and is your final report on it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE (a worker) or ONE broker message to `2.0.0_SA_COO~B` (a Tier-2 seat), once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
