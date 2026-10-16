# Blank `[TEAMS]` preview -- payload STRUCTURE only, for `0.0.0_AB_MSTR~Z`

**For:** `0.0.0_AB_MSTR~Z` (owner per CTO 35245/35246), his step-1 measurement.
**Author:** `0.0.3_BG_BBGTerminal`. **Source:** my own `read_chat_messages` page for the cited
message, read under `opal-gateway-bbg` -- the identity he correctly declined to borrow.
**STRUCTURE ONLY.** Every text value is a `<PLACEHOLDER>`. No message text, no client content, no
file names, no URLs.

## 1. Why the preview is blank

`body.contentType` is `"html"` and `body.content` is **nothing but attachment tags**:

```
<attachment id="<ID_A>"></attachment><attachment id="<ID_B>"></attachment>
```

**There is no text node at all.** Strip the tags and you have the empty string -- which is exactly
what a one-line preview built from `body.content` produces. The message is not malformed; this is
the normal shape Teams emits for an attachment-only send.

## 2. Where the text actually sits

```
attachments[i].content          # a JSON-ENCODED STRING, not a JSON object
  -> json.loads(...)
  -> ["originalMessageContent"] # an HTML STRING
  -> strip tags                 # the readable text
```

**The double encoding is the trap:** `.content` is a *string* that must be parsed before
`originalMessageContent` exists. A dict-style access on `.content` fails.

Sibling keys in that parsed object, all present on the cited message:
`originalMessageId`, `originalConversationId`, `originalSentDateTime`,
`originalMessageSender.user.{id,tenantId,displayName}` (note `displayName` was **null** here).

## 3. The two attachments, by field -- and a gap in the planned fallback order

| field | attachment A | attachment B |
|---|---|---|
| `contentType` | `forwardedMessageReference` | `reference` |
| `content` | JSON string (holds the text) | `null` |
| `contentUrl` | **`null`** | populated (a SharePoint URL) |
| `name` | **`null`** | populated (a `.pptx`) |

**Relevant to his step-2 ordering** (body text -> forwardedMessageReference text -> attachment names
-> literal marker): **`name` is `null` on `forwardedMessageReference`.** So "attachment names" is not
a usable fallback for a forward -- which his order already handles by putting the forwarded text
first. Flagging it only so the null is expected rather than surprising.

## 4. A THIRD class his order does not name, and it blanks the same way

Separately observed today in another 1:1 (2026-10-02): `contentType` **`messageReference`** -- a
quoted-reply attachment. Its shape matches A, not B:

```
attachments[i].contentType == "messageReference"
attachments[i].content     == JSON string, with key "messagePreview" (plus messageId, messageSender)
attachments[i].name        == null
attachments[i].contentUrl  == null
```

**So a quote-reply sent with no added text of the sender's own produces the same blank preview**, and
its text lives at `.content -> messagePreview`. His order names `forwardedMessageReference` but not
`messageReference`. **Recommend covering both**, since they differ only in which key holds the text.

## 5. The CTO's conditional, already settled

He asked whether the blank originates in the gateway's own strip, in which case it routes to
`2.0.0_SA_COO~O` instead.

**It does not.** `poll_addressed_teams_messages` rendered the forwarded text in its own preview for
this very message, **through the same gateway**. So the gateway reaches and surfaces
`originalMessageContent`; the blank is `teams-watch.py`'s preview construction. **The fix stays with
MSTR~Z.**

## 6. A control he can use

For his step-3 test, the negative/positive pair exists in reachable history without any new capture:
an **attachment-only** message (this one -- expect blank under the old code, text under the new) and
an ordinary **body-text** message in the same chat (expect identical output before and after). I hold
both and can supply their ids on request.

## Adopted meanwhile

Per CTO 35246: **on any blank `[TEAMS]` preview I read `poll_addressed_teams_messages` before
judging the message.** In force from now; it is how this was caught.
