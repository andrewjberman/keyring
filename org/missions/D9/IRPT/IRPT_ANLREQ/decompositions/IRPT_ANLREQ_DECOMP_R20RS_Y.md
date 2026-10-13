# IRPT_ANLREQ -- decomposition, round 20 ARTIFACT RESTORE, workstream YR round 9 (issuer 2.0.0_SA_COO~Y2)

**Input:** a measured incident of this round. Two status-rule rebase workers (`~62`, `~64`, cell `AR-y-213`) ran `BUILD_ONLY` at candidate base commits that PREDATE the BUILD_ONLY guard of `infra/aws/lambda/ci/build-and-upload.sh`; at those commits the script uploads. The S3 key `investor-reporting/irpt-holdings.zip` in `opal-313476888478-lambda-artifacts` received three new versions today (`T1NEd9G.` 07:42:43Z, `msFi8sD6` 10:52:50Z, `QCyspt0v` 10:53:08Z, the latest; all 294243 bytes, sha256 base64 `tS/APci3Mz/YRDP7pJboAVqKabShek9jYUqvQDIYwwE=`). The live Lambda `irpt-holdings` is still CodeSha256 `SWRfUfHdJarO2Rhbxw/KQK88DeDNorQujkaR1jUuZc0=` (S3 version `dWoiYeH9MSXq9yOuQkApr2h_XxwrvVi8`, 299273 bytes, 2026-10-12T13:51:17Z; MEASURED by this seat: that version hashes to the live CodeSha256). No function was updated. The cause is the ORDER's: it listed candidate base commits without requiring the guard to be present (row `IRPT_ANLREQ-D2-S69`). The other seven artifact keys were read by this seat and carry no write from today's workers.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-215` | the S3 key `investor-reporting/irpt-holdings.zip` made latest-equal to the live package again (a copy of the live version onto the key; the three wrong versions are kept) and read back | one S3 key (a new latest version) and the applier's ledger | WORLD |

## Edges and chains

- None. M = 1 chain.

fanout: 1 of 1 chains, cap 8, reason: one independent repair act on one key.
