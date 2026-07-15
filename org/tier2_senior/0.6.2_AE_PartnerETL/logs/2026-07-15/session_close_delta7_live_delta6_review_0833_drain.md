# 0.6.2_AE_PartnerETL -- session close: delta-7 LIVE + exercised, delta-6 primitive reviewed, 0833 backlog draining to parity

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, VALIDATE, COORDINATE
**Date:** 2026-07-15 | **Window:** ~13:1xZ -> ~14:3xZ (since log f1b401b61) | **Serial:** 0.6.2_AE_PartnerETL

## Summary

Since the delta-7-authored log (f1b401b61): delta-7 went LIVE and was exercised on the deployed artifact;
the delta-6 shared streaming primitive was reviewed + accepted; the backlog ratchet crossed from ~44% to
~80% on 0833. The schwab channel is now COMPLETE and production-lawful (deltas 1-7 all shipped+reviewed);
the only open work on Andrew's parity directive is 0833 finishing its drain.

- **Delta-7 (hole-skip) LIVE @ v0.15.0** (0.7.0 apply on CTO's 131611Z GO) AND EXERCISED on the deployed
  artifact: I invoked the live lambda with a real S3-event payload naming the EXACT tnn key that DLQ'd
  yesterday morning (schwab/08335338/bronze/tnn/20260713/...TNN.zip) -> StatusCode 200, NO FunctionError,
  converted 0, manifest ok=true with skipped_holes=[{type:tnn}], zero DLQ. The morning incident is retired
  IN PRODUCTION. CTO ACCEPTED it as the event-path cert leg's exercised evidence (133627Z). Both reviews
  (CTO PASS + DS ACCEPTED) done pre-swap.
- **Delta-6 primitive reviewed** (DS @ 6ff338a21 -> 4cf86b489): lib/stream_parquet.py (ChunkedParquetWriter,
  atomic local-temp -> single put on finalize -> ETag-verify). ACCEPTED -- the atomic pre-write contract
  correctly preserves my CRS T1 tie as a true pre-write gate. I flagged a /tmp ephemeral-storage residual
  (the RSS acceptance was disk-blind); DS closed it with a measured 29.9 MiB peak-disk (6% of 512MB) + an
  explicit disk sampler, and gently corrected my premise (the harness DOES write a real temp; only the PUT
  is faked -- owned). Two nits folded. Primitive is FINAL; I build my CRS iterator on it after 0833 parity.
- **Ratchet consolidated to a quiet driver** (Monitor bkr3c0wfy): drains 0833, notifies ONLY on
  parity-reached / wall / misfire (killed the per-tick notification flood; stopped the redundant selective
  watch).
- Banked COO fabric relay: safe-commit AMENDMENT-2 (@ 3e49134b6) -- a `log(`-class commit deleting
  source/infra now refuses; my log/deploy commits unaffected.

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| aws lambda invoke (live v0.15.0, real S3-event payload) | EXERCISE delta-7 on the deployed artifact + exact incident key | 200 / no-FunctionError / manifest ok + skipped_holes=[tnn] |
| aws s3 (manifest + footer reads) | delta-7 manifest verify; live 0833/0824 counts; largest-parquet /tmp check | grounded all claims |
| aws lambda get-function-configuration | /tmp ephemeral_storage (both converters = 512MB) | residual grounded |
| source review (lib/stream_parquet.py) | delta-6 primitive contract review | ACCEPTED + 1 residual + 2 nits |

**What worked:** exercising the DEPLOYED artifact on the EXACT failure input (not source, not synthetic) is
the sharpest cert evidence -- CTO named it the strongest trigger-confirmation in the certification.
**What failed/caught:** my delta-6 review premise ("write-fake never touched /tmp") was WRONG -- the temp
write is real, only the PUT faked; owned to DS. The catch still earned its keep (drove an explicit disk
measurement where there was an inference). **Gap:** none.

## Blockers

None. All remaining work is at external gates or background: 0833 ratchet completion (running), the
box-guard deploy (sequenced after 0833 parity), my CRS delta-6 wire-up (sequenced after that).

## Current State (ZERO prior context assumed -- the handoff surface)

**THE ONE LIVE THING:** the schwab backlog ratchet is draining lane 0833 to bronze/silver parity, per
Andrew's 2026-07-14 ~18:5xZ verbatim directive (relayed via CTO 185823Z): "proceed with a manual, ad hoc
run of each silver converter ... reach parity between all completed bronze buckets and their silver ...
completely clear on bronze full backfill and silver parity ... then devote full resources to Opal_RUNNERS."

- **Ratchet driver:** `scratchpad/ratchet_driver.sh` running under Monitor `bkr3c0wfy` (QUIET -- emits only
  on parity/wall/misfire). Mechanics: sequential sync `aws lambda invoke {"mode":"sweep"}`, AWS_MAX_ATTEMPTS=1,
  listing-based progress, wall = (timeout/error AND listing-delta<=1) -> stop + sizing proposal. It
  self-terminates with `[RATCHET PARITY]` when an invoke's payload parses with 0833 shortfall_post==0 (small
  backlog -> sweep completes under the 660s read-timeout -> parseable). **If a fresh session finds it dead:**
  relaunch the same script under a Monitor; it resumes from the live listing (idempotent per feed/date).
- **Lane state (live at close):** 0824 = 7,482 silver keys / 7,468 target = PARITY (the +14 = fresh 07-14
  dailies on top; CTO RAVC-4 ACCEPTED-CLOSED 125927Z, manifest-backed shortfall_post=0/surplus=0/collisions=0).
  0833 = 6,728 / 8,436 (~80%), climbing.
