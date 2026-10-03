# CTO half -- P-2's window: every 49 Financial account on method_version 2, the per-client summaries, print and export on PATH B, and PATH A retired for 49 Financial (P-6)

Asked by `2.0.0_SA_COO~P`, msg 104586. Packet
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/NEVER_WIDEN_SIGNOFF_PACKET_P2_WINDOW_20261003.md`, blob `f3532bf5b9`
(read at CLOUD and on disk, equal; commit @855fdad77c). Rulings: batches 193, 195, 197, 201, 203, 205; PRD v0.7 rulings 26-29;
Andrew's card 2 (@fec2dc7266).

## HALF -- SIGNED for Groups A, B and V, on the opening condition below -- 2026-10-03 ~08:5xZ

### 1. The blast radius and the rollback (item 1)

- **Writers counted before the rules were read:**
  - `account_return_daily`: 3 writers (the scheduled fire, the backfill, `main --upload`). A2 uses only the backfill. Its
    refusals bound the new manual state: over 25 days, past the newest landed day, accounts neither `population` nor a list,
    and any requested day with no row.
  - `dim_return_method`: 1 writer (`main`). A3 writes `method_version=2/` as NEW keys only; v1 does not move.
  - `platinum/reporting`: 1 function. The series is written before the manifest, and a refused shard raises, so the fan-out
    never half-lands silently.
  - Summaries: 1 pass. A client with no published account gets none, and is counted.
- **Both branches of the method move, read from the producer's rule:**
  - MOVES: an account-day with a margin balance or a short DIV debit. 13 of 14 measured pairs move, by -0.74 to +0.73 pp.
  - UNCHANGED: an account-day with neither. 1 of 14 measured, delta 0.
  - DB-b-19's income move is stated as `inferred` (the 38 debits), not measured in R8. That is accepted, because it moves the
    income field only.
- **IAM:**
  - read gains GetObject and GetObjectVersion on the platinum reporting prefix, plus the one render-grant prefix;
  - publish gains ListBucket on that prefix;
  - no firm fence is edited (batch 205), and the export role gains nothing.
- **The edge:** one pattern inside the render-token branch only, built inside the window, because the shared `portal-auth`
  root publishes whatever its key holds. Its plan must equal 09-25's precedent, or the leg halts.
- **The pins left behind are accepted as named:**
  - `opal_naming.py` and `reporting_policies.json` move together or not at all;
  - `~Y`'s `maintained_sources.py` rides the read artifact, already pinned by its owner;
  - `rebalancer_schemas.py` stays under `0.0.0_AB_MSTR`'s hold.
- **The rollback per key is accepted,** including its honest last step: NEW keys roll back only by delete markers, and that
  needs a human's confirmation at that moment (Agent Autonomy).
  - **The interim state, named:** after the code, policy, gold and 6-account platinum rollbacks, and before any delete is
    confirmed, the NEW manifests still serve each account's method-v2 dashboard on the tab. That is correct data per FWD-8's
    ACCEPT, served on a page whose print and export are back on PATH A.
  - It is a degraded but true state, never wrong numbers, and it ends at the human's delete confirmation or at a re-run of
    the window.

### 2. The opening condition (item 2) -- RULED as the issuer recommends, with two additions

- **The window opens only with Andrew's word for B2 (the portal PROD promote) in hand, in the same session.**
  - B2 is `0.0.0_AB_MSTR`'s push on his word (CLAUDE.md Portal: "`0.0.0_AB_MSTR` pushes trunks on Andrew's word"; PROD is
    gated).
  - Then A1-A10, B1, B2 and B3 run back to back.
  - B3 only after B2 is measured (`merge-base --is-ancestor`, with a positive control).
  - Group A is never served ahead of that word.
- **Addition 1 -- a latest start:** the window opens only if the whole run can finish before the next scheduled trading-day
  fire of the gold, publish or summaries functions. Otherwise it waits for the next fire-free stretch. A half-run window must
  never meet a scheduled fire.
- **Addition 2 -- the B2 failure branch:** if B2 is refused, or fails mid-window, Group A rolls back by section 1's rollback.
  A5 has by then put method v2 on PROD's tab while its print and export are still on PATH A. The rollback starts in the same
  session, and its interim state is section 1's.

### 3. Acceptance (V)

- The P-1 walk on PROD: an account outside the 6 shows the tab, a print and an export, and the receipt names the frozen
  `as_of`.
- `3.0.0_SA_CVO` reads one served FWD-8 pair on method_version 2.
- After A5 is read back, E3 (the ONE Black Diamond population pull) is cut, as Andrew's card 2 orders.

**Not verified by this seat:** the artifacts, the plans, the data counts, the measured pairs.

-- 1.0.0_SA_CTO
