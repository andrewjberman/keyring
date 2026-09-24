# COO never-widen half: exact no-span serving repair

SIGNED by `2.0.0_SA_COO~Z`, 2026-09-23. This is the COO review half for the single act of deploying the exact candidate code package to `opal-amgt-scoped-api`. It completes the pair with CTO's half as amended at `83e9f90be5` and `3b4083a685`; CVO cutover acceptance still follows. No deployment was performed by this review.

## Artifact bound

| Item | Exact identity |
|---|---|
| Repair and packet | `dd91fd3126318f1056b0e5f426e855d84ee0d424` |
| Candidate ZIP SHA256 | `0c44108821fe52850c77b119490039453b082c3639fae6dbf58de054b1397a55` |
| Candidate CodeSha256 | `DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=` |
| Baseline CodeSha256 | `r93CxQqrk8k8h2Q8KO4Iicn3pk8kyF4SFo47a9Cca5w=` |
| Baseline RevisionId from packet | `d906e911-aed5-4e21-afcd-0b9a6dcdbdc7` |
| Changed member | `lib/research/api/scoped_amgt.py` |
| Changed functions | `_drafting_block`, `read_drafted_sections` |

Different package bytes or a changed live baseline require renewed review. The deployer must remeasure live CodeSha256 and RevisionId immediately before applying the artifact. This review did not claim that the live baseline remains unchanged.

## Independently measured bounds

`review_exact_package.py` imported the candidate ZIP's first-party code in an isolated temporary directory, not the producer's working tree. It independently checked both ZIP hashes, 197 identical member names with exactly one changed member, two changed function ASTs, all other module AST nodes identical, repaired functions equal the pinned source and original functions equal the pre-repair source.

The packaged-code census parsed all 126 Python files with zero parse failures. There is one literal `drafted_sections` writer, `_drafting_block`, called four times by the one materializer `read_drafted_sections`; three branches emit empty lists and one emits filtered sections. Two production consumers cross the reader: thesis bundle and overlay description fallback. The packaged caller of `read_description` supplies no injected drafting. The packet's wider repository census is producer evidence, not a separately rerun 3,900-file claim by this seat.

**Both branches measured:** reexecuting the pinned replay script against all 12 exact retained S3 versions through the exact candidate code preserved 210 anchored sentences in order and held 179 spanless sentences: 389 total, zero spanless sentences served. Each source hash matched the pinned census and remained unchanged. The 179 is a pooled total, not a per-document count.

**76 focused tests passed, zero skipped.** These cover drafting validation and missing/blank spans, both served consumers, description positive/negative controls, route mounting, scoped API behavior, and identity boundaries. Tests and ten repository-only fixtures were taken from the exact source pin; packaged runtime code was not replaced with repository code. Earlier harness failures were missing non-runtime fixtures; adding the pinned fixtures resolved them. This is Windows Python 3.11 with host jsonschema, not a Linux Lambda or authenticated browser test. The producer's full-suite count is not this seat's test count.

Evidence beside this half: `EXACT_PACKAGE_REVIEW.json`, `EXACT_PACKAGE_RETAINED_REPLAY.json`, `EXACT_PACKAGE_PYTEST.txt`, reproducible `review_exact_package.py`.

## Scope and failure handling

This half reaches only this one code-package change and the thesis/overlay output paths it repairs. It permits no retained-object rewrite, source rewrite, schema change, vendor call, S3 delete, credentials/configuration/IAM/routing change, or unrelated package refresh. Raw-D1 posture inputs, machine-empty print prose and portal rendering of the new counters remain separate work.

CTO amendment 2 supersedes its original unconditional rollback. The old ZIP restores the known defect and is not a preauthorized fallback. Failure to hold requires fixing forward; a serving regression requires failing closed on the affected route through the authorized cutover owner. An availability-versus-known-violation trade requires Andrew's contemporaneous decision. No endpoint was disabled by this review.

CVO must accept the cutover after this pair. Deployed hash, all twelve served GETs, missing-firm 401, and both overlay controls remain post-deploy obligations. No live acceptance or incident closure is claimed here. This half expires on successful completion of the named act; changed artifact/baseline or a failed cutover cannot silently reuse it for another act.
