# DEPLOY LEDGER — MDPF_COTREMEDIATION AE leg: silver blackdiamond holdings contract (21-col)

**Opened:** 2026-08-25T17:07:45Z by 0.5.0_AE_OpalETL~B (deploy-start; NEVER#6 / COTR-inv-9)
**Status:** OPEN
**Decomp:** `workflows/atom_decomposition/runs/mdpf-cotremediation/20260825T161149Z/DECOMP.md`
@6afd608e0a (41 cells) — cells owned here: COTR-b-3, b-3a, b-4, b-5, b-5a, c-1, c-2, c-3
**PRD:** `docs/architecture/MDPF_COTREMEDIATION_PRD.md` v1.0
**Authority:** Andrew-direct 2026-08-25 ~14:20Z (*"That needs to get fixed immediately"*) · D8
**Rulings consumed:** CTO 70785 (item 1 option (a), item 2 option (b)) · CTO 70793 (disarm same-turn)
· COO 70788 / 70797 · CVO 70791 (source-confirmed, not a gate)
**Trigger:** OBSERVED — DS~M contract commit `288807f747` landed (verified by `git log`, not reported)

⛔ **NOT vendor drift.** We amended the BD holdings template ourselves (@`17c38a26f2`, 2026-08-20
17:56Z, under a CTO pin). The vendor changed nothing. The silver-contract step was never sequenced.

## Legs

| Leg | Act | Artifact | Status |
|---|---|---|---|
| 1 | Targeted vendor — `mirror_schemas.py` ONLY | `infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/mirror_schemas.py` | DONE (pre-commit) |
| 2 | Disarm the armed residual | `.../opal-assets-silver-blackdiamond/BUILD_MANIFEST.json` `vendor_parity_expected_red` | DONE (pre-commit) |
| 3 | Commit code + manifest + this ledger | safe-commit, lane CLOUD_OPS_OR_ETL | OPEN |
| 4 | Build + upload artifact | `ci/build-and-upload.sh` → `s3://.../opal-assets/opal-assets-silver-blackdiamond.zip` | OPEN |
| 5 | Commit tool-written source map | `infra/aws/lambda/ci/lambda-source-map.json` (lane YANG_PIPELINE_DEPLOY) | OPEN |
| 6 | `safe-apply` (Rule 26: this device) | `infra/aws/terraform/opal-assets` `module.silver_converter["blackdiamond"]` | OPEN |
| 7 | COTR-c-2 — deployed package BYTES carry both columns | downloaded zip member, not a config read | OPEN |

## Pre-apply measured state

```
two-home md5, mirror_schemas.py        BEFORE 85fc671e92ba56491419713c93845b15 (both)
                                       AFTER  8818df2f03bad80601fdefc11f54c3db (both)  <- COTR-b-3a
declaration verified at MY seat        21 cols; 'Account Supervised' idx 8 (before AssetID),
                                       'Holding Supervised' idx 20; both "string"
import-closure-check  default mode     OK 9 files, closed
import-closure-check  --sources mode   OK 9 files, closed        <- COTR-b-4
deployed CodeSha256 (pre)              P9VvxJnsa7nea5xhuk+ZL5+0hyqFBXTVIjO7JpJt13Y=
deployed LastModified (pre)            2026-07-23T14:47:39.000+0000
DEPLOYED == VENDORED                   all 8 members, md5-compared from the live package
```

⛔ **`vendor-manifest.sh --check` reads rc=1 / 2-of-8 DRIFT BY DELIBERATE SCOPE, AND IT READ rc=1
BEFORE THIS LEG TOUCHED ANYTHING.** `rebalancer_conversion.py` + `rebalancer_schemas.py`: SOURCE is
AHEAD of vendored/deployed — undeployed 3F-S5 work deferred at `1351c74d96` (2026-07-23, *"0.7.0
lambda-twin rides TF"*, ride never taken, 33 days). **NOT created by this leg.** Disarmed at the
gate's own reading surface (leg 2). **Remediation owner: `0.7.0_AE_CloudOps`**, own sequenced act,
seated by COO when the P0 is clear.

## Rollback

Same-window revert: `git revert` the code commit, re-run `ci/build-and-upload.sh`, `safe-apply`.
The prior artifact is recoverable by CodeSha256 `P9VvxJnsa7nea5xhuk+ZL5+0hyqFBXTVIjO7JpJt13Y=`
and the bucket is versioned. Silver partitions are DS~M's leg and are not written by this deploy.

## Blast radius (COTR-b-4, structural not empirical)

`mirror_schemas.py` is vendored into this package only for the `("blackdiamond","holdings")` key;
`holdings/` exists ONLY under `blackdiamond/cottonwood/`, so cottonwood is the only tree this
declaration can reach. `mirror_conversion.py` is vendored into four packages but is **not modified
by this leg** — the other three are untouched bytes.

## Close (checked only when TRUE, with evidence)

- [ ] Code + manifest + ledger committed
- [ ] Artifact built + uploaded, write VERIFIED (size + sha256)
- [ ] Source map committed (tool-generated, not hand-authored)
- [ ] `safe-apply` complete; post-apply 0-diff re-plan clean
- [ ] COTR-c-2: deployed package BYTES contain `Account Supervised` + `Holding Supervised`
- [ ] Tag created
- [ ] CLOSED
