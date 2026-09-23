# IRPT P -- current status

Seat `2.0.0_SA_COO~P` (CODEX). Contract `IRPT_MVP_COMPLETION_20260922/CONTRACT.md`
v1.3 at f0fcc4516c. Reviewer `1.0.0_SA_CTO` per Andrew. Sequencing ruling5edf991c06.
As of 2026-09-23T17:09:24.626994+00:00.

## Pins

| What | Value |
|---|---|
| Backend working tree | `C:/Users/AndrewBerman/Desktop/irpt-smoke-p-backend-20260923`, branch same name |
| Backend checkpoint | b639e430d0; measured offline package source e3ad48ca23 |
| P portal candidate | e0531491, `C:/Users/AndrewBerman/Desktop/irpt-smoke-p-portal-20260923` |
| Served frontend | clean3b15871b442906c51a98aff96826f13a67458579, `C:/Users/AndrewBerman/Desktop/portal-local-live-20260923` |
| Current backend artifact | Fresh AWS/downloaded ZIP match: iqLKa1RWk9hlcSlAheuoAMgIY4R3VrStPX1eG5Qwq/s=, 149956 bytes; measured17:07:42Z |
| Push state | LOCAL; no push/deploy this tranche |

## Live thread

NOT LIVE. Fresh user screenshot and three real-browser proxy requests confirm
resolve-scope HTTP200, bearerPresent:true, UNAVAILABLE/UNEXPECTED, no data.
Frontend reachability and normal authenticated transport work; scope does not.
The exact downloaded live Lambda lacks the prepared Global-context and selected
firm authorization code. Served frontend also predates the paired scope repair.
See LIVE_FIRST_HOP_20260923.json and LIVE_FIRST_HOP_REVIEW_20260923.md for exact
artifact hashes, missing commit/path set and compatibility requirements.

Existing localhost5174 PID24768 and sanitized trace remain active through the
CloudFront front door. CTO live tree is unchanged. No browser automation surface
is connected; Andrew supplied the real screen and triggered the real requests.
No credentials copied or synthetic principal sent to live services.

## Acceptance IDs

| ID | State | Evidence |
|---|---|---|
| S1 | OFFLINE ONLY; live bootstrap/browse unproved | Fresh first-hop FAIL; paired source repair absent from served artifacts |
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

CTO direct review of exact paired delta in LIVE_FIRST_HOP_REVIEW_20260923.md.
Resolve local-tree integration and runtime publication route under current hold,
then repeat a normal authenticated request on the reviewed paired artifacts.
Local trace files remain .runtime/live-first-5174.stdout.log / .stderr.log.

## Dependencies

| Needs | Owner | Interface/pin | State |
|---|---|---|---|
| Paired scope repair review and permitted publication route | P / CTO | LIVE_FIRST_HOP_REVIEW_20260923.md | HANDED OFF; CLOUD hold preserved |
| Normal authenticated browser trace | Andrew | existing dev:live5174 | OBSERVED FAIL; do not repeat sign-in prompt |
| M/Y support | M/Y | only measured first-hop dependencies | No additional request needed |

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
