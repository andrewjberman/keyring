# DEPLOY LEDGER — portal DEV->PROD promote v2.1.174 (D12 MFA fix + laptop perfrp edges)

| | |
|---|---|
| **Opened** | 2026-09-01T06:45Z (retro-opened at completion — the Andrew-direct arrived mid-session and the open was missed at start; recorded rather than omitted) |
| **State** | CLOSED -- COMPLETE 2026-09-01T07:02Z |
| **Executing seat** | `1.0.0_SA_CTO~Z` under /prod-deploy Step-0 Andrew-direct exemption (non-DT) |
| **Push legs** | `0.0.0_AB_MSTR~Z` (site-Z integrator, LD-0367) |
| **Authorization** | Andrew-direct at the CTO~Z terminal: "I think all of this needs to be pushed" + `/prod-deploy` invoked; passenger scope ruled verbatim "All of its good , go" on the explicit 7-commit list; corroborated by bus-relayed "laptop fabric has performance reporting edges to push, i want all of it pushed" |

## What landed

| Field | Value |
|---|---|
| origin/DEV | `be39451b` -> `89ecfd8947e2d8d8e8c1e3e3e6c24af97dc45768` (Leg 1, ls-remote measured) |
| origin/PROD | `fc3a4421` -> `529f3093d35efdcbc5d4172aba7bf0c1a7856f88` (Leg 2, ls-remote measured) |
| Rollback base | `fc3a4421715a4252471accc6e85cecca54c6e9a2` (encoded in merge message) |
| Parity gate | `git diff origin/DEV HEAD` EMPTY — PROD tree == DEV tree |
| CI | run 33479722920 "Deploy to Production", conclusion=SUCCESS; ALL workflows on the sha enumerated (denominator 1) |
| Tag | `portal-v2.1.174` peeled: `^{commit}` == PROD head, MATCH |
| Served bundle | entry chunk `index-D9vMtGZu.js` -> `index-CQCRJQRU.js`; every MFA token inverted from pre-promote 0 (mfaRequired 4, challengeId 7, mfa/send 1, opt-in + challenge copy present); positive controls fire (DE bundle-plane PASS, gated on the CI conclusion) |
| Workspace pointer | `a8305b3339` on SITEZ, my author, msg verified at the object (`git cat-file`) — LOCAL; the CLOUD push (Leg 3) rides the integrator's held CLOUD integration |
| Main portal tree | on DEV throughout and at close (Rule 19 verified) |
| Worktree | `.runtmp/portal-promote-20260901T064519Z`; physical remove failed "Filename too long" (documented-acceptable), `worktree prune` clean |

## Payload (7 work commits, ruled by Andrew on the explicit list)

- `89ecfd89`, `087a456f` — D12 DE1/DE2/DE3 (MFA login UI, opt-in prompt, challenge form, same-origin /auth proxy, client-side gate-bypass fix). Site-Z, verified end-to-end pre-promote (DE3 accepted).
- `dae4bb62`, `726f66b6`, `24ed70b8`, `52835384`, `9f8d10fa` — perfrp TO-R1-DE render work, `0.4.0_DE_ClientPlatform~D` (laptop lane), dated 2026-08-28; the "performance reporting edges" Andrew named on the bus.
- Integrator reconciled raw count 9 = these 7 + 2 merge-topology commits before pushing (no hidden passengers).

## Holds taken and discharged in-flight

1. Non-integrator DEV push BLOCKED by LD-0367/LD-0368 at the canary (before any merge) — routed to the integrator per design; no half-landed state existed at any point.
2. PROD push HELD by the executing seat on discovery of 5 non-D12 passengers — surfaced to Andrew with the explicit list; discharged by his verbatim ruling.
3. Integrator self-held on a 9-vs-7 count until reconciled.

## NOT in this deploy

No enrolment: MFA remains OFF for all accounts (`mfaEnabled` TRUE on 0 real accounts). Enrolment is a separate act gated on a named-human allowlist (F-7). No backend change (Act B shipped separately via Terraform in the AE lane). No alarm/monitor built.
