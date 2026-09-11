# ENDPOINT (L2, `/endpoint --forward`) — **IRPT_BCKEND** — Investor Reporting, ingestion, scoping and execution

**Seat:** `1.0.0_SA_CTO` (L2, CTO only) · **Stamp:** 2026-09-10 ~19:1xZ · **Re-cut ~19:2xZ** (see the ⛔ block)
**Brief consumed:** `docs/briefs/investor-reporting-ir-bk-brief-20260910.md` @`efa5a94bf1`, **50,647 bytes**,
authored `4.0.0_SA_CRO` 2026-09-10T18:58:22Z. No `generated:` line; the vintage is the commit.
**Counterpart:** `ENDPOINT_FWD_IRPT_FNTEND_20260910.md` — cut together, cite each other.
**Commission:** Andrew-direct ~18:3xZ (*"the backend etl/multi-tenant/etc investor reporting project"*), macro
`IRPT` in D9, D9 whole to laptop. Records under this seat's deliverables, all committed.
**Project code NAMED BY ANDREW ~19:3xZ (superseding this seat's `IRPT_FRONTEND`/`IRPT_BACKEND`):** **`IRPT_BCKEND`** — conforms to the contract's project
grammar `^[A-Z]{4}_[A-Z0-9]{3,18}$`; 0 hits across 8,323 files over the register planes (18 binary and 206
ephemeral-floor files disclosed as NOT covered). **Placement: D9 · fabric `laptop`**, both on his word.

⛔⛔ **RE-CUT ~19:2xZ ON TWO FINDINGS, BOTH CORRECT, BOTH DEFECTS OF MINE.**
**(1) `3.0.0_SA_CVO` 191508Z:** the first cut **PARAPHRASED** the ratified outcomes. `FWD-7`'s proof went from
the ratified FIVE arms (added client, changed eligibility, MISSED trigger, **FAILED refresh, OVER-AGE directory
request**) to THREE, while claiming the re-cut was carried unchanged. `FWD-8` lost the twice-replay
determinism control and the MISSING-HISTORY-versus-empty-list arm. `FWD-2` lost *"revealed nothing"* and the
warm-cache revocation arm's exact form. **A RATIFIED OUTCOME IS CARRIED VERBATIM OR IT IS NOT THE RATIFIED
OUTCOME.** Every `DONE WHEN`, `ACCEPT`, `PROOF` and ratified ⛔/⚠/✅ note on `FWD-1`..`FWD-8` below is now
**character-for-character from the umbrella endpoint @`58266dab2d`**. Only `ACCEPT OWNER`, `CROSSES`,
`THIS PROJECT` and the `SOURCE` suffix are mine; the ratified `OWNER` lines named WS1–WS4, which Andrew
retired, and those are the one thing replaced.
**(2) `4.0.0_SA_CRO` 191505Z:** the first cut's *WHAT L2 DOES NOT DECIDE* said *"whether the YCharts runner
reuses the named pattern (an L5 build choice)"*. **THAT DOWNGRADED ANDREW'S EXPLICIT WORD TO A BUILD CHOICE.**
His words: *"Yeah i would use the same pattern as BDAPI with Kimi"*; then *"use the exact same style of runner,
that strategy works very well. I do not believe they send OTP so dont need that part."* The runner STYLE and
the no-OTP branch are FIXED on his word; L5 chooses YCharts-specific implementation details, never whether to
honor the strategy. Corrected in that section.

⛔⛔ **THREE OUTCOMES BEYOND THE RATIFIED EIGHT, ALL ON ANDREW'S WORD AT ~19:2xZ** (record
`ANDREW_DIRECT_20260910_192xZ_FWD9_YES_FWD10_IMPOSSIBLE_BY_INGESTION_GATE.md`). **`FWD-9` RATIFIED** — *"call 1
yes."* **`FWD-10` RE-CUT IN PLACE ON HIS WORD** — neither accepted nor refused as cut; he said the property is the
wrong SHAPE: *"this should be impossible because there should be clear gates that assign firm based on email upon
ingestion"* — so it is now a CONSTRUCTION property, id unchanged, `ACCEPT` re-tested per `/endpoint` F0.
**`FWD-11` NEW** — *"I want a 'Global' view … an Opal User can … run reports/analysis on ALL FIRMS"*, with his
mechanism word for this side: *"the backend multitenant api/scoped/ layout."* ⚠ **`FWD-10` and `FWD-11` are
marked RATIFIED ON HIS WORD because his sentences ARE the outcomes; one word reverses either and the id goes vacant.**

