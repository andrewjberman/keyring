# ENDPOINT (L2, `/endpoint --forward`) — LIGHTWEIGHT INVESTOR REPORTING

**Seat:** `1.0.0_SA_CTO` (L2, CTO only) · **Stamp:** 2026-09-10 ~13:4xZ
**Brief consumed:** `docs/briefs/investor-reporting-lightweight-brief-20260910.md` @`03c74dc`,
sha256 `1f20ba5d4e9b17c26479f7d338e4525d0488b437935f7544306a9e847b8ca1cd` over 23,151 bytes —
computed at this seat over the blob at the author's own commit, not the worktree.
**Design annex:** `docs/briefs/investor-reporting-lightweight-design-20260910.md` @`03c74dc`,
sha256 `7c596b6f7f6d2ffd9725a1973add0088f97860d5e803634ba6e111e451925ce2` over 31,172 bytes.
**Commission:** Andrew-direct 2026-09-10 09:19 ET + his same-turn ONE-PROJECT clarification, both
verbatim in `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260910_0919ET_LIGHTWEIGHT_INVESTOR_REPORTING.md`.
**Placement:** D9 Opal Workflows. ONE umbrella project, FOUR workstreams. Project code assigned at L3.

⛔ **FWD-n IDS ARE PERMANENT AND NEVER REUSED. A retired outcome leaves its number VACANT.**

⛔ **NO FWD BELOW IS A WAIT.** Every one is provable by an act a seat can take ON DEMAND. The single
place a human gates an act is **FWD-4**, and it is EXPRESSLY QUALIFIED on the outcome with its reason,
per Rule 27's L2 clause. Nothing here waits on an event nobody controls.

---

## THE OUTCOMES

