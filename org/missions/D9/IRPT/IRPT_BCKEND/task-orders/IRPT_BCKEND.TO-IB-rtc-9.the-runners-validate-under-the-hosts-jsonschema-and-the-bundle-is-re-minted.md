# TO IRPT_BCKEND.TO-IB-rtc-9 -- THE RUNNERS VALIDATE UNDER THE HOST'S JSONSCHEMA AND THE BUNDLE IS RE-MINTED: both gold runners call a jsonschema API the host does not have (`Draft202012Validator`, `ValidationError.json_path` -- jsonschema 4.x; the host runs 3.2.0), so every real build now dies at validation after IB-rtc-3's date fix let it reach that line for the first time (row W2-S56); the two call sites are made version-tolerant with a test that pins the tolerance, the bundle is re-minted through the guard, and the fix is EXERCISED ON THE HOST against the real contract with a valid entry, a mutant, and the pre-cell tarball as the positive control of the defect -- a Rule 13 DS act, no apply, no IAM

<to_id>IRPT_BCKEND.TO-IB-rtc-9</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.4.0_DS_ClientPlatform~X</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-18</issued_date>
<status>pending -- HANDED by 2.0.0_SA_COO~B at 2026-09-18T07:5xZ to the DS lane, fourth in its queue, cut on row IRPT_BCKEND-W2-S56 (the issuer's ruling: ADJUDICABLE within L5/L6 -- a DS-lane code defect, fixed in code, never by mutating the shared host's package set). A head; its merge is a precondition of IB-rtc-7 and of IB-rtc-3's AMENDMENT 3 re-run.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 3 (AMENDMENT 1 on R-44/R-45 @57bc083d45; this cell added ~07:5xZ on row W2-S56) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.14 @b8e98d5a4d | **Rulings:** R-44 / R-45 @57bc083d45; the issuer's ruling on W2-S56 (this face) | **Decomp cell:** `IB-rtc-9` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.3, s.R3.6) | **outcome_ref:** FWD-1, FWD-7 (every firm's build dies at validation today)

---

## IDENTITY AND WORKTREE

- **Serial:** `0.4.0_DS_ClientPlatform~X`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.4.0_DS_ClientPlatform~X;`.
- **Worktree:** `/c/tmp/wk-irpt-3-ds5` on branch `wk-irpt_bckend-3-ds5`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`.
- **Repo root for every path below:** the worktree; make a path absolute by prefixing `/c/tmp/wk-irpt-3-ds5/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.4.0_DS_ClientPlatform~X <0.4.0_DS_ClientPlatform~X@opal.agent>" -F <msgfile> -- <paths>`. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/` (granted by the tree convention). Battery `battery_ib_rtc_9.py`.
- **Python:** `py -3.12`. AWS through `.tools/aws`. Capture `safe-commit.sh` and `safe-deploy.sh` output to files, never pipe them to `tail`, never pair with `$( )`. A recursive `grep`/`find` in Bash is DENIED by a rail hook; use the Read/Grep tools.

---

## THE CELL

**The defect, measured (row IRPT_BCKEND-W2-S56, `0.9.0_WK_IRPT_BCKEND~2`, 07:03Z):** with IB-rtc-3 AMENDMENT 2 deployed, the real fires for inflection and cottonwood now pass the runner's business-date check and die at `data/assets/scripts/gold/investor_reporting/directory_runner.py` `validate_entries()` (`:801-813` @a4db909717): `ERROR: <firm>: module 'jsonschema' has no attribute 'Draft202012Validator'`, rc=1, `BUILD_ENDED_UNSUCCESSFUL`. The host (`i-02448edb624a7a7cf`) runs `jsonschema==3.2.0` (its own dependency echo); `Draft202012Validator` arrived in 4.18.0 and `ValidationError.json_path` (used at `:810`) in 4.0.0, so 3.2.0 lacks BOTH, and the second would have raised on the first invalid entry even if the first were fixed. **The issuer's census of the whole bundle population (Rule 22: what the members SHARE):** `holdings_snapshot.py` `validate_snapshot()` (`:1148-1157` @a4db909717) makes the same `Draft202012Validator` call -- two call sites in two members, one shared premise. **The eleven `_contracts/*.schema.json` all declare `$schema` 2020-12 and NONE uses a 2019-09/2020-12-only keyword** (`prefixItems`, `$defs`, `unevaluatedProperties`, `dependentRequired`, `dependentSchemas`, `$dynamicRef`, `$anchor`, `contentSchema`, `minContains`, `maxContains` -- 0 of 11 at HEAD), so a draft-7 validator grades the same set of entries the 2020-12 one does.

**The issuer's ruling (ADJUDICABLE, L5/L6):** fix it IN CODE, in the DS lane, with a version-tolerant validator; **never by changing the shared host's installed packages** (that host is the MDPF daily runner -- an AE act with a blast radius on every MDPF chain, and outside this project). No host mutation of any kind.

- (a) **The fix, both call sites:** the validator class is chosen once, tolerant of the installed version (the 2020-12 class where it exists, else the newest the installed jsonschema provides that grades this contract identically -- draft 7 on 3.2.0; name the choice in a module-level helper the two runners share or duplicate verbatim, your call, stated); the error line in `validate_entries()` is formatted from `ValidationError.absolute_path` (present in 3.2.0), never `json_path`. ASCII only. Every `.py` edit passes `.tools/commit-gate.sh`. The two runners' behaviour on a VALID entry and on an INVALID entry is unchanged in meaning: same accept, same reject, an error line that still names the entry index and the failing path.
- (b) **The test that pins the tolerance** in `data/assets/scripts/gold/investor_reporting/tests/`: (i) an AST walk over the bundle's runtime members asserting NO attribute reference to `Draft202012Validator`, `Draft201909Validator` or `json_path` (the same shape as the Lambda's no-jsonschema-at-module-level test); (ii) `validate_entries()` and `validate_snapshot()` run against the REAL contracts and the REAL fixtures (`infra/aws/lambda/investor-reporting/_contracts/fixtures/DirectoryEntry.valid.json` / `.invalid.json`, `HoldingsSnapshot.valid.json` / `.invalid.json`): valid accepted, invalid refused with a path; (iii) the FALLBACK BRANCH exercised under a mutant environment -- the test removes `Draft202012Validator` from the `jsonschema` module for its duration (`monkeypatch.delattr`) and both validators still grade (ii) identically; a MUTANT of the fix that hard-codes the 2020-12 class fails (iii) -- print that it fails. Whole-suite run of the directory's tests, `N of N` passing, N printed.
- (c) **Re-mint:** `.tools/safe-deploy.sh --mint-bundle investor_reporting` under a change-management entry (OPEN sentinel committed before the act, closed before the grading reads); `head-object` printing `ETag`, `VersionId`, `source-repo-paths`, the tarball `sha256` from downloaded bytes (R-40); closure re-derived at your branch tip and printed (`8 of 8` or the new count with the diff against IB-rtc-8's list -- a test file is not a member); the NEGATIVE CONTROL against the PRE-CELL object (IB-rtc-8's mint, VersionId `q8myxeHdNw48w1uDb7YTcBh8DHV9TzU2`, ETag `479af04c0a3a1eb6651707b340df9926`) DIFFERS; both edited members' bytes inside the new tarball equal the repo blobs at your branch tip (`git hash-object` and sha256 printed); the three distribution members' loose legs unchanged, `3 of 3`, read-only.
- (d) **On the host** (`i-02448edb624a7a7cf`; ONE `StartInstances` admitted if stopped, never a stop; read-only except `/tmp`): the SSM extract of the NEW tarball at repo shape into `/tmp` as IB-rtc-8 did; print the host's `jsonschema.__version__` (the discriminator: expected `3.2.0`; if it is not, say so and grade against what it is); `IMPORT-OK` for every member; then, ON THE HOST, `validate_entries()` on the DirectoryEntry valid fixture (`1 of 1` accepted) and on the invalid fixture (refused, the error line printed with its path), and `validate_snapshot()` on the HoldingsSnapshot fixtures likewise; and the POSITIVE CONTROL OF THE DEFECT: the same two calls against the PRE-CELL tarball's members (extract `q8myxeHd...` beside it in `/tmp`) raise `AttributeError` naming `Draft202012Validator` -- the old bytes fail where the new bytes pass, on the same interpreter, the same minute. No firm build is run; no source bucket is read (49 Financial's `AccessDenied` is IB-rtc-7's, not yours).

---

## DELIVERABLE

The two runner edits + the test; the ledger entry + sentinel commits; the re-minted key's identity; `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/battery_ib_rtc_9.py`, `IB-rtc-9_R39-AC1_battery_output.txt`, `the-runners-validate-under-host-jsonschema.result.md`; the proof instance.

---

## BOUNDS

- **Rule 13 binds you:** the mint goes through `.tools/safe-deploy.sh`; never a bare `aws s3 cp` to a served key. **NO apply, NO IAM, NO package install or upgrade on the host, NO real commit to a distribution member, NO firm build end-to-end** (IB-rtc-3 AMENDMENT 3 and IB-rtc-7's).
- Read-only on the host except `/tmp`; never a stop.
- The contracts under `infra/aws/lambda/investor-reporting/_contracts/` are READ, never edited (their `$schema` line stays 2020-12; tolerance lives in the CALLER).
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

<criterion id="R39-AC1" cell_refs="IB-rtc-9"><invocation>timeout 900 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/battery_ib_rtc_9.py</invocation><expect>IBR39-RUNNERS-VALIDATE-UNDER-HOST-JSONSCHEMA</expect></criterion>
**`R39-AC1` -- PASSES BY OUTPUT:** (a) the AST walk reads `0` references to the three 4.x-only names across the runtime members, denominator printed; (b) the suite `N of N` with the fallback branch exercised under the mutant environment and the hard-coded mutant FAILING it; (c) the minted identity, closure count with diff, negative control against `479af04c` DIFFERS, both members' tarball bytes `==` branch-tip blobs, distribution legs `3 of 3` unchanged; (d) host `jsonschema.__version__` printed, `IMPORT-OK` all members, valid fixtures accepted `2 of 2`, invalid fixtures refused `2 of 2` with paths, and the pre-cell tarball raising `AttributeError` on both calls (`2 of 2`, the positive control). The token prints only when (a)-(d) hold.

<criterion id="R39-AC2" cell_refs="IB-rtc-9" judgment="true"/>
**`R39-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: whether the validator the host now runs grades the DirectoryEntry and HoldingsSnapshot contracts identically to the 2020-12 validator the code intended (the keyword census of the two contracts, printed), and whether any other bundle member or Lambda member in this project carries a jsonschema-4.x-only call the AST walk did not cover (name the population walked and the one not walked). No verdict.

<expected_criteria>R39-AC1, R39-AC2</expected_criteria>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtc-9.the-runners-validate-under-the-hosts-jsonschema-and-the-bundle-is-re-minted.md
data/assets/scripts/gold/investor_reporting/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.3, cell `IB-rtc-9` (s.R3.6, added on row W2-S56 -- the runners' validation under the host's jsonschema).
<owned_cells>IB-rtc-9</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled, changed or fired; one StartInstances is admitted and is not a schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted or applied; the mint runs under the DS lane's existing grant through the guard. BLIND SPOT stated: the guard's S3-membership check is the control, arm (c).
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). `data/assets/scripts/gold/investor_reporting/` is the DS lane's Rule 13 home. A path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: R39-AC1, R39-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rtc-9.the-runners-validate-under-the-hosts-jsonschema-and-the-bundle-is-re-minted.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and -- R-40 -- the content hash of every produced or served artifact the row grades, EACH PINNED TO THE COMMIT THAT CARRIED IT (a `PENDING-THIS-COMMIT` sentinel on an artifact an earlier commit already carried is INVALID at HEAD -- IB-rtc-3's instance @a4db909717 reads INVALID on exactly that, CCX class); a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rtc-9.the-runners-validate-under-the-hosts-jsonschema-and-the-bundle-is-re-minted.proof_of_spec.json R39-AC1,R39-AC2` BEFORE the complete flip; rc 0 AND R39-AC1 PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.
