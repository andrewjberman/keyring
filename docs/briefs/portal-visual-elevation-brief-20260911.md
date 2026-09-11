# L1 BRIEF — Portal Visual Elevation

**Authored** 2026-09-11 by `0.1.1_RD_MarketPerformance` at Andrew's direct instruction.
**Mode** NEW (Andrew-direct 2026-09-11, VERBATIM: *"dont get distracted by that, you are doing a
new thing here. Proceed."* — ruling that this is not a midstream re-frame of any existing design
work).
**Consumer** `/endpoint --forward` at L2 (`1.0.0_SA_CTO`). Every numbered thing below is citable.

---

## ORIGIN — what created this brief

Andrew, 2026-09-11, VERBATIM:

> *"There's gotta be some fast ways to really elevate the look of the dashboard... The premise is
> that it should feel much more elevated, much more expensive. Right now it's a little Lucide toy,
> a little vibe codey. I think there's room here to find a minimal expensive look with more mature
> concepts that don't forego the color of the charts themselves. I Think this might take the form
> of typefaces and more consistency, maybe more subtle color scaling. I'm not 100% sure but thats
> what we need to figure out."*

Three rulings followed the same day, on this seat's `/open-calls` (VERBATIM: *"Agreed with all of
the above"*):

1. **Canvas is LIGHT** — `#F4F6FA` with intentional `#0A1733` inverted bands, not full dark.
2. **Unlicensed third-party skill code is gitignored, not committed**, with a pinned
   repo+SHA manifest so any seat re-pulls byte-identical.
3. **This becomes a registered project.** Andrew first proposed D12 Platform Operations with
   explicit uncertainty (*"Would go under D12 Platform Operations, I guess."*). This brief
   surfaced two measured facts against that placement (§V.4). Andrew then resolved it, VERBATIM:
   *"Also ive had MSTR create D13 for Design, it will be laptop fabric"*. **The directive is
   D13 Design, LAPTOP.**

---

## PART I — THE OUTCOME TERRITORY

Nine outcomes. Each is one thing a named kind of person can DO.

### O1 — A prospect moving from the website into the portal does not experience a change of firm

Today a prospect crosses from `opalinvest.com` into the portal and every measurable visual
dimension changes at the boundary: typeface, canvas colour, corner radius, whether focus is
visible, and whether navy is a background or a text colour. O1 is complete when that crossing is
not perceptible as a change of system.

### O2 — An advisor reads a figure without the typeface telling them it came out of a terminal

Every number in the product currently renders in the browser's code-editor stack. O2 is complete
when figures are set in the firm's own typeface with tabular alignment, and column alignment is
no worse than it is today.

### O3 — An advisor reads the ORDER of an ordered scale off its colour, without consulting a legend

Duration ladders, performance bands and over/under-weight scales are ordered quantities. O3 is
complete when each is encoded as one hue ramped light-to-dark, and no ordered quantity anywhere in
the product is encoded as unordered hue.

### O4 — An advisor can tell at a glance which single thing on a screen is the action to take

O4 is complete when a view spends its accent colour on the one primary action and nothing else —
segmented controls, tabs and toggles mark their active state by weight and rule, not by a filled
accent chip per option.

### O5 — An advisor working by keyboard can see where they are

O5 is complete when focus is visible on every interactive element in the product, using the same
ring the firm's own website already ships.

### O6 — An engineer or an agent building a new portal page derives every visual decision from one written contract, and a reviewer can FAIL the page against it, citing the clause

O6 is complete when there is one contract that resolves typeface, colour role, spacing, shape,
elevation, focus and layout split; when it is the file the estate's design tooling reads; and when
a reviewer rejecting a page can point at the clause it violates rather than at their own taste.

### O7 — A chart series is never painted in the colour the product reserves for "something is wrong"

O7 is complete when status colour and data colour are two separate systems with no aliasing
between them, and a reviewer can demonstrate the separation.

### O8 — Two charts on the same screen share their axis, tick, tooltip and legend treatment

O8 is complete when a screen's charts come from one rendering system, so that visual conventions
are a property of the product rather than of whichever library that page happened to import.

