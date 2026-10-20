# TO NFRA_SCHWABBF.TO-BF-k6 -- the schwab converter build pin in silver.tf moves to the commit the package dir equals, with a byte-equality test (Terraform text only)

<to_id>NFRA_SCHWABBF.TO-BF-k6</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~1</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>release-0840</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-k-6` (`decompositions/NFRA_SCHWABBF_DECOMP_R6.md`) |
**outcome_ref:** FWD-1, FWD-6 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`BF-k-6`. The schwab silver converter Lambda carries an `OPAL_BUILD_COMMIT` environment row taken from the map `silver_build_commit` in `infra/aws/terraform/opal-assets/silver.tf` (about lines 116-122): `schwab = "12ecbe2b8f"` today. The file's own comment (lines 52-110) states the rule: the pin names "the commit whose `data/assets/scripts/silver/` tree the package dir is byte-equal to", measured with `git show` against the package dir, never assumed, with a rollback pin named in a comment line. Rounds 2-5 of this project changed the vendored modules (`conversion_manifest.py`, `set_identity_guard.py`, `schwab_runtime.py`, `schwab_projections.py`, `schwab_conversion.py`, `lib/backfill_status.py`) and the package dir `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/` in step, so the live pin `12ecbe2b8f` now names an older tree and the vintage the converter reports would be a confident, precise, wrong value (row `NFRA_SCHWABBF-W5-S5`). This cell moves ONLY the schwab pin and records it. It edits Terraform TEXT and adds one test; it runs no `terraform init`, `plan` or `apply` and no `aws` command.

**Build.**
1. In `infra/aws/terraform/opal-assets/silver.tf` change exactly one value: `schwab = "12ecbe2b8f"` to `schwab = "27acf60210"` (the other four entries, `etf`, `blackdiamond`, `eclipse`, `orion`, stay byte for byte). `27acf60210` is the merge of the last cell of round 5 on `box/laptop`; at it all vendored modules of the package equal their sources (you prove this in the test).
2. Add ONE comment block (ASCII only, the style of the neighbouring ones) at the end of the pin comment run, before `silver_build_commit = {`: `NFRA_SCHWABBF BF-k-6 moves it to 27acf60210: the merge that carries the firm-form key rule, the by-master guard and manifest, the silver firm key and the state tier in data/assets/scripts/silver/ and lib/backfill_status.py; the package dir equals that commit's blobs for every module in BUILD_MANIFEST.json vendored_modules (tested by data/canonical/schwab/tests/test_schwab_build_pin.py). Rollback pin: 12ecbe2b8f.`
3. New test `data/canonical/schwab/tests/test_schwab_build_pin.py` (function names contain `build_pin`): (a) the schwab pin parsed from `silver.tf` equals `27acf60210` and the rollback pin `12ecbe2b8f` appears in the comment; (b) the other four entries (`etf`, `blackdiamond`, `eclipse`, `orion`) equal their values in the file as committed at `dee04e1b01` (read it with `git show dee04e1b01:infra/aws/terraform/opal-assets/silver.tf`; that literal commit is fixed text in the test); (c) `27acf60210` resolves (`git cat-file -t`) to a commit and is an ancestor of HEAD (`git merge-base --is-ancestor`); (d) for EVERY path in `vendored_modules` of `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/BUILD_MANIFEST.json`, the blob of `git show 27acf60210:<path>` is byte-equal to the file of the same base name in that package dir (print the count, expect 11 of 11 or whatever the manifest lists); (e) the pin appears in no other `silver_build_commit` entry.

### ACCEPTANCE

<criterion id="BF6-k6-AC1" cell_refs="BF-k-6"><invocation>python -m pytest data/canonical/schwab/tests/test_schwab_build_pin.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF6-k6-AC1` -- the schwab pin is `27acf60210`, the others are unchanged, the pin is an ancestor of HEAD, and the package dir equals the pin's blobs module by module.

<criterion id="BF6-k6-AC2" cell_refs="BF-k-6"><invocation>python -m pytest data/canonical/schwab/tests/test_firm_prefix_grants.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF6-k6-AC2` -- the control: the Terraform-text tests of the same file (23 passed at the base, including the `terraform fmt` arm) still pass with the edited `silver.tf`.

<expected_criteria>BF6-k6-AC1,BF6-k6-AC2</expected_criteria>

Dry-run at the base: AC1 "file or directory not found" (rc 4) -- FAIL as expected; AC2 `23 passed` -- PASS as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit.
- **WORLD floor, nothing applied.** No `terraform init`, `plan` or `apply`, no `aws` command, no deploy.
- **Refusal clause.** If a criterion cannot be met as written (for example a vendored module is NOT byte-equal at `27acf60210`), stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; read the investigation file for the highest `W1-S<k>` and use the next). Append the row to `org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md` at the BYTE level (do not use the Edit tool on that file: it mixes CRLF and LF; insert before the closing `]` and keep the file's own line endings; the previous last row gains a trailing comma). Do not weaken the test to pass.

<paths>
infra/aws/terraform/opal-assets/silver.tf
data/canonical/schwab/tests/test_schwab_build_pin.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R6.md</decomp_doc> (round 6), cell `BF-k-6`.
<owned_cells>BF-k-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF6-k6-AC1, BF6-k6-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~1/NFRA_SCHWABBF.TO-BF-k6.schwab-build-pin.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF6-k6-AC1,BF6-k6-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the line of the changed pin and of the comment, the count of modules proven byte-equal, the two pytest summary lines, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- Terraform text; the converter is event-driven and the deploy is the release act R3b.
comp-iam: DECLARED-NOT-APPLICABLE -- the cell moves a build-stamp environment value only; it adds no grant (scanned silver.tf for the pin map and its neighbours, 1 Terraform file; BLIND: the live IAM plane).
comp-adversary: DECLARED-NOT-APPLICABLE -- finding: the literal pin goes stale by construction (the file's own comment says so), so the test measures it instead of trusting it.
lane: the <paths> block IS the grant.
</preflight>

Source: row NFRA_SCHWABBF-W5-S5; release plan `deliverables/2.0.0_SA_COO~SB/RELEASE_PLAN_R5_0840_ALL_TIERS.md` act R3b; the pin comment in silver.tf lines 52-110 (rule and precedent: NFRA_OPLGTW OG-ap-5, OG-ap-15).
