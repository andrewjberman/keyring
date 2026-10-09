# NFRA_OPLGTW task order -- `OG-ab-2` -- generalise copy_site_file_to_s3: admit .pptx -> market_update beside E2's .xlsx -> fee_statement; NO release

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ab-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ab-2</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~49</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code build on a branch; nothing is deployed, applied, scheduled or invoked. No cron, alarm or monitor is created.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell reads and applies no policy. If the new destination needs a PutObject grant, the build ADDS it to `infra/aws/terraform/opal-gateway/advi_billing_gateway_iam.tf` unapplied; the E2 release pair plans and applies it.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is `1.0.0_SA_CTO~Z`'s ruling org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~Z/CTO_RULING_SITE_TO_S3_PPTX_GENERALISATION_FOR_DELL2_FWD6_20261009.md @4e2f00c9fa, on dell2 CTO ruling @1e0c6f1455 (relay MSTR~Z msg 32760).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-ab-2` (decomposition addendum R3-T.37)

`G` = `infra/aws/ec2/opal-gateway/`. `G/app/integrations/advi_billing/site_to_s3.py` copies ONE SharePoint item, with the
caller's delegated token, to the bronze `fee_statement` root (`ADVI_FEE_STATEMENT_S3_ROOT`), `.xlsx` only, by a
conditional put, and returns `{s3_key, bytes, sha256}`. dell2 needs the SAME path for one `.pptx` deck (FWD-6, first
use: item `01ECUY3THSUYX5OOIWW5DJCQKY27LQ5HLW` in Opal Capital / Shared Documents / Market Update) to the `market_update`
bronze address. The CTO ruled: generalise, do not copy.

1. **Two admitted pairs, one table.** Make the root and the extension filter PARAMETERS of the module, selected from ONE
   in-code table of exactly two admitted (extension, destination) pairs:
   - `.xlsx` -> the fee_statement root (E2, unchanged behaviour, partition `quarter=<q>`);
   - `.pptx` -> the `market_update` root, partition as the registry's `market_update` table defines it.
   Each root comes from `lib/opal_naming.py address()`, through an env value the deploy computes, never typed. If
   `address()` REFUSES `market_update` (no registry row), that is a missing registry row: file a BLOCKING row naming it
   and STOP this pair (rule 30 -- never a hand-typed workaround). The tool's public signature gains the minimum needed
   to select the pair (keep E2's existing call working unchanged). Any other extension is REFUSED before any read.
   A `.pptx` is a zip container like `.xlsx`; keep the bytes check per pair.
2. **The deploy line.** In `G/deploy-to-ec2.sh`, beside E2's `ADVI_FEE_STATEMENT_S3_ROOT`, compute the market_update root
   from `address()` and write it into the `.env` printf (one `%s`, one argument). Refuse (exit non-zero before any write)
   if it does not end in `/bronze/market_update/`.
3. **The grant, if needed.** If the gateway role has no PutObject on the market_update prefix, add ONE statement to
   `infra/aws/terraform/opal-gateway/advi_billing_gateway_iam.tf`, the prefix read from the same registry join E2 uses;
   unapplied. Say so in your report.
4. **Tests**, `G/tests/test_og_ab2_pairs.py`, offline, named exactly `test_ogab2_ac01`, `_ac02`, `_ac03`, as
   `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/ab2.AC1.sh`'s header states. E2's suites
   must still pass whole.
5. Update the tool's entries in `destructive_ops.py` only if the classification text names `.xlsx` or one prefix;
   the class stays `WRITE_REVERSIBLE` / `write_files`.

## 2. BOUNDS

- No release, deploy, plan, apply or upload.
- No second tool, no second copy path, no third pair.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into your branch (row Z-W41-S5); override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/advi_billing/
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/app/destructive_ops.py
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
infra/aws/ec2/opal-gateway/tests/
infra/aws/terraform/opal-gateway/advi_billing_gateway_iam.tf
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~49/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W49-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ab-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/ab2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*test_advi_site_to_s3\.py: pytest rc=0.*test_advi_site_to_s3_registration\.py: pytest rc=0.*test_og_ab1_carry\.py: pytest rc=0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ab-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/ab1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)copy_site_file_to_s3 registered in tools\.py: 1 \(want 1\); listed unclassified: 0 \(want 0\); census reports 0 unclassified: yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: two admitted pairs, builder-derived roots, the deploy line, and E2 unchanged.
- `AC2`: still one tool, still classified.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~49/`.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ab-2.site-to-s3-pptx-pair.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If both criteria PASS, edit the ONE `<status>` tag of this order IN PLACE to `complete`.
4. Report once: literal AC outputs; the market_update address `address()` returned; whether a grant was added; commits, rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- CTO~Z ruling @4e2f00c9fa (msg 32768): build now on OG-ab-1 @17828a452d; released WITH E2 under ONE pair naming both
  admitted pairs (CVO half included), at E2's slot after MP-x-4, the allowlist and MX-r-9.
- Pre-cut: see the issuance commit.

<status>pending</status>
<round>33</round>
<workstream>ADVI-E2-PPTX</workstream>
<slot>~49</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
