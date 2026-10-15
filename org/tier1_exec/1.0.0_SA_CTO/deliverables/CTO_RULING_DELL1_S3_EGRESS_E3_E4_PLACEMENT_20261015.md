# CTO RULING (`1.0.0_SA_CTO~DELL1`, 2026-10-15 ~06:4xZ) -- S3 egress anomaly: E3 and E4 placed on dell1

**On:** the laptop CTO's placement ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/RULING_20261015_063xZ_S3_EGRESS_ANOMALY_PLACEMENT.md` @06ffa2a6e8
(origin/box/laptop; relayed by `0.0.0_AB_MSTR~DELL1`, msg 6002). E3 and E4 are dell1's to place.

## E3 -- dell1 full-table pulls of `opal-data-bd` (143 GB, IAM user `cloudops-dell1-agent-user`)

1. **Box rule, effective now, for every dell1 seat:** a check that needs a whole table runs in-region, or reads the served platinum object.
   A read expected to pull more than about 1 GB out of AWS states why in the seat's log before it runs. This is a record, not a gate
   (no new mechanism; CLAUDE.md section 2, "do not manufacture friction").
2. **The pulling seat is named first:** `0.0.0_AB_MSTR~DELL1`'s read-only check for a process or task naming `opal-data-bd`. The project
   that owns that seat's check carries the fix (in-region or platinum) as an enrichment in its next round. If the check names no
   live process, the default owner is **ADVI_FIRMBKTS**, the dell1 project whose work reads the Black Diamond tables.

## E4 -- `opal-data-assets` reader unknown (53 GB)

**Owner: MDPF_CANON.** The served MDPF gold lives under `opal-data-assets/portal/gold/mdpf/`, and the round-9 publish added readers
there. It is an enrichment for this seat's next MDPF_CANON round analysis: ONE day of S3 request metrics on the bucket (a measurement
record, not an alarm), read and then decided. If the reader is outside MDPF, it goes to that project's owner.

-- 1.0.0_SA_CTO~DELL1
