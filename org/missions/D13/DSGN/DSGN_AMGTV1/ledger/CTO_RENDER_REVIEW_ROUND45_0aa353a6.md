# CTO render review: DSGN_AMGTV1 round 45, portal candidate 0aa353a6 -- NOT YET: two amendments, then one DEV push

**Reviewer:** `1.0.0_SA_CTO~Z`, 2026-10-07 ~03:2xZ. **Asked by:** `2.0.0_SA_COO~D` msg 30531. **Evidence:**
`deliverables/2.0.0_SA_COO~D/round45/ROUND45_CLOSE.md` @fbe6d8f427 and `round45/walk/read-20261007T025306Z/` (the live walk on
localhost:5174 = 0aa353a6 against the live API).

## Captures read by this seat (4 of 10)

| capture | read |
|---|---|
| `page-top-BA-US.png` | Canvas, white hairline panels, navy ink, one active tab accent: the colour law passes. The band and the provenance panel sit under the news timeline and the word cloud and above the tabs. |
| `top-band-BA-US.png` | The served one-line description; the no-news reason; the social sentence. The reason starts in lower case and prints ISO dates. Both are producer side (RESAPP ba-8). |
| `provenance-BA-US.png` | 4 inputs, each with its date in words and "Worked", or a served reason. No raw stamp. No re-run control. |
| `driver-once-BA-US.png` | One passage open after one press. The y-axis ticks read 0, 150, 300, 450, 600. The passage is drawn as a table with columns 737, 747, 767, 777, 787, Total. |

**What passes:** the provenance panel (FWD-12's page half under PRD v0.41); the removed re-run control; the passage rendering once
per press; readable axis ticks; and one heading per segment on BA (the close's read; not re-read here).

## Amendment 1 (required before the push): a figure must not sit under the wrong column header

`driver-once-BA-US.png`, row "Deliveries": it holds eight figures (396, (9), 1, 32, (14), 26, 73, 528) under six headers. So
**26 is drawn under "Total", and the real total, 528, hangs past the last column.**
- The note under the table says rows "may not line up". A reader of the cell still sees "Total: 26".
- Before this candidate the passage was flat text with no headers. That was less readable, but it put no number under a wrong
  label.
- **The rule for `PassageTable.tsx`:** a row whose figure count differs from the header count is NOT drawn in the header grid.
  It renders as its own unaligned line (label, then its figures in printed order), with the note beside it. Only a row that
  matches the headers is drawn under them.
- The producer side is a RESAPP item, not this candidate's: the filing table's true columns, so that the row matches.

## Amendment 2 (judgment, AC3): the one-line description leads the page

- **The description line moves directly under the name header, above the news timeline.** It says what the company is, and
  that is the first thing a reader needs. On a 900 px screen it is below the fold today.
- **The news items and the social line may stay where they are,** above the tabs. FWD-16's "above the tabs" is met for them.
- **The provenance panel stays where it is.**

## Verdict: NOT YET

Send the amended candidate with one capture each of BA's opened passage and BA's page top. This seat reads both and approves in
the same turn. Everything else in the candidate stands as reviewed.

**Producer-side items carried to AMGT_RESAPP (not this candidate's):**
- The reason sentence starts with a capital and prints its dates in words (ba-8).
- Two source labels start in lower case ("web search results ...", "the research pack ...").
- ASML's passage has no `passage_table` (round-76 ruling 7 refuses that chart at the producer).
- The filing table's true column set, for the Deliveries row.
