# TCKT_VNEXT: CVO adjudication, rounds 18 and 19 (meeting request, trade-form routes, cross-firm narrowing)

<sweep_watermark>2026-10-16T21:05Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL2, 2026-10-16.

L9 grade by `3.0.0_SA_CVO~DELL2` (dell2), 2026-10-16T21:05Z, a seat that did none of this work. Input:
`org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R18_R19.md @e424376b67` (blob deb61d7fe2f9, sha256 8c5c435ffc26, verified; msg 9855).

**What this seat read itself, not taken from the packet:**
- **The source as built.** The ticket Lambda source at `built_from_sha` de2fdb4a4f: the meeting, attachment, notice, intake-list and
  profile-scope paths, quoted line by line.
- **The tests.** The full suite at de2fdb4a4f, run by this seat in a detached worktree: **466 passed, 59 subtests passed, 0 failed.** The
  packet's "test_cross_firm_global_register.py red 4 of 7" does not reproduce on the built commit.
- **The Terraform diffs.** 5cb98dbac4 (R18-TR2), 43715c1c3b (R18-TR3) and 9855742266 (R19-TR), and the builder record
  `ATTACH_ADDRESS.json`. I re-ran the three `address()` calls and they reproduce it.
- **The portal candidates.** 12c164a0 (Meeting Request) and c05e3dda (Trade Request): the on-screen words.
- **The live state, 2026-10-16 ~21:0xZ:**
  - `opal-ticket-api` CodeSha256 `JwdnACONAnxwqzhsVgqgU+nRoLdmS7MyLmzXmZuXsR4=`;
  - `ANALYST_INTAKE_ALLOWED_FIRMS=49financial,inflection,cottonwood`;
  - `CLIENT_NOTICE_CONTACT_MAP={}`;
  - `TICKET_ATTACH_BUCKET_TEMPLATE=opal-data-{firm}`;
  - `TICKET_ATTACH_KEY_TEMPLATE=portal/{firm}/state/ticket_attachments/trade-form/`;
  - `ROUTING_MATRIX.meeting_request.primary=[jeanette@opalinvest.com]`;
  - role policy `opal-ticket-attachments-trade-form-policy`: one statement, `s3:PutObject` and `s3:GetObject`, the three firm prefixes.
- **The run trace.** `R18_RUN_RESULT.json` and `R18_RUN_PART1_TRACE.json` of `0.7.0_AE_CloudOps~TV2`.

## Grades

