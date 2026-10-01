# DSGN_AMGTV1 ROUND 15 -- L8 COMPILE + L9 GRADES (the Friday round: AC4 of AV-f-1, f-2, f-3, f-5, f-6)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-01 ~07:4xZ
**Input:** `2.0.0_SA_COO~D`'s `round15/ROUND15_CLOSE.md` @`8dcf872b54` (4,315 B, read to EOF), msg 27588.
**L7 re-measured:** AV-f-1..f-6 read `complete` on their LAST `<status>` tag. Five judgment criteria are owed (f-4 carries none).
**Read by this seat:** `C:/tmp/dsgn-r15-close-render/list.png`, `thesis.png`, `exec.png` (a vite build of DEV `f4adf790`);
CloudWatch `/aws/lambda/opalinvest-auth-handler`; `portal/vite.config.ts:86-89`;
`infra/aws/opalinvest_dev/lambda/auth-handler/src/index.ts:284-291, 468-505`.

---

## 1. L9 GRADES

| order | AC4 clause | grade | what this seat read |
|---|---|---|---|
| f-1 price bars | on the close-render PNG **of the price face**: biggest mover first, sign of each move, one design family | **NOT GRADABLE** | No PNG of the price face exists: the states sweep never captures it (packet section 2). A judgment criterion with no artefact is not met. |
| f-2 chatter bubbles | on the close-render PNG **of the chatter face**: which names were collected most this month; step back two months | **NOT MET** | `list.png`'s chatter face renders "Read failure -- the articles collected could not be read." The render fixtures carry no `collected/chatter` capture. No bubble is drawn, so nothing can be read. |
| f-3 panel header | beside /philosophy: the panel **and the selected-name header** read as one card family with the portal | **PARTIAL** | The panel header (`list.png`) is the card face: eyebrow "SECURITY ANALYSIS", title "What is moving", icon, grid band, shared Segmented controls. The selected-name header (`thesis.png`, `exec.png`) is not: see f-6. The Thesis empty state reads "Select a name from the **Lead Panel** to open its Thesis." That is FWD-23's forbidden internal name, on a face `panelhead.cjs` does not grade. The render run holds no /philosophy capture, so "beside /philosophy" was judged on the card face's known elements, not side by side. |
| f-5 pack sentences | on the **walk's** BA Thesis and Exec PNGs: nothing on the two faces contradicts the other about the pack | **MET on the render; the walk's instance is VOID** | Thesis: "The research team's thesis pillars: no research pack for this security." Exec: "no management section, because neither a research pack nor an earnings update is on file for this name." Round 14's split (ADJUDICATION_v16 section 2) is closed on these faces. The walk is VOID (Z-S10), so this rests on fixture data, not a served read. A served re-read is owed. |
| f-6 header cards | beside /philosophy: a reviewer reads the same card family | **NOT MET** | `thesis.png` and `exec.png`: the four header cards render at uneven widths and do not fill their grid columns, and "MARKET FEATURES" wraps into and overlaps its own icon. Separately, the render's `sizes` (10px eyebrow) and `lowContrastChars` (48) FAILs sit on these cards. A reviewer would not read a family; they would read a broken grid. |

**Tally: 1 MET (on fixtures), 1 PARTIAL, 2 NOT MET, 1 NOT GRADABLE.** Three of the five sit on the demo's lead view and header.

## 2. Z-S10 -- the void walk: re-measured on the backend's own log

The packet says the shared auth backend answered **500** to `POST /auth/refresh` twice (walk `20261001T070037Z` netlog lines 259,
263). Read against the handler that serves that route:

- **The path is real.** The dev server proxies `/auth` to the deployed distribution (`portal/vite.config.ts:86-87`, target
  `https://d2n2nzpeqf34ge.cloudfront.net`), and `comp-routes trace /auth/refresh` resolves CloudFront behavior `/auth/*` to
  origin `APIGateway-portal`. The handler is `opalinvest-auth-handler` (`index.ts:284-291`).
- **The handler's only 500 is its catch path** (`index.ts:505`), and that path writes `console.error('Error:', ...)` first
  (`:469`).
- **CloudWatch, 06:59-07:20Z:** 22 auth requests reached the handler, 15 of them `POST /auth/refresh`, including the paired
  refreshes at 07:00:41Z and 07:00:49Z. **0 `ERROR` lines in the window.** The 4 `ERROR` lines since 05:00Z are all
  "Invalid email or password" (05:03, 06:30, 06:37, 06:46), which map to 401, not 500 (`:492-493`).
- **Volume:** 856 refreshes since 09-29 (357, 425, then 74 on 10-01 so far). Refresh is in daily use.

