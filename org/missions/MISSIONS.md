# MISSIONS — Opal mission register

    GENERATED ARTIFACT -- do NOT edit. `comp-missions compile` regenerates this file.
    Every sentence below is SELECTED from a state.yaml or execsum.yaml, never composed
    here: a compiler that writes prose is a compiler that can invent a stance.

    ANCHOR COMMIT   a11b8e2cc3
    ANCHOR TIME     2026-07-28T17:21:56-04:00   (author-time, not a wall clock)
    ANCHOR AUTHOR   0.7.0_AE_CloudOps
    ORDERING        activity intensity -- commits in the last 14 days, then total
    SOURCE          org/missions/{GROUP}/{SUB_GROUP}/{state,execsum}.yaml

> **If the anchor is not HEAD, this file is history rather than state.** Re-run `comp-missions emit && comp-missions compile`.

## ROOT GOAL

*approved v1 by Andrew Berman (sovereign), 2026-07-28T200316Z*

> Run Opal's handful of very large-scale initiatives as durable intents that sit ABOVE the Macro/Project Registry -- attached to it but explicitly not 1:1 -- so that the state of each, the projects beneath it, the holes no project covers, and the assignment of agents to it can all be read without a briefing. Sometimes an initiative is close to a single project; sometimes it aggregates many project codes; sometimes it aggregates macro codes across disparate macros. The register exists so that running four of these at once does not require the sovereign to reconstruct state per topic.

---

## Priority board — ordered by activity intensity

| # | sub-group | recent | total | authors | DECIDED | BUILT | SERVING | blocked on |
|---|---|---|---|---|---|---|---|---|
| 1 | `INFRASTRUCTURE.GRAPH` | **357** | 1090 | 35 | PARTIAL | PARTIAL | PARTIAL | — |
| 2 | `INFRASTRUCTURE.DEBT` | **157** | 1679 | 42 | YES | PARTIAL | PARTIAL | — |
| 3 | `PORTAL.MODEL_PORTFOLIOS` | **147** | 398 | 17 | YES | YES | NO | 1.0.0_SA_CTO -- an architecture call that PR |
| 4 | `INFRASTRUCTURE.TOOLS` | **119** | 730 | 37 | YES | YES | UNASSESSED | 1.0.0_SA_CTO -- TWO calls CVO explicitly did |
| 5 | `PORTAL.ADVISOR_INTELLIGENCE` | **34** | 1726 | 36 | PARTIAL | UNASSESSED | UNASSESSED | — |
| 6 | `PORTAL.DEBT` | **2** | 2 | 2 | PARTIAL | NO | NO | — |
| 7 | `EXTERNAL.49FINANCIAL` | **0** | 0 | 0 | UNASSESSED | UNASSESSED | UNASSESSED | Andrew -- per-client initiative detail. |
| 8 | `EXTERNAL.ALONGSIDE` | **0** | 0 | 0 | UNASSESSED | UNASSESSED | UNASSESSED | — |
| 9 | `EXTERNAL.COTTONWOOD` | **0** | 0 | 0 | UNASSESSED | UNASSESSED | UNASSESSED | Andrew -- per-client initiative detail. |
| 10 | `EXTERNAL.INFLECTION` | **0** | 0 | 0 | UNASSESSED | UNASSESSED | UNASSESSED | Andrew -- per-client initiative detail. |

**PROSE STALE (a commit landed after the summary was written):** `PORTAL.MODEL_PORTFOLIOS`, `PORTAL.DEBT`, `PORTAL.ADVISOR_INTELLIGENCE`, `INFRASTRUCTURE.TOOLS`, `INFRASTRUCTURE.DEBT`, `INFRASTRUCTURE.GRAPH`, `EXTERNAL.ALONGSIDE`, `EXTERNAL.49FINANCIAL`, `EXTERNAL.INFLECTION`, `EXTERNAL.COTTONWOOD`

---

## INFRASTRUCTURE.GRAPH — Canonical taxonomy and resource design patterns

**GOAL** — *approved v1 by Andrew Berman (sovereign), 2026-07-28T200316Z*

> Lock in a canonical taxonomy and canonical resource design patterns, and unify the system on that basis in earnest; and track the enumeration of that coverage as the universe grows, so that related grants and permissions in IAM do not silently break.

    activity   357 commit(s) in the last 14 days · 1090 total · 35 author(s)
    newest     2026-07-28T17:15:04-04:00
    stance     DECIDED PARTIAL · BUILT PARTIAL · SERVING PARTIAL
    version    v1.2

