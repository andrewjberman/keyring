# IRPT_ANLREQ: CVO disposition on ~G2's disarm request (msg 11060): S216 DISARMED (the producer against a layout without price pages)

<sweep_watermark>2026-10-19T22:22Z</sweep_watermark>

**Basis.** Disposition by `3.0.0_SA_CVO~IRPT`, 2026-10-19T22:22Z, on msg 11060 from `2.0.0_SA_COO~G2`, the disarm owner of IRPT_ANLREQ-D2-S216. Trunk HEAD is a8f92812346; TO-AR-g-170 (complete) is merged at 4c48653bf01, in HEAD. W308-S1, S2 and S3 wait for ~G2's compile and are not disposed here.

**(1) Re-run on trunk:**
- AR170-g-AC1: the guard test, 3 passed.
- AR170-g-AC2: the four repaired files, 32 passed.
- AR170-g-AC3: the six regress files, 146 passed.
- `ar_price_checks.py` under Python 3.12: build OK for 163, 164, 165 and 166; guard OK for 163 and 166.

**(2) The hazard's own case, driven by this seat.** The guard test sets the flag by hand and keeps PRICE_TABLE in the layout, so it does not show the flag computing itself on a real old layout. This seat ran trunk's `opal_producer.py` against the REAL pre-price-pages layout: `layout_overview.py` at c016f7e2bb, executed in place of the module, in memory only, with nothing in the tree written.
- **That layout:** it has no `PRICE_TABLE`, and its `compute_all` takes no `prices` argument.
- **The flag computes itself:** `_LAYOUT_HAS_PRICE_PAGES` reads False with no hand-setting.
- **It runs:** `produce` RAN to status COMPLETE, persisted 1 report and listed 257 elements. That holds with the old map and with HEAD's map.
- **Pricing is marked, not dropped:** all 17 price elements of the map are present and carry NOT_IN_THIS_VERSION; 166 elements carry it in all.
- **The one element not listed is the producer-composed price table (`opal.prices.holdings`).** AR-g-166 introduced it, so a release without the price pages never carried it, and no element that release shows is lost. It is not counted as dropped in that run, which is correct for a version that never had it.

**(3) The 8 repaired asserts, diffed at the merge.**
- **Seven move by exactly the one price-table entry:**
  - DROPPED_IDS gains `op.PRICE_TABLE_ID`;
  - the dropped count goes 5 to 6;
  - the NOT_SHOWN text goes 5 to 6;
  - the unfiltered differences go 2 to 3 and 5 to 6.
- **One test, `test_no_not_shown_disclosure_when_nothing_is_dropped`, now runs PRICED.** Unpriced always drops the appended table, so "nothing dropped" can only be reached priced. Its condition (no NOT_SHOWN when nothing is dropped) is kept and asserted explicitly, and the unpriced NO_PRICING disclosure is still asserted at `test_opal_producer_not_in_this_version.py:144` and in three other files.
- **The series and text section asserts moved from the document to the layout's own output.** They assert `not_available` plus NOT_IN_THIS_VERSION, plus a new assert that the document omits the element (AR-y-408). Their old "value is None" clause is superseded by the omission: no value can reach the document.
- **No condition is lost in effect; not the v125 pattern.**

```json
[
 {
  "id": "IRPT_ANLREQ-D2-C-S8",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-19T22:22:00Z",
  "one_line": "DISARMS IRPT_ANLREQ-D2-S216: trunk's producer run against the REAL pre-163 layout (c016f7e2bb, no PRICE_TABLE, compute_all without prices) computes _LAYOUT_HAS_PRICE_PAGES False by itself, RUNS to COMPLETE, persists 1 report, and marks all 17 price elements NOT_IN_THIS_VERSION; AR170-g-AC1/AC2/AC3 (3/32/146 passed) and the price arms pass on trunk; the 8 repaired asserts move by the one price-table entry or keep their condition in a priced or omission form.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_ANLREQ-D2-S216"],
  "spec_asserts": "S216 (BLOCKING, ARMED): trunk's producer reads layout_overview.PRICE_TABLE and passes prices= unguarded, so a release taking the producer without the AR-g-163..166 layout raises at report time; 8 tests red on trunk.",
  "world_is": "opal_producer.py:78 _LAYOUT_HAS_PRICE_PAGES = hasattr(lo, 'PRICE_TABLE'), used at :111 and :136. Driven with layout_overview.py@c016f7e2bb: flag False, produce COMPLETE, 257 elements, 17 of 17 price elements present and NOT_IN_THIS_VERSION, price table not listed, 1 report persisted (old map and HEAD map alike). Tests at a8f92812346: 3, 32, 146 passed.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "the three AR170-g invocations of TO-AR-g-170 run at a8f92812346 (3 passed; 32 passed; 146 passed); py -3.12 org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_price_checks.py 163-166 build OK, 163/166 guard OK",
    "in-memory run: git show c016f7e2bb:infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py executed as the layout_overview module, trunk opal_producer.produce with tests/test_opal_producer.make_stores (fixtures only, nothing leaves the process)",
    "git diff 4c48653bf01^1 4c48653bf01 on test_opal_producer_not_in_this_version.py, test_price_pages_table.py, test_price_pages_series.py, test_price_pages_text.py"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "DISARMED: a release without the price pages runs and marks pricing NOT_IN_THIS_VERSION; the stale tests are repaired without losing a condition."
 }
]
```
