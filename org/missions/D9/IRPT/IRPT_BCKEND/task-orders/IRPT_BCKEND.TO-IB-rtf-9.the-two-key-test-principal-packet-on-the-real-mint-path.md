# TO IRPT_BCKEND.TO-IB-rtf-9 -- THE TWO-KEY TEST-PRINCIPAL PACKET ON THE REAL MINT PATH: IB-rtf-3 STOPPED before any write because the signed packet's K1 (an `opal-users-v2` row carrying `advisorKey/advisorId = abby_horton`) is NEVER READ by the deployed auth-handler -- the token's advisor claim comes ONLY from `opal-partner-49financial` keyed by e-mail (`lib/partner/index.ts:21-37`, `db.ts:29-54`, `auth.ts:202-216`, `jwt.ts:179-185` @4ee8426c72; `getUser()` maps no advisor field, `db.ts:138-167`), so K1 + K2 would mint a 49financial session with NO advisor claim, UNKNOWN on the scoped routes (row S86, BLOCKING). The CTO half's rule (s.1 @482b2c627e): a key the act discovers it needs is a STOP and a NEW PACKET, never a widening. This order WRITES that packet -- two keys, the partner-table binding costed with its own writer and reader census and a verified `DeleteItem` rollback -- and creates NOTHING; both halves are re-signed against its blob before IB-rtf-3 is re-handed

