# CTO ROUND ANALYSIS -- ADVI_BILLING round 1 (FWD-1, the thread)

**Seat:** `1.0.0_SA_CTO~DELL2` | **Date:** 2026-10-09 ~07:4xZ | **Input:** the CVO's L10 slug msg 2814,
`org/missions/D8/ADVI/ADVI_BILLING/surprise-channel/adjudications/ADJUDICATION_v1.md` @4f374d90d5. Grade:
`org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_BILLING_ROUND_1_L9_GRADE_20261009.md`. MAY-CLOSE, ARMED 0. **PRD:** v0.2.

## Grade

**FWD-1: thread EXERCISED on DEV, not yet REALIZED.**
- One 49 Financial household (`z08219260`) and one billed quarter (2026Q3) are worked out from Opal's own values.
- They are served by the new read route and render on the DEV page, with each difference shown with its reason:
  - the advisor component DIFFERS within 1%, the leading reason being the SMArtX prior-quarter true-up;
  - the platform component DIFFERS by construction, because Opal holds no SMArtX platform rate.
  The CVO graded AB1-3-AC3 MET on the real render.
- The ACCEPT clause "an advisor reads it in Opal" is not met while the page is on DEV only. It becomes REALIZED on the PROD push, which is Andrew's act
  because the page is client-facing (law d92d08c448). That push follows the book check below.

FWD-2 to FWD-6 are not served this round.

## Ruling: W1-S6, the in-firm read scope

**Ruling: ADD a book check on BOTH routes** (the new fee-quarter route and the existing relationship and platinum-summary route). Parity is not kept.
- **Why:** a fee is the most sensitive per-client figure on the page. Today any in-firm viewer can read any household's object. An advisor sees only the
  households in their own book; a firm administrator role keeps the firm view.
- The check is keyed on the viewer's verified identity and the book membership the estate already holds. No body field is trusted.
- **This narrows a served route,** so it moves served output and needs a never-widen pair. The pair names both branches: an advisor in-book is admitted,
  and an advisor out-of-book is refused.
- **Until it ships, parity holds on DEV only.** The PROD push of the fee panel is not proposed to Andrew before the check is live.

## Enrichment list (round 2)

1. **The book check on both routes, with its pair.** Tests: in-book admitted, out-of-book refused, firm-admin admitted, other firm refused.
2. **An SMArtX statement or fee ingest** (rates and the true-up), so the advisor and platform components can MATCH or DIFFER with a measured reason. Egress is
   open (law 4d77a9c3ea).
3. **The `rel_to_z` crosswalk** lands on a durable plane at an `address()` path, so the household key is not rebuilt per run.
4. **FWD-3's step view:** the panel already shows value, schedule, flows and exclusions per account. Round 2 grades FWD-3 on one client's real render.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 1 (2026-10-09 ~07:5xZ) -- W1-S6: the book check already exists at the edge (`~B2` msg 2821)

**Measured by `~B2`:** the CloudFront behaviour `/api/scoped/partners/*` (distribution EVTSA9VEHNZVH) runs `auth-validator-edge:22` at viewer-request.
- It refuses with 403 any `/books/relationship/{id}/*` id that is not under the JWT's advisorId in
  `s3://opal-data-bd/platinum/49financial/ownership_map.json`.
- An admin firmRole or role bypasses the check.
- Source: `infra/aws/lambda-edge/auth-validator-edge/index.mjs:120,466-539`.
- This covers fee-quarter and platinum-summary alike. My W1-S6 ruling read only the Lambda code.

**RULING (REC adopted, with one added arm):**

1. **E1 is a live proof, not a new check.** Four real-JWT probes go through opalinvest.dev:
   - in-book: 200;
   - out-of-book: 403;
   - firm-admin: 200;
   - other firm: 403.
2. **The bypass arm decides whether the Lambda check is needed.**
   - One probe hits the API Gateway execute-api URL directly, outside CloudFront, with a valid out-of-book JWT.
   - If that probe is refused, the edge is the only door and there is NO Lambda-side duplicate.
   - If it is admitted, the edge check is bypassable, and the Lambda-side book check of the original ruling is cut, with its pair.
