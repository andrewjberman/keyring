# NEVER-WIDEN CO-SIGN -- ROUND 12, `AMGT-rk-6`: the print-pack redeploy, the packaging act, and the NEW SERVED ROUTES. **CTO HALF.**

**Signer:** `1.0.0_SA_CTO~Z` (the CTO half). **Counterpart:** `2.0.0_SA_COO~Z`'s COO half,
`NEVER_WIDEN_ROUND12_PRINT_PACK_AND_SURFACED_ROUTES_COO_HALF.md` @`34d68dcfaf`, ON FILE. **Act:** `AMGT-rk-6`, worker
`0.9.0_WK_AMGT_RESAPP~24`, chain B (the round's only writer of `lib/research/api/scoped_amgt.py` and the only holder of a live
AWS act). **Signed:** 2026-09-16 ~19:0xZ. **Push state:** LOCAL on SITEZ.

⛔ **THIS HALF NAMES THE ACT'S BLAST RADIUS, NOT THE PRODUCER'S DECISION.** It covers what the act MAY touch and the rollback
per key, and covers BOTH branches of every expected outcome it names.

⛔ **A SEPARATE, FRESH SIGNATURE.** The model-block halves are SPENT on `AMGT-rk-2`. This act ships a different artifact,
CHANGES THE ROUTE SET, and reads prefixes that signature never named.

⭐ **INSTRUMENT SEPARATION, kept.** The COO half read the APPLIED and EXERCISED planes (`get_function`, `head_object`,
`list_object_versions`, `get_role_policy`, a prefix census, a GET-only route census). **This half reads the DESIRED plane
only -- Terraform and source -- so the two halves corroborate rather than repeat** (Rule 22). Every APPLIED value quoted
below is cited to the COO half, never re-measured here; the one exception is the function's `CodeSha256`, which this seat
read on its own instrument at 18:28Z (`x3KrEBvZ...`, LastModified 17:23:29Z) and which agrees.

---

## 1. THE DESIRED PLANE AT SIGNING -- what the source says the act touches

**Terraform.** `infra/aws/terraform/harvest/scoped-amgt-api.tf` (304 lines) is the ONE declarer of the function: the census
over `infra/aws/terraform/` returns 2 files naming `opal-amgt-scoped-api` (denominator 646 scanned) -- the `.tf` and the
build-and-upload script; no second root declares it. Through `modules/yang-lambda`:

| declared | value | line |
|---|---|---|
| `timeout` / `memory_size` | 29 / 512 | `:197-198`, with the comment that 29 s is the API Gateway integration ceiling |
| `environment_variables` | exactly the two table names, set FROM the resources | `:199-211` |
| `layers` | **NOT SET** at signing -- the module exposes `var.layers` (`variables.tf:55`) and wires it at `main.tf:50`, so the LAYER branch of AC2 is REACHABLE on this plane | |
| `source_code_hash` / `s3_object_version` | read from the artifact object's `content-sha256` metadata and its CURRENT `version_id` (`main.tf:37-39`) -- **so every apply after an upload moves the function, and a rollback is "the prior VersionId copied to latest, then apply"** | |
| `local.scoped_amgt_pool_prefixes` | TEN entries, each ending `/`, expanded to `${arn}/${p}*` in limb 1 (`:155`) and `${p}*` in limb 2 (`:163`) | `:110-121` |
| `local.scoped_amgt_routes` | **ELEVEN** keys (8 GET, 3 POST); `for_each` over them mounts one `aws_apigatewayv2_route` each | |
| `terraform_data.scoped_amgt_route_count_check` | precondition `length(local.scoped_amgt_routes) == 11` (`:257-260`) -- the apply STOPS when the set grows until this number is raised | |

**Source, the three modules AC4 names and the print module -- what each READS and WRITES:**

