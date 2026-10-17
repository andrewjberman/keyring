# TCKT_EARLYWARN -- surprise channel, INVESTIGATION v1 (round 1, dell1 fabric)

**Opened by:** `0.7.0_AE_CloudOps~TM1` at TO-EWS-d1 (the order names this file as its channel).
**Id grammar:** a seat's row on the main index is `TCKT_EARLYWARN-D1-S<k>` (the row gate refuses a `W` for a committer that is not a worker). The order text says `TCKT_EARLYWARN-Z-W1-S<k>`; the schema reserves the `Z-` infix for fabric `site-z` and this project's fabric is `dell1`, so `D1-` is used, as in TCKT_MTADTA.
**Append-only.** Never edit an existing row.

```json
[
  {
    "id": "TCKT_EARLYWARN-D1-S1",
    "project": "TCKT_EARLYWARN",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~TM1",
    "surfaced_at": "2026-10-17T04:58:00Z",
    "one_line": "The one container cannot run its default BRIDGE mode on the cert-only secret scope: HttpTransport raises bearer_not_configured without a gateway bearer, and no bearer secret exists in Secrets Manager.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disarm_owner": "n/a (INERT: nothing is deployed; the apply is held until the grant is named)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/client-ops-early-warning/ews/bridge.py bearer_value(): env EWS_MAIL_BEARER, else Secrets Manager id EWS_MAIL_BEARER_SECRET_ID, else empty; HttpTransport.__init__ raises BridgeUnavailable(0, 'bearer_not_configured') on empty",
        "ews/config.py: EWS_MODE defaults to BRIDGE; BRIDGE_BEARER_SECRET_ID defaults to the empty string; GRAPH_APPONLY refuses until the Day 0 Test-ApplicationAccessPolicy read (README, record addendum 4)",
        "aws secretsmanager list-secrets --filters Key=name,Values=opal/ews read 2026-10-17T04:5xZ: exactly one secret, opal/ews/graph-app-cert (denominator 1)",
        "TO-EWS-d1 requirement 3: GetSecretValue on opal/ews/graph-app-cert ONLY; if the deploy needs the BRIDGE bearer, STOP and file a BLOCKING row naming the missing grant"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Deploy the runtime as one always-on container in the default BRIDGE mode with secretsmanager:GetSecretValue on opal/ews/graph-app-cert only, and the task reads RUNNING.",
    "world_is": "In BRIDGE mode the poller cannot construct its transport without a gateway bearer. No bearer secret exists, so the grant the runtime needs (secretsmanager:GetSecretValue on a bearer secret id, plus the EWS_MAIL_BEARER_SECRET_ID value) names a resource that has not been created or chosen. A container started without it exits on its first build_poller call, so a RUNNING read would be a crash loop or a launcher that swallows the refusal; neither is a deployed runtime.",
    "notes": "MISSING GRANT, named: secretsmanager:GetSecretValue on the BRIDGE bearer secret (id not yet chosen; the code reads it from EWS_MAIL_BEARER_SECRET_ID). Needed from the issuer: (a) the secret id and who mints the bearer value (a headless token for the gateway /hx/mail/messages route on Andrew's mailbox, record addendum 4), (b) a ruling that the role's secret scope widens from one secret to two, or that the bearer comes in as a task-definition secret injected by ECS (which needs the execution role, not the task role, to hold the grant). Unblocked work continues meanwhile: registry rows, the Dockerfile, the terraform module and a plan with no apply."
  },
  {
    "id": "TCKT_EARLYWARN-D1-S2",
    "project": "TCKT_EARLYWARN",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~TM1",
    "surfaced_at": "2026-10-17T04:58:30Z",
    "one_line": "The ews package has no runnable entry point (no __main__, no console script), and the order's grant forbids editing ews/ source.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "n/a (INERT: the Dockerfile carries the launcher inline)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "grep for __main__ and def main over infra/aws/ec2/client-ops-early-warning/ews/*.py: only ews/replay.py main(pkg_dir) matches, and it is the replay, not the poller",
        "ews/bridge.py build_poller(store, mode=None, **kw) and ews/poller.py BasePoller.loop(iterations=None) are the library seam; HttpTransport(base_url, bearer) and SqliteStore(path) are the parts a launcher composes"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The entry point is the poller loop, ews/poller.py / ews/bridge.py build_poller().",
    "world_is": "build_poller() returns a poller; nothing in the package constructs the store, the transport and calls loop(). The Dockerfile CMD therefore has to compose them inline (SqliteStore on the container filesystem, HttpTransport, loop()), without touching ews/. The store is SQLite on ephemeral task storage, so a task restart loses open items; the watermark is re-derived from EWS_INITIAL_CUTOFF.",
    "notes": "Not blocking. Persistence beyond the task's life is not in the order (no S3 write, no table in the role), so the open-items store is ephemeral by the order's own constraints."
  }
]
```
