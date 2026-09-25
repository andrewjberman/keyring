# NFRA_MCPORTAL -- surprise channel, INVESTIGATION v1 (site-Z fabric)

**Home:** the project tree's channel. Lane `ANY`; `.tools/surprise-row-gate.py` validates every NEW
row (schema, identity, coordinate, folder == project). **Append-only.**

**Id grammar on this fabric:** a seat's row is `NFRA_MCPORTAL-Z-S<k>`; a worker's row is
`NFRA_MCPORTAL-Z-W<n>-S<k>` with `<n>` its slot; `<k>` restarts at 1 per coordinate.
`"project": "NFRA_MCPORTAL"` and `"fabric": "site-z"` on every new row. The CVO's adjudication rows
live in `adjudications/`, never here.

---

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-W2-S1",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~2",
    "surfaced_at": "2026-09-24T22:00Z",
    "one_line": "GET /api/admin/changes as the TO names it (no tid/oid) has no unscoped read path in the existing store; implemented tid/oid-scoped instead.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "NFRA_MCPORTAL.TO-MP-t-4.grant-handlers.md s.1: 'GET /api/admin/changes: the writer's audit records, newest first, each with before and after' -- no tid/oid named on this route, unlike the two grant routes above it.",
        "infra/aws/ec2/opal-gateway/app/access_state.py@a2b89be579: operator_audit records are stored at POLICY#<tid>#<oid> (policy_key), and AccessState.query(pk, sk_prefix) reads ONE partition -- there is no cross-tenant scan or index this module's existing read path exposes.",
        "app/admin_grants.py@17b7e01c0f: get_changes() requires tid and oid as query parameters and 400s without them, citing this gap in its own error message."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "GET /api/admin/changes lists the writer's audit records, newest first, each with before and after -- stated with no tid/oid, unlike the narrow/widen/grant routes' explicit {tid}/{oid} path segments.",
    "world_is": "The only read this box can make against the existing store (access_state.query) takes one partition key; operator_audit records are partitioned per principal (POLICY#<tid>#<oid>). No global/cross-tenant audit feed exists without a new index, which is outside this cell's <paths> (app/access_state.py is read-only here). Implemented as a tid/oid-scoped GET with required query parameters; AC1's test_changes_newest_first exercises this scoped shape.",
    "notes": "No repair attempted per BOUNDS #2 (never widen a criterion or meet it by a route the face does not name); the mechanical criterion (AC1) is unaffected since it grades this cell's own test file, which exercises the scoped design. A true global feed is a build decision for whichever cell owns access_state.py's read surface."
  }
]
```
