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
all of this in one massive project."* Every id has EXACTLY ONE `ACCEPT OWNER`. This project owns the grade on
`FWD-1` and `FWD-6`; `IRPT_BCKEND` owns every other id and this project appears there only as a CONTRIBUTOR.
Two projects, two decompositions, two task-order sets, two adjudications.

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
         ACCEPT     ** IRPT_BCKEND ** -- a parity claim from capture through export;
         OWNER      canonical meaning, units and dates are that project's
         THIS       the common Opal layout; the UI distinguishing TWR/MWR, net/gross,
         PROJECT    cumulative/annualized, UNITS and UNAVAILABLE; the rendered view
                    and the PDF template BACKEND executes -- graded against
                    BACKEND's certified fixture, never against this project's own
                    reading of the provider
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
         ACCEPT     ** IRPT_BCKEND ** -- the chain from validated input to
         OWNER      certified section is that project's
         THIS       variant selection, the mapping and comparison review, request
         PROJECT    history and status, and the Opal-branded native sections as
                    rendered; "unsupported VISIBLE as unsupported" is this project's
                    display obligation on BACKEND's release state
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
         ACCEPT     ** IRPT_BCKEND ** -- the accept turns on join correctness and
         OWNER      the reconcile-before-and-after control
         THIS       the model-first view, the drill into accounts and securities,
         PROJECT    and keeping target / actual / inferred VISIBLY distinct and the
                    residual visible -- on BACKEND's revision-bound nodes
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
         ACCEPT     ** IRPT_BCKEND ** -- deterministic inflection selection,
         OWNER      evidence validity and export execution are that project's
         THIS       the Opal template from the brand guidelines, the export shell,
         PROJECT    the dashboard-stays-default behaviour, placing BACKEND's dated
                    markers on the series, rendering MISSING HISTORY as such, and
                    preview-to-PDF parity of the package BACKEND executes
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
         (ACCEPT owned by IRPT_BCKEND -- the entitlement class; full block in
         the counterpart)
         THIS       the Global view itself: the firm selector, picking any client
         PROJECT    at any firm, every tab and export working on them, and the
                    firm each result belongs to ALWAYS visible; a firm advisor's
                    session never renders this view
         ⛔ MECHANISM IS HIS WORD, THIS SIDE (Andrew ~19:2xZ, third message):
                    "the same firm dropdown pattern as Model Portfolios on the
                    frontend." The MP firm dropdown is FIXED as the pattern; L5
                    chooses Investor Reporting specifics inside it, never whether
                    to follow it. HOW MP implements it is NOT READ at L2 -- L4
                    reads the existing component and cites it
         SOURCE     Andrew-direct ~19:2xZ verbatim; precedent "just like how it's
                    done in Model Portfolios" -- named, NOT READ at L2
```

**COUNT: 7 outcomes carried. 6 of 6 ratified ids verbatim, plus `FWD-11` on his word. ACCEPT owner:
IRPT_FNTEND 2 (`FWD-1`, `FWD-6`), IRPT_BCKEND 5 (`FWD-3`, `FWD-4`, `FWD-5`, `FWD-8`, `FWD-11`).**

⛔ **A PROJECT WHOSE "DONE" INCLUDES FOUR OUTCOMES ANOTHER PROJECT GRADES IS NOT A DEFECT; IT IS THE SPLIT
ANDREW ORDERED, STATED HONESTLY.** IRPT_FNTEND is CLOSED when its two owned outcomes grade REALIZED **and**
its contribution to the four crossing outcomes is graded as met by IRPT_BCKEND's adjudication.

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

## PROVENANCE (F5)

**GROUNDED ON:** the umbrella endpoint **at its pin** `git show 58266dab2d:…/ENDPOINT_FWD_INVESTOR_REPORTING_LIGHTWEIGHT_20260910.md`
lines 118–360 (the eight ratified blocks, extracted with a positive control that a bogus pin is refused);
`docs/briefs/investor-reporting-ir-fe-brief-20260910.md` @`efa5a94bf1` lines 1–66 and §II.1–II.2;
`docs/briefs/investor-reporting-ir-bk-brief-20260910.md` @`efa5a94bf1` lines 1–64 and §II.1–II.2 (every
CROSSES line); `org/standards/PROJECT_TREE.contract.json` (the code grammar).
**NOT READ:** the TO register; any `org/projects/*.json`; the nine source documents beneath the brief.
