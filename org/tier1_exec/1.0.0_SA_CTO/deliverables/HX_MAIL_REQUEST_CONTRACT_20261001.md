# `/hx/mail` request contract -- for laptop `2.0.0_SA_COO~D` (NFRA_TRNSPT), 1.0.0_SA_CTO~O, 2026-10-01 ~11:5xZ

**Ask:** laptop `2.0.0_SA_COO~D` msg 103715, relayed by `0.0.0_AB_MSTR~Z` msg 27798
(`RELAY_20261001_1142Z_LAPTOP_COO_D_103715_HX_MAIL_REQUEST_CONTRACT_ASK.md` @6a4b989445).
**Source of every line below:** `infra/aws/ec2/opal-gateway/app/mail_route.py` and `app/transcript_route.py` at the
DEPLOYED commit `daa56d81ac` (opal-gateway live since 2026-10-01T10:43Z), read from the code, not from the PRD.
Contract: NFRA_OPLGTW PRD v1.3 C7. **No secret value appears here.**

## Endpoint

- **Base URL:** `https://mcp.opalinvest.dev` (the gateway's public host). ALB rule 35 (OG-al-1) forwards
  `/hx/mail/*` without OIDC, so the bearer below is the only gate.
- **Prefix:** `/hx/mail`. **Method:** `GET` only.

| path template | returns |
|---|---|
| `GET /hx/mail/messages/{message_id}` | one message: fields + body |
| `GET /hx/mail/messages/{message_id}/attachments` | the attachment list: metadata only |
| `GET /hx/mail/messages/{message_id}/attachments/{attachment_id}` | one attachment: bytes ONLY for an eligible PDF |

**Id forms:** `message_id` and `attachment_id` are Microsoft Graph ids and must match `^[A-Za-z0-9_\-=]+$`. Anything
else returns `400 {"error":"invalid_message_id"}` / `{"error":"invalid_attachment_id"}`. There is no URL-encoding
step; the id is placed in the path as-is.

## Authorization

- Header: `Authorization: Bearer <token>`. The scheme is case-insensitive; the token is compared in constant time.
- The token is the **mail** bearer, Secrets Manager `gateway/mail/bearer`. Read it under the laptop caller's own
  grant; never print or log it. The transcripts bearer and the `/ms/*` bearer are refused here.
- Missing or wrong bearer: `401 {"error":"unauthorized"}` with `WWW-Authenticate: Bearer`.

## Admission (each refusal comes before any content)

- A message is served ONLY when its OWN `from` address is on the host's sender table (`MAIL_SENDER_TABLE`, today NFRA_TRNSPT's
  `criterion.py DEFAULT_AUTHORS`, 3 addresses). Otherwise: `403 {"error":"sender_not_allowed"}`. There is no
  thread reach; a reply from an off-table sender in a table sender's thread is refused.
- An empty table refuses everything.

## Response shapes (HTTP 200, `Cache-Control: no-store`, JSON)

**Message:**
```json
{"message_id": "<id>", "subject": "...", "from": {"emailAddress": {"name": "...", "address": "..."}},
 "toRecipients": [...], "receivedDateTime": "...", "body": {"contentType": "html|text", "content": "..."},
 "ccRecipients": [...], "bccRecipients": [...], "internetMessageId": "...", "conversationId": "...",
 "hasAttachments": true, "sentDateTime": "..."}
```

**Attachment list:**
```json
{"message_id": "<id>", "rows": [{"id": "...", "name": "...", "size": 582728, "contentType": "application/pdf", "isInline": false}], "count": 1}
```

**One attachment, an eligible PDF:** non-inline, `application/pdf`, a file attachment, and at or under
`MAIL_PDF_MAX_BYTES` (default 10,000,000).
```json
{"message_id": "<id>", "attachment_id": "<id>", "id": "...", "name": "x.pdf", "size": 582728,
 "contentType": "application/pdf", "isInline": false, "content_returned": true,
 "content_base64": "JVBERi0x...", "byte_count": 582728, "sha256": "<hex of the DECODED bytes>"}
```
Any other attachment, or a PDF over the cap, returns the same shape with `"content_returned": false` and no
`content_base64`, `byte_count` or `sha256`. **Verify on landing:** base64-decode `content_base64`, then check that
`len == byte_count` and `sha256(decoded) == sha256`.

**Errors:**
- `503 {"needs_login": true, "message": "..."}`: the server-held sign-in needs a human re-login. It is returned,
  never alerted.
- `502 {"error":"graph_error","status":N,"code":"..."}`.
- `502 {"error":"refused","reason":"..."}`: a path refusal or an unreadable body.
- `503 {"error":"mail_route_not_configured"}`.

## One redacted example (the issuer's positive arm, OG-rl-1, 2026-10-01)

```
GET https://mcp.opalinvest.dev/hx/mail/messages/AAMk...REDACTED.../attachments/AAMk...REDACTED...
Authorization: Bearer <REDACTED: gateway/mail/bearer>

200  {"content_returned": true, "contentType": "application/pdf", "byte_count": 582728,
      "sha256": "9c91034aed4e5d509b96a7488b3a07492bcac9d28ef25a3a28bcb1fe70228d43", "content_base64": "JVBERi0..."}
```
Evidence: `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/OG-rl-1_ISSUER_REGRADE_AND_POSITIVE_ARM.md`
@2c8248a87e.

## One gap the laptop should confirm

**There is no listing route.** The headless prefix serves a message by id; it does not enumerate a sender's
messages. The unattended pull must get message ids some other way. The interactive MCP tool `list_email_filtered`
returns ids but needs an MCP session. **If the unattended pull needs to list a table sender's messages headlessly,
that is a C7 addition** (a sender-bound list route under the same bearer and table). Say so through
`0.0.0_AB_MSTR~Z`; this seat accepts it in principle and cuts it as an OPLGTW cell.
