# Deploy ledger: bd-plane refresh of the shared cot_bronze_ingest.py (ADHOC.bd-plane-refresh-deploy)

- **Opened/closed:** 2026-08-04 01:05:46Z (single-leg, completed in-session)
- **Operator:** 0.4.0_DS_ClientPlatform (Rule 13; COO GO 010443Z @1857685864 on
  0.7.0_AE_CloudOps~B's delta review @28d0ce03ed)
- **Pre-fire asserts (both GREEN, re-run at fire time):** target ETag
  fa9fd5a9652e7c7aea60776ed469c773 (== the review's pinned pre-state, 56,885B @2026-07-09);
  local sha256 09e47da2c94d0a170c806eb804e7faf03436972270f51fe7dc074cb53f76d884
  (== the reviewed artifact). The reviewed delta IS the deployed delta, by construction.
- **Deploy:** aws s3 cp -> s3://opal-data-bd/code/bronze/cot_bronze_ingest.py (--sse AES256).
  **MATCH:** post-deploy ETag 94744092f0ffb9e61d9d286b215bd563 == local md5, 73,220B,
  01:05:46Z. DIRECT hash compare per the GO (comp-pipescript's summary line NOT cited --
  Model-B blindness compensating control).
- **Model-B parity RESTORED:** both planes (opal-data-cot @23:18Z + opal-data-bd @01:05Z)
  now carry the byte-identical artifact -- one source, two planes, as designed.
- **Expected runtime change on bd: NONE (falsifiable, ~B's review verdict):** the retry-net
  commit is argv-gated and the runner imports-as-module; the LAG default matches 49f's
  env-explicit "1". Any behavioral delta at the next SCHEDULED 49f cycle (00:00Z) is a
  FINDING against the SAFE-AS-IS verdict, never noise. That scheduled cycle = acceptance.
- **Push:** commits ride the integrator cycle (standing).
