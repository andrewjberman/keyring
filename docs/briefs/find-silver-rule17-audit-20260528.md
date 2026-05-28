# FIND_INSURE Silver-Tier Rule 17 Discipline Audit — 2026-05-28

**Author:** 0.1.0_DS_MarketIntelligence~A
**Date:** 2026-05-28T~04:00Z
**Trigger:** ws COO STANDING-PARALLEL Option (a) re-point 03:42Z (post FIND_INSURE.030 RAVC2-ACCEPT-CLOSE)
**Scope:** all silver-tier scripts in the FIND_INSURE pipeline (`data/find/**/silver/*.py`)
**Doctrine ref:** CLAUDE.md Rule 17 + [[feedback_silver_no_field_slimming]] (Andrew directive 2026-05-13: "it annoys me to no end when agents make silver scripts that pare down available fields, they need to not fucking do that")
**Companion to:** parse_web_silver.py Rule 17 fix `3ee6ee869` (5 bronze meta fields preserved)

---

## Verdict: PASS — both silver scripts Rule 17 compliant; zero remediation required

| Script | Verdict | Tier-shape | Notes |
|---|---|---|---|
| `parse_web_silver.py` | **PASS** | dict-based HTML-structure extractor | preserves all bronze; 5-field meta passthrough at `3ee6ee869`; blocked-record symmetry |
| `parse_linkedin_silver.py` | **PASS** | dict-based Lusha-cascade canonicalizer | `_unhandled` carve-out bucket = exemplary preserve-all; verbatim datetime preservation |

`test_parse_linkedin_silver.py` (test, not a silver-runtime script) — out of audit scope; no tier-discipline surface.

---

## Audit method

Three violation surfaces per CLAUDE.md Rule 17 + [[feedback_silver_no_field_slimming]], checked per script:

1. **Field-pruning** — `output_cols` lists / SELECT projections / `usecols=` / `df[[...]]` column-subset that drop bronze columns
2. **Business null-handling** — `fillna()` with business-defaulted values (not whitespace/encoding-artifact normalization)
3. **Business row-filtering** — `dropna()` / `df[df[col]...]` row-removal by business semantic

Plus structural checks: Rule 15 `from __future__ import annotations` first-import; Rule 14 `coerce_silver_ids()` for pandas `build_*` (N/A — neither script uses pandas).

**Grep sweep result:** the only `fillna`/`dropna`/`output_cols` occurrences across both scripts are in **docstring discipline-declarations** (lines `parse_linkedin_silver.py:18`, `parse_web_silver.py:31`) — i.e., the scripts documenting that they do NOT do these things. **Zero occurrences in executable code.**

---

## Per-script findings

### `parse_web_silver.py` — PASS

HTML-structure silver extractor (bronze HTML → structured silver per page). Dict-based; no dataframe operations.

- **No field-pruning:** `build_silver_record()` (L292-348) emits every extracted region — title, all meta_tags (no whitelist, L193-210 `extract_meta_tags` preserves ALL `<meta name|property>`), all h1-h6 headings, full link_graph, structured_blocks, structured_data, plus 5 bronze meta passthrough fields (`http_headers`, `crawl_depth`, `robots_txt_compliance`, `scheme_fallback`, `tls_fail_original`) added at `3ee6ee869`.
- **No business null-handling:** blocked records (`build_blocked_record` L351-386) set `page_text=None` + `body_text=None` as explicit field-presence-symmetry signals (LOCK v0.2.1 `f7e61aa39`), NOT business fill. Success-record `body_text` is full `soup.get_text()` — no boilerplate removal (correctly deferred to gold).
- **No business row-filtering:** every bronze page yields exactly one silver record (success OR blocked). `classify_metadata_block()` (L389-410) tags `blocked_reason` but does not drop the row — the blocked record is still written (audit-trail preservation per PRD §9 Q5).
- **Rule 15:** `from __future__ import annotations` at L57. ✓

### `parse_linkedin_silver.py` — PASS (exemplary)

Lusha-cascade silver canonicalizer (bronze Lusha payloads → silver contact + company records). Dict-based; no dataframe operations.

- **No field-pruning:** `build_silver_contact_record()` (L187-256) + `build_silver_company_record()` (L259-299) enumerate known Lusha fields AND include an `_unhandled` carve-out bucket (L242-247, L288-291) that copies any bronze key NOT explicitly mapped into `record["_unhandled"]` — **structural preserve-all guarantee**. This is the strongest Rule 17 pattern in the find pipeline: even fields the author didn't anticipate are round-tripped, not dropped. Recommend banking as the canonical silver-canonicalizer template.
- **No business null-handling:** `_normalize_iso()` (L173-184) preserves `None` verbatim and preserves clean strings verbatim; only coerces non-string shapes to `str()`. No `fillna`-equivalent business defaulting. Comment L184 explicitly defers business interpretation to gold.
- **No business row-filtering:** the only `continue` (L374-377) skips a contact on `FileNotFoundError`/`JSONDecodeError` — an **IO/parse error**, not a business semantic ("drop contacts missing email"). The docstring (L19) explicitly names "drop contacts missing email" as a forbidden pattern and the code does not do it. Parse errors increment `contacts_parse_errors` counter (audit-visible).
- **Rule 15:** `from __future__ import annotations` at L85. ✓

---

## Cross-pipeline observations (non-blocking)

1. **find/imo is the only find sub-domain with silver scripts.** `data/find/**/silver/*.py` resolves to the 2 imo scripts + 1 test. No other find sub-pipelines have silver tiers yet.
2. **Neither find silver script uses pandas.** Both are pure-dict JSON canonicalizers (Lambda-bundled, per-record). The `coerce_silver_ids()` Int64 enforcement (ADHC `SILVER-ID-DTYPE-UNIFY`) and the `.tools/ds-precommit-check.py` silver `build_*` gate target pandas-dataframe silver builders (e.g., orion/advi) — N/A for these dict-based scripts. ID preservation is handled via explicit `str()` coercion preserving verbatim (`contact_id`, `lusha_company_id`).
3. **`_unhandled` carve-out bucket** in `parse_linkedin_silver.py` is a stronger Rule 17 guarantee than `parse_web_silver.py`'s explicit-enumeration approach — the LinkedIn parser cannot silently drop a future Lusha field, whereas the web parser's preservation is bounded by its explicit field list (acceptable because HTML structure is a fixed extraction surface, but worth noting the asymmetry).

---

## Remediation list

**None.** Both scripts pass clean. No passthrough migration, no field-restoration, no null-handling removal required.

---

## Audit-pattern primitive (future-cycle reuse)

This audit establishes a repeatable silver Rule 17 sweep for any pipeline:

1. `Glob data/{domain}/**/silver/*.py`
2. Grep each for `output_cols|fillna|dropna|\.drop\(|usecols|df\[\[|SELECT |df\[df\[`
3. Triage matches: docstring-declaration (PASS) vs executable code (INVESTIGATE)
4. For executable matches, classify: whitespace/encoding normalization (PASS per Rule 17 permitted-ops) vs business field-pruning/null-handling/row-filtering (FAIL → remediate to passthrough)
5. Confirm Rule 15 `from __future__` first-import + Rule 14 `coerce_silver_ids()` for pandas `build_*`

Applicable to orion/advi/yalp silver tiers on next maintenance touch (opportunistic, not forced backfill per Rule 17 migration stance).

---

— 0.1.0_DS_MarketIntelligence~A 2026-05-28 — FIND_INSURE silver Rule 17 audit (STANDING-PARALLEL Option a)
