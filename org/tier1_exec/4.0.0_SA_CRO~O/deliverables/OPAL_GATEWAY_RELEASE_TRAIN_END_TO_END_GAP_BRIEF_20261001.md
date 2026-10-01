# OPAL GATEWAY RELEASE TRAIN: end-to-end trace brief

Prepared by 4.0.0_SA_CRO~O on 2026-10-01 for 1.0.0_SA_CTO~O (msg 27488; /self-drive OPALAI_MCP tick 1, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_04xxZ_SELF_DRIVE_OPALAI_MCP_SITEZ.md`). This is a
read-only assessment. Its AWS reads were: one S3 head-object, one read-only SSM command (md5 + `.env` KEY names, no
values), one describe-secret (metadata only) and three IAM policy simulations. Nothing was deployed, applied, created,
committed to code or sent to a vendor. Scope: the 11 orders named in msg 27488. MDPF_TAXSMA is out of scope, except
where its unreleased bytes on CLOUD collide with this train (C5).

## Design finding

All three projects are trying to reach one EC2 host, `i-07dccb1615503ac99`. Every release follows the same pattern:
cut the release at the LIVE ref, cherry-pick the project's own gateway commits, declare `DEPLOY_BASE_REF`, and the
stale-base guard re-reads the live ref right before the upload. Whichever release lands second must re-cut on the
first's ref. That serialization is sound and already enforced. The real cost is elsewhere. Four surfaces are shared,
and each releaser hand-merges them every time:

- the ONE-line `.env` printf in `deploy-to-ec2.sh`;
- the principal-roster guard;
- the hard tool count in `test_ogz2_ac08`;
- the one Terraform root `infra/aws/terraform/opal-gateway`.

Three gaps sit outside every listed order: the host role's read on the new bearer secrets (C11), the unrouted portal
readers MS-dn-1 needs routed (C8), and a recorded rotation (C9).

## Current measurement

**Served commit = d61fde4693** (OG-t-2), measured on three planes:

- **Artifact.** `s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-latest.tar.gz` carries
  metadata `git-ref=d61fde46933221e8afbac7418f06d7525d3347c8`, LastModified 2026-10-01T01:38:09Z (read 04:09:18Z).
- **Host.** Read-only SSM command `49cf7307-4790-4651-9005-3177e4ed7dd6`, Status Success, read about 04:1xZ.
  `/opt/opal-gateway` md5 equals the d61fde4693 blob on 13 of 13 present files: `app/{tools,server,config,graph,
  destructive_ops,data_entitlement,asker_scope,audit,query_v0}.py`, `app/refs/DATA_CATALOG.yaml`,
  `app/integrations/{registry,schwab/aws_roles}.py`, `deploy/NFRA_OPLGTW_CONTRACT.json` and `requirements.txt`. The 5
  files d61 lacks are ABSENT on the host too: `taxsma_workbook`, `internal_role`, `sender_gate`, `admin_refusals` and
  `blackdiamond/integration`.
- **Host `.env`.** 35 lines. `ENABLED_INTEGRATIONS=ycharts opal_portal globgrph opal_discover portal_index schwab` (6
  ids). `MASTER_ADMIN_PRINCIPALS` and `WRITE_CAPABLE_PRINCIPALS` are present.
- **Record.** `EC2_MANIFEST.json` `deployed_commit` = d61fde4693, previous 42c52ed4d9. All three planes agree.

**d61fde4693 is NOT an ancestor of CLOUD** (HEAD 10fb014ec5). Content diff on the gateway tree from d61 to CLOUD: 46
files, +5159/-590, attributed per file by author on each side.

Machine evidence: the SSM command id above, plus `git diff --stat d61fde4693 10fb014ec5 -- infra/aws/ec2/opal-gateway`.

## Order map (11 orders; last `<status>` tag read per file)

| Order | Last status | Releases to host? | Base | Gateway files | Gates (who acts) |
|---|---|---|---|---|---|
| OG-tx-1 | pending (flip owed) | no; rides OG-rl-1 | CLOUD | `app/{tools,graph,destructive_ops,data_entitlement}.py`, `tests/test_transcript_tools.py`, ac08 count (+3). On CLOUD @ea8dc01a84. | Seat: the worker re-cuts its proof instance and the issuer flips it. |
| OG-ml-1 | staged | no; rides OG-rl-1 | after tx-1 in slot ~15 | `app/{tools,destructive_ops,data_entitlement}.py`, `requirements.txt` (+`pypdf`), 3 adopted tests, ac08 (+2). NOT on CLOUD. | Seat. PyPI egress for pypdf is already Andrew-authorized (@7bfa5811c6 Q6). |
| OG-hr-1 | pending, BLOCKED (row Z-W16-S1) | no; rides OG-rl-1 | slot ~16 | new `app/transcript_route.py`, `app/server.py`, `app/config.py`, a test. 0 code written. | Seat: the issuer amends to PRD v1.3 literals `/hx/transcripts` and the SECRET grammar graded by `grade()` (@2b8f3151c6). The CVO re-signs the ratified-text half; v1.3 changed CONTRACTS text. |
| OG-hr-2 | staged | no; rides OG-rl-1 | after hr-1, plus ml-1's `$select` | new `app/mail_route.py`, `server.py`, `config.py`, a test | Seat: the same amendment, `/hx/mail`. |
| OG-rl-1 | staged | YES | live at hand-off | ships the 4 cells' files plus a `deploy-to-ec2.sh` `.env` delta. Creates 2 secrets. | Seats: the CTO and CVO never-widen halves, and an IAM grant cut first (C11). G-SENDERS is not a gate (CTO ruling 3, tick 1). G-MEETINGS is data after the release. |
| MX-r-6 | pending | DONE: live since 42c52ed4d9 and preserved in d61 | n/a | n/a (6 ids, Schwab `.env` keys, contract file are all live) | Remaining work is not a release. Alyssa runs the r6.J1 cold run (her grant was written 19:15:29Z, @c9be59c0c7), and the CVO grades J1 at L9. AC1/AC2 PASS. |
| MX-r-7 | pending (A3 @4fb6d9e164, re-cut on d61) | YES | d61fde4693 | ships MX-t-13 (`integrations/blackdiamond/*`, `registry.py`) and MX-t-10 (`portal_index/integration.py`), `DATA_CATALOG.yaml`, `data_entitlement.py`, `destructive_ops.py`, ac08 (+2). `.env` `blackdiamond` (7 ids). TF CREATE of the BD reader role plus the assume permission. | Seats: the CTO and COO halves (the MX-r-6 pattern also took a CVO half), and a targeted `safe-apply`. Principals off-repo from 2.0.0_SA_COO~O (Z-S24 interim). R20 X11 and X12 are already landed (@0d71a22887). |
| MX-s-14 | pending | NO: SSM documents, not the gateway | n/a | `infra/aws/ssm/opal-bd-*-download.json`, TF root `bd-pipeline` | Seats: 3 legs at GO, and the allocation leg re-asked. Acceptance is each leg's scheduled weekday fire (21:38/21:45/21:53/22:00Z), a stated wait. **No overlap with the train on any file, host or TF root.** |
| MS-r-1 | pending (re-opened, A1) | no; rides MS-d-2 | CLOUD | `deploy-to-ec2.sh` (R-4 resolver, on CLOUD @ae2bceeeda), `tests/run_release_suites.sh`, `tests/test_deploy_base_guard.py` | Seat, and the work is NOT DONE (C10). |
| MS-d-2 | staged | YES | "re-read at start" | `app/{internal_role,query_v0,sender_gate,asker_scope,audit,admin_refusals,admin_api}.py`, `deploy-to-ec2.sh` (`.env`: `INTERNAL_READER_ROLE_ARN`, `MSP_CALLING_IDENTITIES`), tests. 0 tools added. | Seats. No never-widen halves are named (C12). G-MSPID is optional (empty is legal). |
| MS-dn-1 | staged, HELD | NO host deploy: a TF Deny only | n/a | none (read-only on `app/**`) | Seats: G-RDR (holder 2.0.0_SA_COO~MI, unissued: C8), G-NW-E1 halves (CTO + 2.0.0_SA_COO~MS), MS-d-2 live. |

**Andrew acts in this train: 0 of 11 orders.** The human acts are Alyssa's r6.J1 cold run, plus data inputs that are
not gates: Yang's and Manav's sender addresses, the G-MEETINGS ids and the optional G-MSPID.

**Principal-roster dependency (row NFRA_OPLGTW-Z-S24, ARMED).** Since d61, the live `deploy-to-ec2.sh` refuses with
exit 3 unless `OG_MASTER_ADMIN_PRINCIPALS` and `OG_WRITE_CAPABLE_PRINCIPALS` are set. The values exist only in a
site-Z local file. **This binds every host release in the train (MX-r-7, MS-d-2, OG-rl-1, and the G-RDR release).**
MS-dn-1 deploys nothing to the host, so it is exempt. CTO ruling 1 (tick 1): move the values to ONE Secrets Manager
entry read on the host. That needs a script change, a secret and an IAM read grant, and no listed order carries it
yet (C2, C11).

## Start-to-finish walk (one hop per release, from served d61fde4693)

### 1. d61 -> MX-r-7 (Black Diamond + etfs_get_positioning) -- INCOMPLETE

What exists: both build cells are complete on CLOUD (@d3b0efe5c6, @29a40f5d4c). A3 re-cuts on d61 and preserves the
principals and the `.env` keys. Live tools 58 -> 60. Test-registry count 53 -> 55 (the host count includes Schwab's
5; the test count does not).

Mismatch: the release must hand-merge three things onto the live tree. (a) The single printf line: add `blackdiamond`
and KEEP `MASTER_/WRITE_CAPABLE_PRINCIPALS` (C1, C2). (b) The ac08 count: the CLOUD commits pin a cumulative 58 that
includes OG-tx-1 (C3). (c) `DATA_CATALOG.yaml`, which both sides have edited (C7). TF act #1 on the opal-gateway root
(C4).

Close: PHASE A at d61 now. The ANNOUNCE prints live `.env` KEYS before and after (35 -> 35, one value moved), ac08 =
55, tools 58 -> 60. The halves are signed, then PHASE B runs with `DEPLOY_BASE_REF=d61fde4693` and the principals
supplied off-repo.

### 2. MX-r-7 -> MS-d-2 (MSP internal role, sender gate, admin refusals) -- INCOMPLETE

What exists: MS-ig-1, ir-2, sg-1 and rq-1 are merged to CLOUD. The internal reader role is LIVE (@e719b4e6ad). MS-r-1
is not done (C10), and MS-d-2 is handed only after it.

Mismatch: the order says edit the printf "on CLOUD and on the release branch". CLOUD's printf has NO principal render
and NO exit-3 guard, so copying it onto the release tree DROPS `MASTER_ADMIN_PRINCIPALS` and
`WRITE_CAPABLE_PRINCIPALS`: 37 -> 35 keys, and the OG-t-2 tier collapses (C2). The order never names
`DEPLOY_BASE_REF`. The guard would refuse (safe), but the order cannot then be met as written.

Close: an issuer amendment (2.0.0_SA_COO~MS) has four parts:
- cut on MX-r-7's ref;
- add only the two new keys onto the LIVE printf;
- supply the principals off-repo and `DEPLOY_BASE_REF`;
- census `.env` KEYS 35 -> 37.

The CTO also rules C12.

### 3. MS-d-2 -> OG-rl-1 (transcript + mail tools, two headless routes) -- MISSING (prerequisites)

What exists: OG-tx-1 is on CLOUD. ml-1, hr-1 and hr-2 have 0 code. hr-1 is blocked on Z-W16-S1, now answered by PRD
v1.3 but not yet amended into the order.

Mismatches:
- (a) **The host role cannot read the new bearers.** `simulate-principal-policy` for `opal-gateway-role`
  `secretsmanager:GetSecretValue` returns implicitDeny on `gateway/transcripts/bearer-*` and on `gateway/mail/bearer-*`.
  The positive control, the live `opal/mcp/ms-ingest-token-mXFTKk`, returns `allowed`. The existing bearers are granted
  per exact ARN (`ms-ingest.tf`, `graph-read.tf`). So PHASE A step 4 WILL stop with a BLOCKING row (C11).
- (b) The hr-1 and hr-2 commits are authored on CLOUD's `server.py` and `config.py`, which carry MDPF_TAXSMA TX-g-1
  and NFRA_OPALAI OA-e-10 hunks. Applying them "by diff" onto the live tree conflicts at the route list and must not
  drag either payload (C5).
- (c) ac08 becomes 55 + 3 + 2 = 60 on the tree; host tools 60 -> 65 (C3).
- (d) `pypdf` installs on the host through the deploy's existing `pip install -r requirements.txt`.
- (e) The Z-W17-S1 rotation has no carrier (C9).

Close: (1) The issuer amends hr-1, hr-2 and rl-1 to v1.3. (2) Build tx-1 flip -> ml-1 -> hr-1 -> hr-2. (3) Cut ONE
IAM cell now: exact-ARN reads for the two bearers plus the Z-S24 roster secret, one targeted `safe-apply`, TF act #2,
applied before PHASE B. (4) OG-rl-1 carries the Z-S24 script change and the Z-W17-S1 rotation, so every later release
needs no off-repo hand-off.

### 4. OG-rl-1 -> G-RDR release (MCPINDEX) -> MS-dn-1 (the Deny) -- MISSING

What exists: `e1z.AC1.sh` run on CLOUD 10fb014ec5 now reads `s3 call sites scanned=20 portal-v2 reader files=3
unrouted=2` (`integrations/opal_discover/integration.py`, `integrations/portal_index/integration.py`), `verdict=NO`.
`query_v0` is routed (MS-ir-2).

Mismatch: G-RDR has no issued order. MS-dn-1's AC3 is a SERVED proof, so the routing must be RELEASED to the host,
not just merged. MX-r-7 adds `etfs_get_positioning` inside `portal_index`, which widens what an early Deny would
break.

Close: 2.0.0_SA_COO~MI cuts the G-RDR build (route both readers through `INTERNAL_READER_ROLE_ARN`) and a release on
OG-rl-1's ref. Then MS-dn-1 applies the Deny (TF act #3) with AC1 reading `unrouted=0`.

## Collisions (C1-C12)

- **C1 -- the `.env` printf is ONE physical line.** MX-r-7, MS-d-2 and OG-rl-1 (plus Z-S24) all edit it, so every
  cherry-pick conflicts. Rule: hand-merge onto the LIVE line, and the ANNOUNCE prints `.env` KEYS before and after
  (prior keys + own keys, nothing lost).
- **C2 -- the principal rosters.** CLOUD's `deploy-to-ec2.sh` lacks the OG-t-2 guard and render, because they live on
  the release branch only. A CLOUD-sourced script or printf silently drops both keys. Interim: values off-repo from
  2.0.0_SA_COO~O for releases 1, 2 and 4. End state: the Z-S24 secret, landed by OG-rl-1.
- **C3 -- the ac08 hard count.** The live tree pins 53 (test registry, which excludes Schwab). CLOUD pins a cumulative
  58 (+BD, +t-10, +tx-1). Each narrow tree sets live + own: MX-r-7 55, OG-rl-1 60. Host tool counts: 58 -> 60 -> 65.
- **C4 -- one Terraform state** (`infra/aws/terraform/opal-gateway`). Acts in order: #1 MX-r-7 BD role create, #2 the
  OG bearer + roster read grants, #3 MS-dn-1 Deny. Each is targeted and never concurrent (state lock).
- **C5 -- CLOUD carries two unreleased foreign payloads** in `server.py` and `config.py`: MDPF_TAXSMA TX-g-1 (Andrew:
  out of scope) and NFRA_OPALAI OA-e-10 (`_login_allowed_identities`, order complete, no release order exists). A
  narrow release must exclude both by content. A whole-CLOUD release would ship both.
- **C6 -- live-only bytes absent from CLOUD:** `deploy/NFRA_OPLGTW_CONTRACT.json`, `tests/test_schwab_host_inputs.py`,
  the Schwab `aws_roles`/`integration` edits, `conftest`, the runbook. Cut-at-live keeps them. A CLOUD-sourced tree
  ships `.env` pointing at a missing contract, and the Schwab tools fail closed. The back-merge to CLOUD is owed by
  2.0.0_SA_COO~MI; it does not change the order.
- **C7 -- shared app files:** `tools.py` (OG-tx-1, OG-ml-1 vs the live MX-r-6/OG-t-2 edits);
  `data_entitlement.py`/`destructive_ops.py` (OG vs MX-t-13/t-10); `DATA_CATALOG.yaml` (MX ~15/~21 on CLOUD vs ~19
  live).
- **C8 -- G-RDR is unissued** (above). MS-dn-1 cannot pass AC1 or AC3 without it plus a release.
- **C9 -- the Z-W17-S1 rotation** ("at the next gateway release", CTO ruling 2) is in no order. The next release is
  MCPINDEX's. Put it in OG-rl-1 (the row is OPLGTW's) with that bearer's consumer list named.
- **C10 -- MS-r-1's amendment is not on any branch.** `git log --all` on `tests/test_deploy_base_guard.py`
  shows only MX-r-6's guard commits (newest 42c52ed4d9); there is no fixture fix on any ref. The worker's worktree `C:/tmp/ms-6` lacks the R-4 merge ae2bceeeda and has no python resolver,
  yet its proof (@c740481308) records AC1-AC3 PASS "on worktree edits". The lane gate that refused the commits was
  fixed @4daa5094ae, so the work is re-doable now. A real site-Z deploy is unaffected (`jq` resolves on PATH); the 6
  suite failures are rig-only.
- **C11 -- the host role cannot read the new bearer secrets** (simulation above). This is predictable today, not a
  PHASE A discovery.
- **C12 -- MS-d-2 names no never-widen halves.** OG-t-2 and MX-r-6 carried CTO + CVO (or COO) halves for the same
  host. A CTO call.

## Recommended release order (shortest safe, from served d61fde4693)

0. **Now, no host act, in parallel:**
   - the OG-hr-1/hr-2/rl-1 v1.3 amendment and the OG builds (tx-1 flip, ml-1, hr-1, hr-2);
   - the MS-r-1 redo;
   - cut the C11 IAM cell (two bearers + the roster secret);
   - 2.0.0_SA_COO~MI cuts G-RDR.
   MX-s-14 runs independently throughout. MX-r-6's J1 runs whenever Alyssa is available.
1. **MX-r-7** on d61. It is the only release whose builds are complete today, and OG-rl-1's own hand-off condition
   already puts it first. TF #1.
2. **MS-d-2** on MX-r-7's ref, once MS-r-1 lands and the C2 amendment is in. It is smaller and nearer-ready than
   OG-rl-1, and the Deny chain needs it.
3. **OG-rl-1** on MS-d-2's ref, after TF #2 is applied. It carries Z-S24 and the Z-W17-S1 rotation. From here, no
   release needs off-repo values.
4. **G-RDR release (MCPINDEX)** on OG-rl-1's ref, which needs no hand-off.
5. **MS-dn-1** (TF #3, no host deploy) once AC1 reads `unrouted=0` on the served tree.

If OG-rl-1 is ready before MS-d-2, swap steps 2 and 3. The guard enforces the re-cut, and C2 then applies to MS-d-2
only until OG-rl-1's Z-S24 lands. Steps 1-4 each re-read the live ref at PHASE A and immediately before the upload.
