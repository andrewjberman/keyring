# NFRA_CTLPLN decomposition -- round 23: the package journey's repair, the hygiene batch in two cells, and the issuer's reads (issuer 2.0.0_SA_COO~C; cut 2026-10-15)

**Status: ISSUED in one issuance. FROZEN at the cut.**

**Input.** `ledger/ROUND_ANALYSIS.round22.md` (1.0.0_SA_CTO) sections 1-3 and msg 109512; the CVO's slug `surprise-channel/adjudications/ADJUDICATION_v27.md` @2464796293; the issuer's `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND22.md` @51ed0a460a. **PRD:** v0.31 with round-21 ADDENDUM 1. **Coverage entering the round (CTO table):** REALIZED 1, 3, 5, 24, 28; ADVANCED 2, 4, 6, 7, 8, 10, 11, 12, 14-19, 21, 22, 23, 25, 27; PARKED 9; MOVED 13, 20, 26. **Process facts in force:** the round-19 worker-face lines; sparse worktrees cut by `wk-provision.sh`; removal at merge by `worktree_gc.py --go --only`; a worker branch cut before an amendment cannot validate against it, so the issuer merges first and validates in the main tree; the registry lanes admit only a worker serial to scripts and test batteries; a seat's row carries no worker coordinate and a dismissed row needs `dismissal_reason`.

## Cells

| cell | what | serves | risk | issued to |
|---|---|---|---|---|
| `CT-am-1` | `intake_receive.py` classes a COLOURED ModuleNotFoundError as a missing dependency (dell1's `install --dry-run` was refused because `FORCE_COLOR=3` wrapped the module name in ANSI codes), and runs its children plain. | FWD-15, 16, 18, 19 | LOCAL | `0.9.0_WK_NFRA_CTLPLN~123` |
| `CT-am-2` | HYGIENE batch A: only the main tree builds the danger map, with `portal/` initialized, and the header names its inputs (`W121-S3/S4`); check 8 is recorded as awaiting, not failed (`W119-S1`); the two real 20261008 fetch records are counted for the laptop by a batch declaration (`W111-S1`). | hygiene | LOCAL | `0.9.0_WK_NFRA_CTLPLN~124` |
| `CT-am-3` | HYGIENE batch B: `crossbox-call.py merge` keeps a null bus id and writes nothing when it refuses (`S9121`); the crossbox suite passes in a sparse worktree (`W79-S2`). | hygiene | LOCAL | `0.9.0_WK_NFRA_CTLPLN~125` |

The CTO asked for ONE hygiene batch; it is cut as two cells (A and B) because its seven items exceed one worker's size floor, and `W8-S7` is carried out of it (below).

## Driven by the issuer in this issuance (not cells)

- **The package journey on dell1 (FWD-15/16/18/19):** dell1's CTO read steps 1-3 OK (all 4 SHA-256 equal, `verify` ok, `prove` installed 1 imported 0) and step 4 REFUSED by the colour bug (call `7bc4`). The issuer answers dell1's question by crossbox: re-run `prove` and `install --dry-run` with `PYTHON_COLORS=0` and `FORCE_COLOR` unset (no tool change needed on dell1), then `install --target`, then the lane's read; `CT-am-1` fixes the tool so the next pack does not need the workaround. The issuer then reads the receipts and the lane's record; the CVO reads the whole journey back.
- **FWD-11:** the CTO read `ib549` (NOT interrupted by the restart, msg 109512's companion); the remaining 15 open dell1 entries read ORDINARY; dell2's manager reports `0.7.0_AE_CloudOps~IB2` LIVE on dell2. FWD-11's per-owner read is complete for the issuer's side; the CVO re-reads it.
- **FWD-14:** the CTO files ONE laptop act beside `c9a4` (a session from this laptop to site Z, dell1 and dell2, and one attempt from off the tailnet). The issuer's reads of the two boxes' logs (calls `2765`, `6c75`) found no trace of the laptop's attempts in the connection manager logs (18 and 20 events in the window, 0 carry `100.96.167.100`); the Security log (failed logons, event 4625) is unread on both boxes (the shell is not elevated and the managers did not open one without Andrew's word) and dropped-packet firewall logging is off on both, so there is no negative proof. Reading the Security log needs an elevated session: an act for Andrew's word, folded into the CTO's laptop act.
- **The four kept-open rows (CTO ruling 4), the issuer's reads:** `S9105` (the three `org/devices` edits of AMENDMENT 9 are commit `5e5e9db7a9` by worker `0.9.0_WK_NFRA_CTLPLN~13`, an ancestor of `box/laptop` HEAD and of `origin/CLOUD`); `S9101` (the step-4 text of AMENDMENT 9 now names five roots and `seeking-alpha` as a configuration defect, commit `5882eb4273`); `W111-S1` and `W79-S2` are in `CT-am-2` and `CT-am-3`.

## Carried with an OWNER and the CONDITION that un-parks each

- **`W8-S7`** (`dell_fence_census.py --live` rewrites its sibling check's baseline): the files are under `infra/aws/terraform/shared-infra/tests/`, an infra path, so the cell is WORLD by the path floor and owes the CRO's research first; owner the issuer; cut when the CTO wants it ahead of the other hygiene.
- **FWD-9:** PARKED. **FWD-14 calls `c9a4` and the CTO's new laptop act, FWD-17 call `318f`:** Andrew's. **FWD-2:** a real second box is a qualified wait. **FWD-27's person arms:** Andrew's.
- **`S9103`, `S9120`, `W89-S3`, `W12-S1`, `Z-S3`, `S9125`, `S9119`, `S9128`:** as in the round-22 packet, section 5.

## Rule 24

**Domain:** the CTO's round-22 section 3 enrichment list (4 items) against the open FWD chain; denominator in the CTO's section 1 table (28 FWDs). **Same grain; one intent; disjoint write surface:** `CT-am-1` writes `intake_receive.py` and its tests; `CT-am-2` writes the graph-module map tools, `intake_check.py`, `intake_request.py`, one declaration file, one round-22 test and its own test; `CT-am-3` writes `crossbox-call.py` and its test suite; no two cells write the same file except the append-only surprise channel. **State coherence:** no cell deploys, pushes or calls AWS; no wheel is installed on the laptop.

## Dependency chains and fan-out

Three chains, no dependency between them. `fanout: 3 of 3 chains, cap 8, reason: three independent laptop worker cells; the dell1 install and the lane's read are crossbox acts of dell1's CTO, the FWD-14 reads wait on Andrew's acts`
