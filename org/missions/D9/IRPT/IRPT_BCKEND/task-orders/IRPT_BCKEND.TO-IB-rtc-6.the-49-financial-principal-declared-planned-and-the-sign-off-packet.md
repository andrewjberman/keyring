# TO IRPT_BCKEND.TO-IB-rtc-6 -- THE 49 FINANCIAL PRINCIPAL, DECLARED, PLANNED, AND THE SIGN-OFF PACKET: a role whose name is the naming builder's output, trusted by the mdpf host role, granted exactly the five 49 Financial dimension reads the directory runner needs and nothing else; the runner's 49 Financial source set reads through that role; the writer census of the 49 Financial directory prefix; a plan with 0 destroys; and the never-widen sign-off packet with the blast radius and per-key rollback written for the two halves -- NO APPLY in this cell (R-44)

<to_id>IRPT_BCKEND.TO-IB-rtc-6</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.4.0_DS_ClientPlatform~X</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-18</issued_date>
<status>complete -- 0.4.0_DS_ClientPlatform~X 2026-09-18T06:1xZ on wk-irpt_bckend-3-ds3: R36-AC1 PASS, 6 of 6 graded arms, token printed (battery output @2a64c390b5, run from a fresh checkout at 7047e09e79); R36-AC2 recorded for 3.0.0_SA_CVO; proof instance VALID rc=0. DECLARED + PLANNED + PACKET only -- NOTHING APPLIED; the apply and the live negative control are IB-rtc-7's after both sign-off halves (packet NEVER_WIDEN_SIGNOFF_PACKET_IB-rtc-6.md; rows S65/S68 ARMED on 2.0.0_SA_COO~B). Was: pending, HANDED by 2.0.0_SA_COO~B at 2026-09-18T04:48Z after IB-rtc-2 (amended) merged @74d8367e75.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 3 (AMENDMENT 1 on R-44/R-45 @57bc083d45) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.14 @b8e98d5a4d (ADMITTED, both L4-R halves SIGNED) | **Round-2 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND2_ANALYSIS.md` @cfe3a33a9b | **Rulings this cell executes:** R-44 / R-45, `org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260917.md` @57bc083d45 | **Decomp cell:** `IB-rtc-6` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.3, s.R3 + s.R3.6) | **outcome_ref:** FWD-1, FWD-7 (the 49 Financial third)

---

## IDENTITY AND WORKTREE