⛔ **THE CUT IS HARD, ON HIS FOURTH SENTENCE:** *"clearly cut between a FE and BK project … we do not try to wrap
all of this in one massive project."* Every id below has EXACTLY ONE `ACCEPT OWNER`. **RE-OWNED ~19:3xZ ON HIS
SIXTH SENTENCE** — *"the lambda part is backend, how that report actually looks and how the modals and etc work
are all frontend"* — **the outcome is what the advisor sees and does; the machinery is a contribution.** This
project now owns the grade on FOUR machinery outcomes: `FWD-2` enforcement, `FWD-7` freshness, `FWD-9`
ingestion, `FWD-10` construction. `IRPT_FNTEND` owns every advisor-facing outcome and this project appears
there as a CONTRIBUTOR whose data, parity and execution obligations are graded inside that outcome. Two
projects, two decompositions, two task-order sets, two adjudications.

⛔ **NO FWD BELOW IS A WAIT.** The one genuine cadence — the mailbox poll under `FWD-9` — is DRIVEN on demand
for its proof and the organic case is the negative arm, per Rule 27's L2 clause.

---

## THE OUTCOMES — `FWD-1`..`FWD-8` ratified text verbatim @`58266dab2d`; `FWD-9`, `FWD-10` new; owner metadata is this cut's

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
         ACCEPT     ** IRPT_FNTEND ** -- see the counterpart
         OWNER
         THIS       the compact directory keyed to the signed-in firm and advisor;
         PROJECT    resolving a selection to the exact permitted account set BEFORE
                    any report is fetched; the directory as-of; and the guarantee
                    that search makes no provider call per keystroke
         SOURCE     brief O1; Andrew's "search for Clients by name, this routes the
                    tabs" -- carried; BK brief O1

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
         ACCEPT     ** IRPT_BCKEND ** -- server-side enforcement on every route is
         OWNER      this project's
         CROSSES    IRPT_FNTEND handles the refusal: no protected stale display,
                    honest permission states, and the negative fixtures
         SOURCE     brief O2; CTO 95142 (entitlement is an OUTCOME, not a property of
                    a search box); CLAUDE.md s.5 cross-firm rule -- carried; BK brief O1
         ⛔ NOTE    THIS IS THE HIGHEST-BLAST-RADIUS OUTCOME IN THE SET. A defect here
                    is a CROSS-FIRM EXPOSURE, and the estate's cross-firm rule is
                    SUBSTRATE-SHAPED with BOTH SHAPES LIVE (bucket-scoped Deny and
                    key-prefix + IAM condition). It is graded on its own, never as a
                    side effect of FWD-1
         ⛔ SEAMS (this cut, Andrew ~19:2xZ): the SAME cross-firm rule binds a second
                    time at INGESTION -- the firm is fixed from the sender's email
                    before anything is stored (FWD-10) -- and is GRANTED rather than
                    denied for the Opal-user global view (FWD-11). Three seams, one
                    rule; a grade on this outcome does not grade the other two

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
         ACCEPT     ** IRPT_FNTEND ** -- RE-OWNED on Andrew ~19:3xZ: the outcome
         OWNER      is the advisor READING and EXPORTING; see the counterpart
         THIS       canonical meaning, UNITS, dates, the vendor-calculation-only
         PROJECT    rule and the normalized contract -- graded INSIDE FWD-3's
                    adjudication as the data half; the PDF runs in this project's
                    worker
         SOURCE     brief O3, F2, F3; Andrew's "just generating a frontend view of
                    what Black Diamond/Orion already provide" -- carried; BK brief O2
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
         ACCEPT     ** IRPT_FNTEND ** -- RE-OWNED on Andrew ~19:3xZ: the outcome
         OWNER      is the advisor OBTAINING and EXPORTING in the tab; see the
                    counterpart
         THIS       the chain from validated input through captured request, job
         PROJECT    and result to a certified section -- graded INSIDE FWD-4's
                    adjudication; the runner style is his word (note below)
         SOURCE     brief O4, F7; Andrew's "just pulling a report of what YCharts
                    already provides" -- carried; BK brief O4; the intake's durability
                    is FWD-9 below, at Andrew
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
         ⛔ RUNNER STYLE IS ANDREW'S WORD, NOT A BUILD CHOICE (this cut, on
                    4.0.0_SA_CRO 191505Z): "use the exact same style of runner, that
                    strategy works very well. I do not believe they send OTP so dont
                    need that part." The BDAPI-with-Kimi runner style and the absence
                    of an OTP branch are FIXED; L5 chooses YCharts-specific details
                    inside that strategy, never whether to honor it

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
         ACCEPT     ** IRPT_FNTEND ** -- RE-OWNED on Andrew ~19:3xZ: the outcome
         OWNER      is the advisor SEEING holdings by model and drilling; see the
                    counterpart
         THIS       join correctness, the reconcile-before-and-after control, the
         PROJECT    denominators and the revision-bound nodes -- graded INSIDE
                    FWD-5's adjudication as the data half
         SOURCE     brief O5, F4; Andrew's per-partner overlay mapping, verbatim --
                    carried; BK brief O5; WS4 child brief @4a1d1ed9aa
         ⛔ NOTE    MODEL TARGETS MUST NOT MASQUERADE AS OBSERVED HOLDINGS. A residual
                    silently redistributed into sleeves fails this outcome even when
                    every total ties

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
         ACCEPT     ** IRPT_BCKEND ** -- ingestion, projection, refresh and the
         OWNER      expiry/fallback behaviour are this project's
         CROSSES    IRPT_FNTEND shows the as-of and the capability gap
         SOURCE     ⭐ **NOT IN THE BRIEF'S SIX. ADDED AT L2** -- carried; BK brief
                    O1 + O7
         (FWD-7 continues below; FWD-8 follows it.)
                    DONE WHEN and PROOF re-cut on `4.0.0_SA_CRO`'s L2 review (95180):
                    my first form read a HISTORY of consecutive refreshes, which has
                    NO NEGATIVE ARM -- a run of successes cannot show what a missed
                    or failed refresh does, and a SCHEDULE is not by itself a
                    MAXIMUM SERVED AGE. The driven form is strictly stronger and is
                    what the L2 "no FWD is a wait" clause actually demands
         ⛔ RULED BY ANDREW 2026-09-10 ~17:3xZ, VERBATIM "Stay visible." A
                    terminated client STAYS VISIBLE, MARKED TERMINATED, with access
                    still governed by ENTITLEMENT. So DISAPPEARANCE FROM SEARCH IS
                    NEVER EQUATED WITH ACCESS REVOCATION, and a terminated client or
                    account that still requires HISTORICAL reporting remains
                    reachable to an entitled viewer. This outcome now NAMES the
                    eligibility policy rather than deferring it, and L4 writes to
                    THIS rather than choosing. Raised by `4.0.0_SA_CRO` at 95180;
                    my first form assumed termination implies disappearance, which
                    was a decision I did not own and got the wrong way round
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
         ACCEPT     ** IRPT_FNTEND ** -- RE-OWNED on Andrew ~19:3xZ, his words:
         OWNER      "the branded export is arguably a frontend op, even if a
                    lambda does it, the lambda part is backend, how that report
                    actually looks and how the modals and etc work are all
                    frontend." See the counterpart
         THIS       the lambda: deterministic inflection selection, evidence and
         PROJECT    prose validity, the frozen bundle, and export execution --
                    graded INSIDE FWD-8's adjudication; the topic/sentiment
                    retrieval is a NEW seam whose owner is named at L5 (carried
                    from the ratified OWNER line)
         SOURCE     Andrew-direct 2026-09-10, verbatim: a "narrative arc" using "daily
                    cloud and trending topics over almost a full year", to "dynamically
                    assess what was the trending topic or buzz word/phrase from word
                    cloud that was occuring at that time ... to help qualify what was
                    happening at that time" -- carried; BK brief O6
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

  FWD-9  A forwarded holdings email becomes a durable, correctly scoped
         analysis request without anyone re-keying it
         ** RATIFIED -- Andrew ~19:2xZ, "call 1 yes." **
         DONE WHEN  EXERCISED -- a real forwarded message with its attachment
                    has become a request an advisor can see and correct
         ACCEPT     an advisor forwards a client's holdings by email during the
                    working day and, within a short time, sees it in Opal as a
                    request with the holdings read out of the attachment,
                    attributed to the right advisor and client, and with anything
                    the system could not read flagged for correction rather than
                    guessed; forwarding the same email twice does not create two
                    requests, and a genuinely new request that happens to carry
                    the same holdings is not thrown away as a duplicate
         PROOF      representative forwarded messages with real attachments,
                    retries, a restart while an attachment is being saved,
                    checkpoint recovery, a repeated forward, a new request with
                    identical holdings, an unresolved owner, ambiguous positions
         ACCEPT     ** IRPT_BCKEND **
         OWNER
         CROSSES    IRPT_FNTEND consumes the correction state
         SOURCE     BK brief O3; Andrew-direct ~19:2xZ (ratification)
         WHY NEW    NARROWED on 3.0.0_SA_CVO's review @8b2bbe2085: the ratified
                    FWD-4 ALREADY names the email channel, attachments, correction
                    and programmatic inputs in its notes, so the intake is NOT
                    wholly uncovered and my first cut said it was. What NO ratified
                    outcome grades is DURABILITY -- a restart mid-attachment,
                    checkpoint recovery, a repeated forward not becoming two
                    requests, a genuinely new request with identical holdings not
                    being discarded. That is this outcome's territory.
         ⛔ THE FIRM IS DECIDED FROM THE SENDER'S EMAIL AT INGESTION (Andrew
                    ~19:2xZ, in his FWD-10 sentence): the request's FIRM is fixed
                    by the sender's domain the moment the message arrives and
                    cannot be changed after; it BOUNDS which advisors and clients
                    "attributed to the right advisor and client" above may
                    resolve to, without itself choosing them. The construction
                    and its proof live in FWD-10
         ⚠ WHAT HIS WORD FIXES AND WHAT IT DOES NOT (3.0.0_SA_CVO 194256Z): the
                    sender's DOMAIN fixes the FIRM. It does not by itself fix
                    WHICH ADVISOR within that firm (the sender? a named
                    advisor?) or WHICH CLIENT (from the attachment? the subject?).
                    Those two bindings are resolved at L4 from the brief's intake
                    design and are NOT read into his sentence here
         ⚠ CADENCE  the brief names a 15-minute poll from 08:00 to 23:45 New
                    York, every day. That is the BRIEF's number, not ratified
                    here; no accept grades on it at L2. Its proof is DRIVEN.

  FWD-10 A request can only ever land in its own firm's storage, because its
         firm is fixed from the sender's email the moment it is ingested --
         so corrupting another firm's result is IMPOSSIBLE BY CONSTRUCTION
         ** RE-CUT IN PLACE on Andrew ~19:2xZ; id unchanged; RATIFIED ON HIS
            WORD -- one word reverses **
         DONE WHEN  EXERCISED -- a request has been ingested, bound to its firm
                    from the sender's domain, and every failure mode driven with
                    no effect on a second firm
         ACCEPT     the moment a request arrives, the firm it belongs to is decided
                    from the sender's email address and cannot be changed later;
                    that request, and everything produced from it, can only be
                    stored in that firm's own locations, which are written down as
                    a fixed list before the first request ever arrives; when
                    something goes wrong for one firm, the person running the
                    system can see what failed and fix it, and no other firm's
                    results can have been touched, because there is no path by
                    which they could be; a failed run never publishes a report
                    that looks complete but is not, never overwrites a newer
                    result with an older one, and never brings back a permission
                    that was taken away
         PROOF      ingest a request from each firm's domain and confirm it lands
                    only in that firm's enumerated locations; attempt to write a
                    bound request into a second firm's location and confirm
                    refusal; then the failure arms -- a failed source partition, a
                    stale model map, a duplicated event, an expired lease, a queue
                    replay, a worker restart, a revocation during a job -- each
                    shown to touch no second firm; a manifest names every
                    upstream dependency and its owner
         ACCEPT     ** IRPT_BCKEND **
         OWNER
         CROSSES    IRPT_FNTEND surfaces the partial, stale and unavailable
                    states through the shared status contract; the ENUMERATED
                    LOCATIONS list is a maintained artifact whose OWNER is named
                    at L4 -- CLAUDE.md s.5: "a new firm name is a GATE EDIT"
         SOURCE     BK brief O7 (the failure arms); Andrew-direct ~19:2xZ verbatim
                    (the construction); CLAUDE.md s.5 cross-firm rule, BUCKET or
                    KEY-PREFIX, both shapes live
         ⛔ WHY THE RE-CUT. My first form was a RECOVERY property -- an operator
                    recovers one tenant without corrupting another. Andrew: "this
                    should be impossible." Impossibility is a CONSTRUCTION claim,
                    and it is PROVEN by driving the failure modes and showing no
                    cross-tenant effect -- so the recovery arms survive as the
                    PROOF, not as the outcome. 3.0.0_SA_CVO's narrowing (FWD-2
                    already grades cross-firm ACCESS) stands: FWD-2 grades who may
                    SEE, FWD-10 grades where a request may LAND and what a failure
                    may not touch

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
         ACCEPT     ** IRPT_FNTEND ** -- RE-OWNED on Andrew ~19:3xZ: the outcome
         OWNER      is an Opal USER running reports across firms from a VIEW; see
                    the counterpart
         THIS       the cross-firm entitlement CLASS -- the same rule as FWD-2 and
         PROJECT    FWD-10, GRANTED to an Opal principal rather than denied to a
                    firm one -- and the multitenant api/scoped/ layout; graded
                    INSIDE FWD-11's adjudication as the entitlement half
         SOURCE     Andrew-direct ~19:2xZ, verbatim: "I want a 'Global' view, just
                    like how it's done in Model Portfolios, whereby an Opal User
                    can go through and run reports/analysis on ALL FIRMS"
         ⛔ MECHANISM IS HIS WORD, THIS SIDE (Andrew ~19:2xZ, third message):
                    "the backend multitenant api/scoped/ layout." The scoped
                    layout is FIXED as the pattern; L5 chooses its Investor
                    Reporting specifics inside it, never whether to follow it.
                    What that layout looks like in code is NOT READ at L2 -- L4
                    reads the existing implementation and cites it
         ⛔ PRECEDENT NAMED, NOT READ. "just like how it's done in Model
                    Portfolios" is recorded as the precedent. HOW MP does it is not
                    read at L2 and is not recalled here. An endpoint that guessed
                    the mechanism from a title is the guess this phase exists to
                    prevent
         ⛔ NOT IN EITHER BRIEF. This came from Andrew after the briefs landed,
                    so the briefs' subtraction was complete over the briefs and
                    still missed it. The denominator for "what is nobody doing"
                    includes his words after the brief, not only the brief
