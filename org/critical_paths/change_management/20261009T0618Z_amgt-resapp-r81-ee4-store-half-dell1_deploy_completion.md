# Deploy Completion Record
**Date opened:** 2026-10-09T06:18:07.483079+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 81 AMGT-ee-4: re-cut and re-analyze five stored 20-F names (ASML NA first), dell1
**Authored by:** 0.9.0_WK_AMGT_RESAPP~321
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | ASML_NA_Equity silver part + analysis + drafting rewritten; AC1 and AC2 YES | AC1 AC2 output lines |  | OPEN |
| L2 | verify | BABA_US_Equity silver part + analysis + drafting rewritten, or silver rolled back | new VersionIds or rollback proof |  | OPEN |
| L3 | verify | NU_US_Equity silver part + analysis + drafting rewritten, or silver rolled back | new VersionIds or rollback proof |  | OPEN |
| L4 | verify | PBR_US_Equity silver part + analysis + drafting rewritten, or silver rolled back | new VersionIds or rollback proof |  | OPEN |
| L5 | verify | SAP_GY_Equity silver part + analysis + drafting rewritten, or silver rolled back | new VersionIds or rollback proof |  | OPEN |

## Log

- 20261009T061807Z OPENED by 0.9.0_WK_AMGT_RESAPP~321 with 5 leg(s)

## PRE-ACT RECORD (read 2026-10-09 ~06:2xZ, before the first write; condition 2 and 4)

Pair: COO half `NEVER_WIDEN_ROUND81_EE4_COO_HALF.md` sha256 e820857fd4b6f18785e198d05154a7934c974eccef997dbe0fef072e8b3cb3eb; CTO half
`NEVER_WIDEN_ROUND81_EE4_CTO_HALF.md` sha256 4ac5bb0933cc026d9e716eabbdeb192931c6188d924e7818767ecdc7a9db89e5 (both under
org/missions/D5/AMGT/AMGT_RESAPP/ledger/). Import check on this tree under py -3.12.10 (anthropic 0.84.0): `import lib.research.filings.fetch, lib.research.filings.analyze` -> IMPORT-OK.
Silver filing_source (sec): ONE part before the act, `sec/harvest/silver/filing_source/date=2026-09-22/part-20260922T033157Z.parquet` (808,344 B); all five prior rows fetched_at 2026-09-22T03:31:57.788873Z, parser opal-filings-fetch/1.0.0.
Full prior rows (rollback source for the silver re-append): deliverables/0.9.0_WK_AMGT_RESAPP~321/prior_silver_rows.json.
CIKs (universe/v1/2026-10-06.json filing_identity, form_expected 20-F): ASML 937966, BABA 1577552, NU 1691493, PBR 1119639, SAP 1000184.

| name | accession | prior silver record_hash | analysis key VersionId (LastModified) | drafting key VersionId (LastModified) |
|---|---|---|---|---|
| ASML_NA_Equity | 000162828026011378 | 8e8b3f33bb3de83fc76b46abcbb524d3192ee52c6dd94dbbfb82bd3963841365 | WIU.oSeIh8NKMhy2DfqsJmRwGOusYTxs (2026-09-30T05:27:33Z, 93121 B) | FWeloN5.zr6pvN1NWUXScK5RakjwF1qV (2026-10-05T23:43:38Z, 13503 B) |
| BABA_US_Equity | 000119312526231755 | 3556dca9d0de13313f73734dc577d19366f8396bb6651ac64c61b4f8d0a9a24b | DmJ7NkDkRBbfQdX6DSA7KDsY1W.uEfVJ (2026-09-17T02:15:50Z, 286275 B) | VFL1upyKN4FJHsLUl4CbYX88uK04IACp (2026-09-30T19:48:26Z, 116539 B) |
| NU_US_Equity | 000129281426002166 | ddc31a976dd1a5c0d862ef78d0c72b3f8ebabfea3a9d806f9fee018579183dd6 | 9TdrmvW.Tu6wyqOiby9bXSODRvSiHCEW (2026-09-17T02:27:44Z, 385571 B) | IOc9Qbp8uD5tBnmaW5nfsTr6dKxK9SH0 (2026-09-30T19:48:28Z, 103452 B) |
| PBR_US_Equity | 000129281426002168 | 81bc74bf096a27784e20d615691d57d01d6fa3fa0aa85e81f5df2a5db2cd199f | olR02tlq3ciXsCxp43HMXRR_8vOxGWkx (2026-09-17T02:29:52Z, 237900 B) | ZmdJB1hRO43_wa4IUJSwiNbMlVdsH0hn (2026-09-30T19:48:28Z, 100899 B) |
| SAP_GY_Equity | 000110465926020058 | 37a6a4576da9a5b8cd27da130e8994ef07f6c79c1a8123c09343c7f5a3147fe1 | rmP1ek8s2AVOO.IMhvmk_3Snqx6vI3zF (2026-09-17T02:32:05Z, 252798 B) | qb9GzRTF0E9_nend.L7Sc_W0d_4b5BTR (2026-09-30T19:48:28Z, 88518 B) |

Analysis key = filings/v1/<KEY>/<accession>.analysis.json; drafting key = drafting/v1/<KEY>.json (bucket opal-data-harvest).
