# NFRA_OPLGTW task order -- `OG-up-1` -- split the data-refresh send: return after /trigger, a read-only status tool, an idempotent re-send (CTO R33)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-up-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~29</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change with tests and one read; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the one AWS read is a Step Functions describe/list, read-only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is the CTO's (ledger/ROUND_ANALYSIS.round23.md @c8a3b2911e, R33).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (one read-only Step Functions read). Tests run offline with fakes.
</preflight>

## 1. THE CELL -- `OG-up-1` (decomposition addendum R3-T.18, item 1)

`infra/aws/ec2/opal-gateway/app/integrations/opal_portal/integration.py` registers ONE tool,
`opal_data_refresh_upload(date, dry_run, confirm)`. On a real send (`confirm=True`) it POSTs `/trigger`, then polls
the status route in a loop of 45 sleeps of 20 s inside the same MCP call (about `:271-280`), then reads the manifest.
The client transport drops near 120 s. On 2026-10-07, 2 of 2 real sends lost their response although each send
landed (row `NFRA_OPLGTW-Z-S63`).

Do, in that file:
1. **The send returns right after `/trigger`.** The tool keeps its name and its three parameters.
   - A real send returns the uploaded list, `upload_id`, `execution_id` and the status it read ONCE.
   - It never waits more than 60 s in total inside the call after `/trigger`.
   - It tells the caller, in the returned text, to read `opal_data_refresh_status` next and never to re-send on a
     dropped transport.
2. **A NEW read-only tool `opal_data_refresh_status(execution_id)`.**
   - It returns the execution's status from the status route, and the served manifest's displayed date and text (the
     existing manifest read).
   - It makes GET requests only, and it is `read_only` in its classification.
   - Register it wherever this gateway enumerates tools, so it is not denied by default:
     - `SPEC.tool_classifications` in this file;
     - `INTEGRATION_TOOLS` in `app/data_entitlement.py`;
     - the tool-count and classification tests;
     - `app/graph_scope_map.py`: an EMPTY frozenset (it makes no Graph call), with the comment saying so.
   - **Do NOT add it to `identity_tool_allowlist.txt` or to the seed in `app/identity_scope.py`.** Widening a scoped
     identity's allowlist is Andrew's ruling (PRD 4.3). The issuer carries that call.
3. **Idempotent re-send.**
   - A `confirm=True` call for a date whose two files (name AND size) equal those of a trigger THIS PROCESS made in the
     last 30 minutes returns that trigger's `execution_id` with `already_triggered: true`, and does NOT POST `/trigger`
     again. It may skip the upload too.
   - The record is in-process (a module-level dict behind a lock).
   - A gateway restart clears it; say so in the docstring.
4. **Tests.** Add `tests/test_opal_portal_send_split.py`, offline, with `httpx` and the Graph helpers faked. Five named
   tests, `test_ogup1_ac01` to `test_ogup1_ac05`, as `up1.AC1.sh`'s header lists them. Test 01 asserts the wait bound
   by faking `time.sleep` and summing the requested seconds.
5. **The two caller texts.** In `.claude/skills/terminal-upload/SKILL.md` and
   `org/tier2_senior/0.2.0_DT_PortfolioAnalytics/deliverables/opal_bbgtml/BBG_DAILY_SKILL.md`, state the new read.
   - After a real send, read `opal_data_refresh_status` with the returned execution id, or the portal's displayed date
     if that tool is not available to your identity.
   - Each file carries this exact line: `Never re-send on a dropped transport.`
6. **One read (R33).** Read-only, with the repo's `.tools/aws` shim: find the yang-pipeline Step Functions execution
   that started about 2026-10-07T01:26Z. Write `W/UP1_0126Z_READ.json` with:
   - `execution_start_utc`, `execution_stop_utc`, `terminal_status`;
   - `overlapped_restart`: true when the execution was still RUNNING at 2026-10-07T01:30:43Z, the r23 gateway restart;
   - `execution_arn_sha256`. Do not record the ARN's execution name if it embeds an email.
   Find the state machine ARN from `infra/aws/lambda/data_refresh/` or its Terraform; do not guess it.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~29/`.

## 2. BOUNDS

- No release and no host act: that is `OG-rl-11`.
- Never call `opal_data_refresh_upload`, `/trigger` or any upload route for real. Never start an execution.
- `integrations/bloomberg/` (the repo root directory of that name) is under Andrew's no-modify order: do not touch it.
  This cell's file is `infra/aws/ec2/opal-gateway/app/integrations/opal_portal/integration.py`, a different tree.
- The dry-run path (`dry_run=True`) behaves exactly as today.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/opal_portal/integration.py
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/app/graph_scope_map.py
infra/aws/ec2/opal-gateway/tests/
.claude/skills/terminal-upload/SKILL.md
org/tier2_senior/0.2.0_DT_PortfolioAnalytics/deliverables/opal_bbgtml/BBG_DAILY_SKILL.md
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~29/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Under `tests/` you may add `test_opal_portal_send_split.py` and change ONLY the tool-count or tool-enumeration
constants that the new tool moves. Name each such change in your report.

Rows: id `NFRA_OPLGTW-Z-W29-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-up-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r25/checks/up1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 5 of 5; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-up-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r25/checks/up1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)failures beyond the live baseline 0; allowlist file changed since live: 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-up-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r25/checks/up1.AC3.sh; echo "exit=$?"</invocation><expect>(?s)skill texts carrying the status read and the no-re-send line: 2 of 2; the 01:26Z execution read recorded: yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the send returns within 60 s, the status tool is read-only, and a re-send does not re-fire.
- `AC2`: the new tool is classified everywhere, nothing else regressed, and no allowlist row was added.
- `AC3`: both caller texts carry the new read, and the 01:26Z execution is read.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-up-1.data-refresh-send-split.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If all three criteria PASS, edit this order's ONE `<status>` tag IN PLACE to `complete`.
4. Report once: literal AC output, every file changed with its reason, commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 24 (addendum R3-T.18, item 1). Chain: `OG-up-1` -> `OG-rl-11`.
- The CTO named `.claude/skills/bbg-daily`. That path does not exist in the repo: the tracked text is
  `org/tier2_senior/0.2.0_DT_PortfolioAnalytics/deliverables/opal_bbgtml/BBG_DAILY_SKILL.md`. The per-device copies
  under the user's home directory are outside any order.
- Open call carried by the issuer, not by this cell: whether opalbloomberg@ may call the new read-only status tool.
- Pre-cut 02:5xZ: `up1.AC1` FAIL (the test file is absent). `up1.AC2` PASS (0 beyond baseline, allowlist unchanged):
  it is the regression guard. `up1.AC3` FAIL (0 of 2 texts, no read).

<status>complete</status>
<round>24</round>
<slot>~29</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
