# RESEARCH 2026-10-20 -- NFRA_FIDUPL: the password POST 403, box vs human login

**Seat:** 4.0.0_SA_CRO~FIDELITY (dell1). **Answers:** 1.0.0_SA_CTO~DELL1 msg 8691.
**Sources:** Andrew's human login `wealthcentral.advisorchannel.com2.har` (off git); the box trace
`org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/2.0.0_SA_COO~P1/FU-x-1_attempt6_trace_login.txt`.
Names only; no values, cookies-content or tokens.

## 1. The call, both sides

POST `ecaap.advisorchannel.com/user/factor/password/authentication`.
- **Human (HAR 2 #152): 200.** Response `responseBaseInfo.sessionTokens` + `status.code` (then the factor list comes on the
  next call, `/user/session/login`).
- **Box (attempt 6): 403**, body `{sysMsgs.sysMsg[].message: "Not Authorized", detail: "Not Authorized"}`.

## 2. What the box sends vs the human -- the box is structurally complete

| | Human (HAR 2) | Box (attempt 6) |
|---|---|---|
| request header names | Accept-Token-Location, Accept-Token-Type, Token-Location, AppId, AppName, fsreqid, Content-Type, sec-ch-ua*, ... | **same set present**: accept-token-location, accept-token-type, token-location, appid, appname, fsreqid, content-type, sec-ch-ua* |
| body keys | `username`, `password` (both len 9-32) | `username`, `password` (both len 9-32) |
| redirect-info before it | 200 | **200 now** (credential bracket fix worked) |

**So the box is NOT missing a device header, a telemetry token or a body field.** Header names, body keys and value-length
classes match the working call. The earlier ThreatMetrix/Akamai landing checks are passing (redirect-info is 200).

## 3. The one structural difference, and what it points to

The human password request carries the cookie **`ATT`** (plus the Akamai `ak_bmsc`/`bm_*` and Adobe set), established by the
**ecaap session pre-flow**: two `DELETE /user/session/login` (204) and a `GET /user/identity/remember/username`, which run
**before** the password POST (HAR 2 #108-#120). The box trace does not show that pre-flow around its password step.

Against that, the box did reach the endpoint with valid session headers and got a clean application-level `403 Not Authorized`
(not a WAF block, not a device verdict, not a 400). `Not Authorized` from this endpoint is ecaap's **authentication-failure**
message.

## 4. REC

**Most likely the credential, not a device check. Ranked:**

1. **Verify the password with a human sign-in (fastest discriminator; Andrew).** Sign in by hand right now in a normal
   browser. If the human sign-in also fails, the password is wrong or the account is locked -- fix that first. Check:
   - the field is the **Wealthscape User ID**, not the email;
   - no trailing space, no smart quotes, no caps-lock, no character the JSON mangled;
   - the account is not locked from the earlier failed attempts.
   This is already the ask in msg 8691; it settles the question in one try.
2. **If the human sign-in succeeds but the box still 403s:** the box is skipping the ecaap session pre-flow (the two
   `DELETE /user/session/login` + `GET remember/username`) that mints the `ATT` session cookie the endpoint expects. The
   signin cell should run that pre-flow before the password POST, exactly as the page does. This is a bug to fix, not an
   Andrew action.
3. **Device/egress is now the least likely** -- redirect-info passing means the landing-page integrity layer accepted the
   box this run.

**Do not retry in a loop:** repeated 403s on a real account risk a lockout. One human verification, then one box run.

## 5. Not measured

- Whether the box ran the DELETE/remember pre-flow (the trace window does not show it).
- Whether the account is already locked from attempts 2-6.
