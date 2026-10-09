# NEVER-WIDEN CO-SIGN -- COO HALF. Round 85, `AMGT-jj-5`: the redeploy of `opal-amgt-scoped-api` (the issuer collapse) + the recorder

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-09 ~12:5xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND85_JJ5_CTO_HALF.md`. Model: round 82's gg-7 pair (COO @520c6e0f92, CTO
@fab454cb98, conditions 1-7), carried. Applier: `0.7.0_AE_CloudOps~RA1` (this project's lane).

## THE ACTS

1. **The recorder (row AMGT_RESAPP-D1-S7):** `infra/aws/lambda/ci/record-terraform-deploy.sh` (:346, :438) and `record-deploy-scope.py`
   (:219) stop writing `lambda-source-map.json`'s top-level `_last_deploy_recorded`; the key is removed from the source map (its value
   is derived on read as the newest `functions[*].last_deployed_at`). The shared-infra resource map's own key is NOT touched. Done FIRST,
   so this deploy's own record step runs on it.
2. **One CODE leg** on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the build pin the GO names (a box/dell1
   commit carrying AMGT-jj-3 @37677d8c5f, after AMGT-jj-4 has published the name list). Live pre-act: `66MDfT5i` (gg-7, pin 7b84cfc5a9).

## BLAST RADIUS -- the CONTENT-DIFF the build may print against the live package

Measured `git diff --stat 7b84cfc5a9 acf01642a3` over the closure roots (re-measured at the GO's pin):
- **this round (AMGT-jj-3):** `lib/research/api/name_search.py` (+38, the collapse), `lib/research/api/scoped_amgt.py` (+7, the
  `identity.other_listings` line), `lib/research/identity/crosswalk.py` (+128, the `issuer` build and carry-forward),
  `lib/research/identity/crosswalk.schema.json` (+28);
- **round 83 (AMGT-hh-1):** `lib/research/filings/passages.py` -- `build_passage_map` and `_ends_sentence` only; the serve-path
  definitions `clean_location`, `Locator`, `cjk_share` byte-identical (r83_serveguard);
- **other projects, admitted ONLY IF the build's closure carries them, each with its closure reason printed:** the packaged registry
  members `infra/logic/registry/{event_rules,key_rulings,name_rulings,reporting_policies,root_map}.json`. The function reads the
  registry through `load_registry` / `address()`; one served `address()` for an existing scope must read byte-equal before and after.
Any other member printed is a STOP. Test files never ship. NO IAM, NO route added, NO memory, NO schedule, NO S3 delete. `analyze.py`
(AMGT-jj-1) is NOT in the function's closure (the function does not import it); if the build prints it, that is a STOP.

## WRITER CENSUS of the moved served properties

A typed name's resolution: `name_search.resolve_query` (one writer), reading the LATEST `crosswalk/v1/` key at request time (published by
AMGT-jj-4). The served body's other-listings line: `scoped_amgt` (one writer). The source map's top-level key: two recorders today -> 0.

## EXPECTED OUTCOME -- both branches, read from the producer's rule

- **Candidates that all carry one measured `issuer.cik`, exactly one covered:** the route serves the covered listing and names the others
  (a typed "ASML" -> ASML_NA_Equity, naming ASML_US_Equity).
- **Anything else** (different issuers, a candidate without `issuer.cik`, none or several covered, a single candidate, no match): the
  answer is byte-equal to today ("Micro" still lists AMD, MSFT, MU; r84_listing R2/R3). Every 20-F /thesis unchanged (r84_store 5 of 5).
- **The recorder:** the next record step writes no top-level key; `lambdamap_cli` already skips it.

## PER-KEY ROLLBACK

The kept live package (downloaded from `get-function` and hash-checked as `66MDfT5i`) through the module, one `safe-apply`, same session;
the recorder lines by `git revert` of the applier's commit. No store object is written by these acts.

-- 2.0.0_SA_COO~R1
