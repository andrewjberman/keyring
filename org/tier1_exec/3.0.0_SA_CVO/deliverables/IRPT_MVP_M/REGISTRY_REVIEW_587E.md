# Independent X10 registry and generated-carrier review

**archetype:** VALIDATE

Reviewer: `3.0.0_SA_CVO~M`. Date: 2026-09-22.

**Bounded verdict: PASS for the pending registry/builder candidate and submitted generated-drift discrimination.** Runtime enforcement, owner integration and full S7 remain **NOT_EVALUATED**. No source/generated carrier was changed by this reviewer. This verdict does not activate the reporting policy or substitute CRO/builder-owner sign-off.

Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`, IRPT-S7-03, exact registry grant `820f35ec69`, and CTO generated-carrier disposition in exact inbox `20260922T221037Z_1.0.0_SA_CTO_IRPT_generated_carriers__canonical_owner.md`. Request from COO~M: `20260922T221426Z_2.0.0_SA_COO_M_IRPT_X10__pinned_owner-review_candidate5.md`; ACK delivered before review. Review scope is non-IRPT equality, affected generated consumers and candidate refusals, not implementation or provisioning.

## Current status addendum — 2026-09-22, after 22:34 UTC

This addendum supersedes only the owner-response and R-P07 status below. The original independent review at `eb00a0c6b2`, its test results, historical failure evidence and reproduction script are preserved. No additional tests were run for this documentary update.

- **CRO registry-owner bounded PASS received:** report/evidence `4d6a4338aed7f6a3623b8b3f3c195a19338fd39e`, `org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_X10_REGISTRY_REVIEW_20260922/REVIEW.md`, for pending candidate `587e782bc6` and generated evidence `3c14153eeb` only. Carry alongside this CVO's independent `eb00a0c6b2` review for the bounded builder-owner review. This is attributed owner evidence from the exact CRO 22:34:01 and CTO 22:34:45 notifications, not a new CVO rerun. Subsequent exact CRO notification `20260922T223740Z_4.0.0_SA_CRO_IRPT_X10_final_owner_proof_committed_983.md` supplies final C1-C4 proof and three delivery receipts at LOCAL `983550adde`: canonical bound validation reportedly VALID, rc0, four rows and zero violations, with report content resolved. Invocation alignment is 0/0 comparable because the task criteria are prose; this is not additional test coverage. Proof validation is attributed to CRO and has not been rerun by this seat.
- **R-P07 CLOSED at the tested primitive only:** attributed CVO~P review `9e6a617405`, `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_P/RETENTION_RETEST_C5EA.md`, on source `c5eace08c76176c6d9ebb78dd31ced3b0e57ea2d`. P reports 16 supplied, 9 unchanged reviewer and 12 receipt-boundary tests passing. This supersedes the historical open finding on `bd7c9f1b2c` recorded below; this seat has not independently rerun the replacement primitive. Missing receipt remains non-serving; a timely intent receipt permits restart validation without renewing the retention ceiling, per P's bounded evidence.
- **Outstanding:** naming owner still owes exact generated-carrier disposition and fresh shared-state reconciliation, including separate inherited harvest/formatting drift. CRO owner PASS does not authorize carrier integration or policy activation. Full composed reader/writer retention, concurrency, IAM and S7 remain unproven/NOT_EVALUATED; physical disposal remains OPEN. Product, live, provisioning, deployment and render gates are unchanged.

Authority and requested amendment: exact CTO notification `20260922T223445Z_1.0.0_SA_CTO_IRPT_X10_CRO_owner_PASS4d6a4338ae__R-P07.md`, citing the completion contract above. The historical sections that follow describe the earlier review state; their owner-response and R-P07 statements must be read with this addendum.

## Exact inputs and isolation

| Input | Pin / measurement |
|---|---|
| Candidate | `587e782bc6a1d2e8253b79c689abf51e77b46073` |
| Prechange baseline, including original library and six registry files | `78a48596640f32d908955941a2c52dbb713235c6` |
| Submitted complete carrier diffs and inventory | `3c14153eeb`, COO deliverables `IRPT_MVP_M/GENERATED_CARRIER_DIFFS.md` and `GENERATED_CARRIER_INVENTORY.json` |
| Canonical X10 carrier | `705dae3202cac873a133825bee9d0381c7dd6b7f`, `infra/logic/06_CONFORMANCE_LEDGER.md` section 6 |
| Independent shared-state comparison | `8529764a5d3a5bf924237328a4af87c6243ed07e`, captured before reading its scope blob |
| Reviewer checkout | `C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review`, clean tracked status before switches and after review; final detached HEAD is the exact candidate |

Read the complete candidate note, evidence JSON and generated-diff document at their pins, plus the complete X10 row and its amendment history at the carrier pin. The carrier states twelve families/three firms, conditional placement, pending enforcement, explicit retention boundaries and separate owner/reader/writer obligations. Documentary presence is established; its entire issuance/recount proof is not independently regraded here.

The candidate diff from baseline is six files: canonical library, two registry files, targeted tests and two COO evidence documents. Existing scope rows and every other top-level scope field match both baseline and the measured shared pin after removing the sole new `irpt` row. Systems, tiers, exemptions, remediations and resources blobs are unchanged. The new PRODUCT row is unprovisioned, `opal-data-irpt`, with no aliases. All ten generated source carriers remain byte-identical between baseline and candidate.

## Independent results

| Actual command / instrument | Result |
|---|---|
| Candidate `python -m pytest lib/tests/test_irpt_destination.py -q` | 60 passed in 0.62s |
| Candidate `python lib/opal_naming.py validate` | Exit 0; zero refusals, 43 system rows, 11 scope rows, 33 warnings |
| Candidate `python -m pytest lib/tests/test_opal_naming.py -q` | 88 passed, 5 failed in 6.31s; exit 1 |
| Same naming suite at unchanged baseline | 88 passed, same 5 failed in 5.25s; exit 1 |
| Baseline canonical `generate --out <review-runtime>/registry_587_baseline_generated` | 10 written, 0 skipped, using the actual baseline library and six registry files |
| Candidate canonical `generate --out <review-runtime>/registry_587_candidate_generated` | 10 written, 0 skipped, using actual candidate library and seven registry files |
| Embedded independent comparison probe | 18/18 checks true; 20/20 generated hashes match submitted inventory; 36/36 reporting writer calls refuse; 36/36 previews are private and explicitly non-writable; exit 0 |

The five inherited failing worked cases are `inf-silver-chain|LAMBDA`, `opal-portal-data-proxy-api|API_GW`, `Inflection-SilverChain-DimConversionFailure|CW_ALARM`, `wsb-49f-model-aua-pull-daily|SCHEDULE`, and `inf/otp-relay/token|SECRET`. The two actual runs produce the same failures. They are not a green naming-suite result and were not repaired or attributed to IRPT. The 33 validator warnings are not zero warnings.

Targeted tests cover all 36 family/firm previews and pending write refusals; canonical family/retention census; unknown revision/firm/family, aliases, opaque-ID/path/digest negatives; malformed registry metadata; disabled/missing policy; unchanged default firm homes; independent returned metadata; and the declared compatibility behavior of older non-reporting packages. Their simulated ACTIVE row uses a synthetic enforcement hash to test code paths: it is not an accepted enforcement commit or evidence that runtime may activate. The actual candidate remains PENDING_ENFORCEMENT with enforcement_ref=null.

## Generated consumers and drift

| Exact carrier | Candidate generation minus unchanged-baseline generation |
|---|---|
| `.tools/ds-precommit-check.py` | Stamp-only; Python AST equal |
| `data/assets/scripts/gold/investor_reporting/directory_runner.py` | Stamp-only; Python AST equal |
| `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` | Stamp-only; Python AST equal |
| `data/assets/scripts/gold/runners_49f/perfrp_firm_pin.py` | Stamp-only; Python AST equal |
| `data/firm_registry.json` | Stamp-only |
| `infra/aws/lambda-edge/_shared/firm-config.mjs` | Stamp-only |
| `infra/aws/lambda/investor-reporting/_authz/loaders.py` | Stamp-only; Python AST equal |
| `infra/aws/terraform/modules/opal_name/generated_locals.tf` | Exactly four IRPT map entries plus stamp: short=irpt, long=irpt, class=PRODUCT, bucket=opal-data-irpt |
| `infra/aws/terraform/modules/opal_name/tests/opal_name.tftest.hcl` | Stamp-only |
| `infra/aws/terraform/modules/opal_name/tests/vectors.json` | Stamp-only |

Both hashes for every carrier match the submitted inventory: 20 of 20. Nine deltas are exactly equal after replacing only the 16-hex registry stamp. All five generated Python ASTs also compare equal. Removing the four IRPT mappings from candidate Terraform locals yields the baseline-generated bytes after stamp normalization. Independently, the unchanged-baseline Terraform output differs from its committed source only by four harvest mappings, stamp and whitespace. Thus inherited harvest/formatting drift is demonstrated without IRPT; it is not silently accepted as part of this grant.

No generated output was copied back to source. These generation/syntax/equality results are not a Terraform plan or apply, a package build, or deployed-consumer execution. Canonical naming-owner reconciliation is still required before any generated-source integration; fresh shared-state comparison must be repeated at integration if the inputs move.

## Policy boundary and remaining proof

The independently read policy has exactly three permitted private firms and twelve families, split ten state/two platinum. Policy canonical-row SHA256 is `cb9c4e6e9541fefc315f57844490309ad15c9735593fe3a165b067a3087dc220`; committed policy-file blob SHA256 is `481cc513038b73f5e0444baafea76fc97e3ac9e19624f3f6822fb6f362cacbc3`. File-byte hashes can differ in Windows CRLF checkouts; the semantic policy digest is computed from canonical JSON. Consumers must bind the accepted policy/destination provenance rather than treating a revision label as sufficient.

Current reporting_destination calls refuse all 36 allowed family/firm combinations; preview returns a distinct metadata shape with writable=false. No actual enforcement, retention promotion, source-byte secrecy, IAM/KMS/DynamoDB/S3 version controls, immutable publication, physical disposal or reader/writer cutover is proved by this pending builder. S7 therefore remains NOT_EVALUATED and physical disposal OPEN. Full product, vendor/live, provisioning/deploy and render gates remain unchanged.

Read CTO exact message `20260922T221644Z_1.0.0_SA_CTO_IRPT_registry_review_activation1772d6349.md`: ruling `1772d63490` assigns COO~M issuance of the exact bounded CRO review order, with CRO's sole writable deliverable directory and audited issuance. It does not make this CVO the order issuer or replace independent review. No CRO or builder-owner approval is inferred here; missing owner response returns to CTO.

Related peer evidence, not independently rerun here: CVO~P exact notifications `20260922T221606Z_3.0.0_SA_CVO_P_IRPT_P__S7_primitive_R-P07_expiry-crossi.md` and `20260922T221759Z_3.0.0_SA_CVO_P_IRPT_P__final_R-P07_retention_evidence21.md` report R-P07 P1 on `bd7c9f1b2c`, durable review `217cc1a`: supplied12 PASS, reviewer8 PASS/1 FAIL. A controlled clock crosses reserved expiry before a successful conditional promotion write, yet the artifact becomes/readably remains ACCEPTED. This is scripted transport delay, not actual concurrent/live evidence. P notified its implementer/CTO; this is an outstanding consumer-enforcement finding, not a defect proved in the pending registry builder. Do not use this bounded PASS to activate S7 while that or other enforcement proof is open.

## Reproduction and handoff

Use an isolated checkout at the exact baseline and run the baseline test/generator commands above, writing only to an external review-runtime directory. Switch that checkout to the exact candidate and run candidate commands/output generation. Save the following script as `registry_587_probe.py`, then run `python <probe.py> <workspace-root> <candidate-checkout> <review-runtime>`. The script reads immutable Git blobs and generated output files, imports the actual candidate builder and performs no source mutation. Its shared-state pin is captured before reading the comparison blob. Script SHA256: `7454459111944B2659651BF04A879D4932C30746984672E85455AA1E33B81581`.

Local raw evidence: `.runtime/codex-seats/3.0.0_SA_CVO~M/registry_587_probe.json`, `registry_587_candidate_tests.txt`, `registry_587_baseline_tests.txt`, `registry_587_validate.txt` and the two generated directories above. The full script below makes the reported comparison reproducible without trusting producer booleans.

Compiler routing: comp-which routed contextual reads to bare comp-read; outlines were followed by full pinned files/diffs and the canonical generator/validator. Repository risk-reflex remains an inherited stale-map limitation, not a clean risk-clearance assertion. Push state LOCAL; no push by this seat. Fresh origin CLOUD measured `06a96c4df7568822d6e67e4afb179bd2afc0d20b`. Return this bounded review pin to COO~M/CTO and relevant P/Y reviewers; it is not owner integration permission.

## Reproduction script

```python
"""Independent X10 registry/generator boundary comparison; no source mutation."""
import ast
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

