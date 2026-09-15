# ANDREW-DIRECT 2026-09-15 ~05:1xZ (1:1x AM ET) -- at the `1.0.0_SA_CTO~W` terminal

**Channel:** Andrew, in person, at the `1.0.0_SA_CTO~W` terminal, site-Z fabric, answering the page-to-pipeline
diagram and the Z-S96 article-store seam this seat had just reported.
**Recorded by:** `1.0.0_SA_CTO~W`, same turn. **Project:** AMGT_RESAPP (D5). **Round at the time:** 10,
EXECUTING (ri-1, ri-2, ri-4 drained; ri-3 in flight). **Class:** L2/L4 DIRECTION for the page's shape, given
to the L4 owner directly. Nothing here is a cell; the decomposition is frozen mid-round.

## VERBATIM

> Yeah I think what needs to really happen here is that the main header panel is the source for the
> trending/breakout price/chatter stuff and also news at the company level (harvest publisher news feed as
> well as social feed) + a very simple description. I think to adam's point, there are actually four tabs on
> this page. 1.) Thesis; includes what the company is doing right now, what are their big challenges what
> are their big bets and happenings. 2.) Exec Management profile (CEO from Lusha + Maybe a targeted web
> search, would have to scope it) 3.) Peers; not sure how we decide this, Seeking Alpha is usually pretty
> good about this might be able to get it from them via one of their lists. 4.) Model; this is just a
> financial model like what Adam attached and we do it from their bloomberg financials + probably include
> some kind of analyzer of their filings. I want you to check out the message Yang Liu sent me on Teams
> about these new Claude for finance tools how theyre scanning earnings reports. I am wondeing if there is
> something we can use from that to scan the earnings/filings we pull from Bloomberg.

## VERBATIM, SECOND WORD (same terminal, ~05:1xZ, minutes after the first)

> I actually think there's one more function in here, and it either sits in the header and/or has a
> full tab at the very end called Posture. Posture is going to be an AI recommendation on what this
> stock means for Opal. In essence, we need to port over our opal-data-etfs info as a RAG system of a
> sort where the AI has access to Opal current holdings in DIVZ/IDVZ/PFDE/PFOE, and basically makes
> recommendatins for where it would see this security in an Opal Portfolio, "IF" it actually sees it
> in an Opal Portfolio, or if it thinks we should steer clear. This is probably the most crucial
> function of the entire pipeline, because its the final execution. So we need to think about how
> this would actually be structured.

