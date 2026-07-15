# 0.6.2_AE_PartnerETL -- 0833 parity CERTIFIED (leg-4 closed), Glacier 257 + C3 closed, box-guard deployed, three Andrew-direct dispatches discharged (frontier / standardization / Door-5 brief)

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, VALIDATE, COORDINATE, SCRIBE
**Date:** 2026-07-15 | **Window:** ~16:2xZ (log 508fc3485) -> ~19:5xZ | **Serial:** 0.6.2_AE_PartnerETL

## Summary

Five commits + one IAM tag; the schwab S1 leg CERTIFIED; three Andrew-direct dispatches landed
same-window. Everything below is committed and pushed; the lane is fully event-gated at close.

- **0833 PARITY -> CERTIFIED.** The quiet ratchet's oracle fired at invoke 20 (completing sweep
  20260715T181504Z-64a7e1f5). Verified on the SERVED manifest: ok=true, shortfall_pre 344 ->
  shortfall_post 0, surplus_post 0, collisions_post 0, holes_named [tcf,tcfx,tnn], DLQ 0. RAVC sent
  182806Z; CTO CERTIFIED on his independent read (183017Z; his 8,452-listing tie exact). Schwab leg-4
  / WS-A1 S1 leg CLOSED; the one-motion v0.16.0 swap + 10240->3008 GO went to 0.7.0 (AC-2 discharged).
- **DS review of delta-6:** ACCEPTED zero-changes (170032Z, at-source + independent suite 208+7 +
  own-hand vendored parity). Canonical stamp of the chunking-arch doc now pends ONLY my AC-1
  post-swap runtime number.
- **GLACIER 257 COMPLETE + C3 CLOSED** (COO idle-capacity dispatch 170053Z, Andrew-direct): thaw was
  done (expiry 07-29); TWO remap-script defects found+fixed at execution (restored-visibility -- a
  restored object lists GLACIER forever, fixed via listing RestoreStatus attr; per-master conditioned
  dst listing) @ 83c81bae5 -> 257/257 copied + 3-TIER verified (246 ETag single-part, 11 multipart
  streamed-MD5), all H1-attested 08242234. PreFloorRestore grant REMOVED per its ruled closure step:
  plan 0/1/0, safe-apply, 0-diff, tag schwab-si2-iam-v1.5.0; simulate s3:RestoreObject on the exact
  key = implicitDeny, positive control s3:GetObject SEPARATE invocation = allowed. C3 TO closed on
  evidence @ 5b0191d13 (all 8 ACs). COO accepted 174012Z; CTO accepted + RULED the follow-up:
  PreFloorRawRead/RawList removal APPROVED, sequenced POST-TONIGHT (my task board).
- **ANDREW-DIRECT 1 -- 07-10-frontier check** (COO 181941Z + CTO evidence shape 182145Z): artifact @
  195653e85. Hypothesis REFUTED w/ mechanism: opal-assets-ingest-mirror ENABLED, fired clean today
  (CW 2 invocations 0 errors), EXACT set parity dst==src (orion 4,640/4,640 gz; eclipse 624/624);
  frontier = the upstream INF raw producer dead UNDER THE HOLD (census discriminator: raw stops 07-10
  while parquet runs to 07-15 in the SAME prefixes). 3 trading days per lib/trading_calendar.
  Accepted by COO (relayed to Andrew) + CTO (folded into the cert matrix); both census smells
  closed-as-known by COO (the perf/txn parquet stop = the deliberate LEG-2 cutover).
- **BOX-GUARD DEPLOYED** (parity condition met, CTO-approved motion order): guarded sdd-daily-pull.ps1
  (c03a8529c vintage confirmed clean) uploaded to s3://opal-data-schwab/_ops/canonical-schwab-si2/
  with --sse AES256; landed listing ETag 0017f9b549ca9f8013704f50c4327bed == local MD5, 35,842 B
  (replaced the 30,017 B unguarded copy). First-fire watch Monitor armed (emits [BOXGUARD FIRE] on
  07-16 meta/pulls manifests or [BOXGUARD MISS] at 12:00Z). V2-2 closes on the fire evidence.
