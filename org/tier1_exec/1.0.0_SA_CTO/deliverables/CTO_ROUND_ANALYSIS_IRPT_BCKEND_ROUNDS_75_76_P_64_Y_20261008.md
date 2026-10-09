# IRPT_BCKEND -- ROUND ANALYSIS, rounds 75-76 (~P) and round 64 (~Y) (sweep 17)

Author `1.0.0_SA_CTO~DELL2`, 2026-10-08 ~17:3xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES.

**Input:** `3.0.0_SA_CVO`'s slug (msg 1326) and ADJUDICATION_v34 @5ee71cfd2c.
- Every order is terminal: IB-pr-361/362/363 and IB-yr-641, with 0 judgment criteria.
- C-S308 dismisses the 6 rows filed this round.
- W140-S1 and W145-S2 are closed.

## 1. State

- **The custody release pair (E2 of round 75) is SIGNED on both halves:**
  - COO half `~P2` @9e444a64c5;
  - CTO half @652141d7cc. This seat measured the census at pin 1e0cdaf90c (`changed_members=3`), the live CodeSha256 (the same as the
    rollback artifact), the route absent live, and the refusal mapping at the pin.
  - Nothing is applied yet.
- **The X-1 release 2 pair (irpt-ycharts-generate, pin f7a9d0b34f) is SIGNED on both halves:**
  - `~Y2` pair @bf4707adf1, with the `~P2` half confirmed in msg 1322;
  - CTO half @6d24511482, which adds three conditions: the test filer has no login identity; the put follows the equality read; live
    code is re-read at the start.
  - Nothing is applied yet. The real filer entitlement stays an act only Andrew can do and does not hold the release.
- **The S391 correction is ACCEPTED.** `api/routes.json` is IB-rt-1's retirement stub, not a stale carrier, so no removal is owed. The
  CTO half for IB-pr-363 does not rely on it.
- **S388 is OPEN and INERT.** `~P`'s four files are regenerated on the DEV candidate. What remains is the AnalysisReport share (`~G2`,
  the IRPT_YCDGEN u-6 recut to v2) and the HoldingsSnapshot share (`~M2`).
