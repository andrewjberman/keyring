# NFRA_DEVPLN round 6 -- drain-end read to 1.0.0_SA_CTO (issuer 2.0.0_SA_COO~DV, 2026-10-14T01:45Z)

Issuance `cf8b7618e0` (PRD v0.3 @14a0501ee5, round-5 analysis @6bbbc233d4). `python .tools/round-close-check.py --project NFRA_DEVPLN --round 6` reads `reviewer=present (3.0.0_SA_CVO~L) orders=1 verdict=MAY-CLOSE`. Push state (ls-remote `1b96ebb9cc`): `cf8b7618e0`, the DP-h-1 merge `a3af4ce06d` and the evidence/row commits are on origin/box/laptop; the close commit is LOCAL. No SERVED or WORLD order this round, so no CVO packet.

## 1. The order (1 of 1 complete, proof VALID, every suite re-run on the merged tree)

| cell | result | merge |
|---|---|---|
| DP-h-1 | `OPAL_CLOUD_READ_LOCAL` is honoured only when `OPAL_STATE_ROOT` is also set; set without it, it is ignored with `NOTE: OPAL_CLOUD_READ_LOCAL ignored: it is a test seam and OPAL_STATE_ROOT is not set`. Cloud-read test 10/10; the other suites 7/7, 11/11, 10/10, 13/13, 19/19 and the payload limb 19/19 stay green | `a3af4ce06d` |

The hazard was reproduced at the base and re-measured after the merge: with a stray `OPAL_CLOUD_READ_LOCAL=/tmp/ocl_probe` (a 2099 fixture, no rows) and no test switch, the real dell1 row read `ABSENT` before and reads `state=APPROVED valid=yes` after.

## 2. The limb install (act A15): 4 of 4 boxes reported by MSTR

Laptop, VERIFIED by the issuer through the installed hook: `cmp` of `portal/.git/hooks/pre-push` against the canonical source is identical; an unapproved commit onto DEV exits 1 (`REFUSED reason=unapproved-commit`); the approved dell1 merge `5e40e541` exits 0 (route A); the PROD-into-DEV merge `63c4f9e3` exits 0 (route C). Re-run after the hook changed (below).
Site Z, dell1 and dell2: reported by MSTR (cmp rc 0, demonstration 1 exit 1 REFUSED, D-1 VALGATE running), dell1 and dell2 on a submodule (gitlink) layout. The issuer's own check of those three is the source blob only: the hook file is the same blob on origin/box/{laptop,dell1,dell2,sitez} and origin/CLOUD. An installed copy on another box is read by MSTR's report; it is the oracle, not the issuer.
The hook changed twice after my merge `367ce6ff40`: MSTR's `6d0381ff98` (finds the real hooks directory and the gates on a submodule layout) and your ruling commit `38d124d991` (a missing gate script fails closed on DEV and PROD). The second supersedes item 5 of order DP-f-1 (it said WARN and do not block). Current blob `8d7368862d95`: committed, working tree and the laptop's installed copy agree.

## 3. Other measured facts

- A second organic promote: PROD `7d5cb34d` (tag `portal-v2.1.215`, CI success) ships the dell1 feature alone, built by a dell1 worker. Direct first-parent read of `origin/PROD` since the settlement: 2 commits, both two-parent merges with both trailers, `unapproved=0`; none of the seven unapproved dell2 DEV commits shipped. Record: `NFRA_DEVPLN_DELL1_ORGANIC_ROUTE_EVIDENCE_20261014.md` (addendum).
- Row `S4`: `portal-release-build.sh --check <name>` reads a stale LOCAL branch of the same name before `origin/<name>` (`--check PROD` printed the stale local tip) and does not print which ref it read. Not cited as evidence; a small repair candidate.
- The DT's ledger `20261013T2048Z_devpln-r2-chosen-set-promote-20261013_deploy_completion.md` reads CLOSED in the laptop working copy but is UNCOMMITTED, so CLOUD and other boxes read it OPEN (MSTR's relay). Asked the DT to commit it under `TO-DP-x-1` step 5; no reply yet.

## 4. Awaiting Andrew (client-facing; neither you nor the CVO can rule these)

dell2 rows `3635`, `8500`, `7b45`, `fde0`, `7773`, all OPEN; the law-edit card `laptop-20261013T223003Z-3d7e`. Act A14 (the integrator's merge-forward, then the DT's chosen-set promote naming only what he approves, SERVED, with the L8 packet) cuts no order until he rules.

## 5. Rows and watermark

Channel: 40 investigation rows, 7 adjudication rows, ARMED 0, 12 open observations (new this round: `S4`, `W1-S16`: test case 9 runs a production git lookup of a ref that exists nowhere, reads nothing).

## 6. ENRICHMENT candidates for round 7

1. After Andrew rules: A14, the client-facing close of FWD-1.
2. One small repair if you want it in code: `S4` (print the resolved ref and sha on the release lines; prefer `origin/<name>` for a trunk name) and `W1-S16` (case 9 should not run a real ref lookup).
