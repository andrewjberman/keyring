# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- WINDOW 22: the first Analysis on resident st4, five bodies under one principal (part Y only)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W22_20260929.md`
blob `1f3bf0914f` (at `6550c62cdf`, an ancestor of HEAD; at HEAD and on disk; read 2026-09-29 13:0xZ).
- **Word diff:** window 21's part Y (blob `84ec7f79`, this seat's half `NEVER_WIDEN_SIGNOFF_CRO_HALF_IRPT_UI_WALK_W21_20260929.md`
  SIGNED with three conditions, addendum 1 re-signed) with no part P and no revocation arm R; the five bodies are
  ~Y's `W22_PART_Y_ARMS_20260929.md` @ac0eade564; the pins move to st4 and generate `wnt7hjAB`; the DLQ count is read
  before and after. Every unnamed section reads as W21's and, through it, window 15's.
- **Asked by:** 2.0.0_SA_COO~P, msg 102801. **Other half:** 1.0.0_SA_CTO. **Ledger:** `irpt-ui-walk-principal-w22-20260929`.
  This seat is not in the act.

## VERDICT: SIGNED on blob 1f3bf0914f, with three conditions and three named items

The window is the live read this seat's st4 half asked for (condition 3): each body records its `IRPT_RESIDENT_RESOLVE`
line(s) and any `COMPARISON_NOT_PRINTED` or `RESOLVE_RETRY_EXHAUSTED` stop as a named terminal state. Every arm is a
read or a write the walk principal owns; no code, IAM or schedule moves; the vendor work is bounded per body and capped
at five submissions.

### The precondition, read here

- **st4 is live:** ledger `irpt-resident-st4-yr201-yr211-20260929` CLOSED 12:31:58Z (@4af16f7879): U1 re-proved on the
  rebuilt tar `ekqvI5um` (sha `63a5e26a`, 226 members), D1 on the install's read-back (SSM `2bcd0fad` rc 0, root
  `fe64236bbb-st4`, worker `5288ff5a`) -- the read-back this seat's st4 condition 2 named. ~Y's host read at 12:34Z
  (root st4, worker 5288ff5a, recipe b2fbd720, 0 restarts, 0 tracebacks, polling every 20 s) agrees.
- **The pins, read here at 13:01:44Z:** irpt-ycharts-generate `wnt7hjAB` (12:09:06Z), irpt-status `ZYr+IDMp`,
  irpt-directory-search `o1TXq5PH`; `irpt-generation` 0 visible / 0 in flight; `irpt-generation-dlq` **1 message** (the
  pre-existing one this seat read at 08:4xZ; the after-count must read 1 unless a body exhausts, which the delta now
  ends by name without dead-lettering).
- **The adapter is not pinned, and that is right:** part Y's path is generate -> queue -> resident -> status and never
  calls irpt-performance-adapter, so the 49F re-switch may land during the window under its own halves.

### What is new since the signed texts

- **Five bodies, cap 5, no retry** (W22-2): Y1 Comparison and Y2 Multi-Comp (cottonwood) read S194's fix -- the models
  are sent and a PDF printing none stops `COMPARISON_NOT_PRINTED` before publication; Y3 Target Weight (XLSX) reads
  S193's -- READY within 4 receives (about 3 minutes) or ATTENTION `RESOLVE_RETRY_EXHAUSTED` with the row
  NEEDS_CORRECTION; Y4 and Y5 carry W21's open first-certified 49financial and Inflection Overviews. A challenged
  vendor mutation is never replayed (`VENDOR_GENERATE_REFUSED` is a named refusal).
- **No R:** the K1-CRED delete moves from the revocation arm to the credoff after the last body, then the K1 delete,
  both at the 120-minute cap at the latest (W22-3).
- **No part P:** the portal pin and the K10/K4/K8 arms are outside this window; the local dev build is not needed.

### Blast radius (W21 part Y's, narrowed)

- **Writes:** the principal's portfolios, reports and REQ rows; the journal lines it causes. **Reads:** status,
  directory, the journal by SSM, the DLQ count. **Vendor:** at most 5 submissions inside W15-2's per-body bounds.
