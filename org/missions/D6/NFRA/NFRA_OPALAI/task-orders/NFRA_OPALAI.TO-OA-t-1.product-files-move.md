# NFRA_OPALAI task order -- `OA-t-1` -- HOP 1: the Analyst's product files move into opal_ai, slice-first

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-t-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OA-t-1` (round 1, decomposition s.2/s.3)

The Opal Analyst (today the seat `0.0.3_BG_BBGTerminal`) becomes a product in `opal_ai`, run later by a separate Windows
account, `Opal_Agent`, that has NO workspace, NO AWS credential and NO agent broker. This cell MOVES its product files.
Code moves and is never copied: each file lands in `opal_ai` and its parent copy is removed on your branch, and every
consumer is re-pointed in the same change.

**In the nested repo `opal_ai` (at `<worktree>/opal_ai`):**
1. The slice-first layout: `README.md` (names the three slices: `opal/` = the Opal implementation, all V1 code;
   `template/` and `clients/` = reserved, a README only, no code), `opal/README.md`, `template/README.md`,
   `clients/README.md`, `docs/README.md`.
2. `opal/agent/refs/` receives the 7 top-level files of `org/tier0_utility/0.0.3_BG_BBGTerminal/refs/`, byte-unchanged,
   EXCEPT `PORTAL_RETRIEVAL.md`. **`refs/census/` does NOT move** (CTO ruling I-4: it is the index's evidence, read by
   `workflows/atom_decomposition/emit_catalog_v02.py`, and moves with the catalog in a later project); opal_ai carries none of it. That file is re-written so the runtime data mechanism is the gateway MCP
   tool `opal_asker_query(chat_id, message_id, key, params)`: the gateway identifies the asker from the Teams message
   itself and scopes the answer to them. `portal_lookup.py` is described as the development-side instrument (it needs
   AWS, which the runtime lacks). **`REQUEST_CATALOG.md` is NOT edited** (C7).
3. `opal/agent/tools/portal_lookup.py`, byte-unchanged.
4. `opal/agent/skills/bbg-teams-assist/SKILL.md` from `.claude/skills/bbg-teams-assist/SKILL.md`. Edit only (a) the
   step-0 arm line and the "Pairs with" line so the watch is `opal/agent/teams_watch/teams-watch.py`; (b) the seat-scope
   lines: the skill now belongs to the runtime agent `Opal_Agent`, not a serial; (c) `refs/` and `tools/` paths so they
   resolve under `opal/agent/`.
5. `opal/agent/prompt.md` from the seat's `prompt.md`:
   - The **`## Hard lines`** section stays byte-for-byte.
   - Rewrite the identity binding and On-launch sections for the runtime. KEEP the whoami identity acceptance gate on
     `opal-gateway-bbg`. REMOVE `register_agent`, `/watcher`, the Secrets Manager read and every other workspace launch
     act. The runtime has no broker (C5), no AWS (C4), and its login re-mint is the operator's.
   - Name the agent `Opal_Agent`.
   - ADD a section headed exactly `## RUNTIME MECHANISM MAP`: a markdown table with one row per APPROVED catalog row
     (`| 1 | ...` through `| 8 | ...`). Each row names the mechanism `Opal_Agent` can reach: `opal_asker_query`
     where the gateway catalog `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` holds a key that serves the
     row (read it, and name the key or channel). Otherwise the row carries the plain, quotable reason
     `not available from the Analyst yet -- ask Andrew` (PRD C11: the cutover drops nothing silently). **Row 7
     (Bloomberg view) takes that decline**: its server launches from the workspace and is the first enrichment. Row 5
     (news DynamoDB) is served only if the catalog holds a key for it; otherwise it too takes the decline.

