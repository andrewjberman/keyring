# E -- EXEC MGMT (PEOPLE), SERP AND SOCIAL: field-level channel map

Scope: Lusha, the management document build (filing roster + Bloomberg fallback + Lusha + CEO search), Bright Data
SERP, Bright Data social (Reddit), and any other search-style operation in `lib/research`. READ-ONLY. No vendor call
made. Every personal value is redacted to its SHAPE. S3 reads: 4 `management/v1` objects, 1 `social/v1/_measurement`
object, 1 Bloomberg `exec_officers` bronze object (downloaded to scratch only). Code at working tree, branch SITEZ,
HEAD `78106b9cea`.

Relied-on prior inventories (verified, not re-derived): `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/RESAPP_DATA_SHAPE_INVENTORY_20260918.md`
s.2 #8 (management skeleton, `:161-171`) and #22 (social measurement, `:330-342`);
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/PLAN_AMGT_HARVEST_CHANNEL_FORMATS_20260921.md` s.5.6-5.8 (`:325-382`).
Where this map differs from them it says so (both predate round 25-27 code and the 09-19/09-21 management writes).

## Live object counts (measured 2026-09-22, `bash .tools/aws s3 ls s3://opal-data-harvest/<prefix> --recursive | wc -l`)

| Prefix | Objects | Note |
|---|---|---|
| `lusha/` (any tier) | **0** | `lusha/harvest/silver/contact_match/` never written |
| `bright-data/` (any tier) | **0** | covers `bronze/serp/`, `silver/serp_result/`, `bronze/social_snapshot/`, `silver/social_post/` |
| `management/v1/` | **18** | 15 per-name objects (15 names, one date each: 09-15 x5, 09-18 x7, 09-19 x3) + 3 `_pool/` |
| `social/` | **1** | `social/v1/_measurement/2026-09-15.json` |
| `bloomberg/harvest/bronze/exec_officers/` | 4 | 2 names x 2 stamps (CSL_AU, 6861_JP) |
| `raw/bloomberg/**/exec_officers.json` (legacy) | 4 | still referenced by served `fallback.raw_key` |
| `bloomberg/harvest/silver/` | 0 | no `executive_officer` silver |

---

## CHANNEL 1 -- LUSHA (officer profile-link enrichment)

### 1.1 Channel
- Vendor Lusha, **REST API** `POST https://api.lusha.com/v3/contacts/prospecting` through the estate client
  `data/find/imo/scripts/_util/lusha_client.py` (`LUSHA_API_BASE` `:93`, `_execute` `:369-451`, header `api_key`,
  `contacts_prospecting` `:537-570`). Credits from `billing.creditsCharged` (`:464-465`).
- **TWO call paths exist, and they do not share a writer:**
  1. **Legacy / the one that produced every served value:** `lib/research/management/enrich.py::build_document`
     (`:635-726`) -> `prospecting_page` (`:308-347`) -> `scrub` (`:91-114`) -> `attach_profiles` (`:377-399`).
     Result folds into the management document (`officers[].profile_url`, `officers[].lusha_title`,
     `officers[].enrichment`, `lusha_enrichment` block). **Writes no Lusha silver.**
  2. **Round-25 public entry point (AMGT-rk-99, B4):** `lib/research/harvest/lusha.py::harvest_company`
     (`:177-216`), CLI `python -m lib.research.harvest.lusha --security-key K --run-stamp S [--since ISO] [--write]`
     (`_cli` `:219-242`). Reaches the client via the public seam `enrich.lusha_client` (`enrich.py:287-292`), reuses
     `enrich.prospecting_page` and `enrich.scrub`, builds rows through the allow-list, runs the
     C-LUSHA-EXCEPTION guard on every call, and writes silver ONLY with `write=True` (default OFF). **No importer
     outside its own tests** (Grep over `**/*.{py,cmd,ps1,sh}` for `harvest.lusha`: only `lusha.py`, its 2 tests, and a
     `.scratch` draft). It does NOT write back into `management/v1`.
- Trigger/cadence: none scheduled. Billed per use; PRD `C-EXEC-MANAGEMENT` `:824` "runs only under Andrew's per-use
  word". Weekly Windows task `OpalResearch-ExecManagement` (`batch.py:13-18`) is created DISABLED.

### 1.2 Request shape (from code, `enrich.py:321-327`)
```
POST /v3/contacts/prospecting
{ filters: { companies: { include: { domains: [<company_domain:str>] } },
             contacts:  { include: { seniority: [9] } } },          # 9 = C-suite (card 2), SENIORITY_C_SUITE :55
  pagination: { page: 0, size: 50 } }                                # LUSHA_PAGE_SIZE :54
```
Fallback on refusal/zero: the estate client's unfiltered call (`enrich.py:342-343`, body `lusha_client.py:569-570`:
domains filter only). Credit bound 2 per name (`CREDIT_BOUND_PER_NAME` `:53`); measured charge is recorded, not clipped
(`:669-679`).

**Domain source:** `enrich.domain_for` reads `lib/research/management/domains.json` (`:140-148`) -- **5 names declared**
(BABA_US, BA_US, COST_US, HD_US, SAP_GY; row fields `company_domain`, `ir_domain`, `entity`, `source`). Both Lusha
paths use it (`build_document :643`, `lusha._cli :238`).

