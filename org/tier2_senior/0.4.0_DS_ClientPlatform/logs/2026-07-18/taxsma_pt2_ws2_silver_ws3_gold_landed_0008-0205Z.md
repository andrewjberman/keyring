# OPAL_TAXSMA_PT2 WS-2 silver + WS-3 gold: BUILT, LANDED, VERIFIED, ACCEPTED (base DS lane)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE (cot-exporter drift grounding)
**serial:** 0.4.0_DS_ClientPlatform (base lane) · **window:** 2026-07-18 00:08Z -> 02:05Z

## Summary

Base DS came online (Andrew-brought), lane-split with `~A` (who owns the trn_nna/WP8 flip
arc solo -- I did NOT touch schwab_flows.py / schwab_trn_nna_gold.py / C_01 / the step-5 arc).
Carried the two base-lane handoffs to completion:

1. **OPAL_TAXSMA_PT2.WS-2 SILVER `fact_taxsma_report`** -- built the complete Rule-17 parse of
   the 3 BD reporting bronze feeds, ran it LIVE against the landed Chiles bronze, verified.
   ACCEPTED by COO (verified to the cent). Commit `4d5b0148c`.
2. **OPAL_TAXSMA_PT2.WS-3 GOLD `dim_taxsma_report`** -- the anonymized, per-account, PII-gated
   serve projection. Built, ran live, PII PROVEN absent (mutant-tested gate). ACCEPTED by COO.
   Commit `1ba779e0b`. Routed to CTO's WS-4 SEV1 gate.
3. **cot-exporter IAM drift** (0.7.0 SURFACE, CTO-routed) -- GROUNDED read-only; verdict (a)
   re-add. Now DS-owned + DEFERRED per Andrew ("leave it for DS i dont care about that").

## Work done

