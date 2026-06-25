# Brief for CTO: Migrate the 49F Black Diamond EC2 Browser-Scrape to the DataMining REST API

**Author:** 3.0.0_SA_CVO
**Date:** 2026-06-25
**For:** 1.0.0_SA_CTO (architecture + PRD/decomposition)
**Requested by:** Andrew-direct 2026-06-25 ("we can do this through REST API, we've already established this... migrate the process over")
**Status:** brief for architecture intake -- not an implementation spec
**Priority:** P0 driver (49F BD bronze dark since 2026-06-19; served AUA silently degrading)

---

## 1. TL;DR

The 49F Black Diamond bronze ingest has been **dark since 2026-06-19** -- all four
BD-scraped silver tables (`allocations`, `transactions`, `realized`, `unrealized`)
froze the same day SS&C enabled **email-OTP MFA** on the `AndrewBerman49F` account,
which the headless Playwright scraper cannot satisfy. The gold lots chain keeps
running nightly on the frozen 06-19 silver, so **served 49F AUA is stale and
degrading, silently**.

We do **not** need to repair the browser scrape. We have **already built and proven
in production** the durable replacement: the **cot (Cottonwood) pipeline runs the BD
DataMining data pull as a pure REST API flow** (`cot_bronze_ingest.py`), and that
code is **firm-parameterized (Model B: shared code, per-firm data plane)**. Migrating
49F is therefore mostly **configuration + a 49F session/auth path + 49F templates** --
not a rebuild.

**The single hard problem is authentication, not data.** The data pull is 100% REST
and proven. The only browser step that remains is the **login that mints the
`.bd.identity` session cookie** -- and that login is exactly where the MFA gate bites.
The brief's core ask of CTO is to pick the auth strategy (Section 7); everything else
is a well-trodden port of an in-production pattern.

---

## 2. Why now (the P0 this resolves)

Grounded live via `comp-freshness` (2026-06-25):

| Silver table | Last modified | Status |
|---|---|---|
| `bd_silver_transactions` | 2026-06-19 21:57Z | FAIL (135h) |
| `bd_silver_allocations` | 2026-06-19 22:03Z | FAIL (135h) |
| `bd_silver_realized_agg` | 2026-06-19 21:46Z | FAIL (135h) |
| `bd_silver_unrealized` | 2026-06-19 21:41Z | FAIL (135h) |
| `bd_silver_canonical_prices` (yfinance, NOT scraped) | 2026-06-25 04:02Z | PASS |
| `bd_gold canonical_lots_*` | 2026-06-25 04:28Z | PASS (running on STALE silver) |

The selective freeze -- every BD-*scraped* table dead at one timestamp, every
non-scraped table fresh -- localizes the break to the **BD scraping ingest**, not any
compute bug. Root cause (memory `project_bd_scraping_broke_ssnc_mfa_20260619_api_bypass`,
proven by a live login screenshot from the box): SS&C added an email-OTP "Verify your
Identity" step-up on the 49F account; valid creds now land on an OTP challenge the
headless scraper times out on. Our stack was proven UNCHANGED at the break (scraper
code, SSM doc, secret, IAM all predate 06-19). It is purely the vendor-side MFA.

A monitoring gap compounded it: only `allocations` had a file-checker alarm, so
`transactions`/`realized`/`unrealized` failed **silently for 6 days**. The API
migration should fold a per-table freshness/absence alarm (the ASTN 4am-absence-check
pattern is a good reference).

---

## 3. Current state -- the 49F browser-scrape fleet (what we are replacing)

The 49F bronze ingest is a fleet of **per-table Playwright browser scrapers**, each on
its own EC2, triggered by a Lambda via SSM, that click through the BD UI
(login -> DATA MINING menu -> report select -> browser download-event):

