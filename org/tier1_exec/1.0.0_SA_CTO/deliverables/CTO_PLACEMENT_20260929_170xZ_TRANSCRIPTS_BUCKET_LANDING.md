# CTO PLACEMENT -- landing the opal-data-transcripts bucket (answers 4.0.0_SA_CRO~T msg 102919)

**Order:** Andrew-direct 2026-09-29, `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260929_19xxZ_TRANSCRIPTS_HOME_S3_BUCKET_OPAL_DATA_TRANSCRIPTS.md`
@`1862bff7b4`. **Handoff:** branch `cro-t-transcripts` @`7e31cce92f`,
`org/tier1_exec/4.0.0_SA_CRO/deliverables/TRANSCRIPTS_BUCKET_20260929/HANDOFF.md`.

## Lanes, read from `.owned-paths.yaml`

- `infra/logic/registry/**`: PLATFORM_LOGIC_DOCS. It permits `4.0.0_SA_CRO` and ~A-~D, not ~T.
- `infra/aws/**`: CLOUD_OPS_OR_ETL. It permits "any AE agent", `0.7.0_AE_CloudOps` first. No AE seat is live on
  this box (liveness 16:5xZ: 10 registrations, 0 AE).
- The restamped generated targets span the IRPT_BCKEND lanes of ~P and ~M.

## Placement

1. **Step 1: the registry rows plus all 12 regenerated targets in ONE commit, by `0.0.0_AB_MSTR` as integrator.** It is a
   cross-lane mechanical commit, with the author override audited. The GAP: right after the ledger
   `irpt-adapter-holdings-gold-49f-r3-20260929` closes D1, and before `2.0.0_SA_COO~M` cuts the packet for the
   directory bundle / Holdings re-mint (AD-10 step 3, TO-IB-m22-222).
   - The 49F r3 artifact TBy0pL is already built and signed, so a restamp before its apply would only make its
     source-map census drift by a comment line. After the apply it is harmless.
   - ~M's bundle packet is not cut yet. Cut after the restamp, it censuses the restamped bytes and pins nothing stale.
2. **Steps 2-3: the Terraform root at `infra/aws/terraform/transcripts/main.tf`, then the ledger entry, safe-apply,
   a 0-diff re-plan, and the `bucket_provisioned` flip.** Owner: `0.7.0_AE_CloudOps`, spawned by this seat. The
   flip is a second restamp. It lands in the same kind of gap and is named to ~P and ~M before it lands.
3. **Step 4: the reader principal for opalbloomberg@opalinvest.com.** It stays with `4.0.0_SA_CRO~T` to establish. The
   bucket serves Andrew's one IAM user until then; no reader is guessed.

## Why

Creating a bucket is reversible and Andrew ordered it. The only live hazard is the restamp moving blob hashes that
signed IRPT packets pin, so the gap is placed between the one signed build in flight and the next packet.
