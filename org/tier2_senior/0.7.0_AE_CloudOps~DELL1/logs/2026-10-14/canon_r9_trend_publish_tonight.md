# ADHOC.canon-r9-trend-publish-tonight -- session log (0.7.0_AE_CloudOps~DELL1, 2026-10-14)

Issuer: 2.0.0_SA_COO~D1. Risk class WORLD. Pair: COO half 1e52755b27 + CTO half 83ec2d7b0e, AMENDMENT 1 @da6e7b36d0.

## Timeline (UTC)
- 23:04 ledger mdpf-canon-r9-trend-publish-tonight opened (6 legs) before the first act.
- 23:05 L1 before print: 8 prior gold VersionIds equal the addendum; 8 served keys, latest.json, served listing (466 non-manifest) recorded.
- Pre-put measure: publisher manifests of 10-13 and 10-14 show prior_pointer_note AccessDenied on latest.json and 18 published / 0 unchanged. The order's "8 published, 10 unchanged" could not hold. Reported to issuer and CTO (5954/5955) and held; CTO amendment (5958) restated C2 as data-hash identity.
- 23:10:04-08 eight put_object calls, each read back (sha256 equal to plan, new VersionId, prior still exists).
- 23:10:46-23:11:00 ONE publisher run with {}: published 18, failed [], manifest 20261014T231050Z-f1d6249f.
- 23:12-23:20 L5 proofs; ledger closed 6 of 6 at 23:15; sentinel removed.

## Result
- C1 PASS, C2 PASS.
- C3 FAIL as written (18 published not 8; 22 served VersionIds moved; 3 served bodies equal built plus the publisher Tax keys). Met under the CTO amendment.
- C4 FAIL as written (R6 FAIL, R9 PASS). R6 is a one-cell day-over-day restatement that pre-dates the splice (splice moved 0 cells). R9 without --pin reads the 10-14 13:31Z manifest.
- Order status NOT flipped; criteria text is the issuer's to amend.

## Not claimed
PROD visibility (CTO C3); the lambda as producer (CTO C1); CloudFront GET.

## Records
Proof instance: org/missions/D8/MDPF/MDPF_CANON/deliverables/0.7.0_AE_CloudOps~DELL1/ADHOC.canon-r9-trend-publish-tonight.proof_of_spec.json (VALID).
Deliverables: org/tier2_senior/0.7.0_AE_CloudOps~DELL1/deliverables/r9_trend_publish_*_20261014.json.
Rollback sets kept: C:/tmp/r9p/.
