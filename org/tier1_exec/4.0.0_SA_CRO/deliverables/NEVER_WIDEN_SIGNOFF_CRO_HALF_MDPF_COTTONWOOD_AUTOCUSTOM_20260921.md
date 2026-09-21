# NEVER-WIDEN SIGN-OFF -- 4.0.0_SA_CRO's half -- mdpf-gold-lambda Cottonwood auto-custom (Phase A + B), LEG A + LEG B

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Authority for this seat to hold the half:** Andrew-direct 2026-09-21 ~18:3xZ at `0.0.0_AB_MSTR`, VERBATIM *"~V Does
work, CRO and CTO signs off"* (record @`0b46309ec2`) -- the half the standing rule gives the COO, THIS deploy only.
Scope widened to LEG B by his ~19:45Z *"Sign first, then push"* (record @`1ab93ec740`).

## VERDICT: **SIGNED** (2026-09-21 ~20:0xZ)

**Signed against, exactly:**
- the packet `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/NEVER_WIDEN_SIGNOFF_PACKET_MDPF_COTTONWOOD_AUTOCUSTOM_20260921.md`,
  **blob `2c59f07389378f8859ce445d76bfe660e346ff22`** @`f8c960746b` (blob id re-derived by this seat: `git rev-parse`);
- **LEG A zip sha256 `9c6db39ae8ae7c9d21060dfbdc5bb451053fbca9564cd046f3df75090804d0cd`**, 868,952 B, pin
  `74d7efe1449b47587cf0d8ca47e3a0f9824bf297` (Phase A + B). NOT the Phase-A-only fallback;
- **LEG B's packet s.5 table AS RE-DERIVED AT PUSH TIME.** A script in the push range that is not in that table is
  OUTSIDE this signature, and the push does not proceed on it without a new read.

This half signs the BLAST RADIUS and the ROLLBACK per key, both branches. **It does not sign the decision to ship
Phase B.** Packet line 9 attributes "Phase A + Phase B ship together" to "CRO/CTO 99196"; this seat's 99196 only
measured that Phase B rides the push. The ship decision is `1.0.0_SA_CTO`'s (99198), on Andrew's /open-calls call 2.

## WHAT THIS SEAT VERIFIED ITSELF (different instruments from the packet's, ~19:5xZ-20:0xZ)

| claim | this seat's instrument | result |
|---|---|---|
| running Lambda | `lambda get-function-configuration` | CodeSha256 `evIYCXURor4V++Ci4HsgwE8zIPZva/BAL+ICaLJIiAE=`, 835,383 B, 2026-09-15T06:09:14Z, `MDPF_GOLD_COMMIT` `48b8671569...` -- **matches s.1** |
| LEG A rollback artifact | `s3api head-object` on the latest version | `9GsracvIPvfBMzF1dttMpew0TkQtt.qg`, 835,383 B (= running size) -- **matches s.3** |
| the zip to upload | `sha256sum` + `wc -c` on `.scratch/mdpf_cot/built_ab.zip` | `9c6db39a...0cd`, 868,952 B -- **matches s.1** |
| LEG B bytes after push | `git rev-parse HEAD:<path>` x4 | `127bad164b` / `4a9a649e60` / `30a1ac7249` / `34c1752129` -- **matches s.5** |
| LEG B bytes served now | `aws s3 cp` (Windows path) + `git hash-object` | timeseries `3e1423e4a1` == `5e8ba0e1d4`'s blob (MDPF_TAXSMA, served 08:55Z) -- **matches s.5** |
| served-vs-HEAD delta, timeseries | full `diff` of the served copy vs HEAD | 18 lines, all Phase B -- the Tax overlay is ALREADY served (corroborated by 0.0.0_AB_MSTR and 1.0.0_SA_CTO on two further instruments) |
| LEG B rollback | `s3api head-object` x4, bucket versioning | Enabled; VersionIds `9sQ6pQNR...`, `b59tDxx...`, `NA2MepxP...`, `syiCAA6n...` -- **match s.5** |
| WRITER COUNT, served gold | `git grep -l 'portal/gold/mdpf' -- '*.py'` (16 non-test files) + write-verb read of each | writers: `mdpf_gold_consolidator.py`, `dim_mdpf_aum_metrics.py`, `build_portal_gold_accrual.py` = **N=3 -- matches s.4**; `opal-assets-mdpf-portal-publisher` READS gold and writes platinum = the platinum **N=1**; `org/modules/graph/pipeline_cli.py` names the path only as a static-analysis regex, not a writer |

Not re-derived by this seat (taken from the packet, stated as such): the discriminating import test and QA dry-runs
(s.2 items 2-5), the name census (s.2 item 6), the 0-of-7 legacy run_step import census (s.5).

## THE BLAST RADIUS THIS HALF COVERS

- **LEG A:** one new version of `s3://opal-data-assets/portal/gold/mdpf/_code/mdpf-gold-lambda.zip`; Lambda
  `mdpf-gold-lambda` code + env `MDPF_GOLD_COMMIT`; one `gold-lambda.tf` literal. The targeted plan must show EXACTLY one
  update (`aws_lambda_function.mdpf_gold`), 0 add, 0 destroy, or the apply does not run.
- **The next scheduled fire (2026-09-22 13:30Z)** may write `opal-data-assets/portal/gold/mdpf/{49financial,inflection,cottonwood,global}/**`
  and, via the publisher, `opal-data-portal-v2/platinum/mdpf/{scope}/**`. **Branch 1:** cottonwood advances to the
  2026-09-18 frontier; **GLOBAL by_model goes 10 -> 9 keys** (`opal_fixed_income` line dropped) -- a SERVED-SHAPE change,
  Andrew's call 2. **Branch 2:** an unknown name raises / identity gate exits -> today's state, no worse.
- **LEG B:** the four `opal-data-mdpf/code/scripts/**` keys in s.5; the EC2 runner picks them up on its next run. Its
  Stage 6 fails today at import (`lib.opal_naming`, MDPF_TAXSMA) before any Cottonwood code, so the EC2 outcome is
  unchanged until that is fixed.
- **Rollback per key:** as the packet's s.3 and s.5 tables state, every bucket versioned; this seat re-measured the
  LEG A artifact version and all four LEG B VersionIds.

## OUTSIDE THIS SIGNATURE (named so nobody reads it as covered)

1. `opal-data-inf/code/gold/lib/tests/test_nna_coverage_guard.py` -- another seat's file riding the same push.
2. The import-closure gate's blind spot (packet s.2 item 1): its PASS proves nothing for guarded imports. Routed to
   `1.0.0_SA_CTO` by the packet.
3. The EC2 runner's Stage 6 `ModuleNotFoundError: lib.opal_naming` from MDPF_TAXSMA's 08:55Z deploy -- that project's
   defect, surfaced here, not fixed.
4. Acceptance. The 09-22 13:30Z scheduled fire is the acceptance; never an ad-hoc invoke.
