# MX-r-14 -- the round 17 catalog release, first attempt, landed

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

**Serial:** `0.7.0_AE_CloudOps~MI` | **Window:** 2026-10-15 18:29Z -> 20:25Z (prior log
`ae_mi_mx_r_13_attempt1_rollback_and_recut_0549-0805Z.md`)
**Order:** `NFRA_MCPINDEX.TO-MX-r-14` at A1 and A2 | **risk:** WORLD | **window:** 13:00Z close on 2026-10-16, met at 19:50Z

---

## What happened

| | |
|---|---|
| cut | `c4c106aea1` on live `06cfb6db64` (the release commit of OG-ap-20; no deploy-only commit beneath it) |
| ships | catalog `b97c59e6ac` + discover `92ca8b57f7` @ trunk `7cfd0b09ec` |
| ledger | `nfra-mcpindex-r14-catalog-release`, 5 legs, CLOSED |
| criteria | `r13.AC2` (99 of 99), `r13.AC3`, `r14.AC4`, `r14.AC1`: all PASS |
| delivers | 44 inferred nl_tags, a `firm` field on 24 table rows, firm-scoped visibility in `_silver_answer`; link counts 33/112 -> 39/119 |

The MX-r-13 pattern ran unchanged and landed first time. PHASE A: live ref read from the host by hash (121 of 121), the
two-blob overlay cut through a temporary index, four censuses (tools 99, keys 57, ids 7, links 39/119 as ruled), the
ANNOUNCE. PHASE B: condition re-read 19:31Z, halt-gate pair rc=0/rc=3, bun cache 77 of 77 (planted arm 77 of 78), deploy
rc=0, label read back before L1 closed, host 121 of 121 equal to the cut, checks, manifest in one guarded edit.

**Two small things worth the next seat's time.** (1) `post_censuses.py` still carries MX-r-13's constants (93 tools, 33/112
links), so its closing EXPECTED line printed MISMATCH on a correct release; the four lines above it are the evidence and
the instance says so. (2) One Bash call was denied by the permission rail because it contained a recursive delete of a
scratch directory; re-run without it, the directory having never existed.

**Not verified live.** A firm principal's view of the 24 rows: `r14.AC4` grades the fields and the issuer's `f1` checks grade
the behaviour on the tree; nothing here exercised a firm principal against the host. Stated in the ANNOUNCE and the instance.

## Compiler Tools

| tool | use | result |
|---|---|---|
| `deploy_ledger.py` | open / close-leg / close | CLOSED, sentinel removed |
| `halt-gate-check.sh` | positive and a both-limbs-defeated negative arm | rc=0 / rc=3 |
| `bun_cache_precheck.py` | positive and planted-package arms at mcportal `17dcbb28` | 77 of 77 rc=0 / 77 of 78 rc=1 |
| `safe-ec2-deploy.sh` | the deploy | rc=0, base guard equal at both checkpoints |
| `safe-commit.sh` | ANNOUNCE, close, proof | landed |
| `r14.AC1`, `r13.AC2`, `r13.AC3`, `r14.AC4` | the order's criteria | see the proof instance |
| `ssm_run.py`, `host_read.py`, `host_vs_cut.py`, `tools_census.py`, `env_render.py`, `link_counts_*.py`, `post_censuses.py`, `write_manifest.py`, `build_instance.py` | probes under `probes_r14/` | adapted from `probes_r13v2/` |

## Open

- The `<status>` flip of the order is the issuer's.
- `OG-ap-21` should cut on `c4c106aea1` (told to the issuer in the close report).
- `nfra-mcpindex-r7-bd-doc-retire` (this seat's) stays OPEN by design until 2026-10-19/20.
- `C:/tmp/mx-dep-r14` is kept and locked until the round closes; its uncommitted `EC2_MANIFEST.json` edit (written by
  `safe-ec2-deploy`) is not part of any commit. No rollback tree was needed or built for this release.
