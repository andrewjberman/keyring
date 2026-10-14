# TO COMM_ASSIST.TO-CA-j-13 -- round 18 CA-j-13: the dell2 reader folder gains two sources, mentions.json and mail_log.json (FWD-13, reader half)

<to_id>COMM_ASSIST.TO-CA-j-13</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~25</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>RDRSRC</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-j-13` (`decompositions/COMM_ASSIST_DECOMP.round18.md`, AMENDMENT 8) | **outcome_ref:** FWD-13 |
**depends_on:** none (PRD v0.10 ADMITTED; the CTO ruling on call 608c, msg 109140)

---

## WORKER FACE

### THE CELL

A job on dell2 runs `data/transcripts/scripts/muse_reader/refresh.py` every 15 minutes and writes a folder (`drafts.json`, `open_calls.json`, `eod_today.json`, `sprint_today.json`, `INDEX.json`, `README.txt`) that Andrew's operator agent muse reads. Muse must now alert Andrew to each new channel @mention and each new considered mail (PRD FWD-13). The assistant (cell CA-j-12, a different worker, different files) will keep two metadata-only lists in its state table rows: `state["mentions"]` and `state["mail_log"]`. You make the reader publish them as two NEW sources in the same envelope as the others. You touch only the reader (and one new test); you do not touch the assistant.

### THE CONTRACT (fixed by the issuer; the check pins every key)

In `refresh.py`:
- `SOURCES` becomes `("open_calls", "drafts", "eod_today", "sprint_today", "mentions", "mail_log")`; `make_readers(now_dt)` returns a reader for each of the six.
- The two new readers scan the state table the way `read_drafts` does (the `scan_table` helper; rows with `sk` "state"; skip `pk` starting with `#index#`) and read the lists inside each row's `data` JSON:
  - `mentions` <- `state["mentions"]` of EVERY object that has one. Each entry has seven keys: `id`, `team`, `channel`, `from`, `snippet`, `mentioned_at`, `seen_at`. Entries whose `seen_at` is older than 7 days before `now_dt` are dropped. Items are merged across objects, NEWEST `mentioned_at` FIRST. Each item is the entry's seven keys plus `age_minutes` and `age_from` (`"mentioned_at"`) from the existing `with_age`.
  - `mail_log` <- `state["mail_log"]` of every object that has one. Each entry has seven keys: `seq`, `tag`, `considered_at`, `from`, `domain`, `firm`, `subject`. Entries whose `considered_at` is older than 7 days are dropped. Merged, NEWEST `considered_at` FIRST. Each item is the entry's seven keys plus `object_id` (the row's `pk`) plus `age_minutes` and `age_from` (`"considered_at"`).
  - If NO row anywhere carries the list at all, the reader raises `Absent` (status `absent`, `items` null, never an empty list: nothing has been recorded yet). If rows carry the list but every entry is expired, the result is `ok` with an empty list (it was true at the time stated). A scan failure makes THAT source `unreadable` with the error, as every other source does; one source failing never stops the others (the existing `refresh()` already does this).
- Everything reaches the files through the existing `refresh()` and so the existing `scrub()` (an address or a key-shaped value never lands). Do not weaken or bypass it.
- `README` (the text written to `README.txt`) names `mentions.json` and `mail_log.json`, says what each row is (one per item, newest first), says that `absent` means nothing has been recorded yet and is never an empty list, and that the lists hold metadata only (no message body).
- Nothing else changes: the four existing sources, `INDEX.json`'s shape (it now lists six), the exit codes, the CLI. Standard library only. No AWS call in tests (inject `aws_json`). No non-ASCII.

### BUILD, IN THIS ORDER

1. Add the two sources and their readers to `refresh.py`; extend the README text.
2. Add `data/transcripts/scripts/tests/test_muse_reader_records.py` (a plain script or pytest, your choice, runnable offline by injecting a fake `aws_json` that returns scan pages): both sources ok with merged newest-first items and the exact keys, the 7-day drop, absent versus an empty-but-ok list, an unreadable scan isolated to the two sources, and scrub on write.
3. Re-run the existing reader controls named below and confirm they still pass.

### RULES

- Edit nothing but the files in `<paths>`. Code and a test; NOT deployed here (dell2 picks it up through the box pass in a later cell).
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAj13-AC1" cell_refs="CA-j-13"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_k2_reader.py"</invocation><expect>K2-READER ok=True arms=7 of 7</expect></criterion>
`CAj13-AC1` -- the issuer's check (read it; do not edit it): both sources are in `SOURCES` and in `make_readers`; the mentions merge newest first with exactly the nine keys and the right ages, an expired entry dropped; the mail log likewise with `object_id`; no recorded list anywhere is `absent` with null items; a scan failure leaves both `unreadable` while the other sources stay ok; the two files and a six-source `INDEX.json` are written; an address and a key in a snippet never reach the file; the README names both files. It prints 0 of 7 at the base.

