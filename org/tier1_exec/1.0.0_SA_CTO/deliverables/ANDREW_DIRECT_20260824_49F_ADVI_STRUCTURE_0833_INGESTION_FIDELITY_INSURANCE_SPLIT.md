# ANDREW-DIRECT 2026-08-24 ~16:0xZ (base CTO terminal) -- 49 FINANCIAL AS A WHOLE: Advisor Intelligence via Schwab 0833 (limited history accepted for now); Fidelity as a comparable ingestion next; the ADVI project SPLITS into functions -- INSURANCE assets from Black Diamond's insurance endpoint as a separate project (backend bucket pattern + light gold + platinum + three frontend integration points; NEVER blended into asset-management calculations)

**Recorded by:** `1.0.0_SA_CTO` (addressed seat) - **archetype:** SCRIBE / COORDINATE
**Context:** his first of three findings from the 49 Financial meeting (Mike), delivered at the terminal
after the six open-calls rulings (~15:2xZ). He asked that this ENTIRE block be logged as an Andrew
Directive before the next two findings. Quoted exactly as typed. Two further findings follow in their
own records.

## VERBATIM

> "FIrst I want to bring some more clarity in on 49 as a whole. Looks like we're clear on setting up
> Advisor Intelligence for them via the 0833 Schwab account. This does not have significant prior
> history, but that is fine for now. The way we'll handle is by effectively splitting the ADVI project
> for them into several functions. On ingestion, we are going to be primarily leaning on the Schwab 0833
> which we've already been ingesting/processing via opal-data-assets. Soon we will get a Fidelity login
> and can create a comparable ingestion/processing function for that which will be aggregated for ADVI
> for 49. Moving from there, there are two separate projects that split out. 1 is the Insurance assets,
> these can be pulled as current value snapshot from Black Diamond's insurance endpoint. The project
> there is going to be figuring out how this integrates backend and frontend. Backend I think we create
> a bucket somewhere in opal-data-assets for black diamond with an insurance subfolder or something
> like that which is subfoldered again to 49. This creates the pattern for how we structure insurance
> NAVs per account on Black Diamond (which will be good to have because this will have to be done later
> for Cottonwood as well as they use Black Diamond and have an insurance book). That covers
> bronze/silver ingestion, the gold transformation will be very, very light, we don't do any analytics
> on this we basically just transform as necessary through an additive script that will keep some kind
> of current state rows in a gold subfolder with in-pattern structured parquets in opal-data-49financial
> (i believe we already have some prior art on setting up this bucket as a home / default structure for
> client queryable data). This goes into some platinum json output which will be readable by the
> portal. Then on the portal frontend, we will need to create a handful of integration points for
> Insurance assets. 1.) We can't blend this in to any asset management calculations because the format
> is too different (asset management is what we do now, it's rigidly time-series and highly
> quantized/qualified; trying to layer in current day Insurance accounts to that is a category error
> and cannot happen). As a result I think in the header view (PartnerAnalytics.Tsx) we feed in the
> insurance segment total NAV to add onto the asset management AUM in the subtext of that panel on the
> default view somehow. 2.) At the account-level, we figure out how to demonstrate an insurance view
> that is separate from the asset management assets that shows their insurance assets, maybe feeding
> that value into their total assets radial chart as it's own segment "Insurance" (NOT folding into
> "Alternatives"). 3.) Because we do this operation at the account level, that means it can aggregate
> up to client/relationship level, up to advisor level, and ultimately up to Firm level in the "Books"
> or related tab views. I think we save ourselves the trouble of trying to figure out how to
> incorporate this into the Advisor or Distribution tabs, and just avoid that categorically. It
> effectively only lives in the "Books" drilldown or the Advisor's "Book" view on their
> advisorpublicprofile component. I will give you two more findings from this meeting after you have
> logged this entire text block as an Andrew Directive."

## WHAT IT BINDS (surfaced, unwidened; the phrasing is the ruling)

1. **49F ADVI runs on Schwab 08335338 ("0833").** History is limited and **"that is fine for now"** --
   this answers the D2 history fork for now: ACCEPT the 0833 floor; no frozen-tail act, no Schwab
   historical request, no BD history dependency is opened by this word. (The `ADVI_49FSRC` blend/
   history analysis stands as record; its stage-3 stays HELD -- see the second finding when it lands.)