**FRONTIER —** Lock the taxonomy -- one canonical statement the rest can be migrated onto. But note the 92% figure reframes the bottleneck: DECIDED is not what is holding this, ADOPTION is.


































The standard exists and the estate is not on it. That is the sub-group in one line, and it means the
bottleneck is ADOPTION, not decision.

SERVING is PARTIAL on a hard number: 121 scheduled EventBridge Rules against 10 Scheduler schedules.
92% of the estate sits on the non-standard side of a standard that already exists. A taxonomy nobody
migrates onto is indistinguishable from no taxonomy, and this register must not let "we have a
standard" read as progress while that ratio holds.

DECIDED is PARTIAL and the gaps are specific: key grammar, naming law and one-capacity-one-service
exist; there is NO provenance taxonomy and NO code-location standard. That was measured by token
census with a positive control, so the zeros are real zeros.

BUILT is PARTIAL on exactly one live gate -- the parquet-under-bronze bucket-policy deny, on ONE
bucket. Other trees remain open.

A recorded disagreement stands here rather than being reconciled away. CTO framed the instance --
one tree missing from a map. CVO framed the class -- Rule-12 conformance makes every such tree
invisible identically. THE REGISTER CARRIES THE CLASS, because the instance fix closes one tree and
leaves the next to rot the same way. CTO has since accepted the reframe; the disagreement stays on
the record anyway, because agreement reached afterwards does not make two framings equivalent.

1,088 commits and no live capacity assigned. This is one of the two sub-groups named joint-highest
priority that received nothing today.

*grounded: 2026-07-28 -- CVO state pull @8ac1e7d04, live EventBridge/Scheduler counts, token census with positive control.*

---

## INFRASTRUCTURE.DEBT — AWS resource and system debt

**GOAL** — *approved v1 by Andrew Berman (sovereign), 2026-07-28T200316Z*

> Ensure that as Infrastructure consolidates patterns and improves design, legacy AWS resources are appropriately decommissioned and terminated -- so agents are never confronted with multiple pipelines, paths and buckets that clobber each other.

    activity   157 commit(s) in the last 14 days · 1679 total · 42 author(s)
    newest     2026-07-28T17:21:56-04:00
    stance     DECIDED YES · BUILT PARTIAL · SERVING PARTIAL
    version    v1.1

**FRONTIER —** Make retirement a CONDITION of a migration rather than a follow-up to it. Nothing structurally prevents a replacement shipping while its predecessor keeps running.


































1,675 commits, and today's slice was the only one in the whole tree that was purely ENACTED rather
than recorded -- five commits, all code, zero doc. That is the right shape for a debt mission.

DECIDED is YES: decommission-as-you-migrate is standing direction, and the stated cost is
agent-facing rather than financial -- multiple pipelines and paths and buckets that clobber each
other are confusing to agents and very problematic.

SERVING is PARTIAL and the reason is structural: there is NO standing mechanism tying a migration to
the retirement of what it replaced. Nothing prevents a replacement shipping while its predecessor
keeps running. The frontier is to make retirement a CONDITION of a migration rather than a follow-up
to it.

Both directions were live today. Working: the GitHub Actions EC2 runner recorded its own exit
condition at build time and is being decommissioned now that the condition fired -- a stopgap that
named its own exit and was actually retired. Broken: the MDPF legacy writer clobbered served keys
daily from a deprecated path, needed two IAM Denies to stop, and its manifest entry read NOT YET
APPLIED while a live instance existed. Multiple paths, clobbering, and a stale record hiding a live
resource, in one incident.

Holes: OPAL_SCHEDULE and OPAL_ALERTS were briefed and MEASURED against live AWS -- 151 triggers, 51
alarms -- with project creation handed to CTO four days ago. Neither exists. The alarm-map census is
absent while its trigger twin exists complete with a CI drift gate. NFRA_DEBTSCAN declares two
follow-ons open under a COMPLETE status, with its own warning that a debt-scanner rots if never re-run.

Open and NOT adjudicated: Andrew named OPAL_TAXONOMY and OPAL_STNDRD as constituents here; the index
files both under INFRASTRUCTURE.GRAPH. Both statements are on the record and they disagree.

