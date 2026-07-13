# OPAL_ASSETS -- PROVENANCE BRIEFING: where each tracked number comes from, and why they are all frozen at 2026-07-10

**Author:** 1.0.0_SA_CTO~B  ·  **Date:** 2026-07-13  ·  **Vintage of every citation below:** `be6a2ba31`
**Audience:** Andrew (primary), COO/MSTR/CVO, 0.8.0_AE_CloudComp (OPAL_ASSETS impl lane)
**Status:** FINDINGS. Authorizes nothing. Explicitly does NOT authorize an INF hold-lift (see section 7).

---

## 1. The one-paragraph answer

Andrew asked for the most recent value of each tracked item and the date that value is *from*.
Producing it surfaced something bigger than the numbers: **every number in `opal-assets-daily-aua` is
frozen at `run_date=2026-07-10`, for a single measured reason.** `mdpf-daily-trigger` is an
**event-driven convergence gate, not a cron** -- it fires only on `ObjectCreated` of the INF spine
sentinel `s3://opal-data-inf/gold/meta/pipeline-complete.json`. The INF gold chain is HELD by the
chokepoint, so no sentinel lands, so the mdpf runner never boots, so the emitter has no new input.
**The OPAL_ASSETS emitter is not broken. It is correctly idle.** Restarting the INF chain unfreezes
this table, and nothing else will.

Second finding, independent of the freeze: **each item's staleness is explained by WHICH TREE it is
read from.** 49F's $1.62B is stale at July 6 because it comes from the sovereign-held BD/Schwab tree;
49F's ETF ownership is stale at **June 24** because that series is built from the RPS book in the same
held tree. Inflection's $137M is current at July 10 (it comes from `opal-data-inf`). The ETFs sit at
07-08/07-09 on their own independent clock. **The headline $1,758,111,296.54 is a blend of a July 6
number and a July 10 number, and nothing in the table says so where a reader would notice.**

---

## 2. What the numbers actually are (live table, 532 rows, full pagination)

The certified headline is the sum of **exactly two** rows:

```
49f_schwab_custody     partner_aua     $1,621,251,574.22    as_of 2026-07-06
inflection_models      partner_aua     $  136,859,722.32    as_of 2026-07-10
                                       -----------------
                                       $1,758,111,296.54    <- ties to mdpf's certified headline
                                                               TO THE CENT (the AC7 write gate
                                                               refuses the partition otherwise)
```

The other 26 rows are **overlapping views of the same money**, not further addends. A naive
`SUM(value)` over all 28 rows in a partition returns **$8,261,089,407.78 -- a 4.70x overstatement**
(CVO measured this independently on the live table; it is the read hazard already routed as a PRD item).

**Latest value of every tracked item, with the date the number is actually from:**

