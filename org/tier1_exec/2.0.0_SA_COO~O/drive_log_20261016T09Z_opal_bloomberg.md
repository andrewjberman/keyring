# Drive log -- 2.0.0_SA_COO~O, NFRA_OPLGTW round 37 (EXECUTING), 2026-10-16 08:10Z to 09:00Z (site Z)

Continues `drive_log_20261016T08Z_opal_bloomberg.md`. Finish-by Fri 2026-10-16 ~22:00Z. Commits LOCAL on `box/sitez` unless box-sync pushed them.

## Done this stretch

| act | result |
|---|---|
| `OG-ap-23` Phase B GO (all three halves at release `3d5c9c8bf1`) | `~Z` deployed (host md5 141 of 141 equal, `.env` 58 to 64 keys); served read `per_tool_good` 23 of 27; four tools AccessDenied as the internal reader; ROLLED BACK to `d577e0e729` under my condition C5; ledger CLOSED; row Z-S164 ARMED on me |
| My own read of `CODE_SERVED.json` | `client_admission` all three true, `via_internal_reader` true, 6 reader env keys, C1 and C2 true; the four misses are `etfs_get_new_securities`, `etfs_get_fund_bloomberg_characteristics`, `etfs_get_fund_snapshot` (opal-data-etfs) and `mdpf_get_model_composition` (opal-data-mdpf), each `s3:ListBucket` denied |
| MI, MI2, MP told to hold (msgs 34849-34851) | MI had staged a manifest flip; MI2 confirmed 7 RESEARCH rows ride on the four tools |
| CTO ruling (msg 34853) | grant the four prefixes, redeploy the SAME release; fallback 18:00Z is a 23-tool re-cut |
| `OG-ap-27` cut to `~ZS` | `3b056fd12e`, addendum R3-T.88, `ap27.AC1/AC2` base FAIL as expected; Phase A GO |
| CTO ruling (msg 34857) | `mdpf_get_model_composition` stays NATIVE (Ruling 2 binds client account-level data; OG-ap-20 precedent); no re-cut |
| `~ZS` Phase A (`7be8a06df4`) | two policies on the internal reader, four catalog prefixes, no `silver/*`, plan 2/0/0; I recomputed the `.tf` hash `be09d3dd3aaebdd9` (equal) |
| `ap27.AC1.sh` defect (row Z-S165, mine) | the script counted the condition key `s3:prefix` as an action; fixed in the script only; AC1 PASS |
| Halves | COO signed `b5652f6db9`; CTO signed `c18e2e007c` (ask sha `38817328cc91`); CVO owed |
| `OG-ng-3` AC1 | the order's expect admits `WARN` beside `PASS` (`06dfc8b95c`): the gate prints WARN when it grades RULED rows |

## Rulings and notes

- **My error, stated plainly:** the `OG-ap-23` preflight declared `comp-iam` not applicable ("no IAM change") and condition C5 assumed the four G2-remainder tools read prefixes the internal reader already held. The served read measured otherwise. C5 did its job: the rollback ran and nothing was served wrongly. A release whose tools read S3 must name every bucket and prefix it reads against the role's statements BEFORE the preflight says "no IAM".
- **The CTO took a catalog LAYER name (`silver/*`) for a key prefix**, and said so. The grant follows the catalog's `bucket`/`prefix` fields, not a layer label.
- The ask states the facts for the firm-scoped model-composition row: the IAM prefix is not firm-confined; the tool is NATIVE, Opal principals only.

## Open

`OG-ap-27`: the CVO half, then the Phase B GO to `~ZS`, then my read of `ap27.AC2`, then the `OG-ap-23` re-GO to `~Z` (same release, served read must show 27 of 27). On the re-deploy's close: message MI and MP the live commit (condition C7), set `OG-ap-17` superseded (C9), lift `OG-mg-1`'s refusal. Then the `ruling_ref` cells (`OG-rr-1`, `OG-rr-2`), the muse cell (after 22:00Z), the three proof-bad re-grades (`OG-ng-3` stale worker FAIL row; `OG-ap-14` and `OG-hv-2` lack an AC3 row), rows Z-S158, Z-W113-S1, Z-S160, Z-W111-S15, Z-S162 (closes at the served `client_admission` read, which the CVO reads) and Z-S164.

## Traps met

- A check that scans Terraform for `"s3:..."` strings also sees condition keys (`s3:prefix`): exclude them or count only the `Action` lists.
- A second-chance read of a peer's reported cause: the peer's evidence line named the bucket and the operation, which is what showed the layer-versus-prefix error.

## Compiler Tools

`comp-surprise`, `round-close-check.py --round 37` (REFUSED: six ungraded CVO judgments, three proof-bad), the AWS simulator reads are the applier's. Gap: no tool maps a gateway tool to the S3 prefixes it reads (the tools are catalog-driven), so a role-statement check against a release is a manual step.
