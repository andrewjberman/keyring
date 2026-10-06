# PROPOSAL -- a control plane for four devices (laptop, sitez, dell1, dell2)

- **Author:** `4.0.0_SA_CRO` (base), 2026-10-06 ~01:0xZ (9:0x PM Eastern, 2026-10-05). A proposal: nothing is
  provisioned, seated, armed or changed by it.
- **Order:** Andrew-direct, verbatim in
  `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_010xZ_FOUR_DEVICE_CONTROL_PLANE_PROPOSAL.md`.
- **Input:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/HANDOFF_TO_CRO_FOUR_DEVICE_STRATEGY_DELL1_DELL2_20261006.md`
  @de9aaf1e1b (its ten questions are answered in section 9).
- **Claim marks:** MEASURED = read by this seat today at the file or command named. INHERITED = from the handoff, not
  re-read. PROPOSED = this document's recommendation. Unmarked design text is PROPOSED.

---

## 1. The proposal in eight lines

1. **Two planes.** The CONTROL plane decides and records: what work exists, which box runs it, in what order, and what
   Andrew has said. The EXECUTION plane does the work. Today every box does both; that is what stops scaling.
2. **Laptop = control plane.** Andrew's terminal, the planning seats (Chief Technology Officer, Chief Research
   Officer, Chief Verification Officer, fabric manager), and every register. It runs at most one execution lane.
3. **Site Z = integration, deploys, heavy jobs, Bloomberg.** It is the ONE writer of the shared trunk and the one box
   that deploys.
4. **dell1 and dell2 = execution boxes.** Each runs two or three execution lanes (a Chief Operating Officer lane plus
   its workers) and nothing else: no planning seats, no deploys, no vendor calls, no pushes to the trunk.
5. **The unit that is placed on a box is the PROJECT, whole.** A round's issuer and all its workers sit on one box.
   Work is split between boxes by which files it writes, so two boxes almost never touch the same file.
6. **Merges become a queue with one writer.** An execution box publishes each finished round as its own branch.
   Site Z merges the queue into the trunk, in the order the control plane sets, and pushes. Four boxes never race for
   the trunk, and no box drifts further than one unpublished round.
7. **Every shared, scarce thing gets one named owner or a lease:** registers (laptop writes), trunk (site Z writes),
   deploys (site Z), Bloomberg (site Z), the walker account and vendor sessions (a lease), Andrew's word (laptop).
8. **Three mechanisms must change before a Dell does real work** (section 8): the push gate deploys on ANY branch
   push; the bus knows only two devices; the push rule requires Andrew at the pushing terminal.

---

## 2. Why the present shape does not stretch to four

| Pressure | Today (two boxes) | At four boxes |
|---|---|---|
| Trunk drift | The laptop is **154 commits ahead** of the remote trunk, from 12 authors (MEASURED: `git rev-list --count origin/CLOUD..HEAD`, 2026-10-06 01:0xZ). The remote has not moved since the restart | four local trunks drifting by hundreds each; every pull merges three other boxes' work |
| Merge cost | a large merge commit is graded by the commit hooks for 15 to 45 minutes (`.claude/skills/integrate/SKILL.md:49-51`) | each box pays that on every pull, and a push that loses the race pays it again |
| Who pushes | only the two fabric managers, on Andrew's word while he is at that terminal (`org/XXX.md` Step 1b) | he cannot be at four terminals |
| A push is a deploy | the push gate uploads every pipeline script in the pushed range to production storage, unconditionally (`integrate/SKILL.md:68-72`). MEASURED: the gate runs for every pushed ref, including a brand-new branch (`.tools/git-hooks/pre-push-safe-deploy.sh:41-58`) | any box that pushes anything deploys |
| Cross-box messages | one queue pair, hardcoded to two device names and resolved from the Windows profile path (MEASURED: `.tools/agentbus-sqs.sh:84-86`, `:157-158`) | a third box has no name and no queue |
| Shared append-only files | two boxes appending to one file collide at the same line; resolved by hand at merge | three or four boxes: a collision on most merges |
| Scarce accounts | the walker account is passed by relayed messages ("held by site Z", "FREE"); Bloomberg quota ran out today (INHERITED) | more claimants, same single accounts |
| Laptop capacity | 31.7 GB memory, 8 cores, 37.6 GB disk free; a worker checkout costs about 2.35 GB (INHERITED, the CTO's reading) | the laptop cannot also be the place the extra work runs |

**The thing that already scales:** the canonical workflow's own rule that the three tracks share FILES, never messages
(CLAUDE.md rule 27). A planning seat on one box and an execution lane on another need only the same files. The whole
proposal rests on that: make the files arrive, and the roles can sit on different boxes.

---

## 3. Roles of the four boxes

| Box | Role | Seats it runs | It is the only box that | It never |
|---|---|---|---|---|
| **laptop** | control plane | fabric manager (base), CTO, CRO, CVO; at most ONE execution lane, for work Andrew wants under his eye | writes the registers; receives Andrew's word; orders the merge queue; hands out leases | integrates other boxes' rounds |
| **sitez** | integration, deploys, heavy jobs, Bloomberg | fabric manager `~Z` as INTEGRATOR; one or two execution lanes for pipeline and deploy work; the Bloomberg scheduled tasks | pushes the trunk; deploys; applies infrastructure; calls Bloomberg | plans or registers work |
| **dell1** | execution | fabric manager lane (re-seats lanes, runs the bus consumer, publishes rounds); 2 to 3 execution lanes with their workers | -- | pushes the trunk, deploys, calls a vendor, writes a register |
| **dell2** | execution | the same | -- | the same |

**Why the planning seats sit only on the laptop.** Today site Z runs its own copies (`~Z` lanes of the CTO, CVO and
CRO). That made sense for two self-contained fabrics. With four boxes it would mean four endpoint authors and four
registrars. One set, on the control plane, is what makes it a control plane. Site Z's planning lanes retire as their
projects close; this proposal does not ask for them to stop mid-project.

**Why site Z is the integrator, not the laptop.** Integration is a heavy job (the 15 to 45 minute grading), and the
push is a deploy. Andrew's framing puts both on site Z. It also keeps the laptop responsive for him. The laptop's
fabric manager is the named fallback integrator if site Z is down.

**What the Dells are for, and the recommendation on the open question.** Recommended: **both Dells are plain
execution boxes, told apart by which files their projects write** (section 4), not by a special function. Reasons: a
specialised box sits idle when its kind of work is quiet; and a box defined by its write surface keeps merges clean,
which is the binding constraint. The alternative Andrew may prefer is in section 10, call 1.

---

## 4. How directives and projects are split between boxes

**Rule 1 -- placement splits in two.** Every directive's CONTROL (endpoint, PRD, register rows, verification
judgment) is on the laptop, always. Only its EXECUTION is placed on a box. Andrew's two standing placement criteria
(oversight-heavy model-portfolio and advisor work stays local; ontology, infrastructure and anything nuanced or
high-risk stays local) keep their meaning: they now say whose execution stays on the laptop's one lane or on site Z.

**Rule 2 -- the placed unit is the project.** One project, one box, one execution lane, its workers on that box. A
worker cannot be messaged and shares files with its issuer through local worktrees, so a round is never split across
boxes. The project's own row already carries the device fact a drive reads (`fabric`; `DIRECTIVES.yaml:396-409`);
the row gains the values `dell1` and `dell2`.

**Rule 3 -- split by write surface.** Two projects go to different boxes only if the paths they write do not overlap.
The check that enforces a worker's write surface exists (`.tools/owned-paths-validate.py`); placement uses the same
idea one level up. Where two projects must write the same file, they go to the same box and are sequenced there.

**Rule 4 -- the portal is its own trunk.** `portal/` is a separate repository with its own `DEV` branch. Portal work
and workspace work therefore do not collide with each other. That gives the natural first split:

| Box | First allocation (PROPOSED; Andrew's per-directive call) |
|---|---|
| **dell1** | portal-facing execution: Opal Workflows front end (D9, the Investor Reporting page), Design (D13), Opal Ticketing (D7) |
| **dell2** | workspace back-end build work whose deploy step is handed to site Z: Opal Workflows back end (D9), Data Pipelines (D8, which holds the classification-table project) |
| **sitez** | what it holds today, which deploys or needs Bloomberg: Model Portfolios (D1), Positioning (D4), Asset Management (D5), Opal AI (D6), Platform Operations (D12); plus the deploy step of every other box's work |
| **laptop (one lane)** | the work the standing criteria keep local, sequenced on the one lane: Agent Infrastructure (D0), Advisor Intelligence (D2), Portfolio Analytics (D3), Partner Implementations (D10), Substrate and Tooling (D11), Platform Logic (D14). Six directives on one lane is tight; which of them may run on a Dell is a per-case call for Andrew |

Current placements, for comparison (MEASURED, `org/missions/DIRECTIVES.yaml`): site Z holds D1, D4, D5, D6, D12; the
laptop holds D0, D2, D3, D7, D8, D9, D10, D11, D13, D14. The laptop ran four execution lanes on D9 alone today.

**Rule 5 -- a sequence, not a scramble.** `org/missions/SEQUENCE.yaml` already orders projects. It gains a per-box
view: each box's lanes take the next project placed on that box. A box with a free lane and nothing placed on it is
visible on the control plane; the control plane moves a project, never the box.

---

## 5. The junctures, one by one

### 5.1 Merges and the trunk: a merge queue with one writer

```
  EXECUTION BOX (dell1 / dell2 / laptop lane / sitez lane)
    round closes -> the lane's drain merges its workers (as today, .tools/safe-merge.sh)
                 -> the box publishes ONE branch:  q/<device>/<PROJECT>/r<N>
                 -> one bus line to the control plane: "round ready", with the branch and its hash
                                    |
  CONTROL PLANE (laptop)            v
    the queue: an ordered list of published rounds  (order = SEQUENCE, then arrival)
                                    |
  INTEGRATOR (sitez)                v
    takes the head of the queue -> merges it into the trunk in its own worktree
                                -> the commit hooks grade the merge ONCE, here
                                -> pushes the trunk (the deploy event, on the deploy box)
                                -> one bus line to every box: "trunk at <hash>"
                                    |
  EVERY BOX                         v
    pulls the trunk at its next round START (a small merge, because it happens every round)
