# Session Log -- MDPF_ASSETS.011 SmartX per-account-model-membership + account-join probe

**Agent:** 0.4.0_DS_ClientPlatform (DS Base lane)
**Date:** 2026-05-18
**TO:** MDPF_ASSETS.011 (dsbase-smartx-per-account-model-membership-probe), issued by 2.0.0_SA_COO
**Project:** MDPF_ASSETS
**Origin:** Andrew direct -- "see if there is a mechanism through the SmartX backend
to start putting the pieces together on which 49 accounts are in what models."

---

## Outcome

COMPLETE. Two verdicts, both YES:
- (A) Per-account 49F model membership + value: obtainable directly via
  `enterprises/allocations?modelid=` (rebuilds model_aua to -0.00% vs the WS-A ref).
- (B) A deterministic SmartX->Schwab->BD account join: solved via a
  holdings-fingerprint bridge -- 95% unique match on an 80-account sample, full
  chain verified end-to-end. No AC4 escalation.

Finding brief: `docs/briefs/mdpf-assets-011-smartx-per-account-model-membership-probe-20260518.md`.

---

## Course of work

Andrew steered this mid-probe across three messages, each sharpening the question:
1. "is there a mechanism" -> probe membership.
2. "match that ID to a client account ... for the join" -> probe the account join.
3. corrected my model: the SmartX UUID is useless cross-system; the BD<->Schwab
   join is deterministic (leading-zero padding), not fuzzy.
Andrew then chose the holdings-fingerprint bridge over a credential request.

## Phase 1 -- membership probe

`enterprises/allocations?modelid=` -- account-grain roster, one row per
(account, model): allocationId, status, advisor, model, value, openedDate.
Open-status value across 7 models = $1,360.24M vs WS-A ref $1,360.27M (-0.00%).
6,849 open allocations. modelId->model_key map confirmed for all 7.

## Phase 2 -- the account-number wall

The brokerage account number is permission-walled on the `opal7` Manager token:
`accounts/{id}` -> 401; `enterprises/accounts` -> 401 "not an administrator";
`users/access.accountAccess` -> []. `allocations/performance` exposes per-allocation
`account.id` (SmartX UUID), `account.type`, `custodian.name="Schwab"` -- but no
account number. The SmartX UUID is a SmartX-internal serial -- useless for the
cross-system join (Andrew-confirmed).

## Phase 3 -- the holdings-fingerprint bridge

Match SmartX accounts to Schwab accounts on the per-account holdings vector.
- SmartX: `accounts/{account.id}/holdings` (works on the Manager token).
- Schwab: `s3://opal-data-schwab/silver/RPS/` -- 5,743 accounts, $1,590.6M, native
  position grain (NOT ULN -- ULN is tax-lot grain + partial 3,690 accts).
- Matcher iterations: v1 (no aggregation) 0/60; v2 (ULN tax-lot agg, exact-set)
  41/75; v3 (RPS + quantity-vector matcher, margin-checked) 76/80 = 95.0% unique
  (73 EXACT + 3 VECTOR). 1 NO_MATCH = a $0 empty account; 3 AMBIGUOUS = small
  accounts needing a tie-breaker. Value cross-check median 0.78%, uniform ~-1%
  (= the 10-day market move; corroborates the matches).

## Phase 4 -- the Schwab->BD link

Schwab `account_id` 10-digit zero-padded (`0049546212`); BD
`silver/allocations.original_account_number` bare 8-digit (`49546212`). Key =
`lstrip('0')`. Verified: 73/76 probe-resolved derived ids present in live BD data.
Exactly Andrew's "couple zeroes on the front." Flagged: the archived
`build_schwab_bd_account_mapping.py` uses fuzzy matching -- contradicts this
deterministic key; surfaced to COO/DE.

---

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-*` graph tools | N/A -- external-backend feasibility probe (SXPL_RESTIN .001 / MDPF .002/.003 precedent), not a pipeline-graph trace. Documented per the TO mandate phase 1. |
| `comp-iam` | N/A -- read-only probe, no committed harness, no new AWS surface. Documented per the TO mandate phase 3. |

---

## Files

| File | Change |
|------|--------|
| docs/briefs/mdpf-assets-011-smartx-per-account-model-membership-probe-20260518.md | NEW -- the finding brief. |
| mdpf011_smartx_account_probe.py / mdpf011_fingerprint_probe.py | NEW (workspace root, uncommitted) -- read-only probe harnesses. |
| mdpf011_probe_result.json / mdpf011_fingerprint_result.json | NEW (workspace root, uncommitted) -- raw probe output. |

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO 2.0.0** | RAVC2 -- MDPF_ASSETS.011 closed YES/YES. Brief feeds WS-B. Flag: the archived `build_schwab_bd_account_mapping.py` fuzzy matcher contradicts the deterministic leading-zero key -- route to DE/ops to confirm it is not in a live path. |
| **DS~A (WS-B)** | Phase-0 question (a) answered. Brief §6 is the build spec: keep `enterprises/allocations`, add `allocations/performance` for custodian + account.id, build the fingerprint bridge against Schwab RPS, derive the BD account number by `lstrip('0')`. |
| **Andrew** | Holdings-fingerprint bridge proven (95%); the higher-privilege-SmartX-credential option remains open if a cleaner direct account-number path is wanted. |
