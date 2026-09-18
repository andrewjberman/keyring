# TO IRPT_BCKEND.TO-IB-rtd-4 -- THE ROUTE-BINDINGS DRIFT MEASURED AND ITS SIGN-OFF PACKET: `aws_s3_object.mdpf_route_bindings` is served at neither the committed blob nor this device's CRLF rendering (row S68), IB-rtc-7 targeted around it and the exposure survived the act; this cell measures the three-way difference by CONTENT, censuses the object's consumers and writers, states what an untargeted apply would change for each consumer, and writes the never-widen packet -- it DECLARES and does NOT apply

<to_id>IRPT_BCKEND.TO-IB-rtd-4</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~3</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-18</issued_date>
<status>complete -- 0.9.0_WK_IRPT_BCKEND~3 measured the three-way content difference (served 12,008B sha256 c9e54ce2... is a stale pre-C-1-repoint snapshot, neither the committed blob nor its CRLF rendering), censused 4 of 4 consumers (0 live code paths read the served object) and writers/readers-by-grant (3 of 263 / 6 of 263), and wrote NEVER_WIDEN_SIGNOFF_PACKET_IB-rtd-4.md recommending a targeted apply from LF bytes. R44-AC1 PASS-by-output, R44-AC2 recorded for 3.0.0_SA_CVO. proof_of_spec VALID rc=0. S68 stays ARMED (owner 2.0.0_SA_COO~B) pending IB-rtd-5's apply.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 4 (the CTO's round-3 analysis @5c59f68d70, msg 97944) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.14 @b8e98d5a4d (no addendum at round 3) | **Round-3 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND3_ANALYSIS.md` @5c59f68d70 | **Rulings carried:** R-40, R-42, R-44, R-45 @57bc083d45; the forward-looking-criterion bar (analysis s.4, ADOPTED) | **Decomp cell:** `IB-rtd-4` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.4, s.R4) | **outcome_ref:** FWD-7 (the deploy discipline the directory's root shares with MDPF)

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~3`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~3;`.
- **Worktree:** `/c/tmp/wk-irpt-4-3` on branch `wk-irpt_bckend-4-3`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree; make a path absolute by prefixing `/c/tmp/wk-irpt-4-3/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~3 <0.9.0_WK_IRPT_BCKEND~3@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/` (granted by the tree convention). Batteries are named `battery_<cell>.py`, the cell id lower-cased with underscores.
- **Python:** `py -3.12`. AWS through `.tools/aws`. `.tools/terraform.exe` is provisioned by the issuer. A recursive `grep`/`find` in Bash is DENIED by a rail hook and a denial aborts the WHOLE call; use the Read/Grep tools and keep a gated read in its own call. Capture `safe-commit.sh` output to a file, never pipe it to `tail`, never pair it with `$( )`.

---

## THE CELL

**The finding (row S68, `0.4.0_DS_ClientPlatform~X`, 05:45Z; CTO 97865 "I accept it as MDPF's owner ... it deserves its own blast-radius read in daylight"; analysis s.6):** `terraform plan` of `infra/aws/terraform/mdpf-pipeline` shows `aws_s3_object.mdpf_route_bindings` `source_hash` `56a03a1410848f88b006f1f98b69dced -> f94e8e4c5d7c56d93f6ab16af227721d`; `data/mdpf/config/route_bindings.yaml` has no `eol` attribute, this box renders it CRLF (185 CR, md5 `f94e8e4c`), the committed blob is LF (md5 `650f893a`), and the DEPLOYED object is neither (`56a03a14`) -- the committed file moved since the object was last applied, and an apply from this box would upload the CRLF rendering. IB-rtc-7 applied that root `-target=aws_iam_role_policy.mdpf_runner` and left the drift exactly as it was.

- (a) THE THREE-WAY DIFFERENCE BY CONTENT, not by hash alone: download the served object (`get-object`, its `ETag`/`VersionId`/`LastModified` and content-sha256 metadata), `git show HEAD:data/mdpf/config/route_bindings.yaml`, and the worktree file; normalise line endings and PARSE all three as YAML; print (i) whether served == committed after EOL normalisation (the committed change is CONTENT or ONLY EOL), (ii) the semantic diff of the parsed documents (keys added/removed/changed, denominator = keys), (iii) which commit last touched the file (`git log -1 -- data/mdpf/config/route_bindings.yaml`) and which deploy last wrote the object (CloudTrail `PutObject` on the key, or the object's metadata). Add the `eol=lf` attribute question as a FINDING (a `.gitattributes` line is a repo change outside this order; a row, not an edit).
- (b) THE CONSUMERS AND WRITERS of the served object: every reader of the key (`comp-pipescript io`, `comp-estate --resource route_bindings`, the graph manifest; the Lambdas/ECS tasks whose code or env names the key -- denominator printed) and every principal that may write it (the IAM census instrument IB-rtc-6 used, `N of M`). For each consumer: does its reader tolerate CRLF (a YAML loader does; a byte-compare or a hash check does not -- READ THE READER, cite `file:line @ commit`), and what the parsed-content change in (a)(ii) means for it.
- (c) THE PACKET, in the shape of IB-rtc-6's `NEVER_WIDEN_SIGNOFF_PACKET_IB-rtc-6.md`: the act (an untargeted apply of the mdpf-pipeline root, OR a targeted apply of `aws_s3_object.mdpf_route_bindings` alone, OR "the committed file is what is wrong and the served object is right" -- recommend one on the evidence), its plan text with hashes, the blast radius per consumer, the rollback (the prior object `VersionId` -- confirm the bucket versions), the writers census, and the untargeted root's FULL plan (anything besides this object is a further finding). The packet is for `1.0.0_SA_CTO` (MDPF's owner) and `2.0.0_SA_COO~B`; NOTHING IS APPLIED HERE.

---

## DELIVERABLE

`battery_ib_rtd_4.py`, `IB-rtd-4_R44-AC1_battery_output.txt`, `the-route-bindings-drift-measured.result.md`, `NEVER_WIDEN_SIGNOFF_PACKET_IB-rtd-4.md` (under your deliverables home); the proof instance.

---

## BOUNDS

- READ-ONLY on every plane: no apply (targeted or not), no `put-object`, no edit of `data/mdpf/config/`, no `.gitattributes` change. `terraform plan` only, with the vendored binary, `init` first.
- **THE FORWARD-LOOKING-CRITERION BAR (round-3 analysis s.4, ADOPTED; R-68's shape):** no criterion on this face certifies what a future event WILL find or load; every claim about a run or a served artifact is bound to that artifact's CONTENT HASH (`VersionId`/`ETag`/`sha256`/`CodeSha256`/`git hash-object`) READ AT THE EVENT -- a prediction made before the event is not evidence and a battery that prints one is refused at the drain.
- **S56 (ARMED, the CVO's): EVERY line citation in this order's JUDGMENT RECORD and result carries a vintage -- `path:line @ <commit-ish>` -- a bare `:NNN` is a defect the issuer greps for at the drain (`0 of N` bare citations is the bar).** CLAUDE.md Rule 22: a citation without a vintage is not a citation.
- **S73 (the `comp-iam roles` snapshot with no vintage) is an ESTATE-INSTRUMENT defect routed elsewhere and does NOT ride this order:** a live-plane IAM read here uses `comp-iam live` or `.tools/aws iam get-role`, never `comp-iam roles`.
- **R-40 (standing bar, `1.0.0_SA_CTO` @233f5fd5e4):** every criterion whose subject is a RUN or a PRODUCED ARTIFACT records that artifact's CONTENT HASH (`git hash-object`, `sha256sum`, or the service's own digest such as `ETag`/`CodeSha256`) beside its run id in the instance, and is graded against the hash; a label, a path or a timestamp ordering is not an identity.
- **Surprises:** ONE row per premise that does not hold, path that is not where this face says, result the invocation does not produce, or capability you lack -- at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W3-S<k>` with k continuing that coordinate's numbering (read the file's highest `W3-S<k>` first; the file now holds SEVERAL fenced json blocks -- append your object INSIDE THE FIRST fence's array at its end, LF line endings, UTF-8 written explicitly, no json fence marker inside any row's text, `surfaced_at` a full ISO timestamp, omit `disarm_owner` on an INERT row and name a SEAT SERIAL, never a cell, when ARMED (R-42)); then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.

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

