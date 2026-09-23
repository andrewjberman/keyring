---
name: closer
description: "Close a product in flight whose components exist but no user journey works end to end, on Andrew's word. Four artifacts: a TRACE brief per product surface (hop walk browser to data to screen), a one-page CONTRACT with one writer per shared surface, a one-page MANDATE per implementing seat, then direct implementation with a CVO grading each pinned candidate. First milestone is the live thread (real backend, real data, real login). A read-only trace needs no Andrew word; building does. Instrument of the spine's Closer subsection, not a second process. Claude and Codex seats. Forms: /closer trace SURFACE, /closer propose PRODUCT, /closer contract PRODUCT, /closer mandate SEAT, /closer run SEAT, /closer review SEAT, /closer status."
---

# /closer -- close a product in flight

**What this is.** The instrument of the spine's **"Closer -- a product in flight, on Andrew's word"** subsection in
`org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md`. The spine is the one process document; this skill carries the
templates and the working rules. Where the two differ, the spine wins and this file is the defect.

**Andrew-direct 2026-09-23, VERBATIM** (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260923_CANONICAL_FLOW_OPS_AND_CLOSER_FLOW.md`):
*"They checked the data flows from the back end all the way to the front end, specifically looking for adapters.
Where are there missing adapters? Where are there adapters that are incomplete? ... it was very light, and it was not
very formalized, but it was highly effective. And so this is something that I want to explore formalizing slightly
more."* Brief: `org/tier1_exec/4.0.0_SA_CRO/deliverables/BRIEF_CANONICAL_FLOW_SPEED_CLOSER_FLOW_SKILLS_PARITY_20260923.md` R4.

## When

- **Applies:** a product whose components exist (parsers, adapters, routes, screens) but **no user journey works end
  to end**.
- **Who decides (Andrew-direct 2026-09-23 ~16:3xZ, calls 2 and 4, record
  `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260923_163xZ_HOLD_OFF_AND_CLOSER_OPEN_CALLS_RULINGS.md`):**
  - **A read-only TRACE needs no Andrew word.** The CRO or any Tier-1 seat may trace a product in flight at any time.
  - **The CTO may PROPOSE a closer** when a project shows **2 or more rounds and 0 live journeys** (`/closer propose`).
  - **Andrew's word gates only the BUILD phase:** the contract, the mandates, and the implementing and reviewing seats.
  - A closer is scheduled in SEQUENCE like any project, and **Codex `2.0.0_SA_COO*` seats count toward the laptop's
    three-COO limit** (call 3).
- **Does not apply:** greenfield work (canonical round 1 already starts with the live thread, spine L2/L5); a
  single-surface fix (just fix it); a governance project. **A purely backend or infrastructure product is OPEN**
  (call 5): what "live" means for it is still being defined, so do not start a closer on one until the spine says.
- **Hands back:** once the live thread and every named journey pass CVO review on a pinned candidate, remaining work
  returns to canonical enrichment rounds, or the product closes. **At hand-back the product becomes ONE project** --
  the thread is its first outcome and the other journeys are enrichment -- and any frontend/backend split projects
  close as superseded (call 6; IRPT_FNTEND and IRPT_BCKEND are the first). The closer effort does not become a
  standing process.

## Project state while a closer runs

- The CTO records the contract path on each affected project row as `"closer_contract": "<path to CONTRACT.md>"`,
  in the same commit as the contract.
- `/canonical-drive` **skips** a project whose row carries `closer_contract`: no recut, no issuance, no nudge. Rounds
  already cut stay as they are; the closer does not re-open them.
- At hand-back the CTO removes the field in the commit that registers or re-points the single product project.

## Invocation

| Form | Who | Produces |
|---|---|---|
| `/closer trace SURFACE` | `4.0.0_SA_CRO`, or any Tier-1 seat; no Andrew word needed | one TRACE brief per product surface (a tab, a report, a feed) |
| `/closer propose PRODUCT` | `1.0.0_SA_CTO` | a one-screen proposal to Andrew: rounds run, live journeys (0), the traces, the seats it would need |
| `/closer contract PRODUCT` | `1.0.0_SA_CTO`, after Andrew's word | CONTRACT.md plus the path grant and the rows' `closer_contract`, in one commit |
| `/closer mandate SEAT` | `1.0.0_SA_CTO` | one MANDATE per implementing seat and one per matching CVO |
| `/closer run SEAT` | each implementing seat (`2.0.0_SA_COO~x`) | Step 4 below: read contract + mandate, reach the live thread first, implement directly, publish pins |
| `/closer review SEAT` | each matching CVO (`3.0.0_SA_CVO~x`) | Step 4 below: grade each pinned candidate PASS / FAIL / NOT_EVALUATED in its own evidence folder |
| `/closer status` | each implementing seat | its STATUS.md, overwritten in place |

## The four artifacts and their owners

| # | Artifact | Owner | Template | Home |
|---|---|---|---|---|
| 1 | TRACE brief, one per product surface | CRO or any Tier-1 seat | `templates/TRACE_BRIEF.md` | author's `deliverables/` |
| 2 | CONTRACT, at most two pages | CTO | `templates/CONTRACT.md` | CTO `deliverables/PRODUCT_COMPLETION_YYYYMMDD/` |
| 3 | MANDATE, one page per implementing seat (and per CVO) | CTO | `templates/MANDATE.md` | same folder as the CONTRACT |
| 4 | EXECUTE + REVIEW | implementing seats implement; a CVO grades each pinned candidate; the CTO integrates | `templates/STATUS.md` | each seat's base-role `deliverables/PRODUCT_LANE/` |

Execute and review is how the IRPT run already worked: an implementing seat hands a pin; a consumer consume-merges
it into its own isolated worktree; the matching CVO grades the pinned candidate; the CTO integrates the reviews into
one release decision. No task orders, no rounds, no recuts for in-scope fixes.

**Worked example (IRPT, 2026-09-22):** trace briefs
`org/tier1_exec/4.0.0_SA_CRO/deliverables/{PERFORMANCE,SENSITIVITY,MODEL_OVERLAY}_END_TO_END_GAP_BRIEF_20260922.md`;
contract and mandates `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/` (`CONTRACT.md`
v1.2, `COO_P.md`, `CVO_P.md` and siblings); the good STATUS shape
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/STATUS.md` (about 5 KB). Copy the shapes, not the IRPT content.

## Step 1 -- TRACE (one brief per product surface)

Walk the journey hop by hop from the user's click to the data and back to the screen, looking for adapters that are
missing, incomplete or mismatched. Use `templates/TRACE_BRIEF.md`. The rules that make it usable:

- **Measure from DEPLOYED bytes.** Download the deployed artifact, compare its digest to source, and say so. A
  configured endpoint, token path or secret name is not an executed connector.
- **Every hop is headed `### N. A -> B -- STATE`**, STATE one of `WORKS`, `INCOMPLETE`, `MISSING`, `MISMATCHED`.
  Each hop names what exists (paths), the exact mismatch, and ends in one `Close:` line.
- **Completion sequence step 1 is the live thread** (LIVE FIRST, below). For a pipeline, the thread's "person" is
  the consumer of the served output.
- **Acceptance is one reconciled trace per case**, not a fixture pass.
- **LGIC (CLAUDE.md Rule 30):** any new S3 address or resource name in a `Close:` line is `lib/opal_naming.py`
  `address()` / `name()` output. A builder refusal is a missing registry row under `infra/logic/registry/`, never a
  hand-typed workaround. Add the LGIC subsection only when the delta adds storage or names.

## Step 2 -- CONTRACT (CTO, at most two pages)

Use `templates/CONTRACT.md`. It holds: the outcome journeys; the operating mode; the one-writer-per-shared-surface
table; the shared semantic contracts, which double as acceptance IDs; the breaking-change rule; the review rule.

- **The ownership table IS the path grant.** The CTO lands each row as an `.owned-paths.yaml` lane (granting only the
  named seat) **in the SAME commit as CONTRACT.md**. IRPT needed five separate grant commits; this rule makes it one.
- **A more specific row wins over a broad directory row.** Consumers send pinned patches; the owner integrates.
- **Breaking change:** one exchange between the peers, then the CTO rules. Silence is not agreement.
- **Review:** the CVO grades a pinned candidate PASS / FAIL / NOT_EVALUATED. *"Offline success cannot be called
  deployed E2E PASS."*

## Step 3 -- MANDATE (CTO, one page per seat)

Use `templates/MANDATE.md`. Each implementing seat gets its first action -- *"implement one ... end to end"* -- its
acceptance IDs, its write surface (the rows it owns in the CONTRACT table) and the pins it consumes. Each matching CVO
gets the same IDs to grade and no write surface beyond its own evidence folder.

## Step 4 -- EXECUTE and REVIEW

Implementing seats implement directly: code, tests, packaging, route and IaC changes, across frontend and backend
for their journey. They coordinate by pinned patches and files. The CVO never fixes what it grades. The CTO rules on
ties and integrates the three-way verdict; no single lane closes the product.

**`/closer run SEAT` -- the implementing seat's loop:**
1. Read the CONTRACT, your MANDATE and the trace brief for your surface. Measure your starting pins.
2. If you own the shared first hop, make the live thread pass FIRST (LIVE FIRST below). If you do not, build against
   the owner's published interface and do not count an offline closure toward an acceptance ID until the thread is live.
3. Implement, test, and publish a pinned candidate: one message, interface published or review handoff.
4. Overwrite STATUS.md (`templates/STATUS.md`). Park anything off the thread (NO SIDE-QUESTS).
5. On a FAIL from your CVO, fix directly and return a new pin. No recut, no round.

**`/closer review SEAT` -- the matching CVO's loop:**
1. Grade the exact pinned candidate in the environment it names: PASS, FAIL or NOT_EVALUATED, with evidence and limits,
   in your own evidence folder. Offline success is never a deployed end-to-end PASS.
2. Grade on evidence you can reproduce: a live trace, the deployed bytes, or a test run. **A Codex CVO grades on
   exactly those three and never on a comp-tool read** (the 2026-09-02 ruling: no comp-tool-grounded adjudication by a
   Codex seat until a Codex rail exists).
3. Send the verdict to the implementing seat and the CTO in one review-handoff message. Never fix what you grade.

## The three rules (each fixes a measured cost of the IRPT run)

### LIVE FIRST

**The first milestone is the live thread** through the **shared first hop** -- auth, scope, bootstrap --
owned by ONE seat and proven live (browser -> API -> backend -> provider/data -> rendered screen, one trace artifact)
before any per-product offline closure counts toward an acceptance ID. Offline closures are allowed; they grade
nothing until the thread is live. A thread with any fixture-fed hop is not done.

**What "live" means (Andrew, call 5):** for a product with a frontend, the **real backend, real data and real login**;
the frontend may run locally or on DEV. A PROD release is an enrichment item, not part of the thread. For a purely
backend or infrastructure product the definition is OPEN.

*Measured cost:* about 8.5 h from the contract to first live contact, and **both** live contacts then failed on the
shared scope/bootstrap hop every tab crosses first (brief section 1.2) -- so no downstream offline closure was worth
anything live.

### FILES OVER MAIL

- **STATUS.md is a fixed-shape current-state file, OVERWRITTEN IN PLACE** (`templates/STATUS.md`): pins, write
  claims, next proof, dependencies with owner, limits. It is not a journal; git history is the journal.
- **INTERFACES.md holds only the CURRENT versioned schema and one example.** Superseded text moves to
  `INTERFACES_HISTORY.md` beside it.
- **A message carries one of three things: interface published, blocker, review handoff.** Each cites path@commit,
  owner, requested action and affected acceptance IDs. **No ACK messages between peers inside the closer.** Receipt
  is the transport's job. This does not cover an acknowledgement Andrew or `0.0.0_AB_MSTR` asks for -- send that one.
- **CTO rulings append to one `RULINGS.md`** in the contract folder and go out as **one message per batch**, not one
  per ruling.

*Measured cost:* 1,544 messages in about 20 hours across ten inboxes, 135 of them ACK-prefixed; STATUS and INTERFACES
files grew into 30-47 KB timestamped journals where M's 5 KB current-state shape was enough.

### NO SIDE-QUESTS

A naming, registry or storage-policy question **not on the thread** is PARKED: one line in STATUS (or the CTO's
RULINGS.md) naming the question, its owner and the condition that un-parks it. It is not run as a review chain inside
the sprint. A question ON the thread is a blocker message to the CTO, ruled once.

*Measured cost:* two governance chains ran inside the IRPT sprint -- a legacy-read review with 7 or more documents,
and a storage-placement question across five seats whose destination was still not writable.

## Runtime -- Claude and Codex seats

This skill is for both runtimes. Artifacts and rules are identical; only the send and the wake differ.

| | Claude seat | Codex seat |
|---|---|---|
| send | MCP `send_message` (opal-agent-comms) | `org/mcp/codex-send.ps1 -To 'SERIAL' -Subject 'PRODUCT LANE: seam' -BodyFile FILE` |
| wake | `/watcher` inbox Monitor | the launcher's inbox turn bridge (`org/mcp/CODEX_INBOX_MONITOR.md`) |
| implementing | directly, in the seat's own worktree | directly, **no subagents** |

Codex seats: the 2026-09-02 ruling that Codex seats issue no comp-tool-grounded adjudication until a Codex rail exists
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260902_230xZ_OPEN_CALLS_x2_TREE_LANES_ANY_CODEX_RAIL.md`)
still bounds a Codex CVO: it grades on a live trace, the deployed bytes or a test run, never on a comp-tool read.

## What stays in force

Commits via `.tools/safe-commit.sh` with pathspecs; code in isolated worktrees (CLAUDE.md 14b); vendor egress on
Andrew's per-use word; production promotion, deploy and provisioning gates; shared-branch pushes by MSTR; the
never-widen sign-off on served output. The contract names these; it does not lift them. No new gate is added here.

## What this skill does not do

- It does not register a project, cut task orders or run rounds. That is the canonical loop.
- It does not replace the spine. It is the spine's Closer instrument.
- It does not grade. The CVO grades pinned candidates; the CTO integrates.
