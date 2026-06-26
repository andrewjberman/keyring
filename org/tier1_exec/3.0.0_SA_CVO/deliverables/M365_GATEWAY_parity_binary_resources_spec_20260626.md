# M365 Gateway — full generalization spec: OneDrive↔Site parity + binary/office reads + MCP resources

**Author:** 3.0.0_SA_CVO · **Date:** 2026-06-26 · **Andrew-direct** (via 0.0.1_UA_mstools 204156Z)
**Builds on:** UA's read_site_file + read_site_workbook (staged in `infra/aws/ec2/m365-mcp-gateway/app/tools.py`)
**Owner split:** CVO designs/specs · **0.8.0_AE_CloudComp owns the tools.py commit + EC2 gateway redeploy** (infra/aws lane)
**Security invariant (KEEP):** per-user DELEGATED scope only — a user reaches only their own mail/files + the SharePoint sites they already have access to. **NO new Graph app perms** — everything below is reachable with the existing consented delegated grants (Sites.Read.All, Files.ReadWrite.All, Mail.*, Calendars.*, Chat.*, Channel.*).

## Grounded current surface (tools.py audit, 2026-06-26)
21 tools. Drive/file family is the gap zone; mail/calendar/chat/teams are complete for their (delegated, /me + membership) model.

| Class | tools | Graph base |
|---|---|---|
| Mail | list_recent_email, search_email, read_email, create_draft, send_email, reply_email | /me/messages, /me/sendMail |
| Calendar | list_calendar | /me/calendarView |
| OneDrive | list_onedrive, search_files, read_file | /me/drive |
| SharePoint site | find_sharepoint_site, list_site_files, **read_site_file**, **read_site_workbook** | /sites, /sites/{id}/drive |
| Chat | list_chats, read_chat_messages, send_chat_message | /me/chats, /chats/{id} |
| Teams | list_teams, list_channels, read_channel_messages, send_channel_message, poll_addressed | /me/joinedTeams, /teams/{id} |

**MCP resources: ZERO** (verified via ListMcpResources → "No resources found"). Gateway is tools-only.

---

## Part 1 — OneDrive ↔ SharePoint-site PARITY matrix (Principle 1)
Every `/me/drive` capability needs a `/sites/{site_id}/drive` counterpart. Fill the matrix:

| Capability | OneDrive (/me/drive) | Site (/sites/{site_id}/drive) | Action |
|---|---|---|---|
| list children | list_onedrive ✓ | list_site_files ✓ | none |
| read text file | read_file ✓ | read_site_file ✓ (UA) | none |
| **read workbook (xlsx)** | **MISSING** | read_site_workbook ✓ (UA) | **ADD `read_workbook`** (`/me/drive/items/{id}/workbook`) — same gap exists on the OneDrive side |
| **search files** | search_files ✓ | **MISSING** | **ADD `search_site_files`** (`/sites/{id}/drive/root/search(q=…)`) |
| **get item metadata** | **MISSING** | **MISSING** | **ADD `get_item` / `get_site_item`** (`…/items/{id}?$select=name,size,file,folder,webUrl,lastModifiedDateTime`) — lets a caller resolve type/size BEFORE choosing read_file vs read_workbook |
| **list libraries (drives)** | n/a (one drive) | **MISSING** | **ADD `list_site_drives`** (`/sites/{id}/drives`) — a site has N document libraries; today only the DEFAULT drive is reachable. Then allow the drive-scoped variants to target a non-default library (`/drives/{drive_id}/…`) |

Net new tools: `read_workbook`, `search_site_files`, `get_item`, `get_site_item`, `list_site_drives` (+ optional `drive_id` param on the site file tools to reach non-default libraries).

---

## Part 2 — BINARY / OFFICE formats via Graph-native APIs (Principle 2)
`read_file`/`read_site_file` byte-decode as text → **garbage for .xlsx/.docx/.pptx/.pdf**. Never parse bytes client-side; ask Graph for structured/converted output.

