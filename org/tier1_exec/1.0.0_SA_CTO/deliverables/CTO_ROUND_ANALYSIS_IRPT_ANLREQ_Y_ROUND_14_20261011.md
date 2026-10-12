# CTO ROUND-14 ANALYSIS -- IRPT_ANLREQ workstream Y -- answering the round-13 L10 slug (2026-10-11 ~21:1xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/remediations/REMEDIATION_v7.md`
@51d95a8860 (3.0.0_SA_CVO msg 5844). **Read by this seat:** the slug and the issuer's L8 compile @6d2fa01d99, sections 1 and 2.
NOT read: the worker's record, the template reader, any fixture. **Prior:** the round-13 analysis @7542d8555c. **No PRD addendum.**

## 1. What round 13 found, said plainly

The upload door the form reaches is the template reader, not the file this seat and two issuers named. **Today that door
accepts a sheet holding two accounts and merges their rows, and accepts a sheet ending in a "Total" row and counts the total
as a holding.** Both were run in process on synthetic sheets with a stub provider; neither was run against the live service.
This is not a missing convenience. It is a served door that can turn a client's file into a wrong input for a report without
saying so. NOT established: whether any upload accepted to date was merged or carried a total.

Row D2-W52-S9 is this seat's error as much as anyone's: ruling msg 5737 named `intake/parse.py` from a worker's inferred read.

## 2. The five questions, RULED

1. **What counts as several accounts.** Two signals, both turned back with words: a column whose header is on a closed list of
   account words holding two or more distinct non-empty values; and a repeated header row. The three signals the read rejected
   stay rejected (the same ticker on several rows is tax lots). **What the door cannot see is said, not hidden:** stacked
   tables with no account column and no repeated header read as one account, and FWD-3's record says so.
2. **A totals row is TURNED BACK, never dropped.** Dropping a row is this service editing a client's file on a guess. A row
   whose label is on a closed list of total words is refused with its row number and what to do. A total with no label
   cannot be seen and is said so. One read first: what the LIVE provider answers for the symbol the label would be taken for.
3. **The words-only edit to `ops/status.py`:** whoever `.tools/owned-paths-validate.py` names for that file makes it. If that
   is not this lane, its issuer is passed the words; no override.
4. **Two presses are NOT acceptable for a finding the door can decide at the POST.** The account and totals findings need no
   pricing, so the door's first answer carries them. Pricing is decided later in the resident: for that alone the form
   re-posts, a bounded number of times with a stated wait, and then shows the findings or says plainly that it is still
   working. Row D2-W52-S11 closes on that.
5. **A second holdings sheet is NOT an error** (the reviewer's question). The repository's own one-account example has
   several sheets. But a sheet the reader did not read is not passed over in silence either: the accepted answer carries one
   line saying that only the first sheet was read and how many others were not. The worker opens that fixture first and says
   what its other sheets hold.

Each closed list (account words, total words) arrives with its Rule 24 record: domain, the uncovered member hunted by
subtraction over the headers and labels of every fixture in the repository, denominator printed.

## 3. ENRICHMENT LIST for round 14 (ONE issuance)

1. The two reads of section 2 (the live provider's answer for a total label, by a seat that can ask it with no new grant;
   the multi-sheet fixture).
2. The census in the template reader and its findings, with tests on synthetic sheets for all four kinds and the multi-sheet
   line. Built, not released.
3. Words for every finding code the form can show; a raw code is shown only inside a closed Details.
4. The form's bounded re-post.
5. The release, under its own pair: every consumer of the door's answer named with one read through each, and BOTH branches
   of a sheet that was accepted yesterday and is turned back today.
6. Counts only, in the next served-read window and not as a single read: of the uploads accepted to date, how many had a
   third column with two or more distinct values, or a row labelled as a total. No file content leaves the window.
7. Every order and record that names `parse.py` as the form's door is corrected (row D2-W52-S9).

## 4. Held, not cut

Release 5's return and the fallback's removal, after the PROD push of portal fc876722.

## 5. Acts only Andrew can do

- The PROD push of portal fc876722 (CLAUDE.md, Agent Autonomy: unsure is client-facing).

## 6. What this analysis did not measure

Nothing was run by this seat. The door's behaviour is one worker's in-process run on four synthetic sheets.

-- 1.0.0_SA_CTO~DELL2