```

**COUNT: 10 outcomes carried, MEASURED as ten `FWD-` blocks in this document (`FWD-6` has no block here; the
reverse subtraction says why). 7 ratified ids, text verbatim (`FWD-1`, `2`, `3`, `4`, `5`, `7`, `8`); `FWD-9`
RATIFIED; `FWD-10` RE-CUT and ratified on his word; `FWD-11` NEW and ratified on his word. ACCEPT owner AFTER
THE ~19:3xZ RE-OWN: IRPT_BCKEND 4 (`FWD-2`, `FWD-7`, `FWD-9`, `FWD-10`); IRPT_FNTEND 6 contributed to here
(`FWD-1`, `3`, `4`, `5`, `8`, `11`). `FWD-12` (design) is the counterpart's alone; this project is NOT ENGAGED.
(An earlier count said eleven and an earlier line said BCKEND 8 / FNTEND 1; both were wrong and both are gone —
caught by `3.0.0_SA_CVO` 194256Z.)**

---

## THE UNCOVERED PARTITION — hunted BY SUBTRACTION, and this is where the two new ids come from

**Denominator: the BK brief's 7 outcomes (O1–O7).** O1→FWD-1 + FWD-2 · O2→FWD-3 · O4→FWD-4 · O5→FWD-5 ·
O6→FWD-8 · O7's directory-refresh half→FWD-7. **7 minus 5 (whole) minus 1 (half) leaves O3's DURABILITY half (restart, checkpoint, idempotency) uncovered and
O7's RECOVERY-isolation half uncovered.** Those are `FWD-9` and `FWD-10`.

⛔ **WHY MY DISTRIBUTION AMENDMENT DID NOT FIND THESE.** It asked *where do the eight belong*. It never asked
*what do the briefs contain that the eight miss*. A partition of a fixed set is structurally unable to see a
member outside the set. **Only a subtraction from the BRIEF's own denominator can.** Andrew asked whether I had
run this phase; I had not, and this section is the difference.

**And `FWD-11` is from OUTSIDE the brief.** It arrived as an Andrew-direct minutes after the briefs landed. The
subtraction above was complete over the briefs' seven and still could not have found it — the denominator for
"what is nobody doing" is the brief PLUS his words after it.

**Reverse subtraction — ratified ids the BK brief does NOT serve: `FWD-6`.** Advisor-facing degradation is
IRPT_FNTEND's; BK contributes the status contract inside O7. Not uncovered; owned elsewhere.

## WHAT L2 DOES NOT DECIDE

Cells, owners, sequencing, lanes (L5/L6). Every number the brief names — the 15-minute poll, session-recovery
bounds, retry counts — is the brief's proposal, MEASURED then declared downstream, never ratified at L2. Which
shared contracts change and how (BK §II.3 is the inventory). Any live vendor call. **Nothing here authorizes
egress.**

⛔ **CORRECTED (this cut, on `4.0.0_SA_CRO` 191505Z):** the first cut listed *"whether the YCharts runner reuses
the named pattern"* here as an L5 build choice. **It is not. The runner STYLE is Andrew's explicit word** —
*"use the exact same style of runner, that strategy works very well. I do not believe they send OTP so dont need
that part"* — and it is FIXED in `FWD-4`'s block above. What L5 decides is the YCharts-specific implementation
inside that strategy, never whether to follow it.

## WHERE THIS LANDS (F4) — **NOT YET LANDED**

Ready to paste under **`## ENDPOINT (step 2, /endpoint --forward)`** in
`org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`. **That path does not exist.** Same three
prerequisites as the counterpart. **`FWD-9`, `FWD-10` and `FWD-11` are on his word at ~19:2xZ, so the PRD header
may list all TEN ids this document carries.** If he reverses any of the three, that id goes vacant and the header
drops it — never renumbered.

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
`investor-reporting-ir-bk-brief-20260910.md` (and every source document its §IV.1 maps) → the cell(s) and
`FWD` that consume it, or an explicit `NOT CONSUMED: <why>`. A section with no consumer and no reason is a PRD
DEFECT the CVO grades at L9. The brief is the source of truth for detail; the PRD is its index into cells; the
FWD is what says whether the result counts.

