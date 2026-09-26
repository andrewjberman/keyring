# CTO rulings -- IRPT, 2026-09-25 ~14:4xZ

By 1.0.0_SA_CTO, answering queued asks.

## R1. Export hop, section A (the render identity's live landing) -- 2.0.0_SA_COO~P 100935

**Owner:** 2.0.0_SA_COO~P. The two function directories are granted exactly to lane IRPT_LIVE_SCOPE_P in
`.owned-paths.yaml`:
- `infra/aws/users/lambda/portal-authorizer/**`
- `infra/aws/lambda-edge/auth-validator-edge/**`

They return to CLOUD_OPS_OR_ETL when section A closes. No CloudOps seat is live, and ~P built and proved both render
branches offline (C-S219, 43 of 43).

**The exp leeway: the PRD holds.** A token past `exp` is refused (IRPT_BCKEND PRD item 7(c)); leeway applies to
`nbf`/`iat` only (item 2).
- The V2 and V3 verify options must stop giving `exp` the 60 s clockTolerance.
- The effective life stays the minted life, not 360 s.
- This lands before A2/A3 deploy.

**A1-A3 are WORLD acts**, each with its own ledger entry opened at start. Every user crosses A2 and A3.
- **Key pair:** A1 mints it by Terraform (safe-apply), never by CLI. Name the Terraform file and it gets an exact row.
- **Order:** A1, then A2, then A3.
- **Each deploy's negative arm, before and after:**
  - a human token on a normal route is ADMITTED;
  - a render token on a non-print route is REFUSED;
  - an expired render token is REFUSED.
- **Rollback:**
  - A2: re-point the alias or version to the prior code.
  - A3: re-associate the prior Lambda@Edge version on the distribution.
  - Record both prior versions in the ledger before acting.

## R2. submit-export on v1: the QUEUED shape -- 2.0.0_SA_COO~P 100936

**P's proposal is ruled.**
- `data` is OPTIONAL on `submit-export` while `status.state` is `QUEUED` or `RUNNING`, and REQUIRED (an
  `ExportReceipt`) at `READY`.
- The `export_id` travels in `status.operation.revision`.
- The `export-receipt` route answers the receipt once `READY`.
- ~P edits the published v1 files in both schema copies.
- 2.0.0_SA_COO~D lands the consumer acceptance in `portal/src/pages/InvestorReporting/contracts/**` (PRD v0.7 PATHS).

**The narrative packet: P's pick stands.** The packet is built at submit from the RETAINED report and retained, and its
sha256 is bound, never taken from the browser.

**The delegator slot is not ruled here.** B0's missing delegator slot in `ExportBundle` needs its own proposal (an
additive member or a sidecar).

## R3. Hop 4 custody: who mints the `cst_` binding -- 2.0.0_SA_COO~P 100937

**(a).** P's custody submit calls `AcceptedCustodyReader.create` from the VERIFIED selection plus the sent holdings
revision, then reads it back.

**Condition:** `create` refuses unless the sent `sourceSetRevision` is a PUBLISHED holdings revision on that firm's
index whose scope covers the selection, so a browser-supplied revision never mints a binding the server did not serve.

This needs no Holdings or portal contract change.

## R4. Holdings as a scheduled daily producer -- 2.0.0_SA_COO~M 100944

**Owner:** 2.0.0_SA_COO~M, steps 1-4 of the request, starting now.
- Step 3's read (whether the resident runner takes a holdings message) is one question to 2.0.0_SA_COO~P, answered
  on ~M's ask; retargeting the schedule is ~M's.
- Step 4, the enable, comes to the CTO as a never-widen half: daily served holdings at 3 firms, rollback per key to
  the prior revision.

## R5. The classifier widening -- 2.0.0_SA_COO~M 100934

- **Decision 3, the two defects:**
  - COT `B_01b` scanning an empty prefix, and the loader skipping rows without a ticker, both go to 2.0.0_SA_COO~M
    under exact-file grants on request.
  - The loader change moves the class of every reader (69 paths, Positioning included) for the securities that flip
    from NONE to a class. Its sign-off names that delta: the flipped securities and the readers, counted, before it
    deploys.
- **Decision 4, the 49F CUSIP-only rows:** yes. The Holdings producer fills symbol and name from the Schwab security
  master before any classification. This is ~M's own producer change and is additive on the next publication.
- **Decisions 1-2 are Andrew's:** whether held-away and manual assets are classified, and a per-use word for an
  OpenAI run. They are put to him at this terminal.

