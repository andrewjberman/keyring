# NEVER-WIDEN CO-SIGN -- ROUND 12, `AMGT-rk-7`: the `/refresh` carrier declaration, the dated rankings fallback, and the served driver chart. **CTO HALF.**

**Signer:** `1.0.0_SA_CTO~Z`. **Counterpart:** `2.0.0_SA_COO~Z`'s COO half, **OWED** (read the APPLIED and EXERCISED planes; this half
reads Terraform and source only, so the two corroborate rather than repeat). **Act:** `AMGT-rk-7` on chain B, after `AMGT-rk-6`.
**Signed:** 2026-09-16 ~23:2xZ, at the restart Andrew directed for 7:10 PM ET. **Source vintage for every line cited:** `@2eb6bec53a`.
**Push state:** LOCAL on SITEZ.

THIS HALF NAMES THE ACT'S BLAST RADIUS, NOT THE PRODUCER'S DECISION. It covers what the act MAY touch and the rollback per key,
and it covers BOTH branches of every expected outcome it names. It is a FRESH signature: the rk-6 halves do not cover rk-7's
served changes (COO restart handoff s.4).

---

## 1. THE ACT, AS THE ORDER STATES IT

`AMGT-rk-7` (issued to `0.9.0_WK_AMGT_RESAPP~24`) changes three served behaviours of `opal-amgt-scoped-api`, all in
`lib/research/api/scoped_amgt.py`, and ships them by one redeploy of that function:

| served behaviour | today, in source | after the act | criterion |
|---|---|---|---|
| `POST /api/scoped/amgt/refresh` | `raise AdapterError(501, "refresh has no queue carrier declared ...")` at `:2564-2569` | a non-5xx DECLARATION naming the carrier -- the page calls `POST /api/private/research/pull`, served by `opal-research-pull-enqueue` -- that SENDS NOTHING | AC1, AC3 |
| `GET /api/scoped/amgt/lead-panel/rankings/{movement}/{subject}` | `read_rankings` (`:499-552`) asks the `_CURRENT` pointer at the requested date only; no generation there -> a classed ABSENT | when the requested date has no generation, serve the LATEST generation WITH its date, `requested_as_of` and `dated: true` | AC4 (proves cell rk-3) |
| `GET /api/scoped/amgt/security/{key}/thesis`, field `thesis_driver_chart` | `thesis_driver_chart` (`:1901-1962`), an EXACT join of the driver's series to a model-block mnemonic or definition | a named driver series served with its points, or a classed absence | AC5 (proves cell rk-15) |

AC2 is a NEGATIVE bar and is binding here too: **no event-source mapping on the pull queue.** The consumer stays on the box
because it needs the Bloomberg terminal at `127.0.0.1:8194` (round-11 ADDENDUM 2, C1).

## 2. THE BLAST RADIUS -- counted in ROUTES (co-sign AMENDMENT 2), and the rollback per key

**A function-code redeploy's blast radius is EVERY route the function serves.** This act does not change the route set: the
eleven routes declared at `scoped-amgt-api.tf:238-249` already include `POST .../refresh`, and after `AMGT-rk-6` the set is
whatever rk-6's deploy printed. **The pre-act anchor is therefore MEASURED WHEN THIS ACT'S CHANGE RECORD OPENS, never pinned
here**: rk-6 moves the function, the route set and the count precondition first, so any value typed now would be stale by the
time it mattered.

| key the act MAY touch | rollback |
|---|---|
| `module.scoped_amgt_api.aws_lambda_function.this` -- code | redeploy the artifact S3 VersionId recorded in the change record at open (copy it to latest, apply); its `CodeSha256` is read back equal |
| the function's `environment_variables` | MAY gain at most TWO non-secret variables naming the carrier, each set FROM a Terraform resource reference (the queue, the enqueue route), never a typed literal (Rule 30); rollback = REMOVE them. The two table variables at `:203` and `:208` do not move |
| served body of `POST /refresh` | covered by the code rollback |
| served body of `GET .../rankings/...` | covered by the code rollback |
| served body of `GET .../security/{key}/thesis` | covered by the code rollback |
| every other GET route's served body | **MUST NOT CHANGE.** The pre/post census over the route table is the control; a route that answered 200 and does not after the act is a regression, and the answer is ROLLBACK |

**NOT COVERED by this signature, and each is STOP-and-file-a-row:**

- **Anything declared in `infra/aws/terraform/harvest/api-gateway.tf`** -- the enqueue function `opal-research-pull-enqueue`, its
  route, the `opal-research-pull-requests` queue, or their policies. ⚠ **rk-7's `<paths>` grant is the whole
  `infra/aws/terraform/harvest/` folder, which includes that file, so the grant reaches resources this act must not move.** The
  act READS those resources to declare the carrier; it changes none of them.