**Reading:** the handler did not produce the 500 the walker saw. It arose between the browser and the handler: the local
vite proxy (whose own proxy errors surface as 500), API Gateway, or CloudFront. **This walk is not evidence that PROD auth refresh
is failing.** It is evidence that the signed-in walk on the 5174 dev path is broken. The two have different owners and different
demo consequences. One discriminating act settles it: a refresh with a live session cookie sent straight to
`https://d2n2nzpeqf34ge.cloudfront.net/auth/refresh` (no vite proxy). A 200 places the defect in the dev proxy; a 500 places it at
the edge or gateway. The disarm owner's call; this seat does not arm the walker (arming a walker arms a real account).

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-S10` (BLOCKING/ARMED: auth refresh 500, the walk VOID) | **ROUTED**, stays ARMED, disarm owner `1.0.0_SA_CTO~Z` | re-measured (section 2): the handler served every refresh in the window without its 500 path; the 500 is upstream of the handler. The discriminating act is named. |
| `Z-W56-S1..S4` | **CARRIED**, INERT | as the packet; S3 (the ranking caption under an unserved chatter payload) is visible on `list.png` |

## 4. L10 PRECONDITION

1. **Every task order terminal:** 6 of 6. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-S10` ROUTED to its disarm owner with the re-measurement. **MET** (dispositioned,
   not disarmed)
3. **Every judgment criterion graded:** 5 of 5 (f-5 MET on fixtures; f-3 PARTIAL; f-2 and f-6 NOT MET; f-1 NOT GRADABLE). **MET**

## 5. FOR THE ROUND-15 ANALYSIS (the freeze is 22:00Z)

1. **Header cards** (f-6) are the most visible defect on every name's page: widths, the overlapping "MARKET FEATURES", the 10px
   eyebrow and its contrast. One cell.
2. **The render instrument cannot see the two demo faces.** It has no `collected/chatter` fixture and no price-face capture, so f-1
   and f-2 cannot be graded by any re-run until it does. RESAPP round 56 shows the route's live shape (ADJUDICATION_v68 there):
   95 rows, 73 with no month, and `by_publisher` omitting zero publishers. Build the fixture from that read.
3. **"Lead Panel"** on the Thesis empty state, and any other face outside `LeadPanel.tsx`.
4. **Z-S10:** the direct-to-CloudFront refresh read decides whether this is a demo risk or a dev-path defect.

---

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S18",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-01T07:45:00Z",
    "one_line": "L9 round 15: f-5 MET on fixtures (Thesis and Exec agree the pack is absent); f-3 PARTIAL (panel header is the card face; selected-name header is not; 'Lead Panel' on the Thesis empty state); f-6 NOT MET (header cards uneven, 'MARKET FEATURES' overlaps its icon); f-2 NOT MET (chatter face 'Read failure', no fixture); f-1 NOT GRADABLE (no price-face PNG). Z-S10 re-measured: opalinvest-auth-handler served 15 refreshes 06:59-07:20Z with 0 ERROR lines -- the walker's 500 arose upstream of the handler (dev proxy, API GW or CloudFront), not evidence of a PROD auth failure.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-AV-f-1..f-6 read 'complete' on their LAST <status> tag.",
        "C:/tmp/dsgn-r15-close-render/list.png: chatter face 'Read failure -- the articles collected could not be read.'; panel header eyebrow 'SECURITY ANALYSIS', title 'What is moving'; thesis empty 'Select a name from the Lead Panel to open its Thesis.'",
        "C:/tmp/dsgn-r15-close-render/thesis.png, exec.png: four header cards at uneven widths, 'MARKET FEATURES' overlapping its icon; Thesis 'no research pack for this security'; Exec 'no management section, because neither a research pack nor an earnings update is on file for this name'.",
        "CloudWatch /aws/lambda/opalinvest-auth-handler 2026-10-01T06:59-07:20Z: 22 '/auth/' requests (15 POST /auth/refresh), 0 ERROR lines; ERROR since 05:00Z = 4, all 'Invalid email or password'; POST /auth/refresh since 09-29 = 856.",
        "infra/aws/opalinvest_dev/lambda/auth-handler/src/index.ts:469 console.error on catch; :505 the only 500; portal/vite.config.ts:86-87 '/auth' -> https://d2n2nzpeqf34ge.cloudfront.net."
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-S10"
    ],
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The close record @8dcf872b54 asserts 6/6 terminal, a render run that FAILs on regressions plus instrument lag, and a void walk because the shared auth backend answers 500 on refresh.",
    "world_is": "The grades above; and the auth handler itself returned no 500 in the walk window, so the 500 is upstream of it.",
    "notes": "FOR THE ROUND-15 ANALYSIS: header cards (f-6); chatter fixture + price-face capture so f-1/f-2 can be graded; 'Lead Panel' outside LeadPanel.tsx; one direct-to-CloudFront refresh read to place Z-S10."
  }
]
```
