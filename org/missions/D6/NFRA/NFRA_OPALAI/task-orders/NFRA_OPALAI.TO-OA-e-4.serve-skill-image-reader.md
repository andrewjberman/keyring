# NFRA_OPALAI task order -- `OA-e-4` -- ROUND 2, E4: the serve skill reads pasted images, or says plainly it cannot

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-e-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~13</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the one AWS touch is AC2's read-only SSM read of two served files.
comp-adversary: DECLARED-NOT-APPLICABLE -- a skill text change; no gate moves.
EGRESS CLASS, declared: NONE (AC2's SSM read is Opal's own AWS plane, read-only).
</preflight>

## 1. THE CELL -- `OA-e-4` (round 2, decomposition section R2.1)

The Opal Analyst answers colleagues in Microsoft Teams. Its serve procedure is the skill
`opal_ai/opal/agent/skills/bbg-teams-assist/SKILL.md`. Colleagues sometimes paste a screenshot into a message; Graph
carries it as the message's `hostedContents`, and the plain text read (`read_chat_messages`) does not include it. The
gateway ALREADY SERVES a reader for it: the tool `read_chat_message_images` on the `opal-gateway-bbg` server, allowed to
the Analyst's identity (verified live at the cut). Nothing is built on the gateway.

Edit the skill so that:
1. when a message carries pasted content (an image, `hostedContents`), the serve steps call `read_chat_message_images`
   for that message and use what it returns in the answer;
2. when the reader returns nothing usable, or errors, the reply says plainly, with this exact sentence:
   `I could not read the image you pasted` -- and then asks the colleague to type the figure or question. The Analyst
   never guesses at an image it could not read (FWD-2: every message is noticed, including pasted content).

Extend the existing serve steps. Do not rewrite them: remove at most 3 existing lines, and change no other file.

## 2. BOUNDS

1. **`opal_ai` is a nested repository** at `<worktree>/opal_ai`, on its own branch off `opal_ai` `fd8ab8a57f`. Commit
   there with `git -C opal_ai commit --author "0.9.0_WK_NFRA_OPALAI~13 <0.9.0_WK_NFRA_OPALAI~13@opal.agent>" -F
   <msgfile> -- opal/agent/skills/bbg-teams-assist/SKILL.md`, the msgfile written with the Write tool.
2. Standing: no push, no install, no vendor call. REFUSE a criterion you cannot meet as written, and report the refusal
   with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
opal_ai/opal/agent/skills/bbg-teams-assist/SKILL.md
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~13/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id
`NFRA_OPALAI-Z-W13-S<k>` (next free k for W13).

## 4. PROOF OF SPEC (literal; run from your worktree root, after the nested commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-e-4"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e4.AC1.sh; echo "exit=$?"</invocation><expect>read_chat_message_images>=1; hostedContents/pasted lines>=1; decline sentence>=1 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-e-4"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e4.AC2.sh; echo "exit=$?"</invocation><expect>served tools.py def read_chat_message_images>=1; served identity_scope.py mentions>=1 (ssm status Success) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OA-e-4"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e4.AC3.sh; echo "exit=$?"</invocation><expect>files changed other than SKILL.md=0; SKILL.md lines removed<=3 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~13/NFRA_OPALAI.TO-OA-e-4.serve-skill-image-reader.proof_of_spec.json`.
Report once: the lines you added and removed, the nested commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E4 (I-5, gap A is the laptop's served reader; FWD-2). Chain D, alone. AC2 is the seam probe against
the served gateway; it is a CONTROL and passes at base. The nested branch merges into `opal_ai` DEV at the cutover window,
before G-PUSH.

SPAWN ONLY WHEN: at the cut (no precondition). Slot `~13`, nested worktree `--nested opal_ai=fd8ab8a57f`.

Dry-run at base (main tree, CLOUD `c8df03c408`; `OA_NESTED_REF=fd8ab8a57f` = the worker's nested base):
- e4.AC1 base: FAIL as expected (fd8ab8a57f: `read_chat_message_images=0; hostedContents/pasted lines=0; decline
  sentence=0`).
- e4.AC2 base: PASS as expected (control: `served tools.py def read_chat_message_images=1; served identity_scope.py
  mentions=1 (ssm status Success, command 10e2ab50-0c20-49f0-8fd3-4400621ac0b7)`).
- e4.AC3 base: PASS as expected at fd8ab8a57f (bound: 0 files, 0 lines removed); FAIL at the stale gitlink HEAD, which
  is not the worker's base.

<status>complete</status>
<round>2</round>
<slot>~13</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
