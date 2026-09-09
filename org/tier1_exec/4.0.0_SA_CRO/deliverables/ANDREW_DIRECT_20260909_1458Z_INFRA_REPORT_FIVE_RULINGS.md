# ANDREW-DIRECT 2026-09-09 ~14:5xZ -- five rulings on the Infrastructure Report review

**Received by:** `4.0.0_SA_CRO~Z` (site-Z terminal, Andrew present)
**Channel:** direct at the `4.0.0_SA_CRO~Z` terminal, in response to this seat's `/open-calls` segment
**Recorded:** 2026-09-09 14:58Z, same turn as receipt, per `org/XXX.md` Andrew-direct law
**Scope note:** this seat does NOT adjudicate scope. Recorded verbatim; surfaced, not interpreted.

---

## THE RULINGS, VERBATIM AND ENTIRE

> 1.) The prioritization should be relayed to CTO~Z, as I've already instructed them that we are
> going to need to create an addendum to the PRD for NFRA_OPSEC202609 to account for the incoming
> work on the Infrastructure Report. 2.) Agreed, CloudFront. 3.) Rec approved, ride the infra
> report. 4.) Ratify on s-23 output. 5.) We've excised the need for this already via not displaying
> an "AGG" view, which is what required aum-metrics. Neither /attribution nor /factor-tilts should
> have any reliance on /json/portfolios/.

---

## WHAT EACH RULING ANSWERS

The five cards were issued by `4.0.0_SA_CRO~Z` at 2026-09-09 14:53Z.

| # | Call | Ruling |
|---|---|---|
| 1 | Relay the OPSEC prioritization now, or hold for the brief? | **RELAY -- to `1.0.0_SA_CTO~Z`**, not the COO. Andrew has already instructed that seat to author a `NFRA_OPSEC202609` PRD addendum for the incoming Infrastructure Report work. |
| 2 | Website edge: CloudFront or Cloudflare? (FWD-13 / `TO-OP-S-13`) | **CloudFront.** Settles the card the OPSEC PRD carried to Andrew; it reverses the 2026-07-13 "NO CloudFront" spec line. |
| 3 | C-6 digest: ride the infra report, or a separate email? | **Ride the infra report.** The `reports/daily/` FILE remains the durable record. No second security email is minted. |
| 4 | C-3 thresholds: set now, or ratify on `TO-OP-S-23`? | **Ratify on S-23 output.** |
| 5 | Does `/attribution` keep sourcing the legacy `json/portfolios/aum-metrics.json`? | **No -- and neither does `/factor-tilts`.** The AGG view that required `aum-metrics` has been excised. Neither page should have ANY reliance on `json/portfolios/`. |

---

## THE CONSEQUENCE OF RULING 5 -- a stale catalog, surfaced not chased

Ruling 5 removes the last consumer this seat had measured on the legacy tree.

**Measured before the ruling** (`4.0.0_SA_CRO~Z`, 2026-09-09, `comp-find --band CONFIG`):

- `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml:650` -- declares
  `json/portfolios/aum-metrics.json (legacy, last written 2026-07-23, vintage field 'period')`
- `DATA_CATALOG.yaml:1015` -- describes that artifact as still supplying
  `AUM totals from the LEGACY json/portfolios/ tree` as tilt CONTEXT on page `/attribution`
- `org/tier0_utility/0.0.3_BG_BBGTerminal/refs/census/ARTIFACT_CENSUS_POD2.yaml:24` -- lists it
  `BORROWED cross-vertical (rendered here, owned elsewhere)` against the same page

**Andrew's ruling states that consumption no longer exists.** Therefore `DATA_CATALOG.yaml:650/1015`
and `ARTIFACT_CENSUS_POD2.yaml:24/149/195/231` describe a consumption that has been excised --
**the catalog and the census are STALE against the live front end.**

This is the SAME CLASS as the finding that produced the review: **a descriptive record outliving the
change it describes.** The freshness config outlived the MDPF_SCOPED migration; the data catalog
outlived the AGG-view excision. Neither has a mechanism that detects its own staleness.

**Disposition: SURFACED, NOT CHASED.** No remediation is authorized by this record. The correction
belongs to the owners of those two files. Routed as an item, not as a gate.

---

## STATE OF `json/portfolios/` AFTER RULING 5

| Fact | Source | Class |
|---|---|---|
| `account-distribution.json` superseded by `json/mdpf/{firm}/account-distribution.json` | `graph_contracts.yaml:278` | measured |
| `aum-metrics.json` had one live reader (`/attribution`) | `DATA_CATALOG.yaml:1015` | **superseded by ruling 5** |
| EC2 `smartx-exporter` dual-writer DORMANT since 2026-06-01 | `graph_contracts.yaml:201` | measured |
| Tree marked `RETIRE-WHOLE-CANDIDATE` | `MDPF_GLOBAL_T5A/kill-list.yaml:36,38` | measured |
| Last write 2026-07-23 | `DATA_CATALOG.yaml:650`; agrees with the report's 1144.1h | measured |

**Consequence for the Infrastructure Report:** the SmartX `RED` is a **false alarm on a fully
retired tree with zero live consumers**, and the monitor is simultaneously **BLIND to
`json/mdpf/{firm}/*`**, which is what actually serves Portfolio Analytics. One defect, two
directions; the blind direction is the dangerous one.

**Retirement itself remains gated** -- moving served output requires never-widen sign-off
(`CTO`+`COO`) per CLAUDE.md. Ruling 5 removes the CONSUMER objection; it is not a delete order and
is not recorded as one.

---

## ACTS TAKEN BY `4.0.0_SA_CRO~Z` ON THIS RECORD

1. This record committed (durable half of the Andrew-direct law).
2. Ruling 1 executed: OPSEC dependency set + prioritization relayed to `1.0.0_SA_CTO~Z` as the
   RAVC 4 answer to its msg 20508 ASK, carrying ruling 2 (CloudFront) so the addendum can name the
   Website edge without a second round trip.
3. Broadcast half: this record notified to `2.0.0_SA_COO~Z` and `0.0.0_AB_MSTR~Z`.

**Not done, and deliberately:** no task order is cut, no sequencing order is issued to any executing
seat, and no retirement is initiated. `4.0.0_SA_CRO` does not dispatch.
