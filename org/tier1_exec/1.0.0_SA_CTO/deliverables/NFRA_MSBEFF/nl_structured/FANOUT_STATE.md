# NL-corpus fanout — state + relaunch (2026-07-23)

**STATE: BLOCKED-ON-SESSION-LIMIT.** All 10 analysis agents (chunk_01..chunk_10) terminated at
launch, 2026-07-23 ~15:45Z: `You've hit your session limit — resets 2:30pm (America/New_York)`
(= 18:30Z). Zero findings files were produced; the corpus chunks + RUBRIC.md are committed and
intact. Nothing partial exists — a clean relaunch, not a resume.

**RELAUNCH (any ~Z session, after 18:30Z):** for each `chunk_NN.txt` (01..10) in this directory,
launch one general-purpose subagent with this prompt (identical to the first attempt):

> You are an analysis agent for the NFRA_MSBEFF project (Opal comp-tool efficiency audit). Read
> `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_MSBEFF/nl_structured/RUBRIC.md` and follow it
> EXACTLY. Your input is `chunk_NN.txt` in the same directory. Read the whole chunk, extract every
> evaluative finding per the rubric, and Write the JSONL to `chunk_NN.findings.jsonl` in that
> directory. Hard rules: quotes VERBATIM (substring-findable in the source), every row carries its
> SOURCE path, no dedup across sections, no padding from bare-PASS rows. Final message: counts only.

**MERGE + VERIFY (after all 10 land):** concatenate `chunk_*.findings.jsonl` →
`findings_merged.jsonl`; run the quote-verification control (every `quote` must be an exact
substring of its `source` file — a non-matching quote is a fabricated row, drop + count it and
print the denominator); then aggregate verdict × layer × tool × month for the Phase-3 ranking.