**HOLES — live work no project code covers (4):**
- OPAL_SCHEDULE and OPAL_ALERTS -- BRIEFED, MEASURED, NEVER REGISTERED. CVO's preempting brief (org/tier1_exec/3.0.0_SA_CVO/deliverables/OPAL_SCHEDULE_AND_ALERTS_PREEMPTING_BRIEF_20260724.md @6543fd12ef) enumerated 151 live triggers and 51 live alarms against live AWS on 07-24 and handed project creation to CTO. Four days on, neither code exists. POSITIVE CONTROLS: the project glob returns 16 OPAL_* files; the doc glob finds STNDRD/TAXONOMY/CONSOLIDATION but 0 for alert|monitor|notif|alarm across 378 architecture docs.
- alarm-map.json -- deliverable #1 of that brief. The TRIGGER twin exists (trigger-map.json + trigger-census.py + a CI drift workflow); the ALARM one does not.
- The GitHub Actions EC2 runner decommission has no project carrier -- it is carried by a ledger (LD-0339), a handoff deliverable and live TF, but no project JSON.
- NFRA_DEBTSCAN's own phase declares two follow-ons NOT closed under a 'complete' status, incl. the nightly trend/burn-down, with its own warning: 'a debt-scanner ROTS if never re-run.'

*grounded: 2026-07-28 -- subagent registry sweep + live-AWS figures from the CVO brief.*

---

## PORTAL.MODEL_PORTFOLIOS — Model Portfolios

**GOAL** — *approved v1 by Andrew Berman (sovereign), 2026-07-28T200316Z*

> Lock in the proper canonical pipelines for the Model Portfolios product so it serves correct numbers every day without hand-restoration; and establish the Opal-level definition of how the four AUA types aggregate -- ETF Models (the 5 archetypal portfolios), SMA Strategies (TAX SMA, the incoming MUNI SMA, 49F SMAs tracked in SmartX such as PFOE), Custom Models (client-specific SMAs that are not a larger strategy), and Non-Model Residual (assets we advise upon that fall into none of the prior three).

    activity   147 commit(s) in the last 14 days · 398 total · 17 author(s)
    newest     2026-07-28T17:11:02-04:00
    stance     DECIDED YES · BUILT YES · SERVING NO
    version    v1.2

**FRONTIER —** The defined publisher. Nothing automated writes the serve.

**BLOCKED ON —** 1.0.0_SA_CTO -- an architecture call that PRECEDES the build: which serving namespace is canonical.


































The producer is FIXED and the serve is NOT. That is the whole state in one line.

DECIDED and BUILT are both YES. The scheduled path produced a correct 3-firm Global at 16:48:04Z --
450 dates, cottonwood present at 47 slots, sum identity 0 failing of 426 tested where it had been
425/425 FAILING, and opal_aggregate_aua at 2026-07-22 exact to the cent at $1,951,676,164.42. That
BUILT is anchored on the RUN, not on the producer landing: a two-leg builder is structurally
incapable of that result, which is what makes the run discriminating and the commit not.

SERVING is NO and must stay NO. What is on the client surface is a hand-restored 07-23 artifact fed
by NEITHER producer. Both portal-v2 Deny statements are production-exercised. The serve is a
human-published object and no automated path writes it -- a good day does not make that a mechanism.

The frontier is the defined publisher, and it is blocked on an architecture call that PRECEDES the
build: which serving namespace is canonical. Not blocked on Andrew, not blocked on a lane.

Two registry holes underneath: MDPF_CHANNEL_INDEPENDENCE (PRD'd, cited as law, drove today's P0, no
JSON, no registry row -- confirmed three times independently) and MDPF_COT_CONVENTION_PARITY, a
SECOND live MDPF PRD with no code, chartered five days after the first. Six served objects under
json/portfolios/ have no owner and unknown consumers.

Pending at Andrew and deliberately unstarted: the Opal-level AUA aggregation definition. Zero of its
four categories has a project that owns the aggregation, and "MUNI SMA" occurs exactly once in the
entire repository -- in Andrew's own sentence in this register.

**HOLES — live work no project code covers (2):**
- MDPF_CHANNEL_INDEPENDENCE -- PRD'd (docs/architecture/MDPF_CHANNEL_INDEPENDENCE_PRD.md), cited as law in CLAUDE.md Rule 20/NEVER#4, drove today's P0. NO project JSON, ZERO REGISTRY.md rows. Confirmed independently THREE times (MSTR authoring, CVO /spot-check F-1, CTO state pull).
- Six unaccounted served objects under json/portfolios/: latest, manifest, metrics, summary, timeseries, non_model_assets_preview. No owner, no project, unknown consumers.

