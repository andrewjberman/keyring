# AMGT_RESAPP round 36: CVO adjudication -- both stacked blockers CLOSED at the bytes, `Z-W128-S1` DISARMED WITH ITS REASON, and FWD-3 is UNBLOCKED IN MECHANISM, not REALIZED

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-23T15:1xZ, LOCAL on SITEZ.
**Inputs:** `2.0.0_SA_COO~Z`'s packet @`12f98aa11d`, the instance, and this seat's own reads of
`lib/research/filings/battery.py` at HEAD. **Graded LATE:** this packet sat undelivered ~7h while this
seat was deaf (see `:72` of the closer contract -- NOT_EVALUATED until now; it is evaluated now).

## Round state

**1 of 1 terminal. Sweep PASS 9 / FAIL 0 / UNVERIFIABLE 0 of 9**, rc=0 VALID, 9/9 alignment.
**111 tests pass**, verified by the issuer in the MERGED tree rather than inherited from the worker.
Live spend: **11 of 12 permitted HKEX fetches**, 0 Bloomberg, 0 deletes -- inside the order's own bound.

## 1. BOTH BLOCKERS CLOSED -- VERIFIED HERE, NOT ADOPTED

| blocker | round 35 state (measured by me @`c56cc0c48c`) | HEAD state (measured by me now) |
|---|---|---|
| **A** -- search returns nothing | `stockId="00992"` -> `recordCnt=0` under every combination tried | ⭐ **ID-SPACE error, not a parameter error:** the adapter now resolves HKEXnews' INTERNAL predictive-search id (`:1227-1257`, `activestock_sehk_e.json` at `:1238`); `00992` -> 0 and `2325` -> **1117**, every other parameter byte-identical |
| **B** -- no branch can win | **5 of 5 return paths `passed: False`**, including the search-success branch | ⭐ **10 return paths, 9 `False` and ONE `True` at `:1445`**; the winner is consumed at `:1574-1575` and the object is built from `battery_extra`, not from the orphaned `seeds` list |

⛔ **`Z-W128-S1` IS VINDICATED AT THE BYTES, AND THAT IS THE ROUND'S LOAD-BEARING FACT: "do not assume
query-tuning alone resolves it" was right because TUNING VARIES THE PARAMETERS AND THE PARAMETERS WERE
ALREADY CORRECT.** A tuning pass could have run forever. **DISARMED WITH ITS REASON, not silently
dropped**, exactly as the issuer asked.

⭐ **And the POSITIVE CONTROL is what made `1117` interpretable:** AC0 proved the interface answers at all
(no `stockId`, `searchType=0`, a date range -> **recordCnt 14376**) BEFORE any conclusion about Lenovo.
**Without it, `0` and `1117` are two numbers from two guesses.** The order made the control mandatory and
refused an unmeasured zero; that bound is why this round closed instead of producing a fourth half-fix.

## 2. ⭐ MY OWN PREDICTION WENT THE OTHER WAY, AND I STATE IT

My close log predicted: *"`AC4` passing while `AC5` fails is the outcome that proves the cell's design
right."* **Both PASSED** -- AC4 on the fixture (`passed=True`, step 5, national-regulator) and AC5 on
`run_battery` over the SAME fixture (`status: RESOLVED`). ⛔ **The separation still did its job: it was
gradeable independently, and had propagation been broken AC5 would have caught it while AC4 stayed
green.** A control that passes is not a wasted control -- but my prediction of WHICH way it would resolve
was wrong, and the record should not read as though I called it.

## 3. RULING ON FWD-3: UNBLOCKED IN MECHANISM, **NOT** REALIZED

⭐ **The packet separates these itself rather than letting nine PASSes read as a served outcome, and the
separation is correct.** The route is now CAPABLE of resolving; a LIVE win additionally requires the
newest filing for the name to be an annual report on the day, because the adapter inherits round 35's
most-recent-filing selection. ⛔ **The worker NAMED that limitation instead of silently widening the cell
to fix it** -- which is why limb 2 is fixture-proven and why this grade can be clean.

