# WINDDOWN PARK -- 0.0.3_BG_BBGTerminal -- 2026-09-15T~23:5xZ

**Trigger:** Andrew-direct ~23:5xZ relayed by `0.0.0_AB_MSTR~Z`, Msg-ID 23306, VERBATIM:
*"huntress is blowing up again we need managed winddown"*. READ-acked from the Msg-ID line.

**Carrier class:** durable file in this seat's own `deliverables/` (the only write surface it has --
`bg-concierge-gate.sh` G2 denies git entirely to this serial, so there is NO commit to make and
"push state LOCAL" is not even reachable here). `0.0.0_AB_MSTR` (either seat) is the named integrator
and sweeps this path.

---

## 1. WHAT IS STILL RUNNING

**Nothing.** No task order, no worker subagent, no gate run, no commit, no browser session, no
background terminal. This seat holds no fabric work and cut nothing this session. The one background
command it started (`comp-find`, task `bd2i54lx5`) completed at exit 0 before the winddown.

## 2. WHAT IS PARKED, AND WHERE

| item | state | OWNER | CONDITION that un-parks it |
|---|---|---|---|
| Gateway entitlement findings (below) | COMPLETE, durable in this file + `threads/2026-08-07-andrew-capability-roster/2026-09-15.md` | **Andrew** (holds Cloud Application Administrator on opal-gateway as of this session) | his ruling on any of the three asks |
| Teams emits 18:10-18:25Z (4, all Andrew) | SERVED -- no reply owed; his own *"Don't respond to this."* at 18:10:14Z | this seat | a new inbound ask in that thread |
| `opal_data_refresh_upload` off the allowlist seed | OPEN QUESTION, unexercised by choice | Andrew / gateway owner | a read of the live overlay file on the EC2, or the next `/terminal-upload` run |
| Attachment blindness, 3 inbound since 09-11 | OPEN, cause now NAMED (two mechanisms, below) | Andrew | the `$select` change and/or an allowlist row |

## 3. THE FINDING THAT WOULD OTHERWISE DIE IN CONTEXT

Everything below was measured 2026-09-15T18:4x-18:5xZ by exercising each bucket against the LIVE
guard (`TEAMS_DUTY.md` "Reply norms" -- a capability roster is a self-report). It is written here
because the FOUR-LAYER model existed only in session context and is the actionable half.

**The gateway has FOUR independent permission layers. Cloud Application Administrator moves ONE.**

| layer | what it is | lever | does Cloud App Admin move it? |
|---|---|---|---|
| L1 | Entra app-registration Microsoft Graph scopes | admin consent | **YES -- the new role's lever** |
| L2 | gateway per-identity tool allowlist | `IDENTITY_TOOL_ALLOWLIST_PATH` on the EC2; rows `<email> <tool>`; hot-reloaded per check; ADD-only | **NO** -- a file, not Entra |
| L3 | gateway code (`$select` field lists, absent tools) | build + deploy | **NO** |
| L4 | `.tools/hooks/bg-concierge-gate.sh` local hook | repo edit, Andrew-asked 2026-08-07 | **NO** |

**THE TRAP, STATED PLAINLY:** granting a Graph scope at L1 changes NOTHING observable until L2 gets a
row. Consent could be granted, this seat would still return `identity_scope_denied`, and the natural
reading is that the consent did not take.

**Allowlist, read at SOURCE** (`app/__pycache__/identity_scope.cpython-311.pyc`, `_SEED`), not inferred
from denial text: `opalbloomberg@opalinvest.com` -> exactly **9** tools --
`whoami, list_teams, list_channels, read_channel_messages, send_channel_message, list_chats,
read_chat_messages, send_chat_message, poll_addressed_teams_messages`. **9 of 43** registered on -bbg
(34 core + graph 2 + ycharts 6 + portal 1). Module docstring clause (iii) VERBATIM: *"email/site-write/
upload/ycharts rows are NEVER added for the concierge identity -- structural via absence (an allowlist
has no fail-open row to forget)."*
⚠ The 9 is the **SEED**. The live overlay file is on the EC2 and this seat cannot read it; the four
measured denials (mail, OneDrive, SharePoint, YCharts) are the evidence the overlay has not added them.

**Attachment blindness is TWO causes, not one -- and only one is an entitlement:**
1. **Mail attachments = entitlement.** Mail is off the allowlist *entirely* (`list_recent_email` denied),
   so the attachment ask is downstream of a mailbox this seat cannot open at all.
   `save_email_attachment_to_site` is ALSO denied at L4. Two layers, either sufficient.
2. **Teams attachments = NOT entitlement, it is L3.** The gateway's message `$select` is
   `id,from,body,createdDateTime,lastModifiedDateTime,importance` -- **`attachments` is not selected**,
   so a file post arrives with no attachment metadata. **Widening the allowlist would NOT fix this.**
   Measured on `read_chat_messages` (the `@odata.context` names the select list).
   *Recommended first move: add `attachments` to that `$select`. No Entra dependency, no new permission
   surface, closes 2 of the 3 known cases.*

**Teams sender identity (measured, 5 chats + 3 messages):** `from.user` carries AAD **object id** (GUID),
**displayName**, `userIdentityType`, **tenantId**. **No mail, no UPN, no company.** There is NO directory
lookup tool on -bbg at all (no `get_user`, no `list_chat_members`) -- so the GUID is unresolvable by this
seat under ANY widening of the CURRENT tool set; partner-firm entitlements need L1 + L3 + a REQUEST_CATALOG
change (catalog is sender-blind today: reachability IS the entitlement, Andrew-direct 2026-08-06).
⛔ **NOT MEASURED AND NOT CLAIMED:** all 5 sampled chats are tenant `6810043e-d171-4adc-9975-068b35e179da`.
This sample CANNOT discriminate an external/partner sender; `tenantId` behavior for a federated user vs a
B2B guest differs and must be measured on a real partner message before anything routes on it.

## 4. WHAT WOULD BE LOST IF THIS SEAT STOPPED IN THE NEXT FIVE MINUTES

**NOTHING.** Every finding is in this file and in the thread daily file. No in-flight commit, no worker,
no unlanded report. **This seat is SAFE TO STOP FIRST** -- it should not consume any of the sequencing
budget that the seats holding live commits need.

## 5. PROCESS FOOTPRINT

| class | count | ids |
|---|---|---|
| worker subagents | **0** | -- |
| browser sessions | **0** | none opened this session |
| background terminals | **0** | `bd2i54lx5` completed rc=0 pre-winddown |
| Monitors | **2** | inbox `btx8astds`, Teams `bh8fap3bc` |
| broker registration | 1 | PID 44856 |

**The 2 Monitors are HELD DELIBERATELY, and this is the one judgment call in this record.** Item 6 says
do not self-kill; letting both watchers lapse un-rearmed would make this seat deaf to the stop order
itself -- a soft self-kill. So reachability is held until `0.0.0_AB_MSTR~Z` takes it. **No NEW Monitor,
no new anything, will be armed.** If MSTR~Z prefers the footprint gone sooner, say so and they drop on
receipt.