| EC2 service | Instance | Role |
|---|---|---|
| `bd-allocations` | i-0800437d1dbb0b5cc | allocations (+realized/unrealized stepwise) Playwright scrape |
| `bd-transactions` | i-00c7568bc510f7423 | transactions Playwright scrape |
| `bd-fees` | i-0868fc7e7ebec26f2 | fees |
| `bd-assets` | i-0e6f6dc014fdcf1cd | assets dim |
| `bd-price-runner` | i-0800437d1dbb0b5cc | (shares the allocations box) |

- Code: `/opt/bd-exporter/src/stepwise/*.ts` (TypeScript/Playwright).
- Trigger: `bd-daily-trigger` Lambda -> SSM (SSM doc `opal-bd-allocation-download`).
- Creds: Secrets Manager `opal/bd/credentials` (49F account `AndrewBerman49F`).
- Output: `s3://opal-data-bd/forwardfill_v2/{table}/{TABLE}_DAILY_{date}.xlsx`.

Failure modes this design has ALWAYS had (pre-MFA): brittle UI selectors, modal/backdrop
interception (see `SCRAPER_FAILURE_ANALYSIS.md`, the 1/27+1/29 losses), browser
download-event flakiness, and now a hard MFA wall. Its own long-term-solution note
already said "replace Playwright with API."

**Key compatibility fact:** the downstream silver engine reads
`forwardfill_v2/{table}/...xlsx` and maps `silver column == to_snake_case(BD dimension
display-name)`. **The API ingest lands at the EXACT same S3 seam in the same xlsx
shape, so silver and gold need ZERO code change.** This is what makes the migration low-risk.

---

## 4. Target state -- the proven cot DataMining REST pattern

The cot pipeline already does this in production. Two components:

### 4a. Data pull -- `data/cot/scripts/bronze/cot_bronze_ingest.py` (pure REST, proven, hardened)

The reverse-engineered DataMining REST flow (Brief 1; auth reference
`docs/briefs/cot-har-auth-api-first-analysis-20260608.md`):

```
GET  /datamining/auth/token                      (Cookie .bd.identity) -> {access_token}
POST /datamining/request/v1/run    {template}    (Bearer)             -> {runId, resultGuid}
GET  /datamining/request/v1/run/{runId}/status   (Bearer)             -> {isComplete}
GET  /Api/DataMining/ExportResults/{resultGuid}  (Cookie)             -> xlsx bytes
```

It is **firm-parameterized (Model B)** -- the entire firm binding is four env vars:

| Env var | cot value | 49F value (to set) |
|---|---|---|
| `BD_S3_BUCKET` | `opal-data-cot` | `opal-data-bd` |
| `BD_FIRM_ID` | `cottonwood` | `49f` (label/provenance only) |
| `BD_SESSION_SECRET_ID` | `blackdiamond/cot/session` | a new `blackdiamond/49f/session` |
| `BD_BASE` | `https://bd3.bdreporting.com` | same (shared BD host) |

