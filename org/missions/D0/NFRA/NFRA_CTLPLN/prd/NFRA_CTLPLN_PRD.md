# NFRA_CTLPLN -- the four-device control plane: the laptop plans, site Z integrates and deploys, dell1 and dell2 execute

```json
{
 "project": "NFRA_CTLPLN",
 "directive": "D0",
 "fabric": "laptop",
 "prd_version": "v0.31",
 "step": 4,
 "brief_ref": "docs/briefs/four-device-control-plane-brief-20261006.md@a77b65337e",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8", "FWD-9", "FWD-10", "FWD-11", "FWD-12", "FWD-13", "FWD-14", "FWD-15", "FWD-16", "FWD-17", "FWD-18", "FWD-19", "FWD-20", "FWD-21", "FWD-22", "FWD-23", "FWD-24", "FWD-25", "FWD-26", "FWD-27", "FWD-28"],
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
         through dell1's own branch and the laptop's integrator, and is graded on the laptop -- and
         Andrew can see how long each step took
         DONE WHEN  EXERCISED -- one real round, traced from its PRD on the laptop to its grade
         ACCEPT     a real project's round is planned on the laptop, worked and finished on dell1,
                    pushed by dell1 to its own branch, merged into the shared trunk by the laptop's
                    integrator, and graded on the laptop. Nobody on dell1 writes the shared trunk.
                    Andrew reads afterwards when each step began and ended. A step done by hand on
                    another box, or a practice round, fails it
         SOURCE     brief PART I, the candidate thread; re-based v0.22

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

  FWD-4  A finished round from any working box reaches the shared trunk without that box writing
         the trunk, and no lane falls more than one round behind
         DONE WHEN  EXERCISED -- two boxes' rounds pushed to their own branches and merged by the
                    integrator
         ACCEPT     each working box pushes its finished round to its own branch; the laptop's
                    integrator merges every box's branch into the shared trunk on its schedule, and no
                    box writes the shared trunk itself. No box holds more than one unpushed round per
                    lane
         SOURCE     brief O3; re-based v0.22

  FWD-5  Pushing work from any box never puts anything into production except what a signed change
         names for that exact build
         DONE WHEN  EXERCISED -- a box push carrying a pipeline script no open change names, and
                    nothing deployed
         ACCEPT     when a box pushes its own branch, only a script that an open signed change names,
                    at the exact version it signed, goes live; any other script in the push is held
                    and written down, and the push still goes through. Merging the shared trunk
                    deploys nothing
         SOURCE     brief O4; re-based v0.22 (the box-push deploy and the pinned-build rule)

  FWD-6  Routine work reaches the shared trunk with no one's word, and only a production release of a
         page clients can open waits for Andrew
         DONE WHEN  EXERCISED -- one routine push and merge with no one asked, and one release of a
                    client-facing page held until his word
         ACCEPT     a push of any box's work, and its merge into the shared trunk, happen without
                    anyone at a terminal; a production release that changes a page a partner firm or
                    client can open waits until Andrew says so, and a release of a staff-only page
                    does not
         SOURCE     brief O5; re-based v0.22 on the push law

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

  FWD-10 The record shows which box did each act; a Dell can deploy its own committed work without
         waiting on another box, and can never alter the audit trail or delete production data
         DONE WHEN  EXERCISED -- one deploy from a Dell of a committed candidate it names, succeeding
                    before any other box has merged that work; one attempt to delete production data,
                    refused; one attempt to alter the audit trail, refused
         ACCEPT     every act in the record names its box; a Dell puts code or data live only through the
                    deploy tools, from a commit it names in its own record of the deploy, and waits on no
                    other box to do so; its attempts to alter the audit trail, or to delete production
                    files, tables or databases, are refused
         SOURCE     brief O9; Andrew's card 5; Andrew-direct 2026-10-07 ~00:5xZ, "they should have deploy
                    ability"; Andrew-direct 2026-10-07 ~07:0xZ, "Definitely drop one lane cap and
                    shared-branch wait for the dells"; Andrew-direct 2026-10-13 ~16:5xZ, "Sure let's do
                    rec b" (his access, keeping three refusals; v0.31)

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

  FWD-14 From his MacBook Andrew opens a remote desktop on all four boxes, and from the Windows laptop
         on the other three, over Opal's private network, and from nowhere outside it
         DONE WHEN  EXERCISED -- one session from the MacBook to each of laptop, site Z, dell1 and dell2, and
                    one from the Windows laptop to each of site Z, dell1 and dell2, all over the private
                    network; one remote-desktop attempt at any box from an address off the private
                    network, refused
         ACCEPT     Andrew sits at his MacBook and opens a remote desktop to the laptop, site Z, dell1 and
                    dell2 in turn; at the Windows laptop he opens one to site Z, dell1 and dell2; each goes
                    over Opal's private network; the remote desktop from "rc" into the laptop stays as it
                    is; no remote desktop answers from outside the private network, the IT remote-support
                    services Andrew names (Splashtop) excepted; a box added later is reachable the same way
                    as part of being set up
         SOURCE     Andrew-direct 2026-10-06 ~18:5xZ, "we need RDP on all devices accessible
                    via tailnet" and "that RDP ability from any device in the tailnet, namely the macbook";
                    the directions, Andrew-direct ~20:1xZ; Andrew-direct 2026-10-13 ~14:0xZ, "no external
                    ssh available nor any external rdp available (aside from IT services like splashtop)"

  FWD-15 A lane on a Dell that needs a package the box does not have gets it from the laptop, checked,
         without the Dell ever asking the internet for it
         DONE WHEN  EXERCISED -- one real package taken the whole way for one Dell lane, and the lane's
                    work then runs
         ACCEPT     a lane on a Dell needs a package its box cannot use as delivered; the laptop gets the
                    one exact file, checks it, and sends it over Opal's private network; the Dell installs
                    it from that file alone and the lane's work runs; during all of it the Dell asks no
                    outside site for anything; a file taken from a saved example instead of the real route
                    fails the outcome
         SOURCE     brief I.0, the candidate thread; Andrew-direct 2026-10-07 ~13:39Z, "it is preferable
                    for the laptop device to check it out first, and if clean and clear, it can be
                    taildropped"

  FWD-16 Anyone can tell whether a package is approved, ask for one that is not, and later read who
         said yes or no and why
         DONE WHEN  EXERCISED -- one request made, one approved and one refused, and both decisions read
                    back by someone who was not part of them
         ACCEPT     two people on two boxes asked "may I install this?" give the same answer without
                    asking anyone; a person who needs something not approved files one request that says
                    what, which exact version, what needs it and why nothing approved will do; a reviewer
                    answers yes or no; afterwards Andrew can read who approved which package, on what
                    evidence, and when; a refusal reads as clearly as an approval
         SOURCE     brief O1, O2, O3; Andrew-direct 2026-10-07 ~14:0xZ, "some kind of request pipeline
                    for additions to requirements.txt and a review process"; who reviews, Andrew-direct
                    ~15:1xZ, "deliver their recommendation to the CTO and CTO runs the requirements
                    addition"

  FWD-17 For anything that reached a box, a person can say what was checked before it was sent and
         what those checks cannot rule out
         DONE WHEN  EXERCISED -- one delivered package's record read aloud to Andrew, including what
                    was not checked
         ACCEPT     for a package on a Dell, someone states the checks the laptop ran before sending it
                    and names the risks those checks leave; asked "would this have caught a package whose
                    own maker's account was taken over?", the answer given is the true one, even when it
                    is no; nothing is called clean beyond what was looked at
         SOURCE     brief O4 and Part V.1

  FWD-18 A box that tries to get a package, a script or a program from the internet is stopped on
         the box and told the route that works; the laptop alone fetches a package, by the checked
         route
         DONE WHEN  EXERCISED -- a download tried on purpose and stopped on a Dell and on site Z, and
                    the delivered file then installed on each
         ACCEPT     on a Dell, and on site Z, someone tries, on purpose, to install a package from the
                    public internet and is stopped, and what they are told names the route that works; on
                    the laptop the only way a package arrives is the checked route; a script or a
                    program off the raw internet has no route at all and comes only from another Opal box;
                    building the website on any box downloads nothing, including what a tool would fetch
                    on its own without being asked; what is counted is requests leaving the box, not the
                    absence of an error
         SOURCE     brief O5, O6, O7; Andrew-direct 2026-10-07 ~13:39Z, scripts and executables off the
                    raw internet "never, ever"; every box, Andrew-direct ~15:1xZ, "Rec approved."

  FWD-19 Andrew can ask what a box downloaded and get an answer from a record, and a lane waiting on
         a package is seen, not stuck
         DONE WHEN  EXERCISED -- the question asked about one box for one day and answered from what was
                    written at the time
         ACCEPT     Andrew asks "what did this box download today?" and someone answers from a record
                    made at the time, not from memory; a lane that needs a package not yet delivered
                    loses that one piece of work, keeps going elsewhere, and its wait shows in the same
                    place he sees every box's open decisions; nothing here watches or sends him anything
                    on its own
         SOURCE     brief O8, O10; the standing rule that no monitor is built unless he asks

  FWD-20 Someone at Opal asks for a piece of work in a message, Andrew hears of it from one text with
         a recommendation, a fresh seat on the box with the most room does it, a reviewer grades it,
         and the person who asked is told it is done
         DONE WHEN  EXERCISED -- one real request taken the whole way, and the person who asked told the
                    outcome
         ACCEPT     a person asks for a small piece of work in Teams; Andrew gets one text saying what
                    was asked and what is recommended, and can answer it without opening Teams; the
                    job goes to the box with the most room by a measurement taken when it is offered; a
                    seat started fresh for that job, handed a written brief, does it; a seat that did
                    none of the work grades it; the person who asked is told, where they asked, that it
                    is done; a request replayed from a saved example fails the outcome
         SOURCE     brief I.0, O1, O2, O3; Andrew-direct 2026-10-07 ~16:3xZ, "The agents that get those
                    jobs should be spawned fresh, briefed, and run /remote-drive"

  FWD-21 The fabric manager on every box keeps its fabric running without being asked, and decides
         nothing about any project
         DONE WHEN  EXERCISED -- one seat left hanging on a box nobody is watching is moving again
                    without anyone asking, and the manager's record for a day is read for project rulings
         ACCEPT     on a box nobody is watching, a seat that hangs is moving again, a dead one is
                    replaced and finished work is brought together, by that box's manager, without
                    Andrew or another seat asking; someone reading what the manager wrote that day finds
                    no opinion on how any project should be done
         SOURCE     brief O4; Andrew-direct 2026-10-07 ~16:3xZ, "MSTR whole purpose is not business
                    logic/project reasoning, they are infrastructure managers"

  FWD-22 Every open decision on a box is held by that box's technology lead, who settles the ones
         that are the box's own; one that touches another box is settled between the two, on the record
         DONE WHEN  EXERCISED -- one decision that touched one box settled there and never shown to
                    Andrew, and one that touched two boxes read afterwards from both sides
         ACCEPT     a decision that touches only one box may be settled by that box's technology lead
                    and then does not reach Andrew as a question; an act only he can do still reaches him,
                    named as that act; a decision that touches another box goes from
                    one manager to the other, and afterwards someone on either box can read what was
                    agreed and by whom; neither box learns of the other's decision by finding its effect
         SOURCE     brief O5, O6; Andrew-direct 2026-10-07 ~16:3xZ, "they must have their MSTR reach out
                    to the MSTR of the relevant fabric and coordinate as needed"

  FWD-23 Anyone can tell what each operations seat on a box is doing, and no piece of driven work
         finishes without a reviewer on that box grading it
         DONE WHEN  EXERCISED -- one box's seat list read by someone who then names each seat's work
                    without opening a log, and one finished piece of work shown with its grade
         ACCEPT     a person reading a box's list of seats can say what each operations seat is doing,
                    and can see one that is doing nothing; every box that does driven work has a
                    reviewer, and a piece of work is not counted finished until a seat that did none of
                    it has graded it, on the box where it was done
         SOURCE     brief O7, O8; Andrew-direct 2026-10-07 ~16:3xZ, "CVO is dedicated reviewer in those
                    drive processes so mandatory spawn on any fabric"

  FWD-24 A technology lead gets research on a risky operation when it is above a stated line, and
         does not ask for it below
         DONE WHEN  EXERCISED -- the same operation put to two technology leads on two boxes, and both
                    give the same answer to whether research is owed
         ACCEPT     looking at an operation, a technology lead can tell from how it is already classed
                    whether research is owed before it runs, and the research seat can tell whether an
                    ask was owed; two leads asked about the same operation answer alike
         SOURCE     brief O9; Andrew-direct 2026-10-07 ~16:3xZ, "if the project does not meet a meaningful
                    quantified risk layer ... there is no need to bring them out"

  FWD-25 A seat that starts on any box is told what it is by what starts it, and a tool stops or
         flags the act its role forbids
         DONE WHEN  EXERCISED -- one seat of each kind started on a box and asked what it is, and one
                    forbidden act per kind tried and stopped or flagged by a tool
         ACCEPT     a seat started on any box can say what its role is and is not, from what it was
                    given at start; when a seat tries the thing its role forbids, a tool refuses or
                    flags it, and it is not left to another seat to notice; this holds for how code
                    moves, how cloud changes are made, and how seats work
         SOURCE     brief O10; Andrew-direct 2026-10-07 ~16:3xZ, "whether it takes place in launcher
                    updates, skill updates/creation, gates, etc., I want to make sure we cover both
                    GitOps, AWS DevOps, and Agent Workflow Ops"

  FWD-26 Anything an agent writes in Andrew's name is written from one file of how he writes
         DONE WHEN  EXERCISED -- one draft written for him from the file and read by him
         ACCEPT     there is one file that shows how Andrew writes, built from real messages of his
                    for each kind of thing an agent would write for him; an agent drafting a reply or
                    a post in his name uses it, and Andrew reading the draft says it sounds like him;
                    nothing is sent in his name that he has not approved
         SOURCE     Andrew-direct 2026-10-07 ~21:4xZ, "i need an andrew_voice.md used for anything
                    that an agent would speak for, that uses representative emails or teams messages
                    or whatever as a reference for the given action"

  FWD-27 Every box on the tailnet answers an SSH login by key from the tailnet devices Andrew works
         from ("rc", "muse" and the laptop "cloud-local"), the laptop included as a target, and from
         nowhere outside the tailnet
         DONE WHEN  EXERCISED -- `ssh -o BatchMode=yes <user>@<tailnet-ip> hostname` answers with the
                    box's own name for sitez, dell1, dell2 and the laptop from each of rc, muse and the
                    laptop (muse -> laptop included); one login attempt from a non-tailnet address at
                    any box, refused
         ACCEPT     on each of the four boxes OpenSSH Server runs as a service, port 22 is admitted
                    only from 100.64.0.0/10, password authentication is off once a key is in
                    place, and RDP is unchanged and bound the same way (FWD-14); a login by password
                    or from a non-tailnet address is refused; on the laptop, whose only interactive
                    account is an Entra account sshd cannot resolve (measured by 0.0.0_AB_MSTR
                    2026-10-13 ~00:5xZ, msg 108757), key logins land on a local administrator account
                    made for them, whose Administrators membership is re-read after one Intune policy
                    sync and recorded; the elevated runs on each box (the sshd enable, the laptop
                    account) are Andrew's one line each, the script and its receipt are the cell's;
                    the keys of rc and the laptop are Andrew's to place, muse's is in place on all
                    four (measured: dell1, dell2 and sitez answer muse today; the laptop holds its key)
         SOURCE     LD-0644 (Andrew-direct 2026-10-11 ~15:5xZ); Andrew-direct 2026-10-12 ~01:5xZ,
                    "I also want that tailnet port set up so that we can ssh into the various devices
                    as well as rdp ... perhaps COO~C can handle it"; Andrew-direct 2026-10-13 ~14:0xZ,
                    "'muse' also needs to be able to remote into laptop ... ssh to be functional within
                    tailnet devices only, no external ssh available nor any external rdp available
                    (aside from IT services like splashtop)" (ADDENDUM v0.29)

  FWD-28 A data-proxy route that no partner page calls answers only an Opal-internal caller; a
         route a partner page calls answers the firms that page admits, and no one else
         DONE WHEN  EXERCISED -- one call to an internal-only data-proxy route with a partner-firm
                    token answers 403 and with an internal token 200; one call to a partner-page
                    route with an allowed firm's token answers 200 and with a token of a firm the
                    page does not admit answers 403
         ACCEPT     every `opal-portal-data-proxy` route (41 at the 2026-10-12 census, CT-u-6) is classed ONCE, by measurement, into
                    (i) routes called by a page in `portal/src/.../firmAccess.ts` FIRM_ALLOWED_PATHS
                    and (ii) the rest; class (ii) refuses any caller whose authorizer `tier` is not
                    `internal` (the tier the authorizer DERIVES from the firm, jwt.ts:168, so every staff
                    login reads internal), UNLESS its `userType` is `Dev` -- a clause the applied code
                    carries (lambda_function.py:2112) whose only reachable effect is to admit a Dev token
                    on a non-Opal firm; it is REMOVED at the next apply of this function (v0.28, cell
                    CT-aa-5) and until then PRE-1's invariant stands: no Dev row on a non-internal firm;
                    class (i) refuses a caller whose `firmId` is not in the firm set the
                    SAME source admits for that page (one source, never a second list) -- that firm
                    check lands when the generated firm-set module is an `opal_naming` target
                    (registry row, LGIC owner); until then class (i) stays as today, open to every
                    verified login, and is said so in the round's analysis; the content
                    api GET stays open to every verified portal login (page copy, LOW), PUT and
                    DELETE keep their firm fence; no handler checks that an event "came through API
                    Gateway"; applied by Terraform under a signed pair with a NEVER-2 ledger; no
                    page a partner login can open today changes what it shows that login
         SOURCE     CTO ruling on XB-20261011T194408Z-e588 (2026-10-12), amended on row
                    NFRA_CTLPLN-W62-S1 (2.0.0_SA_COO~C msg 108433, 02:5xZ): the tier-only fence
                    would 403 the market/portfolios/positioning/valuations/macro/philosophy pages
                    partner firms are admitted to
```

