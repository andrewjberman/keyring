# AMGT_RESAPP -- round 88 remediations (dell1)

<sweep_watermark>2026-10-11T02:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T02:45:00Z. Graduated at ADJUDICATION_v108: 2 rows, both INERT.

```json
[
  {
    "id": "AMGT_RESAPP-S4",
    "project": "AMGT_RESAPP",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The mass-deletion gate's _audit() appends to \"$ROOT/$AUDIT_LOG\" with ROOT = git rev-parse --show-toplevel of the INVOKING tree, so an ATTRIBUTED/BLOCKED verdict written from a linked worktree is lost when the worktree is force-removed after the drain; the commit trailer survives, the audit row does not.",
    "evidence": [
      "investigation row AMGT_RESAPP-S4",
      "3.0.0_SA_CVO read .tools/git-hooks/mass-deletion-check.sh at box/dell1 HEAD: ROOT at :112, _audit() at :160-165, unchanged"
    ],
    "remedy": "The gate writes its audit row to the shared (common-dir) tree, as git-author-override-audit.log does. Close when: a mass deletion committed in a linked worktree leaves its row in the shared tree's org/mass-deletion-audit.log after the worktree is removed",
    "owner": "1.0.0_SA_CTO",
    "round": "v88",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v88"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-S5",
    "project": "AMGT_RESAPP",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "kk-1's guard (refuse to write research_universe ABSENT over a served count) sits only in crosswalk.main; add_security.py's _research_folders_disclosure() (:347-358) is a twin of the swallowing helper (except Exception: return None, None) and its _build_document passes the result into the same write_pool, so the add-security path can still publish ABSENT over a served count. INFERRED: no add-security run was driven.",
    "evidence": [
      "investigation row AMGT_RESAPP-S5",
      "3.0.0_SA_CVO read lib/research/identity/add_security.py:347-358 at box/dell1 HEAD: the swallowing helper is unchanged",
      "lib/research/identity/crosswalk.py:1706-1717: the guard inside main only"
    ],
    "remedy": "Every write_pool caller refuses to write ABSENT over a served count (N = 3 writers named at crosswalk.py:1528). Close when: an add_security run with an unreadable library root exits nonzero with no put, beside a control run that writes",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v88",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v88"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  }
]
```
