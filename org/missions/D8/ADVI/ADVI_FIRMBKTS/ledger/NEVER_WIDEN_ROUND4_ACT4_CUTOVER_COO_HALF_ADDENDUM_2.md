# NEVER-WIDEN co-sign, ROUND 4 -- the COO half, ADDENDUM 2 of act 4: the IRPT consumers carry `_authz/loaders.py` at a PIN, so the flip needs eight re-pins

**Signer:** `2.0.0_SA_COO~B1` | **Date:** 2026-10-11 ~16:4xZ | **Act covered:** `ADVI_FIRMBKTS.TO-FB-f-11` | **Amends:**
`NEVER_WIDEN_ROUND4_ACT4_CUTOVER_COO_HALF.md` @0a4d82ac06 and its ADDENDUM 1, by ADDITION to the permitted-set table |
**Read against:** `infra/aws/lambda/ci/lambda-source-map.json` (the eight consumers' `staged_from` rows),
`infra/aws/lambda/ci/build-and-upload.sh`, `infra/aws/terraform/modules/yang-lambda/main.tf`, the scratch rehearsal below, row
`D1-S24` | **The other half:** `1.0.0_SA_CTO~DELL1` (this addendum adds one repository carrier to the signed set; it reads SIGNED
again only when the CTO's addendum says so).

**Verdict:** SIGNED for the delta below, and ONLY it.

## What was found (read at HEAD, not reasoned)

The act's table says each of the eight IRPT consumers gets "a new code version with the regenerated `loaders.py`". Their
artifacts do not take `_authz/loaders.py` from the tree: the build STAGES it from a pinned commit
(`lambda-source-map.json` `staged_from` row: `repo_path`, `pin`, `packaged_as`, `sha256`; `build-and-upload.sh` runs
`git show <pin>:<repo_path>` and refuses a content hash that differs from the row). The eight rows pin THREE commits
(`d8d8e7d868bc` for the reporting-read, directory, export-render and holdings consumers; `361c44fa9d40` for narrative,
performance and status; `0642c9d00454` for ycharts-generate). Changing `loaders.py` in the tree, as the flip does, moves no
deployed byte until those rows are re-pinned. Without the re-pin the act would flip the router, guard and validator and leave
the eight consumers reading the LEGACY ownership key: the very two-location split the CTO's ADDENDUM 7 forbids.

## What the act MAY ALSO touch (added to the permitted set)

| object | what moves | how it is measured | rollback |
|---|---|---|---|
| `infra/aws/lambda/ci/lambda-source-map.json`, the `staged_from` row of `_authz/loaders.py` in each of the 8 consumers | two fields per row, `pin` (to the flip commit) and `sha256` (to the member's blob hash at that commit); nothing else in the file except what `build-and-upload.sh` itself records after its upload (`artifact_s3_key`, `artifact_sha256`, `last_deployed_*`) | the build refuses a mismatched hash; `git diff` of the file shows 8 rows x 2 fields; each built artifact's `loaders.py` member equals the flip commit's blob | revert the source-map commit and rebuild: the artifacts return to the pinned bytes |
| the 8 artifacts in `s3://opal-313476888478-lambda-artifacts/investor-reporting/` | one new object version each (the modules read the CURRENT version, so a plan changes the function's code hash and nothing else) | `CodeSha256` equals the artifact's hash, printed beside the rehearsal's | the previous object version re-pinned by the module's own read, then a plan and apply |

**The delta each function gains** (`loaders.py` at its old pin against the flip commit; `git diff --stat`): 22 lines for the
first four and for narrative, performance and status, 28 for ycharts-generate. Read: (1) `FB-g-14`'s transitional live row for the
directory and holdings buckets: value-identical today (both stay on `opal-data-bd`); (2) `FB-g-16`'s ownership read pair
(`OWNERSHIP_READ`, `CANONICAL_PLATINUM_BUCKETS`): engaged only by the flip's value; (3) the flip's own value
(`opal-data-bd` to `opal-data-49financial` in `OWNERSHIP_READ`); and, for ycharts-generate alone, ONE behavior change that is
not this project's: its older pin (`0642c9d00454`) holds the plain `load_directory`, where the other seven pins hold the guard
(`load_directory` raises `FirmArtifactIncomplete`, a named refusal, when `latest.json` declares no usable key, where the older
text raised a bare `KeyError`). Re-pinning ycharts-generate brings it to the guard the other seven already run: the same
refusal, a named error, on a pointer that is malformed. The CTO is asked to read that line (it is the one delta of the eight that
is neither the ownership pair nor the flip's value).

## Rehearsal (scratch worktree, no ref moved, nothing uploaded)

`r4_flipcommit.py --apply` in a scratch checkout of HEAD @444feaa500: 16 files change (the registry, the two value-changing
targets, 13 mark lines); `validate` exits 0. A rehearsal commit object (dangling) stood for the flip commit; the eight rows were
re-pinned to it with their member hash; `BUILD_ONLY=1 build-and-upload.sh investor-reporting <function>` built all eight, each
artifact's `loaders.py` carrying `"bucket": "opal-data-49financial"` and `OWNERSHIP_READ`. Rehearsal hashes (base64 SHA-256, the
values the act must read if the tree is otherwise unchanged): reporting-read `IhlTVtU9yYVskJ3PUOcoOKp1HnE2WAW5V8X31IwKkTc=`,
directory-search `TefVhmGStCRorgQFrQFCS0lVUC+pXrWJYfdUCEExqe4=`, export-render `dCzMEt04dtBAlvkj+2rZMGZaU30kY+7leZxN00dbxH8=`,
holdings `SWRfUfHdJarO2Rhbxw/KQK88DeDNorQujkaR1jUuZc0=`, narrative `0+/PHOb/xGvYNBrz/j4Ltk5k85clmAo96BOJzi9n3ZY=`,
performance-adapter `kMB8xCI93/9QLUnzglVIs0EIRY07SSLBiU5ln8iJwUc=`, status `JmOhV/ep4mR1mt2NKKqyUlohgO3mlDw1GEM4eAWYKdw=`,
ycharts-generate `NeAB50CNXWvM5Y6nsba220QmsEiASbVbXcZVRYe4MUM=`.

## Order inside the IRPT leg (bounded, stated)

1. The flip commit M (registry + regenerated targets), on a branch; `r4_flip.py` and `r4_dormant.py` read.
2. The source-map commit M2 (eight rows, two fields each), pins to M; the build must read `OK` for the staged hash.
3. Per function: build-and-upload, the scoped plan (code hash only), the apply: the minutes-long split of ADDENDUM 1's condition 2.
4. The source-map record commit M3 (the script's own `artifact_*` fields) after the uploads.

## Both branches (additions)

- **Branch A:** each of the 8 rows reads the new pin and the member's blob hash; each artifact's hash equals the rehearsal's;
  each scoped plan changes only the function's code hash.
- **Branch B (additions):** a build refuses on a staged hash; an artifact's hash differs from the rehearsal's with an unchanged
  tree (something else moved); a plan names a resource beyond the function. Rollback as the table's.

## What this addendum does not know

- Whether any of the eight functions' OTHER staged members are also pinned behind HEAD for the same reason (this addendum
  re-pins one member only; the others are unchanged by the flip). The act reads each function's `staged_from` before the
  re-pin and records any member whose pin is older than the file's last change: it is named, not moved.

## Provenance

`r4_flipcommit.py`, the scratch rehearsal (HEAD @444feaa500, dangling commit, no ref moved), `build-and-upload.sh` BUILD_ONLY.
Push state: LOCAL.
