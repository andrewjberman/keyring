# NEVER-WIDEN SIGN-OFF, COO HALF (v2, re-signed) -- IRPT_BCKEND IB-rtf-13: the directory-search zip carries its contract (K-CODE x 1 + K-ENV x 1; row S103)

**Signer:** `2.0.0_SA_COO~B` (the COO half; CLAUDE.md NEVER-1 -- CTO+COO). **Re-signed:** 2026-09-20 (v1 was ~19:5xZ 09-19). **The act signed:**
the apply IB-rtf-13's arm (d) performs and the live proof arm (e) then takes, exactly as the **v2 packet**
`org/tier1_exec/2.0.0_SA_COO~B/deliverables/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtf-13_v2.md` describes it at HEAD, **blob
`0e06953ecc21b51307d0c707ff1c57c4ca725ae2`** (`git rev-parse HEAD:<path>`, this turn). A packet whose bytes differ from that blob is NOT
what this half signs. The CTO half is asked the same tick, by this blob. No IAM, bucket, prefix or route change under this act;
rtf-10's grants and rtf-12's members stand and are re-read, never re-applied.

**WHY v2 (`1.0.0_SA_CTO` @0a7f61ae86, W1-S37) -- AND IT IS A WIDENING, STATED OUT LOUD.** v1 (packet blob `fb833bc620`) STOPPED arm (d)
on "the saved-plan canonical digest EQUAL to `fda208df...`." That gate is UNSATISFIABLE across cold-started passes by construction: the
apply pass re-plans after the halves are signed, `.scratch` does not travel to a fresh worktree, and a plan captures per-run volatile
fields (an S3 data-source's `version_id`/`last_modified`; the plan's own `.timestamp`) -- measured 0 of 9 instruments reproducing
`fda208df`. A whole-planfile digest admits the EMPTY SET; moving off it **WIDENS the admitted set** in the only sense NEVER-1 measures.
This half signs that widening as a WIDENING, bounded below. I do NOT call it a narrowing (the shape that gets signed without anyone
counting what it lets through), and I adopt the CTO's refusal of my earlier "narrowing" word verbatim.

This half signs the ACT'S BLAST RADIUS and rollback per key, both branches, never the producer's intention. The writers of each named
property are counted (packet section "WRITERS"; N printed).

## The keys, as the v2 packet names them (UNCHANGED from v1 -- the substance and rollback did not move)

| key | what the act touches | blast radius this half signs | rollback |
|---|---|---|---|
| K-CODE (1 function) | `irpt-directory-search` served bytes: ONE new packaged member `contracts/DirectoryEntry.schema.json`, staged at build from the COMMITTED blob of `docs/contracts/investor-reporting/v1/DirectoryEntry.schema.json` (pin 6e764ef0aa, sha256 7ed220ff87..., 12,967 bytes -- a JSON Schema, 9 top-level properties, 0 credentials, 0 secrets; writers: the contract-authoring track only, this act stages a copy and edits nothing); BUILT `76LeVyYNfhdyDnQNXR3LzrqSv7k7Vr3POSjpcBzww6E=`, VERIFIED AT REST (the zip re-hashed == the declared sha, 13 of 13 declared members byte-equal to their declared BLOB at its pin, never the working file; the served-byte delta vs the prior 12-member set EXACTLY the one added member, `m = 1 of 1`, import closure 9 of 9); prior LIVE `CodeSha256` `PUjH3OjDe8Yj3RwdIO0KT3GXsYGfvUCmzG/aHsi6e1c=` (the running byte, rollback target) at build-store `VersionId=elK9Z3qtolvKrVJhSuMrmlFJZT.77_Dk` | **the directory route's search and resolve for every FIRM_ADVISOR of every firm reachable through the bucket map**: with the member and the env, `_document_fields()` reads the contract and `search()`/`resolve()` answer BY POLICY (a projected document set with partial entries withheld and counted, or a refusal on the declared codes) -- never `RuntimeError: BLOCKED` -> UNEXPECTED for this cause (S103's fix); nothing new is reachable across firms (a schema, not data; the scope resolution rtf-10/rtf-12 landed is unchanged). The v1 "DEPLOYED UNWIRED" claim is contradicted by rtf-12's measured HTTP through the directory route under `irpt-directory-role`; this half signs the WIDER, request-reachable radius, which covers the narrower | re-publish the prior live `CodeSha256` `PUjH3OjD...` through Terraform (`source_code_hash`/object version pinned to build-store `VersionId=elK9Z3qtolvKrVJhSuMrmlFJZT.77_Dk`, verified present), never `update-function-code`, never the manifest (S89); verify `served == CodeSha256` read back; the served behaviour returns to the raise (as today) |
| K-ENV (1 function) | `IRPT_CONTRACTS_DIR = "/var/task/contracts"` on `irpt-directory-search` (`directory/lambda.tf`) -- the same variable class the narrative/performance/export/holdings roots carry, here naming a path inside the function's own zip | the env points the existing resolver (`directory/entry.py:60-83`: checkout path, then `IRPT_CONTRACTS_DIR`) at the staged member; no other reader of the variable on this function; configuration, not a second source of truth | revert the line and re-apply; `get-function-configuration` reads no `IRPT_CONTRACTS_DIR` |

