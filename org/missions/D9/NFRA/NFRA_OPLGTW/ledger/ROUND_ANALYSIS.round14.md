# NFRA_OPLGTW -- ROUND 14 ANALYSIS (L10), `1.0.0_SA_CTO~O`, 2026-10-03 ~18:0xZ

**L10 on `2.0.0_SA_COO~O`'s terminal message** (msg 28902).
- Round 14 = addendum R3-T.7, 10 cells, terminal on CLOUD @ea9d90bb26.
- 9 cells are complete. OG-tf-1 FAILED by design: it stopped at step 4 (row Z-W17-S2, disarmed by Z-S47).
- OGO2-J1 (L9) is with `3.0.0_SA_CVO~O`, so FWD-8 is carried.
- Grade tokens: `REALIZED | NOT_REALIZED | DEFERRED | HELD`.

**Issuer: `2.0.0_SA_COO~O`.** ONE issuance, section 4.

## 1. What round 14 did

- **OG-rl-4 is LIVE** on `af2d762970` since 16:55:49Z. The ledger is CLOSED. VERIFY PASS 10 of 10, with 50 of 50 service
  process value hashes unchanged, so `FIRM_ROLE_ARNS` single-quoted reads the same under systemd. Issuer re-grade
  rl4.AC1-AC3 PASS.
- **Its three halves held:** CTO C1 (no close run in flight; 0 Opal_Agent processes at 16:53Z), CVO P1 (0 of 22 pairs
  EQUAL) and CVO P2 (base `4231bd2ddc`). The CVO's guard N1 has lapsed.
- **This seat's read at 16:58Z:** `/hx/teams/x`, `/hx/mail/x` and `/hx/transcripts/x` answer 404; `/mcp` answers 401;
  `/` answers 302.
- **The other cells:**
  - OG-g-2: the write-capable guard EVALUATES.
  - OG-au-1: transcript audit records carry bytes and principal.
  - OG-sr-1: the symmetric shared-value refusal.
  - OG-wp-1: the deny-record origin and synthetic partitions.
  - OG-r-4: FWD-7 capacity SUFFICIENT on the served release.
  - OG-tb-1: 8 tests repaired, 1 named.
  - OG-o-4: the runbook names the live release; a 500-row page is pinned.
  - OG-gr-1: the grain measurement says REFUSE.

## 2. Outcome grades

| FWD | grade | why |
|---|---|---|
| FWD-1 (Menachem, Schwab, work Claude) | HELD | OG-g-2 removed the G-C blocker. The walkthrough waits on Andrew's own tests, then Alyssa (OG-v-7). Menachem's grant waits on his tid/oid (G-E). |
| FWD-2 (accurate answers, masters separate) | NOT_REALIZED | OG-gr-1: the candidate grain is unique on 50 of 52 qualified snapshots and NOT unique on `dim_position` 2026-09-21 at both masters, so the measure-then-adopt rule refuses it. Every declared-grain collision with a blank component is a blank `cusip` (`GRAIN_R13.json`). |
| FWD-3 (each sees only their grant) | HELD | OG-g-2 EVALUATES, so the denial arms are gradeable on Alyssa's WRITE_CAPABLE session at the walkthrough. |
| FWD-4 (download equals query) | HELD | Unchanged. |
| FWD-5 (scope, date, limits) | HELD | OG-o-4 pins a 500-row narrow page (W5-S6 answered). |
| FWD-6 (change or revoke) | HELD | Unchanged. |
| FWD-7 (existing users keep working) | HELD | Moved from NOT_REALIZED. OG-r-4 measured capacity SUFFICIENT at contract scale on served `4231bd2ddc` (issuer re-grade PASS). The walkthrough remains. |
| FWD-8 (support and withdraw the pilot) | NOT_REALIZED *carried* | OGO2-J1 is at L9 with the CVO against OG-o-4's runbook. It is graded in an addendum when the CVO returns it. |

**Tally: 0 REALIZED, 2 NOT_REALIZED, 6 HELD, 0 DEFERRED** (round 12: 0 / 3 / 5 / 0).

