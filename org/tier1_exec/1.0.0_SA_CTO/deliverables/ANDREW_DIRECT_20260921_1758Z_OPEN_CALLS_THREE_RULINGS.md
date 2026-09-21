# Andrew-direct -- 2026-09-21 ~17:58Z, at the `1.0.0_SA_CTO` terminal (live chat, answering `/open-calls`)

**Channel:** direct conversation with `1.0.0_SA_CTO`, answering the 3-card `/open-calls` output.
**Time:** 2026-09-21 ~17:58Z (measured `date -u`).

## THE THREE RULINGS, VERBATIM AND ENTIRE

> "call 1) Can autoclassify, anything new that says opal in it will be a custom model. 2) rec
> approved. 3) sure rec approved."

## What each answers, and what it authorizes

**CALL 1 -- the name-discovery scanner.** My card asked whether to wire `mdpf_name_discovery.py`
into a scheduled sweep that SURFACES new candidates for manual review (the tool's own design:
never auto-classify). **His ruling goes further and simpler than my REC: auto-classify.** Any new,
unmapped name matching "Opal" (word-boundary, case-insensitive, the same style the estate's own
`_norm`/`matches_word_boundary` already use) becomes a CUSTOM model automatically -- no human
review gate, no pipeline break. This supersedes the discovery tool's `ND-inv-2`/`ND-f-1`
never-auto-classify design **specifically for this one classification** (Custom is the safe,
non-specific catch-all; it cannot inflate a primary/headline figure by construction), not a
blanket repeal of that design principle elsewhere.

**CALL 2 -- Fixed Income / Custom-list naming: APPROVED.** Fixed Income stops carrying its own
`by_model` line (rolls into Other AUA like every other Custom entry); real composed Custom models
and true non-model residuals are treated the same way for Custom-list naming (both individually
named); same deploy cycle as the Cottonwood fix.

**CALL 3 -- stop `irpt-ycharts-runner`: APPROVED.** Authorizes the EC2 stop this seat's own prior
ruling withheld pending his word.

## Execution, same turn

1. Stop `i-0167fd745ad906a66` (`irpt-ycharts-runner`) now.
2. Design and land the auto-classify-as-Custom mechanism (Call 1) + the Fixed Income /
   Custom-list-naming fix (Call 2) as one coherent change, source-first, verified before any
   deploy pin-bump -- both touch already-served MDPF data, same discipline as every other
   served-output change today.

**PUSH STATE:** LOCAL -- this seat does not push a shared branch.
