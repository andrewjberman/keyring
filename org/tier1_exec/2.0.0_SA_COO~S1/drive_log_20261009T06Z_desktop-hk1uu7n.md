# /canonical-drive MDPF_STRATID -- 2.0.0_SA_COO~S1, hour 2026-10-09T06Z

- 2026-10-09T06:06Z drain-read TO-W2-1 A7 | ~4 @8ef4e5be15: W21-LIST-OK, W21-LOADERS-OK (issuer re-run), proof VALID; Muni rule = Opal_Muni_Sleeve only
- 2026-10-09T06:06Z tick 16 | MDPF_STRATID | A7 on ~6 in flight; ~4 done | merges held (W1) | no act owed
- 2026-10-09T06:08Z drain-read TO-W2-3 A7 | ~6 @614bf6e1a8: 4 of 4 checks OK (issuer re-run), proof VALID; LISTED 3 (Opal_Muni_Sleeve + 2 ETF holding names); Opal_Muni_Income excluded as Custom. W2: all 5 cells + A7 pass on branches; drain waits on 13:30Z read
- 2026-10-09T06:16Z tick 17 | MDPF_STRATID | EMPTY -> next-calls --drive: 0 calls, 0 FREE (W2 5/5 + A7 pass on branches; drain and FWD-1 read both gated on the 13:30Z scheduled fire)
- 2026-10-09T06:27Z tick 18 | MDPF_STRATID | EMPTY -> next-calls --drive 0 FREE; gated on 13:30Z fire
- 2026-10-09T06:37Z tick 19 | MDPF_STRATID | THIRD-EMPTY-TICK -> /unblock opened (second case): single remaining block is the 13:30Z scheduled fire
- 2026-10-09T06:47Z tick 20 | MDPF_STRATID | UB-0bc9 at CRO; next-calls --drive 0 FREE
