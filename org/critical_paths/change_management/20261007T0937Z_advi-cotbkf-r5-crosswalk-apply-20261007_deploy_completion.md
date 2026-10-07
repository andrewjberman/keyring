# Deploy Completion Record
**Date opened:** 2026-10-07T09:37:45.339196+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261007T093903Z
**Deploy:** ADVI_COTBKF round 5 E5: the round-4 crosswalk applied over round 3's (opal-data-assets/commonwealth/cottonwood/silver/crosswalk/date=2026-06-23/, 2 objects, rollback pins fN2T8jb... / Jd8TqUf...)
**Authored by:** 2.0.0_SA_COO~C2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | silver crosswalk 2 objects replaced | head-object VersionIds moved off the pins + read back 1533 rows, 439 MATCHED, near_matches_applied=0 | applied 09:38:06Z rc 0 by 2.0.0_SA_COO~C2 from dell2 (CLOUD @b9411881a0 code): crosswalk.parquet VersionId fN2T8jb... -> fatOX6x0HfXRV_O7TKPNmuGBrL5wuoG1 (141,226 B), crosswalk.csv Jd8TqUf... -> RGQHH1zievrDXGUvGO.S9TDdQCNk8faA (692,831 B); independent boto3 read-back of crosswalk.parquet: rows=1533 matched=439 not_matched=1094 accounts_unique=1533; run line near_matches_applied=0 near_matches=21; branch A | CLOSED 20261007T093903Z |

## Log

- 20261007T093745Z OPENED by 2.0.0_SA_COO~C2 with 1 leg(s)
- 20261007T093903Z LEG L1 closed: applied 09:38:06Z rc 0 by 2.0.0_SA_COO~C2 from dell2 (CLOUD @b9411881a0 code): crosswalk.parquet VersionId fN2T8jb... ->
- 20261007T093903Z CLOSED -- all 1 legs proven
