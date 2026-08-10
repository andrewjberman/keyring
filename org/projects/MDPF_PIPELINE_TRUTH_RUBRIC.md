# MDPF_PIPELINE_TRUTH — VERIFICATION RUBRIC (4-agent fan-out)

**Andrew-direct 2026-08-10.** Four agents, one per `status` class in
`org/projects/MDPF_PIPELINE_TRUTH.json`. Each has a **different job**; none of them edits the file.

## 0 · ARCHITECTURAL FRAME — read before deciding what counts as a finding

**Andrew-direct, and it changes the bar:**
> *"We expect bronze ingestion / bronze files / silver ingestion / silver files to all be fairly
> different because they are different data sources. It is in the **gold staging** that we ideally
> flatten down to our **consolidated format** (this is the gold lambda for mdpf), from which point the
> **portal publisher** takes those canonical artifacts to **opal-data-portal-v2** for serving."*

⇒ **VARIANCE AT BRONZE AND SILVER IS EXPECTED AND IS NOT A DEFECT.** Different vendors, different
shapes, different cadences, different key grammars — all fine. **DO NOT report bronze/silver
heterogeneity as a finding.**
⇒ **THE CONVERGENCE POINT IS GOLD.** A defect is: something that **survives into gold**, or something
that makes the gold flattening **wrong / impossible / silently lossy**, or a **divergence between
canonical gold and what the publisher serves**.
⇒ **A per-vendor difference matters ONLY if the gold layer fails to reconcile it.** That is the test.

## 1 · UNIVERSAL METHOD RULES — bind all four agents

1. **READ-ONLY.** Repair nothing, apply nothing, re-run nothing, deploy nothing, delete nothing. You
   are measuring, not fixing. Do not edit the JSON.
2. **PRINT THE DENOMINATOR of every scan you reason from.** A count without its frame is not evidence.
3. **RESOLVE THE TRADING CALENDAR BEFORE ANY STALENESS/GAP CLAIM.** 2026-08-08 = Saturday,
   2026-08-09 = Sunday. **Friday's data IS Monday's correct answer.** This rule has been walked into
   twice today by senior seats; it is CLAUDE.md's first NEVER.
4. **THE CLOCK TAXONOMY** — never conflate: **C1** S3 `LastModified` (when WE wrote it) · **C2** the
   `date=` partition key (**RUN date or DATA date — VARIES, and nothing declares it**) · **C3** the
   as-of INSIDE the file · **C4** the roster/assignment date.
5. **INDEPENDENCE TEST for any provenance field:** it is evidence **only if it CAN DISAGREE** with the
   partition key. A field we write from the key, or a vendor field that echoes the request, is
   **DECORATIVE** — two are already proven so.
6. **DO NOT INHERIT AN ATTRIBUTION YOU DID NOT GROUND.** If you rely on someone else's claim, label it
   and say whose.
7. **`aws` list calls: let the CLI auto-paginate and count client-side.** `--no-paginate` returns page 1
   as a clean complete-looking result. Never `--query 'length(...)'` on a paginated list.
8. **A NEGATIVE RESULT MUST SHOW ITS OBSERVATION.** "Absent" carries the listing it is absent from.
9. **Prefer `comp-*` tools; raw search is the exception** (CLAUDE.md Rule 21).
10. **NO ALARMS, MONITORS, SNS, SES, FRESHNESS CHECKERS.** Standing moratorium. You produce findings.

## 2 · RETURN FORMAT — IDENTICAL FOR ALL FOUR AGENTS

Return **ONLY** a JSON object of this exact shape (so the merge is mechanical):

```json
{
  "agent": "<measured|unmeasured|inferred|not_measurable>",
  "cells_in_scope": 0,
  "cells_examined": 0,
  "patches": [
    {
      "pipeline_id": "inflection.custody",
      "section": "date_semantics",
      "field": "c2_partition_meaning",
      "old_status": "MEASURED",
      "new_status": "MEASURED",
      "new_value": "<the value, or null>",
      "evidence": "<the call you ran or file:line@commit-ish, and what came back>",
      "verdict": "CONFIRMED|DOWNGRADED|PROMOTED|FILLED|REFUTED|UNCHANGED",
      "note": "<one sentence, only if it changes what a reader should do>"
    }
  ],
  "new_findings": [
    {"summary": "...", "pipelines": ["..."], "severity": "HIGH|MED|LOW", "evidence": "...", "survives_into_gold": true}
  ],
  "could_not_do": [
    {"cell": "pipeline.section.field", "why": "...", "what_would_answer_it": "..."}
  ]
}
```

