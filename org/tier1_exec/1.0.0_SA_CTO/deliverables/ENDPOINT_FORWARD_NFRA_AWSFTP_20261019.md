# ENDPOINT (step 2, /endpoint --forward) -- NFRA_AWSFTP: custodian daily files by SFTP, straight into AWS (`1.0.0_SA_CTO`, 2026-10-19 ~15:3xZ)

**Brief:** `docs/briefs/nfra-awsftp-custodian-sftp-direct-to-aws-brief-20261019.md` @6dfe662bc1 (`4.0.0_SA_CRO`, 255 lines, 15,739 bytes,
measured 2026-10-19 ~15:1xZ).
**Order:** Andrew-direct 2026-10-19 ~15:2xZ at the 4.0.0_SA_CRO terminal, VERBATIM: "Yes write the brief. This should go into NFRA_AWSFTP. I
would prefer to run it direct into AWS, so that is how it should be designed." The ask it answers (~15:1xZ): "What i need to know explicitly is
what needs to happen to get this FTP set up immediately."
**Design fixed by his word:** custodians deliver by SFTP to an endpoint Opal runs in AWS, landing directly in S3. Not a desktop session, not an
office box, not a vendor in the middle.

```
  FWD-1  An Opal operations person opens yesterday's positions for one Schwab
         account group of 49 Financial, and those positions came in by file
         delivery straight to Opal's endpoint in AWS, with nobody logged in to
         anything along the way
         DONE WHEN  EXERCISED -- one live trace: a file set is delivered to the
                    endpoint, kept as sent, read into positions, and the operations
                    person reads them. Driven on demand by Opal under its own test
                    login with a recorded Schwab file set, before Schwab sends
                    anything; Schwab's first real delivery is the organic case
         ACCEPT     The operations person can read that account group's positions
                    for the day, and can be shown they arrived by file delivery to
                    Opal's own endpoint with no person keeping a login open; a step
                    fed by a hand-copied file fails it
         SOURCE     brief Part I, candidate thread

  FWD-2  Operations can tell, for each connected account group, that today's
         custodian files came in without anyone keeping a login alive
         DONE WHEN  EXERCISED -- a custodian's own deliveries read on real business
                    days. QUALIFIED WAIT: only the custodian can send its real
                    files, so this needs Andrew's word that the wait is accepted
         ACCEPT     On a normal morning, operations can say the files came in for
                    each connected account group, and no one at Opal had to keep a
                    login, a token or an office computer running for that to happen
         SOURCE     brief O1, Part III first and second tests

  FWD-3  Each custodian reaches one Opal address with its own login and can touch
         only its own files
         DONE WHEN  EXERCISED -- each forbidden move is tried and seen refused
         ACCEPT     A custodian's login can deliver its own files, but cannot see or
                    open another custodian's or another firm's files and cannot
                    delete what it already sent; a partner's compliance reviewer can
                    confirm this from the setup alone
         SOURCE     brief O2, Part III third test

  FWD-4  For every account group and business day, anyone can read whether the
         expected files arrived
         DONE WHEN  EXERCISED -- the record is read on a Monday for the Friday close
         ACCEPT     On a Monday morning an operations person reads, for each account
                    group, whether Friday's files came in complete, late or not at
                    all, and it agrees with what actually arrived; it sends no
                    message to anyone, it is only there to be read
         SOURCE     brief O3, Part II (no alerts), Part III first test

  FWD-5  Every file is kept exactly as the custodian sent it
         DONE WHEN  EXERCISED -- a past day's file is fetched and checked
         ACCEPT     Someone can fetch the exact file a custodian delivered on an
                    earlier day, see when it came and which login sent it, and show
                    it has not been changed since
         SOURCE     brief O4

  FWD-6  One set of holdings, cash and activity answers the same way whichever
         custodian holds the account
         DONE WHEN  EXERCISED -- one Schwab and one Fidelity account read side by
                    side. QUALIFIED WAIT on the Fidelity half: it needs Fidelity's
                    file layouts and authorization, which only the firm of record
                    can obtain; needs Andrew's word that the wait is accepted
         ACCEPT     An analyst asks what an account held, its cash and what moved,
                    and gets the same columns for a Schwab account and a Fidelity
                    account, each saying which custodian and account group it came
                    from, without having to know what each custodian calls things
         SOURCE     brief O5, Part III fourth test

  FWD-7  An account that appears under several account groups counts once
         DONE WHEN  EXERCISED -- the firm total read beside a hand count
         ACCEPT     49 Financial's total counts each account once and matches the
                    count an operations person would make by hand, instead of adding
                    up accounts that sit under two or three account groups
         SOURCE     brief O6, Part VI ($3.67B summed against $1.84B distinct), Part III fifth test

  FWD-8  When one custodian account group holds accounts of several firms, each
         firm's accounts are kept and read only in that firm's own place
         DONE WHEN  EXERCISED -- driven on demand with a recorded file set that mixes
                    firms; a reader for one firm tries to see another firm's
                    accounts and is refused
         ACCEPT     From an account group that mixes firms, each firm's accounts land
                    only where that firm's data lives, and someone working for one
                    firm cannot see another firm's accounts
         SOURCE     brief O7, Part V (multi-firm master)

  FWD-9  Connecting a new account group or a new custodian is a setup entry and a
         login, not a new build
         DONE WHEN  EXERCISED -- the second account group is connected that way
         ACCEPT     When a second account group (or a third custodian) is connected,
                    its files flow through the same delivery, record and holdings
                    with only its entry added and its login issued, and nothing new
                    is built for it
         SOURCE     brief O8

  FWD-10 The desktop-session pull stops for each Schwab account group in one move,
         with a same-day way back
         DONE WHEN  EXERCISED -- one account group switched, and its way back shown
                    to work. QUALIFIED WAIT: the switch needs Schwab delivering that
                    account group's files to the endpoint; needs Andrew's word that
                    the wait is accepted
         ACCEPT     On the day an account group switches, its files arrive the new
                    way and the old pull stops for it; if the switch fails, it is put
                    back the same day; at no point do the two run side by side to be
                    compared
         SOURCE     brief O9, Part II (no shadow pipeline, no standing comparison)
```