| item | basis | value | **as_of** | additive |
|---|---|---:|---|---|
| `49f_schwab_custody` | partner_aua | 1,621,251,574.22 | **2026-07-06** | **Y** |
| `inflection_models` | partner_aua | 136,859,722.32 | 2026-07-10 | **Y** |
| `49f_smartx_platform` | partner_platform_view | 1,400,957,639.03 | 2026-07-06 | - |
| `49f_lt_conservative` | partner_model_detail | 750,069,142.08 | 2026-07-06 | - |
| `49f_intermediate` | partner_model_detail | 292,752,737.07 | 2026-07-06 | - |
| `49f_lt_aggressive` | partner_model_detail | 203,936,115.20 | 2026-07-06 | - |
| `49f_short_term` | partner_model_detail | 107,829,750.36 | 2026-07-06 | - |
| `49f_ultra_short_term` | partner_model_detail | 46,369,894.31 | 2026-07-06 | - |
| `49f_dividend_sma` | partner_model_detail | 18,536,958.91 | 2026-07-06 | - |
| `49f_growth_sma` | partner_model_detail | 4,843,817.65 | 2026-07-06 | - |
| `etf_divz` | etf_fund | 274,962,771 | 2026-07-08 | - |
| `etf_idvz` | etf_fund | 176,926,387 | 2026-07-08 | - |
| `etf_pfde` | etf_fund | 145,541,570 | 2026-07-09 | - |
| `etf_pfoe` | etf_fund | 80,961,056 | 2026-07-09 | - |
| `etf_divz__held_49financial` | etf_ownership | 172,375,369.44 | **2026-06-24** | - |
| `etf_idvz__held_49financial` | etf_ownership | 146,830,347.13 | **2026-06-24** | - |
| `etf_pfde__held_49financial` | etf_ownership | 123,202,894.89 | **2026-06-24** | - |
| `etf_pfoe__held_49financial` | etf_ownership | 66,945,563.93 | **2026-06-24** | - |
| `etf_divz__held_inflection` | etf_ownership | 15,878,460.73 | 2026-07-10 | - |
| `etf_idvz__held_inflection` | etf_ownership | 12,243,061.72 | 2026-07-10 | - |
| `etf_pfde__held_inflection` | etf_ownership | 10,210,192.86 | 2026-07-10 | - |
| `etf_pfoe__held_inflection` | etf_ownership | 5,845,695.33 | 2026-07-10 | - |
| `etf_divz__held_cottonwood` | etf_ownership | 3,680,767.99 | 2026-07-10 | - |
| `etf_idvz__held_cottonwood` | etf_ownership | 2,421,193.56 | 2026-07-10 | - |
| `etf_pfde__held_cottonwood` | etf_ownership | 1,999,511.95 | 2026-07-10 | - |
| `etf_pfoe__held_cottonwood` | etf_ownership | 1,154,132.56 | 2026-07-10 | - |

(plus 2 `basis_total` rows -- `_total__partner_aua`, `_total__etf_fund` -- which are totals, not addends.)

---

## 3. The architecture -- where each number is actually read from

