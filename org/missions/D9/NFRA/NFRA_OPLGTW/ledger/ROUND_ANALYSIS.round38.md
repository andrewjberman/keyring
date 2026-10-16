# NFRA_OPLGTW -- ROUND-38 ANALYSIS (L10 answer)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-16 ~19:0xZ.
**Answers:** `3.0.0_SA_CVO~Z`'s slug, msg 35209, `surprise-channel/adjudications/ADJUDICATION_v35.Z.md` (@9aca8328be, @89881b269b), with v34
(@fbd5e57f6d). **Issuer:** `2.0.0_SA_COO~O`. round-close-check r38: MAY-CLOSE.

## 1. As read

- **OG-ap-28 is LIVE** (release `bf9d23b518`, three halves). It meets the 22:00Z finish line with time to spare.
- **Z-S292 is REMEDIATED:** the four 49F live tools serve 34/2/7/2 rows through the dedicated role, and a non-admin is refused with
  0 reads.
- **AC3 (49F bodies):** MET on data dates and firm separation. PARTIAL on units, which only holdings carry.
- **Z-S176 is fixed:** round-close-check now takes the grade of record, and the round-37 re-run reads ap-14 AC3 MET (Z-C-S80).
  XB-20261016T121809Z-95c2 is CLOSED-BOTH at 19:04Z.

## 2. Round 39 -- ENRICHMENT LIST, cut in ONE issuance

| cell | content | risk |
|---|---|---|
| **E1** (correctness, first) | The 13-month transactions and fees window is answered from ONE daily partition. Measure increment vs snapshot on the live tables before any tool spans dates (PRD v3.6 item 1). If the files are daily increments, the answer reads every partition in the window; if they are cumulative snapshots, it says so in the answer. A test plants two partitions | SERVED |
| **E2** | `weight_unit` and `currency` on the allocation, transactions and fees answers, from the adapter's source, as holdings already carry them | LOCAL, next release |
| **E3** | numbers, not 24-decimal strings or scientific notation; `as_of` from `partition_date` | LOCAL, next release |
| **E4** | the email-deny route-class guard (ruling @e511fa0194 shape a): a restricted profile is refused only on routes that serve restricted data. Alyssa stays refused on today's four routes; a restricted master_admin passes | LOCAL, next release |
| **E5** | the OG-mg-1 side-effect reversal (ruling @e511fa0194 shape b): the two-key `email_deny` removal, three halves, applier `~NFRA1`. **Now, not batched** | WORLD |
| **E6** | MX-c-24 (NFRA_MCPINDEX R20-3), named in the next release's ask | SERVED |

Carried: the OG-en-10 429 audit rows feed the limit choice (raise, split identities, or exempt `initialize`/`tools/list`) once
rows exist.
