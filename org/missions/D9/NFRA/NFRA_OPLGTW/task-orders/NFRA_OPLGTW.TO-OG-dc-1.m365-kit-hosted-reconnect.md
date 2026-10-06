# NFRA_OPLGTW task order -- `OG-dc-1` -- the colleague onboarding kit tells the hosted-gateway reconnect

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-dc-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~21</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a doc edit; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- documentation only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is the CTO's (R18, row Z-S55).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-dc-1` (decomposition addendum R3-T.11, item 3; row Z-S55)

`.tools/m365-mcp-kit/` (README.md, BOOTSTRAP.md; last touched 2026-06-12 @8b0e7d2412) predates the hosted gateway. Read
row `NFRA_OPLGTW-Z-S55` in the project's surprise channel for what it gets wrong. Rewrite the kit, or retire it to a
one-page pointer, so a colleague reconnects to the HOSTED gateway:
1. Remove the old MCP entry. Name the exact old entry (its server name or command) the kit told people to add.
2. `claude mcp add --transport http -s user opalgateway https://mcp.opalinvest.dev/mcp`
3. Authenticate with the work (opalinvest.com) account when prompted.

Keep it short and ASCII-only. Then write `DC1_RECORD.json`:
- `{old_entry_marker: "<the exact string of the old entry the kit used to tell people to add>", kit_files: [...], retired: true|false}`.

`old_entry_marker` must be a string that appeared in the OLD kit, and the check proves it is gone.

## 2. BOUNDS

- **Write:** `.tools/m365-mcp-kit/` and your deliverables only. No code, no gateway change.
- **Never:** push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor; put a secret or a
  personal identifier in the kit.

## 3. SURFACES

<paths>
.tools/m365-mcp-kit/
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~21/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W21-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-dc-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r18/checks/dc1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)kit files carrying the hosted command [1-9]\d*; old entry marker '[^']+' present in 0 file\(s\); README names the work-account sign-in 1.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~21/NFRA_OPLGTW.TO-OG-dc-1.m365-kit-hosted-reconnect.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance>`, and on PASS edit this order's ONE `<status>` tag IN
PLACE to `complete`. Report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 18 (R3-T.11, item 3). Alone.
- Pre-cut: `dc1.AC1` FAIL (the record is absent).

<status>pending</status>
<round>18</round>
<slot>~21</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
