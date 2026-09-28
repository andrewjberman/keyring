# NFRA_MCPORTAL -- ROUND 2 ANALYSIS (L10), `1.0.0_SA_CTO~O`, 2026-09-28 ~20:1xZ

**L10 on `3.0.0_SA_CVO~O`'s slug** (msg 20260928T153830Z; `ADJUDICATION_v2.Z.md` C-S12..C-S21 and
`REMEDIATION_v2.Z.md` @00e8eea2da). Both files and the round's five proof-of-spec files were read to the end. The grade
tokens are `REALIZED | NOT_REALIZED | DEFERRED | HELD`. **The issuer is now `2.0.0_SA_COO~MP`** (placement @094c84f299,
one COO per project); it recuts round 3 in ONE issuance. The three open rows the slug assigns to `2.0.0_SA_COO~O`
transfer to `2.0.0_SA_COO~MP` with the project.

---

## 1. L7, L8 and L9 accepted

- **L7:** 6 of 6 orders are terminal. MP-b-1, b-2, d-1, g-1 and p-1 are complete, each with every acceptance row PASS.
  MP-a-1 was superseded in place @4d2b2a6a51, never spawned, because its spawn precondition G-HDR is Andrew's act.
  Nothing was re-graded by that close.
- **L8:** 11 of 11 rows dispositioned: 8 dismissed with reason and 3 graduated OPEN (Z-W2-S3 ARMED, Z-W1-S5, Z-W2-S6).
  The fold reads 0 of 25 undispositioned.
- **L9:** VACUOUS with its cause named (C-S21). 0 of 13 order files carries `judgment="true"`. Round 3 must carry one
  (section 4, item 5).
- **W1-S1 (round 1, ARMED, disarm owner this seat):** disarmed by this seat's act 6bc980ad5d, which touches only
  `.tools/owned-paths-validate.py` (C-S13 read it). The REMEDIATION_v1.Z row still reads OPEN; the CVO flips it.

## 2. What round 2 put in the world (measured, not reported)

- **The gateway serves the dashboard and the owner gate LIVE.** MP-d-1 deployed `1f7128201a`: its AC3 read, over SSM on
  `i-07dccb1615503ac99`, `/health` 200, `/api/admin/whoami` 401 and `/` 401 with no identity. The later OPLGTW release
  `6a98a0553a` (the current `deployed_commit` in `infra/aws/ec2/EC2_MANIFEST.json`, 2026-09-27T22:17:33Z) still carries
  it: `1f7128201a` is an ancestor of `6a98a0553a` (positive control run beside it), and `app/owner_gate.py` and the
  `/changes` route are present in that tree's bytes.
- **The grant writer is built and NOT applied.** MP-b-1 proved the staged package imports in-zip. MP-b-2 built both
  owner-key branches (`oid` and `sub`) and the writer's own record table in Terraform, and ran the in-package handler
  with no owner header: `REFUSED NO-OWNER-HEADER`. Nothing in `mcportal_grant_writer.tf` is applied.
- **The header measurement is BUILT, NOT TAKEN.** MP-g-1 logs `OWNER-HEADER-CLAIMS keys=...` (claim keys only) the first
  time the owner opens the dashboard. Andrew has not opened it since the release, as far as any record shows; that act
  is G-HDR.
- **The history reads the writer's table** (MP-g-1 AC2, including the 503 when the table is unreachable), and the client
  refuses a non-JSON response (MP-p-1). The table the history reads does not exist yet.

## 3. Outcome grades

| FWD | grade | why |
|---|---|---|
| FWD-1 | NOT_REALIZED | The served half moved: the gateway, the gate and the handlers are live. The writer is not applied, so no grant has been changed from the dashboard. The one step between here and the close run is MP-a-1, held on G-HDR. |
| FWD-2 | NOT_REALIZED | One arm is exercised LIVE: an unauthenticated request is refused on `/` and `/api/admin/whoami`. A2's arms are not: a second SIGNED-IN Opal account refused (403) on every page and write handler with the denominator printed, `/sprint` served to it, and Andrew admitted. |
| FWD-4 | DEFERRED | The cross-principal history is built against the writer's table (R-4). Revert-as-a-write (A4) is not cut. The history's minimum rides FWD-1's close run. |
| FWD-3, 5, 6, 7, 8, 9, 11, 12, 13 | DEFERRED | Enrichment rounds, in Andrew's page order, after FWD-1 is REALIZED. |
| FWD-10 | DEFERRED | Round 1's ruling stands: the call log and the person and server stop use the FILES and do not wait on G-OPLGTW. |

Tally: 0 REALIZED, 2 NOT_REALIZED, 11 DEFERRED. No FWD is HELD; one CELL is (MP-a-1 on G-HDR).

## 4. Rulings

**R-7, G-HDR is an act on demand, not a wait.** It is Andrew opening `https://mcp.opalinvest.dev/` once, signed in. The
issuer's first act of round 3 reads the journal for the `OWNER-HEADER-CLAIMS` line. If it is there, MP-a-1 is cut in the
same issuance. If it is not, the issuer sends Andrew ONE card naming that act, and cuts MP-a-1 with G-HDR as its stated
spawn precondition; the rest of round 3 does not wait on it. The PyPI fetch MP-a-1 needs is the G-PYPI word recorded in
the round-2 spawn note; the issuer re-reads that record before the cut and cards it if it does not cover a new round.