```
  FWD-1  An advisor finds an authorized client and opens its relationship and
         accounts without waiting for a vendor report
         DONE WHEN  EXERCISED -- an advisor who has never used the workspace has
                    searched, selected, and been shown the relationship and its
                    permitted accounts
         ACCEPT     from the header, a search by client name returns an unambiguous
                    selection; the workspace immediately shows the relationship, its
                    permitted underlying accounts, cached context and the directory's
                    as-of; the choice survives a tab switch; an unmapped client stays
                    VISIBLE to an authorized viewer with an explicit capability gap
                    rather than silently missing
         PROOF      a fixture directory carrying duplicate names, an account-only
                    entry and multiple relationships, compared against the expected
                    authorized set; cold and warm timings recorded against the whole
                    captured firm-directory denominator; VENDOR REQUEST COUNT DURING
                    SEARCH IS ZERO. No latency target is invented at L2
         OWNER      WS1
         SOURCE     brief O1; Andrew's "search for Clients by name, this routes the tabs"

  FWD-2  A restricted advisor can use every tab and export ONLY within their
         permitted client population
         DONE WHEN  EXERCISED -- an unauthorized request has been replayed and
                    revealed nothing
         ACCEPT     firm and advisor rights govern suggestions, selected-account
                    membership, report retrieval, job polling, cached results AND
                    PDF download; a relationship containing an account outside the
                    viewer's permitted population NEVER silently grants that account
                    or its value; a firm-authorized viewer gets the firm's population
                    under the same rules
         PROOF      replay authorized and unauthorized requests with SWAPPED firm,
                    advisor, account, relationship, report and PDF identifiers,
                    INCLUDING A REVOKED GRANT AGAINST A WARM CACHE; the negative
                    requests reveal no protected data
         OWNER      WS1 owns the policy and scope contract; WS2-WS4 each enforce it
                    at their own entry points
         SOURCE     brief O2; CTO 95142 (entitlement is an OUTCOME, not a property of
                    a search box); CLAUDE.md s.5 cross-firm rule
         ⛔ NOTE    THIS IS THE HIGHEST-BLAST-RADIUS OUTCOME IN THE SET. A defect here
                    is a CROSS-FIRM EXPOSURE, and the estate's cross-firm rule is
                    SUBSTRATE-SHAPED with BOTH SHAPES LIVE (bucket-scoped Deny and
                    key-prefix + IAM condition). It is graded on its own, never as a
                    side effect of FWD-1

  FWD-3  An advisor reads the provider's performance result in an Opal report and
         exports the same result
         DONE WHEN  EXERCISED -- a captured provider response has been carried to a
                    rendered view and a PDF at one report revision, for each
                    supported partner and scope
         ACCEPT     for the selected account or relationship and period, vendor-
                    calculated performance appears in a common Opal layout and the
                    PDF carries the SAME scope, returned dates, values, method basis,
                    source attribution and approved disclosures; the UI distinguishes
                    TWR/MWR, net/gross, cumulative/annualized, UNITS and UNAVAILABLE
                    fields; a deliberately incomplete provider mapping yields a
                    PARTIAL or UNSUPPORTED result rather than a full-client claim
         ⛔ UNITS ADDED 2026-09-10, PRE-RATIFICATION, on `4.0.0_SA_CRO`'s WS2
                    delivery and verified at source at this seat. ONE PROVIDER
                    RETURNS THE SAME FIELD NAME IN TWO DIFFERENT UNITS: Orion's
                    summary `calculated-performance.performance` is DECIMAL while the
                    daily breakdown `performance` is PERCENTAGE -- "divide by 100 if
                    used as a daily rate", which the CRO confirmed against
                    `factor - 1` for all 276 daily points. **A normalizer treating
                    both as one unit yields a figure WRONG BY 100x THAT RENDERS
                    CORRECTLY, EXPORTS TO PDF, AND TIES TO NOTHING THAT CATCHES IT.**
                    My accept named method basis, fee basis and annualization and did
                    NOT name units. That omission was mine and it is closed here.
                    **A unit is part of a number's MEANING, not its formatting.**
         PROOF      compare captured request/response, normalized report, rendered
                    view and PDF at one revision per partner and scope; relationship
                    return uses a VENDOR CALCULATION for the exact selected account
                    set -- summing or averaging account returns is not a substitute
                    and a fabricated aggregate fails this outcome
         OWNER      WS2 semantic content and adapter; WS1 shared render/export
         SOURCE     brief O3, F2, F3; Andrew's "just generating a frontend view of
                    what Black Diamond/Orion already provide"
         ⛔ NOTE    A NORMALIZER DOES NOT CHANGE A PROVIDER'S METHODOLOGY TO MAKE TWO
                    NUMBERS LOOK COMPARABLE. Making BD and Orion agree by adjusting
                    one of them fails this outcome even when the layout matches

  FWD-4  An advisor obtains a YCharts sensitivity analysis in the same client
         context and exports it
         DONE WHEN  EXERCISED -- an approved report variant has been replayed from an
                    analyst-approved input through its captured request/job/result
                    chain to the tab and the PDF
         ACCEPT     the advisor selects a supported variant, reviews the holdings or
                    saved-portfolio mapping and comparison model it will use, and
                    receives an Opal-branded analysis and matching PDF preserving the
                    input snapshot, configuration, data dates, limitations and vendor
                    attribution; a MODELED comparison is described as modeled;
                    unsupported variants are VISIBLE as unsupported
         PROOF      replay each approved variant end to end
         OWNER      WS3
         SOURCE     brief O4, F7; Andrew's "just pulling a report of what YCharts
                    already provides"
         ⛔ EXPRESSLY QUALIFIED, and this is the ONE human gate in the set.
                    Current evidence covers ONE OF THREE varietals as a static
                    report, and NO complete report-generation HAR has been inspected.
                    The missing evidence -- the generation HAR, the analyst
                    transcripts and input/result specimens -- is obtained by an ACT,
                    not by waiting for an event: it is gated on ANDREW'S ANALYST
                    handing it over, which is a NAMED PERSON'S DECISION and therefore
                    the expressly-qualified exception Rule 27's L2 clause provides
                    for. **THIS PARAGRAPH IS THAT QUALIFICATION.** The outcome is NOT
                    re-cut to what one static varietal can prove; the evidence is
                    fetched. Until it lands, FWD-4 reads NOT_REALIZED with its reason
                    NAMED, and no cell may grade it REALIZED on the one captured
                    varietal
         ⛔ AND NO LIVE VENDOR CALL IS AUTHORIZED BY THIS ENDPOINT. Availability is
                    not authorization; a live YCharts, Black Diamond or Orion call
                    needs Andrew's explicit per-use word

  FWD-5  An advisor sees current holdings organized by models, with the underlying
         securities and unassigned assets preserved
         DONE WHEN  EXERCISED -- dated holdings and model snapshots have been
                    replayed for all three registry client firms
         ACCEPT     the view starts at the model breakdown and drills into accounts
                    and securities; ACTUAL CUSTODY HOLDINGS REMAIN THE TOTAL-VALUE
                    BASIS; SmartX (49F), Eclipse (INF) or BD Rebalancer (COT)
                    supplies the overlay; target weights, actual sleeve values and
                    inferred estimates are DISTINCT; missing attribution stays
                    VISIBLE without double-counting or redistributing the residual
         PROOF      replay across all three firms including an unassigned account, an
                    unmatched join, a blended model and a multi-relationship
                    membership; UNIQUE UNDERLYING HOLDINGS RECONCILE BEFORE AND AFTER
                    THE OVERLAY; coverage and join exceptions carry DENOMINATORS
         OWNER      WS4
         SOURCE     brief O5, F4; Andrew's per-partner overlay mapping, verbatim
         ⛔ NOTE    MODEL TARGETS MUST NOT MASQUERADE AS OBSERVED HOLDINGS. A residual
                    silently redistributed into sleeves fails this outcome even when
                    every total ties

  FWD-6  An advisor can keep working when one report is unavailable, and can tell
         the age of each result
         DONE WHEN  EXERCISED -- a provider has been deliberately failed and a client
                    switched mid-request, with no response landing on the wrong
                    selection
         ACCEPT     client selection and silver-backed holdings stay usable when a
                    provider is slow or down; each tab distinguishes LOADING, READY,
                    STALE, PARTIAL, UNAVAILABLE and FAILED; a late response for a
                    PREVIOUS selection CANNOT populate the current client's tab;
                    cached reports keep their original as-of and revision
         PROOF      delay or fail one provider, switch clients during an outstanding
                    request, expire a cache entry, and complete jobs OUT OF ORDER
         OWNER      WS1 shared lifecycle; WS2-WS4 provider and snapshot status
         SOURCE     brief O6

  FWD-7  The client directory cannot go quietly stale, and its ceiling belongs to
         the system rather than to the advisor's diligence
         DONE WHEN  EXERCISED -- a DRIVEN exercise on a CONTROLLED CLOCK against
                    source fixtures, covering the FAILURE arms, with NO REAL-CALENDAR
                    WAIT anywhere in it
         ACCEPT     a client added, or whose eligibility changes, in the source
                    becomes visible or ceases to be offered within the declared
                    refresh window WITHOUT anyone asking for a refresh; a MISSED
                    TRIGGER and a FAILED REFRESH each read DIFFERENTLY from a
                    completed one; a request served from an OVER-AGE directory hits
                    the declared expiry/fallback behavior rather than being answered
                    silently; the oldest directory an advisor can be served is set by
                    the SCHEDULE, not by whether they noticed the as-of
         PROOF      controlled-clock / source-fixture exercise driving ALL FIVE arms:
                    an added client, a changed eligibility, a MISSED trigger, a
                    FAILED refresh, and an OVER-AGE directory request
         OWNER      WS1
         SOURCE     ⭐ **NOT IN THE BRIEF'S SIX. ADDED AT L2** -- see UNCOVERED below.
         (FWD-7 continues below; FWD-8 follows it.)
                    DONE WHEN and PROOF re-cut on `4.0.0_SA_CRO`'s L2 review (95180):
                    my first form read a HISTORY of consecutive refreshes, which has
                    NO NEGATIVE ARM -- a run of successes cannot show what a missed
                    or failed refresh does, and a SCHEDULE is not by itself a
                    MAXIMUM SERVED AGE. The driven form is strictly stronger and is
                    what the L2 "no FWD is a wait" clause actually demands
         ⛔ OPEN, AND IT IS A PRODUCT DECISION RATHER THAN A CUT DEFECT: a terminated
                    client or account may still require HISTORICAL reporting, so
                    DISAPPEARANCE FROM SEARCH MUST NOT BE EQUATED WITH ACCESS
                    REVOCATION. This outcome names an ELIGIBILITY POLICY and does not
                    write one; my first form assumed termination implies
                    disappearance, which is a decision I do not own. Andrew's, or the
                    project's at L4 with his word. Raised by `4.0.0_SA_CRO`
         ⛔ WHAT THIS OUTCOME IS **NOT**: it is DIRECTORY FRESHNESS AND ELIGIBILITY,
                    and NOTHING about it grades revocation. FWD-2 owns revocation
                    INDEPENDENTLY and the two are not substitutes -- see the
                    correction under UNCOVERED

  FWD-8  An advisor exports a BRANDED Opal report whose narrative page states what
         was happening in the market at the account's dramatic moves -- as
         CONTEMPORANEOUS CONTEXT, never as a cause of the return
         DONE WHEN  EXERCISED -- a KNOWN drawdown window has been replayed against
                    the dated topic history and the same inputs selected the SAME
                    inflection points twice
         ACCEPT     the dashboard stays the DEFAULT view and the export is a separate
                    act; the export renders the Opal template from the deck-generation
                    brand guidelines at the SAME performance revision the advisor
                    reviewed, with advisor logo and information as an OPTIONAL input;
                    the narrative page shows the performance time series and, at the
                    max drawdown and other dramatic moves, the Trending Topic and
                    Topic Cloud terms DATED TO THAT WINDOW, with the other sentiment
                    signals as supporting context; inflection-point selection is
                    DETERMINISTIC -- the same series and the same history select the
                    same moments, every run
         PROOF      replay one known drawdown window twice and diff the selected
                    moments; replay a window that PREDATES the news history and
                    confirm it renders MISSING HISTORY rather than an empty topic list
         OWNER      WS1 owns the export shell, template and branding; WS2 owns the
                    performance content and revision binding; the topic/sentiment
                    retrieval is a NEW seam whose owner is named at L5
         SOURCE     Andrew-direct 2026-09-10, verbatim: a "narrative arc" using "daily
                    cloud and trending topics over almost a full year", to "dynamically
                    assess what was the trending topic or buzz word/phrase from word
                    cloud that was occuring at that time ... to help qualify what was
                    happening at that time"
         ⛔ THE CAUSAL LINE IS IN THE ACCEPT, NOT IN A DISCLAIMER. A page that puts a
                    client's drawdown and a market topic in ONE VISUAL IS READ AS
                    CAUSAL by any reader, whatever the footnote says. Andrew's own word
                    is "QUALIFY WHAT WAS HAPPENING AT THAT TIME" -- contemporaneity --
                    and `4.0.0_SA_CRO` named the same limit unprompted. **The artifact
                    must SAY it is contemporaneous context and must not assert, imply
                    or rank causes.** An export that reads as an explanation of the
                    return FAILS this outcome even when every date is right
         ⛔ MISSING HISTORY IS AN ANSWER, NOT AN EMPTY STATE. The news history is
                    "almost a full year". Any performance period reaching before it has
                    NO topic data, and a narrative page that silently shows nothing
                    there reads as "NOTHING NOTABLE HAPPENED" rather than "WE HAVE NO
                    DATA". The absent-versus-zero distinction is the failure this
                    estate has paid for repeatedly and it is graded here
         ⛔ NOT A BI SURFACE. This is a BOUNDED read of DATED signals for the selected
                    account's own periods. The 2026-09-09 brief's exclusion of broad
                    BI/agent query capability still stands and this does not reopen it
         ⚠ PENDING INPUT: the high-definition advisor logos. Andrew supplies them; they
                    are RECORDED AS PENDING and are neither invented nor scraped
```

