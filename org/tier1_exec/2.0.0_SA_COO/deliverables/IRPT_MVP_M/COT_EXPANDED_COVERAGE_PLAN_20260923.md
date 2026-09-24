# Cottonwood expanded Holdings candidate — 2026-09-23

Prepared only; zero cloud writes. The current live authenticated journey remains FAIL.

## Concrete result

Candidate revision `93f930c265ed242d7e38cb48a7ed4baf267025e8c4dfd06ff39739c6a8f55217` covers 841 of 981 retained source accounts: 13,793 unique positions, 15,475 nodes, USD 548,412,662.59. Every admitted account reconciles independently within USD 0.01. Schema validation and aggregate reconciliation pass. Positions remain honestly classified Client where position model/SMA membership is not established; this is custody coverage, not proven model attribution.

Both Anna accounts are included, individually and as a combined selection: `acc_0698a3de842dbe7b3d48c787` has 30 positions / USD 26,303,302.1722 source precision; `acc_d486fc9455d6b2aa18e13af1` has 57 / USD 19,705,844.8433. Combined display total USD 46,009,147.02. The existing accepted account's 59 node identities, parent links, basis, economic values and clocks are preserved. Whole-publication percentages/denominators change as expected; the route reprojects the selected scope.

140 accounts are explicitly excluded and retained in the account census: 138 have no admitted active custody rows, two contain repeated rows within the same relationship grain. No empty or zero position is fabricated. An arbitrary selection containing any excluded account must continue to refuse. The complete source build currently fails those duplicate rows, so this candidate is the full measured supported subset, not a claim of all-firm completion.

## Exact input and output plan

The seven original S3 source versions and byte hashes are unchanged from the accepted one-account publication. Bytes were reread by VersionId and verified; partition discovery was closed to that retained set. Custody/business date is 2026-09-22 and overlay date 2026-09-23. The source cutoff is not a new custody date.

The 15,239,821-byte snapshot requires the existing v2 multipart publisher: one Gold Parquet, one header, 15 account-complete JSON partitions, one immutable manifest, then one conditional current-index update (19 writes total). Header and partition bytes/hashes/account censuses are in `COT_EXPANDED_COVERAGE_CANDIDATE_20260923.json`; canonical account reconciliation/refusal census is in `COT_EXPANDED_ACCOUNT_CENSUS_20260923.json`.

Current index was read before the candidate build: VersionId `JhtDD.AAg1AO0kdvVkxVZN.zWdjwDkkA`, SHA256 `018f92801f2c7c962cd1c699461084af011926776e10e6628880dee4aec0c228`, ETag `606126dddec555c41e711b18732d3c7f`. Preserve all other date rows; replace only the 2026-09-22 row using that exact IfMatch. All original immutable objects and prior index versions remain retained. If current moved, refuse and reconcile; never overwrite a newer publication blindly. Manifest bytes can only be finalized after S3 returns immutable VersionIds. Verify every immutable write by exact returned version/hash before advancing the index, then verify the exact returned index version.

Local immutable bytes: `.runtime/holdings-journey-20260923/coverage/prepared/` in `ajb_irpt_m`. Reproducible local census/build scripts are beside it; no vendor acquisition. Exact retained originals remain in that private runtime cache, not the public API.

## Remaining execution and proof

CTO adjudicates this concrete publication plan. P consumes runtime-loader repair `3e913e9ce9` and proves the actual Lambda image/package before the one-function update. After both changes, independently test each Anna account and their combined selection at default/date22; date23 must still refuse. Then exercise the actual logged-in browser journey and record request/response evidence. Native-reader checks alone are not authenticated product acceptance.
