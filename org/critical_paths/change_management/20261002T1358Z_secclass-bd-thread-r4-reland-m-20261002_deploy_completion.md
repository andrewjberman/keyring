# Deploy Completion Record
**Date opened:** 2026-10-02T13:58:17.281364+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS BD thread r3 RE-LAND (r4): every class in the mix + the identity read; half blob f926b46157, CTO batches 156/161/173
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P | verify | portal PROD carries eb90f2ad (precondition, Andrew's promote) | ls-remote PROD + merge-base with positive and negative control | 13:56:40Z ls-remote origin refs/heads/PROD = f76b02acb684613699f9fe076c33a0e07c15e056 (tag portal-v2.1.194, Andrew's promote record @0abef798f7, CTO 104283 batch 173); merge-base --is-ancestor eb90f2ad f76b02acb6 = true; positive control old PROD b3a1d8a638 ancestor = true; negative control ed40c8ee (local-only commit) ancestor = false. | CLOSED 20261002T135905Z |
| M | git | safe-merge coo-m-bd-mix-classes into CLOUD + SERVE-RELEASE-ACK commit removing the four DEPLOY-SERVE-HELD lines; stop: merged tree differs from CLOUD only in the ten branch files | merge hash + tree check + release commit |  | OPEN |
| G | s3-prefix | safe-deploy C_06, D_03, D_04, lib/etf_classifier.py, lib/mix_views.py to opal-data-bd code/gold; prior VersionIds recorded first | comp-pipescript deployed MATCH rows + prior VersionIds |  | OPEN |
| W | verify | C_06 watermark keys set back one partition (both keys), prior versions recorded | before/after watermark reads |  | OPEN |
| R | verify | ONE ad hoc QA run bd-gold-trigger incremental: mix_summary lists every class, sums to 100, unclassified <= 5.0 pct; identity hop counts in the log; z08327149 VXX structured/Hedge ties | served key reads + run log |  | OPEN |
| S | verify | next scheduled BD gold fire reads the same; one walked 49 Financial page on PROD readers | served key reads + page walk |  | OPEN |

## Log

- 20261002T135817Z OPENED by 2.0.0_SA_COO~M with 6 leg(s)
- 20261002T135905Z LEG P closed: 13:56:40Z ls-remote origin refs/heads/PROD = f76b02acb684613699f9fe076c33a0e07c15e056 (tag portal-v2.1.194, Andrew's pro