2. **Ingestion = Schwab 0833 primarily, "already ingesting/processing via opal-data-assets"**; **Fidelity**
   is NEXT: a login is coming, and a **comparable ingestion/processing function** is to be created for it,
   **aggregated for ADVI for 49**. (A new custodian plane in the same grammar -- `opal-data-assets/
   fidelity/{firm}/{bronze,silver}` is the in-pattern candidate; not ruled here.)
3. **The ADVI project for 49 SPLITS into several functions; two separate projects split out.** The FIRST
   (this record) is **INSURANCE ASSETS**; the second arrives in the next finding.
4. **INSURANCE ASSETS -- the project:** *"figuring out how this integrates backend and frontend."*
   - **Source:** current-value SNAPSHOT from **Black Diamond's insurance endpoint** (a NEW BD read, snapshot
     grain -- not time-series).
   - **Backend pattern (his design, stated as "I think"):** a home in **`opal-data-assets` for black
     diamond with an insurance subfolder, subfoldered again to 49** -- i.e. the canonical grammar
     `{vendor}/{firm}/{medallion}` applied as `blackdiamond/.../insurance/.../49financial` (exact form is
     the decomp's to fix inside his words). **This creates THE PATTERN for insurance NAVs per account on
     Black Diamond -- to be reused for COTTONWOOD later** (BD user with an insurance book).
   - **Bronze/silver:** the ingestion above (Rule 17/17a bind: raw bytes at bronze; parquet + dtype at silver).
   - **Gold: "very, very light"** -- NO analytics; an **ADDITIVE script keeping current-state rows** in a
     gold subfolder as **in-pattern structured parquets in `opal-data-49financial`** (he believes prior
     art exists for that bucket as the home / default structure for client-queryable data -- it does:
     `opal-data-49financial/gold/advi/{canonical,dimensions,reference}/{table}/date={D}/`, the 08-19 mint).
   - **Platinum:** *"some platinum json output which will be readable by the portal."*
5. **FRONTEND -- three integration points, and ONE PROHIBITION that governs all three:**
   - ⛔ **NEVER blend insurance into ANY asset-management calculation** -- *"the format is too different
     ... rigidly time-series and highly quantized/qualified; trying to layer in current day Insurance
     accounts to that is a category error and cannot happen."*
   - **(1) Header view (`PartnerAnalytics.tsx`):** feed the insurance segment TOTAL NAV to be ADDED ONTO the
     asset-management AUM **in the subtext of that panel** on the default view ("somehow" -- form open).
   - **(2) Account level:** an insurance VIEW separate from the asset-management assets, showing the
     account's insurance assets; possibly feeding its value into the total-assets radial chart as its
     OWN segment **"Insurance" -- NOT folded into "Alternatives"**. (Rule 24: a new value on the radial's
     category axis -- the D1 taxonomy already carries Insurance as a top-level view, consistent.)
   - **(3) Aggregation:** because the operation is at ACCOUNT level, it aggregates up account ->
     client/relationship -> advisor -> Firm **in the "Books" or related tab views ONLY**. **Categorically
     NOT in the Advisor or Distribution tabs.** It lives in the **"Books" drilldown** and the Advisor's
     **"Book" view on `advisorpublicprofile`**.
6. **Process:** these are directive-class words for a NEW project (Rule 27 pipeline: register -> purpose
   PRD -> COO decomp -> TOs). Nothing is dispatched by this record. Registration + PRD follow once the
   three findings are all logged (his sequence).

## BROADCAST
MCP to every live seat + the queued seats that will hold cells (MSTR, CRO; COO, CVO, DS, DE, AE, DT,
0.6.0_AE_PartnerETL -- the BD vehicle owner). Same turn. Push state stated on the commit.

## DISTRIBUTION RESTRICTION -- Andrew-direct ~16:1xZ, immediately after the broadcast above, VERBATIM
> "Do not broadcast any of this to 4.0.0_SA_CRO i am working with them separately from this subject"

Binds this subject (the 49F meeting findings, all three) at this seat and at every relay: **no further
messages on it to `4.0.0_SA_CRO`.** Stated plainly for the record: finding 1 (66227) and the six
open-calls rulings (66216) had already been delivered to CRO's inbox before this instruction; nothing
further is sent, and no "disregard" is sent unless Andrew asks for one. Findings 2 and 3 are recorded
and broadcast WITHOUT CRO on the recipient list. MSTR informed same turn so the restriction binds at
the bridge.