1. **.xlsx → Workbook API** (`…/items/{id}/workbook/worksheets('{sheet}')/usedRange?$select=text,address,rowCount,columnCount`). read_site_workbook does this for sites; ADD the OneDrive twin (`read_workbook`).
2. **.docx / .pptx → Graph format-conversion** (`…/items/{id}/content?format=pdf`) then text-extract, OR Graph's text extraction where available. Provide `read_document(item_id[, site_id], as=text|pdf)` for BOTH OneDrive + site.
3. **Content-type guard in read_file/read_site_file:** detect by extension/`file.mimeType` (use the new `get_item`) and, for a binary office type, RETURN A STRUCTURED HINT ("this is .xlsx — call read_workbook" / ".docx — call read_document") instead of returning decoded garbage. Fail loud + useful, not silently wrong (the false-clean discipline on the value layer).

---

## Part 3 — Expose as MCP RESOURCES (Principle 3 — the "no resources" fix)
Implement `resources/list` + `resources/read` so a client BROWSES the estate by URI, not only via imperative tool calls. The read_* tools become the read backends. Proposed URI scheme:

```
m365://onedrive                         -> resources/list children of /me/drive/root
m365://onedrive/{path}                  -> a folder or file node
m365://sites                            -> the sites the user can see (find_sharepoint_site with no filter / followed sites)
m365://sites/{site_id}                  -> the site's libraries (list_site_drives)
m365://sites/{site_id}/{drive_id}/{path}-> a library folder/file node
m365://mail/{folder}                    -> (optional) recent mail as resources
```
- `resources/list` returns the children at a node (folders + files) with name/size/mimeType/uri.
- `resources/read` on a FILE uri dispatches by type: text → read_(site_)file; xlsx → read_(site_)workbook; docx/pptx → read_document. **Same type-dispatch as Part 2** (one resolver, reused).
- Result: a client (incl. the UA agents) discovers sites→libraries→files and reads by URI — no more "no resources found → grep the gateway source." This is the literal fix for the symptom Andrew/UA hit.

---

## Part 4 — Delivery plan (batch, one coordinated deploy)
- **CVO (me):** this spec is the design. Hand to AE.
- **0.8.0_AE_CloudComp:** implement Parts 1-3 in `app/tools.py` (+ the resources handlers — likely `app/resources.py` registered on the MCP server), on top of UA's staged read_site_* diff. ONE batch.
- **Deploy coordination (KEEP — UA flagged):** each gateway redeploy RESTARTS it → drops live `/mcp` sessions. **Do NOT deploy piecemeal.** Batch all of Parts 1-3 into one redeploy and coordinate the restart window with Andrew (so it doesn't drop active agent sessions mid-task). The standard infra/aws path: stage → py_compile + ruff (UA already does this) → AE commits via safe-commit → EC2 gateway redeploy via the m365-mcp-gateway deploy path → smoke (ListMcpResources now non-empty + a read_site_workbook + a resources/read round-trip).
- **Acceptance smoke (CVO verify on AE's deploy):** (1) ListMcpResources(m365) returns the sites/onedrive hierarchy (non-empty); (2) read_workbook on a OneDrive .xlsx returns a cell grid; (3) read_document on a .docx returns text/pdf; (4) search_site_files returns hits; (5) a binary read_file returns the structured hint, not garbage. I'll run this against the redeployed gateway and RAVC.

## Scope guardrails
- NO new Graph app permissions (everything is in the existing delegated grant — UA-confirmed; I re-confirm: Sites.Read.All covers site read, Files.ReadWrite.All covers drive items, the Workbook + convert APIs need no extra scope beyond Files/Sites read).
- Per-user delegated security model preserved (a user still only reaches what they personally can access).
- infra/aws stays the AE lane; CVO does not commit tools.py — this spec + the acceptance smoke are the CVO deliverables.

— 3.0.0_SA_CVO
