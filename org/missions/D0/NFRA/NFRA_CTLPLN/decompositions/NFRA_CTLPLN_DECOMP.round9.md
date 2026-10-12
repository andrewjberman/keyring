# NFRA_CTLPLN decomposition -- round 9: close the open FWD-28 work, the re-based live thread (E1), the design-text correction, with a stated carry for every enrichment not cut (issuer 2.0.0_SA_COO~C; cut 2026-10-12)

**Status: ISSUED in one issuance (one direct-act worker order and one seat order, plus the carried open orders and the issuer acts below). FROZEN at the cut.**

**Input.** `org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.round8.md` (1.0.0_SA_CTO msg 108511), section 3. Round 8 closed first (`round-close-check --round 8` MAY-CLOSE, proof_bad 0, 3 of 3 judgments graded, 64 gating items dispositioned).
Cut on PRD v0.25.

## The analysis's items, each with its disposition (denominator: 7)

| # | item | disposition |
|---|---|---|
| 1 | `CT-w-8`, `CT-w-9`, `CT-w-10` first, as opened | CARRIED, already issued: `CT-w-8` (workstream FIRMPG round 1, worker `~70`, running), `CT-w-9` (LOGFIX round 1, worker `~71`, running), `CT-w-10` (LOGFIX round 1, seat order for `0.7.0_AE_CloudOps~U7`, staged until `CT-w-9` and `CT-w-8` are merged and the THIRD pair is signed). They are named here so the round-9 drain reads them. |
| 2 | The portal carrier regenerated with `note`, set-equality re-proven, landed on DEV by the author | ISSUER ACT A9, after `CT-w-8` merges: land the regenerated portal commit on portal DEV as a fast-forward under the push law (the CTO's review of the regenerated commit stands if the two proofs hold: 4 firms, 35 pairs set-equal, hand-kept lines byte-identical); the workspace gitlink after; the PROD push is Andrew's. |
| 3 | The crossbox design-text correction (HALF-CLOSED wording) | CUT: `CT-y-1`. |
| 4 | E1: the re-based live thread | CUT: `CT-y-2` (a dell1 seat order issued from the laptop; the trace of ITS round is the exercise). Evidence already in hand, not a substitute: `E1_THREAD_TRACE_LGIC_BLANKFIX_R9.txt` (5 of 5 hops, `pushed_by_working_box=False`, 2h14m23s). |
| 5 | E4: the 12-message matrix | CARRIED, stated: `python .tools/crossbox-matrix.py` reads `pairs=12 with_file=12`; the gaps are acks, and each rests on a seat that is not running. (a) laptop->dell2 `XB-20261012T070501Z-cb95` and dell1->dell2 `XB-20261012T033435Z-54b6`: dell2's manager session is down (`0.0.0_AB_MSTR~DELL1` bus read: no consumer since 2026-10-11 ~13:11Z, 17 messages visible); restarting it is an act at Andrew's dell2 terminal, raised to him by MSTR. (b) dell2->laptop `XB-20261012T024226Z-0dce`: addressed to `0.7.0_AE_CloudOps~ANL`, stood down; the file is dell2's to withdraw or close. Nothing here is a cell an agent can run. It reads again at this round's close. |
| 6 | E2-E3, E5-E8 of the 2026-10-09 list | CARRIED with the state at this cut: E2 done (`TO-CT-x-1`); E3 done on dell1 (`CT-v-1`, `CT-v-3`, `CT-w-5`), the read-aloud to Andrew is his act; E5 done (`TO-CT-t-3`); E6 an ask to `3.0.0_SA_CVO~L` and Andrew, carried by the CVO and Andrew; E7 an ask to each box's manager and `0.0.0_AB_MSTR`, carried by MSTR; E8 done (census in round 7, design in round 8). |
| 7 | E9 FWD-27 | GATED on Andrew's public keys and elevated lines; no cell runs without them; the per-box cells are re-cut ACTIVE with their GO when the keys land. S9111 stays OPEN with the shared portal API root's owner. |

## Cells

| cell | what | serves | risk | issued to |
|---|---|---|---|---|
| `CT-y-1` | DIRECT ACT: correct the wording of the crossbox design document's HALF-CLOSED row (a half-closed call with no ack reads OPEN today; the state comes from the ack first) and add the CVO's one-sentence note | FWD-3, FWD-8 (hygiene) | LOCAL (a document under a deliverables folder) | `0.9.0_WK_NFRA_CTLPLN~72` |
| `CT-y-2` | E1: a REAL thread. This order is planned on the laptop (this issuance), worked and committed on dell1 by `0.7.0_AE_CloudOps~CT1` on `box/dell1`, published by dell1's box-sync, integrated into `CLOUD` by the integrator, graded on the laptop. Its content is a read-only dell1 record that closes a caveat of `CT-v-3`: from a process started AFTER the `PIP_NO_INDEX` user variable was set, the explicit-index download is stopped. | FWD-1, FWD-4, FWD-18 | LOCAL (a read; no change on dell1) | `0.7.0_AE_CloudOps~CT1` (dell1) |

## Rule 24

**Domain:** the seven items above. Every item has a disposition naming its owner or its cell; no item is left unnamed. **Same grain; one intent each.** **State coherence:** `CT-y-1` changes one document; `CT-y-2` changes no machine, it writes one record.

## Dependency chains and fan-out

`CT-y-1` and `CT-y-2` share no file and no edge: M = 2 chains, one worker (`CT-y-1`) and one seat order (`CT-y-2`). The carried orders keep their own workstreams.

`fanout: 1 of 2 chains, cap 8, reason: CT-y-1 is the only worker order; CT-y-2 is a seat order on dell1; the carried CT-w-8, CT-w-9 and CT-w-10 run in their own workstreams`

## Issuer acts (the COO's one real run of each outcome, at the close)

- **A9:** the portal carrier landing described in row 2.
- **A1 (round 9):** `python .tools/thread-trace.py --project NFRA_CTLPLN --round 9 --fetch` after `CT-y-2` is integrated and graded; its last line goes to the record with the hop times.
- **A4:** read `crossbox-matrix.py` at the close.
- **Third pair for `CT-w-10`:** the COO half is written at its GO.
