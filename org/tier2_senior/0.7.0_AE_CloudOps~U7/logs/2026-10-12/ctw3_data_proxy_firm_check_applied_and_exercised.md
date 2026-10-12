# opal-portal-data-proxy firm check applied; the unadmitted-firm arm could not be exercised — 0.7.0_AE_CloudOps~U7

**archetype:** DEPLOY
**Date:** 2026-10-12
**Task Order:** NFRA_CTLPLN.TO-CT-w-3.data-proxy-firm-check-apply-and-exercise
**Status:** COMPLETE for every required read (proof instance VALID); one arm NOT-EXERCISED by construction; the status flip is the issuer's

---

## Objective

Put the FWD-28 firm check live on the two open routes of `opal-portal-data-proxy` (second signed pair), after proving from the function's own logs that no non-internal request to them would be refused. Written for a reader with no prior context.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-iam | service opal-portal-data-proxy | PARTIAL | 35 calls, 18 GRANTED, 17 UNRESOLVABLE-RESOURCE; a floor, unchanged |
| deploy_ledger.py | open, 6 close-leg, close | PASS | entry nfra-ctlpln-ctw3-data-proxy-firm-check-20261012 CLOSED |
| safe-apply.sh | one apply of the saved plan | PASS | 0 added, 1 changed, 0 destroyed |
| proof-of-spec-check.py | instance + CTw3-AC1,2,3 | PASS | VALID rc=0 |
| surprise-row-gate | two rows appended | SKIPPED | runs at commit |

**What worked:** reading the whole 14-day log group (212 KB), so the pre-apply table has no sampling; reading the zip's member list from three places (built, uploaded, deployed).
**What failed:** my first PRE script printed requests=0 (HTTP API v2 events carry the method under `requestContext.http.method`); I treated the zero as a broken instrument, fixed it and reran. `record-terraform-deploy.sh` needs a `/c/` path, not `/cygdrive/c/`.
**Gap found:** the handler logs every caller's bearer token (row NFRA_CTLPLN-S9110); `_report()` in the exercise tool hardcodes GET, so the POST read printed a wrong verb (corrected in the exercise file).

---

## Work Completed

1. Read the order and both halves whole; verified the pin `50c8feb76b` and its three member hashes.
2. PRE: 47 handler Event lines, 16 on the two routes (14 POST and 1 GET by internal staff, 1 GET by my own CT-u-7 synthetic partner), 0 named exceptions, `not_admitted=0`.
3. P0: deployed members equal the CT-u-7 pin, no third member.
4. Built from a detached pin worktree; zip has exactly 3 members, each equal to the pin; uploaded as `iuIjViflW5mz8ggUo9w.jxijqwIEKE8p`.
5. Plan Branch A; one `safe-apply` at 09:53:54Z; live CodeSha256 `aWwkzuxR...`.
6. Reads: partner on `/aum/metrics` 200; partner on a class-(ii) route 403; internal on `/aum/metrics` 200 and on the keyword-intelligence POST 200. Unadmitted-firm arm NOT-EXERCISED: 0 of 57 profile rows belong to any other firm.
7. Cleanup: walker disarmed (post-disarm login refused); synthetic row deleted 1 s after its token's exp, ABSENT with a control.
8. Recorded `7a5e0083e3` (already on origin via the integrator), tag `market-overview-v1.11.6` LOCAL.

## Decisions Made

- Option (a) for the partner caller, as in CT-u-7 (the walker tool takes no second account id).
- Did not mint an unadmitted-firm credential: the order says mint nothing.
- Wrote both `PRE-APPLY` forms because the criterion text and the order's line format differ.

## Files Modified

`infra/aws/lambda/ci/lambda-source-map.json` (one entry), `infra/aws/terraform/market-overview/CHANGELOG.json`, the surprise channel (two rows), this seat's deliverables and logs, the ledger entry and its sentinel.

## Blockers

None. Said plainly: no live read discriminates the new check from the old rule (the admitted-firm read was 200 before as well); the package diff and the issuer's 965 tests are what show it runs.

## Current State

Firm check live and verified to the extent above; ledger closed; no standing credential.

## Next Steps

1. `[2.0.0_SA_COO~C]` Read the proof instance; decide whether the unadmitted-firm arm needs a minted synthetic caller (that needs a CTO word, the order says mint nothing); disposition `NFRA_CTLPLN-S9110` and `-S2`.
2. `[1.0.0_SA_CTO]` Rule the class of `NFRA_CTLPLN-S9110` (bearer tokens in the function's log group).
3. `[0.0.0_AB_MSTR]` Carry tag `market-overview-v1.11.6`.
