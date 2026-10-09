# NFRA_CTLPLN decomposition -- WORKSTREAM INBOUND, round 8: the Teams agent talks to Andrew and publishes only the post -- one drafting contract, a question outcome, a per-tag dialog, and a backstop (issuer 2.0.0_SA_COO~C; cut 2026-10-09 ~21:5xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

Round 7 is drained: its one order, `NFRA_CTLPLN.TO-CT-i-13`, is complete. This workstream is macro COMM's (D9), driven under
NFRA_CTLPLN until a COMM tree row exists. The issuer moves from `2.0.0_SA_COO~R` to `2.0.0_SA_COO~C`, on the CTO's ruling A
("2.0.0_SA_COO~C issues"). This round has one issuer.

**Cut on:** Andrew-direct 2026-10-09 ~21:xxZ, a DEFECT. The record is
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_21xxZ_TEAMS_TEXT_OPS_AGENT_TALK_LEAKED_INTO_EOD_POST.md`
@74fc19c25f; his words are in it verbatim. It holds two rulings:
- **Ruling A** (containment): `1.0.0_SA_CTO` msg 108133.
- **Ruling B** (the conversational contract): adopted from `docs/briefs/teams-text-ops-conversational-agent-brief-20261009.md`
  @64c19e1b4c. The CTO said "ONE cell carries rulings A and B" (msg 108137, @74fc19c25f).

PRD v0.22 is ADMITTED (`prd-signoff.py status`: ratified-text SIGNED current, brief SIGNED). The carrier is FWD-20.

**Measured at the base (`box/laptop` 34ef44c26f):**

- **The leak path.** `tenant._eod_draft` (`tenant.py:271-290`) appends "Your previous draft / Andrew's notes / Rewrite the post
  following his notes" on a redraft. It takes the model's WHOLE output as the draft.
  - When the model answers Andrew above the post, line 1 is prose, and `check_post` reports only "first line is not the sprint
    link". The link-restore branch then PREPENDS the link line over that prose and offers it.
  - The answer to Andrew therefore passes every check, under a valid link line. That is the shape of today's E1009 post.
- **The same pattern elsewhere.** `assist.draft_chat_reply` (`assist.py:516-530`) and `tenant._completion_draft`
  (`tenant.py:629-640`) use the same notes-then-rewrite pattern. Both texts reach Teams on his `1`.
- **The checks are shape-only.** `post_format.check_post` (`post_format.py:115-131`) tests shape only: the link line, the Sprint
  line, two bullets, no serial or hash, no dash. The chat path has no content check.
- **A JSON contract already exists at the routing step.** `INTENT_SYSTEM` (`assist.py:877`) parses JSON `actions` + `reply`.
  The drafting step has no channel to Andrew. That missing channel is the cause of the leak.
- **No dialog memory.** No state keeps the SMS dialog per tag. `state.recent` holds Teams messages only.
- **Baselines:**
  - `check_agent_suites.py`: `AGENT-SUITE ok=True` (127 passed, mail-reply 9/9);
  - `test_inbound_voice.py`: `INBOUND-VOICE-TEST ok=True cases=14/14`;
  - `test_inbound_silent_paths.py`: `SILENT-PATHS ok=True arms=9/9`.

**Rule 24.**
- **Domain:** every model call whose output can reach Teams, read from `tenant.py` and `assist.py`, with a denominator of four
  calls: EOD first draft, EOD redraft, chat draft and redraft, and job completion draft and redraft.
- **Not in the domain:** `CONTEXT_SYSTEM`, `JOB_BRIEF_SYSTEM`, `INTENT_SYSTEM` and `CONFIRM_SYSTEM`. Their outputs are state,
  a brief to an engineer, routing JSON and a yes/no, so none reaches Teams.
- **One cell:** the four calls share one parser, one prompt rule and one backstop, in two files that admit no disjoint split.
  So they are ONE cell.

| cell | what | serves | risk | chain, slot |
|---|---|---|---|---|
| `CT-i-14` | every Teams-bound drafting call returns the one JSON contract; only `post` can reach Teams; non-JSON is refused; a `question` or an unapplied note leaves the open draft unchanged; `state.dialog` keeps the last 8 turns per tag; `check_post` and the chat path refuse text addressed to Andrew; the 2026-10-09 redraft replays clean | FWD-20 | LOCAL | A, `~56` |

`fanout: 1 of 1 chains, cap 8`.

**Battery:**
- `comp-schedule`: DECLARED-NOT-APPLICABLE.
- `comp-iam`: DECLARED-NOT-APPLICABLE (no policy and no AWS call in the cell).
- `comp-adversary`: RUN on the order.

**After the drain:** a code-only deploy of `module.ldo_001` under its own pair. Then the first real End of Day redraft, read
from the logs as `draft_contract` lines, is the live exercise.
