# MISSIONS — Opal mission register

    GENERATED ARTIFACT -- do NOT edit. `comp-missions compile` regenerates this file.
    Every sentence below is SELECTED from a state.yaml or execsum.yaml, never composed
    here: a compiler that writes prose is a compiler that can invent a stance.

    ANCHOR COMMIT   3d1dcbe7b6
    ANCHOR TIME     2026-07-28T18:54:58-04:00   (author-time, not a wall clock)
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
| 1 | `INFRASTRUCTURE.GRAPH` | **358** | 1092 | 35 | PARTIAL | PARTIAL | PARTIAL | — |
| 2 | `INFRASTRUCTURE.DEBT` | **158** | 1680 | 42 | YES | PARTIAL | PARTIAL | — |
| 3 | `PORTAL.MODEL_PORTFOLIOS` | **149** | 400 | 17 | YES | YES | NO | 1.0.0_SA_CTO -- an architecture call that PR |
| 4 | `INFRASTRUCTURE.TOOLS` | **118** | 730 | 37 | YES | YES | UNASSESSED | 1.0.0_SA_CTO -- TWO calls CVO explicitly did |
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

    activity   358 commit(s) in the last 14 days · 1092 total · 35 author(s)
    newest     2026-07-28T17:38:16-04:00
    stance     DECIDED PARTIAL · BUILT PARTIAL · SERVING PARTIAL
    version    v1.2

**FRONTIER —** Lock the taxonomy -- one canonical statement the rest can be migrated onto. But note the 92% figure reframes the bottleneck: DECIDED is not what is holding this, ADOPTION is.






































Top of the board on activity -- 357 recent across 35 authors -- and the session finally put capacity
here after a day where it had none.

The standard-versus-adoption reading is unchanged and remains the sub-group in one line: 121 scheduled
EventBridge Rules against 10 Scheduler schedules, 92% of the estate on the non-standard side of a
standard that already exists. DECIDED is not the bottleneck. ADOPTION is.

MOVED SINCE THE LAST SUMMARY. The tool registry landed and was EXERCISED, and the one-declaration
principle got its first real test: the fix CTO ruled for the PIPELINE_MAP gap would have been a SILENT
NO-OP, because one S3 code tree is fed by TWO repo trees. Adding the missing layers to the obvious
tuple would have globbed a directory those files do not live in, hit a `continue`, and skipped both --
same clean summary, same rc=0, same zero UNCOVERED, with a layer list that merely LOOKED complete.

IT WOULD HAVE CONVERTED A VISIBLE 4-VS-6 GAP INTO AN INVISIBLE ONE -- the precise outcome the ruling
exists to prevent, reproduced by the fix for it. That is this sub-group's whole thesis demonstrated at
its own expense, and it is worth more than the fix.

DECIDED remains PARTIAL: key grammar, naming law and one-capacity-one-service exist; there is still NO
provenance taxonomy and NO code-location standard, measured by token census with a positive control so
the zeros are real. BUILT remains PARTIAL on exactly one live gate, one bucket.

The CTO-versus-CVO instance-versus-class disagreement still stands on the record. The register carries
the CLASS.

**HOLES — live work no project code covers (1):**
- json/latest/ -- 6 keys, WRITTEN TODAY (ALIVE), with NO MODELLED CONSUMER in the canonical graph. ROUTED HERE FROM INFRASTRUCTURE.DEBT BY CVO, DELIBERATELY: an unmodelled thing that is DEAD is debt, but an unmodelled thing that is ALIVE is a COVERAGE DEFECT -- the graph is wrong, not the estate. Something is producing this daily for a consumer the graph cannot see. Anchor: CVO served-prefix registry @bf8aae9c40, liveness measured live with a control (json/mdpf/ = 0d, so the band discriminates). Belongs with the comp-opalbizcluster work.

*grounded: 2026-07-28 -- CVO state pull @8ac1e7d04, live EventBridge/Scheduler counts, token census with positive control.*

---

## INFRASTRUCTURE.DEBT — AWS resource and system debt