### O9 — Andrew can put the portal on screen beside an institutional competitor and the difference is not that ours looks generated

O9 is the outcome the other eight serve, and it is the one Andrew can grade directly. It is
complete when the comparison turns on capability rather than on finish.

---

## PART II — WHERE THE BOUNDARY SITS

**This owns:** the portal's visual layer — the token set and the three files that currently write
it; typography including numerals; colour ROLE assignment (canvas, field, accent, status, data);
spacing, shape and elevation; focus behaviour; consolidation of the charting and icon
dependencies; the written contract (`portal/DESIGN.md`); and the verification gate that enforces
it.

**This does NOT own, and merely relies on:**

- **Data correctness and freshness.** Every screenshot in §VI was captured against an environment
  returning 401s and empty sets. That is out of scope here and must not be pulled in.
- **Information architecture** — which panels exist on a page and what they show. This project
  changes how a panel looks, not what it is for.
- **Route structure, auth, and the backend API.**
- **`deck_generation/`** — the PowerPoint system has its own design law (`DESIGN_BIBLE.md`) and its
  own composer. This project cites that law as precedent and changes nothing inside it.
- **`opalinvest.com`** — the marketing site is the reference surface, not a deliverable. Nothing
  here proposes editing it.

**Sibling projects named, so the decomp does not re-litigate them:**

- `ADHC_DESIGN` — an existing design-scoped project in the registry. **Named here as a boundary,
  not inspected** (Andrew directed this brief away from it). If its scope intersects, that
  intersection is resolved at L3 registration, not in decomposition.
- `IRPT_FNTEND` (D9) — investor-reporting frontend. Shares the portal tree and will inherit any
  token change. It is a CONSUMER of this project's contract, never a sub-scope of it.
- `ADHC_MKOVFX` — market-overview fixes. Same tree, different axis (behaviour, not finish).
- `NFRA_REPORT` (D12) — named only because D12 was the original placement proposal. With the
  directive resolved to D13 (§V.4) it is no longer a sibling, and is listed so the decomp does not
  rediscover the discarded option.

---

## PART III — THE QUALITATIVE BAR

No numbers are invented here. Each statement below is contestable, which is the test.

1. A prospect who clicks from the website into the portal does not notice the handoff.
2. An advisor reading a return figure cannot tell from its typeface whether it came from the
   product or from a developer's console.
3. No screen spends its accent colour more than once.
4. An ordered quantity is never encoded as unordered hue anywhere in the product.
5. The product's charts remain as colourful as they are today; what goes quiet is the chrome
   around them. **Removing colour is a failure of this project, not a success of it** — Andrew's
   constraint, verbatim: *"don't forego the color of the charts themselves."*
6. A reviewer can reject a page by citing a clause, and the page's author agrees the clause was
   violated without further argument.
7. Dark mode is a choice a user makes, not the residue of a stylesheet declaration.
8. A new page built by an agent that has never seen the portal lands inside the system on the
   first attempt.
9. The visual system survives a reader who has raised their browser's default font size.

---

## PART IV — THE SUBSTRATE: is this in a canonical pattern?

Findings, each with what was measured.

### IV.1 — The brand book cannot govern a dashboard, and that is the root cause

**Measured:** `deck_generation/brand/opal_brand_guidelines.pdf`, 13 pages, text-extracted. Pages
3–7 are logo usage. The entire system is four colours (`#163372`, `#0A1733`, `#C4CBDB`, `#5F3BE3`)
and one typeface (Lato, four hierarchy rows). It specifies no neutral ramp, no data-visualisation
palette, no elevation model, no density rule and no state colours.

**Finding:** a dashboard needs all five. Whoever built the portal filled the gap from a free
Bootstrap admin template, and that is the mechanism behind "vibe codey" — not carelessness, a
missing specification.

### IV.2 — The website is a complete, measurable design system, and nobody has read it into the product

**Measured:** headless capture at 1440×900 across three pages (`/`, `/investment-platform/`,
`/opal-ai/`) on 2026-09-11 using the `taste` skill's extractor. Full output:
`design/brand/opalinvest.com.md` and `.json`. Values marked [3/3] agreed on all three pages.