- **ANDREW-DIRECT 2 -- standardization mandate** (my terminal ~18:4xZ, two messages, verbatim
  recorded + broadcast): coverage sweep = 10/10 monolith bronze trees wired (run-time enumerated;
  the <=07-10 class is exactly the two held INF channels; pathfinder/filepoint feeder = open cell);
  LOAD-BEARING census find: TWO scheduling services live (Rules + Scheduler; smartx invisible to
  rules-by-target). BRIEF issued to CTO @ 20b52be25 (six axes: medallion law, trigger grammar
  {unit}-{function}-{cadence} + trigger-map.json + absence-twins, lambda/chunking, EC2
  telemetry/right-sizing/autoshutdown, TF protocol doc, repo registry+INDEX standard). CTO RATIFIED
  all six axes; OPAL_STNDRD spawned under 0.7.0_AE_CloudOps~Z (Andrew spawn word); census-script
  handoff completed 193430Z (script pasted whole -- scratchpads evaporate; ~Z verified against
  OPAL_STNDRD.json before handoff).
- **ANDREW-DIRECT 3 -- Door-5 brief for DS~B** (~19:3xZ): reviewed OPAL_GLDRNS.B1 (strong on
  stamp-order/Door-6/frozen-3; silent on Door 5's live mechanism + the deploy-authorization
  look-in-scope trap). VERIFIED Andrew's hypothesis on the bytes: the ENTIRE gold-vs-silver
  build_assets_dim.py diff is ONE comment block dated 07-10 -- an advisor-of-record TODO (Noel
  Soderblom ~61 AoR mover accounts dropped on reactivation; advisor_key.isin allowlist = Rule-17
  violation; cites lib/inflection_rep_scope.py + INF_C_07/INF_B_00 re-key). So the silver copy is
  the NEWER LOAD-BEARING annotation, not junk -- de-collision design input BANKED by CTO. Brief @
  53a0db73a; DS~B ACKed all four bindings 194317Z, their day-0 instrument reads independently agree
  (ETags differ = Door 5 shut; chokepoint held; Door 6 sentinel at baseline).

## Deployment Sequence + Verification (AE role addition -- actual outputs)

1. TF: PreFloorRestore removal -- `Plan: 0 to add, 1 to change, 0 to destroy` -> HALT_ACK=1
   safe-apply -> post-apply `no differences` -> tag schwab-si2-iam-v1.5.0 pushed.
   Simulate: `{"action": "s3:RestoreObject", "decision": "implicitDeny"}` /
   positive control (separate invocation): `{"action": "s3:GetObject", "decision": "allowed"}`.
2. S3 code deploy: box-guard -- landed `{"etag": "\"0017f9b549ca9f8013704f50c4327bed\"", "size": 35842}`
   == local md5 0017f9b549ca9f8013704f50c4327bed (single-part; ETag==MD5).
3. Glacier remap execute -- `copied 257 / skipped 0 / failed 0 / accounted 257`; verify
   `set 257/257, size 257/257, ETag 246 single-part, MD5 11 multipart`.

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| aws events describe-rule / list-rule-names-by-target (x8) | trigger census, frontier check + coverage sweep | grounded; found the bd49f/etf naming exhibits |
| aws scheduler list-schedules | the OTHER scheduling service | 8 schedules; the rules-only blind spot MEASURED (smartx) |
| aws cloudwatch get-metric-statistics | mirror invocation evidence | 07-15: 2 invocations, 0 errors |
| aws iam simulate-principal-policy (x2, one-ARN + separate control) | AC5 removal evidence | implicitDeny / allowed |
| terraform plan/apply via safe-apply + 0-diff | PreFloorRestore removal | 0/1/0 -> clean |
| S3 census scripts (frontier_census.py, ingestion_coverage_sweep.py) | per-suffix max-date discriminator; 10-tree sweep | the raw-vs-parquet signature; 10/10 wired |
| lib/trading_calendar | NEVER#1 frontier math | trading_days_behind(07-10)=3 |
| diff (gold vs silver build_assets_dim.py, read-only pulls) | verify Andrew's AoR hypothesis | CONFIRMED: one AoR TODO block is the whole delta |
| commit-gate | remap-script edit | clean |

