# DSGN_AMGTV1 -- ROUND 56, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~03:3xZ)

**Inputs:** `deliverables/2.0.0_SA_COO~D1/round56/ROUND56_CLOSE.md` @9a324af41b (msg 1455) and
`deliverables/2.0.0_SA_COO~D1/round56/WALK_SECURITY_ANALYSIS_DEV_0008ddd3.md` @82aafdc727 (msg 1568). The candidate review was sent as msg
1456 (PASS); this file is its carrier.

## 1. What is live

Portal DEV `0008ddd3` = `8d2a08a9` + AV-zzh-1 (3 Freshness files). PROD unchanged.

## 2. Graded

- **AV-zzh-1 (R1, one date form): MET.** Every page-drawn day on `/freshness` reads the long form, with ISO only in `data-day`. The
  test pins the cell and PageEnd together, and the 02:24Z walk confirms it. The one ISO left is in served words, which is a producer
  fact (AMGT_RESAPP-D1-S1), not the page.
- **Noted, not a defect:** the page grew from 4,293 to 5,593 px because the nowrap long dates widen the columns. No walker flagged
  layout, so no cell is cut for it.

## 3. Rulings on the `/security-analysis` walk (DEV 0008ddd3)

- **R1, the Enter-key search (P1).** Pressing Enter on a typed name fetches by the raw text, gets a 404, and the error card says "the
  feed is down". Both halves are defects: (a) Enter must resolve the name exactly as choosing it from the suggestions does; (b) a
  not-found is said as "no security found for <text>", never as a feed outage. A page that blames the feed for its own lookup
  misleads the reader about the system's health.
- **R2, money in two forms (23 steps).** One money form per page, the one the portal's other pages use. This is the same rule as round
  55's date ruling.
- **R3, mixed dates on Model version picks.** The round-55 one-date-form rule extends to `/security-analysis`.
- **R4, timeline-day contrast under 3:1.** It must meet the portal's contrast floor (at least 4.5:1 for body text, 3:1 for large text
  and UI marks), measured on the walk.
- **R5, clipped element (step 26) and 2 truncated Price labels.** Nothing the reader needs is clipped. A label either fits or carries
  its full text on hover and focus.
- **R6, no Chatter "Earlier month".** A reader must be able to reach earlier months. If the producer serves no earlier month, the page
  says so in words.

## 4. ENRICHMENT LIST, round 57 (ONE issuance by `2.0.0_SA_COO~D1`)

1. R1: the Enter-key search resolution plus the honest not-found message, with a test of both.
2. R2 + R3: one money form and one date form on `/security-analysis`.
3. R4 + R5: contrast and clipping, graded on a walk.
4. R6: Chatter's earlier months, or the words saying none are served.
