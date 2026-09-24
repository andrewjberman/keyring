# NFRA_OPALAI task order -- `OA-t-2` -- HOP 2: the Opal_Agent account's provisioning script and boundary verifier

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-t-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~3</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- Windows accounts and ACLs are an OS boundary, not AWS IAM; nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OA-t-2` (round 1, decomposition s.2/s.3)

The Teams-facing agent will run under its own standard local Windows account, `Opal_Agent`. That account is in neither
`Administrators` nor `CodexSandboxUsers`, and the OS denies it the development workspace by construction. Measured
facts: the workspace ACL grants SYSTEM, Administrators, `Opal Bloomberg`, `CodexSandboxUsers` and one unresolved SID;
the profile folder `C:\Users\Opal Bloomberg` grants only the first three. **This session is NOT elevated** (Medium
integrity), and creating a local account needs elevation. So you BUILD and dry-run the scripts, and the one elevated
run happens later, by Andrew at the box (gate G-ACCT). Build, in `opal_ai/opal/runtime/provision/`:

1. **`runtime.config.example.json`** with EXACTLY these keys (other cells read them): `checkout_dir` (where the
   operator keeps the read-only `opal_ai` PROD checkout, e.g. `C:\\opal_runtime\\opal_ai`), `state_dir` (the agent's only
   writable dir, e.g. `C:\\opal_runtime\\state`), `workspace_probe_file` (one workspace file the account must be DENIED,
   e.g. the workspace `CLAUDE.md`), and `prod_ref` (`PROD`). These are example values; the real config lives outside
   every repo. No product code hard-codes a path or names a device.
2. **`provision-account.ps1 -Config <json> [-Plan]`**, idempotent. `-Plan` prints one line per act, each starting
   `PLAN:`, with these eight tokens: `CREATE-USER Opal_Agent`, `ASSERT-NOT-MEMBER Administrators`,
   `ASSERT-NOT-MEMBER CodexSandboxUsers`, `MKDIR checkout_dir`, `MKDIR state_dir`, `ACL checkout_dir Opal_Agent:RX`,
   `ACL state_dir Opal_Agent:M`, `SECRET DPAPI operator`. It changes nothing and exits 0. Without `-Plan` it does those
   acts:
   - the generated password is stored DPAPI-protected (CurrentUser scope) in the OPERATOR's profile, outside every
     repo, and never printed;
   - the checkout dir stays owned and writable by the operator/Administrators, with `Opal_Agent` read+execute only;
   - the state dir grants `Opal_Agent` modify.
   **Not elevated: print `ELEVATION REQUIRED` and exit 3 BEFORE any act.**
3. **`verify-boundary.ps1 -Config <json>`**. It runs, AS `Opal_Agent` (using the stored credential), a read of
   `workspace_probe_file` (it must get Access Denied) and a read/write of a marker in `state_dir` (it must succeed, the
   positive control in the same run). It prints exactly one line starting `BOUNDARY: ` and exits `0` =
   `BOUNDARY: DENIED-OK`, `1` = `BOUNDARY: BREACH ...`, `4` = `BOUNDARY: NOT-PROVISIONED` (no `Opal_Agent`, or no stored
   credential). An absent account must never read as a held boundary.

## 2. BOUNDS

1. **`opal_ai` is a nested repository** at `<worktree>/opal_ai`, on branch `<your worktree branch>-opal_ai`. It has no
   hooks yet. Commit your nested files with `git -C opal_ai commit --author "0.9.0_WK_NFRA_OPALAI~3
   <0.9.0_WK_NFRA_OPALAI~3@opal.agent>" -F <msgfile> -- <nested paths>`, where the msgfile is written with the Write
   tool (the portal-cell precedent).
2. **Never create the account, a runtime dir or a credential on this box.** Every criterion runs in `-Plan` mode, in
   the refusing non-elevated mode, or in the verifier's NOT-PROVISIONED mode.
3. Standing: no push, no install, no vendor call, no AWS. REFUSE a criterion you cannot meet as written, and report the
   refusal with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
opal_ai/opal/runtime/provision/provision-account.ps1
opal_ai/opal/runtime/provision/verify-boundary.ps1
opal_ai/opal/runtime/provision/runtime.config.example.json
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~3/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_OPALAI-Z-W3-S<k>`.

## 4. PROOF OF SPEC (literal; run from your worktree root, after the nested repo is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-t-2"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/t2.AC1.sh; echo "exit=$?"</invocation><expect>rc=0; PLAN acts matched 8 of 8; Opal_Agent after plan: absent -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-t-2"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/t2.AC2.sh; echo "exit=$?"</invocation><expect>session elevated=False; rc=3; ELEVATION REQUIRED lines>=1; Opal_Agent=absent; checkout_dir before/after=no/no; state_dir before/after=no/no -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OA-t-2"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/t2.AC3.sh; echo "exit=$?"</invocation><expect>rc=4; BOUNDARY: NOT-PROVISIONED -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~3/NFRA_OPALAI.TO-OA-t-2.runtime-account-provisioning.proof_of_spec.json`. Report once: what you changed and where, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** hop 2. The elevated run (G-ACCT) and the DENIED-OK read are the close run's, by Andrew at the box,
then the issuer runs `verify-boundary.ps1` (row NFRA_OPALAI-Z-S1).

<status>pending</status>
<round>1</round>
<slot>~3</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
