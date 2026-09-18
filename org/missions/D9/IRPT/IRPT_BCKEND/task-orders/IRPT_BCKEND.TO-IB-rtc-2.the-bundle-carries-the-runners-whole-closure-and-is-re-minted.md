# TO IRPT_BCKEND.TO-IB-rtc-2 -- THE BUNDLE CARRIES THE RUNNER'S WHOLE CLOSURE AND IS RE-MINTED -- AMENDED under R-45: the guard gains a member-level DISTRIBUTION flag (the member keeps its loose leg AND a commit to it re-mints the bundle), the eight-file closure is declared with the two out-of-glob members ADMITTED, the flag's own two-leg hazard is graded by a consistency check with a one-leg MUTANT, the bundle is re-minted through the guard, and the host proves the closure imports at repo shape -- a Rule 13 DS act

<to_id>IRPT_BCKEND.TO-IB-rtc-2</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.4.0_DS_ClientPlatform~X</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-18</issued_date>
<status>pending -- RE-HANDED by 2.0.0_SA_COO~B at 2026-09-18T03:1xZ to the DS lane under AMENDMENT 1 (R-45 @57bc083d45); the first pass (branch 768f558427, drained @f2fc496c3d) read R32-AC1 FAIL as a MEASUREMENT with 0 of 6 arms and surfaced the shape now ruled. A head; no cross-slot wait. Its merge releases IB-rtc-3 and IB-rtc-6.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 3 (AMENDMENT 1 on R-44/R-45 @57bc083d45) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.14 @b8e98d5a4d (ADMITTED, both L4-R halves SIGNED) | **Round-2 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND2_ANALYSIS.md` @cfe3a33a9b | **Rulings this cell executes:** R-44 / R-45, `org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260917.md` @57bc083d45 | **Decomp cell:** `IB-rtc-2` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.3, s.R3 + s.R3.6) | **outcome_ref:** FWD-1, FWD-7 (dependency), FWD-5

---

## IDENTITY AND WORKTREE

- **Serial:** `0.4.0_DS_ClientPlatform~X`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.4.0_DS_ClientPlatform~X;`.
- **Worktree:** `/c/tmp/wk-irpt-3-ds2` on branch `wk-irpt_bckend-3-ds2`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree; make a path absolute by prefixing `/c/tmp/wk-irpt-3-ds2/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.4.0_DS_ClientPlatform~X <0.4.0_DS_ClientPlatform~X@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/` (granted by the tree convention). Batteries are named `battery_<cell>.py`, the cell id lower-cased with underscores.
- **Python:** `py -3.12`. AWS through `.tools/aws`. `.tools/terraform.exe` is provisioned by the issuer. A recursive `grep`/`find` in Bash is DENIED by a rail hook and a denial aborts the WHOLE call; use the Read/Grep tools and keep a gated read in its own call. Capture `safe-commit.sh` output to a file, never pipe it to `tail`, never pair it with `$( )`.
- **You are the Tier-2 DS seat re-handed this order:** your first pass's deliverables and rows (S58, S59, S60, S62; battery_ib_rtc_2.py; the FAIL instance) are at HEAD under this home and are the starting point, not something to redo. The old worktree /c/tmp/wk-irpt-3-ds is gone; use the new one named above.

---

## THE CELL

**The ruling this cell executes (R-45 @57bc083d45, verbatim):** "the bundle takes a member-level DISTRIBUTION flag (the member keeps its loose leg AND a commit re-mints the bundle) plus a REPO-SHAPED unpack. ... ADDED CONTROL, because the flag creates the hazard it removes one level over: a distribution member now has TWO deploy legs per commit, and if one lands and the other does not the result is exactly the divergence the flag exists to prevent, reading green on whichever leg is inspected. The cell grades CONSISTENCY after a real commit -- served loose ETag equals repo md5 AND bundle member bytes equal repo bytes -- with a MUTANT that advances only one leg and must fail. A flag that routes to two places is only as good as the check that both arrived."

