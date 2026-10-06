# NFRA_CTLPLN -- the four-device control plane: the laptop plans, site Z integrates and deploys, dell1 and dell2 execute

```json
{
 "project": "NFRA_CTLPLN",
 "directive": "D0",
 "fabric": "laptop",
 "prd_version": "v0.2",
 "step": 4,
 "brief_ref": "docs/briefs/four-device-control-plane-brief-20261006.md@a77b65337e",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8", "FWD-9", "FWD-10", "FWD-11", "FWD-12", "FWD-13"],
 "status": "RATIFIED"
}
```

**Author:** `1.0.0_SA_CTO` (L2-L4), 2026-10-06.
**Brief:** `docs/briefs/four-device-control-plane-brief-20261006.md` @a77b65337e (`4.0.0_SA_CRO`). Design behind it:
`docs/briefs/four-device-control-plane-proposal-20261006.md` @86bdc8c3cb (sections cited as "proposal N").
**Andrew's words** (all at the `4.0.0_SA_CRO` terminal, records in `org/tier1_exec/4.0.0_SA_CRO/deliverables/`):
- the six-card proposal, "all recs approved" (`ANDREW_DIRECT_20261006_011xZ_FOUR_DEVICE_SIX_RECS_APPROVED.md`);
- the push-rule wording is seen before it lands, "b is better , yes" (`ANDREW_DIRECT_20261006_030xZ_PUSH_RULE_LAW_EDIT_WORDING_FIRST.md`);
- the endpoint, "im good with all of this", with FWD-4's headline fixed, FWD-12 added, register under D0 and start FWD-5 first
  (`ANDREW_DIRECT_20261006_13xxZ_FOUR_DEVICE_ENDPOINT_CONFIRMED_FWD4_FIX_FWD12_ADD.md`).