| module | reads | writes | what this half concludes |
|---|---|---|---|
| `lib/research/freshness/build_view.py` | `list_objects_v2` paginated with `Delimiter="/"` under `packs/{key}/` and `raw/{vendor}/{key}/`, then GETs (`:94-95`) | nothing | needs **limb 2** (`ListBucket`, `s3:prefix`) AND **limb 1** (`GetObject`) on `packs/` and `raw/` -- the COO half's widening, both limbs, confirmed from the calls themselves |
| `lib/research/ledger/ledger.py` | `get_object` on `packs/{key}/input_ledger.json` (`:70`, `:77`) | ⛔ **`_write_ledger_raw` -> `put_object` on the same key (`:83-92`)** | the served route may call **`_read_ledger_raw` ONLY**. The adapter role is READ-ONLY on the pool and this signature grants NO write; **a GET route that reaches `_write_ledger_raw` is NOT this act and is NOT signed.** AC4's `ledger` route reads |
| `lib/research/lists/rot.py` | **local files** `lists_dir/publishers.json` and `social_accounts.json` (`:109-111`); no pool call at all | ⛔ **`main()` writes `rot_signal.json` beside them (`:136-140`)** | the served route calls **`compute_rot_signal(lists_dir)`**, a pure read, over inputs **PACKAGED in the artifact** (a module-relative data directory, the rk-2 AC8 pattern), never `main()`; it writes nothing, not to the pool and not beside its inputs. `lib/` in the pool stays UNGRANTED (COO half s.3). The DNS check inside `_list_rot` (`socket`) runs inside the 29 s ceiling or the route answers a classed ABSENT -- the timeout is never raised for it |
| `lib/research/print/render_pack.py` | `DELIVERABLES` = a worker-local `~1` folder (`:52`); `TEMPLATE_PATH` = a OneDrive `.docx` on this box (`:53-56`); module-level `matplotlib` (`:40-44`) | the PDF | the three reads move: `matplotlib` off module level (AC1), the template INTO THE POOL as ONE new object, the deliverables read off the local path. **The template's key sits under a prefix the role reads after this act -- one of the TWELVE (ten + `packs/` + `raw/`) -- never under `lib/` or `social/` and never under a NEW top-level prefix, which would need a grant nobody signed.** It is uploaded with the worker's own credentials, never by a function write grant |

## 2. THE BLAST RADIUS -- counted in ROUTES, per co-sign AMENDMENT 2 on the model-block half

⛔ **A function-code redeploy's blast radius is EVERY route the function serves, and this act ALSO changes the set.**
At signing the set is **11 (8 GET)**. AC4 requires at least one route each naming `freshness`, `ledger`, `lists`; AC5 at least
one each naming `versions`, `compare`: **at least FIVE new GET routes, so the post-act set is at least 16 (13 GET)**. The
exact post-act count is a number the deploy ledger PRINTS beside the precondition's new value, and the rollback is `11`.

| key the act MAY touch (DESIRED plane) | rollback |
|---|---|
| `module.scoped_amgt_api.aws_lambda_function.this` code | the artifact at `CodeSha256 x3KrEBvZVFmZqZ1KLsuzu6A7fedugZoxfS7+eoJiMUw=` (754470 B), S3 **VersionId `X2ZRUM2EXxnSk2vVgtT9JYn6FET9SziA`** (COO half s.2): copy that version to latest, apply |
| `timeout` | **29 and never above it** -- a value above the integration ceiling is NOT covered; rollback 29 |
| `memory_size` | MAY rise for the render (matplotlib + numpy in 512 MB is the risk this half names); rollback **512** |
| `ephemeral_storage` | rollback **512** |
| `layers` | MAY gain **at most one** `aws_lambda_layer_version` declared in THIS root, carrying only matplotlib / pypdf / numpy and their transitive wheels; rollback **`layers = []`** (detach). The layer version object may stay published; a detached layer serves nothing |
| `environment_variables` | any NEW var is ABSENT at signing; rollback = REMOVE it. The two table vars do not move |
| inline policy **limb 1** (`GetObject`) | gains exactly `arn:aws:s3:::opal-data-harvest/packs/*` and `.../raw/*`; rollback = the TEN |
| inline policy **limb 2** (`ListBucket` `s3:prefix`) | gains exactly `packs/*` and `raw/*`; rollback = the TEN. **In Terraform: the entries `"packs/"` and `"raw/"` appended to `local.scoped_amgt_pool_prefixes`, slash included -- the list's consumers append `*` in both limbs (`:155`, `:163`)** |
| inline policy limbs 3-4 (DynamoDB) | **do not move** |
| `local.scoped_amgt_routes` | gains the new keys, every one `GET`, every one under `/api/scoped/amgt/`, every one `CUSTOM` against the portal authorizer exactly as the eleven; rollback = the ELEVEN keys as listed at `:238-249` today |
| `terraform_data.scoped_amgt_route_count_check` | its `== 11` becomes `== <new count>`; rollback `11` |
| the pool template object | ONE new object under a granted prefix, key recorded in the deploy ledger BEFORE the write; rollback = delete the key (or restore its prior version if it existed) |
| served bodies of the 8 GET routes at signing | the COO half's s.2 census is the anchor: **7 of 8 answer 200, `/print` 500**. A route that answered 200 and does not after the act is a regression: ROLLBACK, not fix-forward |

⛔ **NOT COVERED:** any pool WRITE grant on the role; `lib/` or `social/`; a prefix without its trailing slash; a wildcard
resource or `s3:*`; `s3:DeleteObject`; any DynamoDB change; a second function or a second root declaring this one; any route
declared `authorization_type = "NONE"`; any POST route; a timeout above 29; a layer carrying anything beyond the three
packages and their wheels; any portal act or promote; enabling any schedule, alarm, monitor or notification.

