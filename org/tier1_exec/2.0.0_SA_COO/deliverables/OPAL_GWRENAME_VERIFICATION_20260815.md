# OPAL_GWRENAME -- COO independent verification record (TO-2)

**Verifier:** 2.0.0_SA_COO. **Executor:** 0.7.0_AE_CloudOps (TO-1). **Spec:** runbook @433454738b.
**TOs issued:** @8dfa20c274. **GW-6 cold-login amendment:** @8386ce43c3 (MSTR 015746Z, adopted 015822Z).
**Principle:** my verification shares no derivation with AE's. Live primitives only; AE reports are
claims, not evidence. Interpretation tables are pre-registered BEFORE the evidence exists.

## Pre-flip baselines (all 2026-08-15, BEFORE any live-plane change)

| # | What | By | When | Result |
|---|------|----|----- |--------|
| B1 | Warm whoami via mounted opal-gateway MCP (`mcp.opalinvest.dev/mcp/`) | COO (this session) | ~0156Z | PASS -- Graph payload: displayName "Andrew Berman", mail Andrew@opalinvest.com, odata context graph.microsoft.com/v1.0 |
| B2 | Warm whoami, same path | MSTR | 015830Z | PASS -- same payload shape. Full chain alive: ALB -> listener -> target -> gateway -> Graph |
| B3 | COLD OIDC mount, known-good state (positive control for the discriminator) | COO seat spawn ~0152Z; AE seat spawn ~0152Z | pre-flip | BOTH succeeded -- proves a cold mount PASSES when the gateway is healthy, so a post-flip cold-mount failure cannot be dismissed as "fresh mounts are flaky" |

Gateway is HEALTHY end-to-end going in: any post-flip failure is attributable to the cutover.

## GW-6 interpretation table (pre-registered, MSTR 015904Z, adopted verbatim)

| Post-flip observation | Verdict |
|---|---|
| Cold mount succeeds + whoami returns Graph data | H1 genuinely closed |
| Cold mount FAILS, or mounts but whoami errors | H1 LIVE -- OIDC secret not re-set on the recreated listener |
| Warm sessions still fine but cold fails | H1 LIVE and MASKED by pre-flip tokens -- the row the amendment exists to expose |

Warm-session calls post-flip are REGRESSION checks only, recorded as
"warm call OK (non-discriminating)". A warm PASS is never GW-6 evidence: warm sessions hold
bearer tokens minted before the flip, and H1 is exercised at LOGIN.

**Plan of record for the cold read:** MSTR spawns a throwaway fresh seat at S4-complete
(COO calls for it); the seat's cold MCP mount + first tool call is the acceptance instrument;
seat killed immediately after.