```
OPAL_ASSETS PROVENANCE - where each of the 28 tracked numbers actually comes from

1. The ingestion plane - how a vendor book becomes a row in opal-assets-daily-aua

   SOURCE OF TRUTH          SILVER / GOLD            mdpf FEEDER (WS-*)        AGGREGATE            THE BUCKET
   ---------------          -------------            ------------------        ---------            ----------

  +------------------+                          +----------------------+
  | Orion / SMArtX   |  master 08242234         | WS-B                 |
  | platform book    | -----------------------> | wsb_49f_smartx_      |--+
  | (49F models)     |  per-account model_value |   model_aua          |  |
  +------------------+  daily on runner boot    +----------------------+  |
                                                                          |
  +------------------+  ** SOVEREIGN-HELD TREE **                         |
  | Black Diamond +  |  s3://opal-data-bd       +----------------------+  |
  | Schwab RPS       |   silver/allocations/    | WS-E                 |  |
  | s3://opal-data-bd|   schwab/silver/rps/     | build_mdpf_wse_49f_  |--+
  |  master 08242234 |   silver/fees/           |   non_model_aua      |  |
  |  (08335338 NOT   |   gold/aua_certification |  = custody_total     |  |
  |   pulled - G2)   | -----------------------> |    - model - sma     |  |
  +------------------+  49F's WHOLE custody book+----------------------+  |
                                                                          |
  +------------------+                          +----------------------+  |   +---------------+
  | INF / Eclipse    |  s3://opal-data-inf      | WS-C                 |  +-->| mdpf_aggregate|
  | gold/eclipse/    |   gold/eclipse/{date}/   | build_mdpf_wsc_      |--+   |   _aua.py     |
  | silver/eclipse/  | -----------------------> |   inflection_feeder  |  |   |               |
  | (Inflection AUM) |  per-model account grain +----------------------+  |   | 3.1: AUA =    |
  +------------------+                                                    |   | SUM_partner [ |
                                                                          |   |  model_aua +  |
  +------------------+                          +----------------------+  |   |  sma_aua +    |
  | ETF fund books   |  s3://opal-data-etfs     | WS-D2                |  |   |  non_model ]  |
  | silver/          |   silver/                | build_mdpf_wsd2_etf_ |--+   +-------+-------+
  |  netassets_daily |   netassets_daily.parquet|   netassets_feeder   |              |
  |  .parquet        | -----------------------> |  = etf_decomposition |       writes | {date}.json
  +--------+---------+  fund-level net assets   +----------------------+              v
           |                                                                 +--------------------+
           |                                                                 | SERVED (CloudFront)|
           |                                                                 | opal-data-portal-v2|
           |                                                                 | platinum/mdpf/     |
           |                                                                 |  aggregate_aua/    |
           |                                                                 |   {date}.json      |
           |                                                                 +---------+----------+
           |                                                                           |
           |  s3://opal-data-etfs/daily/{partner}/{date}.json                          | reads the
           |  ownership_value + source_as_of + account_count                           | SERVED body
           |  ** BYPASSES mdpf ENTIRELY - read direct by the emitter **                | ONLY
           |                                                                           v
           |                                                              +-------------------------+
           +------------------------------------------------------------> | opal-assets-daily-      |
              12 ownership rows: (4 ETFs x 3 partners)                    |   emitter  (Lambda)     |
              49F series is built from the RPS book = 08242234            |                         |
                                                                          | build_rows()      -> 14 |
                                                                          | build_ownership() -> 12 |
                                                                          | + 2 basis totals  -> 28 |
                                                                          | AC7 WRITE GATE: refuses |
                                                                          | the partition unless    |
                                                                          | SUM(additive)==headline |
                                                                          +-----------+-------------+
                                                                                      | 28 rows/day
                                                                                      v
                                                                          +-------------------------+
                                                                          | DynamoDB                |
                                                                          | opal-assets-daily-aua   |
                                                                          | PK=run_date SK=cohort_id|
                                                                          | GSI cohort_history      |
                                                                          | 532 rows / 19 partitions|
                                                                          +-------------------------+

2. The freshness plane - WHY every number is frozen at 2026-07-10 (measured, not inferred)

  +------------------+                     +------------------+                +------------------+
  | INF GOLD CHAIN   |  writes the sentinel| mdpf-daily-      | SSM-dispatches | mdpf-daily-runner|
  |                  | ------------------->|   trigger        | -------------->|  EC2 t3.medium   |
  | *** HELD by the  |  opal-data-inf/     | (Lambda)         | mdpf-daily-    | i-02448edb624a.. |
  | chokepoint:      |  gold/meta/         |                  |  dispatch.sh   | start-on-demand  |
  | INF_GOLD_        |  pipeline-          | EVENT-DRIVEN     |                |                  |
  | DISPATCH_RELEASE |  complete.json      | CONVERGENCE GATE |                | *** NEVER BOOTS  |
  | unset ***        |                     | - NOT a cron     |                | - nothing to     |
  |                  |  ** LAST WRITE:     | - fires ONLY on  |                |   dispatch ***   |
  |  -> no sentinel  |     2026-07-10      |   ObjectCreated  |                |                  |
  +------------------+     T14:52:54Z **   +------------------+                +--------+---------+
                           (comp-freshness: FAIL, 77.0h)                                |
                                                                                        | writes
                                                                                        v
  +------------------+                     +------------------+              +----------------------+
  | opal-assets-     |  reads the newest   | the emitter has  |              | platinum/mdpf/       |
  |  daily-aua       | <------------------ | NOTHING NEW TO   | <----------- |  aggregate_aua/      |
  |                  |  served partition   | READ. It is not  |  its only    | ** LAST WRITE:       |
  | newest partition |  = still 07-10      | broken - it is   |  input       |    2026-07-10        |
  | = run_date       |                     | CORRECTLY IDLE.  |              |    T14:53:44Z **     |
  |   2026-07-10     |                     |                  |              | (comp-freshness:     |
  +------------------+                     +------------------+              |  FAIL, 77.0h)        |
                                                                             +----------------------+

     >> THE SENTINEL DIED AT 14:52:54Z. THE mdpf PARTITION DIED 50 SECONDS LATER, AT 14:53:44Z. <<
     That 50-second gap IS the causal chain, measured on the live artifacts.

3. The query plane - how you reach a trustworthy number

    YOU (terminal)
        |  "what is Opal's AUM, and how stale is it?"
        v
   +--------------+   the ONLY safe query - `additive` is DERIVED from `basis`, never hand-set
   | DynamoDB     |   SUM(value) WHERE additive AND run_date = <newest>
   | query        |   -> 2 rows: 49f_schwab_custody + inflection_models
   +------+-------+   (a naive SUM(value) over all 28 returns $8,261,089,407.78 = 4.70x)
          v
   ANSWER back in your terminal:
       $1,758,111,296.54   <- ties to mdpf's certified headline TO THE CENT (AC7 gate enforces it)
       ...but read `as_of`, not `run_date`: $1.62B of it is a JULY 6 number.

  The "overlapping views of the same money" model is exact and deliberate:
  +----------------------------+------------------------------------------------------+
  | A DISJOINT ADDEND          | AN OVERLAPPING VIEW                                  |
  +----------------------------+------------------------------------------------------+
  | 49f_schwab_custody         | the 7 49F models - a SLICE of that same custody book |
  | inflection_models          | 49f_smartx_platform - the SAME 49F money, platform   |
  |                            |   lens instead of model lens                         |
  | = the whole book, once     | etf_divz - fund-level net assets, which ALREADY      |
  |                            |   contains what 49F and Inflection hold of it        |
  |                            | etf_divz__held_49financial - a SLICE of that slice    |
  +----------------------------+------------------------------------------------------+
  | additive = TRUE  (2 rows)  | additive = FALSE (26 rows)                           |
  | SUM these                  | NEVER sum these - they double-count the same dollars |
  +----------------------------+------------------------------------------------------+
```

