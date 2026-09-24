# R no-span repair: review and never-widen packet

Candidate status: local; routine review C, boundary review CVO, CTO+COO pair all pending. No deployment. This packet narrows the incident repair to the two functions that turn retained D-1 sentences into served drafting output.

## Writer census, with grains separated

`WRITER_CENSUS.json` scans all 126 Python files in the actual deployed ZIP (3 matching files, zero parse failures), and 3,900 candidate `lib`/`infra` Python files (16 matching files, zero parse failures). Matching function bodies and call expressions are retained. The served graph compiler did not contain this function; its NOT-FOUND was not used as proof of no callers.

**N = 1 nonempty drafting-section materializer:** `read_drafted_sections`. `_drafting_block` is the one literal writer of the `drafted_sections` response key. Its four callers are all within `read_drafted_sections`: three empty ABSENT/INVALID branches and one SERVED branch. The filter sits before that single nonempty branch.

**N = 2 production consumers / API output routes:**

1. `handler /security/{key}/thesis -> read_thesis_bundle -> read_drafted_sections` emits full drafted sections.
2. `handler /security/{key}/overlay -> read_security_overlay -> read_description -> read_drafted_sections` can emit a drafted company-description sentence if Bloomberg description scalars are absent and the business-description rule passes.

Both cross the repaired reader. No production caller supplies `read_description(drafting=...)`; that injection exists in offline tests. The added positive/negative description tests use the real reader and prove a business-valid unanchored sentence is held while its anchored counterpart is preserved. `read_description`'s Bloomberg-scalar branch is a separate source and remains unchanged.

The `/print` route delegates to `lib/research/print/render_pack.py`: its recommendation/company/thesis/risk/bio paragraphs are literal MACHINE-EMPTY markers; it does not load D-1 prose. This is still an MVP gap, not a third D-1 serving bypass. `posture/packs.py` separately consumes raw D-1 text as model evidence; `judge.py` stores pack summaries and separate posture assertions. That upstream evidence pathway is not repaired by this reader change and merits follow-up; it is not counted as a direct D-1 section emitter. Do not broaden this packet into a claim that every generated assertion everywhere now passes this gate.

## Exact artifact and change bounds

`REPAIR_PACKAGE.json` pins the deployed ZIP and candidate ZIP. Build replaces only `_drafting_block` and `read_drafted_sections` in the deployed API member. Both original function sources equal the repository pre-repair versions. Of 197 ZIP members, exactly ONE changes; all other member bytes match. AST comparison confirms only those TWO function bodies change; all other module AST nodes are identical. This avoids deploying unrelated repository-versus-live drift.

Candidate ZIP SHA256 hex: `0c44108821fe52850c77b119490039453b082c3639fae6dbf58de054b1397a55`.
Candidate API member SHA256: `6c98b25ba5cf51558d3c28db1f9e0fecf5acef1aefeb5c3b3cdc896fefb29a38`.
Build and saved rollback artifacts: `C:/tmp/amgt-r-no-span-package-20260923/`.

No IAM, routing, schedule, model invocation, source data, retained S3 object, figure policy, or producer configuration changes. New response fields count producer-held and reader-held no-span sentences separately from uncited holds. Portal rendering of these counters remains an open consumer gap.

## Evidence and limits

Full candidate API regression: 225 tests passed before the two added consumer controls; focused drafting suite with those controls: 32 passed. Final full-suite result is recorded in REPAIR_CHECKS.json. Ruff passes. `REPAIR_REPLAY.json` and `PACKAGE_REPLAY.json`: all twelve exact retained S3 versions; 210 anchored sentences preserved in exact text order, 179 held, zero no-span output, unchanged source hashes. Package replay imports first-party code from the exact candidate ZIP on Windows Python 3.11 with host jsonschema; it is explicitly not a Lambda Linux runtime test. Dependency members are unchanged from the running package.

`AUTH_BOUNDARY.json` pins the actual authorizer and edge20 artifacts. Their inspected policies admit ordinary valid portal JWTs on AMGT, subject to the origin check and required firm identity; they do not impose an engineering-only condition. Do not paraphrase this as every authenticated identity regardless of firm/header validity. No authenticated browser journey or human viewing is measured.

## Cutover requested for review, not yet approved

Request C routine review of the source/tests and CVO independent acceptance of the exact artifact/retained-byte behavior. Request CTO and COO never-widen halves for this exact two-function, one-member delta, with both served routes named. Before applying a reviewed artifact, recheck live package hash and RevisionId against the packet; refuse changed baseline. Use the pinned candidate ZIP, preserve function configuration, then verify deployed package hash, the twelve GET results, missing-firm 401, and overlay behavior. Independent post-deploy acceptance remains required before disarming S236.

The saved original ZIP is a recovery artifact, but reverting it reintroduces the known incident. Any rollback decision must state that consequence; a hash match to the old ZIP is not a safe-state assertion. A deployed failure is escalated with its measured boundary rather than silently replaying old content.

## Evidence capture correction

Revoked local evidence commit 84ba660442 contained an origin custom-header value. Replacement fa65082078 redacts the field. R verified every CustomHeaders item at the replacement commit has the redaction marker; no value is reproduced here. MSTR reports fresh origin-branch/ref and local ancestry checks found no propagation. The old local Git object may persist; redaction does not revoke a credential. CTO24873 closes the git-axis exposure as local-only and would reopen it on evidence of another reader or remote propagation. No credential rotation was performed by R.

## Other R queues

H03 infrastructure packet sent to CloudOps; H producer ac4316c447 has reported routine review d8cf72e32a. CTO24857 supersedes the earlier proposed refusal plumbing: own S3 errors are not publisher refusals, and only legacy daily DENIED rows are candidates for the separately ratified NO_COVERAGE migration. No enum edit or cutover is authorized here. H02 review of 4f3fdff0d5 is NOT_EVALUATED, queued behind this incident; C's earlier f0883a85fc review is evidence, not a substitute for the newly assigned R review. I4 consumption at d382f2a30e remains open. The amended reviewer cycle is H reviews C, R reviews H, C reviews R until S activates.
