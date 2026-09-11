# localhost:5173 login refused 403 -- the origin gate, not the password -- 0.4.0_DT_ClientPlatform

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, IMPLEMENT

**Date:** 2026-09-11
**Task Order:** ad-hoc (Andrew-direct, session open ~05:40Z)
**Status:** COMPLETE -- Andrew's box unblocked; repo-wide remedy RECOMMENDED, NOT APPLIED (see Next Steps 1)
**Window:** 2026-09-11 ~05:40Z -> 06:10Z
**Commits by this seat in window:** ZERO, and that is the finding, not an omission -- the only
behavioural change lands in `portal/.env.local`, which `.gitignore:21` ignores.

---

## Objective

Andrew reported being locked out of `http://localhost:5173` sign-in with a password he knew to be
correct, the UI saying "forbidden". He explicitly stood down the `org/XXX.md` startup protocol for
this and asked for `comp-find` to be used. Find why, and unblock him.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find (content) | `comp-find "portal login authentication forbidden 403 password check" --limit 40` | FAIL | MEASURED ZERO over 166,381 files. Content mode is a REGEX over the corpus, not a semantic/BM25 match -- a plain-English question is searched as a literal phrase and cannot hit. |
| comp-find (content) | `comp-find "['\"]Forbidden['\"]"` equivalent, run as native Grep | PASS (via substitute) | The token search is what found BOTH decisive files. Run on the rail it would have worked; the first call's shape, not the tool, was the defect. |
| native Grep / Glob | Rule-21 exempt surfaces | PASS | Did all the real locating: the 403 emitter, the runbook, the origin-verify module, the vite proxy. |
| curl (live HTTP) | 4 probes, 3 planes | PASS | The DISCRIMINATOR. See Evidence. |
| playwright MCP | navigate + type + network_requests | PASS | The EXERCISED-plane proof; nothing else could show which URL the browser actually posts to. |
| comp-routes | not run | SKIPPED | The HUD advised it when raw `aws apigatewayv2` was denied. Not needed once the live curl triad had already settled the plane; running it would not have changed an act. Rule 22 stop condition. |

**What worked:** the live three-plane curl triad. One fake account posted at three entry points
answered the whole question in a single round, and it is a DIFFERENT instrument from the source read
that formed the hypothesis -- so the two corroborate rather than repeat (Rule 22 DISCRIMINATION).

**What failed:** `comp-find` content mode on a plain-English question. It returned
`0 hit(s) across 166381 file(s)` with a full, honest denominator and four correct "your zero does not
cover" qualifiers -- a textbook well-behaved measured zero that was nonetheless USELESS, because the
query was a sentence and the matcher is a regex. The tool cannot distinguish "this phrase is absent"
from "you asked me the wrong kind of question", and its output reads identically in both cases.
`comp-which` is the documented router for exactly this and I went straight to `comp-find` instead.

**Gap found:** TWO, both in the rail rather than in a comp-tool.

1. **Rule 21's whole-call abort fired live, twice.** A denied `grep -rn` segment and a denied
   `find` segment each aborted the ENTIRE Bash call, silently no-op'ing every later segment in it --
   including a `cat` of the file I was actually after. CLAUDE.md already warns about this; worth
   recording that it cost two round trips in one session, and that the tell is output that simply
   stops rather than any error naming the lost segments.
2. **A wrong-host curl returns `http=000`, which reads like a measurement.** Probing three guessed
   PROD hostnames gave `000/000/000` at exit 6 (DNS failure). Had I not noticed the exit code, three
   zeros would have read as "PROD is down too" and inverted the entire diagnosis. The real alias
   (`opalinvest.dev`) came from `infra/aws/terraform/portal-auth/cloudfront-distribution.tf:110`.
   **`http=000` is NOT a status code; it is the absence of one.**

---

## Work Completed

### 1. Root cause -- an origin gate that runs before the password is ever read

`infra/aws/opalinvest_dev/lambda/auth-handler/src/index.ts:179-182`, landed 2026-09-03 by
`NFRA_OPSEC202609` OP-s-3:

```
if (!originVerified) {
  console.warn(`Origin verification FAILED: ${method} ${path}`);
  return jsonResponse(403, { error: 'Forbidden' }, undefined, origin);
}
```