**GOAL** — *approved v1 by Andrew Berman (sovereign), 2026-07-28T200316Z*

> Ensure that as Infrastructure consolidates patterns and improves design, legacy AWS resources are appropriately decommissioned and terminated -- so agents are never confronted with multiple pipelines, paths and buckets that clobber each other.

    activity   158 commit(s) in the last 14 days · 1680 total · 42 author(s)
    newest     2026-07-28T17:52:18-04:00
    stance     DECIDED YES · BUILT PARTIAL · SERVING PARTIAL
    version    v1.1

**FRONTIER —** Make retirement a CONDITION of a migration rather than a follow-up to it. Nothing structurally prevents a replacement shipping while its predecessor keeps running.






































Second on activity, 157 recent across 42 authors, and the enacted-not-recorded character held: this
window was applied infrastructure, not documentation.

MOVED SINCE THE LAST SUMMARY. A SEPARATE EGRESS PRINCIPAL was built and APPLIED, scoped to a
NON-SERVED staging location and verified on live primitives rather than on a config read. And a PHANTOM
SCHEDULE was deleted from EC2_MANIFEST.json -- notable because that file is the Rule-8 source of truth,
so a phantom entry there is not clutter, it is the source of truth asserting a thing that does not
exist.

DECIDED stays YES. The stated cost remains agent-facing rather than financial: multiple pipelines,
paths and buckets that clobber each other are confusing to agents and very problematic.

SERVING stays PARTIAL for the structural reason, unchanged: there is NO standing mechanism tying a
migration to the retirement of what it replaced. Nothing prevents a replacement shipping while its
predecessor keeps running, and making retirement a CONDITION of migration rather than a follow-up is
still the frontier.

The holes are unchanged and still unowned: OPAL_SCHEDULE and OPAL_ALERTS briefed and MEASURED against
live AWS four days ago with project creation handed to CTO, and neither code exists. The alarm-map
census is still absent while its trigger twin exists complete with a CI drift gate.

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

    activity   149 commit(s) in the last 14 days · 400 total · 17 author(s)
    newest     2026-07-28T18:40:04-04:00
    stance     DECIDED YES · BUILT YES · SERVING NO
    version    v1.2

**FRONTIER —** The defined publisher. Nothing automated writes the serve.

**BLOCKED ON —** 1.0.0_SA_CTO -- an architecture call that PRECEDES the build: which serving namespace is canonical.






































Producer FIXED, serve STILL NOT. Unchanged as the headline, and the gap is now better specified
rather than smaller.

DECIDED and BUILT remain YES, anchored on the 16:48:04Z scheduled run -- 450 dates, cottonwood at 47
slots, sum identity 0 failing of 426 tested where it had been 425/425 FAILING, exact to the cent. That
BUILT is scored on the RUN; a two-leg builder is structurally incapable of that result.

SERVING remains NO and the reason has not softened: the client surface carries a hand-restored 07-23
artifact fed by NEITHER producer. It is a human-published object and no automated path writes it.

MOVED SINCE THE LAST SUMMARY. The consumer contract is now specified -- CTO's s.19 rules JOIN ON
MACHINE KEYS, with INVARIANT N-1 recorded alongside it, so the publisher has a contract to build
against rather than a shape to infer. DS closed F-2 quantity-blindness in the held patch. And the
Stage 6 IAM grant landed as THREE grants rather than one, which is the kind of correction that only
surfaces when someone counts instead of assuming.

Andrew authorised cottonwood inclusion at 203435Z and the legacy aggregator still carries ZERO
cottonwood tokens against 14 inflection -- a real absence, positive-controlled. A successor AE session
is on-mission for the roster single-sourcing and enrollment; CTO dispatches.

The frontier is unchanged and is still the whole gap: the defined publisher. Blocked on a CTO
architecture call -- which serving namespace is canonical -- that PRECEDES the build.

