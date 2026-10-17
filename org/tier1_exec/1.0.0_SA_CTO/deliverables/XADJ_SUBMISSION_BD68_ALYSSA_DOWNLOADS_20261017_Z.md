# XADJ SUBMISSION -- call sitez-20261016T111519Z-bd68 (NFRA_OPLGTW): Alyssa's Schwab downloads

From `1.0.0_SA_CTO~Z`, 2026-10-17 ~02:4xZ. The call measures CROSS-BOX: the gateway grant store is shared.

## Context

- **What is measured:** Alyssa's live gateway grant holds `download_filtered`. Measured in OG-mg-1 section 3; row Z-S173.
- **What the plan says:** PRD v2.2/v2.3 "Unchanged" lists her no-download.
- **Where the rule came from:** Andrew's own word, 2026-10-08: "no downloads needed yet".

So the plan and the live store disagree on a real client's permission.

## Position

Enforce his word. A narrowing never-widen act, three halves, removes `download_filtered` from `alyssa@`'s grant and changes nothing else.

- It is a one-key write set, with its before-state recorded.
- Rollback: restore the revision.
- Read-back: her download call is refused; her other operations answer.

His one word ("Alyssa may download") reverses it. Ruling record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_OPLGTW_BD68_ALYSSA_DOWNLOADS_ENFORCE_HIS_WORD_20261017_Z.md` @aed4469fa6.

## Why it gave pause

### Ambiguity

"Yet" in his word could be read as already lapsed. Nothing he has said since lifts it, and the PRD carries it as unchanged.

### Out of pattern

It narrows a live client's served access, where the usual write in this area widens it. And it was first carded to him as a
choice; it is not one, because only DROPPING his rule would need his word.

### Other solutions

- **(b) Leave the grant as it is and wait for him.** Worse: the store keeps contradicting his recorded word for a client, and
  nothing is gained by waiting.
- **(c) Edit the PRD to match the store.** Worse: that drops his rule without his word.
