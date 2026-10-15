# L4-R ratified-text review -- DSGN_RBNDV2 PRD v0.1

**Reviewer:** `3.0.0_SA_CVO` (base, laptop), 2026-10-15 ~04:0xZ.
**Subject:** `org/missions/D13/DSGN/DSGN_RBNDV2/prd/DSGN_RBNDV2_PRD.md` @e71a48e4b0 (v0.1).
**Half:** ratified-text (ENDPOINT + CONTRACTS). half_hash `b1eded27a1d5d7aa278a4f2a03491e1e7cf6cc628e2dc2c741ba41eec52cfbec`.
**Signer note:** the PRD's header and `project.json` `leads.cvo` name `3.0.0_SA_CVO~L`. That lane's last heartbeat was
2026-10-15T03:43:54Z (stale). `prd-signoff.py status` routes the owed half to `3.0.0_SA_CVO` (live), and Andrew launched
this base seat on the laptop. The base signs. The lane name in the PRD is a header fact the CTO may correct; it is not a
contract defect.

## Verdict: SIGN

## What was checked, and how

| # | check | instrument | result |
|---|---|---|---|
| 1 | ENDPOINT carried verbatim from the endpoint record | `diff` of the FWD-1..FWD-6 block, `git show 381bba5f54:org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_DSGN_RBNDV2_20261014.md` vs the PRD at HEAD | byte-identical, 37 lines |
| 2 | Andrew's ~00:1xZ and ~00:0xZ quotes | bytes of `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261014_201xZ_DSGN_RBNDV2_SURGICAL_SIDEBAR_AND_PANEL_RESKIN.md` :53-54, :70-73 | match (the record has a double space after "say so."; immaterial) |
| 3 | ~03:5xZ confirmation quote | carried in the PRD and `project.json` (CTO commits e71a48e4b0, a56aa966ed) with channel and time | recorded by the CTO's commits; no separate record file. Acceptable under XXX.md "a commit quoting him verbatim with channel + time" |
| 4 | C-SIDEBAR: sidebar inline at `App.tsx`:93-435 | `git -C portal show origin/DEV:src/App.tsx` (ad7c100b) | `NAV_SECTIONS` opens at :93; `</aside>` at :435. Holds |
| 5 | C-SIDEBAR: avatar retired, underline active state | brief @7c44838003 :251-254 | sourced from the brief's Opal-borrow list (board reading, DEC-1), not invented |
| 6 | C-PANEL: primitives in `portal/src/ui/components/panels/` | `git ls-tree origin/DEV` | Panel, PanelHeader, PanelContent, NestedCard, SectionCard, DarkCard all present |
| 7 | C-PANEL importer counts (Panel 96, PanelHeader 85) | `git grep` of import lines at origin/DEV | 94 / 83 with a narrower regex; same order, immaterial |
| 8 | C-MODAL: 10 `catalyst/dialog` importers | `git grep -l catalyst/dialog origin/DEV -- src` | 10. Holds |
| 9 | C-LIVE: `bun run dev:live` | `portal/package.json` :14 at origin/DEV | `"dev:live": "node scripts/dev-live.mjs"` exists |
| 10 | DEC-3: radius/shadow law | `portal/DESIGN.md` C11 at origin/DEV :404 | present |
| 11 | NO FWD IS A WAIT (FWD-1, FWD-5 graded by Andrew's eye) | DEC-5 + Andrew ~00:1xZ ("we just look page by page ... and point out") | expressly qualified with his word. Holds |
| 12 | FWD-6 provable on demand | `git -C portal ls-remote origin feature/dsgn-rbndv2-light` empty, plus no DEV/PROD push carrying it | an act a seat can take at any time. Holds |

## Advisory (not conditions of the signature; for the L5 decomposition)

- **A1 (C-HEAT / FWD-4 denominator).** F10's heat-map list is a name search, and the PRD says so. FWD-4's ACCEPT says "no
  heat map is left in the old blue scale", which needs a denominator: a census of the old blue-scale values/tokens across
  `portal/src`, printed at the cut and re-run at close. Without it, a zero means only that the named list was covered.
- **A2 (colour law in the verifier).** The `/frontend-dev` skill and the `portal/src/index.css` comments (:87, :93) assert
  the `#F4F6FA` canvas. On this branch DEC-2 governs (`#EAEAF7`). A worker that runs `/frontend-dev` will read the new
  ground as a violation; the task orders should say DEC-2 supersedes it inside this build.
- **A3 (the workspace `portal` gitlink and FWD-6).** While the portal checkout sits on `feature/dsgn-rbndv2-light`, a
  workspace commit that includes the `portal` path would record an unpushed SHA on `box/laptop`, which `box-sync` carries
  to `CLOUD`. No content leaves the laptop that way, but every other box gets a pointer it cannot resolve. Keep `portal`
  out of every workspace commit for the life of the branch.

## Not read

The "A light" board artifact itself (DEC-1's source); the Teams thread; Part II-IV of the brief beyond the lines cited.