**Registered** @1641471f2c (D0/NFRA, fabric laptop).
**Sign-off:** `3.0.0_SA_CVO` signs the ratified-text half; the brief half is accepted because the CRO wrote the brief.

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  One round of one real project is issued and worked on dell1, reaches the shared trunk
         through site Z, and is graded on the laptop -- and Andrew can see how long each step took
         DONE WHEN  EXERCISED -- one real round, traced from its PRD on the laptop to its grade
         ACCEPT     a real project's round is planned on the laptop, worked and finished on dell1,
                    published by dell1, merged and pushed by site Z, and graded on the laptop. Nobody
                    pushes the shared trunk from dell1. Andrew reads afterwards when each step began
                    and ended. A step done by hand on another box, or a practice round, fails it
         SOURCE     brief PART I, the candidate thread

  FWD-2  Andrew adds a box once, in one place, and every tool knows its name and its role
         DONE WHEN  EXERCISED -- a box added that way, and a seat started on it
         ACCEPT     a new box is named once with its role and how many lanes it may run; seats start on
                    it, message it and are recorded under its name, and nobody edits a script that
                    lists boxes by hand
         SOURCE     brief O1

  FWD-3  A seat on any box reaches a seat on any other box through the two boxes' fabric
         managers, and the sender can show it was read
         DONE WHEN  EXERCISED -- one message each way between every pair of boxes in use
         ACCEPT     a message from a seat on one box goes to its own box's fabric manager, which passes
                    it to the other box's fabric manager, which delivers it to the right seat; the sender
                    can show that it was read, not only delivered. No other seat talks across boxes
         SOURCE     brief O2; Andrew-direct 2026-10-06 ~14:0xZ ("only the MSTR agents are the ones that
                    communicate between boxes")

  FWD-4  A finished round from any working box reaches the shared trunk without that box pushing
         it, and no lane falls more than one round behind
         DONE WHEN  EXERCISED -- two boxes' rounds published and merged in the order the laptop set
         ACCEPT     each working box publishes its finished round; site Z merges published rounds in
                    the order the laptop set and pushes. No box holds more than one unpublished round
                    per lane
         SOURCE     brief O3; Andrew's confirmation (headline wording)

  FWD-5  Publishing work from any box never puts anything into production; only site Z's push of
         the shared trunk does
         DONE WHEN  EXERCISED -- a round carrying a pipeline script published, and nothing deployed
         ACCEPT     a published round that contains a pipeline script changes nothing in production
                    until site Z pushes the shared trunk
         SOURCE     brief O4

  FWD-6  Site Z pushes a routine round on its own, and waits for Andrew on any round that would put
         something into production
         DONE WHEN  EXERCISED -- one routine push without Andrew, one held round released by his word
         ACCEPT     a round with no pipeline script reaches the shared trunk without Andrew at a
                    terminal; a round with one waits until he says so
         SOURCE     brief O5; Andrew's card 1

  FWD-7  Anyone can see which box runs each project or workstream, and none is split across boxes
         DONE WHEN  EXERCISED -- the placement read for every live project and workstream
         ACCEPT     each project or workstream names its box; one is on one box; two on different boxes
                    change different files; a box with room and nothing placed on it is visible
         SOURCE     brief O6; Andrew-direct 2026-10-06 ~14:0xZ (the workstream as the unit, by the CRO's
                    stated reading, not corrected by him)

  FWD-8  Two boxes never edit the same file at the same time
         DONE WHEN  EXERCISED -- two boxes working in parallel through one full round each, with no
                    merge conflict on a shared file
         ACCEPT     shared lists have one writer; each project's files have one writer; logs and
                    surprise records are kept per box
         SOURCE     brief O7

  FWD-9  A scarce account is used by one box at a time, and a box that dies gives it back
         DONE WHEN  EXERCISED -- a box holding an account switched off, and another box taking it
         ACCEPT     the YCharts session, the walker account, the portal push and the Bloomberg quota are
                    each held by at most one box; nobody relays "it is free now" by hand; a box that goes
                    down releases what it held
         SOURCE     brief O8

  FWD-10 The record shows which box did each act, and a Dell cannot put anything into production,
         even by mistake
         DONE WHEN  EXERCISED -- a deploy attempted from a Dell, and refused
         ACCEPT     every act in the record names its box; a Dell's attempt to deploy, change
                    infrastructure or write production data is refused
         SOURCE     brief O9; Andrew's card 5

  FWD-11 A box can restart in the middle of a round and nothing is lost
         DONE WHEN  EXERCISED -- one box restarted mid-round, and the round finished
         ACCEPT     after any one box restarts, the next person to look can say which round was where,
                    and the round finishes without work being redone or lost
         SOURCE     brief O10; PART III item 4

  FWD-12 Andrew sees every box's open decisions in one place on the laptop, and a lane on a box
         he is not at never stops waiting for him at that box's terminal
         DONE WHEN  EXERCISED -- a decision raised on another box answered by Andrew from the laptop
         ACCEPT     a decision any box needs from Andrew appears in one list on the laptop, and his
                    answer there reaches the box that asked; no lane sits waiting on a terminal he is
                    not at
         SOURCE     proposal section 5.8; Andrew's confirmation (added at his word)

  FWD-13 When one box can no longer hold its work, a project or workstream moves to another box
         between rounds without losing anything, placed where there is the most room
         DONE WHEN  EXERCISED -- one live project moved between rounds and its next round finished on
                    the new box
         ACCEPT     the CTO decides a project or workstream should move; the box with the most free room
                    is chosen by its measured load, not by guess; the move happens between rounds, never
                    in the middle of one; the next round on the new box starts from exactly where the
                    last one ended, with nothing redone or lost
         SOURCE     Andrew-direct 2026-10-06 ~14:0xZ (the CTO elects, the box's MSTR runs the bid) and
                    "agreed on all points go ahead"
```

## PROVENANCE (outside the ratified section)

- The ENDPOINT was proposed at
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_FOUR_DEVICE_CONTROL_PLANE_20261006.md` and confirmed by Andrew with two
  changes: FWD-4's headline ("lane", not "box") and FWD-12. A word of his that amends an FWD becomes an addendum under the next
  unused id (FWD-13) or an in-place amendment, never a cell's choice.

## CONTRACTS

| Contract | Direction / owner | Binding agreement |
|---|---|---|
| C-ROLES: what each box is | Andrew's six cards; proposal 3 | **laptop:** the control plane. It alone writes the registers, receives Andrew's word, orders the merge queue and runs the planning seats (CTO, CRO, CVO); at most one execution lane. **sitez:** the integrator and the deploy box; it alone pushes the trunk and deploys; it keeps the Bloomberg jobs. **dell1, dell2:** execution only; they never push the trunk, deploy, call a vendor or write a register. Site Z's planning lanes retire as their projects close, never mid-project (card 3). |
| C-TRUNK-DEPLOY: a publish never deploys (FWD-5) | this project; `.tools/git-hooks/pre-push-safe-deploy.sh` | MEASURED at L4 (`pre-push-safe-deploy.sh:41-70`): the hook runs `safe-deploy.sh --commit-range` for EVERY pushed ref that is not a tag or a delete, so pushing any branch uploads the pipeline scripts in its range. After this contract: the deploy gate runs only when the pushed REMOTE ref is `refs/heads/CLOUD`. Every other branch push prints one line saying no deploy ran and why, and exits 0 for the deploy gate (the HALTGT checkpoint above it is unchanged). This lands BEFORE any round branch is published (brief PART V). |
| C-QUEUE: publish and integrate (FWD-4) | this project; `/integrate` split in two (proposal 5.2) | A box publishes ONE branch per finished round, `q/<device>/<PROJECT>/r<N>`, and sends one bus line to the laptop. The laptop holds the ordered queue (SEQUENCE, then arrival). Site Z takes the head, merges in its own worktree (the commit hooks grade once, there), pushes the trunk, announces the new head, and deletes the queue branch. Every box pulls the trunk at its next round start. A same-line conflict at integration is a PLACEMENT finding routed to the laptop, never resolved silently at the merge. This is not the retired two-branch model: a queue branch lives one round and flows one way. |
| C-PUSH-RULE: the standing push rule (FWD-6) | Andrew; the locked law files | The rule lives in `org/XXX.md` Step 1b and is enforced by `.tools/hooks/never-rules-gate.sh` gate 5. It changes only by an `ANDREW_LAW_EDIT_ORDER` naming a record in which Andrew approved the EXACT text. The draft is `4.0.0_SA_CRO`'s (record `ANDREW_DIRECT_20261006_030xZ_PUSH_RULE_LAW_EDIT_WORDING_FIRST.md` @c49017ef52), not yet approved. Until it lands, the current rule stands: only the fabric managers push, on his word at that terminal. |
| C-REGISTRY: the device register (FWD-2) | this project | ONE file holds each box's name, role, inbound queue, seat limit and lane letters. Every script that today names devices reads it instead (MEASURED: `.tools/agentbus-sqs.sh:84-86` and `:157-158` hardcode `laptop` and `sitez` and infer the device from the Windows profile path). A box's identity is set once at bring-up as a user environment setting, never derived from a path (LD-0405, no device-specific code). The file's home and name are builder output where the builder covers them; the register is a registry row in `infra/logic/registry/` if LGIC holds that class. |
| C-BUS: one inbound queue per box (FWD-3) | this project; `.claude/skills/agentbus/SKILL.md` | Four inbound queues, each drained by that box's fabric manager; any box sends to the recipient's queue. What crosses the bus is small: "round ready", "trunk at", a lease grant, a pointer to a record. READ is the agent-side acknowledgement, as on the local broker. **Names, builder output at L4:** `name('agentbus','global','dell1','queue')` -> `agentbus-global-dell1-queue` (likewise per box). The queues are FIFO, which AWS marks with a `.fifo` suffix the builder does not emit today: the cell resolves that with an LGIC registry change, never a hand-typed name. The two existing queues (`agentbus-ajbdev-*`) migrate inside this project, same-window, no parallel bus. |
| C-PLACEMENT: one project, one box (FWD-7) | the laptop; `org/missions/DIRECTIVES.yaml`, `org/missions/SEQUENCE.yaml` | A project's row names its box (`fabric`: `laptop`, `site-z`, `dell1`, `dell2`). A project is never split. Two projects go to different boxes only if their write surfaces do not overlap, checked as `.tools/owned-paths-validate.py` checks a worker, one level up. Andrew's first allocation (card 6) is the starting point; each move is his when it happens, and nothing moves until a Dell is standing. |
| C-ONE-WRITER: files (FWD-8) | this project | Registers (`DIRECTIVES.yaml`, `SEQUENCE.yaml`, `LIVE_ARMS.md`, project rows, missions-tree carriers, the law files): the laptop only. A project's own tree: its box only. Append-only files (surprise channels, audit logs, session logs): one file per box, `<name>.<device>.md`, the pattern `org/surprise_channel/ETFS_INGEST/INVESTIGATION_v1.Z.md` already uses. The surprise-row gate and the readers that compile a channel learn to read every per-box file of a channel. |
| C-LEASE: scarce accounts (FWD-9) | this project; the laptop holds the register | One lease register on the laptop: resource, holder box, expiry. Covered: the walker account, the YCharts session, the portal `DEV` push, the Bloomberg daily quota. A lease expires by itself; a dead box's leases lapse. The Dells take no vendor lease (vendor pulls stay scheduled on their existing homes). |
| C-IDENTITY: per-box cloud identity (FWD-10) | this project; cloud IAM (deployed by site Z) | Each box acts under its own identity so the record names the box. The Dells' identities are DENIED deploys, infrastructure applies and production writes by policy, so "a Dell never deploys" is something the cloud refuses, not a rule people follow. **Name, builder output at L4:** `name('cloudops','global','dell1-agent','role')` -> `cloudops-global-dell1-agent-role` (likewise `dell2`). The IAM traps in `/cloud-ops` apply. |
| C-RESTART: rounds survive a box restart (FWD-11) | this project | A lane on any box publishes its work-in-progress branch at each cell close, so a disk loss loses at most one cell. The round's state is read from the published branches and the ledger, never from one box's memory. Proposal 5.9 lists the cases (a Dell, site Z or the laptop down; a box whose bus consumer is not running). |
| C-ATTENTION: one decision list (FWD-12) | this project | A box records each decision it needs from Andrew as a file on its own tree plus one bus line to the laptop; the laptop shows one list of every box's open decisions; his answer is recorded on the laptop and reaches the asking box as a file and one bus line. No lane on an unattended box blocks on a prompt at that box. |
| C-SERIALS: one fabric manager per box | Andrew, "agreed on all points go ahead" | `0.0.0_AB_MSTR` (laptop), `0.0.0_AB_MSTR~SITEZ`, `0.0.0_AB_MSTR~DELL1`, `0.0.0_AB_MSTR~DELL2`, each with its own tier-0 folder. Site Z's `~Z` stays as an ALIAS in the device register so every past record still resolves; the rename lands at a site-Z restart. Only these seats talk across boxes (FWD-3). |
| C-BID: placement of a move (FWD-13) | Andrew; `.tools/remote-job.py` | One CTO, on the laptop, elects a move and tells the laptop's fabric manager. That fabric manager offers it to the boxes' fabric managers, which bid with measured load; it awards the move. MEASURED at L4 by the CRO (record @ab368f2e7c): `remote-job.py` bids CPU and memory via `psutil`, knows two devices (`DEVICES = ("laptop", "sitez")`), and its awards run through LDO-001; disk and storage are not measured. The bid adds disk and storage and reads devices from the register (C-REGISTRY). LDO-001 keeps awarding Teams remote jobs; the laptop's fabric manager awards moves. A move happens only between rounds: the old box publishes its last round (C-QUEUE), the new box pulls the trunk and seats the lane. |
| C-NAMES | CLAUDE.md rule 30 | Every new queue, identity, register home and branch prefix is builder output, printed in the order that creates it. A builder refusal is a missing registry row to add. |
| C-MORATORIUM | law | No alert, alarm, SNS, SES send, freshness checker or monitor. A box that has not acknowledged is visible on the control plane as a state, not a notification. |
| C-NO-SHADOW | law | No standing comparator between boxes and no second bus or trunk run beside the first; each change replaces the old path in the same window. |

## 1. The arc

**Start.** Two boxes, laptop and site Z, each a self-contained fabric with its own planning seats. Both commit to one trunk; only
the two fabric managers push, on Andrew's word at that terminal. A push of any branch uploads pipeline scripts. The bus knows two
devices by name, from the Windows profile path. The laptop was 154 commits ahead of the remote trunk at 01:0xZ today.

**End.** Four boxes on one control plane. Andrew speaks at the laptop; the planning seats sit there. Rounds are worked on the Dells,
published as short branches, merged and pushed by site Z in the order the laptop sets. Publishing never deploys. Every box is in one
register; messages reach any box and are acknowledged; scarce accounts are leased; the Dells cannot deploy. A box can restart
without losing a round.

## 2. Rounds, and why round 1 is not the thread

FWD-1 is the thread, and it needs dell1 standing. The Dells are not delivered. Andrew ordered FWD-5 first ("register under D0 and
start the work that needs no Dell, FWD-5 first"). So:

- **Round 1 (no Dell needed), in this order:** FWD-5 (the trunk-only deploy gate); FWD-2 (the device register, with the two existing
  boxes in it); FWD-8 (per-box append files and the readers that compile them); FWD-7 (the box field on every project row and the
  placement check). Each is exercised on the two boxes that exist.
- **Round 2 (dell1 standing):** the thread, FWD-1, end to end, with FWD-3 (dell1 on the bus) and FWD-10 (dell1's identity) as its hops.
- **Later rounds:** FWD-4 under load, FWD-6 (once Andrew approves the law text), FWD-9, FWD-11, FWD-12, then dell2 by the same steps.

## 3. ENRICHMENT BACKLOG (ordered, one line each)

1. The queue under load: two lanes publish in the same hour; drift read per lane (FWD-4).
2. Site Z's standing push rule, on Andrew's approved text (FWD-6).
3. The lease register replaces relayed "held"/"FREE" messages (FWD-9).
4. One decision list on the laptop (FWD-12).
5. A box restarted mid-round, measured (FWD-11).
6. dell2 joins; the first allocation moves directive by directive on Andrew's word (C-PLACEMENT).
7. Site Z's planning lanes retire as their projects close (C-ROLES).

## 4. Engines (one row per engine)

| Engine | Serving shape | Role here | Change |
|---|---|---|---|
| `.tools/git-hooks/pre-push-safe-deploy.sh` and `.tools/safe-deploy.sh` | the git pre-push hook | the deploy event | trunk-only (C-TRUNK-DEPLOY) |
| `.claude/skills/integrate/SKILL.md` | the parity skill | becomes publish + integrate | C-QUEUE |
| `.tools/agentbus-sqs.sh` and `.claude/skills/agentbus/SKILL.md` | the cross-device bus | four inbound queues, identity from the register | C-BUS, C-REGISTRY |
| `.tools/hooks/never-rules-gate.sh` gate 5 | push admission | admits the integrator under the standing rule | C-PUSH-RULE (after Andrew's text) |
| `.tools/surprise-row-gate.py`, the channel compilers | the surprise channel | read per-box files | C-ONE-WRITER |
| `.tools/owned-paths-validate.py`, `org/missions/DIRECTIVES.yaml`, `SEQUENCE.yaml` | placement | box per project, write-surface check | C-PLACEMENT |
| `/mstr-spawn`, `/watcher`, the startup protocol | seat lifecycle | read the register | C-REGISTRY |

## 5. WORKSTREAMS AND OWNERS

- **One workstream.** Its COO lane is UNSEATED at registration; seating is `0.0.0_AB_MSTR`'s on Andrew's word. Until a lane is seated
  nothing is issued.
- **Write surface:** the engines above; the device register; the per-box file convention and its readers; this project's tree.
- **Owned elsewhere, named:** the law files (Andrew's order); cloud IAM applies (site Z deploys them; this project writes the
  Terraform); the new-device kit (this seat's Desktop artifact, outside the repo).
- **L4-R:** `3.0.0_SA_CVO` signs the ratified-text half; the brief half is accepted (the CRO wrote the brief).

## 6. Rulings closed at L4 (no decide-first question enters L5)

1. FWD-5 lands before any round branch is published, and before any Dell exists.
2. Site Z is the only trunk writer once C-QUEUE lands; until then the current push rule stands.
3. One project, one box; placement by write surface.
4. Device identity is a setting made at bring-up, never inferred from a path.
5. Append-only files are per box; the readers union them.
6. The Dells' identities cannot deploy, by policy.
7. Every new name is builder output; the `.fifo` suffix is resolved in the registry, not typed.
8. The law edit lands only on Andrew's approval of its exact text.

## 7. SURFACE MANIFEST (step 4 -> step 5)

`claim`: `measured` = read at L4 by this seat; `held` = the brief's or the proposal's measurement; `unmeasured` = new.

| id | outcome_ref | surface | claim | evidence | verb | depends_on | bound |
|---|---|---|---|---|---|---|---|
| S01 | FWD-5 | `.tools/git-hooks/pre-push-safe-deploy.sh` deploys only on `refs/heads/CLOUD` | measured (`:41-70`, every non-tag non-delete ref) | C-TRUNK-DEPLOY | wire | -- | HALTGT checkpoint unchanged |
| S02 | FWD-2 | the device register and its readers | measured (`agentbus-sqs.sh:84-86`, `:157-158`) | C-REGISTRY | wire | -- | no path-derived identity |
| S03 | FWD-8 | per-box append files; the surprise-row gate and channel compilers read all of a channel's files | held (proposal 5.4) | C-ONE-WRITER | wire | S02 | one writer per file |
| S04 | FWD-7 | the box field on project rows; the placement write-surface check | held (proposal 4) | C-PLACEMENT | wire | S02 | nothing moves without a standing Dell |
| S05 | FWD-3 | four inbound queues, consumer per box, read-ack | measured (two queues today) | C-BUS | wire | S02 | same-window migration |
| S06 | FWD-10 | per-box cloud identities; Dell deny policy | unmeasured | C-IDENTITY | wire | S02 | applied by site Z |
| S07 | FWD-4 | publish and integrate; the queue on the laptop | unmeasured | C-QUEUE | wire | S01, S05 | one writer of the trunk |
| S08 | FWD-1 | the thread: one real round laptop -> dell1 -> site Z -> laptop, timed | unmeasured | the ACCEPT line | verify | S01-S07 | a real project, not a practice round |
| S09 | FWD-6 | gate 5 under the standing push rule | measured (gate 5's header, brief F4) | C-PUSH-RULE | wire | Andrew's text | law edit by his order |
| S10 | FWD-9 | the lease register | unmeasured | C-LEASE | wire | S05 | expiry, not release by hand |
| S11 | FWD-11 | work-in-progress publication at cell close | unmeasured | C-RESTART | wire | S07 | at most one cell lost |
| S13 | FWD-13 | the bid for a move: four devices, disk and storage measured, the laptop's fabric manager awards | measured (the CRO's read of `remote-job.py`) | C-BID | wire | S02, S05 | between rounds only |
| S12 | FWD-12 | one decision list on the laptop | unmeasured | C-ATTENTION | wire | S05 | no blocking prompt on an unattended box |

MECE check: every one of the 13 outcomes has at least one row.

## 8. BRIEF COVERAGE -- content carried, not just cited

| Brief heading | Carried content | Consuming sections |
|---|---|---|
| PART I, thread and O1-O10 | the thread; ten outcomes | ENDPOINT FWD-1..FWD-11; section 2 |
| PART II, boundary | owns the register, routing, queue, gate, per-box files, leases, identities, skill edits; relies on the workflow, the law files, the kit, each directive's projects, portal DEV; tradeops out | C-ROLES; section 5; engines |
| PART III, bar | a third lane added without hand edits; no conflict resolved twice; asked only on a deploying push; restart readable; no relayed "free" | FWD-2, FWD-8, FWD-6, FWD-11, FWD-9 |
| PART IV, F1-F8 | one trunk; a push deploys; two-device bus; gate 5; placement field; per-device file exists once; owned-paths; laptop capacity | C-TRUNK-DEPLOY, C-BUS, C-PUSH-RULE, C-PLACEMENT, C-ONE-WRITER |
| PART V, must be true | FWD-5 before FWD-4; Andrew's order for the law edit; dell1 standing; builder names; planning retires at close; seat limits; no shadow | section 2; rulings 1-8; C-NAMES; C-NO-SHADOW |
| PART VII, not claimed | no Dell measured; integration time unmeasured; overlap uncensused; site Z capacity unread; other hooks unchecked; cost unestimated | S-row claims; round 2 measures the thread's timings |

-- 1.0.0_SA_CTO

## ADDENDUM v0.2 (1.0.0_SA_CTO, clock read 14:16Z 2026-10-06) -- an ENDPOINT change on Andrew's word: FWD-3 and FWD-7 amended, FWD-13 added

**Words**, at the `4.0.0_SA_CRO` terminal, records in `org/tier1_exec/4.0.0_SA_CRO/deliverables/`:
`ANDREW_DIRECT_20261006_14xxZ_FOUR_DEVICE_MSTR_RELAY_PER_BOX_FOLDERS_SPLIT_BY_BID.md` @ab368f2e7c and
`ANDREW_DIRECT_20261006_14xxZ_FOUR_DEVICE_THREE_POINTS_AGREED.md` @3bee43ca11 ("agreed on all points go ahead").

- FWD-3 amended in place: box-to-box messages go fabric manager to fabric manager only.
- FWD-7 amended in place: the placed unit is a project or a workstream.
- FWD-13 added: a move between boxes, elected by the one CTO on the laptop, placed by bid, between rounds only.
- New contracts C-SERIALS and C-BID; manifest row S13.
- Unchanged: the push-rule law text is still not approved by Andrew (C-PUSH-RULE).

**Sign-off:** an ENDPOINT change, so the ratified-text half re-opens.
