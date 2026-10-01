# NFRA_OPLGTW task order -- `OG-hl-1` -- the headless /hx/mail LISTING route, BUILD only (PRD v1.4 C7)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-hl-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~16</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a request route; the daily pull's schedule is NFRA_TRNSPT's (laptop). No alert (C7).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the same bearer secret and Graph scope (Mail.Read) as OG-hr-2.
comp-adversary: DECLARED-NOT-APPLICABLE -- the boundary is the CTO's (PRD v1.4 C7 "Mail listing" @dabb8e1e9f, prd-signoff ADMITTED).
EGRESS CLASS, declared: NONE. No AWS call, no Graph call, no deploy.
</preflight>

## 1. THE CELL -- `OG-hl-1` (decomposition addendum R3-T.3)

`GW` = `infra/aws/ec2/opal-gateway`. Read PRD `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` C7 "Headless
content routes" and the **v1.4 addendum** whole (at @dabb8e1e9f or later), and `GW/app/mail_route.py` (the served
`/hx/mail` route, OG-hr-2) as the PATTERN: same bearer, same sender table, same `_graph` allowlist function.

1. **The route.** In `GW/app/mail_route.py` add `LIST_ROUTE = PREFIX + "/messages"` and a GET handler, registered in
   `GW/app/server.py` as `Route(mail_route.LIST_ROUTE, ...)` next to the three existing mail routes. Same bearer check
   (`match_bearer`, constant time; another prefix's bearer refused 401), same `configured()` gate.
2. **Parameters and refusals** (each returned to the caller, never an alert):
   - `sender`: ONE address; refused `403 {"error": "sender_not_allowed"}` when it is not on `sender_table()`
     (case-insensitive) or the table is empty, BEFORE any Graph call; a malformed value `400 {"error": "invalid_sender"}`;
   - `received_from`, `received_to`: UTC ISO 8601, half-open `[from, to)`, both required; missing, unparsable,
     `to <= from`, or longer than **31 days**: `400 {"error": "invalid_window"}`;
   - `has_attachment`: `true` or omitted; anything else `400 {"error": "invalid_has_attachment"}`;
   - `page_size`: default 25, 1..50, else `400 {"error": "invalid_page_size"}`;
   - `page_token`: see 4; a bad one `400 {"error": "invalid_page_token"}`.
3. **The Graph read.** The allowlist gains exactly `^/me/messages$`. The handler builds `$filter` (the sender's address,
   the window, and `hasAttachments eq true` when asked), `$select` (only what the rows and the re-check need),
   `$orderby=receivedDateTime asc` and `$top` server-side only; GET only. Follow Graph's next link server-side, at most
   **200** pages per request.
4. **The opaque page token.** The gateway's own value (e.g. base64url of a JSON carrying the allowlisted path's
   continuation, the sender and the window). A decoded token is honored ONLY when it names the `/me/messages` path
   allowlisted here AND carries the SAME sender and window as the request; anything else, and any raw Graph URL, is
   `400 invalid_page_token`. A Graph URL is never returned.
5. **Rows.** Every returned message's OWN `from` is re-checked against the table; a row that fails is dropped and
   counted in the audit, never listed. Each listed row has EXACTLY `message_id`, `receivedDateTime`, `sentDateTime`,
   `internetMessageId`, `hasAttachments`. Response 200 (`Cache-Control: no-store`):
   `{"rows": [...], "count": <rows in this page>, "next_page_token": <opaque> | null}`, ascending `receivedDateTime`,
   stable across pages, no row repeated. An empty window is `200` with `rows: []`, `count: 0`, `next_page_token: null`.
6. **Audit:** route, sender HASH (sha256 hex), window, row count, dropped count, bearer label. Never an address or content.
7. **The sender-table file (row Z-S36's durable fix, its single source).** Add `GW/deploy/mail_sender_table.txt`: one
   address per line, exactly NFRA_TRNSPT's `data/transcripts/scripts/outlook/criterion.py` `DEFAULT_AUTHORS`, in that
   order. A test keeps it equal (import `criterion`, compare). The release (`OG-rl-2`) makes the deploy read this file
   host-side; this cell does not touch `deploy-to-ec2.sh`.
8. **Tests.** A new `GW/tests/test_mail_listing.py` with exactly the 12 tests `hl1.AC1.sh` names, Graph and the token
   broker stubbed; `test_sender_table_file_equals_criterion` is the file test.

## 2. BOUNDS

1. Code, tests, the one data file and the record only. No AWS call, no Graph call, no deploy. Never edit
   `ms_ingest.py`, `GRAPH_SCOPES`, the identity allowlist, `deploy-to-ec2.sh` or the PRD. The existing three mail routes
   and the transcripts route keep their behaviour (their tests stay green).
2. Every test run sets `AUDIT_PATH` to a temp file; restore `GW/audit.jsonl` if dirtied.
3. Work in the worktree named in your identity line. Never push, merge, rebase, stash, `checkout --` or `clean`.
   REFUSE a criterion you cannot meet as written.
4. Commit with `.tools/safe-commit.sh` under your serial; every `.py` passes `.tools/commit-gate.sh`; each commit message
   names `OG-hl-1` (the release's narrow census reads it).

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/mail_route.py
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/app/config.py
infra/aws/ec2/opal-gateway/deploy/mail_sender_table.txt
infra/aws/ec2/opal-gateway/tests/test_mail_listing.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~16/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W16-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-hl-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/hl1.AC1.sh; echo "exit=$?"</invocation><expect>named tests passed 12 of 12; failed/error lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-hl-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/hl1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)equal True.*carries \^/me/messages\$: True.*registered in server.py: True.*HL ok.*app/ms_ingest\.py changed since base \w+: 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the v1.4 listing rules and the sender-table file, by the 12 named tests.
- `AC2`: the file equals `criterion.py`, the allowlist and route are wired, `/ms/*` is byte-unchanged.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~16/NFRA_OPLGTW.TO-OG-hl-1.hx-mail-listing.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Report once: the diff stat, the 12 test names, the
literal AC1-AC2 output, the commits and the rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round label 11 (decomposition addendum R3-T.3), ONE issuance with `OG-rl-2`; edge `OG-hl-1` -> `OG-rl-2`.
- Pre-cut controls: `hl1.AC2.sh` reads FAIL on today's code (file absent, route unregistered; the over-matching
  "registered" predicate was tightened to `mail_route.LIST_ROUTE` after it read True on today's code).
- `<risk>` WORLD is GATE (xii)'s floor; the cell deploys nothing.

<status>pending</status>
<status>complete</status>
<round>11</round>
<slot>~16</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
