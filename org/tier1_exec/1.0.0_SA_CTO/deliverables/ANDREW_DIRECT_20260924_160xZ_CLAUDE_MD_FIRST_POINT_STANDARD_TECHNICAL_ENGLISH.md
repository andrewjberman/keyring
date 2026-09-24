# ANDREW-DIRECT 2026-09-24 ~16:0xZ -- CLAUDE.md's first point: standard technical English, a prose word threshold, specs never truncated

**Channel:** the 1.0.0_SA_CTO terminal, typed while the CTO was building reports 2 and 3. **Recorded by:** 1.0.0_SA_CTO.
**This record is the ANDREW_LAW_EDIT_ORDER for the CLAUDE.md edit it describes** (`.tools/git-hooks/law-lock-check.sh`).

## Verbatim

> Proceed with your current workflow first and foremost, only when complete you may move onto the next subject,
> included here: Yes another thing I want you to add when you have an opening is an addition in Claude.md. I want the
> first point in the document to instruct that Claude is to communicate in standard technical english. Prose
> responses should have a threshold on word count unless asked otherwise (or in prose-specific exceptions like the
> /exec-sum skill), this is qualified to some extent in the report2 report3 from CRO~A and would tune the threshold
> based on whatever they included in those documents. Technical specs, structured manifests (e.g. json index, yaml
> registry, etc), should never be truncated nor abridged.

## What it orders

1. **Sequence:** the reports 2/3 build finishes first; this edit follows it.
2. **One addition to CLAUDE.md, as its FIRST point:** communicate in standard technical English.
3. **A word-count threshold on prose responses,** unless asked otherwise or in a prose-specific exception (for example
   `/exec-sum`). The threshold is tuned from reports 2 and 3. The figures available there:
   - Rule 31's message cap of 150 words (report 3, Wave 3, would enforce it at the broker);
   - the measured median message of 391 words, with 79-98% of each day's messages over the cap (report 3, section
     1.4).
4. **Never truncated or abridged:** technical specs and structured manifests (a JSON index, a YAML registry and the
   like).

No other line of CLAUDE.md or org/XXX.md is authorized by this record, except the preamble's "Read sections 1-3",
which becomes "0-3" so that the new first point is read.

## Landed

CLAUDE.md `## 0. HOW WE COMMUNICATE`, rule 0, after the reports 2/3 build merged (@6158fc41c4). The threshold is 150
words, the one figure reports 2 and 3 give: Rule 31's message cap, which the broker enforces (LD-0615). Report 3
section 1.4 measured a 391-word median message, with 79-98% of each day's messages over the cap.
