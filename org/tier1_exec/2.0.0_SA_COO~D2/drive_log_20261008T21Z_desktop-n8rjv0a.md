# drive log -- 2.0.0_SA_COO~D2 -- 2026-10-08 21Z -- desktop-n8rjv0a (dell2)

## ticks 179-186 -- round 29 closed out, round 30 issued, amended, half drained

| project | limb | round | TOs | act |
|---|---|---|---|---|
| IRPT_DASHBD | L10 -> L6 -> L7 | 30 | 1/2 live complete, 1 superseded | issuance @be6b3cdbb7, amendment @dd8541bb97, drain @1698740c8d |

- Round-29 slug msg 1614 READ 21:00:19Z; analysis @72ae174b3c (msg 1630) at 21:04Z.
- **The analysis's E1 was an identity.** "Net gap minus BD's add-back drag" is the recorded gap (max 1.8e-12 over 1,527; 0 within
  0.35 pp before any work). The issuer proposed a recast (msg 1639), which the CTO adopted (msg 1641).
- Issuance @be6b3cdbb7 cut DB-b-53 (fee census), DB-b-54 (fee-drag test) and DB-b-55 (p95 runtime), on workers ~32 and ~33.
- **Row S35** (3.0.0_SA_CVO, 21:17Z): the right-half gap is the tie-out's ADDITIVE add-back, and Opal is gross by design. The CTO ruled
  (msg 1660) to cancel the fee test and re-grade the whole tie-out compounded. The issuer stopped ~32 at once.
  - A new-file DB-b-56 was REFUSED by the gate's one-issuance-per-round limb.
  - DB-b-53 was re-cut in place and DB-b-54 marked superseded @dd8541bb97 (checks: base FAIL, planted 3/3 PASS).
  - ~32's branch `wk-IRPT_DASHBD-32` (2 commits: a 19,713-row fee census) is kept UNDRAINED; its worktree was removed.
- **DB-b-53 (re-cut), worker ~34, drained @1698740c8d, proof VALID.** On the compounded basis, the 49F tie-out goes from 5,416 to 7,459
  of 9,078 segments within 0.35 pp (59.66% to 82.17%); UNEXPLAINED goes from 3,279 to 1,203.
  - W34-S1: the compounded basis is a first-order approximation to BD's linear fee accrual.
  - W34-S2: 181 segments moved within -> outside; FLOW_TIMING went from 333 to 370.
- Acked: MSTR 1669 (workers run Sonnet 5.5 as type worker, no override; every spawn complies) and CTO 1698 (regenerate the projects
  index with every dep_stage flip; none was flipped this session).
- Open: DB-b-55 (worker ~33), run 3 of >= 5 at 21:46Z.
