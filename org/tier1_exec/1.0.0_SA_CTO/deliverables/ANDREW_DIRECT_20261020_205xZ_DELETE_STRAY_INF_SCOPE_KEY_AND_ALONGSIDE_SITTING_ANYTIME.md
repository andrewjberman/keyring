# ANDREW-DIRECT 2026-10-20 ~20:5xZ: delete the stray Inflection Scope key; the Alongside sitting can be any time

Given at the laptop 1.0.0_SA_CTO terminal, VERBATIM:

> "1.) Yes go ahead. 2.) Can do this any time"
> "I recommend Tiger VNC for the port"

## 1. The delete (his "Yes go ahead")

- **Key:** `s3://opal-data-assets/orion/inflection/bronze/scope_account_returns/date=2026-10-16/scope.json.gz`
- **Version kept:** `bhq7AficP27Nrqtw3I_oyoUIjVfPCwSa` (111,872 bytes, ETag `1f9df807779c3bb212be2ae5576c3653`, written
  2026-10-18T11:58:07Z). It was recorded before the delete.
- **Why:** every inf run of `opal-assets-ingest-mirror` since 2026-10-18 13:05Z raised `ALIEN SURPLUS` on this key.
- **How:** the delete is versioned, so it adds a delete marker and the version stays. Rollback is removing the delete marker, which restores
  the key exactly.
- **What follows:** IRPT_BCKEND re-points the Scope feed to the source bucket `opal-data-inf` (1.0.0_SA_CTO~DELL2, msg 11514). The feed
  stays frozen until then.

## 2. The Alongside sitting

- He can do the sign-in at any time. It is his act, at his choosing.
- **Tool:** he recommends TigerVNC for the port, so the sitting may use a VNC session through the SSM tunnel instead of RDP. That
  is relayed to `2.0.0_SA_COO~SA`, who owns the runbook.

## Done the same turn (read back)

- **The delete marker:** `MpVo_5Whnavm.Ek6x6YCxGmgd5IsauaZ` is now the latest. Version `bhq7AficP27Nrqtw3I_oyoUIjVfPCwSa` is still held.
- **One catch-up run** of `opal-assets-ingest-mirror` with `{"firm":"inf"}`, called synchronously, returned `status: ok`:
  - `orion/inflection`: 9,893 enumerated, 5,056 already landed, 0 missing, `alien_surplus` 0, failed 0.
  - `eclipse/inflection`: 1,928 enumerated, **39 written and verified** (the days held up since 10-18), 0 missing, failed 0.
- **Next:** the scheduled 13:05Z and 17:05Z fires carry on from here.

-- 1.0.0_SA_CTO (laptop)
