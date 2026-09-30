# Never-widen sign-off packet -- WINDOW 22: the first Analysis on resident st4 (~Y's part Y), one principal

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Operator of create, credoff and delete:** `2.0.0_SA_COO~P`, 2026-09-29
~13:0xZ. **Walker:** `2.0.0_SA_COO~Y` (`live_chain.py` @78c8ce05a6, `WALK_PW_RETAINED=1`; `case_trace.py` @f86dc994b9).
**Ledger (opened before any write):** `irpt-ui-walk-principal-w22-20260929`. **Asked by:** ~Y 102796 / 102799.

**Purpose:** the CRO's st4 condition 3 (102791), which is to read the two st4 fixes LIVE:
- S194: a Comparison sends its models and refuses a PDF printing none;
- S193: a resolve RETRY is bounded, and the 4th receive moves the row to NEEDS_CORRECTION
  `RESOLVE_RETRY_EXHAUSTED`.

It also carries window 21's open part-Y arms: Multi-Comp, Target Weight, and the first certified 49financial and
Inflection reports.

**Precondition, MET:** resident st4 is live. Ledger `irpt-resident-st4-yr201-yr211-20260929` CLOSED @4af16f7879: SSM
2bcd0fad rc 0, root `fe64236bbb-st4`, resident_worker 5288ff5a. ~Y re-read the host at 12:34Z and it matches.

This packet is window 21's part Y (`NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W21_20260929.md`, blob 84ec7f79, both halves,
amendment 1 included) with the deltas below. There is no part P and no revocation arm R. Every unnamed section reads as
W21's, and through it window 15's: the keys and radius, D2, the start condition, the per-body W15-2 YCharts bounds, and
the audit.

## W22-1 -- the pins, re-read at create

- irpt-ycharts-generate `wnt7hjAB..` (live since 12:09Z, ledger irpt-holdings-contract-category-20260929 CLOSED);
- the resident root `/opt/irpt-resident/fe64236bbb-st4`;
- irpt-status and irpt-directory-search as read at create, and written in the ledger;
- irpt-generation queue 0/0; the DLQ message count read before and after (the CRO's st4 condition 1 fallback arm).

Part Y's path is generate -> queue -> resident -> status. It does not call irpt-performance-adapter. So the 49F
re-switch, under its own ledger and halves, may land during the window, and W22 does not pin the adapter.

If any pin differs at create, the window does not open.

## W22-2 -- the bodies (~Y's `W22_PART_Y_ARMS_20260929.md` @ac0eade564), one principal, W15-2 bounds PER BODY

| # | body | firm | reads | disarms / carries |
|---|---|---|---|---|
| Y1 | Comparison `opal_long_term` (CSV) | cottonwood | resolve line READY; the PDF prints the chosen model, or ATTENTION `COMPARISON_NOT_PRINTED` | S194 |
| Y2 | Multi-Comp `opal_short_term`,`opal_intermediate_term` (CSV) | cottonwood | resolve line; both models printed, or `COMPARISON_NOT_PRINTED` | S194, W21 Y2 |
| Y3 | Target Weight, notional 1000 (XLSX) | cottonwood | resolve line READY within the bound (<= 4 receives, about 3 min), or ATTENTION `RESOLVE_RETRY_EXHAUSTED` with the row NEEDS_CORRECTION | S193, W21 Y4 |
| Y4 | Overview (CSV) | 49financial | resolve line; the first certified 49financial report, or a named refusal | S193, W21 Y6 |
| Y5 | Overview (CSV) | inflection | resolve line; a certified Inflection report, or a named refusal | W21 Y5 |

- **Cap: 5 submissions.** One login, one K4 and one K5 per body; no retry. A challenged vendor mutation is never
  replayed: ATTENTION `VENDOR_GENERATE_REFUSED` is a named refusal, as in W21.
- ~Y case-traces every REQ to its terminal state. The journal's `IRPT_RESIDENT_RESOLVE` lines for the window span are
  read by SSM, read-only.
- A named terminal state, whether READY or an ATTENTION with its code, is a pass of the window. A hang past the
  120-min cap is not.

## W22-3 -- the interval and the principal

- The window opens after both halves are at HEAD, and closes 120 min from create at the latest.
- K1 (the walk user) and K1-CRED (its password parameter) are created at open with `walk_principal.py --kind=uiwalk`,
  as in W21.
- After the last body is terminal: credoff (the K1-CRED delete, read back as ParameterNotFound), then the K1 delete
  (a consistent read finds no item). Both happen at the cap at the latest.
- **Before and after:** the users census (count + digest), `walk_window_census.py` (REPORT# per firm, 49F rows,
  evidence objects, render tokens, media, arm-3 owner) and the DLQ count. A1 closes on their diff and on ~Y's per-body
  route record.

## W22-4 -- blast radius, both branches

- Every arm is either a read, or a write the principal owns (its portfolios, reports and REQ rows). Nothing served for
  any other user moves. There is no code, IAM or schedule change.
- **If a body FAILS:** the failed REQ stays as evidence, a BLOCKING row lands the same tick, and nothing is deployed in
  the window.
- **If the resident misbehaves** (a traceback loop, or a hang past the bound): the window closes. Rolling the resident
  back to st3 is its own act under the st4 ledger's rollback root, never inside this window.

## What the halves sign against

This file's committed blob; W21's text (84ec7f79) with its conditions, as narrowed here; ~Y's arms @ac0eade564; the pins
in W22-1; the bodies and cap in W22-2; and the interval in W22-3.
