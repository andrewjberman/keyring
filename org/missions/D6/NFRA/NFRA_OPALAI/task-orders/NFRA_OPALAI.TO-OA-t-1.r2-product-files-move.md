# NFRA_OPALAI task order -- `OA-t-1` -- ROUND 2, item 0 (RE-CUT UNCHANGED): the Analyst's product files move into opal_ai, parent half

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-t-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~12</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a file move; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- a re-cut of a round-1 thread cell; rule J's judgment is the adversary read.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OA-t-1` (round 1 decomposition s.2/s.3, re-cut in round 2 section R2.1, item 0)

**The cell text, verbatim from round 1:**

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

**The state at this re-cut -- what is already done, and what is yours:**
- **The nested half is DONE.** Items 1-5 above are on `opal_ai` origin PROD `fd8ab8a57f` (the move drained at `99190d1`).
  You write NO `opal_ai` file. Your nested checkout at `<worktree>/opal_ai` is read-only for the criteria; first run
  `git -C opal_ai fetch origin` so the pin `fd8ab8a57f` resolves. AC1 and AC3 read the move AT THAT PIN, never at the
  nested HEAD, because two other round-2 cells edit two moved files (`RELAUNCH.md`, `portal_lookup.py`) after the move by
  design.
- **The parent half is YOURS**, on the current HEAD: the removals, the one catalog re-point, and every consumer re-pointed.
  Round 1's parent commits were made on a branch from before the history rewrite. NEVER merge, cherry-pick or read
  `wk-NFRA_OPALAI-1`, and never touch `C:/tmp/oa-1` or `C:/tmp/oa-3`. Redo the parent half here.
- **The catalog moved since round 1's cut** (NFRA_MCPINDEX `2c25c4c831`, `bc0cde67f0`: +61/-3 lines). The
  `guardrails_ref` line is still at `:1241` at this cut, and the file is still CRLF (1396 CR bytes in 1396 lines). AC2
  therefore reads the one-line diff against the ROUND-2 cut, not round 1's.

## 2. BOUNDS

1. You write no file under `opal_ai/`. Commit the parent half with `safe-commit.sh` as usual.
2. The parent-side removals merge in the round's CUTOVER window, not at your drain; commit them on your branch anyway.
3. Standing: no push, no install, no vendor call, no AWS. REFUSE a criterion you cannot meet as written, and report the
   refusal with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
org/tier0_utility/0.0.3_BG_BBGTerminal/prompt.md
org/tier0_utility/0.0.3_BG_BBGTerminal/refs/
org/tier0_utility/0.0.3_BG_BBGTerminal/tools/portal_lookup.py
.claude/skills/bbg-teams-assist/SKILL.md
infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~12/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Consumers AC2 finds referencing a moved path are yours to re-point. If one sits outside `<paths>`, you are refused on it:
STOP on that criterion and file a row naming the file and line.

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_OPALAI-Z-W12-S<k>`
(next free k for W12).

## 4. PROOF OF SPEC (literal; run from your worktree root, after the parent half is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-t-1"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/t1.AC1.sh; echo "exit=$?"</invocation><expect>present 15 of 15; content-equal 7 of 7; census files in opal_ai: 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-t-1"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/t1.AC2.sh; echo "exit=$?"</invocation><expect>moved paths absent at HEAD: 10 of 10; census files kept at HEAD: 4 of 4; catalog lines added/removed vs cut: 1 1 (guardrails_ref re-pointed=yes); code/config files still referencing moved paths: 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OA-t-1"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/t1.AC3.sh; echo "exit=$?"</invocation><expect>hard-lines byte-equal=yes; launch acts named: cut=N>0 runtime=0; whoami mentions>0; map rows 8 of 8, resolved 8 of 8; row 7 declined=1 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="J2" cell_refs="OA-t-1" judgment="true"/>
</proof_of_spec>

J2 is graded by `3.0.0_SA_CVO~O` at L9, never by you: record it in your instance as `UNVERIFIABLE-BY-INSTRUMENT`, with a
`status_reason` naming the CVO, and no PASS or FAIL.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~12/NFRA_OPALAI.TO-OA-t-1.r2-product-files-move.proof_of_spec.json`.
Report once: what you changed and where, the parent commit hashes, every consumer you re-pointed, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** item 0 (R-3), re-cut UNCHANGED: round 1's cell text and three criteria. The check files are round 1's,
copied to `round2/checks/`. Two are amended, each on its own header line:
- `t1.AC1` and `t1.AC3` read the nested `opal_ai` at `$OA_NESTED_PIN` (`fd8ab8a57f`), never the nested HEAD
  (decomposition R2.3).
- `t1.AC2`'s catalog diff reads against `$OA_R2_BASE`, not round 1's `$OA_BASE`. This is a second amendment, and a
  necessary one: NFRA_MCPINDEX moved the catalog +61/-3 after round 1's cut, so the round-1 read would fail a correct
  one-line re-point. The census-kept and moved-absent reads still use `$OA_BASE`; those files are unchanged since, and
  that was measured.

**J2 (rule J, the analysis's second judgment criterion).** The CVO judges the close run's reply to the close run's named
colleague (G-ASKER): do the figure, date, source and coverage match what the portal shows for that date? Graded at L9 on
the close-run artifact in `deliverables/2.0.0_SA_COO~AI/round2/`, and never self-graded.

**Dry-run at base** (main tree, CLOUD `7cb7c7f33d`, nested pin fetched):
- t1.AC1 base: PASS as expected. It is a control: the nested half landed at the pin (present 15 of 15, content-equal 7 of 7, census 0).
- t1.AC2 base: FAIL as expected. The parent half is the build: 0 of 10 moved paths absent, catalog 0 0, re-pointed=no,
  1 code/config file still referencing a moved path (the catalog itself).
- t1.AC3 base: PASS as expected. It is a control on the pinned prompt: hard lines equal, launch acts 3 to 0, map 8 of 8,
  row 7 declined.

**SPAWN ONLY WHEN:**
- Parts A-B of the switchover sitting have landed. G-ACCT: `Opal_Agent` provisioned and `verify-boundary.ps1` reads
  `BOUNDARY: DENIED-OK`. G-AUTH: the setup-token credential is set, and the gateway sign-in as Opal Bloomberg is done.
- Provision the slot with `wk-provision.sh provision NFRA_OPALAI 12 --path <abs> --nested opal_ai=fd8ab8a57f`. The
  worker writes no nested file, but its checks read the pin through the nested checkout.

The slot continues with OA-e-8 after the item-0 close run.

<status>pending</status>
<round>2</round>
<slot>~12</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
