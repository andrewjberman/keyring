# AMGT_RESAPP -- the SA Lambdas, the peer-set question, and the IR scan

**Author:** `4.0.0_SA_CRO~Z` | **Date:** 2026-09-10 | Options 2(check), 3 and 4 of the
`/next-calls` set. All three measured under Andrew's 2026-09-10 egress grant.

---

## 1. THE SA LAMBDAS -- they ARE there; what is missing is their DECLARATION

**Andrew's ask:** *"Check on the lambdas, rectify as needed, if they are not there then note that we
need them."*

**All 7 exist and are `Active`** in `us-east-1`, runtime `python3.12`:

| Function | State | Last modified |
|---|---|---|
| `seeking-alpha-analysis-coordinator` | Active | 2026-02-23 |
| `seeking-alpha-analysis-listing-parser` | Active | 2026-02-23 |
| `seeking-alpha-analysis-scraper` | Active | 2026-02-23 |
| `seeking-alpha-analysis-dedup` | Active | 2026-02-23 |
| `seeking-alpha-news-coordinator` | Active | 2026-02-18 |
| `seeking-alpha-news-dedup` | Active | 2026-02-18 |
| `seeking-alpha-news-scraper` | Active | 2026-02-23 |

**DENOMINATOR: 7 of 7 present. Nothing needs re-creating.**

⛔ **THE ACTUAL GAP: `infra/aws/terraform/seeking-alpha/main.tf` DECLARES ZERO
`aws_lambda_function` RESOURCES.** Its 15 declared resources are **all scaffolding** -- 2
`aws_cloudwatch_event_rule`, 2 `aws_cloudwatch_event_target`, 2 `aws_lambda_permission`, 1
`aws_iam_role`, 1 `aws_iam_role_policy`, 7 `aws_cloudwatch_log_group`. **The functions and their
code are unmanaged**, which is exactly what the graph's `LIVE-no-DECLARED` drift was reporting.

**THE CONSEQUENCE IS A DEPLOY DEAD-END, and it is worth stating plainly:** CLAUDE.md forbids
`aws lambda update-function-code` (Terraform only), and Terraform has no `aws_lambda_function` to
apply. **So a code change to any of these seven currently has NO sanctioned deploy path.** They were
hand-deployed in Feb 2026 and have drifted since.

**RECTIFICATION -- NOT DONE, AND OUT OF THIS SEAT'S LANE.** The fix is to add
`aws_lambda_function` blocks and `terraform import` the seven live functions, bringing them under
management without recreating them. That is an `AE_CloudOps` act under `safe-apply` with a deploy
ledger entry. **Noted, per Andrew's instruction, rather than half-applied.**

> **BUT READ THE PRIORITY HONESTLY:** Andrew's SA design is a **symbol-page one-shot**, which is NEW
> code for AMGT_RESAPP, not these Lambdas. These seven are **archive producers for a parked
> estate**. The undeclared-Lambda gap is a real estate defect and should be fixed on its own merits
> -- but **it does not block AMGT_RESAPP**, and AMGT_RESAPP should not wait on it.

## 2. OPTION 3 -- are peer sets formulaic or analyst judgment? BOTH ANSWERS ARE WRONG.

**Population: all 54 `*ONE PAGER*.xlsx` workbooks across the 89 name folders.** Method: read each
`CSC` sheet, extract Bloomberg-format tickers, score overlap against the peer set found on the SAP
sheet that first raised the flag.

| Outcome | n | % |
|---|---|---|
| **Carries the STALE telecom peer set** | **48** | **88.9%** |
| Has its own name-specific peer set | 4 | 7.4% |
| No `CSC` sheet | 2 | 3.7% |

**The 48 all carry KPN's telecom comps** -- KPN, Vodafone, BT, Orange, Telenor, Telekom Austria,
Rogers, Telus, Swisscom, AT&T, Verizon, Telefonica -- on ASML, AstraZeneca, BP, Boeing, Costco,
Hermes, Home Depot, ICICI Bank, Copa, Intuit, JD.com and 37 others. **It is unrepointed template
residue, copied forward from a KPN workbook.**

**The 4 real ones are unmistakably JUDGMENT, not a screen:**

| Name | Peer set |
|---|---|
| Imperial Brands | IMB LN, BATS LN, 2914 JT (Japan Tobacco), PM US, MO US |
| Kimberly Clark | KMB, PG, CL, CHD, CLX |
| Lenovo | 992 HK, 2357 TT (Asus), DELL, HPQ, 2353 TT (Acer) |
| Petrobras | PETR3 BZ, XOM, CVX, BP/ LN, TTE FP, SHELL NA |

Each is cross-listed, sector-correct and deliberately chosen. **No sector/size screen produces
"Japan Tobacco" for Imperial Brands or "Acer" for Lenovo.**

**=> THE ANSWER: `peers.basis` is `analyst` when populated -- and it is populated 7.4% of the time.
The DEFAULT STATE OF THE CORPUS IS WRONG.**

**THREE CONSEQUENCES:**
1. **The corpus cannot be a source of truth for peer sets.** Any AMGT_RESAPP feature that seeds
   peers from existing packs would inherit KPN's comps for 48 names.
2. **This is a live data-quality defect in circulating research, not a modelling nicety.** My
   earlier SAP flag was not an anomaly -- it was the 89% case. **Under Call 5 I cannot raise it with
   Adam; Andrew is the only route.** ⚠ Whether the stale sheet reaches the PRINTED pack is
   **UNVERIFIED** -- the docx pastes Excel output as an image and I have not traced which image is
   the COMMON STOCK COMPARISON. That check should happen before anyone concludes packs shipped
   wrong.
3. **It strengthens the automation case rather than weakening it.** A *derived* peer set
   (sector/size/geography) would be more correct than the status quo for 48 of 54 names, even
   though it is a weaker instrument than a good analyst's set.

## 3. OPTION 4 -- the IR-page scan works, with one trap

**Andrew's Call 4 ruling:** *"We can do a scan for IR pages associated with the 89 and enumerate
from there."* **Mechanism proven on one name** (`SAP SE investor relations`), zone `serp_opal`,
`brd_json=1`: **HTTP 200, 18.4 KB, 10 organic results, all correctly SAP IR.**

Payload shape: `general`, `organic`, `navigation`, `pagination`, `related`. Per result:
`rank`, `global_rank`, `title`, `description`, `source`, `display_link`, `link`, `icon`.

⛔ **THE TRAP -- USE `display_link`, NEVER `link`.**

```
link          = "https://www.google.com/goto?url=CAESXQHrOzAVF9lj1b1vpvIweuT15IjwMWDJ..."   <- OBFUSCATED REDIRECT
display_link  = "https://www.sap.com > investors"                                           <- THE REAL DOMAIN
source        = "SAP"
```

**`link` is a Google redirect wrapper carrying no resolvable domain.** An enumerator built on the
obvious field would store 89 unresolvable URLs and look like it had worked. `display_link` carries
the real domain plus a path breadcrumb; `source` carries the site name.

**Not run at scale.** One name proves the mechanism; the full 89 is ~89 SERP calls and should be
run as a bounded job that writes to `opal-data-research` on first pull (Andrew's
"store it so we dont need to do it twice").

## 4. NOT MEASURED

- Whether the stale `CSC` sheet propagates to the printed packs (s2, consequence 3).
- The SERP scan at scale, and how many of the 89 resolve to a genuine IR domain vs a data-aggregator
  page. **The ex-US names are the risk** -- the same identity problem the SA symbol mapping has.
- Whether `terraform import` of the seven Lambdas would surface further config drift.
