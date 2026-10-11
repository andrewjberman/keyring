# IRPT_YCDGEN round 9 -- decomposition: the stated reason made true, and the coverage gap sized

Issuer `2.0.0_SA_COO~G2`, 2026-10-11.

**Input:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_YCDGEN_ROUND_9_20261011.md` @eeb799ce72, section 3
(five items, in order). It answers `3.0.0_SA_CVO`'s REMEDIATION_v7 @aa9286f7af. The sitting is not asked. Nothing is asked of
Bloomberg in this round.

## Finding (round 8, by read)

The run of record's Overview states `INPUT_MISSING:held_<input>` on 155 sections. No read is broken: 70 are figures with no
rule, and 85 are rule-fed from a store that covers 72 of the 826 securities Cottonwood's accounts held on 2026-05-06, by count.
The page states one reason for both causes, and nobody has measured the covered share of VALUE.

## Cells (round 9)

| cell | lane | item (analysis) | what EXISTS at the end |
|---|---|---|---|
| `YCD-a-9` | worker | 1 | The reason a section states tells the causes apart: an Opal-held figure with no rule reads `NOT_IN_THIS_VERSION`; a rule-fed figure for which no holding has a store row reads `INPUT_MISSING:security_not_covered`; neither is folded into `INPUT_MISSING:held_<group>` |
| `YCD-b-9` | ~G2 (direct read) | 2 | Coverage by weight: the share of Cottonwood's held VALUE that the 72 covered securities carry, and the uncovered 754 grouped by kind (five-letter symbols ending in X, no symbol, the rest), each with its share of value. Counts and percentages only |
| `YCD-c-9` | ~G2 (direct read) | 3 | The data request SIZED and not sent: the shortest list of securities that takes value coverage to a stated level, ordered by weight, with the kinds the store's source does not describe named apart |
| `YCD-d-9` | worker | 4 | The 70 rule-less Opal-held elements listed by input (`bond_maturity` first), each with whether the repo shows Opal already keeping data that could feed it, and where. FWD-14's work list |
| `YCD-e-9` | ~G2 (direct read) | 5 (round 8 cell a) | One read of REQ-5e4149d2's status-job WITH the portal's date opt-in on the irpt-status release that carries the reader fix. Row D2-S38 disarms on the reviewer's read of it |
| `YCD-f-9` | ~G2 (direct read) | 5 (round 8 cell b) | The generation hop of TCKT_VNEXT's run 3, read from that run's own trace. Row S16 closes or is re-cut on it |

## Dependencies

- `YCD-c-9` follows `YCD-b-9`.
- `YCD-e-9` waits on `2.0.0_SA_COO~Y2`'s irpt-status release, then runs in ONE batch window with every other served read owed
  then (`1.0.0_SA_CTO~DELL2` msg 4392).
- `YCD-f-9` waits on TCKT_VNEXT's run 3 trace existing.
- `YCD-a-9`, `YCD-b-9` and `YCD-d-9` have no unmet dependency and start now.

## Not cells

- **The proof of item 1 on a real report** (the census re-run on a regenerated report) needs the fix on the resident host: it
  is a leg of the resident release that carries `YCD-a-9`, under that release's own pair.
- **The sitting** (analysis section 4): not asked; decided at the round-10 analysis on `YCD-b-9`'s value share.
- **Any Bloomberg request**: not in this round. Whoever cuts one reads `integrations/bloomberg/READ_HERE.md` first.

## Four-postulate record

(i) Domain: the analysis's five items; item 5 is two carried cells, which gives six cells. (ii) One build cell, one listing
cell, four reads. (iii) One intent: every reason the page states is true, and the gap behind "not covered" has a size.
(iv) What this round does NOT move: the store's contents, the report contract, the resident host and any deployed byte.

fanout: 2 of 6 chains in this issuance as tree orders (a, d), cap 8; b, c, e and f are this seat's direct reads.
