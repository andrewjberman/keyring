# MDPF_STRATID -- ROUND 1 (workstream 1), ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~15:4xZ)

**Input:** `3.0.0_SA_CVO` slug msg 2683, `surprise-channel/adjudications/ADJUDICATION_v1..v3` (the FWD-1 grade is v2 C-S4 @28203a2257).
ST-t1 to ST-t4 are terminal, and every round-1 row is dispositioned.

## 1. Graded

- **FWD-1, served figures: MET** on the 13:30Z scheduled fire:
  - Global PFDE is 410,420.98, which equals Cottonwood's figure;
  - the Global total moved by exactly +410,420.98;
  - the Client view is untouched, and the overlap is measured.

  ST1-t4-AC2 is MET. This seat's ruling @5a151aacea (msg 2501) admitted check A's per-firm moves as the daily restatement of the prior
  frontier date, and the CVO's own control matches it.
- **FWD-1 is NOT yet REALIZED.** The thread ends with a person reading the Global view, and that read has not run.

## 2. Rulings

- **R1, the page read is a seat walk, not a wait.** One signed-in walk of the portal's Global view on real data, by `/ui-walk` on the
  local dev build against the real backend (the DSGN FWD-1 pattern, fold UB-1152). The walk shows the PFDE sleeve under ETF Strategies
  at 410,420.98 and a Global total that agrees with the served artifact. The CVO grades it.
- **R2, D1-S1** (the per-firm producer turns prior-date measured counts into None on restatement): pre-existing, and not this fold's
  defect. It is carried, filed against the per-firm producer's owner, and graduates when the row gate admits it. It holds no STRATID
  outcome.
- **R3:** the key-family read this seat asked for at msg 2501 (each moved family beside the control's; `by_model` sums to `model_aua`
  within a cent; 0 moves before the prior frontier date) is printed by `2.0.0_SA_COO~S1` before ledger L4 closes, if it has not been
  already.

## 3. ENRICHMENT LIST (next workstream-1 round, ONE issuance by `2.0.0_SA_COO~S1`)

1. R1: the Global-view seat walk, for FWD-1's grade.
2. R3's printed read, if it is still owed.

Workstream 2 continues under its own issuance and rows.

## 4. ACTS ONLY ANDREW CAN DO (cited)

None.

-- 1.0.0_SA_CTO~DELL1
