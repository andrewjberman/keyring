# NFRA_DEVPLN -- ROUND-6 ANALYSIS (1.0.0_SA_CTO, 2026-10-14 ~01:5xZ)

**On:** the issuer's drain end `org/tier1_exec/2.0.0_SA_COO~DV/deliverables/NFRA_DEVPLN_ROUND6_DRAIN_END_20261014.md` (1 of 1 order,
MAY-CLOSE; no CVO packet). **PRD:** v0.3, unchanged. **Next:** round 7 in ONE issuance on section 3.

## 1. What round 6 moved

- **DP-h-1:** the test seam is honoured only with `OPAL_STATE_ROOT` set. The hazard was reproduced at the base and cleared after the
  merge.
- **The DEV payload limb is installed on all four boxes.** Each manager read it back (`cmp` and demonstration 1 refusing), dell1 and
  dell2 on the gitlink layout after LD-0646. A missing gate on DEV or PROD now fails closed (LD-0647, this seat's ruling
  `CTO_RULING_20261014_013xZ_PORTAL_PREPUSH_MISSING_GATE_FAILS_CLOSED_ON_TRUNKS.md`). That supersedes item 5 of DP-f-1 (WARN), as the
  issuer recorded.
- **A second organic chosen-set promote:** PROD `7d5cb34d` (tag `portal-v2.1.215`, CI success) ships dell1's feature alone. The
  first-parent read of PROD since the settlement shows 2 commits, both approved merges with both trailers, `unapproved=0`. None of the
  seven unapproved dell2 DEV commits shipped.

**Named for the CVO's grade reads, not graded here:**
- FWD-5 (a chosen set shipped, and unapproved work left behind, twice);
- FWD-3 (the route onto DEV is now refused otherwise at both the typed-command gate and the git hook, on four boxes).

## 2. Rulings

- **`S4` and `W1-S16`: one small repair in round 7.**
  - `portal-release-build.sh --check` prefers `origin/<name>` for a trunk name and prints the resolved ref and sha on its result
    lines.
  - Test case 9 stops making a real ref lookup.
- **The DT's uncommitted ledger close** (`20261013T2048Z_devpln-r2-chosen-set-promote-..._deploy_completion.md`) is the DT's to
  commit under TO-DP-x-1 step 5. Until it lands, every other box reads that deploy OPEN.

## 3. ENRICHMENT LIST for round 7

1. **After Andrew rules the dell2 rows** (`3635`, `8500`, `7b45`, `fde0`, `7773`): A14, FWD-1's client-facing close (SERVED, with the
   L8 packet). No order is cut before he rules.
2. **The repair (section 2), one worker-light cell.**

If he has not ruled when round 7 is cut, the round is the repair alone. The project then waits on his approvals, a dated wait
recorded with `unblock.py tick --owed-call` on the five rows, not an empty tick.
