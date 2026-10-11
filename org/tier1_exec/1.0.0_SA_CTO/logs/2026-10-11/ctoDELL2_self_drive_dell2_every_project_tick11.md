# /self-drive -- every dell2 project -- tick 11 (2026-10-11 ~11:52Z) -- 1.0.0_SA_CTO~DELL2

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261011_021xZ_SELF_DRIVE_60M_EVERY_DELL2_PROJECT_REARM_AFTER_HOLD_LIFT.md`
@86d65d0c3e. **Cadence:** 60m, job `511f4ba7`. **/keep-driving:** OFF. **Ticks covered:** 11 (10:52Z to 11:52Z).
**state: ARMED**

## THE HOUR'S MAIN FACT: a second release this seat signed broke a live page, and was rolled back

- IRPT_ANLREQ release 5 (irpt-status build `Iw3FADFr`) went live at 10:25:40Z under both halves; this seat's @2c3d9e91af.
- Its history answer gained `unreadable_rows` on the page and `client_id`, `client_claim` on every row. The portal's reader on
  PROD (`contracts/owned-requests.ts` `readOwnedHistory`, read by this seat on `origin/PROD`) admits EXACTLY two page keys,
  and the row reader an exact set too (2.0.0_SA_COO~Y2's read). So every Investor Reporting history read threw from
  10:25:40Z. Found by 2.0.0_SA_COO~D2 at 11:17Z while probing fixtures; the page itself was not observed by any seat.
- Rollback ruled 11:18Z (msg 4805; record appended to the half @b54f838d09). **Read by this seat at 11:27:42Z: `6idtFvAm`,
  LastModified 11:26:53Z. 61 minutes.** Confirmed by the laptop applier's read of the answer: page keys `[items,
  next_cursor]`, row keys `[accepted_at, identity]`, 40 rows (relay msg 4830); 49financial owners not replayable.
- The miss, this seat's: every after-read in the pair asked whether the SERVICE now said the new thing; none read a CONSUMER.
- Forward: the portal's reader that takes both answers is on DEV `8ed372cb` (approved after this seat read it against the
  contract's own lines). PROD reads `37aa1247ee`. The release returns only after that reader is on PROD.
- A hazard the rollback left, closed: the restored map built the breaking build; the two members are pinned and the map now
  builds `6idtFvAm` (row IRPT_ANLREQ-D2-S46, the issuer's run).

## Measurements (this seat's own reads at 11:51Z)

- **Inbox:** `check_inbox` reads empty. 34 messages read and acked since tick 10's log.
- **Sequence:** whole-file read, 0 DRIFT, UNREADABLE or OUT-OF-SEQUENCE lines.
- **Live:** `irpt-status` `6idtFvAm` (11:26:53Z); `irpt-performance-adapter` `9kYLdR64` (10:03:25Z).
- **Portal:** `ls-remote` DEV `8ed372cb72`, PROD `37aa1247ee`.
- **Push state:** tick 10's log 1a45728a4f, the rollback record b54f838d09 and the round-11 analysis 457305b604 are ancestors
  of origin box/dell2.
- **Statuses:** 11 of 11 project files read: 1 complete.

## Calls closed since tick 10 (all ruled by this seat)

| project | call | ruling | carrier |
|---|---|---|---|
| IRPT_ANLREQ | release 5's after-reads, then its breakage | five reads true, R4 ABSENT; then ROLLED BACK | @b54f838d09 |
| IRPT_ANLREQ | the restored map builds the breaking build (msg 4835) | pin the two members; test is the digest | row D2-S46 |
| IRPT_ANLREQ | who lands the portal's wire folder (msg 4795) | DSGN_IRPTV1; a generated folder holds generator output only | msg 4797 |
| DSGN_IRPTV1 | five fixtures the portal refuses (msgs 4789, 4799, 4803) | map at 16 with six named excuses; the contract arbitrates; wrapped re-run found the live defect | msgs 4790, 4800 |
| DSGN_IRPTV1 | the history reader (msgs 4817, 4845) | takes both answers now, contract-exact in a later named cell; approved for DEV | portal DEV 8ed372cb |
| IRPT_YCDGEN | round-10 and backlog slug | round-11 analysis: the journey read hop by hop against 22 un-re-read rows | @457305b604 |
| IRPT_YCDGEN | a window for one read (msg 4768) | held for the next batch | msg 10:56Z |
| IRPT_YCDGEN + TCKT_VNEXT | the dead-letter inventory (msg 4779) | condition 2 met; the ticket_id guess withdrawn | msg 4780 |
| IRPT_BCKEND | S252 measured whole and by account (msgs 4782, 4824, 4832) | a per-account-day basis ruled, then HELD: NOT_GRADED folds two cases; IB-pr-429 measures | msgs 11:31Z, 11:35Z |
| ADVI_COTBKF | the default moved ahead of the addendum (msg 4770) | back to r28 before the drain | msg 10:57Z |
| ADVI_COTBKF | the served table cannot be reproduced (msg 4843) | the split store is pinned first; a re-mint names every cause | msg 11:43Z |

**Corrections to this seat's own statements this hour:** the release-5 half (no consumer read); the per-account-day rule as
first written (386 of 1,000 accounts never served); "22, two excused" for the smoke map; the ticket_id guess for run 3.

## The pattern in today's two rollbacks, stated once

Both halves were signed on what the changed service does. Neither read what the change is FOR (the first: the project's
ENDPOINT) or who READS it (the second: the portal's reader). From here a pair this seat signs names, for each served change,
the ENDPOINT line it serves and each consumer with one read through it.

## Scope state

1 of 11 complete (IRPT_CUSTDY). REACHABLE 8, UNREACHABLE 2 (ADVI_BILLING, NFRA_OPSWKF). **COMPLETION TEST: NOT DONE.**

## Owed by this seat

- The price-date basis ruling, on IB-pr-429's table.
- The ADVI_COTBKF addendum for method_r29, on a comparison run at a pinned split store; the outlier-days ruling.
- Review of the Holdings-face candidate and the wire-folder regeneration when they arrive.

## Acts only Andrew can do (each with its citation)

- The portal PROD push of the history reader `8ed372cb` and the other Investor Reporting changes on DEV (CLAUDE.md, Agent
  Autonomy: a client-facing page waits on his word). Release 5's return hangs on it.
- His word on `svc-irpt-analysis` and the Opal producer's allow list (IRPT_YCDGEN_PRD.md:248).
- Any word that a vendor figure may be Cottonwood's served Performance answer (IRPT_BCKEND ENDPOINT, 2026-09-28).
- Carried: the organizer's Recordings folder, the SharePoint link, the Ticket Center list, the default fee, the
  Opal_Terminal key's machine, the crawl, the FWD-1 sitting for IRPT_YCDGEN (not asked).

## Compiler Tools

`check_inbox`, `sequence-check.py`, `lambda get-function-configuration` (two functions), `git ls-remote` (portal DEV and
PROD), `git show origin/PROD:<reader>`, `git fetch` + `merge-base --is-ancestor`, `git diff` on two portal candidates,
`safe-commit.sh`.