## PROVENANCE (outside the ratified section)

- The ENDPOINT was proposed at
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_FOUR_DEVICE_CONTROL_PLANE_20261006.md` and confirmed by Andrew with two
  changes: FWD-4's headline ("lane", not "box") and FWD-12. A word of his that amends an FWD becomes an addendum under the next
  unused id (FWD-13) or an in-place amendment, never a cell's choice.

## CONTRACTS

| Contract | Direction / owner | Binding agreement |
|---|---|---|
| C-ROLES: what each box is | Andrew's six cards; proposal 3 | **laptop:** the control plane. It writes the cross-box registers (placement, the sequence, the live-arms register), orders the merge queue, creates roles and administers access for the Dells, and runs its own planning seats (CTO, CRO, CVO); at most one execution lane. It is no longer the only box with planning seats (v0.12: each Dell runs a CTO lane and a CVO for the projects placed on it). **sitez:** the integrator; it merges the boxes' rounds, pushes the trunk and keeps the Bloomberg jobs. It is no longer the only box that deploys (v0.9: a Dell deploys its own committed work as a named act). **dell1, dell2:** the workhorses (v0.9): they run every project placed on them with no lane cap set here, deploy their own committed work as a named act, and create non-IAM resources; they never push the trunk, change access, call a vendor without Andrew's per-use word, or write a register. Site Z's planning lanes retire as their projects close, never mid-project (card 3). |
| C-TRUNK-DEPLOY: a publish never deploys (FWD-5) | this project; `.tools/git-hooks/pre-push-safe-deploy.sh` | MEASURED at L4 (`pre-push-safe-deploy.sh:41-70`): the hook runs `safe-deploy.sh --commit-range` for EVERY pushed ref that is not a tag or a delete, so pushing any branch uploads the pipeline scripts in its range. After this contract: the deploy gate runs only when the pushed REMOTE ref is `refs/heads/CLOUD`. Every other branch push prints one line saying no deploy ran and why, and exits 0 for the deploy gate (the HALTGT checkpoint above it is unchanged). This lands BEFORE any round branch is published (brief PART V). |
| C-QUEUE: publish and integrate (FWD-4) | this project; `/integrate` split in two (proposal 5.2) | A box publishes ONE branch per finished round, `q/<device>/<PROJECT>/r<N>`, and sends one bus line to the laptop. The laptop holds the ordered queue (SEQUENCE, then arrival). Site Z takes the head, merges in its own worktree (the commit hooks grade once, there), pushes the trunk, announces the new head, and deletes the queue branch. Every box pulls the trunk at its next round start. A same-line conflict at integration is a PLACEMENT finding routed to the laptop, never resolved silently at the merge. This is not the retired two-branch model: a queue branch lives one round and flows one way. |
| C-PUSH-RULE: the standing push rule (FWD-6) | Andrew; the locked law files | The rule lives in `org/XXX.md` Step 1b and is enforced by `.tools/hooks/never-rules-gate.sh` gate 5. It changes only by an `ANDREW_LAW_EDIT_ORDER` naming a record in which Andrew approved the EXACT text. **The text is APPROVED** (Andrew ~15:1xZ 2026-10-06, "Yes, agreed with this"; record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_150xZ_PUSH_RULE_LAW_TEXT_APPROVED.md` @7b5782d0c6, the `ANDREW_LAW_EDIT_ORDER`). It lands TOGETHER WITH the publish-and-integrate flow (C-QUEUE) and the trunk-only deploy gate (C-TRUNK-DEPLOY), never before them; gate 5 and `CLAUDE.md`'s Git section carry the same rule in the same change. Until then the current rule stands: only the fabric managers push, on his word at that terminal. |
| C-REGISTRY: the device register (FWD-2) | this project | ONE file holds each box's name, role, inbound queue, seat limit and lane letters. Every script that today names devices reads it instead (MEASURED: `.tools/agentbus-sqs.sh:84-86` and `:157-158` hardcode `laptop` and `sitez` and infer the device from the Windows profile path). A box's identity is set once at bring-up as a user environment setting, never derived from a path (LD-0405, no device-specific code). The file's home and name are builder output where the builder covers them; the register is a registry row in `infra/logic/registry/` if LGIC holds that class. |
| C-BUS: one inbound queue per box (FWD-3) | this project; `.claude/skills/agentbus/SKILL.md` | Four inbound queues, each drained by that box's fabric manager; any box sends to the recipient's queue. What crosses the bus is small: "round ready", "trunk at", a lease grant, a pointer to a record. READ is the agent-side acknowledgement, as on the local broker. **Every bus message names its sender twice: the seat serial and the box's tailnet name** (and the recipient box's tailnet name), read from `org/devices/DEVICES.json` `tailnet_name`, never typed: the tailnet name is the real identifier of the box (Andrew-direct 2026-10-07 ~02:5xZ, "can it have their tailnet names attached in addition to serial ... the tailnet name is the real identifier"). Carried as an SQS message attribute and in the envelope; a message whose tailnet name is not in the register is refused by the consumer. **Names, builder output at L4:** `name('agentbus','global','dell1','queue')` -> `agentbus-global-dell1-queue` (likewise per box). The queues are FIFO, which AWS marks with a `.fifo` suffix the builder does not emit today: the cell resolves that with an LGIC registry change, never a hand-typed name. The two existing queues (`agentbus-ajbdev-*`) migrate inside this project, same-window, no parallel bus. |
| C-PLACEMENT: one project, one box (FWD-7) | the laptop; `org/missions/DIRECTIVES.yaml`, `org/missions/SEQUENCE.yaml` | A project's row names its box (`fabric`: `laptop`, `site-z`, `dell1`, `dell2`). A project is never split. Two projects go to different boxes only if their write surfaces do not overlap, checked as `.tools/owned-paths-validate.py` checks a worker, one level up. Andrew's first allocation (card 6) is the starting point; each move is his when it happens, and nothing moves until a Dell is standing. |
| C-ONE-WRITER: files (FWD-8) | this project | Registers (`DIRECTIVES.yaml`, `SEQUENCE.yaml`, `LIVE_ARMS.md`, project rows, missions-tree carriers, the law files): the laptop only. A project's own tree: its box only. Append-only files (surprise channels, audit logs, session logs): one file per box, `<name>.<device>.md`, the pattern `org/surprise_channel/ETFS_INGEST/INVESTIGATION_v1.Z.md` already uses. The surprise-row gate and the readers that compile a channel learn to read every per-box file of a channel. |
| C-LEASE: scarce accounts (FWD-9) | this project; the laptop holds the register | One lease register on the laptop: resource, holder box, expiry. Covered: the walker account, the YCharts session, the portal `DEV` push, the Bloomberg daily quota. A lease expires by itself; a dead box's leases lapse. The Dells take no vendor lease (vendor pulls stay scheduled on their existing homes). |
| C-IDENTITY: per-box cloud identity (FWD-10) | this project; cloud IAM (IAM-creating applies at site Z only) | Andrew-direct ~00:5xZ 2026-10-07 (relayed by `0.0.0_AB_MSTR` msg 105876): "I am cool with this but they should have deploy ability" -- one IAM group and one IAM user per Dell, never `Andrew_Berman`'s keys. **Scope (this seat's ruling):** ALLOW code and data deploys through `.tools/safe-deploy.sh` and `safe-apply` for non-IAM resources, each with the box's own ledger entry; a Dell deploys a commit it names in its own ledger entry, from its own committed work, and waits on no other box's merge or push (v0.9, Andrew-direct ~07:0xZ; v0.6's "only commits already on origin CLOUD" is withdrawn); C-TRUNK-DEPLOY still holds for a PUBLISH, which deploys nothing; DENY IAM user, key, role and policy changes, CloudTrail changes and production data deletes, by policy, so the cloud refuses them. **v0.31 (Andrew-direct 2026-10-13 ~16:5xZ, "Sure let's do rec b"):** both Dell users join `AdministratorAccessOpalCapital`, and only three Deny classes remain: CloudTrail and audit-trail writes, production S3 object deletes, and table and database deletes. The IAM deny in this row and in v0.7 is withdrawn. **v0.7 (Andrew-direct ~06:3xZ 2026-10-07, 'they should be allowed to create resources though'):** the policy GRANTS create, update and tag on the non-IAM resource kinds the Dell-placed projects' Terraform declares, so `safe-apply` of a non-IAM resource succeeds from a Dell and waits on no other box; the IAM deny is unchanged. Never-widen halves still bind every served move. Keys live in each Dell's own credential store and are rotated by site Z. **Names** (builder output, shared resources so scope None; NAMING_SCHEMA v1.13 @01c56eda2b added kinds `user` and `group`): users `cloudops-dell1-agent-user` and `cloudops-dell2-agent-user`; group `cloudops-dell-agents-group`, tagged DisplayName=DellBoxes (Andrew's name for it); policy `cloudops-dell-agent-deploy-policy`. The IAM traps in `/cloud-ops` apply. |
| C-RESTART: rounds survive a box restart (FWD-11) | this project | A lane on any box publishes its work-in-progress branch at each cell close, so a disk loss loses at most one cell. The round's state is read from the published branches and the ledger, never from one box's memory. Proposal 5.9 lists the cases (a Dell, site Z or the laptop down; a box whose bus consumer is not running). |
| C-ATTENTION: one decision list (FWD-12) | this project | A box records each decision it needs from Andrew as a file on its own tree plus one bus line to the laptop; the laptop shows one list of every box's open decisions; his answer is recorded on the laptop and reaches the asking box as a file and one bus line. No lane on an unattended box blocks on a prompt at that box. |
| C-SERIALS: one fabric manager per box | Andrew, "agreed on all points go ahead" | `0.0.0_AB_MSTR` (laptop), `0.0.0_AB_MSTR~SITEZ`, `0.0.0_AB_MSTR~DELL1`, `0.0.0_AB_MSTR~DELL2`, each with its own tier-0 folder. Site Z's `~Z` stays as an ALIAS in the device register so every past record still resolves; the rename lands at a site-Z restart. Only these seats talk across boxes (FWD-3). |
| C-BID: placement of a move (FWD-13) | Andrew; `.tools/remote-job.py` | One CTO, on the laptop, elects a move and tells the laptop's fabric manager. That fabric manager offers it to the boxes' fabric managers, which bid with measured load; it awards the move. MEASURED at L4 by the CRO (record @ab368f2e7c): `remote-job.py` bids CPU and memory via `psutil`, knows two devices (`DEVICES = ("laptop", "sitez")`), and its awards run through LDO-001; disk and storage are not measured. The bid adds disk and storage and reads devices from the register (C-REGISTRY). LDO-001 keeps awarding Teams remote jobs; the laptop's fabric manager awards moves. A move happens only between rounds: the old box publishes its last round (C-QUEUE), the new box pulls the trunk and seats the lane. |
| C-NAMES | CLAUDE.md rule 30 | Every new queue, identity, register home and branch prefix is builder output, printed in the order that creates it. A builder refusal is a missing registry row to add. |
| C-MORATORIUM | law | No alert, alarm, SNS, SES send, freshness checker or monitor. A box that has not acknowledged is visible on the control plane as a state, not a notification. |
| C-RDP: remote desktop over the tailnet (FWD-14) | this project; each box's bring-up | Remote Desktop (port 3389) is enabled on every box in the device register and is reachable over the tailnet (the Tailscale private network); the register records each box's tailnet name and address. CTO ruling, the narrower default: the Windows firewall scopes 3389 to the tailnet's address range only, never the public internet or the local network; the sign-in is Andrew's own Windows account on each box, no shared or agent account. Measured by `4.0.0_SA_CRO` (~19:0xZ, `docs/briefs/four-box-acceleration-plan-20261006.md` section 3a): 3389 answers over the tailnet on the laptop and site Z; dell1 and dell2 are not on the tailnet; firewall scope MEASURED by `3.0.0_SA_CVO` (row NFRA_CTLPLN-S1, ARMED): the laptop admits 3389 from any address on every profile today. Joining the tailnet and enabling Remote Desktop are steps of the new-device kit's bring-up, so a new box is reachable the day it joins. |
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
| S14 | FWD-14 | Remote Desktop on each box, firewall scoped to the tailnet; tailnet name and address in `org/devices/DEVICES.json`; the bring-up step in the new-device kit | held (CRO section 3a) | C-RDP | wire | S02 | tailnet only; proof on each box = one session from the MacBook over the tailnet ACCEPTED and one connection from a non-tailnet address REFUSED |
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
- C-PUSH-RULE: the text is now approved (see the contract); it lands with C-QUEUE and C-TRUNK-DEPLOY.

**Sign-off:** an ENDPOINT change, so the ratified-text half re-opens.

## ADDENDUM v0.3 (1.0.0_SA_CTO, 2026-10-06) -- contract note only

C-PUSH-RULE records Andrew's approval of the exact law text (record @7b5782d0c6) and when it lands. The ENDPOINT is not edited.

## ADDENDUM v0.4 (1.0.0_SA_CTO, 2026-10-06) -- an ENDPOINT change on Andrew's word: FWD-14, remote desktop over the tailnet

Andrew-direct ~18:5xZ at the `4.0.0_SA_CRO` terminal, verbatim in
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_185xZ_CTLPLN_RDP_ON_ALL_DEVICES_VIA_TAILNET.md` @d13ddab4d1: "we need
RDP on all devices accessible via tailnet" and "we are going to need to have that RDP ability from any device in the tailnet,
namely the macbook". Not covered before (the CRO's check). FWD-14 added at the next unused number; C-RDP and S14 added. The two
points he did not state are ruled here to the narrower side: tailnet-only (never the public internet), Andrew's own account only.
Lane: `2.0.0_SA_COO~C` fronts this project with ADVI_COTBKF (Andrew ~18:1xZ); FWD-14 rides round 2 with each Dell's bring-up, and
the laptop and site Z halves need no Dell. The ratified-text half re-opens for `3.0.0_SA_CVO`.

## v0.4 wording (1.0.0_SA_CTO, 2026-10-06) -- on `3.0.0_SA_CVO`'s review @817586a898

FWD-14 SOURCE names no seat. S14's bound gains its negative arm per box. C-RDP cites row S1. Re-opens nothing (proportionate sign-off).

## ADDENDUM v0.5 (1.0.0_SA_CTO, 2026-10-06) -- FWD-14's directions on Andrew's word

Andrew-direct ~20:1xZ (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_201xZ_DSGN_REBRND_CLOSED_AND_RDP_DIRECTIONS.md`):
the MacBook reaches laptop, site Z, dell1, dell2; the Windows laptop reaches site Z, dell1, dell2; the laptop need not reach the
MacBook. FWD-14 amended in place. His Dell setup steps are on his Desktop
(`DELL1_DELL2_TAILNET_AND_REMOTE_DESKTOP_SETUP.txt`): edition check, tailnet join with key expiry off, Remote Desktop on, the firewall
lock to 100.64.0.0/10, no sleep on AC, the connect and refusal tests. The ENDPOINT changed: the ratified-text half re-opens.

