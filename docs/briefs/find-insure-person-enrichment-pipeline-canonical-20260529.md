# FIND_INSURE — Canonical Multi-Source Person Enrichment Pipeline

**Author:** 1.0.0_SA_CTO
**Date:** 2026-05-29
**Directive:** Andrew sovereign 2026-05-29 — "linkedin url is the joinkey, make all these processes canonical for programmatic pipeline development"
**Status:** ARCHITECTURE BRIEF v1.0 — governs FIND_INSURE Phase 2B+ implementation

---

## 1. Core principle: LinkedIn URL slug is the canonical person entity key

Every enrichment source we have or may add links to a person via their LinkedIn profile URL.
The slug (`chris-surrichio-16052b1` from `linkedin.com/in/chris-surrichio-16052b1`) is:
- **Stable** — LinkedIn slugs rarely change; when they do, the old URL redirects
- **Free** — present in Lusha `contacts/prospecting` response at org-chart cost tier
- **Cross-source** — Bright Data keys directly on the URL; FINRA BrokerCheck + other sources
  can be joined via name+employer fuzzy match seeded by the LinkedIn-confirmed identity
- **Dedup-safe** — same person at multiple IMOs collapses to one entity record

All pipeline artifacts from bronze through serving key person records on `linkedin_slug`.

---

## 2. Source map — what each source contributes

| Source | Endpoint / Dataset | Join key in | Contributes | Cost tier |
|---|---|---|---|---|
| **Lusha prospecting** | `POST /v3/contacts/prospecting` | `company_domain` → returns `id` + `socialLinks.linkedin` | `contact_id` (Lusha FK), `linkedin_url`, name, current title, seniority, department | ~1 cr/25 results (org-chart tier) |
| **Lusha enrich** | `POST /v3/contacts/enrich` | `contact_id` (from prospecting) | email addresses, phone numbers, previous employment, location detail | ~5.9 cr/contact (reveal tier) |
| **Bright Data LI scrape** | `gd_l1viktl72bvl7bjuj0` | `linkedin_url` directly | bio/about, certifications (CFA etc. with credential URLs), activity feed, posts, recommendations, education, organizations, follower/connection counts | per-scrape pricing |
| **FINRA BrokerCheck** | BrokerCheck API (to be integrated) | `crd_number` (via name+employer lookup from BrokerCheck search) | Series-7/66/etc. license status, registration history, disclosures | free public API |

**Source acquisition order (optimal pipeline sequence):**
1. Lusha prospecting (cheapest; seeds `contact_id` + `linkedin_url` for all downstream)
2. Bright Data scrape (keys on `linkedin_url`; can run in parallel with Lusha enrich)
3. Lusha enrich (spend credits only on contacts that pass BD certification + scoring filter)
4. FINRA BrokerCheck (name+employer lookup; free; run on high-scoring contacts)

---

## 3. S3 key schema — person-centric store

```
people/
  {linkedin_slug}/
    meta.json                    # canonical entity record (see §4)
    sources/
      lusha_prospecting.json     # raw Lusha contacts/prospecting result for this person
      lusha_enrich.json          # raw Lusha contacts/enrich result (email+phone)
      brightdata_profile/
        {date}.json              # raw Bright Data scrape (append per refresh)
        latest.json              # symlink-equivalent: copy of most recent scrape
      finra_brokercheck/
        {date}.json              # raw FINRA BrokerCheck result
        latest.json
    silver/
      person_enriched.json       # merged silver record (see §5)
    gold/
      person_scored.json         # final scored record for serving
```

Cross-IMO index (same person may appear at multiple IMOs — e.g. a VP who moved firms):
```
people/_index/
  {linkedin_slug}.json           # {linkedin_slug, imo_slugs: [...], primary_imo_slug}
```

IMO-scoped pointer (existing per-IMO gold artifacts retain backward-compat):
```
corp/{imo_slug}/gold/linkedin-scrape/{run_date}/employees_scored.json
  → each employee entry gains: linkedin_slug, person_s3_path (pointer to people/{slug}/)
```

---

## 4. Canonical `meta.json` — person entity record

```json
{
  "linkedin_slug":       "chris-surrichio-16052b1",
  "linkedin_url":        "https://www.linkedin.com/in/chris-surrichio-16052b1",
  "name":                "Chris Surrichio",
  "title":               "Vice President of Investment Management and Research",
  "imo_slug":            "lincoln-investment",
  "imo_name":            "Lincoln Investment",
  "lusha_contact_id":    "434062182",
  "finra_crd":           null,
  "source_ids": {
    "lusha":             "434062182",
    "brightdata":        "chris-surrichio-16052b1",
    "finra_crd":         null
  },
  "first_seen_utc":      "2026-05-27T...",
  "last_enriched_utc":   "2026-05-29T19:19:37Z",
  "enrichment_status": {
    "lusha_prospecting": "DONE",
    "lusha_enrich":      "DONE",
    "brightdata":        "DONE",
    "finra":             "PENDING"
  }
}
```

---

## 5. Silver `person_enriched.json` — merged cross-source record

Silver merges all source outputs into one canonical person record. Silver discipline
(CLAUDE.md Rule 17) applies: normalize + deduplicate, do NOT slim fields, do NOT
apply business-logic filtering (that belongs in gold).

