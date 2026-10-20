# TCKT_VNEXT round 22 -- the fabric's synthetic S3 residue deleted, with a read-back (`2.0.0_SA_COO~V2`, dell2, 2026-10-20)

**Authority:** the CTO's round-21 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_TCKT_VNEXT_ROUND_21_20261020.md` @3517247cfb ("Round 22, one issuance by `2.0.0_SA_COO~V2`: the residue delete with a read-back; D2-S53 stays on Andrew's word only") and his msgs 11428 and 11434 (ONE pass for all fabric-written synthetic residue: this fabric's four Trade objects and `2.0.0_SA_COO~Y2`'s run 4 to run 7b objects; a throwaway role; an exact key and VersionId list). Andrew-direct 2026-10-16: synthetic and test deletes need no open call. **No PRD addendum.**

## Enrichment list and what each item becomes
| # | item | cell | kind | write surface | risk |
|---|---|---|---|---|---|
| 1 | the residue delete with a read-back, one pass, one pair | `R22-dl-1` | RUN (the applier `0.7.0_AE_CloudOps~TV2`), STAGED until the pair is signed and `~Y2`'s run 7b supplement is merged | a throwaway IAM role and its policies (created, used, destroyed); the manifest's exact S3 versions in `opal-data-cottonwood` and `opal-data-irpt` | WORLD |
| 2 | `D2-S53` | none | on Andrew's word only | -- | -- |

## What the cell does
`R22-dl-1`: per the signed never-widen pair `deliverables/2.0.0_SA_COO~V2/R22_DELETE/R22_DELETE_PAIR.md` (the CTO signs his half): Terraform adds a throwaway role allowing only `s3:DeleteObjectVersion` on the manifest's exact object ARNs and version ids, trusted only by `cloudops-dell2-agent-user`; the applier assumes it for 900 seconds, deletes each manifest version, reads each ABSENT (a 404 only), destroys the role, reads it ABSENT, and reads the Deny and a non-manifest control object. The Deny `DenyS3DeletesOnProductionData` is not touched.

## Chains and fan-out
**M = 1 chain:** {`R22-dl-1`}. **Fan-out: 1 of 1 chain, cap 4, reason:** one applier order (it holds the credentials and the Terraform authority a worker does not), no worker.

## Rule 24 record
The run's states: (a version PRESENT / ABSENT before) x (the role present / destroyed) x (the Deny intact / changed) x (a key outside the manifest touched / not): the check admits only (every manifest version ABSENT, no marker left, the role ABSENT, the Deny intact, the control object PRESENT, nothing outside the manifest touched); anything else is a STOP with its own report. A key is deleted by exact bucket, key and VersionId and by no other means (no prefix, no wildcard).