### 1.3 Response shape (vendor, as received -- from the stub fixture
`data/find/imo/scripts/_util/fixtures/lusha_responses/contacts_prospecting_happy.json`, shape only)
```
requestId: str
pagination: {page:int, size:int, total:int}
results[]: {
  id: str                         # -> person_id (also accepts personId / contactId, lusha.py:50)
  firstName: str  lastName: str   # personal name
  jobTitle: {title: str, departments: list[str], seniority: str}
  company:  {id: str, name: str, domain: str}
  location: {country: str, state: str, city: str}
  socialLinks: {linkedin: str(url)}
  has: list[str]                  # which contact kinds exist (e.g. email/phone flags)
  canReveal: {credits: int}
}
billing: {creditsCharged: int, actions: {api_search: int}}
+ HTTP headers x-rate-limit-*/x-*-requests-left/x-*-usage
```
No email/phone values arrive on prospecting (they need `/v3/contacts/enrich`, which nothing in this package calls --
`enrich.py:16-19`).

### 1.4 Storage and field dictionaries

**Bronze: NONE, by rule.** `C-LUSHA-EXCEPTION` PRD `:926-932`; enforced at `store.bronze_put` (`store.py:222-223`,
raises `LushaExceptionError`).

**Silver `lusha/harvest/silver/contact_match/date=YYYY-MM-DD/part-<run_stamp>.parquet`** -- live 0 objects. Record key
`(domain, person_id)` (`lusha.py:40`). Row = exactly `KEPT_FIELDS` (`lusha.py:45-48`) + `record_hash` added by the store
(`store.py:361-368`):

| field | type | null | shape | meaning / derivation |
|---|---|---|---|---|
| domain | str | no | `"example.com"` | the queried company domain |
| endpoint | str | no | `"contacts/prospecting"` | const |
| person_id | str | no | `"<vendor id>"` or `"__no_result__"` | `id`/`personId`/`contactId`; sentinel row on a zero-result fetch (`:103-112`) |
| first_name, last_name | str | yes | `str (redacted)` | ASCII-folded (`_fold` -> `roster.asciify`) |
| job_title | str | yes | `str` | `jobTitle.title` folded |
| seniority | str | **always null** | -- | see hazard H-L3 |
| profile_url | str | yes | `url (redacted)` | `socialLinks.linkedin` ONLY |
| matched_officer | str | yes | officer name (redacted) | roster officer that `enrich.name_matches` accepted (surname equal + given name equal or initial, `enrich.py:357-374`) |
| results_total | int | yes | `int` | `pagination.total` |
| fetched_at | timestamp tz | no | `2026-..Z` | lineage |
| bronze_key | null | always | -- | null by rule, validated `store.py:333-336` |
| record_hash | str | no | sha256 hex | store-computed over non-lineage fields |

Dropped at silver (allow-list): `company.*`, `location.*`, `has`, `canReveal`, `jobTitle.departments`,
`jobTitle.seniority`, `requestId`, `billing`. Double guard: `_assert_no_contact_field` (`lusha.py:162-174`) +
`store._validate_silver_row` contact-name refusal (`store.py:339-345`) + `enrich.scrub` before rows are built.

**Folded into served `management/v1/<security_key>/<as_of>.json`** (legacy path only):
- per officer: `profile_url` (url|null), `lusha_title` (str|null), `enrichment` enum `MATCHED | ABSENT | NOT-ATTEMPTED`
  (`attach_profiles :381-397`; `NOT-ATTEMPTED` when no domain `:681-683`, and for every Bloomberg-fallback officer
  `:621`).
- `lusha_enrichment` block (schema def `lusha_meta`, required `status, credits_used`):
  `status` enum `CALLED|SKIPPED`, `domain` str|null, `credits_used` int, `results_returned` int|null,
  `results_total` int|null, `matched` int|null, `contact_keys_removed` int, `reason` str (filter used + note, or the
  domains.json gap sentence), `absence_reason_class` enum `pull-missed|null` (`enrich.py:644-651`, `:672-676`).
- Measured: BA_US (09-15) `status CALLED`, officers `enrichment MATCHED` with `profile_url`/`lusha_title` set;
  CSL_AU and 6861_JP (09-19) `status SKIPPED`, `domain null`, `absence_reason_class pull-missed`, all officers
  `NOT-ATTEMPTED`.

### 1.5 Component map
- **Exec Mgmt only.** API: `scoped_amgt.read_management` (`lib/research/api/scoped_amgt.py:2507-2680`) serves
  `officers` verbatim + `lusha_enrichment` (`:2622`, `:2675`) on `GET /api/scoped/amgt/security/{key}/thesis`
  (`bundle["management"]` `:2067`; route listed `:3998`; portal fetch `portal/src/api/endpoints/amgt-lead-panel.ts:132`).
- Portal `portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx`: Profile column renders a link when
  `enrichment === 'MATCHED' && profile_url` (`:37-43`), "not attempted" (`:44-46`), else "ABSENT (Lusha matched no
  profile)" (`:47`); `lusha_enrichment.status === 'SKIPPED'` renders its `reason` (`:195-199`).
- **Read by no component:** `lusha_title` (typed `types.ts:666`, never rendered), `lusha_enrichment.credits_used /
  results_* / matched / contact_keys_removed / absence_reason_class`, the Lusha silver table (no reader at all).
- Lead Panel / Thesis / Peers / Model: NONE.

### 1.6 Gaps and hazards
- **H-L1 Domain source violates the contract.** PRD `:822-823`: company domain "ONLY from the site the filings battery
  VERIFIED ... never a hand list". Both Lusha paths use the 5-row hand list `domains.json`; the CEO search already uses
  `verified_domain_for` (`enrich.py:166-174`). Any name outside those 5 records `SKIPPED / pull-missed`.
- **H-L2 Two writers, one surface.** The served enrichment comes from `build_document`; the silver comes from
  `harvest_company`. Nothing joins silver back into `management/v1`, so running B4 lands silver the page never reads.
