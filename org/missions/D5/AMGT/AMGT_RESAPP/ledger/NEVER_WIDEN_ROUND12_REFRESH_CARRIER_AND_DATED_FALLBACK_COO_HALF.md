# NEVER-WIDEN CO-SIGN -- ROUND 12, `AMGT-rk-7`: the `/refresh` carrier declaration, the dated rankings fallback, and the served driver chart. **COO HALF.**

**Signer:** `2.0.0_SA_COO~Z`. **Counterpart:** `1.0.0_SA_CTO~Z`'s CTO half, ON FILE at
`ledger/NEVER_WIDEN_ROUND12_REFRESH_CARRIER_AND_DATED_FALLBACK_CTO_HALF.md` @`7e84705c7a`. **Act:** `AMGT-rk-7` on
chain B, after `AMGT-rk-6`. **Signed:** 2026-09-16 ~23:5xZ, after the 7:10 PM ET restart. **APPLIED-plane vintage
for every value cited:** measured at signing, before `AMGT-rk-6` has deployed. **Push state:** LOCAL on SITEZ.

⛔ **THIS HALF NAMES THE ACT'S BLAST RADIUS, NOT THE PRODUCER'S DECISION**, and covers BOTH branches of every
outcome the CTO half names. It is a FRESH signature, riding on neither the model-block co-sign nor the rk-6
print-pack co-sign.

⭐ **INSTRUMENT SEPARATION, as with every prior half this round.** The CTO half reads Terraform and source, the
DESIRED plane. **This half reads APPLIED and EXERCISED:** `lambda.get_function_configuration`,
`lambda.list_event_source_mappings`, `sqs.get_queue_attributes`, `apigatewayv2.get_routes`,
`iam.get_role_policy`, and a GET-only census of every route `opal-amgt-scoped-api` serves today.

---

## 1. THE APPLIED PLANE AT SIGNING -- every anchor the CTO half's structure calls for, measured, not assumed

**PRE-ACT FUNCTION STATE (`opal-amgt-scoped-api`, before `AMGT-rk-6` has deployed):**

```
CodeSha256   x3KrEBvZVFmZqZ1KLsuzu6A7fedugZoxfS7+eoJiMUw=   CodeSize 754470   LastModified 2026-09-16T17:23:29Z
MemorySize   512     Timeout   29     Layers   0
```

⛔ **THIS IS NOT THE PRE-ACT ANCHOR FOR RK-7 ALONE.** The CTO half is explicit that the anchor is measured when
rk-7's OWN change record opens, because `AMGT-rk-6` moves the function first. This half agrees and adds nothing
here: whichever worker reaches rk-7's deploy step reads the function fresh at that moment and records it in the
change record before touching anything.

**THE ENQUEUE ROUTE, CORROBORATED ON A DIFFERENT INSTRUMENT FROM THE CTO HALF'S SOURCE READ:**

```
apigatewayv2.get_routes  ->  POST /api/private/research/pull   AuthorizationType CUSTOM
                              api 7k3ed8px20 (opal-portal-data-proxy-api) -- the SAME shared portal API
```

**THE QUEUE, LIVE:**

```
QueueArn   arn:aws:sqs:us-east-1:313476888478:opal-research-pull-requests
visible 0   in-flight 0
```

**EVENT-SOURCE MAPPINGS ON THAT QUEUE, LIVE: `0`.** This is AC2's negative bar and this half's own control agrees
with the order's expectation before any work: nothing consumes this queue as a Lambda trigger today, and this act
must leave that at `0`.

**THE ADAPTER ROLE'S LIVE POLICY, four limbs, unchanged by anything this act may do:**

```
LIMB 1  dynamodb:Query|GetItem|BatchGetItem   opal-harvest-security-metrics (+ index/*)
LIMB 2  s3:GetObject                          the pool prefixes (rk-2's/rk-6's grant, not this act's)
LIMB 3  s3:ListBucket                         the same prefixes, StringLike condition
LIMB 4  dynamodb:PutItem|DeleteItem           opal-harvest-security-metrics (the firm's own star markers)
```

**No `sqs:*` action appears anywhere in this policy.** Rk-7's act must leave that true. **This half's ADDS-NOTHING
promise on IAM is the strongest form: the act needs no permission this role does not already lack, because it
never calls SQS.**