- Canvas `#F4F6FA` at **56.3 / 64.0 / 67.1 %** of visible surface [3/3]
- Dark field `#0A1733` at **20.3 / 20.9 / 31.1 %** [3/3]
- Accent `#5F3BE3` never above **1.0 %** [3/3]
- **Opal Navy `#163372` at 0.2–0.4 %** — a text and hairline colour, **not a surface** [3/3]
- **Lato exclusively** (313 / 332 / 187 elements), weights **400 and 700 only** [3/3]
- `letter-spacing: normal` on every measured heading and body node [3/3]
- Radii **2, 3, 4px** plus pill and circle. No mid-range radius exists on the site.
- **Zero drop shadows** [3/3]. The only `box-shadow` measured is a purple 2px focus ring.
- `focusVisible: true` [3/3]; `prefers-reduced-motion` respected [3/3]
- Two-column grid `506.594px / 759.906px` — a 40/60 split, byte-identical across all three pages

### IV.3 — The portal contradicts that system on every dimension but one

**Measured** in `portal/src/` at 2026-09-11:

| Dimension | Site | Portal | Evidence |
|---|---|---|---|
| Typeface | Lato | Inter | `src/index.css:16`, `:142` |
| Numerals | Lato tabular | code-editor mono | **222** `font-mono` occurrences, no `--font-mono` defined |
| Canvas | `#F4F6FA` | `#C3CADA` mid-silver | `src/index.css:52` |
| Navy | text/hairline | panel surface | three-tier navy nesting |
| Status colours | brand-derived | Creative Tim "Argon" template | `src/index.css:40-43` |
| Chart colours | separate system | **aliased onto status** | `src/index.css:111-115` |
| Loudest colour | purple ≤1% | chartreuse `#ADFF2F` | `src/index.css:69` |
| Radius | 2–4px | 6–8px uniform | `--radius: 0.5rem` |
| Shadows | none | none | **the only agreement** |
| Focus ring | visible purple 2px | `outline: none !important` | `src/index.css:166` |
| `color-scheme` | n/a | `dark` on a light canvas | `src/index.css:132` |

### IV.4 — The token architecture is already correct and already live; only its VALUES are wrong

**Measured:** `portal/design/brands/opal-capital.json` is a well-formed brand token file carrying
navy `#183472`, indigo `#5E3BE2`, silver `#C3CADA` and a complete nine-step dark-navy ramp with
semantic mappings. It is wired live at `portal/src/main.tsx:7` via generated
`design/themes/opal-capital.css`.

**Finding:** this is a value-swap against an existing architecture, not a rebuild. That materially
lowers the risk of every outcome in Part I.

### IV.5 — One of the three token writers is dead code

**Measured:** `portal/tailwind.config.js` declares Tailwind's stock `sky` and `slate` ramps as
`primary`/`secondary`. Under Tailwind **v4.2.1** with no `@config` directive in `src/index.css`,
that file is never loaded, and `primary-500` / `secondary-400` appear in **0** source files.

**Finding:** it is confusing, not causal. Deleting it is cleanup; it explains nothing.

### IV.6 — Dependency duplication is the mechanism behind "inconsistency"

**Measured** by import census across `portal/src/`:

- **Four charting libraries**: recharts (36 files), apexcharts (4), @nivo (1), visx (1), plus
  ag-grid (5).
- **Two icon sets**: lucide-react (102 files), phosphor-react (1).
- **Two animation libraries**: `framer-motion` and `motion` both in `dependencies`.

**Finding:** four renderers cannot produce one visual system. O8 is unreachable without
consolidation.

### IV.7 — The estate already has the pattern this project needs

**Measured:** `design/` exists at the workspace root with `brand/COLOR_ARCHETYPES.md`,
`systems/portal/DESIGN_SYSTEM.md`, `process/UI_VERIFICATION.md`; and a verification loop exists as
the `frontend-dev` skill plus `portal/scripts/ui-smoke.mjs`, which renders a route headlessly and
prints the resolved canvas colour.

