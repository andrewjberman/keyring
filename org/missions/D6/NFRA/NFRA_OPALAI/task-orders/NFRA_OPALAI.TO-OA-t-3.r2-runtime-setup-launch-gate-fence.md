# NFRA_OPALAI task order -- `OA-t-3` -- ROUND 2, item 0 (RE-CUT UNCHANGED): the runtime's Claude setup, the fail-closed launch gate, and the fence, parent half

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-t-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~11</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- a re-cut of a round-1 thread cell; the fence's deny arms are the adversary read.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OA-t-3` (round 1 decomposition s.2/s.3, re-cut in round 2 section R2.1, item 0)

**The cell text, verbatim from round 1:**

The Teams agent `Opal_Agent` runs from a read-only checkout of `opal_ai` PROD, with its own narrow Claude setup. Build,
in `opal_ai/opal/runtime/` (the agent's product files live beside it in `opal_ai/opal/agent/`: `prompt.md`, `refs/`,
`skills/bbg-teams-assist/`, which another cell moves this round):

1. **`CLAUDE.md`**: the runtime's only memory file. It names the agent `Opal_Agent` and imports its guardrails with
   the line `@../agent/prompt.md`. Nothing else from the workspace.
2. **`.claude/settings.json`**: registers `../agent/hooks/concierge-gate.sh` (item 6) as a `PreToolUse` hook on every
   tool. Its skills are `../agent/skills/`.
3. **`mcp.json.example`**: `mcpServers` holds exactly ONE server, `opal-gateway-bbg` (`https://mcp.opalinvest.dev/mcp`).
   Never `opal-gateway` (Andrew's proxy identity), never anything that reaches the workspace, no AWS profile.
4. **`launcher.ps1 -Config <json>`**, run by the OPERATOR account (PRD C3/C4 v0.3):
   - fetch `prod_ref` into `checkout_dir` fast-forward only (`--ff-only`), using the operator account's EXISTING GitHub
     access on this box (no new credential is minted; PRD v0.5 retired the narrow one); a pull that would not
     fast-forward refuses;
   - then start `launch-gate.ps1` and, only if it passes, the agent AS `Opal_Agent`, from `checkout_dir/opal/runtime`,
     passing it NO operator credential, token or environment.
   The config file has the keys `checkout_dir`, `state_dir`, `workspace_probe_file`, `prod_ref` (see
   `opal_ai/opal/runtime/provision/runtime.config.example.json`, written by a sibling cell this round; read it when
   present, never write it).
5. **`launch-gate.ps1 -Config <json>`**, run AS the runtime account. It checks three things:
   - (a) a read of `workspace_probe_file` must be DENIED. A successful read gives the reason `PROBE-READABLE`; a
     missing file gives `PROBE-MISSING` (missing is not denied);
   - (b) `checkout_dir` is clean (no staged, unstaged or untracked change: `CHECKOUT-DIRTY`) and its HEAD equals the
     resolved `prod_ref` (`CHECKOUT-NOT-AT-PROD`);
   - (c) the running account is in neither `Administrators` nor `CodexSandboxUsers` (`ADMIN-GROUP`).
   It prints exactly one line, `GATE: PASS` or `GATE: REFUSE <REASON> [<REASON> ...]` listing EVERY failing reason
   (never stopping at the first), and exits 0 on PASS and 1 on REFUSE.
6. **The fence moves**: `.tools/hooks/bg-concierge-gate.sh` becomes `opal_ai/opal/agent/hooks/concierge-gate.sh`, and
   the parent copy is removed on your branch. Today it fires only for the serial `0.0.3_BG_BBGTerminal` (`:11-14`,
   `:87-91`), allowlists workspace paths (`:23-24`) and uses the workspace's `jq`. In the runtime it must:
   - bind UNCONDITIONALLY: no serial, no session file;
   - read its allowlist from the runtime config named by the env var `OPAL_RUNTIME_CONFIG` (JSON; writes are allowed
     only under `state_dir` and tmp);
   - FAIL CLOSED when `OPAL_RUNTIME_CONFIG` is unset or unreadable (every write denied);
   - reach no workspace file (resolve `jq` from PATH, or drop it; fail closed without it);
   - deny with the same JSON (`"permissionDecision":"deny"`, exit 0).
   G2-G4's denials (git and AWS mutation, Bloomberg download-class, Andrew's proxy gateway, email/site writes) stay
   unchanged in content. Move `.tools/hooks/tests/test_bg_concierge_gate.sh` with it to
   `opal_ai/opal/agent/hooks/test_concierge_gate.sh`, adapted to the runtime binding.

