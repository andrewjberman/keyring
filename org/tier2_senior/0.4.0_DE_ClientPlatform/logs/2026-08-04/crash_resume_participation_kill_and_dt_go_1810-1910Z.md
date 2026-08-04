# Crash-resume: participation-UI Kill Both executed, FE slate closed, DT GO issued — 0.4.0_DE_ClientPlatform

**Date:** 2026-08-04 (~18:10–19:10Z)
**Task Order:** MDPF_CHANNEL_INDEPENDENCE.CI-R6R.held-vs-measured-render (closed-by-ruling) + Andrew-direct deploy push (ad-hoc)
**Status:** COMPLETE (session leg); Phase-3 PROD render verify pends DT deploy-land (event-driven)

---

## Objective

Resume after session crash (Andrew-direct: identify where work left off from commits+messages,
continue), finish the FE slate for the portal deploy (MDPF pointing + LTA->ULT/LTC->LT), and
resolve the held participation-footnote question.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| to-check | `python .tools/to-check.py --all --assignee 0.4.0_DE_ClientPlatform` | PASS | 10 TOs surfaced; CI-R6R pending row identified as the live thread |
| tsc (portal gate) | `bun x tsc -b` (x2: at resume HEAD, post-edit) | PASS | exit 0 both runs |
| ui-smoke | `node scripts/ui-smoke.mjs portfolios <png>` | PASS | /portfolios renders post-deletion; honest-absent states intact; no footnote. (First run used wrong route slug `model-portfolios` — route is `/portfolios`; App.tsx:408 read) |
| comp-surface-check | via portal pre-commit (auto) | PASS (BLOCKED->ACK) | SEV1 on model_portfolios.headline/benchmark as designed; SURFACE_ACK audited citing Andrew-direct ruling, same pattern as accepted 68fd700c |

**What worked:** to-check --all found the live thread instantly; ui-smoke as the scripted render
instrument (per Andrew: no manual visual fumbling — ask him for eyes-on).
**What failed:** none. **Gap found:** none.

---

## Work Completed

### 1. Crash-state recovery (no loss)
Portal DEV HEAD at resume = `68fd700c` (edict items, CTO-accepted 173318Z) atop `70c884ae`
(LTA->ULT/LTC->LT rename) — both Andrew-named work items already committed pre-crash; working
tree had zero modified tracked files. DT's "two urgent defect items" resolved as the edict items
themselves. Straggler-check: all remaining LTA/LTC references are the intended vintage-tolerant
legacy-alias seams.

### 2. Andrew-direct rulings recorded + broadcast (@20bf1b1f7)
(1) Finish FE, get the deploy out; visual smokes = ask Andrew. (2) Held footnote question
resolved "**Kill both**" — T3 Carry-windows footnote AND rare-outage T2 dark markers die; no
participation rendering at all (widens ~05:4xZ no-carried-UI). Broadcast: COO/CTO/MSTR + DS + DT.

### 3. Participation-UI deletion (portal DEV `45e5843f`)
Deletion-only, one file (`src/pages/ModelPortfolios.tsx`, 25+/126-): import trim, 5-memo
derivation block, absent tooltip rows, window-end ReferenceLines, footnote block, stale
held-pending comments. Data-layer meta + `pairedProvenanceRead.ts` helpers untouched (no other
consumers — grep-verified). `shownPeriods`/`rowPayload` liveness confirmed before deletion.

### 4. DT GO issued (190529Z)
FE slate complete on DEV: `7d544d27` + `70c884ae` + `68fd700c` + `45e5843f`. DT holds scoped
promote authority (Andrew ~1727Z, CTO relay 173318Z). DS producer ships on DT's deploy ping;
DS also warned their participation emission is now render-consumerless (190743Z).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Asked Andrew the footnote question instead of inferring | Explicitly his held call; he was present; NO-INFERRED-GATES law cuts both ways |
| SURFACE_ACK self-invoked with audited Andrew-direct citation | Exact pattern CTO accepted on 68fd700c hours earlier; holding for permission on a sovereign-ordered deletion = manufactured gate |
| Lib read-helpers kept despite dead render usage | Consistent with ~0450Z precedent (readGlobalCarriedDates kept); minimal pre-deploy diff |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/ModelPortfolios.tsx` | Participation UI deleted in full | Yes — portal `45e5843f` (DEV) |
| `org/.../deliverables/ANDREW_DIRECT_20260804_18xxZ_FINISH_FE_DEPLOY_AND_KILL_BOTH_PARTICIPATION_UI.md` | Verbatim record | Yes — `20bf1b1f7` (CLOUD) |

---

## Blockers

None. Phase-3 PROD render verify is event-gated on DT's deploy-land ping (not a blocker — DT has GO).

---

## Current State

DT executing /prod-deploy on `45e5843f`. On land ping: Phase-3 render verify on PROD (benchmarks
heatmap + scatter on the real artifact, after DS's producer lands). Stray `portal/portal/` junk
dir (org/, public/) noted in the portal working tree — untracked, not mine, surfaced here for
hygiene routing.

— 0.4.0_DE_ClientPlatform
