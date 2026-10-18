# A sanctioned through-the-service probe without impersonation -- design-fork research (NFRA_OPLGTW Z-S375 / Z-S338)

**By:** `4.0.0_SA_CRO~Z`, 2026-10-18 ~00:3xZ. **For:** `1.0.0_SA_CTO~Z` msg 35580, who rules on it.
**Input:** item 8 of `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/L10_SLUG_ROUND41_DRAFT_20261017.md`.
**Sourcing:** the estate facts are read at box/sitez HEAD, with path:line. The outside-the-estate patterns are from general
practice and were not fetched or sourced in this turn.

## The constraint, as recorded

- `/mcp` takes only a bearer signed by the gateway's RS256 key.
- Minting one as a real roster principal "is impersonation; no one cuts that without his word". Source: CTO half of OG-ap-34,
  Amendment 1 @ddb0eded30, `NEVER_WIDEN_HALF_CTO_OG-ap-34_20261017.md:40-63`.
- The fallback used since then is a fresh process on the host under the gateway role. It measures that process, never the
  running service. That is why Z-S338 (the service heap over a real window call) and the Z-S375 disarm stay open.
- So the probe must exercise the RUNNING service process. A stand-in cannot answer either row.

## What the estate already does (five precedents)

| # | Pattern | Where | Non-human? | Relevant property |
|---|---|---|---|---|
| E1 | A **synthetic, dormant, leased account** | `/ui-walk`: `opal-users-v2` `USER#usr_opal_ui_walker` (`opal-ui-walker@opal.test`), `.claude/skills/ui-walk/SKILL.md` safety table | yes, a test-domain identity | Disabled at rest; `arm` takes a 60-minute lease and mints a one-walk password into SSM; the client side is read-only (a network guard admits GET plus four POSTs); localhost base only; `status`/`disarm` close it. This is the estate's own canary principal. It lives in portal auth, not the gateway's. |
| E2 | A **route-scoped capability bearer**, not a principal | gateway `/hx/mail`, `/hx/teams`, `/hx/transcripts` (`app/mail_route.py:1-35`, `app/teams_route.py:1-35`) | yes | One static bearer per prefix, in Secrets Manager. Compared in constant time, refused on every other prefix, with an audit label. A GET path allowlist fails closed. It reads with a server-held identity. |
| E3 | A **fresh-process stand-in** under the gateway role | OG-ap-31 / OG-ap-34 CT1 (a) | yes | No auth surface at all. It measures the wrong process (the reason for this ask). |
| E4 | A **header-identity local harness** | `infra/aws/ec2/opal-gateway/dev_smoke.py` (`IDENTITY_PROVIDER=header`, `MOCK_GRAPH=1`, `127.0.0.1:8080`) | n/a | Dev only. `config.py:428` admits only `alb_oidc` or `cloudflare` as verified providers, and prod boot refuses the rest. Not a live-service path. |
| E5 | A **real account run by an agent** | `opalbloomberg@opalinvest.com` (BG concierge), PRD v2.3 | the operator is an agent | A real Entra user, so it is not synthetic. It shows what "non-human principal" costs: it now mirrors Andrew's grants and carries an email deny (my record @25a55fbecb). |

## The options

### A. A loopback-only probe route on the running service

A second listener bound to `127.0.0.1:<port>`, kept out of the ALB target group. It is reachable only from an SSM session
on the host, and it runs ONE named read-only tool for a fixed probe principal. It is off by default and armed per order
with a lease, as in E1. The audit record carries a probe label, as in E2.

- **Measures the right thing:** yes. The same process and heap as real callers, which is what Z-S338 asks for.
- **Auth surface:** none on the internet-facing side. No OAuth or AS change, and no Entra object. The guard is the
  listener binding plus SSM IAM, both existing controls.
- **Risks:**
  - (i) Any process on the host can call loopback. A host-local SSRF (a gateway outbound fetch steered to localhost)
    would reach it. Measured: 5 gateway modules make outbound HTTP calls (`identity.py`, `graph.py`, `ycharts/client.py`,
    `globgrph/integration.py`, `opal_portal/integration.py`; 18 call sites). I did NOT check whether any target is
    caller-controlled. That check is the precondition.
  - (ii) A probe principal still needs a data grant to read anything. That is an operator act with a source
    authorization, under the C2 rules.
  - (iii) Code that is off by default rots unless one test exercises the arm path.
  - (iv) A route-level `client.host == 127.0.0.1` check is weaker than a separate listener. The ALB forwards from its own
    private IP, so the check holds, but it is one config change from open.
- **Estate precedent:** E2's route-scoped guard and E1's dormant lease, together.

### B. A synthetic canary principal (a non-human test identity through the normal OAuth path)

An Entra test user, for example `gateway-probe@...`, holds a restricted profile scoped to one test account. It is dormant
and leased like E1, and revocable through the C2 family-revocation path that exists today.

- **Measures the right thing:** yes, end to end: the ALB, the AS, the policy and the tool.
- **Risks:**
  - (i) It is a new Entra object. That is IT's act, and it may need a licence.
  - (ii) The OAuth flow is authorization-code with a browser sign-in (C1). A non-human cannot clear MFA or Conditional
    Access, so it needs a CA exclusion or a stored refresh family. Each is a standing credential and a real weakening.
    This is the material risk.
  - (iii) Every restricted principal gets an email deny (C2), so its browser routes are dead. That is harmless here.
  - (iv) A "test account" scope conflicts with the measurement. The heap of a window call depends on real partition
    size. The `demo` tenant exists (`scopes.json`: `opal-data-demo`, DEMO-TENANT) but would understate the peak unless
    its data is real-sized. A real-sized scope means one real account, which is client data read by a non-human: a grant
    with its own word.
- **Estate precedent:** E1, on another auth plane; E5 is the cautionary version.

### C. A workload identity on the gateway's AS (an OAuth client-credentials grant)

This is the industry-standard machine caller: a registered client with its own scope and no user.

- **Risks:** it is a C1 contract change, a new grant type on an AS that today supports only authorization code. Every
  C1/A2/A17 guarantee would need re-proving for it. It is the most surface for one measurement.
- **Estate precedent:** none.

### D. Delegation with an actor claim (RFC 8693 token exchange, `act`)

The token names both the subject and the acting agent, which removes the impersonation in the literal sense.

- **Risks:** the subject is still a real roster principal, so it still needs his word. It is also AS work on the scale of
  C.
- **Estate precedent:** none.

### E. Observe the service without calling as anyone

Attach a sampler or heap profiler to the running PID over SSM (for example py-spy or memray, or a signal-triggered
tracemalloc dump), timed against the next organic window call.

- **Risks:** it produces no call by itself, so it is a WAIT. Rule 27 L2: "no FWD is a wait", and the organic case is the
  negative arm. It is good as the instrument beside A or B, not as the driver.
- **Estate precedent:** E3-style host access.

## Recommendation (the CTO rules)

**A, with E as its instrument.** It is the only option that drives the running process on demand with no new identity and
no change to the internet-facing auth path. It reuses two controls the estate already proved: E1's dormant lease and E2's
route-scoped guard.

Two preconditions before any cell:
1. Check every outbound-HTTP call site in the five modules for a caller-controlled target. This is the SSRF arm of
   risk (i).
2. Decide the probe principal's data grant: which account, and whose word. Measuring the real heap needs a real-sized
   partition.

**B** is the right answer only if end-to-end realism through the ALB and AS becomes a requirement. Its blocker is MFA and
Conditional Access, which is IT's and Andrew's. **C** and **D** cost the most for this one need.
