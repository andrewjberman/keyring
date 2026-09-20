# NEVER-WIDEN SIGN-OFF PACKET (v2) -- IRPT_BCKEND.TO-IB-rtf-13

**SUPERSEDES** the v1 packet (worker dir, blob `fb833bc620b479e6d3393529fa571e829878ada5`) ON ITS ARM-(d) GATE ONLY,
per `1.0.0_SA_CTO`'s ruling @`0a7f61ae86` (msg 98440) on `2.0.0_SA_COO~B`'s W1-S37 pitch. The ACT, the KEYS, the
BLAST RADIUS, the ROLLBACK and the substantive delta are UNCHANGED from v1 and restated here so both halves bind to
one current blob. Re-cut by the issuer (`2.0.0_SA_COO~B`) because the v1 author `0.9.0_WK_IRPT_BCKEND~1` is terminal;
this file lives in the issuer's deliverables and the amended order arm (d) names it by this path.

**WHY v2 EXISTS -- and it is a WIDENING, said out loud (NEVER-1 turns on this axis).** v1's arm (d) STOPPED on
`saved-plan canonical digest EQUAL to sha256:fda208df...`. That gate is not stale -- it is **UNSATISFIABLE ACROSS
COLD-STARTED PASSES BY CONSTRUCTION**: the apply pass necessarily re-plans after the halves are signed, `.scratch`
does not travel to a fresh worktree, and a `terraform plan` captures per-run volatile fields (an S3 data-source's
`version_id`/`last_modified`; the plan's own `.timestamp`). Measured second pass, W1-S37: 0 of 9 hashing instruments
reproduced `fda208df`. A whole-planfile digest admits the **EMPTY SET**. Moving off it therefore **WIDENS the
admitted set** in the only sense the never-widen law measures -- this is NOT a "narrowing," and calling it one is the
shape that gets signed without anyone counting what it lets through. It is bounded below.

## THE ARM (d) GATE -- BY SUBTRACTION (the ruled construction, `1.0.0_SA_CTO` @0a7f61ae86)

Arm (d) does NOT compare a whole-planfile digest, and does NOT check a forward list of fields (a field list fails
OPEN on a new field -- a plan that changed the function's `role` or `environment` would satisfy a code-deploy field
list exactly). It compares, per root, the **`resource_changes` object of `terraform show -json <planfile>`, WHOLE,
with a CLOSED and PRINTED volatile set SUBTRACTED**:

  SUBTRACTION SET (closed; a SIGNED TERM; nothing added without a re-signature):
    (i)  the plan's own top-level `.timestamp`;
    (ii) the S3 data-source's `version_id` and `last_modified`, wherever they appear in `prior_state` /
         `relevant_attributes`.

Everything else in `resource_changes` is IN the gate BY DEFAULT. **A field that appears in a future plan and is not
in the subtraction set BREAKS the gate (fails CLOSED) rather than slipping through it.** The gate PRINTS both halves
of its own denominator every run: `resource_changes` entries compared, and paths subtracted. A subtraction whose
denominator is not printed is a forward list wearing better grammar.

**COVERAGE -- option (a), all seven roots** (`1.0.0_SA_CTO`'s REC, the cheapest assertion and the half of the radius
most likely to move silently): the gate is taken over ALL SEVEN investor-reporting roots. The `directory` root must
show, after subtraction, EXACTLY the one substantive change below (its sibling `irpt_directory_refresh` `no-op`); the
six other roots (`export`, `holdings`, `intake`, `narrative`, `ops`, `performance`) must each show an EMPTY
`resource_changes` after subtraction (`"No changes"` / all entries `actions ["no-op"]`). Any other content on any
root is a STOP.

**THE SUBSTANTIVE CHANGE (unchanged from v1; this is what the gate must find on the directory root, minus the
subtraction set):** `module.irpt_directory_search.aws_lambda_function.this` -- `actions ["update"]`,
`before.source_code_hash = PUjH3OjDe8Yj3RwdIO0KT3GXsYGfvUCmzG/aHsi6e1c=` (== the prior live `CodeSha256`, the
rollback target), `after.source_code_hash = 76LeVyYNfhdyDnQNXR3LzrqSv7k7Vr3POSjpcBzww6E=` (== the built,
verified-at-rest artifact); `0 to add, 0 to destroy`.

**THE BOUND ON EVERY SIGNATURE (`1.0.0_SA_CTO`'s, adopted):** the signers sign a gate none has seen run. If the
re-cut gate REFUSES on the first apply pass, that refusal is **EVIDENCE, not an obstacle** -- the subtraction set is
incomplete; the remedy is to measure the new field, ROW it, and RE-SIGN. **NEVER widen the subtraction set at the
terminal to make the pass go through.** The subtraction set above is a signed term.

## THE ACT

Deploy `irpt-directory-search` with ONE new packaged member -- `contracts/DirectoryEntry.schema.json`, staged at
build time from the COMMITTED, sha256-verified blob of `docs/contracts/investor-reporting/v1/DirectoryEntry.schema.json`
(pin `6e764ef0aa48a01f922931d66413477a2eff05a4`, sha256 `7ed220ff87a787c6b596bcc66bc90a8a5a69fe2ec7da88e145207297011aab24`,
12967 bytes) -- plus ONE Terraform environment line, `IRPT_CONTRACTS_DIR = "/var/task/contracts"`, on the `directory`
root. No other function's bytes are touched by this act; no other route deploys; no `_authz/`, `_scope/`, `_ids/`,
`directory/` SOURCE file is edited.

## THE KEY -- THE ONE SERVING FUNCTION'S BYTES

`N = 1`. Only `irpt-directory-search` gains this member; arm (a)'s census (13 functions x sites; `battery_ib_rtf_13.py`)
confirms no other of the 7 serving functions' `staged_from`/`files[]` is touched by this act.

| # | function_name | prior `CodeSha256` (rollback target, read live) | LastModified (live) |
|---|----------------|--------------------------------------------------|----------------------|
| 1 | irpt-directory-search | `PUjH3OjDe8Yj3RwdIO0KT3GXsYGfvUCmzG/aHsi6e1c=` | 2026-09-19T17:15:28Z |

The ROLLBACK is "re-publish this exact `CodeSha256`" (Terraform `filename`/`source_code_hash` pinned back to the
pre-deploy zip; NEVER `aws lambda update-function-code`, CLAUDE.md NEVER-9). The build-store rollback source (the S3
object version under `investor-reporting/irpt-directory-search.zip` BEFORE this order's build ran) is
`VersionId=elK9Z3qtolvKrVJhSuMrmlFJZT.77_Dk`, `LastModified=2026-09-19T18:54:54Z`.

**BUILT** (K-CODE): `CodeSha256`/`artifact_sha256` `76LeVyYNfhdyDnQNXR3LzrqSv7k7Vr3POSjpcBzww6E=`, 128K, via
`infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-directory-search`. **VERIFIED AT REST**: the built
zip downloaded from S3 and re-hashed matches the declared `artifact_sha256` (`match=True`); 13 of 13 declared members
byte-equal to their declared blob (the pinned commit for a `staged_from` member, HEAD `19ccf82226` for a
directly-tracked one) -- **never the working file** (this box has `core.autocrlf=true`). The served-byte delta
against the prior 12-member set is EXACTLY the one added member, `['contracts/DirectoryEntry.schema.json']` -- `m = 1`
of 1. `import-closure`: 9 of 9 packaged `.py` files' top-level imports satisfied. **The apply pass RE-VERIFIES the
artifact is the latest at `76LeVyYN...` before applying** (an idempotent rebuild is expected; the gate above does not
turn on the build's byte-identity, only on the substantive `source_code_hash` transition it produces).

## THE CONTRACT DESCRIBED

`DirectoryEntry.schema.json`: a JSON Schema document (`$schema: https://json-schema.org/draft/2020-12/schema`), 12967
bytes, 9 top-level `properties`. Zero credential fields; zero secrets; zero PII beyond what a DirectoryEntry document
already legitimately carries in the projected response it types (this member is the SCHEMA, not data). Writers of
this file at its repo path: the L4 PRD/contract-authoring track only (`docs/contracts/investor-reporting/v1/`) -- this
order does not edit it, only stages a build-time copy of the committed blob.

## THE BLAST RADIUS -- BOTH BRANCHES

**`irpt-directory-search`'s wiring:** v1 claimed "DEPLOYED UNWIRED, direct-invoke only"; that claim is CONTRADICTED by
measurement and this packet does NOT rely on it -- rtf-12's arm (f) sent real HTTP through
`https://opalinvest.dev/api/scoped/investor-reporting/directory/*` at 17:31Z and reached `irpt-directory-search`
under `irpt-directory-role`. So the radius is the WIDER, request-reachable one, which covers the narrower.

  * **INVOKED, WITH the member and the env (forward branch).** `directory/entry.py:74-83` `_document_fields()` finds
    `contracts/DirectoryEntry.schema.json` under `IRPT_CONTRACTS_DIR` (`/var/task/contracts`), reads the 9 declared
    properties, and `search()`/`resolve()` answer BY POLICY (a projected document set, or a refusal on the declared
    reason codes `UNPROJECTED_GRANT`/`EMPTY_GRANT`/`INVALID_INPUT`) -- never `RuntimeError: BLOCKED` for this cause.
    Row `S103`'s fix.
  * **INVOKED, WITHOUT the member (as today, the negative control / rollback state).** The same call raises
    `RuntimeError: BLOCKED: the DirectoryEntry contract is not readable from this runtime`, uncaught by `entry.py`,
    propagating to `_authz`'s dispatcher as `UNEXPECTED`. A rollback is a return to this branch, not a NEW failure.
  * **UNAFFECTED.** Every other function's served behavior (0 of 6 other functions' manifests touched); the
    `directory` root's OTHER resource `irpt-directory-refresh` (`no-op` in the plan); the 28 existing CloudFront
    behaviors and 14 pre-existing scoped routes (none reference this function).

## ROLLBACK

Re-publish `irpt-directory-search` at `CodeSha256` `PUjH3OjDe8Yj3RwdIO0KT3GXsYGfvUCmzG/aHsi6e1c=` via Terraform
(`filename`/`source_code_hash` pinned to the pre-deploy zip, build-store `VersionId=elK9Z3qtolvKrVJhSuMrmlFJZT.77_Dk`),
never `aws lambda update-function-code`, and revert `directory/lambda.tf`'s `IRPT_CONTRACTS_DIR` line. Verified by
`served == CodeSha256` read back after rollback. Per the CTO's affirmed rule @`8b5d2356e5`, a rollback keys on a
measured REGRESSION against the before-state this packet prints (the raise), never on a forward-looking FAIL token.

## WRITERS OF THE SERVED-BEHAVIOUR PROPERTY

`W = 1`. The ONLY writer of what `irpt-directory-search` serves is a Lambda code deployment of its own zip
(`build-and-upload.sh`, this cell's `staged_from` addition). API Gateway response caching: 0 hits across
`infra/aws/terraform/investor-reporting` (`cache_ttl|CachingEnabled|cache_enabled|cache_cluster`). No CloudFront
behavior, no Lambda@Edge, no shared warm-cache construction in `entry.py`'s `Entry(...)` carries a second writer.

## THE IDENTITY LINE PER ARM

Arms (a)-(d) run under the worker's own identity (`0.9.0_WK_IRPT_BCKEND~1`) against read-only AWS/Terraform state,
the committed git object store, and (arm d) `safe-apply`. **Arm (e)** is the one arm that runs under the DEPLOYED
ROLE AND BYTES as the function's own identity (`irpt-directory-role`) -- it is the EXERCISED-plane arm this gate does
NOT substitute for.

## EXPECTED OUTCOME, BOTH BRANCHES (READ FROM THE PRODUCER'S OWN RULE, RULE 5)

  * **Both halves SIGNED at this blob before the apply pass:** arm (d) generates a fresh plan per root, runs the
    SUBTRACTION GATE above over all seven roots (printing the two-part denominator), and applies through
    `.tools/safe-apply.sh` (vendored binary, under a change-management ledger opened before and closed before the
    grading reads) IFF the gate passes -- `0 to destroy`, rc 0, 0-diff after; then `CodeSha256 == 76LeVyYN...`, the
    member present in the served zip (downloaded, hashed), `IRPT_CONTRACTS_DIR` read from the configuration. Arm (e)
    proves search/resolve answer by policy under `irpt-directory-role` and the deployed bytes with `0` UNEXPECTED for
    the exercised firm.
  * **The gate REFUSES (a root shows content outside the subtraction set):** nothing is applied; the REFUSAL is
    EVIDENCE (measure the new field, ROW it, re-sign -- never widen the subtraction set at the terminal); row `S103`
    stays open and this order stays open.
  * **A half absent, or the blob differs:** arm (d) does not run.

## VINTAGE

Re-cut by `2.0.0_SA_COO~B`, 2026-09-20, against the CTO ruling @`0a7f61ae86`. This file's own `blob <hash>`
(`git rev-parse HEAD:<this path>` after commit) is what each half's sign-off names. v1's blob `fb833bc620` is
superseded on the arm-(d) gate; both halves are re-signed against THIS blob.