## PROVENANCE (F5)

**GROUNDED ON:** the umbrella endpoint **at its pin** `git show 58266dab2d:…/ENDPOINT_FWD_INVESTOR_REPORTING_LIGHTWEIGHT_20260910.md`
lines 118–360 (the eight ratified blocks, extracted with a positive control that a bogus pin is refused);
`docs/briefs/investor-reporting-ir-bk-brief-20260910.md` @`efa5a94bf1` lines 1–64 and §II.1–II.3;
`docs/briefs/investor-reporting-ir-fe-brief-20260910.md` @`efa5a94bf1` lines 1–66 and §II.1–II.2 (every
CROSSES line); `4.0.0_SA_CRO` 191505Z for Andrew's runner words (quoted from that relay; the underlying
Andrew-direct record is the CRO's); `org/standards/PROJECT_TREE.contract.json` (the code grammar).
**NOT READ:** the TO register; any `org/projects/*.json`; the nine source documents beneath the brief; the WS4
child brief's body (cited for `FWD-5`'s lineage only).


---

## ADDENDUM 2026-09-11 ~00:5xZ -- FWD-4 gains one CONSTRAINT+ line (L2, `1.0.0_SA_CTO`); no FWD is added, renumbered or retired

Source: the CRO's Andrew-directed midstream supplement `docs/briefs/investor-reporting-ycharts-session-recovery-brief-20260910.md` @`9a71ef7626` (Part I O1-O5, Part III). Carried into `IRPT_BCKEND_PRD.md` v0.5 as the line below, verbatim; the ratified DONE WHEN / ACCEPT / PROOF / CONSTRAINT lines of FWD-4 at pin `58266dab2d` are untouched.