**TABLE SUPERSEDED 0300Z -- TWO INDEPENDENT DERIVATIONS OF THE SAME MECHANISM (MSTR 025946Z
live listener-rule read; COO 0259-0300Z uvicorn-401 + alb.tf source read, made BEFORE reading
MSTR's message):** listener rule prio-10 forwards `/mcp`,`/mcp/*`,`/authorize`,`/register`,
`/token` with NO authenticate-oidc -- the gateway runs its OWN app-side OAuth server, and ALL
MCP traffic bypasses the ALB OIDC action. COO's unauth GET to /mcp/ returned 401 with
`server: uvicorn` + MCP-spec `www-authenticate: Bearer resource_metadata=...` -- the app
answered, proving forward-without-ALB-auth; AE's 302 was a default-action path; both reads
correct, different rules. **Therefore NO MCP call -- warm or cold -- can see H1.** Re-scoped
evidence design (MSTR's correction, COO concurred):
- COLD SEAT still runs at S4-complete, re-scoped to the claim it actually tests: A NEW AGENT
  SESSION CAN MOUNT AND USE THE GATEWAY (the operational bar for every seat spawning
  tomorrow). It is NOT H1 evidence.
- H1 (ALB default-action client_secret): blast radius = interactive/browser access to
  non-rule paths ONLY; no agent path uses it. NOT headlessly testable; NO config oracle
  (describe-listeners omits ClientSecret by design, MSTR-checked). Census grade: "re-set
  CLI act performed (DESIRED-state evidence); not independently verified; blast radius
  named; APPLIED truth requires a real browser login." NEVER "H1 verified" off an MCP call.
- Two claims, two evidence grades, stated separately -- never blended into one green.

## Stage verification log (COO independent reads)

- S1 (additive): **VERIFIED-INDEPENDENT (COO), 0201Z.** GW-1: my own live read -- 4 of 4
  secret pairs sha256-MATCH (aws CLI pipeline, values never printed; my absolute hashes differ
  from AE's boto3-derived ones because the pipelines differ -- the old==new equality holds on
  BOTH instruments, and the differing absolutes evidence genuinely independent derivation).
  GW-2: my own recursive listings materialized client-side -- 38 of 38 relative keys present,
  size-identical, diff clean.
  **CENSUS ADJUDICATION (COO, acceptance-bar holder): 36 of 38 blobs inside the NEW prefix
  retain m365-*.tar.gz basenames (version history). DECLARED EXCEPTION -- retained, not pruned:
  (a) pruning inside the new prefix is NOT a runbook-named act and S3 object deletion is
  Andrew-reserved, so it is out of tonight's authorization; (b) the census surfaces are
  live-plane resource NAMES -- history blob basenames are content, not a live surface;
  (c) post-S4 they are dormant history (deploys mint opal-named artifacts). Will be surfaced
  to Andrew in the final report for an optional prune order.**
- S2 (plan-only): **VERIFIED-INDEPENDENT (COO), 0219-0222Z, against the @3e8c3522f1 tree.**
  My own read-only plan re-derivation (`terraform plan -lock=false`, 1,769 lines captured):
  Plan 40 add / 7 change / 35 destroy -- REPRODUCES AE's numbers exactly. STOP-CONDITION
  CLEAR on my instrument: "aws_instance.gw will be updated in-place" (:862), zero
  `forces replacement` lines in its block. 35 must-be-replaced 1:1 with destroys; the 5
  taxsma creates account for the 40-vs-35 delta; `aws_lb_listener.https must be replaced`
  (H1 exposure confirmed real); route53 alias updated in-place (follows new ALB). Diff
  checks: ART + latest literals now DERIVE from $SERVICE (source-read at @a7312b946b);
  producer-regression class closed. taxsma sweep-in: 5 resources enumerated at source,
  both role names ABSENT on my own live get-role reads. COO ruling: sweep-in ACCEPTED
  (additive-only IAM, committed CTO-gated config, -target surgery riskier).
  RESOLVED 022546Z (MSTR ruling, converged): (a) taxsma sweep-in CONCUR -- lands with the
  apply; (b) REVERT @3e8c3522f1 -- MSTR withdrew their 021548Z conditional on the record as
  malformed (a plan verb is a DESIRED-state statement and does not disclose the convergence
  mechanism; an EC2 stop is Andrew-reserved and the reservation binds on the ACT). Andrew's
  stop/start word sought in parallel, explicitly NON-GATING. Unified S3 GO issued to AE 0227Z.
  **CARRIED RESIDUAL (census + close report, verbatim):** "user_data still references m365
  paths; TRIP-CONDITION: any future instance replacement first-boots against the old /opt
  path and, post-S6, a DELETED S3 prefix -- must be fixed as part of any deliberate
  replacement act."
  **PRECONDITION recorded against any FUTURE approved stop act (MSTR 022546Z):** a stop/start
  assigns a new PUBLIC egress IP (no EIP); Entra Conditional Access has NOT been verified free
  of IP-restricted policies, so a new egress IP could break Microsoft auth in a way that
  MIMICS H1. Checking Entra CA is a precondition of the stop, not a follow-up. Scope note:
  tonight's reverted tree has no egress IP change, so this hazard CANNOT contaminate tonight's
  cold-login read.
- S3 (apply + H1 re-set): **INCIDENT MID-WINDOW, ROLL-FORWARD IN FLIGHT (025105Z-).**
  Apply #1 rc=1: default destroy-before-create deadlocked on the SG replacements (old SG
  deletion blocked by the instance ENI; instance cannot swap until the new SG exists).
  Casualty map (AE apply log): 29 creates + 31 destroys landed incl. BOTH old listeners;
  new SGs/ALB/listeners/alias never ran. **COO INDEPENDENT CONFIRMATION 025215Z: curl to
  /mcp/ AND /health both connection-timeout HTTP:000 -- outage total.**
  **PRE-REGISTERED ATTRIBUTION: warm-session MCP failures during this window are THE OUTAGE,
  NOT H1.** COO warm mount deliberately untouched until restore so its regression meaning
  survives. AE decision CONCURRED (COO + relayed to MSTR 025227Z): roll-forward -- CBD on
  both SGs @e0e4c62fba, re-apply running (deadlock is order-dependent, not name-dependent;
  a var.name re-flip re-runs the same order). SECOND CLOCK: old role+profile destroyed
  while associated -- on-box STS creds die at lease expiry (SSM risk); apply-2's profile
  association closes it; any apply-3 is immediate, not deliberated. Ledger OPEN, NEVER#8.
  **OVERTAKEN + CORRECTED 025455Z (MSTR live reads):** IAM plane ALREADY CONVERGED
  (opal-gateway-profile associated; opal-gateway-role full policy set + SSM; old role
  NoSuchEntity) -- the STS/SSM clock was dead on arrival, and COO's dependent "apply-3
  immediate" instruction to AE was EXPLICITLY WITHDRAWN 0256Z. Governs on apply-2 failure:
  MSTR's fork -- no third blind apply; failing resource reported, then -target SERVICE PATH
  ONLY (a NAMED INCIDENT ACT; open item: the reconciling untargeted apply afterward, held by
  COO so the surgery cannot silently become the end state). MSTR independently confirmed:
  both ALBs 0 listeners at their read; new opal-gateway ALB EXISTS as of 0252Z; rollback is
  NO LONGER a restore path (old listeners/rules/WAF-assoc gone). GW-6 bar UNMOVED -- fresh
  listener makes H1 MORE live; post-outage field has no warm-token masking left, so the
  cold test is cleaner than designed. Andrew being notified by MSTR.
  **RESOLVED 0255-0301Z: apply-2 rc=0, SERVICE RESTORED. Outage ~35 min (~0240Z-0255Z).**
  COO INDEPENDENT GW-4 READS (0300-0301Z, live primitives): ALB opal-gateway ACTIVE
  (opal-gateway-616252801...elb.amazonaws.com), 2 of 2 listeners; TG opal-gateway-tg target
  i-07dccb1615503ac99 HEALTHY; WAF opal-gateway-waf ASSOCIATED; instance-profile
  opal-gateway-profile ASSOCIATED; instance SG = opal-gateway-sg; old ALB
  LoadBalancerNotFound + old role NoSuchEntity (both with passing positive controls on the
  live twins). Warm regression whoami: PASS, recorded non-discriminating. GW-5: AE
  modify-listener CLI act cited with ClientId cross-check (DESIRED-grade per the superseded
  table note above). MSTR end-to-end verify at 0257Z concurs. -target fork NOT needed.
- S4 (on-box): **INCIDENT #2 (contained, on-box only, 030611Z):** deploy #2's fresh venv
  pulled unpinned mcp 2.0.0 (requirements `>=1.2.0`; 2.0 removed `mcp.server.fastmcp`) ->
  import crash-loop, TG target unhealthy minutes, ALB plane untouched. AE restore-first
  (old unit green) -> pin mcp==1.28.0 READ FROM LIVE OLD VENV @81615fbd3e -> redeploy #3.
  COO order AMENDED on physical grounds (both units bind :8080): build-while-old-serves,
  seconds swap gap accepted, UNIT + /opt REMOVAL only post-verify (the restore lane just
  exercised). BANKED follow-ups: bare-jq in safe-ec2-deploy.sh + deploy-to-ec2.sh (Rule 16
  class, masked as a manifest error); systemd ACTIVATING-rc=3 wrapper false-negative (fixed
  in-script); unit-file /opt literals (4) caught @90b89562bc -- 4th member of tonight's
  enumerate-some-members class. GW-10 artifact-name evidence CONFIRMED opal-named
  (opal-gateway-90b89562bc.tar.gz + latest). Battery report pending.
- **GW-12 (NEW CRITERION, minted 0310Z, MSTR 030938Z + COO corroboration): ON-BOX RUNTIME
  STATE MIGRATED (.token_cache).** The cache holds per-user Microsoft refresh tokens
  (Fernet-encrypted) -- a HUMAN CONSENT ACT, the one thing on the box that cannot be
  rebuilt from Secrets Manager/S3; deploy artifacts EXCLUDE it by design, so it exists only
  at the old /opt path until copied. MEASURED both oracles: MSTR whoami 0309Z AND COO whoami
  0310Z both return needs_login (20 min after both returned full Graph payloads) -- and the
  COO call REACHING the app (MCP bearer still valid) isolates the loss to the Graph-consent
  state specifically. **S6 IS BLOCKED** until cache copied (not moved, ownership/mode
  preserved) -> new unit restarted -> MSTR's independent whoami returns a REAL Graph payload
  (MSTR is the named oracle; AE's copy-succeeded is not acceptance).
  **METHOD FINDING for the close report: A NAME CENSUS CANNOT SEE A STATE MIGRATION** --
  every name-based check passes right now (zero m365, target healthy, app answering) while
  the gateway is useless to its actual users. 5th member of the enumerate-some-members
  class; general remedy = define the class structurally (AE's $SERVICE pattern), not by
  listing members.
- **SSM CONTROL-PLANE LOSS + NO-REBOOT RULING (0310-0317Z):** SSM agent ConnectionLost
  (likely OOM during back-to-back venv builds on the t4g.nano 0.5GB); COO independent reads
  0316Z: ConnectionLost / instance running ok-ok / TG healthy (gateway serving). MSTR RULED
  NO REBOOT (the copy saves one interactive login; an instance state transition on the box
  holding the only consent-state copy is not spent on a convenience; boot outcome currently
  UNINSPECTABLE because SSM is the thing that is down). **NEW LATENT RISK, OUTRANKS THE
  CACHE (close-report open item with owner regardless of outcome): both units bind :8080
  and may both be systemd-enabled -- an UNPLANNED reboot brings up an UNDEFINED service,
  and the confusing case is the OLD unit winning (it HAS the cache, so auth would appear to
  "heal" while the accepted tree lost).** COO SEQUENCING RULING 0317Z: when SSM returns --
  disable-old-unit FIRST, cache copy second, S6 on-box legs last; if SSM down through
  S5-completion -- GW-12 closes HONESTLY-NOT-MIGRATED (tonight's status, NOT a
  never-migrate decision), S6 SPLITS (cloud-side proceed post-S5 / on-box deferred to AE,
  trip = SSM return, /opt deletion only after cache-migrated+oracle OR Andrew-re-auth).
  **COLD-SEAT INTERPRETATION PRE-REGISTERED 0317Z (before the seat runs): mount + first
  call returning EITHER a Graph payload OR the well-formed needs_login envelope = PASS on
  the new-session claim (needs_login corroborates GW-12, does not fail GW-6); transport/
  auth-plane failure = FAIL.** Banked: t4g.nano undersized for on-box venv builds (cost the
  control plane; Deployment Rule 5 spirit); no SSM-agent restart guard; bare-jq defects.
  **S4 CLOSED 0318Z:** battery members all evidenced by DIRECT on-box reads 0307-0308Z
  (pre-ConnectionLost, not inference across the gap): opal-gateway.service ACTIVE with
  ExecStart resolving the new venv; m365 unit INACTIVE (enable-state DESIRED-grade, is-enabled
  read pinned as first act on SSM return); /health ok on-box + ALB checks 200 both AZs; /mcp
  401 on-box AND through-ALB; md5 9/9 == repo @81615fbd3e; mcp==1.28.0 on-box; GW-10 artifact
  names opal-* on first real $SERVICE run; EC2_MANIFEST manually updated (Rule 8, surgical
  diff, wrapper bind-race fix banked). COO corroboration: TG healthy, through-ALB 401, and
  the COO needs_login read as NEW-TREE DISCRIMINATOR (the old tree holds the cache and would
  have returned a Graph payload). GW-12 DEFERRED-SSM. Cold seat CALLED 0318Z.
- **GW-12 RESOLVED 0322-0324Z:** SSM self-reconnected; AE ran the sequence in ruled order --
  enable-state read FIRST (opal enabled / m365 DISABLED, APPLIED-grade -> the reboot-
  nondeterminism latent risk is CLOSED), cp -a 4 cache blobs (ec2-user:600 preserved),
  restart, active + /health ok. **COO CORROBORATION 0324Z: my whoami returned the FULL
  Graph payload (Andrew Berman / Andrew@opalinvest.com)** -- consent state migrated intact;
  same session read needs_login 14 min earlier, so the flip is the copy. MSTR oracle read
  pending (named oracle; COO corroborates).
- S5 (verify): **CENSUS VALIDATED-INDEPENDENT (COO), 0325Z.** AE census @032047Z (13 cloud
  surfaces, materialized client-side). MY OWN REPRODUCTION, every list materialized to JSON
  and counted in python (no --query length, no --no-paginate): IAM roles 0 of 208 |
  instance profiles 0 of 23 | secrets 4 of 88 (the 4 old m365 twins, S6-SCHEDULED) | ALBs
  0 of 1 | SGs 0 of 23 | lambdas 0 of 195 | log groups 2 of 238 (/aws/lambda/m365-{otp,
  ms-ingest}-liveness, S6-SCHEDULED) | EventBridge rules 0 of 136 | EC2 tags 0 of 6
  (Name=opal-gateway, System=OpalGateway). **EVERY NUMBER REPRODUCES AE's EXACTLY,
  DENOMINATOR FOR DENOMINATOR.** S3 split (from AE, my S1 read anchors the history count):
  old prefix 38 objects S6-SCHEDULED; new prefix 41 = HISTORY 36 (declared exception,
  unchanged) + 3 opal-named artifacts minted tonight + latest = PRODUCERS 0. Non-zero rows
  are ALL S6-SCHEDULED items -- zero m365 on every LIVE surface. Cold seat (GW-6) pending.
  **GW-6 PASS + GW-12 ORACLE PASS (MSTR 033046Z):** GW-12 -- MSTR whoami 0327Z FULL Graph
  payload (same session read needs_login 0309Z); COO 0324Z corroborates; Andrew does NOT
  need to re-authorize. GW-6 -- TWO cold seats BRACKETING the copy: #1 `3.0.0_SA_CVO~V`
  032201Z PRE-copy -> well-formed needs_login envelope = PASS on the transport/auth-plane
  claim ONLY; #2 `3.0.0_SA_CVO~W` 032929Z POST-copy -> FULL Graph payload = PASS on the full
  new-session-with-Graph claim. The pair is a before/after control across independent fresh
  sessions: the flip is ATTRIBUTABLE to the copy, not merely concurrent. **CAVEATS (MSTR-
  disclosed, recorded verbatim):** (a) neither seat registered with the broker -- both seat
  messages carry "Sender-unverified"; mitigation = MSTR-spawned with process-truth checks,
  timestamps match spawns, payloads differ exactly as the copy predicts, #2 matches MSTR's
  own oracle -- three-instrument consistency, no claim rests on either message alone;
  (b) seat #1's PASS is transport/auth-plane only -- never merged with #2's. **S6 RELEASED
  0331Z** with one add: an off-path on-box .token_cache copy retained until the state-key
  migration completes and the cutover is CLOSED.
- S6 (retire): **CLOUD-SIDE LEGS VERIFIED-INDEPENDENT (COO), 0337Z** -- my APPLIED reads:
  4 old m365 secrets carry `DeletedDate` (deletion SCHEDULED with recovery window, NOT
  forced); 4 new opal-gateway secrets present (positive control); old prefix
  ec2/m365-mcp-gateway/ = 0 objects recursive vs new prefix 41 (positive control); both
  liveness lambdas live as opal-*. MSTR's independent reads 033552Z concur.
  **EXPLAINED CENSUS ROW (adjudicated at source by MSTR, re-derived by COO): /aws/lambda/
  opal-otp-liveness EXISTS, /aws/lambda/opal-ms-ingest-liveness ABSENT while both lambdas
  are live -- NOT an incomplete apply.** Source: neither otp-liveness.tf nor ms-ingest.tf
  declares an aws_cloudwatch_log_group (0 of 0 in each, my grep); Lambda creates the group
  lazily on FIRST INVOCATION; ms-ingest runs `rate(6 hours)` (ms-ingest.tf:100) and has not
  fired since recreation. Expected resolution: appears on its own at the next scheduled
  fire, no action. Becomes a real finding ONLY if still absent after that lambda's next
  invocation. Recorded so "0 m365 log groups" and "the opal twin is absent" do not read as
  contradictory. Remaining legs at AE: on-box old-tree removal (insurance copy held) +
  state-key migration LAST (backup verified before, 0-diff plan after).
