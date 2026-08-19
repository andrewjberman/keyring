# 0.4.0_DS_ClientPlatform~A -- session log 2026-08-19 0111-0130Z: GOLDHOME-REPOINT DSA legs executed

**archetype:** MIGRATE-VERIFY

## Frame
AE's RP-AE-1 mint MCP 011113Z unblocked my staged legs (prep @ the 08-18 commit; TO @1b2ee34db7,
Andrew ~1730Z supersession: the ADVI gold home -> the per-client bucket `opal-data-49financial`).

## Work executed
- **RP-DSA-1 SYNC, two-sided PASS**: `portal/gold/advi/49financial/` -> `opal-data-49financial/gold/advi/`
  -- 4,222/4,222 objects, 327,275,368/327,275,368 bytes, per-table 10/10, relative-key sets equal
  BOTH directions, top-5 ETag identity. Manifests (rollback instrument) committed @d62b47cc44.
- **RP-DSA-2 one commit @d62b47cc44**: executed as the prep's measured SPLIT -- `runner_common` +
  `a00_runner` gain SILVER_BUCKET/GOLD_BUCKET + `_bucket_for(prefix)` (silver/meta/jd2 STAY on
  opal-data-assets; OUT_ROOT `gold/advi` resolves to the client bucket); c00-c03 gold-plane
  put/verify -> GOLD_BUCKET (CONV reads stay); entrypoint constants; safe_deploy_core advi row ->
  bucket-root `_code/` (CTO pin 174449Z). Exercised pre-commit: real silver read (fact_fam 7,202
  rows from assets) + real gold read (canonical_valuation 7,254 rows / 526 partitions from the
  NEW bucket) + bogus-table negative control naming the new bucket + a00's three planes (silver
  531 partitions ..08-17 / gold 2 / conv attested 7,308); mapping battery 6/6; test_safe_deploy
  14/14; pipescript-suite 140/140 at commit. Ruff caught 3 now-unused BUCKET imports (fixed).
- **_code MOVE (no twin)**: exec-time enumeration 51 objects (d_publisher_port.py verified
  PRESENT directly -- arithmetic-vs-listing resolved by reading, not reasoning), copy 51/51
  ETag-identical to `s3://opal-data-49financial/_code/`, OLD prefix deleted to KeyCount=0 with
  an adjacent positive control. The old GOLD DATA root untouched (RP-SPINE-2 = AE, after CVO +
  live-verify -- hold read back to CTO and confirmed).
- **P2D-4 FIELD 3 RE-ISSUED to AE** (012338Z): bucket-root code key + sync line + IAM deltas;
  AE confirms their REV 3 grant rows already byte-consistent (B5/B6).
- **Proof instance VALID rc=0**: `PROOF_OF_SPEC_GOLDHOME_REPOINT_49F_DSA_20260819.json`
  (RP-DSA-1/RP-DSA-2/RP-VAL; two-homes mutant FIRED with discriminating adjacent control;
  checker's artifact-coverage grammar mismatch declared honestly, not worked around silently).
- **CTO gate-seat validation 012326Z** (sync shape + split + pin honored + a01 FILED-not-chased);
  CVO's pre-staged re-anchor fired on my 012401Z MCP.

## Banked (no action)
- The sync wrapper task "failed" on my own `grep -c '^copy:'` counter (progress text prefixes
  copy lines) while the sync was rc=0 -- retrieval-control class; the two-sided census is the
  verify, never the log count.
- safe-deploy's 1739Z push stripped my sha/vintage metadata on <=3 _code keys (bonus lost,
  not a criterion; ETag verify is the instrument).

## Compiler Tools
| Tool | Invocation | Result |
|---|---|---|
| test_safe_deploy + pipescript-suite | at commit | 14/14 + 140/140 green |
| proof-of-spec-check | RP-DSA-1,RP-DSA-2,RP-VAL positional, bare rc | rc=0 VALID |
| comp-pipescript io | (runners registry gap stands until 0.8.0 REG) | direct exercise battery substituted, disclosed |

## State at close
DSA legs DONE + validated. Spine: CVO re-anchor (fired) -> AE RP-SPINE-1 independent read ->
RP-SPINE-2 old-prefix delete (AE). Next at this seat: P2D-3 QA exercise on the NEW root (08-19,
with AE; yields their binding duration) -> P2D-5 instance; P3-CLOSE 08-20; BDMERGE 08-21.
Watcher live; zero crons; nothing running.
