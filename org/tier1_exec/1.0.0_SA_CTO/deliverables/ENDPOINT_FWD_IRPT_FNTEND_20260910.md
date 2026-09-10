# ENDPOINT (L2, `/endpoint --forward`) — **IRPT_FNTEND** — Investor Reporting, the advisor-facing product

**Seat:** `1.0.0_SA_CTO` (L2, CTO only) · **Stamp:** 2026-09-10 ~19:1xZ · **Re-cut ~19:2xZ** (see the ⛔ block)
**Brief consumed:** `docs/briefs/investor-reporting-ir-fe-brief-20260910.md` @`efa5a94bf1`, **30,287 bytes**,
authored `4.0.0_SA_CRO` 2026-09-10T18:58:22Z. No `generated:` line; the vintage is the commit.
**Counterpart:** `ENDPOINT_FWD_IRPT_BCKEND_20260910.md` — cut together, cite each other.
**Commission:** Andrew-direct ~18:3xZ (*"the frontend and client facing investor reporting project"*), macro `IRPT`
in D9 (~18:3xZ), D9 whole to laptop (~18:5xZ). Records under this seat's deliverables, all committed.
**Project code NAMED BY ANDREW ~19:3xZ (superseding this seat's `IRPT_FRONTEND`/`IRPT_BACKEND`):** **`IRPT_FNTEND`** — conforms to the contract's project
grammar `^[A-Z]{4}_[A-Z0-9]{3,18}$`; 0 hits across 8,323 files over the register planes (18 binary and 206
ephemeral-floor files disclosed as NOT covered). **Placement: D9 · fabric `laptop`**, both on his word.

⛔⛔ **RE-CUT ~19:2xZ ON `3.0.0_SA_CVO`'S FINDING (191508Z), AND THE DEFECT WAS MINE.** The first cut of this
document **PARAPHRASED** the eight outcomes Andrew ratified at ~17:3xZ. Paraphrase dropped arms: `FWD-8` lost its
twice-replay determinism control and its MISSING-HISTORY-versus-empty-list arm here; `FWD-6` lost *"a late
response for a PREVIOUS selection CANNOT populate the current client's tab"*; `FWD-3` lost the UNITS clause;
`FWD-4` lost *"unsupported positions are not silently removed"* and the no-live-vendor-call bar. **A RATIFIED
OUTCOME IS CARRIED VERBATIM OR IT IS NOT THE RATIFIED OUTCOME.** Every `DONE WHEN`, `ACCEPT`, `PROOF` and
ratified ⛔/⚠/✅ note below is now **character-for-character from the umbrella endpoint @`58266dab2d`**. **The
ONLY lines that are mine are `ACCEPT OWNER`, `CROSSES`, `THIS PROJECT` and the `SOURCE` suffix** — the split
requires new owner metadata because the ratified `OWNER` lines name WS1–WS4, which Andrew retired. Those WS
lines are the one thing replaced, and this paragraph is the record of it.

⛔ **THIS SUPERSEDES THE UMBRELLA ENDPOINT** `ENDPOINT_FWD_INVESTOR_REPORTING_LIGHTWEIGHT_20260910.md` **for this
project's half.** Its eight ratified ids are PERMANENT and carried unchanged; its distribution amendment
(@`58266dab2d`) is the source of the ACCEPT-owner column and is not re-derived.

⛔ **FWD-n IDS ARE PERMANENT AND NEVER REUSED.** The FE brief's six outcomes map one-to-one onto six ratified ids
(§UNCOVERED). Three outcomes beyond the eight are BACKEND-owned and live in the counterpart (`FWD-9` ratified,
`FWD-10` re-cut on Andrew's word, `FWD-11` new on Andrew's word at ~19:2xZ); **`FWD-11` is carried here too**,
because the Global view is this project's surface, with his mechanism word for this side: *"the same firm
dropdown pattern as Model Portfolios."*

⛔ **THE CUT IS HARD, ON HIS FOURTH SENTENCE:** *"clearly cut between a FE and BK project … we do not try to wrap
all of this in one massive project."* Every id has EXACTLY ONE `ACCEPT OWNER`. **RE-OWNED ~19:3xZ ON HIS SIXTH
SENTENCE** — *"how that report actually looks and how the modals and etc work are all frontend"* — **the
outcome is what the advisor sees and does; the machinery underneath is a contribution.** This project now owns
the grade on every advisor-facing outcome: `FWD-1`, `3`, `4`, `5`, `6`, `8`, `11`, and `FWD-12` (design, at
Andrew). `IRPT_BCKEND` owns the four machinery outcomes — `FWD-2` enforcement, `FWD-7` freshness, `FWD-9`
ingestion, `FWD-10` construction — and appears here as a CONTRIBUTOR whose data, parity and execution
obligations are graded inside each outcome's adjudication. Two projects, two decompositions, two task-order
sets, two adjudications.

⛔ **NO FWD BELOW IS A WAIT.**

---

## THE OUTCOMES — ratified text verbatim @`58266dab2d`; owner metadata is this cut's

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
         ACCEPT     ** IRPT_FNTEND ** -- the accept is an exercised advisor
         OWNER      journey and "survives a tab switch" is selection state
         CROSSES    IRPT_BCKEND supplies the permitted account set, the directory
                    as-of, and the zero-vendor-request guarantee -- observed here,
                    enforced there
         SOURCE     brief O1; Andrew's "search for Clients by name, this routes the
                    tabs" -- carried; FE brief O1 (this cut)

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
         ACCEPT     ** IRPT_FNTEND ** -- RE-OWNED on Andrew ~19:3xZ: the outcome is
         OWNER      the advisor READING the provider's figure here and EXPORTING it
         CROSSES    IRPT_BCKEND supplies canonical meaning, UNITS, dates, the
                    vendor-calculation-only rule and the certified fixture this
                    view is graded against -- the data half of this outcome's
                    proof, graded inside it; the PDF runs in BCKEND's worker
         SOURCE     brief O3, F2, F3; Andrew's "just generating a frontend view of
                    what Black Diamond/Orion already provide" -- carried; FE brief O2
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
         ACCEPT     ** IRPT_FNTEND ** -- RE-OWNED on Andrew ~19:3xZ: the outcome is
         OWNER      the advisor OBTAINING the analysis in the tab and EXPORTING it
         CROSSES    IRPT_BCKEND supplies the chain from validated input through
                    captured request, job and result to a certified section, and
                    the release state behind "unsupported VISIBLE as unsupported"
                    -- graded inside this outcome; the runner style is Andrew's
                    word and lives in BCKEND's block
         SOURCE     brief O4, F7; Andrew's "just pulling a report of what YCharts
                    already provides" -- carried; FE brief O3; the intake itself is
                    BACKEND's FWD-9, at Andrew
         ✅ THE EXPRESS QUALIFICATION IS **DISCHARGED**, 2026-09-10. It read: the
                    evidence is gated on ANDREW'S ANALYST handing it over, a named
                    person's decision, so FWD-4 reads NOT_REALIZED with its reason
                    NAMED until it lands. **IT LANDED** -- `4.0.0_SA_CRO`'s WS3
                    delivery @`129fc4a09d` carries six transcripts, 26 hash-matched
                    ZIPs, three HARs at 220/403/462 entries, six POST-201 -> exact-URL
                    GET-200 pairs, and TWELVE cited source hashes re-verified UNCHANGED
                    AFTER the cross-fabric merge. **That closed one of Andrew's open
                    calls from this seat.** The qualification is kept verbatim above
                    rather than deleted: a discharged gate that leaves no trace reads
                    as a gate that never existed
         ⚠ WHAT REPLACED IT, and it is an EVIDENCE GAP rather than a human gate:
                    native section/export parity still needs ACTUAL three-variant PDFs,
                    and upload multipart is missing. Named here AND on FWD-8's export
                    half -- ⛔ **name it in both or it gets closed silently in one**
         ⛔ AND THE REQUEST ARRIVES BY EMAIL, WHICH THIS OUTCOME DID NOT SAY. WS3's
                    intake is a mailbox poller (Andrew-direct: every day, quarter-hour,
                    08:00-23:45 ET, actual holdings attachments). The advisor still
                    OBTAINS and EXPORTS in the tab, so FWD-4's substance holds -- but
                    the request channel is mail, not a click, and a cell must not
                    assume a synchronous request path
         ⛔ UNSUPPORTED POSITIONS ARE NOT SILENTLY REMOVED TO OBTAIN A SUCCESSFUL
                    REPORT. Lifted to the ACCEPT from `4.0.0_SA_CRO`'s revised O2
                    because it is the session's recurring failure wearing a client's
                    money: a report that drops what it could not resolve renders
                    CLEAN and is WRONG, and no reader can tell it from a complete one.
                    Clear inputs proceed PROGRAMMATICALLY; review is the EXCEPTION
                    path and never a gate on every request -- Andrew hoped for
                    entirely programmatic and the revised brief delivers that shape
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
         ACCEPT     ** IRPT_FNTEND ** -- RE-OWNED on Andrew ~19:3xZ: the outcome is
         OWNER      the advisor SEEING holdings by model and drilling through them
         CROSSES    IRPT_BCKEND supplies join correctness, the reconcile-before-
                    and-after control, the denominators and the revision-bound
                    nodes this view draws -- the data half, graded inside this
                    outcome
         SOURCE     brief O5, F4; Andrew's per-partner overlay mapping, verbatim --
                    carried; FE brief O4; WS4 child brief @4a1d1ed9aa
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
         ACCEPT     ** IRPT_FNTEND ** -- continued use under degradation, and the
         OWNER      "late response cannot populate the current tab" control, are
                    this project's lifecycle
         CROSSES    IRPT_BCKEND supplies the status states and the as-of / revision
                    each result carries
         SOURCE     brief O6 -- carried; FE brief O6

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
         ACCEPT     ** IRPT_FNTEND ** -- RE-OWNED on Andrew ~19:3xZ, his words: "the
         OWNER      branded export is arguably a frontend op, even if a lambda does
                    it, the lambda part is backend, how that report actually looks
                    and how the modals and etc work are all frontend." The Opal
                    template, the export options and modals, the dashboard-stays-
                    default behaviour, the narrative page's composition, MISSING
                    HISTORY rendered as such, and preview-to-PDF parity
         CROSSES    IRPT_BCKEND is the lambda: deterministic inflection selection,
                    dated evidence and prose validity, the frozen bundle, and
                    execution of this project's package -- graded inside this
                    outcome as its evidence half
         SOURCE     Andrew-direct 2026-09-10, verbatim: a "narrative arc" using "daily
                    cloud and trending topics over almost a full year", to "dynamically
                    assess what was the trending topic or buzz word/phrase from word
                    cloud that was occuring at that time ... to help qualify what was
                    happening at that time" -- carried; FE brief O5
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

  FWD-11 An Opal user can run reports and analysis on ALL firms from one
         Global view, the way Model Portfolios already does it
         ** NEW -- Andrew ~19:2xZ -- RATIFIED ON HIS WORD, one word reverses **
         DONE WHEN  EXERCISED -- an Opal user has opened the global view, picked
                    a client at a second firm, and run a report and an export
         ACCEPT     someone at Opal, signed in as Opal rather than as any firm,
                    can pick any client from any firm and use every tab and
                    export on them; a firm's advisor can never reach that view or
                    see a second firm through it; the global view shows the same
                    numbers that firm's own advisor would see for that client,
                    never a recomputed or blended one; which firm each result
                    belongs to is always visible
         PROOF      an Opal user opens the global view, selects clients at two
                    different firms, runs a report and an export on each; replay
                    the same requests as a firm advisor and confirm refusal;
                    compare the global-view figures to the firm-scoped figures for
                    the same client and revision
         ACCEPT     ** IRPT_FNTEND ** -- RE-OWNED on Andrew ~19:3xZ: the outcome is
         OWNER      an Opal USER running reports across firms from a VIEW
         CROSSES    IRPT_BCKEND supplies the cross-firm entitlement CLASS (the same
                    rule as FWD-2 and FWD-10, GRANTED to an Opal principal) and
                    the multitenant api/scoped/ layout -- graded inside this
                    outcome as its entitlement half
         ⛔ MECHANISM IS HIS WORD, THIS SIDE (Andrew ~19:2xZ, third message):
                    "the same firm dropdown pattern as Model Portfolios on the
                    frontend." The MP firm dropdown is FIXED as the pattern; L5
                    chooses Investor Reporting specifics inside it, never whether
                    to follow it. HOW MP implements it is NOT READ at L2 -- L4
                    reads the existing component and cites it
         SOURCE     Andrew-direct ~19:2xZ verbatim; precedent "just like how it's
                    done in Model Portfolios" -- named, NOT READ at L2

  FWD-12 The Investor Reporting screens look and behave like the rest of the
         Opal portal, so an advisor who already uses the portal needs no
         re-learning
         ** NEW -- cut from Andrew ~19:3xZ and the FE brief IV.2 -- AT ANDREW:
            he named the GAP, not the outcome; yes / no **
         DONE WHEN  EXERCISED -- an advisor who already uses another portal page
                    has used all three tabs and the export without being shown
                    anything new to learn
         ACCEPT     the page is built from the portal's own header, tabs, client
                    search box, category tree, model colours, panels and brand --
                    not look-alikes made for this project; the firm dropdown is
                    the Model Portfolios one; an advisor who knows another portal
                    page finds the same controls in the same places doing the
                    same things; the screen and the exported report share one
                    brand; it works at a narrow width
         PROOF      a census of EVERY component the page uses against the portal's
                    existing component set, denominator printed -- each is REUSED
                    from a named existing path or is NEW with a stated reason a
                    reviewer can dispute; a review against the brand guidelines
                    and the brand spec; the Model Portfolios firm dropdown REUSED,
                    not rebuilt; the narrow-viewport exercise the brief's sketch
                    already ran, repeated on the real page
         ACCEPT     ** IRPT_FNTEND ** -- IRPT_BCKEND is NOT ENGAGED on this outcome
         OWNER
         SOURCE     Andrew ~19:3xZ: "following portal patterns and what the
                    frontend is supposed to look like ... component structure and
                    design"; FE brief IV.2, the named existing paths --
                    PageHeaderVariants, PageSurfaceControl, TabNavigation +
                    useTabNavigation, the catalyst combobox, ClientListPanel,
                    CategoryViewTree + modelPortfolioColors, the AdvisorIntelligence
                    radial precedents, brand.json + the brand guidelines + the
                    official logo package; IV.4, the narrow-viewport exercise
         ⛔ THE PATHS ARE THE BRIEF'S, NOT RECALLED. IV.2 is a table of existing
                    paths with intended use, existence-checked in the split
                    evidence manifest. This outcome names them so the census in
                    PROOF has a printed denominator to subtract from
```

**COUNT: 8 outcomes carried. 6 of 6 ratified ids verbatim; `FWD-11` on his word; `FWD-12` NEW, at Andrew.
ACCEPT owner AFTER THE ~19:3xZ RE-OWN: IRPT_FNTEND 8 (`FWD-1`, `3`, `4`, `5`, `6`, `8`, `11`, `12`),
IRPT_BCKEND 0 here -- its four machinery outcomes (`FWD-2`, `7`, `9`, `10`) live only in the counterpart.**

⛔ **CLOSURE, AFTER THE ~19:3xZ RE-OWN (the earlier two-plus-four rule is SUPERSEDED, caught by `3.0.0_SA_CVO`
194256Z).** IRPT_FNTEND is CLOSED when its SEVEN RATIFIED owned outcomes grade REALIZED, plus `FWD-12` if and
when Andrew ratifies it -- closure cannot depend on an outcome he has not confirmed. **Five of them cross** (`FWD-3`,
`4`, `5`, `8`, `11`): each of those grades reads BOTH proof halves — this project's view and IRPT_BCKEND's data,
parity, entitlement or execution half — and is not complete on the frontend's mock alone. The FE brief's own
Part V: *"neither can certify the other half with its own mock."*

---

## THE UNCOVERED PARTITION — hunted BY SUBTRACTION

**Denominator: the FE brief's 6 outcomes (O1–O6).** O1→FWD-1, O2→FWD-3, O3→FWD-4, O4→FWD-5, O5→FWD-8, O6→FWD-6.
**6 minus 6 = 0 uncovered on this side.**

**Reverse subtraction — ratified ids the FE brief does NOT serve as outcomes: `FWD-2` and `FWD-7`.** Both are
backend-owned; FE contributes their visible halves inside O1 and O6 (*"correct response handling, no
protected stale display, UI permission states"*; *"displays the as-of"*). Not uncovered; owned elsewhere.

## WHAT L2 DOES NOT DECIDE

Cells, owners-per-cell, sequencing, lane suffixes (L5/L6). Latency and TTL numbers. The shared contract
schemas (BK's §II.3 inventory is the source; a change needs matching producer and consumer fixtures). Which
analysis sections are "supported" (paired fixtures decide). Any live vendor call.

## WHERE THIS LANDS (F4) — **NOT YET LANDED**

Ready to paste under **`## ENDPOINT (step 2, /endpoint --forward)`** in
`org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md`. **That path does not exist.** It needs
`MACROS.yaml` D9 `[IRPT]` landed by `0.0.0_AB_MSTR` (record @`643116f787`, ratification already given), the D9
`LAPTOP` flip, and the register row.

## ⛔ THE BRIEF-COVERAGE OBLIGATION ON L4 — his seventh sentence, answered in writing

*"Please confirm the FWDs and PRDs are not lossy."* **THE FWDs ARE LOSSY BY DESIGN AND ON HIS OWN WORD** —
2026-09-01, *"This does not have to be a deliverable contract. It can be qualitative because we will not know
enough about the quantitative mechanics at this point."* They are the ACCEPTANCE layer: what counts as done,
in plain English, gradeable by the person the outcome is for. They were never the spec and must not become it.

**THE PIPELINE IS LOSSY BETWEEN BRIEF AND WORKER UNLESS THE PRD CLOSES THE GAP, AND NOTHING ELSE CAN.** A
worker's face at L7 is *"the worker's whole context — cell text, absolute paths, ONE clause per criterion."* A
worker never opens a brief. So every one of the brief's detailed sections — and the nine sources its Part IV
maps — reaches a builder ONLY if the PRD pulls it through into a cell. **BINDING ON THIS PROJECT'S PRD:** a
BRIEF COVERAGE MAP, by SUBTRACTION with the denominator printed — every section of
`investor-reporting-ir-fe-brief-20260910.md` (and every source document its §IV.1 maps) → the cell(s) and
`FWD` that consume it, or an explicit `NOT CONSUMED: <why>`. A section with no consumer and no reason is a PRD
DEFECT the CVO grades at L9. The brief is the source of truth for detail; the PRD is its index into cells; the
FWD is what says whether the result counts.

## PROVENANCE (F5)

**GROUNDED ON:** the umbrella endpoint **at its pin** `git show 58266dab2d:…/ENDPOINT_FWD_INVESTOR_REPORTING_LIGHTWEIGHT_20260910.md`
lines 118–360 (the eight ratified blocks, extracted with a positive control that a bogus pin is refused);
`docs/briefs/investor-reporting-ir-fe-brief-20260910.md` @`efa5a94bf1` lines 1–66 and §II.1–II.2;
`docs/briefs/investor-reporting-ir-bk-brief-20260910.md` @`efa5a94bf1` lines 1–64 and §II.1–II.2 (every
CROSSES line); `org/standards/PROJECT_TREE.contract.json` (the code grammar).
**NOT READ:** the TO register; any `org/projects/*.json`; the nine source documents beneath the brief.
