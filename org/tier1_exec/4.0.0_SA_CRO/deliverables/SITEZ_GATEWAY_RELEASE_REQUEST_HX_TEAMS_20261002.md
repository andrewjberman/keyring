# Site Z gateway release request -- /hx/teams (Andrew's Teams assistant) + Z-S41

**From:** 4.0.0_SA_CRO (laptop). **To:** the site Z gateway owner (NFRA_OPLGTW, 1.0.0_SA_CTO~O / 2.0.0_SA_COO~O), via
0.0.0_AB_MSTR. **Authority:** Andrew-direct 2026-10-02, record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261002_020xZ_EOD_UPDATE_AUTOMATION.md`.

## The ask

Ship commit **`db92656c72`** (CLOUD) in the next gateway release, and add one `.env` line on the host.

## What it carries

| File | Change |
|---|---|
| `infra/aws/ec2/opal-gateway/app/teams_route.py` | NEW: headless Teams routes on prefix `/hx/teams` |
| `infra/aws/ec2/opal-gateway/app/config.py` | `TEAMS_BEARER`, `TEAMS_BEARER_LABELS` |
| `infra/aws/ec2/opal-gateway/app/server.py` | four Routes registered beside `/hx/mail` |
| `infra/aws/ec2/opal-gateway/app/taxsma_workbook.py` | **Z-S41**: `_OTHER_ROUTE_BEARERS` gains `TRANSCRIPT_BEARER`, `MAIL_BEARER` (and `TEAMS_BEARER`) |
| `infra/aws/ec2/opal-gateway/tests/test_teams_route.py` | NEW: 14 tests |

Routes (own static bearer, MS_INGEST_IDENTITY's server-held token, one Graph allowlist per verb, allow-by-key output,
opaque page tokens, audit without content):

- `GET /hx/teams/me`
- `GET /hx/teams/chats`
- `GET|POST /hx/teams/chats/{chat_id}/messages` (POST = send to a chat)
- `GET|POST /hx/teams/channels/{team_id}/{channel_id}/messages/{message_id}/replies` (POST = reply in a thread)

## Host configuration

```
TEAMS_BEARER=<value of Secrets Manager secret gateway/teams/bearer>
# optional: TEAMS_BEARER_LABELS=teamsassist
```

The secret is created by the laptop's cloud half of this project. Unset `TEAMS_BEARER` leaves `/hx/teams` returning
503 (the gateway boots fine without it). If the ALB has a per-path rule for `/hx/mail/*` and `/hx/transcripts/*`
(no OIDC on the headless prefix), `/hx/teams/*` needs the same treatment.

**Graph scopes:** the routes call `/me/chats`, `/me/chats/{id}/messages`, `/chats/{id}/messages` (POST) and the
channel `/replies` (GET and POST) with MS_INGEST_IDENTITY's delegated token. That token needs Chat.ReadWrite,
ChannelMessage.Read.All and ChannelMessage.Send. The MCP tools already use these scopes through the same app, but
this request does not read the identity's cached grant. A missing scope shows as 502 `graph_status` 403.

## Tests (laptop, Python 3.12, `python -m pytest tests -q --continue-on-collection-errors` in the gateway dir)

- `tests/test_teams_route.py`: **14 passed**.
- Whole suite: **397 passed, 3 failed, 1 skipped, 15 errors**. Baseline on the untouched tree: 383 passed, with
  the same 3 failed and 15 errors. The failure set is IDENTICAL before and after, by diff. The 15 errors are
  `ModuleNotFoundError: moto` (not installed on the laptop). The 3 failures were already there:
  - `test_portal_grant.py::test_asker_portal_scope_admits_granted_channel`
  - `test_portal_grant.py::test_asker_portal_scope_refuses_other_channel`
  - `test_schwab_export_stream.py::test_ogx4_ac03`

## sha256 at db92656c72 (git blob bytes, LF)

```
f470540078a23b8a874e0bebd2fa67cad7e23a82c1aa513c6f904e012ae87337  app/teams_route.py
3128d463bd6f5e424bff5c2729501802acad848d08eb5aa351452b308e36bc2a  app/config.py
2a34bd9fe175c68de2f89590dc9595d769a5737fb68a47afe39fb928996516d1  app/server.py
56d4f49017e4c17f721c8613e57195cfe341b7b6e0e1f96bc3524999a65f83a7  app/taxsma_workbook.py
d7632f564353c9a93f7d008650c1d87fb05863fd121f13b0ec8236e9b2d31d79  tests/test_teams_route.py
```

**Push state:** LOCAL on the laptop at the time of writing. 0.0.0_AB_MSTR pushes the trunk.

## Z-S41 closing hash

`db92656c72`. That's the hash relay 103997 asked to have posted to 0.0.0_AB_MSTR.
