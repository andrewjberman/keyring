# TO COMM_ASSIST.TO-CA-k-1 -- round 19 CA-k-1: the mail object keeps a LIST of open mail drafts keyed by seq; a newer considered mail adds and never overwrites

<to_id>COMM_ASSIST.TO-CA-k-1</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~27</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-k-1` (`decompositions/COMM_ASSIST_DECOMP.round19.md`) | **outcome_ref:** FWD-4, FWD-13 |
**depends_on:** none (CTO round-18 analysis ruling 2, msg 109267; PRD v0.10 ADMITTED)

---

## WORKER FACE

### THE CELL

Every considered mail lands on ONE object (the mail object, `kind == "mail"`), and `mail_requests.on_mail_messages` writes the new draft to `ctx.state["pending"]`, so a second considered mail REPLACES the first draft: Andrew can no longer answer the older one. You make the object keep a LIST of open mail drafts. A newer considered mail ADDS an entry; it never overwrites an older one. Four places read the single `pending` today and must each learn the list: the mail reply path, the signed-answer path, the natural-language "what is waiting" list, and the dell2 reader. This cell is code and tests only; a later cell deploys it.

### THE CONTRACT (fixed by the issuer; the issuer's check pins every point)

Your whole interface is the header of `org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r19/checks/check_l1_pending.py` plus the five points below. READ that file first (it is in your worktree at HEAD); do not edit it.

1. **The list.** `ctx.state["pending_list"]` is a list of every open mail draft on the mail object, ordered by `texted_at` (oldest first). Each entry is the same dict shape as a `pending` (its own `seq`, `tag`, `version`, `draft`, `texted_at`, `mail`, ...). `ctx.state["pending"]` stays and ALWAYS holds the NEWEST open entry (the one texted last), or `None` when none is open, so every existing reader, text and test keeps working. Created lazily: an object that has only a legacy `pending` and no `pending_list` is read as a one-entry list.
2. **The writer** (`mail_requests.on_mail_messages`). Each considered mail APPENDS its entry; the existing `draft_seq` counter, tags, texts and `mail_log` row are unchanged. On every write drop entries whose `texted_at` is more than 7 days before `ctx.now()` and keep the newest 20 (use `folder_records.prune`). A new mail's tag never repeats the tag of an entry still open (probe past open tags the way `mail_tag` already probes past other objects' tags). Considering the SAME mail id again replaces that mail's own entry, never another's.
3. **Replies** (`tenant.on_sms_reply` for `kind == "mail"`, and `mail_requests.on_mail_reply`, `_redraft`). The entry is the one whose tag equals the payload `tag` (no tag: the newest). Approve (1), drop (0), notes (redraft) and `#dev` act on THAT entry only. The stale-version check (`unseen`) is per entry. A redraft re-texts its entry, so it becomes the newest and `pending` points at it. After any removal `pending` is the newest remaining entry or `None`. An unknown tag changes nothing and says "Nothing waiting under #<tag>." exactly as today.
4. **Signed answers and the open list.** `tenant.on_muse_reply` checks an answer's seq against `pending`; it must resolve the entry by tag so an answer for an older open mail is accepted (and one for a closed or unknown entry is refused as today). `tenant.open_items` (the "what is waiting" list) must list every open draft, not only the newest.
5. **The reader** (`data/transcripts/scripts/muse_reader/refresh.py`, the drafts source). ONE row per open mail draft (from `pending_list`; the legacy `pending` when there is no list), each with its own `seq`, so two open mails on one object give two rows with distinct seq. The row keys are otherwise unchanged. A chat or End of Day object still gives its single row.

Standard library only. No AWS, no network. No non-ASCII. Do not change what is texted to Andrew, the tags, `draft_seq`, `mail_log`, the mention record, the ingress mark, or any existing key.

### BUILD, IN THIS ORDER

1. `mail_requests.py`: the writer (point 2) and the reply helpers (point 3). Put the small list helpers (find by tag, set newest, remove) in `mail_requests.py` so the other two files import them.
2. `tenant.py`: `on_sms_reply`'s mail branch, `on_muse_reply`, `open_items` (points 3 and 4).
3. `refresh.py`: the drafts rows (point 5).
4. Tests: add arms for the new behaviour to `data/transcripts/scripts/tests/test_inbound_mail_reply.py` (reply to the older tag, drop, redraft, `#dev`, an unknown tag) and `data/transcripts/scripts/tests/test_inbound_mail_draft.py` (two mails one minute apart keep both drafts, the 7-day and 20-entry pruning, a legacy object). Run every test file under `data/transcripts/scripts/tests` that touches mail, replies or the reader (the scripts run as `python <file>`; the rest under pytest) and keep them passing. `test_inbound_mail.py` fails 4 of its 15 cases AT THE BASE (stale party-registry cases; cell CA-k-3 repairs them): it must read exactly `cases=11/15` before and after, and you do not edit it.

### RULES

