# NFRA_CTLPLN decomposition -- round 25: FWD-16's absent-package arm driven deliberately, dell1's own pip-logged receipt, the organic ask (issuer 2.0.0_SA_COO~C; cut 2026-10-16)

**Status: ISSUED in one issuance. FROZEN at the cut.** (A cell cut later in the round, once its dependency clears, is an AMENDMENT of this document stating its gate limb, as `CT-al-4` was in round 22 and as round 24 stated.)

**Input.** `ledger/ROUND_ANALYSIS.round24.md` (1.0.0_SA_CTO) @6b8e48b0d5 sections 2-3 and msg 109567; the issuer's `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND24.md` and `ROUND24_INPUTS_FOR_ROUND_ANALYSIS.md` @52567a1a41. **PRD:** v0.31 with round-21 ADDENDUM 1. **Coverage entering the round (CTO table, round-24 analysis section 1):** REALIZED 1, 3, 5, 24, 28; ADVANCED 2, 4, 6, 7, 8, 10, 11, 12, 14-19, 21, 22, 23, 25, 27; PARKED 9; MOVED 13, 20, 26. **Cadence:** `/canonical-drive` 30m (LIVE_ARMS @9cb8890499).

## Cells

| cell | what | serves | risk | issued to |
|---|---|---|---|---|
| `CT-ao-1` | **Cut as AMENDMENT 1 (below).** Fetch `tabulate==0.9.0` (`tabulate-0.9.0-py3-none-any.whl`) through the checked route and run checks 1-7 (the shape of `CT-al-1`); the CTO signs check 8. | FWD-16 | SERVED (one public-index fetch into a quarantine folder, as `CT-al-1`) | `0.9.0_WK_NFRA_CTLPLN~127` |
| `CT-ao-2` | **Cut as AMENDMENT 2 (below).** Release, pack and Taildrop to dell1 (the shape of `CT-al-4`), using `CT-an-1`'s pip log from the start. | FWD-15, FWD-16 | SERVED (a release record, a pack and one file set sent to one box; as `CT-al-4`) | `0.9.0_WK_NFRA_CTLPLN~128` |

No order is cut at the issuance: both cells wait on the CTO's decision, which only the CTO can give.

## Amendments

1. **`CT-ao-1` cut, 2026-10-16 ~03:1xZ.** Dependency cleared: status read 2 of 3 reads `APPROVED` for `tabulate==0.9.0` (CTO decision 02:59:56Z, @3ae1c0fc0e) and the CTO's fetch approval is committed (@a486dee2a8, batch `intake-20261016-tabulate`). Status read 3 of 3: `polars==1.12.0` reads `REFUSED`. The one correction to this document: its text below says `requirements.txt` has 98 lines; the CTO's approval counts 98 lines, 93 non-empty (the issuer's own non-comment count is 67); `tabulate` is absent under every count. **Gate limb that graded the amendment:** `.tools/to-pipeline-gate.py` at the commit (a NEWLY-ADDED order; the amendment commit states the limb output). `CT-ao-2` stays deferred to check 8.
2. **`CT-ao-2` cut, 2026-10-16 ~03:3xZ.** Dependency cleared: `CT-ao-1` complete (merge `5834b9f30e`, flip `66837d94dc`) and the CTO SIGNED check 8 (`CTO_CHECK8_NFRA_CTLPLN_INTAKE_TABULATE_20261016.md` @9aed0e1263). Risk class stated as `SERVED` (the first table said `WORLD`; `CT-al-4` carried SERVED for the same release, pack and Taildrop acts, and the paths imply no higher floor). Worker `0.9.0_WK_NFRA_CTLPLN~128`. **Gate limb that graded the amendment:** `.tools/to-pipeline-gate.py` at the commit (a NEWLY-ADDED order). The dell1 call (driven item 3) opens after the Taildrop.

## Driven by the issuer in this round (not cells)

1. **The organic ask, filed first.** Calls `XB-20261016T025654Z-e2a3` (dell2) and `XB-20261016T025654Z-ae75` (site Z) ask each box's CTO the one question dell1 answered NONE to. A YES replaces the stand-in lane before the request is filed; since the request is already filed, a YES names a second request and does not hold this chain. A NONE from both is the organic negative.
2. **The deliberate drive of the arm.** `requirements.txt` read at the cut (98 lines): `tabulate` is absent, and `intake_request.py status --name tabulate --version 0.9.0` read `UNKNOWN`. Request `REQ-20261016T025712Z-tabulate` filed by this lane, a test act stated as one. **Status read 1 of 3 ("not approved"):** `REQUESTED` (issuer read, 2026-10-16 ~02:57Z). **CTO decides** (msg to `1.0.0_SA_CTO`); **status read 2 of 3 ("approved")** by the issuer; **status read 3 of 3 ("refused")** on `REQ-20261015T163055Z-polars`.
3. **dell1's receive on a scratch target.** After `CT-ao-2`, one crossbox call to dell1: pull `CT-an-1`; on the delivered pack run `intake_receive.py verify`, `prove` and `install --target <a scratch folder that is not dell1's TARGET>`; commit the receipts with their pip logs on `box/dell1`; delete the scratch folder. The issuer reads the committed files from `origin/box/dell1`.
4. **`requirements.txt` is not touched by any act of this chain.** The issuer reads the file before (98 lines at the cut) and after; `git diff` of the file across the round reads empty.
5. **duckdb's receipt (FWD-15):** the receipts committed at `d4e34f4a58` stand as relayed, without terminal output; step 3 carries the arm.

## FWD-14, FWD-17 (no cell)

FWD-14 waits on Andrew's sitting (`c9a4`, `b87f`; the Security-log read joins `b87f`). FWD-17 (`318f`) is the CTO's ping to Andrew. FWD-9 PARKED; FWD-2 a qualified wait; FWD-27's person arms Andrew's. `W8-S7` waits behind the outcome cells.

## Carried with an OWNER and the CONDITION that un-parks each

As in the round-24 decomposition: `W8-S7`, `S9103`, `S9120`, `W89-S3`, `W12-S1`, `Z-S3` (before 2027-12-01), `S9125` (dell1, before 2026-12-31), `S9119`, `S9128`, `W121-S3`/`S4`. `W126-S1` is closed by the CTO's acceptance (round-24 analysis ruling 5).

## Rule 24

**Domain:** the CTO's round-24 section 3 enrichment list (3 items) against the open FWD chain; denominator in the CTO's section 1 table (28 FWDs). **Same grain; one intent; disjoint write surface:** both cells write intake records and a release folder under the holding root, not `intake_receive.py` or any tool. **State coherence:** the only network act of the chain is the checked fetch of `CT-ao-1`, the thing under test, which runs on the CTO's approval; no wheel is installed on the laptop; dell1 installs into a scratch folder it deletes.

## Dependency chains and fan-out

Three chains: (1) the organic ask (issuer-driven, no cell); (2) the drive: request, decision, `CT-ao-1`, check 8, `CT-ao-2`, then dell1's receive; (3) FWD-14 (waits on Andrew's sitting). `fanout: 0 of 3 chains, cap 8, reason: the only chain with a cell waits on the CTO's decision; the ask and the status reads are the issuer's own acts, FWD-14 waits on Andrew's sitting`
