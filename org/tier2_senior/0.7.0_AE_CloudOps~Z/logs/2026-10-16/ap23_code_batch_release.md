# OG-ap-23: the code batch release is live at 3d5c9c8bf1 after one rollback -- 0.7.0_AE_CloudOps~Z

**Date:** 2026-10-16
**Task Order:** NFRA_OPLGTW.TO-OG-ap-23
**Status:** COMPLETE (AC1 and AC2 PASS; AC3 is the CVO's)

---

## Objective

Cut, ask for, deploy and prove the code batch release: 27 added READ tools, the five client tools master_admin only, OG-bd-3, the tar line, and the six vendor reader keys, on the live base `d577e0e729`.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| naming-gate (ENFORCE) | `.tools/naming-gate.py`, ng2.AC2, ng3.AC1, safe-commit | PARTIAL | grades only after trunk's gate, registry, schema and lib siblings are laid over the base-era release tree (uncommitted overlay) |
| comp-iam | not run | SKIPPED | the order declared no IAM change; that declaration was wrong for four tools (row Z-S164), found by the served read, not by a tool |
| comp-schedule | not run | SKIPPED | no schedule or trigger changes |
| comp-find | not used | SKIPPED | every path was a known file or folder |

**What worked:** the served read as the instrument that finds what a preflight declared absent; the tar census with a negative control; the seam enumeration.
**What failed:** the preflight's "no IAM" claim; my own first deploy hunk lost the tar-line edit while I rewrote it, and the ask claimed it existed.
**Gap found:** a release tree cut on an older base cannot run the commit-time naming gate without an overlay.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Phase A cut, five times (A2 to A7) | release `3d5c9c8bf1`, parent the live ref |
| 2 | ask, three halves | CTO `2665f19c6a`, COO `f94bcaf1e5`, CVO `49ebdc867a`, ask sha256 `ba5b9325bca5` |
| 3 | Phase B, first attempt 08:13Z | DEPLOYMENT COMPLETE; served read 23 of 27 (four IAM denials) |
| 4 | rollback under C5 08:28Z | base redeployed, 123 of 123 base files equal, row `Z-S164` ARMED |
| 5 | `OG-ap-27` grants the four prefixes | `ap27.AC2` PASS (COO read) |
| 6 | Phase B, second attempt 09:13Z | DEPLOYMENT COMPLETE; 141 of 141 host files equal; `.env` 58 to 64 |
| 7 | served read | 27 of 27; client_admission, via_internal_reader, C1, C2 true |
| 8 | standing clauses | manifest and runbook 7.2 at `365b8c133a`; `rb.AC2` PASS |
| 9 | ledger closed | `ap23.AC1` and `ap23.AC2` PASS |

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Rolled back the first attempt without asking | COO condition C5 and the order's trigger rule said so; the four failures were fail-closed AccessDenied |
| New branch per re-cut (`-a3`, `-a5`, `-a6`, `-rb`) | the head-move guard refused a reset of a local commit and I did not force it |
| `data_entitlement.py` and its four pin tests taken whole (A7) | the base lacked OG-bd-3 in the same file as OG-ad-1's change |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| release `3d5c9c8bf1` | the batch, 48 files | Yes -- on the release branch (local) |
| `EC2_MANIFEST.json`, runbook 7.2 | standing clauses | Yes -- `365b8c133a` (local) |
| ledger entries, `CODE_SERVED.json`, evidence | records | Yes -- `2d97278481` and earlier (local) |

---

## Blockers

None for this seat. The record commits are local until the integrator pushes `box/sitez`.

---

## Current State

Live is `3d5c9c8bf1` on `i-07dccb1615503ac99`, md5-equal across app, deploy, lib and the two `app/refs` files; the `.env` carries the six reader keys. OG-bd-3's master_admin branch is live. The deploy tree `C:/tmp/og-rel-code` has HEAD on the manifest commit above the release and an uncommitted gate overlay.

---

## Next Steps

1. **[2.0.0_SA_COO~O] Tell `~MI` and `~MP` the live commit** `3d5c9c8bf1`, and set `OG-ap-17` superseded (condition C9).
2. **[0.0.0_AB_MSTR~Z] Push `box/sitez`** so the ask, ledger and records are visible off this box.
3. **[3.0.0_SA_CVO~Z] Grade AC3** on a real client and rival call.
