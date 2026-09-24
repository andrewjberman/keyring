# AMGT_RESAPP round 22 -- the COO's drain-end packet to `3.0.0_SA_CVO~Z`

**From:** `2.0.0_SA_COO~Z`. **Vintage:** SITEZ after `543d2561cb`, LOCAL; the push is `0.0.0_AB_MSTR~Z`'s (LD-0522).
**Written:** 2026-09-22 ~06:0xZ.

**DRAIN-END, complete:** 6 of 6 terminal, 0 open.
- Issued as one slug @`f7fcf11592`, per msgs 24119, 24123 and 24125 (M4 moved to chain G).
- The moves ran as a sequential chain. Each CTO half was signed against the state the prior move left: rk-90 @`e803978fc3`, rk-91 @`1b9eb552c3`, rk-92 @`a74268ba4d`.

## 1. Round state, final

| cell | drain | second instrument (this seat's own) |
|---|---|---|
| rk-87 H4 Lusha silver writer | `597abf6c7a` | module surface read directly: no bronze-capable name; KEPT_FIELDS is 12 names, none a contact field; `lusha.store is store`. harvest 37 passed. (A probe with a hand-built record did not match Lusha's shape and produced 0 rows, so it is NOT counted as a leak test; the worker's 9 arms cover the real shape.) |
| rk-88 H5 SERP writer | `b48fe0cd6b` | branch scope read; harvest 46 passed on the merged tree; the module has 1 importer, its own test |
| rk-89 PROD promote (`0.2.0_DT_PortfolioAnalytics`) | DT commits `058d62973d` / `75de778a8a` / `6c64d69977` | portal `ls-remote`: PROD `6dfc33909e` = tag `portal-v2.1.182^{}` (peeled match); origin/PROD contains `f22e369c` (rk-78 + rk-80); `App.tsx` diff 07d5af72..PROD empty; opalinvest.dev 200. The DT seat's AC6 counted the 3 new literals in the served chunks. The ledger was opened BEFORE the push |
| rk-90 M1 `raw/bloomberg` | `e995453666` | 119 of 119 objects copied (110 bronze, 9 pull_log state), sha-equal; the CTO read them back independently. The window condition held: 119 objects, newest 16:25:37Z. Adapter at `stDlDaeG...` after the move |
| rk-91 M2 filings `.source.json` | `96045cc865` | paginated counts: filings/v1 206 (194 source, newest 17:22:08Z, plus 12 analysis) UNCHANGED; `sec` and `issuer-site` filing_source 1 part each; filing_attempt 180. Thesis leaf for CAT, CSL and 6861: 200. Scoped policy: filings/v1 ABSENT, filing_attempt PRESENT |
| rk-92 M3 `raw/seekingalpha` | `33ea2e4e00` | adapter `cRT7dOyf...` Active/Successful; raw/seekingalpha 18 objects UNCHANGED; seeking-alpha/harvest/bronze 18; all 13 GET routes invoked with REAL params (see s.2 item 4) |

Every live act (rk-89 through rk-92) had its deploy ledger opened before the first live write and closed on the read-back. No rollback fired. No S3 object was deleted.

## 2. For the grade

1. **rk-90: four issuer-text defects, all this seat's.**
   - AC3 used a `deploy_ledger --legs` flag that does not exist.
   - AC6 ran `safe-apply ... plan`, which safe-apply refuses.
   - AC1: a test pinning `raw/bloomberg` sat outside `<paths>`.
   - AC6's policy hash used default separators and was compared against a compact-separator digest (W90-S6).

   The CTO ruled an amendment (msg 24133) and a fresh ~90 re-graded; no live act was re-run. Each lesson was carried into M2's and M3's briefs.
2. **rk-91: two live incidents, both fixed the same turn.**
   - `Z-S213` is an EXPOSURE: the grant add and a redeploy ran before the copy, with 0 invocations.
   - `Z-S214` is an INCIDENT: 4 served 500s from a `lib.opal_naming` import outside the adapter closure, the M1 class again. PROD was gated to Andrew and third-party traffic was 0.

   The remedy is the CTO's ruling (c), under which the adapter imports GENERATED new-grammar constants (`_harvest_prefixes.py`, built from `address()`), plus a binding pre-deploy closure check on every adapter order.
3. **rk-92: AC7 stopped the deploy on a FALSE POSITIVE of this seat's check design.**
   - The isolated interpreter excluded boto3, which the python3.11 Lambda runtime provides.
   - It was corrected at L5 within the ruling @`081792416a`: the runtime package set is included, and isolation is proven by `lib` resolving inside the artifact and repo-only modules (the naming builder, the store, pyarrow) being unimportable.
   - The CTO accepted the correction (msg 24141). On the re-run, AC7 passed 4 of 4 arms before any deploy.
4. **FOUND AT M3's DRAIN, NOT CAUSED BY M3: row `Z-S215` (ARMED).**
   - The PRINT route serves a 500 for all three validation names (CAT, CSL, 6861); BA and COST return 200.
   - Cause: `render_pack.py:264` sorts model-block fiscal years of MIXED type. Historical years are stored as str ('2016'..'2025') and forecast years as int (2026, 2027).
   - This seat reproduced it box-side on PRE-M3 code (@`a74268ba4d`).
   - rk-92's worker saw 2 of 13 routes return 400, but that came from synthetic path parameters. With real parameters those two routes return 200; the print route is the real fault.
   - Routed to the CTO for round 23.
5. **rk-89 row `Z-S210`:** this seat's order told a Tier-2 addressee to use a row-id form the gates refuse. Recorded in `Z-S211`.

## 3. Rows (this round)

| row | disposition |
|---|---|
| Z-S208, Z-S209 (DT seat) | INERT, for L9 |
| Z-S210 / Z-S211 | Z-S201 disarmed by Z-S211; the row-id defect is recorded there |
| W88-S1 (multi-page SERP rows cannot carry their exact page) | OPEN, owner this seat: the wiring cell must use max_pages=1 or refuse |
| W88-S2 | dismissed |
| W90-S1..S6 | S2 disarmed by S5; S1, S4 and S6 are issuer-text defects; S3 fixed the same turn |
| Z-S212 (3 artifact versions against the 1 named) | INERT; the "one or more builds" wording is now standard |
| W91-S1..S3, Z-S213, Z-S214 | as in s.2 item 2 |
| W92-S1 / S2 | S1 disarmed by S2 |
| **Z-S215** | **ARMED**, owner the CTO; see s.2 item 4 |

## 4. What this seat asks of L9/L10

- Grade the 6 terminal cells on their branch-HEAD criteria. None carries a judgment criterion.
- **Standing practice from this round:** run test suites ONE pytest call per directory. A multi-directory call trips the W85-S1 module-identity clash, 10 failed of 178.
- **Candidates for round 23:**
  - Z-S215's print fix. REC: sort on a normalised key in `render_pack`, which is an adapter redeploy under a pair with the closure check. The producer-side string normalisation belongs in chain G.
  - The backfill runs B1..B5, which need Andrew's GO and his vendor/EDGAR words. The CTO cards those now that M1..M3 have read back.
- **Chain G, recorded in s.30b:** model_block, M4 publications, filings `.analysis.json`, the chatter carry-along (rk-68, rk-76), the chatter `bloomberg/harvest/silver/` grant, and the generated Terraform IAM prefix list.
