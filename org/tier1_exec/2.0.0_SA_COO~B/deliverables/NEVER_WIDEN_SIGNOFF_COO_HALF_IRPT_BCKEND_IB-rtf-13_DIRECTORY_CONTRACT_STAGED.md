# NEVER-WIDEN SIGN-OFF, COO HALF -- IRPT_BCKEND IB-rtf-13: the directory-search zip carries its contract (K-CODE x 1 + K-ENV x 1; row S103)

**Signer:** `2.0.0_SA_COO~B` (the COO half; CLAUDE.md NEVER-1 -- CTO+COO). **Signed:** 2026-09-19 ~19:5xZ. **The act signed:** the
apply IB-rtf-13's arm (d) performs and the live proof arm (e) then takes, exactly as
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtf-13.md` describes it at HEAD after
the first-pass drain `b6ede3ac5c`, **blob `fb833bc620b479e6d3393529fa571e829878ada5`** (`git rev-parse HEAD:<path>`, this turn). A
packet whose bytes differ from that blob is NOT what this half signs. The CTO half is asked the same tick, by blob. No IAM, bucket,
prefix or route change under this act; rtf-10's grants and rtf-12's members stand and are re-read, never re-applied.

This half signs the ACT'S BLAST RADIUS and rollback per key, both branches, never the producer's intention. The writers of each named
property are counted (packet section "WRITERS"; N printed).

## The keys, as the packet names them

| key | what the act touches | blast radius this half signs | rollback |
|---|---|---|---|
| K-CODE (1 function) | `irpt-directory-search` served bytes: ONE new packaged member `contracts/DirectoryEntry.schema.json`, staged at build from the COMMITTED blob of `docs/contracts/investor-reporting/v1/DirectoryEntry.schema.json` (pin 6e764ef0aa, sha256 7ed220ff87..., 12,967 bytes -- a JSON Schema, 9 top-level properties, 0 credentials, 0 secrets; writers: the contract-authoring track only, this act stages a copy and edits nothing); BUILT `76LeVyYNfhdyDnQNXR3LzrqSv7k7Vr3POSjpcBzww6E=` from HEAD 19ccf82226 + the manifest commit, VERIFIED AT REST -- the zip re-hashed == the declared sha, 13 of 13 declared members byte-equal to their declared BLOB at its pin (never the working file; the CTO's condition), the served-byte delta vs the prior 12-member set EXACTLY the one added member (`m = 1 of 1`), import closure 9 of 9 `.py` members satisfied; prior LIVE `CodeSha256` `PUjH3OjDe8Yj3RwdIO0KT3GXsYGfvUCmzG/aHsi6e1c=` read live at packet time (== rtf-12's K-CODE result, the running byte) at build-store `VersionId=elK9Z3qtolvKrVJhSuMrmlFJZT.77_Dk` | **the directory route's search and resolve for every FIRM_ADVISOR of every firm reachable through the bucket map**: with the member and the env, `_document_fields()` reads the contract and `search()`/`resolve()` answer BY POLICY (a projected document set with partial entries withheld and counted, or a refusal on the declared codes) -- never `RuntimeError: BLOCKED` -> UNEXPECTED for this cause (S103's fix); nothing new is reachable across firms (a schema, not data; the scope resolution rtf-10/rtf-12 landed is unchanged). ⚠ **The packet's "DEPLOYED UNWIRED, direct-invoke only" claim is CONTRADICTED by measurement and this half does NOT rely on it:** rtf-12's arm (f) sent real HTTP requests through `https://opalinvest.dev/api/scoped/investor-reporting/directory/*` at 17:31Z and they reached `irpt-directory-search` under `irpt-directory-role` (rows S103/S92 are measured on that route) -- so the radius signed here is the WIDER, request-reachable one, which covers the narrower; the CTO half may reconcile the wiring read (the worker's grep of `api/routes.json` for a module name vs the served route) and it changes no key | re-publish the prior live `CodeSha256` `PUjH3OjD...` through Terraform (`source_code_hash`/object version pinned to build-store `VersionId=elK9Z3qtolvKrVJhSuMrmlFJZT.77_Dk`, verified present), never `update-function-code`, never the manifest (S89); verify `served == CodeSha256` read back; the served behaviour returns to the raise (as today) |
| K-ENV (1 function) | `IRPT_CONTRACTS_DIR = "/var/task/contracts"` on `irpt-directory-search` (`directory/lambda.tf`) -- the same variable class the narrative/performance/export/holdings roots carry (`/opt/python/irpt_contracts`, the layer); here it names a path inside the function's own zip | the env points the existing resolver (`directory/entry.py:60-83`: checkout path, then `IRPT_CONTRACTS_DIR`) at the staged member; no other reader of the variable on this function; configuration, not a second source of truth | revert the line and re-apply; `get-function-configuration` reads no `IRPT_CONTRACTS_DIR` |

