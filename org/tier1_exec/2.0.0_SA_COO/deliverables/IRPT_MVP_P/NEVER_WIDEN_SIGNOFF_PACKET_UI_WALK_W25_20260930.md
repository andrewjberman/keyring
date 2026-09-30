# Never-widen sign-off packet -- WINDOW 25: the S218 step-2 one-body read, one principal

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Operator of create, credoff and delete:** `2.0.0_SA_COO~P`, 2026-09-30
~03:2xZ. **Walker:** `2.0.0_SA_COO~Y` (`live_chain.py`, `case_trace.py`; arms
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y/S218_STEP2_DISCRIMINATING_READ_ARMS_20260929.md`).
**Ledger (opened before any write):** `irpt-ui-walk-principal-w25-20260930`. **Asked by:** ~Y 103123.

**Andrew's per-use word for the vendor call, verbatim:** "yeah Yes run it" (the ~P terminal, 2026-09-30 ~03:02Z). Record:
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260930_030xZ_S218_STEP2_ONE_BODY_YCHARTS_WINDOW_YES.md`
@d821060b8b. Scope: the ONE window as armed; no retry, no second window.

**Purpose:** read `IRPT_BCKEND-S218` step 2 on the build that carries IB-yr-231: one solo job on a cold resident, whose
journal (`IRPT_RESIDENT_EVICTION verdict=<NAME> job=<id>`) says whether W24's `SESSION_REFRESH_ALREADY_USED` was a
pre-job session rejection or per-call evictions. It may also settle row S151. The four outcomes and the remedy each
implies are in the arms file, written before the run.

**Precondition, MET:** resident st5 is live. Ledger `irpt-resident-st5-yr231-20260930` CLOSED @12dd4b35a5: SSM
ce23ee40 rc 0, root `fe64236bbb-st5`, resident_worker 8d1f5431, pid 307882 from 02:47:36Z; CTO half 103106
(@9fa83724fe); ~Y re-read the running root by SSM (103114). The resident has handled 0 jobs since install (~Y 103123).

This packet is window 24's (`NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W24_20260929.md`, blob 49148a2d2a, both halves,
amendments included) with the deltas below. Every unnamed section reads as W24's and, through it, W22's, W21's and
window 15's: the keys and radius, the start condition, the per-body W15-2 YCharts bounds, and the audit. There is no
part P, no K10 read, no Performance presses, and no revocation arm.

## W25-1 -- the pins, re-read at create

Measured 03:1xZ for this text; re-read at create and written in the ledger:
- irpt-ycharts-generate `inrij6hL..` (LastModified 2026-09-29T15:00:32Z, unchanged);
- irpt-status `ZYr+IDMp..` (2026-09-28T14:04:55Z); irpt-directory-search `s0riHZ9h..` (2026-09-29T14:58:27Z);
- the resident root `/opt/irpt-resident/fe64236bbb-st5`, resident_worker `8d1f5431`;
- irpt-generation 0/0; the irpt-generation DLQ 1 visible / 0 in flight (the pre-existing message, the no-growth baseline).

If any pin differs at create, or the queue is not 0/0, or another job is in flight, the window does not open.

## W25-2 -- the one body, from ~Y's arms file

| # | body | firm | run |
|---|---|---|---|
| Y1 | the W15 CSV, Overview | cottonwood | one login, one K4, one K5, no retry, nothing else in flight |

- **Cap: 1 submission.** A challenged vendor mutation is never replayed.
- **Solo, and provably so:** `irpt-generation` read 0/0 immediately before the K5, and no non-principal job in flight
  (the CTO's W24 condition 2). If other work is live the read WAITS.
- ~Y case-traces the REQ to a terminal state by name and reads `IRPT_RESIDENT_EVICTION` / `IRPT_RESIDENT_ATTENTION` /
  `IRPT_RESIDENT_RESOLVE` lines for the window span by SSM, read-only.
- **A named terminal state, READY or an ATTENTION with its code, is a pass of the window.** A clean READY with no eviction
  line is also a result (arms file, outcome 4). A hang past the cap is not.

## W25-3 -- the interval, the principal and the credential

- Opens once both halves are at HEAD; closes **60 min** from create at the latest (W24 was 120; one body needs less).
- K1 (the walk user) and K1-CRED (its password parameter) are created at open with
  `walk_principal.py --kind=uiwalk` (the v3 shape, blob 07b7a000: role admin, opal-capital, userType Dev), the epoch
  named in the ledger. The password is written only to the SecureString and never printed.
- **Credoff BEFORE the vendor call.** ~Y logs in (`WALK_PW_RETAINED` unset); the moment its login line prints, this seat
  runs `walk_principal.py --kind=uiwalk credoff <epoch>` (K1-CRED deleted, read back as ParameterNotFound). ~Y's
  `live_chain.py` polls for that before K4. So the credential does not exist while the vendor is called.
- After the body is terminal: the K1 delete (a consistent read finds no item), and both at the cap at the latest.
- **Before and after:** the users census (count + digest), `walk_window_census.py` (REPORT# per firm, 49F rows,
  evidence objects, render tokens, media, arm-3 owner) and the DLQ count. Any DLQ growth over the baseline is a BLOCKING
  row the same tick (the CTO's W22 condition).

## W25-4 -- blast radius, both branches

- Every arm is a write the principal owns (its portfolio, report and REQ rows) plus reads. Nothing served for any other
  user moves. No code, IAM or schedule change; no resident restart.
- **If the body FAILS:** the failed REQ stays as evidence, a BLOCKING row lands the same tick, nothing is deployed in the
  window and no retry is fired.
- **If the resident misbehaves** (a traceback loop, or a hang past the cap): the window closes. Rolling the resident
  back to `fe64236bbb-st4` is its own act under the st5 ledger's rollback root, never inside this window.
- **Reachable:** one login, one vendor session, one Comparison-free Overview job for the cottonwood firm.

## What the halves sign against

This file's committed blob; W24's text (49148a2d2a) with its conditions, as narrowed here; ~Y's arms file; Andrew's
record @d821060b8b; the pins in W25-1; the body and cap in W25-2; the interval and credential order in W25-3.
