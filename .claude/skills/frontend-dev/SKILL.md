---
name: frontend-dev
description: Portal UI verification loop: render a portal route headlessly, READ the screenshot, and check it against the portal's colour law (the light #F4F6FA canvas, white hairline panels, navy ink, ONE band per page) before committing any page or visual change. Use whenever building or modifying portal frontend, or on "check the frontend" / "screenshot the portal". Light text or ghost-white fills anywhere but the band are the recurring defect a grep cannot see.
---

# /frontend-dev — render, LOOK, then commit

**The law is `portal/CLAUDE.md` ("Color law") and the contract is `portal/DESIGN.md` (C1..C12); this skill only runs
the check.** Andrew-direct 2026-09-11 superseded the 2026-07-15 "silver canvas" archetype one way: a page or comment that
still calls the canvas silver, or makes a dark container the default, describes the retired vintage.

- The page canvas is light `#F4F6FA` (`--bg-page`); the screenshot script prints it and it must read `rgb(244, 246, 250)`.
- Containers are white `#FFFFFF` panels marked by a 1px `#C4CBDB` hairline, no shadow; ink is navy `#163372`.
- `#0A1733` is ONE deliberate full-bleed band per page (C3), never the default container. The white idiom
  (`text-white*`, `text-{color}-100..300`, `bg-white/N`) is legal ONLY on the band; on the canvas and on every white
  panel it is near-invisible and illegal.
- The charts keep their colour (C6); what goes quiet is the chrome.

**Canonical design repository: `design/`** (workspace root — brand law `design/brand/COLOR_ARCHETYPES.md`, portal system
`design/systems/portal/`, verification law `design/process/UI_VERIFICATION.md`).
Reference: `portal/src/ui/components/panels/` (README there) and the contract's clauses, not any one page.

## The loop (run for EVERY new/changed portal page or visual component)

1. **Dev server on port 5174, the only dev port** (portal law, Andrew-direct 2026-09-24). Check first:
   `curl -s -o /dev/null -w '%{http_code}' http://localhost:5174`. If it is not up, from `portal/` run
   `bun run dev --port 5174` in the background (resolve `bun` from the profile; never bake a path).

2. **Screenshot the route** (from `portal/`; auth is stubbed — no credentials, no devBypass):
   ```bash
   node scripts/ui-smoke.mjs <route-without-leading-slash> <out.png> --port 5174 [--fixtures f.json] [--click <name>]
   ```
   - Route **without** the leading slash (MSYS mangles `/x` args; the script also de-mangles).
   - `--fixtures f.json`: `{ "<url-substring>": <response-body>, ... }` to render realistic rows when the backend has no
     data. Longest substring wins. Put fixture files in the session scratchpad, not the repo.
   - `--dist <built dir>` serves a vite build from disk (no port bound) when the change lives on a branch the 5174
     server is not running.
   - Interactive states (open form, modal, hover): `--click`, or copy the script's pattern and add `page.click(...)`.

3. **READ the PNG** (Read tool) and check, in this order:
   - `LOC` matches the route (a silent bounce to `/login` or `/` means you screenshotted the wrong page — fix the run,
     not the checklist), and `CANVAS` reads `rgb(244, 246, 250)`.
   - **No light text, light buttons or ghost-white fills off the band** — not on the canvas, not on a white panel.
     Content lives inside `Panel > PanelHeader > PanelContent`; page-level actions go in the `PanelHeader actions` slot;
     ONE `#5F3BE3` primary action per view (C8).
   - **At most one band per page (C3).** `Panel variant="chart"/"mixed"` and the `--bg-header`/`--bg-medium`/`--bg-card`
     tiers still resolve to the band (a stated divergence in `portal/CLAUDE.md`): a new page does not reach for them to
     get the white idiom back.
   - **Canvas-level errors are a `status.danger` icon beside navy text, never a red block or a translucent tint (C12,
     C5.8).**
   - Empty, error and any toggled state (form open, modal) each get their own screenshot when the change touches them.
   - A rejection cites the contract clause NUMBER beside its evidence ("C3", "C5.8", ...).

4. **Only then** typecheck (`bun run typecheck`, never bare `tsc --noEmit`) and commit; portal commits respect any
   active DEV-push freeze.

## Traps (each one cost real time — do not rediscover)

- **Color comments lie.** Comments still call the canvas "silver" (row DSGN_REBRND-W2-S15) and once called a navy token
  "light blue". Resolve live: the script prints the canvas; for any token,
  `getComputedStyle(document.documentElement).getPropertyValue('--...')` in the page.
- **"Same classes as another page" is NOT verification** — a white idiom is legal only on the band. This exact reasoning
  shipped the TicketCenter defect.
- **Shared Playwright-MCP browser locks.** Never point playwright at the MCP profile; the script launches system Edge with
  a fresh headless profile.
- **Credentialed CORS rejects wildcard origins** — the script's auth stub echoes the exact dev origin; keep it that way if
  you copy the pattern.
- A full `page.goto` after an in-page auth stub RELOADS the app and drops in-memory auth; the script stubs `/auth/refresh`
  instead so every load self-bootstraps.

History: the 2026-07-15 incident record (session log 0.5.0_AE_OpalETL, Andrew-direct #6) is the old-canvas vintage; the
current law is `portal/CLAUDE.md` and `portal/DESIGN.md`.
