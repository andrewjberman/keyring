# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, tick 55 (2026-10-17 ~04:59Z to 05:27Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Rulings and acts

| input | act | record |
|---|---|---|
| ~NFRA1 35377 / COO~O 35379, OG-ap-34 CT1 pre-deploy chain. Fresh process, 12 pages, 334 partitions. Host peak 58.0 percent; median page +0.3 MB; process +239 at the end, +337 at a page end, +592 mid-page. As written, Amendment 1 step 1 FAILS; COO~O recommended grading the service ("Reading 1") | **Ruled: Amendment 2.** The FAIL is recorded and not re-read. The 300 MB bound is replaced by a two-chain plateau test before deploy: second-chain net growth of 50 MB or less, host under 80 percent, no page over 55 s. COO~O's post-deploy triggers are adopted: host 80 percent, service +700 MB, over 20 MB per call after the first. "Reading 1" is refused because no page ran in the service | @24bc48799d; msgs 35380-35382 |
| BBGTerminal 35384: its Andrew-direct record of 03:5xZ (the full rivalfunds backfill) cannot be committed in its lane | Read in full, then committed unchanged under the CTO~Z author | @72d51b3a24 |

## Scope state

4 open on site Z (55 rows), all `act`: f0d2, 8ed7, def4 (postponed by Andrew) and 5b35. Inbox: 0 unread. OG-ap-34: no deploy;
the two-chain test is owed by ~NFRA1; live is `d3ae88be46`.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| send_message / ack_messages | the Amendment 2 ruling, record receipt | DELIVERED / READ |
| safe-commit | amendment 2, BBGTerminal record | LANDED |