No comp-* graph tools this window -- deliberate: all three dispatches demanded LIVE primitives per
their evidence shapes (Rule 22a; the CW/simulate/scheduler reads ARE the deliverables), and the one
code edit (remap script) is a leaf with no graph consumers beyond its own leg.
**What worked:** the per-suffix census discriminator (raw .gz vs .parquet max dates in the SAME
prefixes) -- one listing answers wiring-vs-upstream definitively. **What failed/caught:** (a) the
remap script's frozen test read all 217 THAWED objects as uncopyable (restored objects list GLACIER
forever) -- the listing-native RestoreStatus attr is the fix; (b) rules-only trigger enumeration
reads Scheduler-driven lambdas as unwired -- both banked into OPAL_STNDRD. **Gap:** pathfinder/
filepoint feeder unidentified (open cell, may resolve with tonight's ETF cutover -- CTO's read).

## Blockers

None. All remaining work is at event gates (below).

## MCP traffic

~14 in / ~12 out. Significant: CTO leg-4 CERTIFICATION 183017Z + one-motion GO to 0.7.0; CTO
follow-up ruling 174141Z (RawRead/List removal, post-tonight); DS zero-changes review 170032Z; COO
idle-capacity dispatch 170053Z + item-3 re-route 170326Z + RAVC-close accept 174012Z; CTO frontier
accept 183827Z; OPAL_STNDRD ratification + ~Z handoff 193430Z; DS~B Door-5 ACK 194317Z + CTO banked
design input 195126Z.

## HANDOFF -- NEXT SESSION (zero context assumed; read this first)

**Identity/startup:** serial 0.6.2_AE_PartnerETL; /watcher first (LD-0290 serial file; the inbox
Monitor + the box-guard watch Monitor BOTH die with this session). Check for orphan
inbox-watch/ratchet bash children from session a4191bac before arming (the /clear boundary orphans
detached children -- this session reaped three such pairs at startup).