Its own header comment states the behaviour exactly: *"A request that did not come through CloudFront
is refused here, BEFORE any route runs, even with a real login."* The gate requires header
`x-opal-origin-verify`, injected by CloudFront, constant-time compared against the two-slot
Secrets Manager value `opal/auth/origin-verify`
(`infra/aws/users/lambda/portal-authorizer/originVerify.mjs:111-130`).

The dev browser was posting **direct to API Gateway**, bypassing CloudFront, so it could not carry the
header at all. `portal/src/contexts/AuthContext.tsx:45` falls back to the hardcoded
`https://7k3ed8px20.execute-api.us-east-1.amazonaws.com` whenever `VITE_AUTH_API_URL` is unset -- and
it was unset in BOTH `.env.development` and `.env.local`.

The word Andrew saw is the gate's fixed, deliberately detail-free body rendered verbatim by
`LoginPage.tsx` via `throw new Error(error.error || 'Login failed')`.

**The symptom was pre-documented.** `NFRA_OPSEC202609.TO-OP-S-3.origin-secret-rotation-runbook.md:150`
says: *"Symptoms are unambiguous: `403 {"error":"Forbidden"}` from `/auth/*`"*. The runbook existed
before the lockout did.

### 2. Evidence -- one throwaway account, three planes

Probed with `nobody-probe-0411@example.invalid`, an account that does not exist, specifically so the
measurement added ZERO failed attempts to Andrew's own record and no real credential was ever typed
into an instrument.

| entry point | result | what it proves |
|---|---|---|
| direct to API Gateway (what the browser did) | `403 {"error":"Forbidden"}` | refused PRE-CREDENTIAL |
| direct + deliberately wrong header value | `403` | the gate compares the VALUE, not mere presence |
| through CloudFront (`opalinvest.dev`, PROD) | `401 {"error":"Invalid email or password"}` | reached the credential check |
| through the vite proxy (`localhost:5173`) | `401`, 37-byte body | the proxy ALREADY clears the gate |

**A NONEXISTENT email drawing 403 rather than 401 is the proof the gate is pre-credential.** No
property of Andrew's password can influence a branch that runs before the body is parsed. Andrew's
independently reported "I can sign in just fine on PROD" is the same fact measured from the other
side, and it narrowed nothing -- it confirmed.

The 403-vs-401 split also cleanly rules out the severe reading. The Lambda distinguishes a BROKEN
SECRET (`Origin verification unavailable`) from a WRONG/ABSENT HEADER (`Origin verification FAILED`);
PROD answering 401 proves the secret is readable and the control healthy. This was localhost-only
throughout, never an outage.

### 3. The fix already existed in the repo; only one env line was missing

`portal/vite.config.ts:74-81` already proxies `/auth/*` to CloudFront
(`d2n2nzpeqf34ge.cloudfront.net`), added under D12_PLATFORM_OPS DE3 for this exact reason. Its comment
states the activation condition outright: *"setting `VITE_AUTH_API_URL=` in a local .env reproduces the
production wiring exactly: same-origin request, first-party cookie, real deployed handler."*

So the remedy is one line, and `??` (nullish coalescing) is what makes an EMPTY value work -- `''` is
not nullish, so it defeats the hardcoded fallback instead of re-triggering it.

Applied to `portal/.env.local` (backup `portal/.env.local.bak-20260911`), then restarted the dev
server: PID 32504 was a bare `node node_modules/vite/bin/vite.js`, stopped and relaunched DETACHED via
`Start-Process -WindowStyle Hidden` so it outlives this session rather than dying with it.

**Why not the other two candidate fixes.** Putting the origin secret into a dev env file would place a
production secret on a workstation and make localhost a peer of CloudFront -- which is precisely the
property the control exists to deny, and a change of that class is Andrew's call, not a seat's.
Pointing `VITE_AUTH_API_URL` at `https://opalinvest.dev` directly would clear the gate but break the
session: the refresh cookie is `SameSite=Strict`
(`auth-handler/src/index.ts:103`), so cross-site it would never be sent and `/auth/refresh` would fail
on every reload. The proxy is the only one of the three that is same-origin, secret-free, and
already-built.

### 4. Verification -- EXERCISED plane, not inspection

`import.meta.env` is resolved at RUNTIME in vite dev, so reading the served module showed only the
unsubstituted expression and settled nothing. Confirmed in a real browser instead:

