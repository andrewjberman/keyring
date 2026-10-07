# L1 BRIEF -- what each seat does on a fabric, and how work that arrives by Teams or Outlook gets done

**Author:** `4.0.0_SA_CRO` (Chief Research Officer), 2026-10-07. **Mode:** NEW scope, added to a project in flight.
**Project:** NFRA_CTLPLN (the four-box control plane, directive D0). An ADDITION to it, on Andrew's word "I want all of
this folded in to NFRA_CTLPLN". After this brief: `1.0.0_SA_CTO`'s PRD addendum (new outcomes from FWD-20), then
`2.0.0_SA_COO~C` cuts. **Asked by:** `1.0.0_SA_CTO` msg 106411.
**Consumer:** `/endpoint --forward` at L2.

**Andrew's words, VERBATIM AND ENTIRE**, are in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_163xZ_FABRIC_ROLES_MSTR_CTO_COO_CVO_CRO_AND_THE_INBOUND_WORK_PIPELINE_INTO_NFRA_CTLPLN.md`
@df6d1ad20b (typed at the `1.0.0_SA_CTO` terminal, ~16:3xZ). The sentences this brief leans on are quoted where used.

Terms. A **fabric** is the set of agent seats on one box (the laptop, site Z, dell1, dell2). **MSTR** is a fabric's
manager seat (`0.0.0_AB_MSTR`). **CTO**, **COO**, **CVO**, **CRO** are the technology, operations, verification and
research seats. A **drive** is a skill a COO runs to move work: `/canonical-drive` (a project through the ten-step
workflow), `/closer-drive` (finishing a product while Andrew is present), `/remote-drive` (one small job from a
message). The **Kimi Teams agent** is the cloud service that reads Opal's Teams channel and answers there. The **Quo
line** is the text-message service Andrew receives texts on.

---

## PART I -- THE OUTCOME TERRITORY

### I.0 The candidate thread (one journey, end to end)

**Who:** one person at Opal who asks for a small piece of work in Teams, and Andrew.
**Journey, coarse grain:** one request, one box, the default path. The person asks in Teams. The Kimi agent recognises
it as a request for work. Andrew gets ONE text on the Quo line: what was asked and a recommendation. The job is offered
to the boxes; the box with the most room takes it; its manager spawns a FRESH operations seat, hands it a brief, and
that seat runs `/remote-drive`; a reviewer on that box grades the result; the person who asked is told it is done.
At no step does a fabric manager reason about the job itself, and at no step does Andrew read a channel to find it.

Most hops of this exist, the text to Andrew included (finding F2). The thread is the first time they are run as one,
with a recommendation in the text and a reviewer in the job.

### O1 -- Andrew learns of inbound work from one text, with a recommendation

"I will get the text at the Quo line from the Kimi agent with a recommendation if they identify that work is being
requested." He does not scan Teams or Outlook for requests.

### O2 -- A person who asks for work in Teams or Outlook has it taken up, and is told when it is done

They do not need to know which box did it or which seat. "that needs to be organized and tightened."

### O3 -- A fabric manager places an inbound job on the box with the most room

"They also need to have that functioning bid pipeline for pulling in work based on utilization." The placing is by
measured load. The manager routes the job and decides nothing about its content.

### O4 -- A fabric manager keeps its fabric running without being asked

"MSTR whole purpose is not business logic/project reasoning, they are infrastructure managers. They manage
merges/pulls/pushes/integrates across the fabric. They also can manage /unstick /mstr-spawn /mstr-kill to keep their
fabric running cleanly." A stuck seat is unstuck, a dead one replaced, branches integrated, by the manager, on every box.
A reader of its record finds no ruling on a project's substance.

### O5 -- A CTO holds every open call on its fabric and rules the ones that are its own

"They are responsible for accruing any and all /open-calls on their fabric. If the open call in question only pertains
to their fabric, does not interfere with any other projects resources or materials, they can adjudicate them." Andrew
is shown only the calls a CTO could not rule.

### O6 -- A call that touches another fabric is settled between the two fabrics, on the record

"if however there is an open call that touches multiple surfaces, they must have their MSTR reach out to the MSTR of
the relevant fabric and coordinate as needed." Someone on either box can read afterwards what was agreed and by whom.

