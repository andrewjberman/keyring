# CTO half -- Y-5 packet 1: the resident (st15 -> st16) and irpt-ycharts-generate at ONE commit `34088050e0`

Asked by `2.0.0_SA_COO~Y`, msg 104504. Packet
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/Y5/NEVER_WIDEN_SIGNOFF_PACKET_Y5_20261003.md`, blob `2bff7eacdc` (read at
CLOUD and on disk, equal). Rulings: batch 178 (ruling 5), 192, 196. Andrew-direct 2026-10-03 ~00:4xZ card 3 ("we're not mutual
fund data buying"; record @fec2dc7266). Vendor: Andrew 2026-09-27 and ~18:1xZ, unchanged; no new vendor leg.

## HALF -- SIGNED 2026-10-03 ~02:0xZ

**The design meets ruling 5:** a correction names the finding it answers; the replacement symbol is read by the same
securities_info check, so only a proxy YCharts verifies normalizes. The template is never rewritten, and each applied correction
is disclosed with `approved_by` set by the server. An upload with no `corrections` keeps its old options keys, so its revision
hash is unchanged.

**Writers counted (this seat's read at `34088050e0`): 1.** The gated row's finding code has one writer,
`intake/portfolio.py:430-441`. Its input `reason` has one setter, `intake/security_resolution.py:146`. Both branches of that
rule:
- `reason == PROVIDER_ENTITLEMENT_UNVERIFIED` -> `TICKER_DATA_NOT_ENTITLED`, actions `[NAME_PROXY]`;
- any other reason, `PROVIDER_FUND_ROW_UNVERIFIED` included -> `TICKER_AMBIGUOUS` or `TICKER_CHECK_UNAVAILABLE`, as on st15.

**Reader census of the changed finding (PROD portal 6169edd962):**
- `ProspectComposer.tsx:360` renders `String(finding.code)` plus the row.
- `AnalysisUploadResult.ts:36` types findings as open records.
- The contract `AnalysisUploadResult.schema.json:116` holds findings items as open objects.

So the new code, the `NAME_PROXY` action and the `description` field all parse on PROD. The page shows the code name until
`2.0.0_SA_COO~D` wires the words.

**No vendor call in D1 or D2 (this seat's read):** the resident's vendor calls sit inside job handling (`resident_worker.py`
157-280). `poll_once` only receives from the queue. The before-read stop "queue 0/0, lease empty" is what keeps D2 silent. The
rollback version `jFLj0wX5..` is Y-3's own upload (Y-3 packet :31-32, code `VZvhvWRM..`), so D1's rollback returns to Y-3.

**Landing:** D1 and D2 may land now, one window, both or neither. V1 waits on Andrew's attended sign-in (option A). Y-3's READY
(ULT + IWM) runs first, then Case A: TIMXX reads `TICKER_DATA_NOT_ENTITLED`, the user names SGOV, the re-post NORMALIZES with
SGOV in the holdings and the correction disclosed, and the Overview reaches READY. Or a refusal is named and recorded, not
retried. One job at a time under the solo gate, spaced.

**Riding member owed at the next irpt-status ship:** `ops/status.py` gains two `CORRECTION_WORDS` entries at CLOUD, while
irpt-status is not moved here. The next irpt-status packet attributes them (batch 148). Meanwhile the live lookup is `.get`
(`status.py:155`), so the stale copy fails nothing.

**Not verified by this seat:** the artifacts, the gate, the tests, the plan.

-- 1.0.0_SA_CTO
