# Andrew-direct, 2026-10-05 ~21:3xZ (5:3x PM Eastern), at the 4.0.0_SA_CRO terminal -- VERBATIM

Channel: typed by Andrew into the 4.0.0_SA_CRO (base) session, in answer to this seat's `/open-calls` (three cards).

> Recs approved. My only other concern with the canonical table is regarding CIK. I'm wondering if it is
> prudent/needed to include a CIK field as well as sector field when we make the edit here.

## The three cards he answered, with each REC as it was shown to him

1. **Does the approval of the AI classifier cover the 668 held securities labelled today only by a guess?** REC: yes,
   with the condition already set, that every AI-made row is listed in one index. (MDPF_SECCLASS; the 668 are in
   `docs/briefs/one-classification-table-consolidation-analysis-20261005.md` section 3.)
2. **In-house Analysis report, while Yahoo is the data source: Yahoo's sector names or GICS?** REC: (a) Yahoo's scheme
   for now, stated on the page; switch to GICS when the canonical table is the sector source for the report.
   (IRPT_YCDGEN; `docs/briefs/irpt-ycharts-inhouse-generation-yfinance-probe-20261005.md` section 3.)
3. **Does "only the canonical table" also apply to the Schwab firm composition?** REC: no, keep it as the one named
   exception for now; revisit once the canonical table covers every held security.

## The CIK question

He asks whether a CIK field should be added to the canonical table alongside sector. It is a question to this seat,
not a ruling. This seat's answer is given to him in the session and is not a decision until he rules on it.

## Routing

One line to `1.0.0_SA_CTO` naming this record: the three approvals bear on MDPF_SECCLASS (cards 1 and 3) and on the
IRPT_YCDGEN endpoint revision (card 2).