### O7 -- Anyone can tell which drive a COO is in

"COOs are the workers, they either run /canonical-drive /closer-drive to proceed projects, running /remote-drive if a
one-off request comes in." A COO seat's record names its one drive, and a COO that is in none is visible as idle.

### O8 -- Every fabric has a reviewer, and no drive finishes ungraded

"CVO is dedicated reviewer in those drive processes so mandatory spawn on any fabric. If there are multiple projects
attached to one macro on a fabric, it is best practice to spawn a CVO specific to that macro, e.g. CVO~NFRA."

### O9 -- A CTO gets research on a risky operation when it is above a stated line, and not below it

"researching risky or otherwise unclear operations of meaningful [risk] at the behest of the fabric's CTO ... if the
project does not meet a meaningful quantified risk layer ... there is no need to bring them out." A CTO can tell from
the operation's class whether to ask, and the CRO can tell whether an ask was owed.

### O10 -- A new seat reads one place that says what it is, and the tools hold it to that

"We need to lock in these processes more formally, whether it takes place in launcher updates, skill updates/creation,
gates, etc., I want to make sure we cover both GitOps, AWS DevOps, and Agent Workflow Ops." A seat that starts on any
box is told its role by what launches it, and where a rule can be checked by a tool it is, across the three areas he
names: how code moves (GitOps), how cloud changes are made (AWS DevOps), and how seats work (agent workflow).

---

## PART II -- WHERE THE BOUNDARY SITS

### II.1 This scope OWNS

- The statement of each seat's role, in one place, and its enforcement where a tool can enforce it.
- The inbound pipeline's missing halves: the constant check for requests, the recommendation in the text to Andrew,
  the reviewer in the job, the dedicated COO, Outlook.
- The route for a call that crosses fabrics.
- The line above which a CTO asks the CRO.

### II.2 It RELIES ON and does not own

- **The Kimi Teams agent** (called LDO-001 in the estate; `data/transcripts/scripts/teams_chat/`,
  `infra/aws/terraform/transcripts/chat_assist.tf`): it already opens, offers and closes jobs. This scope extends what
  it watches and adds the text; it does not rebuild it.
- **`.tools/remote-job.py`, the `/remote-drive` skill and
  `org/tier1_exec/4.0.0_SA_CRO/deliverables/REMOTE_JOBS_PROTOCOL_20261002.md`**: the bid, award and close.
- **NFRA_CTLPLN's own contracts**: C-BID (FWD-13, a move placed by bid), C-ATTENTION (FWD-12, one decision list),
  C-ROLE-REQUEST. O3 and O5 extend them; they are not replaced.
- **NFRA_OPLGTW** (the Opal gateway, site Z): the only sanctioned read of Teams and Outlook.
- **The skills that already exist**: `/unstick`, `/mstr-spawn`, `/mstr-kill`, `/integrate`, `/agentbus`, `/govern`,
  `/open-calls` (with `--adjudicate`), `/self-drive`, the three drives.
- **`org/tier0/STAKES_MATRIX.md`** and the task-order `<risk>` class (finding F1).

### II.3 NOT this scope -- named so no decomposition re-opens it

- **The canonical workflow's limb owners.** Who writes a brief, an endpoint, a PRD, a decomposition and a grade is
  unchanged. The CTO's record of his word says the same.
- **The hard stops** of CLAUDE.md and the never-widen rule.
- **Who may push a shared branch.** His word says managers "manage merges/pulls/pushes"; which manager pushes which
  trunk, and on whose word, stays as `org/XXX.md` states it unless he changes it (call B).
- **The Ticket Center.** A request that arrives as a ticket is D7's. This scope is requests that arrive as messages.
- **The park-or-close list** of quiet projects.

---

## PART III -- THE QUALITATIVE BAR

No number here is a target.

- **O1.** For a real request, the text reaches him before he would have noticed it himself, and he can answer it
  without opening Teams.
- **O2.** The person who asked can say when their job was picked up and when it finished, from what they were told.
- **O3.** The box that took the job was the least loaded one by a measurement taken at the offer, and the manager's
  record contains no opinion about how to do the job.
