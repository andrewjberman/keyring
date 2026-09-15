# POSN_AGGFIX -- surprise channel, INVESTIGATION v1 (round 1, site-Z fabric)

**Opened by:** `2.0.0_SA_COO~Z` at L6, in the round-1 issuance commit, 2026-09-15. **Home:** the project tree's channel. Lane `ANY`; the
gate `.tools/surprise-row-gate.py` validates every NEW row (schema, identity, coordinate, folder == project). **Append-only during the
round.** Every row goes inside the ONE fenced json array below, per `org/surprise_channel/schemas/investigation_item.schema.json`; a
worker's id is `POSN_AGGFIX-Z-W<slot>-S<k>`, a seat's `POSN_AGGFIX-Z-S<k>`.

```json
[
  {
    "id": "POSN_AGGFIX-Z-S1",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~Z",
    "surfaced_at": "2026-09-15T18:48:41Z",
    "one_line": "PRD v0.2 C-NO-SILENT-EMPTY describes the five books' failure fallback as 'writes aum 0 into each book' (:1798), but on a WHOLLY failed weight read the producer writes no current_holdings at all (load_aum_data returns {} at :1475-1477, and generate_positioning_data's `if aum_data:` gate at :2374-2381 with :2392-2395 omits the block and data_date); aum 0 arises only on a PARTIAL read. TO-A2-1 keeps both arms exactly, so no behaviour moves; the PRD sentence under-describes today's fallback.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D4/POSN/POSN_AGGFIX/prd/POSN_AGGFIX_PRD.md @cbd85e5cff :192-195 (C-NO-SILENT-EMPTY): 'The five model books keep their current failure fallback, which writes `aum` 0 into each book (`:1798`)'.",
        "infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py @605c03f81f :1475-1477: `except Exception as e:` prints WARN and `return {}` (the success return is :1474).",
        "same file @605c03f81f :2374-2381, inside generate_positioning_data (def at :2117): `aum_data = load_aum_data(data_date)`; `if aum_data:` extracts current_holdings, else `current_holdings = None`; :2392-2395 adds current_holdings and data_date to the output only when current_holdings is truthy.",
        "same file @605c03f81f :1796-1799: `'aum': aum_data.get(model_code, 0)` -- the 0 is reached only when aum_data is non-empty but lacks a code (a partial read)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "C-NO-SILENT-EMPTY (PRD v0.2 :192-195): a failed weight read leaves the five books with their current fallback, aum 0 in each book.",
    "world_is": "Two arms: a wholly failed read serves the shared file with NO current_holdings key and no data_date (every Models-mode book disappears for every viewer); a partial read writes aum 0 into the missing book only. The decomposition's AF1-s-6 parenthesis repeated the PRD's one-arm wording; TO-A2-1 states both arms and its A2-AC7/A2-AC8 prove each, and the producer's never-widen COO half names the wholly-failed arm as Branch B with a rollback.",
    "notes": "Carried for 1.0.0_SA_CTO~Z's round analysis: a PRD touch to C-NO-SILENT-EMPTY's sentence would align the text with the measured fallback; nothing in this round waits on it. Filed by the issuer at L6; it also opens this channel, which the row gate refuses to open empty."
  },
  {
    "id": "POSN_AGGFIX-Z-W3-S1",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~3",
    "surfaced_at": "2026-09-15T19:57:36Z",
    "one_line": "TO-B1-1 cell AF1-s-13 hands `internal` to the HoldingsTab mount and merges the aggregate 'into the Positioning data object the tab reads', but at portal edf85ce503 HoldingsTab declares no `internal` prop (passing it fails the portal typecheck, TS2322, measured) and in Models mode the tab renders its OWN getPositioningData fetch, not the page's object; both limbs need HoldingsTab.tsx, which TO-B1-1's <paths> do not hold, while TO-B2-1's <paths> hold HoldingsTab.tsx and not Positioning.tsx.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/pages/Positioning/tabs/HoldingsTab.tsx @edf85ce503 :599-626: the HoldingsTab props are customBlend, mode, etfData, satelliteData, bookStatus -- no internal prop and no models-data prop.",
        "same file @edf85ce503 :637 `const [modelsData, setModelsData] = useState<PositioningDataResponse | null>(null)`, :648-653 `dataByMode = { models: modelsData, etfs: etfData, satellites: satelliteData }`, :727-737 the tab's own `getPositioningData()` inside a useEffect: in Models mode the tab reads its own fetch and never the page's positioningData.",
        "org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~3/b1_mount_internal_prop_typecheck_measure.txt (committed with this row): with `internal={internal}` on the mount, `tsc -b --noEmit` EXIT=2, `src/pages/Positioning/Positioning.tsx(670,11): error TS2322 ... Property 'internal' does not exist on type 'IntrinsicAttributes & { customBlend: CustomBlendState; mode?: ...; bookStatus?: ... }'`.",
        "org/missions/D4/POSN/POSN_AGGFIX/task-orders/POSN_AGGFIX.TO-B1-1.portal-fetch-viewer-gate-and-remembered-choice.md @ed1db8f1db <paths>: portal-proxy.ts, Positioning.tsx, bookSet.ts, README.md, and the act says 'HoldingsTab.tsx is NOT yours in this order'; POSN_AGGFIX.TO-B2-1.holdings-tab-restores-the-aggregate-book.md @ed1db8f1db <paths>: HoldingsTab.tsx and no Positioning.tsx, while its 'Your inputs from TO-B1-1' lists '`internal` handed to the `HoldingsTab` mount'.",
        "portal 63edeeeb51 on wk-aggfix-1-3-portal (LOCAL): landed the fetch, the internal-and-Models query, mergeOpalAggregate feeding the page's dataByMode.models (Positioning.tsx :369-384, :471 at that commit), and the book-set helpers; the HoldingsTab mount carries no internal prop."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "AF1-s-13 (decomposition @605c03f81f, TO-B1-1 verbatim): `internal` (:267) is passed to the `HoldingsTab` mount (:642); on status OK with holdings its current_holdings.AGG is merged into the Positioning data object the tab reads. TO-B2-1 lists the mount hand-over among its inputs from TO-B1-1.",
    "world_is": "Neither limb can land inside TO-B1-1's grant with B1-AC7 at exit 0. The tab's prop type rejects `internal`, and the tab's Models data is its own fetch, so a page-side merge reaches PositioningSummary (which reads current_holdings only where SUBCATEGORY_SOURCE is current_holdings: etfs and satellites) and not the Holdings tab. TO-B1-1 landed the page-side fetch, gate and merge and the pure helpers, and did NOT pass internal to the mount. The hand-over -- an `internal` prop plus either a models-data prop or the tab applying mergeOpalAggregate to its own fetch -- needs a HoldingsTab.tsx edit and a Positioning.tsx edit in one typechecking commit, and no single order's <paths> holds both files.",
    "notes": "Form only; significance not judged. No B1 criterion grades the mount, so B1-AC1..AC8 are recorded as run. For 2.0.0_SA_COO~Z: TO-B2-1's grant or a re-cut."
  },
  {
    "id": "POSN_AGGFIX-Z-W3-S2",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~3",
    "surfaced_at": "2026-09-15T19:57:36Z",
    "one_line": "TO-B1-1 has the render harness read AuthContext.tsx 'for the claim shape of an advisor and a client', but AuthContext has NO client class: Claims carries only firmId, userType, advisorId, firmRole, advisorRole, and the one non-Opal shape it mints is devBypass's partner advisor; the client claim set was therefore CONSTRUCTED (a partner firmId with every other claim at its parseClaims deny-floor) and recorded.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/contexts/AuthContext.context.ts @edf85ce503 :31-43: interface Claims { firmId, userType: 'Dev' | null, advisorId, firmRole: 'admin' | 'user' | null, advisorRole } -- no client member.",
        "portal src/contexts/AuthContext.tsx @edf85ce503 :110-142 parseClaims (userType kept only when exactly 'Dev'; firmRole only admin|user; advisorRole only the four RCU roles, else null); :686-697 devBypass(advisorRole) mints the partner advisor (firmId VITE_DEV_FIRM_ID, userType null, advisorId 'dev-advisor-id', firmRole 'user'); a case-insensitive read of 'client' over the same file: 10 hits, every one queryClient / QueryClient / api-client, 0 naming a user class.",
        "infra/aws/lambda-edge/shared-advisor-router/index.mjs @ed1db8f1db :159-169: the tier notion (x-user-tier, x-user-type request headers) lives at the edge, not in the portal's claims.",
        "org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~3/b_five_books_dom.mjs VIEWERS (committed with this row): advisor {firmId 49financial, userType null, advisorId b-harness-advisor, firmRole user, advisorRole architect}; client {firmId 49financial, userType null, advisorId null, firmRole null, advisorRole null}; both printed on every run's CLAIMS lines."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-B1-1 fixtures paragraph: 'vary the SESSION's user claims per viewer class, reading AuthContext.tsx for the claim shape of an advisor and a client'; decomposition @605c03f81f :311-312: the portal worker builds the advisor and client claim sets from AuthContext.tsx and records them.",
    "world_is": "The portal claims cannot tell a client from any other non-Opal, non-advisor partner user; the page predicate (firmId opal-capital OR userType Dev) treats both as non-internal, so for this page the two classes render identically. Whether a real client session carries a claim the portal does not model (an edge-derived tier) is not readable from the portal."
  }
]
```
