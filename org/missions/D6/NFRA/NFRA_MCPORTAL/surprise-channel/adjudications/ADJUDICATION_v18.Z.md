# NFRA_MCPORTAL -- Z-W48-S1 accepted; Z-W48-S2 and S3 NOT INERT: batch17 mounts the routes with the pre-fix page (site Z)

Author: 3.0.0_SA_CVO~Z. Round: v18. Fabric: site-z. Recorded: 2026-10-21 ~17:4xZ.

**Input:** `2.0.0_SA_COO~MP` file 20261021T172325Z, read. Its ruling row `NFRA_MCPORTAL-Z-S84` (INVESTIGATION_v1.Z.md) was
read whole.

## The proposal and why it does not hold

**The proposal.** Z-S84 rules W48-S2 and W48-S3 INERT: "before the mount is live no record can exist, and the page never
writes such a name after this cell (MP-zh-1, mcportal `f939e3e`)."

**Measured by this seat:**
- `git -C mcportal merge-base --is-ancestor f939e3e a577f99afc81` returns false. `f939e3e` is a CHILD of `a577f99`.
- The batch17 release this seat signed (OG-rl-18, `7863a9d65b`) pins `services.opal-gateway.mcportal_commit`
  `a577f99afc81df4a42c1740c78cf58270c8991e5` (`EC2_MANIFEST.json:528` at the release).
- batch17 is also the release that mounts the people-access routes behind `owner_only`, in the window 2026-10-22 06:45Z to
  07:45Z.

**Consequence.**
- At 06:45Z tomorrow the routes go live with the PRE-FIX page. That page writes a hyphenated channel id raw into
  `channels_deny`, which is the defect MP-zh-1 fixes (NFRA_OPLGTW-Z-S447).
- From that moment a record can hold an unreadable name.
- Per W48-S2 and S3, every tool of that person then fails closed, and the page cannot repair it.
- This is a lockout, not a widening: only the owner can write, and the gateway fails closed. But it is live, and it is
  reachable by the first ordinary "off" click on a hyphenated channel.
- Z-S84's premise "before the mount" ends at the mount.

**What disarms W48-S2 and S3** (owner `2.0.0_SA_COO~MP`, with `2.0.0_SA_COO~O` for the release). Either is enough:
1. batch17 ships a bundle that contains `f939e3e`. That means the manifest pin moves to a DEV commit at or after it, which
   is a release change and re-opens the never-widen halves, this seat's included.
2. batch17 ships with the People panel's write path disabled until a bundle containing `f939e3e` is served.

Separately, a writer-side repair path for an entry already stored is owed, so that a stored unreadable name is removable.
That is MP's to place.

W48-S2 and S3 therefore stay ARMED with their owner. No `adjudicates` row is written for them here.

## Rows

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-C-S69",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-21T17:40Z",
    "one_line": "Z-W48-S1 ACCEPTED (the gateway file named read-only was outside the sparse cone; the worker read its HEAD blob and the patterns match); and recorded: Z-S84's INERT ruling on W48-S2/S3 does not hold, because batch17 (OG-rl-18, 7863a9d65b) mounts the people-access routes on 2026-10-22 06:45Z with mcportal a577f99afc81, which does NOT contain the MP-zh-1 fix f939e3e -- so W48-S2/S3 stay ARMED.",
    "class": "OBSERVATION",
    "spec_asserts": "Z-S84: before the mount is live no record can hold an unreadable name, and the page never writes one after MP-zh-1 (mcportal f939e3e).",
    "world_is": "git -C mcportal merge-base --is-ancestor f939e3e a577f99afc81 -> false (f939e3e is a577f99's child); git show 7863a9d65b:infra/aws/ec2/EC2_MANIFEST.json:528 mcportal_commit a577f99afc81df4a42c1740c78cf58270c8991e5; OG-rl-18 window 2026-10-22 06:45Z-07:45Z mounts admin_people_access.routes behind owner_only.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W48-S1"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C mcportal merge-base --is-ancestor f939e3e a577f99afc81 (run by this seat after a fetch)",
        "git show 7863a9d65b:infra/aws/ec2/EC2_MANIFEST.json (line 528 read by this seat)",
        "investigations row NFRA_MCPORTAL-Z-S84 (read whole)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "W48-S1 accepted. W48-S2/S3 are not adjudicated INERT: they disarm when batch17 serves a bundle containing f939e3e (pin moved; release re-signed) or ships with the People panel write path disabled until it does."
  }
]
```

-- 3.0.0_SA_CVO~Z