```json
{
  "linkedin_slug":          "chris-surrichio-16052b1",
  "linkedin_url":           "...",
  "name":                   "Chris Surrichio",
  "title":                  "Vice President of Investment Management and Research",
  "seniority_class":        "vp_director",
  "department":             "Finance",
  "location": {
    "city":                 "Fort Washington",
    "state":                "Pennsylvania",
    "country":              "US"
  },
  "imo_slug":               "lincoln-investment",
  "lusha_contact_id":       "434062182",
  "emails":                 [ {"address": "...", "isVerified": false} ],
  "phones":                 [ {"number": "...", "type": "..."} ],
  "bio":                    "...",
  "followers":              613,
  "connections":            500,
  "certifications": [
    {
      "title":              "CFA Institute Charterholder",
      "issuer":             "CFA Institute",
      "credential_id":      "113018247",
      "credential_url":     "https://credentials.cfainstitute.org/fd0ec862...",
      "issued":             "Aug 2024"
    }
  ],
  "education":              [...],
  "activity_recent":        [...],
  "posts":                  [...],
  "recommendations":        [...],
  "organizations":          [...],
  "finra_crd":              null,
  "series_licenses":        [],
  "previous_employment":    [],
  "source_freshness": {
    "lusha_prospecting_date":  "2026-05-27",
    "lusha_enrich_date":       "2026-05-29",
    "brightdata_date":         "2026-05-29",
    "finra_date":              null
  }
}
```

---

## 6. Gold `person_scored.json` — enrichment-aware scoring

Gold re-scores using all available dimensions (CLAUDE.md Rule 17: business-logic
belongs in gold, not silver). Scoring additive layers:

| Dimension | Source | Weight class |
|---|---|---|
| Title + seniority | Lusha prospecting | Base (always present) |
| AM-domain relevance | Title taxonomy | Base |
| CFA / CFA-candidate certification | Bright Data `certifications` | +SIGNAL |
| Series-7 / Series-66 license | FINRA BrokerCheck | +SIGNAL (strongest) |
| Activity recency + domain relevance | Bright Data `activity` | +SIGNAL |
| Direct contact info available | Lusha enrich | +REACHABILITY flag |
| Email verified | Lusha enrich | +REACHABILITY |

---

## 7. Script map — what needs to be built / extended

| Script | Status | Action |
|---|---|---|
| `bronze/crawl_linkedin_bronze.py` | EXISTS | **Extend**: persist `linkedin_slug` + write pointer to `people/{slug}/sources/lusha_prospecting.json` |
| `serving/reveal_top25_contacts.py` | EXISTS (f9dd72e57) | **Generalize**: → `bronze/crawl_lusha_enrich_bronze.py` writing to `people/{slug}/sources/lusha_enrich.json` |
| `bronze/crawl_brightdata_profile_bronze.py` | **NEW** | Batch-scrape Bright Data `gd_l1viktl72bvl7bjuj0` for a slug list; write to `people/{slug}/sources/brightdata_profile/{date}.json` |
| `bronze/crawl_finra_brokercheck_bronze.py` | **NEW** | Name+employer BrokerCheck search → CRD lookup → license records; write to `people/{slug}/sources/finra_brokercheck/{date}.json` |
| `silver/merge_person_silver.py` | **NEW** | Read all source artifacts for a slug; emit `people/{slug}/silver/person_enriched.json` |
| `gold/score_person_gold.py` | **NEW** | Multi-source scoring; emit `people/{slug}/gold/person_scored.json` |
| `serving/build_contacts_target.py` | EXISTS | **Extend**: read from `people/{slug}/silver/person_enriched.json` instead of per-IMO gold artifacts |

---

## 8. Dispatch sequence for a new IMO cohort

```
1. crawl_linkedin_bronze      (Lusha prospecting)   → seeds linkedin_slug + lusha_contact_id
2. parse_linkedin_silver       (existing)             → normalizes bronze
3. score_linkedin_gold         (existing)             → initial org-chart score
   ↓  (filter: top-N by score, or all above threshold)
4. crawl_brightdata_profile_bronze  (NEW, batch)     → BD scrape per linkedin_url
5. crawl_lusha_enrich_bronze        (NEW, generalized reveal)  → email+phone per contact_id
6. crawl_finra_brokercheck_bronze   (NEW)            → license records per person
   ↓  (all 3 can run in parallel after step 3)
7. merge_person_silver              (NEW)            → canonical person_enriched.json
8. score_person_gold                (NEW)            → final multi-source score
9. build_contacts_target            (EXTENDED)       → serving output for IR team
```

---

## 9. Implementation priority

Per Andrew direction and credit-conservation posture:

1. **`crawl_brightdata_profile_bronze.py`** — highest immediate value (certifications,
   activity, bio); keys directly on `linkedin_url` (no extra lookups); cost TBD per
   Andrew Bright Data account tier
2. **`bronze/crawl_lusha_enrich_bronze.py`** (generalized from reveal_top25) — already
   proven; just needs path generalization + `people/` write target
3. **`merge_person_silver.py`** — enables the joined view across sources
4. **`crawl_finra_brokercheck_bronze.py`** — free + highest-signal (series licenses);
   needs BrokerCheck API rate-limit + name-match strategy design
5. **`score_person_gold.py`** — multi-source scoring (extends existing score_linkedin_gold)

---

## 10. Open design questions for Andrew

**Q1 — Bright Data pricing model:** per-record or subscription? Determines whether we
scrape all 746 org-chart contacts vs. top-N only.

**Q2 — FINRA BrokerCheck name-match strategy:** BrokerCheck search takes first/last name
+ firm name. Hit rate on common names (e.g. "Chris Johnson") may require CRD disambiguation
via employer cross-check. Accept fuzzy match with confidence score, or require exact?

**Q3 — Refresh cadence:** people change jobs. How often to re-scrape? Suggestion:
re-scrape on any score-change trigger (e.g. IMO gets a new company score) + quarterly
baseline. Store `{date}.json` per scrape so history is retained.

**Q4 — Cross-IMO dedup scope:** same person appearing at 2 IMOs (job change, dual-role)
should yield one `people/` record, two `_index` pointers. Is IR targeting per-person
or per-IMO relationship? Affects serving layer design.