**R-8, on Z-W2-S3 (ARMED): the fixture, as the issuer planned (Z-S5).** The gateway suite points `AUDIT_PATH` at a temp
file through a session fixture. The code default at `app/config.py:307` does not change, because the running gateway's
env sets it. Disarms when a full suite run leaves `infra/aws/ec2/opal-gateway/audit.jsonl` unmodified (`git status
--porcelain` on that path empty, with a planted append as the positive control).

**R-9, on Z-W1-S5: folded into the MP-a-1 re-cut.** `infra/aws/lambda/ci/lambda-source-map.json` still names
`MCPORTAL_OWNER_OID` once (read ~20:1xZ). The re-cut adds that file to MP-a-1's `<paths>` and replaces the note with the
two variables MP-b-2 introduced, `MCPORTAL_OWNER_KEY_CLAIM` and `MCPORTAL_OWNER_KEY`.

**R-10, on Z-W2-S6: NOT this project's remedy; subtracted.** `file_checksums` is a fabric-wide manifest field: 19 of 27
services in `EC2_MANIFEST.json` carry it, and no tool under `.tools/` or the deploy scripts reads it as a gate (one
terminal NFRA_OPALAI check script reads it). Retiring or refreshing it for one service would make the manifest
inconsistent. The row stays OPEN and INERT with the issuer, re-routed to the manifest writer's owner (the CloudOps lane)
as a fabric item. Until then, every gateway release face in this project reads `deployed_commit` and the tree's bytes,
never `file_checksums`.

**R-11, on C6 (the pre-draft `deliverables/1.0.0_SA_CTO~O/ROUND3_ENRICHMENT_DRAFT_C6.md`): ADOPTED, cut in round 4.**
Both of its gates now hold (G-OPLGTW lifted 2026-09-26; OPLGTW re-seated @6fba157e76). It is not cut in round 3 because
it changes what EVERY caller is allowed and its step 3 extends the writer, which does not exist yet. It heads round 4's
list, cut the round after FWD-1 grades REALIZED. The contract amendment in its step 1 is this seat's act at that cut.

## 5. THE ENRICHMENT LIST ROUND 3 CUTS (ONE issuance by `2.0.0_SA_COO~MP`)

In order, with dependencies. A build order carries at most three mechanical criteria.

1. **E1, the G-HDR read** (R-7). WORLD, read-only: the latest `OWNER-HEADER-CLAIMS keys=...` journal line, keys only.
   Its output picks MP-a-1's branch. If the line is absent: ONE card to Andrew, and item 2 cuts with G-HDR as its spawn
   precondition.
2. **E2, MP-a-1 re-cut: the writer's apply** (unchanged from round 2, plus R-9). The layer build, the targeted
   `safe-apply` of `mcportal_grant_writer.tf` only, the NEVER-2 ledger, the live refusal invoke, and the source-map note.
   If the header lacks `oid` or `iat`, the C4 wording addendum is signed before the apply (round-1 R-2 stands).
3. **E3, the batch cell:** R-8's audit fixture. LOCAL.
4. **E4, FWD-2's live arms (A2).** WORLD. One signed-in Opal account other than Andrew's, one request per page and per
   write handler, denominator printed, each 403; `/sprint` served 200 to the same account; Andrew's own request admitted.
   The issuer names the account at the cut. If no second account can sign in without a colleague's hands, that arm is
   ONE card to Andrew and the rest of the cell runs.
5. **Close run, FWD-1 LIVE (A1 plus A1n), after E2.** Andrew narrows one colleague's data grant from the Entitlements
   tab; the colleague's next MCP call is answered within the new limit and no wider; the grant is widened back; both
   writes show in the history. A1n's four negative arms run LIVE against the applied writer, each refused before any
   store call.
   **JUDGMENT criterion (WORLD, graded by `3.0.0_SA_CVO~O` at L9, never self-graded):** from the colleague's actual MCP
   exchange before and after the narrowing (transcript committed, values the grant covers redacted), judge that the
   narrowed answer is a REAL answer confined to the new grant, not an error, an empty result, or a refusal that happens
   to pass the mechanical check, and that the widened-back answer matches the original. This is the plausibility oracle
   the round-2 grid lacked (C-S21).

**Subtracted from round 3, with the reason for each:**
- C6 (R-11): round 4, after FWD-1 is REALIZED;
- the remaining pages (FWD-3, 5-9, 11-13) and revert-as-a-write (FWD-4's A4): they follow FWD-1 in Andrew's order;
- Z-W2-S6 (R-10): a fabric item, re-routed to the manifest writer's owner.

## 6. What this analysis does not do

- It does not read the journal. E1 does, and R-7's branch is chosen there.
- It does not change the ENDPOINT. A C4 wording addendum, if E1 triggers one, is CONTRACTS only.
- It does not touch NFRA_OPLGTW's store, contract or record types; C6's contract amendment waits for round 4.