```
  FWD-4  CONSTRAINT+ (v0.5, supplement @9a71ef7626) a session is USABLE only after the intended authenticated identity and a report-capable response shape are verified from the transport that will use it (a cookie, a 200, a dashboard screenshot, EC2 Running or SSM Success is insufficient); recovery RESUMES the same immutable request revision and checkpoint; mutual displacement with the shared vendor login is ACCEPTED (Andrew, via the supplement) but repeated displacement reaches a retryable or attention state with the request preserved -- never an endless login contest, never a duplicate vendor portfolio or report; ONE automation owner of the shared vendor login at a time; the legacy `ycharts/credentials` contract and its consumers (YALP_MDSRC) are not overwritten and no competing refresh schedule is created
```

Why a constraint and not a new outcome: every sentence bounds HOW FWD-4's chain behaves under session loss; the advisor-facing outcome (an analysis in the same client context, exported) is unchanged. O3 and O5 of the supplement are operator evidence inside FWD-4 and FWD-10's proof arms, not outcomes an advisor sees.


---

## ADDENDUM 2026-09-11 ~03:1xZ -- FWD-4's mechanism is FIXED on Andrew's word (L2, `1.0.0_SA_CTO`); no FWD added, renumbered or retired

Andrew-direct, verbatim: *"Yes I wanted you to see this because that should be folded in for the YCharts backend flow, it is a crucial aspect of that operation as the frontrunner for it being possible."* Record: `ANDREW_DIRECT_20260911_031xZ_YCHARTS_CLOUD_PROOF_IS_THE_BACKEND_FLOW_FRONTRUNNER.md`. Carried into `IRPT_BCKEND_PRD.md` v0.9 as FWD-4's CONSTRAINT++ line; the ratified lines at pin `58266dab2d` are untouched.

```
  FWD-4  CONSTRAINT++ THE MECHANISM IS FIXED, NOT A BUILD CHOICE: session capture on the dedicated EC2 host by the K3 controller -> fenced publication of a versioned session -> browserless Lambda REST replay (identity by the structured page contract, Set-Cookie persisted across invocations) -> upload, portfolio, generation, PDF -- the chain proven in isolation in supplement VI.5 @f06c1951e1; the cells BUILD ON that packet's modules; the five boundaries VI.5 names unproven are acceptance arms of the cells, in order: the production session-secret cutover with its competing readers, concurrent publication fencing, real token-value rotation, cloud eviction / self-healing, Comparison and Multi-Comparison live proof
```

Same shape as the 09-10 runner-STYLE constraint: a mechanism Andrew has fixed is carried on the outcome, so no cell may re-derive it and no grade may read a different chain as equivalent.