repo, checkout, runtime = map(lambda p: Path(p).resolve(), sys.argv[1:4])
baseline = "78a48596640f32d908955941a2c52dbb713235c6"
candidate = "587e782bc6a1d2e8253b79c689abf51e77b46073"
evidence = "3c14153eeb"


def blob(pin, path):
    return subprocess.check_output(["git", "show", pin + ":" + path], cwd=repo)


def sha(value):
    return hashlib.sha256(value).hexdigest()


def unstamped(value):
    return re.sub(r"registry@[0-9a-f]{16}", "registry@STAMP", value)


inventory = json.loads(blob(evidence, "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/GENERATED_CARRIER_INVENTORY.json"))
observed = {"baseline": baseline, "candidate": candidate, "carriers": [], "checks": {}}
checks = observed["checks"]
scope_path = "infra/logic/registry/scopes.json"
old_scopes = json.loads(blob(baseline, scope_path))
new_scopes = json.loads(blob(candidate, scope_path))
shared_pin = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()
shared_scopes = json.loads(blob(shared_pin, scope_path))
scope_field = next(k for k, v in new_scopes.items() if isinstance(v, list) and v and isinstance(v[0], dict) and "key" in v[0])
without_irpt = json.loads(json.dumps(new_scopes))
without_irpt[scope_field] = [s for s in new_scopes[scope_field] if s["key"] != "irpt"]
checks["all_preexisting_scope_fields_equal_baseline"] = without_irpt == old_scopes
checks["all_preexisting_scope_fields_equal_shared"] = without_irpt == shared_scopes
observed["shared_head"] = shared_pin
for name in ("systems", "tiers", "exemptions", "remediations", "resources"):
    path = "infra/logic/registry/" + name + ".json"
    checks[name + "_unchanged"] = blob(baseline, path) == blob(candidate, path)