**Reading, narrow:** a FIFTH surface, POSTURE -- a header element and/or a last tab -- carrying an AI
recommendation of where the security would sit in an Opal portfolio (DIVZ / IDVZ / PFDE / PFOE), if
anywhere, or steer clear; grounded on Opal's CURRENT HOLDINGS read from the `opal-data-etfs` plane as
retrieval context. He names it the most crucial function ("the final execution") and asks for its
STRUCTURE, not its build. It is a new OUTCOME (the recommendation is machine-written prose and falls
under FWD-9's marking rule and the verbatim gate by construction) and a new CONTRACT (AMGT READS the
ETF holdings plane, which is the `~Z` fabric's POSN_ASTTAX / ETFS_* domain; it never writes it). The
structure proposal is this seat's reply at the terminal and the addendum's Posture section; no cell,
no vendor call, no model call is authorized by the word.

## VERBATIM, THIRD WORD (same terminal, ~05:2xZ)

> I think the gist of it is that we would run this harvest pipeline not only on the target 89 stocks,
> but also on whatever the Opal ETFs Holdings are. That way we can essentialy make asset/sector
> allocation calls by comparing the adjacent firms and what they'd do in the portfolio and make
> suggestions on where to trim or add or buy or sell.

**Reading, narrow:** the harvest UNIVERSE becomes the UNION of the coverage list and the current
holdings of the four Opal ETFs, so that every name Posture compares against has the same model
block, feed and filings evidence as the target name. Posture's output is allocation-shaped
(trim / add / buy / sell, at the asset and sector level, by comparison with adjacent holdings), which
makes it a RECOMMENDATION SURFACE, never an order: nothing here touches the trade pipeline, and "the
final execution" is Andrew's and the PMs' act on the page, not the page's act. The "89" is his count
of the target list; the measured universe file's count is printed in this seat's reply beside it.

## VERBATIM, FOURTH WORD (same terminal, ~05:2xZ)

> the Posture call is really a function of the following. If on a non-Opal security, it compares to
> the adjacent opal holdings (same sector similar size/characteristics), and basically identifies if
> this stock seems like a better pick or worse than the Opal comparable. If it is for an opal security,
> it does the same thing but for the non-opal holdings with the same characteristics/sector/size etc

**Reading, narrow:** Posture is a SYMMETRIC COMPARABLE-SET JUDGMENT. The comparable set is always drawn
from the OTHER side: a non-Opal name is compared with the adjacent Opal holdings (same sector, similar
size and characteristics), an Opal holding with the adjacent non-Opal names in the harvest universe.
The output is "better or worse pick than the comparable", with the comparable named. So Posture is
defined by three things the estate can measure and card: (1) the MEMBERSHIP test (is this security in
any of the four books at the snapshot vintage), (2) the COMPARABLE-SET rule (sector + size band +
characteristics, from the model block's header scalars and the ETF plane's classification), and (3) the
JUDGMENT over evidence the page already serves for both names (model block, feeds, filings, peers).
Nothing in it is an order.

## READING -- NARROW, AGAINST THE PAGE AS BUILT (refs/drains/rg-2-portal @a845a8be)

| his sentence | what stands today | what moves |
|---|---|---|
| the HEADER PANEL is the source for trending/breakout x price/chatter | the Lead Panel already is (RankedList / RankedChart, movement x subject) | stays |
| + news at the company level: harvest publisher feed AND social feed | the Coverage TAB reads the articles table; no social feed is served (S13 is measure-then-build) | the company-level feed moves UP into the header; the social feed joins it once S13 has measured a source |
| + a very simple description | the SecurityOverlay carries header figures and identity, no prose description | a description line joins the header (its source is to be named: Bloomberg description field, or the filings class) |
| four tabs: 1 Thesis | ThesisTab exists and today carries the model-block figures (the Model tab was CUT in round 5 and its figures rehomed here) | Thesis becomes what the company is doing now, big challenges, big bets, happenings -- prose over evidence, S9's drafting face with the verbatim gate |
| 2 Exec Management profile (CEO from Lusha + maybe a targeted web search, to be scoped) | no tab; no FWD carries it at PRD v0.5 (FWD-1..15) | a NEW tab and a NEW outcome; his ~05:04Z word at the COO~W terminal already names executive managers and Lusha; the web-search half is "would have to scope it" and is NOT an egress word |
| 3 Peers ("not sure how we decide this"; SA lists as a candidate source) | PeersTab exists; S8 THE PEER SET is BROKEN TODAY (48 of 54 stale) | stays a tab; its SOURCE question is open and SA's own lists are the candidate to measure first |
| 4 Model (a financial model like Adam's attachment, from Bloomberg financials + probably a filings analyzer) | the Model tab was CUT in round 5; its figures live in Thesis and the overlay; the model block (~20 line items x 10 FY + ~25 header scalars) is served from S3 derived/model_block/ | the Model tab RETURNS as its own tab carrying the model block; a FILINGS ANALYZER is a NEW capability over the earnings/filings pulled from Bloomberg |
| "check out the message Yang Liu sent me on Teams about these new Claude for finance tools" | -- | read at this seat through the Opal gateway, same turn; the assessment is in this seat's reply and log, not a commitment |

**NOT READ INTO IT:** no vendor call (Lusha, a web-search API, any Claude-side tool) is authorized by this
word; each stays on his per-use word. No cell is cut and round 10 is not re-cut. No FWD number is minted
here: the ENDPOINT's ids are permanent and a new outcome takes the next unused number at the addendum.

## THE CARRIER

This is a change to the ENDPOINT (new outcomes: the executive-management profile; the filings analyzer;
the header feed and description) and to the CONTRACTS (the Model tab restored; the Coverage tab's content
relocated), so it is a **PRD addendum at the round-10 L10** -- a `prd_version` bump that re-opens the
ratified-text half for `3.0.0_SA_CVO~W` and the brief half for `4.0.0_SA_CRO~W`, delivered by the notifier
to those `~W` lanes (the router's alphabetical pick lands on `~W` for this project, which is correct here
and wrong for POSN). The round-10 slug is the trigger; the addendum folds this word, the Z-S96
article-store choice, and the ~05:04Z executive-managers word into one bump, so round 11 cuts against one
PRD rather than three messages. Until then round 10 finishes as cut.

## ACTS THIS TURN

1. This record, committed.
2. Yang Liu's Teams message read through the Opal gateway; the assessment delivered to Andrew in reply
   and carried into the addendum's filings-analyzer outcome as a candidate substrate, carded (Rule 28)
   before any cell builds on it.
3. Broadcast to `2.0.0_SA_COO~W`, `3.0.0_SA_CVO~W`, `4.0.0_SA_CRO~W`, `0.0.0_AB_MSTR~Z`, push state stated.
