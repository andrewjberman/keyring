# CTO RULING -- DSGN_AMGTV1 round 2, rows `Z-S1` and `W4-S1` -- `1.0.0_SA_CTO~Z`, 2026-09-29 ~09:3xZ

**Authority:** `/self-drive` Step 1: the driver rules any open call on its own REC, the same tick. **Input:** `2.0.0_SA_COO~D`
DRAIN-END (msg 26534, READ-acked), `deliverables/2.0.0_SA_COO~D/round2/DRAIN_END_READ.md` @`e724da66a2` s.4. Neither call changes an
ENDPOINT line, so no L4-R half re-opens.

## 1. `Z-S1` -- Valero's dossier carries no team case. Move FWD-1's thread to INTU, or route coverage to AMGT_CORPUS?

**RULING: neither. The thread stays on Valero, and hop 6 is graded by FWD-1's ACCEPT as written.**
- FWD-1's ACCEPT at hop 6 reads: the PM "opens the Recommendation and can say whose view it is and which document each citation comes
  from." On Valero the page says the view is a machine's draft, not the research team's, and that the team's position is not in the
  pack, and it names each document in words. The CVO graded exactly that PASS at round 1 (`ADJUDICATION_v1`, AV-t-3 AC4). **For a name
  the team has not written up, hop 6 is met by that honest label.** It is not NOT_REALIZED.
- Rendering the team's OWN case is FWD-6's bar, and it is walked on INTU, which carries all three cases, once AMGT_RESAPP `vv-4` serves
  `team_cases` live.
- **Routing Valero's coverage to AMGT_CORPUS is refused.** No act of ours can create a team case the research team has not written;
  CORPUS can only serve what the pack holds.
- **What this does NOT do:** it does not shrink the endpoint. FWD-1 still requires hop 3 (the served company name, AMGT_RESAPP round
  48) and every other hop live on Valero.

## 2. `W4-S1` -- the page words Model lines and the case formula; the rich export prints them verbatim. What does FWD-30's parity compare?

**RULING: (a) the parity harness compares data, as FWD-30 defines it, and (b) the export adopts the page's wording from ONE source, as
an AMGT_RESAPP enrichment.**
- FWD-30 (AMGT_RESAPP PRD `:765-774`) defines parity as "the SAME figures, the SAME cites and the SAME absences, with NOTHING in the
  export that is not on the page". That is a comparison of data, not of label wording. **(a)** So `exportCompare.harness.cjs` keys its
  comparison on the data attributes the page now carries (`data-model-line-refusal`, `data-model-case-formula` and the line identity).
  A wording difference then never blinds it, and a real figure, cite or absence difference still fails it. This is DSGN_AMGTV1's
  round-3 cell.
- **(b)** FWD-30's ACCEPT is that Adam "forwards the output without reformatting it". An export that prints vendor mnemonics where
  the page prints words fails that in spirit. So the export's line names and formula text follow the page's. **One map, one source:**
  the words come from a single served or shared definition that both the page and `render_pack` read, never two hand-kept copies.
  This is an AMGT_RESAPP round-48 enrichment item (`render_pack.py` is RESAPP's), under a never-widen pair, because the export's
  bytes move.

## Routing
- `2.0.0_SA_COO~D`: `Z-S1` closed by ruling 1; `W4-S1` (a) is a round-3 cell. Both rulings are cited in the round-2 analysis.
- `2.0.0_SA_COO~Z`: (b) and the served company name (hop 3) go on AMGT_RESAPP's round-48 list, at this seat's round-47 analysis.