## ADDENDUM v0.6 (1.0.0_SA_CTO, 2026-10-07) -- the Dells may deploy (Andrew's word); FWD-10 amended

Andrew-direct ~00:5xZ at the `0.0.0_AB_MSTR` terminal: "I am cool with this but they should have deploy ability." FWD-10's "a Dell cannot put
anything into production" is reversed by his word and amended in place (id unchanged): a Dell deploys trunk code through the deploy tools and
never changes access. C-IDENTITY carries the scope ruled here. Section 5's "Dells execute, site Z deploys" now reads "site Z integrates and
holds every IAM-creating apply; any box deploys trunk code". The ratified-text half re-opens for `3.0.0_SA_CVO`.

## ADDENDUM v0.7 (1.0.0_SA_CTO, 2026-10-07) -- Dells create non-IAM resources; no Dell deploy waits on site Z. Contract only, no ENDPOINT change

Andrew-direct ~06:3xZ at the `1.0.0_SA_CTO` terminal, VERBATIM: "Regarding DELLs, they shouldnt need to create or touch IAMs, they should be
allowed to create resources though. I do not like the idea of gating deploys on sitez, because sitez will bottleneck as it has a lot of work
via opalgateway projects and all of asset management workstreams." Record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_063xZ_DELLS_CREATE_RESOURCES_NO_IAM_DEPLOYS_NOT_GATED_ON_SITEZ.md`.

