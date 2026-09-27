# MX-s-8 -- never-widen sign-off, SECOND (non-acting) half: SIGNED

Signer: `3.0.0_SA_CVO~O`, a non-acting seat. It neither issues nor deploys this act. Recorded 2026-09-27 ~09:5xZ.
Ask: `2.0.0_SA_COO~O` file `20260927T092019Z_2.0.0_SA_COO_O_MX-s-8_never-widen_second_half_asked.md`.
Authority: Andrew's arming term, "Served output still moves only under a never-widen sign-off (CTO half + a second,
non-acting half)" (`ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md`).

**The act this half covers, and nothing wider:** `NFRA_MCPINDEX.TO-MX-s-8` as amended @a296ac3598. It builds and
uploads the artifacts of `opal-assets-silver-{blackdiamond,etf,eclipse,orion}` from the vendored tree at @e0750442c9,
then runs `safe-apply` with exactly `Plan: 0 to add, 4 to change, 0 to destroy`, under the NEVER-2 ledger
`nfra-mcpindex-silver-mirror-guard`. It does NOT sign the backfill of the 4 pathfinder dailynav partitions, which is
0.4.0_DS_ClientPlatform~D's separate literal-key write.

## Blast radius, re-read by this seat

| claim | this seat's read, 2026-09-27 ~09:3xZ | holds |
|---|---|---|
| the build ships only the two hunks | The build input is `lambda-source-map.json`'s fixed file list per function. Each listed file at the cut was hashed against the DEPLOYED zip saved for rollback (`C:/tmp/mx-s8-rollback/`). Identical: blackdiamond 8/9, etf 8/9, eclipse 6/7, orion 6/7. The one differing file is `mirror_conversion.py` in each, and its diff against the deployed bytes is exactly 5 lines: `if v == "": return None`, and the widened float64 guard. No zip-only files. | yes |
| the base has not moved | live `CodeSha256` read now = the announce's (XiJ6..., Zyhz..., 5hRk..., rwI6...), LastModified unchanged | yes |
| writers of the rule (NEVER-1) | 5: the 4 Lambdas plus the source `data/assets/scripts/silver/mirror_conversion.py`, which already carries both fixes. 4 of the 218 source-map functions vendor the file (bd49finsurance, schwab and smartx do not). After the act, all 5 writers apply one rule. | N = 5 |
| Z-S25 reaches pathfinder | `convert_filepoint` lives in the etf Lambda's `etf_conversion.py` and calls `mc._numeric_or_raise` (`:214`) | yes |

## Both branches of the producer's rule (`_numeric_or_raise`, `mirror_conversion.py:283-308`)

- **No cell is exactly `""` in a float64 column:** output is byte-for-byte the current rule. Every non-numeric text
  still raises.
- **A cell is exactly `""`:** the unit now WRITES, with a typed NULL in that cell, where it used to fail whole
  (VendorDriftError, no partition). Rule 17 reading: an empty field carries no value, and a typed NULL keeps it
  absent. No value is invented, no row is dropped, and non-numeric text still raises. That is dtype standardization,
  not fillna. Gold consumers see NULL where they saw a missing partition before.
- **Which units move at deploy:** in the logs' 14-day retention window, VendorDriftError fired 0 times across all 4
  functions. The positive control on the same group read 72 invocations (etf, `"START RequestId"`, counted client-side). The sweep's `backfill-status.json` reads
  holes 0 for orion/inflection, eclipse/inflection, blackdiamond/cottonwood, pathfinder/PFDE and pathfinder/PFOE.
  So the next runs and sweeps change no existing partition. The 4 known 08-29/08-30 pathfinder units are outside
  retention and are not retried automatically; they land only through DS's backfill. Limits: blackdiamond/49f,
  blackdiamond/49financial and pathfinder/filepoint have no status file, so their current holes are unread. The
  status file cannot see a conversion raise, which is why the log count is the instrument here.
- **Z-S3 hunk:** all 4 functions run `pandas-pyarrow-layer:1`, read by the worker as pandas 2.3.2. On pandas 2 the
  `str` dtype does not arise, so the arm is latent, and this act does not change the layer.

## Rollback, per key

For each of the 4 functions: the saved deployed zip, sha-verified against its `CodeSha256`, and the prior S3 artifact
VersionId recorded before upload (order step 9). Re-applying restores `CodeSha256`. No data is written by this act.

## Verdict

**SIGNED** for the act above as bounded here. Nothing is added: the order's own guards (the plan must read exactly
4 to change, then `plan -detailed-exitcode` 0, then the import smoke, under the NEVER-2 ledger) stand as written.

-- 3.0.0_SA_CVO~O
