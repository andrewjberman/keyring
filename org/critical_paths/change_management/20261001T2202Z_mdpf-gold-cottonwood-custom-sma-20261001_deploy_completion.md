# Deploy Completion Record
**Date opened:** 2026-10-01T22:02:01.620525+00:00
**Status:** OPEN
**Deploy:** Cottonwood custom models into Models > Custom + Opal SMA sleeves into SMA (Andrew-direct ~20:3xZ/~20:4xZ; serve now ~21:5xZ 'Now. Go now'): mdpf-gold-lambda 0f1a67e196 -> e20899bce7 (zip 05902dbd..), delete-mark the measured set of 2026-09-30 Gold documents, one Gold run, one publisher run. Halves CTO @3338690683 (V2 amended (a), five identities), COO @32c62ba1b9 (condition 1: if the MSTR push uploads build_dim_model_portfolio.py / build_cottonwood_mdpf_pair.py / build_cottonwood_mdpf_slice.py / rebalancer_schemas.py to opal-data-mdpf/code/scripts/, rollback = prior versions assets_gold/build_dim_model_portfolio.py fCOzEWVPFMtPod70YMkVHr0grna40R0y, assets_gold/build_cottonwood_mdpf_pair.py 6M6Vt9o.S28RcOtgYjSWlZeW7vgqaqGT, assets_gold/build_cottonwood_mdpf_slice.py misXby7frL9LITjH7ZwLsyhWwfbu4oS0, silver/rebalancer_schemas.py Df7qDAY2nSu0irFarIl8QIx9cTooMA.8).
**Authored by:** 4.0.0_SA_CRO
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | upload the built zip | downloaded back, sha256 05902dbd.. equal; prior version 5uNyXSXz.. recorded |  | OPEN |
| D1 | activation | saved plan + safe-apply mdpf-pipeline | plan 0/1/0 code + MDPF_GOLD_COMMIT only; CodeSha256 BZAtvS5mfjkkt9zi1zzkGm007DL21qwYsjM9K5XAypA=; re-plan No changes |  | OPEN |
| V1 | verify | deployed qa_local dry run vs the stored 2026-09-30 documents | green 16 of 16; the differing set measured (the delete-mark set) |  | OPEN |
| M1 | activation | delete-mark the measured set (Andrew-direct 215xZ record) | markers recorded, head 404, prior versions intact |  | OPEN |
| G1 | activation | one production Gold run | green; rewritten keys equal the dry run; the CTO's five identities hold |  | OPEN |
| S1 | verify | one publisher run + served read | served Cottonwood Custom/SMA and Global as measured |  | OPEN |

## Log

- 20261001T220201Z OPENED by 4.0.0_SA_CRO with 6 leg(s)
