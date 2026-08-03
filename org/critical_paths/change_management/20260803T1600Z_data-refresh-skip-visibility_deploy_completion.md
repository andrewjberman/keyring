# DEPLOY LEDGER: opal-data-refresh-api -- MDLP_MONPUB.W3 Skip*/Choice state visibility

**Opened:** 2026-08-03T16:00Z by `0.2.0_DT_PortfolioAnalytics` (at deploy START, per NEVER#6)
**Status:** **CLOSED 2026-08-03T16:20Z -- APPLIED + VERIFIED, all legs closed. Live CodeSha256
`dH/GOrT+Pj1/Jj3daUVPjDnY5MiROYYd8m3OebhE5yQ=` (LastModified 16:08:22Z), 0-diff, differential PASS
on live execution ba852138 (exec-75a7627c8734): steps array carries labeled SkipBothPKLs +
SkipDataPKL/SkipModelPKL/SkipCMAExcel/SkipPeerExcel + all 8 Check* Choice states; 25 steps total,
Task order preserved, zero Task steps lost. Tag data-refresh-v2.4.0 EXISTS (verified cat-file -> tag,
points at 405512137c whose ancestry contains ci 261cf7b388 + code b48785adad); push rides the MSTR
integration window (LD-0367 -- lane cannot push). Record commit 2603dca42f under audited
CLOUD_OPS_OR_ETL override (enumeration gap: TO assigns DT the deploy leg, lane enumerates AE-only).**

## Authorization
- CTO GO 20260803T145458Z (MDLP_MONPUB deploy support; TO `1.0.0_SA_CTO-2026-08-03-monpub-w3`).
- Spec: `docs/architecture/MDLP_MONPUB_MANIFEST_REGRESSION_FIX.md` @d59fc15920 section 3 W3
  (CVO conditional-GO folded; Choice-state widening is the CVO addition).
- CTO ruling (via DS log 5dd8ddfe9c): W3 stands as coded (Pass + Choice widening).

## The change
- Code: DS commit `b48785adad` -- `infra/aws/lambda/data_refresh/lambda_function.py` (+22/-3).
  `handle_status()` parses PassStateEntered/Exited + ChoiceStateEntered/Exited (was TaskState* only);
  STATE_LABELS gains all 7 Pass states (denominator cited in-code: 50 states = 28 Task / 8 Choice /
  7 Pass / 5 Parallel / 1 Succeed / 1 Fail). Visibility only -- no alarm/notification machinery.
- Deploy: TF-only via `.tools/safe-apply.sh`, `infra/aws/terraform/data-refresh/`,
  artifact `data-refresh/opal-data-refresh-api.zip`.
- Baseline CodeSha256 pre-deploy: `BVKpj9pdZcmA7g1fIfefL7QPdai7lW8ywUIKnOg1XtE=` (live 2026-08-01T19:12:31Z).

## Legs (close each; unclosed at session end = COO alarm)
- [x] Artifact build + S3 upload write-verified (sha dH/GOrT+... size 18604, metadata match)
- [x] Source-map delta committed 261cf7b388 (clean single-line delta; the earlier inf-lane sweep
      happened in W2's record commit fa6f891aeb and is disclosed separately -- see note below)
- [x] terraform plan: exactly the one Lambda hash change (BVKpj9... -> dH/GOrT+...)
- [x] safe-apply: apply complete (1 changed, 16:08:22Z)
- [x] 0-diff second plan ("no differences")
- [x] Live CodeSha256 changed from baseline (verified get-function-configuration)
- [x] Phase-3 differential: PASS -- labeled SkipBothPKLs + 4 sibling skips + 8 Check* states,
      25 steps, statusCode 200, on the DEPLOYED handler against live history
- [x] Tag data-refresh-v2.4.0 created + existence verified (cat-file -> tag); push = MSTR window
- [x] Ledger closed 16:20Z

## Post-hoc note (W2's record commit, same session)
record-terraform-deploy.sh's auto-commit (fa6f891aeb, yang leg) commits the WHOLE source map and swept
0.7.0_AE_CloudOps~E's uncommitted inf-etf-ownership-daily files-list hunk (files still untracked).
Disclosed to lane owner + MSTR 16:06Z. Process gap flagged to CTO: the record script needs a scoped
pathspec or a co-tenant dirty-hunk pre-check.

## Note
Prior ledger for this Lambda: `20260717*` entry (07-17) -- separate change, closed; noted per TO.