<to_id>IRPT_BCKEND.TO-IB-rtf-9</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~V</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-19</issued_date>
<status>pending -- HANDED by 2.0.0_SA_COO~B at 2026-09-19T08:5xZ to 0.7.0_AE_CloudOps~V (the seat that found S86 and already holds the mint-path reads) mid-round on IB-rtf-3's STOP @f60b3f0942 (row S86, BLOCKING/ARMED, disarm_owner 2.0.0_SA_COO~B: "the disarm is a re-cut packet naming the partner-table key with both halves re-signed against the new blob"). Andrew's 17:3xZ approval (@af794c77e3) covers a BOUNDED test principal under both halves, deleted at round close -- the partner-table binding is the part of that principal the first packet mis-located, not a new act; the halves cover it once re-signed. This order is DECLARE-ONLY (the IB-rte-1 shape): no key is created here. IB-rtf-3 stays open and is re-handed against this packet's blob once both halves are at HEAD.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 6 (the CTO's round-5 analysis @81472c3a47, msg 98115) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.14 @b8e98d5a4d (no addendum at round 5) | **Round-5 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND5_ANALYSIS.md` @81472c3a47 | **L4 rulings carried:** no-source members @457cf494c6; partial projection @61627f39f9; registry deadlock @9eeb9a70a8 + @80dada6d8d | **Rulings carried:** R-40, R-42, R-44, R-45 @57bc083d45; the forward-looking-criterion bar; Rule 30; the reader-census bar and the blob-pin notation (round-5 analysis s.1, s.4) | **Decomp cell:** `IB-rtf-9` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.6, s.R6.7) | **outcome_ref:** FWD-1, FWD-2, FWD-5, FWD-11

---

## IDENTITY AND WORKTREE

- **Serial:** `0.7.0_AE_CloudOps~V` (a Tier-2 AE lane, seated by the issuer's /mstr-spawn; the CTO half names the operator class). Every Bash call begins `export OPAL_AGENT_SERIAL=0.7.0_AE_CloudOps~V;`.
- **Worktree:** `/c/tmp/wk-irpt-6-ae1` on branch `wk-irpt_bckend-6-ae1`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree; make a path absolute by prefixing `/c/tmp/wk-irpt-6-ae1/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.7.0_AE_CloudOps~V <0.7.0_AE_CloudOps~V@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~V/` (granted by the tree convention). Batteries are named `battery_<cell>.py`, the cell id lower-cased with underscores.
- **Python:** `py -3.12`. AWS through `.tools/aws`. `.tools/terraform.exe` is provisioned by the issuer. A recursive `grep`/`find` in Bash is DENIED by a rail hook and a denial aborts the WHOLE call; use the Read/Grep tools and keep a gated read in its own call. Capture `safe-commit.sh` output to a file, never pipe it to `tail`, never pair it with `$( )`.

---

## THE CELL

**What IB-rtf-3 measured (its result @700bc86ec2, its instance @f60b3f0942, VALID):** the deployed `opalinvest-auth-handler` zip (`CodeSha256` `h1tnQVRpRA52eWyfAia6CfBsJmn6xKwHa8IUC0zBSsQ=`, equal to the live one) sources the token's `advisorKey`/`advisorId` ONLY from `opal-partner-${firm}` via `GetItem` on `Key {email}`; `opal-partner-49financial` is keyed HASH=email and `0 of 11` rows carry `advisorKey = abby_horton` -- no login binds `abby_horton` today; a 49financial login with no partner row is UNKNOWN on the scoped routes (`_scope/resolve.py:193-196`) and admitted by firmId alone on the older portal routes (`lib/partner/index.ts:39-47`) -- an EXPOSURE the CTO holds, not this order's. The live ownership map (VersionId `nR.FkCE1frsI9R5zRp2wJWB7vyMZ04NK` at 08:29Z) carries `abby_horton` PRESENT with 33 accounts / 18 relationships (the packet's 43 / 18 moved: W1-S30).

- (a) THE KEYS, RE-DECLARED FROM THE MINT PATH, NOT FROM THE FIRST PACKET: **K1** the `opal-users-v2` item (as before: `PK = USER#usr_irptrte_<epoch>`, `firmId = 49financial`, a `.test`-TLD e-mail, no phone, no MFA -- keep only the fields the deployed `getUser()` reads, cite `db.ts:138-167`; drop `advisorKey/advisorId` from it since nothing reads them there, say so); **K1b** the `opal-partner-49financial` item for the SAME test e-mail carrying `advisorKey = abby_horton` (and whatever other attributes `lib/partner/index.ts:21-37` requires for the claim to be minted -- the exact attribute set cited line by line, no extra attribute); **K2** the ephemeral session (access token TTL `jwt.ts:17`, the refresh token dying with the row `jwt.ts:220-224`). Each key's exact shape printed; each key's rollback = `DeleteItem` on its own PK, VERIFIED by a consistent-read `GetItem` returning no `Item`; K1b's deletion ordered FIRST (the binding goes before the login).
- (b) THE WRITER AND READER CENSUS of `opal-partner-49financial` (the property the first packet never counted): every principal with `dynamodb:PutItem`/`UpdateItem`/`DeleteItem` on that table (`n of N` roles/users, `comp-iam live` or `.tools/aws iam` -- never `comp-iam roles`), and every READER of its rows (the auth-handler's mint path, the older portal routes' `canAccessFirm`, any other consumer -- Grep, unscoped, `r of R` cited `file:line @commit`), each with the SENSE it reads (identity claim vs firm membership). A property with N writers needs N rules read, N printed.
- (c) THE BLAST RADIUS, BOTH BRANCHES, PER KEY: with K1b present a login on the test e-mail mints a session carrying `advisorKey = abby_horton` -- EXACTLY `abby_horton`'s existing 49financial entitlement (the partial: `k` of 33 today, disclosed), no new grant; on the older portal routes the same session is admitted by firmId (the exposure the CTO holds -- named as in-radius, not widened); with K1b absent (STOP / rollback) the login is UNKNOWN on the scoped routes and the older routes' admission is the pre-existing exposure, not this act's. Every branch the first packet stated (`NEVER_WIDEN_SIGNOFF_PACKET_IB-rte-1.md` @f08295cc8f) is re-derived, not copied; what changed is the KEY LIST and the WRITERS.
- (d) THE EXERCISE PLAN unchanged in substance from IB-rtf-3's face -- the four outcomes by real signed requests on the disclosed-partial path, the negative controls, the deletion as the last arm (K1b first, then K1, each verified by a failing read), the interval closed -- restated against the two keys so the re-handed IB-rtf-3 reads ONE packet, not two.
- (e) NOTHING CREATED. The packet `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~V/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtf-9.md` committed; its `blob <hash>` printed; the halves are the issuer's and the CTO's to sign against that blob -- this order does not wait for them.

---

## DELIVERABLE

`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~V/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtf-9.md`; `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~V/battery_ib_rtf_9.py`, `IB-rtf-9_R66-AC1_battery_output.txt` (the mint-path citations re-derived at HEAD, the writer/reader census tables, the key shapes, `0` writes measured on both tables before and after), `the-two-key-packet.result.md`; the proof instance.

---

## BOUNDS