- **ARMED after this sweep: 2.**
  - **S334 (this seat's):** the comp-tagauthz pre-apply gate makes no progress on trees that set `default_tags`, so it fails closed.
    Its last code change was 65ec0e0f5a (2026-07-09). It is ARMED, and it bites both release orders below.
    - **Interim disarm, ruled here on the precedent of CTO batch 259:** each release order may carry `TAGAUTHZ_OVERRIDE` for its own
      named apply(s) only. The reason cites S334, and the order commits the plan text before the apply.
    - **Permanent disarm:** the gate's owner (`0.5.0_AE_OpalETL`, laptop fabric) bounds the IAM read. That routing is cross-fabric, so it
      goes through `0.0.0_AB_MSTR~DELL2`.
  - **W165-S2:** `0.0.0_AB_MSTR~DELL2`, on Andrew's word; unchanged.

## 2. ENRICHMENT -- ONE issuance each: `~P2` round 77, `~Y2` round 65, `~M2` (workstream M)

| # | lane | item | criteria (at most three) | risk |
|---|---|---|---|---|
| E1 | `~P2` | **The custody release order**, run as signed (IB-pr-363 pair) | (1) function at pin 1e0cdaf90c live with the new CodeSha256, then the route applied, and the post-deploy census reads `changed_members=0`; (2) the other-firm read returns `OBJECT_NOT_COVERED` with no body; (3) an Opal read by reference returns the requested report and revision. Branch B is executed if any of these fails. | SERVED |
| E2 | `~Y2` | **Release 2, run as signed** (X-1 pair plus the CTO half's three conditions) | (1) after-reads 1 to 7 PASS, with the deployed hash = `798Lgqw2...`; (2) the test row and its uploads read back NOT FOUND in every branch; (3) on any failure, the rollback to `ZspX0qD2...` runs the same session | SERVED |
| E3 | `~M2` | **S388, the HoldingsSnapshot share** | (1) the cell names which side moved (the schema or the committed wire type) and brings them into agreement; the generator test regenerates 0 diffs for HoldingsSnapshot | LOCAL |

E1 and E2 each open their change-management ledger entry at start, and each may use the S334 override as ruled above. The print page's
DEV and PROD landings (IB-pr-356 at 63b9382a) stay Andrew's word, after E1.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 1 (2026-10-08 ~17:3xZ): E4 -- S334's permanent disarm is seated on dell2

This addendum follows the laptop `1.0.0_SA_CTO` ruling, relayed by `0.0.0_AB_MSTR~DELL2` as msg 1342 (laptop bus 02560565), VERBATIM:
"ruled -- dell2 seats the fix itself; it holds the reproduction and the blocked trees, and the Dells are the work boxes. Bound the read in
.tools/comp-tagauthz: a timeout on get-account-authorization-details, failing CLOSED with a named reason, or a narrower read (--filter
scoped to the principals the tree tags), whichever settles row IRPT_BCKEND-S334 on a real default_tags tree. Lane:
GIT_COMMIT_AUTHOR_OVERRIDE=0.5.0_AE_OpalETL, audited, naming this ruling; it reaches every box by the trunk. Your interim per-order
override 0a91529221 stands until it lands."

| # | lane | item | criteria (at most three) | risk |
|---|---|---|---|---|
| E4 | `~P2` | **Bound comp-tagauthz's IAM read** (`.tools/comp-tagauthz`), committed under `GIT_COMMIT_AUTHOR_OVERRIDE=0.5.0_AE_OpalETL`, with the audit line naming msg 1342 | (1) on one real `default_tags` tree, the gate returns a verdict in bounded time (the elapsed time is printed); (2) when the IAM read is forced to exceed its bound, the gate fails CLOSED with a named reason (negative arm); (3) S334 is disarmed in the investigation row, citing the commit | LOCAL |

E4 may be issued in the round already open, or in the next one. The interim override stays in force until E4's commit is on the trunk.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 2 (2026-10-08 ~18:0xZ, on `~Y2` msg 1361, row D2-W156-S2): X-1 is recut on the live guard by `~P2`; release 2 re-pins after

**What failed.** E2, release 2, ran and was rolled back to `ZspX0qD2...` at 17:44:54Z (`IRPT_BCKEND_ROUND65_Y_L8_COMPILE.md` @87a95c6fca).
This seat read the cause in the source:
- `_authz/served.py:919` resolves the create owner as `access.prospect_owner()` with no storage firm;
- `_scope/interactive_access.py:123-137` therefore builds the owner from the actor's own firm and principal.

So the on-behalf branch at `uploads.py:241-248` is never reached on the served path. The unit tests passed because they hand `create`
an owner that the live guard never builds. The release-2 pair (@bf4707adf1, CTO half @6d24511482) is VOID: its pin no longer ships the
behavior it signs.

**Ruling: lane `~P2`** (`_scope/` and `_authz/served.py`, lane IRPT_LIVE_SCOPE_P, as in msg 944 (1)).

| # | lane | item | criteria (at most three) | risk |
|---|---|---|---|---|
| E5 | `~P2` | **The live guard resolves an on-behalf owner.** For a CREATE by an OPAL_GLOBAL filer that names an owner firm in its `allowedFirmIds`, the owner the guard resolves is the shape `uploads.py`'s on-behalf branch admits. Every other case keeps today's owner. | (1) a test drives the REAL served path (`served.py`'s guarded handler with a verified internal subject), not `create` directly: the listed firm is admitted and the stored record names the actor and the owner firm; (2) negative arms on the same path: an unlisted firm, `"ALL"`, a non-internal principal and owner opal-capital are each refused with their existing codes; (3) the existing guard and uploads suites pass | LOCAL |

After E5 drains:
- `~Y2` re-runs the release census at the new pin.
- A NEW release-2 pair is signed, with both halves at the new pin. This seat's three conditions carry over.
- Then the release runs.

S1 (the irpt-requests decrypt) stays moot until then.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 3 (2026-10-08 ~18:0xZ, on `3.0.0_SA_CVO` slug msg 1369, REMEDIATION_v26 @69ae308272): round 65 ~Y analysis

**State.** The live code read back is release 1 (`ZspX0qD2...`). S392 is disarmed by AMENDMENT 2. Two rows are OPEN to this seat.

- **D2-W156-S2** (the on-behalf branch cannot be reached on the served route): ruled in ADDENDUM 2. `~P2` does E5, then `~Y2`
  re-pins, and then a new pair is signed.
- **D2-W156-S1** (BLOCKING: `cloudops-dell2-agent-user` lacks `kms:Decrypt` on irpt-requests' CMK, so the admit's UPLOAD# record could
  not be read back or deleted). **Ruling:** the NEW release-2 pair names, before any write, who reads back and who deletes the test
  admit's record, and through which path. The paths are tried in this order, and the first one that works is used:
  1. **No new grant.** Read back through the function's own read operation by direct invoke, since the function decrypts. Delete with
     `delete-item` by key. A dry probe on a non-client item first measures whether delete and NOT-FOUND need `kms:Decrypt`.
  2. **A laptop seat that holds the decrypt** does the read and the delete through the fenced path, and returns a counts-only file.
  3. **A new decrypt grant to the dell2 user,** asked laptop `~C` through `0.0.0_AB_MSTR~DELL2`. This is a last resort, because
     irpt-requests holds client request content.

  The pair does not sign until one path is named and its probe has printed.

**ENRICHMENT for `~Y2`, after E5 drains:** E6 is the re-pinned release 2, run under the new pair. Its criteria are the void pair's
after-reads 1 to 7, plus this read-back and delete path printed with its probe.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 4 (2026-10-08 ~18:1xZ, on `3.0.0_SA_CVO` slug msg 1377, ADJUDICATION_v35 @cdf801e03b): rounds 77-78 ~P

**State.**
- **E1 (the custody release pair) is LIVE.** The CVO read `irpt-export-render` CodeSha256 `03p2eIEK...`; the census at 1e0cdaf90c reads
  `changed_members=0`; the custody-report route is present.
- **E4 (comp-tagauthz bounded) landed** at fad269226b. S334 is DISARMED; it closes once the commit is on the trunk.
- **ARMED:** W165-S2 (MSTR) and D2-S3 (`~P2`: the shared tree's modified `export/entry.py` drops the custody route).

**D2-W172-S3, ruling: `~P2` cuts it.** It is a repin in `~P`'s function, not new code, and not IRPT_CUSTDY's. HEAD's
`reports/repository.py` carries `CUSTODY_REPORT` in KINDS, since b13bab7495. `irpt-export-render`'s source-map row still packages it at
83e8b9577a, which does not.

| # | lane | item | criteria (at most three) | risk |
|---|---|---|---|---|
| E7 | `~P2` | **Repin `reports/repository.py`, plus any reporting-policy row the read path checks, past b13bab7495, and release it under a new pair** | (1) `release-census.py irpt-export-render --pin <new pin>` lists only the repinned members, each against b13bab7495 or its named owner; (2) the build runs from a clean worktree at the pin, never the shared tree (D2-S3), and the built `entry.py` still routes `custody-report-read`; (3) after release, an Opal custody-report-read of one existing CUSTODY_REPORT by reference returns it, and the other-firm read still returns `OBJECT_NOT_COVERED` | SERVED |

D2-S3 is disarmed by `~P2` the same turn it is next read: restore or commit the shared-tree `entry.py` with its owner, so that no build
can pick it up.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 5 (2026-10-08 ~18:4xZ, on `~P2` msgs 1405 and 1406, row D2-W175-S1): E7 releases first; the CUSTODY_REPORT retention family is `~M2`'s (E8)

- **E7 part 1 (IB-pr-367) is signed by the CTO half,** with a retained-read regression check added (`NEVER_WIDEN_IB_pr_367_REPOSITORY_REPIN_CTO_HALF.md`).
  It releases first. The custody read keeps failing closed until E8 lands.
- **D2-W175-S1:** `infra/logic/registry/reporting_policies.json` policy `irpt-x10-v1` registers no CUSTODY_REPORT family. So the enforced
  repository refuses to retain or read a custody report. **Owner: `~M2`.** `.owned-paths.yaml:66-74` grants lane IRPT_COMPLETION_REGISTRY
  to `2.0.0_SA_COO~M2` on dell2, the CRO lanes, and `~M`.

| # | lane | item | criteria (at most three) | risk |
|---|---|---|---|---|
| E8 | `~M2` | **A CUSTODY_REPORT retention family in the served reporting policy,** as a new enforcement revision if the registry's rules require one for an ACTIVE policy, with the lane note's equality proof and naming-owner review | (1) the policy row carries CUSTODY_REPORT, with retention terms stated and the source of each term cited (the custody PRD, or an existing family it mirrors); (2) the existing 13 families are byte-unchanged in meaning (the equality proof); (3) the repository's retention check admits a CUSTODY_REPORT reference and refuses an unregistered kind in a test | LOCAL |

**Then, in order:** the served policy carries E8 -> IRPT_CUSTDY E2 (`~K2`) retains one real custody report -> the release order runs
IB-pr-367's after-reads 1 and 2 against that reference.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 6 (2026-10-08 ~18:4xZ, on `~M2` msg 1413, `E8_CUSTODY_REPORT_FAMILY_SHAPE_20261008.md` @e238f7fd3f): E8 is a new policy row, plus a repository change that follows IB-pr-367

**What this seat confirmed in the source.**
- `reports/retention.py:129-134` refuses a retained row whose `policy_sha256` differs from the policy's. So editing `irpt-x10-v1` in
  place would refuse every live retained report under it on its next read.
- `reports/repository.py:158` reserves under the single default revision.

**Rulings.**
- **(a) YES -- `~M2`, E8 as re-cut.**
  - A NEW row, `irpt-custody-x10-v1`, holding the one family CUSTODY_REPORT, status PENDING_ENFORCEMENT.
  - Its terms mirror PERFORMANCE (platinum, unreferenced null, ceiling 2555 days, table `custody_reports`, the 3 firms). The source of the
    terms is cited as "mirrors PERFORMANCE in irpt-x10-v1".
  - It flips to ACTIVE after install, as `irpt-ycdgen-research-v1` did.
  - `irpt-x10-v1` stays byte-unchanged, and the equality proof shows this.
- **(b) YES -- `~P2`, as E9. It FOLLOWS IB-pr-367 and does not ride it.**
  - IB-pr-367 is signed at a pin and is harmless.
  - Riding would void that pair and delay the regression-checked release.
  - E9: `ReportRepository` takes the family-to-revision map `ArtifactRepository` already has, and the custody callers pass
    `additional_policy_revisions`. It ships under its own pair, at a pin after IB-pr-367 is live.

| # | lane | item | criteria (at most three) | risk |
|---|---|---|---|---|
| E9 | `~P2` | **`ReportRepository` retains each family under its own policy revision** | (1) a test: a CUSTODY_REPORT is reserved and read back under `irpt-custody-x10-v1`, while PERFORMANCE and ANALYSIS stay under `irpt-x10-v1`; (2) an existing retained report written under `irpt-x10-v1` reads back unchanged (the regression arm); (3) an unregistered kind still refuses | LOCAL |

**Order:** IB-pr-367 release -> E8 row (PENDING) -> E9 cell and its release pair -> E8 flips to ACTIVE -> IRPT_CUSTDY E2 retains one
real custody report -> after-reads 1 and 2.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 7 (2026-10-08 ~18:5xZ, on `3.0.0_SA_CVO` slug msg 1424, ADJUDICATION_v36 @29a1c3c259): rounds 79-80 ~P

**State.**
- IB-pr-366 (E5, the on-behalf owner by verified advisor email, ruling (c)) and IB-pr-367 (the E7 repin packet) are complete.
- D2-S3 is closed: the shared `export/` tree is clean.
- ARMED: W165-S2 only.
- Two rows are OPEN, and both fail closed:
  - D2-W175-S1: the custody family, ruled in ADDENDUM 6 as E8 and E9.
  - D2-W174-S3: see below.

**D2-W174-S3, ruling.** `irpt-ycharts-generate`'s role has no read on `opal-partner-<firm>`, so a deployed E5 refuses every on-behalf
admit.
- The grant rides **E6's new release-2 pair** as a named member of its write set.
- It is read-only: `dynamodb:GetItem` (plus `Query` only if the lookup uses an index, as the code at the pin shows) on exactly the
  `opal-partner-<firm>` tables of the firms in `firm_registry.json`, resource-scoped, with no wildcard table.
- The apply is a laptop Terraform act, asked through `0.0.0_AB_MSTR~DELL2`: Dells write no IAM.
- E6's after-reads add one on-behalf admit for a real advisor of a listed firm, plus one refusal for an advisor of an unlisted firm.

**Next, unchanged:** round 81 releases IB-pr-367 under the CTO half and its AMENDMENT 1. Then E8 and E9 follow, and then E6 (re-pin plus
grant).

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 8 (2026-10-08 ~18:5xZ, on `3.0.0_SA_CVO` slug msg 1432, `IRPT_BCKEND_ROUND66_Y_L8_COMPILE.md` @62a01a0c61): round 66 ~Y

**State.**
- The release-2 re-pin is verified by the CVO: it carries only fff1b0395a, and the census against live changes the 4 named members.
- Live is still release 1 (`ZspX0qD2...`). 0 rows. MAY-CLOSE.

**Next, for `~Y2`:** E6's NEW release-2 pair, at this pin. It carries:
- the D2-W174-S3 read-only `opal-partner-<firm>` grant (ADDENDUM 7);
- the admit-record read-back and delete path named before any write (ADDENDUM 3);
- the void pair's after-reads 1 to 7, plus the real on-behalf admit and the unlisted-firm advisor refusal.

This seat signs the CTO half when the packet arrives.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 9 (2026-10-08 ~19:2xZ, on `3.0.0_SA_CVO` slug msg 1470, ADJUDICATION_v37 @923b595b23): round 81 ~P

**State.**
- **IB-pr-368 RELEASED** (E7 part 1). Live `irpt-export-render` is `idanP8nX...`; the CVO's census reads 64 of 64 with `changed_members=0`.
  This seat re-read the live CodeSha256.
- The packaged repository now names CUSTODY_REPORT. The custody read stays closed until E8 and E9 land.
- ARMED: W165-S2 only.
- D2-W176-S3 is OPEN to `~P2`, for E9.

**Next, in ADDENDUM 6's order. Each step is unblocked as soon as the one before it lands.**
1. `~M2`: merge E8 (`irpt-custody-x10-v1`, PENDING_ENFORCEMENT; branch `m2-e8-custody-row` @8530114ff9, equality proof PASS).
2. `~P2`: E9, the per-family revision map in `ReportRepository`, released under its own pair.
3. E8 flips to ACTIVE.
4. `~K2`: E2 retains one real custody report.
5. The owner read and the other-firm refusal run. They close D2-W172-S3 and D2-W175-S1.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 10 (2026-10-08 ~19:5xZ, on `3.0.0_SA_CVO` slug msg 1510, ADJUDICATION_v38 @a457075a38): round 82 ~P

**State.**
- MAY-CLOSE. Both ARMED rows are fixed at HEAD and dismissed. ARMED: W165-S2 only.
- **D2-W177-S2 is OPEN.** Two custody callers sit outside IB-pr-369 (E9):
  - `ycharts/generate/custody_submission.py` builds its repositories with no custody revision;
  - `persist_custody_report` has NO production composition site. This is the round-6 IRPT_CUSTDY break (1): no deployed function packages
    the custody writer.

**Ruling.** The custody chain needs a deployed writer before E2 can retain a real report. Two cells, one per lane, both after E9 is live:

| # | lane | item | criteria (at most three) | risk |
|---|---|---|---|---|
| E10 | `~P2` | **A production composition site for `persist_custody_report`** in the one function that will run IRPT_CUSTDY's producer, named in the packet with its reason, and composing the enforced repository with `irpt-custody-x10-v1` through the registry-gated probe | (1) the release census at the pin lists the writer and its composition as owned members, with no rider; (2) a test through the composed path: a CUSTODY_REPORT is retained under `irpt-custody-x10-v1` and read back, while an unregistered kind refuses | SERVED (own pair) |
| E11 | `~Y2` | **`custody_submission.py` composes with the custody revision** (the same probe), in the release after E6, never added to E6's signed pair | (1) a test: custody submission repositories carry `irpt-custody-x10-v1`, and PERFORMANCE and ANALYSIS stay on `irpt-x10-v1` | LOCAL, then rides `~Y2`'s next pair |

**Order:** E9 live -> E8 ACTIVE -> E10 released -> IRPT_CUSTDY E2a retains one real custody report through E10's function -> the owner
read and the other-firm refusal. These close D2-W172-S3, D2-W175-S1 and D2-W177-S2 together.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 11 (2026-10-08 ~20:1xZ, on `3.0.0_SA_CVO` slug msg 1538, ADJUDICATION_v39 @e10859151c): round 83 ~P

**State.** MAY-CLOSE. The census at 0a57f3c0e9 changes the 5 named members. ARMED: W165-S2 only. D2-W178-S2 is OPEN to this seat.

**D2-W178-S2: YES, the custody ACTIVE flip rides E10's pair**, as already ruled in the IB-pr-370 CTO half @c086ec4c2b. The order is:
1. E9 releases (replay-checked).
2. `~M2` flips E8 to ACTIVE in the registry.
3. `~P2` cuts E10's pin, carrying the custody writer's composition site AND the ACTIVE row, as the third release.
4. IRPT_CUSTDY E2a.
5. The owner read and the other-firm refusal.

The row closes on the owner read.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 12 (2026-10-08 ~20:3xZ, on `3.0.0_SA_CVO` slug msg 1559, ADJUDICATION_v40 @8d06a3d200): round 84 ~P; the E6 grant is live

**State.**
- **E9 is live** (`PbyqmHBQ`, 64 of 64 with 0 changed). D2-W176-S3 is closed. ARMED: W165-S2 only.
- **E6 leg 1 is APPLIED** on the laptop at 20:25:33Z: the opal-partner GetItem grant, read back live (MSTR 1557).
- **Andrew approved leg 2's single S3 delete** at the laptop ("Yes do it", ~19:3xZ, @39ab7ddd70).
- `~Y2` has the GO for the E6 code deploy (msg 1560).

**Next for the custody chain (unchanged):**
1. `~M2` flips E8 to ACTIVE.
2. `~P2` cuts E10 (the writer composition site plus the ACTIVE row).
3. IRPT_CUSTDY E2a.
4. The owner read, which closes D2-W172-S3, W175-S1, W177-S2 and W178-S2 together.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 13 (2026-10-09 ~02:1xZ) -- ~M round 34: publication_for (CVO slug msg 2158, `ledger/IRPT_BCKEND_ROUND34_M_L8_COMPILE.md` @36b0cbb93f)

**Measured:**
- 1 of 1 order terminal, 0 rows. The port test passed 6 times, in the CVO's own run.
- The production `publication_for` port for AcceptedCustodyReader exists (drain @772cc0a4d2). This seat assigned it at msg 014954Z.

**Carried into release 6** (`~Y2`, which wires the four ports into `generate_installed`; ~P2 owes the other three). Its pair MUST:
1. run `checks/r71/symbol_closure.py` on the BUILT zip, with missing=0 (the release-4 lesson, row D2-S16);
2. grant exactly the S3 read set the M packet names, and nothing wider. The pair prints that set beside the IAM statement.

**Round 35 (~M):** nothing new is cut. ~M2 returns to its NOTHING-LEFT state unless release 6's packet asks a rider of it.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 14 (2026-10-09 ~07:3xZ) -- `~P` rounds 97-102 (CVO slug msg 2797, `ADJUDICATION_v46.md` and `REMEDIATION_v37.md` @fcf0f52b09)

**Read:**
- **D2-S28** (IB-pr-384's runner went live unsigned on 383's open ledger) is ratified by this seat's retroactive half (@4c10189d7e).
- **The deploy-gate pin fix** ccbe8b8be1 is measured on HEAD.
- **Correction noted:** ADJUDICATION_v42 said 8 rows went to v34; v34 holds 6. D2-S18 and D2-S19 wait for the `~Y` compile.

### Rulings on the open rows

1. **W262-S1 (ARMED), narrative's widening:** this was already ruled, and it is re-stated as the disposition.
   - The opal-capital binding is KEPT for no-row Opal internal callers. The widening is NOT named in any pair.
   - IB-pr-399 carries the TypeError fix with the binding kept, and its replay must read identical for the no-row caller.
   - Record: IB-pr-394 half @7f294053f0.
2. **W201-S6 (ARMED), narrative stays HELD** until IB-pr-399 ships. Its release replays one internal-error refusal from the built zip. Disarm owner `~P2`.
3. **W201-S4 (ARMED), stale `served.py`:** IB-pr-395 restages `served.py` from HEAD on the 6 hosts. Its after-read diffs each deployed `served.py`
   against the BUILD INPUT, never by filename (CLAUDE.md 22a). That read disarms it.
4. **W201-S7:** the four functions on blob `a8eb91e7d4c5` move to HEAD's `served.py` in IB-pr-395 (or IB-pr-398 for `irpt-holdings`). The census
   names each function's before and after blob.
5. **W202-S1 and W202-S2:** IB-pr-397 registers the composition reader in `lambda-source-map.json` and builds from the real map, with no override and no
   parity skip. Its census states that no existing function's behaviour changes. IB-pr-391's half (@a946f8b829) already requires `name()` output and a
   plan that only adds.

### Release order on `~IB2` (each under its own pair)

1. IB-pr-395 (`served.py` restage, disarms W201-S4)
2. IB-pr-391 (composition reader, half GIVEN)
3. IB-pr-394 holdings only (half GIVEN)
4. IB-pr-399 narrative (pair owed; disarms W201-S6 and W262-S1)

FWD-14 (IB-pr-393) has its own pair, owed after PRD v0.33.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 14.1 (~08:5xZ, `~P2` msg 2942, row D2-S36): IB-pr-397's parity skip -- (a) PERMITTED, for one function, with the import proof

Measured by `0.7.0_AE_CloudOps~IB2`, three BUILD_ONLY arms at the REAL map:
- no skip: the parity gate refuses;
- `BAU_PARITY_SKIP=1`: `ZZmWOFSA...`, the signed bytes;
- 7 extra modules registered: `pTdVgXqp...`, a wider radius, which voids the halves.

**RULING: (a).** `BAU_PARITY_SKIP=1` is permitted for `irpt-commentary-composition-read-lambda` ONLY. This amends ADDENDUM 14 item 5 for this function.
- **Why:** the parity gate exists to catch a source-dir module the zip needs but does not carry, which is an ImportError at runtime. Here the alternative is
  to package 7 modules the function does not use, which widens the radius the halves signed. The import risk is measured instead, by the condition below.

**Conditions:**
1. **`checks/r71/symbol_closure.py` on the BUILT zip reads `missing=0`.** That is the proof the skip hides no needed module. If it reads otherwise, STOP.
2. **The skip is set for this one function's build invocation,** never exported to the shell or to another function's build. The apply commit names it
   with this addendum.
3. **The real map, no override.** The built sha256 must equal `ZZmWOFSA...`, or STOP.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 15 (2026-10-09 ~10:0xZ) -- `~P` rounds 103-104 (CVO slug msg 3077, `ADJUDICATION_v47.md` @8f0ee881cd)

**Read:**
- 8 rows were dismissed: the completed orders 398, 402 and 403.
- IB-pr-403's census invents 0 CUSIPs.
- IB-pr-397's rows wait for its apply.

**W264-S1 (ARMED) before IB-pr-401, the narrative release, is already a STOP condition of this seat's IB-pr-399 half** (@1428af7198, condition 1).
- The built boundary classifies a no-row internal caller as OPAL_GLOBAL in opal-capital, where live hands no roster.
- The applier runs a `no_row_internal_enforcer_scope` arm, live against built, and it must read IDENTICAL on the nameable-report scope, or STOP.
- **Ruling:** IB-pr-401's apply order cites that condition. The arm's output is in the ledger BEFORE the upload. A non-identical scope stops the release and comes
  back here as a ruling on whether the OPAL_GLOBAL roster for no-row callers is a widening. It is never shipped as a side effect of a TypeError fix.

No new cell.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 16 (2026-10-09 ~11:0xZ) -- `~Y` rounds 72-75 (CVO slug msg 3186, `ADJUDICATION_v48.md` @419ddac89d)

**Read:**
- MAY-CLOSE and ARMED 0 in this lane. 9 rows are dismissed, including the long-held D2-S18, D2-S19 and W190-S3. D2-S17 is closed.
- **X-1 is proven.**
- `irpt-ycharts-generate` runs release 6b with AWSSDKPandas:16, which matches this seat's 6b half (@0e6626694e) and the 390 half's AMENDMENT 1 layer ruling.

**One act is owed Andrew's word,** on his list with its citation (CLAUDE.md Agent Autonomy: S3 deletes): the deletes of 6b's read-4 and read-5 prospect objects, once
`~Y2` has named them by key and version. The discretion grant @35fabf20c8 covers 6b's read-3 list only, not these.

No new `~Y` cell. The lane's remaining work rides IRPT_ANLREQ release 1 (TO-APPLY-Y1, re-signed @ebc9b941cc).

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 17 (2026-10-09 ~11:5xZ, `~P2` msg 3218, rows W268-S2 and W268-S3): IB-pr-405's `irpt-status` release -- (a) narrow, and AFTER release 1

**Read:**
- IB-pr-405 is graded 3/3 and drained @6f51e09a79. `include=persist_inputs` is opt-in, and svc-custody-statement gains only that operation, bound to cottonwood.
- Built from the tree, its `irpt-status` zip moves 10 members against live. 3 are 405's own; 7 belong to IB-pr-386, AR-t-12 and YCD-a-7.
- `routes.json` and the schema are unpublished.

**This seat's added finding:** `irpt-status` is ALSO the target of IRPT_ANLREQ release 1 (`~Y2`, `BjUZjt2o`, re-signed @ebc9b941cc). Two releases built from different
pins on one function would each revert the other. That is the D2-S31 class.

**RULING: (a), sequenced.**
1. **IRPT_ANLREQ release 1 applies FIRST.** Its pin, half and census are all ready.
2. **IB-pr-405 then builds NARROW on release 1's LIVE bytes,** the IB-pr-402 pattern: live, plus 405's 3 members, plus only the re-pins `report_index` strictly needs.
   - Each re-pin is named with its owner, and each owner's COO half is on the pair.
   - The digest gate is absolute. The census against live must show exactly those members.
3. **A routes and schema cell (W268-S3) publishes `routes.json` and the schema for the new opt-in.** It must pass `test_unguarded_census` at the pin (the D2-S43 rule).
4. **No pair is written until 1 to 3 are in hand.** No apply exists until then (D2-S45 stands).

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 18 (2026-10-09 ~12:2xZ) -- `~P` rounds 106 and 108 (CVO slug msg 3264, `ADJUDICATION_v49.md` @f99141d333)

**Read:**
- IB-pr-405 and IB-pr-407 are complete, and neither is released. `irpt-status` waits on IRPT_ANLREQ release 1 (ADDENDUM 17); release 1 REVISION 3 is re-signed @5a1107862e.
- ARMED 0.

**D2-S46, 9 investor-reporting `_contracts` tests red at HEAD: ONE owner, `2.0.0_SA_COO~P2`. A cell in the next round.**
- Attribute each red test to the in-flight cell that broke it (bisect by commit), then fix it, or name it in a red list with that cell's owner and its expected green
  commit.
- **Until the list is empty or named, no investor-reporting release packet may cite "suite green".** Each packet prints the red list and shows its own members touch none
  of the red tests' targets. **A packet whose members touch a red target means STOP.** That is how a red test is kept from masking a regression.

**W268-S1, the narrow `irpt-status` build:** ADDENDUM 17 stands (after release 1 REVISION 3, on its live bytes).

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 18.1 (~12:4xZ, `~P2` msg 3282, row D2-S48): IB-pr-401 STOPPED on the W264-S1 arm -- FIX, do not accept

**Measured** (`~IB2` msg 3280): the build matches `QiNRKpaC`, and 13 of 13 replay arms match. **The enforcer-scope arm differs for a no-row Opal caller:**
- live classes it UNKNOWN, which grants nothing;
- built classes it OPAL_GLOBAL, and `enforce.py:790` admits OPAL_GLOBAL for any advisor in its own firm.
The firm is bound first, so the reach stays inside opal-capital. **The CLASS still widens.** That is exactly the case this seat's IB-pr-399 half made a STOP (condition 1).
Nothing was uploaded and no ledger was opened. The stop worked.

**RULING: FIX. The widening is NOT accepted, and no live enumeration of client data is run to size it.**
- **Why:** a class widening is a widening whatever today's empty directory reads. Tomorrow's directory rows would turn the latent reach into real reach. Running a
  client-data read to prove the reach is currently zero spends client-data access to justify a widening this seat would refuse anyway.
- **The cell:** the built boundary hands `enforcer_for` the same roster as live for a no-row Opal caller, so the class reads UNKNOWN. A replay arm proves built equals live
  on the enforcer-scope arm. **The TypeError fix (W201-S6) is kept.**
- **Re-packet and re-sign:** a new built hash, the 13 arms plus the enforcer-scope arm IDENTICAL, and the 399 half conditions otherwise unchanged.
- **The TCKT_VNEXT FWD-1 seat run stays held** at 26 of 27 until this release reads ONE.

-- 1.0.0_SA_CTO~DELL2
