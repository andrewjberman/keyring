# RULING 2026-10-14 ~20:2xZ (1.0.0_SA_CTO, cluster lead) -- the 21 Security Analysis gaps fold into dell1's AMGT and DEMQUE projects

**On:** `4.0.0_SA_CRO`'s findings
`org/tier1_exec/4.0.0_SA_CRO/deliverables/SECURITY_ANALYSIS_DAILY_PULLS_DEMQUE_DOSSIER_FINDINGS_20261014.md` @fa0415e1d5. That is
the order of Andrew's ~19:1xZ word, `ANDREW_DIRECT_20261014_191xZ_AMGT_SECURITY_ANALYSIS_DAILY_PULLS_AND_DOSSIER.md`.
Denominator: 95 covered securities.

## The finding in one paragraph

The page is not pulled daily as a whole.
- Four inputs run on a live daily trigger.
- The chatter job runs daily but commits empty.
- About fifteen producers run by hand, lagging 1 to about 19 trading days.
- Seeking Alpha has stopped.
- DEMQUE meters only four one-off requests. The page's largest Bloomberg draw, the model block (~94,900 cells a day,
  INFERRED upper bound), bypasses the queue.
- There is no JSON download (the server returns 400). The gold dossier carries a source on every present value, but no
  research value carries an as-of, and almost none carries a claim.

## Ruling: the CRO's fold-in shape, AS PROPOSED, at overflow priority

dell1 is wholly ADVI/MDPF plus overflow AMGT (`ANDREW_DIRECT_20261014_185xZ_DELL1_WHOLLY_ADVI_MDPF_AMGT.md`).

| project (dell1) | gaps | priority |
|---|---|---|
| **MDPF_DEMQUE** | G9, G10, G11, G12: meter the model block and every other Bloomberg pull through `record_fire_budget`; correct the history and bql reserves to measured use; enrol the covered list as a standing daily tier; give the drawer a `model_block` path | **MDPF work, so dell1's own lane, first.** Unmetered Bloomberg draws are a budget risk across the cluster. |
| **AMGT_RESAPP** | G2-G5, G8, G13-G21, as ONE daily journey: the covered list as the single input (G15), then the producers on schedule (G3, G8, with G4 below), then the page, then the JSON dossier (G13, G14) | overflow, behind ADVI/MDPF |
| **AMGT_HARVST** | G1, G6 | overflow |

## Rulings inside the list

- **G7 (Bright Data SERP, 0 objects, "wired into nothing"): RETIRE the `serp` freshness column (YAGNI).** It reads NEVER for
  every name and nothing writes it. If the management chain later needs CEO search, it comes back as a scoped cell.
- **G13 and G14, the JSON dossier, are Andrew's own ask today and lead RESAPP's list.**
  - `format=json` on the same `/print` route, with a declared `*.schema.json`.
  - Every value carries source, as-of and a claim field (measured, inferred, held or absent), with one absent shape.
  - Drafted sentences read `inferred`.
  - The page is Opal-internal, so the building box's CTO approves the candidate.
- **G6 (Seeking Alpha):** the site Z cycle runner was stopped by an operator at 2026-10-13T23:53Z. Before restarting it,
  AMGT_HARVST reads whether that stop was on Andrew's word. If it was, the restart is his.
- **G16 (AI fill held off the page)** stays held under the round-105 FWD-41 ruling. It is not a gap until that restore is cut.
- **G18 (90/365-day windows)** waits on Andrew's recorded vendor word, as RESAPP v0.35 already says.

## For Andrew (carded)

- **G4: the LLM tier's batch tasks** (drafting and filings, management, posture, scores) were "created DISABLED: activation
  is Andrew's word". Management lags 7 trading days and posture about 19. The REC is to activate them with an event-driven
  trading-day trigger that re-runs only on a new filing, new roster or new model block.

## Route

`0.0.0_AB_MSTR` relays this to `1.0.0_SA_CTO~DELL1`, whose next round analyses for MDPF_DEMQUE, AMGT_RESAPP and AMGT_HARVST
cut these gaps.
