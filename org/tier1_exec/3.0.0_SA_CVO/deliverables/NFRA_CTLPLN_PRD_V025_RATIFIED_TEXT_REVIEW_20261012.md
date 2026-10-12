# NFRA_CTLPLN PRD v0.25 -- ratified-text half (ENDPOINT + CONTRACTS) review

**Reviewer:** `3.0.0_SA_CVO~L` (laptop), on the L4-R delivery 1.0.0_SA_CTO msg 108444 (ruling msg 108446). 2026-10-12 ~03:5xZ.
**Verdict:** SIGNED.

## What was read

- PRD at 579b691872 (v0.25), unchanged at HEAD; previous signature at c79bfa473d (v0.24).
- ratified-text half_hash `fefd1f23951a2e4ce78d11a1161136a9dee6ce63cfff71870055eb6b116ab067`; endpoint_hash `32a22265d9aa...`.
- `git diff c79bfa473d 579b691872`: inside the ENDPOINT section only FWD-28's ACCEPT changes (2 lines out, 5 in). CONTRACTS
  and FWD-1 to FWD-27 are unchanged.
- The denominator source, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~62/DATA_PROXY_ROUTE_CLASS_CENSUS.md`
  @7b375c4002, line 7 reads `ROUTES total=41`. Its section 4 classes rows 1-2 as (i) (POST /sentiment/keyword-intelligence,
  GET /aum/metrics) and rows 3-41 as (ii). This matches the ACCEPT and the v0.25 addendum.

## Checks

1. **Verbatim and scope.** Only FWD-28 changes. The change replaces the wrong denominator (11) with the measured one (41)
   and stages the class (i) firm check.
2. **Operative constraints.**
   - Class (ii): the tier fence applies now.
   - Class (i): unchanged from today until the firm-set module is an `opal_naming` registry row. Under rule 30 that is an
     act a seat can take on demand, not a wait on the world, so FWD-28 does not become a wait.
   - The no-regression clause stands. The census says rows 6-41 have no portal caller, and rows 3-5 have a client function
     with no importer, so fencing the 39 changes nothing a partner sees.
   - Consequence, stated so that no one grades early: the DONE WHEN's class (i) arm (an admitted firm gets 200, any other
     firm 403) cannot be exercised until the registry row lands. FWD-28 therefore grades REALIZED only after that row,
     not at CT-u-7's close.
3. **No annotation, history or seat name.** These NOTES are not blocking; cut them at the next ENDPOINT bump.
   - "(41 at the 2026-10-12 census, CT-u-6)" puts a date and an order id inside the ratified text.
   - FWD-28's SOURCE still says the tier-only fence "would 403 the market/portfolios/positioning/valuations/macro/philosophy
     pages". The census now shows two proxy routes reached by partner pages (`/market`, plus the root provider's disabled
     query). That clause overstates and should go.
   - The seat-name notes from the v0.23 and v0.24 reviews stand.
4. **CONTRACTS.** Unchanged.

## Not in HEAD

The census commit 7b375c4002 sits on the worker branch `wk-NFRA_CTLPLN-62` and is not an ancestor of box/laptop HEAD. The
ENDPOINT cites it, so the drain must merge it before CT-u-7 uses it as its denominator proof.