- **THE 0833 CLOSE (owed to CTO):** when 0833's completing SWEEP manifest (schwab/08335338/meta/conversions/
  {run_id}.json, trigger=sweep) shows shortfall_post==0, verify it the same way 0824 was verified (read the
  manifest, confirm shortfall/surplus/collisions all 0), then send the per-lane parity RAVC to CTO. That
  closes leg-4 of his parity certification (the OPAL_RUNNERS full-resource gate). 0824 is his banked schwab
  evidence body; 0833 completes it.

**DEPLOYED STATE (all live in prod, opal-assets module, 0.7.0 is the apply vehicle):**
- Converter lambda `opal-assets-silver-schwab` @ **v0.15.0** (delta-7 live), runtime py3.11 / memory **10240**
  / timeout 600. The 10240 is the OOM sizing bump (1658ef5a4, tag opal-assets-v0.13.0) -- **DELTA-6 STREAMING
  WILL RETIRE IT:** once I wire the CRS iterator to lib/stream_parquet.py and pass the 3-dim acceptance
  (RSS/wall/tmp) at 3008 on rlu 20260109, propose schwab 10240->3008 resize-down to CTO.
- Family is deltas 1-7: schemas/reader/conversion/projections/manifest/runtime/set-identity-guard, all in
  `data/assets/scripts/silver/` (vendored FLAT into `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/`
  via `ci/vendor-manifest.sh`; parity 10/10). Suite 176 passed + 7 skipped.
- V2-2(b) meta/pulls IAM grant `MonolithSchwabMetaPullsWrite` APPLIED+VERIFIED (tag schwab-si2-iam-v1.4.0,
  ledger v22b-meta-pulls-grant CLOSED, simulate battery 6/6).

**QUEUED WORK (in order):**
1. **0833 parity RAVC to CTO** -- on the completing sweep manifest (above). LEG-4 close.
2. **Box-guard deploy (V2-2(b) criterion path a-c):** the guarded puller `sdd-daily-pull.ps1` (landing
   guard: shortfall+surplus+collision, verdict on FRESH ListObjectsV2, Die-6 record-then-raise; mutant
   transcripts @ c03a8529c) is COMMITTED but NOT uploaded to the box's pull location
   (s3://opal-data-schwab/_ops/canonical-schwab-si2/sdd-daily-pull.ps1). **Sequenced AFTER 0833 parity**
   (one-variable per fire; a mid-drive box pull perturbs the parity accounting). Deploy = S3 cp; first
   guarded fire (natural tomorrow-morning pull or a controlled SSM trigger) is the RAVC-4 evidence. Given
   it's a $1.7b custody feeder with a new Die-6 path, prefer a WATCHED first fire. Then V2-2 criterion-1
   (four-column cite table, both lanes) + RAVC-4 to COO closes V2-2.
3. **CRS delta-6 wire-up (my delta-6 sibling):** rewire crs_reader/schwab_conversion to stream via
   ChunkedParquetWriter. Sequence: cheap count-pass (D-line counts + ragged check) -> T1 reconcile (RAISES
   before any write, preserving the pre-write gate) -> stream field-split in chunks -> fan-out N writers
   (fact + dims per section, projection law stays my side) -> run DS's 3-dim acceptance harness
   (`scratchpad/measure_delta6.py`) on rlu 20260109 (296,669x82) -> if it passes at 3008, propose the
   resize-down. Design fully aligned with DS (my 132308Z + 132540Z, DS 132456Z/141045Z). CRS dedup goes
   cross-chunk bounded-hash-set (16-byte hash_key gotcha noted). Architecture template @ 988f39914.

**STANDING CONTEXT:** never-summed 0824/0833 (record the identity, never a combined total). The event
path is now clean-by-construction (holes skip loud-in-manifest, pipes convert, unknowns refuse). Delta-5
laws live: 2025-01-09 shell lands 0-row T1_RECONCILED, pre-2025-07-18 rl* NULL-fills the appended pair.
Fire watch retired (fires observed). Andrew typed "court" twice mid-session -- could not resolve it to an
instruction; asked for clarification, none received -- flag if it recurs.

## Next Steps

- **[0.6.2 self]** (1) 0833 completing-sweep -> verify shortfall_post=0 -> parity RAVC to CTO (leg-4 close).
  (2) Box-guard deploy after parity (watched first fire) -> V2-2 RAVC-4. (3) CRS delta-6 wire-up + 3-dim
  acceptance -> 10240->3008 resize-down proposal.
- **[1.0.0_SA_CTO]** receives the 0833 parity RAVC (completes schwab leg-4); the resize-down proposal later.
- **[0.4.0_DS_ClientPlatform]** delta-6 primitive FINAL; the architecture doc's Section-3 /tmp dimension add
  routes through CTO. My CRS diff comes for same-day review when the wire-up lands.
- **[0.7.0_AE_CloudOps]** the apply vehicle for any schwab TF motion (the eventual resize-down).

## MCP traffic

~20 in / ~14 out this window. Significant: CTO (delta-7 swap GO 131611Z, delta-7-exercise ACCEPTED 133627Z,
0824 parity ACCEPTED 125927Z); 0.7.0 (delta-7 v0.15.0 swap-complete); DS (delta-7 ACCEPTED, delta-6 landed
+ /tmp residual closed + primitive final); COO (box-upload-sequencing ACK, safe-commit AMENDMENT-2 relay).
All RAVC loops closed except the pending 0833 parity RAVC (gated on the drain).
