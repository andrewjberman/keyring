---
session: 0.4.2_RD_AdvisorIntelligence~B
date: 2026-05-28
time: ~2017Z
to: MDPF_SCOPED.S1.partner-mode-selector
archetype: IMPLEMENT
---

## MDPF_SCOPED.S1 — partner-mode selector scaffold

### Summary

Delivered scaffold milestone for S1 (Select Partner: dropdown on Model Portfolios).

### Actions taken

1. Read AdvisorIntelligence/index.tsx dispatcher pattern + 49financial partner view dropdown rendering
2. Read ModelPortfolios.tsx (existing Global view — stays intact as scaffold base)
3. Read PageHeaderCleanBadge (has `actions` prop — perfect placement point)
4. Read PageSurfaceControl (as="dropdown" onChange: (value: string) => void — direct setSelectedFirmId pass)
5. Implemented 4 edits to `portal/src/pages/ModelPortfolios.tsx`:
   - Added imports: `useAuth`, `PageSurfaceControl`
   - Added `ALL_MDPF_PARTNER_FIRMS` constant (Global/49financial/inflection)
   - Added `useAuth` + `useState('global')` inside `ModelPortfolios()`
   - Wired dropdown into `PageHeaderCleanBadge actions=` prop (internal-only; exact AI className match)

### Compiler tools

| Tool | Command | Result |
|---|---|---|
| schema-check (pre) | `comp-transform schema-check ModelPortfolios` | WARN: types.ts not co-located (pre-existing, not caused by change) |
| TypeScript | `bun run tsc --noEmit` | CLEAN — no errors |

### Commits

- `d9e74ec3` (portal DEV) — feat(MDPF_SCOPED.S1): scaffold Select Partner: dropdown
- `def371104` (CLOUD) — chore(MDPF_SCOPED.S1): bump portal pointer

### State

RAVC2-Request sent to COO, CC CTO. TO remains in_progress pending S3 artifacts for
per-firm mode wiring (Phase 2). Q1 flag (Global vs 49financial internal default) banked
for COO/Andrew resolution.