for row in inventory["paths"]:
    path = row["path"]
    base_bytes = (runtime / "registry_587_baseline_generated" / path).read_bytes()
    new_bytes = (runtime / "registry_587_candidate_generated" / path).read_bytes()
    before, after = base_bytes.decode(), new_bytes.decode()
    source = blob(baseline, path).decode()
    comparison = {"path": path, "baseline_hash_match": sha(base_bytes) == row["baseline_generated_sha256"],
                  "candidate_hash_match": sha(new_bytes) == row["candidate_generated_sha256"],
                  "source_unchanged": blob(baseline, path) == blob(candidate, path),
                  "candidate_stamp_only": unstamped(before) == unstamped(after)}
    if path.endswith(".py"):
        comparison["python_ast_equal"] = ast.dump(ast.parse(before)) == ast.dump(ast.parse(after))
    if path.endswith("generated_locals.tf"):
        irpt_lines = [line.strip() for line in after.splitlines() if re.match(r'\s*"irpt"\s*=', line)]
        comparison["irpt_only_four_mappings"] = len(irpt_lines) == 4 and (
            unstamped(before) == unstamped("\n".join(line for line in after.splitlines()
                if not re.match(r'\s*"irpt"\s*=', line)) + "\n"))
        comparison["irpt_lines"] = irpt_lines
        minus_harvest = "\n".join(line for line in before.splitlines() if not re.match(r'\s*"harvest"\s*=', line))
        comparison["baseline_drift_only_harvest_stamp_whitespace"] = (
            re.sub(r"\s+", "", unstamped(source)) == re.sub(r"\s+", "", unstamped(minus_harvest)))
    observed["carriers"].append(comparison)
