# THE BI PLANE IS LOCATED -- and qt6 ties it TO THE CENT (Andrew-supplied HAR)

**Seat:** `4.0.0_SA_CRO~A` | **2026-08-20 ~0200Z**
**Source:** `C:\Users\AndrewBerman\Downloads\BI_scrape_BD_dashboard.har` -- **Andrew recorded the
browser session himself and handed it over.** 15,461,452 B, 230 entries.
**Egress: ZERO.** A local file read. The browser-observation instrument question is **MOOT** -- the
sovereign performed the observation; nothing was authorized to me and nothing was needed.

## 1. THE PLANE: `bd3.bdreporting.com/advisor/api/v1/`

**It is a different API on the SAME HOST as datamining.** Not a subdomain, not a separate app.

> **That is why the entire night's sweep could not find it.** Twelve `/datamining/*` paths, six
> subdomains -- all structurally incapable of reaching a sibling path prefix on a host I had already
> treated as covered. **The wildcard catch-all made subdomain probing look like a search while it
> was answering nothing.**

**`ClientView` is likewise a PATH** (`/ClientView/api/menu`), which is exactly why
`clientview.bdreporting.com` timed out -- I was probing a host that was never supposed to exist.

## 2. THE CALL THAT SERVES THE ADVISOR DASHBOARD

```
POST bd3.bdreporting.com/advisor/api/v1/Dashboard/data          (791,931 B response)
{ "dateRange": {"type":"YearToDate","startDate":"08/18/2026","endDate":"08/18/2026"},
  "supervisedFilterType": 1, "billableFilterType": 1,
  "filterTypeId": 1140, "levelType": "PortfolioGroup",
  "frequency": 5, "includeDirectAssign": false, "values": [], "isAllSelected": false }
```

`filterTypeId: 1140` is **the same dimension id as the qt6 Portfolio Group dim** -- the two planes
share one dimension model. Response: `firmAggregateResult` plus
**`levelTypeAggregateResults` = 216 entries.**

## 3. CROSS-PLANE TIE-OUT: EXACT TO THE CENT

| instrument | Travis Penfield EMV | groups |
|---|---|---|
| BI dashboard `/advisor/api/v1/Dashboard/data` (id 272271) | **456,773,323.40** | **216** |
| my qt6 datamining probe (template 517678 / run 517753) | **456,773,323.40** | **216** |

**Two independent API planes, different auth path, different request shape, different response
schema -- identical to the cent, and identical group count.**

This **PROVES** what the predecessor scan could only assert: that the qt6 group-grain read is the
number the ADVISOR SEES on their BD dashboard. It is no longer an interpretation of a probe; it is
the same figure the dashboard renders. **DS~B's L1 authority leg is now anchored to the
advisor-facing surface itself.**

## 4. WHAT THE BI PLANE CARRIES THAT qt6 DOES NOT

| field | Travis | why it matters |
|---|---|---|
| `supervisedBmv` | 365,944,087.94 | **the supervision split, absent from qt6 entirely** |
| `unsupervisedBmv` | 20,607,285.89 | 5.3 pct of BMV sits unsupervised |
| `relationshipCount` | 106 | relationship grain at group level |
| request `supervisedFilterType` / `billableFilterType` | 1 / 1 | supervised + billable are **filter axes** |
| request `includeDirectAssign` | false | **direct assignment is a first-class concept here** |

The supervision split lands directly on the ADVI_49F PARITY supervision-sleeve GRAIN convention
(ADDENDUM A6). qt6 cannot express it, so any parity work needing supervised-vs-unsupervised has to
come from this plane.

## 5. THE GROUP-MEMBERSHIP PRIMITIVES (where the dim-436 question actually lives now)

```
POST /advisor/api/v1/advisorview/multiPortfolioGroups
     {"searchString":"travis","selectedIds":[],"take":20}
     {"searchString":"","selectedIds":[272271],"take":20}
GET  /advisor/api/v1/advisorview/groupingLevel?groupExternalId=z08362691
GET  /advisor/api/v1/Dashboard/groupingDetailSearch
     -> dimension objects, SAME schema as the datamining catalog
        (id / name / isSelected / mappedColumn / ordinal / dataType / ...)
```

Groups carry **BOTH** an internal id (`272271`) and an **external z-id** (`z08362691`) -- the same
z-key family DS~B's Layer 1 leans on for relationships. **This is the plane to ask the
account-to-group primacy question of**, now that dim 436 is dead (empty, and portfolio-level).

**NOT YET PROVEN to yield account-grain primacy** -- response bodies for these three were not
captured in the HAR. Stated as the right plane, not as an answered question.

## 6. OTHER SURFACES CONFIRMED REAL

`firm-api.bdreporting.com/query/firmDetailSearch` (POST) - `alerts.bdreporting.com/v1/alerts/negotiate`
- `broadcast-api.bdreporting.com/V2/GetActiveBroadcastsByUser` - auth via `login.bdreporting.com`
OIDC -> `bd3/session/signin-oidc` -> `bd3/auth/token`.

## 7. THE METHOD LESSON

Three invented-input controls correctly killed three false leads tonight, and **the REST pursuit's
honest verdict was still "exhausted, not found."** It was exhausted **because the target was never on
the surface being swept** -- and no amount of discipline inside a wrong search space finds a thing
outside it. **A correctly-bounded negative result is not the same as coverage.** One recorded browser
session answered in minutes what a rigorous blind sweep could not answer at all.

**NO CREDENTIAL, TOKEN, COOKIE OR CLIENT ROW FROM THE HAR IS REPRODUCED HERE OR COMMITTED ANYWHERE.**
The file stays in Andrew's Downloads; this record carries endpoint structure, schema, and the one
figure already published in our own records.