**Finding:** this project does **not** need a new design repository, a new verification mechanism
or a new gate pattern. It populates and enforces ones that already exist. A parallel structure
would be a shadow system and is banned.

### IV.8 — A contract format exists that the estate's design tooling already reads

**Measured:** `google-labs-code/design.md` specifies `DESIGN.md` — YAML token front matter plus
prose rationale. `pbakaus/impeccable` v4.3.1 (installed) loads `DESIGN.md` at session start as its
visual authority.

**Finding:** `DESIGN.md` is the container that makes agent design tooling produce Opal's system
instead of its own defaults. A first draft has been written to `portal/DESIGN.md`; it is a
**candidate for L4 ratification, not a ratified artifact.**

---

## PART V — WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

Named, not sequenced. Sequencing is L5.

1. **Lato must be self-hostable in the portal.** `opalinvest.com` self-hosts it as woff2 at five
   weights, which is evidence it is licensed for web serving — but this brief did **not** verify
   the licence terms. Confirm before relying on it.
2. **The three-writer problem must be resolved.** Token values are currently written by
   `src/index.css` `:root`, by generated `design/themes/opal-capital.css`, and (dead) by
   `tailwind.config.js`. A change applied to one is not applied to the product.
3. **The light-canvas ruling is settled** (Andrew, 2026-09-11). Every colour outcome descends from
   it. The existing dark theme survives as the user-selectable toggle.
4. **Directive placement — RESOLVED 2026-09-11. The directive is D13 Design, LAPTOP.**
   Recorded here because the reasoning matters to L3 and because the register carries a caveat
   that this ruling clears.

   Andrew first proposed D12 Platform Operations, with explicit uncertainty. Two measured facts
   sat against it: (a) **`DIRECTIVES.yaml` places D12 on SITEZ**, while the portal is a submodule
   of this LAPTOP fabric; (b) D12's members — `PLATFORM_OPS_USERMGMT`, `D12_PHONE_OTP_ALL_AWS`,
   `NFRA_OPSEC202609`, `NFRA_REPORT`, `NFRA_IAMROLES202609` — are authentication, security and
   reporting infrastructure, not client-facing surface.

   Andrew resolved it by minting a new directive, VERBATIM: *"Also ive had MSTR create D13 for
   Design, it will be laptop fabric"*.

   ⚠ **This clears a standing caveat in the register.** `D13.placement` currently reads
   *"LAPTOP — DEFAULTED BY `0.0.0_AB_MSTR` (register owner), NOT RULED BY ANDREW... ONE WORD FROM
   HIM CHANGES IT."* Andrew has now given that word, and it **confirms** the default rather than
   changing it. The placement field should be restated as Andrew-ruled. That edit belongs to the
   register's owner, not to this brief — surfaced, not adjudicated.

   Verified present at `org/missions/DIRECTIVES.yaml` both locally and at `origin/CLOUD:498`
   on 2026-09-11. **This project is D13's first client-facing-surface member.**
5. **Portal commits respect any active DEV-push freeze**, and a shared branch is pushed only by
   `0.0.0_AB_MSTR` on Andrew's word.
6. **Third-party skill provenance.** Six repositories were pulled on 2026-09-11; three carry no
   licence file (`senlindesign/taste-skill`, `vercel-labs/agent-skills`, `anthropics/skills`) and
   three are licensed (`nextlevelbuilder/ui-ux-pro-max-skill` MIT, `leonxlnx/taste-skill` MIT,
   `pbakaus/impeccable` Apache-2.0). Andrew ruled the unlicensed three are gitignored with a
   pinned manifest.
7. **A reviewer-facing gate must exist** or O6 is unenforceable and the system decays back.

---

## PART VI — STATUS  ⛔ **NOT OUTCOME-BEARING**

Do not cut outcomes from this part. It is a snapshot and it ages.

**Measured at 2026-09-11, portal dev server on :5173, branch `CLOUD` / portal `DEV`.**