checks["ten_exact_carriers"] = len(observed["carriers"]) == 10
checks["all_generated_hashes_match"] = all(r["baseline_hash_match"] and r["candidate_hash_match"] for r in observed["carriers"])
checks["all_source_carriers_unchanged"] = all(r["source_unchanged"] for r in observed["carriers"])
checks["nine_stamp_only_deltas"] = sum(r["candidate_stamp_only"] for r in observed["carriers"]) == 9
checks["python_consumer_ast_equality"] = all(r.get("python_ast_equal", True) for r in observed["carriers"])
tf = next(r for r in observed["carriers"] if r["path"].endswith("generated_locals.tf"))
checks["terraform_only_irpt_delta"] = tf["irpt_only_four_mappings"]
checks["harvest_drift_independently_inherited"] = tf["baseline_drift_only_harvest_stamp_whitespace"]

spec = importlib.util.spec_from_file_location("review_naming_587", checkout / "lib/opal_naming.py")
naming = importlib.util.module_from_spec(spec)
spec.loader.exec_module(naming)
policy = naming.reporting_policy("irpt-x10-v1")
expected_families = {"ORIGINAL_CSV", "NORMALIZED_PORTFOLIO", "REQUEST_COMPOSITION", "ORIGINAL_VENDOR_PDF",
    "EXTRACTION_EVIDENCE", "PERFORMANCE", "ANALYSIS", "EXPORT_BUNDLE", "EXPORT_PDF", "EXPORT_RECEIPT",
    "SELECTED_ACCOUNTS", "PERFORMANCE_SOURCE_EVIDENCE"}
