# SOC2_MSLOGS decomposition -- ROUND 2 (2026-10-17, issuer 2.0.0_SA_COO~S1)

Cut on the CTO's round-1 analysis `org/missions/D12/SOC2/SOC2_MSLOGS/ledger/ROUND_ANALYSIS.round1.md` @843819d1ab (msg 7370), whose section 3 is this round's
ENRICHMENT LIST (seven items), plus the CVO's four graduated remediations `surprise-channel/remediations/REMEDIATION_v1.md` @94d3a6ce41 (owner this seat).
PRD v0.2 is unchanged (`prd/SOC2_MSLOGS_PRD.md`). The round-1 decomposition `SOC2_MSLOGS_DECOMP.md` stays the record of round 1; its contracts (COLLECTOR v3, DOOR v3,
SILVER v3) bind unless this file says otherwise.

FWD-1 is NOT MET and waits only on Andrew's recognition of the enriched read (analysis section 1); no cell of this round waits on it.

**Andrew-direct words carried into the faces that touch them (verbatim):**
- "we need to have a mechanism with the globgrph lambda where it can do a print out to the desktop on this machine." (2026-10-16 ~23:40Z; CTO ruling: the CALLER'S read client writes the Desktop file; the door cannot push.)
- "use the biggest lambad" (2026-10-17 ~00:55Z; the door runs at 10240 MB until the streaming derive is proven on the busiest day, then the memory comes down in one release.)
- "the premise is not for workflows, its for identifying common patterns and establishing if a suspicious one appears." / "Silver is just formatted bronze in parquet for query."

## The rectangle (round 2)

| cell | enrichment item | surfaces | outcome | status | placement | risk | worker_class | depends on (observed completion) |
|---|---|---|---|---|---|---|---|---|
| `SM-s-2` | 2: silver `client_ip` also reads Exchange's `ClientIPAddress` | silver builder and its test | FWD-2, FWD-3 ("from where") | NOT-EVALUATED | dell1 | WORLD (path floor) | worker | -- |
| `SM-d-2` | 3: a memory-bounded (streaming) derive in the door | door handler `derive_silver`, silver builder, their tests | FWD-1, FWD-7 | NOT-EVALUATED | dell1 | WORLD (path floor) | worker | SM-s-2 (same files; one queue) |
| `SM-n-2` | 5 + remediation D1-W2-S3: the door's bronze prefixes come from the naming builder | door handler, door build script, tests | (rule 30) | NOT-EVALUATED | dell1 | WORLD (path floor) | worker | SM-d-2 (same file; one queue) |
| `SM-k-2` | 1: the read client (paging, detail, Desktop print-out, MFA session, derive) and the retirement of the two round-1 stopgaps | `door_client.py` (new), `read_timeline.py`, their tests, the two COO stopgap files (deleted) | FWD-1 (second half), FWD-2, FWD-9 | NOT-EVALUATED | dell1 | LOCAL | worker | -- |
| `SM-c-2` | 4: the collector's async retry set to 0 | `collector.tf` | FWD-7 | NOT-EVALUATED | dell1 | WORLD (path floor) | worker-light | -- |
| `SM-t-2` | 6 + remediations D1-W1-S1, D1-W5-S1, D1-W7-S1: text | README, RUNBOOK, `main.tf` comment | (record accuracy) | NOT-EVALUATED | dell1 | WORLD (path floor) | worker-light | -- |
| `SM-e-2` | 7: FWD-2 starts: the `exposure` read (door module + client) | `exposure.py` (new), `read_exposure.py` (new), their tests | FWD-2 | NOT-EVALUATED | dell1 | WORLD (path floor) | worker | -- (builds to the EXPOSURE CONTRACT below; the door hookup is the issuer's at the merge) |
| `SM-r-2` | release: build the two zips, one `safe-apply`, re-derive the 8 days, the streaming proof on the busiest day, memory down, exposure read live | the live account | FWD-1, FWD-2, FWD-7 | NOT-EVALUATED | dell1 | WORLD | seat (`0.7.0_AE_CloudOps~SOC21`) | all seven cells merged and the hookup landed |

**Chains (M = 5; fan-out 5 of 5, cap 8).**
- A = SM-s-2 -> SM-d-2 -> SM-n-2 (slot ~9): all three write `handler.py` and/or `silver_builder.py`, so one worker's queue.
- B = SM-k-2 (slot ~10). C = SM-c-2 (slot ~11). D = SM-t-2 (slot ~12). E = SM-e-2 (slot ~13).
- SM-r-2 joins by observed completion (it applies the merged tree).

**Write sets (disjoint across chains).**
- A: `infra/aws/lambda/globgrph-trino-access/{silver_builder.py,handler.py,build.sh,names.py (new),tests/test_silver_builder.py,tests/test_handler.py}`.
- B: `data/m365_metadata/scripts/silver/{door_client.py (new),read_timeline.py}`, `data/m365_metadata/scripts/tests/{test_door_client.py (new),test_read_timeline.py}`, and the deletion of `org/tier1_exec/2.0.0_SA_COO~S1/deliverables/{derive_days.py,read_timeline_to_desktop.ps1}`.
- C: `infra/aws/terraform/trino/collector.tf`.
- D: `data/m365_metadata/README.md`, `data/m365_metadata/scripts/app/RUNBOOK.md`, `infra/aws/terraform/trino/main.tf` (comment lines only).
- E: `infra/aws/lambda/globgrph-trino-access/{exposure.py (new),tests/test_exposure.py (new)}`, `data/m365_metadata/scripts/silver/read_exposure.py` (new), `data/m365_metadata/scripts/tests/test_read_exposure.py` (new).
- Hookups at the merge, by the issuer in ONE commit: `handler.py` (`exposure` op: `ALIAS_OPS["member"]`, `KNOWN_OPS`, the dispatch branch, `_exposure`), `tests/test_handler.py` (one test).
  `build.sh` is chain A's (it packages every top-level `*.py` of the door directory), so `exposure.py` rides the zip with no further hookup.

**Rulings by the issuer.**
1. **The read client pages by time.** The door's detail answer ends at 1000 rows or 5,000,000 bytes and says `truncated`; it has no cursor. The client's next page starts AT the last
   row's time (inclusive) and drops rows already held by `record_id`; a page whose rows all share one second raises, never loops.
2. **The Desktop file holds the answer the screen would show, nothing else.** It is written by the caller's client from the user's shell Desktop folder (never typed), refused inside
   the repository, UTF-8, and the screen then shows the path only. `--json` writes the merged door answer instead. It is never committed, uploaded or sent (CTO ruling 2026-10-16 ~23:4xZ).
3. **The MFA session lives in the client.** `--profile` names a member's AWS profile, `--mfa-code` trades a fresh code for a short session on that identity's only MFA device
   (`--mfa-serial` when it has several); the keys live in the process and are never printed. This retires `read_timeline_to_desktop.ps1`; `derive_dates` retires `derive_days.py`.
4. **Streaming derive.** `derive_silver` for date D reads the bronze objects of D and D+1 one at a time and holds no more than a bounded working set whatever the day's size; its
   output is identical, row for row and byte for byte of every column, to `build(records, only_date=D)` over the same records in listing order. `build` stays as the reference.
   The answer stays `{"ok": true, "rows": n}`, `n` the records read. Any temporary file is under the function's temp directory and removed before the return.
5. **`exposure` is a member read, over silver `raw_json`, with no content.** It reports what the audit records say and says plainly what they do not record.
6. **Memory comes down in the release, not in a cell.** `access.tf` is untouched by workers; the release seat lowers `memory_size` after the streaming proof on the busiest of the 8 days.
7. **The Terraform cell carries `terraform validate` on a scratch copy** (analysis section 2; `s1_check_r2.py tfvalidate`), as a standing criterion of every Terraform-touching cell.

**THE CONTRACTS this round touches (fixed here).**

*EXPOSURE CONTRACT v1.* Door module `exposure.py`: `compute(rows, account) -> {"opened": [...], "left": [...], "unrecorded": [...]}`. `rows` are the silver reader's detail rows
(`time`, `feed`, `operation`, `client_ip`, `item_name`, `user_id`, `record_id`, `result_status`, `raw_json` a JSON string); rows whose `user_id` is not the lower-cased `account` are ignored;
every list is ascending by `time`, ties in input order.
- `opened`: a row whose `operation` is one of `MailItemsAccessed`, `FileAccessed`, `FileDownloaded`, `FilePreviewed`, `FileSyncDownloadedFull`, `FileSyncDownloadedPartial`. Entry keys:
  `time`, `operation`, `feed`, `item_name`, `client_ip`, `record_id`.
- `left` (everything that went to someone outside the account's own domain; the domain is the part after `@` of `account`, compared case-insensitively). Entry keys: `time`, `kind`, `recipient`,
  `operation`, `item_name`, `record_id`. Kinds:
  - `share_invitation`: operation `SharingInvitationCreated`; `recipient` is the raw record's `TargetUserOrGroupName`; included when it is an address outside the domain or `TargetUserOrGroupType` is `Guest`.
  - `anonymous_link`: operation `AnonymousLinkCreated`; `recipient` is the fixed text `anyone with the link`; always included.
  - `forward_rule`: operations `New-InboxRule`, `Set-InboxRule`, `UpdateInboxRules`; the raw record's `Parameters` list of `{Name, Value}`; for each parameter named `ForwardTo`, `ForwardAsAttachmentTo` or
    `RedirectTo`, split `Value` on `;`, `,` and whitespace, strip a leading `smtp:` (any case), and make one entry per address outside the domain.
  - `mailbox_forward`: operation `Set-Mailbox`; the same rule over the parameters `ForwardingSmtpAddress` and `ForwardingAddress`.
- `unrecorded`: a list of `{"category", "reason"}`. Always `mail_recipients` (reason: the audit feed does not say who a sent mail went to). Also `mail_opened` when no row of the window has operation
  `MailItemsAccessed` (reason: no MailItemsAccessed record in this window, so mail opened is not recorded for this account or licence, or none was opened).
- No entry carries `raw_json`, the raw record or `ObjectId`.
Door op (the issuer's hookup): `exposure` on the member alias, `{op, account, start, end}`, window at most 31 days as `timeline`, answer `{"ok": true, "opened", "left", "unrecorded", "truncated"}`,
each list capped at 5000 entries with `truncated` true when a list was cut.
Client `read_exposure.py`: `fetch(invoker, account, start, end) -> reply` (the payload is exactly `{"op":"exposure","account","start","end"}`; account validated as in `read_timeline.fetch`; a reply whose `ok` is not true raises
`RuntimeError`); `render(reply) -> str` with three sections headed `OPENED`, `LEFT`, `NOT RECORDED`, one line per entry (Eastern time first), the word `none` under an empty section, and a final
`TRUNCATED` line when the reply says so; `main(argv, invoker=None, out=None, desktop=None, repo_root=None)` with `--account --start --end --profile --mfa-code --mfa-serial --desktop`, building its invoker
with `door_client.build_invoker` (imported inside `main` only) and its Desktop file with `door_client.write_desktop`.

*DOOR CLIENT CONTRACT v1.* `data/m365_metadata/scripts/silver/door_client.py`:
`build_invoker(profile=None, mfa_code=None, mfa_serial=None, boto3_module=None) -> invoker(payload) -> dict`; `desktop_dir(environ=None, platform=None, known_folder=None) -> str`;
`write_desktop(text, account, start, desktop=None, repo_root=None) -> str`; `derive_dates(invoker, dates) -> [(date, "ok rows=N" | "REFUSED (reason)")]`.

**The cards at Andrew (his acts; the issuer cards each when its step is reached).**
1. FWD-1 recognition: he runs the enriched read (now the Desktop option of the new client) against his own account for one day he remembers, and says in one line whether it shows who did what, from where and when.
2. FWD-2 recognition, once the exposure read is live: he chooses a window and reads the list.

**Not in round 2:** `session_span`, `persistence`, `baseline`, `outside_baseline`, gold, the residual statement, the auditor answer, the FWD-3/FWD-4 drills.

## Rule 24 record (the cell set is a schema)

- **MECE over a declared domain.** Domain: the seven items of the CTO's ENRICHMENT LIST plus the four remediations. By subtraction: item 1 = SM-k-2; item 2 = SM-s-2 (the code) and SM-r-2 (the 8-day re-derive);
  item 3 = SM-d-2 (the code) and SM-r-2 (the memory down); item 4 = SM-c-2; item 5 = SM-n-2 (also closes D1-W2-S3); item 6 = SM-t-2 (also closes D1-W1-S1, D1-W5-S1, D1-W7-S1); item 7 = SM-e-2 and the issuer's
  hookup; the Desktop option = SM-k-2. Remainder: none. The CTO's "not cut, noted" line (the named AWS profile on dell1) is carried by SM-k-2's `--profile` and SM-t-2's README usage line.
- **Same grain.** Workers build in the repository and apply nothing; only SM-r-2 touches the account.
- **Intent coherence.** `s` silver, `d` derive, `n` naming, `k` client, `c` collector, `t` text, `e` exposure, `r` release.
- **State coherence.** The five workers call nothing live. The Terraform cells validate on a scratch copy and apply nothing.

## Battery (round 2)

- `comp-schedule`: RUN at SM-r-2 (the hourly rule read back; the retry config read back from the live function). BLIND: a fire proves no new content landed.
- `comp-iam`: DECLARED-NOT-APPLICABLE for the workers (no IAM change in any cell); the release reads the door role policy unchanged.
- `comp-adversary`: DECLARED-NOT-APPLICABLE for the workers; findings inlined where they touch a cell: the CVO's round-1 negative arms (write-once bronze, recollect already-stored) stand and no cell touches them.
- The naming gate (`.tools/naming-gate.py`) was run on the door handler at the base: it REFUSES 5 lines, of which 2 name `audit_records`; the other 3 name state and gold and silver prefixes that no registry module places
  (a HOLE the gate itself assigns to `1.0.0_SA_CTO`). SM-n-2 closes the 2 and reports the 3.