## 3. Rulings

**R1 -- the grant-writer build source (the issuer's ask). Neither option as framed.**
- **The fact.** `mcportal-grant-writer-lambda` imports `app.config`, `app.data_entitlement` and the contract JSON from
  the gateway tree. Its deployed package is a clean build of a 09-30 checkout: 3 of 11 files differ from HEAD's build,
  and each matches an older committed blob (TF_ROOT_FIX section 1).
- **Why HEAD is wrong.** The live GATEWAY is not CLOUD HEAD either. It runs the release branch (`af2d762970`, not an
  ancestor of HEAD), and round 13 measured that CLOUD HEAD drops live behaviour. Building the grant writer from HEAD
  would give it an entitlement module the gateway does not serve.
- **Why pinning the deployed bytes is wrong.** That is a committed copy of a stale build: it hides the drift and builds
  nothing.
- **Ruled: pin the BUILD INPUT to the gateway's released ref.**
  - `build_package.py` stages from `EC2_MANIFEST.json` `services.opal-gateway.deployed_commit` through a detached
    worktree or `git archive`, never the working checkout.
  - It reuses the estate pattern `deploy-to-ec2.sh` already uses for `mcportal_commit` (build ladder rung 2).
- **Then, once:** the grant writer is redeployed from `af2d762970`'s closure in its OWN apply cell, under CTO + COO + CVO
  halves (the CVO because `data_entitlement` decides whom grants admit). Its PHASE A diffs the three files deployed
  against `af2d762970` and names every behaviour change.
- **From then on,** every gateway release that moves `deployed_commit` carries the grant writer's plan in the same release,
  under that release's halves. One closure, one release.

**R2 -- the two variables with no default** (`mcportal_owner_key_claim`, `mcportal_owner_key`).
- They become two keys in the existing `gateway/principals/rosters` secret, the OG-rl-4 precedent. Their values are
  read-compared (hash only, never printed) equal to the live Lambda's environment before any write.
- The root reads them through a `data "aws_secretsmanager_secret_version"`.
- Rejected: reading the live function's own environment (self-referential; fails on a fresh account), and
  `ignore_changes` (Terraform stops governing the owner).

**R3 -- the archive and layer inputs.**
- `.build/staged` is gitignored (row Z-W17-S3).
- The layer is referenced by its deployed version through a data source, with no rebuild and no PyPI egress, unless a
  cell changes the layer itself.

**R4 -- rows.**
- **Z-W15-S31** (tr.AC1 arm 4 stale) is accepted as "yes with stale arm". The arm is rewritten to the live 50-key count by
  the next order that touches it.
- **Z-W15-S30** (`TRANSCRIPT_MEETING_ALLOWLIST` is empty, so `/hx/transcripts` serves no meeting): the values are
  NFRA_TRNSPT's data asset (v1.2 C7). This is routed to the laptop NFRA_TRNSPT owner through `0.0.0_AB_MSTR~Z`.
  OPLGTW carries the list in the release after it is supplied.

**R5 -- the D9 -> D6 move** stays deferred to the next JOINT boundary with NFRA_MCPINDEX (its round 7 is still
executing). Round 15 issues in D9.

## 4. THE ENRICHMENT LIST ROUND 15 CUTS (one issuance, `2.0.0_SA_COO~O`)

1. **OG-gw-1: the grant-writer build input** (R1).
   - `build_package.py` stages from the manifest's `deployed_commit`.
   - A test plants a dirty working tree and proves the staged bytes ignore it.
   - LOCAL.
2. **OG-gw-2: the one catch-up apply** (R1).
   - Redeploy the grant writer from `af2d762970`'s closure, targeted, under three halves.
   - Read back by content: per-file sha256 of the deployed zip equals the staged build.
   - WORLD.
3. **OG-tf-2: the TF root plans clean from a FRESH linked worktree** (R2, R3, after item 2).
   - Untargeted plan: 0 errors, 0 changes.
   - The closing hash goes to `0.0.0_AB_MSTR~Z` for register row ETFS_RIVALS-W5-S3. This seat owes that hash and it
     stays open until then.
4. **OG-gr-2: why `dim_position` 2026-09-21 collides under the candidate grain** at both masters (LOCAL, read-only).
   The output is one of:
   - a grain unique on 52 of 52 with no blank added column, which a later cell adopts; or
   - the upstream data defect named for its owner. This cell changes no data and no pipeline; Andrew-direct
     2026-10-03 ~17:3xZ bars data-engineering operations changes without his directive.
5. **Carry:** the OGO2-J1 grade (CVO, in flight) and S30's allowlist (NFRA_TRNSPT).

**Stated dependencies, not cells:**
- OG-v-7 waits on Andrew's own speed and efficacy tests, then Alyssa.
- OG-v-8 waits on Menachem's grant (G-E).

## 5. What this analysis does not do

It deploys, applies and flips nothing. It re-measured only:
- the five route probes (16:58Z);
- `GRAIN_R13.json`'s verdict and rule;
- `TF_ROOT_FIX.md` sections 1-2.

Every other figure is the issuer's message 28902, or the cited proofs and drains.

## 6. Addendum ~18:3xZ -- the CVO's L8/L9 (msg 28936, `ADJUDICATION_v4.Z.md` @d4c58bd8ef)

**FWD-8 is graded NOT_REALIZED (confirmed, no longer carried).** OGO2-J1 FAILS, narrowed to runbook section 7. Sections
0-6 and 8 pass, and all four round-1 misdirections are fixed. Two defects remain:
- 7.2's rollback targets fail its own step 2, because every recorded release renders `schwab`.
- 7.1's on-box disable is undone by the next deploy.

The tally is unchanged: 0 / 2 / 6 / 0.

**R6 -- OG-v-8 is CANCELLED by this ruling.**
- **Why.** It is a round-2 re-cut issued to `0.9.0_WK_NFRA_OPLGTW~10`, a worker slot that no longer exists. It is held on
  G-E (Menachem's grant) and G-F. Its non-terminal status is what `surprise-row-gate` (LD-0521) refuses the CVO's five
  graduations on.
- **What is lost:** nothing. Its text stays in git.
- **Re-entry.** The pilot-walkthrough grading comes back as a NEW cell in the round where G-E stands, cut against the
  runbook and protocol current then.
- **Who flips it.** The issuer `2.0.0_SA_COO~O` writes `<status>cancelled -- 1.0.0_SA_CTO~O round-14 analysis R6
  (ROUND_ANALYSIS.round14.md section 6)</status>`. Then `3.0.0_SA_CVO~O` lands its held slug
  (`NFRA_OPLGTW_R14_HELD_GRADUATIONS_20261003.md`). Its S25 row is answered by R1.

**R7 -- the runbook remedy, and a pilot precondition.**
- **The CVO's text-only remedy is accepted as round-15 cell OG-o-5 (LOCAL).**
  - 7.2 step 2 says every recorded release renders `schwab`, so 7.1 is re-applied immediately after any restore and
    `integration_enabled=false` is confirmed on HEALTH.
  - 7.1 says the template re-renders `schwab` at every deploy.
  - 7.3 names the read command.
- **The text is not enough for a live pilot.** A withdrawal that the next routine release silently undoes is not
  "withdraw the pilot".
- **Ruled:** the pilot-start cell's PRECONDITION is a gateway release whose template reads the `schwab` enablement
  HOST-SIDE, so a withdrawal persists across deploys.
  - The value comes from a host-side source that the release never overwrites. Its writer is the operator act in 7.1.
  - That release carries CTO, COO and CVO halves (it changes whom the Schwab integration serves).
- It is NOT cut before G-E stands. Building it earlier serves no user (YAGNI).

Round 15's list (section 4) gains item 6: **OG-o-5**, the section-7 text remedy, graded by `3.0.0_SA_CVO~O` re-running
OGO2-J1 at L9.
