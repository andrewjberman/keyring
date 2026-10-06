# L1 BRIEF -- a control plane for four devices (laptop, sitez, dell1, dell2)

- **Author:** `4.0.0_SA_CRO` (L1), 2026-10-06 ~03:0xZ (11:0x PM Eastern, 2026-10-05). **Mode:** NEW.
- **Order and rulings:** Andrew-direct at the `4.0.0_SA_CRO` terminal, 2026-10-06:
  - the proposal asked for: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_010xZ_FOUR_DEVICE_CONTROL_PLANE_PROPOSAL.md`
    ("What we need is to develop a control plane. I Think the laptop is the control plane, the sitez is the heavy box
    for heavy jobs and deploys, and the dell1 and dell2 boxes im not quite sure.");
  - the layout: "yes I like this layout" (`ANDREW_DIRECT_20261006_011xZ_FOUR_DEVICE_LAYOUT_LIKED.md`);
  - the six decisions: "all recs approved" (`ANDREW_DIRECT_20261006_011xZ_FOUR_DEVICE_SIX_RECS_APPROVED.md`).
- **The design this brief is cut from:** `docs/briefs/four-device-control-plane-proposal-20261006.md` @86bdc8c3cb
  ("the proposal"; sections cited). Context: `1.0.0_SA_CTO`'s handoff
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/HANDOFF_TO_CRO_FOUR_DEVICE_STRATEGY_DELL1_DELL2_20261006.md`.
- **Consumer:** `1.0.0_SA_CTO`, `/endpoint --forward` at L2. Proposed home: D0 Agent Infrastructure.

---

## PART I -- THE OUTCOME TERRITORY

### The candidate thread

**One round of one project travels the whole control plane.** Its PRD is written on the laptop; its round is issued,
worked and drained on dell1; dell1 publishes the round; site Z merges it into the trunk and pushes; the laptop sees it
in the trunk and the verification seat grades it. Andrew can read, afterwards, how long each hop took. Everything
else in this brief enriches that one journey (proposal section 7, stage 1).

### O1 -- Andrew adds a box to the fabric and every tool knows its name and role

A box is added once, in one place, with its name, its role and its seat limit. From then on the startup protocol,
the message bus, the archive and the seat-spawning tool recognise it without anyone editing a script that lists
device names. Today two names are hardcoded in the bus script and identity comes from the Windows profile path
(proposal 2, 5.5).

### O2 -- A seat on any box sends a message to any other box and gets an acknowledgement

Four boxes, one inbound queue each. The far box's fabric manager receives it and the sender can show it was read
(proposal 5.5).

### O3 -- An execution box's finished round reaches the trunk without that box pushing the trunk

The box publishes the round; site Z merges published rounds in the order the laptop sets and pushes. No box's local
trunk drifts further than one unpublished round per lane. Today the laptop alone is 154 commits ahead of the remote
trunk, with no ceiling (proposal 2, 5.1).

### O4 -- Publishing work never deploys anything; only site Z's trunk push does

Today the push gate uploads pipeline scripts to production on ANY pushed branch (MEASURED,
`.tools/git-hooks/pre-push-safe-deploy.sh:41-58`). After this, a publish from any box is inert, and the deploy event
happens once, on the deploy box (proposal 5.3).

### O5 -- Site Z pushes a routine round without Andrew at its terminal, and waits for him on any round that would deploy

The standing push rule Andrew approved (card 1): a round with no pipeline script goes without asking; a round with one
waits for his word (proposal 5.8, 10).

### O6 -- Anyone looking at the control plane can see which box runs each project, and nothing is placed by guess

Each project row names its box; a project is placed whole; two projects on different boxes write different files.
A box with a free lane and nothing placed on it is visible (proposal 4).

### O7 -- Two boxes never collide on a shared file

Registers have one writer (the laptop). A project's own tree has one writer (its box). Append-only files (surprise
channels, logs) are per box (proposal 5.4).

### O8 -- A scarce account is used by one box at a time, and a box that dies releases it

One lease register on the laptop covering the walker account, the YCharts session, the portal DEV push and the
Bloomberg quota. It replaces today's relayed "held" and "FREE" messages (proposal 5.6).

### O9 -- The audit trail shows which box acted, and a Dell cannot deploy even by mistake

Each box has its own cloud identity; the Dells' cannot deploy, apply infrastructure or write production storage
(card 5; proposal 5.7).

### O10 -- A box can reboot mid-round and nothing is lost

The failure cases of proposal 5.9: a Dell, site Z or the laptop going down, and a box whose message consumer is not
running.

---

## PART II -- WHERE THE BOUNDARY SITS

**This project owns:** the device registry; the cross-box message routing; the publish-and-integrate flow and its
queue; the push gate's trunk-only rule; the per-box append-file convention; the lease register; per-box identities;
the edits to `/integrate`, `/agentbus`, `/watcher`, `/mstr-spawn` and the startup protocol that name devices.

