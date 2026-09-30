# Never-widen sign-off packet -- WINDOW 21: the page arms (K10, K4, K8) and the Analysis bodies (K5 + ~Y's arms), one principal

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Operator of create and delete:** `2.0.0_SA_COO~P`, 2026-09-29 ~02:0xZ.
**Walkers:** `2.0.0_SA_COO~D` (the page, part P) and `2.0.0_SA_COO~Y` (`live_chain.py` @78c8ce05a6, part Y).
**Ledger (opened before any write):** `irpt-ui-walk-principal-w21-20260929`. **Asked by:** ~Y 102405, 102408, 102524;
STATUS~P next-list item 3. **Precondition:** the resident runs st3 (ledger `irpt-resident-saved-type-st3-20260929` D1
closed); if D1 has not closed, the window does not open. **D1 CLOSED** 02:49Z (@a45157fe5a: root fe64236bbb-st3, SSM
add63ec1 rc 0).

This packet is two signed packets joined under ONE principal, with the deltas below:
- **part P** = window 19's (`NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W19_K8_20260927.md`, blob 35c9083d, both halves): K10,
  K7/K8, the route classes, the byte-proof, the /download body out of the HAR, the %PDF audit on the SERVED object, and
  K1-CRED;
- **part Y** = window 15's (`NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W15_ANALYSIS_20260927.md`, both halves, itself window
  13's): the keys and radius, the route audit, D2 (the principal stays until every job is terminal, cap 120 min), the
  start condition (Andrew's "yes you can run as many analysis attempts as needed", @460e2ae8cb), the per-body YCharts
  bounds of W15-2, and the audit of W15-4.
Every unnamed section reads as those.

## W21-1 -- the pins, re-read at create (read live 2026-09-29 ~01:5xZ)

- irpt-ycharts-generate `AdE17rT6..`; the resident root `/opt/irpt-resident/fe64236bbb-st3` (after D1);
- irpt-status `ZYr+IDMp..`; irpt-performance-adapter `qfxZ0DzB..`, with NO plan; irpt-export-render `BORQ2shb..`;
  irpt-directory-search `o1TXq5PH..`;
- the page: local portal DEV, ~D names its pin at create with 0 tracked changes.

If any differs at create, the window does not open.

## W21-2 -- part P arms (~D, the page), in this order

1. **K10 (read-only):** window 15's REQ-67e12718 (cottonwood) reads READY ANALYSIS_READY PER_SECTION on the page and
   RPT-5288c06d opens. Closes A1 of `irpt-status-dates-rebuild3-20260928`.
2. **K4 (read-only):** window 15's Dollars CSV downloads from the page; the file's rows match the report's figures.
3. **K8 (one export):** window 19's arms 1-4 unchanged -- ONE POST QUEUED with an `exr_` revision under 29 s; the page
   polls the receipt without a reload; the render's Performance read has 0 AccessDenied; READY with a %PDF on the served
   object, or a named FAILED; ONE download; exactly 2 irpt-export-render invocations. Closes the A1 legs of
   `irpt-adapter-render-grant-kms-20260927`, `irpt-adapter-render-selection-20260927`,
   `irpt-export-async-submit-20260927`, `irpt-export-receipt-running-20260928` and `irpt-export-reopen-rule-20260927`.

## W21-3 -- part Y bodies (~Y, `live_chain.py`), one principal, W15-2 bounds PER BODY

| # | body | firm (chosen on the principal) | expected |
|---|---|---|---|
| Y1 | Comparison `opal_long_term` (K5) | cottonwood | ACCEPTED; READY or a named terminal state |
| Y2 | Multi-Comp, two keys from `WALK_COMPARISON_KEYS` | cottonwood | ACCEPTED; READY or named |
| Y3 | Y2 XLSX template arm | cottonwood | as live_chain.py names it |
| Y4 | Y2 Target Weight arm | cottonwood | as live_chain.py names it |
| Y5 | Overview | inflection | the firm's first certified Analysis report, or a named refusal |
| Y6 | Overview | 49financial | the firm's first certified Analysis report, or a named refusal |
| R | revocation, driven deliberately | cottonwood | see below |

- **Total YCharts work:** at most 7 submissions, each inside W15-2's bounds (one upload, one create, the read-back
  bounds, one saved GET, validate, one report create, ONE PDF download). No retry of a body.
- **R (the revocation arm, ~Y item 5):** after R's own Overview job reads RUNNING, `walk_principal.py credoff` deletes
  K1-CRED; its ParameterNotFound read is timestamped in the ledger. Expected: R's job reaches a NAMED terminal state
  (READY or ATTENTION/FAILED with a reason), never a hang past 120 min; a fresh page read under the revoked credential
  is refused. Y1-Y6 are the organic negative arm. R runs LAST, after Y1-Y6 are terminal, so it cannot strand them.
- **New with st3:** a saved portfolio type other than `fixed` with a tolerated setting stops at ATTENTION
  `TOLERANCE_REQUIRES_STATIC` before generation. That is a named terminal state, not a failure of the window.
- ~Y grades every REQ with `case_trace.py <firm> <REQ>` plus the resident journal, and commits each trace under
  `deliverables/2.0.0_SA_COO~Y/`.

## W21-4 -- the interval

It opens only after st3's D1 closes, and it closes 120 min from create at the latest. MSTR's 03:00-05:00Z freeze, if
it is running that night, is respected: the window opens after 05:00Z or completes before 03:00Z. K1-CRED is deleted at
R, the last arm; the principal is deleted when every job is terminal.

## W21-5 -- blast radius, both branches

- Every arm is either a read, or a write the principal owns: the export receipt and PDF for part P, and the portfolios,
  reports and REQ rows for part Y. Nothing served for any other user moves; there are no code, IAM or schedule changes.
- **If an arm FAILS:** part P follows window 19's rollback pointers (dd91065c section 3; f7aa7b3c section 3); part Y
  keeps the failed REQ as evidence, and a BLOCKING row lands the same tick. Neither branch deploys anything in the
  window.

## Amendment 1 (2026-09-29 ~02:5xZ, ~Y 102555) -- part Y's tool re-pinned e29a2e7d27 -> 78c8ce05a6

The halves of blob 32152ea0 signed `live_chain.py` @e29a2e7d27, which cannot run W21 as written. 78c8ce05a6 (~Y; its
commit body lists the dry runs) changes three things only; bodies and bounds are unchanged:
1. the firm comes from `WALK_TENANT`, checked against the registry (it was hard-coded to cottonwood), for Y5 and Y6;
2. `WALK_PW_RETAINED=1` skips each body's wait for the K1-CRED delete, which W21 keeps until R;
3. `request_id` is per second, not per day, so Y3, Y4 and R cannot collide.
The CRO half's three conditions (102553) are carried unchanged.

## What the halves sign against

This file's committed blob; window 19's text (35c9083d) and window 15's text with their conditions, as amended here; the
pins in W21-1; the arms and bounds in W21-2 and W21-3; the precondition (st3 D1 closed); and the interval in W21-4.
