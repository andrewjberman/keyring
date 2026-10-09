# Deploy Completion Record
**Date opened:** 2026-10-09T11:31:48.516106+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T114606Z
**Deploy:** AMGT_RESAPP round 84 AMGT-ii-3: re-cut and re-analyze BABA, SAP, PBR in English (BABA first, gated), dell1
**Authored by:** 0.9.0_WK_AMGT_RESAPP~336
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | BABA_US_Equity silver part + analysis + drafting rewritten, or rolled back; AC1 AC2 YES; four-prefix diff | new VersionIds or rollback proof, diff | BABA landed, AC1 YES AC2 YES (10 business locations of 20, 32 of 40 English-marked): fetch 11:33:50Z parser 2.0.0 language en items business,risk,mdna, silver part-20261009T113350Z VersionId AXl3_0eUuLX1VZulZuzDoPKAea54DkMd; analysis BphBd7FPGSJwYDMh6n5CgKs3GY_FbvYk (prior yIcDOS4H), drafting 1qNTUIXdb4c7AxTjIL2jeWdIVpwMgmjY (prior qUdrTs_2); 2 model calls USD 0.7092 tokens in 78020 out 12763; 40 sentences 0 dropped; no splice markers on prior draft; four-prefix diff added 3 removed 0 outside 0 (diff_BABA_US_Equity.txt) | CLOSED 20261009T113738Z |
| L2 | verify | SAP_GY_Equity silver part + analysis + drafting rewritten, or rolled back or skipped; four-prefix diff | new VersionIds or rollback proof, diff | SAP landed (not rolled back): AC1 YES; AC2 T1 T2 PASS (9 business locations of 20), T3 reads 76% against the 80% floor (26 of 34) because 8 served sentences are English numeric sentences with no ' the/and/of' (listed, all English), AC2 SAP NO as the unedited check reads: fetch 11:37:54Z parser 2.0.0 language en items business,risk,mdna, silver part-20261009T113754Z VersionId .RxdBd0RPdSpzwAh5zDtnI.F4Yi82p7U; analysis AWd0Tnoq3G8ZH4eirVrw8cfKKqrUwash (prior rmP1ek8s), drafting PN03Mcrkm.OvgvMjGD1Va1xp5WLYNNiw (prior qb9GzRTF); 2 model calls USD 0.6854 tokens in 71557 out 13103; 40 sentences 2 dropped; no splice markers on prior draft; four-prefix diff added 4 removed 0 outside 0 (the BABA part is a sibling write on the shared silver prefix) (diff_SAP_GY_Equity.txt); see row | CLOSED 20261009T114120Z |
| L3 | verify | PBR_US_Equity silver part + analysis + drafting rewritten, or rolled back or skipped; four-prefix diff | new VersionIds or rollback proof, diff | PBR landed: AC1 YES AC2 YES (14 business locations of 28, 36 of 40 English-marked, 90%): fetch 11:41:34Z parser 2.0.0 language en items business,risk,mdna, silver part-20261009T114134Z VersionId PNP_dM7xylmc2pEpwiAc6jMMVtl3.Vtx; analysis 6XsHBjI_r0qQ23ZqyNvQiam.pmdzv2Vw (prior olR02tlq), drafting udNXabeQDGrI2lWggAed7LQkh.HbopbJ (prior ZmdJB1hR); 2 model calls USD 0.6616 tokens in 70593 out 12346; 40 sentences 0 dropped; no splice markers on prior draft; four-prefix diff added 5 removed 0 outside 0 (diff_PBR_US_Equity.txt) | CLOSED 20261009T114428Z |

## Log

- 20261009T113148Z OPENED by 0.9.0_WK_AMGT_RESAPP~336 with 3 leg(s)
- 20261009T113738Z LEG L1 closed: BABA landed, AC1 YES AC2 YES (10 business locations of 20, 32 of 40 English-marked): fetch 11:33:50Z parser 2.0.0 langua
- 20261009T114120Z LEG L2 closed: SAP landed (not rolled back): AC1 YES; AC2 T1 T2 PASS (9 business locations of 20), T3 reads 76% against the 80% floor (
- 20261009T114428Z LEG L3 closed: PBR landed: AC1 YES AC2 YES (14 business locations of 28, 36 of 40 English-marked, 90%): fetch 11:41:34Z parser 2.0.0 la
- 20261009T114606Z CLOSED -- all 3 legs proven
