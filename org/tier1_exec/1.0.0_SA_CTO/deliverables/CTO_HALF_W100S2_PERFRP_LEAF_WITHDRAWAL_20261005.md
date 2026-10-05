# CTO half -- W100-S2 withdrawal of the 49F perfrp account leaf (IRPT_BCKEND.TO-IB-pr-319)

Author `1.0.0_SA_CTO`, 2026-10-05 ~02:4xZ. Never-widen half (CLAUDE.md NEVER-1), on `2.0.0_SA_COO~P` msg 105098 and CTO batch 251
(@8ea5889048).

**Packet read:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~122/W100S2_WITHDRAWAL_PACKET.md`, blob
`11a60f2d15c2575223df2ade7ef8b0ba7122f67c`. Disk and HEAD were equal at signing; the blob was committed @3187d58a92 and drained @a99454d66b.

## What this half covers

**The act:** one `delete-object` (no version id) on `s3://opal-data-portal-v2/platinum/advi/49financial/perfrp_performance_account.json`.
- Versioning is Enabled, so the act writes a delete marker and destroys no bytes.
- **Before-read stop:** the act stops if the current ETag is not `9873b72ef5da73fc0399d2905d4f7821`, or the current VersionId is not
  `E78kI4KB4KsZhdwsAFzfSvkI.kn5Snim`.
- **Rollback (one key):** delete the marker by its version id, which restores version `E78kI4KB4KsZhdwsAFzfSvkI.kn5Snim` as current.
  No byte copy is written.
- **Blast radius:** the one key. Never the other three perfrp keys (`perfrp_book_advisor`, `perfrp_gainloss_account`,
  `perfrp_gainloss_relationship`), `_manifests/`, any other firm or bucket, the bucket policy, versioning, logging, CloudFront, the
  router or the portal.

**Writers counted: 1.** `data/assets/scripts/gold/runners_49f/d_publisher_port.py` writes all four perfrp keys. This seat read its
two rules:
- **The scheduled path:** `infra/aws/terraform/opal-assets/advi_49f_publisher.tf:2-20,75-87` keeps the publisher schedule INERT
  (DISABLED).
- **The chain:** `chain_49f_entrypoint.py:423-432` runs the perfrp projection as "BUILD ONLY -- and that is a structural property".
- The key's LastModified is 2026-09-01T03:16:07Z, 33 days with no re-emit.

**Both branches:**
- **(a) No manual publisher run:** the route answers 404, and the page renders its designed shell (`AdvisorBookView.tsx:459-464`).
- **(b) A manual run of `d_publisher_port.py`:** the key returns as a new version. That is outside this act's write set and is ADVI_PERFRP's
  hold to keep. The after-read below sees it as a 200, and row W121-S1 then stays ARMED.

**After-read (owed by `~P`):**
- `head-object` returns 404 with the delete marker current;
- one 49F login on PROD `/advisor-intelligence`: the leaf request answers 404 and the page shows the shell, read rather than inferred.
- Only then does W121-S1 disarm.

**The inflated day:** the leaf holds window returns, with 0 literal hits for 2025-01-10, and its since-inception window spans that
date. It is withdrawn by batch 251's ruling by name; whether the values embed the inflated day is row W122-S1's question and does not
change this act.

## SIGNED

CTO half SIGNED for the one-key withdrawal above, on packet blob `11a60f2d15`.

Still owed before the act:
- the COO half, by `2.0.0_SA_COO~P`; the packet carries no COO line;
- Andrew's word on the delete (CLAUDE.md Agent Autonomy, "S3 deletes"; batch 247).

-- 1.0.0_SA_CTO
