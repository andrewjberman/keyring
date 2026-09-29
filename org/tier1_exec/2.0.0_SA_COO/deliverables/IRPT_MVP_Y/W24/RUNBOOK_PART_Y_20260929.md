# W24 part Y -- the runbook, ready before the signal

`2.0.0_SA_COO~Y`, written 16:2xZ while HOLDING for `2.0.0_SA_COO~P`'s start signal (~P 102908: "start Y1 on my
signal only"; my bodies follow ~D's BEFORE reads, the r3 apply, ~D's P2 and ~D's K10).

**Window:** OPEN 16:18:34Z, **cap 18:18:34Z**. Ledger `irpt-ui-walk-principal-w24-20260929` (C1 closed).
**Packet:** blob `49148a2d2a` @91b587480d. **CTO half** SIGNED @1f8d659554, two conditions. **Order ruled by ~P**
(102890): K10 first, then Multi-Comp, Target Weight, 49financial, Inflection, discriminator **droppable by name**;
the cap truncates from the bottom of that order.

## Pins verified at 16:2xZ, before any body

| pin | expected | read |
|---|---|---|
| K1-CRED | exists, never decrypted here | `/irpt/ui-walk-principal/1790698706/password`, SecureString, modified 1790698716 (16:18:36Z) |
| `irpt-ycharts-generate` | W24-1 pins `inrij6hL` | `inrij6hLQiz/ZtOL3Wnzu3aA3xekxlRxYSEajtYqVZw=`, 15:00:32Z, Successful -- **EQUAL** |
| `irpt-generation` | 0/0 | 0 visible / 0 in flight |
| `irpt-generation-dlq` | the A1 BEFORE baseline | **1** (the pre-existing message). Any growth is a BLOCKING row (CTO's W22 condition, carried) |

## The two CTO conditions, and how each is met

1. **Serialize on the `irpt-jobs` row terminal, not the `NORMALIZATION` row.** `live_chain.py` returns as soon as its
   K5 POST is accepted, so serialization cannot come from it. `job_terminal_wait.py` (new, this lane's tooling) blocks
   on the jobs row until READY / FAILED / ATTENTION and then holds a 20 s floor. **Controls run before the window:**
   W22's `REQ-7ea49c2d` returns TERMINAL READY; W22's `REQ-51f1413b` returns TERMINAL ATTENTION with
   `{"code":"SESSION_REFRESH_ALREADY_USED"}`; a nonexistent REQ keeps waiting and never reports terminal.
2. **The discriminator touches no other user.** Immediately before Y5/Y6, read `irpt-generation` 0/0 AND confirm no
   non-principal job is in flight. If another user's work is live, the discriminator **waits for it or is skipped, by
   name** -- it is the droppable item in ~P's order.

## Common environment

```
WALK_PW_NAME=irpt/ui-walk-principal/1790698706/password      # no leading slash: Git Bash mangles it
WALK_EMAIL=irpt-uiwalk-1790698706@opal.test
WALK_PW_RETAINED=1
WALK_AUTHORITY="W24 packet 49148a2d2a (@91b587480d); CTO half 1f8d659554; ledger irpt-ui-walk-principal-w24-20260929; ~P 102908"
```
`WALK_DEADLINE` is set PER BODY, bounded and always inside 18:18:34Z. Output goes to
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/W24/`.

## The bodies, in ~P's ruled order

Each is: one `live_chain.py` run (one login, one K4, one K5, no retry), then `job_terminal_wait.py` before the next.

| # | body | firm | the arm it closes | extra env |
|---|---|---|---|---|
| Y1 | Multi-Comp | cottonwood | W21 Y2 / W22 Y2 -- both models printed, or `COMPARISON_NOT_PRINTED` | `WALK_COMPARISON_KEYS=opal_short_term,opal_intermediate_term` |
| Y2 | Target Weight, notional 1000, XLSX | cottonwood | W22 Y3 -- the REPORT (the vendor half is already proven) | `WALK_UPLOAD_FILE=...aapl-vnq-target-weight.xlsx WALK_FILE_TYPE=xlsx WALK_REFERENCE_NOTIONAL=1000` |
| Y3 | Overview | 49financial | the FIRST certified 49financial report | -- |
| Y4 | Overview | inflection | a certified Inflection report | -- |
| Y5+Y6 | two Comparisons, SIMULTANEOUS | cottonwood | the S206 discriminator -- droppable | `WALK_COMPARISON_KEYS=opal_long_term` |

**Preflight, all six validated OFFLINE at 16:0xZ after the `live_submit.py` repair @4d676b93a9** (row
`IRPT_BCKEND-S211`): 5 of 5 body shapes print `K5 body validates` (Y5 and Y6 share a shape).

## Reading each body's terminal state (row S207)

The resident journals NO line for a job ATTENTION -- over W22's 14:08-14:34Z span, 79 lines, all
`IRPT_RESIDENT_POLL`, while a job moved to ATTENTION `SESSION_REFRESH_ALREADY_USED`. So per body:

1. `irpt-requests` `NORMALIZATION#<upload_id>`, consistent Query: `state`, `reason`, `findings`, `dispatched_at`,
   `resolved_at`;
2. `irpt-jobs` by `tenant` + `job`: `state`, `job_detail.code`, `outbox_state`, the `intent_*` claims and fence;
3. `case_trace.py <firm> <REQ>` on every body that reaches a report;
4. the `IRPT_RESIDENT_RESOLVE` lines by SSM as **corroboration, never the oracle**.

## Grading the discriminator (the interpretation rule sent at 15:49Z)

W22's solo Comparison ran on generate `wnt7hjAB`; W24 runs on `inrij6hL`. The solo baseline is therefore not
established on this build, and Y1-Y4 serialized ARE the control:

- at least one of Y1-Y4 READY, and both Y5/Y6 exhaust -> **S206 CONFIRMED**;
- at least one of Y1-Y4 READY, and both Y5/Y6 READY -> **S206 REFUTED**, re-open the row;
- one of each -> single-flight at a finer grain; record which won and its ordering;
- **none of Y1-Y4 READY -> Y5/Y6 grade UNINTERPRETABLE, never CONFIRMED.**

## At the end

Every REQ case-traced to a terminal state by name; the DLQ re-read against the baseline of 1; leg Y proof and the A1
per-body route record committed; then hand ~P the credoff. A hang past 18:18:34Z is a fail of that body, not a reason
to extend.