**Rules for the return:** one patch per cell examined — **including UNCHANGED ones**, so coverage is
countable. `cells_examined` must equal `len(patches)`. If you examined fewer than your scope, say so
in `could_not_do` rather than silently narrowing.

## 3 · PER-AGENT MISSIONS

### A · `MEASURED` agent — **VERIFY. This is the highest-stakes job.**
**Scope:** every cell with `status == "MEASURED"` (~186). **Everything downstream rests on these, and
several were asserted fast under time pressure.**
**Your job is ADVERSARIAL:** for each cell, ask *"could this evidence have produced this value if the
value were FALSE?"* Re-derive the ones that carry weight.
- Verdict **CONFIRMED** only if you re-derived it or the cited evidence is directly checkable.
- Verdict **DOWNGRADED** (→ `INFERRED`/`UNMEASURED`) if the evidence does not actually establish the
  value, cites a vintage-less line, or rests on someone's summary rather than the artifact.
- **PRIORITISE** cells that gate action: anything under `cross_firm`, `date_semantics`, the floor /
  publisher times, and every `c1_write_clock_utc`.
- ⚠ **Known trap in this very file:** several MEASURED cells cite *another agent's* measurement. That
  is acceptable **only if labelled**. Flag any that are not.

### B · `UNMEASURED` agent — **FILL.**
**Scope:** every cell with `status == "UNMEASURED"` (~59). Each `evidence` names the call that fills it.
- **Run those calls.** Return `FILLED` with the value and the exact command/output.
- **`49financial.custody` (Schwab) has 19 open cells — the least-assessed pipeline in the estate.
  START THERE.**
- If a call cannot be run, return `could_not_do` with what would answer it — **do not guess, and do
  not mark it NOT_MEASURABLE unless no instrument exists.**

### C · `INFERRED` agent — **RESOLVE. Rule 22: inferred is NON-ACTIONABLE.**
**Scope:** every cell with `status == "INFERRED"` (~11). Each is a hypothesis someone found plausible.
- **PROMOTE** to MEASURED with grounding, or **DEMOTE** to UNMEASURED, or **REFUTE**.
- **Try to KILL each one first.** An inference that survives a genuine attempt to refute it is worth
  far more than one nobody challenged.
- ⚠ **The highest-value cell in your scope is `inflection.custody.date_semantics.consequence`** — if
  Orion silver is not normalised upstream, MDPF labels inflection custody **one trading day late on a
  client-facing number**. Ground it or kill it.
- ⚠ **Second: the mirror→bronze attributions** (`bronze.writer` on both inflection legs) rest on
  **1-minute time tie-outs only**. A rename has been ordered and **a wrong attribution would cement a
  wrong name.**

### D · `NOT_MEASURABLE` agent — **CHALLENGE, then widen.**
**Scope:** the 3 cells with `status == "NOT_MEASURABLE"` (all on `inflection.model` / eclipse).
- **First ask whether the WRONG INSTRUMENT was tried.** "Not in the artifact" is not "not measurable" —
  the ingest source, the vendor contract, a value tie-out against a known-dated source, or the
  producer's own log may all answer it.
- **The load-bearing one is eclipse's `c2_partition_meaning` (`G-3b`).** Eclipse is the MODEL leg — the
  one that actually fails. **If eclipse's `date=` is a RUN date, then Inflection is NOT missing
  2026-08-06 and today's entire diagnosis moves.**
- ⛔ **DO NOT infer eclipse from Orion.** The estate's own normalizer says *"Orion-only … never call on
  schwab/bd — their labels are accurate,"* so a **per-vendor** label policy already exists and eclipse
  is simply unclassified.
- If it truly is not measurable, return the **reason** and **what would make it measurable** — that is
  a legitimate, valuable result.