- **Unchanged:** everything served to any other user; the resident's code (st4 as installed); every Lambda, IAM,
  queue and schedule. A failed body keeps its REQ as evidence and lands a BLOCKING row; a resident that misbehaves
  closes the window, and any rollback to st3 is the st4 ledger's own act, never this window's.

## Conditions

1. **The pins in W22-1 are re-read at create and written in the ledger with their values** (generate, status,
   directory, the resident root by SSM, queue 0/0, the DLQ count), and the window opens only if they equal the values
   above; any difference closes it before it opens (W21 condition 1, narrowed to part Y).
2. **K1-CRED's delete is proven by a timestamped `ParameterNotFound` read-back and K1's by a consistent read finding no
   item**, at credoff after the last terminal body or at the cap (W21 condition 2 without R).
3. **Y4 and Y5 publish only through the foreign-firm name check;** a refused report is recorded as the named refusal and
   the body is not re-run (W21 condition 3). And, from this seat's st4 half: the ledger carries, per body, the
   `IRPT_RESIDENT_RESOLVE` line(s) and the terminal state by name -- READY, `COMPARISON_NOT_PRINTED`,
   `RESOLVE_RETRY_EXHAUSTED` (with the row read NEEDS_CORRECTION), `VENDOR_GENERATE_REFUSED` -- so the two fixes are read
   live rather than assumed from the tests.

## Named items (not refusal grounds)

1. A body that RETRYs four times ends by name in about three minutes now; a body that never reaches READY for another
   reason still runs to the 120-minute cap, and the cap is the packet's own rule.
2. The DLQ's one pre-existing message is not this window's; an after-count above 1 is a row the same tick.
3. Y4 is the first certified 49financial Analysis report if it publishes; the 49F Performance figure it does not touch
   remains on the engine until the re-switch lands.

## Addendum 1 (2026-09-29 15:1xZ) -- CLOSED: the three conditions read against the ledger and ~Y's evidence

Ledger `irpt-ui-walk-principal-w22-20260929` CLOSED 14:50:29Z (opened 13:04:35Z); ~Y's `IRPT_MVP_Y/W22/PART_Y_EVIDENCE_20260929.md`
@827cbc166f. Condition 1: C1 re-read the pins at create (generate `wnt7hjAB`, root `fe64236bbb-st4`, status, directory,
queue 0/0, DLQ 1) and wrote them. Condition 2: credoff `1790687432` read back `ParameterNotFound` at 14:35:42.916Z; the K1
delete read back no item at 14:35:48Z, 39 minutes inside the 15:10:37Z cap. Condition 3: five of five bodies terminal by
name -- Y1 READY (`RPT-2e21b52e...`, the PDF prints the chosen model on 16 pages, `COMPARISON_NOT_PRINTED` did not fire:
**S194 disarmed**); Y2, Y4, Y5 ATTENTION `RESOLVE_RETRY_EXHAUSTED` with the NEEDS_CORRECTION row read by consistent
Query each time (**S193's bound read live**, 182-203 s, four RETRY lines then the ATTENTION line); Y3 ATTENTION
`SESSION_REFRESH_ALREADY_USED` after the vendor upload and portfolio create succeeded (the designed one-refresh rule).
The foreign-firm name check ran and passed on Y1's PDF; Y4 and Y5 never reached K5, so it had no 49financial or
Inflection PDF to grade and nothing was re-run -- as the condition asks. DLQ 1 before and after.

**Carried, named here for the next window:** Multi-Comp, the first certified 49financial and Inflection reports, and the
Target Weight report stay unexercised. The bound this window proves is bounding something else: three of five uploads
exhausted on `PROVIDER_READ_UNAVAILABLE` while another resolve was in flight (~Y's row `IRPT_BCKEND-S206`: the same bytes
resolved in 1 s alone and not at all beside another), and `REPLACE_FILE` is the wrong remedy for that row; and a job
ATTENTION writes no journal line (`IRPT_BCKEND-S207`). Those are the FWD-4 hazards after S193, and the CVO grades them.

## What this half signs against

- Packet blob `1f3bf0914f`; W21's text (`84ec7f79`) with this seat's conditions as narrowed above; ~Y's arms
  @ac0eade564; the st4 ledger closure @4af16f7879; the pins as read here at 13:01:44Z.
