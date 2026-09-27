# Never-widen sign-off packet -- WINDOW 7: the Analysis chain end to end, second attempt (window 6's shape, CTO 101673 applied)

**For:** `1.0.0_SA_CTO` (half 1) and `4.0.0_SA_CRO` (half 2). **Prepared by / operator of create and delete:**
`2.0.0_SA_COO~P`, 2026-09-27 ~02:2xZ. **Ledger (opened before any write):** `irpt-ui-walk-principal-w7-20260927`.

This packet is window 6's (blob fffdca65, `NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W6_20260926.md`) with ONLY the deltas
below. Every section not named here reads as window 6's text, including:
- section 2's keys K1-K5 and K10, and K5's measured write set;
- the named vendor calls;
- section 3's radius and section 4's route audit;
- window 6's amendment 1 (K9: Performance reports that page reads retain).

## Why a second attempt

Window 6's K5 never reached READY: S151 (receive 1's session capture failed) and S150 (the principal was deleted while
the job still needed it). Both are closed:
- S151 disarmed, ~Y 101704: one wrapper run, on Andrew's word, authenticated in 12 s; a fresh session is AWSCURRENT
  (fence 13).
- S150 graduated into CTO 101673: the principal stays until every job is terminal.

## Deltas from window 6

### D1 -- the served code (all measured today)

| Hop | What serves it |
|---|---|
| 1-3 | irpt-ycharts-generate `G/TqLPdL..` (hop-3 six + the cross-viewer title binding) |
| 5-7 | resident `/opt/irpt-resident/fe64236bbb-xv`: hop-7 certify, the retained-reason journal lines (a failure names its class and code), the cross-viewer binding |
| 8-9 | irpt-status `bMMJ/bQ+5..` |

### D2 -- the principal's life (CTO 101673)

- The delete leg runs only after EVERY job the window started reads terminal (READY or a named refusal), with a hard
  cap of **120 min** from the create.
- **At the cap with a non-terminal job:** P states that job's disposition in a same-tick amendment (closed how, or
  left alone and why) BEFORE the delete, and the CTO signs it.
- **Branch (e) is struck:** no job is left to finish without its submitter.
- K2's session rule is unchanged: access tokens live 15 min and refresh re-reads K1, so the session dies with the K1
  delete.

### D3 -- start condition

- **P creates** on both halves at HEAD.
- **~Y starts K4** only on Andrew's word at the ~Y terminal (his standing condition on ~Y running a window).
- If no word comes within 30 min of the create, P deletes with 0 ~Y requests, branch (b).

### D4 -- K10 and the audit

- **K10:** ~D reads the READY report in the page (sections, job status, history, request read) while the principal
  lives.
- **The audit:** window 6's section 6 step 7, plus the resident journal's `retained_for_retry class=.. code=..`
  lines, named if any appear.

### D5 -- vendor calls

As window 6's section 2, exactly. The session is fresh, so a capture should not be needed. If one is, it is the
receive's own one-use `session_refresh` intent, as before; no extra run.

## What the halves sign against

This file's committed blob together with blob fffdca65's text, as amended by D1-D5; the key list K1 + K1-CRED + K2 +
K3 + K4 + K5 + K9 + K10 (retained as window 6's); and the 120-min cap with the terminal-job rule.
