# COO half -- Cottonwood custom models into Models > Custom, Opal SMA sleeves into SMA

**Request:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/NEVER_WIDEN_REQUEST_COTTONWOOD_CUSTOM_AND_SMA_20261001.md`, blob
`e32aef245c` (@d2d219824a; msgs 103975, 103977). CTO half: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_COTTONWOOD_CUSTOM_AND_SMA_20261001.md`
@3338690683 (msg 103979), V2 amended to (a) under five identities. Andrew's word:
`ANDREW_DIRECT_20261001_203xZ_COTTONWOOD_CUSTOM_MODELS_AND_SMA_SLEEVES_YES_TO_ALL_FOUR.md`.

## SIGNED, 2026-10-01 ~22:0xZ, by 2.0.0_SA_COO~M

Signed on the blast radius the request measures: 9 of 16 documents move. Cottonwood: Custom 0 -> 24,020,674.01 and PFDE SMA
405,856.99, both out of Client; total 541,313,055.76 unchanged. Global: total and Custom +24,020,674.01; SMA and Client unchanged.
49 Financial and Inflection: null Custom members only, with no dollars moving. Both production branches are covered: DIVZ SMA present
(about 1,365,000 from Client to SMA at Cottonwood, no Global move) or absent (nothing from it moves). Rollback: code to pin
0f1a67e196 by plan and safe-apply; the dated documents restored by the CTO half's terms.

Read by this seat at signing:

1. **The package delta is exactly the three commits.** Over the 40 repo paths of the candidate's own
   `mdpf-gold-lambda/build_package.py`, `git diff 0f1a67e196 e20899bce7` touches 8 files (260 added, 22 removed). The
   same diff from the merge base `036b888e4f` is identical, and `0f1a67e196..036b888e4f` touches none of them. So the
   CLOUD merge inside the candidate carries no other seat's change into the function.
2. **The producer's rule for the DIVZ branch**, read in the diff of `build_dim_model_portfolio.py`: a leaf joins the
   attributed set when `is_opal` OR `rs.opal_sma_member_of(model_name)` names it. The row's `is_opal` label does not move.
   The no-renormalization rule stands, so a parent's other non-Opal remainder still stays in non_model.
3. **Writers, counted.** The served A4 documents have one writer, `mdpf-gold-lambda` (the publisher copies them). The
   Cottonwood dim partitions this builder writes: write census of
   `blackdiamond/cottonwood/gold/dim_model_portfolio/` since 2026-09-24: every version lands at 13:30Z on its own date (8 of 8 days)
   plus today's 19:18Z extra run. All are the Lambda's minutes. **A second writer exists in code and is dormant in the window:**
   the EC2 `mdpf-daily-runner` stage 6d (`infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh:547-556`) runs `build_dim_model_portfolio.py`,
   `build_cottonwood_mdpf_pair.py` and `build_cottonwood_mdpf_slice.py` with `--upload` from the scripts it `s3 sync`s from
   `opal-data-mdpf/code/scripts/` (`:125`). It left no dim write in the 8 days read.
4. **My own open acts are unaffected.** `healgap-cottonwood-catchup-m-20261001` leg D2 reads the catch-up's plan (unvalued
   dates against gold partitions), which this change does not touch: expected 0 planned, 0 built on 10-02. The
   `irpt_holdings_*` bundles minted tonight (ledger `irpt-inf-split-positions-m-20261001`) carry their live members.
   The `OPAL_SMA_LEAF_KEYS` effect the request names for `holdings_snapshot.py` reaches holdings only at a later mint.

## Conditions

1. **The candidate files are on CLOUD (`85dd7adc26`, merge `f3044f1e84`) and so are in the laptop push range.** If the push
   uploads `build_dim_model_portfolio.py`, `build_cottonwood_mdpf_pair.py`, `build_cottonwood_mdpf_slice.py` or
   `rebalancer_schemas.py` to `opal-data-mdpf/code/scripts/`, then that upload is the second writer's code move. In that case the
   rollback also restores those S3 copies to their prior versions. Otherwise hold them in the push (`0.0.0_AB_MSTR`'s list,
   msg 103967).
2. Delete-marks to serve today run only on Andrew's word for this change, recorded (as the CTO half states).

-- 2.0.0_SA_COO~M
