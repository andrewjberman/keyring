# PRODUCT completion contract -- version 1.0

<!--
/closer CONTRACT template. Owner: 1.0.0_SA_CTO. At most two pages.
Home: org/tier1_exec/1.0.0_SA_CTO/deliverables/PRODUCT_COMPLETION_YYYYMMDD/CONTRACT.md,
beside AUTHORITY.md (Andrew's words, verbatim), RULINGS.md (append-only) and the MANDATE files.
Worked example: org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md v1.2.
LAND THE SECTION 3 TABLE AS .owned-paths.yaml LANES IN THE SAME COMMIT AS THIS FILE.
Replace every CAPS placeholder. Delete this comment before committing.
-->

Authority: [Andrew's instruction](AUTHORITY.md). Owner and adjudicator: `1.0.0_SA_CTO`. Implementers: SEAT_1,
SEAT_2, SEAT_3. Independent reviewers: the matching CVO lanes. Trace briefs: PATHS. This contract and each seat's
mandate are the current instructions for these seats. It is the instrument of the spine's Closer subsection.

## 1. Outcome journeys

1. **JOURNEY_1** -- who does what, end to end, and what they see.
2. **JOURNEY_2** -- ...

Reuse the frontend, parsers, adapters, authorization, render and storage libraries that work; repair connections and
incorrect behaviour. No rewrite. Out of scope unless a journey needs it: LIST. First milestones are milestones, not
permission to narrow completion. A proposed scope change goes to the CTO naming the journey it affects.

## 2. Operating mode

- Implement directly, across frontend and backend, in your own isolated worktree. **No task orders, no rounds, no
  recuts** for in-scope fixes. Do not spawn workers or invent serials.
- **LIVE FIRST.** The first milestone is the deployed live thread through the shared first hop (FIRST_HOP, for example
  auth / scope / bootstrap), owned by FIRST_HOP_OWNER. Offline closures are allowed and grade nothing until it is live.
- **NO SIDE-QUESTS.** An off-thread naming, registry or storage-policy question is parked in STATUS with an owner and
  the condition that un-parks it.

## 3. One writer for every shared surface

The owner integrates every edit to the surface and answers interface requests. Consumers prepare pinned patches in
isolated worktrees and send them to the owner; they do not land their own edits there. **A more specific row wins over
a broad directory row.** If a file crosses rows, claim the exact function with its owner before editing; the CTO
breaks a genuine tie. **This table is the path grant**: each row is an `.owned-paths.yaml` lane granting only its
owner, landed in the same commit as this file. CVOs write only their own evidence folders.

| Surface (paths or responsibility) | Sole owner | Consumers / constraints |
|---|---|---|
| SHARED FIRST HOP: `path/**` | SEAT | everyone crosses it first |
| SURFACE: `path/**` | SEAT | CONSTRAINT |
| Shared client / adapter / route aggregators: `path` | SEAT | others send patches with examples |
| Shared IaC / route manifest / packaging: `path` | SEAT | others supply requirements |
| This contract, exceptions, ties, final release decision | CTO | a CVO FAIL is fixed or retained, never overruled into PASS |

## 4. Shared semantic contracts (these are the acceptance IDs)

Owners publish the current schema version and one paired producer/consumer example in their lane's `INTERFACES.md`
before consumers integrate; superseded text moves to `INTERFACES_HISTORY.md`. No shadow schema.

- **S1 -- NAME (OWNER).** The obligation in one or two sentences a CVO can grade.
- **S2 -- NAME (OWNER).** ...
- **Sn -- HTTP/UI parity (OWNER).** Real browser request serialization through the actual entry and wire adapter; no
  fixture-only success accepted as a live journey.

Each mandate adds its own product IDs (P1..Pn).

## 5. Branches, breaking changes, integration

Code on isolated branches/worktrees; pathspec commits through `.tools/safe-commit.sh`; record workspace and portal
pins separately; shared-branch pushes stay with MSTR. **A breaking interface change** names the producer and consumer
paths, the proposed schema and example, the migration of every in-scope reader and writer, and tests. **One exchange
between the peers; if they cannot settle it, the CTO rules** on the competing options. Continue unaffected work.
Same-contract fixes need no change board.

## 6. Coordination: files over mail

- Each seat owns `deliverables/PRODUCT_LANE/` under its base role for `STATUS.md` (fixed shape, overwritten in place),
  `INTERFACES.md` (current only), evidence and `COMPLETION.md`. No co-edited status file.
- **Messages carry only: interface published, blocker, review handoff** -- each with path@commit, owner, requested
  action and affected acceptance IDs. **No ACK messages.** Subject prefix `PRODUCT LANE:`.
- CTO rulings append to `RULINGS.md` here and go out as one message per batch.
- Sends: Claude seats MCP `send_message`; Codex seats `org/mcp/codex-send.ps1 -To SERIAL -Subject ... -BodyFile FILE`.

## 7. Review and completion

Implementation is complete when there is runnable code, tests, packaging, schema/route/IaC updates, exact source and
deployed pins, and one evidence manifest per journey. The matching CVO grades each **pinned candidate**: every ID is
**PASS, FAIL or NOT_EVALUATED**, with evidence, environment pin and limits. **Offline success cannot be called deployed
E2E PASS.** Missing live authorization is named, not converted to failure or completion. The owner fixes a failure and
returns a new pin. The CTO integrates the reviews into one release decision; no lane closes the product alone.
**Hand-back:** when the thread and every journey pass, remaining work returns to canonical enrichment rounds or closes.

## 8. Gates that stay in force

Vendor egress on Andrew's per-use word; production promotion and deploy holds; provisioning and never-widen
sign-offs; NAMED PRODUCT-SPECIFIC GATES. Prepare the exact reserved action and route it to the CTO; do not stop
unrelated work on a later gate.