- **Serial:** `0.4.0_DS_ClientPlatform~X`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.4.0_DS_ClientPlatform~X;`.
- **Worktree:** `/c/tmp/wk-irpt-3-ds3` on branch `wk-irpt_bckend-3-ds3`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree; make a path absolute by prefixing `/c/tmp/wk-irpt-3-ds3/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.4.0_DS_ClientPlatform~X <0.4.0_DS_ClientPlatform~X@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/` (granted by the tree convention). Batteries are named `battery_<cell>.py`, the cell id lower-cased with underscores.
- **Python:** `py -3.12`. AWS through `.tools/aws`. `.tools/terraform.exe` is provisioned by the issuer. A recursive `grep`/`find` in Bash is DENIED by a rail hook and a denial aborts the WHOLE call; use the Read/Grep tools and keep a gated read in its own call. Capture `safe-commit.sh` output to a file, never pipe it to `tail`, never pair it with `$( )`.

---

## THE CELL

**The ruling this cell executes (R-44 @57bc083d45, verbatim):** "the 49 Financial build runs under a 49 Financial principal, assumed by the dispatch for that firm only, reading only that firm's dimensions and writing only that firm's directory prefix; the other two firms keep the host role. ... THREE CONDITIONS: 1. The role name is BUILDER OUTPUT (Rule 30) -- name(<registry key>, ..., kind="role"), never typed. 2. The IAM apply is a never-widen-class act. The sign-off names the BLAST RADIUS -- what the role may touch and the rollback per key -- not the producer's intention. Ledger entry opened at start, closed at completion. 3. A NEGATIVE CONTROL ON THE NEW ROLE, not only a positive one. ... Count the WRITERS of the 49 Financial directory prefix while you are there."

**What this cell DOES and does NOT do, split deliberately:** it DECLARES, PLANS and WRITES THE PACKET; it does NOT apply. The apply and the negative control on the LIVE principal are IB-rtc-7's, after both sign-off halves exist at HEAD (the COO's is `2.0.0_SA_COO~B`'s, the CTO's is `1.0.0_SA_CTO`'s -- CLAUDE.md: never-widen sign-off is CTO+COO). A cell cannot wait for a signature, so the round splits the act at the signature.

**What L5 adds:**
- (a) THE NAME: call `lib/opal_naming.py` `name(...)` for the role (and any policy name) with the 49 Financial scope from `infra/logic/registry/scopes.json` (`49financial`) and a function word for the directory identity read; record the exact call and its output in the instance (Rule 30). ⛔ If the builder REFUSES (system or function word unknown), that is a MISSING REGISTRY ROW to add under `infra/logic/registry/` per Rule 30 -- print the refusal verbatim, propose the row in your result, file a BLOCKING row, and STOP the naming arm; never hand-type a name.
- (b) THE DECLARATION, in `infra/aws/terraform/investor-reporting/directory/` (the root that owns the refresh; its `iam.tf` idiom -- one role per root, prefix-conditioned `ListBucket`, never bucket-wide): `aws_iam_role` with a trust policy assumable ONLY by `mdpf-daily-runner-ec2-role` (`sts:AssumeRole`, an `ExternalId` or a session-name condition if the root's idiom has one); an inline policy granting `s3:GetObject` on the FIVE `opal-data-49financial/gold/advi/dimensions/<table>/*` prefixes W2-S49 names and a prefix-conditioned `s3:ListBucket` on exactly those five, and NOTHING on any other bucket or prefix -- the write to the 49 Financial directory destination stays on the host role's existing `IrptDirectoryFirmDestWrite` grant (the destination is `opal-data-bd/investor-reporting/directory/`, the legacy 49 Financial bucket, until D14 moves it; say so). Plus, on the host role's own declaration (`infra/aws/terraform/mdpf-pipeline/iam.tf`, `mdpf-runner-scoped`), ONE statement: `sts:AssumeRole` on the new role's ARN -- read that file's header rules first (prefix-conditioned, never bucket-wide, and the DELIBERATELY ABSENT prefixes 1-5 note at :592-621, which this design honours by never granting the mdpf role those reads).
- (c) THE RUNNER: `directory_runner.py`'s `Firm49F` source set reads its dimensions through a boto3 session on the assumed role (`sts.assume_role` with the role ARN from an environment variable or the dispatch's parameter, never a literal), and ONLY that source set; INF and COT unchanged; a unit test with a stubbed STS proves the 49F reads go through the assumed session and the other two do not. `refresh.py` (IB-rtc-3's surface, merged before you start) passes the role ARN into the runner's environment for the 49f firm only -- if that needs a `refresh.py` edit, it is a `<paths>` entry below.
- (d) THE WRITER CENSUS (R-44): every principal that can write `investor-reporting/directory/` under the 49 Financial destination bucket, read from the live policies (`comp-iam-usage who-can-reach`, plus the bucket policy), denominator printed; the new role is NOT among the writers.
- (e) THE PLAN: `terraform plan` on BOTH roots (`directory/`, `mdpf-pipeline/`) with the vendored binary, printed `N to add, 0 to change, 0 to destroy` (or the exact non-zero explained), saved as artifacts with their sha256 (R-40). NO APPLY.
- (f) THE PACKET: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtc-6.md` -- for each key/prefix the act touches: the exact statements added, the blast radius (who can now do what they could not), the rollback per key (the `terraform` state before, the exact removal), the writer census from (d), the negative-control design IB-rtc-7 will run (the assumed role attempting `inf` and `cot` reads and the 49F DESTINATION write, each expected `AccessDenied`), and the name-prefix check (the builder's name matches none of `role/cot-*`, `role/inf-*`, `role/mdpf-*`, `role/opal-assets-mdpf-*`). The two halves are signed by the seats, not by you.

---

## DELIVERABLE

The Terraform declarations (uncommitted-to-live, committed-to-branch); the runner edit and its test; the plans; the packet; `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/battery_ib_rtc_6.py`, `IB-rtc-6_R36-AC1_battery_output.txt`, `the-49f-principal-declared.result.md`; the proof instance.

---

## BOUNDS

- **NO APPLY, NO IAM CHANGE ON THE LIVE PLANE, NO MINT.** Plans only. The guard on `data/*/scripts/gold` (Rule 13) is why this is the DS lane's.
- **Cross-firm, both shapes (s.8 item 3):** the new role reads ONE firm's dimensions and nothing else; a grant on any other firm's prefix is a design error, not a convenience.
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

<criterion id="R36-AC1" cell_refs="IB-rtc-6"><invocation>timeout 900 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/battery_ib_rtc_6.py</invocation><expect>IBR36-PRINCIPAL-DECLARED-PLANNED-PACKET-WRITTEN</expect></criterion>
**`R36-AC1` -- PASSES BY OUTPUT:** (a) the builder call and its output printed, the name matching `0 of 4` denied prefixes; (b) the declaration's statements enumerated: `5` GetObject prefixes, `1` prefix-conditioned ListBucket with `5` prefixes, `1` trust principal, `1` AssumeRole statement on the host role, `0` statements on any other bucket; (c) the runner test: 49F reads through the assumed session `1 of 1`, INF/COT through the host session `2 of 2`; (d) writers of the 49F directory prefix `W of W` enumerated, new role among them `0`; (e) two plans, `0 to destroy` each, sha256 recorded; (f) the packet present with every key's rollback and the negative-control design. The token prints only when (a)-(f) hold.

<criterion id="R36-AC2" cell_refs="IB-rtc-6" judgment="true"/>
**`R36-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: whether the trust policy is as narrow as the host role's own assumption path allows; whether reading the five dimensions through an assumed role changes what the runner writes (it must not); and whether the destination's legacy-bucket location (opal-data-bd) leaves the 49 Financial directory OUTSIDE the firm's own bucket in a way FWD-7's DONE WHEN cares about before D14. No verdict.

