# COO never-widen half -- NFRA_CTLPLN workstream INBOUND (macro COMM), round 8: the drafting contract (code-only deploy, one targeted apply of `module.ldo_001`)

**Author:** `2.0.0_SA_COO~C`, 2026-10-09 ~22:3xZ. **Read at:** `box/laptop` `bde0c0fc90`, round 8's merge of cell CT-i-14.
Root: `infra/aws/terraform/transcripts/`. **Counterpart owed:** a CTO half.

**Authority:**
- Andrew-direct 2026-10-09 ~21:xxZ, the agent's talk posted into the End of Day post. Recorded verbatim in
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_21xxZ_TEAMS_TEXT_OPS_AGENT_TALK_LEAKED_INTO_EOD_POST.md`
  @74fc19c25f.
- Rulings A (msg 108133) and B (msg 108137).
- This act changes what can reach Teams and what is texted to Andrew, so it owes a pair, as the round-6 and round-7 deploys did.

## The act

One `safe-apply` of the root, TARGETED at exactly `module.ldo_001`, at the laptop, by `0.7.0_AE_CloudOps~CTL`, from a trunk that
contains `bde0c0fc90`. Code only.

**What is live now** (read by the issuer at 22:3xZ):
- the deploy COMM_ASSIST CA-d-2 at pinned build `2ad98c2e3a`, applied 18:33Z 2026-10-09 by `0.7.0_AE_CloudOps~CA`;
- ledger entry `20261009T1801Z_comm-assist-r12-mail-deploy-2`, CLOSED;
- both functions at `CodeSha256` `op92gM7rlR9956tienAEp2Dscy2zhdARV3WEbYDFp/M=`;
- `MAIL_BEARER_SECRET` set, and policy `v4`.

## What becomes live -- the packaged-path diff `2ad98c2e3a..bde0c0fc90`: 3 files, +297/-36; no `.tf` file changed

| file | what it changes live |
|---|---|
| `assist.py` | `DRAFT_CONTRACT_RULE` plus a STRICT `parse_draft`. The model answers every Teams-bound drafting call with ONE JSON object `{post, to_andrew, question, applied, not_applied}`. Only `post` can reach Teams. Prose around the JSON, a missing `post`, or `question` together with `post` is refused. One `draft_contract` log line per parse (counts, never text). `draft_chat_reply` uses it. |
| `tenant.py` | The End of Day first draft and redraft, the chat draft and redraft, and the job completion draft all use the contract. Outcomes: **refused** (nothing offered; Andrew gets one line naming the problem; the open draft is kept); **question** (texted with the tag; no new version; the open draft, its version and its alarm unchanged); **unchanged** (`to_andrew` texted; the open draft kept); **post** (offered as today, plus one text carrying `to_andrew` and any not-applied notes). The link-restore runs on `post` only, and never over a preamble. `st["dialog"]` keeps the last 8 turns per tag and is passed to the next drafting call. |
| `post_format.py` | `addresses_andrew` and two lists. `check_post` (the End of Day post) refuses the full list of phrases addressed to Andrew. The chat and job paths refuse only the five drafting-exchange phrases (issuer AMENDMENT 1; the CTO was told at 22:17Z). |

**Evidence on the trunk, from the issuer's own re-runs in the worker's tree at `4577df3916`:**
- `DRAFT-CONTRACT ok=True arms=9/9 base_leaked=True` -- the base posts today's leak shape and the new code refuses it;
- `AGENT-SUITE ok=True` (127 pytest, mail-reply 9/9);
- `INBOUND-VOICE-TEST ok=True cases=14/14`;
- `SILENT-PATHS ok=True arms=9/9`;
- `INBOUND-CLOUD-TEST ok=True cases=9/9`;
- proof instance VALID.

Every model call and send in them is faked.

## What changes for Andrew

- Nothing the agent says to him can be posted to Teams.
- When his notes cannot be applied, he is told why by text, and the draft he had stays open.
- He may get a question instead of a redraft, and a short "what changed" text beside a new version.
- No new vendor, no new kind of content sent to the model, no send to Teams without his `1`, no schedule, no alarm, no policy line.

## Expected plan, BOTH branches

- **A:** targeted `0 to add, 2 to change, 0 to destroy`. The changes are `module.ldo_001.aws_lambda_function.handler` and
  `.ingress[0]`, `source_code_hash` (and `last_modified`) only, decoding to the built package. Nothing outside the module, no
  policy change, and `MAIL_BEARER_SECRET` unchanged -> apply.
- **B:** anything else -> apply NOTHING, report. That covers:
  - an add, a destroy or a replacement;
  - any other argument or environment change;
  - a policy line, or an address outside the module;
  - an `init` migration prompt;
  - a packaged-path diff since `bde0c0fc90` under `teams_chat/`, `ldo.py`, `handlers.py` or `daily_reports/eod/`;
  - live `CodeSha256` not equal to `op92gM7r...` at BEFORE (someone deployed since);
  - inside the End of Day window 20:00Z-21:45Z;
  - an End of Day event in flight.

## The risk this half names: the live model and the contract

The one thing no test here reads is whether the live model (kimi-k3) answers in the contract.
- **If it does not:** every draft is REFUSED and Andrew gets a one-line refusal instead of a draft. That is loud, never a wrong
  post; it is a lost draft, not a leak.
- **Within the first hour after the apply, the issuer reads** the `draft_contract` log lines by outcome (counts only).
- **If refusals dominate:** the rollback below is taken the same hour, and the contract wording goes back to a cell.

## Rollback

Code only: the live package is downloaded before the act (its hash equal to `op92gM7r...`), copied over
`dist/teams-chat-assist.zip`, and the same targeted apply is run.

State: `st["dialog"]` is a new key that the old code ignores; no migration; the live `cursor.json` is saved anyway. A text
already sent is not recalled.

## Conditions

1. Branch A is read immediately before the apply, with the lock taken. Never untargeted.
2. **BEFORE:**
   - both `CodeSha256` and `LastModified` saved;
   - `MAIL_BEARER_SECRET` present, by name only, never its value;
   - the live zip and the live `cursor.json` saved with hashes;
   - a NEVER-2 entry opened, naming both function families.
3. **AFTER, live:**
   - both `CodeSha256` equal the built package's;
   - a targeted re-plan reads no changes;
   - within 5 minutes, `ingress_poll` lines continue with no `ingress_step_failed`. `channel_poll failed=1` is pre-existing.
4. The applier makes no invocation, sends no test event or text, and reads no message content.
5. The exercise belongs to the issuer: the first real drafting call's `draft_contract` line, and the first End of Day redraft.
   Until then the status is APPLIED, not EXERCISED.

**SIGNED** -- `2.0.0_SA_COO~C`
