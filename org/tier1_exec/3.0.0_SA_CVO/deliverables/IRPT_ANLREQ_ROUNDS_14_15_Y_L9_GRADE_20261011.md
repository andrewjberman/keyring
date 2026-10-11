# IRPT_ANLREQ rounds 14 and 15, workstream Y -- L9 grade of AR142-y-AC3J, AR144-y-AC2J and AR145-y-AC2J

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T23:37:38Z. Row IRPT_ANLREQ-D2-S64.
**Input:** `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND14_Y_L8_COMPILE_20261011.md @73dd169157 (msg 6114)`. The build these criteria grade was REVERTED off the trunk; nothing of the upload check is released.

| criterion | verdict |
|---|---|
| AR142-y-AC3J, the two closed lists and each finding's words | **NOT MET as written: one list is incomplete and one finding's words misdirect.** Both are small and are fixed before the re-land |
| AR144-y-AC2J, a bad sheet is explained without a second press or a code | **MET for the form's half; the words half depends on the reverted service** |
| AR145-y-AC2J, no consumer of the door's answer is missing | **MET, and it is the cell that found the build unsafe** |

## AR142-y-AC3J

Read in the build commit, lines 28 to 52 of the reader, and in its closed-lists record.

**The totals list is right for what it is:** five whole-cell labels, never a substring, and `Subtotal` left out on the CTO's
ruling with a test that pins it.

**The account list is incomplete.** It holds `account`, `acct`, `account number`, `account no`, `account id`, `acct #`,
`custodian account`, matched as a whole cell. It holds `acct #` and not `account #`. It holds `account number` and not
`acct number`. A sheet whose third column is headed `Account #` with two accounts in it is accepted and merged, which is the
defect the cell exists to stop.

The record's subtraction did not find this, and could not: its denominator is the first-row cells of 13 fixture files, and none
of those files has an account column at all. A subtraction over a population that holds no member of the class proves nothing
about the class. The record says the lists were not checked against a real uploaded file. The list should be built from the
header forms custodians and advisors actually use, or the match loosened to the leading word with the named exclusions kept.

**Three of the four findings' words tell a person what to do. One misdirects.** The repeated-header finding says the row "usually
means a second account was pasted below the first" and tells the person to remove the rows under it and upload them as their own
file. A header pasted twice into ONE account's sheet produces the same row; how often each happens is not known. A person who follows the words splits one account
into two files and gets two reports. Round 13's own record warned of exactly this and said to word it as a repeated header, not as
several accounts. The words should say what is seen and ask: a header row appears again at row N; if the rows below belong to
another account upload them separately, otherwise delete the repeated header.

A worker's row adds a smaller one: the form already prefixes "Row N:" to a sentence that begins "Row N" (row D2-W53-S8).

## AR144-y-AC2J

Read on portal DEV. The form posts the same upload again by itself while the service answers that it is still checking, a fixed
number of times three seconds apart, and says so while it waits. A finding with no words shows one plain line with the code
folded away. So a person does not press twice and does not read a code. That half is met.

Two limits. If the check takes longer than the form waits, the person is told it is still being checked and must press again;
how long the check really takes was not measured. And "learns what to fix" is the service's words: the 24 codes that gained words
in this round lost them in the revert, so for those the person gets the plain line and nothing to act on. Not looked at as a page.

## AR145-y-AC2J

The census asked what else reads the door's answer, and found the consumer nobody had asked about: a stored original is re-read
with the deployed reader and refused unless the result EQUALS the template stored when it was accepted. This seat printed that
line at HEAD (`uploads.py` 516 to 539; the census cites it at the build commit's numbering). A reader that adds a finding
to a sheet accepted yesterday makes that sheet unreadable today. The build was reverted on it before any release.

Not re-derived: the count of 21 consumers and 235 map entries.

**What the round shows about order.** The issuer says it plainly: the cell that asks what re-reads a stored input was the last
cell, after the merges. The census did its job; it was cut too late. Nothing was released, so the cost was one revert.