- **Any `aws_lambda_event_source_mapping`**, anywhere (AC2).
- **Any IAM change** on `opal-amgt-scoped-api-role`: no `sqs:*`, no new prefix, no write. The adapter DECLARES; it does not send.
  A `/refresh` that calls `send_message` is outside this act -- and would fail AccessDenied as a 5xx, which the census catches.
- **Any change to `read_generation_pointer` (`:376`) or `read_point_record` (`:555-596`).** ⛔ **`read_security_overlay` reads its
  point through `read_point_record` (`:1811`), which calls `read_generation_pointer` (`:574`).** A fallback placed in the SHARED
  pointer read would silently change what `/overlay` serves; the fallback lives in `read_rankings` or in a helper only
  `read_rankings` calls. `read_rank_series` (the timeseries route, `:724`) likewise stays exact-date.
- **Any fuzzy, keyword or prose-parsed match in `thesis_driver_chart`.** Its docstring (`:1904-1912`) states the rule and this half
  adopts it: the join is equality to a mnemonic or a definition, or an explicit declared mapping table; every served point comes
  from the model block's fiscal figures, never from numbers parsed out of filing prose.
- A route added or removed; a layer; a timeout above 29; memory changed (rk-6's half governs those); any schedule, alarm or
  monitor; any portal act. The page's own call to the enqueue route is chain A's portal code (rk-12 AC4), a commit, not a deploy.

## 3. WRITER CENSUS, N PRINTED PER NAMED PROPERTY (DESIRED plane)

| named property | WRITERS (N) | which this act moves |
|---|---|---|
| the function's code and configuration | **1** -- `scoped-amgt-api.tf` via `modules/yang-lambda` | this one |
| the `POST /refresh` response | **1** -- the dispatch at `scoped_amgt.py:2564` | this one |
| the rankings rows served | **3** -- the reader `read_rankings`, the price-axis generation writer (the rk-3 path, last run for 2026-09-15 by rk-17), and the chatter-axis producer on its daily schedule | **only the reader.** A dated fallback serves whatever the latest producer wrote; it creates no generation |
| `thesis_driver_chart` | **3** -- the adapter's join, the D-1 drafted document that names the driver series (the filings and drafting producer, rk-15 and rk-18), and the model-block pull that supplies the fiscal figures (rk-17, landed for 33 names) | **only the join.** Whether points appear for a name depends on the two producers, which is why AC5's absent branch exists |
| the enqueue route, function and queue | **1** -- `api-gateway.tf` | **none** |

## 4. EXPECTED OUTCOMES -- BOTH BRANCHES, read from the source's own rule

- **`POST /refresh`.** COVERED: any 2xx declaration with `refused` not true that names the enqueue route and the queue and sends
  nothing. NOT COVERED: a 5xx of any kind (the census treats it as a regression), or a response that enqueues.
- **Rankings, three branches.** (A) A generation exists at the requested date: served as today, `dated: false`. (B) No generation
  at the requested date, one exists EARLIER: the latest generation **on or before** the requested date is served with its own
  `as_of_date`, `requested_as_of` and `dated: true`. (C) The axis has no generation at all (`BREAKOUT_PRICE` today): a classed
  ABSENT or EMPTY, never rows. ⛔ **NOT COVERED: serving a generation dated AFTER the requested date**, which would present a later
  list as an earlier one; and serving rows without `as_of_date` and `dated`, which strips the claim a consumer needs to reject a
  stale list.
- **`thesis_driver_chart`.** (A) The driver's series matches by the exact rule: `SERVED` with points and a unit. (B) No driver, or
  no exact match: `ABSENT` with a classed reason. A named series with zero points is not a success (AC5 says so), but it is a
  safe served state and not a regression.
- **The apply.** (A) The targeted plan changes only the function. (B) It fails after the upload and before the function moves:
  the pre-act build keeps serving and the change record stays OPEN until closed, never overnight.

## 5. THE DISCRIMINATOR

⭐ **The worker's targeted `terraform plan` (`-target=module.scoped_amgt_api`) lists exactly ONE resource change:
`module.scoped_amgt_api.aws_lambda_function.this` (update).** Anything else -- a resource from `api-gateway.tf`, an event-source
mapping, a role policy, a route, a destroy of any kind -- is STOP. The plan's resource list is pasted into the change record.
**The EXERCISED check on the same act is the pre/post GET census over `scoped_amgt_route_table()`**, with the 200-sets equal and
the three changed bodies (refresh, rankings, thesis) read and pasted.

**If `2.0.0_SA_COO~Z` chooses to ship rk-6 and rk-7 as ONE deploy**, both CTO halves (rk-6 @`653de214b1` and this one) and both
COO halves together cover the union, the census is anchored before the combined act, and the plan list is the union of the two
halves' lists.

Push state: LOCAL on SITEZ.
