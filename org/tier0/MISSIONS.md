# MISSIONS — the Opal mission register

**Owner: `0.0.0_AB_MSTR`. Maintained at MSTR startup and on sovereign direction.**
**Source of the taxonomy: Andrew-direct 2026-07-28, verbatim captured in `org/tier0/ledger/LD-0341.md`.**

---

## What this is

A layer that sits **above** the Macro/Project Registry. Opal is running a handful of very large
initiatives that no single project code contains. This register names them, and tracks whether each is
actually moving.

A **Sub-group** is a durable intent. It ends when the intent is satisfied, not when a ticket closes.
Sub-groups attach to macro codes and project codes **many-to-many and non-exclusively** — sometimes a
sub-group is roughly one project, sometimes it spans a dozen project codes, sometimes it spans several
macros that otherwise have nothing to do with each other. **The attachment is a pointer, never a
containment claim, and it is explicitly NOT 1:1.**

## Taxonomy (Andrew-direct 2026-07-28, ratified)

```
MISSION GROUP    Portal · Infrastructure · Debt · External   (4, fixed unless Andrew changes them)
  SUB-GROUP      the large initiative -- VERSIONED           (PORTAL.MODEL_PORTFOLIOS v1.0, INFRASTRUCTURE.GRAPH v1.0, ...)
    OBJECTIVE    a nameable outcome inside it                (PORTAL.MODEL_PORTFOLIOS.O2, ...)
      -> attaches to  macro codes and/or project codes       (many-to-many, non-exclusive)
```

| level | examples | versioned? |
|---|---|---|
| **Mission Group** | `Portal`, `Infrastructure`, `Debt`, `External` | no — these are stable |
| **Sub-group** | `Advisor Intelligence` under Portal · `Backend` under Debt | **YES** |
| **Objective** | `PORTAL.MODEL_PORTFOLIOS.O3` | no — versioned by its parent |

**Sub-group versioning.** Each sub-group carries a `vMAJOR.MINOR` and a version history.
**MAJOR** = the intent or scope changed (what "done" means is now different). **MINOR** = objectives
added, removed, or re-anchored within an unchanged intent. **The version is a statement about the
DEFINITION, not about progress** — progress lives in the three axes below and must never be inferred
from a version number.

> *Read of Andrew's "the mission sub-segments should be versioned" as applying at the **sub-group**
> level, since that is the level he named in the same breath. If he meant the objective level instead,
> the scheme pushes down one tier unchanged — say the word.*

## What this is NOT — the design constraint that matters most

> **THIS REGISTER CREATES ZERO OBLIGATIONS FOR ANY OTHER AGENT.** No status field for Tier-1 to
> maintain, no flip ceremony, no new gate, no TO type, nothing to remember. Andrew-direct: *"I don't
> want to add more process architecture and bullshit for the tier1 agents to have to do."*

**MSTR derives every value here from artifacts the fabric already produces** — commits, project JSONs,
PRDs, ledger entries, live/served state. If a sub-group's state cannot be derived from what already
exists, that is a **finding about our instrumentation**, not a request for someone to file a form.

It is also **not** a replacement for `org/projects/REGISTRY.md`. The registry answers *"what work
exists."* This answers *"are the big things actually moving, and what would move them next."*

---

## How progress is assessed

**No percentages. Ever.** A percentage on work like this is a fabricated number, and this fabric has
paid repeatedly for plausible numbers whose axis nobody could state.

Each objective carries a stance on **three independent axes.** They are separated because collapsing
them is precisely how this estate has been burned — *"it is deployed and it works"* is not an
architecture, a green suite describes a file rather than a runtime, and *"the chain ran"* is not
*"the product is fixed."*

| axis | question | fails when |
|---|---|---|
| **DECIDED** | Is the target definition settled, by someone with the authority to settle it? | we are building toward a shape nobody ruled |
| **BUILT** | Does the mechanism exist — in the repo, in the estate? | the design is right and nothing exists |
| **SERVING** | Is it live, carrying the real thing, and verified at the surface that consumes it? | it exists, is deployed, and no consumer is on it |

Values: `NO` · `PARTIAL` · `YES`. **Every non-`NO` value carries an anchor** — a commit-ish, an
artifact key, a ruling reference, a PRD. A value with no anchor is written `ASSERTED` and is
**non-actionable**, exactly as an ungrounded causal claim is.

Each objective also carries:

- **FRONTIER** — the single next thing that would move it. One line. Not a plan, not a decomposition.
- **BLOCKED-ON** — a named owner or a named sovereign call, when something is genuinely waiting.
- **GROUNDED** — the date this was last re-derived, and against what.

> **A SUB-GROUP STATE IS A CLAIM WITH A DATE ON IT.** Anything not re-grounded in the current pass is
> marked `STALE` rather than carried forward silently. A stale record that reads confident is worse
> than one that reads unknown — the estate's own recurring lesson, and this register is not exempt
> from it.

**`UNASSESSED` is a legal and expected value.** It means MSTR has not looked yet. It is never to be
quietly upgraded to `NO` — those are different claims.

## MSTR startup protocol

Cheap by design; it must survive being run every session.

1. Read this file.
2. For each objective, re-derive what is cheap to re-derive (project JSON status, PRD presence, commit
   activity on attached codes, live/served state where a one-call check exists).
3. Update stances **and their GROUNDED dates**. Mark anything not re-derived `STALE`.
4. Surface to Andrew, in his terms: **what moved, what did not move that should have, and what is
   waiting on him.** Not a status dump.
5. Sub-groups do not get dispatched from here. Routing stays with CTO and COO; MSTR observes and reports.

---

