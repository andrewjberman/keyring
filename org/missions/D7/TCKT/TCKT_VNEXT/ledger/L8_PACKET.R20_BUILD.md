# TCKT_VNEXT round 20 -- L8 PACKET, part 1 (the two build cells; the rendered read is part 2)

**Compiled by** `2.0.0_SA_COO~V2`, 2026-10-16 ~23:4xZ, on dell2. **For** `3.0.0_SA_CVO~DELL2` at L9, as a FILE. Not the L10 slug. Commits named are LOCAL on `box/dell2` unless a line says otherwise; the workspace push state is not read. Portal DEV is read by ls-remote.
**Authority:** the CTO's rounds 18-19 analysis (rulings 2, 4, 5). **Decomposition:** `decompositions/TCKT_VNEXT_DECOMP_R20.md`. **Issuance:** `f893f927bb` (fanout 2 of 2 chains, cap 4).
**This packet grades only the two BUILD judgments.** The third judgment of the round, `R20RV-AC1J` (the rendered read of the filer's ticket after the confirm and after completion, and the rendered meeting form), is NOT in this packet: `TO-R20-RV` is staged and has not run (it waits for the CTO's 5174 handover, which waits for Andrew's smoke). **The round is not closeable, and FWD-11 is NOT REALIZED, until `R20RV-AC1J` is graded** (the CTO: "shot 5 decides FWD-11").

## 1. What was built and where it is

| cell | order | what | where it is |
|---|---|---|---|
| `R20-pt-1` | `TO-R20-PT` (worker `0.9.0_WK_TCKT_VNEXT~50`) | the Ticket Center board shows the meeting outcome line for a meeting ticket that is not completed OR carries a `meeting` outcome (a completed one with none shows nothing); the coordinator's two actions render only to a viewer whose email is in the ticket's `routing.primary` (trimmed, case-insensitive), never on a completed ticket | portal `origin/DEV` `6cdd0bfd917b` (merge of `cand/dell2/tckt-meeting-outcome-visibility` head `8e4f0885`, row `dell2-20261016T224727Z-330e` APPROVED by the CTO, waiver XA-20261016T222303Z-5b3b; ls-remote read); drained into the workspace at `59281c016c` |
| `R20-lm-2` | `TO-R20-LM` (worker `0.9.0_WK_TCKT_VNEXT~49`) | `attachment_open_ticket` fences and presigns on ONE member: a ticket whose `requester.firm` differs from `answers.firm` is refused with the same 404 body as "carries no attachment", and the presign is built from the fenced member | source drained at `44933b266b`; RELEASED live by `TO-R20-REL` (TV2): the live package source equals the tree byte for byte (the issuer's read, `CodeSha256` `iRxJZYp6...cy3RM=`, 23:28:26Z); TV2's result file and the ledger close were not in at this writing |

## 2. For L9 -- the judgments (graded on the artifacts, never self-graded)

| judgment | what bears on it | evidence to read |
|---|---|---|
| `R20PT-AC4J` a completed meeting ticket that carries an outcome still shows it; a completed ticket with none shows nothing; the coordinator's two actions render only for a viewer in `routing.primary`; every other viewer sees the line without a control; no call, route, colour or principal was added | the diff of the one feature commit (4 files under `src/pages/TicketCenter/`: `MeetingRequestParts.tsx` +`showsMeetingOutcome` and `viewerIsCoordinator`, `TicketCenter.tsx` the board mount, the new test file with the ten named tests, and ONE existing fixture: the `useAuth` mock in `meeting-request.test.tsx` gained `user: { email: COORDINATOR }`, no assertion changed) | `git -C portal diff fcbf2bce 8e4f0885`; `deliverables/0.9.0_WK_TCKT_VNEXT~50/R20_PT_RECORD.json` and `render_markup.txt` (DOM text of the confirmed line); mechanical results the issuer re-ran: `r20_checks.py pt-outcome` `R20-PT-OK pass=10`, `portal-tsc` `R20-TSC-OK`, the mutant `MUTANT-FIRES` with the file restored; the worker's drain check `bun test src/pages/TicketCenter` 206 of 206 |
| `R20LM-AC3J` the open route fences and presigns on ONE member, refuses a ticket whose two firms differ with the same body as a ticket with no attachment, and nothing else in the function changed | the diff is one hunk: one line out, six in (a two-line comment, `req_firm`, the equality test, `firm = req_firm`) | `git diff 430b378b8f 44933b266b -- infra/aws/lambda/ticket_center/lambda_function.py`; `deliverables/0.9.0_WK_TCKT_VNEXT~49/R20_LM_RECORD.json`; the five tests (the issuer re-ran: `5 passed`) and the mutant (`MUTANT-FIRES`); the live package carries the same hunk and nothing else (the issuer diffed the live member against the tree before the release: exactly that hunk); the CTO's pre-apply count read by TV2: 0 of 19 attachment tickets have differing firms (33 scanned) |

## 3. Limits (what this packet cannot show)

- **Nothing in this packet was RENDERED.** `R20PT-AC4J` is graded on the diff, the tests and the DOM text of one markup; the rendered page and the three filer/bystander/coordinator views are part 2. A pass here is not a pass of FWD-11.
- The worker's folder run of the ticket-service tests is not clean in a worker worktree (11 failed, 8 errors; the same counts on the unchanged base; none names `attachment_open_ticket`): rows `TCKT_VNEXT-D2-W49-S1` and `S2` (INERT, observations).
- The release's result file, `r20_rel_check.py` printing `REL-OK` and the ledger close are TV2's and are not read at this writing; the issuer re-runs the check when they exist and amends this packet if it differs.
- The workspace commits above are LOCAL. The portal DEV merge is read on origin.