**So: FWD-3 is UNBLOCKED IN MECHANISM. It grades REALIZED only on a live end-to-end win**, and nothing in
this round claims one. Per closer-contract `:66`, the evidence level here is **offline exercise + live
interface probe**, not **actual end-to-end**; a fixture PASS is not a live PASS.

## 4. ⛔ THE `.scratch/**` LANE GAP NOW COSTS LIVE RESEARCH EVIDENCE

Ten `.scratch/r129/` scripts behind AC0-AC7 were REFUSED by `owned-paths-check` and exist **only** in
`C:/tmp/wk-amgt-36-129`. ⭐ **The issuer therefore did NOT remove the worktree, against `safe-merge`'s own
closing advice, because removing it discards untracked files silently.** ⚠ **That is the correct call and
I affirm it: DO NOT REMOVE THAT WORKTREE until the scripts have a durable home.** Third instance of this
gap and the FIRST where it costs live research evidence rather than convenience -- a stronger card row
than the previous two, and it is `0.0.0_AB_MSTR~Z`'s to carry.

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S411",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T15:15Z",
    "one_line": "L9 GRADE RECORD for round 36: 9 of 9 PASS, rc=0 VALID, 111 tests in the merged tree, 11 of 12 permitted live fetches. BOTH stacked blockers verified CLOSED on this seat's own instrument -- blocker A was an ID-SPACE error (internal predictive-search id 2325 vs listed code 00992, 1117 records vs 0, every other parameter byte-identical) and blocker B is closed by a passed:True path at battery.py:1445 consumed at :1574. Z-W128-S1 DISARMED WITH ITS REASON. FWD-3 is UNBLOCKED IN MECHANISM, NOT REALIZED: a live win still requires the newest filing to be an annual report on the day.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "battery.py at HEAD: _hk_national_regulator at :1294 has 10 return paths, 9 carrying passed False and ONE carrying passed True at :1445; run_battery consumes the winner at :1574-1575. At c56cc0c48c the same function had 5 of 5 passed False.",
        "Internal-id wiring at :1227-1257 with _HK_ACTIVE_STOCK_LIST_URL at :1238; the code records the isolated measurement stockId=00992 -> 0 and stockId=2325 -> 1117 with every other round-35 parameter held byte-identical.",
        "Instance: 9 acceptance entries, all PASS, each with a printed denominator -- AC0 2 of 2 attempts plus the 14376-record positive control, AC1/AC8 111 of 111 tests, AC2 4 of 4 parameters, AC4 fixture passed=True, AC5 run_battery RESOLVED on the same fixture, AC6 2 of 2 controls, AC7 11 of 12 permitted fetches logged per URL."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine v3 L9: the CVO grades the round against the criteria that bound it, and grades a forward outcome only on the evidence level actually reached.",
    "world_is": "The route is capable of resolving and is not demonstrated end-to-end; both blockers that made it incapable are closed.",
    "notes": "MY OWN PREDICTION WENT THE OTHER WAY AND I SAY SO: my close log predicted AC4 passing while AC5 failed as the outcome proving the design; BOTH passed. The separation still did its job -- it was independently gradeable -- but the record should not read as though I called the result. GRADED LATE: this packet sat undelivered about seven hours because I killed my own watcher at wind-down, which made me deaf rather than idle; closer-contract :72 retained it NOT_EVALUATED and it is evaluated here. AFFIRMED: C:/tmp/wk-amgt-36-129 must NOT be removed -- ten .scratch/r129 scripts were refused by owned-paths-check and exist only there, the third instance of that lane gap and the first to cost live research evidence.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W128-S1"
    ],
    "dismissal_reason": "Grade record and disarm: Z-W128-S1's warning was correct and is now vindicated at the bytes, so it is disarmed WITH its reason rather than dropped; FWD-3 moves to unblocked-in-mechanism, not realized."
  }
]
```
