# ANDREW-DIRECT 2026-09-21 ~19:4xZ at the 0.0.0_AB_MSTR terminal -- push CLOUD for the SITEZ integration, after the MDPF sign-off

**Channel:** the 0.0.0_AB_MSTR terminal (laptop): a typed message, then an answer to an AskUserQuestion card.
**Recorded by:** 0.0.0_AB_MSTR, the same turn.

## VERBATIM

**Message:**

> **"also make sure that we push to CLOUD so we can integrate however necessary with Sitez because it looks like theyre waiting on some guidance from our side with regard to some of the naming for the backend work they are doing with opal-data-harvest which I believe we may have alreasy sorted iwth 4.0.0_SA_CRO earlier on the LGIC subject"**

**Card answer** (MSTR showed that the push would safe-deploy 4 unsigned Cottonwood/MDPF gold files):

> **"Sign first, then push (Recommended)"**

## Measured at ~19:45Z

- `origin/CLOUD..HEAD` = 174 commits; origin/CLOUD is d32d3ad8b8.
- The pre-push safe-deploy exposure ceiling is 6 `.py` files:
  - `data/assets/scripts/gold/build_cottonwood_mdpf_pair.py`
  - `data/assets/scripts/gold/build_cottonwood_mdpf_slice.py`
  - `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py`
  - `data/mdpf/scripts/gold/mdpf_revamp_model_crosswalk.py`
  - `data/inf/scripts/gold/lib/nna_coverage_guard.py`
  - `data/inf/scripts/gold/lib/tests/test_nna_coverage_guard.py`
- The mdpf tree is deploy-enabled (`safe_deploy_core.py` CODE_TREES "mdpf" -> opal-data-mdpf).
- His ~18:3xZ word, record @0b46309ec2, requires the CRO and CTO to sign off before the Cottonwood work
  ships.

## Ruling as stated

1. Push CLOUD.
2. Do it **after** `1.0.0_SA_CTO` and `4.0.0_SA_CRO` confirm their never-widen halves on the four MDPF files.
3. Then carry the SITEZ integration forward (the harvest naming work landed by 4.0.0_SA_CRO today:
   @1675a8f631, @b282500581, @74a988631d).

## Pending at the write

The CTO and CRO were asked at ~19:45Z (msgs 99187/99188). The push fires when both confirm. The ceiling is
re-read immediately before the push.

**4.0.0_SA_CRO's reply (99189): NOT SIGNED.** No package from 0.7.0_AE_CloudOps~V has reached that seat: no
pin, no byte-diff, no ledger entry.

The CRO also notes that the push is a DIFFERENT leg from the one it agreed to co-sign. It agreed to the
mdpf-gold-lambda minimal-pin build. The push is a safe-deploy of four gold scripts to opal-data-mdpf's
code prefix, which is LEG B in the 08-26 ledger. So its sign-off needs those four files' delta against
what S3 serves today, and the served keys the next run would move.

The CRO's recommendation matches his answer: sign first, then push. The CTO's reply is outstanding.