- **H-L3 `seniority` is dead.** In `KEPT_FIELDS` but no code derives it; the raw result carries it only nested at
  `jobTitle.seniority`, so `candidate.get("seniority")` is always null (`lusha.py:125-139`).
- **H-L4 Keying.** Silver is keyed by `(domain, person_id)` -- no `security_key`, no FIGI. The join back to a security
  is via `domains.json` (keyed by ticker-derived `security_key`). A composite-FIGI working key has no path here.
- **H-L5 Non-US.** Name matching is ASCII-fold + surname/given-name tokens (`enrich.py:350-374`); a JP roster from a
  yuho or Bloomberg in romanised order (family-first) fails the surname test. Unmeasured on a live call.
- **H-L6 PRD requires `record_hash` on Lusha silver** (`:931`) -- met by the store, not by `KEPT_FIELDS`, and the
  `_assert_no_contact_field` guard runs BEFORE the store adds it, so it does not refuse it (correct, but order-dependent).

---

## CHANNEL 2 -- THE MANAGEMENT DOCUMENT (M-1) end to end

### 2.1 Build and ranking of sources
`enrich.build_document(security_key, as_of)` (`enrich.py:635-726`), CLI `python -m lib.research.management.enrich
--security-key K --write-pool [--skip-pool]` (`main :1154-1298`); batch `lib/research/management/batch.py` (local,
weekly task DISABLED `:13-18`); repair modes `--reproject-public-profile` (`:888-934`), `--research-stored-ceo`
(`:954-1044`), `--rederive-roster-reason` (`:1047-1130`), `--pool-only` (`:1214-1225`).

Order of sources (who ranks first):
1. **Filing roster (authority).** `roster.load_source_object` (`roster.py:1116-1164`): SILVER `sec` then `issuer-site`
   `filing_source` rows (`:1084-1096`), ranked EDGAR accession > `doc-<16hex>` > other (`:1099-1113`); else
   `amgt/harvest/state/filing_attempt/security_key=<k>/UNRESOLVED-SOURCE.json`. `derive_roster` (`:1183-1264`) parses
   `officer_section.text` with `parse_officer_section` (strategies `narrative-*`, `table-paren`, `table-yuho`,
   `table-age/year`, `:975-1039`).
2. **Bloomberg fallback** only if roster not RESOLVED: `bloomberg_fallback.pull_exec_officers` (`:129-198`), one
   `ReferenceDataRequest` for `NAME`, `COMPANY_EXEC_OFFICERS` via the Terminal DAPI client; bronze
   `bloomberg/harvest/bronze/exec_officers/security_key=<safe>/<stamp>.json` when `write_raw` (`:171-177`).