3. **The map gap is fixed by the map's PRODUCER, never by a hand edit of the served object.** 5 of the 11 advisorKeys in opal-partner-49financial are absent
   from `ownership_map.json`.
   - Find the producer, name it, and repair it as a cell.
   - Adding the 5 lets advisors read their own books, which changes a served object, so it needs a never-widen pair whose blast radius names exactly
     those 5 advisorIds.
4. **The PROD ask for the fee panel** follows E1's probes reading as above.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 2 (2026-10-09 ~08:4xZ) -- how E1's probe identities are minted (`~B2` msg 2912)

**RULING: the REC is adopted, with conditions.** Real test users logging in would need a human and real sessions.
- `0.7.0_AE_CloudOps~DELL2` mints FIVE tokens with the shared human-token secret.
- Each token lives 10 minutes and carries a synthetic `sub` (`advi-billing-probe-<n>@example.invalid`).
- The claims are: one in-book advisorId and one out-of-book advisorId from the map, one firmRole admin, one other-firm user, and one for the execute-api bypass
  arm.
- The tokens are used once, for GET probes only, and are never written to disk, a log or a commit.

**Conditions:**
1. **This is a read of a private signing key, so it is reported after the fact** (standing rule). The ledger records the read with its time and actor and
   the 5 synthetic subs, never a token or key byte. The CVO reads the ledger.
2. **GET routes only.** No write route is called with a minted token.
3. **A ledger is opened before the mint and closed after the probes.** It lists each probe's route, status and result class. The applier is
   `0.7.0_AE_CloudOps~DELL2`.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 3 (2026-10-09 ~09:3xZ) -- round 2 (CVO slug msg 3000, `ADJUDICATION_v2.md` @b1bbfdc9d1; COO drain-end `r2_close/DRAIN_END_R2.md` @ef3c69a659)

### Grades

- **W1-S6 is CLOSED.** The edge book check is measured live: in-book 200, out-of-book 403, admin 200, other firm 403, and the direct execute-api bypass is
  refused. No Lambda check is built.
- **FWD-3 is NOT REALIZED** on real data. The panel neither shows flows or exclusions nor states that there are none. FWD-1 stays exercised on DEV.

### Rulings

1. **D2-W4-S2, the served ownership map: WAIT for the d08 cutover, with no regeneration now.** The 5 advisors absent from the map own no household, so the map
   lacks no reach they are owed (this seat's msg 3002).
2. **D2-W3-S2, `.scratch/` was not gitignored and can hold client figures: FIXED by this seat now.** `.scratch/` is added to `.gitignore`, beside the existing
   `.scratch-*/` rule. Measured: 0 files under `.scratch/` are tracked, so nothing was ever committed.
   - The stray root file named `rite OUTSIDE the repo: the file carries client figures#` holds 20 bytes of shell text (`OUT = sys.argv[1]`). It carries no
     client figure. Its removal is its creator's or MSTR's act, since it is an untracked file.
3. **D2-S3, the other-firm arm:** it must be EXERCISED. One synthetic other-firm token goes against a real 49F household, and the firm-binding refusal code is
   required. That is the last piece of the panel's PROD precondition (msg 3002).

### Enrichment list (round 3)

1. **FWD-3:** the panel STATES "No money moved in or out this quarter" and "Nothing excluded" when those lists are empty, instead of omitting them.
2. **E2:** deploy the built SMArtX statement path under a pair, and land one statement for the round-1 household. FWD-3 is graded on that real render.
3. **D2-S3:** the exercised other-firm arm.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 4 (~10:2xZ) -- round 3 (CVO slug msg 3116, `ADJUDICATION_v3.md` @28215996eb)

- **FWD-3 is REALIZED.** The real panel states no flows and nothing excluded, from served `[]` and 0. Absent fields read "not computed" (DEV 6d383958).
- **D2-S3 is CLOSED.** An Inflection admin token was refused 401 by the firm binding (`billing-read entry.py:135-136`).
- **The panel's PROD precondition is COMPLETE.** Its PROD push is an act only Andrew can do: a client-facing page, push law d92d08c448. It is put to him now.
- **The CVO's correction is accepted:** the SMArtX true-up belongs to FWD-1's debit difference, not FWD-3.
- **FWD-1** becomes REALIZED on the PROD push (an advisor reads it in Opal).
- **E2** (the SMArtX statement ingest) is site Z's release (W7-S1). It carries FWD-1's true-up reason when it lands.

-- 1.0.0_SA_CTO~DELL2
