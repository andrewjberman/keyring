# ANDREW-DIRECT 2026-08-11 ~1445Z — fee_earning_aua investigation (at the ~A terminal)

**VERBATIM:** "we need to get to the bottom of this 'fee earning aua' because certain figures
were established that showed that true non-fee-earning aua was more like 8m but we're saying
here its 60m+ which is definitely not right"

**Channel:** direct to 0.4.0_DS_ClientPlatform~A at the session terminal, immediately after the
d02 inverted-band report cited served `total.fee_earning_aua = $137,185,162.73` beside
`total.aua = $209,129,912.97` (implied non-fee-earning residual ≈ $71.9M).

**Scope as received:** get to the bottom of the fee_earning_aua figure — an INVESTIGATION
directive to this lane. The FIX choice for the underlying billing-window substrate remains at
CTO+COO per their standing ruling (COO 093155Z); nothing here re-scopes that.

**Working hypothesis at record time (to be measured, not assumed):** the ~$60M+ implied
non-fee-earning residual is the fee-earning-AUA UNDERSTATEMENT artifact (the rolling-3y
Activity window class, MSTR @dbddd3fe52: served fee_earning ≈ $137.19M vs true ≈ $201M if
non-fee-earning truth is ~$8M — an understatement of ~$64M ≈ 31%, matching the known ~30%
class and the $68.39M/312-account coerced-zero census).

**Broadcast:** COO + CTO + MSTR, same turn, per the record+broadcast law.

---

## FINDINGS (measured ~1500Z, all legs same-vintage 2026-08-10; reconciliation closes to <$1)

**The "60M+" is NOT non-fee-earning AUA. It is fee-earning clients' AUA suppressed to zero by
the rolling-3y billing-window artifact.** Decomposition of the implied served residual
($209,129,912.97 − $137,185,162.73 = $71,944,750.24), exact:

| component | measured |
|---|---|
| TRUE non-fee-earning AUA (billing mask × positions truth, 118 accounts) | **$12,374,779.77** |
| COERCION-SUPPRESSED fee-earning AUA (259 fee-earning accounts, billing ending_mv==0, positions>0) | **$59,619,641.81** |
| basis residue (vintage/rounding) | −$49,671.34 |
| **sum** | **$71,944,750.24 ✓** |

**Independent leg (artifact-free mask):** custody flow-ledger Management-Fee activity,
trailing 12m → 755 fee-active accounts; **non-fee-earning AUA = $6,270,920.28** — consistent
with Andrew's established ~$8M. The $12.37M billing-mask figure is higher because the
`is_fee_earning` FLAG itself rides the same defective billing pull (young fee-paying accounts
can read non-fee when their window returns empty) — the flag inherits the artifact.

**De-artifacted fee-earning AUA:** $196,998,563.73 (billing mask × positions) /
$203,102,423.22 (ledger mask) vs served $137.19M — the known ~30% understatement, now
decomposed at account grain (259 of 789 flagged fee-earning accounts carry coerced zeros).

**Mechanism at source (grounded):** `INF_D_04.client_portal_summary.py:107` (billing dim =
the fee_earning_aua source) + `INF_D_02.advisor_client_detail.py:1373-1376`:
`fee_earning_aua = SUM(billing.ending_mv | is_fee_earning==True)` — the VALUE and the MASK
both ride the billing plane, so the window artifact suppresses both. Served-basis
reproduction: my same-formula sum $137,378,921.92 vs served $137,185,162.73 (−$194K ≈
day-skew) — basis confirmed, not inferred.

**Fix ownership unchanged:** the window-fix choice (inception-anchored vs raw currentValue)
stays at CTO+COO; Andrew's ~1450Z absence-serves-NULL law (@162965ed1c) governs the serving
side; per-account self-heal on 3y anniversaries means these figures drift up slowly on their
own — drift is the artifact healing, not a fix.

---

## ANDREW-DIRECT #2 (same terminal, ~1530Z) — the flag-derivation fix assigned to this lane

**VERBATIM:** "fix the is_fee_earning flag derivation too when the window fix lands"

**Binding read (addressed seat, no scope adjudication):** the sealed-order member
"is_fee_earning re-derivation, window-independent" (admitted CTO 145936Z) now has THIS LANE
as its executor, TRIGGERED BY the window fix landing. The window CHOICE itself
(inception-anchored vs raw currentValue, orion_billing_dim.py) stays at CTO+COO — Andrew did
not move that; he assigned the flag-derivation fix that follows it.

**Trigger discipline (every clock needs a named live owner):** trigger = the CTO+COO window
fix landing on the billing pull. Asked COO/CTO in the broadcast to NOTIFY THIS LANE at that
landing; standing task armed on my side so a dead notification does not kill the clock.

**Design intent pre-staged (subject to the ruled constraints, stated not decided):**
re-derive is_fee_earning at ONE home on the **GOLD canonical plane** (CTO placement
correction 155818Z: a judgment classification is GOLD-tier logic — Rule 17 forbids it in
silver; the natural home is the gold billing/account dim on the canonical plane, the same
plane build_billing_dim.py's successor lands on). Basis: the SINGLE ruled derivation (CTO:
ledger leg presumptively truth side — custody Mgmt-Fee activity, both lag edges declared,
window length a ruled tunable). INF_D_04's own ledger mask then CONSOLIDATES onto the healed
gold flag in the same act (single-basis law — today's D_04-local mask is correct but is a
second derivation site the fix retires). *(Prior text staged "in silver" — CORRECTED before
any build inherited it; the wrong placement would have been the first each-layer-one-job
violation inside the new canonical plane.)* Trigger notification armed AT THE SOURCE by CTO
(base instructed to notify this lane at window-fix landing); lane-side task = backstop.
**Tree-boundary interaction, surfaced not adjudicated:** the derivation lives in
build_billing_dim.py — base's retained file per the TO boundary; COO squares the lane
mechanics before the trigger fires (time exists; the instruction is future-triggered).

-- 0.4.0_DS_ClientPlatform~A
