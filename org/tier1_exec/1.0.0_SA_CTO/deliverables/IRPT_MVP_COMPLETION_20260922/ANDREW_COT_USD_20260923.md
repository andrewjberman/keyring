# Andrew-direct Cottonwood report currency confirmation

Received directly by1.0.0_SA_CTO in this session on2026-09-23. Recorded at 2026-09-23T20:57:59.993881+00:00 .

Question: Can you confirm that Cottonwood's Black Diamond reports express market values and cash flows in USD? The retained API responses omit currency, so I need an explicit firm-level confirmation before labeling those amounts.

Andrew's answer, verbatim:

> Yes—all COT report amounts are USD

## Implementation consequence

COT Black Diamond report market values/cash flows may be denominated USD on this explicit firm-level authority. P owns the shared mapping/schema/runtime provenance; M consumes the same authority for Cottonwood holdings source amounts. Preserve the attestation reference and date in private source/normalization evidence alongside unchanged raw vendor responses. Do not label it as a vendor-returned currency field. No new vendor query or currency research is required.

Scope is Cottonwood report amounts. It does not settle INF/49F source denomination, FX/security-native currency, missing values, duplicate/census/date failures, valuation basis, fees or return methodology. Percent/decimal returns remain dimensionless. A future contradictory explicit vendor currency is a source conflict to adjudicate, not an excuse to overwrite vendor evidence. No currency conversion is implied.

P now proceeds with retained provider result -> report repository -> scoped API -> real-login screen. M proceeds with validated COT custody classification/reconciliation and per-account availability; unknown values remain unknown. The first proved Holdings flow may be whichever firm/account is actually ready; INF and49F still require completion.
