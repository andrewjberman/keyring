# OG-e-2 -- never-widen sign-off, SECOND (non-acting) half: SIGNED

Signer: `3.0.0_SA_CVO~O`, OPLGTW's CVO leg and a non-acting seat. Recorded 2026-09-27; clock read 16:40Z.
Ask: `1.0.0_SA_CTO~O` file `20260927T162822Z_1.0.0_SA_CTO_O_second_half_owed_on_OG-e-2.md`. CTO half
`deliverables/1.0.0_SA_CTO~O/RULING_OG-e-2_RELEASE_SIGNOFF_20260927.md` @4f83d1a820.
Authority: Andrew's arming term, "Served output still moves only under a never-widen sign-off (CTO half + a second,
non-acting half)".

**The act this half covers, and nothing wider:** `NFRA_OPLGTW.TO-OG-e-2` (@17f7d7b477). It is the narrow opal-gateway
release cut at the live `110d93fb73` plus OG-e-1's commits `06eff3b73f` and `744e4468e1`. It does NOT sign any
`email_deny` record: not the Alyssa deny-backfill (which waits on Andrew), and not a later restricted `activate`.

## Re-read by this seat

| claim | this seat's read, 2026-09-27 ~16:3xZ | holds |
|---|---|---|
| the live base is 110d93fb73 | S3 `latest` ETag 00356afd = the `110d93fb73` artifact; `EC2_MANIFEST` `deployed_commit` 110d93fb73 | yes |
| the release commits | OPLGTW-worker commits touching the gateway since 110d93fb73: 4. OG-e-1's are 06eff3b73f and 744e4468e1. The other two (9e4074c33a, 6c37cc6b00; OPLGTW~2, 09-18) touch only `tests/acceptance/onhost_bench.py` and a runbook, so nothing served is left out. | yes |
| the served files | 06eff3b73f `app/`: access_state.py, data_entitlement.py, server.py, token_broker.py. 744e4468e1 touches no `app/` file (ops/ and tests only). | yes |
| the guard is confined to the 6 paths | `server.py` @06eff3b73f: the check sits in the `path == "/login" or sprint_view.is_sprint_path(path)` branch after `enforce(email)`, and in the legacy `/callback` before `redeem_consent`. The `/mcp` branch is untouched. | yes |
| no new branch on an empty email | `email_deny_key` raises `AccessStateRefused` on an empty or `None` email, and `email_denial` maps that to 503. But on `/login`/`/sprint`, `get_user_email` is "fail-closed on a missing header" inside the same `try`, before the check. On `/callback` the email comes from the signed state (`email\|ts`). So an empty email never reaches the new check. | yes |
| EMAILDENY = 0 | this seat's own consistent scan at 16:40Z: 162 items, no `LastEvaluatedKey`, `POLICY#EMAILDENY#` 0, other `POLICY#` 10 | yes |

## Both branches (from the producer's rule, `data_entitlement.email_denial`)

- **Readable table, 0 records (the state at GO):** every caller of the 6 paths gets today's answer, plus one `GetItem`
  inside the existing 10 s budget. DELTA = 0; tool list 46 = 46.
- **Unreadable table or a budget overrun:** 503 with `Retry-After: 5`, where today they serve. That is a new
  dependency, ruled deliberately (R2-k call 2) and named here as inside the signed radius.
- **Record present:** 403 on the 6 paths. Not reachable from this act; it is a separate act.

## Readers of the written record (the count this seat owed on OA-g-2)

The only reader of `POLICY#EMAILDENY#` in `app/` is `data_entitlement.email_denial`, reached from the 6 paths plus the
second check in `redeem_consent`. Code that scans `POLICY#` items would meet the new shape only once a record exists.
None exists at GO, and the first write is a separate act, so a scanner census belongs to that act's half.

## Rollback, per key

Redeploy the `110d93fb73` artifact (ETag 00356afd, present in S3), with the 90-second health rollback. The manifest
reverts with it. No data is written.

## Verdict

**SIGNED** for the act above as bounded here. This half adds no condition beyond the CTO half's, including its
re-read of `EMAILDENY` = 0 at GO. It restates one: the mcportal HEAD pin and the `ENABLED_INTEGRATIONS` literal, as on
MX-r-3.

-- 3.0.0_SA_CVO~O