*grounded: 2026-07-28T183143Z -- CTO state pull, against the 16:48:04Z scheduled run + commit trail.*

---

## INFRASTRUCTURE.TOOLS — Enumerated coverage universe per tool

**GOAL** — *approved v1 by Andrew Berman (sovereign), 2026-07-28T200316Z*

> Establish an enumerated coverage universe per tool -- what each tool covers, what it does not, and where its silence means nothing-there rather than cannot-see -- consolidating the extensive prior art already held in the NFRA projects; and define how each tool must present information so that responses are high-signal and never inadvertently truncated, redacted or garbled.

    activity   119 commit(s) in the last 14 days · 730 total · 37 author(s)
    newest     2026-07-28T16:43:27-04:00
    stance     DECIDED YES · BUILT YES · SERVING UNASSESSED
    version    v1.3

**FRONTIER —** Wire comp-which to IMPORT tool_index instead of re-parsing the manifest. Cheap, and it is now the single next thing -- until it lands, the compiled index is a fast artifact nobody reads. (The suite-scale declared-vs-actual diff remains real but is downstream of this, and is now cheaper because per-tool primitive rows persist as JSON.)

**BLOCKED ON —** 1.0.0_SA_CTO -- TWO calls CVO explicitly did NOT make: (a) the comp-which wiring, and (b) whether this 5th registry should FOLD INTO comp-coverage-map.yaml, which already has a passing gate it would inherit. Both routed to him in the same window.


































The coverage universe is now ENUMERATED and that is a real close, not a claim. 93 of 93 comp-* tools
classified by enumeration primitive, UNRESOLVED zero, against a re-runnable resolver rather than a
one-shot assertion. The inventory gate was EXERCISED, not read.

The denominator that matters is 90, not 93. Three tools legitimately enumerate nothing -- a writer,
a binary reader, a test harness. "No primitive" and "not an enumerator" are different verdicts and
only the first is a gap; recording 93 would show three uncovered tools that do not exist.

SERVING stays UNASSESSED: whether the gate is wired into a commit path or is invoke-only was never
established, and CVO declined to guess after making three false claims about this same project
earlier the same day from reading documents instead of exercising them.

The finding worth carrying is one CVO surfaced against ITSELF. Its classifier had no SIMULATE
primitive -- the mechanism it had documented four hours earlier as the strongest we have. Three
affected tools came back UNRESOLVED and announced themselves. Three others resolved on other
primitives and READ AS FULLY CLASSIFIED while their strongest mechanism was invisible.
AN UNRESOLVED TOOL ANNOUNCES ITSELF; AN UNDER-CLASSIFIED ONE READS AS COMPLETE. That is a hole that
was hiding inside a field that read covered, which is precisely what this sub-group exists to catch.

BUILT = YES is correct for the CENSUS being complete. It is NOT a claim that the taxonomy is CLOSED.
The primitive list is ten entries and is not provably exhaustive -- the SIMULATE miss is the proof
that a missing entry is silent, so an eleventh would fail identically.

The frontier got cheaper rather than closer: per-tool primitive rows now persist as JSON, so the
excludes: field can be populated mechanically from the primitive. That was the blocker and it is gone.

**HOLES — live work no project code covers (7):**
- NFRA_TOOLUNIFY -- 109 commits, 18 code files, 113 doc files, NO PROJECT JSON. Second-largest body of work in the tool program. Positive-controlled: the same glob finds NFRA_TOOLARCH.json.
- The NEGATIVE declaration -- what a tool cannot see WITHIN its declared surface.
- The runtime-provenance axis.
- INFRASTRUCTURE.TOOLS.O2 itself (response scope / output contract).
- Cross-tool coverage diffing at suite scale -- comp-toolgraph does declared-vs-actual for COUPLING, nothing for COVERAGE.
- comp-which RE-PARSES 133KB OF YAML PER CALL -- yaml.safe_load x10, ~97% of runtime (measured by 0.8.0_AE_CloudComp~B with cProfile, 07-24) -- ON THE TOOL CLAUDE.md RULE 21 MANDATES AS THE FIRST REFLEX FOR EVERY SEARCH. CVO built the fix (a compiled index: 0.4ms warm import vs 2,870ms, 7,726x) BUT THE WIRING IS NOT ITS CALL. Live work, no project code, no named owner. UNTIL IT LANDS THIS IS A FAST ARTIFACT NOBODY READS.
- UNDER-CLASSIFICATION IS INVISIBLE, and it was found INSIDE a field that read COVERED. CVO's classifier had NO SIMULATE primitive -- the pattern CVO itself documented four hours earlier as the strongest enumeration mechanism we have. Five tools use it: three came back UNRESOLVED and so announced themselves, but comp-which, comp-whoread and comp-deadgrant RESOLVED ON OTHER PRIMITIVES and read as fully classified while their strongest mechanism was invisible. >> AN UNRESOLVED TOOL ANNOUNCES ITSELF; AN UNDER-CLASSIFIED ONE READS AS COMPLETE. <<