**HOLES — live work no project code covers (2):**
- MDPF_CHANNEL_INDEPENDENCE -- PRD'd (docs/architecture/MDPF_CHANNEL_INDEPENDENCE_PRD.md), cited as law in CLAUDE.md Rule 20/NEVER#4, drove today's P0. NO project JSON, ZERO REGISTRY.md rows. Confirmed independently THREE times (MSTR authoring, CVO /spot-check F-1, CTO state pull).
- Six unaccounted served objects under json/portfolios/: latest, manifest, metrics, summary, timeseries, non_model_assets_preview. No owner, no project, unknown consumers.

*grounded: 2026-07-28T183143Z -- CTO state pull, against the 16:48:04Z scheduled run + commit trail.*

---

## INFRASTRUCTURE.TOOLS — Enumerated coverage universe per tool

**GOAL** — *approved v1 by Andrew Berman (sovereign), 2026-07-28T200316Z*

> Establish an enumerated coverage universe per tool -- what each tool covers, what it does not, and where its silence means nothing-there rather than cannot-see -- consolidating the extensive prior art already held in the NFRA projects; and define how each tool must present information so that responses are high-signal and never inadvertently truncated, redacted or garbled.

    activity   118 commit(s) in the last 14 days · 730 total · 37 author(s)
    newest     2026-07-28T16:43:27-04:00
    stance     DECIDED YES · BUILT YES · SERVING UNASSESSED
    version    v1.3

**FRONTIER —** Wire comp-which to IMPORT tool_index instead of re-parsing the manifest. Cheap, and it is now the single next thing -- until it lands, the compiled index is a fast artifact nobody reads. (The suite-scale declared-vs-actual diff remains real but is downstream of this, and is now cheaper because per-tool primitive rows persist as JSON.)

**BLOCKED ON —** 1.0.0_SA_CTO -- TWO calls CVO explicitly did NOT make: (a) the comp-which wiring, and (b) whether this 5th registry should FOLD INTO comp-coverage-map.yaml, which already has a passing gate it would inherit. Both routed to him in the same window.






































The registry architecture landed, one blocked-on call was ANSWERED, and the answer immediately caught
a real defect in the generator that implemented it.

CTO ruled 212335Z on the question CVO explicitly declined to decide: comp-coverage-map.yaml is the
SOLE POPULATION AUTHORITY. TOOL_MASTER.yaml may remain a separate ATTRIBUTE STORE but must NEVER be a
population source, and the generator must FAIL LOUD on divergence in either direction -- no silent
skip, no continue. CVO's own generator was in violation: it derived population from disk, making the
master a FIFTH copy of the population.

THE PARITY GUARD FIRED ON FIRST EXERCISE AND THIS IS THE PART TO KEEP:
AUTHORITY 89. MASTER 89. COUNTS MATCH EXACTLY. SETS DIVERGE BY 12 MEMBERS.
A count-equality check would have passed clean and said nothing.

THAT UPGRADES A RULE I WROTE INTO THIS REGISTER EARLIER TODAY. I recorded the count cascade -- 93 disk
/ 89 classified / 89 homed / 69 tools_index / 105 use-cases -- with the rule that the POPULATION must
ride with the NUMBER. CTO's doctrine III-g shows that is necessary and NOT SUFFICIENT: two populations
can share a denominator and not share a member, BECAUSE THE DENOMINATOR IS A SCALAR TOO. The rule is
now COMPARE SETS, BOTH DIRECTIONS, AND NAME THE DIVERGING MEMBERS. My version would have passed the
exact check that caught this.

BUILT stays YES for classification -- 89 of 93 typed, generated mechanically from source. O2 moved to
PARTIAL: the card now carries knows_own_denominator and excludes, the two fields that make silent
truncation detectable, but NO TOOL HAS BEEN CHANGED TO USE THEM. The artifact exists; the behaviour
has not moved.

SERVING stays UNASSESSED. Gate wiring was never established and nobody has guessed at it.

The open frontier is cheap and unowned: wire comp-which to IMPORT the compiled index rather than
re-parsing 133KB of YAML per call (~97% of runtime, on the tool Rule 21 makes the first reflex).
Until that lands it is a fast artifact nobody reads.

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






































Largest body of work in the tree, least established state, and that has not changed: 1,726 commits
against 34 recent, BUILT and SERVING both UNASSESSED.