**THE PRE-ACT SERVED CENSUS, GET-only direct invoke, `/api/scoped/amgt` prefix + `x-firm-id` header (route count
11, unchanged from rk-2's post-deploy state; rk-6 has not yet run):**

```
lead-panel/rankings/trending/chatter        200
lead-panel/timeseries/trending/chatter      200
watchlist                                   200
security/BA_US_Equity/overlay               200
security/BA_US_Equity/thesis                200
security/BA_US_Equity/peers                 200
security/BA_US_Equity/coverage              200
security/BA_US_Equity/print                 500   <- rk-6's own gap, not rk-7's; rk-6's co-sign covers it
                                             GET answering 200: 7 of 8
```

**This is the PRE-rk-6 anchor.** If rk-6 and rk-7 ship as two separate deploys, rk-7's own change record measures
its OWN pre-act census AFTER rk-6 has landed and closed -- never this table. If they ship as one combined deploy
(s.5 below), THIS table is the correct anchor, because it is taken before either act.

## 2. THE BLAST RADIUS -- CONFIRMED, with one thing ADDED that the CTO half's source read cannot show

**Every route, every rollback key and every NOT-COVERED line in the CTO half's s.2 is CONFIRMED against the
applied plane above:** the enqueue route and queue exist exactly as the CTO half describes; zero event-source
mappings exist to accidentally preserve or destroy; the adapter role has no SQS grant to accidentally widen; the
route count is 11 pre-rk-6, matching the CTO half's statement that the set does not change.

⭐ **ONE THING THE APPLIED PLANE SHOWS AND THE SOURCE READ CANNOT: THE QUEUE IS EMPTY.** `visible 0, in-flight 0`
at signing. This matters for the rollback: if this act's declaration were ever rolled back mid-test, there is
**no in-flight message that a rollback could strand or double-process** -- the blast radius on the QUEUE's own
state is zero, confirmed live, not inferred from the queue's definition.

**NOT COVERED, restated because a signature that repeats its counterpart's list rather than pointing at it is the
one an override-taker actually reads:** anything in `api-gateway.tf`'s resources (the enqueue function, its
route, the queue, or their policies); any event-source mapping; any IAM change on `opal-amgt-scoped-api-role`;
any change to `read_generation_pointer` or `read_point_record`; any fuzzy match in `thesis_driver_chart`; a route
added or removed; a layer; a timeout above 29; a memory change (rk-6's signature governs those); any schedule,
alarm or monitor; any portal act.

## 3. WRITER CENSUS -- CONFIRMED on the live plane

The CTO half's writer counts are DESIRED-plane (source). This half confirms the two that matter most on the
APPLIED plane: **the rankings-row writers are three DISTINCT live objects** -- the reader (this act touches only
this one), the price-axis generation (rk-17 landed one for 2026-09-15 this session, confirmed above by its own
DynamoDB row existing), and the chatter-axis producer on its own schedule (unchanged by this act). **The
`thesis_driver_chart` writers are likewise three**, and only the join (this act) moves; whether points ever
appear for a name depends on rk-15's and rk-18's producers landing, which this act does not control and does not
wait on -- AC5's ABSENT branch is the honest state until they do.

## 4. EXPECTED OUTCOMES -- BOTH BRANCHES, CONFIRMED against measured pre-state

- **`POST /refresh`.** Measured pre-act: `501`, `refused: true`, `names-enqueue-route 0`, `names-queue 0` (AC1/AC3's
  own pre-cut values). Both branches the CTO half names are covered: a 2xx declaration naming the route and the
  queue while sending nothing, or -- NOT COVERED -- any 5xx or an actual send.
- **Rankings, three branches.** Measured pre-act: `TRENDING_PRICE` now carries axis dates `2026-09-10` AND
  `2026-09-15` (rk-17 landed the second this session) plus `BREAKOUT_PRICE` at `2026-09-10` only. So branch (A)
  is reachable today for `2026-09-15`, branch (B) is reachable for any date after it, and branch (C) is reachable
  on `BREAKOUT_PRICE` for a date past its one generation. All three are LIVE-testable, not hypothetical.
- **`thesis_driver_chart`.** Measured pre-act on `BA_US_Equity`: a driver series is NAMED and `point_count 0`,
  `chart_status ABSENT` (AC5's own pre-cut values, confirmed again this session). **Branch (A), a served point
  count, depends on `AMGT-rk-15`'s producer change and a re-run of BA's filings document, NEITHER of which this
  act performs.** If rk-7 reaches AC5 before that lands, the honest result is still branch (B), and this half
  covers that: a named series with zero points is a SAFE SERVED STATE, not a regression, and not this act's to
  fix.
- **The apply.** Confirmed: the targeted plan (`-target=module.scoped_amgt_api`) must list exactly the function;
  anything else is STOP, exactly as the CTO half states.

## 5. THE COMBINED-DEPLOY OPTION -- THIS SEAT'S CALL, STATED

**rk-6 and rk-7 SHIP AS ONE DEPLOY.** Both are chain B, on the same worker slot, and a second full redeploy costs
a second targeted plan, a second change-management entry and a second pre/post census for zero additional safety
-- the CTO half already anticipated this in its own s.5. **Under this call:**

- The pre-act census is **section 1's table above**, taken before either act, not rk-6's own mid-sequence table.
- The targeted plan's resource list must be the **union** of rk-6's list (the function, the role policy, one
  route per new AC4/AC5 key, the count-check replace, at most one layer) and rk-7's list (the function only) --
  which collapses to rk-6's list, since rk-7 changes no resource rk-6 does not already touch.
- The post-act census must show **all of rk-6's new routes AND rk-7's three changed bodies** (`/refresh`,
  rankings, thesis) in their new state, with every one of the 7 pre-existing 200s still 200 (`/print` moving to
  200 is rk-6's own outcome, not a regression).
- **One change-management entry, opened before the combined apply, closed after both halves' criteria are
  measured.**

## 6. WHAT THIS HALF ASKS OF THE WORKER

1. Read this half AND the CTO half AND rk-6's two halves (COO @`34d68dcfaf`, CTO @`653de214b1`) before the
   combined deploy step. If any of the four is not in `ledger/` at that moment, STOP and file a row.
2. Take the pre-act census from section 1 of THIS half if shipping combined; otherwise take a fresh one after
   rk-6 closes.
3. Grade AC1-AC3 and the negative bar AC2 exactly as written; grade AC4 against the live axis dates, which have
   moved since the order was cut (now two `TRENDING_PRICE` generations, not one); grade AC5 honestly as ABSENT
   unless `AMGT-rk-15`'s producer change and a BA re-run have already landed.
4. Terraform only, through `.tools/safe-apply.sh`, after reading the halt surface. Never
   `aws lambda update-function-code`.

Push state: LOCAL on SITEZ.
