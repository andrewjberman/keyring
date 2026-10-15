# NFRA_CTLPLN decomposition -- round 19: OUTCOME cells first -- the register, the seat list, the unsigned push, the SSH read, the intake records, and one hygiene batch (issuer 2.0.0_SA_COO~C; cut 2026-10-15)

**Status: ISSUED in one issuance. FROZEN at the cut.**

**Input.** `ledger/ROUND_ANALYSIS.round18.md` (1.0.0_SA_CTO, @721e05298f) sections 2-4 and msg 109398; the issuer's `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND18.md`. **PRD:** unchanged. **Process facts in force:** every worker face carries the early-commit and named-VALID-instance lines; each worker worktree is cut by `wk-provision.sh` (sparse) and removed at its merge by `worktree_gc.py --go --only` (a relative path); the CTO's rule from this round: the enrichment list cuts outcome-serving cells first, hygiene at most one batch.

## Cells (serving the open FWDs)

| cell | what | serves | risk | issued to |
|---|---|---|---|---|
| `CT-ai-1` | A fixture box added to a copy of the register is named by every box-reading tool; the 57 placement overlaps each classed SHARED or SPLIT. (`FABRIC_ENUM` has been register-derived since CT-t-3/ab-8; the cell proves the exercise the DONE WHEN names.) | FWD-2, FWD-7 | LOCAL | `~106` |
| `CT-ai-2` | The laptop seat list refreshed (10449 min old), read, and every seat named from the list alone; one finished piece with its grade. | FWD-23 | LOCAL | `~107` |
| `CT-ai-3` | The real pre-push hook, executors stubbed: a push carrying a script no open change names goes through, deploys nothing, and holds the script on a record. The signed-change arm waits on a CloudOps seat. | FWD-5 | LOCAL | `~108` |
| `CT-ai-4` | The laptop-side SSH logins by key to site Z, dell1 and dell2, read once and recorded; the arms only a person or another device can drive are named with owners. | FWD-27 | SERVED | `~109` |
| `CT-ai-5` | ONE hygiene batch: the commit hooks print `not graded: N .tsx` (109393); `org/ref/` in the sparse base set (W105-S2); the batch test leaves no fixtures (W105-S5). | hygiene | LOCAL | `~110` |
| `CT-ai-6` | The package request, decision and downloads-today records that do not exist: `intake_request.py` with file, decide, status, show, downloads. | FWD-16, FWD-19 | LOCAL | `~111` |

## Outcomes driven by the issuer in this issuance (not worker cells)

- **FWD-3:** the open directed pair is laptop -> dell1 (`crossbox-matrix.py`: 11 of 12 acknowledged; dell1 -> sitez is already acknowledged). CALL `XB-20261015T121712Z-5b04` (committed @5b3b8eec9c) asks `1.0.0_SA_CTO~DELL1` to acknowledge; the push and the send are `0.0.0_AB_MSTR`'s (asked). Read when `crossbox-matrix.py` prints `acked=12`.
- **FWD-24:** CALL `XB-20261015T121713Z-e670` puts the same question (an IAM write on a production Lambda role) to `1.0.0_SA_CTO~Z`; the laptop `1.0.0_SA_CTO` is asked the same by message. The two answers are compared on the record when both arrive.

## Outcomes that need a person or another box's seat, named per FWD (CTO ruling 2)

- **FWD-14:** needs Andrew at a MacBook (a real remote-desktop session record). Filed as an act on the laptop list.
- **FWD-17:** needs Andrew to hear the "what was checked and what it cannot rule out" record read to him. Filed as an act on the laptop list.
- **FWD-15:** needs a real Dell lane that needs a package; owner `1.0.0_SA_CTO~DELL1` names one. The route exists and ran once for click 8.3.1 (no lane needed it); with `CT-ai-6` landing, the next round cuts the fetch for the named package. Condition that un-parks it: the named lane.
- **FWD-16:** `CT-ai-6` builds the missing records; the real requests, one approval and one refusal, are acts of `4.0.0_SA_CRO` and `1.0.0_SA_CTO`, driven next round with the tool.
- **FWD-18:** laptop side runs now (`kit_pip_no_egress.py wrap -- download six` prints the refusal that names the route); the attempt on site Z needs a site Z seat (owner `0.0.0_AB_MSTR~Z`), asked next round by crossbox.
- **FWD-19:** `CT-ai-6` builds the reader; a Dell box's day needs that box's seat.
- **FWD-27, the arms outside `CT-ai-4`:** rc and muse logins (Andrew's devices), the laptop as a target (Andrew's one line for a local administrator account), the off-tailnet refusal (`0.0.0_AB_MSTR`), password login off (Andrew's elevated line per box).
- **FWD-8:** no design word is needed yet; not cut this round.

## Carried with an OWNER and the CONDITION that un-parks each

- **FWD-11:** a qualified wait on Andrew's word (open call `laptop-20261014T205216Z-7841`); cut FRESH in the round after he names the hour. **FWD-9:** PARKED (no lease exists). **FWD-6, FWD-10:** the CVO grades them at its next L9 (CTO ruling 1).
- **`S9125`:** dell1, before 2026-12-31. **`S9119`:** read when a dell2 lane is live (owner `0.0.0_AB_MSTR~DELL2`). **`S9103`:** no cell. **`S9120`, `S9122`:** per the CVO. **`Z-S3`, `W12-S1`:** each function's next deploy. **`W89-S3`:** ADVI_FIRMBKTS's. **`D1-S8`:** open, the issuer's; `CT-ai-3` reads the hook and does not fix it.

## Rule 24

**Domain:** the CTO's round-18 section 3 rulings 2-4 (the FWD list) against the open FWDs 2, 3, 5, 7, 14-19, 23, 24, 27 (denominator printed in the CTO's table: 28 FWDs, 2 realized). **Same grain; one intent; disjoint write surface:** each cell writes its own new test file (and `seats.json`, `intake_request.py`, the hook scripts in `CT-ai-5` only); no two cells write the same file except the append-only surprise channel. **State coherence:** no cell deploys, pushes or calls AWS; `CT-ai-4` reads three boxes by SSH key; the cross-box calls leave the held dell1 restart untouched.

## Dependency chains and fan-out

Six chains, no dependency between them. `fanout: 6 of 6 chains, cap 8, reason: six independent laptop worker cells, outcome cells first and one hygiene batch`
