# Never-widen sign-off packet -- WINDOW 8: INF's ONE Orion read (plan 7f64b166, end 09-22) + an optional third Analysis attempt

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Operator:** `2.0.0_SA_COO~P`, 2026-09-27 ~03:5xZ.
**Ledgers (opened before any write):** `irpt-ui-walk-principal-w8-20260927`, `irpt-performance-inf-one-use-4-20260927`.

This packet is window 7's (blob 3ab51a52, which is window 6's fffdca65 + D1-D5), with only the deltas below. Every
unnamed section reads as window 7's, including:
- K1 / K1-CRED / K2 / K3;
- the superadmin radius;
- the route audit;
- the principal kept until every job is terminal, with a 120-min cap;
- the K1-CRED deletion as soon as the walkers have logged in.

## W8-1 -- INF's ONE Orion read (Andrew's call 2, still UNUSED: 0 Orion calls so far)

**The plan** (`INF_ONE_USE_PLAN_4_20260927.json`, `inf_one_use_plan.py` with no vendor call):

| field | value | source |
|---|---|---|
| account | `acc_5510a3054a409d548a12c57d` (****4944) | the stated rule; the same pick as plans 3a/3b (rank 55) |
| window | 2026-01-01..**2026-09-22** | end READ at build from the served INF holdings answer: `irpt-holdings` GET on sel_366d4891.., `source_dates.business_date` 2026-09-22 (CTO 101756 / CRO 101753 (b)) |
| expires_at | 1790510400 = 2026-09-27T12:00:00Z | |
| sha256 | `7f64b166f58eb672e5e2ff43fc9624a3a528eaf5bcc3274764f5eed33a319c10` | |

**Order:**

1. **The arm-OFF pre-check (CRO 101753).** The live plan is the spent 01209afb. ~D, logged in with the firm selector
   on Inflection, opens Performance on the account once. The request's `end` must read **2026-09-22** in the URL or
   HAR. With the arm off, the adapter refuses VendorEgressRefused and makes no vendor call. **If `end` is not
   09-22, nothing arms.**
2. **The arm, on 3a68bb2d's terms:**
   - safe-apply re-plans 0/1/0 with exactly the two env keys; any other diff stops it;
   - readback: the env plan sha is 7f64b166 and the egress digest matches.
3. **K11:** ~D re-opens Performance on the same account (the same page, no new login). This is ONE matching read =
   ONE Orion Performance request, spending the plan at `PERFORMANCE_USE#7f64b166..`. The outcome is the result
   (READY/PARTIAL = INF's first signed-in journey, or a named refusal). No retry.
4. **Disarm:**
   - if spent, it stays spent (the gate refuses further reads);
   - if K11 did not claim before the window's delete, re-apply the spent 01209afb the same tick (CTO 3a68bb2d item 2).

**The audit (CRO):** exactly ONE Orion call across call 2 in total, counted from the adapter log; INF REPORT# 0 -> at
most 1, traced to K11's HAR response.

## W8-2 -- an optional third Analysis attempt (ONLY on Andrew's word at the ~Y terminal)

- As window 7's K4/K5/K10, on the resident now served at `/opt/irpt-resident/fe64236bbb-rb` (the read-back poll
  fix; ledger irpt-resident-read-back-poll-20260927).
- **CTO 101763's condition:** K5's named vendor reads include up to **12** `model_portfolios/{id}/status` GETs, 5 s
  apart, plus the read-back, besides window 6's list.
- **If no word reaches ~Y**, W8-2 does not run; window 8 is W8-1 alone.
- **K10 caveat (DSGN_IRPTV1-S18):** the page cannot list a job from another session. K10 is therefore the resident
  journal plus read-only table reads, and ~D's page read only if the page can show it.

## W8-3 -- the served pins, re-read at create (CTO condition carried)

- generate `G/TqLPdL..`;
- the resident root `fe64236bbb-rb`;
- the adapter code `Ll6t4VPa..` with the live plan sha 01209afb.

If any differs, the window does not open.

## What the halves sign against

This file's committed blob; window 7's text (3ab51a52) as amended here; the INF plan 7f64b166 with its arm-off
pre-check, arm terms, ONE read and disarm; and W8-2 gated on Andrew's word with the 12 status polls named.