- **O4.** A seat that hangs on a prompt on an unattended box is moving again without Andrew or another seat asking.
- **O5.** A call that touched only one fabric never reached Andrew as a card. It displaces today's shape, where a call
  reaches him from whichever terminal he happens to be at.
- **O6.** Neither fabric learns of the other's decision by finding its effect.
- **O7.** A person reading a box's seat list can name what each COO is doing without opening its log.
- **O8.** A drive's result is graded by a seat that did none of the work, on the box where the work was done.
- **O9.** The same operation put to two CTOs gets the same answer to "is the CRO owed here".
- **O10.** A seat that tries the act its role forbids is refused or flagged by a tool, not by another seat noticing.

---

## PART IV -- THE SUBSTRATE: what exists to build on

Measured 2026-10-07 ~17:1xZ at the laptop, working tree near `3c3e24417c`.

**F1. The "quantified risk layer" he refers to exists three times, and none of the three is named as the CRO's
line.** This is the index his word asks to be named.

| Index | Grain | Classes | Where | Who it binds today |
|---|---|---|---|---|
| The stakes matrix | one action | S0 to S4 (S3 = irreversible, resource-committing or external; S4 = governance) | `org/tier0/STAKES_MATRIX.md` v1.5, ratified by Andrew; six classification rules, "highest class binds" first | written for the fabric manager's autonomy; Andrew alone may edit it |
| The evidence law's risk class | one task order | `LOCAL`, `SERVED`, `WORLD` | CLAUDE.md rule 22; refused when absent by `.tools/to-pipeline-gate.py` gate (xii) | every task order |
| The danger map | one file | 1,662 scored nodes, read by `comp-pulse diff` before each commit | printed by `safe-commit.sh` | every commit |

The first is the one that classifies an OPERATION by how reversible and how visible it is, which is what his sentence
describes. The second is the one already stamped on work a CTO sees every day. Call A asks him which one is the line.

**F2. The inbound pipeline is half built, for Teams only.**
- Live in AWS: `teams-global-chat-assist-ingress-lambda` and `teams-global-chat-assist-handler-lambda`, both last
  changed 2026-10-04.
- On every box: `.tools/remote-job.py` (bid, accept, complete, fail, close, show; written 2026-10-02) and the
  `/remote-drive` skill. The skill's own text: the cloud side "opens the job on Andrew's `#dev`, offers it on the agent
  bus, picks the least-loaded available machine, talks to the requester, and closes the job"; the box's manager bids
  and spawns `2.0.0_SA_COO~<N>`; that COO traces, fixes, validates and reports; one job per machine at a time.
- **It already texts Andrew and acts on his reply.** `teams_chat/assist.py` `send_sms` sends through the AWS text
  service; `teams_chat/tenant.py` tags each text (a job, a drafted chat reply, an end-of-day update), keeps a list of
  "everything waiting on Andrew", and routes his texted answer (`send`, `drop`, `edit`) back to the tagged item. A job
  is opened with a brief and goes to `bidding`. So O1's text is not new machinery; what was NOT read is whether a text
  about requested work carries a RECOMMENDATION, which is what his sentence adds.
- NOT found: any read of Outlook for requests (0 matches for Outlook or a mail tool across `teams_chat/*.py`); a
  reviewer step in `/remote-drive` (0 matches for the reviewer seat or "review" in the skill); a COO dedicated to
  inbound work. Whether the agent checks "constantly" or only when addressed was not read.