# EXEC SUMMARY — current state

    ANCHOR COMMIT   a7c78a05ec
    ANCHOR TIME     2026-07-28T14:55:20-04:00   (author-time of that commit, not a wall clock)
    ANCHOR AUTHOR   1.0.0_SA_CTO
    ANCHOR SUBJECT  prd(MDPF_DEBTCLEAN): s.13.2a ASSETS-SIDE HOME -- portal/gold/mdpf/{scope}/{artifact-
    WINDOW          2026-07-28 00:00 -04:00 -> anchor
    SOURCE          `comp-missions scan`. Prose is MSTR's; every number is the tool's output,
                    not recollection.

> **Re-derived, never edited in place. Stale the moment a commit lands after the anchor — which is
> why the anchor is a COMMIT, not a clock. If the anchor is not HEAD, this is history, not state.**

## The measured shape of the day

**85 commits.** 12 are governance/meta (register upkeep, ledger, law, comms) and are **excluded from
the denominator** — correctly unattributed, not a blind spot. That leaves **73 mission-attributable
commits: 19 mapped, 54 unmapped.**

| sub-group | commits | code | doc | newest |
|---|---|---|---|---|
| `PORTAL.MODEL_PORTFOLIOS` | **18** | 6 | 17 | `a7c78a05ec` 14:55:20 |
| `DEBT.BACKEND` | **5** | 5 | 0 | `04e230b749` 13:21:26 |
| `PORTAL.ADVISOR_INTELLIGENCE` | 0 | — | — | **no activity** |
| `INFRASTRUCTURE.TOOLS` | 0 | — | — | **no activity** |
| `INFRASTRUCTURE.GRAPH` | 0 | — | — | **no activity** |
| `DEBT.FRONTEND` · `EXTERNAL.49FINANCIAL` · `EXTERNAL.INFLECTION` · `EXTERNAL.COTTONWOOD` | 0 | — | — | **no activity** |

**Four commits are AMBIGUOUS** (`DEBT.BACKEND` + `PORTAL.MODEL_PORTFOLIOS`) — all four are the MDPF
IAM/Terraform work, which genuinely is both. **Reported, not tie-broken.** A commit that is honestly
two things is not improved by forcing it to be one.

## What it says, in one line

**Every mission-attributable commit today landed in Model Portfolios or backend debt. The two
Infrastructure sub-groups named joint-highest priority received nothing.**

Second instrument to say so today, and **the two disagree on detail**: CVO's independent mapper read
`INFRASTRUCTURE.TOOLS` at 5 and `INFRASTRUCTURE.GRAPH` at 1 (that one from a stale session); this one
reads 0 and 0. **Neither is wrong — they classify differently, and I am not reconciling them into a
false precision.** What survives both is the direction, and the direction is unambiguous: **roughly an
order of magnitude of misallocation against the stated priority.**

## The blind spot, as a number rather than a caveat

**54 of 73 attributable commits could not be attributed — 74%.** They are overwhelmingly **agent-home
deliverables, session logs and record commits** under `org/tier1_exec/**` and `org/tier2_senior/**`:
real work product, neither pure governance nor path-attributable.

> **That number is the argument for the DECLARED trailer, and it is why path-globs alone cannot be the
> mechanism.** A path map only ever sees work that touches a distinctive directory. Most of this
> fabric's output is prose in an agent's own folder, and no glob will tell you which mission it served.
> **The commit's author knows; the filesystem does not.** The trailer moves attribution to the only
> party holding the information — and because the hook writes it from the spawn tag, it asks no agent
> to remember anything.

**Do not read 74% as a defect rate.** It is the coverage of a mechanism live for zero commits so far.
**The honest reading: this is the baseline the trailer has to beat.**

## Register state at the anchor

- **`PORTAL.MODEL_PORTFOLIOS`** — `DECIDED` YES · `BUILT` **YES** (corrected off the 16:48:04Z
  *scheduled run*, not off a commit) · `SERVING` **NO**: the serve is a hand-restored artifact fed by
  neither producer. **Frontier: the defined publisher. Blocked on a CTO architecture call — which
  serving namespace is canonical — that precedes the build.**
- **`INFRASTRUCTURE.TOOLS`** — `DECIDED` YES · `BUILT` YES for positive enumeration (gate
  **exercised**: 88 homed tools, 12 rules, 0 unverifiable) / NO for the negative declaration ·
  `SERVING` **UNASSESSED** — gate wiring unestablished, and CVO declined to guess after three false
  claims about that same project earlier the same day. **Largest hole in the register: `NFRA_TOOLUNIFY`
  — 109 commits, 113 doc files, no project JSON.**
- **`INFRASTRUCTURE.GRAPH`** — `SERVING` PARTIAL: **121 EventBridge Rules vs 10 Scheduler schedules —
  92% on the non-standard side of a standard that already exists.** The bottleneck is **adoption**,
  not decision.
- **`DEBT.BACKEND`** — 5 commits, **all code, zero doc**: the only sub-group today whose output was
  purely enacted rather than recorded.
- **`DEBT.FRONTEND`** — **LOW priority by sovereign instruction**, brief only, not decomposed, not
  staffed (`docs/briefs/DEBT_FRONTEND_mission_brief_20260728.md`, DT). Measured: **24 cache behaviors
  + 1 default enumerated in full, 18 canonical, 5 not.** Its central question is Andrew's own
  hypothesis — *generated ≠ displayed* — and early evidence supports it. **It finishes a migration
  already begun**, with the precedent recorded in-source at `portal-proxy.ts:356-357`.

## Open at Andrew

1. The **AUA aggregation expansion** (`PORTAL.MODEL_PORTFOLIOS.O2`) he said he would send.
2. **Per-client initiative detail** for the three `EXTERNAL.*` sub-groups.
3. **"Cottonwood Capital Advisory" vs "Advisors."**
4. **The allocation gap above** — surfaced, not sized. Allocation is COO's, dispatch is CTO's.

---

## PRIORITY (Andrew-direct 2026-07-28)

**Highest priority right now:** `PORTAL.MODEL_PORTFOLIOS` (Model Portfolios) · `INFRASTRUCTURE.TOOLS` + `INFRASTRUCTURE.GRAPH`
(enumeration and coverage clarity). Everything else is real but is not what the fabric is being
pointed at this week.

**Why it is stated here rather than left implicit** — Andrew's reason, and it is the operative one:
> *"I cannot be getting in the weeds right now on one topic as it prevents me from pushing the fabric
> forward on the collective missions above."*

**The register's job is to make that possible.** A sovereign who has to reconstruct state per topic
cannot run four mission groups. Every field in here is chosen so state can be read without a briefing.

> ### ⚠ PRIORITY vs ACTUAL ALLOCATION — measured 2026-07-28 (CVO)
> Today's session ran **82 commits**, mapped by sub-group:
>
> | sub-group | commits | live capacity |
> |---|---|---|
> | `PORTAL.MODEL_PORTFOLIOS` | **42**, across 5 agents | heavy |
> | `DEBT.BACKEND` | 14 | present |
> | `INFRASTRUCTURE.TOOLS` | **5** | thin |
> | `INFRASTRUCTURE.GRAPH` | **1** — and that one from a **STALE** session | **none live** |
>
> **Two of the three joint-highest-priority sub-groups have six commits between them, and `INFRASTRUCTURE.GRAPH`
> has no live capacity at all.** The stated priority and the actual allocation disagree by roughly an
> order of magnitude.
>
> **CAVEAT, CVO's own and load-bearing: 32 of 82 commits went unmapped (~39%), and the mapper likely
> undercounts `INFRASTRUCTURE.TOOLS` because its deliverables cite MDPF as their worked example. DIRECTIONAL
> ONLY — do not quote it as a metric.** The direction survives the caveat; the precision does not.
>
> **Surfaced, not sized.** Allocation is COO's call and dispatch is CTO's. **This is the one thing a
> project-level view structurally cannot show you: not what is happening, but what is happening
> INSTEAD of what you said mattered.**

---

## THE ASSESSMENT PROTOCOL — how state gets logged on a consistent basis

**MSTR owns the register; Tier-1 owns the ground truth.** This is the exchange format between them.
Five fields, deliberately few, because a format nobody can produce in five minutes does not get
produced.

For each sub-group they hold, a Tier-1 agent returns:

| # | field | what it must contain |
|---|---|---|
| 1 | **ATTACH** | which macro/project codes actually cover this, in their view |
| 2 | **HOLES** | live work covered by **NO** project code — named, with evidence |
| 3 | **STANCE** | `DECIDED` / `BUILT` / `SERVING`, each `NO`/`PARTIAL`/`YES` **with an anchor** |
| 4 | **FRONTIER** | the single next thing that would move it |
| 5 | **BLOCKED-ON** | a named owner or a named sovereign call — or `nothing` |

**Field 2 is the one that justifies the exercise.** The registry can already answer *what projects
exist*. It cannot answer *what is happening that no project covers* — and that gap is where the
expensive surprises live. `MDPF_CHANNEL_INDEPENDENCE` was exactly this: live, PRD'd, cited as law,
driving a P0, and **invisible to every registry instrument we own.** Assume there are more.

**Rules that keep the exchange honest:**
- **`UNASSESSED` is a legal answer.** *"I have not looked"* is information; a guess is not.
- **An unanchored stance is `ASSERTED` and non-actionable.** Same bar as any other claim here.
- **Nobody re-derives another agent's lane.** Report your own; disagreements are findings, not edits.
- **This is a state pull, NOT a dispatch.** Routing and sequencing remain CTO's and COO's. MSTR
  collects, grounds, folds, and reports — under Andrew-direct instruction to coordinate, which does
  not convert the observer into a dispatcher.

---

## MISSION-TAGGED SPAWNS — grouping the fabric by mission so context stays focused

Andrew-direct: deploy agents **grouped by mission per session**, so context is focused and preserved,
on a **tilde-lane basis** as needed. *"It really is just a function of launch instructions at spawn."*

**The whole mechanism, and it is deliberately this small:**

```
1. COO names the sub-group it needs an agent for      ->  "spawn for PORTAL.MODEL_PORTFOLIOS"
2. MSTR spawns with that tag in the startup context   ->  /mstr-spawn <serial> --mission PORTAL.MODEL_PORTFOLIOS
3. The agent starts already knowing its mission,      ->  reads MISSIONS.md at that sub-group:
   its intent, its attached codes, and its frontier       intent + ATTACH + FRONTIER + BLOCKED-ON
```

**No new artifact, no new registry, no new obligation.** The tag rides the existing `--say`
first-message channel that `/mstr-spawn` already carries. **The mission context is a POINTER INTO
THIS FILE, not a copy of it** — so it cannot drift from the register, which is the failure a copied
briefing would guarantee.

**Tilde lanes are the unit of mission focus.** A base serial spread across three sub-groups is the
context dilution this is meant to end; `~A` on `PORTAL.MODEL_PORTFOLIOS` and `~B` on `INFRASTRUCTURE.GRAPH` keeps each
session's working set coherent.

### TWO SPAWN TRIGGERS, TWO PATHS (COO refinement 183123Z — accepted)

**COO falsified my step 1 using the day's own evidence.** It assumed spawn demand originates with COO.
**Today's only real spawn need did not** — `0.7.0_AE_CloudOps` hit context limit and said so itself.

| trigger | who names the mission | why |
|---|---|---|
| **NEW CAPACITY** | **COO** | a genuine allocation decision, and allocation is COO's |
| **CONTINUITY** (context-exhausted / dying agent) | **nobody — the successor INHERITS the predecessor's tag** | a mechanical succession is not a decision at all |

**COO's reasoning is my own pointer-not-copy principle turned back on my design:** routing a succession
through COO so it can name a tag *it would simply copy off the predecessor's broker summary* **adds a
transcription step and nothing else — and a transcription step is exactly where drift enters.**

**Authority unchanged:** COO decides which mission needs **new** capacity (it owns allocation); MSTR
provisions and tags (it owns spawn/kill); CTO dispatches the actual work. **Spawn is not dispatch** —
the tag orients a session, it does not authorise work.

**FIRST EXERCISE, 2026-07-28 ~1832Z:** `0.7.0_AE_CloudOps~C` spawned tagged `INFRASTRUCTURE.TOOLS`, successor to
the context-exhausted base serial. Taxonomy call was MSTR's — COO explicitly deferred it. Placement
reasoning at `INFRASTRUCTURE.TOOLS`.

---
---

# GROUP 1 — PORTAL

*Major initiatives spanning portal product surfaces and the backend/pipelines behind them.*

## PORTAL.MODEL_PORTFOLIOS — Model Portfolios   `SUB-GROUP` **v1.2**

*Version history: `v1.0` 2026-07-28 created · `v1.1` +O3 (Andrew-direct 174108Z channel-trace) · `v1.2` CTO state pull 183143Z — O1 BUILT corrected to YES, HOLES recorded*

**Intent:** the Model Portfolios product serves correct, canonical numbers from canonical pipelines,
every day, without hand-restoration.

**Attaches to:** `MDPF_*` (macro) — `MDPF_REVAMP` (complete), `MDPF_3FIRMS` (active),
`MDPF_DEBTCLEAN` (active), `MDPF_MONOCLEANUP` (superseded), `MDPF_OWNTS`, `MDPF_CADENCE`,
`MDPF_COUNTS`, `MDPF_BASISSWITCH`, `MDPF_SCOPED`, `MDPF_VARFLAG`, `MDPF_COTMDL`, `MDPF_ASSETS` ·
plus `OPAL_CONSOLIDATION`, `ETFS_*`, `OPAL_TAXSMA*`, `SSCN_PFOE`.

### PORTAL.MODEL_PORTFOLIOS.O1 — Lock in the canonical pipelines
```
DECIDED : YES      @ Andrew-direct 2026-07-28 ~1427Z (canonical non-model basis) + ~1710Z
                     (deprecate legacy, move full force to REVAMP canonical) -- bf986d81a
BUILT   : YES      @ CTO-CORRECTED 183143Z. At 16:48:04Z the SCHEDULED path produced a correct
                     3-firm Global -- 450 dates, cottonwood 47 slots, sum identity 0 failing /
                     426 tested (was 425/425 FAILING), opal_aggregate_aua @2026-07-22 =
                     $1,951,676,164.42 exact. DS producer landed 14:08Z.
SERVING : NO       @ serve is a hand-restored 07-23 artifact fed by NEITHER producer; both
                     portal-v2 Deny statements production-exercised 2026-07-28 16:44Z
```
**FRONTIER:** the **defined publisher** — nothing automated writes the serve.
**BLOCKED-ON:** `1.0.0_SA_CTO`, and it is **an architecture call that precedes the build**: which
serving namespace is canonical. **Not blocked on Andrew, not blocked on a lane.**

> **MY `BUILT: PARTIAL` WAS ~2 HOURS STALE AND CTO CORRECTED IT.** I scored it against the producer
> *landing*; the discriminating evidence is **the run, not the deploy** — *"a two-leg builder is
> structurally incapable of"* a 3-firm identity-clean result. **A register that scores BUILT off a
> commit rather than off an exercised run reproduces the exact deployed-is-not-working error the
> three axes exist to prevent.** Scoring rule adopted: **BUILT anchors on an exercised run wherever
> a run exists.**

> **`SERVING: NO` kept EXACTLY as written, at CTO's explicit request** — *"the serve is a human-
> published object; no automated path writes it. That is the whole gap and it should not soften just
> because today went well."* **A good day is not a mechanism.**

**GROUNDED:** 2026-07-28T183143Z, CTO-corrected against the 16:48:04Z scheduled run.

### PORTAL.MODEL_PORTFOLIOS.O2 — The Opal AUA aggregation definition  *(PENDING — Andrew to expand)*
**Logged now at Andrew's direction so it is not lost; he will delineate it in a future message and
expand it into project PRDs + registration with CTO.**

An Opal-level definition process for how to aggregate several types of AUA:

1. **ETF Models** — our 5 archetypal model portfolios.
2. **SMA Strategies** — TAX SMA, the incoming MUNI SMA, 49F SMAs tracked in SmartX (e.g. PFOE), others.
3. **Custom Models** — client-specific SMAs that are not a larger strategy.
4. **Non-Model Residual** — assets we advise upon that fall into none of the above.

```
DECIDED : NO       -- the definition process is the work; it has not been written
BUILT   : NO
SERVING : NO
```
**FRONTIER:** Andrew's expansion message, then a PRD and registration with CTO.
**BLOCKED-ON:** Andrew (by his own statement — this is authored, not derived).
**NOTE:** this is described as *"an even larger product need"* than O1. Treat O1 as the floor for this
mission, not its ceiling.
**GROUNDED:** 2026-07-28, authored from Andrew-direct. Nothing measured yet.

### PORTAL.MODEL_PORTFOLIOS.O3 — Every channel traced to the Gold DDB: what feeds it, on what schedule, and whether it arrives
**Andrew-direct 2026-07-28T174108Z, VERBATIM** (COO-recorded `db9b11524`):
> *"I agree with your framing, we need to trace every necessary channel, e.g. 0824 schwab and smartx
> buckets for 49F, and identify what feeds them on what schedule and make sure that they are getting
> to the Gold DDB table."*

Sits under the ~1725Z priority ruling — **canonical routes and schedules before monitoring**
(CTO-recorded, `c60de93156`). That ruling had an ambiguity and this direction resolves it:
establishing *what a route is, what feeds it, on what schedule, and whether it arrives* is **ROUTE
work, not monitoring** — so the gold-DDB value-stall sequences **upstream** of the publisher rather
than behind it.

```
DECIDED : YES      @ Andrew ~1815Z mandate 5851ba0eca -- SUPERSEDES the 1725Z ruling as the
                     governing statement: channels ingest daily -> a DEFINED publisher slots
                     platinum to the portal's locations -> derive server-vs-client.
                     (Prior anchors: Andrew 174108Z; CTO 1725Z routes-before-monitoring c60de93156)
BUILT   : NO       -- no per-channel feed+schedule+arrival enumeration exists as an artifact
SERVING : NO
```
**FRONTIER:** the enumeration itself — per channel, its feeder, its schedule, and evidence it lands in
the Gold DDB. **Note this is the same shape as `PORTAL.ADVISOR_INTELLIGENCE.O1`'s frontier** (enumerate what each gold
runner actually reads). Two missions, one missing artifact class: **we do not have a per-channel
source-and-schedule map anywhere.** That is worth seeing as one gap rather than two.
**BLOCKED-ON:** `1.0.0_SA_CTO` as PRD owner; COO holds the decomposition.
**RELATED STANDING LAW:** a pipeline whose only trigger is another pipeline's success **has no
schedule and is a defect** — it freezes silently when its upstream breaks. This objective is the
direct remedy for that class, and `mdpf-daily-trigger` is a live instance of it.
**GROUNDED:** 2026-07-28, from the sovereign record. Nothing enumerated yet.

