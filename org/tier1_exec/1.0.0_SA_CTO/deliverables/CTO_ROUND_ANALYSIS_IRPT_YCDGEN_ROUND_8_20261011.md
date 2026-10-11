# CTO ROUND-8 ANALYSIS -- IRPT_YCDGEN -- answering the round-7 L10 slug (2026-10-11 ~07:0xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/remediations/REMEDIATION_v6.md`
@0e5dbdaa91 (3.0.0_SA_CVO msg 4306), on `deliverables/2.0.0_SA_COO~G2/r7/ROUND7_DRAIN_END_READ_20261011.md` @6505291224.
**PRD:** `org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md`. **No PRD addendum.**

## 1. Where the project stands

**FWD-1 is NOT MET, and it has never been run as written.** The run of record was a service account reading an existing
49financial request on irpt-status revision 6: 6 of 6 calls answered HTTP 200, and 251 of the report's 257 sections read
NOT_AVAILABLE. That establishes the served read path. It is not Andrew submitting a Cottonwood portfolio and opening the
Overview. Round 8 is therefore still a thread round: nothing is enrichment until one journey runs.

This seat's msg 4152 called the status answer for that request "designed"; the opt-in read 2.0.0_SA_COO~G2 then made showed a
real break (row D2-S38). That is recorded here so the first statement is not cited later.

## 2. Rulings on the rows

| row | ruling |
|---|---|
| **D2-S39** (BLOCKING, INERT; owner this seat) | Two parts. **(a) The sitting is Andrew's act** and is asked of him only after section 3's four items read clean; his 2026-10-07 sitting was spent on a build that stopped at generation, and that is not repeated. **(b) Is 6 of 257 valued sections an acceptable first Overview? NOT RULED on that number, because nobody knows what the 251 are.** FWD-1's ACCEPT admits a figure Opal cannot work out when the page says so with the reason. So the question is which reasons, on how many sections, on which pages. Section 3 item 3 is that census. This seat rules on its result: a section unavailable because Opal does not keep the data is the outcome working; a section unavailable because a step is unbuilt or refused is a break to fix before the sitting. |
| **D2-S38** (BLOCKING, ARMED) | As ruled in msg 4188: the Opal producer writes undated rows under `undated_sections` with `date_claim` NONE; the reader (`ops/prospect_dates.py:30-42`) is not loosened. It disarms on the reviewer's read of the portal's own status call answering for a READY Opal report generated AFTER the fix. Retained reports are immutable; the log census found 1 refusal in 14 days, a test read, so no reader cell is owed. |
| **S16** (OBSERVATION, ARMED) | Re-measured before any sitting, section 3 item 2. The generation step is exercised tonight by another project's run under its own pair (TCKT_VNEXT R2-tr-1 submits one analysis for `49financial`); 2.0.0_SA_COO~G2 reads that run's trace for the generation hop and does not order a second vendor-facing run for this row alone. |
| **W6-S1, W6-S2, D2-W6-S3, D2-W7-S1** (BLOCKING, ARMED) and **D2-W6-S1, D2-W6-S2** (INERT) | One re-measure cell at the tree as it stands, section 3 item 4. Each row closes on what the tree does today or is re-cut; a row armed against code that later cells rewrote is neither true nor false until it is read again. |
| **D2-S3** (BLOCKING, INERT) | One listing of the resident host's brand spec and logo, in the same cell. |
| **D2-W8-S1** (BLOCKING, INERT): the accepted request record carries no server-recorded actor | **New accepted requests carry their actor,** taken from the verified token and never from the body. For records already accepted, the upload row is the source where one exists, and a selection-based request with no upload row reads ABSENT, stated. The acceptance writer is IRPT_ANLREQ workstream Y's file, so the cell and its pair are 2.0.0_SA_COO~Y2's; 2.0.0_SA_COO~G2 sends it the row id. The owner-read cell here uses the upload row meanwhile. |

## 3. ENRICHMENT LIST for round 8 (ONE issuance, in this order; every item is thread work)

1. **The producer conforms** (D2-S38): undated rows under `undated_sections`, with a test that feeds the producer's output
   to `section_dates()`. Then ONE fresh Opal report is generated and the portal's own status call is read on the live
   function.
2. **The generation step, re-measured** (S16), from the trace named above; what changed since 2026-10-07 stated.
3. **The section census.** For the retained report of the run of record: the 257 sections, counted by availability and, for
   the unavailable, by the reason the page would state, grouped by report page. Read-only, through the served read. It
   comes to this seat, which then rules D2-S39 (b).
4. **The re-measure cell** for the six generator, test and builder rows, plus the host's brand listing (D2-S3).
5. **The sitting,** when 1 to 4 read clean: Andrew, signed in as himself, one real Cottonwood portfolio, an Opal-branded
   Overview opened in the same sitting. The issuer prepares what he needs to know beforehand in three lines and no more.

Items 1, 3 and 4 are independent and start now. Each build order carries at most three mechanical criteria.

## 4. One cross-project note (FWD-20 and tonight's DSGN_IRPTV1 ruling)

FWD-20 of this PRD reads "Someone reading the report can tell a corrected typo from a stand-in". Tonight this seat approved an
upload-review wording for DSGN_IRPTV1 (portal 1cd1cf25) that is deliberately the SAME for both, because the served correction
carries nothing that tells them apart. The two do not conflict today: one wording that is true for both is the honest cell
while the kind is not served. **When FWD-20's cell serves the kind, the upload review's cell and its disclosure line follow
it;** that supersedes this seat's line to 2.0.0_SA_COO~D2 that the single wording stays "anyway".

## 5. Acts only Andrew can do

- **The FWD-1 sitting** (section 3 item 5). Citation: PRD FWD-1 ACCEPT, "Andrew, signed in as himself". Not asked yet.

## 6. What this analysis did not measure

It rests on the slug, the reviewer's grade and the issuer's drain-end read as filed. This seat read `ops/owned_status.py` and
`ops/prospect_dates.py` tonight. It read none of the generator, the builder or the report's sections. About 45 INERT rows of
rounds 6 and 7 are not compiled yet, by the reviewer's own statement; this analysis rules only the 11 it was sent.

-- 1.0.0_SA_CTO~DELL2
