# ANDREW-DIRECT 2026-09-10 ~02:5xZ -- `/open-calls` at `1.0.0_SA_CTO~Z`, ALL SIX RECS APPROVED

**Terminal:** `1.0.0_SA_CTO~Z`. **Recorded by:** `1.0.0_SA_CTO~Z`.

## VERBATIM AND ENTIRE

> go with your recs on all six

⛔ **A ONE-LINE APPROVAL OF SIX CARDS IS SIX RULINGS, AND EACH ONE'S SCOPE IS ITS CARD'S REC AND
NOTHING WIDER.** Each is written out below at the exact scope of the REC he approved, because "all
six" is only as precise as the recs were, and a REC read wider than written is the widening this seat
is forbidden to do.

---

## 1. CALLER MIGRATION -> **THROUGH THE OWNING LANES**

**REC APPROVED:** *"Through their owning lanes. PRD s.3 already lists them under 'Relies on, does not
own', so name the lanes for `bd-49f-auto-login` / `bd-cot-auto-login` (OpalETL/PartnerETL) and
`globgrph derive` (CloudComp) and let `2.0.0_SA_COO~Z` raise the ask through them. The 2 in-lane
liveness Lambdas need no word and can cut now."*

**WHAT IT AUTHORISES:** `2.0.0_SA_COO~Z` raises the migration ask to the three callers' owning lanes
rather than acting on them directly, and cuts the two in-lane liveness Lambdas now.
⛔ **WHAT IT DOES NOT AUTHORISE:** it does NOT move the three callers into `NFRA_OPSEC202609`'s
territory, and it does NOT let that lane change another lane's code. PRD s.3's boundary stands.
**CONSEQUENCE:** `TO-OP-S-15-19` stays cancelled until a non-probe, firm-attributed sign-in window
exists -- the migration is what produces it, and it is now unblocked to start.

## 2. `NFRA_IAMROLES202609` -> **SEAT A COO LANE NOW**

**REC APPROVED:** *"Seat a new lane now, don't wait for OPSEC."*
**ROUTED, NOT EXECUTED:** seating is not this seat's act. Relayed to `0.0.0_AB_MSTR~Z`.
**WHY NOW:** OPSEC's close is gated on call 1, which is outside its control; waiting couples a ready
project to a blocked one. The PRD is at v0.2 with its manifest and adversary grid, endpoint ratified.

## 3. INTEGRATE-LEG PAUSE -> **LIFTED FOR ONE `CLOUD -> SITEZ` LEG**

**REC APPROVED:** *"Yes, one leg."*
**ROUTED, NOT EXECUTED:** the leg is `0.0.0_AB_MSTR~Z`'s act. Relayed.
⛔ **SCOPE IS ONE LEG, ONE DIRECTION.** This is not a general lift of the pause and not a push
authorization. **The reason is v3.9:** an L7 worker-death clause that BINDS BY READING, is unreadable
on this fabric (462 lines here vs 480 on the laptop), and governs workers `2.0.0_SA_COO~ZZ` is running
right now. **A clause that binds by reading and cannot be read is not binding.**

## 4. `FWD-4`'s ATTRIBUTION AXIS -> **FOUR MEMBERS**

**REC APPROVED:** *"Four: Dashboard, Website, Gateway, Graph."*
**EXECUTED at `NFRA_REPORT` PRD v0.7** -- section 6 ruling closed, `S13`'s bound amended, version bumped.
**WHY FOUR:** `opal-gateway` (EC2, MCP server) and `opal-globgrph` (ECS, 3 of 3 services) are both
live, both always-on, and fail differently. Folding either into `Dashboard` makes `FWD-4`'s own bar --
*one problem belongs to one part* -- false by construction.
⚠ **`UNGROUPED` IS NOT RETIRED.** It now means *a live surface outside all four*, a smaller set than
before, and it must still RENDER rather than vanish. **The ruling names the members; it does not
promise the four are exhaustive of everything this estate will ever run.**

## 5. `trade-submission-api` -> **DECLARE THE GATEWAY IN TERRAFORM; HOLD MONITORING AND CONSOLIDATION**

**REC APPROVED:** *"Declare the gateway first; hold monitoring and consolidation."*
⛔ **NO ALARM, MONITOR OR NOTIFICATION IS AUTHORISED BY THIS.** The standing moratorium is untouched
and the REC explicitly held monitoring. Anyone reading this ruling as permission to instrument that
path is reading it wider than it was written.
⚠ **NO LANE OWNS THIS TODAY, AND THAT IS THE ITEM THIS RULING EXPOSES.** `NFRA_REPORT`'s `FWD-11`
FOUND it; `NFRA_IAMROLES202609` covers declared-vs-live for ROLES, not gateways. **The ruling is
recorded and the work needs an owning lane** -- surfaced rather than parked in a seat that cannot
execute it.
**WHAT IS STILL UNMEASURED and bears on consolidation:** no request logs were read, so nothing shows
whether the undeclared door takes traffic.

## 6. RESOURCE-LEVEL COST EXPLORER -> **APPROVED, AND IT IS CONSOLE-ONLY**

**REC APPROVED:** *"Enable it."*
⛔ **THIS SEAT CANNOT EXECUTE IT, AND THE CHECK THAT ESTABLISHED THAT WAS ITSELF CORRECTED.** A first
probe reported "no write verbs in `aws ce`" -- **that was a BROKEN PATTERN**, caught by a positive
control: the same census shape returns **23 `get-`, 4 `update-`, 3 `create-` verbs**. So the API is
not read-only. **But none of the write verbs enables resource-level data** -- they cover anomaly
monitors, cost categories, and `update-cost-allocation-tags-status`. **Resource-level / hourly
granularity is a BILLING CONSOLE preference with no CLI verb**, so it needs Andrew in the console.
⛔ **AND `create-anomaly-monitor` IS NOT TAKEN AS AUTHORISED BY THIS.** It exists, it is adjacent, and
it is a MONITOR -- the standing moratorium forbids it without his explicit word, which this is not.
⚠ **ADJACENT AND NOT DONE:** `update-cost-allocation-tags-status` IS CLI-reachable and bears on the
same defect (tags null on 9 of 27 rows, with a casing drift). **It is not what he approved**, so it is
surfaced rather than executed.

---

## WHAT REACHES `FWD-8`

Calls 6's console step is the precondition for **BOX-GRAIN** cost anomaly. Until it lands, `FWD-8`'s
box limb stays out of scope exactly as the round-2 adjudication ruled; **SEGMENT grain is live and
unaffected.**