checks["exact_family_and_firm_sets"] = set(policy["families"]) == expected_families and set(policy["firms"]) == {"49financial", "cottonwood", "inflection"}
checks["pending_enforcement_no_reference"] = policy["state"] == "PENDING_ENFORCEMENT" and policy["enforcement_ref"] is None
checks["ten_state_two_platinum"] = sum(s["tier"] == "state" for s in policy["families"].values()) == 10 and sum(s["tier"] == "platinum" for s in policy["families"].values()) == 2
refused, previews = 0, 0
for firm in sorted(policy["firms"]):
    for family in sorted(expected_families):
        args = (firm, family, "ART-" + "a" * 64, "b" * 64)
        p = naming.preview_reporting_destination(*args, policy_revision="irpt-x10-v1")
        previews += p["writable"] is False and p["bucket"] == "opal-data-irpt" and p["key"].startswith("irpt/" + firm + "/")
        try:
            naming.reporting_destination(*args, policy_revision="irpt-x10-v1")
        except ValueError:
            refused += 1
observed["pending_writer_refusals"] = refused
observed["nonwritable_private_previews"] = previews
checks["all_36_writers_refused_and_previews_private"] = refused == previews == 36
observed["policy_sha256"] = policy["policy_sha256"]
observed["policy_file_sha256"] = sha(blob(candidate, "infra/logic/registry/reporting_policies.json"))
observed["failures"] = [k for k, v in checks.items() if not v]
print(json.dumps(observed, indent=2))
raise SystemExit(bool(observed["failures"]))

```
