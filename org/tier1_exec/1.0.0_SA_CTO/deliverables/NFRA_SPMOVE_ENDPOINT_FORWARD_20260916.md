# /endpoint --forward -- NFRA_SPMOVE (AWS -> SharePoint file movements; first instance: Schwab transactions to monthly workbooks)

**Phase 0, greenfield.** Emitted 2026-09-16 ~19:5xZ by `1.0.0_SA_CTO` on Andrew-direct "a small project" (record
`ANDREW_DIRECT_20260916_194xZ_SCHWAB_SHAREPOINT_A_SMALL_PROJECT.md`).

**Brief read:** `docs/briefs/schwab-trn-sharepoint-export-brief-20260916.md` @d5e870fed2, author `4.0.0_SA_CRO~G`, 231 lines, pure
ASCII, read whole. Part I carries six outcomes O1-O6; Part V ten preconditions; Andrew's five inputs and his card answers
(monthly, separate per master, 140 columns) verbatim in its first section.

**NOT READ, deliberately:** the register (no project existed at emission), any task order, any project JSON. Phase 0 reads the brief
and nothing else.

**The tag is `DONE WHEN` -- the BAR the outcome must reach, never a current state.** `FWD-n` ids are permanent: a new outcome takes
the next unused number; a retired one leaves its number vacant.

---

  FWD-1  Andrew opens one spreadsheet per Schwab master per month on the main Opal
         SharePoint and reads every transaction in it
         DONE WHEN  EXERCISED -- he has opened one and used it instead of asking someone
                    to pull the transactions
         ACCEPT     the month's file for a master holds every day's transactions with all
                    the columns the custodian sends; a row in it matches the same row at the
                    source field for field; he uses the file rather than asking an agent
         PROOF      one month's file opened by Andrew; one of its rows compared with its
                    source row; his word that he used it
         SOURCE     brief O1; Part III bullets 1-2; his inputs 2 and his card answers
                    (monthly, separate per master, 140 columns)

  FWD-2  Each morning, yesterday's transactions are already in the current month's file,
         without anyone running anything
         DONE WHEN  EXERCISED -- two consecutive mornings have been observed, one of them
                    after a late custodian pull
         ACCEPT     the file updates itself about fifteen minutes after the day's Schwab pull
                    completes and never on a clock alone; a late pull means a late update,
                    not a missing one; a day never appears half-written
         PROOF      two mornings' files and their run records, one following a pull that
                    completed on its second attempt of the day
         SOURCE     brief O2; his input 5; Part IV 4.2; Part V 4-5

  FWD-3  Anyone who knows where a dataset lives in AWS knows where it lives in SharePoint,
         and the reverse
         DONE WHEN  APPLIED -- the rule is written into the naming canon and the first
                    folder follows it
         ACCEPT     the SharePoint location under the AWS folder repeats the naming rule's
                    address for the dataset segment for segment, and the rule is part of the
                    naming canon so the next dataset follows it without anyone deciding a path
         PROOF      the canon's rule and the first folder's path set beside the dataset's
                    AWS address
         SOURCE     brief O3; his words "follow AWS path structure via LGIC_NAMING"; Part IV
                    4.3; Part V 1

  FWD-4  Andrew can check what each run delivered and tell a short file from a quiet day
         DONE WHEN  EXERCISED -- he has read the record on a quiet day and on a day the run
                    could not read its source
         ACCEPT     every run records which days it read and how many rows it wrote, per
                    master per month, somewhere Andrew reads; a day with no transactions
                    reads differently from a day the run failed to read
         PROOF      the run record on a quiet day; the run record on a deliberately
                    withheld source; both read by Andrew
         SOURCE     brief O4; Part III bullet 4; Part V 7

  FWD-5  Nothing reaches Menachem until Andrew says the files are clean, and then it does
         DONE WHEN  EXERCISED -- a send was refused before his word, his word was recorded,
                    and the first delivery after it arrived
         ACCEPT     while the files are being built and checked, Menachem receives nothing,
                    and an attempt to send to him is refused; after several clean days
                    Andrew says so, an operator turns delivery on, and Menachem receives the
                    file
         PROOF      one refused send before the word; the word; the first delivery after it,
                    seen by Menachem
         SOURCE     brief O5; his input 4 ("we will wait for that"); Part V 8

  FWD-6  The next file that has to go from AWS to SharePoint is a change of inputs, not a
         new build
         DONE WHEN  EXERCISED -- a second dataset or the second master has been delivered by
                    changing inputs only
         ACCEPT     dataset, masters or firm, period and columns are inputs; the trigger,
                    the path mirror, the replace-in-place delivery and the run record are
                    shared; the second instance is produced without copying or rewriting the
                    first
         PROOF      the second master's monthly file produced from the same build with only
                    inputs changed; a third configuration exercised as a dry run
         SOURCE     brief O6; his ~18:2xZ words "AWS -> Sharepoint file movements as a
                    patterned structure, with this case being the actual initial
                    implementation"

---

**Provenance.** Every outcome traces to a brief line above; O1-O6 map one to one onto FWD-1..FWD-6 (no outcome added, none dropped).
The brief's Part V preconditions -- the Gateway's large-file replace capability (V.3), the delivery tier under the canon (V.2), the
scoped read role (V.6), the backfill decision (V.9), the rollback (V.10) -- are L4 CONTRACTS and cell material, not outcomes, and
are carried to the PRD. **Waits, audited (Rule 27):** FWD-5 waits on Andrew's word by his own instruction ("we will wait for that") --
EXPRESSLY QUALIFIED, the mechanism driven deliberately (the refused send, the switch); FWD-2's "two mornings" is driven by the
custodian's daily pull, which fires every day on an enabled schedule, so it is a bounded observation, not an event nobody controls.

**Home:** the PRD's section titled `ENDPOINT (step 2, /endpoint --forward)` at `org/missions/D9/NFRA/NFRA_SPMOVE/prd/NFRA_SPMOVE_PRD.md`
-- NOT YET LANDED: the PRD is L4, cut on Andrew's DONE WHEN confirmation of these six lines.