```

- **One writer** removes the race: nobody's push is ever rejected, and the long grading runs once per round instead
  of once per box per pull.
- **Drift is bounded by construction:** a box holds at most one unpublished round per lane. Today's 154 is a number
  with no ceiling.
- **Conflicts surface at one place,** to the seat best placed to route them. A real same-line conflict is a placement
  finding (rule 3 was broken), sent to the control plane, not absorbed at the merge.
- **This is not the two-branch model returning.** The retired `SITEZ` branch was a second long-lived trunk that had
  to be kept in parity. A queue branch lives for one round, flows one way, and is deleted after it merges.

### 5.2 `/integrate`

It becomes two skills with two owners: **publish** (any box's fabric manager: push the round branch, tell the control
plane) and **integrate** (site Z only: take the queue head, merge, grade, push, announce). The laptop's launch-time
"assess" form stays, reading the queue depth and each box's distance from the trunk.

### 5.3 The push gate and deploys

MEASURED: the push gate uploads pipeline scripts for every pushed ref. So before any queue branch is pushed, **the
gate must upload only when the pushed ref is the trunk.** With that change the rule becomes simple and mechanical:
publishing never deploys; the integrator's trunk push is the only deploy event; it happens on the deploy box.

All other deploy acts (infrastructure applies, function updates, served-output moves) also sit on site Z. Because one
box deploys, the open-deploy ledger lives in one tree and the "union every worktree on every box" problem does not
arise. A Dell that needs something deployed asks through a file the integrator reads, as a worker's round does today.

### 5.4 Registers and other shared files: one writer per file

| File class | Writer | Others |
|---|---|---|
| Registers: `DIRECTIVES.yaml`, `SEQUENCE.yaml`, `LIVE_ARMS.md`, project rows, the missions tree carriers, law (`CLAUDE.md`, `org/XXX.md`) | laptop only | read |
| A project's own tree (task orders, deliverables) | the box the project is placed on | read |
| Append-only files (surprise channels, audit logs, session logs) | each box writes ITS OWN file: `<name>.<device>.md` | read all |

The per-device append file already exists once in the estate (`org/surprise_channel/ETFS_INGEST/INVESTIGATION_v1.Z.md`,
MEASURED by the commit gate's corpus listing today). Making it the rule removes the append collision entirely.

### 5.5 Messaging

- **Inside a box:** unchanged. One local broker per box.
- **Between boxes:** one inbound queue per device, four in total, each drained by that box's fabric manager. Any box
  sends to the recipient's queue. (Today's pair is named sender-to-receiver; four boxes in that style would need
  twelve.)
- **Device identity** comes from a setting made once at bring-up, not from the Windows profile path. A device
  registry (one small file: name, role, queue, seat limit, lane letters) is the single place a box's name lives;
  scripts read it instead of carrying the names (the no-device-specific-code rule, LD-0405).
- **What crosses the bus is small:** "round ready", "trunk at", lease grants, and a pointer to a record. Content
  travels in files, as now.

### 5.6 Scarce accounts and vendors: leases

One lease register on the control plane: resource, holder, expiry. Covered at the start: the walker account, the
YCharts session, the portal `DEV` push, the Bloomberg daily quota. A box takes a lease before use and the lease
expires by itself if the box dies. It replaces the relayed "held" and "FREE" messages seen four times today.
Dells take no vendor lease at all: every vendor pull stays a scheduled job on its existing home.

### 5.7 Identity and credentials

Each box signs in as itself, with its own cloud identity, so the audit trail records which box acted. The Dells'
identity cannot deploy, cannot apply infrastructure and cannot write production storage. That turns "Dells never
deploy" from a rule people follow into something the cloud refuses.

### 5.8 Andrew's attention

- He speaks at the laptop. A word that concerns another box is recorded there and reaches the box as a file plus one
  bus line, which is today's pattern made the only pattern.
- Dells run unattended. A lane there never stops on a question to him; its open decisions roll up to ONE view on the
  laptop.
- The trunk push no longer needs him at the pushing terminal. In its place: a standing rule he sets once (what the
  integrator may push without asking, and what always waits for his word, such as a push that carries a pipeline
  script).

### 5.9 Limits and failure

| Event | What holds |
|---|---|
| A Dell reboots mid-round | workers' commits are on that box's disk; the lane re-seats from its handoff and continues. To survive a disk loss, each lane also publishes its work-in-progress branch at every cell close (safe once 5.3 lands) |
| Site Z is down | rounds queue; nothing is lost; execution continues; the laptop's fabric manager integrates if the outage is long |
| The laptop is down | execution boxes finish their current rounds and stop at the round boundary; nothing new is registered or ordered |
| A box's bus consumer is not running | its mail accumulates in its queue; the control plane sees a box that has not acknowledged |

Seat limits are per box in the device registry: laptop one execution lane; site Z two; each Dell two to start, three
once measured.

---

## 6. Naming

| Thing | Proposed |
|---|---|
| Device names | `laptop`, `sitez`, `dell1`, `dell2` (Andrew's names) |
| Fabric manager lanes | `0.0.0_AB_MSTR` (laptop), `0.0.0_AB_MSTR~Z`, `0.0.0_AB_MSTR~D1`, `0.0.0_AB_MSTR~D2` |
| Execution lanes | keep the project letter (`2.0.0_SA_COO~Y`). The lane does not encode the box; the device registry and the project row say where it runs. A suffix is an attribution, not a device fact (the bus skill already says so) |
| Queue branches | `q/<device>/<PROJECT>/r<N>` |
| Per-device files | `<name>.<device>.md`; audit archive `org/audit/archive/<device>/` |
| Queues and cloud identities | builder output from `lib/opal_naming.py`, not typed here (CLAUDE.md rule 30) |

---

## 7. Rollout: one working journey first

| Stage | What Andrew can see when it lands |
|---|---|
| **0. Bring-up** | dell1 stands up from the new-device kit, has its own identity, appears in the device registry, and answers a bus message from the laptop |
| **1. The thread** | ONE project is placed on dell1. Its PRD is written on the laptop; its round is issued, worked and drained on dell1; its round branch is published; site Z integrates it and pushes; the laptop sees it in the trunk and the CVO grades it. One round, end to end, with the time of each hop written down |
| **2. The queue under load** | two lanes on dell1 and the laptop's lanes publish in the same hour; the queue orders them; nothing is pushed twice; drift per box is read and stays at one round |
| **3. dell2** | the second Dell joins by the same steps; the first allocation of section 4 moves |
| **4. The laptop goes quiet** | its execution lanes drop to one; site Z's planning lanes retire as their projects close |

Stage 1 is the test of the whole idea. If one round cannot travel laptop to dell1 to site Z to laptop cleanly, no
later stage is worth starting.

---

## 8. What must change first (mechanisms, named not sequenced)

1. **The push gate deploys on any ref** (`.tools/git-hooks/pre-push-safe-deploy.sh`). It must deploy on the trunk
   only. Until then a Dell cannot publish anything safely. This is the hard prerequisite.
2. **The bus knows two devices** (`.tools/agentbus-sqs.sh`): names, queue map and path-based identity.
3. **The push rule** (`org/XXX.md` Step 1b; `.tools/hooks/never-rules-gate.sh` gate 5) admits only the two fabric
   managers and assumes Andrew at the terminal. It needs the integrator's standing rule and the publish act.
   `org/XXX.md` is a locked file: this is Andrew's express order.
4. **A device registry** does not exist. Placement criteria live in a comment block of `DIRECTIVES.yaml`.
5. **Append-only files are shared**, not per device.
6. **The Dells need their own cloud identity** with the limits of 5.7.
7. **`/integrate`, `/agentbus`, `/watcher`, `/mstr-spawn` and the startup protocol** each name two devices somewhere.

---

## 9. The handoff's ten questions, answered

| # | Question | This proposal |
|---|---|---|
| 1 | What the Dells are for | plain execution boxes, 2 to 3 lanes each, split by write surface (sections 3, 4) |
| 2 | Naming | section 6 |
| 3 | The trunk | one writer (site Z) fed by a queue of round branches; drift bounded at one round per lane (5.1) |
| 4 | Can a round's workers sit on another box from its issuer | no; the project is the placed unit (4, rule 2) |
| 5 | Messaging | a broker per box; one inbound queue per device; small messages, content in files (5.5) |
| 6 | Deploys and the open-deploy ledger | one deploy box, so one ledger (5.3) |
| 7 | Scarce vendor seats | leases on the control plane; Dells make no vendor calls (5.6) |
| 8 | Credentials and identity | one cloud identity per box; the Dells' cannot deploy (5.7) |
| 9 | Andrew's attention | he speaks at the laptop; Dells unattended; one view of open decisions (5.8) |
| 10 | Limits and failure | per-box seat limits in the registry; the failure table (5.9) |

---

## 10. Decisions for Andrew, each with a recommendation

1. **The Dells: two plain execution boxes, or one specialised?** Recommend plain, split by write surface. The
   alternative is dell1 = portal and front end only, dell2 = back end only, fixed.
2. **Site Z as the single trunk writer.** Recommend yes. The alternative is every box pushing the trunk in turn under
   a lock, which keeps today's model and its merge cost on every box.
3. **Planning seats only on the laptop.** Recommend yes, with site Z's retiring as projects close.
4. **A standing push rule for the integrator, replacing "on Andrew's word at that terminal".** Recommend: the
   integrator pushes a round that carries no pipeline script without asking; a round that carries one waits for your
   word. This edits a locked file and needs your express order.
5. **The first allocation in section 4.** Recommend it as a starting point; each directive's move is yours.
6. **Dell identities that cannot deploy.** Recommend yes.

---

## 11. What this proposal does not know

- **The Dells' hardware, network location and arrival date** (the CTO's handoff says the same). "Two or three lanes
  each" is Andrew's estimate; no Dell was measured.
- **How long one round's integration takes.** The 15 to 45 minutes is for large merges of mixed work; a single
  round's merge was not timed. The queue's throughput depends on it.
- **How often two projects really write the same file.** Rule 3 assumes it is rare; no overlap census was run.
- **Whether the hooks behave on a queue branch** as they do on the trunk; only the push gate was read.
- **The cost** of two more boxes' cloud identities, queues and model usage.
- **The site-Z side.** Every measurement here was taken on the laptop. Site Z's capacity to be the integrator while
  running Bloomberg jobs and its own lanes was not read.
- **Tradeops**, the second fabric on its own broker port, is not addressed.
- It read `/integrate`, `/agentbus`, the push gate's ref loop, the push rule's header and `DIRECTIVES.yaml`'s
  placement block. It did not read the new-device kit.

## REFS

```
  THIS FILE      docs/briefs/four-device-control-plane-proposal-20261006.md
  ORDER          org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_010xZ_FOUR_DEVICE_CONTROL_PLANE_PROPOSAL.md
  INPUT          org/tier1_exec/1.0.0_SA_CTO/deliverables/HANDOFF_TO_CRO_FOUR_DEVICE_STRATEGY_DELL1_DELL2_20261006.md @de9aaf1e1b
  MECHANISMS     .claude/skills/integrate/SKILL.md; .claude/skills/agentbus/SKILL.md; .tools/agentbus-sqs.sh;
                 .tools/git-hooks/pre-push-safe-deploy.sh; .tools/hooks/never-rules-gate.sh (gate 5);
                 org/missions/DIRECTIVES.yaml (placement); org/missions/SEQUENCE.yaml; org/XXX.md Step 1b
  DIRECTIVE HOME D0 (agent infrastructure), if this becomes a project; registration is 1.0.0_SA_CTO's
  MEASURED AT    2026-10-06 ~01:0xZ, laptop only
```
