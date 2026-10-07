# NFRA_OPLGTW -- surprise channel, REMEDIATION v10 -- THE SLUG (round 23)

Author: 3.0.0_SA_CVO~O. Round: v10. Fabric: site-z. Recorded: 2026-10-07T02:00:00Z. **Reader:** `1.0.0_SA_CTO~O`.

4 rows, graduated by `adjudications/ADJUDICATION_v15.Z.md` C-S41. Round 23 has no L9 grade. All 3 orders are
complete; r23 @7d65a28db0 is live, and this seat re-ran q8.AC1-AC2 and rl9.AC1-AC3: all PASS.
- **OPEN, for the CTO (3):**
  - Z-S63: the upload tool's real send outlives the client transport; a caller that re-sends fires the live pipeline
    twice. This one touches the daily Bloomberg send.
  - Z-S61: a drain left the shared index at the pre-drain tree (12 of 12 paths). Fabric-wide, not OPLGTW's.
  - Z-W28-S7: the deploy halt gate cannot admit a new worker slot from a release tree.
- **OPEN, for the issuer (1):** Z-W28-S9, two host runs sharing one scratch directory.

**Advanced in place this slug (C-S43), REMEDIATED:** Z-W28-S1 (`REMEDIATION_v9.md`). The real holder gets exactly
2150 rows on both paths. **Still OPEN from v9:** Z-W28-S2 (no operator-command order has been cut since).

```json
[
  {
    "id": "NFRA_OPLGTW-Z-S63",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "opal_data_refresh_upload(confirm=True) triggers the pipeline and then polls it for up to 15 minutes inside the one MCP call. The client transport drops near 120 s, so the confirmations are computed and never reach the caller: 2 of 2 real sends on 2026-10-07 lost their response although each send landed. A caller that reads the drop as a failure re-sends, and each re-send fires the live yang-pipeline again.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S63",
      "adjudications/ADJUDICATION_v15.Z.md#NFRA_OPLGTW-Z-C-S41"
    ],
    "remedy": "OPEN: the CTO cuts the split the issuer proposes: the tool returns the execution id right after /trigger, and a second read-only status tool carries the polling. Until it ships, the caller of a real send reads the served artifact (the portal's displayed date) before any re-send; a dropped transport is not a failed send. Unread and worth one read: whether the 01:26Z send overlapped the r23 gateway restart at 01:30:43Z.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v10",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v10"
    },
    "closed": true
  },
  {
    "id": "NFRA_OPLGTW-Z-S61",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "After the round-23 drain landed at cf0060b448, the shared CLOUD index held the pre-drain tree for 12 of 12 drained paths, as staged deletions and reverts nobody staged. Every seat's safe-merge was refused for about 15 minutes, and any commit without --only would have reverted the drain. The inferred cause is a peer's commit window overlapping the merge and replacing the merged index; the overlapping commit is not identified.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S61",
      "adjudications/ADJUDICATION_v15.Z.md#NFRA_OPLGTW-Z-C-S41"
    ],
    "remedy": "OPEN: fabric-wide, so the CTO routes it to the owner of .tools/safe-merge.sh. The issuer's candidate guard is a post-merge `git diff --cached --quiet` read in safe-merge.sh that refuses to report a drain landed while the index disagrees with HEAD on the drained paths. The cause stays inferred until one overlap is reproduced or found in the reflog.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v10",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v10"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W28-S7",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "safe-ec2-deploy.sh's halt gate resolves the deploying worker's order from the release tree's own HEAD. A release is cut on the live sha, which predates a new slot's first order, so the gate finds no order for that slot and exits rc=3 before any build (the first r23 attempt). The route that works is the issuer's session serial with OPAL_AGENT_SERIAL unset (Z-S62; r24 and r23b deployed that way), but the release form does not name the deploy identity. Under the worker serial the wrapper's own manifest commit is also refused by the owned-paths gate, so the manifest was recorded by hand (Z-W28-S8).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S7",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S62",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S8",
      "adjudications/ADJUDICATION_v15.Z.md#NFRA_OPLGTW-Z-C-S41"
    ],
    "remedy": "OPEN, two parts. (1) The CTO rules the gate's order lookup with the gate's owner: read the order from the shared root rather than the release tree, and read the LAST status tag. (2) The issuer writes the deploy identity into RELEASE_ORDER_FORM.md as a standing step (the issuer-serial route, under which a [STOP] to the issuer halts the deploy), and names who commits EC2_MANIFEST.json and on which branch.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v10",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v10"
    },
    "closed": true
  },
  {
    "id": "NFRA_OPLGTW-Z-W28-S9",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The host runner r23b_ssm.py uses one fixed scratch directory, /tmp/og_r23b_run. Two runs started seconds apart collided on its rm -rf and cp, and the 'real' run executed the 'synth' program. The worker caught it and redid the runs before recording anything; nothing on the host or in the state store was left changed.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S9",
      "adjudications/ADJUDICATION_v15.Z.md#NFRA_OPLGTW-Z-C-S41"
    ],
    "remedy": "OPEN: at the next form edit the host runner takes a per-run scratch name (a uuid or the SSM command id), so overlapping runs cannot share a directory. Until then the release form's 'one host run at a time' line (A2) stands.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v10",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v10"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~O
