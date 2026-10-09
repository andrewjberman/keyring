# NFRA_GATSCP -- round 2 remediations (dell1)

<sweep_watermark>2026-10-09T13:16Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T13:16:00Z. Graduated at ADJUDICATION_v3: 3 rows, all INERT.

```json
[
  {
    "id": "NFRA_GATSCP-D1-S10",
    "project": "NFRA_GATSCP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "FWD-7's first real cross-box order needed three manager hands C-DELIVER does not name: the issuing COO cannot commit the crossbox file it opens, the receiving lane cannot commit its ACK (Z-S1), and the crossbox record (one side's bus_message_id null) plus the channel union HELD box/sitez's integrate until site Z's manager resolved them.",
    "evidence": [
      "investigation rows NFRA_GATSCP-D1-S10, -Z-S1",
      "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/TRACE_round2.md @70a5e67c54 s.2"
    ],
    "remedy": "Name the commit custody of the crossbox file on both ends in C-DELIVER (or admit the issuer and the receiving lane to DEVICES_CROSSBOX for their own record), and give the integrate a resolver for a two-sided crossbox record. Close when: one crossbox order completes with no manager hand",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "NFRA_GATSCP-D1-S7",
    "project": "NFRA_GATSCP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Seven commit-path gates outside C-SCOPE still read the shared working tree or grade beyond the act (commit-gate, to-pipeline-gate, to-decomp-ref-lint, owned-paths, mstr-ledger-check, pipescript-suite, ...), so FWD-6's ACCEPT holds for this project's two gates while the commit path as a whole still reads disk.",
    "evidence": [
      "investigation row NFRA_GATSCP-D1-S7"
    ],
    "remedy": "Rule whether those gates join this project's scope (a round-3 cut) or stay out with the limit stated. Close when: the ruling is recorded",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "NFRA_GATSCP-D1-S12",
    "project": "NFRA_GATSCP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "box-sync.sh line-unions agent-spawn-audit.log and safe-deploy-bypass-audit.log but not org/git-author-override-audit.log, so a box pass is HELD on a content conflict whenever CLOUD carries other boxes' override lines.",
    "evidence": [
      "investigation row NFRA_GATSCP-D1-S12"
    ],
    "remedy": "Add org/git-author-override-audit.log to box-sync's union set. Close when: a box pass with other boxes' override lines reads uptodate",
    "owner": "0.0.0_AB_MSTR~DELL1",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "at": null
    },
    "closed": true
  }
]
```
