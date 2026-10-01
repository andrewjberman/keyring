# DSGN_AMGTV1 -- ROUND 15 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-01 ~07:3xZ

**Input:**
- the CVO slug, msg 27599, `ADJUDICATION_v17.md` @4ebd70149f (6 of 6 terminal; AC4: 1 MET on fixtures, 1 PARTIAL,
  2 NOT MET, 1 NOT GRADABLE);
- the drain-end read @8dcf872b54 (render FAIL 16 of 75: 3 regressions and 4 instrument lags);
- CRO~Z's trace `UI_WALK_AUTH_END_TO_END_GAP_BRIEF_20261001.md` @a4b87b85f3.

PRD v0.6 is ADMITTED. CONTRACT amendments 1 and 2 apply. **The freeze is Thu 18:00 ET (22:00Z).**

## 1. WHAT THE ROUND DELIVERED

Six orders reached portal DEV f4adf790:
- f-1, the ranked price bars;
- f-2, the chatter bubbles;
- f-3, the panel header in the card family;
- f-4, the served-day header;
- f-5, the pack sentences;
- f-6, the header cards through GraphicCard.

**Round 15 is CLOSED.** Three of the five graded faces sit on the demo's lead view and header, and none is demo-ready yet.

## 2. Z-S10 -- placed and DISARMED (this seat is the disarm owner)

**Cause (CRO~Z trace, CloudTrail):**
- A laptop seat shares the one walker account (`USER#usr_opal_ui_walker`).
- It armed the account at 06:57:07Z. Its end-of-walk disarm ran at 07:00:48Z and disabled the account.
- COO~D's session from 07:00:39Z then failed on refresh. The laptop re-armed at 07:08:10Z.

**Correction to CVO v17 section 2:**
- `opalinvest-auth-handler` DID produce the 500. A direct `filter-log-events --filter-pattern ERROR` over 06:59-07:20Z
  returns at least 4 events.
- Two of them are `ERROR Error: Error: Account disabled` at 07:00:49.060Z and 07:00:49.089Z (`r1`, the refresh
  function), the walk's paired refreshes. They are in exactly the `console.error('Error:', ...)` form of the catch path
  that returns 500.
- The v17 census reported 0 in that window. Its conclusion "upstream of the handler" therefore does not stand.

**Consequence:**
- This is NOT a PROD auth defect, and refresh is in daily use (856 since 09-29).
- It IS a walker-tool defect: two devices share one dormant account, and either device's disarm kills the other's
  walk.

**Disarm:**
1. Effective now: walks run one device at a time. MSTR~Z finds the laptop seat over `/agentbus`, and COO~D walks only
   after the laptop reports its disarm (msgs to MSTR~Z and COO~D, 07:22Z).
2. The fix is cell 1 below.

The row is DISARMED by (1); (2) is the repair.

## 3. RULINGS

| # | ruling | why |
|---|---|---|
| 1 | **The walker lease fix is DSGN's, round 16 cell 1.** Arm writes a conditional DynamoDB lease (`armedBy`, `armedAt`, written before SSM). Disarm runs only for the holder. A second arm while a lease is live waits or refuses, and never steals. | CRO trace; the close walk is the Friday acceptance read |
| 2 | **The render instrument must see the demo faces before any face is graded again.** It needs a `collected/chatter` fixture built from RESAPP's live shape (95 rows, 73 with an empty `by_month`, `by_publisher` with no zero publishers; RESAPP v68) and a price-face capture. | f-1 and f-2 cannot be graded otherwise (CVO v17 sections 1 and 5.2) |
| 3 | **The chatter face's "Read failure" on the live page is expected until RESAPP round 57 deploys the route.** Until then the face renders the designed unavailable state in plain words, not a failure. After the deploy, the wiring reads the route. | CONTRACT section 4: a designed state, never a raw failure |
| 4 | **The header cards (f-6) are the most visible defect.** They need equal widths that fill the grid, no "MARKET FEATURES" overlap, an eyebrow of 11px or more, and contrast that passes. This cell also carries the 3 render regressions of the round. | CVO v17 section 5.1 |
| 5 | **"Lead Panel" must appear nowhere on any face** (it is on the Thesis empty state today). The selected-name header joins the card family (f-3 PARTIAL). | FWD-23 |

## 4. THE ENRICHMENT LIST -- round 16, `2.0.0_SA_COO~D`, ONE issuance (fan-out cap 3; the files are disjoint as listed)

| # | cell | files | criteria shape |
|---|---|---|---|
| 1 | walker lease (ruling 1) | the ui-walk arm/disarm module | a second concurrent arm is refused while a lease is live; disarm by a non-holder is a no-op; a planted race (two arms) leaves the first walk signed in |
| 2 | header cards + the 3 render regressions (ruling 4) | `HeaderCards.tsx`, `GraphicCard.tsx` consumers | equal widths; no overlap; eyebrow at 11px or more; contrast PASS; render regressions 3 to 0 |
| 3 | render instrument: chatter fixture from the live shape + price-face capture (ruling 2) | the close-render script and its fixtures | the price-face PNG exists; the chatter-face PNG shows bubbles from the fixture with the "N of 95" denominator |
| 4 | chatter unavailable state + route wiring (ruling 3) | `ChatterBubbles.tsx` | before the deploy: a designed sentence, no "Read failure"; after RESAPP r57: bubbles from the live route |
| 5 | "Lead Panel" removed from every face; the selected-name header in the card family (ruling 5) | the Thesis empty state, `SecurityOverlay.tsx` | 0 visible "Lead Panel" strings in the render; the header uses the card component |

**Order:** cells 1, 2 and 3 first; cells 4 and 5 after. Each build order carries at most three mechanical criteria.
**L9 (CVO, as a person):** cells 2, 4 and 5 on the render PNGs. **Close walk:** after cell 1 lands or the laptop
releases the account, whichever comes first.

## 5. ACTS ONLY ANDREW CAN DO (cited)

1. **The PROD promote payload beyond Security Analysis** (CVO verdict 27503).
2. **Recursive removal of the DSGN worktrees and scratch roots** (CLAUDE.md human confirmation for recursive deletion).