**F3. "The manager reasons about no project" is already written three times, and binds by reading.** CLAUDE.md rule
27 ("`0.0.0_AB_MSTR` integrates and never works a project"); the workspace memory ("manages the fabric only, never
opines on project work, and unsticks a stuck seat without asking"); `org/XXX.md`'s shared-branch law. No tool refuses a
manager seat that rules on a project.

**F4. A CTO ruling its own fabric's calls exists in two narrower forms.** `/open-calls --adjudicate <PROJECT>`: one
project, past step 2, on two named triggers. `/self-drive`: an armed seat rules the calls found at each tick. His word
is wider than both: every open call on the fabric that touches only that fabric. Nothing gathers a fabric's calls into
one list on that fabric; NFRA_CTLPLN's FWD-12 gathers every BOX's calls on the laptop, which is a different list.

**F5. No route for a cross-fabric call was found.** The agent bus carries messages between boxes
(`/agentbus`); today's cross-box rulings went manager to manager as free text. No message kind, record or
acknowledgement for "a call that touches your fabric" exists.

**F6. One reviewer is live on the laptop; the other boxes were not read.** Live seats registered on the laptop at
17:1xZ: `0.0.0_AB_MSTR`, `1.0.0_SA_CTO`, `2.0.0_SA_COO~C`, `2.0.0_SA_COO~G`, `3.0.0_SA_CVO`, `4.0.0_SA_CRO`, and four
cloud-operations lanes. No macro-specific reviewer lane is live. A CTO record of today mentions the laptop's reviewer
reading on dell2's behalf. Whether dell1, dell2 and site Z each hold a reviewer was not measured from here.

**F7. The law files are locked, and his sentence does not name them.** `CLAUDE.md` and `org/XXX.md` take an edit only
on his express order, named in a record and passed to the commit (`.tools/git-hooks/law-lock-check.sh`). The stakes
matrix is his alone. He lists "launcher updates, skill updates/creation, gates". Whether the seat roles also go into
the law text is call B.

**F8. Two parts of the inbound pipeline are things the estate otherwise forbids, and he asks for them here.** A
service that constantly checks for requests and a text sent to him are a monitor and a notification; the standing
moratorium bars building either "unless Andrew explicitly asks". He asks. The ask covers the inbound check and the
text to him, and nothing wider.

**F9. Outside services in the path.** The Kimi model reads each candidate message, and a text service sends to his
line (the code calls AWS's own text service; "the Quo line" is his name for where he receives it, and how the two
connect was not read). The Teams agent already does both under earlier words of his, not re-read here. The new use is
mail content to the model.

**F10. Capacity for a dedicated COO.** The laptop's standing preference is at most three COO sessions; two are live.
On the Dells his word of this morning is "no lane cap".

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

Named, not ordered.

- The line of O9, in one of the indexes of F1 (call A).
- What "touches only its fabric" is measured by. Candidates already in the estate: a task order's `<paths>` and its
  `<risk>` class; a project's `placement`; the cloud resources its Terraform root names. A call about a shared bucket
  or a shared trunk touches every fabric.
- A record kind for a cross-fabric call, with an acknowledgement from the other side (CLAUDE.md rule 22a: sent is not
  read).
- Mail content read for requests passes through the gateway only, and client names in it do not reach a model
  unwiped unless he says so.
- A reviewer seat exists on a box before any drive on that box is counted finished.
- A fresh seat for each inbound job, briefed from a file, as he says: "spawned fresh, briefed, and run /remote-drive".
- Where enforcement lives for each role rule: the launcher (what a seat is told at start), a skill (what it does), or
  a gate (what is refused). His word names all three and chooses none.
- The thread's requester is told the outcome through the same channel they asked in.

**Calls for Andrew, each with a recommendation.**

- **A. Which index is the CRO's line, and where on it?** REC: either top band calls the CRO: an operation of stakes
  class S3 or above, or a task order classed `WORLD`. Below that, no CRO. Both are already assigned to work today,
  so no new classification is built.
- **B. Do the seat roles go into the locked law text (`CLAUDE.md`, `org/XXX.md`) as well as skills and gates?** REC:
  yes, as one short law edit after the PRD addendum, with the exact text put to you first. A role that lives only in
  a skill is not read by a seat that never loads that skill.
- **C. Does an inbound job start on your reply to the text, or at once?** REC: on your reply, for now. Your sentence
  says you get a recommendation; it does not say the job proceeds without you. Move to "at once" per kind of request
  once the recommendations have been right.
- **D. Where does the dedicated inbound COO sit?** REC: on a Dell, not the laptop. The laptop holds two of its three
  COO slots and is the control plane; the Dells have room and no lane cap.
- **E. One reviewer per box now, and a macro reviewer when?** REC: one per box now, on every box that runs a drive. A
  macro reviewer only where one box holds several projects of one macro and its reviewer is the bottleneck; that is a
  CTO's call per box, not a rule.
- **F. May mail be read for requests the way Teams is?** REC: yes, your own mailbox only, through the gateway, with
  the same name-wiping the commentary pipeline uses before any model sees the text.

---

## PART VI -- STATUS -- NOT OUTCOME-BEARING

Do not cut outcomes from this part. Measured 2026-10-07 ~17:1xZ at the laptop.

| Item | State |
|---|---|
| NFRA_CTLPLN | PRD v0.16, outcomes FWD-1 to FWD-19; round 4 in flight; next unused outcome id FWD-20 |
| Teams agent | two Lambdas live, last changed 2026-10-04 |
| Bid tool and `/remote-drive` | present on the trunk; `remote-job.py` last changed 2026-10-06 |
| Text to Andrew, and his texted reply routed back | present in the Teams agent (`send_sms`, tagged items); a recommendation in it: not read |
| Outlook read for requests | not found |
| Reviewer step inside `/remote-drive` | not found |
| A fabric-wide open-calls list held by a CTO | not found; two narrower forms exist (F4) |
| A cross-fabric call route | not found |
| Seat skills present | `/unstick`, `/mstr-spawn`, `/mstr-kill`, `/integrate`, `/agentbus`, `/govern`, `/remote-drive`, `/canonical-drive`, `/closer-drive`, `/open-calls`, `/self-drive` |
| Reviewer seats live | laptop: 1. Other boxes: not read |
| Risk indexes | three (F1); none named as the CRO's line |

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **Nothing on dell1, dell2 or site Z was measured**: which seats are live there, which skills are armed, whether a
  reviewer exists.
- **How the Teams agent decides a message is a request**, how often it checks, and what it sends today were not read.
- **That the bid pipeline works under load.** It is described by its skill and its tool; no job was run for this brief.
- **That the three risk indexes agree.** An S3 action inside a `SERVED` task order is possible; which governs is part
  of call A.
- **What "utilization" should measure.** The tool's own bid is the existing answer and was not evaluated.
- **Any design**: what the launcher says, which gate refuses what, the shape of the cross-fabric record.
- **How a text reaches the Quo line**, and that service's limits or cost.

---

## REFS TO CARRY

```
BRIEF PATH        docs/briefs/nfra-ctlpln-seat-roles-and-inbound-work-pipeline-brief-20261007.md
PROJECT           NFRA_CTLPLN (D0), an addition by PRD addendum; next unused outcome id FWD-20
EXISTING PRD      org/missions/D0/NFRA/NFRA_CTLPLN/prd/NFRA_CTLPLN_PRD.md v0.16 (C-BID, C-ATTENTION, FWD-12, FWD-13)
SIBLING SCOPES    package intake (FWD-15 to FWD-19); the Ticket Center (D7); NFRA_OPLGTW (the gateway); NFRA_TRNSPT's Teams agent
PRIOR ART         .tools/remote-job.py ; .claude/skills/remote-drive/SKILL.md
                  org/tier1_exec/4.0.0_SA_CRO/deliverables/REMOTE_JOBS_PROTOCOL_20261002.md
                  org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261002_020xZ_EOD_UPDATE_AUTOMATION.md
                  data/transcripts/scripts/teams_chat/ ; infra/aws/terraform/transcripts/chat_assist.tf
                  .claude/skills/{unstick,mstr-spawn,mstr-kill,integrate,agentbus,govern,open-calls,self-drive,
                    canonical-drive,closer-drive}/SKILL.md
                  org/tier0/STAKES_MATRIX.md v1.5 ; CLAUDE.md rule 22 ; .tools/to-pipeline-gate.py gate (xii) ; comp-pulse
                  .tools/git-hooks/law-lock-check.sh
ANDREW'S WORD     org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_163xZ_FABRIC_ROLES_MSTR_CTO_COO_CVO_CRO_AND_THE_INBOUND_WORK_PIPELINE_INTO_NFRA_CTLPLN.md @df6d1ad20b
MEASURED AT       2026-10-07 ~17:1xZ, laptop, working tree near 3c3e24417c
```
