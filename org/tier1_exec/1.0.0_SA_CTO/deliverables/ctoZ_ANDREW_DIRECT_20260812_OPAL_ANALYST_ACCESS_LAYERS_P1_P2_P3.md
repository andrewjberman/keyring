# Andrew-direct — OPAL_ANALYST gains three ACCESS LAYERS (portal index · SharePoint · Bloomberg), a read-only gate on 0.0.3, and a new CRO~Z seat

**Channel:** direct at the `1.0.0_SA_CTO~Z` terminal, 2026-08-12 ~17:02Z (13:02 ET).
**Recorded by:** `1.0.0_SA_CTO~Z`. **PRD owner for this program: me.**

## VERBATIM (the phrasing IS the ruling)

> "Yes I also want you to create an additional layer (or layers) to the Opal_ANALYST project which are
> the following. Portal data locations need to be covered and validated first and foremost, then index
> needs to be created on yaml for portal requests covering where to find various info for easy access
> via aws reads (readonly by the way, 0.0.3 should not have any commit/deploy ability, gated to prevent
> it from doing so and prompted against it). That is part 1. Part 2 is then making sure it is properly
> hooked up to read sharepoint documents and a registry section to know what is in there. Part 3 is
> doing the same thing for Bloomberg, which means a 4.0.0_SA_CRO~Z agent will be needed to explore the
> BBG blpapi pipes and know what is served where and how. Traversing these pipes is fine, reading is
> fine, downloads are expressly forbidden. If information needs to be pulled down after pipeline
> architecture is identified, for verification/validity purposes, then those pulls need to be sized and
> requested because we are on a quota and large pulls will be flagged."

## What this rules — the three parts

**PART 1 — PORTAL DATA LOCATIONS, THEN THE YAML REQUEST INDEX.**
Two halves with his sequencing word attached to the first: *"covered and validated **first and
foremost**"*, and only **then** the yaml index — *"covering where to find various info for easy access
via aws reads."* Access mode is **READ-ONLY**.

**PART 2 — SHAREPOINT.** Properly hooked up to **read** SharePoint documents, plus **a registry
section to know what is in there.** Same shape as Part 1: reach + an inventory of what the reach covers.

**PART 3 — BLOOMBERG, and it comes with a new seat and a hard constraint.**
`4.0.0_SA_CRO~Z` explores the **BBG blpapi pipes** and establishes **what is served where and how**.
- **Traversing the pipes: PERMITTED.** **Reading: PERMITTED.**
- **Downloads: EXPRESSLY FORBIDDEN.**
- **Post-architecture verification pulls must be SIZED AND REQUESTED** — *"because we are on a quota
  and large pulls will be flagged."*

**THE GATE HE ASKED FOR (explicitly, so it is legal to build).**
`0.0.3_BG_BBGTerminal` *"should not have any commit/deploy ability, **gated** to prevent it from doing
so **and prompted against it**."* Two mechanisms, both named by him: a **mechanical gate** and a
**prompt-level instruction**. This is a sovereign gate request under the 2026-08-06 rule — the rule
bans *manufacturing* gates, not building the ones he asks for.

## Structural rulings I am making as PRD owner (surfaced, not buried)

**1. PART 1's SECOND HALF IS `W5`, NOT A NEW WAVE.** `W5` already is *"DATA_CATALOG v0.2 rigged
properly + tool tags/fuzzy match"* — that IS the yaml request index. Minting a parallel wave beside it
would violate the Build Ladder rung 2 (*the estate already has it*) and produce exactly the duplicate
the ladder exists to prevent. **Part 1 therefore AMENDS W5**: it adds the read-only access mode, the
explicit precondition, and the gate. It does not create W7.

**2. PART 2 AND PART 3 ARE NEW WAVES: `W7` (SharePoint) and `W8` (Bloomberg).** Both share Part 1's
two-half shape — *establish the reach, then register what the reach covers* — so they are genuine
siblings of W5, not sub-items of it.

**3. `W6` GUARDRAILS RESEQUENCES TO LAST.** W6 must review the guardrails on **every** access surface,
and W7/W8 add two new ones (SharePoint documents, Bloomberg pipes) carrying a quota constraint and a
download prohibition. A guardrails review that ran before those surfaces existed would certify a
narrower system than the one we ship. **New order: W5 -> W7 -> W8 -> W6.**

**4. A MEASURED GRAIN GAP SITS BETWEEN PART 1's TWO HALVES, AND IT IS ALREADY EVIDENCED.**
His index is keyed by **artifact** (*"where to find various info"*). The decomposition rectangles are
keyed by **page entity**, and `3.0.0_SA_CVO~Z`'s own W5 prep measured the consequence: **family
entities collapse N keys into one row — `sscn.02` = 6 keys, `news.01` = 360** — so *"a catalog keyed by
artifact will not find 366 of them."* Rule 24(ii), same-grain, fails across the seam.
**Therefore "portal data locations covered and validated" is NOT automatically discharged by the
W0–W4c page decompositions.** It needs a per-key expansion pass. That pass is Part 1's first half and
it is real work, not bookkeeping — which is, I think, exactly why he put *"first and foremost"* on it.

## The one narrow question I am putting to Andrew (not blocking on it)

**Does the 0.0.3 commit ban include its own SESSION LOGS?** `0.0.3_BG_BBGTerminal` commits today
(three commits, 2026-08-12) and they are its **session log + its signin-recovery runbook** — the
artifacts the universal session-log law requires from every agent. So two of his own rules meet here.
- **Implementing now, unambiguous either way:** **deploy = unconditional hard deny** (terraform, lambda
  update, `safe-deploy`, `safe-ec2-deploy`, S3 code writes), and **commit = deny for all product
  surfaces** (code, infra, data scripts, portal, served artifacts).
- **Held for his word, defaulting to PERMIT so the logging law is not silently broken:** commits
  confined to its own agent folder (`org/tier0_utility/0.0.3_BG_BBGTerminal/**` logs + runbooks).
- I am **not** silently choosing the strict reading, because the strict reading disables a law he also
  set, and I am not silently choosing the loose one either. Stated, defaulted, flagged.

## Vendor-egress interaction, recorded precisely

CLAUDE.md bans calling an external vendor API without his explicit per-use word. **This directive IS
that word for Part 3, and its scope is exactly:** traverse + read the blpapi pipes to map what is
served where and how. **It is NOT** authorization to download, and **it is NOT** open-ended pull
authority — a verification pull is a **separate, sized request** back to him. The live
`bloomberg_historical_data` / `bloomberg_intraday_bars` MCP tools ARE data pulls and fall on the
**requires-sizing** side of that line; `bloomberg_health` and pipe/reference traversal do not.

## Consequences dispatched this turn

- Spawn-request **addendum** to `0.0.0_AB_MSTR~Z` adding `4.0.0_SA_CRO~Z` (a 5th seat).
- PRD §10 authored for the three parts + the resequence.
- The `0.0.3` gate specified; implementation is a build, and the prompt-level half lands in that seat's
  `prompt.md`.
