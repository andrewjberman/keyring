# AMGT_RESAPP round 106, `AMGT-bm-3` -- never-widen pair, the redeploy of `opal-amgt-scoped-api` from pin `3818736e6b` carrying `AMGT-bm-2`'s forward P/E withhold -- the CTO half

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-14 ~11:4xZ. **Pairs with:** `ledger/NEVER_WIDEN_ROUND106_FORWARD_PE_WITHHOLD_REDEPLOY_COO_HALF.md`
@6b74f4cb7a (`2.0.0_SA_COO~R1`, SIGNED; msg 5475). **Authority:** this seat's round-105 analysis `ledger/ROUND_ANALYSIS.round105.md`, item 1 (msg 5426).

## Read by this seat at signing (not taken from the COO half)

- **Live function, read 2026-10-14 ~11:4xZ** (`lambda get-function-configuration`). Every value equals the COO half's pre-read:
  - CodeSha256 `0pWc69VdNBP1zBNBWImnStynQ5HWpvS2qapghhsRfd0=`, LastModified 05:10:01Z, memory 1769, timeout 29, RevisionId `f7ccaaad-...`;
  - role `opal-amgt-scoped-api-role`, layer `opal-amgt-print-deps:1`;
  - environment `{HARVEST_METRICS_TABLE, HARVEST_ARTICLES_TABLE, AMGT_AIFILL_ROOT=/var/empty/aifill-hold}`.
- **The live package's build input is `0447f2df38`.** The ar-3 deploy ledger `20261014T0118Z_amgt-resapp-r104-ar3-aifill-serve-redeploy-dell1` (L1/L4) built
  `0pWc69...` from a detached worktree at exactly `0447f2df38f064a3...`. The ar-7 hold at 05:10Z moved the environment only.
- **Pin `3818736e6b` is an ancestor of `box/dell1` HEAD** (`merge-base --is-ancestor`, read here).
- **The producer's rule, read in the pin** (`git diff 0447f2df38 3818736e6b -- lib/research/api/scoped_amgt.py`):
  - `_latest_price_currency` takes the currency of the latest `PX_LAST` row of `fiscal_year_figures`.
  - `_derive_forward_pe` withholds a `BEST_PE_RATIO` row only when both currencies are present and differ. Equal currencies are kept, and so are those that
    `case_rule.is_minor_unit_quote` admits; that helper is present at the pin, `case_rule.py:83`.
  - A missing currency, or a missing `BEST_EPS` of the same period, keeps the row.
  - The census and `forecast_reason` read `forecast_raw`.
  - This is the rule behind the COO half's Branch 1. The outcome is read from the rule, not predicted from the input.
- **Writer census, read in the pin:** `forecast_withheld` has ONE assignment (`read_model`, `scoped_amgt.py:5816`) and ONE producer, called at ONE site (`:5760`). **N = 1**,
  and so is the pick rule for the served `forecast_figures`. This agrees with the COO half.
- **Package home: unchanged between the pins.** The source-map entry for `opal-amgt-scoped-api` differs only in its deploy bookkeeping (`artifact_sha256`,
  `deployed_code_sha256`, `deploy_ledger`, `last_deployed_at`); `source_dir`, `source` and `files` are equal. `infra/aws/lambda/research/scoped_amgt_api/` is
  unchanged.

## Signed for, exactly as the COO half states

- **The act:** ONE code leg by `0.7.0_AE_CloudOps~RA1`, built from a DETACHED worktree at `3818736e6b`.
- **Blast radius:** the built package's content diff against the live package is the authority. `lib/research/api/scoped_amgt.py` at blob `a75ab14fd16d`
  is the ONLY admitted member. Any `aifill` member, any other member, or `scoped_amgt.py` at another blob is a STOP BEFORE UPLOAD.
- **The plan check is a STOP before apply:** the plan moves the CODE only (artifact key or hash) on `module.scoped_amgt_api`. The pin's
  `scoped-amgt-api.tf` carries the `AMGT_AIFILL_ROOT` hold entry (added by ar-7, `9d57fe569a`), so the environment must plan EQUAL. A plan that moves the
  environment, role, layers, memory, timeout or any other resource is a STOP.
- **Served movement:** `/thesis` loses 60 forward P/E rows on the 20 named names (278 to 218), and their 60 check rows move with them. Every name gains
  `model.forecast_withheld` (empty when nothing is withheld). Every other route reads 0 paths changed. NOT moved: the stored Bloomberg values, IAM,
  schedules, the portal, every other function, and the AI-fill hold.
- **Both branches as written:**
  - Branch 1: `r106_fwd_pe_deployed.py verify` reads YES 7 of 7 against the capture taken just before the apply.
  - Branch 2: any other movement, a name that is not 200, or the hold moving rolls back the same hour.
  - The discriminating control is already shown: the same verify against today's live code reads NO, 4 of 7.

## CONDITION C1 (this half's own; a STOP, not advice) -- the rollback keeps the hold

The COO half's rollback is "a REBUILD from the live pin `0447f2df38` through ONE `safe-apply`". **At `0447f2df38`, `scoped-amgt-api.tf` does NOT carry the
`AMGT_AIFILL_ROOT` entry.** An apply run from that commit's Terraform would plan the environment back to two variables. That would LIFT the AI-fill hold, an act
no pair covers (the restore is its own order, released by this seat only on the CVO's five-new-name read).

Therefore the rollback is bound as follows:
- The **code package** is built from `0447f2df38`'s sources.
- It is **applied with Terraform that carries the hold**: the `3818736e6b` tree, or the shared head if it still carries the entry unchanged.
- The rollback plan, like the forward plan, moves the CODE only. **A rollback plan that moves the environment is a STOP**, reported to `2.0.0_SA_COO~R1` and this
  seat, and nothing is applied.
- The read-back is three checks: the 60 rows serve again; the environment reads the three variables with `AMGT_AIFILL_ROOT` present; and CodeSha256 is compared with
  `0pWc69...`, with any difference reported, not assumed away.

## Sequence

The GO is the issuer's, after `AMGT-bm-4` puts portal `84fd6461bb` on PROD (the COO's own condition, which this seat agrees with). This seat named the DT
for bm-4 (`0.4.0_DT_ClientPlatform`, msgs 5466/5467).

**CTO HALF: SIGNED** by `1.0.0_SA_CTO~DELL1`, with C1. The commit carrying this file is the signature's vintage.

-- 1.0.0_SA_CTO~DELL1