<criterion id="CAj13-AC2" cell_refs="CA-j-13"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i1_ages.py"</invocation><expect>I1-AGES ok=True arms=5 of 5</expect></criterion>
`CAj13-AC2` -- the bound, a control that PASSES at the base and must still pass: the reader's ages on the existing sources.

<criterion id="CAj13-AC3" cell_refs="CA-j-13"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r16/checks/check_h1_failure_shape.py"</invocation><expect>H1-FAILURE-SHAPE ok=True</expect></criterion>
`CAj13-AC3` -- the bound, a control that PASSES at the base and must still pass: a failed source reads unreadable with null items and its last good time, never an empty list.
</proof_of_spec>

<expected_criteria>CAj13-AC1,CAj13-AC2,CAj13-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 250`. Commit the code and test FIRST. Then write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~25/COMM_ASSIST.TO-CA-j-13.reader-publishes-mentions-and-mail-log.proof_of_spec.json`, modelled on `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~23/COMM_ASSIST.TO-CA-j-9.ingress-mark-four-hour-freshness.proof_of_spec.json`, recording each invocation EXACTLY as the criterion text (no `timeout` prefix) and pinning each artifact row to the commit that carried it (a row left as pending-this-commit goes INVALID the moment a later commit lands). Flip `<status>` to `complete` only when all three pass. Validate by running the WORKTREE'S OWN `.tools/proof-of-spec-check.py` from inside the worktree AFTER your last commit: `python .tools/proof-of-spec-check.py <instance> CAj13-AC1,CAj13-AC2,CAj13-AC3`, and read the LAST line: it must be `VALID (rc=0)` at the final head. Your final report names the changed lines, the new test and its result, and the three check lines. Your surprise rows are `COMM_ASSIST-W25-S<k>`; append only to the investigation file and keep its existing line endings; `surfaced_at` = `date -u +%FT%TZ` at filing. Commit with `.tools/safe-commit.sh` as your serial.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round18.md</decomp_doc>
<owned_cells>CA-j-13</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/muse_reader/refresh.py
data/transcripts/scripts/tests/test_muse_reader_records.py
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-j-13.reader-publishes-mentions-and-mail-log.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~25/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing; the dell2 job's 15-minute task is unchanged and picks the code up through the box pass in a later cell.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves and no AWS call is made here; the new readers use the same DynamoDB scan the drafts reader already performs (read-only, the same table), so the dell2 identity needs nothing new.
comp-adversary: RUN -- an empty list shown where the source was never written (refused: AC1 `absent-not-empty`); one failing source hiding the rest (refused: AC1 `unreadable-isolated`; AC3); a secret, key or address in a snippet reaching the folder (refused: AC1 `scrub-on-write`); a row older than 7 days shown as new (refused: AC1 expiry in both ok arms); the existing four sources disturbed (refused: AC2 and AC3). BLIND: the live table holds no mention or mail-log entry until the assistant deploy (CA-j-14), so a real row is read only after cells CA-j-14 and CA-j-15; the real scan cost on the live table (606 items, one more scan per new source per run) is measured live, not here.
naming: the two file names are muse's requested names (`mentions.json`, `mail_log.json`) beside the existing sources; no resource name is created (CLAUDE.md rule 30 non-application).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base: CAj13-AC1 base: FAIL as expected (0 of 7). CAj13-AC2 base: PASS as expected (control, 5 of 5). CAj13-AC3 base: PASS as expected (control). AC1 green arm: PASS as expected (7 of 7) against a scratch reference (the reader patched in a throwaway worktree, removed); a negative control with no 7-day expiry reads 4 of 7; the two controls read the same against the patched reader (5 of 5 and ok=True).
Source: CTO ruling on call 608c (`RULING_20261014_124xZ_COMM_ASSIST_608C_FWD13_TWO_SCRUBBED_RECORDS.md`, msg 109140); PRD v0.10 FWD-13; muse's requested shape (Gmail thread, 2026-10-14 13:16Z: `mentions.json`, `mail_log.json`, flat rows, stable ids, timestamps, ages); `refresh.py` `SOURCES`, `make_readers`, `with_age`, `scrub`.