<expected_criteria>R36-AC1, R36-AC2</expected_criteria>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtc-6.the-49-financial-principal-declared-planned-and-the-sign-off-packet.md
infra/aws/terraform/investor-reporting/directory/
infra/aws/terraform/mdpf-pipeline/iam.tf
infra/aws/lambda/investor-reporting/directory/refresh.py
data/assets/scripts/gold/investor_reporting/
infra/logic/registry/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.3, cell `IB-rtc-6` (s.R3.1 the rectangle; s.R3.6 AMENDMENT 1 -- the edges, seating and bounds of this cell as amended).
<owned_cells>IB-rtc-6</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled, changed or fired.
comp-iam: RUN by this cell as arm (d) (who-can-reach on the 49F directory prefix) and as the plan; DESIRED plane only until IB-rtc-7 applies.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `.tools/**`, `data/**` and `lib/**` path resolves to its own lane at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: R36-AC1, R36-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rtc-6.the-49-financial-principal-declared-planned-and-the-sign-off-packet.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and -- R-40 -- the content hash of every produced or served artifact the row grades; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rtc-6.the-49-financial-principal-declared-planned-and-the-sign-off-packet.proof_of_spec.json R36-AC1,R36-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it. The PENDING-THIS-COMMIT sentinel is one-shot: pin artifact rows to the commit that carries them.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
