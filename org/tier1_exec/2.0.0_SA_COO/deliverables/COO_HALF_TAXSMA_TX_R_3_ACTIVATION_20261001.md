# COO half -- MDPF_TAXSMA TX-r-3, Tax SMA activation

**Request:** `org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/4.0.0_SA_CRO/NEVER_WIDEN_REQUEST_TX-r-3.md`, **blob `d2598ef965`**
(the file with its 17:3xZ addendum; the same blob the CTO half binds). Asked of `2.0.0_SA_COO~M` by `4.0.0_SA_CRO`, msg 103922.
Andrew's word: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261001_170xZ_TAXSMA_APPLY_AND_DEPLOY_NOW_WITH_EGRESS.md`
@28e5589af0. CTO half: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_TAXSMA_TX_R_3_ACTIVATION_20261001.md` @1b43d6f201.

## SIGNED, 2026-10-01 ~17:3xZ, by 2.0.0_SA_COO~M

On the blast radius the request measures: turning Tax on moves 9 of the Gold function's 16 documents as its table states, and
leaves 7 identical. All five branches are covered (complete on the frontier date; activation day with no dollar moved; a day Tax
cannot be read, carried and dated; a Cottonwood Tax account gaining a model, withheld and carried; Tax off). The rollback is
capability off and switch OFF, effective from the next run, as the CTO half reads it.

**What this half reads that the CTO half did not, so the two halves together cover the writers:**

1. **THE PUBLISHER'S RULE, read** (`infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher/lambda_function.py` at HEAD,
   `_publish_one` :356-430 and `TAXSMA_ROLLOUT_SWITCH` :131). It copies the Gold document's body to
   `<SERVE_ROOT>/<scope>/<type>.json`, adds a `_provenance` block, and -- only with the switch ON, only on a category-views
   document that carries the Tax member -- adds the stamp fields (`taxsma_coverage`, the contract version). It changes no value.
   An unchanged source sha writes nothing. So every dollar the request names moves in the Gold function, and the publisher
   carries it verbatim.
2. **THE WRITER COUNT, measured on the served keys.** Each of the 9 changing documents' newest dated key
   (`portal/gold/mdpf/{49financial,global,cottonwood}/{aum-metrics,category-views,aggregate-aua-timeseries}/2026-09-30.json`
   in `opal-data-assets`) has exactly ONE stored version, written 2026-10-01 13:31Z, the Gold function's run. A third principal
   is PERMITTED to write that prefix -- `mdpf-daily-runner-ec2-role`, statement `AssetsPortalGoldMdpfAccrualBridgeWrite20260729`
   on `opal-data-assets/portal/gold/mdpf/*` -- for the accrual bridge's own objects (its bundle is
   `portal/gold/mdpf/_code/mdpf-accrual-bridge.tar.gz`). The single version per key says it did not write these documents
   today. Writers of the named documents: 2 (Gold function, publisher), 2 rules read between the halves; 1 more permitted, not
   writing them.
3. **THIS SEAT'S OWN COUPLING.** The HEALGAP catch-up's acceptance leg S on the same 2026-10-02 13:30Z run reads Cottonwood's
   served model dollars on five past dates (ledger `healgap-cottonwood-catchup-m-20261001`). Activation day moves no dollar
   (branch 2) and touches no past date, so that read is unaffected; the CTO's amendment of condition 3 admits exactly branch 2.

**Not verified by this seat:** the probe's two builds; the Gateway release's contents and the Graph read's scope; whether a
dated document already written with Tax can be rewritten the same day. **Not covered:** portal PROD promotion (put to Andrew by
name, as the request and the CTO half say).

-- 2.0.0_SA_COO~M
