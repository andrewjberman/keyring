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

## ADDENDUM 1 (~03:5xZ) -- site Z 1.0.0_SA_CTO~Z msg 32344

aw-1 to `0.7.0_AE_CloudOps~DELL1` STANDS; both never-widen halves stand, because they name the act, not the applier. The four lanes
`~ZV/~ZQ/~ZW/~ZC` HOLD no act until Andrew answers site Z's question: does "Do not seat site-Z CloudOps agents for dell1's deploys"
also cover site-bound acts? Until then no site-bound order is re-addressed; each stays as issued. `2.0.0_SA_COO~H1`'s R2-L3 at
`0.7.0_AE_CloudOps~Z` collides with Rule 27, because ~Z holds NFRA_OPLGTW; that re-ruling is open with `1.0.0_SA_CTO~Z`. Broadcast:
msgs 1610-1615.

## ADDENDUM 2 (~04:1xZ) -- site Z LIFTS its hold (msg 1642, bus 91f67522)

Addendum 1's hold is lifted: it was site Z's caution, not a ruling. The table above governs as written. Site-bound orders go to
`~ZV/~ZQ/~ZW/~ZC` (all LIVE), and pure cloud acts go to `0.7.0_AE_CloudOps~DELL1`. `2.0.0_SA_COO~W1`'s restore @33d4bbc32a is undone:
bs-3 and bs-4 go to `~ZW`. Still open with `1.0.0_SA_CTO~Z`: `2.0.0_SA_COO~H1`'s R2-L3 at `~Z` (Rule 27, ~Z keeps NFRA_OPLGTW).

Consequences for fold `CTO_FOLD_UNBLOCK_RIVALS_CORPUS_SECHIST_20261009.md` @79c8d84e65:
- Section 0: the sign-in pre-flight's site-Z owner is `0.7.0_AE_CloudOps~ZV`, ordered by `2.0.0_SA_COO~V1` as a one-read ask. The
  queue booking is unchanged.
- Section 2: the CORPUS re-pin lane is `0.7.0_AE_CloudOps~ZC`, and the 12:45Z cut-off and fallback stand.

## ADDENDUM 3 (~05:4xZ) -- dell1 IAM parity APPLIED (TO-APPLY-27); three conditions ride with the grant

Relayed by `0.0.0_AB_MSTR~DELL1` msg 1797 from the laptop `0.7.0_AE_CloudOps` (msg 107753). The identity apply was exact 1/1/0 at
05:39:17Z and the transcripts KMS key exact 0/1/0 at 05:40:13Z; live verification is running. Conditions from the laptop `1.0.0_SA_CTO`.
Every dell1 order to a `0.7.0_AE_CloudOps` lane (`~DELL1`, `~SC1`, `~RA1` and any new one) carries them as criteria:
1. A send that writes a firm data bucket, or that assumes the 49F principal outside the runner's own documented job, is told to the
   laptop FIRST.
2. Every send to `mdpf-daily-runner` is reported after the fact, with its command id and purpose.
3. 49 Financial data is never written into another firm's tree.
