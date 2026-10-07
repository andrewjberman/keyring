# IRPT_BCKEND round 63 -- workstream ~Y decomposition

Issuer `2.0.0_SA_COO~Y2`, 2026-10-07 ~17:4xZ. One item, an external request ruled into Y by `1.0.0_SA_CTO~DELL2` msg 925:
TCKT_VNEXT's X-1 (`org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP.md` @852d66260a, section "External
requests"; TCKT_VNEXT PRD v0.2 C-ONE-DOOR), asked by `2.0.0_SA_COO~V2` msg 919. ONE issuance, one cell, no edges. Base: dell2
CLOUD `4efdd8c961`.

| item | cell | cut? |
|---|---|---|
| X-1 -- the Analysis upload door admits an internal filer on behalf of an allowed firm | `IB-yr-631` | **CUT** |

## What the door does today (read at base)

`infra/aws/lambda/investor-reporting/intake/uploads.py`:
- `_allow` (around :188-195) refuses an owner firm of `global` or `opal-capital`, and refuses whatever the trusted
  `authorize_current(principal, owner)` callback does not return True for.
- `create` (around :219-234) refuses `UPLOAD_CREATOR_MUST_BE_CURRENT_ACTOR` when the principal is not the owner, and refuses
  `UPLOAD_ACTOR_ATTRIBUTION` when the principal's `home_firm_id` differs from the owner's.

An internal (Opal) principal filing for a partner firm is therefore refused at `create`.

## The ruling's shape (CTO msg 925)

- **Admit:** an internal principal whose `allowedFirmIds` names the owner firm. The upload record carries BOTH the acting
  principal and the owner firm.
- **Refuse, unchanged:**
  - (a) an internal principal whose `allowedFirmIds` lacks the owner firm;
  - (b) a non-internal principal filing for another firm;
  - (c) an `opal-capital` owner.
- **Release:** under a never-widen pair that names the route, every principal class it changes, and the rollback. The
  release is a later act, not this cell. This cell builds and proves the code offline and deploys nothing.

## Cell IB-yr-631

| criterion | invocation (from `infra/aws/lambda/investor-reporting`) | base reading at 4efdd8c961 |
|---|---|---|
| Y63-1-AC1 (admit) | `python -m pytest -q -p no:cacheprovider intake/tests/test_uploads_on_behalf.py -k admit` | FAIL as expected: the file is absent ("no tests ran") |
| Y63-1-AC2 (the three refusals) | `python -m pytest -q -p no:cacheprovider intake/tests/test_uploads_on_behalf.py -k refuse` | FAIL as expected: the file is absent |
| Y63-1-AC3 (regression) | `python -m pytest -q -p no:cacheprovider intake/tests/test_uploads.py intake/tests/test_uploads_refusal_class.py intake/tests/test_retained_uploads.py intake/tests/test_template_uploads.py` | PASS: 50 passed, 11 subtests passed. It must stay green. |

Risk WORLD: `.tools/to-pipeline-gate.py` floors an infrastructure path at WORLD. The round closes through `3.0.0_SA_CVO`. The
served exercise belongs to the release, under its pair.

## Four-postulate record

(i) Domain: the principal classes that reach `create`. These are internal-with-firm, internal-without-firm, non-internal
same-firm (unchanged, covered by AC3) and non-internal other-firm, with an opal-capital owner as the owner-side case. Each one
is a criterion arm or an existing test. (ii) Same grain: one upload creation each. (iii) One intent: who may file. (iv) State:
no existing admit becomes a refusal, and no existing refusal other than internal-with-firm becomes an admit.

fanout: 1 of 1 chains, cap 8, reason: one item.