- Edit nothing but the files in `<paths>`. Code and tests; NOT deployed here.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAk1-AC1" cell_refs="CA-k-1"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r19/checks/check_l1_pending.py"</invocation><expect>L1-PENDING ok=True arms=15 of 15</expect></criterion>
`CAk1-AC1` -- the issuer's check (read it; do not edit it): two mails one minute apart both keep their drafts; a reply to the older tag acts on the older draft only; a drop, a redraft and `#dev` each touch one entry; the stale check is per entry; the 7-day and 20-entry pruning; a single mail behaves as before; a legacy object still replies; a signed answer binds to its tagged entry; the open list shows every draft; the reader emits one row per open draft. It prints 1 of 15 at the base.

<criterion id="CAk1-AC2" cell_refs="CA-k-1"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i2_regression.py"</invocation><expect>I2-REGRESSION ok=True</expect></criterion>
`CAk1-AC2` -- the bound, a control that PASSES at the base (64 passed) and must still pass: the assistant's flow tests.

<criterion id="CAk1-AC3" cell_refs="CA-k-1"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_k2_reader.py"</invocation><expect>K2-READER ok=True arms=7 of 7</expect></criterion>
`CAk1-AC3` -- the bound, a control that PASSES at the base: the reader's six sources with the contracted keys.
</proof_of_spec>

<expected_criteria>CAk1-AC1,CAk1-AC2,CAk1-AC3</expected_criteria>

Each invocation runs from the worktree root, by that RELATIVE path, under `timeout 250`: the issuer's checks import repository code from the current directory's checkout, so running one by an absolute path to the shared tree would test the trunk and not your work. Commit the code and tests FIRST. Then write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~27/COMM_ASSIST.TO-CA-k-1.mail-object-keeps-a-list-of-open-drafts.proof_of_spec.json`, modelled on `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~24/COMM_ASSIST.TO-CA-j-12.assistant-keeps-mention-and-mail-records.proof_of_spec.json`, recording each invocation EXACTLY as the criterion text (no `timeout` prefix) and pinning each artifact row to the commit that carried it (a row left as pending-this-commit goes INVALID the moment a later commit lands). Flip `<status>` to `complete` only when all three pass. Validate by running the WORKTREE'S OWN `.tools/proof-of-spec-check.py` from inside the worktree AFTER your last commit: `python .tools/proof-of-spec-check.py <instance> CAk1-AC1,CAk1-AC2,CAk1-AC3`, and read the LAST line: it must be `VALID (rc=0)` at the final head. Your final report names the changed lines, the helper interface, every existing test you changed, the tests you added, and the passed/failed count of every test file you ran. Your surprise rows are `COMM_ASSIST-W27-S<k>`; append only to the investigation file and keep its existing line endings; `surfaced_at` = `date -u +%FT%TZ` at filing. Commit with `.tools/safe-commit.sh` as your serial.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round19.md</decomp_doc>
<owned_cells>CA-k-1</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/mail_requests.py
data/transcripts/scripts/teams_chat/tenant.py
data/transcripts/scripts/muse_reader/refresh.py
data/transcripts/scripts/tests/test_inbound_mail_reply.py
data/transcripts/scripts/tests/test_inbound_mail_draft.py
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-k-1.mail-object-keeps-a-list-of-open-drafts.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~27/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves and no AWS call is made; the deploy is a later cell (CA-k-4) with its own pair.
comp-adversary: RUN -- a newer mail overwriting an older draft (refused: AC1 `two_mails_both_kept`, and the overwrite negative control reads 3 of 15); a reply acting on the newest draft whatever tag Andrew names (refused: AC1 `approve_older_leaves_newer`, `dev_one_removes_only_it`, `muse_answer_binds_to_the_tagged_entry`; that negative control reads 8 of 15); an older draft invisible to the "what is waiting" list or refused as a signed answer (refused: AC1 `open_items_lists_each_draft`, `muse_answer_binds_to_the_tagged_entry`); a reader row collision when two mails share the object (refused: AC1 `reader_rows`: distinct seq); a list that grows without end (refused: AC1 pruning arm, 7 days and 20); a legacy object with only `pending` breaking (refused: AC1 legacy arm); the existing flows and the reader moving (refused: AC2 and AC3). BLIND: the live state table is not read here; the served behaviour is read only after the deploy (CA-k-4), by a served-code probe on a `probe:` object.
naming: no name is created (CLAUDE.md rule 30 non-application).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base: CAk1-AC1 base: FAIL as expected (1 of 15: only the unknown-tag control holds). CAk1-AC2 base: PASS as expected (control, 64 passed). CAk1-AC3 base: PASS as expected (control, 7 of 7). AC1 green arm: PASS as expected (15 of 15) against a scratch reference in a throwaway worktree (since removed); the scratch reference also kept `check_i11_seq`, `check_i1_ages` and `check_h1_failure_shape` green.
Source: CTO round-18 analysis ruling 2 (`ledger/ROUND_ANALYSIS.round18.md` @5e4395ae5c, msg 109267); the fork's measurements of the four readers of `pending` (`tenant.on_sms_reply`, `tenant.on_muse_reply`, `tenant.open_items`, `refresh.py` drafts rows); `mail_requests.on_mail_messages` (the single `pending` write at line 287).