**In the parent (your worktree):** remove `org/tier0_utility/0.0.3_BG_BBGTerminal/prompt.md`, its 7 top-level `refs/` files
(`refs/census/` STAYS, byte-equal to the cut),
its `tools/portal_lookup.py`, and `.claude/skills/bbg-teams-assist/SKILL.md`. Re-point every code/config consumer. In
`infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` re-point exactly ONE line, `:1241` `guardrails_ref`, to
`opal_ai/opal/agent/refs/BLOOMBERG_GUARDRAILS.md`; its 30 `census_ref` lines stay byte-unchanged. The file is committed
with CRLF line endings: preserve every CR byte, so the diff against the cut is one line removed and one added. The seat's `README.md`, `threads/`, `logs/` and `deliverables/` STAY (state, C5).
**Not yours:** `.tools/hooks/bg-concierge-gate.sh` and its test (OA-t-3), `.claude/skills/teams-assist/**` (OA-t-4),
`.claude/settings.json` and `.tools/ajb.ps1` (the issuer's cutover hookups).

## 2. BOUNDS

1. **`opal_ai` is a nested repository** at `<worktree>/opal_ai`, on branch `<your worktree branch>-opal_ai`, off opal_ai
   `DEV` `90ca424fc7`. It has no hooks yet. Commit your nested files there with `git -C opal_ai commit --author
   "0.9.0_WK_NFRA_OPALAI~1 <0.9.0_WK_NFRA_OPALAI~1@opal.agent>" -F <msgfile> -- <nested paths>`, where the msgfile is
   written with the Write tool (the portal-cell precedent). Commit parent files with `safe-commit.sh` as usual.
2. The parent-side removals merge in the round's CUTOVER window, not at your drain; commit them on your branch anyway.
3. Standing: no push, no install, no vendor call, no AWS. REFUSE a criterion you cannot meet as written, and report the
   refusal with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
opal_ai/README.md
opal_ai/opal/README.md
opal_ai/template/README.md
opal_ai/clients/README.md
opal_ai/docs/README.md
opal_ai/opal/agent/prompt.md
opal_ai/opal/agent/refs/
opal_ai/opal/agent/tools/portal_lookup.py
opal_ai/opal/agent/skills/bbg-teams-assist/SKILL.md
org/tier0_utility/0.0.3_BG_BBGTerminal/prompt.md
org/tier0_utility/0.0.3_BG_BBGTerminal/refs/
org/tier0_utility/0.0.3_BG_BBGTerminal/tools/portal_lookup.py
.claude/skills/bbg-teams-assist/SKILL.md
infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~1/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_OPALAI-Z-W1-S<k>`.

## 4. PROOF OF SPEC (literal; run from your worktree root, after BOTH repos are committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-t-1"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/t1.AC1.sh; echo "exit=$?"</invocation><expect>present 15 of 15; content-equal 7 of 7; census files in opal_ai: 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-t-1"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/t1.AC2.sh; echo "exit=$?"</invocation><expect>moved paths absent at HEAD: 10 of 10; census files kept at HEAD: 4 of 4; catalog lines added/removed vs cut: 1 1 (guardrails_ref re-pointed=yes); code/config files still referencing moved paths: 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OA-t-1"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/t1.AC3.sh; echo "exit=$?"</invocation><expect>hard-lines byte-equal=yes; launch acts named: cut=N>0 runtime=0; whoami mentions>0; map rows 8 of 8, resolved 8 of 8; row 7 declined=1 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~1/NFRA_OPALAI.TO-OA-t-1.product-files-move.proof_of_spec.json`. Report once: what you changed and where, the commit hashes in BOTH repos, the row-by-row mechanism map you wrote, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** hop 1 + S1 + C11's map. Parent-side merge held to the cutover window (decomp s.8). The map's
declined rows feed the cutover record.

<status>pending</status>
<round>1</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>

<status>superseded -- CLOSED for round 1 by 2.0.0_SA_COO~O, 2026-09-28T13:0xZ, on Andrew's direction to close out the rounds so the CVO can slug. HELD, never graded: this cell's parent-side removals merge only in the round's CUTOVER window (decomp s.8), and that window opens on Andrew's gates G-ACCT, G-AUTH and G-PUSH (carded by 1.0.0_SA_CTO), none of which has landed. Holding it open would deadlock round 1's L10 on an Andrew act (the refuser counts open orders PER PROJECT). NOTHING IS RE-GRADED BY THIS CLOSE. The cell RE-CUTS as round 2's first cutover cell, unchanged, once the gates land. Was: pending.</status>