- Three routes rendered headlessly at 1440×900 and read as images: `/market`, `/positioning`,
  `/portfolio-management`. All three resolved canvas `rgb(195,202,218)`.
- `/positioning` carries **five distinct button idioms on one screen**, including a five-hue
  segmented control (`UST · ST · INT · LT · ULT`) encoding an ordered duration ladder.
- All three pages nest **three rounded containers deep**, each a different navy.
- Roughly the lower third of each captured page is empty canvas.
- `/portfolio-management` renders a native unstyled `<select>` with an OS chevron.
- `/market` renders a duplicated error string in red directly on the canvas, which violates the
  portal's own documented colour law.
- The data environment was failing at capture time (401s, empty sets). **Chrome was assessed;
  populated density was not.**
- 29 design skills were installed to `.claude/skills/` from six repositories on 2026-09-11.
- `portal/DESIGN.md` and `design/brand/opalinvest.com.{md,json}` exist as **uncommitted drafts**.

---

## PART VII — WHAT THIS BRIEF DOES NOT CLAIM

1. **Prior art inside the estate's own design system is UNMEASURED.** `ADHC_DESIGN`,
   `design/systems/portal/DESIGN_SYSTEM.md`, `design/brand/COLOR_ARCHETYPES.md` and
   `design/process/UI_VERIFICATION.md` were located but **not read** — a tool error interrupted the
   read and Andrew directed this brief away from that thread. **This is the largest known gap in
   this brief**, and it bears directly on §IV.7. L2 or L4 should close it before the PRD commits to
   a contract shape.
2. **Three of twenty-six routes were rendered.** The other twenty-three are unmeasured, and the
   defect counts in §IV.3 are code-wide while the visual findings in §VI are not.
3. **Responsive and mobile behaviour was not measured at all.** Every capture was 1440×900.
4. **No contrast ratios were computed.** Accessibility claims here are structural (focus
   visibility), not colorimetric.
5. **Lato's licence was not verified** — see §V.1.
6. **Density was not assessed against real data**, because there was none at capture time.
7. **The star counts in Andrew's source table were wrong in three places** and were corrected
   against the GitHub API on 2026-09-11; the table had conflated two different `taste-skill`
   repositories. `ui-skills/ui-skills` did not resolve and was never assessed.
8. **`portal/DESIGN.md` is a draft authored by this seat**, not a ratified contract. It is offered
   as input to L4 and carries no authority until then.
9. **No estimate of effort or duration appears anywhere in this brief**, deliberately. A number
   invented at L1 is treated as ratified by every later stage.

---

## REFS TO CARRY

```
BRIEF PATH        docs/briefs/portal-visual-elevation-brief-20260911.md
PROJECT           NONE-YET  (CTO mints at L3)
DIRECTIVE         D13 Design (LAPTOP) -- RULED by Andrew 2026-09-11, see PART V.4.
                  Supersedes the initial D12 Platform Operations proposal.
                  This is D13's first client-facing-surface member.
EXISTING PRD      NONE  (D13's own directive doc docs/architecture/D13_DESIGN_PRD.md is
                  referenced by the register; not read by this brief)
SIBLING PROJECTS  ADHC_DESIGN (named, not inspected) - IRPT_FNTEND (D9) - ADHC_MKOVFX
PRIOR ART         portal/design/brands/opal-capital.json (live token architecture, correct shape)
                  design/ (workspace design repository -- LOCATED, NOT READ, see PART VII.1)
                  frontend-dev skill + portal/scripts/ui-smoke.mjs (verification loop, exists)
                  deck_generation/DESIGN_BIBLE.md (precedent: colour law B1, dark->light traversal)
MEASURED AT       2026-09-11, portal :5173, branch CLOUD / portal DEV
                  opalinvest.com captured 2026-09-11 at 1440x900, 3 pages
CAPTURE OUTPUT    design/brand/opalinvest.com.md - design/brand/opalinvest.com.json
CONTRACT DRAFT    portal/DESIGN.md  (draft, unratified)
ANDREW RULINGS    2026-09-11 -- light canvas - gitignore unlicensed skills + manifest
                  - register as a project - "you are doing a new thing here"
```