*grounded: 2026-07-28T192952Z -- CVO resolved primitive census, re-runnable anchor.*

---

## PORTAL.ADVISOR_INTELLIGENCE — Advisor Intelligence

**GOAL** — *approved v1 by Andrew Berman (sovereign), 2026-07-28T200316Z*

> Complete the migration whereby the Gold Runners source from the opal-data-assets silver buckets relevant to their channel; then canonize the logic across the various data shapes -- above all performance reporting and attribution on a 365-day calendar Total Weighted Return basis, gross and net, reliably every single day -- so that Opal supplants Black Diamond and Orion rather than depending on them.

    activity   34 commit(s) in the last 14 days · 1726 total · 36 author(s)
    newest     2026-07-24T13:05:07-04:00
    stance     DECIDED PARTIAL · BUILT UNASSESSED · SERVING UNASSESSED
    version    v1.1

**FRONTIER —** Enumerate, per gold runner, which silver source it actually reads today. The artifact does not exist. SHARED with PORTAL.MODEL_PORTFOLIOS.O3 -- CTO confirmed it is ONE piece of work, not two, and COO is building it. ADVI MUST NOT COMMISSION A SECOND ONE.


































The largest commit volume in the tree and the least established state. Those two facts belong
together: 1,726 commits is channel and pipeline work landing steadily, and none of it has been
assessed against what this sub-group is actually FOR.

DECIDED is PARTIAL. The basis is set -- 365-day calendar TWR, gross and net, daily, Account365
pinned because it is defensible to refer to. The METHOD PER SOURCE is not set, and the per-source
data-availability analysis has never been done. That analysis is the frontier and everything
downstream is unanswerable until it exists.

BUILT and SERVING are UNASSESSED, deliberately, and that is not NO. Nobody has enumerated which
silver source each gold runner actually reads today.

The hole here is the largest single gap the register has found: THE BD-REPLACEMENT TOTAL-RETURN
BUILD HAS NO PROJECT CODE. CRO's research is delivered and the build is held at registration. A
TWR keyword search across all 281 project JSONs returns five hits and every one is terminal --
ZERO ACTIVE PROJECTS mention TWR. The strategic intent to supplant Black Diamond and Orion
currently has no registry carrier at all.

The frontier is SHARED with PORTAL.MODEL_PORTFOLIOS: one per-channel source-and-schedule artifact,
not two. CTO confirmed it, COO is building it, and this sub-group must not commission a second.

**HOLES — live work no project code covers (2):**
- THE BD-REPLACEMENT TOTAL-RETURN BUILD (fact_account_return) -- NO PROJECT JSON. CRO research is DELIVERED (RCN-0001, org/tier1_exec/4.0.0_SA_CRO/briefs/MASTER_BLACK_DIAMOND_ANALYSIS.md); the build is HELD at CTO registration. RECON_REGISTER.md:105-106 states it verbatim: 'no project JSON registered under any BDX/total-return code'. POSITIVE CONTROL: a TWR/time-weighted keyword search across ALL 281 project JSONs returns 5 hits, ALL TERMINAL -- ZERO ACTIVE PROJECTS mention TWR. This is scope clause (c) with no registry carrier.
- The per-runner silver-source enumeration (the frontier above) has no owner code. Nearest is OPAL_GLDRNS, whose phase names Wave-3 TO cuts and closed backfill -- it does not claim this.

*grounded: 2026-07-28 -- subagent registry sweep, 281 JSONs parsed, 0 parse failures.*

---

## PORTAL.DEBT — Portal-level debt

