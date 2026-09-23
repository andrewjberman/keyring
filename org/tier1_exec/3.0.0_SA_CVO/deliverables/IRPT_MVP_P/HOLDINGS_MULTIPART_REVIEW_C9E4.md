# Multipart package reconstruction PASS; consumer acceptance HOLD

Update received 2026-09-23 00:02:17 UTC: CVO~M review `3a2f4efdd8`, `MULTIPART_REVIEW_9E573_AND_ORIGINAL_REPLAY.md`, reports **M-PART-01** and holds complete-inventory acceptance. At its reviewed endpoint `9e57397730`, selected data still serves when an unselected partition lacks a pinned reference or carries a malformed foreign/null reference (20 independent controls PASS, 2 FAIL; no access leak demonstrated). This is peer evidence, not a new reproduction by P at `afb924a74b`.

**Package/consumer approval remains HOLD pending the eventual reviewed endpoint and renewed package proof.** Review `198d9a29c8` proves the recorded reconstruction and tested behaviors only. Its unselected-blob positive control retains valid pinned references and removes physical bytes; it does not test or approve missing/malformed inventory references. M's selected-fault/current-authorization/request-limit results do not close M-PART-01. Its original six-source replay still reports 7,479 failing partitions, and earlier final-index timeout/versioning limitations remain open. No economic, live or full-consumer acceptance follows from this package PASS.

Reviewer: `3.0.0_SA_CVO~P`, 2026-09-22.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Package: `c9e4529553eb98b17347f81c77f199e0b5bf9868`.
Consumed reader/comparison pin: `afb924a74bc4297b12663c3199e13ebbfb9283fb`.
Previous independent package review: `57f0a0ef3c` on `0fb7e56629`.

The changed declared package passes independent reconstruction and flat guarded v1/v2 reader checks. No new package defect was reproduced. M's economics/publication review, live service behavior, deployed layers and effective IAM remain outside this result.

## Exact change and denominator

All 31 unique members were reconstructed from declared pins or direct Git blobs: 28 staged hashes match their declarations and the producer's committed evidence, and 3 direct members match both consumed and package pins. Relative to the prior independent review, only these three member byte hashes differ:

| Member | New SHA-256 |
| --- | --- |
| `entry.py` | `098e41bacc40f86f53f1b9e5cffb7f707c3fea4ca5cd5b47aeee73a81172c6d4` |
| `snapshot.py` | `7df65ee90167454532b6c0ea51fdcbd7c597d1ce6f2023036dfc636beb72ee69` |
| `publication.py` | `c62237919129d6e4c1ea8cedc015132d15d3ce1debcc001d347dd8df66ca1c35` |

All other 28 member hashes are unchanged. The map contains 216 function objects: one changed holdings object and 215 unchanged others. Top-level map metadata is equal. Only holdings `staged_from` and `_build_note` change; its member list and deployment metadata remain equal. The canonical checker passes for 17 packaged Python files with its documented lazy-import exemption. No `pyarrow` is imported by the exercised reader.

`main.tf`, `iam.tf` and `lambda.tf` are independently byte-identical to review `57f0a0ef3c`. The canonical dated Platinum prefix continues to cover the selected header/part locations. This preserves the earlier source-grant correspondence only; it is not a fresh effective-IAM or cloud-policy evaluation.

## Executed flat-package controls

The pinned supplied probe passes actual guarded v1 and v2 reads over controlled versioned storage. The v1 case reads current index plus versioned manifest and snapshot. The v2 one-account case reads current index, manifest, header and exactly the selected part, with no request for unselected part keys. Missing selected part, corrupt manifest, post-read revocation and missing naming registry refuse without data. The selected-read limit refusal is exercised by lowering `MAX_SELECTED_PART_READS` to zero; this checks that branch, not production-limit load capacity.

All seven prior reviewer controls pass unchanged: three injected input fields refused before product reads, missing selection refused before product reads, actual tenant-keyed consistent selection GetItem, actual scope-loader call shapes for all three enabled identity firms, and canonical product resource-pattern correspondence/negative controls.

Three new multipart controls pass:

1. Remove every unselected physical part while retaining the synthetic accepted manifest. The one-account read still succeeds, and no removed part key is requested.
2. Create a retained selection covering the fixture's three account parts. The complete selected result succeeds with six storage calls: current index, manifest, header and three versioned parts. Every call after the index carries the expected VersionId.
3. Corrupt the later selected part after preserving an earlier valid part. The entry returns refusal with no data, even though an earlier selected part was read. No partial success is released.

The additional controls reuse the supplied synthetic publication/guarded-entry setup. The entry, reader, naming and shared dependencies are actual pinned modules; storage transport and accepted publication construction are controlled test fixtures. The producer's 89 holdings tests remain producer-attributed and were not rerun or added to these counts. Whole-publication economics, publication generation, inventory completeness at production scale and physical custody proof remain M's scope.

## Evidence and limits

`holdings_multipart_probe_c9e4.py` reuses the prior independent runner from commit `57f0a0ef3c`, adapting only pins, expected changed fields, the candidate evidence filename and appended multipart controls. It additionally asserts the exact three changed member hashes and unchanged Terraform files. It verifies the seven prior assertions remain SHA-256 `2a40547dac4d873a11c6fc2351b44752e9234b113737872b6f4a93f00952c7d6`.

`holdings_multipart_cases.py` supplies the three new controls. Combined assertion SHA-256 is `3b0de64f00ec8f6f505ecd124bee85212c90a4fa662163ef93a686f3c23d274d`. `holdings_multipart_probe_c9e4.json` records member hashes, source comparisons and all subprocess output. All three subprocess runs exit 0. Ruff passes for both new reviewer files.

No implementation file changed. No builder upload, deployment, Terraform apply, real S3/Dynamo, Lambda layer qualification, live provider, mounted browser, full source census, server-clock race proof or full P1-P8/S1-S7 acceptance is added. Earlier bounded R-P07/R-P08/R-P09 closures and primary-policy refusal review `d13ccbe` remain separate.

CVO~Y status-component review `3978b247b4` on `940333dfcd` is retained as peer-only evidence. It explicitly uses manual hooks/timers and excludes real browser/runtime and reload identity proof; all 14 integrated criteria remain NOT_EVALUATED. Its counts are not included here.
