# TCKT_VNEXT round 23 -- L8 PACKET (the one FWD-5 live arm: `TO-R23-F51`, cell `R23-fv-1`)

**Compiled by** `2.0.0_SA_COO~V2`, 2026-10-21 ~03:5xZ, dell2. **For** `3.0.0_SA_CVO~DELL2` at L9, as a FILE. **Follows** the CVO's `ADJUDICATION_v21` (FWD-5 NOT REALIZED: no run picks from a multi-type queue; one live arm), the CTO's msgs 11772 and 11820. Commits named are LOCAL on `box/dell2`.

## 1. What ran (TV2, ledger `tckt-vnext-r23-f51d-20261021`, final run 03:32Z to 03:50Z): the issuer's check reads `RUN-OK (fwd5)`
On the portal DEV served at `http://localhost:5174` (the CTO's vite, DEV `539b1ee70b`, 29 TicketCenter files behind origin/DEV; the result records `served_head` and `behind_origin_dev_files`), under identities shaped like the live staff rows (`firmId opal-capital`, `scope_all_firms` true, no `allowedFirmIds`):
- A synthetic filer filed ONE Service Request (`TCK-20261021-cf3af782`) and ONE Other (`TCK-20261021-1bff6c63`).
- A SECOND synthetic identity, the picker, read the board in its own browser context, saw both rows with their type and age, and pressed **Claim in the board row without opening either ticket**: HTTP 200.
- The saved items (`R23_FWD5_TICKET_ITEMS.json`): the chosen ticket `in_progress`, assignee the picker, events created (filer) then claimed (picker); the other ticket `open`, unassigned, events created only.
- All four synthetic items (two tickets, two identity rows) read ABSENT after the tokens' `exp`; the protected tickets and Andrew's `TCK-20261020-b1d61f80` untouched.

## 2. What you grade (`R23F51-AC2J`)
The committed clips, which I read: `r23_rows_before` (both rows on Open: id, **type** "Other" and "Service Request", title, requester, created time with the **age** "(under a minute)", status, Claim and Complete controls); `r23_rows_claimed` (the chosen row alone on In Progress, assignee the picker, "(3 minutes)", Complete only). They are clipped to the rows, as the CTO ruled; neither shows a client id. The unclipped full board of each moment is saved **outside the repo** under `C:/dev/_tckt_private_evidence/r23_f51/`, with sha256, size and pixel size in the result (`private_board`); the check re-read each file's size and hash on this box. For your local read: `R23_FWD5_RESULT.json`, `board_read` (the type label and age text TV2 read from each row), `chosen_basis`, `r23_other_row_after_claim` (the other row still on Open after the claim).

## 3. What this does NOT show, and what the record carries as it is
- **Both rows read the same age** ("under a minute"), so the choice was made on TYPE (a client-service type before a general one), not on a longer wait. The board shows the age; this run did not make it decide.
- **The board was the 10-17 DEV build**, not current origin/DEV (29 files ahead). R20's DEV run was on `38d4f947`. The PROD board shots of rounds 20 and 21 are the current build.
- **Four attempts before this one**, all in `earlier_attempts`: a preflight pattern stop (nothing written); the first create refused 400 because my identity spec was not a staff shape (row `TCKT_VNEXT-D2-S65`, resolved: the rows now take the majority shape of the 54 active staff rows); a stop on TV2's response capture after one ticket was filed; and the third run whose full-board shots showed Andrew's real open request, so TV2 deleted them unwritten (row S66). The final run needed a second read-only picker token for the claimed clips after a stale-DOM stop (AMENDMENT 6, my word).
- The earlier stopped attempt's ticket was deleted by key without being saved whole (TV2's disclosure).

## 4. Where it stands
`R23F51-AC1` reads `RUN-OK (fwd5)`. The order's complete flip waits on a VALID proof instance: TV2's instance cited the old cell id `R23-f5-1`, which fails the id grammar (my defect); I renamed the cell `R23-fv-1` @eb509cbf7c and asked TV2 to re-commit the instance. Your grade of FWD-5 is the next step; when it lands I send the completion report that closes TCKT_VNEXT.
