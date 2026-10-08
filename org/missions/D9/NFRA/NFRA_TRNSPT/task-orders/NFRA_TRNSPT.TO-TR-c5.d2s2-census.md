# TO NFRA_TRNSPT.TO-TR-c5 -- D2-S2: the deployed mail route against HEAD, and a counts-only listing census tool

<to_id>NFRA_TRNSPT.TO-TR-c5</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~2</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>transcripts</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-c-5` (`decompositions/NFRA_TRNSPT_DECOMP_R5.md`) |
**outcome_ref:** FWD-7 (residue row NFRA_TRNSPT-D2-S2) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-c-5` (CTO round-4 analysis @856673477a, section 2, E2): "D2-S2: truncation or classification, read against the running gateway.
First compare the deployed gateway bytes for `mail_route.py` ... with HEAD. Then take ONE counts-only listing of the 2026-08 span
per sender." The live listing is the ISSUER's run after your merge; you build and test the tool it runs.

**Background (row NFRA_TRNSPT-D2-S2).** The scheduled fire of 2026-10-07T23:30Z listed `listed=100` messages over a 60-day window and
did not land the 2026-08-11 message. 100 = 4 x 25. In SOURCE both ends page to the end: the Lambda-side client
`data/transcripts/scripts/outlook/gateway_mail.py:147-169` (`list_rows`: cuts the window into spans of at most 31 days and follows
`next_page_token` until absent) and the gateway route `infra/aws/ec2/opal-gateway/app/mail_route.py` (its listing and `nextLink`
handling; see around lines 280-380). So a truncation can only come from a RUNNING gateway that differs from that source, or from Graph
returning no `nextLink`. Otherwise the message was classified out.

**Build:**
1. **The deployed-vs-HEAD record**, `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/R5_MAIL_ROUTE_DEPLOYED_VS_HEAD.md`.
   - Read the opal-gateway entry's `deployed_commit` in `infra/aws/ec2/EC2_MANIFEST.json` at HEAD (at the cut it read
     `aa75078e1b72a28219e6148d3ec8e9bf705ea111`, line 503; the analysis's `240ac2fe5a` is an older release -- use what the
     manifest says when you run).
   - Compare `git show <deployed_commit>:infra/aws/ec2/opal-gateway/app/mail_route.py` with `git show HEAD:infra/aws/ec2/opal-gateway/app/mail_route.py`
     (byte compare, e.g. both through `sha256sum`, or `git diff <deployed_commit> HEAD -- infra/aws/ec2/opal-gateway/app/mail_route.py`).
     In Git Bash prefix a `git show <ref>:<path>` with `MSYS_NO_PATHCONV=1`, never add `2>/dev/null` to it, and treat an EMPTY output
     as an error, not as "same".
   - POSITIVE CONTROL: run the same comparison for `mail_route.py` between HEAD and a commit you know CHANGED it (the parent of the
     newest commit in `git log --format=%h -- infra/aws/ec2/opal-gateway/app/mail_route.py`); it must read DIFFERS. This proves the
     instrument can see a difference.
   - The record carries, each on its own line, exactly:
     ```
     MAIL_ROUTE: deployed@<full deployed_commit> SAME-AS-HEAD|DIFFERS SOURCE: infra/aws/ec2/EC2_MANIFEST.json:<line of deployed_commit>
     POSITIVE_CONTROL: <control commit> DIFFERS
     ```
     then a short paragraph: the two sha256 values, the diff's changed-line count if DIFFERS (and whether a changed line touches paging or
     `nextLink`), and the same comparison for the Lambda's BUILD INPUT copy
     `infra/aws/lambda/transcripts-pull/dist/pkg/data/transcripts/scripts/outlook/gateway_mail.py` against
     `data/transcripts/scripts/outlook/gateway_mail.py` at HEAD (a plain file byte compare), stated SAME or DIFFERS.
2. **The census tool**, `data/transcripts/scripts/outlook/listing_census.py`:
   `census(client, senders, start, end, has_attachment=True) -> dict`. For each sender (by its INDEX in the list, `sender#1`,
   `sender#2`, ... -- never the address) and each span from `gateway_mail._spans(start, end, gateway_mail.LIST_WINDOW_DAYS)`, call
   `client.list_page(...)` (the existing `HxMailClient.list_page`, unchanged) and follow `next_page_token` to its end, recording per span:
   `{"sender": "sender#<n>", "span": [<iso lo>, <iso hi>], "listed": <rows>, "pages": <pages>, "page_counts": [..],
   "next_token_seen": <bool, any page returned a token>, "last_page_had_token": <bool>}`, plus a total per sender. Same loop guards as
   `list_rows` (a repeated token or more than `MAX_LIST_PAGES` pages raises). Output carries COUNTS AND DATES ONLY: no message id,
   subject, address, name or body. A `main()` with `--senders-env <ENV NAME>` (the sender list read from that environment variable,
   whitespace/comma split), `--start`, `--end` (ISO dates) and `--out <file>`; the bearer via `gateway_mail.read_bearer()`. Do NOT run
   `main()` live.
