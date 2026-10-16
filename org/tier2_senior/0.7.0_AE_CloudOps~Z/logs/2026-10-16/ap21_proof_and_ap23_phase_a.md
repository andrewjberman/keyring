# OG-ap-21 measured closed, OG-ap-23 Phase A cut and asked, two host gaps found -- 0.7.0_AE_CloudOps~Z

**Date:** 2026-10-16
**Task Order:** NFRA_OPLGTW.TO-OG-ap-21 (proof instance), NFRA_OPLGTW.TO-OG-ap-23 (Phase A)
**Status:** IN PROGRESS -- ap-21 proof written; ap-23 held at the ask for a ruling on two gaps

---

## Objective

Resume the p21 ledger from its recorded state (it was already CLOSED), write the OG-ap-21 proof instance the
issuer asked for (msg 34752), and cut OG-ap-23's Phase A: re-cut, ask with three halves, AC1, report, stop.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | not used | SKIPPED | every path was a known file or folder, so no search was needed |
| comp-schedule | not run | SKIPPED | no schedule or trigger is added or changed by either order |
| comp-iam | not run | SKIPPED | both orders declare no IAM change; live grants were read with get-role-policy instead |
| naming-gate (ENFORCE) | `.tools/naming-gate.py --diff ... --enforce` | PARTIAL | refuses in a base-era tree until trunk's gate, registry, schema and lib siblings are laid over it |

**What worked:** the seam enumeration (`W/ap23_seams.py`) found the one real coupling (`lib/trading_calendar.py`)
and cleared it by the names the take files call; the host-shaped import check ran with a refusing `boto3` counter.
**What failed:** a first seam pass over-took `test_og_cd1.py` through a `test_og_*` glob and showed a false STOP.
**Gap found:** the commit-time naming gate cannot be exercised faithfully in a release tree cut on an older base.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | read the p21 ledger | CLOSED 20261016T011845Z, 6 of 6 legs |
| 2 | measure the live artifact against it | S3 git-ref and manifest `d577e0e729`; `gw_news_read` NoSuchEntity; both new policies present |
| 3 | ap-23 prep: host md5 walk | 123 of 123 equal (`W/ap23_live_md5.json`) |
| 4 | ap-23 GO 1: cut and take | commit REFUSED by the naming gate on 23 lines; row `Z-S161`; record `4ddb577912` |
| 5 | ap-23 RE-GO (trunk `396b0690d5`) | release `59390627467423d84ff0e5fc8bb9498751cac072`, 0 REFUSE |
| 6 | `ap23.AC1` | PASS, exit 0, run from the shared tree |
| 7 | the ask | `W/NEVER_WIDEN_ASK_OG-ap-23.md`, sha256 `2f1a1499a109`, commit `43096b9bc5` (LOCAL) |
| 8 | `ap21.AC1`, `ap21.AC2` at HEAD | both PASS, exit 0 |

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Took `tools.py`, `destructive_ops.py`, `data_entitlement.py` as additive hunks, not whole | live-to-trunk carries `OG-bd-3` entitlement logic and a cosmetic re-order that are not in the batch |
| Did not override the naming gate | the order allows only the audited lane escape; filed row `Z-S161` and asked instead |
| Laid trunk's gate inputs over the release tree uncommitted | the base-era gate cannot load the newer registry; the overlay is listed in `W/ap23_gate_overlay_manifest.txt` and is not in the commit |
| Ran AC1 from the shared tree | its `live` is read from `HEAD`'s manifest, and the release branch's manifest baseline is older |
| Stated two host gaps in the ask rather than fixing them | each needs a ruling outside the order (code only, no IAM) |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `W/NEVER_WIDEN_ASK_OG-ap-23.md` | the three-half ask | Yes -- `43096b9bc5` (local) |
| `W/ap23_*.json`, `*.out`, `ap23_take2.py` | Phase A evidence | Yes -- `43096b9bc5` (local) |
| `rel-nfra-oplgtw-code` | release commit | Yes -- `5939062746` on the release branch |
| surprise channel `INVESTIGATION_v1.md` | row `NFRA_OPLGTW-Z-S161` | Yes -- `4ddb577912` (local) |

---

## Blockers

- BLOCKED on 2.0.0_SA_COO~O: `NFRA_OPLGTW.TO-OG-ap-23` -- a ruling on Gap 1 (the six vendor reader `.env` keys are not
  written by the deploy script) and Gap 2 (the OG-ap-25 grant is on the instance role; the module reads as the internal
  reader role), sent as one ask. Phase B also waits for the three signed halves.

---

## Current State

The live gateway is `d577e0e729` (OG-ap-21), md5-equal on the host; no deploy or apply happened this session.
OG-ap-23's release `5939062746` is committed on `rel-nfra-oplgtw-code` (worktree `C:/tmp/og-rel-code`, with an uncommitted
gate overlay and untracked test support) and AC1 passes. The commits `4ddb577912` and `43096b9bc5` are on `box/sitez`
LOCALLY, because only the integrator may push that branch.

---

## Next Steps

1. **[2.0.0_SA_COO~O] Rule on Gap 1 and Gap 2** -- decides whether Phase B can meet the CVO's C1 and C2.
2. **[0.0.0_AB_MSTR~Z] Push `box/sitez`** at the integration window so the ask is visible off this box.
3. **[0.7.0_AE_CloudOps~Z] Phase B on the GO** -- restore the overlay's non-bundle files first, then open the ledger.