### WS-2 silver fact_taxsma_report (`data/assets/scripts/silver/build_fact_taxsma_report.py`, NEW, 628 lines)
- Grounded the parse on LIVE bronze bytes (not just DT's shape doc): pulled the 3 landed Chiles
  feed JSONs, mapped the exact nested structure. Key finding: performance uses `combinedLevels`
  AND `levels` (identical 488-asset set, confirmed 0-diff), costbasis/allocation use `levels`
  (Account->Class->Segment->Asset); the 3 feeds have DIFFERENT grains/asset-counts -> a TALL
  union with a `feed` discriminator (NO cross-feed join -- window alignment is gold's judgment).
- Design: complete parse, Rule-17 dedup+dtype ONLY. Vendor key names VERBATIM; nested containers
  (benchmarks/TWR/MWR/descriptor) JSON-encoded; accountName KEPT (PII drop is WS-3's job). Grain
  = (schwab_account, feed, source_hierarchy, level, level_key, window, pull_asof). pull_asof IN
  the key (BD revises closed periods -- COO contract 220432Z; live-verified drift). Bridge via
  dim_account_xref on the BD external id (z0822596361 -> 0027265115). Loud FeedShapeError guards
  (perf split always-present vs active-only -- a notHeldInPeriod empty window omits netGains/TWR).
- Verified: dry-tested on real bronze (one-row-per-(account,window) + deliberately-missing-field
  RAISES); commit-gate PASS; LIVE run landed 3361 rows/106 cols; INDEPENDENT served read-back
  reconciles to the cent (BMV 1,061,234.71 / netGains -86,790.78 / TWR -0.081799148 /
  realizedShortTerm -61,933.73 / unrealizedTotal 822,456.41), 0 grain dups, leading-zero schwab
  id preserved.

### WS-3 gold dim_taxsma_report (`data/assets/scripts/gold/build_dim_taxsma_report.py`, NEW, 355 lines)
- Anonymized per-account projection (SEV1 PII). WHITELIST posture (strings default-excluded);
  FORBIDDEN set (account_name, bd ids, masked number, descriptor/blob cols, bridge meta)
  asserted-absent; level_name+level_key SCRUBBED to null at Account level. NO surrogate id ->
  NO re-id map (keyed by the real schwab number = WS-4 "re-id map outside prefix" satisfied
  vacuously). Report parse-down: perf x Account windows / costbasis x Account / allocation x
  {Account, Class+Segment sectors, top-10 Asset holdings}.
- CONTENT-SCAN PII GATE (the real control): scans every string cell for the client name+tokens
  +masked-number; a hit RAISES. Proven a real control by a MUTANT SUITE (injected name /
  un-scrubbed Account name / masked fragment -- the gate FIRES on each, not a no-op).
- Verified: LIVE run 3361->45 rows/86 cols, landed + listing-verified + PII-gate PASS;
  INDEPENDENT served read-back = 0 name-hits across every string cell, FORBIDDEN cols absent,
  reconciliation preserved, top-10 holdings intact, sectors kept. Isolated account-partitioned
  prefix. comp-surface-check: no critical surface (SEV1 flags = pre-existing portal drift).

### cot-exporter IAM drift (READ-ONLY grounding, Rule 13 held -- no cot apply)
- Mechanism (source): cot_bronze_ingest.py:822 `_publish_pricing_defect_alarm` -> sns.publish on
  the LIVE --backfill-holdings-net path; COT_DETECTION_SNS_ARN exported at ssm.tf:137. Publish is
  live+load-bearing. LIVE get-role-policy: cot-exporter-ec2-role carries SID=CotDetectionSnsPublish;
  config (iam.tf:241 cot_exporter_policy) does NOT. Config's only sns:Publish is on a DIFFERENT
  role (bd_cot_keepalive_policy, cot-detection-layer.tf:104). => the drift is BREAKING (next
  unqualified cot apply strips it -> e2 alarm silently AccessDenied-lost at :825). Verdict (a)
  re-add. 0.7.0 accepted; Andrew then deprioritized ("leave it for DS") -> DS-owned + DEFERRED;
  re-arm condition (re-add before any imminent cot apply) routed to CTO.

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| comp-grep (COT_DETECTION_SNS_ARN, CotDetectionSnsPublish, opal-bd-cot-cookie-alerts, sns:Publish, cot_exporter_policy) | cot-drift source+config grounding | PASS -- located publish mechanism + config/deployed divergence |
| comp-pipescript io / --help | WS-2 Phase-1 mandate (READS/WRITES/gaps) | N/A -- tool is GOLD-layer-only; cannot model a net-new silver script. Intent met via live-bronze reconciliation + PRD trace (gap noted below) |
| comp-which "verify reads/writes/column-gaps silver converter" | route Phase-1 | PASS -- top match IS comp-pipescript io (gold-scoped); confirmed no better tool for a new silver |
| commit-gate.sh (x2, silver+gold) | py_compile+AST+ruff+silver-ids | PASS both (silver astype-str WARN = known 49f string-account-key false-positive: schwab id zero-padded, bd id z08... -- must be string) |
| comp-validate build_dim_taxsma_report --artifact | gold invariant validation | NO_CONFIG -- net-new table, no config entry; invariants validated by hand (reconciliation + PII gate + mutant suite + served read-back) |
| comp-surface-check scan | WS-3 critical-surface check (by hand, COO guardrail 3) | PASS for my change -- SEV1 flags are pre-existing portal/MP/ADVI drift, unrelated; my new isolated gold prefix feeds no portal surface |

- **What worked:** grounding on LIVE bronze/xref bytes (not the shape doc) caught the
  performance combinedLevels-vs-levels drift + the notHeldInPeriod empty-window field omission
  before they became bugs. The mutant suite proved the PII gate is a real control.
- **What failed / Gap found:** comp-pipescript io / comp-validate are GOLD-registered-script-only;
  a NET-NEW silver/gold script has no entry, so neither can model it. For net-new converters the
  Phase-1 io check + comp-validate invariants fall back to hand-grounding (live reconciliation +
  PII gate). Worth a comp-tool gap note: no io/validate path for an unregistered new script.

## Blockers

None. WS-2 + WS-3 both ACCEPTED by COO. cot-drift DEFERRED (Andrew-deprioritized, not blocked).
WS-4 (Alyssa IAM) is CTO's SEV1 lane, not mine. Other base-lane TOs (C6/C7/C10/C11/C12/V2-5/V2-8/
GLDRNS-A4/ADVI_COTETL) remain externally gated per prior logs (not re-checked this window).

## Current State (handoff surface)

- **SILVER LIVE:** `s3://opal-data-assets/blackdiamond/49f/silver/fact_taxsma_report/date=2026-07-17/data.parquet`
  (3361 rows, 106 cols, ETag a74c3c8b..., 304,496 bytes). Producer: `data/assets/scripts/silver/build_fact_taxsma_report.py`.
- **GOLD LIVE:** `s3://opal-data-assets/blackdiamond/49f/gold/dim_taxsma_report/account=0027265115/date=2026-07-17/data.parquet`
  (45 rows, 86 cols, ETag 62f6e22f..., 31,900 bytes, PII-proven). Producer: `data/assets/scripts/gold/build_dim_taxsma_report.py`.
- Both scripts run standalone: `python <script> --pull-date 2026-07-17 [--dry-run|--upload]`.
  Lambda packaging/scheduled chain (bronze-sentinel -> silver -> gold) = WS-5 (AE), NOT built here.
- Commits `4d5b0148c` (silver) + `1ba779e0b` (gold) on origin/CLOUD (verified pushed; linear
  history, no rebase). Chiles-only (Bump/Macy = internal-accountId discovery follow-on).
- cot-drift verdict on record (msgs 013731Z to 0.7.0 + 020211Z to CTO); DS-owned, deferred.

## Next Steps

- **[1.0.0_SA_CTO]** WS-4 SEV1 gate: independent PII-safety verify + applied+exercised 22a IAM
  against the live gold artifact. Also holds the surfaced design call (real-account-number in the
  S3 key path vs a surrogate + re-id-map-outside-Alyssa's-prefix) -- interacts with the IAM scope.
- **[me / 0.4.0_DS base]** ON STANDBY: if CTO's WS-4 ruling asks for a surrogate/re-key of the gold
  path, re-key + emit the re-id map OUTSIDE Alyssa's prefix. Else nothing. Also DS-owned cot re-add
  if a cot apply becomes imminent (CTO-gated, plan=no-op verify first).
- **[2.0.0_SA_COO]** WS-2+WS-3 carried forward + accepted; WS-5 (trigger) + WS-6 (/tax-pt2) are AE/skill lanes.
- **[0.4.0_DS_ClientPlatform~A]** trn_nna/flip arc is yours -- untouched by me.
