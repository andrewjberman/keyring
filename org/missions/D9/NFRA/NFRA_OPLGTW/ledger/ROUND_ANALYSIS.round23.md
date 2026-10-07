# NFRA_OPLGTW -- ROUND 23 ANALYSIS (L10), `1.0.0_SA_CTO~O`, 2026-10-07 ~02:1xZ -- r23 live; round 24 = the send split and the gate lookup

**L10 on `3.0.0_SA_CVO~O`'s round-23 slug** (msg 30508, `surprise-channel/remediations/REMEDIATION_v10.md`
@c883f56b8c; graduated by `adjudications/ADJUDICATION_v15.Z.md` C-S41):
- 3 OPEN for this seat: Z-S63, Z-S61, Z-W28-S7.
- 1 OPEN for the issuer: Z-W28-S9. Z-W28-S2 is still open from v9.
- Z-W28-S1 is REMEDIATED in place (C-S43).
- The channel reads 0 OPEN and 0 ARMED of 381.

## 1. What round 23 did

- **OG-q-8** built R29: `position_cusips` drops None and whitespace-only values.
- **OG-rl-10 (R32, the hotfix, workstream PORTAL-LOGIN-HOTFIX).** r24 @9d3e2eb3fc went live 2026-10-06T23:59:57Z.
  - The `opal_portal` login moved from the raw API Gateway host to `www.opalinvest.dev`.
  - Cause: the auth Lambda's origin gate (NFRA_OPSEC202609 OP-s-3) refuses a request that did not come through
    CloudFront.
  - R32 is on record in `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_NEVER_WIDEN_HALF_OG-rl-10_20261006.md`
    @d274986e8d.
- **OG-rl-9 (re-cut).** r23 @7d65a28db0 went live 2026-10-07T01:30:43Z on `9d3e2eb3fc`.
  - The real holder reads 2150 rows on the query and the download path, with 0 blank and 0 unheld.
  - `/rivalfunds/{day}/audit` is served.
  - The CVO re-ran q8.AC1-AC2 and rl9.AC1-AC3: all PASS.

## 2. Outcome grades

**0 REALIZED, 0 NOT_REALIZED, 8 HELD, 0 DEFERRED** (round 22: 0 / 1 / 7 / 0).

| FWD | grade | basis |
|---|---|---|
| FWD-3 (each person sees only the information granted to them) | **HELD** (was NOT_REALIZED) | The measured violation is gone: 2150 of 2150 on both paths (Z-W28-S1 REMEDIATED). It returns to the walkthrough, OG-v-7. |
| FWD-4 (Menachem downloads the same approved information he can query) | HELD | Download equals query, and both equal the held set, for the one real holder. Menachem's own run waits on G-E. |
| FWD-1, 2, 5, 6, 7, 8 | HELD | Unchanged: OG-v-7, G-E and R7's host-side flag. |

## 3. Rulings

**R33 -- Z-S63: the real send is split, and a re-send does not re-fire.**
- Measured by the issuer: `opal_data_refresh_upload(confirm=True)` polls the pipeline for up to 15 minutes inside one
  MCP call. The client transport drops near 120 s. 2 of 2 real sends on 2026-10-07 lost their response although
  each send landed.
- The tool keeps its name and its parameters. A real send returns right after `/trigger` with the execution id and
  the status it read once. It never polls past 60 s inside the call.
- A NEW read-only tool carries the polling: status by execution id, and the served manifest's displayed date.
- **Idempotent re-send.** A `confirm=True` call for a date whose two files (name and size) equal those of a trigger
  this process made in the last 30 minutes returns that execution id with `already_triggered: true`. It does NOT
  call `/trigger` again.
  - The record is in-process. A gateway restart clears it, and the cell's test names that limit.
- This is a gateway tool under `app/integrations/opal_portal/`. It is not under `integrations/bloomberg/`, so
  Andrew's no-modify order (record `ANDREW_DIRECT_20261006_201xZ_...`) does not reach it.
- The two caller skills (`.claude/skills/terminal-upload`, `.claude/skills/bbg-daily`) state the new read in the same
  cell: after a send, read status; never re-send on a dropped transport.
- **Until it ships,** the caller of a real send reads the portal's displayed date before any re-send. A dropped
  transport is not a failed send.
- One read is owed in the same cell: whether the 01:26Z send overlapped the gateway restart at 01:30:43Z, and what
  that execution's terminal status was.

**R34 -- Z-S61 goes to the owner of `.tools/safe-merge.sh`.**
- The last 8 of 8 commits on that file are `0.0.0_AB_MSTR` or `0.0.0_AB_MSTR~Z`. This seat asks `0.0.0_AB_MSTR~Z`.
- Candidate guard, the issuer's: after the merge, `git diff --cached --quiet` over the drained paths; refuse to
  report a drain landed while the index disagrees with HEAD.
- The cause stays INFERRED. No OPLGTW cell is cut for it.

**R35 -- Z-W28-S7: the halt gate reads the order from the shared root, and the form names the deploy identity.**
1. The gate's order lookup reads the deploying seat's order from the SHARED root, not from the release tree's HEAD,
   and reads the LAST `<status>` tag. One cell, with a fixture: a release tree cut on a sha that predates the slot's
   first order. Expected: the gate finds the order and proceeds; a `[STOP]` still halts.
2. The issuer writes the deploy identity into `RELEASE_ORDER_FORM.md` as a standing step. Until cell 1 ships, that
   is the issuer-serial route, under which a `[STOP]` to the issuer halts the deploy. The form also names who
   commits `EC2_MANIFEST.json`, and on which branch.

**The issuer's rows:** Z-W28-S9 (a per-run scratch name on the host runner) and Z-W28-S2 (operator-command output)
are order-form edits, made at the next form edit. No cell.

## 4. Enrichment list for round 24 (ONE issuance)

1. **R33 cell:** the send split, the status tool, the idempotent re-send, the two skill texts and the 01:26Z read.
   At most three mechanical criteria.
2. **R35 cell 1:** the halt gate's order lookup, with its fixture.
3. **The release** of cell 1 under the usual three halves.
   - It adds one tool, so R21's route and tool arms apply.
   - Post-release read: a `dry_run=True` call, and the status tool on a known execution id. No `confirm=True` is run
     by this project.

After round 24 the project parks again on OG-v-7, G-E and R7's flag (R28).

## 5. What this analysis does not do

It deploys, applies and grants nothing, and it amends no PRD text. It re-measures nothing beyond the slug, the
deploy commits and `git log` on the two tool files.

-- 1.0.0_SA_CTO~O
