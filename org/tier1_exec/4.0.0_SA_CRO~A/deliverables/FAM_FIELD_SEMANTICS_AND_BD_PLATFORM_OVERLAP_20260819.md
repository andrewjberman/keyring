# FAM FIELD SEMANTICS + THE BLACK DIAMOND PLATFORM OVERLAP (4.0.0_SA_CRO~A, 2026-08-19)

**Commissioned:** two Andrew-directs, same hour -- (1) via CTO relay ~15:3xZ: per-field assessment of
fam ("it seems to me those are stable fields, not transaction events"); (2) live at this terminal
~1535Z (verbatim record committed): "use the most recent data we have for it" + check the Black
Diamond PLATFORM pull ("bd3") schedule + content for overlap with fam.
**Method:** estate reads only (silver parquet partitions, the landed BD bronze exports' HEADER rows,
the deployed Lambda's source, the applied EventBridge schedule). PII handled per charter: names/keys
never printed beyond field NAMES; all scratch copies deleted after measurement. Companion:
`FINDING_FAM_IS_A_SLOW_DIM_20260819.md` (the dynamics half).

---

## PART 1 -- FAM PER-FIELD SEMANTICS: the stable-fields read is CONFIRMED, no exceptions

Grounding: a01_dim_relationship.py:9-22 build-verified positional parse @HEAD + direct parquet reads
(partitions 2026-07-10 / 08-07 / 08-10).

| field | what it IS | identity or event? | evidence |
|---|---|---|---|
| col_1 | master grouping id (advisor-relationship layer) | IDENTITY | 19 distinct; 0 changes on shared accounts over a full month |
| col_2 | master grouping / firm name | IDENTITY | 8 distinct; 0 changes/month |
| col_3 | rep name | IDENTITY | 9 distinct; 0 changes/month |
| col_4 | account number (the key) | IDENTITY (key) | 8-digit, 1 row per account, all rows |
| col_5 | registration / holder name | IDENTITY | 5,084 distinct; the ONLY column that moved in a month: 2 of 7,050 (name corrections) |
| col_6 | household key | IDENTITY (SENSITIVE -- TIN-shaped; grouping-only, never emitted; a01 emits a hashed account-anchor) | 4,246 distinct; 0 changes/month |

**ZERO date fields, ZERO amounts, ZERO quantities/prices, ZERO event/transaction content.** All six
columns are text; nothing in the file can move with the market. The file is the account -> holder ->
household -> rep -> firm REGISTRY, republished daily as a full snapshot; the only motion is
membership (~5 accounts/business day). His read is confirmed field-by-field.

## PART 2 -- THE BD PLATFORM PULL: schedule, content, and the overlap verdict

**The vehicle (the "bd3" pull):** Lambda `opal-assets-bd49f-daily-pull`
(`infra/aws/lambda/opal-assets/opal-assets-bd49f-daily-pull/lambda_function.py` -- the D1 BD REST
datamining vehicle; auth = `blackdiamond/49f/session`, keepalive-maintained).
**Applied schedule (live EventBridge read):** `cron(30 6 * * ? *)` daily pull + `cron(30 8 * * ? *)`
re-attempt, both ENABLED. **Landing daily through 2026-08-18 (T-1) -- the BD platform feed stayed
LIVE through the entire Schwab FAM stoppage.**

**What it lands today** (`opal-data-assets/blackdiamond/49f/bronze/`):
- `allocation_390224/` -- the 92-column allocation export (daily, current to 08-18)
- `fees_435407/` -- fees-transactions (daily, current)
- `template_roster/` -- ⚠ NOT an account roster: the datamining TEMPLATE CATALOG (14 user + 29
  system + 4 compliance report definitions). Zero fam overlap in this feed itself.
- `reporting_*` -- ClientView endpoints, TAXSMA-scoped, stale since 07-17 (separate thread).

### The overlap verdict -- two axes, opposite answers

**FIELD-DOMAIN OVERLAP: CONFIRMED, AND RICHER THAN FAM.** The daily `allocation_390224` export's
92-column header carries the entire fam identity plane plus what fam lacks:

| fam field | BD allocation column(s) |
|---|---|
| account number (col_4) | **Original Account Number** (the Schwab custodial number -- verified join key) + Account Number / AccountID |
| grouping id/name (col_1/2) | Portfolio Group + PortfolioID / Portfolio Name |
| rep (col_3) | **Rep Code** (17 distinct) + the full 49F advisor-role model: **Architect / Consultant / Implementor / Local Ops / Additional Advisor, each with Split %** |
| holder/registration (col_5) | Account Name / Account Owner / Account Registration Type / Client Name |
| household key (col_6, TIN-shaped) | **Relationship ID** (BD synthetic z-key -- NOT a TIN; strictly better privacy) + Relationship Name / Display Name / SEC Client Type |
| (absent from fam) | Relationship Inception/Termination Date, Account Is Open/Closed Date, Account Type, Fee Schedule plane, Tax Status, Managed Account Manager |

**ACCOUNT-COVERAGE OVERLAP: PARTIAL -- 73.3%, structural in both directions.** Set-diff on the
2026-08-10 fam vs the 2026-08-18 BD export: fam 7,202 accounts | BD export 6,145 (8-digit) |
**in both 5,277 (73.3% of fam)** | fam-only 1,925 | BD-only 868. INFERRED characterization (stated,
not confirmed): fam-only = Schwab custodial accounts outside BD portfolio groups (closed/unmanaged --
the export is Account Is Open=True on 30,567 of 30,577 rows); BD-only = the firm's book at OTHER
custodians (BD is multi-custodial; fam is Schwab-only by construction). **So the allocation export
AS-SCOPED is not a fam substitute; the platform, however, natively holds the full domain:**

**The BD-native identity templates exist in the catalog, unpulled:** the system-template roster lists
**Firm Householding · Client Account Assignment · Firm User Account Assignment · Bulk Relationships ·
Account Registration Codes · Firm Contacts** -- exactly fam's content domain in the vendor's own
vocabulary, runnable by the already-proven vehicle. ⛔ Running ANY new template = a NEW vendor call
on bd/49f, which the standing lift does NOT cover (cot-BD only) -- **one Andrew egress word away,
not taken.**

## SYNTHESIS (for the card)

1. His stable-fields read: **CONFIRMED per field** -- fam carries no time-sensitive content; the
   most-recent-data carry is semantically safe (the SS6 decouple's basis, now field-grounded).
2. His BD-native suspicion: **CONFIRMED at the platform level** -- the identity domain lives
   natively in Black Diamond, a richer form of it already lands DAILY at 06:30Z, and it kept landing
   through the entire Schwab stoppage.
3. The immediately-usable half: for the 5,277 joint accounts, the daily BD export can serve as a
   FRESHNESS CROSS-CHECK on the carried fam (identity drift detectable at T-1 despite the stalled
   Schwab file) -- an ad-hoc read, no build implied.
4. The structural option (his call, one egress word): pull **Firm Householding + Client Account
   Assignment** via the proven vehicle to make BD the native source of the relationship dim and
   retire the Schwab-fam dependency entirely. Routes through CTO (one-producer-per-key: dim_relationship
   would change SOURCE, a P2/P3-class act, not a quiet swap).

**Routes:** 1.0.0_SA_CTO (frame) · 2.0.0_SA_COO (ledger) · Andrew's card (items 1/4).

---

## ADDENDUM (2026-08-19 ~1750Z, Andrew-direct at this terminal): the VALUE-LEVEL cross-reference -- last fam (as-of 08-10) x BD allocation identity plane (08-18), joint 5,277 accounts

**Method:** account-grain join on fam col_4 = BD Original Account Number; BD deduped to account grain
(138 of 6,145 accounts vary an identity column across group-rows -- 2.2%, surfaced not chased).
Aggregates only; scratch deleted. **Instrument honesty applied:** every mapping-consistency score is
reported AGAINST its majority-class baseline -- two first-pass "alignments" were DISCOUNTED as
baseline artifacts (the cannot-fail-instrument class, caught in-pass).

| comparison | result | verdict |
|---|---|---|
| **fam household (col_6) vs BD Relationship ID** | 96.8% of fam households sit fully inside ONE BD relationship; BD relationships are COARSER: 589 of 2,689 span 2+ fam households; 41.6% of joint accounts sit in a multi-household relationship | **REAL, structural: fam-household NESTS inside BD-relationship.** BD's grouping is the client-relationship super-grouping (multi-TIN: spouses/trusts/entities); fam's is per-taxpayer. Consistent hierarchies, not conflicting ones |
| **fam holder (col_5) vs BD name columns** | best = **Client Name**: 55.8% identical token-set, 92.1% at >=50% token overlap (registration-string variants explain the tail); Account Owner: 0% (different thing entirely) | **REAL: col_5 = the client name.** Baseline ~0 with thousands of distinct names |
| **fam rep/grouping (col_1/2/3) vs BD Rep Code / role columns** | Rep Code "consistency" 82.3% vs majority-class baseline **82.1%** -> NO signal; SEC Client Type 98.5% vs baseline 98.5% -> NO signal (both DISCOUNTED) | **NOT ESTABLISHED.** fam's rep layer and BD's role model (Architect/Consultant/Implementor/Local Ops + splits) are different vocabularies; the correspondence is exactly what the queued Firm User Account Assignment probe target answers |
| universe | 2 of fam's 9 reps have books ENTIRELY outside the BD export; 1,925 fam-only accounts | fam's irreplaceable content is UNIVERSE, not fields |

**RICHER: BD, decisively, at account grain** -- 36 registration types + 15 account types (vs fam's
one free-text string), the four-role advisor model with split %s (vs one rep name), relationship
names + SEC type + inception/termination dates + open/closed + fee plane (fam: none of these), and a
household super-grouping that cleanly CONTAINS fam's. **What fam alone still carries:** the full
Schwab custodial universe (1,925 accounts + 2 rep books) and the TIN-keyed per-taxpayer grain (which
BD's synthetic nesting reproduces at 96.8% without exposing a TIN). The rep-layer mapping is the one
open cell; it rides the already-queued probe.
