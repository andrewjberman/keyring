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
  SUB-GROUP      the large initiative -- VERSIONED           (PORTAL.MP v1.0, INFRA.GRAPH v1.0, ...)
    OBJECTIVE    a nameable outcome inside it                (PORTAL.MP.O2, ...)
      -> attaches to  macro codes and/or project codes       (many-to-many, non-exclusive)
```

| level | examples | versioned? |
|---|---|---|
| **Mission Group** | `Portal`, `Infrastructure`, `Debt`, `External` | no — these are stable |
| **Sub-group** | `Advisor Intelligence` under Portal · `Backend` under Debt | **YES** |
| **Objective** | `PORTAL.MP.O3` | no — versioned by its parent |

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
---

# GROUP 1 — PORTAL

*Major initiatives spanning portal product surfaces and the backend/pipelines behind them.*

## PORTAL.MP — Model Portfolios   `SUB-GROUP` **v1.1**

*Version history: `v1.0` 2026-07-28 created · `v1.1` 2026-07-28 +O3 (Andrew-direct 174108Z channel-trace)*

**Intent:** the Model Portfolios product serves correct, canonical numbers from canonical pipelines,
every day, without hand-restoration.

**Attaches to:** `MDPF_*` (macro) — `MDPF_REVAMP` (complete), `MDPF_3FIRMS` (active),
`MDPF_DEBTCLEAN` (active), `MDPF_MONOCLEANUP` (superseded), `MDPF_OWNTS`, `MDPF_CADENCE`,
`MDPF_COUNTS`, `MDPF_BASISSWITCH`, `MDPF_SCOPED`, `MDPF_VARFLAG`, `MDPF_COTMDL`, `MDPF_ASSETS` ·
plus `OPAL_CONSOLIDATION`, `ETFS_*`, `OPAL_TAXSMA*`, `SSCN_PFOE`.

### PORTAL.MP.O1 — Lock in the canonical pipelines
```
DECIDED : YES      @ Andrew-direct 2026-07-28 ~1427Z (canonical non-model basis) + ~1710Z
                     (deprecate legacy, move full force to REVAMP canonical) -- LD-0339 amend,
                     bf986d81a
BUILT   : PARTIAL  @ REVAMP producer satisfies the 0824 canonical EXACT 3/3 (DT trace f68266a2d);
                     correct 3-firm gold exists at gold/mdpf_revamp/global/
SERVING : NO       @ serve is a hand-restored 07-23 artifact fed by NEITHER producer; both
                     portal-v2 Deny statements production-exercised 2026-07-28 16:44Z
