# ANDREW-DIRECT 2026-09-10 (at the `4.0.0_SA_CRO~Z` terminal) -- the Seeking Alpha investigation, Bright Data parked for the interim, test the Kimi authenticator

**Recorded by:** `4.0.0_SA_CRO~Z` | **Channel:** typed into this seat's session, four messages
**Clock brackets:** this seat's own tool-log reads. Message 1 preceded the first browser navigation at
`2026-09-10T18:58:30Z`; messages 2-4 landed between `19:04Z` and `19:10Z`, each interrupting a tool call.
**Scope stance:** SURFACED, NOT ADJUDICATED. The receiving seat relays; it does not widen or narrow.

## VERBATIM AND COMPLETE

**Message 1** (the day's task, replacing the startup protocol):

> "No need to read all the startup shit. Here's what you're doing today. You are going to go check
> previous Seeking Alpha art for scraping via comp-find --corpus aws for cloud resources, normal
> comp-find for repo. you are going to read the PRD scope for the AMGT project that was just minted.
> You are then going to do a little investigation for me on Seeking Alpha whereby you run through a
> login protocol using bright data residential proxy and scrape and let me know how it goes. You are
> also going to do a manual playwright op with my credentials and see how they transfer auth. You are
> going to then try to pull data from a sample url via said REST API,
> https://seekingalpha.com/symbol/RTX/virtual_analyst_report and even
> https://seekingalpha.com/symbol/RTX. I want to know if we can just use REST API with my credentials
> as a paying user. Go now."

**Message 2** (after this seat had called the Bright Data support assistant once):

> "no reaching out to bright data support, we must drive straight to successful outcome"

**Message 3** (a question, answered in-session; recorded so the exchange is whole):

> "what do you mean no-KYC mode, are you implying that there is a mechanism wherby we can use login
> credentials/"

**Message 4** (the pivot):

> "I would recommend finding the BDAPI markdown in data/assets/docs or in /architecture that discusses
> how the computer vision kimi works, I think we may just say fuck bright data in the interim while i
> work on that kyc registration. i think it may make more sense to just have you be testing the bdapi
> kimi setup"

## WHAT THESE WORDS NAME, read plainly

1. **Message 1 IS the per-use word** `C-VENDOR-EGRESS` requires, for THIS investigation: Bright Data
   residential proxy, Seeking Alpha login with his credential, the two named URLs, the REST API. It
   does not extend to a scheduled consumer; a cell that would fetch on a schedule still needs its own
   word.
2. **Message 2 closes a channel:** no Bright Data support contact. The one call already made (a
   timed-out assistant query, `dialog_id 6aa30055f1890d17dd8545b7`) is disclosed; nothing further.
3. **Message 4 places the Bright Data KYC on Andrew** ("while i work on that kyc registration") and
   points the seat at the estate's own Kimi computer-vision authenticator (`bd_49f_auto_login.js`)
   as the mechanism to test. "In the interim" bounds it: the proxy is parked, not retired.
4. **Nothing here changes the AMGT_RESAPP boundary, the PRD, or any surface row.** The results are a
   CRO investigation deliverable (`AMGT_RESAPP_SEEKING_ALPHA_AUTH_INVESTIGATION_20260910.md`) for
   `1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~ZZZ` to fold into L4/L5 as they see fit.

Broadcast: MCP to `2.0.0_SA_COO~ZZZ`, `1.0.0_SA_CTO~Z`, `0.0.0_AB_MSTR~Z` in the same turn as this commit.
Push state: LOCAL. `0.0.0_AB_MSTR~Z` holds all pushes.
