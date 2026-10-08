# TO NFRA_CTLPLN.TO-CT-i-13 -- workstream INBOUND round 7 CT-i-13: the Teams agent never goes silent -- every draft is texted, every approved reply is posted, a refused End of Day draft says why, chat cursors stay bounded

<to_id>NFRA_CTLPLN.TO-CT-i-13</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~41</issued_to>
<issued_by>2.0.0_SA_COO~R</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>INBOUND</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-i-13` (`decompositions/NFRA_CTLPLN_DECOMP.inbound7.md`) | **outcome_ref:** FWD-20 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CT-i-13`. Andrew's Teams assistant (a Lambda on the "LDO" object runtime; code in `data/transcripts/scripts/teams_chat/`, runtime
`infra/aws/terraform/modules/ldo/runtime/ldo.py`) texts him drafts of replies to his Teams chats, posts a reply to Teams when
he answers `1`, and drafts his End of Day post. Three defects, all measured, all silent:

1. **Run-once key collision (the main one).** Outside effects run through `ctx.once(key, fn)` (`ldo.py:382-396`): if a record
   for `key` exists on this object, `fn` is NOT run and the recorded result is returned. Records live 7 days. In `tenant.py`:
   - `offer()` texts a draft under `"offer:%s:v%d" % (tag, version)`. The chat's tag is fixed (`chat_tag`, kept in state), and
     `on_chat_messages` starts a NEW draft at `version` 1 whenever no draft is pending (after he answered by hand, after a
     send or a drop). So a chat's second draft within 7 days hits the first draft's record: the event returns `texted`, and
     NO text is sent. Measured on the live logs today: 14 chat outcomes `texted`/`updated`, 0 texts sent.
   - the send of an approved chat reply to Teams, `ctx.once("send:%s:v%d" % (tag, version), ...)` (~line 394), has the same
     shape: his second approved reply in a chat within a week may never post.
   - `mail_requests.py` (~line 213): `ctx.once("offer:%s:v1" % tag, ...)` for a mail item: same shape if a tag is reused.
   - End of Day keys use a per-day tag (`E1008`) and job keys live on a per-job object: not affected; leave them.
2. **A refused End of Day draft fails silently.** `_eod_draft()` (~line 237) raises `RuntimeError("End of Day draft refused:
   ...")` when `post_format.check_post()` (`daily_reports/eod/post_format.py`) finds problems. The event then fails, the queue
   retries it hourly, 3 times, then dead-letters it, and Andrew hears nothing. Measured: today at 20:22Z his redraft request
   was acknowledged ("redrafting E1008") and then refused with "first line is not the sprint link". Callers: `on_eod_ready`,
   `on_eod_updated`, and the redraft branch of `on_sms_reply` (~line 412).
3. **Chat cursors are never pruned.** `poll_chats()` (rewritten in round 6: cursor v2 `{"v": 2, "chats": {...}, "floor", ...}`,
   `LAG_MARGIN_S`) reads the chat list down to the oldest stored cursor, so the read deepens as quiet chats accumulate.

### BUILD, IN THIS ORDER

1. **Unique keys.** Give every chat draft a draft number that never repeats on its object: a counter in the chat's state
   (for example `st["draft_seq"]`), incremented when a NEW draft starts (version 1), carried in the pending dict, and put in the
   `offer` and `send` keys: `"offer:%s:%d:v%d" % (tag, seq, version)` and the same for `send`. A pending draft created before
   this change (no `seq` in it) keeps its old key, so a deploy never re-texts a draft he already has. Do the same for the mail
   item's `offer` key in `mail_requests.py`. Change no End of Day or job key. Search both files for every `ctx.once(` and say
   in your report, key by key, why each is or is not affected.
2. **End of Day refusals.** In `_eod_draft()`: when the only problem is the missing link line, restore it deterministically
   (put the sprint link line first, in the form `post_format.user_prompt` asks the model for -- read it), then check again.
   When problems remain, do NOT raise. Return a refusal the callers handle:
   - first draft (`on_eod_ready`) and page update (`on_eod_updated`): text Andrew ONE line through `tell()` or
     `text_andrew()` (once per day and reason) naming the day and the problem; keep any open draft unchanged; return
     `"refused"`;
   - redraft (`on_sms_reply`): text him `#<tag> redraft refused: <problems>. The previous draft is still open: reply 1 to
     post it or send new notes.`; keep the previous pending draft and its version unchanged; return `"redraft-refused"`.
   The message text names the problems from `check_post`, never the draft's content.
3. **Cursor pruning.** In `poll_chats()`: drop a chat's cursor when it is older than `floor` minus `PRUNE_AFTER_S = 7 * 86400`
   (a named constant). A pruned chat that becomes active again uses `floor` as its cursor, so its new messages are still
   delivered; say so in a comment.
