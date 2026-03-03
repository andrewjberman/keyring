# Page Codes & ADVI Migration -- 1.0.0_SA_CTO

**Date:** 2026-03-03
**Start Time:** session continuation
**End Time:** session end

## Objective

Introduce canonical 4-character project codes for all portal pages and pipelines,
and migrate the existing AdvisorIntelligence project from code `AI` to `ADVI`.

---

## Work Completed

### 1. PAGE_CODES.md

Wrote `org/projects/PAGE_CODES.md` — canonical reference for 19 codes:

| Pod | Codes |
|-----|-------|
| Pod 1 MarketIntelligence | MKPF, CENG, CMAS, MKOV |
| Pod 2 PortfolioAnalytics | POSN, ATTR, FCTL, VALU, MACR, CORR |
| Pod 3 TradingOperations | PFMG, TRSB, DRFR |
| Pod 4 ClientPlatform | MDLP, ADVI |
| Cross-pod / AE | YALP, BDPL, NPPL, SXPL, SHIF |

Each code maps to responsible pod (DE/DS/DT), RD agent, portal directory, and pipeline.
Rules: all codes exactly 4 chars; 1:1 page/pipeline mapping; must register before use.

### 2. AI -> ADVI migration

Renamed `org/projects/AI.json` -> `org/projects/ADVI.json`.
Updated all internal fields and every downstream reference:

| File | Change |
|------|--------|
| `org/projects/ADVI.json` | `"code": "ADVI"`, serials ADVI-001/002/003 |
| `org/projects/REGISTRY.md` | Code column, thread serials, template reference |
| `org/threads/README.md` | Project serial system section, exploratory example, thread ID table, orchestrator CLI example |
| `org/threads/ARCHITECTURE.md` | Project file schema example, THREAD.json schema, receipt naming, staging script example, filter example |
| `org/threads/CONFIG.md` | Thread ID format example, receipt filename example |
| `org/threads/THREAD_KNOWLEDGE.md` | M8 task order prefix example, M9 serial format examples, project template reference |
| `org/AGENT_START_HERE.md` | XML template comment, task order filename examples, filter bash examples |
| `org/tier1_exec/2.0.0_SA_COO/prompt.md` | Active project reference |

Zero `AI-00X` or `AI.json` references remain in the `org/` tree (verified with grep).

### 3. Commit

| Files | Author | Commit |
|-------|--------|--------|
| 9 (rename + PAGE_CODES + 7 updated docs) | `1.0.0_SA_CTO` | `a6adaf16` |

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| 4-char codes for all pages | Prevents future 1-2 char collisions as project list grows; AI collides with common acronym |
| ADVI for AdvisorIntelligence | Disambiguates from generic "AI"; maps cleanly to page name |
| PAGE_CODES.md in org/projects/ | Lives next to the project JSON files it governs; single lookup source |
| Cross-pod codes included (YALP, BDPL, etc.) | Pipelines that span pods or have no single page also need project codes |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/projects/ADVI.json` | Renamed from AI.json; code + serials updated | Yes -- `a6adaf16` |
| `org/projects/PAGE_CODES.md` | Created | Yes -- `a6adaf16` |
| `org/projects/REGISTRY.md` | ADVI migration | Yes -- `a6adaf16` |
| `org/threads/README.md` | ADVI migration | Yes -- `a6adaf16` |
| `org/threads/ARCHITECTURE.md` | ADVI migration | Yes -- `a6adaf16` |
| `org/threads/CONFIG.md` | ADVI migration | Yes -- `a6adaf16` |
| `org/threads/THREAD_KNOWLEDGE.md` | ADVI migration | Yes -- `a6adaf16` |
| `org/AGENT_START_HERE.md` | ADVI migration | Yes -- `a6adaf16` |
| `org/tier1_exec/2.0.0_SA_COO/prompt.md` | ADVI migration | Yes -- `a6adaf16` |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

PAGE_CODES.md is committed at `a6adaf16` with 19 codes covering all 4 pods and 3 AE pipelines.
AI.json renamed to ADVI.json with internal code + serial fields corrected.
All documentation references (`AI-004` examples, `AI.json` template pointers, `--project AI` flags)
migrated to `ADVI-004`, `ADVI.json`, `--project ADVI` across 7 files.

---

## Next Steps

1. **Push to remote** -- `git push origin CLOUD` when DT is ready
2. **Session A: Pod 1 MarketIntelligence enrichment** -- 0.1.0_DE, 0.1.0_DS, 0.1.0_DT, 0.1.1_RD, 0.1.2_RD, 0.1.3_RD
3. **Session C: Pod 3 TradingOperations enrichment** -- 0.3.0_DE, 0.3.0_DS, 0.3.0_DT, 0.3.1_RD, 0.3.2_RD, 0.3.3_RD
4. **Session E: Exec SA enrichment** -- 1.0.0_SA_CTO, 2.0.0_SA_COO
5. **Wave 6: architecture_brief.xml** -- CTO synthesis after all pod + AE + SA prompts confirmed enriched

**Do NOT:**
- Use `AI-` as a serial prefix for any new AdvisorIntelligence threads -- code is now `ADVI`
- Create project JSON files with codes shorter than 4 chars
- Commit `response.json`, `response2.json`, `.tmp_sandp_feb23.json`, or `tfplan` files