**It relies on, and does not own:**
- **The canonical workflow** (CLAUDE.md rule 27, `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md`). Its tracks
  already share files, not messages; that is why this works. The workflow itself is not changed.
- **The law files** `org/XXX.md` and `CLAUDE.md`, edited only on Andrew's express order (O5 needs one).
- **The new-device kit** (`Opal_New_Device_Kit_20261005.zip`, per the CTO's handoff): standing a single box up.
- **Each directive's projects.** Moving a directive to a box is Andrew's call per move (card 6), not this project's.
- **The portal repository's own `DEV` trunk**, which keeps its existing rules.
- **Tradeops**, the second fabric on its own broker port: out of scope.

---

## PART III -- THE QUALITATIVE BAR

1. Andrew adds a third execution lane on a Dell and nothing on the other three boxes has to be touched by hand.
2. No one, on any box, ever has to resolve the same merge conflict twice, or wait for another box to finish pushing.
3. Andrew is asked about a push only when it would deploy something.
4. When a box is switched off unexpectedly, the next person to look can say exactly which round was where.
5. Nobody has to relay "the account is free now" by hand.

---

## PART IV -- THE SUBSTRATE: what exists, measured

- **F1.** One trunk, `CLOUD`, both devices commit to it; the two-branch model was retired 2026-09-24
  (`.claude/skills/integrate/SKILL.md:7-18`).
- **F2.** The push is a deploy event: the gate uploads every pipeline script in the pushed range, for every pushed
  ref (`integrate/SKILL.md:68-72`; `pre-push-safe-deploy.sh:41-58`).
- **F3.** The bus is one queue pair named sender-to-receiver, two devices, identity from the Windows profile path
  (`.tools/agentbus-sqs.sh:84-86`, `:157-158`). It already enforces one consumer per device.
- **F4.** Only the fabric managers may push or pull a shared branch, enforced by `.tools/hooks/never-rules-gate.sh`
  gate 5, and by law only on Andrew's word at that terminal (`org/XXX.md` Step 1b).
- **F5.** Directive placement lives in a comment-governed field of `org/missions/DIRECTIVES.yaml`; the device fact a
  drive reads is the project row's `fabric` field (`DIRECTIVES.yaml:396-409`).
- **F6.** A per-device append file already exists once (`org/surprise_channel/ETFS_INGEST/INVESTIGATION_v1.Z.md`).
- **F7.** Worker write surfaces are already enforced per order (`.tools/owned-paths-validate.py`); placement by write
  surface is the same idea one level up.
- **F8.** Laptop capacity (the CTO's reading): 31.7 GB memory, 8 cores, 37.6 GB disk free; a worker checkout costs
  about 2.35 GB.

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- The push gate deploys on the trunk only, before any box publishes a round branch (O4 before O3).
- Andrew's express order for the law edit behind O5; until it lands, the current push rule stands.
- dell1 exists, is reachable, and has its own identity before the thread can run.
- Each new name (queues, identities, branches' prefix) is builder output from `lib/opal_naming.py` (CLAUDE.md rule 30).
- Site Z's planning seats retire only as their projects close, never mid-project (card 3).
- Andrew's standing seat limits per box are respected; the Dells start at two lanes each.
- No standing parity comparator and no shadow pipeline is built to prove any of this (CLAUDE.md, section 5).

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-10-06 ~01:0xZ on the laptop: 154 commits ahead of the remote trunk, from 12 authors; remote trunk
`01a47ac2e7`. The Dells are not yet delivered; their hardware, network location and arrival date are unknown.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- No Dell was measured; "two or three lanes each" is Andrew's estimate.
- A single round's integration time was not measured; the queue's throughput depends on it.
- How often two projects write the same file was not censused.
- Site Z's capacity to integrate while running Bloomberg jobs and its own lanes was not read.
- Only the push gate's ref loop and gate 5's header were read; the other hooks' behaviour on a queue branch is
  unchecked.
- The cost of two more identities, queues and model usage is not estimated.

---

## REFS

```
  BRIEF PATH        docs/briefs/four-device-control-plane-brief-20261006.md
  PROJECT           NONE-YET (CTO registers at L3; proposed home D0)
  EXISTING PRD      NONE
  DESIGN            docs/briefs/four-device-control-plane-proposal-20261006.md @86bdc8c3cb
  ANDREW'S WORDS    org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_010xZ_FOUR_DEVICE_CONTROL_PLANE_PROPOSAL.md
                    org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_011xZ_FOUR_DEVICE_LAYOUT_LIKED.md
                    org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_011xZ_FOUR_DEVICE_SIX_RECS_APPROVED.md
  SIBLING PROJECTS  the canonical workflow; the new-device kit; the law files; each directive's projects; portal DEV
  PRIOR ART         /integrate one-trunk model; the agent bus and its one-consumer lock; never-rules gate 5;
                    owned-paths validation; the per-device ETFS_INGEST surprise file
  OPEN FOR ANDREW   the wording of the law edit behind O5 (card 1 approved the rule, not the text)
  MEASURED AT       2026-10-06 ~01:0xZ, laptop only
```