## 3. WRITER CENSUS on the DESIRED plane -- N printed per named property

| named property | WRITERS (N) | how this half knows |
|---|---|---|
| the function's code and configuration | **1** | one `.tf` declares it (census above: 2 files name it, 1 declares, 1 builds); the module pins the artifact by version |
| the route set under `/api/scoped/amgt/` | **1** | `aws_apigatewayv2_route.scoped_amgt_api` `for_each local.scoped_amgt_routes` in the same file; the shared API (`local.portal_api_id`) carries OTHER prefixes from OTHER roots, which this act must not touch |
| the role's inline policy | **1** | the same file, both limbs from one local |
| `packs/{key}/input_ledger.json` | **2 in source** -- the pack producer, AND `ledger.py:_write_ledger_raw` | this is the writer the COO half's live census could not see: it exists in code. The act keeps N at the live 1 by NEVER wiring `_write_ledger_raw` behind a served route |
| `raw/{vendor}/{key}/` objects | **1 per vendor lane** (COO half s.5) | the act grants read only |
| `rot_signal.json` | **1** -- `rot.py:main()` | never called from the adapter; the route computes in memory |

## 4. EXPECTED OUTCOMES -- both branches, read from the source's own rule

- **AC3 `/print`.** BRANCH A: packages in the artifact or the layer, template read from the pool, inputs off the box -> 200
  with PDF magic and nonzero length. BRANCH B: an absent template key or an uncovered security -> a classed ABSENT with its
  reason, COVERED; a 200 with zero bytes is NOT met and NOT covered.
- **AC4 `freshness` / `ledger` / `lists`.** BRANCH A: `packs/{key}/` resolves (the COO half's key-form trap: `BA_US/` short vs
  `NVDA_US_Equity/` long) and the routes serve. BRANCH B: no object at the key the route derived -> a classed ABSENT NAMING
  THE KEY, COVERED, and distinguished from AccessDenied before anyone concludes the grant is wrong. ⛔ **A `ledger` GET that
  writes the ledger, or a `lists` GET that writes `rot_signal.json`, is outside both branches and outside this signature.**
- **AC5 `versions` / `compare`.** BRANCH A: `derived/model_block/` (granted, both limbs) lists real stamps for the 3 covered
  keys plus NVDA; compare with no query defaults to the two latest. BRANCH B: fewer than two stamps -> a classed ABSENT,
  never an invented stamp. COVERED.
- **The apply.** BRANCH A: it stops at the route-count precondition until the number is raised -- the guard working.
  BRANCH B: a failure after the upload and before the function moves leaves the pre-act `CodeSha256` serving and the
  ledger entry OPEN until closed; never left overnight.

## 5. THE DISCRIMINATOR THIS HALF ADDS -- the PLAN's resource list

⭐ **Before the apply, the worker's targeted `terraform plan` names exactly and only:** `module.scoped_amgt_api.aws_lambda_function.this`
(update), `aws_iam_role_policy.scoped_amgt_api_grants` (update), one `aws_apigatewayv2_route.scoped_amgt_api["GET ..."]`
(create) per new key with its integration if the root mounts one per route, `terraform_data.scoped_amgt_route_count_check`
(replace), and at most one `aws_lambda_layer_version` (create). **Any other resource in the plan -- a destroy of any kind, a
second function, a route outside `/api/scoped/amgt/`, a DynamoDB change -- is STOP: file the row, do not apply.** The plan's
resource list is pasted into the deploy ledger entry; the post-act route census (COO half s.7.3) is the EXERCISED check on the
same act. Two planes, two instruments, one act.

## 6. WHAT THIS HALF ASKS OF THE WORKER (with the COO half's s.7, which stands)

1. The change-management entry OPENS before the first live act and records the new route count, the template's exact key and
   the plan's resource list; it CLOSES on the post-act census.
2. The three re-pointed reads (`render_pack.py:40-44`, `:52`, `:53-56`) land with the rk-2 discipline: module-relative, lazy or
   guarded, never an import-time read of a path the artifact does not carry.
3. The `ledger` route wires `_read_ledger_raw` only; the `lists` route wires `compute_rot_signal` over packaged inputs only.
4. Correcting the stale comment at `scoped-amgt-api.tf:106-109` (the model-block grant is APPLIED, both halves on file) is inside
   this act's grant and moves no resource; do it in the same commit.
5. If a limb cannot be written slash-form, a route needs a prefix neither half names, a route would need a pool write, or the
   plan lists a resource s.5 does not name: STOP and file a row.

Both halves are on file at `ledger/`; `AMGT-rk-6`'s deploy is signed for the act bounded above and for nothing wider.