---

## THE UNCOVERED PARTITION — hunted BY SUBTRACTION, not by recall

⛔ **THE DOMAIN IS FALSIFIED FIRST, per Rule 24(i) as amended at `b3bc1d7511`.** The domain is not the
brief's own six outcomes — subtracting a document from itself certifies nothing. The domain is
**ANDREW'S TWO VERBATIM MESSAGES**, which are the population this endpoint answers to. Subtracting the
brief's coverage from his words leaves ZERO uncovered: page, search/routing, performance via BD and
Orion, YCharts sensitivity, holdings with per-partner model overlay, PDF export, the opal-data-assets
client/relationship/account cache, and firmID/advisorID serving all land on O1-O5. The brief's own
ownership check says the same and it holds.

**BUT THE BRIEF'S SIX ARE NOT THE ONLY POPULATION.** A second domain — *what must be true for these
six to keep being true* — yields one member the six do not carry:

**FWD-7, THE DIRECTORY'S OWN FRESHNESS.** The brief makes the directory a **derived product
projection** and says so plainly (Part II.2: *"calling it a cache does not make it a silver
transformation... the pilot can avoid a new full analytical pipeline while still owning these small
projections AND THEIR REFRESH MECHANISM"*). O1 requires the as-of to be **DISPLAYED**. **DISPLAYING
STALENESS IS NOT BOUNDING IT.** O6 covers the staleness of REPORTS and CACHED RESULTS; nothing covers
the DIRECTORY. So a directory that silently stops refreshing passes every one of O1-O6: search is
fast, the as-of renders honestly, entitlement holds, reports and holdings work — while a client
onboarded last week is INVISIBLE and a terminated one is still selectable.

**That is the FWD-3 versus FWD-4 distinction from `NFRA_CLDGRPH` arriving in a new project** — age
being *legible* and age having a *ceiling* are different outcomes with different owners, and this
estate has already paid to learn that they do not travel together.

⛔ **CORRECTION TO MY OWN ARGUMENT, MADE BEFORE RATIFICATION RATHER THAN AFTER.** My first cut escalated
this by claiming that, because entitlement rides on the same projection, *"a terminated advisor's
population can outlive the termination."* **THAT IS WRONG AGAINST THIS DESIGN, and `4.0.0_SA_CRO`
refused it at 95180.** Verified at source rather than conceded on assertion — the design annex says so
in two places: §1.2 *"A scope token/reference must be bound to the authenticated principal and CURRENT
PERMISSION VERSION, not a bearer grant that outlives revocation. Recheck authorization when requesting
a report, polling it and downloading it"*, and §2.1 *"KEEP AUTHORIZATION REVISION SEPARATE so
permission changes can invalidate visibility without rebuilding all names."* **Authorization revision
is separate from the directory projection BY DESIGN.** A stale directory yields stale NAMES, not stale
PERMISSIONS.

**HOW I GOT IT WRONG, because the shape matters more than the error:** I read the BRIEF and asserted a
mechanism that is specified in the DESIGN ANNEX — a 31,172-byte document I had not opened. I certified
the gap between what I read. That is the unread-gap hazard, committed by the seat that has been citing
it at others all day, and it was caught by the author of the document I skipped.

**FWD-7 SURVIVES THE CORRECTION; ONLY MY ARGUMENT FOR ITS SEVERITY DIES.** The outcome stands on its
own plain facts: a directory that silently stops refreshing leaves a client onboarded last week
INVISIBLE and a terminated one still OFFERED, while every one of O1–O6 passes. That is sufficient. It
does not need the revocation escalation and must not borrow FWD-2's weight — **FWD-2 owns revocation
independently, and nothing in FWD-7 grades it.**

**NOT ADDED, and I name them so the exclusion is deliberate rather than an omission:** vendor
retirement, a replacement performance engine, estate-wide pipeline consolidation, BI/agent query
surfaces and historical model reconstruction. All are the 2026-09-09 unification brief's territory,
which the brief says remains in force. This endpoint does not cancel it and does not absorb it.

---

## WHAT L2 DOES NOT DECIDE

Project code and register row (L3). Cells, owners-per-cell, sequencing and lane suffixes (L5/L6 — and
Andrew's proposed COO~N staffing is a pattern for the COO to apply at issuance, not a decision taken
here). Latency and TTL numbers — **none is ratified at L2 and none may be invented downstream; they
are MEASURED from provider behavior and then declared.** Which of the three YCharts varietals are
approved (FWD-4's evidence decides). Any live vendor call.

## PUSH STATE
Measured at authorship, and it ages the moment an integrator runs.
