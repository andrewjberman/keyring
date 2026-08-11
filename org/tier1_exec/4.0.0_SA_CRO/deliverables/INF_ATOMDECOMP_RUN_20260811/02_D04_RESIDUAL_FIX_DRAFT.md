# F4 — the non-fee-AUA residual fix, drafted ready-to-land (DS lane via COO)

**Authority:** Andrew-direct (MSTR relay 044428Z): *"fix that bullshit residual error … that is what
results in the residual figure that freaked out patrick."* Grounded at deployed+repo source per the
relay's own instruction — the arithmetic below is read from
`data/inf/scripts/gold/INF_D_04.client_portal_summary.py:763-836 @f72495f387`, not from the relay.

## The defect, at source

`:822` — `non_fee_aua = max(0.0, float(total_aua) - fee_earning_aua)`
- `total_aua` = canonical_holdings market-value sum (current holdings, holdings date, holdings population)
- `fee_earning_aua` = billing-dim `SUM(ending_mv WHERE is_fee_earning)` (billing-period-end value,
  billing population)
- The subtraction therefore absorbs EVERY cross-source mismatch — missing billing rows (3 in
  Patrick's book), advisor_key-vs-rep_id book drift (6 accounts), period-end-vs-current date drift,
  frozen vintages — into a number displayed as if it were classified client money. Measured cost
  (predecessor brief §1): displayed ~$606K vs true classified $127,961.76.
- Counts at `:823-827` have the same residual shape.

## The fix (classification + explicit unmatched bucket; display contract preserved)

Replace `:822-836` body so all six existing fields become CLASSIFICATION-derived from the SAME
billing dim, and the cross-source gap becomes its own named field instead of contaminating non-fee:

```python
    non_fee_mask = ~fee_mask
    non_fee_aua = float(b.loc[non_fee_mask, 'ending_mv'].fillna(0).sum()) if 'ending_mv' in b.columns else 0.0
    non_fee_clients = int(b.loc[non_fee_mask, 'household_id'].dropna().nunique()) if 'household_id' in b.columns else 0
    non_fee_accounts = int(b.loc[non_fee_mask, 'account_id'].nunique())

    # The cross-source gap, SURFACED not absorbed (Andrew-direct 2026-08-11: non-fee AUA must be a
    # classification, never a residual). Sign is signal: negative = billing period-end values
    # exceed current holdings (date drift); positive = AUA with no billing row (unmatched accounts
    # + book-definition drift). NEVER clamped, NEVER folded into non_fee.
    unreconciled_aua = round(float(total_aua) - fee_earning_aua - non_fee_aua, 2)

    return {
        'fee_earning_aua': round(fee_earning_aua, 2),
        'fee_earning_client_count': fee_earning_clients,
        'fee_earning_account_count': fee_earning_accounts,
        'non_fee_earning_aua': round(non_fee_aua, 2),
        'non_fee_earning_client_count': non_fee_clients,
        'non_fee_earning_account_count': non_fee_accounts,
        'unreconciled_aua': unreconciled_aua,
        'unreconciled_basis': 'total_aua(canonical_holdings) - billing_classified(fee+non_fee)',
    }
```

Plus: extend `null_block` (`:784-791`) with `'unreconciled_aua': None, 'unreconciled_basis': None`;
update the docstring methodology block (`:767-780`) to state classification + surfaced gap; delete
the `max(0.0, …)` clamps (a negative gap must be visible, not floored).

## Contract check (P7)

The six existing field names/types are unchanged — the portal Profile tab reads them as-is; only
the VALUE of non_fee corrects (~$606K-class → ~$128K-class for Patrick's view). The two NEW fields
are additive JSON — no consumer breaks; the portal MAY later display the unreconciled bucket
(routed as a suggestion to the portal lane, not required for this fix).

## Acceptance bar upgrade (RATIFIED @d272021791, CTO relay 054315Z)

This fix is the **retirement vehicle** for the non-fee residual's TRANSITIONAL slot in the ratified
must-calculate exception set: on verified landing, the residual LEAVES the exception set and the raw
Billing classified sum becomes the served source. DS's acceptance therefore proves not just
correctness but SUCCESSION — the residual path is gone, not co-resident.

## Landing route

`data/inf/scripts/gold/**` = `0.4.0_DS_ClientPlatform` lane (Rule 13); DS stood down tonight; COO
is the wake point (their 044116Z). This draft makes the landing one review + one safe-deploy. After
landing: a `mode:incremental` (or gold-d) dispatch republishes platinum with the corrected figure —
~15 min end to end. Until it lands, tonight's unstick run republishes the OLD arithmetic — flagged
to Andrew via MSTR so the sequencing is his call (corrected-figure-tonight vs morning-landing).