## R6. DSGN_IRPTV1 rows W11-S1 and W11-S2 -- 2.0.0_SA_COO~D 100940

- **W11-S1: keep `fe-s-10/parity.test.ts` as it is.** A firm's name is client language, not system vocabulary.
  FWD-2 puts the firm on the header, and FWD-15 bars system words, not names. `FirmAttribution.tsx` keeps the visible
  name; anything else on that chip that is a system token moves to a disclosure. The decomp cell's listing of the
  chip is over-reach. Disarmed by this ruling.
- **W11-S2: re-scope `fe-s-5/states.test.ts`**, in the next round's cell with that file in its `<paths>`:
  - the unsupported-benchmark cell asserts "not supplied", with the reason in the cell's hover;
  - the two sub-tests that pin the retired `render/performance/Summary.tsx` block are re-scoped to what `ReportingTab`
    renders now, or removed with that reason stated.
  Disarmed by this ruling: the re-scope is next-round work.

## R7. MDPF_TAXSMA-S6 -- 0.0.0_AB_MSTR 100939 (the gateway release shape)

**The disarm owner is re-addressed to 1.0.0_SA_CTO** (live), because 2.0.0_SA_COO~T is seated on neither device.

**Ruling:** any MDPF_TAXSMA gateway release is cut NARROW, at the deployed commit plus TX-g-1's own three commits
(`6abf60e5d5`, `8dce9aeb0b`, `e8f800e6a9`). That is the shape `RULING_OA-t-6_NARROW_GATEWAY_RELEASE_20260925.md`
@`592e319a06` gave NFRA_OPALAI.

A deploy of `infra/aws/ec2/opal-gateway` from CLOUD HEAD is not admitted while the NFRA_OPLGTW commits sit under
Andrew's 2026-09-22 stop. No seat is releasing TX-g-1 now, so the hazard is inert until one is seated.

## R8. Relationship-level (multi-account) Performance -- 2.0.0_SA_COO~P 101260, card `RELATIONSHIP_PERFORMANCE_CARD_20260926.md` @`db39879a8f`

**Ruling: B this round. A is routed as a design fork.**

**B:** a selection of n > 1 accounts runs the proven one-account computation once per account and composes ONE
`PerformanceReport`:
- `account_detail` = n rows;
- the set-level `summary_returns`, `period_returns` and `daily_cumulative_series` are ABSENT, with the named reason
  "set-level return not computed";
- `dates` = the intersection of the accounts' windows, disclosed;
- an account the engine cannot link is an `absence` row, never dropped.

The COT and INF plan gates stay per account and are not widened. More than 25 accounts refuses by name (1 entry of
4548 at 49F).

**Why B:**
- It unblocks FWD-1's Performance hop for the 43% / 68% / 70% of entries (49F / COT / INF) refused today.
- It invents no method, and the missing summary carries its reason (A VALUE MUST CARRY ITS CLAIM).
- FWD-5's "the lagging account in one screen" is served by `account_detail`.
- A set return formed inside the IRPT adapter would be an unratified method.

**A (the set-level aggregate) is a DESIGN FORK:** how a set return is formed (weighting, intra-day flows, accounts
entering or leaving).
- It is routed to 4.0.0_SA_CRO for research of the estate's prior art: the ADVI GIPS aggregate work and Black
  Diamond's group-return shape, per Andrew-direct @`964fb4ed6b` ("match the same shape and compare against Black
  Diamond").
- The CTO rules the method when the research lands, and A becomes an enrichment outcome.
- It goes to Andrew only if the research finds the choice changes a figure a client would see differently from Black
  Diamond.

**The page:** rendering `account_detail` n rows, with the summary reading "not supplied" and its reason, is a
DSGN_IRPTV1 round-6 enrichment item (FWD-5, FWD-1). It is not an off-spec edit mid-round.

**R8 SUPERSEDED (Andrew-direct ~15:1xZ, record `ANDREW_DIRECT_20260926_151xZ_PERFORMANCE_ACCOUNT_LEVEL_FRONTEND_ROUTES_CLOSER_TRACE.md`):**
"Performance is always going to be account-level, not client level ... this is just a frontend code issue rather than
a backend data issue."
- B is not built, and A and its research ask are withdrawn.
- The backend's one-account refusal stands as designed.
- The fix is a frontend route structure, from 4.0.0_SA_CRO's `/closer` traces.
