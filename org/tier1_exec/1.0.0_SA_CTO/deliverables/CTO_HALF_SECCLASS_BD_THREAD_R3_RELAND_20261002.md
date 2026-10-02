# CTO half -- MDPF_SECCLASS: the Black Diamond thread r3 RE-LAND (every class in the mix; the identity read)

Asked by `2.0.0_SA_COO~M`, msg 104222, at @8147b5e4fb. Packet
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_BD_THREAD_R3_RELAND_20261002.md`, blob
`f926b46157` (read at CLOUD and in the worktree, equal). Rulings: batch 117 item 4, batches 144, 155 and 156.

## HALF -- SIGNED 2026-10-02 ~12:1xZ, CONDITIONAL ON LEG P

**Condition:** legs M, G, W, R and S run only after leg P holds. Leg P is the portal reader commit `eb90f2ad` on portal PROD,
which renders commodities, structured, unclassified and cash. PROD today is `b3a1d8a6`, without it. A PROD page that drops a class
would serve a mix that does not sum to 100. The promote is Andrew's act (CLAUDE.md Portal: "DEV only, PROD gated"). This is the
same condition batch 113 put on the Cottonwood re-point.

**The conditions are met as measured on the 09-30 positions:**
- No ticker leaves the mix: there are eight classes, and an unknown reads `unclassified`.
- 49 Financial unclassified is 4.63 pct (86.48 M), at or under 5.0.
- The residual is listed by name (767 names).
- The identity read follows batch 156, unique at every hop and both ways. VUG carries three CUSIPs, so VANGUARD MORNINGSTAR GROWTH
  ETF (35.8 M) is refused (row S14), as the guard intends.

**Named, so the move is not read as a defect:** alternatives fall from 2.11 to 0.01 pct.
- The old library's alternatives were bd-securities labels: "Hedge fund", "Structured Notes", "Commodities" and "Gold".
- The canonical table carries alternatives only for real estate. Those labels now read structured or commodities when a table
  row exists, and unclassified when none does.
- The private funds among them (Cliffwater, AQR TA Delphi, Waldrop DAF) are in the residual by name. The next per-ticker act
  takes the residual in dollar order (batch 139's method).

**Blast radius:**
- The served families are the r3 half's (`gold/views/mix_daily_summary.json`, `gold/artifacts/firm_mix_views*`,
  `platinum/firm/mix_summary.json`, `platinum/clients/{rid}/composition.json`, the advisor and account summaries).
- Writers: one pipeline (C_06, D_03, D_04). The fleet emitter `d06_firm_mix_summary.py` reads the key and does not write it.
- Not moved: the Holdings tab, Cottonwood, Inflection, E_18, the silver builder, `lib/_shared` and SSM v5.

**Both branches:**
- Leg R's QA run reads every class, a sum of 100 and unclassified at or under 5.0 pct; leg S's scheduled fire is read the same
  way, and the ledger closes on it.
- Or a check fails, or a PROD reader drops a class, and the rollback runs in the same window.

**The manual state change is covered:**
- Leg W sets the watermark back one partition.
- The rollback restores both watermark keys to their pre-run versions, beside the five code keys' recorded VersionIds. Nothing
  is deleted.
- The QA run tests the change. The scheduled fire is the acceptance.

**Read by this seat at signing:** branch head `29747a2ecb`, equal to the packet's; the merge base to the head changes exactly 10
files, matching the stop in leg M.

**Not verified by this seat:** the 87 tests, the real run on 09-30, the residual file, the lineage sweep.

-- 1.0.0_SA_CTO
