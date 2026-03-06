# NNAVAR Phase 5 Transfer Out EC2 Execution — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 23:29
**End Time:** 23:35

---

## Objective

Execute Phase 5 transfer_out_desc_audit on EC2. Tests whether Transfer Out rows
with Schwab-platform keywords in description account for the -$119M volume gap.
Per brief: stop and report after desc_audit if `exclusion_warranted: false`.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Upload script | `s3://opal-data-bd/scripts/diagnostics/diag_nnavar_phase5_transfer_out.py` (24.7 KB) |
| 2 | Suite: transfer_out_desc_audit | CMD `1feef78b` — SUCCESS, 3s |
| 3 | Read gating flag | `exclusion_warranted: false` — transfer_out_exclusion SKIPPED |

---

## Results: transfer_out_desc_audit

```json
{
  "transfer_out_rows_post_exclusion": 5992,
  "transfer_out_gross_volume": 145664126.0,
  "schwab_keyword_rows": 8,
  "schwab_keyword_volume": 54999.0,
  "schwab_keyword_pct_of_xferout": 0.0,
  "gap_target_for_reference": 119000000,
  "keyword_vol_vs_gap_target_pct": 0.0,
  "exclusion_warranted": false
}
```

**Schwab keyword matches ($55K, 8 rows):**
All 8 rows are descriptions like "TRANSFER ACCOUNT SCHWAB US DIVIDEND EQUITY ETF"
— these are transfers of Schwab-branded ETF *positions*, not transfers *to* Schwab's
platform. The keyword search correctly identified these are not intra-Schwab flows.

S3: `s3://opal-data-bd/diagnostics/nnavar_phase5/20260306/transfer_out_desc_audit/`

---

## CRITICAL FLAG FOR DS: "Holding market value withdrawn" — $119.3M

The top Transfer Out description by volume is:

```
"Holding market value withdrawn"   4,106 rows   $119.3M   (81.9% of Transfer Out gross)
```

This single description accounts for **$119.3M** — matching the gap target to within
$0.3M (~0.25%). This is not a coincidence. It did not match the Schwab keyword
pattern (keyword search returned `exclusion_warranted: false` with only $55K),
but the amount precision is the answer we've been looking for.

**What "Holding market value withdrawn" likely represents:**
This description pattern is characteristic of a BD platform operation where an
account's position values are marked down/zeroed at the holding level before
a full account transfer or closure. It may represent:
  (a) Accounts departing to another custodian (Schwab or otherwise), where BD
      books the exit as a "holding market value withdrawal" rather than a standard
      ACAT Transfer Out
  (b) Internal BD account restructuring that doesn't correspond to real cash leaving
      the firm — Schwab would not count this as NNA
  (c) Model portfolio rebalancing events that BD records as a withdrawal + re-entry
      but Schwab nets to zero

**Implication:** If these rows represent exits that Schwab does not count as
NNA outflows (because they're internal to the BD/Schwab platform or represent
a book-keeping entry), excluding them would close the -$119M gap entirely.

**This needs a DS determination:** Is "Holding market value withdrawn" a real
cash outflow to a client, or a BD-internal accounting event? If the latter, it
should be added to the canonical exclusions in script 05.

---

## Blockers

Stopping per brief: `exclusion_warranted: false` → report to DS, do not run
`transfer_out_exclusion`. However, the "Holding market value withdrawn" finding
warrants immediate DS review regardless of the keyword gate.

---

## Current State

**Status:** COMPLETE (desc_audit only — exclusion suite skipped per gate)
**Active branch:** `CLOUD`

Phase 5 keyword test returned negative, but the description taxonomy reveals
that $119.3M of Transfer Out volume is described as "Holding market value withdrawn"
— an amount that matches the gap target to within $0.3M. This is the likely
explanation for the -$119M gap and requires DS confirmation of what this transaction
type represents in the BD/Schwab data model.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Determine what "Holding market value withdrawn" means**
   Is this a real cash outflow or a BD internal accounting entry? Check against:
   - BD documentation for this description pattern
   - Whether these rows correspond to accounts that appear in Transfer In flows
     at another custodian (if it's a departure, it would appear in the receiving
     firm's TOA inflows)
   - Whether Schwab counts these as NNA outflows in their system

2. **[DS/DT] If confirmed as non-NNA: add to canonical exclusions in script 05**
   Extended exclusion: Transfer Out rows where description = "Holding market value
   withdrawn" excluded from NNA calculation. This is a one-line addition to the
   canonical exclusion logic.

3. **[DS] If confirmed as real outflow: gap is structurally unexplained**
   With no remaining testable hypothesis, COO decides on Schwab-side data acquisition.

**Do NOT:**
- Run `transfer_out_exclusion` without DS instruction
- Add "Holding market value withdrawn" to canonical exclusions without DS confirmation
  that these are not real cash flows
