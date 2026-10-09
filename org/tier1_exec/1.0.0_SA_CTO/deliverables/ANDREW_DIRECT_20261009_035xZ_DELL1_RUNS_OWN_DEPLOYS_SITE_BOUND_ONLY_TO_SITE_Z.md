# ANDREW-DIRECT ~03:5xZ 2026-10-09 (via site Z) -- dell1 runs its own deploys; only site-bound acts go to site Z

**Words, verbatim** (at the `0.0.0_AB_MSTR~Z` terminal, bus e01b768c, relayed by `0.0.0_AB_MSTR~DELL1` msg 1587):
*"why is DELL1 sending deployment orders here? They should be able to run deploys on their own box"*

**Ruled by:** `1.0.0_SA_CTO~DELL1`. The ruling adopts site Z's reading as written.

## Ruling

1. **A pure cloud act (a Terraform apply, a Lambda or S3 deploy, an AWS read) issued by a dell1 project is issued to
   `0.7.0_AE_CloudOps~DELL1`**, never to a site-Z lane.
2. **Only SITE-BOUND acts go to site Z.** An act is site-bound if it needs the Bloomberg Terminal or BLPAPI, or a site-Z Windows user's
   sessions or scheduled tasks. Site-bound acts go to the per-project Codex lanes: `0.7.0_AE_CloudOps~ZV` (ETFS_RIVALS), `~ZQ`
   (MDPF_DEMQUE), `~ZW` (AMGT_HARVST), `~ZC` (AMGT_CORPUS). A dell1 project without its own lane keeps `0.7.0_AE_CloudOps~Z`.
3. **Unchanged:** a dell1 change to a site-Z producer path still needs `1.0.0_SA_CTO~Z`'s never-widen half. That rule governs WHAT may
   change, not WHO applies it.

## Dell1's orders at site Z (census: `<issued_to>...~Z` over org/missions, 16 hits, 7 in dell1 projects)

| order | issuer | class | issued_to becomes |
|---|---|---|---|
| ETFS_RIVALS.TO-APPLY-R28-aw1 (rivalfunds Lambda, Terraform) | `2.0.0_SA_COO~V1` | cloud | `0.7.0_AE_CloudOps~DELL1` (window 11:00-12:55Z) |
| ETFS_RIVALS.TO-RELAY-tw1-vehicle-log | `2.0.0_SA_COO~V1` | site-bound (terminal) | `~ZV` |
| MDPF_DEMQUE.TO-DQ-t14 demand-ledger uploader | `2.0.0_SA_COO~Q1` | site-bound | `~ZQ` |
| AMGT_HARVST.TO-HVST-bs-3 runner, bs-4 r47 resume | `2.0.0_SA_COO~W1` | site-bound (Windows user) | `~ZW` |
| AMGT_CORPUS.TO-READ-R40-ap10b-lv fire log | `2.0.0_SA_COO~C1` | site-bound (13:00Z read) | `~ZC` |
| MDPF_SECHIST.TO-READ-R2-L3 pull exit and budget line | `2.0.0_SA_COO~H1` | site-bound (terminal pull log) | stays `~Z` (no SECHIST lane) |

Each issuer amends its own order (Rule 27 L6: an issuer amends without a CTO ruling) and states the amendment in the commit.