4. NEW `data/transcripts/scripts/tests/test_inbound_silent_paths.py` (a plain script, no network; inject fakes the way
   `data/transcripts/scripts/tests/test_teams_chat_tenant.py` does; a fake `ctx.once` that keeps records ACROSS events, like
   the runtime). Arms, each printing `ARM <name> ok=<True|False>`:
   - `second_draft`: in one chat, draft 1 is texted, he answers by hand, a new message arrives: draft 2 IS texted (two
     `send_sms` calls). **Difference control in the same arm:** the same sequence against the BASE `tenant.py` (load it with
     `git show 09ed3ed8ce:data/transcripts/scripts/teams_chat/tenant.py` into a temp module) sends only ONE text.
   - `second_send`: two approved replies in one chat within a week both reach `send_chat`.
   - `legacy_pending`: a pending draft with no `seq` (created before the change) is not re-texted by a retry.
   - `mail_second`: two mail items under a reused tag are both texted.
   - `eod_link_restored`: a model draft whose only problem is the missing link becomes a valid draft that `check_post` accepts,
     and is offered.
   - `eod_redraft_refused`: a redraft with a remaining problem returns `redraft-refused`, texts him once with the problem, and
     leaves the previous draft and version unchanged; the handler does not raise.
   - `eod_first_refused`: a first draft with a remaining problem returns `refused`, texts him once, and does not raise.
   - `prune`: a chat whose cursor is 10 days older than `floor` is dropped; a 2-day-old one is kept; a pruned chat's new message
     is delivered.
   LAST line `SILENT-PATHS ok=<True|False> arms=<passed>/<total> base_texts_second_draft=<n>`.

### RULES FOR THIS CELL

- **Nothing you run leaves this machine**: no S3, gateway, Graph, model, text or queue call. Everything is injected.
- Edit nothing but the files in `<paths>`. Do not change `ldo.py`, `post_format.py`, `assist.py` or the End of Day or job keys.
- No real message, person's, client's or firm's name in any file you write. No non-ASCII. Bake no absolute path.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTi13-AC1" cell_refs="CT-i-13"><invocation>python data/transcripts/scripts/tests/test_inbound_silent_paths.py</invocation><expect>SILENT-PATHS ok=True</expect></criterion>
`CTi13-AC1` -- the built behaviour and its difference control in one run: eight arms; the base sends one text where the new code sends two.

<criterion id="CTi13-AC2" cell_refs="CT-i-13"><invocation>python "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~R/checks/check_agent_suites.py"</invocation><expect>AGENT-SUITE ok=True</expect></criterion>
`CTi13-AC2` -- the cell's bound (the issuer's check; read it, do not edit it): the agent's seven existing pytest files (127 passed at the base) and the mail-reply script (9/9 at the base) still pass. Where an existing case asserts an old key's exact string, change that case only as far as the new key requires and name it in your report.
</proof_of_spec>

<expected_criteria>CTi13-AC1,CTi13-AC2</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~41/NFRA_CTLPLN.TO-CT-i-13.agent-never-silent.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance> CTi13-AC1,CTi13-AC2`, and flip `<status>` to `complete` only when
both criteria pass and the instance is VALID. Your surprise rows are `NFRA_CTLPLN-W41-S<k>`; append lines only to the
investigation file and keep its existing line endings.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.inbound7.md</decomp_doc>
<owned_cells>CT-i-13</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/tenant.py
data/transcripts/scripts/teams_chat/mail_requests.py
data/transcripts/scripts/tests/test_inbound_silent_paths.py
data/transcripts/scripts/tests/test_teams_chat_tenant.py
data/transcripts/scripts/tests/test_teams_chat_stale_eod.py
data/transcripts/scripts/tests/test_teams_chat_eod_republish.py
data/transcripts/scripts/tests/test_inbound_mail_reply.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing; the End of Day alarms are unchanged.
comp-iam: DECLARED-NOT-APPLICABLE -- denominator: 0 policies and 0 AWS calls in this cell; the face forbids every network call. BLIND: none claimed.
comp-adversary: RUN -- a deploy that re-texts every open draft (legacy pending keeps its old key, arm `legacy_pending`); a fix that also changes End of Day or job keys (forbidden, named key by key in the report); a refusal text that leaks a draft (problems only); a refused redraft that loses the previous draft (arm `eod_redraft_refused`); a pruned chat whose message is lost (arm `prune`); a test that passes on the base (arm `second_draft` requires the base to send one). BLIND: whether other objects of the runtime reuse keys outside these two files; the run-once records already written live are not read.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/NFRA_CTLPLN_PRD.md` v0.20 (ADMITTED), FWD-20; `1.0.0_SA_CTO` msg 107329 ruling (3); rows NFRA_CTLPLN-S33, S34.
