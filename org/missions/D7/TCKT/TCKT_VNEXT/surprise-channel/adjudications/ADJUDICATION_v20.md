# TCKT_VNEXT: CVO read, round 22 (the residue delete pass; no judgment criterion)

<sweep_watermark>2026-10-21T02:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL2, 2026-10-21.

Read by `3.0.0_SA_CVO~DELL2` (dell2), 2026-10-21T02:20Z. Input:
`org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R22_RESIDUE_DELETE.md`, blob 636253505108 (msg 11750; verified by `git hash-object`).
Round 22 carries no judgment criterion: `R22DL1-AC1` and `R22PL1-AC1` are mechanical. This file records the live spot-check this seat ran
on a production-data delete, as the cost of being wrong warrants.

## What this seat read live, 2026-10-21 ~02:1xZ

- **The deleted versions.** `deleted.json` lists 42 entries. A sample of four was taken: the first entry, which was deleted alone, plus
  three random with seed 7. For each, `s3api list-object-versions --bucket opal-data-irpt --prefix <exact key>` gives **0 versions and 0
  delete markers**.
  - A HEAD at the deleted VersionId answers 400, which is S3's response for a version that is gone. It was not used as the instrument.
  - Control: `list-objects-v2` on the sibling prefix of the first key returns 2 objects, so the listing sees objects where they exist.
- **The throwaway roles.** `iam get-role opal-ticket-residue-delete-{0..3}-role` gives NoSuchEntity for all four.
- **The Deny.** `cloudops-dell-agent-deploy-policy`, at its default version, still carries `DenyS3DeletesOnProductionData` (1 match).

## Reading

The pass did what its signed pair says, and this seat's sample agrees with the issuer's full check:
- 42 exact versions, no marker left;
- the roles created and destroyed;
- the Deny untouched.

The disclosed whole-root `plan -destroy` was a plan only. It was never applied, and the root plans `No changes` (PL1).

**Stays:** the four 31-byte `opal-data-cottonwood` trade-form objects.
- That bucket's policy denies deletes to all but a break-glass role (STOP 2), so removing them needs that role or a bucket-policy act.
- That decision is the CTO's row 3ffe, correctly placed with Andrew this time. The obstacle is the bucket fence, not the synthetic-delete
  word.
- Later residue (runs 7e and 7f, and `~Y2`'s FWD-9 and Multi-Comp objects) is a separate pass needing its own pair.

```json
[
  {
    "id": "TCKT_VNEXT-D2-C-S18",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "3.0.0_SA_CVO~DELL2",
    "surfaced_at": "2026-10-21T02:20Z",
    "one_line": "Round 22 read: the 42-version opal-data-irpt residue delete is confirmed by a live sample (4 of 42 keys: 0 versions, 0 markers), the throwaway roles are absent and the deploy-policy Deny is intact; 4 cottonwood objects stay behind the bucket fence (row 3ffe).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-R22-DL1's pair: 42 exact versions deleted with no marker left, roles destroyed, the Deny untouched.",
    "world_is": "Sampled keys (first entry plus 3 random) list 0 versions and 0 delete markers in opal-data-irpt; opal-ticket-residue-delete-0..3-role NoSuchEntity; DenyS3DeletesOnProductionData present in cloudops-dell-agent-deploy-policy's default version.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R22_RESIDUE_DELETE.md blob 636253505108 (msg 11750)",
        "org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r22_delete/deleted.json",
        "live: s3api list-object-versions (4 keys), iam get-role (4 roles), iam get-policy-version (deploy policy)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A verification read; no defect found."
  }
]
```

-- `3.0.0_SA_CVO~DELL2`
