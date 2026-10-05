# COO half -- W100-S2 withdrawal of the 49F perfrp account leaf (never-widen)

**Signer:** 2.0.0_SA_COO~P (issuer of IRPT_BCKEND round 50). **Signed on:** packet
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~122/W100S2_WITHDRAWAL_PACKET.json` (drained @a99454d66b), the same
packet the CTO half signed (blob 11a60f2d15, CTO half @4a63c9b600). **Ruling:** 1.0.0_SA_CTO batch 251. **The delete is Andrew's.**

## Blast radius: what the act may touch

- **Exactly one key:** `s3://opal-data-portal-v2/platinum/advi/49financial/perfrp_performance_account.json`. At signing
  (head-object, 2026-10-05 ~02:5xZ), its ETag is `"9873b72ef5da73fc0399d2905d4f7821"`, its version is
  `E78kI4KB4KsZhdwsAFzfSvkI.kn5Snim`, and it was last modified 2026-09-01T03:16:07Z.
- **The act:** a plain `delete-object` with no VersionId. Bucket versioning is Enabled, so this writes a delete marker and the
  version stays.
- **Never touched:** the other three perfrp keys under `platinum/advi/49financial/`; every other key in the bucket; any version;
  the bucket policy, including `AllowAdvisorRouterOAIPlatinumAdvi`; CloudFront EVTSA9VEHNZVH; `shared-advisor-router`; and the
  portal code. The portal call `AdvisorBookView.tsx:479` stays as it is, and its designed 404 shell is the intended state.

## Writers of the property (N = 1, and 1 rule read)

The one writer is `data/assets/scripts/gold/runners_49f/d_publisher_port.py`. Its EMIT set holds `perfrp_performance_account`
(:159), and it publishes only with `--publish` AND `OPAL_ADVI_PUBLISH_GRANT=1` (:524-528). It has two invokers:
1. **The `advi-49f-publisher` EventBridge Scheduler schedule.** The live state read at signing is `DISABLED`, and terraform
   declares `state = "DISABLED"` (`infra/aws/terraform/opal-assets/advi_49f_publisher.tf:78`). It cannot re-publish while disabled.
2. **The `advi-49f-gold-floor` chain** (ENABLED, `chain_49f_entrypoint.py:423-454`). Its `perfrp_projection` stage runs the
   publisher with `--keys` set to the perfrp families and WITHOUT `--publish`, so it stages and never serves.

The leaf's LastModified of 2026-09-01 agrees: no serve write in 34 days. A manual `--publish` run with the grant would re-serve it.
That residual is a human act, outside this sign-off; ADVI_PERFRP's D2 hold governs it.

## Both branches, read from the act's own rule

- **The ETag at act time equals `"9873b72e..."`:** delete. A delete marker becomes current, and head-object answers 404.
- **The ETag differs:** STOP. Nothing is deleted, and the packet returns to the CTO and COO for a fresh read.

## Rollback per key

`aws s3api delete-object --bucket opal-data-portal-v2 --key platinum/advi/49financial/perfrp_performance_account.json --version-id
<the delete marker's VersionId>` removes the marker, and version `E78kI4KB4KsZhdwsAFzfSvkI.kn5Snim` becomes current again,
byte-identical. The same window holds: rollback is in the same session as the act.

## After-read (W121-S1 disarms only on both)

1. head-object returns 404 with the delete marker current (`list-object-versions` shows `IsLatest` on the marker).
2. One 49F login on PROD `https://opalinvest.dev/advisor-intelligence`: the leaf request answers 404 and the page shows its
   designed shell state.

**COO half: SIGNED -- 2.0.0_SA_COO~P, 2026-10-05.**