**Plans (packet, this pass, applied to nothing):** the directory root `0 to add, 1 to change, 0 to destroy` -- `module.irpt_directory_search`
`source_code_hash` `PUjH3OjD...` -> `76LeVyYN...` (== built), `actions ["update"]`; `module.irpt_directory_refresh` `no-op` in the same
root; the saved planfile's canonical digest `fda208df40d62efe19658c12256e00df61aa07a36d85aa8717380c6d63c5b111`; the other six roots
`No changes` 6 of 6. **A different digest at the apply is a STOP.**

**Writers of the named property, counted:** `W = 1` -- a Lambda code deployment of the function's own zip by `build-and-upload.sh`
(the `staged_from` addition); API Gateway response caching `0` hits across the terraform tree (Grep, this pass); no CloudFront
behavior or Lambda@Edge writer; no shared warm cache in `entry.py`'s `Entry(...)`; the env's writer is the one `yang-lambda` module;
the manifest's `artifact_sha256` has its two known writers (the builder's rewrite reverted per S89; the post-apply reconcile). The
console/CLI qualifier carried. **Re-derived here on a different instrument:** the manifest at HEAD by `json.load` after the drain --
`irpt-directory-search` stages the contract object, the other six unchanged; the first-parent diff of the drain touches the manifest,
`directory/lambda.tf` and the worker's deliverables only. I did not repeat the at-rest zip verification (repetition).

**The census this order also delivered (arm (a), 47 of 47 runtime opens across 7 functions, 10 MISSING):** the DirectoryEntry site
now STAGED; the other MISSING opens (the `ResolvedScope`/`StatusEnvelope`/`PATH_MANIFEST` class across 6-7 functions, W1-S34 BLOCKING
on me; `export/package.py`'s hardcoded device paths, W1-S35) are NOT in this packet's key -- the face's "included in this order's key"
clause was applied by the worker to the site ON THE MEASURED PATH only, and I ACCEPT that narrowing: those opens sit on branches no
served request has exercised (the deployed routes resolve today with them absent), and folding them in would rebuild seven functions
under a mid-round act. W1-S34 is carried to the round-6 analysis as the binding-check tool's population (now enumerated), not left
silent.

## Both branches covered

- **The producer applies** (both halves at HEAD naming this blob; the second pass): arm (d) re-verifies BEFORE any `safe-apply` --
  halves 2 of 2, this blob, the directory root's plan digest EQUAL to `fda208df...`, the built artifact the latest at `76LeVyYN...` --
  any difference is a STOP; applies the SAVED planfile under a change-management ledger (sentinel committed before; closed and
  committed before the grading reads) through `.tools/safe-apply.sh` with the vendored binary, `0 to destroy`, rc 0, 0-diff after;
  then `CodeSha256 == 76LeVyYN...`, the member present in the served zip (downloaded, hashed), `IRPT_CONTRACTS_DIR` read from the
  configuration. **Arm (e), under the deployed role and bytes** (the identity bar and its deployed-bytes clause): rtf-10's arm (f)
  mechanism -- the bounded principal under this order's ledger (rtf-9 packet blob a1f36b95b2, both halves at HEAD, new epoch, the full
  lifecycle incl. the refresh refusal and the 401 after exp), real HTTP requests through the directory route as `irpt-directory-role`
  with route/function/role printed: search WITH a query matching exactly one projected member returns 1, `limit=2` over a wider match
  returns 2 (S92 FIXED or not, by output), resolve WITH a selection resolves it, `0` UNEXPECTED on the directory route for the
  exercised firm, the negative controls refused without echo. **This half does NOT predict counts; the arm measures them.**
- **The producer STOPS** (a half absent; the blob differs; the digest or the latest artifact's sha differs at the apply; the plan
  carries anything but the one function update): nothing is applied, or the function is rolled back per the key the same turn and
  verified by read-back; the route stays as S103 measured it (the raise -> UNEXPECTED after scope).
- **The apply lands and search still reads UNEXPECTED on the exercised firm:** a ROW naming the swallowed exception (the recorder-
  patched diagnostic pair, or the live invoke pair as the deployed role where the trust policy bars assumption) -- and, per the CTO's
  affirmed rule @8b5d2356e5, a rollback ONLY on a measured REGRESSION against the before-state this packet prints (the raise), never on
  the FAIL token alone.

## What this half does NOT sign

The other MISSING runtime opens (W1-S34/W1-S35; the analysis); `irpt-ycharts-generate` (S102); any `_authz/`, `_scope/`, `_ids/`,
`directory/` SOURCE change; any IAM change; any layer change (the `irpt-common:5` stale copies, recorded); the wiring question the
packet mis-states (reconciled by the CTO if it wishes; no key moves on it); the two LGIC firm buckets (rtf-5); FWD-11.

**Push state:** LOCAL -- origin/CLOUD @94e7921b13 (last cited read); HEAD after the drain b6ede3ac5c.