**EVENT DUTY 1 -- AC-1 runtime confirm (RE-SHAPED by CTO push-forward 203538Z):** THE SWAP IS LIVE
-- grounded 20:4xZ: opal-assets-silver-schwab memory=3008, NEW CodeSha yMma9jOm..., modified
2026-07-15T18:40:47Z (0.7.0's one-motion, applied version v0.17.0 per CTO). EARLY AC-1: tonight's
21:45Z/22:15Z schwab box fires convert fresh files at 3008 -- read the converter's CW REPORT
max-memory-used for those invocations and send the NUMBER to 1.0.0_SA_CTO (0.7.0 has the same note;
ONE of us reads it, CITES the other -- coordinate). The heaviest-unit stamp confirm (rlu-class real
S3-event invoke on schwab/08335338/bronze/rlu/20260109/...RLU.zip, 298,507x82) remains the CANONICAL
leg. PASS = <3008 w/ headroom (planning ~1,036MB); FAIL -> STOP + CTO gate, no reflex resize-up.

**EVENT DUTY 2 -- box-guard first fire (CORRECTED: TONIGHT 21:45Z/22:15Z, not tomorrow):** the si2
cron is 9,21/10,22 -- the guarded puller's TRUE first fire is the EVENING pair tonight. Watch v2
armed this session (Monitor b0hzalwsl; script boxguard_watch_v2.sh in scratchpad a4191bac --
session-mortal, re-author on relaunch): baseline-diff poller on schwab/{master}/meta/pulls/, emits
per NEW manifest, [MISS evening] flag 23:30Z, runs through the 07-16 morning pair to 12:15Z. On the
fire: read the per-pull manifest verdict (guard: shortfall+surplus+collision on FRESH ListObjectsV2)
-> V2-2 four-column cite table (both masters, live primitives) -> RAVC-4 to 2.0.0_SA_COO -> close
V2-2 TO. NB tonight's evening fire = guard's first fire AND the swapped converter's first natural
event fire in one window -- the AC-1 early read (duty 1) covers the converter half; the guard
manifest covers the puller half; read BOTH before calling either clean.

**EVENT DUTY 2b -- NEW (CTO push-forward 203538Z): Wave-1 projection duty = the c04 gate, UN-PARKED.**
The same-lambda-pass emission of dim_position/dim_transaction/dim_asset beside their facts
(projection law verbatim) is now the LAST GATE on c04 (the recon guard; DS's a00/a01 live runs open
tonight at the flip). NOTE TO SCOPER: the schwab converter ALREADY emits Wave-1 projections
per-chunk since delta-6 (schwab_projections.PROJECTIONS: dim_position/RPS-s1, dim_transaction/TRN,
dim_asset/SEC, dim_balance/RPS-s2) -- so SCOPE means: read the c04 gate definition + contract SS7
cells against what is deployed, identify the actual delta (contract edit? another family's
converter? certification evidence?), and design it. Tonight if the queue allows, else first thing
tomorrow. Deploy rides the normal cycle.

**EVENT DUTY 3 -- post-tonight IAM cleanup (CTO-APPROVED 174141Z):** remove PreFloorRawRead +
PreFloorRawList from opal-schwab-monolith-remap-role (infra/aws/terraform/canonical-schwab-ec2/
monolith-iam.tf). Same form as v1.5.0: commit-before-apply, plan 0/1/0, safe-apply, 0-diff, tag
v1.6.0, simulate deny (one-ARN) + SEPARATE positive control = s3:PutObject on
arn:aws:s3:::opal-data-assets/schwab/08242234/bronze/x (MonolithSchwabWrite remains). Post-removal
the role is write+list-monolith only. Sequenced AFTER tonight's parity-path legs clear.

**STANDING STATE:** schwab family COMPLETE + both masters PARITY-CERTIFIED (0824 @ 125927Z, 0833 @
183017Z). Delta-6 n=2 reviewed (DS zero-changes + CTO). Glacier/C3/frontier-check/standardization-
brief/Door-5-brief all CLOSED-ACCEPTED. OPAL_STNDRD is 0.7.0~Z's (my census script handed off).
DS~B drives the inf AoR chain (GLDRNS.B1) -- I answer monolith/mirror-side questions, never touch
the inf estate. Never-summed 0824/0833 binds any platinum-shape work. Door 5/2/6 + frozen-3 + the
stamp-order trap: see BRIEF_DSB_DOOR5... @ 53a0db73a for the compact current statement.

## Next Steps

- **[0.6.2 self]** the three event duties above, in whatever order their gates fire.
- **[1.0.0_SA_CTO]** receives the AC-1 number (canonical stamp leg ii); rules on the OPAL_STNDRD
  decomposition; owns the eventual Door-5 open staging (design input banked).
- **[0.7.0_AE_CloudOps]** applies the one-motion swap+resize on the GO already issued.
- **[0.7.0_AE_CloudOps~Z]** owns OPAL_STNDRD Z1 (trigger-map census + registry + CI gate).
- **[0.4.0_DS_ClientPlatform~B]** GLDRNS.B1 inf AoR drive, briefed + bound on the doors.
- **[2.0.0_SA_COO]** receives V2-2 RAVC-4 on the first guarded fire.
