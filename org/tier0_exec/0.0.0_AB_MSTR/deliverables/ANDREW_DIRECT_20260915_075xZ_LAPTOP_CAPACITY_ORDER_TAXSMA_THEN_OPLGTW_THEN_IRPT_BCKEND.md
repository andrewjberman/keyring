# ANDREW-DIRECT 2026-09-15 ~07:5xZ -- laptop capacity order: MDPF_TAXSMA, then NFRA_OPLGTW, then IRPT_BCKEND

**Seat:** `0.0.0_AB_MSTR` (laptop) · **Channel:** typed at this terminal, mid-turn · **Recorded:** the same turn it was
given.

## VERBATIM AND ENTIRE

> "If laptop has capacity let's get mdpf_Taxsma going; then nfra_opalgt or whatever the mcp hook up new nfra project
> was, then IPRT_BCKND if the lgic work is in proper position and we can address backend canonically now"

"nfra_opalgt ... the mcp hook up new nfra project" resolves to `NFRA_OPLGTW` (D9; the Claude work-account access
project through the gateway). "IPRT_BCKND" resolves to `IRPT_BCKEND` (D9).

## WHAT IT SETTLES

The ORDER in which laptop capacity goes to three projects: **MDPF_TAXSMA first, NFRA_OPLGTW second, IRPT_BCKEND third**,
and the third only "if the lgic work is in proper position and we can address backend canonically now". That
condition extends his own 2026-09-14 ~14:5xZ word (logic first; the backend follows its patterns).

## WHERE EACH PROJECT STANDS, MEASURED 07:5xZ (project rows at HEAD; `prd-signoff.py status`)

| project | stage | what "going" needs next | whose |
|---|---|---|---|
| MDPF_TAXSMA (D8) | REGISTERED; L2 complete, all eight bars approved | L4 PRD, then the two L4-R signatures | `1.0.0_SA_CTO` (L4 at `1.0.0_SA_CTO~A`) |
| NFRA_OPLGTW (D9) | PRD v0.2 ADMITTED, both halves SIGNED | a COO lane for L5 decomposition, then L6 | a `2.0.0_SA_COO` lane |
| IRPT_BCKEND (D9) | EXECUTING round 2 under `2.0.0_SA_COO~B` | its COO lane, which has no live session; and the CTO's read on the LGIC condition | `1.0.0_SA_CTO` (the read), a COO lane (the round) |

## HOW THIS SEAT APPLIES IT, NARROWLY, AND SAYS SO

- **Capacity** is the three-COO cap on this box. Live COO sessions at 07:5xZ: `2.0.0_SA_COO~F` (IRPT_FNTEND round 8)
  and `2.0.0_SA_COO~G` (LGIC). One slot is free. C: has 20 GB free.
- **MDPF_TAXSMA does not need a COO seat yet.** Its next step is the CTO's L4, so "get it going" goes to
  `1.0.0_SA_CTO` as the priority. Nothing is taken from it by seating a lane for the second project.
- **The one free COO slot goes to NFRA_OPLGTW's L5** now, as `2.0.0_SA_COO~O` (no open task order, surprise row or
  project row names that letter).
- **IRPT_BCKEND waits on two things:** the CTO's read of whether LGIC is in position, and a free seat. Seating a fourth COO
  would break the cap.
- **NOT decided here, carried to him:** when `2.0.0_SA_COO~F` frees after round 8, his 2026-09-14 ~18:2xZ word gives that
  seat to LGIC_CANON. Today's order puts MDPF_TAXSMA ahead once it reaches L5. Which one gets that seat is his call.

## BROADCAST

`1.0.0_SA_CTO` (MDPF_TAXSMA L4 priority and the IRPT_BCKEND/LGIC read), `2.0.0_SA_COO~F`, `2.0.0_SA_COO~G`, and the
new `2.0.0_SA_COO~O` once it is live.