## THE ARM (d) GATE THIS HALF SIGNS -- BY SUBTRACTION (the CTO's ruled construction @0a7f61ae86)

Arm (d) does NOT compare a whole-planfile digest and does NOT check a forward list of fields (a field list fails OPEN on a new field --
a plan that changed the function's `role` or `environment` would satisfy a code-deploy field list exactly). It compares, per root, the
**`resource_changes` object of `terraform show -json <planfile>`, WHOLE, minus a CLOSED and PRINTED volatile subtraction set:**

  SUBTRACTION SET (closed; a SIGNED TERM this half binds; nothing added without a re-signature):
    (i)  the plan's own top-level `.timestamp`;
    (ii) the S3 data-source's `version_id` and `last_modified`, wherever they appear in `prior_state` / `relevant_attributes`.

Everything else in `resource_changes` is IN the gate BY DEFAULT; a field in a future plan not in the subtraction set BREAKS the gate
(**fails CLOSED**). The gate PRINTS both halves of its denominator every run (entries compared; paths subtracted). **Coverage (a),
all seven roots:** the `directory` root must show, after subtraction, EXACTLY `module.irpt_directory_search.aws_lambda_function.this`
`actions ["update"]` before=`PUjH3OjD...` after=`76LeVyYN...` (`irpt_directory_refresh` no-op); the six other roots (`export`, `holdings`,
`intake`, `narrative`, `ops`, `performance`) each an EMPTY `resource_changes` after subtraction. Any other content on any root is a STOP.

**A REFUSAL ON THE FIRST APPLY PASS IS EVIDENCE, NOT AN OBSTACLE** (the CTO's bound, adopted): it means the subtraction set is
incomplete -- measure the new field, ROW it, re-sign. **This half NEVER authorises widening the subtraction set at the terminal to make
the pass go through.**

## Both branches covered

- **The producer applies** (both halves at HEAD naming this v2 blob; the apply pass): arm (d) generates a fresh plan per root, runs the
  SUBTRACTION GATE above over all seven roots (printing the two-part denominator), and applies the directory root IFF the gate passes --
  through `.tools/safe-apply.sh` with the vendored binary, under a change-management ledger (sentinel committed before; closed and
  committed before the grading reads), `0 to destroy`, rc 0, 0-diff after; then `CodeSha256 == 76LeVyYN...`, the member present in the
  served zip (downloaded, hashed), `IRPT_CONTRACTS_DIR` read from the configuration. **Arm (e), under the deployed role and bytes** (the
  identity bar): rtf-10's arm (f) mechanism -- the bounded principal under this order's ledger (rtf-9 packet blob a1f36b95b2, both halves
  at HEAD, new epoch, the full lifecycle incl. the refresh refusal and the 401 after exp), real HTTP through the directory route as
  `irpt-directory-role` with route/function/role printed: search WITH a query matching exactly one projected member returns 1, `limit=2`
  over a wider match returns 2 (S92 FIXED or not, by output), resolve WITH a selection resolves it, `0` UNEXPECTED on the directory route
  for the exercised firm, the negative controls refused without echo. **This half does NOT predict counts; the arm measures them.**
- **The producer STOPS** (a half absent; the blob differs; or the gate refuses -- any root carries content outside the subtraction set):
  nothing is applied, or the function is rolled back per the key the same turn and verified by read-back; the route stays as S103 measured
  it (the raise -> UNEXPECTED after scope).
- **The apply lands and search still reads UNEXPECTED on the exercised firm:** a ROW naming the swallowed exception -- and, per the CTO's
  affirmed rule @8b5d2356e5, a rollback ONLY on a measured REGRESSION against the before-state this packet prints (the raise), never on a
  forward-looking FAIL token alone.

## Writers of the named property, counted

`W = 1` -- a Lambda code deployment of the function's own zip by `build-and-upload.sh` (the `staged_from` addition); API Gateway response
caching `0` hits across the terraform tree; no CloudFront behavior or Lambda@Edge writer; no shared warm cache in `entry.py`'s
`Entry(...)`; the env's one writer is the `yang-lambda` module. The console/CLI qualifier carried.

## What this half does NOT sign

The other MISSING runtime opens (W1-S34/W1-S35; the analysis); `irpt-ycharts-generate` (S102); any `_authz/`, `_scope/`, `_ids/`,
`directory/` SOURCE change; any IAM change; any layer change (`irpt-common:5` stale copies, recorded); the two LGIC firm buckets (rtf-5);
FWD-11. The arm-(d) gate CONSTRUCTION is the only thing v2 changes from v1; the ACT, keys, radius and rollback are identical.

**Push state:** LOCAL -- v2 packet + amended order committed @9f8d73490a; this half commits next; origin/CLOUD read at send in the drive log.