**The state at this re-cut -- what is already done, and what is yours:**
- **The nested half is DONE.** Items 1-6's `opal_ai` files are on `opal_ai` origin PROD `fd8ab8a57f`. You write NO
  `opal_ai` file. First run `git -C opal_ai fetch origin` so the pin `fd8ab8a57f` resolves in your nested checkout. The
  criteria run the gate and the fence from a throwaway detached `opal_ai` worktree AT THAT PIN (the check's own
  `_pin.sh` makes and removes it), never at the nested HEAD. The round-2 cell before you on this slot, OA-e-2, adds a G4
  deny line to the fence by design.
- **The parent half is YOURS**, on the current HEAD: remove `.tools/hooks/bg-concierge-gate.sh` and
  `.tools/hooks/tests/test_bg_concierge_gate.sh`. Round 1's parent commits were made on a branch from before the history
  rewrite. NEVER merge, cherry-pick or read `wk-NFRA_OPALAI-3`, and never touch `C:/tmp/oa-1` or `C:/tmp/oa-3`. Redo the
  removal here.

## 2. BOUNDS

1. You write no file under `opal_ai/`. The parent-side removals go through `safe-commit.sh`, and they merge in the
   round's cutover window.
2. **Do not start the agent, create an account or run anything as another user.** AC1 runs the gate as THIS account
   (an Administrator that can read the workspace), and it must refuse. That refusal is the seam probe.
3. `.claude/settings.json` (the workspace's fence registration line) and `.tools/ajb.ps1` are NOT yours. The issuer
   changes them at cutover.
4. Standing: no push, no install, no vendor call, no AWS. REFUSE a criterion you cannot meet as written, and report the
   refusal with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
.tools/hooks/bg-concierge-gate.sh
.tools/hooks/tests/test_bg_concierge_gate.sh
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~11/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_OPALAI-Z-W11-S<k>`
(next free k for W11).

## 4. PROOF OF SPEC (literal; run from your worktree root, after the parent half is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-t-3"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/t3.AC1.sh; echo "exit=$?"</invocation><expect>arm1 rc!=0 GATE: REFUSE naming PROBE-READABLE and ADMIN-GROUP and not CHECKOUT-DIRTY; arm2 rc!=0 GATE: REFUSE naming CHECKOUT-DIRTY, PROBE-READABLE and ADMIN-GROUP -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-t-3"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/t3.AC2.sh; echo "exit=$?"</invocation><expect>mcp servers=[opal-gateway-bbg]; CLAUDE.md import>=1 name>=1; fence registrations>=1; launcher --ff-only>=1; runtime files naming workspace/AWS/serial=0; parent fence gone=yes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OA-t-3"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/t3.AC3.sh; echo "exit=$?"</invocation><expect>fence arms as expected: 5 of 5 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~11/NFRA_OPALAI.TO-OA-t-3.r2-runtime-setup-launch-gate-fence.proof_of_spec.json`.
Report once: what you changed and where, the parent commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** item 0 (R-3), re-cut UNCHANGED: round 1's cell text and three criteria. The check files are round 1's,
copied to `round2/checks/` with the ONE amendment each (decomposition R2.3): the nested files are read from a detached
`opal_ai` worktree at `$OA_NESTED_PIN` (`fd8ab8a57f`), made by `round2/checks/_pin.sh`. That worktree is placed under
`$HOME`, NOT under TMPDIR/TEMP/TMP. The fence allowlists the tmp roots for writes, so a pin under TMPDIR would pass
t3.AC3's "edit own prompt -> DENY" arm through the tmp allowance and read as a fence defect.

The gate's PASS arm (as `Opal_Agent`) and its negative arm (a workspace read granted for a test) are the close run's
(A7, FWD-7), after G-ACCT and G-AUTH. Cutover hookups, the issuer's: remove the fence line from
`.claude/settings.json`, and retire the BG launch line in `.tools/ajb.ps1`.

**Dry-run at base** (main tree, CLOUD `7cb7c7f33d`, nested pin fetched; the pin worktree was removed after each run, and
`git -C opal_ai worktree list` shows none left):
- t3.AC1 base: PASS as expected. It is a control: arm1 `GATE: REFUSE PROBE-READABLE ADMIN-GROUP`, arm2 adds
  `CHECKOUT-DIRTY`, both rc=1.
- t3.AC2 base: FAIL as expected. The parent half is the build: `parent fence gone=no`, and every nested read is as
  expected.
- t3.AC3 base: PASS as expected. It is a control: fence arms 5 of 5 at the pin.

**SPAWN ONLY WHEN:**
- Parts A-B of the switchover sitting have landed (G-ACCT, G-AUTH).
- OA-e-2 has drained. The slot continues here after it.
- The nested checkout carries the pin. Provision with `--nested opal_ai=fd8ab8a57f`; a slot continued from OA-e-2
  already has it.

<status>pending</status>
<round>2</round>
<slot>~11</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
