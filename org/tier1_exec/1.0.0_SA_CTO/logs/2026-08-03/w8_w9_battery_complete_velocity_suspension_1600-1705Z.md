# W8/W9 ordered and W2 battery closed; NFRA_VELOCITY suspended for RCG; three arch-gates in one day

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, SCRIBE

Continues `w1_refutation_etfs_final_deliverables_and_rulings_1450-1600Z.md`. Window 1600-1705Z.

## MDLP_MONPUB arc (continued)

- **W4 promote GO issued** (160441Z) after live-verifying W2 on the Lambda myself (LastModified
  15:46:38Z, 05dcbe7651 via yang-v2.4.17) -- 5 conditions incl. trigger-path-only + pinned
  post-publish expectations. **Recovery PUBLISHED 16:10Z** (exec 20260803_v2-c2ea0112);
  **CVO witness PASS x7 VALUES-READ** (@b16913d35e, all 10 periods vs sitez's pinned table to
  2dp). **Serve HEALED at true T-1 2026-07-31.** W1 closed complete-as-superseded @1ab18def94.
- **Pinned-expectation lesson applied to myself:** my GO named "sitez's preview" -- numbers
  nobody receiving the criterion could read. Routed the actual table (MSTR 161104Z) to CVO+me;
  generating script @12a17b857.
- **W2 BATTERY COMPLETE 4-of-4** (CVO @ff496d7621 legs A/2b live + @9ba99fcb5c leg C scratch;
  passing leg = W4 publish + organic 16:21:45Z user pull). TO marked WITNESSED-COMPLETE with the
  as-exercised table. CVO's leg-C control was BOUND to the scratch bucket via invocation log --
  the discriminating detail vs leg A's identical refusal message.
- **W5 deployed + accepted** (hex-sort rollback picker; exec-5a4149176fb6 absent->present
  differential, 133-vs-20 denominator). **W3 deployed + differentially exercised** earlier.
- **W8 ordered, code closed same hour** (4024664d71): DT's grounding found rollback has TWO
  paths -- guard blocks only the re-processing FALLBACK (force_publish grep 0 in data_refresh);
  the PRIMARY version-based path is raw S3 copies = residual R2's class source-located INSIDE
  our own feature (:1318-1328), ruled out-of-scope/unguardable (DDB record is its control).
  Rulings: coherent-vintage semantics (estate-wide regeneration IS a fallback rollback's
  meaning); negative control required (normal publish still refuses post-plumbing); CVO's
  entry-point requirement (both W8 legs through handle_rollback end-to-end, never direct-invoke)
  mechanized INTO the TO acceptance. DS's implementation verified the manifest channel is the
  only SFN-reachable one (top-level flag would be silently dropped) + fixed a latent
  trigger-before-data listing race by writing manifest LAST.
- **W9 ordered via COO -> AE~F** (CVO Andrew-direct audit): /api/general/* cache policy
  DefaultTTL is 86400 -- the 5-min TTL exists ONLY via the cache-control-injector stamping
  max-age=300; injector failure = silent 24h edge caching. Fix = custom policy (managed is
  immutable) + targeted swap, blast-radius denominator BEFORE TF. W6 re-weighted watched-priority
  per Andrew's 1641Z emphasis (via CVO).
- **Trace corrections recorded** (spec 5b): .ST = UNGATED RACE between two Bloomberg custom
  indices answering the ambiguous bare ".ST" (correct YBH:2238 vs deprecated ~2021 predecessor,
  Yang deleted his side 16:32Z), ACCOUNT-SCOPED TO ALYSSAAKEITH; producer dup-append >=7 months
  old (Dec 70 / Mar 62 dups) -- crash recency = build_rfr_daily is newer; -4003 = consumption
  review, unrelated. **PARSEKEYABLE_DES pin fix TESTED but HELD at Yang's explicit request --
  NO-AGENT-PUSHES recorded.** Consequence surfaced to Andrew: W7 (content gate) is now the only
  candidate MECHANIZED defense against a confirmed randomly-firing mechanism.

## Governance

- **Three arch-gate PASSes** (all independently grounded before ruling): DS into
  YANG_PIPELINE_DEPLOY + DATA_REFRESH_DEPLOY (permanent-scoped, @46d4b1110d); TF-root path rule
  infra/aws/terraform/data-refresh/** (@ac778cbbcd); yang SOURCE path rule
  infra/aws/lambda/v2_portal/yang_pipeline/** (PASS 170310Z, COO landing). Three
  override-for-a-standing-role instances in one family, one day.
- **NFRA_VELOCITY SUSPENDED (temporary)** -- two Andrew-directs: 1612Z hold (MSTR record) +
  the CRO-terminal verbatim ("effectively suspend (temporarily)... we need to figure out the
  RCG first"). Executed: both project JSONs On-Hold + open-work ledgers, REGISTRY rows moved,
  **NFRA_REPOCOHERENCEGRAPH PRD landed canonically** to docs/architecture (ANY_CTO lane).
  Timing reasoning vs COO's wait-for-GO read, reconciled by message: the suspension is effective
  on utterance; the spec GO gates the RCG BUILD (CRO asks 3-4 wait there).
- **SURFACE_ACK unauditable-diligence seam** banked as gate candidate (COO observation).
- COO items closed: sweep-fix TO @89def67d27 (record-terraform-deploy whole-file sweep);
  R4-A self-demonstration (4 fresh token-sweep findings incl. 2 nonexistent projects --
  discriminating fixtures for ~B's fix).

## Compiler Tools

| tool | result | note |
|---|---|---|
| `aws lambda get-function-configuration` (live) | PASS | W2 deployed-verify BEFORE issuing W4 GO -- tag alone is not deployment |
| `grep` on .owned-paths.yaml (x3) | PASS | independent grounding for all three arch-gates; # rail-checked implicit: single-file config reads |
| `head-object`/body (live, several) | PASS | serve-state pins through the arc |
| comp tools not otherwise run this window | -- | window was coordination/witness-validation; grounding was live-AWS + file reads at cited vintages |

## Current State / Next Steps

- [DT+DS+CVO] W5+W8 joint data-refresh deploy cycle -> W8 scratch legs (handle_rollback
  end-to-end, held env) + W6 mechanical exercise -> CVO witnesses; live W6+W8 legs ride the next
  genuine rollback occasion.
- [AE~F] W9 TTL hardening (custom policy + targeted swap, denominator first).
- [ANDREW] W7 content-gate decision (now the sole mechanized-defense candidate vs the .ST race);
  Yang pin-fix timing (his call, held); Bloomberg review; RCG spec GO (gates the build + CRO asks
  3-4); VELOCITY resume word.
- [1.0.0_SA_CTO] event-driven: W8/W6 witness evidence, RCG build arch-gates when GO'd.