### PORTAL.MODEL_PORTFOLIOS — HOLES (field 2), returned by CTO 183143Z

Live work covered by **no project code**:

1. **`MDPF_CHANNEL_INDEPENDENCE` — CONFIRMED ABSENT from `REGISTRY.md`** by CTO, independently of my
   authoring check and of CVO's `/spot-check` F-1. **Three independent confirmations.** PRD'd, cited
   as law in `CLAUDE.md` (Rule 20 / NEVER#4), drove today's P0.
2. **Six unaccounted served objects** under `json/portfolios/` — `latest` · `manifest` · `metrics` ·
   `summary` · `timeseries` · `non_model_assets_preview`. **No owner, no project, unknown consumers.**

**DELIBERATELY NOT RECORDED AS A FINDING — the two-namespace serving question** (`json/mdpf/*` vs
`json/portfolios/*`, ~23 live objects, including `account-distribution.json` **and**
`account_distribution.json` in the same directory). CTO surfaced it and then withheld it himself:
**Andrew has told him these are known data shapes, not a discovery** — the open question is the
*migration state*, not the existence — and **he has asked Andrew and not yet had an answer.**

> **Logging the withholding rather than the item, because the discipline is the point.** A register
> that hoovers every surfaced observation into "findings" manufactures a backlog out of things the
> sovereign already knows, and then spends credibility defending it. **An unanswered question is not
> a finding.** Recorded as *open at Andrew, held by CTO*, and nothing more.

### ⚠ PORTAL.MODEL_PORTFOLIOS — REGISTRY GAP FOUND AT AUTHORING (this is the register earning its keep)
Andrew named `MDPF_CHANNEL_INDEPENDENCE` as a driver of this mission. **It has a PRD
(`docs/architecture/MDPF_CHANNEL_INDEPENDENCE_PRD.md`), it is cited as law in `CLAUDE.md`, it is
driving live P0 work today — and it has NO project JSON and ZERO rows in `REGISTRY.md`.**
Independently found by `3.0.0_SA_CVO` in today's `/spot-check` (F-1) before this authoring, and
confirmed here. **A load-bearing initiative is invisible to every registry instrument we own.**
Routed as CVO's finding; recorded here because it is exactly the class this layer exists to catch.

Also: Andrew named `MDPF_DEBTSCAN`. **No such code exists.** The two real neighbours are
`MDPF_DEBTCLEAN` (active) and `NFRA_DEBTSCAN` (complete). Attached to `MDPF_DEBTCLEAN` above as the
live one; flagged rather than silently resolved, because guessing which code a sovereign meant is how
a register starts lying.

---

## PORTAL.ADVISOR_INTELLIGENCE — Advisor Intelligence   `SUB-GROUP` **v1.0**

*Version history: `v1.0` 2026-07-28 created*

**Intent:** Advisor Intelligence runs on canonical, channel-correct sources, with performance and
attribution computed our own way — reliably, every day.

**Attaches to:** `ADVI_*` (macro, ~90 project codes) · `OPAL_ASSETS`, `OPAL_CONSOLIDATION`,
`NFRA_PPL49F`, `NFRA_PPLINF`, `NFRA_PPLCOT`.

### PORTAL.ADVISOR_INTELLIGENCE.O1 — Gold Runners source from the channel's `opal-data-assets` silver
```
DECIDED : YES      @ OPAL_CONSOLIDATION is the ratified P0 master; the assets grammar is live
                     (s3://opal-data-assets, {source}/{scope}/{layer}/{type|feed}/{date})
BUILT   : UNASSESSED  -- per-runner migration state not yet enumerated by MSTR
SERVING : UNASSESSED
```
**FRONTIER:** enumerate, per gold runner, which silver source it actually reads today. That
enumeration does not exist as a single artifact — building it is the next move, and it is cheap.
**GROUNDED:** 2026-07-28, structure only. **Deliberately `UNASSESSED`, not `NO`.**

### PORTAL.ADVISOR_INTELLIGENCE.O2 — Canonical performance + attribution: 365-day TWR, gross and net, daily
**The larger refactor.** Decide how to make canonical logic across the various data shapes,
particularly performance reporting and attribution.

- **Canonical basis: 365-day calendar TOTAL WEIGHTED RETURN (TWR).**
- `4.0.0_SA_CRO` research identified this is **how Black Diamond does it**.
- **Strategic intent: supplant Black Diamond and Orion** — canonical methods, on a **gross and net**
  basis, reliably, **every single day**.
- Requires comprehensive analysis of what each source location actually makes available:

| firm | source of record |
|---|---|
| 49 Financial | the `0833*` account in Schwab |
| Inflection Wealth Management | Orion |
| Cottonwood Capital Advisors | Black Diamond |

```
DECIDED : PARTIAL  -- the BASIS is decided (365-day TWR, gross+net, daily). The METHOD per source
                      is not, and the per-source data analysis has not been done
BUILT   : NO
SERVING : NO
```
**FRONTIER:** the per-source data-availability analysis — what can each of the three actually give us,
daily, to compute TWR gross and net. **Everything downstream is unanswerable until that is enumerated.**
**BLOCKED-ON:** nothing external. This is unstarted, not stuck.
**NOTE — standing law that constrains this mission:** `0833` is the ADVISOR INTELLIGENCE master and
`0824` is the MODEL PORTFOLIOS master. **Never added, never substituted.** A TWR effort that reaches
across both must respect the business-purpose split; this mission does not loosen it.
**GROUNDED:** 2026-07-28, authored from Andrew-direct + CRO research reference.

---
---

# GROUP 2 — INFRASTRUCTURE

*Two items, stable for reference.*

## INFRASTRUCTURE.TOOLS — enumerated coverage universe per tool   `SUB-GROUP` **v1.3**

*Version history: `v1.0` 2026-07-28 created · `v1.1` +O2 (Andrew-direct response-scope) · `v1.2` CVO state pull 183509Z — attach corrected (+COMPUNIFY), stance grounded on an exercised gate, O2 sharpened*

**Intent:** for every comp-tool, a known and enumerated coverage universe — what it covers, what it
does not, and where its silence means "nothing there" versus "I cannot see that."

**Attaches to (CVO-CORRECTED 183509Z @`8ac1e7d04`):** **`NFRA_COMPUNIFY`** (the owner — see below) ·
`NFRA_MSBEFF` · `NFRA_COMPLEARN` + `NFRA_COMPDRIFT` (the map's own *"one noun, two verbs"* pair,
LD-0227 — structurally attached, not adjacent) · `NFRA_TOOLARCH`, `NFRA_TOOLBHVR`, `NFRA_TOOLCHECK`,
`NFRA_TOOLGRAPH`, `NFRA_TOOLHEALTH`, `NFRA_TOOLHUD`, `NFRA_COMPASSURANCE`, `NFRA_COMPREG`,
`NFRA_COMPROUTE`, `NFRA_SYSPARITY`.
· **`NFRA_COMPRAIL` — reclassified MECHANISM, not scope**: the live enforcement point where a coverage
mismatch becomes catchable.
· **`NFRA_TOOLSEM` — attached but INERT: 4 commits and ZERO code files.** Anything routed there lands
nowhere today. Flagged so nobody dispatches into a hollow project.

> ### ⚠ MY ATTACH LIST OMITTED THE PROJECT THAT *IS* THIS SUB-GROUP — and the reason indicts the method
> `NFRA_COMPUNIFY` owns **`comp-coverage-map.yaml`** (a 1,081-line per-tool ledger) **and** its
> enforcing gate **`comp-coverage-check`**. CVO **exercised** the gate: it **PASSES** — 88 homed tools
> (36 `tools[]` + 52 `meta_tools[]`), 12 `gate_contract` rules, 0 unverifiable, inventory complete.
>
> **I built the attach list from CODE PREFIXES.** `COMPUNIFY`'s name says nothing about tools, so a
> prefix scan cannot see it — **and it is the answer to the sub-group.** That is text-local,
> connection-blind retrieval producing a confident and wrong map: **precisely the failure the comp-rail
> exists to prevent, committed by the agent maintaining the register.** *A register assembled by
> pattern-matching names inherits every blind spot of the names.* **Attach lists get built from
> knowing the work, or they get verified by someone who does.**

```
DECIDED : YES      @ comp-coverage-map.yaml:87-153 -- a 12-rule gate_contract + 4 locked CTO rulings
BUILT   : YES      @ comp-coverage-check EXERCISED 2026-07-28T155xZ (a RUN, not a read), verbatim:
                     "PASS ... 88 homed tool(s) (36 tools[] + 52 meta_tools[]) | 12 gate_contract
                     rule(s), 0 unverifiable | inventory complete."
          NO       @ for the NEGATIVE declaration -- no `excludes:` field exists in the schema.
                     Anchor: CVO @a3dac97be section 2. Beyond COMPUNIFY's charter: a HOLE, not drift.
SERVING : UNASSESSED  -- gate wiring (commit/CI path vs invoke-only) NOT established. DO NOT upgrade
                        this to NO; they are different claims.
```

**PROJECT TABLE — measured 2026-07-28 (CVO).** `code` = distinct files under
`.tools/|org/modules/|infra/|data/`; `doc` = under `docs/|org/tier*|org/projects`.
**The ratio is the ENACTED-vs-RECORDED signal**, which is why both columns are kept.

```
project              status    commits  code  doc
NFRA_SYSPARITY       active      143     43    77
NFRA_TOOLUNIFY       NO-JSON     109     18   113   <-- HOLE
NFRA_COMPLEARN       active       75     22    75
NFRA_TOOLARCH        active       69     24    41
NFRA_COMPRAIL        complete     46     17    23
NFRA_TOOLCHECK       active       45     20    25
NFRA_COMPUNIFY       complete     41      7    29
NFRA_MSBEFF          active       39     25    39
NFRA_TOOLHEALTH      active       29     12    29
NFRA_COMPDRIFT       complete     27     12    12
NFRA_TOOLBHVR        active       10      1     5
NFRA_TOOLGRAPH       active        5     17    14
NFRA_TOOLSEM         active        4      0     1
```
**`NFRA_TOOLGRAPH` is disproportionately relevant to the frontier** — only 5 commits but **17 code
files**, and it already implements the declared-vs-actual diff shape for coupling. Small, real, and
the nearest existing thing to what the frontier needs.

> **`SERVING: UNASSESSED` is the most credible field in this entry.** CVO's stated reason: *"I made
> three false claims about this same project today — 'gate not built,' '36 tools,' 'exclusions written
> nowhere' — all from reading documents instead of exercising them."* A forward-looking S0 header read
> to it as current state. **`UNASSESSED` is it declining to do that a fourth time.** This is exactly
> what the value was made legal for.

**FRONTIER:** wire **PATTERN C (cross-derive) at suite scale** — diff each tool's DECLARED `surface`
against the surface implied by its ENUMERATION PRIMITIVE. **It needs no oracle** (Andrew's explicit
constraint), and `comp-toolgraph` already implements the shape for *coupling*.

### HOLES — and the largest one found so far in this register

> ## `NFRA_TOOLUNIFY` — 109 commits, 18 code files, 113 doc files, **NO PROJECT JSON**
> **The second-largest body of work in the entire tool program, and it has no project code.**
> Verified with a positive control: `NFRA_TOOLARCH.json` is found by the same glob; `TOOLUNIFY` is
> absent. **This is not drift on a delinquent record — there is no record to drift from.**
>
> **It is bigger than `MDPF_CHANNEL_INDEPENDENCE`, which was the example I used to justify the whole
> exercise.** Two holes of this size found on the register's first two population passes, in two
> different mission groups, by two different agents. **The prior is not "assume there are more" — it is
> COO's sharper version: assume the instrument that would find them is the same one that missed these.**

Also holed, no project code covers any: the **negative declaration** (what a tool cannot see *within*
its declared surface) · the **runtime-provenance axis** · **`INFRASTRUCTURE.TOOLS.O2` itself** · **cross-tool
coverage diffing at suite scale** (`comp-toolgraph` does declared-vs-actual for coupling, nothing for
coverage).

**NOT ASSESSED — recorded so it is not read as covered:** gate wiring · `NFRA_COMPASSURANCE` /
`COMPSIMILAR` / `COMPTEAM` (active, unmeasured) · **the remaining 57 of 92 tool enumeration primitives
— UNRESOLVED, not absent.**
**NOTE — why this mission is not cosmetic:** we have repeatedly found tools whose *silence* was read
as *absence*. `comp-iam` reports nothing for whole classes of call and that silence has been the
defect, not the trace. **An unenumerated coverage universe is what makes a tool's silence
uninterpretable.**
**GROUNDED:** 2026-07-28, structure + prior art located. Per-tool coverage NOT enumerated.

### INFRASTRUCTURE.TOOLS.O2 — response scope: high-signal output that is not truncated, redacted or garbled
**Andrew-direct 2026-07-28, and it is a distinct function from coverage:** once the coverage universe
is known, decide **how each tool must work mechanically — namely the scope of how information is
presented.** Big responses get truncated; the output must be high-signal and **not inadvertently
redacted or garbled.**

```
DECIDED : NO       -- no standard exists for how a comp-tool bounds and shapes its output
BUILT   : NO
SERVING : NO
```
> ### CVO'S SHARPENING, ADOPTED — it unifies O2 with coverage instead of letting them drift apart
> **BOUNDING IS NOT THE PROBLEM. UNDECLARED BOUNDING IS.** A tool returning **40 of 400 and saying so**
> is correct and useful. The defect is **truncation the reader cannot detect** — which is *the same
> property as an unenumerated coverage universe*: the output is **byte-identical to the complete one**,
> so the silence is uninterpretable. **O2 is the coverage problem on the OUTPUT side.** Stated that way,
> `INFRASTRUCTURE.TOOLS` carries one doctrine rather than two.

**FRONTIER:** a per-tool **output contract**, four clauses (CVO):
**C1** declare the denominator **in-band** (`showing N of M`, with **M measured BEFORE bounding**) ·
**C2** truncation is a **visible token**, never an absence ·
**C3** an **EMPTY** result must be distinguishable from a **FAILED** retrieval (this folds the
`git show` clean-empty and binary-mode-`grep` classes into one clause) ·
**C4 THE CONTRACT IS THE TOOL'S, NOT THE CALLER'S.**

> **C4 is the load-bearing clause.** All four measured instances came from a **caller's** bounding.
> **A tool that emits its own denominator survives a careless caller; one that does not cannot be made
> safe by discipline** — which is the entire argument for building this into the tools rather than into
> a habit. *Care is not a control, applied to output shape.*
**WHY THIS IS NOT COSMETIC — a truncated response and a complete one are byte-indistinguishable to
the reader.** This is the retrieval-control class the estate already knows by name: `grep` silently
entering binary mode and truncating its own output at exit 0; a `git show` on a bad ref returning
clean-empty stdout that reads as *"file absent."*
**MEASURED INSTANCE, 2026-07-28, MSTR's own — recorded because a self-inflicted one is the honest
kind:** a manifest inspection piped through `head -40` truncated mid-output, and I reported
*"the runner is NOT registered in EC2_MANIFEST"* to Andrew. **It was registered.** I read an absence
out of a truncated retrieval, on a decommission decision. Caught and corrected within one turn, but
**nothing in the output distinguished truncated from complete** — which is precisely the defect this
objective is about.
**FOUR MEASURED INSTANCES IN ONE DAY, TWO AGENTS:**
1. **MSTR's** — `head -40` → I told Andrew the GH-Actions runner was **NOT** in `EC2_MANIFEST.json`. It was.
2. CVO — `--query length(events)` applies **per page**: returned `2,0,0,0,0`, no total.
3. **CVO's, and the sharpest: THE FIX WAS THE DEFECT.** `--no-paginate` truncated to page one and
   reported **1 invocation instead of 4** — turning *"1 of 4, it stopped"* into *"1 of 1, still firing
   every run."* **Opposite verdict, same log, via a flag whose entire purpose is tidier output.**
4. CVO — `head -40` on `comp-clobber`; had to re-run unbounded before the zero could be trusted.

**RELATED STANDING LAW:** *control the RETRIEVAL, not the pattern* · *print the denominator of every
scan you reason from* · **a wrong number is more dangerous than a zero**, because a zero invites
suspicion and a plausible count does not.
**GROUNDED:** 2026-07-28, authored from Andrew-direct + a live self-caught instance.

## INFRASTRUCTURE.GRAPH — canonical taxonomy and resource design patterns   `SUB-GROUP` **v1.2**

*Version history: `v1.0` 2026-07-28 created · `v1.1` CVO state pull 183509Z — class-over-instance framing recorded*

**Intent:** lock in canonical taxonomy and resource design patterns, and sincerely unify the system on
that basis.

**Attaches to:** `OPAL_STNDRD`, `OPAL_TAXONOMY`, `NFRA_ONTOLOGY`, `NFRA_ONTOLOGY2`,
`NFRA_ONTOCLARITY`, `NFRA_GLOBGRPH`, `NFRA_GRAPHS`, `NFRA_GRAPHUNI`, `NFRA_GRAPHDEPTH`,
`NFRA_TSGRAPH`, `NFRA_SEMCTL`, `NFRA_NERVES`, `NFRA_EDGES`.

```
DECIDED : PARTIAL  @ key grammar + naming law + one-capacity-one-service EXIST; NO provenance
                     taxonomy, NO code-location standard. Token census over NFRA_TOOLARCH_PRD.md
                     (116 lines): provenance 0, "Rule 12" 0, "artifact store" 0 --
                     POSITIVE CONTROL: "archetype" 12, so the zeros are real.
BUILT   : PARTIAL  @ exactly ONE live gate -- the .parquet-under-bronze/ bucket-policy deny, on ONE
                     bucket (opal-data-assets, 07-16). Other trees open.
SERVING : PARTIAL  @ 121 scheduled EventBridge Rules vs 10 Scheduler schedules --
                     92% on the NON-STANDARD side of a standard that already exists. Measured live.
```

> **That last number is the sub-group in one line: the standard exists and 92% of the estate is not on
> it.** `DECIDED: PARTIAL` is therefore not the bottleneck — **adoption is.** A taxonomy nobody migrates
> onto is indistinguishable from no taxonomy, and the register should not let "we have a standard" read
> as progress while the ratio sits there.
> ### RECORDED DISAGREEMENT — CVO vs CTO, and the register carries the CLASS version
> Sent by CVO **without reconciling with CTO**, per my instruction that two views of one sub-group is
> signal. CTO's framing was **the INSTANCE**: `mdpf` missing from `PIPELINE_MAP`. CVO's is **the
> CLASS**: Rule-12 conformance makes *every* such tree invisible the same way.
> **The register carries the CLASS.** CVO's reason, adopted: *"the instance fix closes one tree and
> leaves the next to rot identically."* CTO has since accepted the reframe in writing; the disagreement
> is kept on the record anyway, because **an agreement reached after the fact does not retroactively
> make the two framings equivalent** — and the next reader needs to know which one the register means.

**FRONTIER:** lock the taxonomy — one canonical statement that the rest can be migrated onto.
**THE OPERATIVE PROBLEM, in Andrew's framing:** *as the universe grows, we need to track the
enumeration of that coverage so we don't get breaks in, for example, grants and permissions in related
IAMs.* **This is a coverage-tracking problem before it is a modelling problem.** It ties directly into
`DEBT.BACKEND` — the two are one loop, and this register should always show them together.
**GROUNDED:** 2026-07-28, structure + attachment located.

---
---

# GROUP 3 — DEBT

## DEBT.BACKEND — AWS resource and system debt  **[THE FOCUS]**   `SUB-GROUP` **v1.0**

*Version history: `v1.0` 2026-07-28 created*

**Intent:** as Infrastructure consolidates patterns and designs, legacy resources are **actually
decommissioned and terminated** — not left running alongside their replacements.

**Attaches to:** `NFRA_DEBTSCAN` (complete), `MDPF_DEBTCLEAN` (active), `MDPF_MONOCLEANUP`
(superseded), `NFRA_TERRAFORM`, `NFRA_COSTAWS`, `OPAL_CONSOLIDATION`, `DEBT_1STRUN`.

**Andrew's stated cost, and it is an agent-facing cost rather than a dollar one:**
> *"it is very confusing to agents when there are multiple pipelines and paths and buckets and they
> all clobber each other, it is very problematic."*

```
DECIDED : YES      -- decommission-as-you-migrate is the standing direction
BUILT   : PARTIAL  @ NFRA_DEBTSCAN complete; debtscan ledgers live at org/modules/graph/debtscan/
SERVING : PARTIAL  -- no standing mechanism ties a migration to the retirement of what it replaced
```
**FRONTIER:** make retirement a **condition of** a migration rather than a follow-up to it. Today
nothing structurally prevents a replacement from shipping while its predecessor keeps running.
**LIVE EVIDENCE, today, both directions:**
- *Working:* the GitHub Actions EC2 runner recorded its own exit condition at build time
  (`"48-HOUR UNBLOCK, NOT ARCHITECTURE"`) and is being decommissioned on Andrew-direct now that the
  condition fired — LD-0339 amendment 1, `0dee7524e`. **A stopgap that names its own exit and is
  actually retired is the pattern this mission wants.**
- *The problem, exactly as described:* the MDPF legacy writer clobbered the served keys daily from a
  deprecated path, requiring two IAM Deny statements to stop it — and its own manifest entry read
  `"NOT YET APPLIED"` while a live instance existed. **Multiple paths, clobbering, and a stale record
  hiding a live resource, in one incident.**
**GROUNDED:** 2026-07-28, against today's live work.

## DEBT.FRONTEND — portal-level debt   `SUB-GROUP` **v1.0**

*Version history: `v1.0` 2026-07-28 created*

```
DECIDED : n/a   BUILT : n/a   SERVING : n/a
```
**STATUS: NOT A FOCUS.** Andrew-direct: *"Right now we don't need to focus on frontend."*
Logged so the category exists and so its deprioritization is a **recorded decision** rather than an
accident of attention. **Do not open work here without Andrew.**
**GROUNDED:** 2026-07-28, by direction.

---
---

# GROUP 4 — EXTERNAL

*Subdivided by client. Andrew: initiative detail for these is not being specified at this time.*

## EXTERNAL.49FINANCIAL — 49 Financial   `SUB-GROUP` **v1.0**

*Version history: `v1.0` 2026-07-28 created*
**Attaches to:** `ADVI_49*`, `MDPF_3FIRMS`, `NFRA_PPL49F`, `SSCN_PFOE`, `OPAL_TAXSMA*`, `BD_RPSAUTO`.
**Standing constraints that bind anything here:** AUA source is **Schwab** (certified-AUA deprecated,
Andrew-direct 2026-07-24); `0824`/`0833` never added and never substituted; bd↔cot↔inf firm separation
is gate- and IAM-enforced.
```
DECIDED : UNASSESSED   BUILT : UNASSESSED   SERVING : UNASSESSED
```
**GROUNDED:** 2026-07-28, container only. Awaiting Andrew's initiative detail.

## EXTERNAL.INFLECTION — Inflection Wealth Management   `SUB-GROUP` **v1.0**

*Version history: `v1.0` 2026-07-28 created*
**Attaches to:** `ADVI_INF*` (~25 codes), `NFRA_PPLINF`. Source of record: **Orion**.
```
DECIDED : UNASSESSED   BUILT : UNASSESSED   SERVING : UNASSESSED
```
**GROUNDED:** 2026-07-28, container only.

## EXTERNAL.COTTONWOOD — Cottonwood Capital Advisors   `SUB-GROUP` **v1.0**

*Version history: `v1.0` 2026-07-28 created*
**Attaches to:** `ADVI_COT*`, `NFRA_PPLCOT`, `NFRA_COT_RULE15`, `MDPF_COTMDL`, `WSE_COTMDL`,
`AUTH_COTTON`. Source of record: **Black Diamond**.
```
DECIDED : UNASSESSED   BUILT : UNASSESSED   SERVING : UNASSESSED
```
**NOTE:** Andrew wrote *"Cottonwood Capital Advisory"*; the estate and org chart use **"Cottonwood
Capital Advisors."** Using the estate's form for attachment so the codes resolve. **Flagged rather
than silently normalised** — if the legal name is Advisory, the estate is wrong and that is worth
knowing.
**GROUNDED:** 2026-07-28, container only.

---
---

## Register metadata

| field | value |
|---|---|
| created | 2026-07-28, `0.0.0_AB_MSTR`, Andrew-direct |
| groups | 4 (fixed unless Andrew changes them) |
| mission groups | 4 |
| sub-groups (all versioned) | 9 |
| objectives with a measured stance | 5 (`PORTAL.MODEL_PORTFOLIOS.O1`, `PORTAL.MODEL_PORTFOLIOS.O3`, `INFRASTRUCTURE.TOOLS`, `INFRASTRUCTURE.GRAPH`, `DEBT.BACKEND`) |
| objectives `UNASSESSED` | 4 (`PORTAL.ADVISOR_INTELLIGENCE.O1` partial, `EXTERNAL.*` x3) |
| objectives pending Andrew | 1 (`PORTAL.MODEL_PORTFOLIOS.O2` — the AUA aggregation definition) |
| last maintenance pass | 2026-07-28T17:45Z — folded Andrew-direct 174108Z as `PORTAL.MODEL_PORTFOLIOS.O3` |

### Cross-sub-group observation (the kind only this layer surfaces)

`PORTAL.MODEL_PORTFOLIOS.O3` and `PORTAL.ADVISOR_INTELLIGENCE.O1` have **the same frontier**: enumerate, per channel/runner, what
the actual source is and on what schedule it arrives. **Neither is blocked on a decision; both are
blocked on an artifact that does not exist.** Sitting in either project alone it reads as that
project's homework. Seen across sub-groups it is **one missing artifact class — a per-channel
source-and-schedule map — that two separate large initiatives are independently waiting on.**
**CONFIRMED BY CTO 183143Z: it is ONE piece of work, not two — and COO is building it right now** for
Andrew's Part 1. **ADVI MUST NOT COMMISSION A SECOND ONE.** CTO's framing is exact: that would be
*"the parallel-channel pattern we spent today on, reproduced at the project layer instead of the data
layer."* **The register's job here was not to find the work — it was to stop it being done twice.**
Standing note until the artifact exists. Routing stays with CTO and COO.

**Open at Andrew:**
1. `PORTAL.MODEL_PORTFOLIOS.O2` — the AUA aggregation expansion he said he would send.
2. `EXTERNAL.*` — initiative detail per client, when he wants it.
3. Whether "Cottonwood Capital Advisory" or "Advisors" is correct.

**Known gap this register surfaced on day one:** `MDPF_CHANNEL_INDEPENDENCE` — live, load-bearing,
PRD'd, cited in `CLAUDE.md`, and **absent from the project registry entirely.**
