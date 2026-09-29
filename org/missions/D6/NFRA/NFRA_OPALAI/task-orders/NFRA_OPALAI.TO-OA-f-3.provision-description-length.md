# NFRA_OPALAI task order -- `OA-f-3` -- DIRECT ACT, ADDENDUM R2-A1: provision-account.ps1's account Description fits New-LocalUser's 48-character limit

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-f-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~18</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-line literal change; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- a literal's length; no gate moves.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OA-f-3` (decomposition ADDENDUM R2-A1; row NFRA_OPALAI-Z-S37; CTO ruling msg 26231)

`opal_ai/opal/runtime/provision/provision-account.ps1` creates the Windows account `Opal_Agent`. At line 101 it calls
`New-LocalUser ... -Description 'Opal Teams-facing runtime agent account (provisioned by provision-account.ps1, OA-t-2)'`.
That literal is 86 characters, and `New-LocalUser` refuses any `-Description` over 48 characters. So the real
(elevated) run refused before any act, and the account was never created.

Change ONLY that one literal to a plain description of 48 characters or fewer. It must still say this is the Opal
runtime agent account, for example `Opal runtime agent (Teams-facing, OA-t-2)`. Change no other line, character or
file. The literal carries no behaviour.

**Your committed line is compared byte for byte.** `0.0.0_AB_MSTR~Z` will run the provisioning from a scratch copy of
the script with exactly your one changed line, and must see a diff of exactly that one line.

## 2. BOUNDS

1. **`opal_ai` is a nested repository** at `<worktree>/opal_ai`, on its own branch off `opal_ai` `fd8ab8a57f`. Commit
   with `git -C opal_ai commit --author "0.9.0_WK_NFRA_OPALAI~18 <0.9.0_WK_NFRA_OPALAI~18@opal.agent>" -F <msgfile> --
   opal/runtime/provision/provision-account.ps1`, the msgfile written with the Write tool. Do not re-save the file
   through a tool that rewrites line endings: keep every other byte identical.
2. Never run the script without `-Plan`, and never elevated. AC2 runs `-Plan` against a scratch config.
3. Standing: no push, no install, no vendor call. REFUSE a criterion you cannot meet as written, and report the refusal
   with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
opal_ai/opal/runtime/provision/provision-account.ps1
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~18/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id
`NFRA_OPALAI-Z-W18-S<k>` (none exist at the cut; the first is S1).

## 4. PROOF OF SPEC (literal; run from your worktree root, after the nested commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-f-3"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f3.AC1.sh; echo "exit=$?"</invocation><expect>desc_len<=48; numstat added/removed vs fd8ab8a57f=[1 1]; other files changed=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-f-3"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f3.AC2.sh; echo "exit=$?"</invocation><expect>parse errors=0; -Plan rc=0 PLAN lines=8 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~18/NFRA_OPALAI.TO-OA-f-3.provision-description-length.proof_of_spec.json`.
Report once: the old and new line verbatim, the nested commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** a direct act, outside round 2's issuance (it carries no `<round>`, as round 1's addenda OA-f-1/OA-g-2 did;
the L6 gate keys ONE issuance per round), on `1.0.0_SA_CTO~O`'s ruling (a) (msg 26231), under row Z-S37. It reaches opal_ai PROD in
the cutover G-PUSH (Andrew-direct @f8d1103a38). Ruling (b): once this line is committed, `0.0.0_AB_MSTR~Z` re-runs
G-ACCT steps 1-6 from a scratch copy OUTSIDE `C:\opal_runtime\opal_ai`. Before step 2 it prints `git diff --no-index`
against PROD fd8ab8a's script, and that diff must be exactly this one line. The issuer relays the committed line to
`0.0.0_AB_MSTR~Z` at the drain.

SPAWN ONLY WHEN: at the cut. Slot `~18`, nested worktree `--nested opal_ai=fd8ab8a57f`.

Dry-run at base (opal_ai fd8ab8a57f):
- f3.AC1 base: FAIL as expected (`desc_len=86; numstat added/removed vs fd8ab8a57f=[0 0]; other files changed=0`).
- f3.AC2 base: PASS as expected (`parse errors=0; -Plan rc=0 PLAN lines=8`: the bound control).

<status>complete</status>
<direct_act>true</direct_act>
<slot>~18</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
