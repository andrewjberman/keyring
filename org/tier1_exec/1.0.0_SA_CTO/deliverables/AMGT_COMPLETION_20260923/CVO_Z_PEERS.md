# MANDATE -- `3.0.0_SA_CVO~Z` -- grade the AMGT **Peers** tab (B04 / P1)

**Authority:** Andrew-direct 2026-09-24 ~02:2xZ, VERBATIM: *"granted, spawn 2.0.0_SA_COO~Z. Then yes, go."*
**Contract:** `CONTRACT.md` (this folder). **Trace:** `PEERS_END_TO_END_GAP_BRIEF_20260923.md` + `.evidence.json`.
**Implementing seat:** `2.0.0_SA_COO~Z` (already LIVE; not spawned).

## WHAT YOU GRADE

Each pinned candidate: **PASS / FAIL / NOT_EVALUATED**, with evidence and limits, in **your own evidence
folder**. ⛔ **Offline success is never a deployed end-to-end PASS.** ⛔ **You never fix what you grade.**

**Grade on a live trace, the deployed bytes, or a test run.** The 2026-09-02 ruling stands: **no
comp-tool-grounded adjudication** until a Codex rail exists.

## ACCEPTANCE -- the brief's matrix, unchanged. One RECONCILED TRACE PER CASE, not a fixture pass

A case reconciles when ONE request is followed through: the user's selection -> the route's **identity block**
-> the **`peer_read` record** -> the **pool object key** -> the **served member rows** -> the **rendered column
states and counts**.

**SELECTIONS (5):**

| key | expected |
|---|---|
| `BA_US_Equity` | resolved, basis **derived**, **12** members, USD |
| `992_HK_Equity` | resolved, derived, 12, **FX caveat SHOWN** (subject cap HKD, database cap USD) |
| `ASML_US_Equity` | **today** UNRESOLVED at the route *with an object in the pool*; **after step 2** resolved, basis **absent**, its "no classification" reason shown |
| `CAT_US_Equity` | resolved, **no object** today; **after step 4** an object exists |
| `NOSUCHKEY_ZZ_Equity` | UNRESOLVED, raw string shown -- **the negative control** |

**x CONSUMERS (2): the Peers tab AND the Posture comparable read.**
⛔ **Hop 8 is why: `PostureTab.tsx:339-347` calls `usePeerSet` for subject AND comparable. A case graded on
Peers alone is HALF-GRADED, and a PASS on that basis is the defect this line exists to stop.**

**x FAILURE CASES (3):** expired session (edge 401 -> refresh -> retry) · **`peer_read.status READ_FAILED`
MUST NOT render as ABSENT** (a permission or parse failure is not an empty set) · a pool key with a literal
`/` (`BP/_LN_Equity` shape, 10 objects).

## THE FOUR PROOF OBLIGATIONS TO HOLD THE SEAT TO

1. **Live thread:** served stack, PROD authorizer, deployed digest `DEQQiCH+...`; identity "BA US", derived
   badge, 12 comparables, "5 present / 12 absent of 17". **A `/market` redirect FAILS the case.**
2. **One key space:** `crosswalk.resolve()` over the **191** newest pool keys prints **191 MEASURED** *or* a
   printed refusal list with reasons; then deployed `/peers` for `AAPL_US_Equity` -> `basis: derived`,
   `peer_read.status SERVED`. ⚠ **111 stranded sets is the number this step is worth** -- if the count moves,
   ask why before crediting.
3. **Present columns:** served Boeing members carry all **five** present codes; rendered table reports **"5
   present / 12 absent of 17 declared; 5 column(s) carry a per-member value"**, summary rows at **n=12**.
   ⚠ **`P/E 2026` must render from `factors.ey_ntm` as `1 / ey_ntm` under the R-1 `display_label`, NTM grain**
   -- rk-14 forbids a fiscal-year label over an NTM figure. A fiscal label there is a FAIL even if a number shows.
4. **Batch owner + trigger:** a new partition whose key set **equals** the crosswalk's MEASURED set, **both
   denominators printed**.

## WHAT THE CTO HAS ALREADY RULED -- grade against it, do not re-litigate

**The ranker keeps its fall-through; the crosswalk widens to meet it.** Converge the route UP to the producer.
**REFUSED:** the route accepting a landed peers object's own identity block as a third identity surface.
If you believe the ruling is wrong, **execute it and surface the disagreement in one line** -- escalation runs
upward, never sideways.

## LIMITS YOU SHOULD EXPECT TO CARRY (the brief states them; do not silently drop them)

- The brief did **not** exercise a signed-in walkthrough, nor the **edge header injection** (cited from this
  seat's C4 measurement, not re-derived), nor the CloudFront behavior on the **live** distribution.
- `AMGT_MODEL_BLOCK_ROOT` / `AMGT_POOL_ROOT` are **unset** on the deployed function, so the route's second
  identity surface cannot fire there and every pool read goes to `s3://opal-data-harvest`.
- The universe vintage is **2026-08-06**. A stale-universe result is not a Peers defect.
- **One shape hazard, not a defect today:** "latest" is the LAST `.json` key in **string** order; a future
  date-only partition would sort AFTER a same-day timed one.

**Write surface: your evidence folder only.** Send the verdict to `2.0.0_SA_COO~Z` and `1.0.0_SA_CTO~Z` in
**one review-handoff message**. ⚠ Working branch is **`CLOUD`** (ONE TRUNK, `f534c14693`).
