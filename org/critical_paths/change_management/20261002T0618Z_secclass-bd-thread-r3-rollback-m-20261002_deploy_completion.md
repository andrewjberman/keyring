# Deploy Completion Record
**Date opened:** 2026-10-02T06:18:43.253962+00:00
**Status:** OPEN
**Deploy:** ROLLBACK (NEVER-2) of MDPF_SECCLASS BD_THREAD_R3's served mix producers: C_06, D_03, D_04, lib/etf_classifier.py to their pre-r3 VersionIds (the r3 half's tested rollback branch, restore targets of leg P). Cause: leg B4 failed outside the signed blast radius -- on the 2026-10-02 04:00Z run the 49F firm mix for 09-30 holds 445.7 M of 1,843.1 M in no class line; client mixes drop structured/commodities dollars since 10-01 07:46Z (z08327149: VXX 1.10 M). Escalated to 1.0.0_SA_CTO 06:17Z. E_18, silver, lib/_shared and the SSM document stay (E_18 does not import lib/etf_classifier).
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P | verify | runner stopped; live VersionIds of the four keys equal r3 leg S1's; restore targets equal r3 leg P's | describe-instances + list-object-versions | 06:2xZ: runner i-01003b035d2988dfb stopped (User initiated) after the 04:00Z run (log gold_incremental_2026-10-02_20261002_060640.log, COMPLETE exit 0 06:06:40Z). Live (IsLatest) VersionIds equal r3 leg S1's: C_06 S1.KsOFBBQwftbA95vubbHYa1kFtP.Vn (e84817dc), D_03 7xEAZkTQBL2M1D0AZzgtE4QxtNZhYbVP (705adba8), D_04 fc_AlGdW.mlCI7BXds6ILVS4qwmhyI.1 (ffcdc362), lib/etf_classifier.py SLjBWVc1qu9cN6C8MfzBJkwlV0smZFXW (96ad9dde) -- no deploy since. Restore targets (r3 leg P, the 09-30 18:16Z tested rollback copies): C_06 DF0mrQMYPQUVaROwXfWx_ujZzby33Pd_ (8b1f012c), D_03 yAWDop5v36OOwguqHMJovAMw3ISs1nMv (346e7b0f), D_04 mLh4U.wMEWiVMNO9Ztbsvjubgrk1Z_Qm (a4b867d4), lib yk0qwnF4Dyur2rUn1alS5Nt2_EtsR5Kx (884889c0). Next scheduled fires: 22:10Z silver, 23:00Z gold. | CLOSED 20261002T061921Z |
| C | s3-prefix | copy-object of the prior VersionId onto each of the four keys; head-object ETag equals the restore target's | ETag per key | copy-object 06:19:25Z-06:19:31Z of the prior VersionId onto each key (metadata COPY), opal-data-bd: code/gold/C_06.client_mix_timeseries.py <- DF0mrQ.. new VersionId IHqg0qnURRcAH57.ld35YrbNGJl_JChI ETag 8b1f012c37a0d75d24453b6351290efc 38,469 B; D_03.composition_artifacts.py <- yAWDop.. new w8SLmmCxl089ReuNI_bFgrjFPj.o6Rw5 ETag 346e7b0f6f2279280201e22da728c0b7 38,337 B; D_04.client_portal_summary.py <- mLh4U.. new _WpGGia_LX.yu.zpZna3cvZZQHzMzHkZ ETag a4b867d46cb58f4e252255799c44e383 158,827 B; lib/etf_classifier.py <- yk0qwn.. new 4o.XQapbBNy7l4sIKbKyAZj6tEwM5VOU ETag 884889c0bc1f78cc7b8f91a09d3a39d8 6,605 B. head-object readback: ETag equals the restore target on 4 of 4. The r3 versions stay in history (S1.KsOF.., 7xEAZ.., fc_AlG.., SLjBW..) for a roll-forward. Not touched: E_18, silver builder, lib/_shared (x3), SSM document v5, gold_dispatch.sh. | CLOSED 20261002T062016Z |
| W | verify | served restore: per the CTO's answer either (a) C_06 watermark reset to 2026-09-29 + one ad-hoc downstream chain run, or (b) the 23:00Z scheduled fire; the 09-30 firm mix's class lines sum to its total and z08327149 carries VXX | served keys read |  | OPEN |

## Log

- 20261002T061843Z OPENED by 2.0.0_SA_COO~M with 3 leg(s)
- 20261002T061921Z LEG P closed: 06:2xZ: runner i-01003b035d2988dfb stopped (User initiated) after the 04:00Z run (log gold_incremental_2026-10-02_202610
- 20261002T062016Z LEG C closed: copy-object 06:19:25Z-06:19:31Z of the prior VersionId onto each key (metadata COPY), opal-data-bd: code/gold/C_06.clien
