# ETFS_RIVALS FAST lease -- CVO grades of landed pins (3.0.0_SA_CVO~RV)

- Lease: FAST from 2026-10-02T05:08Z to 17:08Z, seat `2.0.0_SA_COO~RV` (`org/mcp/drive-mode.log` line 56, msg 28219).
- Grading rule (`/closer-drive` Review, `/closer` Step 4): PASS, FAIL or NOT_EVALUATED, graded on the real run's artifact,
  never on static markup. Offline success is never a served PASS. A FAIL becomes the builder's next item.
- This file is overwritten per grade. Its history is git.

## Grade 1 -- the A1 drain @7aa0186d45 (pt-1, pg-1, rk-1, tb-1, ic-1, ai-1, ai-2, wiring), read at CLOUD e950e5157e, 2026-10-02 ~06:55Z

**Verdict: NOT_EVALUATED.** No real run exists yet: STATUS.md item 9 is not done and the pin table reads "none yet". The
served page is unchanged: `platinum/page/date=2026-10-01/manifest.json` reads generated_at 2026-10-01T22:03:35Z, batch
d5-publish-a1, 12 of 13 updated, page_version publish_page/2.

**Offline evidence (this seat's runs, CLOUD e950e5157e):**
- All 12 A1 acceptance checks read `RESULT: PASS 0 failures`, each rc=0: pt-1.AC1, pg-1.AC1, pg-1.AC2, rk-1.AC1, tb-1.AC1,
  ic-1.AC1, ic-1.AC2, ai-1.AC1, ai-1.AC2, ai-2.AC1, ai-2.AC2, ai-2.AC3. Two of them (ic-1.AC2, ai-1.AC2) read live S3
  read-only; the rest are offline.
- The package suite reads 359 passed, 2 skipped, 0 failed.
- The checks are the builder's own. None of the twelve is a judgment criterion, so this run has no plausibility oracle.
  The page's look and the AI text get their first independent read at the real run.

**What the real run must show for a PASS (read from the code at HEAD, not predicted from the checks):**
1. The publish Lambda's role holds the A1 grants. `policies/rivalfunds-publish-page-lambda.json` names Put on
   gold/{holding_contribution, buying_trend, input_census} and Get on the market readings. The generating commit
   556a61986d says "PLAN input, not applied", so an un-applied role makes `produce_a1()` record FAILED and the page show
   each table as not available (`publish_page.py:251-273`). Such a page publishes, but it does not demo FWD-14/15/20.
2. `produce_a1()` runs three producers inside the 900 s publish Lambda (`generated.auto.tfvars.json`). tb-1 reads G5
   history from 2024-10-01. The real run's duration is read against 900 s.
3. The served manifest names each A1 table's status, and the page renders the components first (pg-1). I read the
   served HTML, not the fixture.
4. ai-2's prompt revision 38ec58bc5a sits on `rv-fast` and is not drained at this read. AI accounts are not produced by
   `produce_a1()` ("a vendor call is its own act"), so FWD-16/17 on the served page depend on a separate act.

-- 3.0.0_SA_CVO~RV
