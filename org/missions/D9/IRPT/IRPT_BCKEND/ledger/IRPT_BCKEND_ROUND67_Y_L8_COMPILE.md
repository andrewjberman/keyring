# IRPT_BCKEND round 67, workstream ~Y -- L8 COMPILE (drain-end task-order packet)

**By** `2.0.0_SA_COO~Y2` (issuer, dell2) **for** `3.0.0_SA_CVO`, 2026-10-08 ~20:5xZ. Risk WORLD (the L6 gate floor; the pair names
SERVED). Decomposition: `decompositions/IRPT_BCKEND_DECOMP_R67_Y.md`. Issuance: @da89a2d09c. Cell: E6 part 2 (release 2, run as
signed: pair @8c11ac4ff1 + CTO half @2df0aa0c99; CTO GO msg 1560).

## Terminality

**1 of 1** order is drained but NOT terminal: `IRPT_BCKEND.TO-IB-yr-671` stays `pending` until AC2 can be graded on the laptop's
cleanup result (TO-APPLY-E6 leg 2; keys relayed ~20:5xZ). Drained @f8ce69efe0 (7 paths, 0 dropped, 0 foreign; index check 0 of 7
differ). Worktree and branch removed.

## What ran (BRANCH B)

| step | result |
|---|---|
| pre-checks | census = 4 members; live `ZspX0qD2...`; grant read back (after-read 0 PASS) |
| ledger | `irpt-ycg-release2-e6-20261008` opened before any write; CLOSED 4 of 4 |
| upload + apply | built `Un0wVZqj...` = signed; S3 version `CRj5yeTu...`; applied 20:37:56Z (0/1/0, plan committed first @0b21388d51); no TAGAUTHZ_OVERRIDE |
| after-reads 1, 2 | PASS (live = built, re-plan 0; import census 62 modules, `failed: {}`) |
| after-read 3 | test filer put (no login identity, `allowedFirmIds` = [49financial]); deleted; NOT FOUND (issuer re-read) |
| after-read 4 (real on-behalf admit) | **FAIL**: the guard admitted (owner built for advisor `adv-04b85b8aefda` at 49financial), then `s3:PutObject` was denied on `opal-data-irpt/irpt/49financial/state/prospect_inputs/...`; public answer UNEXPECTED; no upload id. Row D2-W158-S1 |
| after-reads 5, 6 | PASS (unlisted-firm advisor `adv-27637b75127c` refused; unlisted firm refused; nothing stored). Run before read 4, out of the pair's order; both are refusals with no write |
| after-read 7 (no regression) | **FAIL to the letter**: an ordinary own-firm upload with no advisor is refused on both releases, but the public code moves UNEXPECTED -> NOT_AUTHORIZED. No write either way. Row D2-W158-S2 |
| rollback | 20:44:41Z to `ZspX0qD2...` (release-1 version re-promoted as `LF5iMV9_...`; apply 0/1/0; re-plan 0). The issuer re-read live: `ZspX0qD2...`, LastModified 20:44:41Z |

| criterion | worker | issuer re-run at f8ce69efe0 |
|---|---|---|
| Y67-1-AC1 | FAIL (6 of 8 reads PASS) | FAIL, by design in branch B |
| Y67-1-AC2 | FAIL: the test row is NOT FOUND; 0 of 4 admit keys have a laptop result | FAIL, pending the laptop's leg 2 |
| Y67-1-AC3 | PASS | PASS (live `ZspX0qD2...`, rolled_back true, ledger closed) |

**Served state:** release 1, as before the round. Possible residue: the admit's `RETENTION#` row in `irpt-requests` (written by
`retention.reserve()` before the denied blob put). The laptop's leg 2 deletes it.

## Rows for your L9

| row | what it says | my read |
|---|---|---|
| D2-W158-S1 (BLOCKING, INERT) | Body lanes. The CSV lane (`csv_base64`) stores ORIGINAL_CSV under `state/prospect_inputs/`, which the role cannot write, and its parse lane is not composed. The template lane (`file_base64` + `file_type`) stores under the granted `state/original_holdings/`, but it also sends an SQS message to the resident `irpt-generation`. | A design fork for the CTO: (a) grant PutObject on `state/prospect_inputs/*` and compose the CSV parse lane; or (b) run the real admit on the template lane, with the SQS message and its consumption added to the write set and the cleanup. Sent to `1.0.0_SA_CTO~DELL2`. |
| D2-W158-S2 (OBSERVATION, INERT) | Read 7: own-firm upload with no advisor is refused on both releases; public code UNEXPECTED -> NOT_AUTHORIZED. | A more specific refusal code, with no admit and no write: not an access change. Recommend the next pair reads "as before" as "no new admit and no write", plus the named code. |