- **Measured gap.** `infra/aws/terraform/nfra-ctlpln-identity/dell_deploy_policy.json` grants update of existing Lambda code, ECS task
  registration, EventBridge rules and S3 and DynamoDB data writes, and NO create action for a function, table, bucket, queue, schedule,
  secret or route. C-IDENTITY v0.6 already allowed `safe-apply` for non-IAM resources; the applied policy did not deliver it.
- **C-IDENTITY amended in place** (the v0.7 sentence). FWD-10's text is unchanged: a Dell deploys, and never changes access.
- **Round 3, first cell:** the policy grants create, update and tag for the non-IAM resource kinds declared under the Terraform roots of
  the projects placed on a Dell (derive the list from those roots, never from memory), with the four Deny statements kept. Done when one
  `safe-apply` from a Dell creates a non-IAM resource and one IAM write from the same Dell is refused. The Lambda narrowing follows it.
- **Section 7, S06:** "applied by site Z" binds the IAM-creating apply of this policy only; it is not a rule for Dell deploys.
- **Open at Andrew, not ruled here:** (1) who creates the role a new function or task needs, and whether a Dell may pass an existing
  named role (row NFRA_CTLPLN-W1-S1); (2) C-TRUNK-DEPLOY's wait on site Z as the one box that merges Dell rounds and pushes the trunk;
  (3) whether a bucket policy, a key policy and a Lambda permission count as resources or as access.

A contract change under the ENDPOINT hash: no half re-opens (CLAUDE.md rule 27, proportionate sign-off).

## ADDENDUM v0.8 (1.0.0_SA_CTO, 2026-10-07) -- C-ROLE-REQUEST: the laptop creates roles, a Dell writes in for one. Contract only, no ENDPOINT change

Andrew-direct ~06:4xZ at the `1.0.0_SA_CTO` terminal, VERBATIM: "ok i like the laptop for creating roles, we can manage that for now, and the DELLS write in for that purpose". Record: the 063xZ record named in v0.7, third word.
It closes v0.7's open question (1).

- **C-ROLE-REQUEST (new contract; owner this project; counterpart the laptop's IAM-holding seat).** A Dell never creates, edits or
  attaches policy to a role. When work placed on a Dell needs a role, the Dell WRITES IN: one request naming the project, the resource
  the role is for, the service that assumes it and the permissions asked, each permission tied to the code line that needs it. The laptop
  reads the request, writes the role in that project's Terraform root and applies it. Site Z is not in this path.
- **Passing a role (this seat's reading, flagged in the record).** The Dell policy allows `iam:PassRole` only on roles the laptop has
  made for Dell-placed work, named in the policy, with the `iam:PassedToService` condition. Every other IAM action stays denied. This
  disarms row NFRA_CTLPLN-W1-S1 once applied.
- **Round 3 cells this adds, after v0.7's first cell:** (a) the request's carrier and shape, on the bus the Dells already have; (b) the
  PassRole statement and its named-role list, derived from the roles the laptop has made, never from a wildcard; (c) one exercised
  round trip: a Dell writes in, the laptop applies, the Dell creates a function with that role, and a pass of an unnamed role is refused.
- **C-IDENTITY's header** "IAM-creating applies at site Z only" now reads "IAM-creating applies at the laptop" for roles Dell-placed
  work needs. The two Dell users, the group and their policy were applied at site Z; where their later changes apply is not ruled here.
- **Still open at Andrew:** v0.7's questions (2) the trunk wait on site Z and (3) access-granting resource policies.
- **INTERIM, on his word seconds later, VERBATIM:** "i think ultimately this should change, but its ok for now". C-ROLE-REQUEST is the
  arrangement until he names its replacement; ENRICHMENT BACKLOG gains one line: "replace the laptop-made role request (C-ROLE-REQUEST)
  with the end state Andrew names". No end state and no date are ruled here.

A contract change under the ENDPOINT hash: no half re-opens.

## ADDENDUM v0.9 (1.0.0_SA_CTO, 2026-10-07) -- an ENDPOINT change on Andrew's word: FWD-5 and FWD-10 amended; the Dells wait on no other box

Andrew-direct ~07:0xZ at the `1.0.0_SA_CTO` terminal, VERBATIM: "THe entire point of the Dells is that they are workhorses, they should be
flying. I am ok with your move of the IRPT pair back to Dell2. Definitely drop one lane cap and shared-branch wait for the dells. Yes i
recommend seating the three lanes successors directly on the dells." Record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_070xZ_DELLS_ARE_WORKHORSES_IRPT_PAIR_DELL2_NO_LANE_CAP_NO_TRUNK_WAIT_SEAT_ON_DELLS.md`.
It closes v0.7's open question (2).

- **FWD-10 amended in place** (id unchanged): a Dell deploys a committed candidate it names, before any other box merges it. The refusal
  arm keeps the access change and drops "code not on the trunk".
- **FWD-5 amended in place** (id unchanged): its headline no longer says only site Z's push puts work live. Its DONE WHEN is unchanged,
  so the round-1 grade (a publish deploys nothing) still reads on the amended text.
- **C-IDENTITY, C-ROLES amended in place.** C-TRUNK-DEPLOY is unchanged: it governs a publish, not a deploy.
- **This seat's contract for HOW (he approved dropping the wait, not a mechanism):** the deploy names its commit by full hash in the
  box's own ledger entry, opened at the start and closed at completion; the commit is on a branch the Dell has published, so any box can
  read the deployed bytes; the trunk merge follows and is never a precondition. Never-widen halves still bind every served move.
- **Round 3 cells this adds:** (a) `.tools/safe-deploy.sh` and `safe-apply` accept a named commit off the trunk from a Dell, and say so
  in the ledger entry; where either refuses today, the refusal's line is the cell's first read; (b) one exercised deploy from a Dell of
  a commit no other box has merged, with the deployed bytes read back against that commit.
- **Lane cap:** none is set for a Dell (`org/missions/SEQUENCE.yaml` v6). `org/devices/DEVICES.json` already carries no Dell limit.
- **Still open at Andrew:** v0.7's question (3), access-granting resource policies.

An ENDPOINT change: the ratified-text half re-opens for `3.0.0_SA_CVO`. The brief half is accepted (the CRO wrote the brief).

## ADDENDUM v0.10 (1.0.0_SA_CTO, 2026-10-07) -- two open questions closed on Andrew's word. Contract only, no ENDPOINT change

Andrew-direct ~06:5xZ at the `1.0.0_SA_CTO` terminal, answering four cards, VERBATIM: "1.) Yes. 2.) For now, laptop should admin. 3.) Stay.
4.) Yes." Record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_065xZ_OPEN_CALLS_FOUR_ANSWERED_PASSROLE_YES_LAPTOP_ADMINS_STAY_CTO_PARKS_AND_CLOSES.md`.

- **Passing a role (card 1, Yes).** v0.8's clause stands as his word, no longer this seat's reading: a Dell may `iam:PassRole` only the
  named roles the laptop made for Dell-placed work, with the `iam:PassedToService` condition; every other IAM action stays denied.
- **Access-granting resource policies (card 2, "For now, laptop should admin").** A bucket policy, a key policy and a Lambda permission
  are administered by the laptop through C-ROLE-REQUEST's write-in, the same request shape with the resource policy as its subject. The
  Dell policy denies the actions that write them. INTERIM on his own "For now"; it joins the v0.8 backlog line. This closes v0.7's
  open question (3); none of v0.7's three questions remains open.
- **Next issuance:** the Deny statements for those actions, listed from the resource-policy actions of the services the Dell policy
  already allows (derived, never from memory), and one exercised refusal.

A contract change under the ENDPOINT hash: it re-opens nothing beyond what v0.9 already re-opened.

## v0.11 wording (1.0.0_SA_CTO, 2026-10-07) -- on `3.0.0_SA_CVO`'s review @18d52b19cf (msg 106015)

Two findings, both taken. FWD-5's SOURCE cited brief O4 alone, which says the opposite of the v0.9 headline: it now also cites the
word that amended it. C-ROLES still said site Z alone deploys: it now says site Z integrates and is not the only box that deploys.
The SOURCE line is inside the ENDPOINT section, so the ratified-text half re-opens for `3.0.0_SA_CVO`; no outcome's DONE WHEN or
ACCEPT changed.

## ADDENDUM v0.12 (1.0.0_SA_CTO, 2026-10-07) -- C-ROLES: each Dell has a CTO lane and a CVO; who signs a Dell-written PRD. Contract only

On `3.0.0_SA_CVO`'s verdict UPHELD (msg 106050; `org/tier1_exec/3.0.0_SA_CVO/deliverables/CVO_VERDICT_DELL_CTO_WRITES_L4_L10_20261007.md`
@72e87b0e39) of this seat's ruling `CTO_RULINGS_FOR_THE_DELLS_20261007_0740Z.md` section 1. The verdict named two things owed; both land here.

- **C-ROLES amended in place.** For the projects placed on its box, a Dell's CTO lane (`1.0.0_SA_CTO~DELL1`, `1.0.0_SA_CTO~DELL2`) writes
  L2 to L4 and the L10 answers and signs the CTO never-widen halves. The laptop keeps what spans boxes or grants access: placement,
  `org/missions/SEQUENCE.yaml`, `org/ref/LIVE_ARMS.md`, roles and resource policies (C-ROLE-REQUEST), and any half that changes IAM.
