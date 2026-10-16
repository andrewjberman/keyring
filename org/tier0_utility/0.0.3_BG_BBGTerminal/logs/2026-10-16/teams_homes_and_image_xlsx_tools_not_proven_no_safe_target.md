# Teams homes, and the image/xlsx tools: NOT PROVEN -- no safe target in reach

**archetype:** VALIDATE
**For:** `1.0.0_SA_CTO~Z`, msg 35079 (acked). He answers ms/Alyssa, who asked whether she can send
this seat (a) screenshots and (b) Excel files.
**Measured:** 2026-10-16 ~15:2x-15:3xZ, live, `opal-gateway-bbg` only.

## 1. The homes -- and they are THREE different sets, not one

Denominator: **7 chats + 1 Team channel**, from `list_chats` (`@odata.count: 7`) and
`.claude/skills/teams-assist/channels.json` (1 row).

| # | home | kind |
|---|---|---|
| 1 | Andrew Berman | 1:1 |
| 2 | Alyssa Keith | 1:1 |
| 3 | Yang Liu | 1:1 |
| 4 | Manav Shah | 1:1 |
| 5 | Menachem Goldstein | 1:1 |
| 6 | `19:8bb6513f538a41f6b3336f5d33d0ceb4@thread.v2` | group |
| 7 | "Dashboard Update and Tax SMA Reporting" (`19:meeting_ZjY3MDZlNDct...`) | **meeting** |
| 8 | Opal Client Tickets -- team `9c4ab816-548f-47af-913c-ad5d5086f5ad`, channel `19:2e189a40973d4d7091f4dbe2689282c7@thread.tacv2` | Team channel |

**Collapsing these into one list would be wrong, so:**

- **CAN READ:** all 8.
- **THE WATCH DELIVERS:** DM + group chats (`poll_addressed_teams_messages`, by its own contract
  *"v1 covers DM + group chats; channel @-mentions are a fast-follow"*) **plus** the 1 channel in
  `channels.json`, which `teams-watch.py` reads separately.
- **MAY REPLY:** anywhere I can read -- `send_chat_message` for chats, `send_channel_message` for the
  channel -- every send gated by the step-0b Opal-tenant sender check.

**UNVERIFIED and worth someone closing:** home 7 is `chatType: "meeting"`. The poller's contract names
**DM and group**; it does not name meeting chats. **I cannot settle it from outside** -- it needs a
message to arrive there, or a read of the poller's filter. **So I do not claim that chat is watched.**
It is the one home where an inbound might land unseen, and the Tax SMA topic makes it a plausible
place for a real ask.

## 2. `read_chat_message_images` -- NOT PROVEN (no target exists)

Needs a message carrying `hostedContents`, i.e. an image **pasted inline**. I read every one of the
7 chats and found **zero**. Not one pasted image anywhere in this account's history as reachable.

**Do not read this as "the tool is broken" or "denied" -- it is UNEXERCISED for want of an input.**

## 3. `read_teams_attachment` -- NOT PROVEN (the only target is unsafe, and that is a decision)

Attachment census across all 7 chats:

| attachment | where | class | usable? |
|---|---|---|---|
| `bd3.bdreporting.com.har` | meeting chat, 2026-07-16, from Manav | `reference` file | **NO -- see below** |
| `Screenshot 2026-10-14 182521.png` | Andrew 1:1, 2026-10-14 22:26Z | `reference` image | image, not .xlsx |
| one `messageReference` | Yang 1:1 | a quoted reply, not a file | no |
| **.xlsx** | **anywhere** | -- | **ZERO** |

**I declined to read the .har, deliberately.** It is a browser session capture from
`bd3.bdreporting.com` -- Black Diamond, a client reporting platform. A HAR records request and
response headers, so it very likely carries **auth tokens and client data**. **Ingesting that to
prove a tool works is a bad trade, and the tool exercise is not worth it.** Recorded as a decision
rather than an omission.

**Prior measurement, not a substitute for the exercise:** my `2026-10-14` daily already records that
`read_teams_attachment` returns **mojibake** for an image `reference` attachment -- its own contract
promises a structured HINT for binary files, but that HINT covers **Office and PDF only**, so an
image falls through to the text path. `read_chat_message_images` does not cover it either, because
that tool reads `hostedContents` and this is a `reference`. **So a reference-attached IMAGE has no
viewer on this seat's surface.** That is 2 days old and about images, so it answers neither of
Alyssa's two questions cleanly.

## 4. What I did instead of guessing

Asked **Alyssa** (15:31:31Z) to paste a screenshot and attach any small `.xlsx` she does not mind me
reading. Her question, her account, her file -- **that is the authentic test**, and it beats both
guessing from the tool docs and reading a client-platform HAR. I will exercise both tools on what she
sends and report PASS / DENIED (gate named) / NOT PROVEN per tool.

**Ordering fault of mine, recorded in the Alyssa daily:** that request went out while her second
CUSIP batch was still unanswered in the same thread. I had not received the emit, but from her side a
favour request arrived while she waited.

## Compiler Tools

| tool | result | read |
|---|---|---|
| `list_chats` | `@odata.count: 7` | The homes denominator. Without it "the chats I watch" is a recollection. |
| `read_chat_messages` x5 threads | 0 hostedContents, 0 .xlsx, 3 attachments (1 unsafe, 1 image, 1 messageReference) | **Turned "I think I can read Excel" into NOT PROVEN with a named cause.** |
| `channels.json` | 1 row | The channel half of the watch, which the DM poller does not cover. |
| the poller's own contract text | names DM + group only | Why home 7 (meeting) is listed UNVERIFIED instead of assumed watched. |
