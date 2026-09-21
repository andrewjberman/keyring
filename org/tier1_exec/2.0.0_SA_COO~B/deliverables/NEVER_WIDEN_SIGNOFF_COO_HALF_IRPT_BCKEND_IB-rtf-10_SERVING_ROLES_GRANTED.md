# NEVER-WIDEN SIGN-OFF, COO HALF -- IRPT_BCKEND IB-rtf-10: the serving roles granted the ownership map and the directory, the bucket map on every scoped function, and `irpt-directory-search` rebuilt from HEAD (rows S90/S93/S95/S96; the CTO's ruling @606e7d14ce)

**Signer:** `2.0.0_SA_COO~B` (the COO half; CLAUDE.md NEVER-1 -- CTO+COO). **Signed:** 2026-09-19 ~13:3xZ. **The act signed:** the
apply IB-rtf-10's arm (e) performs and the live proof arm (f) then takes, exactly as
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~V/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtf-10.md` describes it at HEAD after
the third-pass drain `58f292f335`, **blob `c3a44074d2dabe4292bfc648d855be4b99fe48db`** (`git rev-parse HEAD:<path>`, this turn). A
packet whose bytes differ from that blob is NOT what this half signs; blobs `4e7ba624fa` and `609fbba9de` are SUPERSEDED and no half
was spent on either. The CTO half is asked the same tick, by blob; the CTO's ruling @606e7d14ce is the design authority this half
executes (its four conditions are met at packet sections 0, 1, 3, 6; the identity bar at section 9).

This half signs the ACT'S BLAST RADIUS and rollback per key, both branches, never the producer's intention. The writers of each named
property are counted (packet section 5, re-read here; N printed per property).

## The keys, as the packet names them

| key | what the act touches | blast radius this half signs | rollback |
|---|---|---|---|
| K-OM (6 roles) | one `aws_iam_role_policy` per serving role that binds the shared loader (`irpt-directory-role`, `irpt-status-role`, `irpt-narrative-role`, `irpt-export-render-role`, `irpt-performance-adapter-role`, `irpt-ycharts-generate-role`), `Sid OwnershipMapReadOnly`, `s3:GetObject` on EXACTLY three objects derived from `data/firm_registry.json` at blob 99b8eeb54f: `opal-data-bd/platinum/49financial/ownership_map.json`, `opal-data-inf/platinum/inflection/ownership_map.json`, `opal-data-cot/platinum/cottonwood/ownership_map.json`; never `platinum/*`, never ListBucket; builder-named, naming gate 6 of 6; `irpt-holdings-role` gets none (it binds `_no_grant` by design) | each role reads ONE object per client firm in that firm's own bucket; the rest of every `platinum/` tier stays unreadable; on the shared `opal-data-bd` the object KEY is the fence against `mockadv`; a new registry firm is a plan diff a human reads (condition 1) | remove the resource (revert), re-apply the root via `.tools/safe-apply.sh`, verify `simulate-principal-policy` reads implicitDeny again per role per firm |
| K-DIR (4 roles) | the SAME prefix-scoped `s3:GetObject` on `<bucket>/investor-reporting/directory/*` per client firm that `directory/iam.tf:36-38` already derives for the directory role, extended to the four roles that bind the shared loader (narrative, export-render, performance-adapter, ycharts-generate); my ruling on S93 (98244); inside the CTO's condition (3) -- four of the seven serving roles | those four functions can read the directory their loader reads FIRST (`loaders.py:71-80`); nothing beyond that prefix; never ListBucket | as K-OM |
| K-ENV (6 functions) | `IRPT_DIRECTORY_BUCKET_MAP = {"49financial":"opal-data-bd","cottonwood":"opal-data-cot","inflection":"opal-data-inf"}` on status, holdings, narrative, export-render, performance-adapter, ycharts-generate -- the ONE value `irpt-directory-search` already carries, from the same registry expression (condition 4: configuration, not a second source of truth) | each function resolves the VERIFIED tenant's bucket (`loaders.py:76, 104-105`), never the request's | revert the line, re-apply, verify `get-function-configuration` reads no map |
| K-CODE (1 function) | `irpt-directory-search` served bytes: the IB-rtf-11 fix (drained @52ffa27636; `directory/entry.py` reads `q`/`limit`/`selection` from the payload-2.0 shape) BUILT from HEAD 46a106b4d1 under ledger `irpt-bckend-ib-rtf-10-k-code-build-2` after the S96 remedy (ONE `staged_from` object, sibling-identical, @2b1c672e1f; `artifact_sha256` untouched per S89); built sha256 `HOpXPDoHhrVK/ayqsx1uKgzt9mWOjDlK+Ix2CPbCamI=` at build-store version `hk9OUfwHZxlcwZDqN7cEknbJOXtvB3jd`, verified at rest 7 of 7 (10 of 10 members == `files[]`, each equal to its committed blob) | on the directory route search honours `q`/`limit` and resolve honours `selection` (today: query ignored, resolve answers "nothing" -- S92); the served-byte delta is EXACTLY `entry.py` plus the seam member's line endings (the CRLF hand copy replaced by the committed blob); the other 8 members byte-identical -- `_authz/`, `_scope/`, `_keys/`, `_ids/`, `handler.py` unchanged; K-CODE changes how parameters are READ, never which firm's data is reachable | re-publish the prior live `CodeSha256 aQxATFkcdtEBvs+v/zztQBOPcbR9XH9Lzjm9kUOmhmU=` from build-store version `l4JK6aUnUgtrg.TFrxiKU8.XBM_6APl4` (verified present and equal) through Terraform -- never `update-function-code`, never the manifest (S89); verify `CodeSha256 == aQxATFkc...` |

**The S95 restore (already run, section 4, carried):** the build store for status, narrative, export-render and performance-adapter holds
the SERVED bytes (4 of 4 under ledger cc154f5c7c; the displaced 07:29-07:31Z builds kept by VersionId), so their plans carry an
object-version bump with an UNCHANGED hash -- plan noise, named; the CTO read that write as the verified-DELTA=0 case needing no half of
its own (98256), and this half agrees: the served plane did not move. **PLAN-CODE-CHANGES: 1 of 7, K-CODE's own, after-hash == built
sha; any other code change at the apply is a STOP.** 7 of 7 roots planned, `0 to destroy`, 18 changes, canonical digests printed (six
EQUAL to the second pass; the directory root moves by exactly K-CODE's address).

**Writers of the named properties, counted (packet section 5, declared plane):** role policy sets W = 2 / 2 / 2 / 4 / 5 / 3 / 3 (each
new statement its own resource, so the rollback is one resource); each function's environment W = 1 (its `yang-lambda` module); each
artifact key W = 2 (`build-and-upload.sh`, and this order's restore / K-CODE build once each under its own ledger); the served code
of `irpt-directory-search` W = 1 (`module.irpt_directory_search`); the manifest's `artifact_sha256` W = 2 (`build-and-upload.sh`
pre-apply and `record-terraform-deploy.sh:748-768` post-apply -- neither a rollback source, S89). The console/CLI qualifier the CTO's
rtf-8 half names is carried: a ban is not a census; the rollback's own re-read covers the rest. **Re-derived here on a different
instrument:** the packet's own battery compared its census lines to re-derived counts and read EQUAL (a comparison that read DIFFERS
3 of 3 on the pre-packet run, so it can fail); I re-derived the S96 premise on `json.load` of the manifest at HEAD before ruling
(directory-search: `files[]` carries the seam, `staged_from` did not; `irpt-status` carries the object at pin c28c728a30 / sha256
87f2f92f) and the four K-DIR resources are visible in the drain's first-parent diff. I did not repeat the IAM simulation (repetition).

## Both branches covered

- **The producer applies** (both halves at HEAD naming this blob; the fourth pass): arm (e) re-verifies BEFORE any `safe-apply` the
  per-root canonical digests EQUAL to section 6, the registry blob EQUAL to 99b8eeb54f, and the latest search zip == `hk9OUfwH` /
  `HOpXPDo` -- any difference is a STOP; applies 7 roots under a change-management ledger (sentinel committed before, closed before
  the grading reads) through `.tools/safe-apply.sh` with the vendored binary, `0 to destroy`; then reads `simulate-principal-policy`
  allowed per role per firm map (and per directory prefix for K-DIR) with the negative controls denied (`platinum/<firm>/anything-else`,
  a second firm's map from a firm-scoped role), `get-function-configuration` reading the bucket map on 6 of 6 and `CodeSha256`
  UNCHANGED on 6 of 7 serving functions with `irpt-directory-search == HOpXPDo...`. **Arm (f), under the deployed roles (the identity
  bar):** the bounded test principal re-created under this order's ledger (the rtf-9 packet blob a1f36b95b2, both halves at HEAD,
  new epoch, the full lifecycle incl. the refresh refusal and the 401 after exp) sends real HTTP requests through
  `https://opalinvest.dev/api/scoped/investor-reporting/<route>`; every request on a firm whose map EXISTS reads a SCOPE-RESOLVED
  answer (served with `unprojected_grant` present, or a POLICY refusal with a firm_id) and NEVER `UNEXPECTED`, `m of m`; search WITH
  a query and resolve WITH a selection record S92 FIXED or not by output; holdings reads its designed `EMPTY_GRANT`; inflection is
  recorded UNEXPECTED-BY-ABSENCE with S94 cited and NOT counted (the CTO's S94 ruling @c0a1466be5 puts the map's existence in ratified
  text v0.15; the producer's act is cut in its own lane); the token's `0 UNEXPECTED` reads over `n of N` registry-enabled firms whose
  map exists (2 of 3 today). **This half does NOT predict k or count; the arm measures them.**
- **The producer STOPS** (a half absent; the packet blob differs; a digest, the registry blob or the latest search zip differs at the
  apply; a plan carries a code change other than K-CODE's; a negative control fails): nothing is applied, or the roots applied so far
  are rolled back per key the same turn and verified by read-back; the path stays as S90 measured it (12 of 12 UNEXPECTED, an outage,
  not a refusal); S92 stands on the directory route; the K-CODE artifact serves nothing until an apply points the function at it.
- **The apply lands and a request on an existing-map firm still reads UNEXPECTED, or a served response omits `unprojected_grant`, or
  search still ignores `q`:** a BLOCKING row and a same-turn rollback of the key that owns it; nothing is flipped `complete`.

## What this half does NOT sign

S94's remedy (the producer's map, DS-owned, cut in its own lane per the CTO); holdings serving an advisor (rt-7's `_no_grant`, the
CTO's at the round-6 analysis); any code other than K-CODE (the four restored functions stay at their served bytes; no `_authz/`,
`_scope/`, `_keys/`, `_ids/` change); the manifest beyond the one `staged_from` object (the stale `_staged_from_note` "7 of 9" and the
`artifact_sha256` `hxfwVT7E...` that is neither the prior live nor the built hash -- named, S89's bar applies, reconciled only by the
post-apply writer); the pre-existing `terraform fmt` deltas; the two LGIC firm buckets (rtf-5, fenced); FWD-11; the live
`irpt-directory-search` zip's non-reproducible CRLF hand copy (carried to the CTO's analysis; K-CODE's rebuild replaces it).

**Push state:** LOCAL -- origin/CLOUD @4290315df9 (the CTO's 13:2xZ ls-remote read, cited); HEAD after the drain 58f292f335.
