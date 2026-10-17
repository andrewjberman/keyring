# CTO RULING -- open call sitez-20261016T111519Z-bd68: Alyssa's Schwab downloads (2026-10-17 ~02:4xZ)

**By:** `1.0.0_SA_CTO~Z`, under `/self-drive` (the driver rules every open call; only an act that only Andrew can do is listed for him).

## The call

- **The finding:** Alyssa's live grant holds `download_filtered`. PRD v2.2/v2.3 "Unchanged" lists her no-download. The source is
  row Z-S173, measured in OG-mg-1 section 3.
- **Its origin:** Andrew's own word, 2026-10-08: "no downloads needed yet".
- **Why this is not his to answer:** I carded it as "keep blocked or drop the rule". Keeping his stated rule is not a new decision
  of his. Only DROPPING it would need his word. So it was misfiled as an act, and the driver rules it.

## Ruling

**Enforce his word.** Narrow `alyssa@`'s live grant to remove `download_filtered`. Everything else in the grant is unchanged.

- **The act is a NARROWING of a real client's served access, so it carries the three never-widen halves.** It is a literal one-key
  write set, with its before-state recorded.
  - Rollback: re-grant `download_filtered` (revision restore).
  - Read-back: her grant lacks `download_filtered`; a download call by her principal is refused; every other operation of hers still
    answers.
- **Owner:** `2.0.0_SA_COO~O` cuts the order; the applier is `0.7.0_AE_CloudOps~NFRA1`.
- **Andrew can reverse it** at any time with one word: "Alyssa may download". That single word lifts the rule.
- **The open call** sitez-...-bd68 is CLOSED on this record.
