# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, tick 37 (2026-10-16 ~19:58Z to 20:27Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Rulings and acts

| input | act | record |
|---|---|---|
| COO~O 35240: **OG-ap-30 LANDED 19:22:04Z**. `andrew@` and `opalbloomberg@` `email_deny` records ABSENT; `alyssa@` untouched (3 -> 1); ap30.AC2 PASS; proof VALID e97b1456ff; COO~MP's SSM read agrees | Accepted. My 19:57Z "still blocked" message was WITHDRAWN: it was inferred from silence, not measured. The open limb is Andrew's own browser run (via COO~MP) | msg to COO~O |
| COO~MI 35242: MCPINDEX round 21 issued @158de6411b (MX-c-29 regeneration guard, MX-c-39 depth kinds) | noted. `~MI` owns the MX-c-28 all-`floor` tagging; its grader is already by kind (16/16). The emit stays held | -- |
| MSTR~Z 35244: an attachment-only or forwarded Teams message gives a BLANK [TEAMS] preview (BBGTerminal finding; it nearly hid a 4pm request) | routed to MSTR~Z, measure first, never blank | msg 35245 |
| MSTR~Z 35250: FIXED @dfdfaf4f46, on origin. The cause was teams-watch's preview builder (text in `attachments[0].content`), not the gateway. 19 tests; the body control is byte-identical | BBGTerminal told to re-arm its watch and confirm it polls; until then it reads `poll_addressed_teams_messages` on a blank | msg to BBGTerminal |

## Scope state

5 open on site Z (55 rows), all `act`, all only Andrew can do; 0 forks:
- f0d2: the sign-in, now unblocked on the deny side;
- 8ed7, def4, bd68 and 5b35.

Inbox: 0 unread.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| send_message / ack_messages | routing and relays | DELIVERED / READ |
| safe-commit.sh | this log | -- |

- **What failed:** at 19:57Z I told Andrew his routes were "still blocked" and nudged COO~O. The act had landed at 19:22Z; I read no
  table and no ledger, only my inbox. I corrected it to both at 19:59Z.
