# Deploy Completion Record
**Date opened:** 2026-10-09T02:14:25.908645+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / the first COT gold run after the 2026-10-09 02:14:55Z ship of cot C_06 (ea7e6700): cron(30 10 * * ? *) -> 2026-10-09 10:30Z; legs V and D CLOSED; leg G = 0 multi_asset over all opal-data-cot platinum/clients/*/concentration.json and gold/entities/clients/*.json (denominator printed), CTO condition 3 @ca7b0da512; log logs/cot-exporter/gold-run/cot-gold-run-20261009-*.log polled. (held since 2026-10-09T07:26:16.849203+00:00)
**Deploy:** MDPF_SECCLASS SC-e-67: deploy data/cot/scripts/gold/C_06.client_mix_timeseries.py ALONE to s3://opal-data-cot/code/gold/ (retired multi_asset reclass of stored concentration history + new-row guard), before the 2026-10-09 10:30Z COT gold fire. Code rollback VersionId M.bUto2CRQ9XPSkdUiF_3wd3nlXsQdEM (ETag 75135f33). Data rollback VersionIds (versioning Enabled): platinum/clients/z09305621/concentration.json DfXq4SeTor5mGg0gJrW9PT3Yaz7WzcpC, z09305679 m1m21YA9LMlmYvL_ErUL_PwxyrwIc2fk; gold/entities/clients/z09305621.json hNsqK58x7zkQq6TG.rWEBUFGPtERTT0h, z09305679 RJHXuBYNWMwd.Q5QmNB9aYknftljm5.E; gold/client_timeseries/z09305621.json m83maHzEWKuJXqbD6tGLcSm63s0scw3U, z09305679 2SZIBskTbVpR3cDVgo1me82kL72Zc04Z. Halves: COO SIGNED @202af6d413, CTO SIGNED @ca7b0da512 (conditions 1-4).
**Authored by:** 2.0.0_SA_COO~M1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V | verify | versioning Enabled; the six data VersionIds and the code VersionId recorded before the ship (CTO cond 1) | the reads | 2026-10-09 ~02:2xZ, 2.0.0_SA_COO~M1: get-bucket-versioning opal-data-cot -> Enabled (read ~02:1xZ); head-object of the six data keys recorded in the title (re-read ~02:1xZ, LastModified 2026-10-08T11:35-11:36Z); code key code/gold/C_06.client_mix_timeseries.py ETag 75135f33950396de58f9f439b8ac66c3 VersionId M.bUto2CRQ9XPSkdUiF_3wd3nlXsQdEM; pre-ship watch values E_18 8e302500ba4645dcf89fa40d7b01bfd5 (YbfGw1.3...), _shared etf_classification_scheduled.py 3f1e6be8910952f33c88bf100c610ab6 (0e4OsubY...). | CLOSED 20261009T021440Z |
| D | s3-prefix | cot C_06 served equals repo ea7e6700; E_18 (8e302500) and lib/_shared/etf_classification_scheduled.py (3f1e6be8) unchanged after the ship (CTO cond 2) | safe-deploy VERIFY line + head-object ETags | 2026-10-09 02:14:55Z, 2.0.0_SA_COO~M1: safe-deploy.sh data/cot/scripts/gold/C_06.client_mix_timeseries.py -> 'DEPLOYED [cot] data/cot/scripts/gold/C_06.client_mix_timeseries.py' + 'VERIFY OK comp-pipescript deployed ...C_06...'; the three _shared modules printed '[not shipped] ... NOT named by this deploy'. head-object after the ship: C_06 ETag ea7e6700509611a1866701f4f8e0984e (= repo md5) VersionId fwzHY6gQsOHL7QSFWBsIXv_fvEMqwrfk; E_18 8e302500... VersionId YbfGw1.3... LastModified 2026-06-17 (UNCHANGED); _shared etf_classification_scheduled.py 3f1e6be8... VersionId 0e4OsubY... 2026-10-07 (UNCHANGED); tests/test_d04_no_multi_asset.py 404 (not shipped). CTO condition 2 met: no STOP. Seat-gate WARN printed (mode WARN): APPLY-WHO REFUSED kind=COO, crossbox open_deploy=hit (this ledger). | CLOSED 20261009T021535Z |
| G | verify | after the 2026-10-09 10:30Z COT fire: 0 multi_asset over all platinum/clients/*/concentration.json and gold/entities/clients/*.json, denominator printed (CTO cond 3); other holdings in the two files unchanged | scan output |  | OPEN |

## Log

- 20261009T021425Z OPENED by 2.0.0_SA_COO~M1 with 3 leg(s)
- 20261009T021440Z LEG V closed: 2026-10-09 ~02:2xZ, 2.0.0_SA_COO~M1: get-bucket-versioning opal-data-cot -> Enabled (read ~02:1xZ); head-object of the s
- 20261009T021535Z LEG D closed: 2026-10-09 02:14:55Z, 2.0.0_SA_COO~M1: safe-deploy.sh data/cot/scripts/gold/C_06.client_mix_timeseries.py -> 'DEPLOYED [
- 20261009T072616Z HELD-SOVEREIGN-GATED gate=external/the first COT gold run after the 2026-10-09 02:14:55Z ship of cot C_06 (ea7e6700
