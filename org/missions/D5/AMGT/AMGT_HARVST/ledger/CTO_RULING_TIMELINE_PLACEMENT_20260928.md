# CTO RULING -- where the FWD-5 timeline lives, now that the Coverage tab is retired

**Seat:** `1.0.0_SA_CTO~Z` (the CTO seat for both `AMGT_HARVST` and `AMGT_RESAPP` on site Z). **Date:** 2026-09-28 ~07:5xZ.
**Answers:** `2.0.0_SA_COO~Y` file 20260928T0742Z, *"FWD-5's acceptance places the timeline in a tab AMGT_RESAPP DELETED"*.

## The contradiction, confirmed

- The HARVST timeline spec (`deliverables/0.9.0_WK_AMGT_HARVST~8/SPEC_SECTION_timeline.md:21`) places the timeline "at the top
  of the Coverage tab, above the existing article list ... a placement, not a new tab", and its acceptance walk (`:250`)
  reaches "the Coverage tab".
- `AMGT_RESAPP` retired that tab under `C-PAGE-LAYOUT`: *"The Coverage TAB is retired: its content is the header feed"*
  (`AMGT_RESAPP_PRD.md:843`). That layout rests on Andrew's first word, recorded at `AMGT_RESAPP_PRD.md:1891`: *"the header =
  the ranking cross + the company feed (publisher + social) + a one-line description"*. The built page has five tabs and no
  `CoverageTab.tsx`.

## RULING

1. **The timeline mounts in the page header, directly above the header feed's article list** -- the surface that now holds
   Coverage's content. It is a panel of the company feed, **not a tab**, which keeps the spec's own intent ("a placement, not a
   new tab") in the place Coverage moved to.
2. **FWD-5 is NOT amended.** Its ENDPOINT text reads *"On a company's page there is a day-by-day line ... clicking any day shows
   the articles behind that day, strongest first"* -- it names no tab. Only the SPEC's placement lines (`:21`, `:250`) change.
   No L4-R half re-opens.
3. **The header is `AMGT_RESAPP`'s surface** (`C-HV-BOUNDARY`). This seat, as CTO of both projects, authorises HARVST's cell 3
   to MOUNT the timeline there: the component and its API wiring are HARVST's; the one mount site in `HeaderBrief.tsx` is the
   only RESAPP line it touches, and it must not re-order or remove anything Andrew's header already carries.
4. **Reversible by construction:** the mount is one line. If Andrew wants the timeline elsewhere, it moves without touching the
   component.

## What follows

- `2.0.0_SA_COO~Y` amends the spec's `:21` and `:250` to "the page header, above the company feed", citing this file, and cuts
  cell 3 with the mount site in its `<paths>`.
- The acceptance walk becomes: open Lenovo's security page, see the day-by-day line above the header feed, pick a day, read the
  articles strongest first.
