# Andrew-direct -- 2026-09-21 ~20:2xZ, at the `1.0.0_SA_CTO` terminal (mid-turn, during the IRPT self-drive tick)

**Channel:** direct conversation with `1.0.0_SA_CTO`, sent mid-turn as advance notice, not an immediate-build
instruction.

## VERBATIM AND ENTIRE

> "One thing that we are going to need for the 'Sensitivity Analysis' Tab 2 product is the ability to upload
> excel sheets with Securities ($Ticker) in column A (starting in A2), and either dollars or shares or
> potentially current weights in Column B (starting in B2). This may be a common form of how advisors scan new
> client holdings against the Opal Model Comparable for the Y Chart, so I want to make sure that is designed
> properly both in the frontend and the backend (saving these uploads in some relevant backend location, based
> on firm). The primary firm that will be doing this is 49 Financial, but we should build out the mechanism for
> each firm. The majority of this work will be backend in nature, but it does have a small frontend component
> which is why i wanted to let you know her enow."

## What it specifies

- **Product surface:** a "Sensitivity Analysis" **Tab 2** -- named as an existing or planned product area this
  seat has not yet located a project/directive for (checked `SEQUENCE.yaml` + `docs/architecture/*.md` for
  "sensitivity" as a feature name; no match -- this is new scope, not a rename of tracked work).
- **The upload mechanism:** an Excel file with a fixed, simple shape -- **Column A = Security ($Ticker), starting
  row A2** (row 1 presumed header); **Column B = one of {dollars, shares, current weights}, starting row B2**.
  The column-B unit is not pinned to one choice -- the design must accommodate more than one interpretation of
  that column (dollars OR shares OR weights), which is itself a design question (auto-detect? explicit selector?
  header-text-driven?) not answered by this message and not to be assumed.
- **Purpose:** lets an advisor scan a **new client's holdings** against **the Opal Model Comparable for the
  YCharts** surface -- so the upload feeds a comparison, not a standalone artifact.
- **Storage:** uploads are saved server-side, in "some relevant backend location, **based on firm**" -- a
  per-firm partition is explicit; the exact bucket/prefix scheme is not specified and is this seat's (or the
  eventual brief owner's) design call, governed by the estate's existing firm-separation law (CLAUDE.md Hard
  Stops: never reference another firm's data from a pipeline tree).
- **Primary user, not exclusive:** **49 Financial** is the firm expected to use this first/most, but the
  mechanism is to be **built for every firm**, not 49F-only.
- **Weight of work:** "the majority... will be backend in nature," with "a small frontend component" -- Andrew's
  own estimate, stated to explain why he is notifying this seat (a CTO-facing, largely-backend build) rather than
  a portal-only seat.
- **Timing, read from the message's own words:** "we are going to need" and "wanted to let you know here now" --
  advance notice of a coming requirement, not "build this now." No urgency language, no stated deadline.

## What this seat does with it

- **Recorded here, precisely, before anything else** -- the column layout, the per-firm build scope, and the
  frontend/backend split are exactly the kind of detail that is costly to reconstruct from memory later.
- **Does NOT start building.** Today's device priority is IRPT (`IRPT_FNTEND` / `IRPT_BCKEND`, Andrew ~12:37Z,
  "everything else can wait"), with the Cottonwood MDPF fix as the one explicit, named exception -- now closed.
  This request's own language ("going to need," advance notice) does not read as a second such exception, and
  nothing here overrides the standing priority.
- **Queued, not silently deferred** -- flagged back to Andrew this same turn, following the pattern already used
  today for CRO's registry-compiler ask (queued behind IRPT + the MDPF deploy, and confirmed correct by CRO
  without objection).
- **Not yet given a project code, PRD, or brief.** Per the canonical workflow (Rule 27), a genuinely new product
  surface starts at L1 (a brief, `4.0.0_SA_CRO`'s lane) before this seat could write an L2 endpoint -- this record
  is the input that brief would consume, not a substitute for it.

**PUSH STATE:** LOCAL on CLOUD; `origin/CLOUD` `526937843e` per `ls-remote` read this write; only
`0.0.0_AB_MSTR` pushes.
