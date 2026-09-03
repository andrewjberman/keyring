---
name: frontend-dev
description: Portal UI verification loop: render a portal route headlessly, READ the screenshot, and check it against the silver-canvas color law before committing any page or visual change. Use whenever building or modifying portal frontend, or on "check the frontend" / "screenshot the portal". Light text or ghost-white buttons outside a dark Panel are the recurring defect a grep cannot see.
---

# /frontend-dev — render, LOOK, then commit

The portal's page canvas is **light silver** (`--bg-page`, `222 24% 81%`). Dark navy panels
float on it. Every recurring UI defect in this class is the same mistake: white-text idiom
(`text-white*`, `text-{color}-300`, `bg-white/N`) placed directly on the canvas instead of
inside a dark container. The law + container table: `portal/CLAUDE.md` ("Color law").
**Canonical design repository: `design/`** (workspace root — brand law
`design/brand/COLOR_ARCHETYPES.md`, portal system `design/systems/portal/`, verification law
`design/process/UI_VERIFICATION.md`).
Reference implementation: `portal/src/pages/SecurityScanner/` + `portal/src/ui/components/panels/`.

## The loop (run for EVERY new/changed portal page or visual component)

1. **Dev server** (if not already running — check first: `curl -s -o /dev/null -w '%{http_code}' http://localhost:5175`):
   ```bash
   cd portal && /c/Users/AndrewBerman/.bun/bin/bun run dev --port 5175
   ```
   (run_in_background; vite auto-bumps the port if taken — read the actual port from its output).

2. **Screenshot the route** (from `portal/`; auth is stubbed — no credentials, no devBypass):
   ```bash
   node scripts/ui-smoke.mjs <route-without-leading-slash> <out.png> --port <port> [--fixtures f.json]
   ```
   - Route **without** the leading slash (MSYS mangles `/x` args; the script also de-mangles).
   - `--fixtures f.json`: `{ "<url-substring>": <response-body>, ... }` to render realistic
     rows when the backend has no data. Longest substring wins. Put fixture files in the
     session scratchpad, not the repo.
   - Interactive states (open form, modal, hover): copy the script's pattern and add
     `page.click(...)` before the screenshot — see the incident record for a worked example.

3. **READ the PNG** (Read tool) and check, in this order:
   - `LOC` printed by the script matches the route (a silent bounce to `/login` or `/` means
     you screenshotted the wrong page — fix the run, not the checklist).
   - **No light text / light buttons directly on the silver canvas.** Content lives inside
     `Panel > PanelHeader > PanelContent`; page-level action buttons go in the
     `PanelHeader actions` slot.
   - Canvas-level notices/errors are dark-on-light (`text-red-900` on `bg-red-500/10`), never
     `text-{color}-300`.
   - `Panel variant="nested"/"heatmap"` are LIGHT (74%) — dark text inside those.
   - Empty state, error state, and any toggled panel (form open) each get their own screenshot
     when the change touches them.

4. **Only then** typecheck + commit (portal commits respect any active DEV-push freeze).

## Traps (each one cost real time — do not rediscover)

- **Color comments lie.** Components said "light blue" for tokens that resolve navy 25%
  (rebrand lag). Resolve live: the script prints the canvas; for any token,
  `getComputedStyle(document.documentElement).getPropertyValue('--...')` in the page.
- **"Same classes as SecurityScanner" is NOT verification** — SecurityScanner's whites are
  inside `Panel`; the classes are only legal in that containment. This exact reasoning
  shipped the TicketCenter defect.
- **Shared Playwright-MCP browser locks.** Never point playwright at the MCP profile; the
  script launches system Edge with a fresh headless profile.
- **Credentialed CORS rejects wildcard origins** — the script's auth stub echoes the exact
  dev origin; keep it that way if you copy the pattern.
- A full `page.goto` after an in-page auth stub RELOADS the app and drops in-memory auth;
  the script stubs `/auth/refresh` instead so every load self-bootstraps.

Incident record + before/after screenshots: session log 0.5.0_AE_OpalETL 2026-07-15
(Andrew-direct #6); design doc `portal/src/ui/components/panels/README.md`.
