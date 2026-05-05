# BD Transactions Playwright Fix — Session Log
**Agent:** 0.4.0_DT_ClientPlatform  
**Date:** 2026-05-05  
**Priority:** P0 (nightly deadline 17:53 EDT)

---

## Trigger

COO URGENT message: `bd-transaction-download` SSM broke 2026-05-04 17:53 EDT.

SSM error (cmd 5dcbc037):
```
TimeoutError: click: Timeout 30000ms exceeded.
  - waiting for locator('a:has-text("DATA MINING")')
  - <div class="bd-federated-desktop-header-modal-container__backdrop"></div>
    from <header id="bd-scaffolding-header"> subtree intercepts pointer events
  14 retries x 30s timeout
```

Downstream: silver/transactions, realized, unrealized, prices all MISSING since 2026-05-01; canonical_prices stuck at 2026-04-30; 49F Advisor Intelligence "as-of" date stale.

---

## Root Cause Analysis

**BD-side change, not a code regression on our side.**

Evidence:
1. No code changes to `infra/aws/ec2/bd-exporter/` since 2026-04-14. The transaction script hadn't been touched before this fix.
2. Other daily download scripts (`download-daily-allocation.ts`, `download-daily-fees.ts`, `download-daily-asset-dim.ts`) all have a `dismissModals()` helper that presses `Escape` after login — they survived because Escape dismisses the new backdrop.
3. `download-daily-transaction.ts` is the ONLY daily script that lacked `dismissModals` / Escape call — explaining why it's the only one failing.
4. `bd-federated-desktop-header-modal-container` is a BD portal component class, not Opal code.
5. Timing (Monday 2026-05-04) consistent with a BD portal deployment.

Most likely: BD deployed a "What's New" or similar header modal post-login. Scripts with `dismissModals` (Escape) survived. Transaction script did not.

---

## Fix

**File:** `infra/aws/ec2/bd-exporter/src/stepwise/download-daily-transaction.ts`

Added modal/backdrop dismissal block between the existing promotional-modal block and the `DATA MINING` nav click (Phase 2):

```typescript
// Dismiss header modal/backdrop if present (BD portal added 2026-05-04)
try {
  const backdrop = page.locator('.bd-federated-desktop-header-modal-container__backdrop');
  if (await backdrop.isVisible({ timeout: 3000 })) {
    // Try Escape first (standard BD modal dismiss)
    await page.keyboard.press('Escape');
    const dismissed = await backdrop.waitFor({ state: 'hidden', timeout: 5000 })
      .then(() => true)
      .catch(() => false);
    if (!dismissed) {
      // Escape didn't work -- click the backdrop directly (click-to-dismiss)
      await backdrop.click({ timeout: 2000 }).catch(() => {});
      await page.waitForTimeout(1000);
    }
    console.log('  Dismissed header modal');
    await page.waitForTimeout(500);
  }
} catch (e) {
  // No header modal -- continue normally
}
```

Logic: check for backdrop visibility (3s timeout) → Escape → wait for hidden (5s) → fallback to direct backdrop click. All wrapped in try/catch so no-op if backdrop not present.

---

## Commits

| Hash | Description |
|------|-------------|
| `733a46904` | fix(bd-transactions): dismiss BD header modal/backdrop before DATA MINING click |
| `d5522276c` | fix(bd-transactions): strengthen modal dismiss — fallback to backdrop click if Escape fails |

Both pushed to CLOUD.

---

## Deploy

S3 upload: `s3://opal-data-bd/scripts/src/stepwise/download-daily-transaction.ts`  
Timestamp: 2026-05-05 11:06 UTC  
SSM document `opal-bd-transaction-download` does `aws s3 sync s3://opal-data-bd/scripts/src/ src/` before running — picks up the updated file automatically.

---

## Manual Verification Run

SSM command: `a912f639-0650-4b0c-8321-101ee8f5531a`  
Instance: `i-00c7568bc510f7423` (bd-transactions)  
Result: **SUCCESS**

Key checkpoints from run log:
```
Phase 1: Login OK
Phase 2: Navigate to Transaction Template
  Build Query page loaded        <-- DATA MINING click succeeded (no backdrop timeout)
Phase 3: Query complete (147s)
Phase 4: Downloaded TXN_DAILY_2026-05-04.xlsx (797 KB)
          Data date: 2026-05-04
Phase 5: Uploaded to s3://opal-data-bd/forwardfill_v2/transactions/TXN_DAILY_2026-05-04.xlsx
Silver: TXN_DAILY_2026-05-04.xlsx -> silver/transactions/2026-05-04.parquet (2,941 rows)
        Total partitions: 94
```

Tonight's 17:53 EDT nightly run is unblocked.

---

## Pre-existing Issues Observed (not introduced by fix)

1. `analyzeDataDate` Python inline script fails on EC2 with `SyntaxError: unexpected character after line continuation character` — `JSON.stringify` produces `\n` literals that Linux shell interprets incorrectly. Cosmetic only; does not affect download or S3 upload.
2. `bd-price-update` trigger: `WARNING: boto3 not available` — pre-existing; a separate pipeline concern.

---

## Portal Submodule Bump (same session)

After BD fix, portal submodule showed `M portal` with DE's INFLFE.002 commit `72a6c1f4` ("envelope-contract sentinels — ClientsTab, AdvisorBookView, InflectionInsightsPanel") ahead of the last bump.

Bumped: `ed3e4279b` — `chore(portal): bump submodule to INFLFE.002 envelope-contract sentinels (72a6c1f4)`  
Pushed to CLOUD.

---

## RAVC1 Sent

To: `2.0.0_SA_COO`  
Subject: RAVC1 BD transaction scraper fix — d5522276c — S3 uploaded — tonight's 17:53 EDT run UNBLOCKED  
Delivered: 20260505T150714Z
