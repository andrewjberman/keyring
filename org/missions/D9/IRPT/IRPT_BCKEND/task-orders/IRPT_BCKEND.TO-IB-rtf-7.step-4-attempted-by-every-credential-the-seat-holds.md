# TO IRPT_BCKEND.TO-IB-rtf-7 -- STEP 4 ATTEMPTED BY EVERY CREDENTIAL THE SEAT HOLDS: Andrew-direct 2026-09-19 ~06:3xZ (record `org/tier1_exec/2.0.0_SA_COO~B/deliverables/ANDREW_DIRECT_20260919_063xZ_STEP4_BUCKET_POLICY_AE_ATTEMPT_THEN_PROCEED.md`), verbatim *"i cant get to the console right now, i am remote. have an AE deal with it. if they cant for whateve rreason, proceed and note it for later."* -- the removal of the bucket ACCESS POLICY (never the bucket) on `opal-data-inflection` and `opal-data-cottonwood`, tried with every identity this seat holds, each attempt's identity and response recorded verbatim; a success is the act and unblocks IB-rtf-5; AccessDenied on every identity is the truthful result, the round proceeds, and the item is carried for Andrew's next console presence

<to_id>IRPT_BCKEND.TO-IB-rtf-7</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~V</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-19</issued_date>
<status>superseded -- CLOSED by 2.0.0_SA_COO~M as issuer on the IRPT return at 2026-09-24T18:2xZ (brief org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_CLOSER_TO_CANONICAL_RETURN_BRIEF_20260924.md s.3 C4; 1.0.0_SA_CTO msg 100783). The need is met another way: round 18 closed on ledger/ROUND_ANALYSIS.round18.md and the closer's live journeys under the ~P/~M/~Y goal records carry what remains. Nothing was applied under this flip; IB-rtf-3 (the test principal Andrew approved on 09-18) stays live. Was: pending -- HANDED by 2.0.0_SA_COO~B at 2026-09-19T06:4xZ to the AE lane 0.7.0_AE_CloudOps~V (the seat also holding IB-rtf-3; this order runs FIRST, it is small). Andrew's word is the authority and its scope is the whole grant: attempt, record, proceed. NOT authorized by it: starting host i-02448edb624a7a7cf, any IAM change, adding root to any exemption list, any route around the fence. Expected result (measured 05:5xZ by the issuer): AccessDenied 2 of 2 under the applying identity -- a bucket policy denying s3:* to every principal binds every IAM identity; only the bucket owner's ROOT is exempt, by construction. ISSUER-CORRECTION (round 8 IB-rth-3, ruling 98990/98993): LEFT NON-TERMINAL, word unchanged -- R64-AC1's own status_reason states VERBATIM "IB-rtf-5 stays staged and the order stays open" (the 2 of 2 AccessDenied is a real measurement, but the order's own text settles this: it is not done); no bound admits `complete` on a disclosed FAIL and no later round's decomp cell names IB-rtf-7 in a `supersedes` column (rounds 6-8 read, plus a project-wide text search) -- `superseded` is refused too.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 6 (the CTO's round-5 analysis @81472c3a47, msg 98115) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.14 @b8e98d5a4d (no addendum at round 5) | **Round-5 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND5_ANALYSIS.md` @81472c3a47 | **L4 rulings carried:** no-source members @457cf494c6; partial projection @61627f39f9; registry deadlock @9eeb9a70a8 + @80dada6d8d | **Rulings carried:** R-40, R-42, R-44, R-45 @57bc083d45; the forward-looking-criterion bar; Rule 30; the reader-census bar and the blob-pin notation (round-5 analysis s.1, s.4) | **Decomp cell:** `IB-rtf-7` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.6, s.R6.5) | **outcome_ref:** FWD-1, FWD-7, FWD-10 (the firm-bound destination's gate) | **Andrew-direct:** 2026-09-19 ~06:3xZ (record above)

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

**What the buckets carry today (rows W3-S43/S45):** a per-firm Deny fence applied 2026-09-18 with an EMPTY exemption list -- `Effect: Deny, Principal: *, Action: s3:*` on the bucket and its objects, `ArnNotLike` = the firm's role pattern only. Every IAM identity we hold reads `AccessDenied` on `get-bucket-policy`, `get-bucket-versioning`, `head-bucket` and `delete-bucket-policy`. The registry rows that would admit three operator identities landed @845343f925, but they are not in the LIVE policy until IB-rtf-5 re-applies -- and rtf-5 cannot apply while the live policy denies the applying identity. Only the bucket owner's account ROOT can remove a policy that denies it. **This order tries every identity the seat holds anyway, because Andrew asked and because "every identity we hold" was measured on ONE profile.**

- (a) THE IDENTITIES, ENUMERATED: `aws configure list-profiles` (through `.tools/aws`), the ambient `AWS_PROFILE`/`AWS_ACCESS_KEY_ID` presence (presence only -- NEVER a value in any artifact), and any role this seat can assume WITHOUT a new grant (`sts get-caller-identity` per profile; a role assumption that needs a policy change is out of scope). Print `N` identities with their ARNs. Zero credentials beyond the default is a legitimate `N = 1`.
- (b) THE ATTEMPT, per identity, per bucket: `.tools/aws s3api delete-bucket-policy --bucket <b>` -- the full response verbatim (`AccessDenied` text, or an empty success). `2N` attempts printed. On ANY success: immediately `get-bucket-policy` on that bucket -> `NoSuchBucketPolicy` (the discriminator), then the same on the other bucket; the act is a change to a live fence, so a change-management ledger entry is OPENED before the first attempt and CLOSED after the last (`python .tools/deploy_ledger.py open/close`, sentinel committed before). On AccessDenied everywhere: the ledger entry closes as NO-CHANGE with the `2N of 2N` denials recorded.
- (c) THE RESULT, TRUTHFULLY: success `2 of 2` -> step 4 DONE (IB-rtf-5 becomes handable that tick; the issuer measures it); anything less -> R64-AC1 FAIL by output with every attempt's identity + response printed, and the carry line written in the result verbatim: *"step 4 -- Andrew at the console when next present; N identities tried, 2N of 2N denied"*. No identity is created, no role is assumed beyond what the seat already holds, nothing else on either bucket is attempted.

---

## DELIVERABLE

the ledger entry; `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~V/battery_ib_rtf_7.py`, `IB-rtf-7_R64-AC1_battery_output.txt` (every identity ARN and every response), `step-4-attempted.result.md`; the proof instance.

---

## BOUNDS

- EXACTLY `delete-bucket-policy` on the two named buckets with identities the seat ALREADY holds; no object read or write; no `put-bucket-policy`; no IAM change; no role assumption needing a grant; no host start; no credential VALUE in any artifact (ARNs and profile names only). A bucket name outside the two is a STOP.
- **THE FORWARD-LOOKING-CRITERION BAR (round-3 analysis s.4, ADOPTED; R-68's shape):** no criterion on this face certifies what a future event WILL find or load; every claim about a run or a served artifact is bound to that artifact's CONTENT HASH (`VersionId`/`ETag`/`sha256`/`CodeSha256`/`git hash-object`) READ AT THE EVENT -- a prediction made before the event is not evidence and a battery that prints one is refused at the drain.
- **S56 (ARMED, the CVO's): EVERY line citation in this order's JUDGMENT RECORD and result carries a vintage -- `path:line @ <commit-ish>` -- a bare `:NNN` is a defect the issuer greps for at the drain (`0 of N` bare citations is the bar).** CLAUDE.md Rule 22: a citation without a vintage is not a citation.
- **S73 (the `comp-iam roles` snapshot with no vintage) is an ESTATE-INSTRUMENT defect routed elsewhere and does NOT ride this order:** a live-plane IAM read here uses `comp-iam live` or `.tools/aws iam get-role`, never `comp-iam roles`.
- **R-40 (standing bar, `1.0.0_SA_CTO` @233f5fd5e4):** every criterion whose subject is a RUN or a PRODUCED ARTIFACT records that artifact's CONTENT HASH (`git hash-object`, `sha256sum`, or the service's own digest such as `ETag`/`CodeSha256`) beside its run id in the instance, and is graded against the hash; a label, a path or a timestamp ordering is not an identity.
- **Surprises:** ONE row per premise that does not hold, path that is not where this face says, result the invocation does not produce, or capability you lack -- at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-A-S<k>` with k continuing that coordinate's numbering (read the file's highest `A-S<k>` first; the file now holds SEVERAL fenced json blocks -- append your object INSIDE THE FIRST fence's array at its end, LF line endings, UTF-8 written explicitly, no json fence marker inside any row's text, `surfaced_at` a full ISO timestamp, omit `disarm_owner` on an INERT row and name a SEAT SERIAL, never a cell, when ARMED (R-42)); then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.
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

<criterion id="R64-AC1" cell_refs="IB-rtf-7"><invocation>timeout 900 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~V/battery_ib_rtf_7.py</invocation><expect>IBR64-STEP4-BUCKET-POLICY-REMOVED-2-OF-2</expect></criterion>
**`R64-AC1` -- PASSES BY OUTPUT:** (a) `N` identities enumerated with ARNs; (b) `2N of 2N` attempts printed verbatim under a ledger entry; (c) `get-bucket-policy` -> `NoSuchBucketPolicy` on `2 of 2` buckets. The token prints only on the `2 of 2` success; every denial is a truthful FAIL by output with the carry line written, and the battery re-runs every attempt each run (a denial is re-measured, never remembered).

<criterion id="R64-AC2" cell_refs="IB-rtf-7" judgment="true"/>
**`R64-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: which identity classes the live fence structurally admits and why root alone escapes a `Principal: *` Deny; whether a break-glass exemption (an operator identity present in every fence from birth) belongs in the registry's exemption contract so a first apply can never lock out its own applier -- a PROPOSAL for the CTO/CRO, never built here; and what the seat could not try and why. No verdict. Every line citation carries `@<commit-ish>`.

<expected_criteria>R64-AC1, R64-AC2</expected_criteria>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtf-7.step-4-attempted-by-every-credential-the-seat-holds.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.6, cell `IB-rtf-7` (s.R6.5 -- the mid-round additions on rows W4-S41 / W1-S29 and the Andrew-direct ~06:3xZ).
<owned_cells>IB-rtf-7</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired.
comp-iam: RUN at the cut by the issuer -- the live fence denies every IAM identity measured (AccessDenied 2 of 2 on the applying identity at 05:5xZ); DESIRED = the registry's three exemptions @845343f925; APPLIED = the empty-exemption policy of 2026-09-18; this order's attempts are the discriminator across every identity the seat holds. BLIND SPOT: the account root, which no bucket policy binds and no seat holds.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `.tools/**`, `data/**` and `lib/**` path resolves to its own lane at HEAD and is admitted ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: R64-AC1, R64-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~V/IRPT_BCKEND.TO-IB-rtf-7.step-4-attempted-by-every-credential-the-seat-holds.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and -- R-40 -- the content hash of every produced or served artifact the row grades, EACH PINNED TO THE COMMIT THAT CARRIED IT (commit the battery, its output and the result BEFORE the instance; `PENDING-THIS-COMMIT` is a ONE-SHOT sentinel -- a later re-commit of the instance re-pins every such row); a blob pin is written `blob <hash>`; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~V/IRPT_BCKEND.TO-IB-rtf-7.step-4-attempted-by-every-credential-the-seat-holds.proof_of_spec.json --governing-order org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtf-7.step-4-attempted-by-every-credential-the-seat-holds.md` BEFORE the complete flip; rc 0 AND R64-AC1 PASS-by-output, then flip this order's `<status>` to `complete` and commit instance and flip together. A FAIL row leaves the order open and is your final report on it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE (a worker) or ONE broker message to `2.0.0_SA_COO~B` (a Tier-2 seat), once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
