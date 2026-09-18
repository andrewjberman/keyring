# Andrew-direct ~17:4xZ 2026-09-18 -- Peers: a solution built on Seeking Alpha's peers comparison

**Recorded by:** `4.0.0_SA_CRO~Z`, at this terminal, before the first call it authorizes. Context: the panel series
moved to PEERS (after Lead Panel, Thesis and Exec Management), under his standing direction that each panel is briefed
current / desired / delta, and that the product is the process that instantiates a NEW security.

## Verbatim

> Let's begin with Peers. What I'd like to do here is figure out a solution with Seeking Alpha where we basicaly pull
> the information from here: https://seekingalpha.com/symbol/{TICKER, e.g. BA for Boeing}/peers/comparison. I have
> included a HAR so you can understand the shape: "C:\Users\Opal Bloomberg\Downloads\seekingalpha.com.har"

## Reading, narrow

1. **The design target:** the Peers panel takes its peer set and comparison data from Seeking Alpha's peers
   comparison for each security.
2. **The HAR** is read for SHAPE only: endpoints, query field names, response structure. No header, cookie, token or
   account identifier from it is printed, stored in the repo or replayed. It is his browser session, and a seat does
   not exercise a person's login.
3. **Egress:** a minimal feasibility probe -- two unauthenticated GETs for Boeing (the suggested-peers endpoint and
   one metrics call), honestly identified, no browser impersonation, no attempt to get past bot protection. A producer,
   a schedule, a pool write or any use of his session is NOT covered and comes back to him.
4. Seeking Alpha's terms of use on automated access are raised to him, as Bloomberg's were, not decided here.

**Done under item 3:** three unauthenticated GETs for Boeing (the two named, plus the metrics call repeated once to
print every value). All returned 200 JSON; BA's forward P/E came back null and flagged not meaningful.

## Addendum ~17:5xZ -- use the parked session through the existing REST function

Verbatim, in order, as this seat was reading the HAR:

> yes but that can be worked into the pull mechanics, we have that set up already in the opal-data-harvest ecosystem.
> You should be using a cookie via rest api, that is the point of sending you the HAR to see the endpoints

> look into the opal-data-harvest REST API lambda ops, you should just be able to hit the rest api with the necessary
> bundle

> you shouldnt have to build at all, you should just take the existing function that is designed for the rest api hit
> (not the crawler script), and test the endpoints we need for Peers

> the rest fetch is probably it, that looks like the one

**Reading, narrow:** a TEST of the Peers endpoints (suggested peers, tickers with GICS, metrics, metric grades) through
the existing `integrations/seekingalpha/rest_fetch.py` -- its own `load_config`, `build_session` (the PARKED session
bundle from Secrets Manager, egress through the residential proxy) and `_do_get` (Referer, logging and block
detection) -- for a few subjects. This supersedes item 2's "not replayed": his word covers riding the parked session
for this test. **Not covered:** the harvester or any sign-in (his "not the crawler script"; if the parked session has
aged out, the test STOPS and says so); `run-ticker`'s landing of raw bytes in `opal-data-harvest` (responses stay in
the session scratchpad); any schedule or producer; any new fetch code in the repo.

**Done:** 15 GETs (BA, SAP, KDDIY x suggested peers, tickers+GICS, two metrics groups, grades) through
`rest_fetch.load_config` / `build_session` / `_do_get`, all classified OK by `detectors.classify`. The parked session
(captured 2026-09-11T02:13Z) was accepted. Nothing was landed in any bucket; bodies and the request log sit in the
session scratchpad (`sa_peers_test/`). No cookie, proxy credential or session value was printed.

## Addendum ~18:0xZ -- three rulings on the Peers shape

Put to him: the Peers V eight-peer floor against SA's five peers; the two CSC columns SA does not carry (5-year EBIT
growth, 5-year FCF growth); preferred and minority interest arriving as one SA field. Verbatim:

> It's now 5 instead of 8, we'll fit to the SA shape. If we can get the remaining two from BBG then do that, if not,
> fall back to what SA provides, as a general rule for the pipeline for that process. Yes we can do that in SA shape.

**Reading, narrow:**
1. **The Peers V peer floor is 5, replacing his earlier ruled 8** (`lib/research/scores/peers_v.py:64`, asserted at
   `:70`), and the panel fits SA's shape. **Consequence, stated for the CTO to confirm rather than assumed silently:**
   the per-measure floor `MIN_PEERS_PER_MEASURE = 6` (`:62`) sits above five, so with SA's five peers no measure would
   ever compute. "Fit to the SA shape" is read as moving it to 5 as well; the measure-count floor (`|M| >= 3`, `:69`) is
   not touched.
2. **A general rule for the Peers pipeline:** a column SA does not carry is taken from Bloomberg if Bloomberg has it;
   otherwise the pipeline falls back to what SA provides.
3. **Preferred and minority interest are shown as SA's single combined field.**

**Then, verbatim:** *"Agree with everything youve got write up the brief and issue to CTO~Z"* -- which confirms item 1's
consequence (the per-measure floor moves to 5 with the peer floor) and directs the Peers brief to `1.0.0_SA_CTO~Z`.

## Addendum ~18:3xZ -- MODEL panel: the source for forecast years

Asked, on the Model panel, whether forecast years (FY1-FY3 consensus) should come from Bloomberg's `BEST_` fields or
from Seeking Alpha. Verbatim:

> I'd use Bloomberg as primary, seeking alpha as a fall back.

**Reading, narrow:** Model-tab forecast years take Bloomberg consensus first; where Bloomberg has no value, Seeking
Alpha's, labelled as SA's. This is the mirror of the Peers rule (SA first there, Bloomberg filling). It does NOT answer
the separate question of the Upside / Base / Downside cases, which stays open.

**Then, verbatim:** *"write it up and get it over to CTO~Z. I told them after they receive this brief and integrate it
into their flow, they may proceed with COO~Z. You and I will proceed to Posture regardless, but the greater fabric does
not need to be held up on that."* -- the Model brief goes to `1.0.0_SA_CTO~Z`; on integrating it, the CTO may proceed
to `2.0.0_SA_COO~Z` without waiting for the Posture brief.
