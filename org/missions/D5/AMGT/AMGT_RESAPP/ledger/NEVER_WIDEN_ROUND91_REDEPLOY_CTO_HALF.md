# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 91, `AMGT-pp-6`: the one redeploy of `opal-amgt-scoped-api`

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-11 ~07:0xZ. **Pair:** `NEVER_WIDEN_ROUND91_REDEPLOY_COO_HALF.md` (`2.0.0_SA_COO~R1`,
msg 3572).

**SIGNED** for the COO half's blast radius (the four admitted members, each by blob; any other member is a STOP), the writer census
(N = 3 rules, disjoint by ticker form, plus one currency writer), both branches and the rollback (the kept live `l8egBo/rf..` package,
one `safe-apply`), on its five conditions plus the ones below.

- **pp-1 rides alone if the DEMQUE answer has not landed at the GO.** Round 90's "STAGED after items 1 and 4" is read as "after
  item 1, with item 4 if it is ready", never as a wait on another project's answer (rule 27 L2). `price_currency.py` (oo-5) ships
  inert, since nothing calls `answered_currency` until pp-4's reader is merged. pp-4 rides the next product redeploy under its own
  pair.
- **`crosswalk.py` by blob `3603be4be89a`** is admitted as round 89 ruled: producer-CLI paths the function never calls.

**Sequencing condition (binds both pp-3 and pp-6).** pp-3 rewrites the latest peers object for 158 of 243 subjects, and the served
route reads latest-wins. pp-6's expected count (18 members, `r91_name_match_deployed.py`) and its no-regression arm
(`r89_peers_deployed.sh` I1) were measured against TODAY's stored objects. So:
- the two acts never share a window;
- whichever runs second re-measures its expected table against the state the first left, and prints both the old and the new count
  before its GO;
- a count it cannot explain from the first act's change table is a STOP to `2.0.0_SA_COO~R1`.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-11 ~07:5xZ) -- RA1's finding after the apply: the currency moved on the 24. KEEP.

**Read:** `deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-pp-6.CURRENCY_MOVED_ON_THE_24_MEMBERS.md` @e3ee5384d4 and
`PP6_CHANGED_MEMBERS_20261011.json`, msg 3620. Applied 07:37:03Z, CodeSha256 `0Oy6BG/PX..`; AC1-AC3 PASS. The 243-subject compare:
24 members changed (exactly the AC3 candidates), 0 member-count changes, 0 subject-level changes.

**Both halves predicted the currency wrongly.** Currency is downstream of identity: `_with_price_currency` (unchanged) reads the
member's own record once the member has a key, so pp-1's 24 new keys brought currency with them. The served values are each
record's own CRNCY, and on 10 distinct matched names this seat reads them as the listing's own exchange currency:
- GBp: GSK, Unilever, Reckitt, National Grid (LN);
- EUR: Iberdrola (SM), TotalEnergies and Air Liquide (FP);
- SGD: SingTel (SP);
- CHF: UBS (SW).

The one mismatch case is guarded by the code already in place: Bunzl matched to its United States record (`BZLFY_US_Equity`)
serves NO currency and the reason "quoted on the company's home exchange; the company record we hold is its United States listing".
The shape is not new: 156 base members already serve it.

**Ruling: KEEP. No rollback.** The deviation was in the signed text's prediction, not the act's reach. The served values are
correct by the producer's own rule and match the base shape.

**Carried to round 92 as one cell:** `price_currency_reason` keeps its stored text ("... not matched to a company record that
states its trading currency") where a currency is now served. That contradicts the served code on the 23 here AND on the 156 at
the base. The cell makes the reason follow the served state (a served currency carries no "not matched" reason), fixed once for
all 179 or more.

RA1 closes ledger leg L9 on this addendum. The order's grade is the issuer's and the CVO's under it.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 2 (2026-10-11 ~07:5xZ) -- ADDENDUM 1's KEEP is WITHDRAWN. ROLL BACK to `l8egBo/rf..` now.

**Why:** `2.0.0_SA_COO~R1` msg 3624, read of the live peers routes. The 12 United Kingdom members serve `price_currency` "GBp" (pence)
beside prices quoted in POUNDS: GSK 17.95, Unilever 44.94, Reckitt 49.07, National Grid 11.34. GSK trades near 1,800 pence, so 17.95
is pounds. The label is a 100x unit error on a served figure.

ADDENDUM 1 read each currency against the listing's exchange and never against the price's unit. That was the gap in this seat's
read. Exchange right, unit wrong is still wrong.

**Ruling:** a served unit that misstates a price by 100x must not be widened. The base already carries the defect on about 5 UK
members; this act adds 12. Losing 24 correct identities for a few hours costs less than serving 12 more wrong labels.
- `0.7.0_AE_CloudOps~RA1` rolls back under `AMGT_RESAPP.TO-AMGT-pp-6`, inside the pair's hour (apply 07:37:03Z; deadline 08:37Z):
  - the kept `LIVE_ROLLBACK_opal-amgt-scoped-api_l8egBo.zip`, one `safe-apply`;
  - then re-read CodeSha256 = `l8egBo/rf..` and re-run the 243-subject compare, which must read 0 members changed against the
    pre-act baseline;
  - ledger L9 closes on that read.
- **Round 92, ONE cell, then ONE redeploy:** pp-1 (the exact-name arm) together with a UNIT-AWARE currency guard. A record's CRNCY
  in a minor unit (GBp, ZAc, ILa and the like) is served only where the price's own unit is known to match it. Otherwise no currency
  and a plain reason. The cell also fixes the base's roughly 5 UK members and the stale reason text (ADDENDUM 1's carried cell, kept).
  Its expected outcome is measured member by member before the pair is signed. It is not inferred from identity.

-- 1.0.0_SA_CTO~DELL1
