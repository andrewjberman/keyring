# Drive log -- 2.0.0_SA_COO~Z -- 2026-10-07 10Z-12Z hours (site Z)

## tick 2026-10-07T10:30Z-10:40Z
AMGT_RESAPP | limb L7 (issuer acts) | stage EXECUTING, round 77 | lease FULL | ba-21/22 wait on the 11:00Z vehicle (task Ready, last run still 10-06 result 267014); re-mint waits on CORPUS's 13:00Z fire; ba-23 after it | thread: FWD-1 on AMD not re-read | outcome: DRIVE FORWARD (a read the CTO asked for)
- CTO msg 30798: MSFT US serves 0 of 7 header figures on PROD, one name or a class? READ DONE: 0 of 95 covered names blockless on the deployed function (control AMD 0); MSFT is not a covered name (ETF-universe pool record, no stored company record), served as av-1 built it. Row AMGT_RESAPP-Z-S364 @bb38ea2d43, OBSERVATION. Check file r77_blockless_census.py.
- plan name lists committed before any pull: segments 85, officers 86 (PLAN_*_20261007.txt), same commit
- SECHIST: working-tree blob still c9de003ed6 (merge not landed); now inside the 10:30Z-12:00Z exclusion

## tick 2026-10-07T11:00Z
AMGT_RESAPP | limb L7 (issuer acts) | stage EXECUTING, round 77 | lease FULL | outcome: NO-OP (the vehicle is RUNNING: started 07:00:01 local, result 267009; ba-21's C1 waits for it to COMPLETE and for the 07:30 ET check to pass by)
- inbox empty; CTO correction msg 30812 acked (MSFT: nothing routed to RESAPP)
- 11:19Z relay msg 30833 (dell1 2.0.0_SA_COO~H1 via MSTR~Z): today's scheduled ETF leg landed 11:08:14Z on the OLD script; after site Z takes etf_daily_pull.py (Andrew's word, 12:00Z earliest) the ledger owner runs ONE ad-hoc QA run of the leg (dell1 CTO ruling 167). Replied with the ledger entry path; asked for ruling 167's path. Owed before the run: read ruling 167 and how the leg treats an ad-hoc run class and its keys.
- 11:2xZ ruling 167 read (@4b1da8e663). Pre-run read of the signed leg: a hand-run overwrites 7 objects under bbg/2026-10-06/ on an UNVERSIONED bucket and relabels the manifest scheduled -> adhoc. Own conditions recorded in MDPF_SECHIST_SITEZ_DEPLOY_ACT_RECORD_20261007.md: local byte copy first, comparisons after, one run, outside 10:30Z-12:00Z.

## tick 2026-10-07T11:30Z-11:46Z
AMGT_RESAPP | limb L7 (issuer acts) | stage EXECUTING, round 77 | lease FULL | outcome: DRIVE FORWARD (two issuer acts fired)
- C1 read 11:30Z: vehicle LastTaskResult 0, every leg landed (log last write 07:09 local), the 07:30 ET check finished result 0
- ba-21: ONE call on AMD at 11:32:01Z. BRANCH B: NAME answered; SEGMENT_NAME, SEGMENT_REVENUE, GEOGRAPHIC_SEGMENT_NAME each BAD_FLD/INVALID_FIELD. Landed as received (458 B). The 85-name pull did NOT run. First invocation under Python 3.14 (no blpapi) read TERMINAL_DOWN with 0 calls: row Z-S366.
- ba-22: slice of five, all five read through the deployed /thesis route (15, 11, 20, 26, 27 officers, BLOOMBERG_FALLBACK), then 81 more. 86 calls, 0 failed. After: A 84, landed-not-read 2 (BP/ LN, NG/ LN: raw-slash reader prefix, row Z-S365). Plan 86 -> 2.
- commits: acts + rows @bf4fd45456; TO-GUARD-3 flipped complete @7f22fe3cf6 (first live read validated by own read of the vehicle log line and both task results)
- two decisions asked of 1.0.0_SA_CTO~Z: who finds the segment mnemonics (REC the CRO); the slash-reader repair now or round 78
- still waiting: pool re-mint (CORPUS 13:00Z fire), ba-23 after it; SECHIST merge (blob still c9de003ed6); TO-GUARD-4 merge (Andrew)
- 11:45Z CTO ruling msg 30847/30856: the CRO names candidates, then ONE more AMD probe; the slash-reader repair is a round-78 cell
- 11:48Z second probe: BRANCH A. PG_REVENUE and PG_OPERATING_INCOME served as bulk rows (6 each on AMD); 4 names INVALID_FIELD. Fields edit @588a7fc70e (test updated, 20 pass).
- 11:50Z-11:52Z segments pull: 85 of 85 landed, 0 failed. Read after: 76 with revenue rows, 9 with none and no error (seven banks, two Mexican names); op income rows on 50. 87 calls under the pair. Nothing served moved (reader uncut). ADDENDUM 1 to the ba-21 act record.
- 11:56Z CTO ruling msg 30870 (DSGN_AMGTV1 FWD-27): two items go to the NEXT RESAPP list: the served country in plain case ("Country: UNITED STATES" is a vendor value in capitals), and the Filings input-ledger row ("has not run yet" beside 10-K citations)
- CARRY TO THE ROUND-78 RECUT (so far): the slash-safe officers reader (row Z-S365); the segments bronze reader (slash partitions, near-zero missing periods, unnamed periods); Peers V not-available reason (row Z-S162); the country case; the Filings ledger row; the research_pulls interpreter trap (row Z-S366)

## tick 2026-10-07T12:00Z-12:15Z
AMGT_RESAPP | limb L7 -> L8 prep | stage EXECUTING, round 77 | lease FULL | TOs 23/23 terminal (order files, last status); issuer acts ba-21 and ba-22 done, ba-23 open behind the re-mint | thread: FWD-1 on AMD still unread by the page (no segments reader) | outcome: DRIVE FORWARD (the compile)
- ONE REAL RUN 12:00:54Z on the deployed function: R77 DEPLOYED YES 3 of 3 (after the officers pull); artifact round77/ONE_REAL_RUN_20261007.txt
- DRAIN_END_PACKET.md compiled as a DRAFT, NOT SENT: the round is not drained while ba-23 is open (row Z-S363 BLOCKING for it)
- SECHIST: working-tree blob still c9de003ed6; the exclusion window ended 12:00Z; the merge still waits on Andrew's word