<criterion id="R44-AC1" cell_refs="IB-rtd-4"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/battery_ib_rtd_4.py</invocation><expect>IBR44-ROUTE-BINDINGS-DRIFT-MEASURED-AND-PACKETED</expect></criterion>
**`R44-AC1` -- PASSES BY OUTPUT:** (a) the three-way content comparison printed with the EOL-normalised verdict and the parsed diff with denominator; (b) consumers `N of N` with each reader's CRLF tolerance cited `file:line @ commit`, writers `n of M`; (c) the packet written, naming the act recommended, its plan hashes, blast radius per consumer, rollback `VersionId`, and the full untargeted plan. The token prints only when every arm holds; the battery re-derives every count from the real world each run and never reads its own earlier output.

<criterion id="R44-AC2" cell_refs="IB-rtd-4" judgment="true"/>
**`R44-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: which of the three renderings is the intended one (the committed content, the served bytes, or neither), whether the drift is a rider of some other project's unapplied change (name the commit and its project), and whether the fix belongs to this project at all or to MDPF's owner as a separate act. No verdict. Every line citation carries `@<commit-ish>` (S56).

<expected_criteria>R44-AC1, R44-AC2</expected_criteria>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtd-4.the-route-bindings-drift-measured-and-its-sign-off-packet.md
infra/aws/terraform/mdpf-pipeline/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.4, cell `IB-rtd-4` (s.R4 -- the round-4 rectangle, edges, seating and bounds).
<owned_cells>IB-rtd-4</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired.
comp-iam: DECLARED-NOT-APPLICABLE at the cut (read-only); the packet's writers census is arm (b), with the census instrument's blind spot (identity policies only) stated there.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `.tools/**`, `data/**` and `lib/**` path resolves to its own lane at HEAD and is admitted ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: R44-AC1, R44-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/IRPT_BCKEND.TO-IB-rtd-4.the-route-bindings-drift-measured-and-its-sign-off-packet.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and -- R-40 -- the content hash of every produced or served artifact the row grades, EACH PINNED TO THE COMMIT THAT CARRIED IT (commit the battery, its output and the result BEFORE the instance, so no `PENDING-THIS-COMMIT` sentinel is needed); a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/IRPT_BCKEND.TO-IB-rtd-4.the-route-bindings-drift-measured-and-its-sign-off-packet.proof_of_spec.json --governing-order org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtd-4.the-route-bindings-drift-measured-and-its-sign-off-packet.md` BEFORE the complete flip; rc 0 AND R44-AC1 PASS-by-output, then flip this order's `<status>` to `complete` and commit instance and flip together. A FAIL row leaves the order open and is your final report on it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
