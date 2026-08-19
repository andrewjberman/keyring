# 49F DATA CALL -- Andrew Berman x Mike Little, 2026-08-19 (~60 min) -- ANALYSIS
**Raw:** `20260819_49F_mike_little_data_discussion.vtt` (same folder, byte-faithful).
**Caveat:** the VTT capture is LOSSY (many cues truncated mid-sentence); characterizations below
carry that; timestamps cite the condensed turn positions. Andrew's ask: analyze + store, directly
relevant to MDPF + ADVI.

## 1. WHO/WHAT
Mike Little = 49F-side data lead (ex-Tamarack/Black Diamond service team -- knows BD internals).
Waiting on **Databricks access** (Azure-hosted) via **Fulton May** (49F's third-party IT).
Follow-up call once access lands ("hopefully this week"). Luke = the 49F principal wanting a
data solution; "his reaction suggested he's open" to moving toward AWS (~57:36).

## 2. EXTRACTIONS THAT BIND TO LIVE WORK

### 2a. PARITY PROGRAM (push plan SS7) -- pre-register these as likely non-EXACT causes
- **BD-vs-Schwab discrepancies EXIST AT THE SOURCE** (~04:45): Mike has a live advisor case with
  "discrepancies between [BD and] Schwab." Our parity census compares three-way in effect --
  our figures vs BD's vs Schwab's own -- and a BD-vs-Schwab delta is NOT our defect. Pre-register.
- **Return method** (~02:07): BD's standard is the "simple" return; the more-accurate method is
  what investment people mean by return -- a named convention fork (the TIGHT-class candidate).
- **Fee timing** (~15:52, Andrew's impression): BD marks fees QUARTERLY, does not amortize --
  net-of-fee comparisons off-quarter will diverge by construction. Pre-register.
- **Market data** (~46:51-49:41): BD prices/dividends come from IDC-class vendors; dividend rates
  update quarterly. Price-source deltas are a parity denominator item.

### 2b. ADVI PRODUCT SIGNAL (validates the roadmap verbatim)
- **Item-3 overlay demand, named by an advisor** (~17:11-18:36): "a quick way to see what
  [model a client is in] without having to dig... oh yeah, seventy-thirty" -- the account-level
  model overlay is a stated 49F day-to-day need. GOES IN THE ITEM-3 PRD as the user story.
- **BD org model** (~06:22-09:58): portfolio groups = the scoping unit (admin sees firm; advisor
  sees own book); organization is "tribal knowledge." Keys discussion: relationship ID +
  account ID; admin output divides by portfolio group. Feeds the ADVI advisor-scoping views.
- **Advisor attribution** (~29:24-31:00): architect/consultant roles COME FROM BD; accounts
  tagged to "49F house" or advisor-implicit (the Travis/373M example) -- confirms the R-1
  role_aua consumption ruling's premise.
- **Small-account admin burden** (~31:00, Luke+Hunter): tiny accounts (<$40K) cleanup view --
  ADVI already carries the local-ops chart; a named follow-on.
- **Meeting-prep + calendar/Salesforce link** (~37:04): executive view linking client meetings
  to model breakdown -- future ADVI feature signal.
- **Client-facing**: BD portal dated; Orion's is the modern bar (Plaid, full picture); ~90% of
  49F clients never log in (~21:00-22:46). Opal stays ADVISOR-LEVEL for now (compliance);
  client-facing later -- consistent with standing posture.

### 2c. MDPF / ITEM-1 TIES
- **SmartX<->BD join** (~18:36-20:21): one account can sit in multiple models; SmartX hashes;
  Andrew's current match ~99% -- wants PERFECT ("know it's perfect rather than an estimate").
  A named workstream: the exact-join spec (feeds Item 1 Custom/constituent models + MDPF).
- **Dividend/income view** (~47:24-52:24): projection function pulled earlier (responsibility
  concern -- Austin); Tamarack pattern = actuals backward, declared rates forward; a ~30-security
  scan over model holdings would be cheap. BANKED as a candidate, needs Andrew's word to revive.

### 2d. THE STRATEGIC ARC (the big one -- the infra-graph endpoint made concrete)
Andrew's proposal on the call (~34:25-46:24, ~55:00-58:46): Opal's Schwab-native centralized
pipeline (raw -> parquet -> gold) becomes 49F's data source; give Mike API access / scripts /
templates; **"replace the middleman entirely with Black Diamond"** (BD ~$400K/yr "to upload a
few tables"); possibly steer 49F from Azure-Databricks toward AWS (Mike open, Luke likely open);
Opal infra as the PARTNER TEMPLATE -- onboarding "days to a couple weeks rather than the
six-month lead time." **This is verbatim-adjacent to the infra-graph program's endpoint ("spin
up our entire Opal infrastructure for this new partner") -- the 49F/Mike thread is that
program's first live instance.** Andrew has already built Databricks-ready logic tables.
- **Salesforce as roles/location source** (~55:46-56:41): Mike proposes; Andrew skeptical of
  maintenance quality ("is it them managing their book or...?"); native API exists. OPEN QUESTION
  -- park until Mike has Databricks access + the data is inspectable.

## 3. FOLLOW-UPS EMERGING (for the delegation pass; none dispatched here)
1. Parity spec addendum: pre-register 2a's four convention candidates (CRO methodology + the
   harness classifier).
2. Item-3 PRD: fold the 2b user story verbatim.
3. SmartX<->BD exact-join spec (Item 1 / MDPF adjacency).
4. Partner-data-platform thread: prep the API-access/template package for Mike (gated on his
   Databricks access landing + Andrew's word on scope); tie to the infra-graph program as its
   first instance.
5. Dividend-scanner candidate: banked, Andrew's word to revive.
6. Next Mike call: after his access lands; agenda = joint look at what's in Databricks + the
   AWS question.
