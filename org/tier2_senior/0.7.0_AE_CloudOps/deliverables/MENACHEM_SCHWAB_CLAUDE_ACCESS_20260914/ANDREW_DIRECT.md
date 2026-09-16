# Andrew-direct request: Menachem Schwab access
Archetype: instruction record / specification request
Seat: 0.7.0_AE_CloudOps
Channel: direct user messages in this Codex conversation
Recorded: 2026-09-14T18:20:06Z (recording time; original message timestamps are not exposed)
Scope: research and specification. No access provisioning or deployment requested.

Verbatim request:

```text
This is what i need you to look into and spec out. the issue is this opal user is non-technical, and they use the claude application not claude code (no cli), so we'd have to figure out what is an easy mechanism for them to be able to query the data herein: [<Also I need to get an Opal User, menachem@opalinvest.com, access to the Schwab files in
  opal-data-assets. I want to customize his access and gradually expand it as he uses it. I also
  want to make sure that he has read-only access on those files, he can download but no write, no
  bucket modification, etc. so he can't accidentally delete it or something. Let's identify how we
  can do this.>]
```

Verbatim clarification answers, in order:

```text
An Opal Team or Enterprise workspace
```

```text
Both questions and downloads
```

```text
Both masters, kept separate
```

Verbatim architectural steering:

```text
Part of me thinks this whole thing can be managed through the opal-gateway mcp server, and this can be done as an entitlement to menachem's account
```

Verbatim download-format answer, received before completion:

```text
Filtered CSVs initially; expand original-file access later
```

Resulting specification uses the existing opal-gateway, a per-user Schwab data entitlement, and a dedicated assumed read role. Filtered CSVs initially and later expansion of original-file access are confirmed. Initial fields/date range/account scope remain proposed defaults. This record does not authorize implementation, grant expansion, or unrelated task orders.

Follow-up review request, direct Codex user channel; recorded 2026-09-14 after 18:41Z (exact user submission time unavailable):

```text
C:\Users\AndrewBerman\Downloads\Claude_Remote_MCP_Requirements_Brief.docx Here is the doc on requirements from GPT, take a look at it and see if theres anything we're forgetting or if we're good to go with the brief as you've laid it out thus far.
```

Reviewed the exact document and updated the local specification. This request does not authorize deployment, access provisioning or outbound messages.
