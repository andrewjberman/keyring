# COO~C Session Log — ADVI_DEMOV1 Driver — State Snapshot

- **Agent:** 2.0.0_SA_COO~C
- **UTC:** 2026-05-22T21:52Z
- **Supersedes:** the 18:15Z snapshot.
- **Scope lock:** ADVI_DEMOV1 only.

## This turn — TO-3 DS-scope RAVC2 VALIDATED + ACCEPTED; TO-4 GO'd (scoped)

### TO-3 DS-scope — RAVC2 ACCEPTED (COO~C empirical validation)

DS~C delivered the ADVI_DEMOV1.003 DS-scope RAVC2. Evidence independently
verified by COO~C (not self-report):

- **Commits on origin/CLOUD** (`git branch -r --contains`):
  - `2ea34ba81` — `scripts/register_demo_tenant.py` (+208, single file; correct
    `scripts/` lane, NOT the owned-paths-blocked `infra/aws/auth/migration/`).
  - `594520fa9` — TO-3 session log.
- **DynamoDB records** (COO~C `aws dynamodb get-item` on `opal-users-v2`):
  - `FIRM#demo / META` — s3Bucket=opal-data-demo, firmId=demo, tier=advisor,
    status=active, name="Demo Advisory", domain=demo.test, config={},
    createdAt 2026-05-22T21:03:56Z, createdBy 0.4.0_DS_ClientPlatform@opal.agent.
  - `USER#demo@demo.test / PROFILE` — firmId=demo, role=user, tier=advisor,
    status=active, passwordHash + password_hash both bcrypt `$2b$12$`,
    mustChangePassword=false, createdAt 2026-05-22T21:03:57Z.
  - Demo login: `demo@demo.test` / `OpalDemo2026!`.
- **Scope correction honored** — the `2ea34ba81` stat confirms no
  `advisor-intelligence.ts` edit; DS~C ran no portal `bun build`. The carved
  portal items stayed untouched.
- **firmId-token consistency:** 3-of-4 DS-runnable points all resolve to token
  `demo` (JWT firmId claim, DynamoDB FIRM# key, edge FIRM_CONFIG['demo']).
  Point [4] ROUTER_FIRM_SUFFIX deferred to the post-DE track.

TO-3 TO file LEFT at `<status>pending</status>` (correct — DS~C did this): the
DS-scope is done but TO-3 does not fully close until the DE-laned portal items
land.

### TO-4 — GO'd to DS~C, SCOPED

Per the 18:18Z driver decision ("On TO-3 DS-scope RAVC2: GO TO-4"). TO-4 file
`<status>` flipped staged -> pending with a COO note documenting the scope:

- **Proceeds now** (gated on TO-3 DS-scope, met): ACs 1,2,3,5,6,7,8 — the EC2
  one-shot transform populating `opal-data-demo/platinum/**`, the mandatory
  PII-leak scan (ruling R5 — the closure gate), Sigma-identity reconcile.
- **Deferred** to the post-DE verification track: AC4 (visual smoke across
  Advisor Intelligence surfaces AS THE DEMO USER) — needs the carved portal
  items live.
- The TO-4 file's literal gate text ("TO-3 all RAVC-closed") predates the
  TO-3 DS/DE split; the COO note in the TO file records the refinement.
- **Likely infra follow-up:** the EC2 one-shot needs a scoped write role on
  opal-data-demo (TO-1 provisioned serving/read only). DS~C surfaces the exact
  grant at Phase 1; AE~C pre-warned.

## ADVI_DEMOV1 standing

| TO | Phase | Owner | State |
|----|-------|-------|-------|
| TO-0 | probe | DS~C | CLOSED — RAVC2-accepted |
| TO-1 | infra | AE~C | CLOSED — RAVC2-accepted |
| TO-2 | transform engine | DS~C | CLOSED — RAVC2-accepted |
| TO-3 | firm + user registration | DS~C | DS-scope CLOSED (RAVC2-accepted); TO file `pending` — portal items carved DE-lane |
| TO-4 | transform run + PII-leak scan | DS~C | **PENDING — GO'd scoped; transform+scan proceed, AC4 deferred** |

**Critical path:** TO-4 EC2 transform -> PII-leak scan (R5 gate) -> project
closure review. The DE track (TO-3 portal items + TO-4 AC4) runs parallel,
still unresourced.

## Open for Andrew

- **DE-lane resourcing gap** (unchanged) — the TO-3 portal items + TO-4 AC4
  visual-smoke need a DE; no DE in the ~C team. Stand up a DE~C lane or assign
  the base Pod-4 DE.
- Andrew Q1 (verbatim vs scaled dollars) + Q2 (refresh policy) — non-blocking.

## Notes

- COO~C commits under the base `2.0.0_SA_COO` serial (owned-paths).
- DS~C stall scare earlier this session (~60min flat telemetry) resolved —
  it was genuine heads-down work; DS~C delivered a clean artifact-grounded
  RAVC2. Calibration held (escalated as "verify", never "relaunch").
