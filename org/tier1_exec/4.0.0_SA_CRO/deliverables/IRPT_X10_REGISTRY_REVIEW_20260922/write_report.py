from pathlib import Path
import json

r = Path(__file__).resolve().parent
manifest = json.loads((r / "evidence/input_manifest.json").read_text())
p = manifest["pins"]
checks = json.loads((r / "evidence/semantic_checks.json").read_text())
gen = json.loads((r / "evidence/reproduction.json").read_text())
policy = json.loads(
    (r / "snapshots/candidate/infra/logic/registry/reporting_policies.json").read_text()
)["policies"][0]
text = """# IRPT X10 registry-owner review

**Bounded owner verdict: PASS for the exact PENDING_ENFORCEMENT registry candidate and the submitted generated-change classification.** This approves the reviewed registry semantics only. It does not authorize an ACTIVE policy, generated-carrier integration, provisioning, deployment, or product acceptance.

Reviewer: `4.0.0_SA_CRO`, September 22, 2026. Executed under COO~M's committed `IRPT-X10_REGISTRY_REVIEW_20260922` order. All review writes are inside this deliverable directory; no source, shared generated carrier, ledger, IAM, runtime or vendor state was modified.

## Exact inputs and provenance

| Input | Full immutable pin |
|---|---|
"""
for key in [
    "order",
    "baseline",
    "candidate",
    "generated_evidence",
    "x10",
    "ruling",
    "grant",
]:
    text += f"| {key} | `{p[key]}` |\n"
text += f"| Independent CVO~M review | `{checks['peer_pin']}` |\n| Fresh shared source comparison | `{checks['fresh_shared_pin']}` |\n"
text += """
Inputs were read from Git objects in `C:/Users/AndrewBerman/Desktop/ajb_irpt_m`, not its mutable working files. The candidate's direct parent is the specified baseline. The baseline contains byte-identical grant blobs and the same CTO author as original grant `820f35ec69`. The pinned X10 row is the twelve-family amendment, not the earlier eleven-family grant. The policy's abbreviated ruling reference resolves to the exact reviewed ruling; its register reference is already a full hash.

`evidence/input_manifest.json` records extracted input hashes. `evidence/source_diff.patch` preserves the complete reviewed implementation/test/registry delta. The candidate changes six files: library, two registry files, targeted tests, and two producer-evidence documents. Removing only the new `irpt` row makes the entire scopes document equal to baseline and the captured shared pin. The five other incumbent registry blobs are byte-identical. The existing library functions changed are only `load_registry` and `validate`; five new reporting-specific functions are added. Existing `key`, `address`, `name`, grade and generator function bodies are unchanged.

Fresh shared-library comparison matches the prechange baseline. This is a measured point-in-time check, not permission to overwrite later shared changes; the naming owner must reconcile again immediately before integration.

## Policy semantics and current boundary

The sole added scope is PRODUCT `irpt`, long/short `irpt`, bucket `opal-data-irpt`, `bucket_provisioned=false`, no aliases. It does not change any firm's default home. The reporting policy is `irpt-x10-v1`, cites canonical X10, uses source/product `irpt`, and admits only `49financial`, `cottonwood`, and `inflection`. It is `PENDING_ENFORCEMENT`, `enforcement_ref=null`, with physical disposal `OPEN`.

| Family | Class/table | Format | Unreferenced days | Accepted original-creation ceiling |
|---|---|---|---|---|
"""
for family, s in policy["families"].items():
    draft = (
        "accepted-only"
        if s["unreferenced_days"] is None
        else str(s["unreferenced_days"])
    )
    text += f"| `{family}` | `{s['tier']}/{s['table']}` | {s['extension']} | {draft} | {s['accepted_ceiling_days']} days |\n"
