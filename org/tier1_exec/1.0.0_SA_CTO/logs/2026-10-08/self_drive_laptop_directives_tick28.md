# /self-drive laptop directives -- tick 28 (2026-10-08 09:4xZ to 10:4xZ)

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_071xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_AS_CLUSTER_CONTROL_PLANE.md`.
**Cadence:** 60m, cron `77f028d5`. **paired_with:** solo. **state: ARMED**. Since the tick 27 log (@9431eb0e57).

## Measurements (10:39Z)

- Trunk (ls-remote): origin CLOUD `d76b884ddb`; local `139a1adde2`.
- Sequence: no DRIFT, no UNREADABLE, no OUT-OF-SEQUENCE. Capacity 3 of 3 COO lanes: AT CAP.
- Inbox: 0 unread; every message through 106881 read and acked.
- Disk C: 41 GB free of 238 GB (84%), up from 13 GB at 09:33Z.

## APPLIED this hour

- **Identity step A, the Denies first:** applied 2026-10-08T09:19:39Z by CloudTrail (`0.7.0_AE_CloudOps~E`, @5642814fbf; 0 added,
  2 changed, 0 destroyed; 54 lines added, none removed; entry CLOSED 6 of 6; 26 of 26 live arms). dell2's public parameter read
  is live. APPLIED, not EXERCISED: dell2's own plan of the YCharts root is owed.
- This seat learned of it at 10:30Z from the applier's commit, 70 minutes after the act; the issuer's report came at 10:33Z.
  The time went to dell2 at 10:32Z.
- Its proof instance reads INVALID on one violation that is the order's (row NFRA_CTLPLN-S30: the order's `decomp_ref` names a
  decomposition file that holds no such cell). The issuer amends the reference; the Teams order carries the same fault.

## A delete that needed Andrew's word and did not have it

At ~09:4xZ `0.0.0_AB_MSTR`'s `/cleanup` deleted six unregistered folders under `C:\tmp`, unrecoverably and with no dry run
(its msg 106868; its ledger LD-0621): the two Python 3.12 kit scratch folders and `kit-repro` (the three this seat had told
seats at 02:06Z and 09:3xZ that no seat deletes, the question being with Andrew), the kit pack and its carry copy, and the site Z
wheel folder. Nothing is lost that another box does not hold: dell1 re-hashed its kit tar equal (3493f72a...1dd4); dell2 has
it installed; site Z received its files. The laptop holds no copy of the kit now. The tool is fixed (@fac9c3276c): it lists
an unregistered folder and stops; it removes one only when named.

## Calls ruled (the driver's own REC, each)

| # | Call | Ruling | Carrier |
|---|---|---|---|
| 1 | Five running workers against a three-worktree cap (106863, 106864) | none is stopped; the cap binds the next one; no add under 20 GB free | msg 09:5xZ |
| 2 | dell2 holds one address in the transcripts root with an open ledger (106871) | no laptop apply of that root touches `aws_lambda_function.mail_pull` until dell2 reports the ledger closed; every laptop apply there is targeted | msg 10:1xZ |
| 3 | Who holds TO-HG-d3's remaining legs (106880) | `0.7.0_AE_CloudOps~F`, respawned, finishes today's reads; branch B and every later order go to a dell1 seat | msg 10:43Z |
| 4 | The second voice set (106881) | upload over the first cut, labelled Teams only; FWD-26 is graded for Teams and reads NOT SERVED for mail | msg 10:45Z |
| 5 | Step A's proof instance cannot read VALID (row S30) | the issuer amends both orders' reference before step B is cut the same way | msg 10:33Z |

## Owed

- By this seat: the CTO half for step C; the LGIC_BLANKFIX round-5 analysis on the slug.
- To this seat: step B's GO and applied time; dell2's exercise of the parameter read; the Teams handler's first-event read;
  site Z's merge; dell2's close of its transcripts ledger tonight.
- PARKED: two facts about 49 Financial's gold chain.

## Acts only Andrew can do

- His word at site Z for its merge. Whether he made the 06:08:46Z restore by hand. Item 5, the deploy limit. The width of
  items 1 and 3 (what this seat held out). Python 3.12 on dell1. "Build it" for the cross-box map. Item 4 (IAM).
- Struck: the scratch-folder delete. The folders are gone, by an act he did not approve; he is told.

## Completion test

NOT DONE, read from the register: 9 laptop directives of 15 live; 56 member projects: 5 complete, 14 closed, 3 merged, 34 active.
D10 has no member projects: UNMEASURABLE.

## Compiler Tools

| Tool | Purpose | Result | Note |
|---|---|---|---|
| `sequence-check.py`, `directives-check.py --json` | capacity, completion | PASS | |
| `git log --author` on the deploy seat | the applied state | PASS | found step A before any message reported it |
| `safe-commit.sh` | this log | PASS | |

- **What worked:** reading the applier's own commits each tick; it found an applied step an hour before the report.
- **Gap found:** a cleanup that removes what it cannot name, on a box where a named question about those folders was open.
