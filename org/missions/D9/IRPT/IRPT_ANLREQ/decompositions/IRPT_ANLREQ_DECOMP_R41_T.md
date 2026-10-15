# IRPT_ANLREQ -- decomposition, round 41, workstream T (issuer 2.0.0_SA_COO~T2)

**Input:** CTO ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_ANLREQ_FOUR_LANES_END_TO_END_20261015.md` lane COMMENTARY, ADDENDUM 1 @d0323f6e0d and erratum @1822f49820
(msg 8392, 8405): (a) Kimi gets abstract figures only (variant and model names; allocation and sector weights as percentages; period and benchmark returns as percentages; top
holdings as tickers with weights), never a name, account number, dollar amount or raw upload row, and the prompt is logged by field name; (b) precedents stay C-SLICE's Outlook
commentary gold, the no-precedent branch drafts and says so in words; Teams transcripts are NOT an input. No PRD addendum; the endpoint is unchanged.

**Thread:** FWD-1 is Y2's. This workstream serves FWD-10 only: the drafter's input, so a draft reads the produced report's figures.

**Measured before the cut** (record `deliverables/2.0.0_SA_COO~T2/R25_T_COMMENTARY_INPUTS_READ_20261015.md`, commits 7a5d98a2ef, fcb85ff151, 749a73ae00): the drafter's prompt carries no figure;
`lambda_handler.py:282` wires `gold_rows` to an empty list; gold has 6 partitions with 0 rows; silver has 12 rows, 11 held out, 1 clear; the retained composition carries no figure and nothing writes
`commentary_basis`. Contract draft `deliverables/2.0.0_SA_COO~T2/C_COMM_FIG_CONTRACT_DRAFT_v0.1_20261015.md` (b7a91d497a), with the producer (`~G2`, read AR-g-54 in flight) and the reader (`~P2`'s surface) not yet agreed.

## Cells

| cell | source | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-t-31` | ADDENDUM 1 (a) | the consumer half of C-COMM-FIG v0.1: `drafter.py` projects `commentary_basis.figures` through a closed whitelist of the seven members (variant, model names, allocation and sector percentages, period and benchmark returns, top holdings as tickers with weights), puts that block and nothing else figure-like in the prompt, and records the prompt's field NAMES (never values) in the draft's provenance; `entry.py` carries the block from the reader's `commentary_basis` into the abstract request. Fakes only; a planted client name and a dollar amount in the basis never reach the prompt. | `data/transcripts/scripts/commentary/drafter.py`, `.../commentary/entry.py`, `data/transcripts/scripts/tests/test_commentary_figures.py` (new) | LOCAL |

## Not cells (and why)

- The producer of the figures (`~G2`'s resident) and the reader that returns them (`~P2`'s surface): other lanes' surfaces; the contract draft is with them.
- The gold re-run over silver and a gold reader port in the Lambda (`gold_rows`): the producer side is the Outlook pull's, not this lane's; named at the drain, cut after the read that finds its owner.
- The deploy of the changed drafter: a WORLD act for the applier under a pair, cut after this cell drains.

## Edges and chains

- One cell. M = 1.

fanout: 1 of 1 chains, cap 8, reason: one cell on a disjoint write set.