Already battle-hardened in cot (these are paid-for lessons the 49F port inherits free):
- **Persisted templates** tapped by id (no create-per-call); only date window re-stamped.
- **Per-table date modes** (`TABLE_DATE_MODE`): Custom 14d window; holidays/restatement
  handled. (The COTETL AUAFIX CurrentDay->Custom fix that recovered cot's frozen AUA.)
- **Holdings completeness floor** -- rejects an unvalued ($0-MV) early-day snapshot
  pre-land so a partial day never poisons silver.
- **Bronze-complete sentinel** emitted only on verified all-table success -> EventBridge
  fires the silver stage (no SSM-exit-0 false-advance).
- **Per-table isolation + fail-loud** on run errors.

Migrating it to bd is: set the four env vars + provide 49F templates (Section 6).

### 4b. Session/auth -- `data/cot/scripts/bronze/cot_bd_session_fetch.py` (Playwright LOGIN-only)

This is the ONE remaining browser step, and it is **login only** (not data scraping):
navigate -> OIDC login form -> capture `.bd.identity` + full cookie jar -> write to
Secrets Manager (`blackdiamond/cot/session`), TTL ~20h, keepalive. The bronze ingest
reads that cookie and mints the bearer. It already has **`FAILED_MFA_REQUIRED`
detection** -- it knows when MFA blocks it.

**This is the crux: the 49F account has MFA on; cot's account path works headless.**
The migration's real design decision is how 49F gets a valid `.bd.identity` into
`blackdiamond/49f/session` despite the email-OTP gate (Section 7).

---

## 5. The migration gap -- what is actually 49F-specific work

Because 4a is parameterized and 4b is a known pattern, the net-new work is small:

1. **49F session secret + auth path** (the hard part -- Section 7): stand up
   `blackdiamond/49f/session` and a reliable way to keep it fresh past MFA.
2. **49F DataMining templates**: capture the 49F query bodies (one real export per
   table via DevTools "Copy as cURL", or `--provision` against a live 49F session) and
   land `s3://opal-data-bd/code/bronze/templates/{table}.json` for
   `{allocations, transactions, realized, unrealized, holdings}`. The 49F template set
   may differ from cot's (49F has a far larger account universe + its own dimensions).
3. **Runner infra**: one `bd-exporter` API box (or Lambda -- the pull is light HTTP +
   xlsx passthrough; no browser needed for the data pull) replacing the 4-box scrape
   fleet, on the cot-exporter EventBridge->SSM model. Decommission the per-table scrape
   boxes after parity.
4. **Backfill 06-19 -> today** to un-freeze the 4 silver tables (the `--backfill
   --start --end` path) once auth is restored.
5. **Per-table absence/freshness alarm** closing the silent-failure gap (only
   allocations was alarmed).

Everything downstream of `forwardfill_v2/{table}` (silver merge, gold C-chain, served
AUA) is **unchanged** -- proven by the identical S3 seam.

---

## 6. Templates note

The cot templates live at `data/cot/scripts/bronze/templates/{table}.json` and are
ALSO mirrored to `s3://opal-data-cot/code/bronze/templates/`. They encode the persisted
`templateId`, the dimension/fact selection, and `dateRangeType`. 49F needs its OWN
captured templates (its account scope + selected measures differ). The
`--provision` flag in `cot_bronze_ingest.py` exists precisely for this: run once
against a live 49F session to create the persisted templates and print their ids.

---

## 7. The crux decision for CTO -- the 49F auth strategy

The data pull is solved. Pick how 49F maintains a valid `.bd.identity` session past
email-OTP MFA. Options (durable -> fastest), from the incident memory:

| # | Strategy | Pros | Cons / open question |
|---|---|---|---|
| **A** | **Ask SS&C to exempt the 49F service account from MFA** (or IP-allowlist our egress) | Fully durable; restores clean headless login; no OTP handling ever | Vendor-dependent; Andrew/relationship action; lead time unknown |
| **B** | **Inject a manually-captured post-MFA `.bd.identity` (+ `bd_DeviceRegistration` device-trust cookie) into the session secret**, skip login | Fastest restore (no code); reuses proven device-trust to skip future MFA | Cookie TTL/refresh cadence; who re-captures when it expires; is device-trust durable? |
| **C** | **Email-OTP automation** -- read the OTP from a mailbox and complete the step-up in the session-fetch | Fully automated, no vendor ask | Most build; couples to a mailbox; OTP-relay maturity (cf. the inf/Orion OTP-relay gating) |
| **D** | **Pure DataMining REST with a bearer minted from a maintained session** (Andrew's stated preference) | The clean target architecture; data pull already proven | Still needs A/B/C to *seed and refresh* the underlying `.bd.identity` -- auth is upstream of D |

**Important framing for CTO:** D is the data-plane target (and it's done). A/B/C are not
alternatives to D -- they are the **auth seed/refresh** that feeds D. The realistic
shape is **D for the pull + (A or B) for the session**, with C as the automated
fallback if A is slow and B's cookie proves short-lived. `bd_DeviceRegistration`
(device-trust) is the key unknown to probe: if injecting it makes headless logins skip
MFA durably, B becomes near-permanent and the cleanest path.

device-trust + cookie details, all HTTP-200-proven from Andrew's egress, are in the
incident memory and `cot-har-auth-api-first-analysis-20260608.md`.

---

## 8. Suggested phasing (for CTO to shape into a PRD)

- **Phase 0 (unblock, hours):** establish a valid 49F `.bd.identity` (B: manual cookie
  capture into `blackdiamond/49f/session`) -> run `cot_bronze_ingest.py` with the bd
  env vars + 49F templates -> **backfill 06-19..today** -> 4 silver tables un-freeze ->
  served AUA recovers. This alone resolves the P0.
- **Phase 1 (durable):** stand up the `bd-exporter` API runner (one box/Lambda) on the
  cot-exporter EventBridge->SSM model + the session-fetch refresh job; decide A vs B vs
  C for steady-state auth refresh; add the per-table absence alarm.
- **Phase 2 (cleanup):** parity-verify API vs the last good scrape, then decommission
  the 4 per-table Playwright scrape boxes (`bd-allocations`/`bd-transactions`/`bd-fees`/
  `bd-assets`) -- a real cost + reliability win.

---

## 9. Ownership / lanes

- **CTO:** architecture + PRD + auth-strategy decision (Section 7) + decomposition.
- **AE (infra/ingest lane):** the runner infra, SSM/EventBridge wiring, session-fetch
  job, template provisioning, backfill, scrape-box decommission. This is the
  `0.6.x_AE_PartnerETL` / `0.7.0_AE_CloudOps` pattern that already owns cot-exporter.
- **DS:** confirm the silver merge ingests the API-landed xlsx with zero change
  (expected -- same seam) and co-verify `source_system`/row-count sanity on first
  nightly.
- **CVO (me):** independent co-verification -- the 4 silver tables un-freeze
  (`comp-freshness`), row-count/magnitude/`source_system` sanity vs the last good
  pre-06-19 snapshot, and served-AUA recovery, on the first restored nightly.
- **Andrew:** the SS&C MFA-exemption ask (Option A), if elected; and the initial 49F
  cookie capture (Option B) since it's his account/egress that proved the flow.

---

## 10. Verification bar (CVO)

This is not "done" until, grounded on the SERVED/LIVE artifact:
1. All 4 `bd_silver_{allocations,transactions,realized,unrealized}` show a fresh
   (today-dated) partition, `comp-freshness` = PASS.
2. The restored rows are sane vs the pre-06-19 baseline (row counts within band,
   AUA magnitude plausible, no all-$0 / no schema drift).
3. Served 49F AUA reflects post-06-19 dates (the freeze clears end-to-end, not just bronze).
4. The per-table absence alarm is EGRESS-verified (fires on a missing table), closing
   the silent-6-day-failure gap.

Mechanism claims here (e.g. "MFA is the cause") are grounded INFERRED-but-strong
(date + selectivity + the live login screenshot); AE confirms the exact authn failure
at fix time. The FIX is well-defined regardless of that last confirmation.

---

## Appendix -- source grounding

- Proven REST ingest: `data/cot/scripts/bronze/cot_bronze_ingest.py` (read in full).
- Login/session: `data/cot/scripts/bronze/cot_bd_session_fetch.py`.
- Auth reverse-engineering: `docs/briefs/cot-har-auth-api-first-analysis-20260608.md`.
- Incident + API bypass: memory `project_bd_scraping_broke_ssnc_mfa_20260619_api_bypass`.
- Current scrape failure history: `data/black_diamond/archive/SCRAPER_FAILURE_ANALYSIS.md`.
- Live freshness: `comp-freshness all` (4 bd-scraped tables FAIL @06-19; non-scraped PASS).
- Current EC2 fleet: `infra/aws/ec2/EC2_MANIFEST.json` (bd-allocations/transactions/fees/assets).
- Templates: `data/cot/scripts/bronze/templates/{allocations,transactions,realized,unrealized,holdings}.json`.
