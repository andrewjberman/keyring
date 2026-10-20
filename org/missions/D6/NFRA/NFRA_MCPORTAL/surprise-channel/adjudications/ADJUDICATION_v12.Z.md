# NFRA_MCPORTAL -- OGW round 1 L9: six worker rows adjudicated (site Z)

Author: 3.0.0_SA_CVO~Z. Round: v12. Fabric: site-z. Recorded: 2026-10-20 ~23:2xZ.

**Input:** `2.0.0_SA_COO~MP` FERRY packet `deliverables/2.0.0_SA_COO~MP/ogw/OGW_R1_CLOSE_PACKET_20261020.md`, commit b2eb47cb58,
read whole.
- OGW round 1 has no judgment criterion.
- The issuer's cited commits were read: `6debfb2b2e` (zo-3 AMENDMENT 1), `55b33623db1` and `979787698da` (the drains), and
  `2e6385a297` (z-6 AMENDMENT 1).
- `mcportal` origin/DEV `src/api/admin.ts:582-592` handles 409 as a REFUSED verdict body, which is Z-S52's cure.

**Verdicts, one row each below:**
- Z-W43-S1 and Z-W42-S2 are DISARMED.
- Z-W42-S1 and Z-W42-S3 are ACCEPTED.
- Z-W28-S1, Z-W32-S1 and Z-W16-S2 are DISARMED, the last with its residue owned by `0.0.0_AB_MSTR` as the naming gate's
  owner.

**Two points for the record:**
1. **The writer's widening refusal (zo-3) is behind the owner gate** once NFRA_OPLGTW mounts it. That is the W1' reading
   this seat signed in PRD v0.10 @314290bab3: only the owner's confirm counts. The mount's never-widen ask must state
   that the routes are wrapped by `owner_only`, not by a master_admin tier check.
2. **Nothing in OGW round 1 is served-proven.** FWD-23 to FWD-29 are not REALIZED, and the close run waits on batch17.

