# NFRA_OPLGTW task order -- `OG-ln-1` -- the gateway lineage reconcile: CLOUD = live + a LISTED CLOUD-only set

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ln-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~22</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a source reconcile; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; no release.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ruling is the CTO's (R16, round-17 analysis s.3).
EGRESS CLASS, declared: NONE (repo-only; a read-only host md5 read is allowed to confirm live).
</preflight>

## 1. THE CELL -- `OG-ln-1` (decomposition addendum R3-T.11, item 2; CTO R16)

Releases were cut on live, so CLOUD and live diverged both ways.

**At the cut**, `git diff --stat 37be3485db CLOUD -- infra/aws/ec2/opal-gateway` lists 23 files (+1144/-686):
- `app/integrations/schwab/integration.py` on CLOUD lacks live's `environ_with_external_ids` call (0 occurrences).
- `tests/test_schwab_host_inputs.py` exists on live and not on CLOUD.
- `tests/conftest.py`, `tests/acceptance/onhost_bench.py` and `test_login_retire.py` (OA-e-10's `/login` narrowing,
  drained @09dc173612 and never released), among others, exist only on CLOUD.

Live is the manifest's `deployed_commit`; confirm it by host md5.

Do this:
1. For EVERY file in that diff, classify each hunk as LIVE_ONLY (present on live, absent on CLOUD) or CLOUD_ONLY
   (CLOUD's change, not released).
2. **Port every LIVE_ONLY hunk to CLOUD.** That covers live's template lines, the `environ_with_external_ids` call,
   `test_schwab_host_inputs.py` and the rest. Do not touch a CLOUD_ONLY change.
   - Run the gateway's schwab and login test files, each in its own process; no new failure beyond the per-file
     baseline `r17/Q7_SUITE_BASELINE.txt`.
   - Commit.
3. Write `LINEAGE_R18.json`:
   - `{live, live_only_remaining: 0, ported: [{path, what}], items: [{path, kind: "CLOUD_ONLY", owner, disposition, note}]}`.
   - `owner` is the cell or order that wrote the CLOUD-only change, by commit.
   - `disposition` is `SHIPS_IN_RELEASE` (name the release item, for example OA-e-10, "a named release after OG-ln-1")
     or `REVERTS_ON_OWNER_WORD`.
   - After your port, every file still differing must appear in `items`.

   Also write a short `LINEAGE_R18.md`.
4. Use the issuer's form, `deliverables/2.0.0_SA_COO~O/RELEASE_ORDER_FORM.md` (Phase D, DRAIN-BACK), for the record's
   shape. Do not edit the form.

## 2. BOUNDS

- NO release and no host write. CLOUD source only, plus your deliverables.
- Never revert a CLOUD_ONLY change. List it, with its owner.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~22/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W22-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ln-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r18/checks/ln1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)missing 0 \[\]; malformed 0 \[\]; live_only_remaining 0; environ_with_external_ids on CLOUD [1-9].*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~22/NFRA_OPLGTW.TO-OG-ln-1.gateway-lineage-reconcile.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance>`, and on PASS edit this order's ONE `<status>` tag IN
PLACE to `complete`. Report once: the ported list, the CLOUD_ONLY list with owners and dispositions, test readings, AC
output, rows, commits.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 18 (R3-T.11, item 2). Alone. The DRAIN-BACK step and the pre-GO check exercise are written into the issuer's
  form `RELEASE_ORDER_FORM.md` in this issuance. The form is the issuer's own artifact, so it is outside this cell.
- Pre-cut: `ln1.AC1` FAIL (the record is absent; `environ_with_external_ids` on CLOUD 0).

<status>pending</status>
<round>18</round>
<slot>~22</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