3. **Lusha** enrichment (Channel 1) on whichever officers exist.
4. **CEO search** (Channel 3) on `find_ceo(officers, exchange)` (`enrich.py:433-447`: `_CEO_RE`
   `chief executive officer|ceo` `roster.py:196`; JP-only fallback to "president"/"representative director and
   president").
5. `completeness_guard` (`:450-481`) may downgrade RESOLVED -> `INCOMPLETE-NO-CEO`; then a whole-document `scrub`.
Pool: `compute_pool` (`:786-861`) -> `management/v1/_pool/<as_of>.json`.

### 2.2 Bloomberg `exec_officers` bronze (as received; `bloomberg/harvest/bronze/exec_officers/security_key=CSL_AU_Equity/20260921T162530Z.json`)
```
security: str ("<ROOT> <CC> Equity")   pulled_at: str ISO-Z
response: { NAME: str,
            COMPANY_EXEC_OFFICERS: list[ {"Executive Officers": "<name>,  <title>"} ] }   # 14 rows here
```
Parse: split on first `",  "` -> `{name, title}`, ASCII-fold (`bloomberg_fallback.py:117-126`).

### 2.3 Served `management/v1/<security_key>/<as_of>.json` -- FULL FIELD DICTIONARY (current vintage)
Measured on `management/v1/CSL_AU_Equity/2026-09-19.json` and `management/v1/6861_JP_Equity/2026-09-19.json`; schema
`lib/research/management/management.schema.json` (`additionalProperties:false`; required `security_key, as_of,
roster_status, roster_source, source_accession, officers, avg_tenure_years, ceo_profile, ceo_public_profile, fallback,
generated`). Values REDACTED.

| field | type | null | shape | meaning / writer |
|---|---|---|---|---|
| as_of | str | no | `"2026-09-19"` | build date (`roster.py:1186`) |
| security_key | str | no | `"<ROOT>_<CC>_Equity"` | ticker-derived key |
| roster_status | enum | no | `RESOLVED \| UNRESOLVED-SOURCE \| INCOMPLETE-NO-CEO` | `roster.py:102-107` |
| roster_reason | str | yes | readable sentence | why not RESOLVED |
| source_accession | str | yes | EDGAR digits (18) or `doc-<16hex>` (20) | filing id |
| source_key | str | yes | `s3://opal-data-harvest/filings/v1/<k>/<acc>.source.json` or `silver:filing_source:<k>:<acc>` | label of the source read (older objects carry the legacy filings/v1 URI) |
| source_item | str | yes | `"Item 10. ..."` or `""` | filing section heading |
| parse_strategy | str | yes | `narrative-entry`, `table-yuho`, ... | parser branch |
| parser_version | str | no | `"opal-management-roster/1.0.0"` | const |
| text_normalization | str | no | sentence | ASCII-fold rule |
| section_refers_to | str | yes | sentence | incorporation-by-reference pointer |
| generated | bool | no | `true` | |
| generated_at | str | no | ISO-Z | |
| roster_source | enum | no* | `FILING \| BLOOMBERG_FALLBACK \| null` | `enrich.py:600,624,631` |
| avg_tenure_years | float | yes | `float` | mean over officers with role_start |
| officers[] | list[obj] | no (may be []) | 1-14 rows | see below |
| officers[].name | str | no | `str (redacted)` | filing or Bloomberg, ASCII-folded |
| officers[].name_ascii | str | yes | `str (redacted)` | new at `roster.py:1245`; absent on all 4 objects read |
| officers[].role | str | no | title text | |
| officers[].role_start | str | yes | `"2016"`/`"2019-05-01"`-like | from filing "since" clause/column |
| officers[].role_start_basis | enum | no | `filing-since-clause \| filing-since-column \| absent` | |
| officers[].tenure_years | float | yes | `float` | computed at as_of |
| officers[].age | int | yes | `int` | from table-age / yuho |
| officers[].profile_url | str | yes | `url (redacted)` | Lusha `socialLinks.linkedin` |
| officers[].lusha_title | str | yes | str | Lusha `jobTitle.title` |
| officers[].source | enum | no | `filing \| bloomberg` | |
| officers[].confirmed | bool | no | `true` | |
| officers[].enrichment | enum | no | `MATCHED \| ABSENT \| NOT-ATTEMPTED` | |
| fallback | obj | no* | | `enrich.py:599-632` |
| fallback.status | enum | no | `NOT-CALLED \| OK \| EMPTY \| FAILED` | |
| fallback.security / field / entries_returned / officers_parsed / pulled_at / reason / label | str/int | yes | `field="COMPANY_EXEC_OFFICERS"` | |
| fallback.raw_key | str | yes | `raw/bloomberg/<k>/<stamp>/exec_officers.json` | **legacy key** (see H-M2) |
| lusha_enrichment | obj | no | see 1.4 | |
| ceo_profile | obj | no* | see 3.4 | the full CEO search block |
| ceo_public_profile | obj | no | see 3.4 | legacy projection the API reads |
| absence_reason_class | enum | yes | `source-lacks \| pull-missed` | `enrich.py:187-223` |
| absence_reason_evidence | str | yes | sentence | |

(*) required by the current schema but ABSENT on the 09-15 vintage: `management/v1/BA_US_Equity/2026-09-15.json` has no
`roster_source`, `fallback`, `ceo_profile`, `section_refers_to`, `absence_reason_*`; its `ceo_public_profile` is the
8-field pre-rk-48 shape (`url,title,snippet,status,basis,ceo_name,query,ir_domain`) with a `site:<ir_domain> "<name>"`
query from the retired `enrich.ceo_public_profile` (`:497-546`). MEASURED on BA_US only; the other four 09-15 objects
(BABA_US, COST_US, HD_US, SAP_GY) share the write date but were NOT read, so their shape is INFERRED, not measured.

Pool `management/v1/_pool/<as_of>.json`: `as_of` str, `pool_avg_tenure_years` float|null,
`pool_denominator{names_in_union:int, names_with_roster:int, officers_with_role_start:int}`, `universe_vintage` str
(`enrich.py:842-851`).

### 2.4 Transformations
Filing text -> parsed officers (deterministic parser, no model). Bloomberg string -> split name/title, role_start etc.
forced ABSENT (`:617-622`). Lusha -> 2 fields attached on exact name match. SERP -> `ceo_profile` (model-curated, see
3.4) -> `ceo_public_profile` projection (`ceo_search.py:753-811`). Every non-ASCII char folded; every contact key
dropped by `enrich.scrub` (`:723`).

### 2.5 Component map (Exec Mgmt)
API `read_management` partitions by officer count first (`scoped_amgt.py:2555-2574` ZERO_OFFICERS;
`:2577-2627` BLOOMBERG_FALLBACK SERVED with no pool read; `:2628-2650` ROSTER_UNRESOLVED_NO_FALLBACK; `:2651-2680`
RESOLVED SERVED + pool). Portal `ExecManagementTab.tsx`:
- officer table `name, role, role_start, tenure_years, profile/enrichment, source/confirmed` (`:35-67`, `:176-193`);
- header line `source_item`, `source_accession`, `as_of` (`:165-169`); fallback banner `roster_source`,
  `roster_status`, `roster_reason` (`:170-175`, subtitle `:228-230`);
- `avg_tenure_years` + `avg_tenure_denominator`, pool line `pool_avg_tenure_years` + `pool_denominator.*` +
  `pool_read.reason` (`:71-78`, `:200-202`);
- ABSENT state `management_status`, `absent_because`, `reason`, `roster_status`, `roster_reason`, `source_item`,
  `source_accession` (`:142-160`);
- CEO line from `ceo_profile_reading` + `ceo_public_profile.{ceo_name,url}` (`:88-139`).
- Served but NOT rendered: `fallback.*` (except via label), `absence_reason_*`, `officers[].age`, `role_start_basis`,
  `lusha_title`, `source_key`.
- Also consumed by Posture's cite resolver (`postureCites.ts:11-12`, `O:<officer>`, `M:avg_tenure_years`) -- Posture is
  out of scope. Lead Panel / Thesis / Peers / Model: NONE.

### 2.6 Gaps and hazards
- **H-M1 Keying.** Object path, crosswalk, domains.json and the filings silver lookup are all keyed by the
  ticker-derived `security_key` (`<ROOT>_<CC>_Equity`; slash-bearing roots like `BP/_LN_Equity` handled by prefix
  listing, `enrich.py:814-817`). No FIGI anywhere in this channel. A composite-FIGI working key needs a
  FIGI -> security_key crosswalk hop before every read here.
- **H-M2 Stale lineage pointer.** Served `fallback.raw_key` = `raw/bloomberg/<k>/<stamp>/exec_officers.json` (legacy,
  4 objects still present) while the current writer lands `bloomberg/harvest/bronze/exec_officers/...`
  (`bloomberg_fallback.py:171-177`). The API turns it into `source_key` (`scoped_amgt.py:2596-2600`). Retire the
  legacy `raw/` copy and the served pointer 404s.
- **H-M3 Mixed vintages served side by side** (see (*) above): the API tolerates missing `roster_source` by deriving it
  (`scoped_amgt.py:2487-2504`), but BA_US (measured) serves a CEO line from the retired IR-domain search. The other
four 09-15 names probably do too (inferred, not read).
- **H-M4 Non-US.** JP President rule only (`enrich.py:420-447`); other non-US rosters (CSL_AU) are Bloomberg-fallback
  with no role start, so no tenure and no pool comparison. `name_ascii` exists in code for the yuho path but no served
  object carries it yet.
- **H-M5 Coverage.** 15 names landed of the universe; no Bloomberg silver `executive_officer` table (PLAN s.5.1).

---

## CHANNEL 3 -- BRIGHT DATA SERP (CEO public profile)

### 3.1 Channel
- Vendor Bright Data, **SERP API** (a Google results page fetched through the `serp_opal` zone), NOT a dataset.
  Transport `POST https://api.brightdata.com/request` body `{zone, url:<google search url>, format:"raw"}`, Bearer key
  (`data/find/dualbiz/scripts/serp.py:377-393`). Google URL `https://www.google.com/search?q=<q>&gl=<gl>&hl=<hl>[&start=10n]`
  (`:426-427`). Zone from Secrets Manager `find-dualbiz/bright-data/serp` or env `BD_SERP_ZONE` (`:205-242`); key from env
  `BRIGHT_DATA_API_KEY` injected by `enrich._serp_module` (`enrich.py:406-417`) / `ceo_search._serp_module_lazy`
  (`ceo_search.py:309-330`).
- Primitive `serp_brightdata_records(query, max_pages=1, gl, hl, retries=2, transport)` (`serp.py:399-502`);
  classifier OK/EMPTY/FAILED (`:250-301`); retries only captcha/5xx.
- Caller today: `ceo_search.ceo_profile` (`ceo_search.py:473-705`), called from `build_document` (`enrich.py:687-705`)
  and `research_stored_ceo` (`:1009-1011`). Query: `"<CEO name>" <company short name> CEO` (`:540`), 1 SERP page,
  `gl=us, hl=en` always. Gate: needs `verified_domain` from the filings battery `verified_site.host`
  (`enrich.py:166-174`), else `NOT_SEARCHED / NO_VERIFIED_SITE` (`ceo_search.py:528-532`).
- Harvest writer `lib/research/harvest/bright_data_serp.py::harvest_serp` (`:81-160`) -- **"CODE ONLY ... wired into
  nothing"** (`:19-24`); no importer outside its test. Cadence: manual; per-use word (PRD `:839`).

### 3.2 Vendor response (bronze, as received) -- Bright Data Google JSON (keys read by code; values not seen live)
`general{query, detected_query, results_cnt, mobile}`, `spelling{original_empty}`, `organic[]{rank, link|url,
title, description, display_link, source, ...}`, plus `navigation`, `pagination`, `related` (shape per
`coverage/ir_scan.py:34-35`). Vendor headers read: `x-brd-status-code`, `x-brd-error-code`, `x-brd-error`.

### 3.3 Storage
- **Bronze** `bright-data/harvest/bronze/serp/date=YYYY-MM-DD/<query_sha256>-p<n>.json` -- live **0**. Raw 2xx body,
  UNSCRUBBED by ruling (`bright_data_serp.py:15-18`, `:119-126`), metadata `received-form: brightdata-raw-body`.
  Fetch key `query_sha256` = sha256 of canonical `{q (whitespace-normalised), engine:"google", gl, hl}` (`:49-56`).
- **Silver** `bright-data/harvest/silver/serp_result/date=.../part-<stamp>.parquet` -- live **0**. Record key
  `(query_sha256, rank)`. Row (`:136-149` over the primitive record `serp.py:486-490`):

| field | type | null | shape | meaning |
|---|---|---|---|---|
| rank | int | no | `int` | organic rank |
| link | str | no | url | resolved (`google.com/goto` unwrapped by one GET, `serp.py:348-374`) |
| link_form | enum | no | `DIRECT \| WRAPPED_RESOLVED \| WRAPPED_UNRESOLVED` | |
| host | str | yes | `"example.com"` | |
| title | str | yes | str | `contact_scrub_text` applied (emails/phones -> `[CONTACT-REDACTED]`) |
| snippet | str | yes | str | from vendor `description`, scrubbed as title |
| display_link | str | yes | str | |
| source | str | yes | str | |
| answers_detected_query | bool | no | bool | Google rewrote the query |
| query | str | no | contains a personal name (redacted) | |
| query_sha256, gl, hl, detected_query | str | | | |
| bronze_key, fetched_at, record_hash | lineage | | | |

- **Folded into served `management/v1` today** (the only live landing): `ceo_profile` and `ceo_public_profile`.

### 3.4 `ceo_profile` / `ceo_public_profile` field dictionary (from `6861_JP_Equity/2026-09-19.json`, status CURATED; and CSL NOT_SEARCHED)
```
ceo_profile:
  status: enum CURATED|NOTHING_FOUND|UNREADABLE|SEARCH_FAILED|NOT_SEARCHED        (ceo_search.py:57-61)
  reason_code: enum|null  NO_CEO_ON_ROSTER|ROSTER_UNRESOLVED|STEP_NOT_CONFIGURED|ORIGINAL_EMPTY|
               NO_RESULT_ABOUT_PERSON|NO_PAGE_READABLE|VENDOR_FAILURE|CONFIG_FAILURE|TRANSPORT_FAILURE|NO_VERIFIED_SITE
  reason: str   ceo_name: str(redacted)   name_source: FILING|BLOOMBERG_FALLBACK|null   company: str   role: str
  search: {instrument:"brightdata-serp-records", query:str|null, detected_query, query_rewritten:bool,
           original_empty:bool, gl:"us", hl:"en", attempts[]{http_status:int, brd_status:str, brd_error_code, seconds:float},
           results_returned:int, searched_at:ISO}
  triage: {model:"claude-opus-5"|null, prompt_version:"ceo-triage-v1"|null, same_person:int, different_person:int,
           company_only:int, uncertain:int, broker_dropped:int}
  items[]: {url, host, title, source_kind: official_bio|professional_profile|reference|interview_or_talk|news_profile|third_party_bio,
            why_kept:str, identity{anchor_distance_chars:int, quote:str, verified:true},
            read{http_status:int, content_type:str, chars:int, sha256_16:str, fetched_at:ISO},
            facts[]{topic: current_role|prior_role|tenure_or_appointment|education|board_or_outside_role|stated_view_or_priority,
                    quote: str (verbatim from page), char_range:[int,int], also_stated_at?:list[url]}}
  found_not_read[]: {url, host, title, source_kind, reason: "LINKEDIN_LINK_ONLY..."|"HTTP_<n>"|"UNREADABLE"|"not_kept: ..."}
  counts: {results, about_person, pages_read, facts_proposed, facts_verified, facts_dropped_unverified, contact_strings_scrubbed}: int
  cost: {serp_requests:int, fetches:int, model_input_tokens:int, model_output_tokens:int, model_usd:float}
  generated_at: ISO
ceo_public_profile: {url, title, snippet(always null), status: RESOLVED|ABSENT, basis: sentence, ceo_name, query,
                     ir_domain(null in new vintage), absence_class: null|NOTHING_FOUND|CANNOT_SAY, reason_code}
```
Transformations SERP -> ceo_profile (`ceo_search.py:539-705`): broker hosts dropped (`BROKER_HOSTS :100-104`); **model
call 1** triage over title/snippet/host (`_default_triage :379-399`, `anthropic_call` from
`lib.research.filings.analyze`, model label `claude-opus-5` `:108`); SAME_PERSON+UNCERTAIN pages (<=3) fetched by a
direct urllib GET (`_default_fetch :429-466`, LinkedIn never fetched `:611-617`); page text contact-scrubbed; identity
anchor (surname + company token within 500 chars `:229-244`); **model call 2** extraction to verbatim quotes
(`_default_extract :402-415`); every quote re-located with `passages.Locator` (`:646-671`); `source_kind=official_bio`
only when host = verified domain (`:253-261`). Projection: url = first official_bio item else first item
(`:778-780`). NOTE: SERP organic title/snippet are kept only inside `items[].title` / triage input -- the per-result list
itself is NOT stored anywhere today (only counts); that is what `serp_result` silver would add.

### 3.5 Component map
- **Exec Mgmt:** API serves `ceo_public_profile` + a server-side `ceo_profile_reading` (`scoped_amgt.py:2401-2484`:
  CONFIRMED / NOT_SEARCHED / SEARCHED_NOTHING_FOUND / SEARCHED_LINKS_UNREADABLE / SEARCH_FAILED / UNREADABLE_OBJECT).
  Portal `CeoProfile` (`ExecManagementTab.tsx:88-139`) renders the reading, `ceo_name`, `url`, `reason`,
  `urls_returned`.
- **`ceo_profile` (items, verified facts, triage, cost) is served by NO route and rendered by NO component** --
  `read_management` never copies it (`:2583-2625`, `:2652-2679`). The curated facts are stored and invisible.
- SERP bronze prefix is read only by the freshness view (`scoped_amgt.py:3247-3266`, `:3351-3356`) -- not a tab.
- Lead Panel / Thesis / Peers / Model: NONE.

### 3.6 Gaps and hazards
- **H-S1 Freshness reader cannot see the writer's keys.** `_bright_data_serp_stamps` expects
  `bright-data/harvest/bronze/serp/security_key=<safe>/<stamp>.json` (`scoped_amgt.py:3249-3260`); `harvest_serp`
  writes `serp/date=YYYY-MM-DD/<qsha>-p0.json` (`bright_data_serp.py:109-125`). Once wired, SERP freshness still reads
  NEVER for every name.
- **H-S2 No security key on SERP bronze/silver.** The fetch key is a query hash; the only join back to a security is the
  query text (a CEO name + company short name). No `security_key`, no FIGI column.
- **H-S3 Personal data in silver.** `query` carries the CEO's name and `link` can be a LinkedIn profile URL; the scrub
  covers only emails/phones in `title`/`snippet`. Bronze is unscrubbed by ruling.
- **H-S4 Contract drift on reading vocabulary.** PRD `:836-838` names five page states incl. "SEARCHED, NOTHING KEPT";
  the reader maps UNREADABLE/SEARCH_FAILED/NOT_SEARCHED to `absence_class CANNOT_SAY` (`ceo_search.py:783-788`), and
  `ceo_profile_reading` then routes a searched CANNOT_SAY to SEARCHED_LINKS_UNREADABLE, whose portal sentence says
  "none resolved to the company's IR domain" (`ExecManagementTab.tsx:118-125`) -- a sentence from the retired
  IR-domain search, now shown for UNREADABLE and SEARCH_FAILED as well.
- **H-S5 Non-US / language.** `gl=us, hl=en` hard-coded for every name (`ceo_search.py:474`); a JP/AU CEO is searched on
  the US English index; the model prompts and the identity anchor assume Latin-script surnames.
- **H-S6 `max_pages=3` in `ceo_profile`** is the page-FETCH cap, the SERP itself is always 1 page (`:545`).

---

## CHANNEL 4 -- SOCIAL (Bright Data Reddit)

### 4.1 Channel -- a DATASET API, not SERP
`lib/research/social/collect.py` calls the **Bright Data Datasets API v3** (asynchronous job), NOT the SERP zone:
`POST https://api.brightdata.com/datasets/v3/trigger?dataset_id=gd_lvz8ah06191smkebj4&include_errors=true&type=discover_new&discover_by=keyword&limit_per_input=<n>`
-> `GET /datasets/v3/progress/<snapshot_id>` poll -> `GET /datasets/v3/snapshot/<snapshot_id>?format=json`, plus
`GET /customer/balance` (`:76-86`, `:204-254`). Key `brightdata-api-key` via `.tools/comp-secrets` (`:183-201`); the
module states the SERP zone is "a DIFFERENT product ... not used here" (`:30-37`). Dataset "Reddit - Posts".
Inputs: ONE job, TWO keyword inputs `{keyword: <company name> | <ticker root>, date: "Past month", num_of_posts}` (cap 50)
(`build_inputs :520-538`; the `role` field is stripped before sending `:541-543`). Keywords come from the repo-local
universe file `deliverables/0.9.0_WK_AMGT_RESAPP~19/universe.v1.2026-09-15.json` (`:260-295`). Trigger: manual CLI,
**collection OFF** (Andrew 09-15 hold; PLAN s.5.6). `lib/research/social/measure.py` is a refusing plan stub (exits 3
without a word record, `:5-9`).

### 4.2 Bronze `bright-data/harvest/bronze/social_snapshot/date=<as_of>/<request_sha256>.json` -- live **0**
Only with `--write-harvest` (`:866-886`); snapshot response as received. Vendor record keys (30, MEASURED from the
`aboutness_note` of `social/v1/_measurement/2026-09-15.json`): `archived, author_icon, bio_description, comments,
community_description, community_members_num, community_name, community_rank, community_url, date_posted, description,
description_markdown, discovery_input, embedded_links, input, locked_post, num_comments, num_upvotes, photos, post_id,
post_karma, related_posts, subreddit_icon_image, tag, timestamp, title, url, user_id, user_posted, videos`.
Fetch key `request_sha256` = sha256 of `{dataset, type, discover_by, inputs, method_version}` (`:546-554`).

### 4.3 Silver `bright-data/harvest/silver/social_post/...` -- live **0**
Row = the vendor record flattened one level (`_flatten_one_level :580-593`: nested dict -> `<k>__<sub>`, lists JSON
strings) + `platform:"reddit"`, `post_id:str`, `bronze_key`, `fetched_at`, `record_hash`; record key
`(platform, post_id)` (`:910-935`). Nothing is dropped -- incl. `user_posted`, `user_id`, `author_icon`,
`bio_description`.

### 4.4 Normalized item (in memory only, `to_item :379-446`; never stored except a 10-item sample)
`item_id "reddit:<id>"`, `platform "Reddit"`, `account{handle, official:"UNRESOLVED", official_reason}`, `posted_at`,
`text` (title else body, ASCII-stripped), `url`, `admitted` (PASS|REFUSE|PROVISIONAL from the EXISTING rule
`lib/research/rules/item.py::qualify`), `rule_reason`, `source_line`, `keyword`, `community`, `stale` (window
re-applied locally on `posted_at`). Adapter: `primary_subject` always None; ticker counted only as a whole word in
title/flair/community.

### 4.5 `social/v1/_measurement/<as_of>.json` (legacy served gold-ish; 1 object, 2026-09-15)
Top: `as_of, security_key, security_name, method{platform, dataset, dataset_name, type, discover_by, route, inputs[],
cap, cap_basis, window{days, api_date_value, from, to, enforced_by}, keyword_source}, job{id, submitted_at,
completed_at, state, vendor_status, resumed, ledger_path, request_sha256, retrieval_flow, errors},
delivery{records, valid, invalid, admitted, rejected_by_rule, provisional, stale, fresh, capped}, latency_seconds,
cost{usd, unit, claim, basis, estimate_usd, unit_price_usd, usd_cap}, quality{relevance_sample[<=10]{item_id,
admitted, rule_reason, keyword, community, posted_at, url, text(<=280)}, relevance_sample_denominator,
verdict_counts{PASS, PROVISIONAL, REFUSE}, aboutness_note}, second_candidate{platform, dataset, discover_by,
profile_urls_from, profile_urls_available, status, reason}, method_version, normalisation{rule, items_affected,
chars_removed}, generated_at, generated_by` (`collect.py:1062-1151`; matches INVENTORY #22). Measured values (counts
only): job state COMPLETE, 48 records, 48 valid, **0 admitted**, 22 rejected, 26 provisional, 2 stale; `cost.claim
absent`. The local ledger/items files land in the repo under `deliverables/0.9.0_WK_AMGT_RESAPP~22/social_jobs/`
(`:452-466`, `:1165-1191`).

### 4.6 FWD-11 and components
PRD `FWD-11` (`:451-459`): "An analyst sees social discussion admitted by a written rule ... not because it contained
the ticker letters"; S13 "measure, then build" (`:1431`). Status: measured once, **0 of 48 admitted** because the
Reddit record has no subject/ticker field the rule can use.
- **No component reads any social data.** The API emits a static `feed.social = {status: "no source measured (S13)",
  items: []}` (`scoped_amgt.py:2311`, `:3047`); Lead Panel header `HeaderBrief.tsx:108-109` prints that status string.
  The Lead Panel's "Chatter" axis is the publications-driven `chatter_axis` (DynamoDB), unrelated to Reddit.
- Thesis: NONE. Exec Mgmt / Peers / Model: NONE.

### 4.7 Gaps and hazards
- **H-X1 Keying.** Job keyed by company-name/ticker-root keywords; measurement object keyed by ticker-derived
  `security_key`; silver keyed by `(platform, post_id)` with **no security column** -- a post cannot be joined back to a
  security from silver alone (only via bronze -> `discovery_input.keyword`).
- **H-X2 Ticker ambiguity.** The ticker-root keyword (e.g. a 1-3 letter root) is a deliberate ambiguity control; for
  JP numeric codes it is near-useless. English/ASCII only: non-ASCII is stripped (`normalise_text :336-351`), so
  non-Latin posts become empty text.
- **H-X3 Personal data in silver.** Author handle, user id, avatar and bio pass into `social_post` unscrubbed.
- **H-X4 Official accounts** unreachable: second candidate (X profiles) not run; account pass lookup is by exact company
  name (`:298-322`).

---

## CHANNEL 5 -- OTHER SEARCH-STYLE OPERATIONS in `lib/research`
Grep for `google.com|serp|search_engine|bing.com|brightdata|bright_data|/search?` over `lib/research`: 37 files; after
subtracting Channels 1-4 and their tests, the remainder is:
- `lib/research/coverage/ir_scan.py` (`:21-50`): **built, NOT run** -- `build_query(company) = "<name> investor
  relations"`; `parse_serp_results` reads `organic[]{rank, title, source, display_link, link}` -> `{rank, title,
  source, display_domain, raw_link}`. Exercised only on fixtures (`coverage/fixtures.py`). Feeds `coverage/reader.py`
  (IR/publication coverage). No S3 landing, no component.
- `lib/research/identity/resolver.py:24,140` and `build_universe.py:339`: text only ("a SERP zone request would be
  needed") -- no call.
- `lib/research/rules/source.py:5-60`, `metrics/chatter_gate.py:29`: fixtures/comments only.
- The retired IR-domain CEO search `enrich.ceo_public_profile` (`enrich.py:497-546`, `serp_brightdata` URLs-only) is
  no longer called by `build_document` but its output survives in the 5 objects dated 09-15.
No Bing/DuckDuckGo/web-search call exists in `lib/research`.

---

## SUMMARY
1. **Lusha** has two paths: the served values (officer `profile_url`/`lusha_title`/`enrichment` and the
   `lusha_enrichment` block) come from the legacy `enrich.build_document`. The round-25 entry point
   `lib/research/harvest/lusha.py::harvest_company` (with the `KEPT_FIELDS` allow-list and the `is_contact_key` guard)
   writes only `lusha/harvest/silver/contact_match` (0 objects), has no caller, and nothing reads it. No bronze, by rule.
2. Both Lusha paths take the company domain from the 5-row hand list `domains.json`. The PRD requires the battery's
   verified site. `seniority` in `KEPT_FIELDS` is always null.
3. **Management M-1**: the filing roster comes first, then the Bloomberg `COMPANY_EXEC_OFFICERS` fallback, then Lusha,
   then the CEO search. 15 names are served. The 09-15 vintage does not match the current schema (measured on BA_US,
   inferred for the other four 09-15 names), and the fallback `raw_key` still points at legacy `raw/bloomberg/`.
4. **Exec Mgmt** reads officers, tenure, pool, fallback label, the Lusha SKIPPED reason and the CEO reading through
   `/thesis` -> `read_management` -> `ExecManagementTab.tsx`. `lusha_title` and the whole `ceo_profile` (verified facts,
   triage, cost) are stored but never served or rendered.
5. **SERP** is a Bright Data SERP-zone Google fetch (`serp_opal`). It is one query per CEO, `"<name>" <company> CEO`,
   and is gated on a verified site. Two model calls (triage and verbatim extraction) are labelled `claude-opus-5`. The
   harvest writer `bright_data_serp.harvest_serp` exists but is wired into nothing, so the bronze `serp/` and silver
   `serp_result` hold 0 objects.
6. The SERP freshness reader expects `serp/security_key=<k>/` keys, but the writer uses `serp/date=<d>/<qsha>`, so they
   can never meet. SERP keys carry no security_key or FIGI.
7. **Social** is a Bright Data **Datasets API** job (Reddit Posts, `discover_by=keyword`), not SERP. It was measured
   once: 48 records, 0 admitted. Bronze `social_snapshot` and silver `social_post` hold 0 objects, and collection is OFF.
8. FWD-11 is unmet. No component reads social: the header prints a static "no source measured (S13)". The Lead Panel's
   "Chatter" axis is publications-based, not Reddit.
9. Keying across all four channels is the ticker-derived `security_key` or a query/domain hash. No channel carries a
   composite FIGI. Social and SERP silver cannot be joined back to a security without the query text.
10. The only other search-style code is `coverage/ir_scan.py` (an `"<name> investor relations"` SERP). It is built,
    never run, and fixture-only.