**The issuer's L6 rulings inside this amendment:**
- **S58 is ADMITTED:** `data/firm_registry.json` and `infra/aws/lambda/investor-reporting/_contracts/DirectoryEntry.schema.json` are bundle members although they sit outside the member globs the first face named; the bundle already carries `_ids/ids.py` under amendment H3 on the same reading. Both are `<paths>` below.
- **Member names ARE repo paths** (the closure member for `data/inf/scripts/gold/runners_inf/runner_common.py` is stored under that name in the tarball, never flattened), because IB-rtc-3's repo-shaped unpack (R-45's other half) extracts at `$W` by member name. The runner's own three (`directory_runner.py`, `holdings_snapshot.py` and whatever else the first pass found beside them) keep their present names only if the unpack still places them where `directory_runner` derives; state which.
- **The REPO-SHAPED UNPACK is NOT this cell's** -- `refresh.py` is IB-rtc-3's write surface. This cell proves the closure at repo shape ON THE HOST by its own extract into `/tmp` (arm e), never through the deployed dispatch.

**What L5 adds:**
- (a) The DISTRIBUTION flag: one declarative marker per member in `.tools/safe_deploy_core.py` `CODE_TREES` (the shape is yours inside the guard's own idiom; `bundle_for_member()` and the X-iii loop at `:1272-1303` must read it), such that a flagged member stays in `loose` AND triggers the bundle re-mint. The guard's tests: the two files that failed at IB-rt-5's baseline (S29) are not this cell's to repair, but NO test that passed before may fail after, and the flag gets its OWN tests (a flagged member routes to BOTH legs; an unflagged member routes as before). Print `k of k` passing with the baseline failures named.
- (b) The closure declared: `8 of 8` (your first pass's derived set; re-derive at the branch tip and print the diff against 8), three of them flagged DISTRIBUTION.
- (c) THE CONSISTENCY CONTROL (R-45): after a REAL commit to one distribution member on your branch (a comment line is a real commit), the QA-deploy through `.tools/safe-deploy.sh` must land BOTH legs: the served loose key's `ETag == repo md5` AND the bundle's member bytes `== repo bytes` (sha256 both), printed per member; then the MUTANT -- advance exactly one leg (re-upload the loose key from a stale copy, or re-mint from a stale tree, whichever the guard lets you do WITHOUT a bare `aws s3 cp` to a production key... if neither is reachable without a bare copy, the mutant is run against a QA prefix or a local dry-run of the guard's routing with the divergence INJECTED, and the plane is named) -- and the check must read FAIL. ⚠ Every leg you touch is a FIRM's served module: do it on the QA path the guard provides, under a ledger entry with its OPEN sentinel committed before the act (bound 4), and print before/after ETags so a reader can see nothing production-facing moved except by the guard's own mechanism.
- (d) Re-mint: `.tools/safe-deploy.sh --mint-bundle investor_reporting`; `head-object` on the minted key printing `ETag`, `VersionId`, `source-repo-paths` naming 8 of 8, and the tarball `sha256` from downloaded bytes (R-40); the NEGATIVE CONTROL against the PRE-CELL object `7791109bada2dbb44c5ac742b65671ee` (4 members) so a re-mint is told from a no-op.
- (e) On the host (`i-02448edb624a7a7cf`; ONE `StartInstances` admitted if stopped, never a stop): a READ-ONLY SSM command that downloads the minted tarball to `/tmp`, extracts it REPO-SHAPED under a `/tmp` root, lists `8 of 8` members, and imports `directory_runner` instantiating `SourceSet` for all three firms -> `IMPORT-OK` x3, with `0` network events (your first pass's counter and its positive control).

---

## DELIVERABLE

The guard edit with its tests; the declaration; the ledger entry + sentinel commits; the re-minted key's identity; `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/battery_ib_rtc_2.py` re-cut to grade (a)-(e), `IB-rtc-2_R32-AC1_battery_output.txt`, `battery_ib_rtc_2.result.md` (append a dated AMENDMENT-1 section; keep the first pass's text), the proof instance.

---

## BOUNDS

- **Rule 13 binds you:** the mint and every QA-deploy leg go through `.tools/safe-deploy.sh`; never a bare `aws s3 cp` to a served key.
- **Read-only on the host** except `/tmp`; no runner is executed end-to-end here; no Terraform apply; `refresh.py` is not yours.
- **R-40 (standing bar, `1.0.0_SA_CTO` @233f5fd5e4):** every criterion whose subject is a RUN or a PRODUCED ARTIFACT records that artifact's CONTENT HASH (`git hash-object`, `sha256sum`, or the service's own digest such as `ETag`/`CodeSha256`) beside its run id in the instance, and is graded against the hash; a label, a path or a timestamp ordering is not an identity.
- **Surprises:** ONE row per premise that does not hold, path that is not where this face says, result the invocation does not produce, or capability you lack -- at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-D-S<k>` with k continuing that coordinate's numbering (read the file's highest `D-S<k>` first; the file now holds SEVERAL fenced json blocks -- append your object INSIDE THE FIRST fence's array at its end, LF line endings, UTF-8 written explicitly, no json fence marker inside any row's text, `surfaced_at` a full ISO timestamp, omit `disarm_owner` on an INERT row and name a SEAT SERIAL, never a cell, when ARMED (R-42)); then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.

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

<criterion id="R32-AC1" cell_refs="IB-rtc-2"><invocation>timeout 1200 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/battery_ib_rtc_2.py</invocation><expect>IBR32-CLOSURE-MINTED-AND-IMPORTS-ON-HOST</expect></criterion>
**`R32-AC1` -- PASSES BY OUTPUT, every arm with its denominator:** (a) the flag's tests pass `k of k`, no prior pass regressed, baseline failures named; (b) `8 of 8` declared, `3` flagged; (c) both legs consistent after the real commit (`ETag == md5` and `sha256 == sha256`, per member) AND the mutant reads FAIL, plane named; (d) the minted key's identity with `source-repo-paths` naming `8 of 8`, sha256 recorded, negative control against `7791109b` DIFFERS; (e) `8 of 8` members extracted repo-shaped on the host and `IMPORT-OK 3 of 3` with `0` network events. The token prints only when (a)-(e) hold.

<criterion id="R32-AC2" cell_refs="IB-rtc-2" judgment="true"/>
**`R32-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: whether the flag's shape is the guard's own idiom or a second mechanism beside X-iii; what the mutant actually advanced and on which plane; whether a firm's served module moved by anything other than the guard's own routing during (c); and what the host import proved about the 49 Financial module WITHOUT reading 49 Financial data. No verdict.

<expected_criteria>R32-AC1, R32-AC2</expected_criteria>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtc-2.the-bundle-carries-the-runners-whole-closure-and-is-re-minted.md
.tools/safe_deploy_core.py
.tools/safe-deploy.sh
.tools/tests/
data/assets/scripts/gold/runners_49f/runner_common.py
data/inf/scripts/gold/runners_inf/runner_common.py
data/cot/scripts/gold/runners_cot/runner_common.py
data/firm_registry.json
infra/aws/lambda/investor-reporting/_contracts/DirectoryEntry.schema.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.3, cell `IB-rtc-2` (s.R3.1 the rectangle; s.R3.6 AMENDMENT 1 -- the edges, seating and bounds of this cell as amended).
<owned_cells>IB-rtc-2</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, rule or trigger is created, changed or fired; one StartInstances is admitted and is not a schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted or applied; the mint and the QA legs run under the DS lane's existing grant through the guard. BLIND SPOT stated: the guard's S3-membership check is the control, arm (d).
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `.tools/**`, `data/**` and `lib/**` path resolves to its own lane at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: R32-AC1, R32-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rtc-2.the-bundle-carries-the-runners-whole-closure-and-is-re-minted.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and -- R-40 -- the content hash of every produced or served artifact the row grades; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rtc-2.the-bundle-carries-the-runners-whole-closure-and-is-re-minted.proof_of_spec.json R32-AC1,R32-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it. The PENDING-THIS-COMMIT sentinel is one-shot: pin artifact rows to the commit that carries them.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