```
**FRONTIER:** a publisher that puts `gold/mdpf_revamp/*` on the served keys. It does not exist —
AE's leg-b is **design-only** by its own commit message (13:02Z, *"DESIGN ONLY, nothing built"*).
**BLOCKED-ON:** `1.0.0_SA_CTO` — sequencing. Deprecating legacy removes the only producer ever wired
to serve, and its replacement is unbuilt. **This is the live sovereign-class exposure in this mission.**
**GROUNDED:** 2026-07-28, against live serve state + commit trail.

### PORTAL.MP.O2 — The Opal AUA aggregation definition  *(PENDING — Andrew to expand)*
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

### PORTAL.MP.O3 — Every channel traced to the Gold DDB: what feeds it, on what schedule, and whether it arrives
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
DECIDED : YES      @ Andrew-direct 174108Z + the ~1725Z priority ruling c60de93156
BUILT   : NO       -- no per-channel feed+schedule+arrival enumeration exists as an artifact
SERVING : NO
```
**FRONTIER:** the enumeration itself — per channel, its feeder, its schedule, and evidence it lands in
the Gold DDB. **Note this is the same shape as `PORTAL.ADVI.O1`'s frontier** (enumerate what each gold
runner actually reads). Two missions, one missing artifact class: **we do not have a per-channel
source-and-schedule map anywhere.** That is worth seeing as one gap rather than two.
**BLOCKED-ON:** `1.0.0_SA_CTO` as PRD owner; COO holds the decomposition.
**RELATED STANDING LAW:** a pipeline whose only trigger is another pipeline's success **has no
schedule and is a defect** — it freezes silently when its upstream breaks. This objective is the
direct remedy for that class, and `mdpf-daily-trigger` is a live instance of it.
**GROUNDED:** 2026-07-28, from the sovereign record. Nothing enumerated yet.

### ⚠ PORTAL.MP — REGISTRY GAP FOUND AT AUTHORING (this is the register earning its keep)
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

## PORTAL.ADVI — Advisor Intelligence   `SUB-GROUP` **v1.0**

*Version history: `v1.0` 2026-07-28 created*

**Intent:** Advisor Intelligence runs on canonical, channel-correct sources, with performance and
attribution computed our own way — reliably, every day.

**Attaches to:** `ADVI_*` (macro, ~90 project codes) · `OPAL_ASSETS`, `OPAL_CONSOLIDATION`,
`NFRA_PPL49F`, `NFRA_PPLINF`, `NFRA_PPLCOT`.

### PORTAL.ADVI.O1 — Gold Runners source from the channel's `opal-data-assets` silver
```
DECIDED : YES      @ OPAL_CONSOLIDATION is the ratified P0 master; the assets grammar is live
                     (s3://opal-data-assets, {source}/{scope}/{layer}/{type|feed}/{date})
BUILT   : UNASSESSED  -- per-runner migration state not yet enumerated by MSTR
SERVING : UNASSESSED
```
**FRONTIER:** enumerate, per gold runner, which silver source it actually reads today. That
enumeration does not exist as a single artifact — building it is the next move, and it is cheap.
**GROUNDED:** 2026-07-28, structure only. **Deliberately `UNASSESSED`, not `NO`.**

### PORTAL.ADVI.O2 — Canonical performance + attribution: 365-day TWR, gross and net, daily
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

## INFRA.TOOLS — enumerated coverage universe per tool   `SUB-GROUP` **v1.0**

*Version history: `v1.0` 2026-07-28 created*

**Intent:** for every comp-tool, a known and enumerated coverage universe — what it covers, what it
does not, and where its silence means "nothing there" versus "I cannot see that."

**Attaches to:** `NFRA_TOOLARCH`, `NFRA_TOOLBHVR`, `NFRA_TOOLCHECK`, `NFRA_TOOLGRAPH`,
`NFRA_TOOLHEALTH`, `NFRA_TOOLHUD`, `NFRA_TOOLSEM`, `NFRA_COMPRAIL`, `NFRA_COMPASSURANCE`,
`NFRA_COMPREG`, `NFRA_COMPROUTE`, `NFRA_SYSPARITY`.

```
DECIDED : PARTIAL  -- extensive prior art exists across the NFRA_* projects above; Andrew has
                      discussed the shape with 3.0.0_SA_CVO. Not consolidated into one target
BUILT   : PARTIAL  @ comp-manifest-check enforces a registration invariant; the registries carry
                      the true tool count; comp-which routes ~68 tools
SERVING : PARTIAL
```
**FRONTIER:** the consolidated statement of the target — Andrew was explicit that the details already
exist inside those NFRA projects, so **the work is consolidation, not discovery.**
**NOTE — why this mission is not cosmetic:** we have repeatedly found tools whose *silence* was read
as *absence*. `comp-iam` reports nothing for whole classes of call and that silence has been the
defect, not the trace. **An unenumerated coverage universe is what makes a tool's silence
uninterpretable.**
**GROUNDED:** 2026-07-28, structure + prior art located. Per-tool coverage NOT enumerated.

## INFRA.GRAPH — canonical taxonomy and resource design patterns   `SUB-GROUP` **v1.0**

*Version history: `v1.0` 2026-07-28 created*

**Intent:** lock in canonical taxonomy and resource design patterns, and sincerely unify the system on
that basis.

**Attaches to:** `OPAL_STNDRD`, `OPAL_TAXONOMY`, `NFRA_ONTOLOGY`, `NFRA_ONTOLOGY2`,
`NFRA_ONTOCLARITY`, `NFRA_GLOBGRPH`, `NFRA_GRAPHS`, `NFRA_GRAPHUNI`, `NFRA_GRAPHDEPTH`,
`NFRA_TSGRAPH`, `NFRA_SEMCTL`, `NFRA_NERVES`, `NFRA_EDGES`.

```
DECIDED : PARTIAL  -- the intent is stated across OPAL_STNDRD / OPAL_TAXONOMY and others; a single
                      canonical taxonomy is not locked
BUILT   : PARTIAL  @ comp-kuzu, the global graph, comp-system parity checking all live
SERVING : PARTIAL
```
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

## EXT.49F — 49 Financial   `SUB-GROUP` **v1.0**

*Version history: `v1.0` 2026-07-28 created*
**Attaches to:** `ADVI_49*`, `MDPF_3FIRMS`, `NFRA_PPL49F`, `SSCN_PFOE`, `OPAL_TAXSMA*`, `BD_RPSAUTO`.
**Standing constraints that bind anything here:** AUA source is **Schwab** (certified-AUA deprecated,
Andrew-direct 2026-07-24); `0824`/`0833` never added and never substituted; bd↔cot↔inf firm separation
is gate- and IAM-enforced.
```
DECIDED : UNASSESSED   BUILT : UNASSESSED   SERVING : UNASSESSED
```
**GROUNDED:** 2026-07-28, container only. Awaiting Andrew's initiative detail.

## EXT.IWM — Inflection Wealth Management   `SUB-GROUP` **v1.0**

*Version history: `v1.0` 2026-07-28 created*
**Attaches to:** `ADVI_INF*` (~25 codes), `NFRA_PPLINF`. Source of record: **Orion**.
```
DECIDED : UNASSESSED   BUILT : UNASSESSED   SERVING : UNASSESSED
```
**GROUNDED:** 2026-07-28, container only.

## EXT.CCA — Cottonwood Capital Advisors   `SUB-GROUP` **v1.0**

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
| objectives with a measured stance | 5 (`PORTAL.MP.O1`, `PORTAL.MP.O3`, `INFRA.TOOLS`, `INFRA.GRAPH`, `DEBT.BACKEND`) |
| objectives `UNASSESSED` | 4 (`PORTAL.ADVI.O1` partial, `EXT.*` x3) |
| objectives pending Andrew | 1 (`PORTAL.MP.O2` — the AUA aggregation definition) |
| last maintenance pass | 2026-07-28T17:45Z — folded Andrew-direct 174108Z as `PORTAL.MP.O3` |

### Cross-sub-group observation (the kind only this layer surfaces)

`PORTAL.MP.O3` and `PORTAL.ADVI.O1` have **the same frontier**: enumerate, per channel/runner, what
the actual source is and on what schedule it arrives. **Neither is blocked on a decision; both are
blocked on an artifact that does not exist.** Sitting in either project alone it reads as that
project's homework. Seen across sub-groups it is **one missing artifact class — a per-channel
source-and-schedule map — that two separate large initiatives are independently waiting on.**
Surfaced, not sized; routing stays with CTO and COO.

**Open at Andrew:**
1. `PORTAL.MP.O2` — the AUA aggregation expansion he said he would send.
2. `EXT.*` — initiative detail per client, when he wants it.
3. Whether "Cottonwood Capital Advisory" or "Advisors" is correct.

**Known gap this register surfaced on day one:** `MDPF_CHANNEL_INDEPENDENCE` — live, load-bearing,
PRD'd, cited in `CLAUDE.md`, and **absent from the project registry entirely.**
