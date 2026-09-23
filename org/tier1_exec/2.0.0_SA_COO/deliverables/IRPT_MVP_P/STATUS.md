# IRPT P -- current status

Seat `2.0.0_SA_COO~P` (CODEX). Contract `IRPT_MVP_COMPLETION_20260922/CONTRACT.md`
v1.3 at f0fcc4516c. Reviewer `1.0.0_SA_CTO` per Andrew. Sequencing ruling5edf991c06.
As of 2026-09-23T17:00:27.432447+00:00.

## Pins

| What | Value |
|---|---|
| Backend working tree | `C:/Users/AndrewBerman/Desktop/irpt-smoke-p-backend-20260923`, branch same name |
| Backend checkpoint | b639e430d0; measured offline package source e3ad48ca23 |
| P portal candidate | e0531491, `C:/Users/AndrewBerman/Desktop/irpt-smoke-p-portal-20260923` |
| Served frontend | clean3b15871b442906c51a98aff96826f13a67458579, `C:/Users/AndrewBerman/Desktop/portal-local-live-20260923` |
| Current backend artifact | NOT freshly measured; historical live directory digest iqLKa1RWk9hlcSlAheuoAMgIY4R3VrStPX1eG5Qwq/s= is not a current verification |
| Push state | LOCAL; no push/deploy this tranche |

## Live thread

NOT LIVE / authenticated trace pending. First measured failure was no localhost5174
listener and connection refusal. Restored existing committed `scripts/dev-live.mjs`
with `--port 5174`, PID24768, host localhost. HTTP GET / now200 text/html with
Vite client and src/main.tsx. This proves only frontend reachability.

Real auth/data retain the existing CloudFront front door and normal login/MFA.
No browser surface is connected to this Codex session (`cua.getState` empty;
`cua.getBrowser` reports unavailable). Andrew has been asked to sign in normally
and open IRPT so the existing sanitized proxy trace can capture the failing hop.
No credentials copied and no synthetic principal sent to a live service.

The served tree remains fac3b6a0 plus dev launcher/diagnostics, not P's e0531491
Opal scope candidate. It is clean and has not been edited. Prior CTO trace
LOCAL_LIVE_PARTNER_SCOPE_20260923.md reports authenticated resolve HTTP200,
ok:false/UNAVAILABLE/UNEXPECTED; this is historical, not a new observed response.
Current served backend revision and authenticated response remain unmeasured.

## Acceptance IDs

| ID | State | Evidence |
|---|---|---|
| S1 | OFFLINE ONLY; live bootstrap/browse unproved | P e0531491; current first-hop trace pending |
| S2 | OFFLINE ONLY; source admission unproved | M200ba442f5, CTO155213fedf bounded package review |
| S3 | OFFLINE ONLY; live product acceptance unproved | Existing committed lane artifacts preserved |
| S4 | OFFLINE ONLY; live product acceptance unproved | Existing committed lane artifacts preserved |
| S5 | OFFLINE ONLY; live product acceptance unproved | Y10627906f2, review36131adb48 |
| S6 | OFFLINE ONLY; live product acceptance unproved | Existing committed lane artifacts preserved |
| S7 | OFFLINE ONLY; live product acceptance unproved | Existing committed lane artifacts preserved |

Offline passes close no acceptance ID before the live thread is established.

## Write claims

Current: P STATUS and exact first-hop trace evidence. Existing live-scope exception
covers P repairs in owned portal/backend worktrees. Do not edit CTO's live tree.
Parked draft `verify_packaged_custody.py` is unexecuted and not wired into any
checker, source map or deployed artifact.

## Next proof

Fresh authenticated localhost5174 resolve request through CloudFront: record
sanitized request route/status/envelope structure and exact frontend/backend
revisions; locate and repair the first failing boundary before deeper custody work.
Local trace files: `.runtime/live-first-5174.stdout.log` / `.stderr.log`.

## Dependencies

| Needs | Owner | Interface/pin | State |
|---|---|---|---|
| Normal authenticated browser trace | Andrew/current browser connection | existing dev:live5174 | AWAITED; no connected browser in Codex |
| Current server artifact identity and concrete runtime delta if required | P / CTO | current auth/scope/bootstrap | NOT YET MEASURED |
| M/Y support | M/Y | only measured first-hop dependencies | AVAILABLE; no general source review requested |

## Parked

| Question | Owner | Un-parks when |
|---|---|---|
| Actual M reader/naming closure missing from78-member ZIP | P, preserve M source | first hop live or trace proves necessary; finding155213fedf |
| Checker provenance mismatch and invalid-owner refusal mislabeled absent-source | P | same; preserve review155213fedf and unexecuted draft |
| Actual economic/source receipts and admission | M/P/Y | first hop live or a concrete required dependency |
| General naming/registry/storage work | existing owners | measured first-hop necessity or later sequencing |

## Limits

Latest offline evidence b639e430d0: exact36-source/78-member parity accepted by CTO,
Linux construction and source-level actual M/P/Y17tests pass; packaged M path is
OPEN. These remain bounded offline results. Source-byte correction5ea4441702
is retained. No new source capability, runtime attachment, provisioning,
vendor egress, cloud write, promotion or live acceptance is claimed.
