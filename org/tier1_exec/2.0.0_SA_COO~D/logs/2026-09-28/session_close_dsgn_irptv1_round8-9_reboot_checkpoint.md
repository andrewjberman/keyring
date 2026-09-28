# DSGN_IRPTV1 rounds 8-9 drive to the reboot checkpoint -- 2.0.0_SA_COO~D

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, IMPLEMENT

**Date:** 2026-09-28
**Task Order:** DSGN_IRPTV1 round 8 close + round 9 (IV-e-54..79)
**Status:** IN PROGRESS (checkpointed for the Andrew-direct laptop reboot, CTO 102348)

---

## Objective

Drive DSGN_IRPTV1 through the canonical workflow on Andrew's standing mandate ("calls approved + set /canonical-drive loop for your work on IRPT, drive your responsibilities to completion"): issue and drain worker orders, walk the page in ~P's signed windows, compile L8 packets, and cut each round from the CTO's analysis. Stop cleanly at the reboot checkpoint.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find (rail) | redirected raw repo greps in Bash | PARTIAL | the rail denied several raw greps; native Grep and pipe receivers covered the gap |
| .tools/to-pipeline-gate.py | on every issuance and amendment commit | PASS | refused a round order missing `<round>` and a terminal flip on an INVALID proof instance |
| .tools/surprise-row-gate.py | on channel commits and every drain | PASS | caught a worker GRADUATED disposition and a seat committing W-coordinate rows |
| .tools/proof-of-spec-check.py | before every flip | PASS | also exposed that PENDING-THIS-COMMIT portal rows read ABSENT at the flip (W36-S5) |
| .tools/safe-merge.sh | every drain | PASS | rc=4 channel conflicts resolved with .runtmp/union_rows2.py; rc=2 on other seats' staged index |

**What worked:** the gates caught every malformed commit before it landed; the union script made channel conflicts a one-step fix.
**What failed:** nothing silent; the complete-flip gate cannot see artifacts that live only in the portal repo.
**Gap found:** the flip gate's artifact resolution is workspace-only (row W36-S5); the row gate reads the committing seat, not --author, so an issuer committing a dead worker's rows needs the audited override.

---

## Work Completed

### 1. Round 8 close
- IV-e-54..63 plus direct acts IV-e-53/64/65/66/67 drained to local portal DEV; IV-e-50 superseded. L8 packet `deliverables/2.0.0_SA_COO~D/round8-L8-packet.md` sent to 3.0.0_SA_CVO (READ). CTO round-8 analysis (102160) cut as round 9 in one issuance (IV-e-68..77).

### 2. Export hop walks (windows 19, 20)
- W19 K7 8.05% PARTIAL; K8 one POST /export answered QUEUED exr_9f785460, the receipt read answered UNAVAILABLE/NOT_READY and the page went silent (row S27). The render failed at the backend's RENDER_DELEGATE refusal (~P). CTO ruled S27 (b): the backend answers RUNNING; the page names every refused read (IV-e-78). R11 ratified.
- W20 K10: irpt-status 5fSyChId answered 500 for REQ-67e12718 (row S28); ~Y traced an IAM read gap plus a stale errors.py; the CTO rolled back; rebuild 3 follows the reboot. Both walks closed with the byte-proof (HEAD pinned, 0 tracked, 0 /__mockcot/; HAR sha 9259170d and 32e2da7a, gitignored).

### 3. Round 9 drains
- Terminal and drained: IV-e-68 (fe-s-45 port pool), 69 (performance answer), 70 (model vs class colour, amendment 1 lime600), 73 (one firm mention), 74 (history in words + S28 tenant), 78 (receipt refusal named + R11 wire copy), 79 (five re-goldened firm-chip tests). Portal DEV 28f5118c: tsc 0, lint 0, suite 933 pass / 27 skip / 5 fail (the 5 known), 0 new.
- Two workers died at ~01:00Z on an account spend limit; the work survived uncommitted and was finished by fresh finisher sessions. IV-e-70 was committed by the issuer on the worker branch (audited surprise-row override) under the reboot checkpoint.

### 4. Rows filed
- S27, S28 (walk findings), S29 (UIC-09 reopened), S30 (NEW-02 COT pie draws nothing) per the CRO re-walk and CTO 102358.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| IV-e-70 amendment 1: the asset-class palette yields to model colours only, never to commodities' ratified colour | two CTO rulings constrained ASSET_CLASS from different sides; both bars can hold (lime600) |
| IV-e-79: re-golden the KEPT parity test with a new failing control | UIR-30 removed the chip the old control read; the claim stays, the control moves |
| IV-e-74 amendment 1: S25 settled as backend; add the S28 tenant thread | W20 plus ~Y 102268 measured it; no further page diagnosis |
| Issuer commits IV-e-70 under an audited override | the worker session could not be resumed and the checkpoint forbade a new seat |

---

## Files Modified

See the commit messages on the new history (post-S19 purge): drains 210a8cc1b4 (73+79), b5124e4586 (70), 37fda644e2 (74), bc094c51f9 (78); orders 2261dbe286 (IV-e-78), 680607bcfe (78 amendment 1), dadbd3d1c9 (IV-e-79), 02d37f7a22 (70 amendment 1), 9e23598a38 (74 amendment 1); rows 995a271bf8 (S27), 7f25e55f32 (S28), f16ecab8bf (S29/S30); drive log d2673db5bc.

---

## Blockers

- None on this seat. The K8 re-run waits on 2.0.0_SA_COO~P (RENDER_DELEGATE adapter fix, the R11 RUNNING receipt answer) and K10 on irpt-status rebuild 3 (~P) -- both evidence-cited in rows S27/S28 and CTO 102271/102228.

---

## Current State

Portal local DEV is 28f5118c and carries round 9 IV-e-68/69/70/73/74/78/79; nothing of this seat is pushed (MSTR integrates). CLOUD holds every record through 37fda644e2 on the post-purge history (origin/CLOUD 3dcd7d4049 per MSTR 102371). No DSGN worktree or worker is live. Round 9 pending: IV-e-71, 72 (chain H), 75 (chain X), 76, 77 (chain Z), plus new cells for S29/S30. The handoff lists the first acts in order.

---

## Next Steps

1. **Amend IV-e-76** per CTO 102351 (its own view target in lib/opal_naming.py) -- first act after the reboot.
2. **Cut S29/S30 cells**, then seat IV-e-75, chain H, then chain Z.
3. **[2.0.0_SA_COO~P] open windows** for the K8 re-run (after the adapter fix and the R11 RUNNING answer) and K10 (after rebuild 3).
4. **Round-9 walk and L8 packet** to [3.0.0_SA_CVO] after the round drains.
