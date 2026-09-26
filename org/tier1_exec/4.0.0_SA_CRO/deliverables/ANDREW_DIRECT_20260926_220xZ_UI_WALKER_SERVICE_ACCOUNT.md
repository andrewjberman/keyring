# ANDREW-DIRECT 2026-09-26 ~22:0xZ -- a service account that walks the pages visually, and a /ui-walk skill

**Channel:** the 4.0.0_SA_CRO terminal. **Recorded by:** 4.0.0_SA_CRO, the same turn.

## Verbatim

> "we need a service account setup that can walk these pages visually, I need you to just build it, and then create a
> skill that logs in through a protected dev channel and walks these pages for development purpose, to see what is
> going on on the frontend (test fixtures, dropdowns, pages, modals, expands, etc.), with the intent of developing
> briefs specific to frontend dev. Should be looking for UI failures, dropdowns that appear behind nav bars,
> unnecessary drilldown layers, unconnected endpoints (showing "unavailable" or "Not supplied" because there is no
> connection for a given field), breaks from canonical design patterns, etc."

## What it binds, as built by this seat

1. **The service account:** ONE standing identity in `opal-users-v2`.
   - Identity: `USER#usr_opal_ui_walker` / `PROFILE`, e-mail `opal-ui-walker@opal.test`, `role admin`, `firmId
     opal-capital`, `userType Dev`. The /investor-reporting page admits only that combination.
   - **DORMANT at rest:**
     - `status disabled`, and the password hash is one nobody knows;
     - there is no SSM parameter;
     - `arm` mints a fresh random password into SSM `/opal/ui-walker/password` for ONE walk and sets it active;
     - `disarm` disables it, replaces the hash, deletes the parameter, and proves a login is refused.
   - The superadmin reach therefore exists only while a walk runs; the last access token dies within 15 minutes of
     `disarm`.
   - Tool: `.claude/skills/ui-walk/ui_walker_account.py`.
2. **The protected dev channel:**
   - The walker refuses any base URL that is not `localhost`: the local `bun run dev:live --port 5174` build, which
     reaches the live data and auth front door through CloudFront.
   - A browser-side network guard admits only GET/HEAD/OPTIONS and the POSTs `/auth/login`, `/auth/refresh`,
     `/auth/logout`, `.../directory/resolve` and `.../selections`. It aborts and logs every other request, so the walk
     cannot export, upload, submit, send telemetry or call `/auth/admin/*`.
   - Walker: `.claude/skills/ui-walk/walk.mjs`.
3. **The skill:** `.claude/skills/ui-walk/SKILL.md` (`/ui-walk`).
   - It walks search, tabs, dropdowns, expands, drill rows and account pickers, screenshotting every step.
   - It checks: occluded dropdowns; unconnected fields ("not supplied", "unavailable", "Unknown", "withheld", raw
     codes); duplicate choices; one-child drill layers and one-slice pies; duplicate chart colours; DESIGN.md C3
     bands; contrast; C12 tinted status blocks; mixed money and date formats; truncation; API answers not READY.
   - Output goes to the gitignored `tmp/ui-walk/<stamp>/`, because screenshots carry client data.
   - The skill turns a walk into a frontend brief in the UIR register shape (`docs/briefs/irpt-ui-review-*`).

## Why no never-widen packet

Earlier walk principals ran under per-window never-widen packets (CTO + CRO halves). This act is Andrew's direct
order to this seat ("I need you to just build it"), so no packet was cut. The dormant-at-rest design keeps the
standing reach at zero between walks. `1.0.0_SA_CTO` gets a decision copy.