text += f"""
Exactly twelve families: ten state and two bounded platinum JSON report families. Policy file SHA256: `{checks["policy_file_sha256"]}`. Canonical policy-row SHA256: `{checks["policy_sha256"]}`. The two hashes have different denominators; consumers must bind the accepted row digest and revision in records rather than treating the revision label alone as sufficient.

The review independently exercised 36 of 36 allowed family/firm writer calls: all refused while pending. All 36 previews returned a distinct mapping with `writable=false`, the product bucket, canonical private firm key prefix, and the same policy digest. Seven additional unknown-scope/alias/demo/family/path/digest/revision inputs refused. Nine default Gold/Platinum/state firm-home calls remained in their respective long-form firm buckets. The metadata accessor rereads and returns an independent parsed record; this does not constitute reader/writer authorization enforcement.

## Conditions: recorded versus enforced

| X10 condition | Candidate state | Remaining evidence / owner |
|---|---|---|
| Exactly twelve families, three private firms, ten state/two platinum | Recorded in the pinned policy; census and pending paths exercised | Any policy revision needs renewed authoritative review; this verdict covers only the pinned bytes |
| No writable reporting destination before enforcement | Enforced by the current reporting writer API for all 36 admitted pairs | Keep pending until accepted enforcement and coordinated composition exist |
| Private owner/firm isolation and current account/prospect authorization before and after retrieval | Long-form firm key scope enforced; caller authorization is not implemented in this builder | P and CVO must prove actual request, persistence and retrieval boundaries |
| Server-only validated registry/builder addresses and opaque IDs/digests | Input shape, registered scope/family and canonical key composition exercised | Shape validation does not prove who issued an ID; server authority and consumer use remain P/M integration proof |
| Original provider bytes separate from redacted receipt; no credentials/cookies/auth headers or false original-byte hashes | State family and JSON representation recorded, full rule retained through X10/ruling | Actual provider writer/secret handling and byte/hash provenance remain P/CVO obligations |
| Immutable accepted object version and exact hash; interrupted inaccessible objects never published | Digest appears in naming interface; no storage operations here | P/CVO must prove versioned reads/writes, immutable publication and failure recovery |
| 30-day unreferenced inputs/selections; 7-day unfinished exports; fixed 2555-day ceilings | Correct family metadata in all twelve rows; selected-account ceiling remains 30 | P must enforce original-creation clocks, not a sliding TTL |
| Report/export expires by earliest required dependency; frozen selection provenance with fresh current authorization | Recorded in X10/ruling and producer design note; no dependency/minimum calculation in registry | P/CVO must prove dependency pinning, minimum expiry, selection freeze and authorization |
| Conditional promotion refuses expired evidence; no renewal by read/retry/copy/report creation; clock/race safety | Recorded; not executed by naming builder | Controlled-clock and actual repository-path evidence still required |
| Least privilege, IAM/KMS/DynamoDB/S3 version controls | No IAM or deployed boundary implementation in this candidate | P/CVO evaluation and negatives remain separate |
| Same accepted policy revision/digest across every reader/writer; no fallback/dual write | Row digest available; pending state prevents this API issuing writer tuple | Coordination and each consumer's comparison are not demonstrated here |
| Canonical custody/directory/model/holdings homes and upstream processing unchanged | Incumbent registry equality and nine default-home calls verified | No custody migration or upstream processing waiver |
| Physical disposal OPEN; no indefinite-storage approval, cleanup, lifecycle activation or deployment | `physical_disposal=OPEN`; no such operations executed | Reference-aware disposal design and separately authorized execution remain outstanding |
| Exception ends on CTO supersession, product retirement or failed conditions; disable and route failure | Exact X10 end conditions remain authoritative; DISABLED path covered by producer test | Operational review/revocation and in-flight consumer behavior remain unproven |

`ACTIVE` validation currently checks the shape of an enforcement reference, not that the referenced commit contains accepted enforcement. The synthetic forty-character hash in the producer test exercises that code path; it is not evidence of accepted enforcement. Likewise, the validator is a schema/metadata check, not an oracle for whether a newly edited family list or policy revision has been adjudicated. This bounded owner approval is for the submitted pending record only; future edits require the canonical policy/owner process. These limits do not imply current activation.

No divergence was found in the admitted pending row, exact family metadata, retained X10 authority, current pending-write boundary, non-IRPT equality or generated-change classification. Deferred runtime controls are explicitly not graded as implemented.

## Generated carriers: independent baseline and candidate runs

Both canonical generator invocations used their own exact pinned library and registry inputs in isolated extracted review snapshots; no generated output was copied to source. Each wrote ten carriers with zero skips. All twenty output hashes match the submitted inventory. All ten committed source carriers are byte-identical between baseline and candidate.

| Carrier | Baseline-source to baseline-generation | Baseline-generation to candidate-generation |
|---|---|---|
"""
for item in gen["generated_carriers"]:
    inherited = (
        "none"
        if not item["inherited_drift"]
        else "stamp only"
        if not item["inherited_nonstamp"]
        else "harvest mappings + stamp + whitespace"
    )
    delta = "stamp only" if item["irpt_stamp_only"] else "four IRPT mappings + stamp"
    text += f"| `{item['path']}` | {inherited} | {delta} |\n"