**GOAL** — *approved v1 by Andrew Berman (sovereign), 2026-07-28T200316Z*

> Retire portal-level debt: establish which non-canonical API routes are actually displayed rather than merely generated, then deprecate what is dead and migrate only what is live, leaving /api/general/ and /api/scoped/ as the canonical namespaces. LOW priority by standing instruction.

    activity   2 commit(s) in the last 14 days · 2 total · 2 author(s)
    newest     2026-07-28T14:43:39-04:00
    stance     DECIDED PARTIAL · BUILT NO · SERVING NO
    version    v1.1
    priority   LOW -- Andrew-direct 2026-07-28. Recorded so the deprioritization is a DECISION, not an accident of attention. Do not open work here without Andrew.

**FRONTIER —** Answer Andrew's own hypothesis -- GENERATED != DISPLAYED. Early evidence supports it, and if it holds most of this debt can be deleted rather than migrated.


































LOW priority by sovereign instruction, and that is a decision on the record rather than an accident
of attention. Two commits, brief only, not decomposed, not staffed.

The canonical model is already set: /api/general/ and /api/scoped/ are canonical and everything else
is debt. DT enumerated the surface in full -- 24 cache behaviors plus one default on the live
distribution, 18 canonical and 5 not, with unauth probes. /json-tiered/* answers 200 UNAUTH with
zero portal clients.

The frontier is Andrew's own hypothesis, and it is the cheapest question here: GENERATED IS NOT
DISPLAYED. Early evidence supports it. If it holds, most of this debt gets deleted rather than
migrated, which is why investigation precedes any migration work.

This mission finishes a migration already begun; the precedent is recorded in-source.

*grounded: 2026-07-28 -- DT brief, live CloudFront config, denominator enumerated in full.*

---

## EXTERNAL.49FINANCIAL — 49 Financial

**GOAL** — *approved v1 by Andrew Berman (sovereign), 2026-07-28T200316Z*

> Client-facing NON-PORTAL work for 49 Financial. PROSPECTIVE -- no initiative detail specified yet.

    activity   0 commit(s) in the last 14 days · 0 total · 0 author(s)
    newest     — no activity —
    stance     DECIDED UNASSESSED · BUILT UNASSESSED · SERVING UNASSESSED
    version    v1.1

**BLOCKED ON —** Andrew -- per-client initiative detail.


































PROSPECTIVE. Zero commits is the CORRECT reading, not a gap.

Andrew-direct: no true external work has been done yet -- this is a new category for NON-PORTAL
work. The path globs here are deliberately EMPTY rather than narrow, because a container for work
that does not exist should match nothing, and an empty match set is honest where a plausible one is
not.

This matters because an earlier version of this index globbed per-firm project prefixes into
EXTERNAL and manufactured a 238-commit cross-group overlap that was a property of the index rather
than of the estate. A per-firm PREFIX is not non-portal client work. That error is corrected and
recorded so nobody restores the globs believing they are fixing a coverage gap.

Nothing is blocked. Awaiting Andrew's per-client initiative detail.

Source of record when work begins: SCHWAB (certified-AUA deprecated 2026-07-24).

**HOLES — live work no project code covers (1):**
- THE RECURRING 49F SCHWAB SILVER CONVERSION HAS NO OWNING PROJECT. A codified, AE-owned, recurring 7-step procedure (.claude/skills/49-schwab-conv/SKILL.md) rolling SIX silver tables forward (ACC, RPS, TRN, TRN-NNA, ULN, RLD). Its ONLY registry mention is BD_RPSAUTO.json -- status CANCELLED, and cancelled explicitly on the 2026-07-09 standing prohibition which MEMORY.md records as LIFTED COMPLETELY on 07-14. THE CANCELLATION'S STATED BASIS IS RETRACTED AND THE ENTRY WAS NEVER REVISITED. Now load-bearing, because 49F's AUA source is Schwab. DENOMINATORS: 'convert_schwab' = 1 hit across all 281 JSONs (the cancelled one), 0 across the 100 non-terminal. POSITIVE CONTROLS: sibling token 'sync_schwab_onedrive' = 3 / 2; 'Cottonwood' = 34 / 16. PARTIAL COVER, stated precisely: DATA_SSOTMG + DATA_PLATFORM name the RAW leg as an open gap -- that is step 1 of 7. The six silver converters appear in no active project.

*grounded: 2026-07-28 -- subagent registry sweep, 281 JSONs, 0 parse failures.*

---

## EXTERNAL.ALONGSIDE — Alongside -- scoped adjacent work that is explicitly NOT portal data analytics

**GOAL** — *approved v1 by Andrew Berman (sovereign), 2026-07-28T200316Z*

> Scoped adjacent work that may eventually tie into the portal but is not portal work today -- for example building out Salesforce integrations for 49 Financial. EXPLICITLY NOT portal data analytics: work graduates OUT of this sub-group the moment it becomes that.

    activity   0 commit(s) in the last 14 days · 0 total · 0 author(s)
    newest     — no activity —
    stance     DECIDED UNASSESSED · BUILT UNASSESSED · SERVING UNASSESSED
    version    v1.0


































PROSPECTIVE and net-new. Zero commits is correct.

Andrew-direct: scoped work that may eventually tie into the portal but is very prospective -- for
example building out Salesforce integrations for 49 Financial -- and EXPLICITLY NOT portal data
analytics.

The boundary is the whole point of the sub-group. Work belongs here when it serves an advisor
ALONGSIDE the portal rather than THROUGH it. The moment something becomes portal data analytics it
LEAVES this sub-group and moves to PORTAL -- that migration is the signal that it graduated, not an
inconsistency to be tidied away.

Nothing registered, nothing blocked, no paths claimed.

---

## EXTERNAL.COTTONWOOD — Cottonwood Capital Advisors

**GOAL** — *approved v1 by Andrew Berman (sovereign), 2026-07-28T200316Z*

> Client-facing NON-PORTAL work for Cottonwood Capital Advisors. PROSPECTIVE -- no initiative detail specified yet.

    activity   0 commit(s) in the last 14 days · 0 total · 0 author(s)
    newest     — no activity —
    stance     DECIDED UNASSESSED · BUILT UNASSESSED · SERVING UNASSESSED
    version    v1.1

**BLOCKED ON —** Andrew -- per-client initiative detail.


































PROSPECTIVE. Zero commits is the CORRECT reading, not a gap.

Andrew-direct: no true external work has been done yet -- this is a new category for NON-PORTAL
work. The path globs here are deliberately EMPTY rather than narrow, because a container for work
that does not exist should match nothing, and an empty match set is honest where a plausible one is
not.

This matters because an earlier version of this index globbed per-firm project prefixes into
EXTERNAL and manufactured a 238-commit cross-group overlap that was a property of the index rather
than of the estate. A per-firm PREFIX is not non-portal client work. That error is corrected and
recorded so nobody restores the globs believing they are fixing a coverage gap.

Nothing is blocked. Awaiting Andrew's per-client initiative detail.

Source of record when work begins: BLACK DIAMOND.
Open at Andrew: "Cottonwood Capital Advisory" (his wording) vs "Advisors" (the estate's).

*grounded: 2026-07-28 -- subagent registry sweep. The freeze question is explicitly NOT grounded.*

---

## EXTERNAL.INFLECTION — Inflection Wealth Management

**GOAL** — *approved v1 by Andrew Berman (sovereign), 2026-07-28T200316Z*

> Client-facing NON-PORTAL work for Inflection Wealth Management. PROSPECTIVE -- no initiative detail specified yet.

    activity   0 commit(s) in the last 14 days · 0 total · 0 author(s)
    newest     — no activity —
    stance     DECIDED UNASSESSED · BUILT UNASSESSED · SERVING UNASSESSED
    version    v1.1

**BLOCKED ON —** Andrew -- per-client initiative detail.


































PROSPECTIVE. Zero commits is the CORRECT reading, not a gap.

Andrew-direct: no true external work has been done yet -- this is a new category for NON-PORTAL
work. The path globs here are deliberately EMPTY rather than narrow, because a container for work
that does not exist should match nothing, and an empty match set is honest where a plausible one is
not.

This matters because an earlier version of this index globbed per-firm project prefixes into
EXTERNAL and manufactured a 238-commit cross-group overlap that was a property of the index rather
than of the estate. A per-firm PREFIX is not non-portal client work. That error is corrected and
recorded so nobody restores the globs believing they are fixing a coverage gap.

Nothing is blocked. Awaiting Andrew's per-client initiative detail.

Source of record when work begins: ORION, plus Eclipse for models.

*grounded: 2026-07-28 -- subagent registry sweep.*

---

