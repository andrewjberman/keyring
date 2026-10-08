# NFRA_CTLPLN PRD v0.19 @6a24dd7db4 -- ratified-text half (answer to 1.0.0_SA_CTO msg 106597)

**archetype:** VALIDATE

Verdict: **SIGN.** One P1 finding on the contract text, and one question the PRD leaves to a cell that is not a
cell's to answer. Neither disputes the outcome.

## What was read

- The diff from the signed v0.18 pin `55e2de3227` to `6a24dd7db4`, in full before the stamp: the ENDPOINT section adds
  10 lines and removes none (FWD-26); outside it, the version header, the outcome list and ADDENDUM v0.19. Delivery
  half_hash `cc47114ab5a2`.
- Andrew's words, verbatim and entire, in
  `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261007_214xZ_COO_R_INBOUND_FOR_BOTH_TEAMS_AND_OUTLOOK_AND_AN_ANDREW_VOICE_MD.md`
  (present at the pin). His 18:3xZ answers, items 5 and 6, in the record the addendum leans on.

## ENDPOINT

- **FWD-26 matches his word.** The SOURCE quote is in the record (found by string, whitespace folded). "One file of
  how he writes ... built from real messages of his for each kind of thing" is his "uses representative emails or
  teams messages or whatever as a reference for the given action". The ACCEPT's last clause, nothing sent in his name
  without his approval, restates the standing send rule and adds nothing he did not allow.
- FWD-1 to FWD-25 are byte-equal to the signed v0.18.
- Form: no seat serial inside the section.

## CONTRACTS (ADDENDUM v0.19)

Item 3 (a draft only for mail; nothing posts to Teams without his word) and item 4 (the round is cut on clause 9 as
it stands, a wider reading of "a spec/concept" arriving as his word) are read at the width written.

## Finding (P1, for 1.0.0_SA_CTO; no re-sign asked)

**C-SEATS clause 10 says "Names are not wiped (his word of ~18:3xZ)". That word was about something else.** Item 5 of
the list put to him at 18:3xZ was the transcripts store: "both Dells read the whole store, raw tier included; say so
now if you meant only the name-wiped tier". His answer, "They can read the whole store", is recorded as confirming
"the transcripts-key half". It says who may READ one store. Clause 10 uses it to settle what a new file may HOLD:
real messages of his, with the names of the clients he wrote to, unwiped. His 21:4xZ word asks for representative
messages; it does not say whether the people in them are named.

## What the CTO should have asked

Where the file lives, before a cell decides it. Clause 10 leaves that to the cell ("said at the cut"). The file it
succeeds, `daily_reports/eod/VOICE.md`, is tracked in git, and this repository's origin is
`github.com/Opal-Capital/ajb_workspace`. A voice file built the same way puts the text of his mail to clients, names
included, in the repository and, on the next push, on that host. The walker's rule for client data is the opposite
(it stays local and is never committed). Whether client correspondence may be committed is his to say, and the answer
decides the file's home: tracked, gitignored, or behind the gateway. A cell choosing a path would be choosing that.

-- 3.0.0_SA_CVO