## Rows

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-C-S50",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-20T23:20Z",
    "one_line": "Z-W43-S1 (BLOCKING) DISARMED: the zo-3 face asked for a WIDENING judged against the prior record and a WIDEN-NO-CONFIRM refusal with zero store calls, which cannot both hold; AMENDMENT 1 (6debfb2b2e) moved the refusal to after the one strong read and before any write, and zo3.AC1 then passed 5 of 5 (drain 55b33623db1).",
    "class": "OBSERVATION",
    "spec_asserts": "A BLOCKING row is dispositioned before the round's L10 slug; the issuer's disarm row Z-S76 names AMENDMENT 1 as the cure.",
    "world_is": "6debfb2b2e (2.0.0_SA_COO~MP): MP-zo-3 AMENDMENT 1 after worker ~43's row Z-W43-S1; drain 55b33623db1 merges wk-NFRA_MCPORTAL-43; packet section 1 records zo3.AC1.sh PASS, 5 of 5, 40 passed 0 failed, re-run by the issuer.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W43-S1"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git log -n1 6debfb2b2e and 55b33623db1 (read by this seat)",
        "deliverables/2.0.0_SA_COO~MP/ogw/OGW_R1_CLOSE_PACKET_20261020.md sections 1 and 3 (read whole)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarmed by the issuer's amendment; the contradiction was the order text's, not the worker's, and the rebuilt refusal passes its named tests."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S51",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-20T23:20Z",
    "one_line": "Z-W42-S2 (ARMED) DISARMED for OGW round 1: a plain Read of a one-file order hands the worker the RECORD FACE; harmless here because OGW round 1 carries no judgment criterion, so no grading text reached a worker that could self-grade; the line-range prompt is a mitigation, not a mechanism.",
    "class": "OBSERVATION",
    "spec_asserts": "CLAUDE.md rule 27 L7: the TO's WORKER FACE is the worker's whole context; the RECORD FACE never travels.",
    "world_is": "The zo-1 order file holds both faces; a Read returned both. round-close-check reads judgment 0 for OGW round 1, so the record face carried no judgment criterion. The issuer's mitigation names the line range in the worker prompt (Z-S76).",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W42-S2"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/2.0.0_SA_COO~MP/ogw/OGW_R1_CLOSE_PACKET_20261020.md section 3 (read whole)",
        "investigations rows Z-W42-S2 and Z-S76 (read by this seat)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "No harm in a round with no judgment criterion. Not dismissed as a class: a round that carries a judgment criterion must hand the worker a face-only extract (a file or a tool cut at the marker), not a line-range instruction; enrichment for the issuer's next cut."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S52",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-20T23:20Z",
    "one_line": "Z-W42-S1 (helper module shadowed by a case-insensitive filesystem) and Z-W42-S3 (the audit list reads /api/admin/changes through its own checked reader because getRecentChanges types entries without an action) ACCEPTED as observations; neither is a hazard.",
    "class": "OBSERVATION",
    "spec_asserts": "Observation rows are dispositioned at L9.",
    "world_is": "Z-S76 rules both accepted; the packet states the audit list shows only the four access actions and labels an empty who/when unattributed.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W42-S1",
      "NFRA_MCPORTAL-Z-W42-S3"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations rows Z-W42-S1, Z-W42-S3, Z-S76 (read by this seat)",
        "deliverables/2.0.0_SA_COO~MP/ogw/OGW_R1_CLOSE_PACKET_20261020.md section 2 (read whole)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Accepted. Bound on S3: an audit entry with no action field is not shown at all rather than labelled unattributed; the served store-direct arm of the close run must show what an outside writer's entry looks like before FWD-28 grades."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S53",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-20T23:20Z",
    "one_line": "Z-W28-S1 (ARMED in the rollup) DISARMED: the REFUSED verdict's status is now stated (409, the verdict as the body) and the client reads it, so a refused write shows its reason and detail.",
    "class": "OBSERVATION",
    "spec_asserts": "MP-pd-4: a REFUSED verdict reaches the page with its reason and detail.",
    "world_is": "mcportal origin/DEV src/api/admin.ts:582-592 at f90f03a: 'The gateway answers a WRITTEN verdict with 200 and a REFUSED verdict with 409, the verdict object as the body'; the client branches on response.status === 409. Issuer row Z-S52 records the same.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W28-S1"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C mcportal grep 409 origin/DEV -- src/api/admin.ts (read by this seat)",
        "investigations rows Z-W28-S1 and Z-S52"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarmed by the code at DEV."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S54",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-20T23:20Z",
    "one_line": "Z-W32-S1 (ARMED in the rollup) DISARMED: the style authority absent from the worker's sparse worktree was read at DEV by the issuer and the page was rendered and looked at; the one break (browser-blue links) was fixed.",
    "class": "OBSERVATION",
    "spec_asserts": "MP-pe-2 names portal/DESIGN.md as the style authority for the new page.",
    "world_is": "Issuer row Z-S54 records the DEV read, the render and the link-colour fix.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W32-S1"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations rows Z-W32-S1 and Z-S54 (read by this seat)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarmed on the issuer's render. Bound: this seat did not view the render; the colour law is re-read at the close run's served screenshot."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S55",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-20T23:20Z",
    "one_line": "Z-W16-S2 (ARMED in the rollup) DISARMED for NFRA_MCPORTAL: the commit-time naming gate printed NAMING ERROR in a sparse worktree and the commit still landed rc=0; the project's commit was not harmed, and the residue (an error that does not refuse) is the naming gate's owner's, 0.0.0_AB_MSTR.",
    "class": "OBSERVATION",
    "spec_asserts": "CLAUDE.md rule 30: the commit-time naming gate REFUSES names today (LGIC_ENFORCE).",
    "world_is": "Z-W16-S2: NAMING ERROR (function-map folder missing) printed, commit landed rc=0 in the sparse worktree. Issuer row Z-S75 disarms it for the project and carries the residue to 0.0.0_AB_MSTR.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W16-S2"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations rows Z-W16-S2 and Z-S75 (read by this seat)",
        "GW_R1_CLOSE_PACKET_20261019.md section 4 (the residue carried to 0.0.0_AB_MSTR)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarmed for this project. The gate's fail-open on a missing input is a fabric defect owned by 0.0.0_AB_MSTR: a gate that prints ERROR and exits 0 reads PASS to every caller."
  }
]
```

-- 3.0.0_SA_CVO~Z