- DECLARE ONLY: `0` items written to `opal-users-v2` or `opal-partner-49financial` (the battery measures both tables' item counts / the test PK's absence before and after); no session minted; no vendor call; no credential VALUE in any artifact; the keys named EXACTLY as the deployed mint path reads them (a field nothing reads is not a key); the older portal routes' firmId admission is NAMED as in-radius and NOT widened, narrowed or fixed here.
- **THE FORWARD-LOOKING-CRITERION BAR (round-3 analysis s.4, ADOPTED; R-68's shape):** no criterion on this face certifies what a future event WILL find or load; every claim about a run or a served artifact is bound to that artifact's CONTENT HASH (`VersionId`/`ETag`/`sha256`/`CodeSha256`/`git hash-object`) READ AT THE EVENT -- a prediction made before the event is not evidence and a battery that prints one is refused at the drain.
- **S56 (ARMED, the CVO's): EVERY line citation in this order's JUDGMENT RECORD and result carries a vintage -- `path:line @ <commit-ish>` -- a bare `:NNN` is a defect the issuer greps for at the drain (`0 of N` bare citations is the bar).** CLAUDE.md Rule 22: a citation without a vintage is not a citation.
- **S73 (the `comp-iam roles` snapshot with no vintage) is an ESTATE-INSTRUMENT defect routed elsewhere and does NOT ride this order:** a live-plane IAM read here uses `comp-iam live` or `.tools/aws iam get-role`, never `comp-iam roles`.
- **R-40 (standing bar, `1.0.0_SA_CTO` @233f5fd5e4):** every criterion whose subject is a RUN or a PRODUCED ARTIFACT records that artifact's CONTENT HASH (`git hash-object`, `sha256sum`, or the service's own digest such as `ETag`/`CodeSha256`) beside its run id in the instance, and is graded against the hash; a label, a path or a timestamp ordering is not an identity.
- **Surprises:** ONE row per premise that does not hold, path that is not where this face says, result the invocation does not produce, or capability you lack -- at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-S<k>` (the SEAT form -- the `A-S<k>` form earlier faces named is refused by the row gate's `ID_RE` and the schema, row S83) with k continuing above the file's highest `S<k>` at your worktree's HEAD (read it first; the file holds SEVERAL fenced json blocks -- append your object INSIDE THE FIRST fence's array at its end, the file's PREVAILING line endings (CRLF today, W4-S44), UTF-8 written explicitly, no json fence marker inside any row's text, `surfaced_at` a full ISO timestamp, omit `disarm_owner` on an INERT row and name a SEAT SERIAL, never a cell, when ARMED (R-42)); then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.
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

<criterion id="R66-AC1" cell_refs="IB-rtf-9"><invocation>timeout 900 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~V/battery_ib_rtf_9.py</invocation><expect>IBR66-TWO-KEY-PACKET-DECLARED-NOTHING-CREATED</expect></criterion>
**`R66-AC1` -- PASSES BY OUTPUT:** (a) the three keys' exact shapes with every attribute cited to the deployed reader (`m of m` attributes cited); (b) writers `n of N` and readers `r of R` of `opal-partner-49financial` printed with sense; (c) both branches per key with rollback verified-by-failing-read stated; (d) the exercise plan restated on the two keys; (e) the packet committed with its `blob <hash>` printed and `0` writes measured on both tables. The token prints only when every arm holds; the battery re-derives every count each run.

<criterion id="R66-AC2" cell_refs="IB-rtf-9" judgment="true"/>
**`R66-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: whether the advisor identity living in a partner table keyed by e-mail (not on the user row) is the intended design or an accident the IRPT scoped routes now depend on; the exposure IB-rtf-3 named (a firm login with no book admitted by firmId on the older routes -- an UNSCOPED census of whether any such login exists is the CTO's, name what it would take); and whether FWD-11's global viewer needs a partner row in EVERY firm's table or a different mint path. No verdict. Every line citation carries `@<commit-ish>`.

<expected_criteria>R66-AC1, R66-AC2</expected_criteria>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtf-9.the-two-key-test-principal-packet-on-the-real-mint-path.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.6, cell `IB-rtf-9` (s.R6.7 -- the mid-round addition on row S86).
<owned_cells>IB-rtf-9</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired.
comp-iam: RUN by this order as arm (b) -- the writer/reader census of opal-partner-49financial is the cell; DESIRED = the two-key packet; APPLIED = nothing (declare only); the discriminator is IB-rtf-3's re-hand. BLIND SPOT: the auth-handler's own signup path is a writer IAM cannot see (named by the first packet, re-checked here).
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). A path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: R66-AC1, R66-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~V/IRPT_BCKEND.TO-IB-rtf-9.the-two-key-test-principal-packet-on-the-real-mint-path.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and -- R-40 -- the content hash of every produced artifact the row grades, EACH PINNED TO THE COMMIT THAT CARRIED IT (commit the battery, its output and the result BEFORE the instance; `PENDING-THIS-COMMIT` is a ONE-SHOT sentinel); a blob pin is written `blob <hash>`; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~V/IRPT_BCKEND.TO-IB-rtf-9.the-two-key-test-principal-packet-on-the-real-mint-path.proof_of_spec.json --governing-order org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtf-9.the-two-key-test-principal-packet-on-the-real-mint-path.md` BEFORE the complete flip; rc 0 AND R66-AC1 PASS-by-output, then flip this order's `<status>` to `complete` and commit instance and flip together. A FAIL row leaves the order open and is your final report on it.
</proof_of_spec>

**REPORT:** ONE broker message to `2.0.0_SA_COO~B`, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, the packet's `blob <hash>`, every row id filed with its class, anything you could not do and why).