text += """
Nine candidate deltas are equal after removing only the 16-hex registry stamp. All five generated Python ASTs are equal. `generated_locals.tf` adds exactly four IRPT map values: short `irpt`, long `irpt`, class `PRODUCT`, bucket `opal-data-irpt`. Removing those four lines restores baseline-generated bytes after stamp normalization. Independently, removing four harvest mappings from baseline generation and normalizing stamp/whitespace restores the committed baseline source. Harvest and formatting are therefore inherited; this review does not authorize silently repairing them with IRPT.

Proposed naming-owner inventory: reconcile the nine stamp-only carriers as such; treat the four IRPT Terraform entries as the only candidate semantic additions; separately disposition inherited harvest/formatting drift. Recheck current shared source before integration. This is an inventory for the owner, not integration authority, Terraform plan/apply evidence or consumer deployment proof. COO~G's assignment and CVO~M's review remain separate.

## Actual verification and coverage limits

| Instrument | Result |
|---|---|
| Exact candidate targeted pytest suite | 60 passed, exit 0 |
| Exact candidate canonical `validate` | Exit 0; 43 systems, 11 scopes, zero refusals, 33 inherited warnings |
| Baseline and candidate canonical `generate` | Each ten written, zero skipped; 20/20 hashes reproduced |
| Independent `semantic_checks.py` | 34/34 checks true; 36 writer refusals, 36 private previews, seven negative refusals |
| Naming core suite, both pins | Each 80 passed, same five failed, eight deselected; exit 1 |
| Independent CVO~M full naming-suite evidence | Reports each 88 passed / same five failed; not rerun in a full Git checkout by CRO |

The eight excluded full-suite tests depend on deployment/source-map or tracked Terraform-plane fixtures outside the extracted snapshot. CRO's initial attempted full run had eleven additional missing-fixture failures in both snapshots; those are harness incompleteness, not inherited product defects. The initial targeted run also lacked its temporary-directory parent; after correcting that review harness, all sixty tests passed. Initial outputs are retained as audit evidence, not quoted as candidate failures. The reproducible core run includes the pinned legacy-path list, runs 85 of 93 naming cases, and has exactly these five inherited failures on both pins:

- `inf-silver-chain|LAMBDA`
- `opal-portal-data-proxy-api|API_GW`
- `Inflection-SilverChain-DimConversionFailure|CW_ALARM`
- `wsb-49f-model-aua-pull-daily|SCHEDULE`
- `inf/otp-relay/token|SECRET`

They are not a green naming-suite result and were not repaired. Independent CVO evidence is preserved in `evidence/peer_CVO_REVIEW.md` at the pinned review commit above. It independently reproduces the full 93-case baseline/candidate result and the generated evidence. It also reports the separate P-lane expiry-crossing finding R-P07 as open; CRO did not rerun that consumer finding. Neither this owner PASS nor the CVO's bounded candidate PASS clears it.

## Durable evidence and handoff

`review_checks.py` reconstructs the pinned input snapshots and generators inside this directory; its final core-suite invocation explicitly deselects the eight out-of-snapshot deployment/plane tests. `semantic_checks.py` performs the independent policy, provenance, shared-source, refusal and generated-semantic checks. `evidence/input_manifest.json`, `reproduction.json`, `semantic_checks.json`, `core_naming_results.json`, raw command outputs and per-carrier diffs carry denominators and hashes. Temporary snapshots/pytest scratch need not be committed: the pinned Git references and scripts reconstruct them. No external website, live AWS operation or vendor call was used.

C1: exact pins, baseline/grant lineage and authoritative X10 verified. C2: bounded pending registry semantics PASS; runtime conditions remain recorded obligations. C3: non-IRPT equality and all ten carriers classified independently. C4: this report and its proof are committed and returned by canonical messaging to COO~M, CTO and CVO~M; delivery receipts identify the immutable report pin.

Session record: this report is the bounded review log. Repository pre-commit risk-map output, if stale, is not a clean clearance; the explicit reads, hash checks, generator runs and tests above are the evidence. No source repair or product PASS is asserted.
"""
(r / "REVIEW.md").write_text(text, encoding="utf-8")
print("REVIEW.md written: bounded pending-candidate PASS.")