3. **Its test**, `data/transcripts/scripts/tests/test_listing_census.py`, with a stub `fetch` injected into `HxMailClient` (the pattern
   of `data/transcripts/scripts/tests/test_gateway_mail.py`): at least a two-page span counted as `pages=2` with the right `listed`;
   a 60-day window cut into two spans; a repeated token raising; and `test_no_sender_address_in_output` -- a planted sender address
   (e.g. `planted.sender@example.com`) never appears in the JSON-serialised result.

### ACCEPTANCE

<criterion id="TR5-c5-AC1" cell_refs="TR-c-5"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R5_CHECKS/r5_checks.py c5-record</invocation><expect>R5-C5-RECORD-OK</expect></criterion>
`TR5-c5-AC1` -- the record names the deployed commit, a verdict, a manifest source line that exists, and the positive-control line.

<criterion id="TR5-c5-AC2" cell_refs="TR-c-5"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R5_CHECKS/r5_checks.py c5-census</invocation><expect>R5-C5-CENSUS-OK</expect></criterion>
`TR5-c5-AC2` -- the census test file passes, including the planted-address test.

<expected_criteria>TR5-c5-AC1, TR5-c5-AC2</expected_criteria>

Dry-run at the base (CLOUD 1e02ea542a): AC1 `R5-C5-RECORD-FAIL absent`, AC2 `R5-C5-CENSUS-FAIL absent` -- FAIL as expected. Whether the
verdict is right is read by the issuer at the drain against its own `git show`.

### AMENDMENT 1 (issuer 2.0.0_SA_COO~T2, 2026-10-08) -- AC1's deployed bytes are resolved by CONTENT

The manifest's `deployed_commit` `aa75078e1b...` is a local release branch that never reached this repository or origin, so
`git show` of it is empty (your row NFRA_TRNSPT-D2-W2-S1). The issuer read the deployed bytes from the release artifact instead:
`org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R5_DEPLOYED_ARTIFACT_READ.md` (artifact ETag `58f375cd...`, 509420 bytes,
git-ref `aa75078e1b...`; its `app/mail_route.py` sha256 `c7bf6ad9...` equals HEAD's; 0 diff lines; positive control 19 lines).
Write the MAIL_ROUTE line from that read: `MAIL_ROUTE: deployed@aa75078e1b72a28219e6148d3ec8e9bf705ea111 SAME-AS-HEAD SOURCE:
infra/aws/ec2/EC2_MANIFEST.json:503`, and add one paragraph saying the verdict is the issuer's content read of the release artifact
(cite the file above), not a `git show`. Keep your POSITIVE_CONTROL line. Make no AWS call. Then re-run AC1 and AC2 and flip only if
both PASS. The issuer files the resolution of row D2-W2-S1.

## BOUNDS

- **Grant.** `listing_census.py`, its test, your deliverables folder, this order's file and the investigation file. Nothing else is
  written; `gateway_mail.py` and the gateway are READ only.
- **LOCAL.** No gateway call, no HTTP request, no AWS call, no Secrets Manager read. Tests use a stub `fetch` only.
- Run `python -m pytest data/transcripts/scripts/tests/test_listing_census.py -q -p no:cacheprovider` from the worktree root.
- **Refusal clause.** If the manifest has no opal-gateway `deployed_commit`, or `git show` of it fails, write `MAIL_ROUTE: deployed@<what
  you found> DIFFERS SOURCE: <path:line>` only if it truly differs; otherwise leave AC1 failing, and file a surprise row (id
  `NFRA_TRNSPT-W2-S<k>`, next unused across every document under `surprise-channel/`) naming what is missing. Never write SAME on an
  empty read.

<paths>
data/transcripts/scripts/outlook/listing_census.py
data/transcripts/scripts/tests/test_listing_census.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ and
never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R5.md</decomp_doc> (round 5), cell `TR-c-5`.
<owned_cells>TR-c-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR5-c5-AC1, TR5-c5-AC2. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/NFRA_TRNSPT.TO-TR-c5.d2s2-census.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR5-c5-AC1,TR5-c5-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the MAIL_ROUTE and POSITIVE_CONTROL lines, the two sha256 values, the gateway_mail build-input verdict, the census output shape,
the two check lines, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read of git bytes and an offline tool.
comp-iam: DECLARED-NOT-APPLICABLE for the worker; the issuer's live run reads secret gateway/mail/bearer by name (dell2 read unmeasured).
comp-adversary: RUN -- traps are an empty `git show` read as SAME (MSYS mangle) and a manifest hash taken from the analysis rather than HEAD; the face names both and AC1 requires a DIFFERS positive control.
lane: two new files under data/transcripts/scripts/, deliverables, the investigation file.
</preflight>

Source: CTO round-4 analysis @856673477a section 2 E2; decomposition round 5 cell TR-c-5 and issuer rulings 4-5.
