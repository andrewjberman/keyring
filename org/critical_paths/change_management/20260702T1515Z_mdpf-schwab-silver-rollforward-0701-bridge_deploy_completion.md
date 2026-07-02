# Deploy Completion Record
**Date opened:** 2026-07-02T15:15:22.441637+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260702T151547Z
**Deploy:** MDPF Schwab-silver 07-01 ONE-OFF BRIDGE (validation prefix -> prod, Andrew GO Option A; N=5 repoint hold INTACT)
**Authored by:** 0.6.2_AE_PartnerETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | Promote 11 CRS20260701.* validation->prod 01_raw/ (SSE AES256) + RPS->bronze/rps/ | S3-verified 11 files + rps mirror | prod 01_raw/ has 11 CRS20260701.* (ACC/RPS/TRN/ULN/ULT/RLD/SEC/TCF/TCFX/UPN/UPT) + bronze/rps/CRS20260701.RPS=79365491B; server-side copy SSE AES256 @15:04Z | CLOSED 20260702T151546Z |
| L2 | verify | Convert + S3-verify all 6 silver tables date=20260701 non-zero (acc/rps/trn/trn_nna/uln/rld) | converter rc=0 + parquet sizes non-zero | opal-data-bd/schwab/silver/{acc,rps,trn,trn_nna,uln,rld}/date=20260701/data.parquet all non-zero: acc 429002 / rps 1514336 / trn 439789 / trn_nna 12273 / uln 13598934 / rld 912513 B; converters rc=0 ERR=0 | CLOSED 20260702T151547Z |
| L3 | verify | CVO gate-1 byte/schema/scope parity PASS + independent served-silver verify | CVO RAVC PASS | CVO independent verify 151237Z: rps 91387 rows/5913 accts custody $1,604,173,986.44 (DoD -0.24% sane); gate-1 byte-parity PASS (CRS20260629 all 11 ext identical, box SI2==OneDrive SI2); N=5 hold INTACT (--src-dir avoided OneDrive write) | CLOSED 20260702T151547Z |

## Log

- 20260702T151522Z OPENED by 0.6.2_AE_PartnerETL with 3 leg(s)
- 20260702T151546Z LEG L1 closed: prod 01_raw/ has 11 CRS20260701.* (ACC/RPS/TRN/ULN/ULT/RLD/SEC/TCF/TCFX/UPN/UPT) + bronze/rps/CRS20260701.RPS=79365491B;
- 20260702T151547Z LEG L2 closed: opal-data-bd/schwab/silver/{acc,rps,trn,trn_nna,uln,rld}/date=20260701/data.parquet all non-zero: acc 429002 / rps 15143
- 20260702T151547Z LEG L3 closed: CVO independent verify 151237Z: rps 91387 rows/5913 accts custody $1,604,173,986.44 (DoD -0.24% sane); gate-1 byte-parit
- 20260702T151547Z CLOSED -- all 3 legs proven
