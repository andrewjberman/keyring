# MX-r-13 -- the round 13/14/16 catalog release: a first attempt rolled back on r13.AC2, a re-cut that landed

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Serial:** `0.7.0_AE_CloudOps~MI` | **Window:** 2026-10-15 05:49Z -> 08:05Z (prior log
`../2026-10-14/ae_mi_mx_r_12_v1_and_v2_0213-0430Z.md`)
**Order:** `NFRA_MCPINDEX.TO-MX-r-13` at A3 to A6 | **risk:** WORLD | **window:** 13:00Z close, met at ~08:05Z

---

## What happened

| | attempt 1 | attempt 2 (re-cut) |
|---|---|---|
| cut | `d020bee315` on live `ee23dd004c` | `1b18b94979` on live `ee23dd004c` |
| ships | catalog `11620b3c52` + discover `f3cf344cc3` @`789ffd57b0` | catalog `e5096b5d6c` + discover `f3cf344cc3` @`32d0bc608a` |
| ledger | `nfra-mcpindex-r12-catalog-release`, CLOSED, rolled back | `nfra-mcpindex-r12-catalog-release-v2`, 5 legs, CLOSED |
| criteria | AC3, AC4 PASS; **AC2 FAIL** (7 MISSING) | AC2, AC3, AC4 PASS; AC1 PASS after the close |
| outcome | rolled back to `ee23dd004c` 06:46Z, verified | `1b18b94979` SERVING, manifest written |

**PHASE A (attempt 1).** Read the live ref from the host by hash (118 of 118), cut a deploy-only commit by a temporary
`GIT_INDEX_FILE`, and found the MC Portal per-tool link counts DIFFER (11/14 -> 33/112). That census is one the halves call
EQUAL, so I stopped and the issuer ruled it EXPECTED at exactly 33/112. The cut catalog is 1,059,657 bytes, too big for an
SSM inline command, so the cut side of the link counts is the same reader run off-host (the host's real import was the
control on the live side).

**PHASE B (attempt 1).** All pre-checks passed; deploy landed; label, host bytes and four censuses held; AC3 and AC4 passed;
`r13.AC2` failed (index rc=1: five tools without a depth claim, two without a definition). Both signed halves say "any other
read-back fails -> redeploy ee23dd004c plus a BLOCKING row", so I redeployed from a clean tree at `ee23dd004c`
(`C:/tmp/mx-dep-r13-rb`) and verified 118 of 118. That rollback re-uploaded `opal-gateway-ee23dd004c.tar.gz` (629,787 B,
ETag `3cd90347`; the halves had named 629,899 B / `159fa4ea`), contents equal. Rows `Z-S118` (BLOCKING) and `Z-S119`.
The surprise-row gate refused the order's worker-form ids (`Z-W35-S<k>`) for a seat; the seat form `Z-S<k>` is what lands.

**The issuer's finding.** Both causes were the issuer's: the AC2 checker did not know the per-link depth claim, and the catalog
took two definition lines from the deployed source rather than the shipped one. `r13.AC2` on the base reads 67 of 93 by
construction, so the order's "PASS now" was wrong.

**PHASE A/B (attempt 2).** New cut, new tree (`C:/tmp/mx-dep-r13v2`), fresh pair. Everything passed first time:
host 118 of 118 equal to the cut, tools 93, keys 57, ids 7, links 33/112 (real import on the host), AC2 sum 93 of 93 with
definitions 93 of 93, AC3, AC4. Manifest written by hand in one guarded edit (five fields), because `safe-ec2-deploy`'s own
manifest commit fails closed in a sparse tree.

## Compiler Tools

| tool | use | result |
|---|---|---|
| `deploy_ledger.py` | open / close-leg / close, both slugs | both CLOSED, sentinels removed |
| `halt-gate-check.sh` | positive and a both-limbs-defeated negative arm, per attempt | rc=0 / rc=3 |
| `bun_cache_precheck.py` | positive and planted-package arms at mcportal `17dcbb28` | 77 of 77 rc=0 / 77 of 78 rc=1 |
| `safe-ec2-deploy.sh` | the deploy and the rollback | rc=0, base guard equal at both checkpoints |
| `safe-commit.sh` | ANNOUNCEs, closes, rows | landed; its surprise-row gate refused W-form ids |
| `r13.AC1`-`AC4` | the order's criteria | see the proof instance |
| `ssm_run.py`, `host_read.py`, `host_vs_cut.py`, `tools_census.py`, `env_render.py`, `link_counts_*.py`, `post_censuses.py`, `write_manifest.py` | probes under `probes_r13/` and `probes_r13v2/` | reused and written this act |

## Open

- The `<status>` flip of the order and the disposition of `Z-S118` / `Z-S119` are the issuer's.
- `nfra-mcpindex-r7-bd-doc-retire` (this seat's) stays OPEN by design until 2026-10-19/20.
- `C:/tmp/mx-dep-r13`, `C:/tmp/mx-dep-r13-rb` and `C:/tmp/mx-dep-r13v2` are kept and locked until the round closes; their
  uncommitted `EC2_MANIFEST.json` edits (written by `safe-ec2-deploy`) are not part of any commit.
