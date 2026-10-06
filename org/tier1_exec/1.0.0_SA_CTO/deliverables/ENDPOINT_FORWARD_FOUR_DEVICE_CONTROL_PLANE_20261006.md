# ENDPOINT (step 2, /endpoint --forward) -- the four-device control plane (laptop, sitez, dell1, dell2)

Author `1.0.0_SA_CTO`, 2026-10-06 ~03:1xZ (11:1x PM Eastern, 2026-10-05). **STATUS: CONFIRMED by Andrew** ("im good with all of this", record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_13xxZ_FOUR_DEVICE_ENDPOINT_CONFIRMED_FWD4_FIX_FWD12_ADD.md`), with
the two changes below. Registered as NFRA_CTLPLN under D0; the PRD carries this section.

**Brief read:** `docs/briefs/four-device-control-plane-brief-20261006.md` @a77b65337e (`4.0.0_SA_CRO`, 175 lines, read in full).
Design behind it: `docs/briefs/four-device-control-plane-proposal-20261006.md` @86bdc8c3cb (not re-read here). Andrew's words: the
three records the brief names, in `org/tier1_exec/4.0.0_SA_CRO/deliverables/` (the control-plane ask, "yes I like this layout",
"all recs approved").

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

  FWD-3  A seat on any box sends a message to a seat on any other box, and the sender can show it
         was read
         DONE WHEN  EXERCISED -- one message each way between every pair of boxes in use
         ACCEPT     a message sent from one box reaches the right seat on another, and the sender can
                    show that it was read, not only delivered
         SOURCE     brief O2

  FWD-4  A finished round from any working box reaches the shared trunk without that box pushing
         it, and no lane falls more than one round behind
         DONE WHEN  EXERCISED -- two boxes' rounds published and merged in the order the laptop set
         ACCEPT     each working box publishes its finished round; site Z merges published rounds in
                    the order the laptop set and pushes. No box holds more than one unpublished round
                    per lane
         SOURCE     brief O3

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

  FWD-7  Anyone can see which box runs each project, and no project is split across boxes
         DONE WHEN  EXERCISED -- the placement read for every live project
         ACCEPT     each project names its box; one project is on one box; two projects on different
                    boxes change different files; a box with room and nothing placed on it is visible
         SOURCE     brief O6

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
```

## Reachability

- **FWD-1, FWD-9, FWD-10, FWD-11, and FWD-3 for a Dell, need dell1 standing.** The Dells are not delivered; no seat can do that.
- **FWD-6 needs Andrew's law edit** (the brief's one open item). The current push rule stands until it lands.
- **Can start before a Dell arrives,** on the two boxes that exist: FWD-5 (the push gate deploys from the trunk only), FWD-2 (one
  device register), FWD-7 and FWD-8 (placement and per-box files). The brief's PART V puts FWD-5 before FWD-4.

## Three calls for Andrew

1. **Confirm these eleven outcomes and their DONE WHEN lines.**
2. **Register now under D0 and start the pre-Dell work** (FWD-5 first, then FWD-2, FWD-7, FWD-8). Recommended: a push gate that
   deploys on ANY pushed branch is a hazard the moment a second branch is pushed, Dells or not.
3. **The law-edit wording for FWD-6:** this seat drafts it and shows it to him; his yes to that text is the order.

## Provenance

GROUNDED ON: the brief, read in full. NOT READ: the proposal (cited by the brief), any code (the brief's file-and-line claims are its
measurements), the task-order register (no project exists). Not checked by this seat: the push gate deploying on any pushed branch
(`.tools/git-hooks/pre-push-safe-deploy.sh:41-58`); that is the work's first read.

-- 1.0.0_SA_CTO