## CONFIRMED by Andrew 2026-10-19 ~16:5xZ -- and the project is ON HOLD

"Yes all recs approved for this" -- FWD-1..10 confirmed as written, the three qualified waits below accepted. Same word: "we cannot start
this project until we actually have an FTP solution ... listed as 'hold' in status in the registry". Record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261019_165xZ_NFRA_AWSFTP_RECS_APPROVED_D8_REGISTERED_ON_HOLD.md`.

## Reachability (L2 "NO FWD IS A WAIT")

- **Reachable by working, on demand:** FWD-1, FWD-3, FWD-4, FWD-5, FWD-7, FWD-8, FWD-9 (7 of 10). Each is driven by Opal's own test login
  and recorded file sets; the custodian's real delivery is the organic case.
- **Qualified waits, each on an act no seat can perform (3 of 10):** FWD-2 and FWD-10 (Schwab, and Fidelity for FWD-2, sending real files),
  FWD-6's Fidelity half (Fidelity's layouts and authorization). The paperwork is the firm of record's, driven by Andrew and Menachem (brief
  Part II, Part V). Each needs Andrew's word that the wait is accepted.
- **Open before the PRD (brief Part V, not ruled here):** whether Schwab offers SFTP delivery at all; push or pull, fixed IP, PGP; what the
  $15k Fidelity figure is; the multi-firm master's landing home; SSN masking and who may read raw files.

## Provenance

- GROUNDED ON: the brief above, read in full; its Part IV measurements are the CRO's (2026-10-19), not re-run here.
- NOT READ: the task-order register, any project JSON, any PRD (none exists), the CRO's research file (cited by the brief, not needed to
  cut outcomes).
- NOT YET LANDED IN A PRD: this block belongs under the section `ENDPOINT (step 2, /endpoint --forward)` of
  `org/missions/D8/NFRA/NFRA_AWSFTP/prd/NFRA_AWSFTP_PRD.md` at L4, after Andrew confirms the DONE WHEN lines.

-- 1.0.0_SA_CTO (laptop)
