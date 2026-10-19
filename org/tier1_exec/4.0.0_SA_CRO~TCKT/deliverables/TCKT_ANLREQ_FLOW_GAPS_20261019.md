# Ticket Center analysis-request flow -- gaps found 2026-10-19 (4.0.0_SA_CRO~TCKT)

Order: `ANDREW_DIRECT_20261019_165xZ_TCKT_ANALYSIS_REQUEST_FLOW_BREAKS.md` (same folder). Read-only research; nothing
written to AWS, portal or code. Portal lines cite `origin/DEV` (the dell2 `portal/` checkout is 141 commits behind).
Claim: M = measured (code read or live read), I = inferred.

## G1 NOT_AUTHORIZED on a staff filing for 49 Financial (design gate, not identity)
- M: `irpt-ycharts-generate` logs, 2026-10-19 16:38:54Z and 16:39:17Z (12:38-12:39 PM ET): caller admitted as
  INTERNAL, then `ProspectOwnershipRefused: advisor has no partner profile at the named firm` -> NOT_AUTHORIZED.
- M: refusing predicate `infra/aws/lambda/investor-reporting/_authz/served.py:1109-1111` (`_advisor_owner`, looks up
  the typed advisor email in `opal-partner-<firm>`); `served.py:1069` maps it to NOT_AUTHORIZED.
- M: `opal-partner-49financial` (11 rows) holds no dawson.moses; `opal-users-v2` (86 rows) neither.
- M: second gate on the same path, `served.py:1089-1091`: staff leaving the advisor email blank are refused
  ("must name the firm advisor"). Earlier runs worked around it with a synthetic advisor (5f19ba81e7, fec24f492d).
- Fix (I): in `_create_owner` (`served.py:1073-1093`) an Opal staff caller falls back to `access.prospect_owner()`
  when the advisor is absent or unprovisioned; the email becomes attribution only. Portal: advisor field optional.
  `authorize_current` already passes staff (`_scope/interactive_access.py:115-116`).

## G2 Firm list is a hard gate on staff submission
- M: `submitHeldReason` (`analysisRequest.ts:370`, origin/DEV) holds the submit until the firm list loads; only READY
  firms are offered (`TicketCenter.tsx:123`). A failed load or a non-READY firm blocks an Opal user outright.

## G3 Report-type dropdown is redundant
- M: select at `AnalysisRequestParts.tsx:190`; read by `answersRefusal` (`analysisRequest.ts:74-75`),
  `variantRefusal` (`:516`, called `:587`), `variant` (`:541`), submission body (`:295`).
- M: backend already derives the type from the count and accepts `variant: "auto"`
  (`ycharts/generate/submission.py:72-74`, `recipe.py:138-163`). Ticket service stores `report_type` from a fixed enum
  (`ticket_center/lambda_function.py:78, 119-121`) -- derive it client-side from the count.
- M: dropdown was added deliberately in portal `80d7c70a` (AR-y-275, 2026-10-13); removal reverses that ruling.

## G4 Opal model checkboxes wait on a four-step chain (not YCharts)
- M: firm list load -> firm choice -> 400 ms debounce (`TicketCenter.tsx:351`) -> `GET .../analysis/comparisons`
  (`comparisonCatalogue.ts`), which server-side also scans `etf-classifications`. Until then:
  "The Opal model list is not loaded." (`AnalysisRequestParts.tsx:199`). Failed fetch is never retried.
- M: the five models are a static `templates.json` in the backend; `getAllModelColors()` already holds them in portal.
- Fix: render the five models statically, large text (legend and labels are `text-xs`, `:196`, `:207`). Keep the
  catalogue fetch only for the free-text "Other ETFs" box.

## G5 "Form as filled" attachment re-fetches the catalogue per package only to print model names
- M: `AnalysisRequestParts.tsx` (`(names not loaded)` fallback, `:583`). Make static with G4.

## G6 The 400+ "text / NOT_IN_THIS_VERSION" cards
- M: "Open report" reads `GET .../analysis/{requestId}/sections` and renders every element of the PDF layout map as a
  card (`NativeSections.tsx:172-262`; producer `opal_producer.py:168-171, 532`). For REQ-d6231c013ae90519c67d18e9:
  427 elements = 280 builder-only + 144 vendor-sourced not-available + 3 with values.
- M: the green SUPPORTED badge is the report-level validation, not the card's status (`NativeSections.tsx:173`).
- M: AR-y-404 (`4050bbd629`, today) drops the 280 builder-only cards; does not rewrite stored reports; 144 remain.
  Deployment not read.
- The panel is an internal trace surfaced as the user deliverable. The board never opens the PDF (`pdf` kind
  deliberately excluded from the attachment list).

## G7 The four attachments never attach when commentary is off
- Spec (M): IRPT_ANLREQ PRD FWD-1 -- original upload, form as filled, Opal report PDF, commentary PDF; the packager
  (`ycharts/research/opal_packager.py`) posts them to `POST /tickets/{id}/package`.
- M: `resident_worker.py:254` (`send_ready_if_ticketed`) sends `analysis_ready` only when
  `commentary_requested is True`; the packager is triggered only downstream of it. No commentary -> no package, ever.
- M: TCK-20261017-5af976ff: `add_commentary: false`, no `package`; run.json COMPLETE, 61-page PDF retained (ART-1630441c,
  290,707 bytes) -- two of four files exist and are never attached. Zero package outcomes Oct 10-19 per the
  ~IB2 notes.
- Fix (I): package unconditionally on generation complete; commentary PDF is the optional fourth item.

## G9 Typed "Advisor login email" field (Andrew-direct 18:xxZ: remove; the signed-in email is known)
- M: field `AnalysisRequestParts.tsx:172` (origin/DEV), added by AR-y-378; validated by `advisorEmailRefusal`
  (`analysisRequest.ts:83`), sent as query `advisor_email` (`investor-reporting.ts:1233`). It is the input G1's
  `served.py:1109` lookup refuses on.
- Coupling (M): removing the field alone makes a staff filing hit `served.py:1089-1091` ("must name the firm
  advisor"). The field and G1's backend fix land together: the owner is the signed-in principal.

## G10 "Add commentary" checkbox (Andrew-direct 18:xxZ: remove; commentary on by default)
- M: checkbox `AnalysisRequestParts.tsx:227-229`, default `add_commentary: false` (`:71`), sent at
  `analysisRequest.ts:313`, echoed in the form-as-filled table (`AnalysisRequestParts.tsx:593`).
- Effect (M via G7): with `commentary_requested` True on every request, `resident_worker.py:254` stops skipping, so the
  packager is reached on every run. G7's decoupling (package on generation complete) still stands so a commentary
  failure cannot withhold the other three files (I).

## G8 Report link written two days late; no vendor calls on a Multi-Comp
- M: request accepted 2026-10-17 05:14:30Z; ticket `report_ref` written 2026-10-19 13:42Z.
- M: run.json `calls: []` on a Multi-Comp; I: comparison figures in the PDF are likely empty (144 vendor elements
  not available).
