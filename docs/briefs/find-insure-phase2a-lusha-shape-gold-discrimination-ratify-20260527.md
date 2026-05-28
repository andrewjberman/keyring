# FIND_INSURE Phase 2A — Lusha v3 response shape ratify for gold-tier discrimination

| | |
|---|---|
| **Author** | 0.1.0_DS_MarketIntelligence~B |
| **Date** | 2026-05-27 |
| **Status** | DRAFT-for-review — ratification ask to ws CTO + CVO (CC ws COO + MSTR + DS~C + DS~E) |
| **Parent** | FIND_INSURE.011 AC3 (per MSTR-DIRECT SPAWN-WITH-DIRECTION 2026-05-27T~23:35Z, Andrew direct 23:25Z "parallelize: bring on 3 or 4 more DS") |
| **Lusha reference** | `docs/reference/lusha-api-v3.md` (workspace copy; upstream <https://docs.lusha.com/apis/openapi/section/data-source-and-privacy>) |
| **Sister artifacts** | `data/find/imo/scripts/gold/score_linkedin_gold.py` + `test_score_linkedin_gold.py` (this cycle) ; `data/find/imo/scripts/silver/parse_linkedin_silver.py` (DS~C .011 AC2) ; `data/find/imo/config/scoring-weights-v0.1.json` (DS~E .E1) |

---

## 1. Question this brief answers

> Does the Lusha v3 API response shape — as captured in `docs/reference/lusha-api-v3.md` §7 + the per-endpoint OpenAPI bundle — carry enough information for the gold-tier `score_linkedin_gold` module to (a) identify named individuals, (b) count Series-license holders, and (c) extract AUM numbers, with discrimination quality sufficient for the Phase 3 IR-team-facing ranking?

Short answer: **YES for (a) and (b); MOSTLY-YES for (c) with one carve-out + one v0.2 enrichment recommendation.**

This brief is the structural counterpart to the implementation that ships
alongside it — the code can be reviewed against this ratify-doc to confirm
each gold-tier discrimination axis has a load-bearing Lusha field underneath.

---

## 2. Gold-tier discrimination axes mapped to Lusha fields

### 2.1 Named individuals (AC3 "named-individuals extraction")

| Gold field | Source — Lusha endpoint | Lusha response field | Silver field (per `parse_linkedin_silver.py`) | Discrimination quality |
|---|---|---|---|---|
| `contact_id` | `POST /v3/contacts/prospecting` + `POST /v3/contacts/enrich` | `id` (string) | `contact_id` | **HIGH** — Lusha-stable identifier; load-bearing for the cross-IMO join key |
| `full_name` | enrich result | `fullName` (string) | `fullName` | **HIGH** — Lusha returns canonical fullName; firstName + lastName also preserved for downstream disambiguation |
| `linkedin_url` | enrich result | `linkedinUrl` (string) | `linkedinUrl` | **HIGH** — direct LinkedIn profile URL; primary evidence-of-existence; IR-team-actionable |

**Verdict (a):** Lusha shape is sufficient. Named-individual identification at
the IR-team-actionable level (name + LinkedIn URL + Lusha-stable id) lands at
silver and gold preserves it verbatim per Rule 17 silver passthrough discipline.

### 2.2 Series-license counts (AC3 "Series-license counts")

Lusha does NOT have a structured `series_licenses` field in the v3 contact
response. License mentions land as free text in:

| Source field | Endpoint where it appears | Detection method |
|---|---|---|
| `currentPosition.description` | enrich result | regex on text (`detect_series_licenses` in `score_linkedin_gold.py`) |
| `currentPosition.title` | enrich result | regex (catches "VP, Series 65 RIA" patterns) |
| `previousPositions[].description` / `.title` | enrich result | regex (preserves historical license-holder pattern even if not active) |
| `certifications[].name` / `.title` / `.text` | enrich result | regex on each cert entry (handles both dict + bare-string shapes) |
| `education[*]` | enrich result | NOT scanned at v0.1 — Series-license context typically appears in work history + cert lists, not education entries |

**Detection regex pattern** (in `score_linkedin_gold._SERIES_LICENSE_REGEX`):

```
\b(?:series[\s-]?|s)(\d{1,3})\b
```

Plus a 40-character negation-window scan downstream of each match for
`retired|lapsed|inactive|expired|former(ly)?` to suppress "Series 7
(retired)"-class false positives.

**Valid-code allowlist (matches `scoring-weights-v0.1.json` series_license_weights):**

```
6, 7, 22, 24, 26, 51, 52, 53, 63, 65, 66, 79, 82
```

Codes outside this set are silently dropped — Series 9, Series 28, etc. don't
correspond to weighted axes in the E1 ratification so they don't contribute
even if they were detected.

**Discrimination quality (b):** **HIGH** at the count level (count of
Series-licensed leadership per IMO is the load-bearing axis for
`series_licensed_employee_count` rollup); **MEDIUM-HIGH** at the per-license-
class weighted level (E1 `series_license_weights` differentiates 65/66 [0.40]
from 7/24 [0.30] from 63/6 [0.05-0.10]).

**Known false-negative class — recommended v0.2 enrichment:**
Some IMOs list FINRA license codes on the company website (via Phase 1 web-
scrape `term-taxonomy-v1.json`) without the individual employees surfacing the
same license on their LinkedIn profile. The cross-channel signal is captured
at Phase 3 `build_companies_serving` consolidation — Phase 2A LinkedIn alone
can under-count. Acceptable v0.1 boundary.

### 2.3 AUM number extraction (AC3 "AUM number extraction")

Lusha does NOT have a structured `aum_usd` field in the v3 contact or company
response (it's a marketing-platform identifier — not an asset-data vendor).
AUM mentions land in:

| Source field | Endpoint | Detection |
|---|---|---|
| `currentPosition.description` | contact enrich | `extract_aum_usd` regex (this module) |
| `bio` / `about` | contact enrich (if present in payload extras) | regex; Lusha v3 doesn't document these as canonical fields but the `_unhandled` pass-through in silver preserves them when Lusha emits them |
| `companies/enrich` `description` field | company enrich | NOT scanned at v0.1 — company-level AUM mentions are typically a marketing-page artifact that Phase 1 web-scrape already captures; double-counting would be cross-channel noise |

**Extraction regex pattern** (`extract_aum_usd` in `score_linkedin_gold.py`):

```
amount: (?:\$\s*)?(\d{1,4}(?:,\d{3})*(?:\.\d+)?)\s*(b|bn|billion|m|mm|million|k|thousand)\b
context: AUM | assets under management | under management | manages over | portfolio of | managing over
proximity: 80 chars between context-phrase and dollar-amount
```

Tested cases (in `test_extract_aum_usd`):
- `$500M AUM` -> 500,000,000 USD
- `$1.2 billion in assets under management` -> 1,200,000,000 USD
- Multi-amount text takes MAX value, preserves all evidence for audit
- `$100K bonus` (no AUM context) -> None (correctly filtered)

**Discrimination quality (c):** **MEDIUM** — bio-text extraction has lower
recall than a structured field would. The mitigating factor: AUM is a
secondary discriminator in the Phase 2A gold; the primary axes are
seniority + Series-licenses + tenure + title-keyword. AUM enriches the
single-employee profile when present but does NOT block the gold-tier
discrimination when absent (E1 weights don't include an `aum` term).

**Carve-out:** AUM extracted at the employee-bio level is necessarily
**self-reported by that individual** ("oversees $500M AUM across model
portfolios" in their LinkedIn description). That's a noisy proxy for true
firm-AUM — useful as a directional signal, not as a balance-sheet number.
The Phase 3 serving table should label this column accordingly
(`aum_self_reported_extracted_usd` rather than `aum_usd`) to avoid
downstream consumers misreading the provenance. Recommendation routed to
DS~E for inclusion in `serving/employees.{json,parquet}` column naming.

**Recommended v0.2 enrichment:** for the Phase-3-confirmed top-N IMOs, add
a Form ADV scrape (publicly available at <https://adviserinfo.sec.gov>) to
get structured firm-AUM. This is a separate data-source — out of Phase 2A
scope but routed to the FIND macro roadmap as a candidate FIND_INSURE.v0.2
TO.

---

## 3. Lusha-shape-derived discrimination quality matrix

| Phase 2A discrimination axis | E1 scoring weight | Lusha shape sufficient? | Confidence |
|---|---|---|---|
| Named individual (name + linkedin URL) | — (pass-through) | YES | HIGH |
| Tenure at company (years from `currentPosition.startDate`) | 0.25 | YES — startDate present in enrich payload | HIGH |
| Title seniority class | 0.25 | YES — `title` field reliable; classification via regex taxonomy in `score_linkedin_gold.py` | HIGH |
| Series-license codes detected | 0.30 | YES — text-scan on certifications + descriptions covers the v0.1 valid-code set | MEDIUM-HIGH |
| Title-keyword match | 0.20 | YES — title field reliably populated | HIGH |
| AUM number | — (orthogonal, not in employee_score) | PARTIAL — text-scan only; structured AUM unavailable | MEDIUM |

Composite verdict: **employee_score's four weighted axes all have
load-bearing Lusha fields underneath**. AUM is orthogonal (not in
employee_score formula); its extraction is a bonus discriminator preserved
for downstream consumer + audit but does NOT block gold-tier discrimination
quality.

---

## 4. Recommended v0.2 enrichments (out of v0.1 scope)

1. **Form ADV scrape** for Phase-3-confirmed top-N IMOs — gives structured
   firm-AUM + RIA registration date + form-ADV-listed advisory-firm size +
   custodian relationships. Source: `https://adviserinfo.sec.gov`.
   Estimated effort: 1 new bronze/silver/gold channel in `data/find/imo/scripts/`.

2. **Lusha company `description` AUM extraction** — currently scoped out of
   `score_linkedin_gold` to avoid Phase-1-web-scrape double-count. If Phase 1
   AUM term-taxonomy fails to capture (e.g., AUM on a non-crawled subpage),
   reactivate at v0.2 with cross-channel dedup logic.

3. **Lusha `signals` companyChange / surgeInHiring overlay** per PRD v0.7
   §4 Phase 3 — already scoped as Phase 3-overlay (Stage 3); listed here for
   completeness as a v0.2+ enrichment target.

4. **License-mention NLP** — current regex-based detection misses paraphrastic
   forms like "FINRA-licensed General Securities Representative" (S7
   description without the literal "Series 7" string). v0.2 could add a
   FINRA-license-name -> code map. Low priority at v0.1 because the
   canonical "Series N" form dominates LinkedIn profile mentions.

---

## 5. Ratification ask

**Routed to ws CTO + ws CVO via ws COO** (per LD-0116 worker MCPs only via
fabric COO — no T2/3 ↔ MSTR direct comms).

Verdict shape requested:

- **CORROBORATE** — Lusha shape is sufficient for gold-tier discrimination
  at v0.1 per the mapping in §2 + the matrix in §3. Implementation in
  `score_linkedin_gold.py` correctly binds each weighted axis to a
  load-bearing Lusha field.
- **CORROBORATE-with-CONCERN** — soft-fix the AUM column naming
  (`aum_self_reported_extracted_usd` rather than `aum_usd`) to avoid
  downstream provenance confusion; fold into DS~E `serving/employees.parquet`
  column-naming.
- **COUNTER** — if the mapping has a load-bearing gap not yet identified,
  document the gap + the v0.2 enrichment recommendation.

Acceptance class per [[feedback_corroborate_with_concern_verdict_shape]] + the
LD-0095 verification-class taxonomy: this is a **rationale-narrative-class**
verification (mechanical bookkeeping that the mapping documents match the
implementation), not an empirical-smoke-class verification (which fires when
real Lusha calls land for Phase 2A — a downstream RAVC2 moment).

---

## 6. Acceptance evidence already shipped (this cycle)

- `data/find/imo/scripts/gold/score_linkedin_gold.py` — gold-tier scoring module
  implementing every axis mapped in §2.
- `data/find/imo/scripts/gold/test_score_linkedin_gold.py` — fixture-based
  unit-test suite (50+ self-test cases across 9 test functions); `python
  test_score_linkedin_gold.py` exits 0; covers named-individual
  pass-through, Series-license positive + negation + multi-code, AUM
  million/billion/multi-amount/no-context, tenure + normalization,
  title-keyword indicator, full employee scoring (high + low signal
  contacts), company aggregation, stub-mode handler end-to-end.

---

## 7. Routing summary

| Recipient | Role | Action |
|---|---|---|
| ws COO `2.0.0_SA_COO` | RAVC2 destination + fabric-COO routing | RAVC2-Request for FIND_INSURE.011 AC3 ship; route this brief to CVO for verify-channel-mode-A rationale-narrative-class |
| ws CTO `1.0.0_SA_CTO` | brief author + design authority | CC awareness; CORROBORATE expected per §5 |
| ws CVO `3.0.0_SA_CVO` | priority architectural corroborator | verdict-shape ratify per §5 |
| MSTR `0.0.0_AB_MSTR` | spawn-with-direction authority | CC ship-notification |
| DS~C `0.1.0_DS_MarketIntelligence~C` | sister-coord (silver input contract + remaining .011 AC1+AC2+AC4+AC5 bundle) | CC awareness; this brief documents the silver shape contract `score_linkedin_gold` consumes |
| DS~E `0.1.0_DS_MarketIntelligence~E` | sister-coord (scoring weights config author) | CC awareness; AUM column-naming recommendation in §2.3 may inform Phase 3 serving build |

— 0.1.0_DS_MarketIntelligence~B 2026-05-27T~23:55Z
