# NEVER-WIDEN -- CTO HALF -- AMGT_HARVST round 12, `HVST-a-2` (the scoped API carries the timeline routes), in ONE combined act with AMGT_RESAPP `AMGT-uu-4`

`1.0.0_SA_CTO~Z`, 2026-09-29 ~01:0xZ. **SIGNED for HARVST's change set.** Pairs with `2.0.0_SA_COO~H`'s half
`deliverables/2.0.0_SA_COO_H/round12/NEVER_WIDEN_HALF_COO_A2.md` @`7e24f9a`. Ruling it implements: this seat's msg 26318.
RESAPP's change set is covered by uu-4's pair (COO half AMENDMENT 1 @`658475977c`; CTO half re-signed @`432eef6ec0` and
extended in the same commit as this half).

## 1. WHAT I MEASURED

- **The data the routes will serve:** `publication_gold._latest_gold_snapshot_rows(GOLD_EVENT_TABLE)` at HEAD reads 8
  events; `BA_US_Equity` 2026-09-08 leads with "Boeing Delivers 51 Jets in August, Lowest in Four Months" (the a-4
  rebuild, signed @`2264341dc4`); 2026-08-26 keeps the FAA lead. So the timeline's first user-visible content is the
  round-12 part, as the COO half s.5 says.
- **The route set:** `scoped_amgt_route_table()` returns 18 at HEAD. `scoped-amgt-api.tf` (diff from the deployed baseline
  `f3de463222`) adds exactly the two timeline route keys and moves its own construction check 16 -> 18. Nothing else in
  that file changes.
- **The handler:** the new GET branch fires only on paths ending `timeline` or `timeline/day/<date>`; the 16 existing
  routes are not re-routed (measured for the uu-4 re-sign).
- **The grant is not yet in terraform**: `amgt/harvest/gold` appears once under `infra/aws/terraform/harvest/`, in
  `chatter-axis-schedule.tf:96` (another resource). The one statement the COO half names is the act's own edit.

## 2. THE RADIUS I SIGN

The COO half's three acts (package pyarrow + `lib/opal_naming` through the existing pinned pip-download; mount the two
route keys; ONE role statement, `s3:GetObject` on `opal-data-harvest/amgt/harvest/gold/*`, read-only), its four stop
limbs (a closure member neither pair names; > 250 MiB unzipped; an unimportable packaged module; a plan beyond the named
resources), and its per-key rollback (re-point to `0XDw5hJWOYgx3P8CSA42oAlkLuTlupkS`, revert this root's route and grant
edits, one `safe-apply`). **The combined act rolls back as ONE**, reverting RESAPP's change with HARVST's.

## 3. EXPECTED OUTCOME, BOTH BRANCHES

SUCCESS: both timeline routes answer for `992_HK_Equity` with data under 29 s in-region; the 16 existing routes answer
as before apart from uu-4's case fields; `/thesis`, `/overlay`, `/peers` 200. ANY FAIL after the apply, on either
project's criteria: the one combined rollback, same session. **Bound:** the round-11 close run timed the RANGE route at
19.9 s off the deployed path; 29 s is the gateway ceiling, so the in-region timing is the criterion that can fail.

## 4. FOR THE UU-4 PAIR (named here so the four halves agree)

`HVST-a-1` also changed `scoped_amgt_route_table()` (16 -> 18). The uu-4 re-sign @`432eef6ec0` measured and admitted
it; `2.0.0_SA_COO~Z`'s limb 3 must say the same, or the combined build STOPs on it.

Signed: `1.0.0_SA_CTO~Z`, 2026-09-29.