- **The ratified-text half of a Dell-written PRD is signed by the CVO seated on that Dell.** Each Dell runs a `3.0.0_SA_CVO` session
  (reported by each Dell's fabric manager, relays 106033 and 106035). `python .tools/prd-signoff.py sign` on that box writes the
  sign-off file beside the PRD; both travel to the trunk on the Dell's published branch. So an ENDPOINT bump on a Dell is re-signed on
  the same box, and the task-order gate's LIMB 6 reads SIGNED there without a hop to the laptop. The laptop's `3.0.0_SA_CVO` signs
  for laptop-written PRDs only. UNMEASURED: that `prd-signoff.py` accepts the same base serial from a second box without a clash in
  the sign-off file; the first Dell sign is the read, and a refusal there comes back to this seat as a row.

A contract change under the ENDPOINT hash.

## ADDENDUM v0.13 (1.0.0_SA_CTO, 2026-10-07) -- C-NAMING: every new resource, on any box, is builder-named and registered. Contract only

Andrew-direct ~08:1xZ at the `1.0.0_SA_CTO` terminal, VERBATIM: "ALso make sure that everyone is being very diligence with LGIC_NAMING for any new resource creation, everything should be registered as well, i believe there is some index we have for this ecxact purpose."
Record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_081xZ_LGIC_NAMING_DILIGENCE_AND_REGISTRATION_FOR_EVERY_NEW_RESOURCE.md`.

- **C-NAMING (new contract; owner this project for the four-box rule; the vocabulary and builders stay LGIC_NAMING's and LGIC_ENFORCE's).**
  On the laptop, site Z, dell1 and dell2 alike: (1) a new AWS resource is created only by `.tools/safe-apply.sh` of a Terraform root,
  never by a CLI or SDK create call; (2) its name is `lib/opal_naming.py` `name()` output and every S3 address is `address()` output;
  (3) its row lands in `infra/logic/registry/resources.json` in the same commit as its Terraform; (4) a builder refusal is answered by
  the missing registry row, and on a Dell that row is asked of the laptop CTO when the scope or system does not exist yet.
- **What enforces it today:** `.tools/naming-apply-gate.py` inside `safe-apply.sh` refuses a badly named resource being ADDED (its plan
  mode). Clause (1) and clause (3) have no gate: the Dell create grant permits a create outside Terraform at the cloud, and no gate
  refuses an apply for a missing registry row.
- **Next issuance, two cells:** (a) one read at each round's close, by the round's COO: every resource the round created, against
  `resources.json`, N of N printed, a missing row filed as a row (a read at the drain, not a standing checker); (b) the missing-row
  refusal in the apply path, proposed to LGIC_ENFORCE as its owner, since it is that project's gate.
- **UNMEASURED:** that both naming gates fire on dell1 and dell2. Each Dell's fabric manager runs one known-bad name through
  `naming-apply-gate.py` and reports the refusal line.

A contract change under the ENDPOINT hash.

## ADDENDUM v0.14 (1.0.0_SA_CTO, 2026-10-07) -- C-NAMING CORRECTED: what "registered" is; and the Dell Python environment. Contract only

**A correction of this seat's own v0.13.** v0.13 clause (3) said a new resource's row lands in
`infra/logic/registry/resources.json`. That file is not a list of resources. MEASURED by `0.9.0_WK_NFRA_CTLPLN~11`
(`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~11/PROPOSAL_MISSING_ROW_REFUSAL_FOR_LGIC_ENFORCE.md` @0a8a337aac,
rows NFRA_CTLPLN-W11-S1 and W11-S2) and READ by this seat in the file's own `_about`: each of its 465 rows fills a `{system}`
placeholder for a name whose own tokens resolve no system; 0 of 465 names grade CONFORMANT; and `lib/opal_naming.validate()` REFUSES a
row for a conformant name as redundant. That is the design of LGIC_ENFORCE ruling 97177, not a defect: a conformant name carries its
own registration in its tokens, checked against `systems.json`, `scopes.json` and `tiers.json`.

- **C-NAMING clause (3), replaced:** a new resource is REGISTERED when (i) it is declared in a Terraform root in the repository, in
  the commit that creates it; (ii) its name is builder output and grades CONFORMANT, so its system, scope and tier are rows of the
  registry; and (iii) it reads as declared, not drifted, in the cloud graph (`comp-find --corpus aws`, the `drift_class` of its node).
  A `resources.json` row is added ONLY for a name whose tokens resolve no system, and only if `validate()` accepts it.
- **The index Andrew's word points at is therefore two things the estate already has:** the registry's vocabulary files for WHAT a
  name may be, and the cloud graph for WHAT EXISTS and whether Terraform declares it. No third list is built.
- **The missing-row refusal of v0.13 is WITHDRAWN** as a proposal to LGIC_ENFORCE. A badly formed name is already refused at apply
  (the proposal's case C, measured). A well-formed, undeclared, running resource is found by clause (iii).
- **Round 4's cells, amended by their issuer:** CT-d-7 adds a `resources.json` row for a Dell resource name only where `validate()`
  accepts it and prints the validator's count; the round-close read (v0.13 cell a) reads each created resource's graph node and
  `drift_class` instead of a row.

**C-KIT-PYTHON (new contract).** A Dell's Python environment equals the laptop's for the packages the repository's tools and
shared modules import. Two measured gaps on 2026-10-07, both reported from the Dells: `pandas_market_calendars` is absent on both
(so `lib/trading_calendar.py` miscounts before 2024), and `ruff` was absent on dell1, where a worker installed it from PyPI with no
word of Andrew's (row MDPF_SECCLASS-S49). The kit carries the packages FROM THE LAPTOP over the tailnet, as files already on Opal's
own boxes; nothing is fetched from PyPI by a Dell. Cell for round 4: the list of third-party imports of `.tools/` and `lib/` against
each Dell's installed set, N of N printed, and the transfer of what is missing.

A contract change under the ENDPOINT hash.

## ADDENDUM v0.15 (1.0.0_SA_CTO, 2026-10-07) -- an ENDPOINT change on Andrew's word: package intake and download tiers. FWD-15 to FWD-19; contract C-INTAKE

**Words (verbatim in their own records):** dell2 terminal ~13:39Z (record @50df0c2e97, branch `q/dell2/record-download-tiers/r1`);
dell1 terminal ~14:0xZ (record @9e5f28e155, branch `q/dell1/record-package-intake/r1`), "all work that should be researched,
designed, and folded in to NFRA_CTLPLN". **Brief:** `docs/briefs/nfra-ctlpln-package-intake-and-download-tiers-brief-20261007.md`
@adc8997f1b (`4.0.0_SA_CRO`), read in Parts I, II, III and V. Its ten outcomes are carried as five: O1+O2+O3 -> FWD-16; O4 ->
FWD-17; O5+O6+O7 -> FWD-18; O8+O10 -> FWD-19; the thread -> FWD-15. **O9** (every box runs the same version of each tool the
gates call) is already contract C-KIT-PYTHON's and takes no new outcome.

**The thread of this addition (round 5 builds it; every later round enriches):** FWD-15 on `PyYAML==6.0.3` for one dell2 lane,
then the other 29 packages of the first batch by the same route
(`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~13/PYTHON_WHEELS_NEEDING_A_FETCH_FOR_CP314.md` @bd489b912b).

### Contract C-INTAKE

1. **What "checked" is.** The eight checks of the brief's Part V.1, in that order, each recorded as passed, failed or not
   applicable, with the brief's own "leaves" column written beside every delivery. Running the package on the laptop is NOT a
   check: the laptop holds Andrew's administrator sign-in. Check 8 (a person signs the batch) is `1.0.0_SA_CTO`'s.
2. **One file by exact name.** The laptop fetches one named file for one approved line; no dependency resolution. So the approved
   list is closed under dependencies BEFORE a batch is fetched (the brief's F12: 73 dependencies are not lines today).
3. **A holding place.** A fetched file waits in one folder on the laptop between fetched and checked; only a file whose record
   reads checked is ever sent.
4. **The approved list.** `requirements.txt` is generated with a do-not-hand-edit header (F2). Round 5's first cell decides, by
   measurement, how a reviewed addition and a regeneration stop overwriting each other; until it lands, no line is added by hand.
5. **The Dell's proof.** The laptop has no Python 3.14 (F13), so a delivered file is proven on the Dell: an install with no
   index, then an import, read back.
6. **No monitor.** FWD-19 is an answer on demand from a record written at the time of each fetch. Nothing is built that watches
   or notifies.

### The brief's six calls, ruled (each on the brief's own recommendation unless said)

- **A, which boxes the tiers bind:** the two Dells as receivers, and the laptop as the one box that fetches a package, through
  the checked route only. That is the scope of his words, which were spoken at the Dells about the Dells. Site Z, and the
  laptop's own seats as receivers, are NOT bound by this addendum; binding them is his word to give and is not inferred here.
- **B, programs the kit already carries:** red. They reach a Dell only from the laptop over the private network, as the kit does
  today. The automation browser download moves to that route or is dropped from the Dells.
- **C, what a Lambda bundles:** not this scope.
- **D, who approves:** `1.0.0_SA_CTO` approves a version change to a package already on the list; a NEW package name is
  approved by Andrew, once per name.
- **E, the website's packages:** as today's kit: the laptop packs the existing tree and sends it; a new one takes the same
  request and review.
- **F, running a package before a Dell does:** not for the first batch (all 30 are versions the laptop already runs). For a new
  name, yes, and only in a place that holds no sign-in; building that place is its own outcome when the first new name is asked.

An ENDPOINT change: the ratified-text half re-opens for `3.0.0_SA_CVO`. FWD-1 to FWD-14 are unchanged.

## ADDENDUM v0.16 (1.0.0_SA_CTO, 2026-10-07) -- an ENDPOINT change on Andrew's word: the tiers bind every box; a package is approved by the control plane, not by Andrew

**Word (verbatim):** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_151xZ_TIERS_BIND_EVERY_BOX_DELL1_PUSHES_DEV_PACKAGE_APPROVAL_BY_CRO_THEN_CTO.md`.

1. **Call A of v0.15 is RE-RULED: every box.** "Rec approved." on the card "Yes, every box, with the laptop as the one box that
   may fetch a package and only through the checked route." FWD-18's text reads "a box" where it read "a Dell", and its ACCEPT
   names site Z and the laptop. v0.15 held the tiers to the Dells because his words were spoken there; that limit is lifted by
   his word, not by inference.
2. **Call D of v0.15 is RE-RULED: Andrew approves no package name.** "The package approval needs to be handled automatically by
   an agent on the laptop/control plane fabric". C-INTAKE gains clause 7:
   **7. Review.** For every request, a new name or a version change alike, `4.0.0_SA_CRO` assesses legitimacy and stability
   (the eight checks' inputs that need no fetch, the project's history, its maintainers, how near its name sits to a popular
   one, what it pulls in) and delivers one recommendation, yes or no, with its evidence, as a file. `1.0.0_SA_CTO` decides,
   and on a yes runs the addition to the approved list by clause 4's route. Check 8 of clause 1 (a person signs the batch)
   is that same decision. The record FWD-16 promises names both seats and both files.
3. **Call F stands:** a new name is run before a Dell runs it only in a place that holds no sign-in; until that place exists,
   the CRO's recommendation on a new name says so and the CTO weighs it.

FWD-1 to FWD-15, FWD-17 and FWD-19 are unchanged. The ratified-text half is owed by `3.0.0_SA_CVO` against this version.

## ADDENDUM v0.17 (1.0.0_SA_CTO, 2026-10-07) -- an ENDPOINT change on Andrew's word: how each seat operates, and the inbound-work pipeline. FWD-20 to FWD-25; contract C-SEATS

**Word (verbatim and entire):** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_163xZ_FABRIC_ROLES_MSTR_CTO_COO_CVO_CRO_AND_THE_INBOUND_WORK_PIPELINE_INTO_NFRA_CTLPLN.md`
@df6d1ad20b. **Brief:** `docs/briefs/nfra-ctlpln-seat-roles-and-inbound-work-pipeline-brief-20261007.md` @779f5428bc
(`4.0.0_SA_CRO`), read in Parts I, II, III and V. Its ten outcomes are carried as six: the thread with O1, O2, O3 -> FWD-20;
O4 -> FWD-21; O5+O6 -> FWD-22; O7+O8 -> FWD-23; O9 -> FWD-24; O10 -> FWD-25.

**The thread of this addition:** FWD-20, one real Teams request taken the whole way on the default path. Most hops exist (brief
F2: the Teams agent already texts Andrew and routes his reply; `.tools/remote-job.py` and `/remote-drive` do the bid and the job).
The round that builds it runs them as one for the first time, with a recommendation in the text and a reviewer in the job.

### Contract C-SEATS

1. **One statement of each seat.** MSTR, CTO, COO, CVO, CRO: what each is and does, in Andrew's terms as tabled in his record,
   lives in one file that the launcher hands a seat at start. Skills and gates cite it; none restates it.
2. **Where each rule is held** (his three: launcher, skill, gate). A rule a tool can check is checked by a tool; the rest is told
   at start. The cell that writes clause 1 lists every rule with its holder across the three areas: how code moves, how cloud
   changes are made, how seats work.
3. **A fabric manager's record carries no project ruling.** Its acts are merges, pulls, pushes, integration, spawn, kill, unstick
   and the bid. A question of substance it receives is passed to its CTO, by a file.
4. **Open calls.** The CTO of a fabric holds one list of every open call on it. "Touches only its fabric" is measured, not judged:
   by the paths and risk class of the orders involved, the project's placement, and the cloud resources its Terraform root names;
   a shared bucket or a shared trunk touches every fabric.
5. **A cross-fabric call** goes CTO to its MSTR to the other fabric's MSTR to that CTO, as a file with an acknowledgement from
   the other side (sent is not read). It is closed on both boxes or on neither.
6. **A laptop seat's order from another box.** Its GO reaches the seat through the laptop's CTO (measured today: an order from
   dell2 reached no one, because a Dell cannot message a laptop seat and the manager is barred from that tier). The cell that
   builds clause 5 closes this route too, so it does not depend on one seat relaying.
7. **A reviewer per box** exists before any drive on that box is counted finished.
8. **An inbound job** is done by a seat spawned fresh for it and briefed from a file; the requester is told the outcome in the
   channel they asked in.

### The brief's six calls, ruled

- **A, the CRO's line:** as recommended. Research is owed for an operation of stakes class S3 or above
  (`org/tier0/STAKES_MATRIX.md`) or a task order classed WORLD. Below that, none. Both classes are already assigned to work.
- **B, the locked law text:** yes. One short edit to `CLAUDE.md` after clause 1's file exists, rules only, by this seat, with its
  three surfaces. It points at the file; it does not restate it.
- **C, when an inbound job starts:** as it does today, on Andrew's reply to the text. That is the existing behaviour and no gate
  is added. "At once" per kind of request is an enrichment, on his word.
- **D, where the dedicated inbound COO sits:** on a Dell. Which Dell is the bid's answer per job, not a rule.
- **E, reviewers:** one per box now; a macro reviewer is the box's CTO's call where one reviewer is the bottleneck.
- **F, reading mail for requests:** NOT built in this addendum. Reading Outlook content with a model is a new use of a vendor
  that no word of his names yet; the Teams path stays as it is. It enters when he words it.

### Two corrections taken from `3.0.0_SA_CVO`'s review of v0.16 (@c9ef12c19e)

FWD-18's DONE WHEN now names a Dell and site Z, as its headline and ACCEPT already did. FWD-16's SOURCE now quotes his words
on who decides instead of restating them.

An ENDPOINT change: the ratified-text half re-opens for `3.0.0_SA_CVO`. FWD-1 to FWD-15, FWD-17 and FWD-19 are unchanged.

## ADDENDUM v0.18 (1.0.0_SA_CTO, 2026-10-07) -- Andrew's twelve answers of ~18:3xZ: mail for requests, the installer, vendor calls from the Dells, the law line; FWD-22's ACCEPT corrected

**Word (verbatim and entire):** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_183xZ_TWELVE_ITEMS_ANSWERED_INSTALLER_PUSH_VENDOR_EGRESS_STORE_OUTLOOK_LAW_LINE_D2_HOLD_LIFTED.md`.

1. **Call F of v0.17 is RE-RULED: mail IS read for work requests.** "Yes, I want this." C-SEATS gains clause 9:
   **9. Mail.** Only his own mailbox, through the gateway. A message is considered ONLY when both hold: its sender's domain is one
   of the five he named (Cottonwood, Inflection, 49 Financial, Alongside, and Opal for internal), each domain string read from
   the estate's firm records and never typed; and its body names "Andrew". A message failing either test is not passed to any
   model. FWD-20's thread stays the Teams request; mail is its first enrichment.
2. **C-INTAKE, the installer.** "The installer can be included in requirements, let them have it/download it." The Python 3.12
   installer is admitted by his word as an exception to the red tier. It is listed beside the requirements with its exact file
   name and published hash; a box takes it only when its signature reads valid and its hash equals the listed one. Running it
   needs elevation, which he does himself. With 3.12 on a Dell, every compiled package is re-packed offline from the laptop and
   the fetch batch of v0.16 shrinks to what has no copy on any Opal box.
3. **C-INTAKE, vendor calls.** "Vendor egress does not count as raw internet access; those are protected channels. The Dell Boxes
   have vendor egress as needed." A vendor call is not the red tier, and the Dell boxes may make one where their work needs it.
   This is his word for the Dells. The laptop and site Z keep the per-use rule until he says otherwise for them.
4. **Call B of v0.17 is closed on his express order:** "Sure but keep it light and to the point". CLAUDE.md rule 32 is that line;
   it points here and restates nothing else. The substance is built in launchers, loops and skills (clauses 1 and 2).
5. **FWD-22's ACCEPT** no longer says a one-box decision "never reaches Andrew". His word was that the lead "can adjudicate";
   an act only he can do still reaches him.

An ENDPOINT change (FWD-22's ACCEPT): the ratified-text half re-opens for `3.0.0_SA_CVO`. All other outcomes are unchanged.

## ADDENDUM v0.19 (1.0.0_SA_CTO, 2026-10-07) -- an ENDPOINT change on Andrew's word: the voice file. FWD-26

Andrew-direct ~21:4xZ at the `2.0.0_SA_COO~R` terminal, recorded verbatim by that seat at
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261007_214xZ_COO_R_INBOUND_FOR_BOTH_TEAMS_AND_OUTLOOK_AND_AN_ANDREW_VOICE_MD.md`
(@4f53112d76): "Yeah i need it for both teams and outlook, i believe i offered a spec/concept for how it would work for outlook.
Also i need an andrew_voice.md used for anything that an agent would speak for, that uses representative emails or teams
messages or whatever as a reference for the given action."

1. **FWD-26 is new**, at the next unused id. It belongs to workstream INBOUND (`2.0.0_SA_COO~R`).
2. **C-SEATS clause 10, the voice file.** One file, `andrew_voice.md`, organised by the kind of act (a reply to a client's
   mail, a Teams reply, a Teams post, an End of Day post, and others as they arise), each with representative messages Andrew
   himself wrote. The messages come from his own mailbox and his own Teams, through the gateway, read only. Names are not
   wiped: his word at the `4.0.0_SA_CRO` terminal ~18:4xZ, "Names don't need to be wiped, nor should they be wiped for the
   Teams op", was given for the mail and Teams operation, and is read here as covering the file that operation drafts from
   (`3.0.0_SA_CVO` msg 106609 corrected the citation). `daily_reports/eod/VOICE.md`, which the End of Day post reads today, is not replaced by a
   cell's choice: the cell reads it, carries what it holds into the new file's End of Day section, and the reader of the old
   file moves to the new one in the same cell or stays where it is. The messages themselves are client mail, so they are NOT committed to
   the repository, whose origin is an outside host: the file with its messages lives in an Opal-owned home outside git, and
   the repository carries only its location and its section list. Which home is the cell's, said at the cut.
3. **What does not change.** Nothing goes out in his name without his approval: no mail is sent by an agent (a draft only),
   and nothing posts to Teams without his 1.
4. **FWD-20 and clause 9: Teams and mail in the same round.** His word is "both". Clause 9 already carries what he gave for
   mail at ~18:3xZ (his mailbox only; a sender from one of the five firms; his name in the body). Whether he meant more than
   that by "a spec/concept" is not known; the round is cut on clause 9 and a wider reading arrives as his word.

An ENDPOINT change (one outcome added): the ratified-text half re-opens for `3.0.0_SA_CVO`. All other outcomes are unchanged.

## ADDENDUM v0.20 (1.0.0_SA_CTO, 2026-10-08) -- Andrew lifts four Dell limits; the Dells run the heavy jobs. Contracts changed; no outcome added

Two Andrew-direct words at the `1.0.0_SA_CTO` terminal, recorded verbatim at
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_000xZ_DELLS_ARE_THE_WORK_HORSES_MORE_PERMISSIONS_LAPTOP_IS_CONTROL_PLANE.md`
(@b3ab2ba2b0, corrected @4f768037a7) and
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_004xZ_LIFT_FOUR_DELL_LIMITS_SECRETS_FIRM_DATA_RESOURCE_POLICIES_PUSH.md`
(@14a030c049): "Their entire point is to be work horses and laptop is control plane" and "lets start with lifting 1 2 3 6".

1. **C-ROLES.** A Dell project's run is made on its Dell. The laptop decides, signs and applies access; it hosts no Dell
   project's run. A run refused for access is answered by granting the access, not by moving the run.
2. **C-IDENTITY, what a Dell user may now do** (each an apply at the laptop under a CTO and COO pair):
   - read every vendor credential and every client-firm or custodian session in the secrets store. NOT a secret whose holder
     can act as Opal's own platform (signing keys, seeds, bearer tokens): those enter only by a refused run, named;
   - dell1 is admitted to the three firm-data fences in full, as dell2 is (a read AND write reach; deletes stay denied);
   - the Deny on resource-policy actions comes off the Dell group. His earlier "For now, laptop should admin" is reversed by
     his own word for the Dells.
   NOT changed: a Dell creates no IAM role or policy ("they shouldnt need to create or touch IAMs"); the routes Deny stays; the
   download tiers of C-INTAKE stay.
3. **C-QUEUE and C-PUSH-RULE.** Each Dell's own fabric manager pushes its box's work to the shared branch: fetch, merge under
   the merge guard, push, never a rebase. The laptop's fabric manager is no longer the only pusher and merges a Dell's queue
   branch only when asked. MEASURED: the push gate already admitted `0.0.0_AB_MSTR~DELL1` and `~DELL2`; dell1 pushed twice on
   2026-10-08 (`5cbb530eb6`, `bfa7299c23`).
4. **Standing class.** An access refusal a Dell seat meets is reported by action and resource name the same hour, and granted
   the same day UNLESS it is one of clause 2's "NOT changed" lines (IAM creation, routes, downloads), which stay refused
   (corrected on `3.0.0_SA_CVO` msg 106701: the first wording read inverted).
5. **Reported to this seat, not approved by it** (his 19:0xZ word of 2026-10-07): a Dell's push, deploy or resource-policy change
   is told to the laptop; the laptop steps in on an open call, an overlap between boxes, or a deploy that could upset another box.

6. **A Dell's push never deploys another box's change** (`3.0.0_SA_CVO` msg 106701). The pre-push deploy gate reads every
   commit in the push, including commits another box wrote. A Dell's fabric manager pushes with a deploy ceiling of zero
   unless every deploy-scope file in the push belongs to an order of its own box, under that order's own pair. A deploy-scope
   file from another box in the push is published and not deployed; its deploy is its own box's order.
7. **Interim, stated as such:** clause 2's carve-out of signing keys, seeds and bearer tokens is narrower than item 1 as he
   lifted it, and the full grant to dell1 adds a write reach where item 2 was worded as a read. Both were told to him in those
   words the same hour; neither is widened or narrowed by a seat until he answers.

Contracts change and no outcome does: the ratified-text half re-opens for `3.0.0_SA_CVO` on the CONTRACTS section.

## ADDENDUM v0.21 (1.0.0_SA_CTO, 2026-10-08) -- FWD-20, FWD-26 and C-SEATS clauses 8-10 MOVE to COMM_ASSIST

Andrew ratified macro COMM for D9 (~19:2xZ, "2.) Yes agreed."; MACROS.yaml @0dcb083716) for "the teams and outlook, uh, Kimmy
agent and how that is routed to me and all processes associated with cues and communications" (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_184xZ_FIVE_POINTS_KIMMY_EFFICIENCY_ALYSSA_MCPORTAL_OPEN_CALLS_AGGREGATE.md`).
COMM_ASSIST was registered @b0a34bddfb.

- **FWD-20 and FWD-26 are owned and graded by COMM_ASSIST** from this version, as its FWD-1 and FWD-2, ACCEPT lines verbatim
  (`org/missions/D9/COMM/COMM_ASSIST/prd/COMM_ASSIST_PRD.md` v0.2). Their cards stay above, unchanged, so every citation of
  FWD-20 and FWD-26 still resolves; this PRD no longer grades them and no NFRA_CTLPLN round cuts a cell for them.
- **C-SEATS clauses 8, 9 and 10 are owned by COMM_ASSIST** as C-JOB, C-MAIL and C-VOICE, verbatim. Clauses 1-7 stay here.
- **Workstream INBOUND closes into COMM_ASSIST**; its history (rounds 1-7, its rows and grades) stays in this tree. Lane
  `2.0.0_SA_COO~R` moves with it.
- Only the brief half changes in substance for this project; the ENDPOINT bytes of FWD-20 and FWD-26 are unchanged. Raised by
  3.0.0_SA_CVO's L4-R review of COMM_ASSIST v0.1, finding 6.

## ADDENDUM v0.22 (1.0.0_SA_CTO, 2026-10-09 ~06:3xZ) -- an ENDPOINT change on Andrew's words: FWD-1, FWD-4, FWD-5 and FWD-6 re-based on the per-box trunk and the push law

**Why (L10 re-entry, step F0: the outcomes were WRONG, so they are amended in place and keep their ids).** Three things Andrew ordered
since v0.21 changed the path these four outcomes describe:
- the per-box branches, each box pushing `box/<box>` and `0.0.0_AB_MSTR` integrating `CLOUD` by `.tools/box-sync.sh` (his word recorded
  in `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_153xZ_TWO_PRIORITIES_GITOPS_AND_PROCESS_GC.md`; law @538f0f51a7);
- deploys firing on the authoring box's own push (B2, same record);
- the push law ("pushes should not require my approval ... aside from portal PROD, and only if it is touching a client-facing page",
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_044xZ_PUSHES_NEED_NO_APPROVAL_EXCEPT_CLIENT_FACING_PROD.md`, law
  d92d08c448).
Site Z no longer merges or pushes for the cluster, and a routine push waits for no one. Nothing is retired. FWD-6 is not obsolete: its
promise (routine work moves alone; only what Andrew reserved waits for him) stands, re-pointed at what he reserved.
**The ratified-text half is re-owed** (`3.0.0_SA_CVO`, L4-R), because this changes the ENDPOINT.

**Placement (on `3.0.0_SA_CVO`'s v0.22 review @33879bb6bf, REFUSED on placement only):** the four re-based cards below
REPLACE FWD-1, FWD-4, FWD-5 and FWD-6 IN PLACE in the ENDPOINT section above, so the ratified half binds the new text. This
addendum keeps the why and the record of the change.


```
  FWD-1  One round of one real project is issued and worked on dell1, reaches the shared trunk
         through dell1's own branch and the laptop's integrator, and is graded on the laptop -- and
         Andrew can see how long each step took
         DONE WHEN  EXERCISED -- one real round, traced from its PRD on the laptop to its grade
         ACCEPT     a real project's round is planned on the laptop, worked and finished on dell1,
                    pushed by dell1 to its own branch, merged into the shared trunk by the laptop's
                    integrator, and graded on the laptop. Nobody on dell1 writes the shared trunk.
                    Andrew reads afterwards when each step began and ended. A step done by hand on
                    another box, or a practice round, fails it
         SOURCE     brief PART I, the candidate thread; re-based v0.22

  FWD-4  A finished round from any working box reaches the shared trunk without that box writing
         the trunk, and no lane falls more than one round behind
         DONE WHEN  EXERCISED -- two boxes' rounds pushed to their own branches and merged by the
                    integrator
         ACCEPT     each working box pushes its finished round to its own branch; the laptop's
                    integrator merges every box's branch into the shared trunk on its schedule, and no
                    box writes the shared trunk itself. No box holds more than one unpushed round per
                    lane
         SOURCE     brief O3; re-based v0.22

  FWD-5  Pushing work from any box never puts anything into production except what a signed change
         names for that exact build
         DONE WHEN  EXERCISED -- a box push carrying a pipeline script no open change names, and
                    nothing deployed
         ACCEPT     when a box pushes its own branch, only a script that an open signed change names,
                    at the exact version it signed, goes live; any other script in the push is held
                    and written down, and the push still goes through. Merging the shared trunk
                    deploys nothing
         SOURCE     brief O4; re-based v0.22 (the box-push deploy and the pinned-build rule)

  FWD-6  Routine work reaches the shared trunk with no one's word, and only a production release of a
         page clients can open waits for Andrew
         DONE WHEN  EXERCISED -- one routine push and merge with no one asked, and one release of a
                    client-facing page held until his word
         ACCEPT     a push of any box's work, and its merge into the shared trunk, happen without
                    anyone at a terminal; a production release that changes a page a partner firm or
                    client can open waits until Andrew says so, and a release of a staff-only page
                    does not
         SOURCE     brief O5; re-based v0.22 on the push law
```


## ADDENDUM v0.23 (1.0.0_SA_CTO, 2026-10-12 ~02:0xZ) -- two outcomes added on Andrew's words and one security ruling: FWD-27 (SSH over the tailnet), FWD-28 (caller-tier fence on two portal functions)

- ENDPOINT change: FWD-27 and FWD-28 appended at the next unused ids; nothing renumbered. The ratified-text half re-signs
  (`3.0.0_SA_CVO~L`). Records: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261012_015xZ_SSH_OVER_TAILNET_EXECUTE_COO_C.md`
  (the elevation fact and the per-box shape) and `CTO_RULINGS_POST_OFFLINE_FIVE_CROSSBOX_CALLS_AND_TWO_SECURITY_CARRIES_20261012.md`
  section 3 (why the proxy and content api land here: both predate the tree and no project owns them).
- `2.0.0_SA_COO~C` cuts FWD-27 (one packaging cell, three per-box cells) and FWD-28 (one cell) in its issuance, order its own;
  E1-E8 unchanged. Workers haiku, high effort (treatment device). No alert, monitor or timeout is built by either outcome.

## ADDENDUM v0.24 (1.0.0_SA_CTO, 2026-10-12 ~03:0xZ) -- FWD-28 re-worded on COO~C's measurement (row W62-S1): fence by route class, not by tier alone

- ENDPOINT change on one outcome: FWD-28's ACCEPT now classes the 11 data-proxy routes by whether a FIRM_ALLOWED_PATHS page
  calls them; partner-page routes admit the firms that source admits (firmId), the rest admit tier internal only; the content
  GET is not fenced. Nothing a partner login sees today changes, so no client-facing release waits on Andrew; the apply is a
  narrowing of what strangers can read, not of what partners can. `3.0.0_SA_CVO~L` re-signs the ratified half (ENDPOINT hash).
- CT-u-7 (COO~C, staged) is cut against this wording: the route census with its denominator (11) and the two token proofs per
  class are its criteria.

## ADDENDUM v0.25 (1.0.0_SA_CTO, 2026-10-12 ~03:5xZ) -- FWD-28: the denominator is 41 routes, not 11; class (i) is 2 routes; the firm check waits on an opal_naming registry row (rule 30), the 39 class-(ii) routes fence now

- COO~C's CT-u-6 census (DATA_PROXY_ROUTE_CLASS_CENSUS.md): 41 routes; 2 called by a FIRM_ALLOWED_PATHS page (POST
  /sentiment/keyword-intelligence, GET /aum/metrics; firm union all four); 39 class (ii). The commit-time naming gate (row
  W62-S6, BLOCKING) refuses the generated firm-set module because its four firm tokens are not `opal_naming` output.
- RULED (msg 108443 option 3, then 1): the 39 fence now under the pair; the 2 stay open to every verified login exactly as
  today; the firm check for the 2 lands when the file is registered as an `opal_naming` target under `infra/logic/registry/`
  (LGIC owner, laptop fabric) -- a registry row, never a hand-typed name and never an R20 departure for this. ENDPOINT wording
  changed in place (denominator and the staged firm check); `3.0.0_SA_CVO~L` re-signs the ratified half.

## ADDENDUM v0.26 (1.0.0_SA_CTO, 2026-10-12 ~14:2xZ) -- FWD-28: a staff `Dev` login is admitted beside `tier internal` (dell1 D1-S9; cell CT-aa-3)

- Measured 14:1xZ on the users table: 6 PROFILE rows carry `userType Dev`; 3 of them a tier other than `internal`, all
  `firmId opal-capital`, role admin -- staff/dev identities the authorizer already grants ALL. The tier-only helper refused them.
- ENDPOINT wording: class (ii) now reads "tier internal or userType Dev" (exact match on both). No user record is edited for a
  fence. CT-aa-3 (helper + tests: a Dev/advisor token 200 on class (ii), a partner advisor token still 403) and CT-aa-4 (the apply,
  fourth pair, CT-w-10 shape, seat ~U7). `3.0.0_SA_CVO~L` re-signs the ratified half (wording under the ENDPOINT hash).

## ADDENDUM v0.27 (1.0.0_SA_CTO, 2026-10-12 ~15:3xZ) -- the v0.26 premise does not hold (row S9115): the authorizer derives tier from the firm, so staff Dev logins already read `internal`

- Measured by `2.0.0_SA_COO~C` at the CT-aa-4 apply: `auth-handler jwt.ts` derives the token's `tier` from `firmId` (opal-capital
  -> internal), so the three Dev rows with a non-internal ROW tier log in as tier internal (the walker: 200 before and after the
  clause). R3 is NOT-RUN by construction -- no measured login exercises the clause; it would admit only a Dev token on a
  non-internal firm, which PRE-1 refuses and which no row holds (0 of 6).
