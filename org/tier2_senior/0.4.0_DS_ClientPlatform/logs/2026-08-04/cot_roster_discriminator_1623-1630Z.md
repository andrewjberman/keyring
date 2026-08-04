# cot BD roster discriminator: Moderate Income = ADDITION (three-way confirmed)

**archetype:** VALIDATE
**Serial:** 0.4.0_DS_ClientPlatform
**Window:** 2026-08-04 ~16:23Z -> ~16:30Z (delta since cot_partial_floor_fix log)

## Arc

CTO 162352Z discriminator ask (gates the fresh 4/4 aum-metrics: the pair builder's
vocabulary gate fired on 'Opal Moderate Income Portfolio', stage 6 aborted pre-6e) +
162728Z amendment (CRO branch 3: also report the 'Opal - Income' residual's presence).

Evidence read: the FRESH gold dim the pair consumed --
s3://opal-data-assets/blackdiamond/cottonwood/gold/dim_model_portfolio/date=2026-08-04/
data.parquet (10 rows, model-grain: the relationship-grain collapse already happened at
the dim build; per-model rows read directly, nothing summed across models) vs
date=2026-07-28.

**THREE-WAY VERDICT: ADDITION.**
- (a) ALL prior is_opal models PRESENT at their SAME model_ids, values continuous
  (Conservative Growth 96/$31.25M; Long-Term Aggressive 12/$1.128M; Short-Term
  105/$16.27M; Intermediate-Term 224/$74.91M (+1 acct); Ultra Short-Term Income
  6/$1.443M). Prior-only set EMPTY. A rename shows a persisting id under a new name or
  an absent prior name -- neither occurs.
- (b) 'Opal Moderate Income Portfolio' NET-NEW: model_id fef636c2-c1d6-43df-91f9-
  1923e1b3b068, rebalance_model_type=STRATEGY, account_count=6,
  dollar_value=$5,003,805.83, accounts_with_value=6, value_date=2026-07-31.
- (c) 'Opal - Income ' residual PRESENT-UNCHANGED-IN-CLASS: 88597ef7, Strategy, 2 accts,
  $1,216,569.21 (vs $1,246,019.40 = -$29.4K ordinary day drift). The STOP-AND-ESCALATE
  branch (residual absent) does NOT hold.
- No transfer signature (residual -$29.4K vs Moderate Income $5.0M; no donor model shed
  ~6 accounts) -- new assignment activity, not meta-residual dollars re-entering
  by_model.

Riders delivered to CRO (vocabulary holder): the new row is STRATEGY-type (the F2
blend/carrier class -- the map entry needs a decomposition disposition, not just a
display name), and the entry must key through _norm() (the live roster carries a
trailing-space raw name 'Opal - Income ').

Reports: CTO 162711Z + 162812Z; CRO 162738Z + 162824Z. CRO mints opal_moderate_income;
the chain resumes on the map extension.

## Compiler Tools

Direct parquet evidence reads (2 partitions, both directions of the diff printed with
denominators) -- no comp-tool models the cot gold dim roster (the assets-tree gap,
already C-2-banked); hand-derivation labeled per the standing rule.

## Addendum ~16:30Z -- COO scope-widening (162838Z) discharged

COO widened to the same three-branch structure (CRO 162706Z) + one-message routing with
FULL denominators to the landing seat. Discharged 163028Z/163049Z: full rosters BOTH
vintages delivered (FRESH 10 rows / PRIOR 9 rows, single delta = Moderate Income) to
0.2.0_DS (who lands opal_moderate_income per the pre-authorized CRO+CTO co-word) + COO;
CTO/CRO already held the three-way verdict (162812Z/162824Z). Branch-3 HARD-STOP
explicitly does NOT hold (residual present, unchanged, no transfer signature).

## Blockers

None. Fresh-artifact tie reads resume on chain-green post map-extension (0.2.0_DS lands
the key; AE resumes the chain).