---

## 4. Per-item provenance -- staleness is explained by WHICH TREE, not by luck

| item(s) | true source | why its as_of is what it is |
|---|---|---|
| `49f_schwab_custody` (**additive**) | `opal-data-bd` via **WS-E** -- `silver/allocations/`, `schwab/silver/rps/date={D}/`, `silver/fees/`, `gold/aua_certification/` | **SOVEREIGN-HELD TREE.** 07-06 and rolled forward since. |
| the 7 `49f_*` models + `49f_smartx_platform` | Orion/SMArtX via **WS-B**, master 08242234 | Same 07-06 vintage; a SLICE of the custody book above. |
| `inflection_models` (**additive**) | `opal-data-inf` `gold/eclipse/`, `silver/eclipse/` via **WS-C** | 07-10 -- the freshest thing in the table. Dies with the INF hold. |
| the 4 `etf_*` fund rows | `opal-data-etfs` `silver/netassets_daily.parquet` via **WS-D2** | 07-08/07-09 -- an **independent clock**, unaffected by INF or BD. |
| the 12 `etf_*__held_*` rows | `opal-data-etfs` `daily/{partner}/{date}.json` -- **read DIRECT by the emitter, bypassing mdpf entirely** | 49F's series is built from the **RPS book (08242234)** in the held tree -> **2026-06-24, nineteen days old**. Inflection/Cottonwood are fund-level and current at 07-10. |

**The single stalest number in the set is `etf_*__held_49financial` at 2026-06-24 -- and it carries
roughly half a billion dollars of ownership.** It is stale for the same structural reason the $1.62B
is: it is sourced from the sovereign-held Schwab/RPS tree.

Note also: cohort-8 (`49f_schwab_custody`) is `coverage_state=incomplete` **by design and correctly** --
master **08335338 is not pulled** (that is G2, sovereign-gated). The emitter discloses the undercount
rather than hiding it. Do not "fix" that flag; fix the producer when G2 lands.

---

## 5. GROUNDING -- how each claim is anchored (Rule 22 / 22a)