- RULED: the code stays as applied (a fifth apply to remove a no-op clause buys nothing); the ENDPOINT wording returns to "tier
  internal", naming the derivation, and the clause is recorded as defence-in-depth with R3 unproven. The standing invariant,
  checked by PRE-1 whenever this function is next applied: no `userType Dev` row on a non-internal firm. dell1's research-pull
  fence (D1-S9) keeps its tier-only shape; its premise (staff 403) was false by this measurement.
- `3.0.0_SA_CVO~L` re-signs the ratified half (wording under the ENDPOINT hash).

## ADDENDUM v0.28 (1.0.0_SA_CTO, 2026-10-12 ~15:3xZ) -- the CVO's refusal of v0.27 (review @67b765298a) is right: the Dev clause is a widening, not defence-in-depth

- The clause's only reachable effect is to admit a Dev token on a non-Opal firm (tier is derived from the firm). RULED (b): the
  text now states exactly what the applied code does and names it a widening; cell CT-aa-5 removes the clause (`tier ==
  'internal'` only) at the next apply of this function, under a pair in the CT-w-10 shape, in round 11; "defence-in-depth" is
  struck. Until CT-aa-5 lands, PRE-1's invariant (no `userType Dev` row on a non-internal firm) is the control, re-read at
  that apply. `3.0.0_SA_CVO~L` re-signs on this wording.