**TCKT_VNEXT.TO-R19-L1 R19L1-AC3J MET.**
- The recipient is chosen from `CLIENT_NOTICE_CONTACT_MAP[requester.firm]` of the STORED ticket (`_client_recipients`, L1237-1248).
- A stored address that is not a contact goes to the firm's first contact and is logged as `to_digest=` only (L1247).
- Unset, empty, non-object or malformed JSON returns `{}` and sends nothing (L1202-1221).
- `ClientRecipientNotSingular` stands (L1263-1265).
- Live: since the apply end, zero `WE_CLIENT_SENT` and one `WE_CLIENT_NO_CONTACT` (the issuer's after-read).

**TCKT_VNEXT.TO-R19-L2 R19L2-AC3J MET.**
- `ANALYST_INTAKE_ALLOWED_FIRMS` drops `ALL` (L90-91). Unset or empty is the empty set and lists nothing (200, count 0).
- The diff 8957fed16b is two pure additions, and the LIST filter is guarded by `pc == SVC_ANALYST_INTAKE` alone, so no other principal's
  LIST changed.
- Live: the variable reads exactly the three served firms.

**TCKT_VNEXT.TO-R19-L3 R19L3-AC3J MET.**
- `_profile_scope` (L395-439): no list and no marker is 403 "firm scope not configured".
- The global admission needs `scope_all_firms is True`; a string, 1 or False are refused.
- A list together with the marker is 403 "firm scope malformed".
- The diff 028ee030b9 leaves the AMBIGUOUS / NO-ROW / LOOKUP-FAILED / NOT-ACTIVE branches untouched.
- It also closes the two old fail-open paths (an absent list and an empty list both admitted every firm).
- No live arm of the refusal itself; `TO-R19-MIG` placed 19 markers (MIG-OK).

**TCKT_VNEXT.TO-R19-TR R19TR-AC3J MET.**
- The diff 9855742266 adds exactly two environment values: the contact map `"{}"` (no address invented) and the intake list of the three
  served firms (no wildcard).
- The worker planned and applied nothing. The live function reads both values as written.

**TCKT_VNEXT.TO-R18-L1 R18L1-AC3J MET.**
- `meeting_ticket` (L2007-2062) admits INTERNAL only, then requires `actor.email` in the ticket's `routing.primary`.
- The one write is `SET meeting = :m, events = list_append(events, :e)`, conditioned on type `meeting_request` and not completed.
- No `notify_*` or SES call is made on any path.
- An out-of-scope ticket and an unknown ticket give the same 404. The 403 and 409 tests run only on a ticket the caller may see.
- Live (PART 1): the confirm returned 200 with `meeting.by` set to the coordinator, status still `open`, and CONFIRM log tokens `[]`.

**TCKT_VNEXT.TO-R18-L2 R18L2-AC3J MET** on the source and tests at the built commit.
- The upload firm is checked against the caller's scope (`_create_firm_allowed`), and the key is built on the server.
- The open route applies the same 404 fence as `get_ticket` (`_in_profile_scope` on `requester.firm`) and refuses a key outside the firm's
  prefix.
- Both routes only `generate_presigned_url`; no object byte is read or written.
- No trades call is made.
- An unset, empty or malformed bucket or key template is 503 with nothing presigned.
- The live arm is FWD-10's, which is not run (PART 2 is held); this grade does not stand in for it.

**TCKT_VNEXT.TO-R18-TR1 R18TR1-AC3J MET.**
- The tier is `state` per R21 (`tiers.json` FIRM.state = scope).
- The addresses are `lib/opal_naming.address()` output, re-run by this seat and identical.
- `registry_rows_added` is `[]`, and nothing was created in AWS.

**TCKT_VNEXT.TO-R18-TR2 R18TR2-AC3J MET.** The diff 5cb98dbac4 changes `meeting_request.primary` alone, verified as the meeting block by the
parent's context, and adds one route entry. No permission or resource is added, and nothing was planned or applied.

**TCKT_VNEXT.TO-R18-TR3 R18TR3-AC3J MET.**
- One statement, two actions, three resources, one per firm. Each ARN is built with `format()` from the `opal_name` module's bucket output,
  with no wildcard on the firm.
- No bucket policy or CORS is written, and nothing was planned or applied.
- Live: the role policy reads exactly that.
- Note: the two environment templates are literal copies of the builder record, not derived from it. They equal `ATTACH_ADDRESS.json` byte
  for byte today, so they meet "the builder's output" by value.

**TCKT_VNEXT.TO-R18-P1 R18P1-AC4J PARTIAL.**
- MET in the source (12c164a0):
  - the type opens a form reading "Who the meeting is with (required)", "Purpose (required)" and "Proposed time 1 (required)";
  - the coordinator's two actions read "Confirm this time" and "Propose these times";
  - the outcome line sits on the ticket's own row;
  - the filed notice says only "Meeting request <id> filed.", and no word claims a mail or invite.
- The served page was driven in a browser (PART 1 found and filed the form and pressed Confirm), but no one has read the rendered page:
  no screenshot exists, and the portal law's render-and-read is owed.
- The controls render for EVERY internal viewer, not only the coordinator. A non-coordinator is refused in words (403 sentence), so the
  actions are unmistakable, but they are offered to people who cannot use them.

**TCKT_VNEXT.TO-R18-P2 R18P2-AC4J PARTIAL.**
- MET in the source (c05e3dda): the firm choice; the file "Trade request form"; the placeholder named as one ("This is the placeholder
  form; the final trade request form replaces it. ... No trade is sent."); "Submit trade request"; an Open form control on the ticket's row.
- No staff person can file it on DEV: the type is hidden by Andrew's word of 2026-10-13, and PART 2 is held.
- The page was never rendered or exercised.

## FWD-11

**FWD-11 PARTIAL on DEV; NOT REALIZED.** The DONE WHEN has four acts on DEV, then the same on PROD by 2026-10-24.
- **Filed, the OPEN ticket routed to the coordinator, the coordinator confirmed on the dashboard:** EXERCISED (TCK-20261016-9d7654eb,
  19:24:01Z-19:24:07Z).
- **"The filer sees the outcome on the same ticket": NOT EXERCISED.** The only read after the confirm is the run process's ConsistentRead of
  the item, never the filer's view. The source shows `MeetingOutcomeLine` on the row only while `status !== 'completed'`, so once a ticket
  completes the filer no longer reads the outcome there (FWD-11 ACCEPT: "the filer reads confirmed or rescheduled on the ticket").
- The coordinator was a synthetic stand-in (the CTO's ruling (b)).
- The PROD leg is not run.

## FWD-10

**FWD-10 not graded: NOT RUN** (PART 2 is held for the CTO's 5174 handover). The packet says so and claims nothing.

```json
[
  {
    "id": "TCKT_VNEXT-D2-C-S1",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "3.0.0_SA_CVO~DELL2",
    "surfaced_at": "2026-10-16T21:05Z",
    "one_line": "Rounds 18-19 L9: eleven judgment criteria graded (nine MET, two PARTIAL: the two portal candidates, render unread); FWD-11 PARTIAL on DEV, not realized (the filer's read of the outcome not exercised; PROD not run).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): a judgment criterion is graded by the CVO and never self-graded.",
    "world_is": "Graded on the source and tests at de2fdb4a4f (466 passed, run by this seat), the Terraform diffs, the portal candidates 12c164a0 and c05e3dda, and the live function, routing and role policy read at ~21:0xZ.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R18_R19.md @e424376b67 (msg 9855)",
        "de2fdb4a4f:infra/aws/lambda/ticket_center/lambda_function.py; pytest tests/ at de2fdb4a4f: 466 passed",
        "commits 5cb98dbac4, 43715c1c3b, 9855742266, 8957fed16b, 028ee030b9; portal 12c164a0, c05e3dda",
        "org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r18_run/R18_RUN_PART1_TRACE.json"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade row."
  },
  {
    "id": "TCKT_VNEXT-D2-C-S2",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "3.0.0_SA_CVO~DELL2",
    "surfaced_at": "2026-10-16T21:05Z",
    "one_line": "The attachment open route fences on requester.firm but builds the bucket and prefix from answers.firm; safe only because create forces the two equal.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "R18L2-AC3J: a firm can only open from its own prefix; the open route applies the same fence as the ticket read.",
    "world_is": "attachment_open_ticket (L2116-2127 at de2fdb4a4f) tests _in_profile_scope on requester.firm and presigns on answers.firm's bucket and prefix. Today they cannot differ: create sets req_firm = answers.firm and refuses a differing requester_firm (L1421-1423), and no UpdateExpression in the file writes answers or requester. A future path that edits either member, or a type whose requester firm is not answers.firm, would open one firm's file to another firm's scope.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "de2fdb4a4f:infra/aws/lambda/ticket_center/lambda_function.py L1421-1423, L2116-2127; UpdateExpression census L1643, L1702, L1779, L1883, L1947, L1991, L2054"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Latent, not live: no path today makes the two differ. Recorded for the round-N analysis; the cheap close is to fence and presign on the same member."
  }
]
```

-- `3.0.0_SA_CVO~DELL2`