| claim | layer | grounding |
|---|---|---|
| the emitter reads ONLY the served mdpf partition + `opal-data-etfs/daily/{partner}/` | SOURCE | `infra/aws/lambda/opal-assets/opal-assets-daily-emitter/lambda_function.py:1-60, 623-745` @ `be6a2ba31` |
| the 5 basis grains; `additive` DERIVED from `basis`, never hand-set | SOURCE | same file, `:398-495` (`_is_additive`) |
| the AC7 write gate refuses a non-reconciling partition | SOURCE | same file, `:947-1080` |
| WS-C reads `opal-data-inf` gold/silver eclipse | SOURCE | `data/mdpf/scripts/gold/build_mdpf_wsc_inflection_feeder.py:18-20, 64-68` |
| WS-D2 reads `opal-data-etfs/silver/netassets_daily.parquet` | SOURCE | `data/mdpf/scripts/gold/build_mdpf_wsd2_etf_netassets_feeder.py:15, 54-55` |
| WS-E reads BD + Schwab RPS silver/gold | SOURCE | `data/mdpf/scripts/gold/build_mdpf_wse_49f_non_model_aua.py:51-64` |
| the chain topology (trigger -> runner -> feeders -> aggregate -> served) | DESIRED | `pipescript mdpf` -> thread `mdpf-global-view` |
| **the trigger is EVENT-DRIVEN on the INF sentinel, and is ENABLED** | **APPLIED** | `aws events describe-rule --name mdpf-daily-refresh-trigger` -> `State: ENABLED`, EventPattern names `opal-data-inf` / `gold/meta/pipeline-complete.json` / `Object Created` **literally** |
| the sentinel's last write | APPLIED | `comp-freshness artifact s3://opal-data-inf/gold/meta/pipeline-complete.json` -> `2026-07-10T14:52:54Z`, **FAIL, 77.0h** |
| the mdpf partition's last write | APPLIED | `comp-freshness artifact s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/` -> `2026-07-10T14:53:44Z`, **FAIL, 77.0h** |
| **the runner's last boot** | **APPLIED** | `aws ec2 describe-instances i-02448edb624a7a7cf` -> `State: stopped`, **`LaunchTime: 2026-07-10T14:52:58Z`** |
| the INF chain is held | APPLIED | `aws lambda get-function-configuration --function-name inf-gold-trigger` -> `INF_GOLD_DISPATCH_RELEASE: null` (absent = held, fail-closed) |

### The mechanism is EXERCISED, not merely correlated

I did not infer the causal chain from two artifacts stopping on the same day. The EventBridge rule's
event pattern names the sentinel key **literally**, and the boot trace catches the rule **in the act**:

```
14:52:54Z   sentinel written    opal-data-inf/gold/meta/pipeline-complete.json   (last ever)
14:52:58Z   runner EC2 BOOTS    +4s   <- the ObjectCreated rule firing
14:53:44Z   mdpf partition      +50s  <- the runner finishing
  ...       never again.        State=stopped. RELEASE=null. No sentinel -> no boot.
```

**Four seconds** between the sentinel landing and the runner booting is the rule executing. That is
the mechanism, observed. It is why "restart the INF chain" is the *only* thing that unfreezes this
table, and why nothing done to the emitter, the table, or mdpf itself will move a single number.

---

## 6. METHOD -- how this was found (and it was the comp tools that found it)

I started down the wrong road: reading the emitter source and hand-tracing S3 prefixes with raw
`grep`/`aws s3 ls`. That produces a file-local picture and it is exactly the "text-local,
connection-blind" failure Rule 21 exists to prevent. **The rail caught me** -- the PreToolUse HUD
denied a raw `aws s3 ls` freshness eyeball and routed me to `comp-freshness`. That reroute is what
produced the finding.

**What each tool contributed:**

- **`pipescript mdpf`** gave me the thing no amount of grepping would have: the *named-thread estate
  traversal*. It named `mdpf-daily-trigger` as an **"EVENT-DRIVEN CONVERGENCE GATE (not a cron)"**,
  named the exact sentinel key it fires on, named the runner instance ID, and listed all four WS-*
  feeders and the served prefixes -- **producers -> served -> frontend, in one call.** The "not a cron"
  detail is the entire finding. A grep for `mdpf` would never have surfaced it, because the fact lives
  in the *relationship* between a Lambda, an EventBridge rule, and a bucket in another pipeline's tree.

