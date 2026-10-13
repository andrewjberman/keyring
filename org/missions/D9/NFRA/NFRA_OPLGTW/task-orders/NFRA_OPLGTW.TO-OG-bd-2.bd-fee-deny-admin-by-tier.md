# NFRA_OPLGTW task order -- `OG-bd-2` -- deny `blackdiamond_list_fees` to unprofiled principals, master_admin admitted by tier (E1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-bd-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-bd-2</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~60</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code, tests and an ask; the deny reaches users only in a later gateway release under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the code narrows a tool's admission and widens nothing.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z's round-35 analysis E1 (org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round35.md @682d1ced78) on Andrew's YES (sitez-1b36, "Yes that is fine").
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-bd-2` (decomposition addendum R3-T.48, E1)

Today, `decide()` (`infra/aws/ec2/opal-gateway/app/data_entitlement.py:448`) passes `blackdiamond_list_fees` through for a
principal with NO profile, while the Schwab tools are denied. The census (`deliverables/0.9.0_WK_NFRA_OPLGTW~57/BD1_CENSUS.json`)
found 2 unprofiled callers:
- `2cdb43ed4d`, tier `master_admin`, 4 calls, outcome ok;
- `fc9aed2e22`, tier `standard`, 1 call, already DENIED by the tool's own gate, with NO principal on record.

Ruling (CTO E1, on Andrew's YES): the real callers keep their access, and an unknown principal no longer reaches client
fee data. Do NOT write a profile: the only profile kind, `restricted`, confines its holder on the data-grant family.

1. **Code.** Make `decide()` deny `blackdiamond_list_fees` to a principal with NO profile, UNLESS that principal's tier is
   `master_admin`.
   - The tier comes from the gateway's existing tier logic (`app/tier.py`; `app/entitlements.py` and `app/blast_cap.py`
     also read `master_admin`). Read how the request's tier is known, and pass it to the decision without inventing a
     second source.
   - A profiled principal's answer is unchanged. The Schwab tools stay denied to unprofiled principals, master_admin
     included, exactly as today.
2. **Tests,** in `infra/aws/ec2/opal-gateway/tests/test_og_bd2.py`:
   - `test_ogbd2_ac01`: a master_admin principal with no profile is ALLOWED `blackdiamond_list_fees`.
   - `test_ogbd2_ac02`: a standard principal with no profile is DENIED it (`entitlement_denied`).
   - `test_ogbd2_ac03`: a profiled principal's answers are unchanged, and the Schwab tools are still denied to an
     unprofiled master_admin and an unprofiled standard principal.

   If an existing test pins the old pass-through (for example `tests/test_data_entitlement_family.py::test_ogpf1_ac02`),
   re-pin it to the new answer and name it in your report.
3. **Ask.** Write `W/NEVER_WIDEN_ASK_OG-bd-2.md` for the gateway release that ships this. It names:
   - the admitted class `master_admin` and the caller `2cdb43ed4d` it keeps;
   - the still-denied unlinked caller `fc9aed2e22`, which loses nothing it has;
   - the blast radius: one tool, unprofiled non-master_admin principals;
   - the rollback: the prior release ref.

   The release itself is a later order.

## 2. BOUNDS

- Code, tests and the ask only. No release, no deploy, no profile or grant written.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a person's name or email; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/app/tier.py
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/tests/test_og_bd2.py
infra/aws/ec2/opal-gateway/tests/test_data_entitlement_family.py
infra/aws/ec2/opal-gateway/tests/test_data_entitlement_guard.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~60/`. Rows: id `NFRA_OPLGTW-Z-W60-S<k>`, fabric
`site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-bd-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r36/checks/bd2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*failing ids not in the baseline: 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-bd-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r36/checks/bd2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ask: master_admin lines [1-9]\d*; fc9aed2e22 lines [1-9]\d*; rollback lines [1-9]\d*.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the deny is built, the admin is admitted by tier, and nothing else regresses. `AC2`: the release ask exists.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-bd-2.bd-fee-deny-admin-by-tier.proof_of_spec.json`. Validate it after
your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the
ONE `<status>` tag to `complete` only if both PASS, and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 36, E1. Supersedes OG-bd-1's re-cut, with E4 of round 35 on Andrew's answer.
- Pre-cut:
  - bd2.AC1 base FAIL as expected: the test file is absent, and the baseline limb reads 0 new ids after the issuer fixed
    the path separator.
  - bd2.AC2 base FAIL as expected: the ask is absent.

<status>pending</status>
<round>36</round>
<slot>~60</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
