# ANDREW-DIRECT 2026-08-11 ~1953Z — OPAL_INVPHL design concept + all nine decisions APPROVED

**Recorded by:** `2.0.0_SA_COO` · **Channel:** COO terminal · **Status:** SOVEREIGN. Verbatim.
**Broadcast:** MSTR (spawn request, same turn) · CTO (project owner) · the build seat on registration.

## VERBATIM

> Approved your artifact-design on Investment Philosophy and all recs, get it done, ask MSTR for any agents you need

## THE REFERENT, AS READ (stated so a different holding can be corrected cheaply)

The approval lands on the design concept I published for his critique at ~1945Z (model-portfolio modal on
two trigger surfaces · `/cma` → `/philosophy` rename · the five-pillar strip and its modals), **and on all
NINE decisions the concept raised, each at my stated recommendation.** *"All recs"* is read as the nine
recommendations in that document — not as anything wider. **The project's design questions are now CLOSED;
what remains is build.** If he meant a narrower object, one line corrects it.

## THE NINE, AS RULED

| # | decision | RULED (my rec, approved) |
|---|---|---|
| 1 | Naming | Page header **"Investment Philosophy"** · sidebar **"Philosophy"** · route `/philosophy` |
| 2 | Performance-pane shape | **Single labelled column**, ordered **Target → YTD → 1Y → Since Inception → Yield → Makeup**. Not the deck's 2×3 grid — the field LIST changed under B-1, so the deck is a format reference, not a template |
| 3 | Modal title name | **CANONICAL** portal name only. **Deck alias DROPPED** — clients never saw the deck |
| 4 | Target Return home | **Per-model range string** (e.g. `"7–9%"`) in the **same file as the model definitions**, so name + colour + target sit in one place. ⚠ *Sub-question still open and NOT ruled: who may change it, and whether it surfaces anywhere else* |
| 5 | Click discoverability | **Name-only hit target** with dotted underline at rest + corner arrow, both going accent on hover/focus. NOT a whole-row/whole-cell target |
| 6 | Old `/cma` URL | **REDIRECT.** Advisors bookmark pages and links live in email; a dead URL is a support ticket for no benefit |
| 7 | Pillar iconography | **Five DISTINCT icons** if slide 9's are clean enough to reuse; **repeated gear is the fallback** if extraction is messy |
| 8 | Narrow-screen strip | **Reflow 3-up then 2-up.** NOT a horizontal scroller — a pillar the client never scrolls to is a pillar they never read |
| 9 | Yang/Manav editable pillar text | **Ship the copy IN THE REPO.** Editability stays a **separately scoped question, NOT folded into this build.** If they need to iterate wording immediately, the cheap intermediate is **a served JSON the publishers already own — never a CMS** |

## WHAT THIS APPROVAL DOES *NOT* AUTHORIZE
- ⛔ **No CMS / admin editor** (decision 9). PRD acceptance 4 still requires a scoping ANSWER on record.
- ⛔ **No new API field, no backend leg, no serving-plane change** — B-1 (Andrew ~1925Z) already dropped
  3-Yr and 2025; the project is **PURE FRONTEND**.
- ⛔ **No second model-name mapping** (B-2) and **no second dialog primitive**.
- ⛔ **The AUM metrics radial legend stays OUT** as a third trigger surface.
- **Decision 4's sub-question** (who may edit Target Return) is unruled and must not be invented by the
  build lane — ship the config, surface the question.

## CARRIED OBLIGATION FROM THE PRD (unchanged by this approval)
**PRD acceptance 5:** the commit that renames the route **also amends CLAUDE.md Rule 25's parenthetical to
cite the ARTIFACT** (`08_capital_market_assumptions`, 1yr life) **rather than the route** — same act, per the
`bd-client-detail` precedent. A rename without it reintroduces map-vs-territory drift.

## STAFFING
Route **(b)** of my own registered condition: **a spawned portal-frontend seat**, requested at MSTR 195359Z
with boot direction. **NOT taken out of the DS lanes** — all three are on the P1-close critical path (9
remaining 49F families, zero ownerless, BAR-CLEARED 2 of 16, every remaining step emission).
**Two task orders (TO-1 model modal, TO-2 philosophy page) dispatch into the seat on registration.**

## RECORDS
Design concept artifact (the approved object) · PRD `docs/architecture/OPAL_INVPHL_PRD.md` · authoritative
dev spec `docs/references/OPAL_INVPHL/primer.md` + `reference_guide.md` · registry
`org/projects/OPAL_INVPHL.json` · B-1 ruling @8fc01e9f98 · project registration @63eca83f34.
