# ANDREW-DIRECT — 2026-09-11 — Portal Visual Elevation: five rulings

**Channel:** `0.1.1_RD_MarketPerformance` terminal, direct.
**Recorded by:** `0.1.1_RD_MarketPerformance`, same turn as receipt, per `org/XXX.md`.
**Scope note:** recorded VERBATIM. This seat does **not** adjudicate scope. Where a ruling could
be read wider than its words, the narrow reading is recorded and the width is flagged, not taken.

---

## The originating instruction

> *"There's gotta be some fast ways to really elevate the look of the dashboard, so that is what I
> want to explore with you. The premise is that it should feel much more elevated, much more
> expensive. Right now it's a little Lucide toy, a little vibe codey. I think there's room here to
> find a minimal expensive look with more mature concepts that don't forego the color of the charts
> themselves. I Think this might take the form of typefaces and more consistency, maybe more subtle
> color scaling. I'm not 100% sure but thats what we need to figure out."*

Preceded by: *"This is our website, I want you to go through it: https://opalinvest.com/. I also
want you to go look at our brand guidelines pdf in the ajb_workspace/deck_generation/ folder."*

And: *"i need you to go get all the skills, pull them into the claude skill folder first and
foremost, then i need you to frontend-dev bun run dev spin up a portal build on 5173 already one
there and go look at everything then basically just keep going through all of this until you have a
plan."* · *"Also lok in here: https://github.com/google-labs-code/design.md"*

---

## RULING 1 — Canvas is LIGHT

**Trigger:** this seat's `/open-calls` CALL 1 — light `#F4F6FA` with inverted `#0A1733` bands,
versus full dark `#0A1733`.
**Andrew, VERBATIM:** *"Agreed with all of the above"*
**Effect:** the portal canvas becomes `#F4F6FA`. `#0A1733` is reserved for deliberate full-bleed
inverted bands. The existing dark theme in `portal/design/brands/opal-capital.json` survives as the
user-selectable toggle rather than being the accidental default.
**Narrow reading recorded:** this rules the PORTAL canvas. It does not rule anything about
`deck_generation/`, the marketing site, or any other surface.

## RULING 2 — Unlicensed third-party skill code is gitignored, not committed

**Trigger:** `/open-calls` CALL 2. Three of six repositories pulled 2026-09-11 report no SPDX
licence: `senlindesign/taste-skill`, `vercel-labs/agent-skills`, `anthropics/skills`.
**Andrew, VERBATIM:** *"Agreed with all of the above"*
**Effect:** those three sources' 13 installed skills are gitignored; a pinned repo+SHA manifest
lives at `design/SKILLS_MANIFEST.md` so any seat re-pulls byte-identical trees. The MIT and
Apache-2.0 sources (`nextlevelbuilder`, `leonxlnx`, `pbakaus`) commit normally.
**APPLIED same turn** — `.gitignore` block added and verified with `git check-ignore -v` on three
ignored paths (all matched) and three licensed paths (rc=1, correctly not ignored).

## RULING 3 — This becomes a registered project

**Andrew, VERBATIM:** *"Agreed with all of the above, i need you to write a big brief that covers
all of this so we can turn it into a full Project. Would go under D12 Platform Operations, I
guess."*
**Effect:** L1 brief authored at `docs/briefs/portal-visual-elevation-brief-20260911.md`.
**⚠ LANE NOTE, surfaced not adjudicated:** Rule 27 assigns L1 to `4.0.0_SA_CRO` only. Andrew
directed THIS seat to write it. The brief is written as instructed; `4.0.0_SA_CRO` and
`1.0.0_SA_CTO` decide whether it is adopted as-is, re-authored in lane, or treated as input.

## RULING 4 — The directive is D13 Design, LAPTOP

**Andrew, VERBATIM:** *"Also ive had MSTR create D13 for Design, it will be laptop fabric"*
**Effect:** supersedes the D12 Platform Operations proposal in RULING 3. Verified present at
`org/missions/DIRECTIVES.yaml` locally and at `origin/CLOUD:498`.
**⚠ REGISTER CAVEAT NOW CLEARED, for the register's owner:** `D13.placement` currently reads
*"LAPTOP — DEFAULTED BY `0.0.0_AB_MSTR` (register owner), **NOT RULED BY ANDREW** ... ONE WORD FROM
HIM CHANGES IT."* Andrew has given that word and it **CONFIRMS** the default. The field should be
restated as Andrew-ruled. **That edit belongs to `0.0.0_AB_MSTR`, not to this seat.**

## RULING 5 — This is NEW work, not a re-frame of existing design work

**Trigger:** this seat surfaced `org/projects/ADHC_DESIGN.json` and the workspace `design/` tree as
possible prior art, which would have made the brief `--midstream`.
**Andrew, VERBATIM:** *"dont get distracted by that, you are doing a new thing here"* · *"Proceed"*
**Effect:** the brief is authored in NEW mode. `ADHC_DESIGN` is **named as a boundary sibling and
not inspected**. This is carried as the brief's largest declared gap (PART VII.1) rather than
suppressed, because the instruction was "do not chase", not "do not disclose".

---

## Prior rulings in the same session, recorded for completeness

- **Identity.** The launch prompt named `0.1.1_RD_MarketOverview`, which is not in the org chart.
  Andrew, VERBATIM: *"i dont remember your username honestly, just assume one of the tier 3 pod 1 RD
  agents"*. Resolved to `0.1.1_RD_MarketPerformance` (slot 0.1.1; its latest log
  `mkov_trends_005_bullet_images.md` corroborates the market-overview scope). No live peer held the
  serial.
- **Comms.** VERBATIM: *"you dont have any need to talk to anybody finish startup and await further
  advisory and i will explain your task"*. Honoured — no messages sent during startup.

---

## Artifacts produced under these rulings

| Path | What |
|---|---|
| `docs/briefs/portal-visual-elevation-brief-20260911.md` | L1 brief, 9 outcomes, 7 parts |
| `design/brand/opalinvest.com.md` / `.json` | `/taste` capture, 3 pages, anti-slop audit passed |
| `portal/DESIGN.md` | Draft visual contract — **unratified**, input to L4 |
| `design/SKILLS_MANIFEST.md` | Pinned repo+SHA provenance for 29 installed skills |
| `.gitignore` | Ruling 2 block, verified effective |

## Broadcast

MCP to `1.0.0_SA_CTO`, `2.0.0_SA_COO`, `3.0.0_SA_CVO`, `4.0.0_SA_CRO`, `0.0.0_AB_MSTR` in the same
turn as this record, with push state stated.
