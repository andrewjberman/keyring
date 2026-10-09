# NFRA_TRNSPT decomposition -- ROUND 17 (2026-10-09, issuer 2.0.0_SA_COO~T2, dell2, box/dell2)

Cut on `1.0.0_SA_CTO~DELL2` msg 2293, `CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_12_20261008.md` ADDENDUM 4: "Round 17 = E1, TR-c-17 commentary.tf
(5 env names, composition and secret reads, address() output), then the apply pair; E2, the Apple re-write on CloudOps~DELL2; E3, the 365-day
backfill on CloudOps~DELL2 under the pair (simulate first, VersionIds first, counts only)."

| cell | item | outcome | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|
| `TR-c-17` | E1: complete `commentary.tf` (row D2-S8) -- the five env names, the svc-commentary secret read, the composition read, `KIMI_STANDING_WORD_REF`; `lambda_handler` reads the token's `.token` field | FWD-10 | dell2 worker | WORLD | worker | -- |
| `TR-p-17` | E1 tail: the Lambda's never-widen pair (COO half on the merged bytes; CTO half), then the apply by `0.7.0_AE_CloudOps~DELL2` | FWD-10 | ISSUER (served) | WORLD | -- | TR-c-17 |
| `TR-a-17` | E2: the Apple re-write (29 Research silver objects), read back Apple > 0, re-wipe 0 | FWD-5 | ISSUER (served; `0.7.0_AE_CloudOps~DELL2` writes) | SERVED | -- | MSTR's relay of the laptop stand-down (msg 2229) |
| `TR-b-17` | E3: the ONE 365-day backfill under its pair (COO half `1bb934be65`, CTO half AMENDMENT 1) | FWD-10 (precedent) | ISSUER (served; `0.7.0_AE_CloudOps~DELL2` writes) | SERVED | -- | MSTR's relay of the laptop stand-down |

**Chains.** A = TR-c-17 -> TR-p-17 (slot ~1). TR-a-17 and TR-b-17 are the issuer's served acts. Fan-out 1 of 1 worker chain, cap 8.

**Issuer rulings.** (1) The ticket token is the `.token` field of `opal/ticketing/svc-commentary`'s JSON value (contract v0.2 @20784c5462 row O1),
so `lambda_handler.token_reader` is in the cell; a Bearer of the whole JSON would 401. (2) `KIMI_API_URL` is the estate's constant
`https://api.moonshot.ai/v1/chat/completions` (`infra/aws/lambda/investor-reporting/ycharts/generate/kimi_port.py:18`). (3) The composition
address is `lib/opal_naming.py address()` output for where IRPT retains the analysis composition, measured from the producer's write; a builder
refusal is a row, never a typed name. (4) The KMS key-policy side on the `irpt` key is the laptop's; the cell writes the IAM side only.

## Rule 24 record

Domain: ADDENDUM 4's three items. E1 = TR-c-17 + TR-p-17; E2 = TR-a-17; E3 = TR-b-17. Remainder: none.

## Battery

Checks `org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R17_CHECKS/r17_checks.py` at base box/dell2 ce7106eecf: c17 FAIL (absent).