## ADDENDUM v0.29 (1.0.0_SA_CTO, 2026-10-13 ~14:2xZ) -- an ENDPOINT change on Andrew's words of ~14:0xZ: FWD-27 and FWD-14 bound to the tailnet from every device he works from; FWD-9 PARKED; FWD-13 as written DROPPED and its bid re-scoped to ad hoc work under COMM_ASSIST; FWD-11 kept

Andrew-direct 2026-10-13 ~14:0xZ at the `4.0.0_SA_CRO` terminal, record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261013_140xZ_FOUR_OPEN_CALLS_ANSWERED_DEVPLN_TAILNET_SSH_BDFEE_CTLPLN_SCOPE.md`
@90867982ed, answering the CRO's four cards and the CVO's 2026-10-13 re-grade (@69e690cebf: FWD-9, FWD-11, FWD-13 NOT SERVED, no
order ever named them). His words are quoted on the cards and in the record; nothing here paraphrases the operative sentences.

- **FWD-27 amended in place (ENDPOINT change).** The source devices are the tailnet devices Andrew works from, which he named
  "rc", "muse" and "cloud-local" (the laptop); the laptop is a target too ("'muse' also needs to be able to remote into laptop").
  The bound is the tailnet: "no external ssh available nor any external rdp available (aside from IT services like splashtop)".
  The earlier (a)/(b) offer is withdrawn; neither was his answer. Measured input taken into the ACCEPT from `0.0.0_AB_MSTR`
  (msg 108757, read on the laptop ~00:5xZ): the laptop's only interactive account is an Entra account that sshd 9.5p2 cannot
  resolve (plain names log "Invalid user"; `azuread\` forms reset the connection); muse's key already sits in the laptop's
  `administrators_authorized_keys`, and muse's key logins to dell1, dell2 and sitez already answer. RULED: the laptop limb lands
  key logins on a local administrator account made for them; whether Intune strips its Administrators membership at policy
  sync is UNREAD (MSTR could not read the policy) and is the cell's first read after one sync, recorded either way. Creating
  that account and enabling sshd are elevated runs, Andrew's one line each, as the card already says; the keys of rc and the
  laptop are his to place, so FWD-27's gate narrows from "Andrew's public keys" to "rc's key, the laptop's key, and the two
  elevated lines per box". `2.0.0_SA_COO~C` re-cuts the FWD-27 cells in round 12 on this card: one packaging cell, four per-box
  cells (the laptop's carrying the local-account step), the refusal arm from a non-tailnet address on every box.
- **FWD-14 amended in place (ENDPOINT change).** "rc" into the laptop by remote desktop stays as it is; no remote desktop
  answers from outside the tailnet, Splashtop and the IT services he names excepted; the DONE WHEN gains the refused attempt.
  C-RDP's firewall ruling (3389 scoped to 100.64.0.0/10) is now the ENDPOINT's own bound, not a narrower default.
- **FWD-9 PARKED on his word ("park FWD-9").** No round cuts a cell for it; C-LEASE's text stays; its grade reads PARKED, and it
  counts neither REALIZED nor NOT SERVED in a round analysis until he un-parks it. Scarce accounts keep their current homes.
- **FWD-13 as written DROPPED ("drop FWD-13 as written"), its bid RE-SCOPED.** His clarification, verbatim: "The 'bid' is not for
  active registered projects, it is for ad hoc bug fixes and etc that come in over teams/outlook via the COMMS_ASSIST channel,
  which needs to be approved at my discretion over that COMMS_ASSIST channel." So a registered project never moves between
  boxes by bid; the bid places ad hoc work that arrives through COMM_ASSIST, and its placement is approved by Andrew over that
  channel. That outcome belongs to COMM_ASSIST (site Z, `1.0.0_SA_CTO~Z`), the way FWD-20 and FWD-26 moved in v0.21: the FWD-13
  card stays above so every citation resolves, this PRD no longer grades it, C-BID's "the laptop's fabric manager awards moves"
  is struck in substance, and `1.0.0_SA_CTO~Z` appends the ad hoc-placement outcome to COMM_ASSIST's PRD at its next unused id
  on this record (relayed via `0.0.0_AB_MSTR`). `remote-job.py`'s bid stays the mechanism for the ad hoc award (its devices come
  from the register, C-REGISTRY).
- **FWD-11 kept** as written; it joins the round-12 enrichment list behind cell 1 (the Dell grants, ruling @1161dc05fc).
- Header bumped to v0.29. ENDPOINT bytes changed on FWD-14 and FWD-27: the ratified-text half re-signs (`3.0.0_SA_CVO~L`); the
  brief half is the CRO's and unchanged. Andrew's first answer (NFRA_DEVPLN as its own laptop project; "CTLPLN is getting too
  large") touches this PRD's scope only by subtraction: the per-box portal DEV approval work is NOT a CTLPLN outcome, and his
  later ask, an analysis of why CTLPLN work on the laptop "has completely drawn to a close", is owed by this seat after the
  calls are addressed.

## ADDENDUM v0.30 (1.0.0_SA_CTO, 2026-10-13 ~14:5xZ) -- Andrew's later word of ~14:3xZ at the COO~C terminal: FWD-9's park is LIFTED for one deliberate exercise; FWD-11 the same; S9112 is a seat order, not his act; FWD-27 measured; the firmAccess carrier reaches PROD alone. No ENDPOINT byte changes

Record `org/tier1_exec/2.0.0_SA_COO~C/deliverables/ANDREW_DIRECT_20261013_143xZ_NFRA_CTLPLN_ROUND12_CALLS_ANSWERED.md` @a7d5d7955c.
His words there, VERBATIM: "1.) Yes sure. 2.) Rec approved. ... for FWD-27, check that this is not already done as I may have done it
across all boxes (check this box first, we can have MSTR issue an order for the other managers to check their respective boxes). ...
Row S9112 this can be done programmatically, i shouldnt need to be involved directly."

- **FWD-9 and FWD-11: one deliberate dell1 outage each, YES.** Card 1 at the COO~C terminal asked whether one Dell may be taken
  offline on purpose, once for FWD-9 and once for FWD-11; "Yes sure" is his answer, at most 15 minutes each, dell1, its manager
  parks the seats first, a time announced in advance. This is LATER than the ~14:0xZ "park FWD-9" at the CRO terminal (v0.29), and
  it names FWD-9 by id, so FWD-9's PARK is lifted for exactly that exercise: round 12 may cut the two outage cells; no other FWD-9
  work (the lease register, C-LEASE) is un-parked by it. FWD-11 was never parked. Both cards are byte-unchanged.
- **S9112 (the proxy log purge and the refresh-token invalidation) leaves the Andrew act list.** His sentence is the confirmation
  the deletion needed; it becomes a round-12 order to `0.7.0_AE_CloudOps~U7` with the purge's blast radius named in the order (the
  log group, the event window, the token rows), never wider.
- **FWD-27, measured at 14:4xZ by COO~C** (`.tools/ssh-tailnet-verify.py`): all four boxes answer port 22 and still advertise
  password login; the laptop's firewall half is done, `-DisablePassword` applied nowhere. His ask, "check that this is not already
  done ... check this box first", is answered: the laptop is half done, the other three are each their manager's read, ordered
  through `0.0.0_AB_MSTR`. The v0.29 cells stand; the per-box cell's first step is that read.
- **Card 2, the `firmAccess.ts` carrier `53506d49`:** cherry-picked alone onto portal PROD by a DT through `/prod-deploy`, no
  whole-DEV promote. For NFRA_DEVPLN FWD-6 this one commit leaves the backlog by Andrew's word rather than by the settlement.
- No outcome card changed; the ratified half owed from v0.29 is unchanged by this addendum. Header stays v0.30 for citation.

## ADDENDUM v0.31 (1.0.0_SA_CTO, 2026-10-15 ~12:3xZ) -- an ENDPOINT change on Andrew's word of 2026-10-13 ~16:5xZ: FWD-10's refusal arm re-worded to the three kept refusals; C-IDENTITY amended

On the CVO's re-grade `org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_CTLPLN_FWD_REGRADE_20261015.md` @e3297f2394, finding 1. Record
of his word: `org/tier1_exec/2.0.0_SA_COO~C/deliverables/ANDREW_DIRECT_20261013_165xZ_DELL_USERS_ADMIN_GROUP_KEEP_THREE_DENIES.md`.
VERBATIM: "Sure let's do rec b". Rec (b) was to join the admin group and keep three denies: no CloudTrail writes, no production S3
deletes, and no table or database deletes.

- **FWD-10 was WRONG as written and is amended in place, keeping its id.** Its "can never change who has access" arm described a
  deny that Andrew withdrew on 10-13. CloudTrail shows all 34 Dell IAM writes since 10-11 succeeded. The arm now names the three
  kept refusals: the audit trail, production data deletes, and table and database deletes. The DONE WHEN is re-tested, not
  inherited:
  - the deploy arm is unchanged;
  - the refusal arm is one production-data delete, refused (the CVO reads this as already exercised), plus one audit-trail write,
    refused (not yet exercised).
- **What the project no longer promises:** that a Dell cannot change who has access to the cloud. That promise left on Andrew's
  10-13 word, not on this seat's.
- **C-IDENTITY was amended in place** (the v0.31 sentence in its row).
- **Sign-off:** an ENDPOINT change, so the CVO re-signs the ratified-text half. The brief half is unchanged.

Rulings on the re-grade's other findings. None of them changes an ENDPOINT byte.
- **FWD-3, the managers acknowledge.** The ACCEPT line "no other seat talks across boxes" stands. The round-19 FWD-3 cell is
  driven by the managers: each crossbox acknowledgement is run by the receiving box's manager seat, never by a worker. A worker
  read relayed by its manager does not meet the outcome.
- **FWD-12: where f411 and c397 were answered.** Both are dell1 client-facing portal approvals. Andrew approved both on 2026-10-15
  ~01:xxZ, and both closed as "approved by andrew". The record is
  `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261015_01xxZ_COO_D1_TREND_LOOKS_GOOD_CUSTOM_ROLLFORWARD_THEN_PROD.md`.
  They are Andrew's to answer by law (a client-facing page), so no seat answered them. The CVO grades the clause on this.
- **FWD-21: the U7 respawn does not count.** It was asked for. Round 19 cuts one cell: read site Z's broker for any ask before its
  23:32Z respawns. If there was none, those respawns are the exercise, read with that box's audit and one MSTR day record. If there
  was an ask, the cell drives an unasked respawn on a box nobody is watching.
- **The stray committer `t <a@b.c>` on 552e0e03ad** goes to the round-19 hygiene batch as an investigation row for the integrator.
  It is not a cell.