- **`comp-freshness artifact`** turned "the table looks stale" into two timestamps with a verdict:
  the sentinel and the mdpf partition, both **FAIL at 77.0h**, **50 seconds apart**. It is the
  validate-on-served check, not a listing plus an mtime eyeball -- and it is what made the causal
  chain visible rather than merely suspected.

- **The live primitives (Rule 22a)** closed the APPLIED gap that a comp-tool structurally cannot:
  `pipescript` parses Terraform (DESIRED) and its census is a 2026-06-15 vintage. `describe-rule`
  proved the rule is really ENABLED with that pattern; `describe-instances` gave the **14:52:58Z boot
  time** that upgraded the claim from correlation to an exercised mechanism.

**The lesson worth banking:** the raw-search instinct would have found every file and understood
none of the system. `pipescript` answered a question I had not thought to ask -- *"what makes this
run?"* -- and the answer was the whole story.

### Tool gaps found (routed, not adjudicated)

1. **`comp-freshness chain` has NO `mdpf`** -- it accepts only `{bd, inf, cot}`. **Nothing routinely
   scans the chain that produces the company's AUM number.** This is the
   *"a guard nothing invokes is indistinguishable from a guard that does not exist"* class, live.
2. **`comp-freshness ddb opal-assets-daily-aua` reads clean on a table it never looked at** --
   returns `WARN: No items found with PK prefix ''` because it cannot enumerate a composite
   `(run_date, cohort_id)` key. **A freshness oracle that cannot see the table prints no alarm for
   it.** The table has been frozen for 3 days and this tool has nothing to say about it.
3. **`comp-which` misrouted** this provenance question to `comp-transform schema-check` (a React
   component checker). Per NFRA_COMPRAIL, a repeat misroute for one intent is a coverage gap ->
   build the tool.

---

## 7. WHAT THIS DOES AND DOES NOT AUTHORIZE

**This briefing authorizes NOTHING. Read this section before acting on anything above.**

- **It is NOT an argument to lift the INF hold.** The freeze of this table is a **consequence** of the
  hold, and it is a *cheap* consequence -- a stale AUM number that is honestly labelled. The hold
  exists because `patrick_scanlan` is short **$52,604.80** on the served spine and **14 accounts hold
  $439,326.22** of served NNA that today's source cannot reproduce, surviving **by accident**. A stale
  dashboard is not a reason to trade those away. **The pressure to lift the hold so a number refreshes
  is precisely the pressure the hold exists to withstand.**
- **It does NOT authorize touching the mdpf runner, the trigger, or the sentinel.** Do not "kick" the
  chain, do not hand-write a `pipeline-complete.json`, do not enable anything. Writing that sentinel by
  hand would dispatch the runner **and is functionally an INF chain release by the back door.**
- **It does NOT authorize clearing cohort-8's `incomplete`.** That flag is correct and structurally
  unclearable until G2 lands AND mdpf emits a master marker. Fix the producer, never the disclosure.
- **The rule stays FUNCTIONAL, not lexical:** not *"does this say INF?"* but ***"would doing this
  ADVANCE THE INF CHAIN?"*** Everything in section 6's freshness plane is downstream of that question.

**What it DOES support, and what I am routing:**

1. **[0.8.0_AE_CloudComp]** The read-hazard restructure already routed: **a non-summable row must not
   carry a summable attribute named `value`.** This briefing adds a second requirement --
   **a partition must disclose its BLENDED vintage.** `_total__partner_aua` correctly carries the
   worst contributor's `as_of` (07-06); nothing surfaces that to a reader of the number.
2. **[CTO / tooling]** The three tool gaps in section 6. Gap 1 and 2 are the same failure in two
   instruments: **the AUM chain has no freshness oracle that can see it.**
3. **[Andrew]** Unchanged from earlier: the daily gaps (06-25 -> 07-02, 07-09 missing) need an explicit
   yes/no against the "bullet-proof DAILY" mandate.

---

*-- 1.0.0_SA_CTO~B, 2026-07-13. Every number in this document was read from the live artifact, never
from a ledger. Every causal claim carries its APPLIED grounding. The one claim I could not exercise --
whether the runner would boot if a sentinel landed -- I did not make.*
