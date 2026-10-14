# NFRA_OPLGTW task order -- `OG-gt-7` -- the hookup of the ten G1 typed harvest tools: registrations, SAFE and NATIVE lists, the two re-pinned counts

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gt-7</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-gt-7</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~78</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests only; no deploy. The release is NFRA_OPLGTW.TO-OG-ap-18 (the release order this cell rides).
comp-iam: RUN-BY-ISSUER at the cut: the new code's AWS calls are s3:GetObject and s3:ListBucket on opal-data-harvest, read through OG-hv-2's grant (A5: the policy on gateway-global-internal-reader-role, which `harvest_read._client()` assumes); this cell changes no IAM and adds no AWS call beyond those two. Live probes run with the box's own credentials, read only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z msg 34077 and msg 34083 on PRD v3.0 (FWD-22; Andrew-direct ~12:4xZ), the CRO's G1 census @0d7c29b3c5 section 3, and the two corrections of the CRO's L4-R review @e47fafb709.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-gt-7` (decomposition addendum R3-T.50, workstream G1-TYPED, FWD-22)

The hookup of the ten G1 typed tools (gt-1..gt-4, merged): `tools.py` registrations, `SAFE_TOOLS` and `NATIVE_TOOLS` lists, the registry count 65 -> 75 and the non-data count 56 -> 66. Applied by the issuer's prepared script.

The hookup of the ten G1 typed harvest tools (builds OG-gt-1 to OG-gt-4, all merged on your HEAD). The five tool modules exist
(`app/harvest_identity.py`, `app/harvest_press.py`, `app/harvest_figures.py`, `app/harvest_research.py`, with `app/harvest_typed.py` beneath them) and
none of their ten tools is registered, classified or counted yet. Registration belongs to no tool cell (CUT BY WRITE SET), so this cell is the one place
it lands. `harvest_get_published_analysis` (OG-gt-5) is NOT registered here: it rides its own ask.

1. **Apply the prepared hookup.** The issuer wrote and dry-ran the edit as a script on HEAD copies: `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/hookup_g1.py`. Run it from your worktree root:
   `python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/hookup_g1.py infra/aws/ec2/opal-gateway`. It makes exactly these edits, and nothing else:
   - `app/tools.py`: one import line beside `harvest_read`'s and ten `@mcp.tool()` registrations after `harvest_read`'s, each
     `return _run("<name>", {<audit args>}, lambda t: <module>.<name>(<args>))`;
   - `app/data_entitlement.py`: the ten names into `NATIVE_TOOLS` (read class, `legacy`; NOT `DATA_GRANT_TOOLS`);
   - `app/destructive_ops.py`: the ten names into `SAFE_TOOLS`;
   - `tests/test_entitlement_admin.py`: the registry count pin 65 -> 75;
   - `tests/test_data_entitlement_family.py`: the non-data count pin 56 -> 66, in the assertion and in its two comments.
   The ten names: `harvest_resolve_security`, `harvest_security_coverage`, `harvest_get_chatter`, `harvest_search_articles`, `harvest_get_article`, `harvest_get_fundamentals`, `harvest_query_columns`, `harvest_get_research`, `harvest_get_filing_analysis`, `harvest_get_peers_and_scores`.
   If the script refuses (an expected line has moved because another seat edited one of the five files), STOP, file a BLOCKING row naming the file, and
   change nothing by hand.
2. **Check that every registration's arguments match the module function it calls.** For each of the ten, read the module function's signature
   and compare it with the registration (`from_day` and `to_day` are the Python names for the schema's `from` and `to`). A mismatch is a BLOCKING row; do not
   edit a tool module (it is not in your `<paths>`).
3. **Run, in `infra/aws/ec2/opal-gateway`:** `tests/test_entitlement_admin.py`, `tests/test_data_entitlement_family.py`, `tests/test_data_entitlement_guard.py`,
   `tests/test_og_hv1.py`, `tests/test_og_gt0.py` to `tests/test_og_gt4.py`, `tests/test_og_gt6.py`. The only failure allowed is `test_ogz1_ac08`, which is
   in `tests/baseline/failing_ids_full.txt` (a pinned route set that predates this work). Print the pass and fail counts.
4. Commit the five files only. The commit-time naming gate and the non-ASCII WARN are expected to print; neither may be overridden.

## 2. BOUNDS

- Code, tests and your probe only. No release, no deploy, no IAM or Terraform change, no write to any bucket, no grant written.
- `app/tools.py`, `app/data_entitlement.py`, `app/destructive_ops.py` and the pinned-count tests are NOT yours: the issuer
  registers every tool and re-pins the counts at the merge, in one commit. Do not edit them; name the registration you
  expect in your report.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a person's name or a full email address, or an object's
  text body into a report, a row or a log; write the catalog file (`app/refs/DATA_CATALOG.yaml` is NFRA_MCPINDEX's alone);
  override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/app/destructive_ops.py
infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py
infra/aws/ec2/opal-gateway/tests/test_data_entitlement_family.py
infra/aws/ec2/opal-gateway/tests/baseline/failing_ids_full.txt
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/hookup_g1.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~78/`. Rows: id `NFRA_OPLGTW-Z-W78-S<k>`, fabric `site-z`,
disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gt-7"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt7.AC1.sh; echo "exit=$?"</invocation><expect>(?s)tools registered in app/tools\.py: 10 of 10.*entitlement-admin suite \(the registry count pin is 75\): passed 9 of 9, failed lines 0, rc 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-gt-7"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt7.AC2.sh; echo "exit=$?"</invocation><expect>(?s)classified: SAFE 10 of 10, NATIVE 10 of 10, in DATA_GRANT_TOOLS 0 \(want 0\); files outside this cell's five \(and its records\) 0 \(want 0\).*pytest rc=0; named tests passed 1 of 1; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: all ten tools are registered and the registry count test passes at 75.
- `AC2`: the ten names are classified read-class, none in DATA_GRANT_TOOLS, nothing outside the five files changed, and the non-data family test passes.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-gt-7.g1-hookup.proof_of_spec.json`. Validate it after your last commit with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to
`complete` only if both PASS, and report once. Your report names the tool registrations and the pinned-count moves you expect
the issuer to make at the merge.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G1-TYPED (decomposition addendum R3-T.50 @d9371ffe81; PRD v3.0 ADMITTED: ratified-text SIGNED by
  3.0.0_SA_CVO~Z, brief SIGNED by 4.0.0_SA_CRO~Z, `prd-signoff.py status` read at the cut). CTO msgs 34077 and 34083.
- The hookup the issuer owes at the merge (CUT BY WRITE SET). The gateway app files are in lane CLOUD_OPS_OR_ETL, which the COO cannot commit: a worker order grants them, so no lane escape is taken. Rides `OG-ap-18`.
- Pre-cut: gt7.AC1 and gt7.AC2 base FAIL as expected (no tool registered, none classified).

<status>pending</status>
<round>37</round>
<workstream>FWD22-W4</workstream>
<slot>~78</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
