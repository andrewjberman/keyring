# CTO half -- MDPF_SECCLASS: the 33 `multi_asset` rows remapped into the six classes by rule B -- SIGNED

**Signer:** `1.0.0_SA_CTO`, 2026-10-07 ~02:0xZ. **Request:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_MULTI_ASSET_REMAP_B_20261007.md` (CLOUD de33fcb674),
COO half signed by `2.0.0_SA_COO~M`. Asked in msg 105912. Andrew's words: six classes only, no multi-asset; "I like B".

## Read and signed as named

- **The act:** 33 conditional compare-and-set updates on existing `etf-classifications` keys (25 to equity, 8 to fixed_income), none created or
  deleted; sub-class restored on the 5 rows that held one before batch 183, otherwise removed with `low_confidence = true`. Nothing invented.
- **Served effect, from the producers' own rule** (every producer reads `asset_class` verbatim): $2,717,324.92 held at the three firms moves,
  $2,147,518.10 to equity and $569,806.82 to fixed income; Cottonwood's four SGIIX clients sum to 1 again; both firms' composition gaps close.
- **Blast radius:** the 33 keys, read by the three firms' Holdings producers, the Cottonwood and Black Diamond gold chains and, through them, the
  portal. **Writers:** N = 7 counted; only the seed path can rewrite these keys, and it does not run until its module carries the six-class
  values (condition 1 below). **Both branches** covered by the per-row condition. **Rollback:** the snapshot and `--rollback`, for a failed act
  only.
- **The five rows that are the COO's call:** First Eagle Global, Vanguard Wellington x2 and LifeStrategy Moderate Growth to equity. ACCEPTED: each is a
  balanced or allocation fund by its category, which is rule B's equity limb; that is the rule applied, not a new rule.
- **Recorded for Andrew, not changed:** Income Fund of America, Capital Income Builder and Franklin Income go to fixed income because rule B sends
  "income-oriented" funds there. Their actual holdings may be equity-majority. That is his rule's known imprecision; he can move any of them by name.

## Conditions

1. The seed script does not run until `infra/aws/lambda/v2_portal/_shared/etf_classification.py` carries the six-class values for these funds; that
   module edit, the AI classifier's vocabulary, the Holdings contract enum and the portal class lists are the next cell, in this round.
2. Acceptance 1 (a full scan reads zero `multi_asset` rows) is read before the ledger's leg S closes.

**SIGNED.**

-- 1.0.0_SA_CTO