```
network: POST http://localhost:5173/auth/login  ->  [401] Unauthorized
UI alert: "Invalid email or password"
```

The posted URL is `localhost:5173` (proxy, header injected), not `execute-api`; the status is 401, not
403; the rendered string is a credential verdict, not "Forbidden". Gate cleared, credential check
running, fake account correctly rejected. Form left clean by reload.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Probe with a nonexistent throwaway account | Response SHAPE is the whole discriminator; a real credential was unnecessary and would have added failed attempts to Andrew's record while he was already locked out. |
| Fix via the existing vite proxy, not a dev-side secret | Secret-free, same-origin, first-party cookie, and the mechanism was purpose-built for this. A dev-side secret would weaken the control the fix is meant to respect. |
| Write `.env.local`, NOT tracked `.env.development` | Smallest reversible act that unblocks the reporter; a tracked change alters every dev box and was not what was asked. Recorded as Next Step 1 instead. |
| Relaunch the dev server detached | A session-tied child dies with this seat and would re-break his sign-in silently an hour later. |
| Did not run `comp-routes` | The live triad had already settled the plane; Rule 22 -- the next check would not have changed an act. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/.env.local` | +`VITE_AUTH_API_URL=` (empty -> same-origin -> vite proxy -> CloudFront) | **No -- gitignored** (`.gitignore:21`). Device-local by construction. |
| `portal/.env.local.bak-20260911` | Backup of the one-line prior state | No -- gitignored, same rule |
| this log | the record | Yes -- see commit |

No source, infra or Terraform file was touched. Nothing was deployed. The auth Lambda, the secret, the
distribution and `vite.config.ts` are all exactly as found.

---

## Blockers

None blocking the reported problem -- it is fixed and exercised.

One state a reader must not mistake for health: **this seat skipped the `org/XXX.md` startup protocol
at Andrew's explicit direction**, so it is NOT registered on the broker and has NO inbox watcher
armed. It is unreachable to every other seat for the life of this session, and mail addressed to
`0.4.0_DT_ClientPlatform` will sit unread with no bounce and no staleness signal -- the silent-hole
shape CLAUDE.md names under "Queued if not live". Not a defect; a disclosed condition.

---

## Current State

`http://localhost:5173` sign-in WORKS as of 2026-09-11 ~06:04Z, verified in a browser: the login POST
goes same-origin to `localhost:5173/auth/login`, vite proxies it to CloudFront
`d2n2nzpeqf34ge.cloudfront.net`, CloudFront injects `x-opal-origin-verify`, and the auth-handler origin
gate at `infra/aws/opalinvest_dev/lambda/auth-handler/src/index.ts:179` passes, so the request reaches
the real credential check for the first time since 2026-09-03. The enabling change is the single line
`VITE_AUTH_API_URL=` in `portal/.env.local` (GITIGNORED -- it exists only on this workstation, is in no
commit, and will not survive a fresh clone). The dev server is a DETACHED
`node node_modules/vite/bin/vite.js --port 5173` launched from `portal/`, not tied to any agent
session. Andrew should expect the MFA opt-in/challenge step after his password -- that is the designed
D12 DE1/DE2 three-step flow (`LoginPage.tsx:22`), not a fault. PROD was never affected and was measured
healthy mid-diagnosis (401 on a bad credential through `opalinvest.dev`).

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Carry the one-line fix into tracked `portal/.env.development` --
   RECOMMENDED, awaiting Andrew's word.** My fix repaired ONE WORKSTATION. `.env.development` is
   tracked and not ignored, `.env.local` overrides it, and `.env.production` already sets
   `VITE_AUTH_API_URL=` -- so adding that same line to `.env.development` aligns dev with prod, costs
   nothing, and means no other box or fresh clone hits this. Held back only because it changes a shared
   tracked file beyond the scope of "why am I locked out". One line, reversible.
2. **[0.7.0_AE_CloudOps] Note the dev-plane consequence on the OP-s-3 record.** The origin gate is
   working exactly as designed; what it lacked was a documented dev path through it. The runbook
   anticipated the 403 symptom but not the localhost-developer case, and the remedy it points to
   (restore the previous secret value) is the WRONG remedy for this cause -- it would have changed
   nothing here.
3. **[0.4.0_DT_ClientPlatform] Run `/watcher` before taking any fabric-routed work** -- see Blockers.
   Until then this seat is write-only to the fabric.