Nothing landed against this sub-group in the window since the last summary. That is itself the
finding -- it sits fifth on activity while carrying the most accumulated work and the least
assessment, and the two Infrastructure sub-groups above it absorbed the session.

DECIDED stays PARTIAL. The basis is set -- 365-day calendar TWR, gross and net, daily, Account365
pinned. The METHOD PER SOURCE is not, and the per-source data-availability analysis has still not been
done. That analysis remains the frontier and everything downstream is unanswerable until it exists.

The hole is unchanged and remains the largest in the register: THE BD-REPLACEMENT TOTAL-RETURN BUILD
HAS NO PROJECT CODE. CRO's research is delivered, the build is held at registration, and a TWR search
across all 281 project JSONs returns five hits of which every one is terminal -- zero active projects.

The shared frontier with MODEL_PORTFOLIOS.O3 still stands: ONE per-channel source-and-schedule
artifact, not two. COO is building it. This sub-group must not commission a second.

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






































Unchanged, and correctly so. LOW priority by sovereign instruction, two commits total, brief only --
not decomposed, not staffed. Nothing landed in the window.

The canonical model is set: /api/general/ and /api/scoped/ are canonical, everything else is debt. The
surface is enumerated in full -- 24 cache behaviors plus one default, 18 canonical and 5 not, with
unauth probes. /json-tiered/* answers 200 UNAUTH with zero portal clients.

The frontier remains the cheapest question here and it is Andrew's own hypothesis: GENERATED IS NOT
DISPLAYED. If it holds, most of this debt is deleted rather than migrated -- which is exactly why
investigation precedes migration and why staying at zero activity is the right posture for now.

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






































PROSPECTIVE. Zero commits, and zero is the CORRECT reading rather than a gap.

Nothing landed in the window and nothing was expected to. The path globs are deliberately EMPTY: a
container for work that does not exist should match nothing, and an empty match set is honest where a
plausible one is not.

This is recorded rather than left implicit because an earlier version of the index globbed per-firm
project prefixes here and manufactured a 238-commit cross-group overlap that was a property of the
index, not of the estate. A per-firm PREFIX is not non-portal client work. Nobody should restore those
globs believing they are closing a coverage gap.

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






































PROSPECTIVE and net-new. Zero commits is correct; nothing landed and nothing was expected to.

Scoped adjacent work that may eventually tie into the portal but is not portal work today -- Andrew's
example is building out Salesforce integrations for 49 Financial -- and EXPLICITLY NOT portal data
analytics.

The boundary is the entire point of the sub-group. Work belongs here when it serves an advisor
ALONGSIDE the portal rather than THROUGH it, and the moment something becomes portal data analytics it
LEAVES and moves to PORTAL. That migration is the signal that it graduated, not an inconsistency to be
tidied away.

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






































PROSPECTIVE. Zero commits, and zero is the CORRECT reading rather than a gap.

Nothing landed in the window and nothing was expected to. The path globs are deliberately EMPTY: a
container for work that does not exist should match nothing, and an empty match set is honest where a
plausible one is not.

This is recorded rather than left implicit because an earlier version of the index globbed per-firm
project prefixes here and manufactured a 238-commit cross-group overlap that was a property of the
index, not of the estate. A per-firm PREFIX is not non-portal client work. Nobody should restore those
globs believing they are closing a coverage gap.

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






































PROSPECTIVE. Zero commits, and zero is the CORRECT reading rather than a gap.

Nothing landed in the window and nothing was expected to. The path globs are deliberately EMPTY: a
container for work that does not exist should match nothing, and an empty match set is honest where a
plausible one is not.

This is recorded rather than left implicit because an earlier version of the index globbed per-firm
project prefixes here and manufactured a 238-commit cross-group overlap that was a property of the
index, not of the estate. A per-firm PREFIX is not non-portal client work. Nobody should restore those
globs believing they are closing a coverage gap.

Source of record when work begins: ORION, plus Eclipse for models.

*grounded: 2026-07-28 -- subagent registry sweep.*

---

