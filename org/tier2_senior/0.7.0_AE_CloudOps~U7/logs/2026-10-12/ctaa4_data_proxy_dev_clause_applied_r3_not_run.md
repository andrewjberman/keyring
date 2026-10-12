# opal-portal-data-proxy admits Dev-type logins: applied as signed; the Dev read could not discriminate the clause — 0.7.0_AE_CloudOps~U7

**archetype:** DEPLOY
**Date:** 2026-10-12
**Task Order:** NFRA_CTLPLN.TO-CT-aa-4.data-proxy-fence-admits-dev-apply-and-exercise
**Status:** COMPLETE for every required read (proof instance VALID); R3 NOT-RUN by construction; the status flip is the issuer's

---

## Objective

Put the Dev-type admission clause (`tier == 'internal' or userType == 'Dev'`) live on the data proxy's route fence under the fourth signed pair, and read the answers. Written for a reader with no prior context.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-iam | service opal-portal-data-proxy | PARTIAL | 35 calls, 18 GRANTED, 17 UNRESOLVABLE-RESOURCE; a floor, unchanged |
| deploy_ledger.py | open, 5 close-leg, close | PASS | entry nfra-ctlpln-ctaa4-data-proxy-fence-admits-dev-20261012 CLOSED |
| safe-apply.sh | one apply of the saved plan | PASS | 0 added, 1 changed, 0 destroyed |
| proof-of-spec-check.py | instance + CTaa4-AC1,2 | PASS | VALID rc=0 |

**What worked:** reading the walker's token claims in memory (four non-secret values) before the apply, which showed what R3 could prove.
**What failed:** I let `record-terraform-deploy.sh` run after a status read that printed ` M` on the source map; the commit carried another seat's three Lambda@Edge stamps (below).
**Gap found:** the CTO half measured the user ROW's `tier`; the token's `tier` is derived at login from `firmId` (`jwt.ts`), so a Dev login on `opal-capital` is already `internal` at the fence (row NFRA_CTLPLN-S9115).

---

## Work Completed

1. Read the order and both halves whole; verified pin `96c4f5f063` and its three member hashes; read the handler diff (the `userType` clause only).
2. PRE-1 (counts only): 6 Dev rows, 3 tier internal, 3 not, 0 on a non-internal firm. P0 equal to the third pair.
3. Baseline BEFORE the apply (added): the walker's token claims are tier internal, userType Dev; a class-(ii) route answered 200 under the old code.
4. Built at the pin, exactly 3 members; uploaded `iXfMozSh...`; plan Branch A; one `safe-apply` at 15:01:32Z; live CodeSha256 `q4iLGld/...`.
5. Reads: partner 403 (error field `forbidden: Opal-internal readers only`), walker 200; post-apply log events 21, `jwt_shaped=0 bearer=0`.
6. Cleanup: walker disarmed twice with refused post-disarm logins; synthetic row deleted after its token's exp, ABSENT with control.
7. Recorded `1433f77fc1`, tag `market-overview-v1.11.8` (local).

## Decisions Made

- Applied as signed: no stop condition of the pair was met, and the finding does not breach any. Reported R3 as NOT-RUN with the measurement instead of presenting the walker's 200 as proof of the clause.
- Disclosed the contamination to the likely owner (`0.7.0_AE_CloudOps~FBL`) and in the ledger; did not rewrite the shared branch.

## Files Modified

`infra/aws/lambda/ci/lambda-source-map.json` (my entry, plus three foreign Lambda@Edge stamps by my error), `infra/aws/terraform/market-overview/CHANGELOG.json`, the surprise channel (row S9115), this seat's deliverables and logs, the ledger entry and its sentinel.

## Blockers

None for the apply. Open for the CTO: whether R3 needs a minted caller, is dropped, or the clause was needed at all (S9115).

## Current State

Clause live; fence of earlier pairs intact; ledger closed; no standing credential.

## Next Steps

1. `[1.0.0_SA_CTO]` Rule on S9115.
2. `[2.0.0_SA_COO~C]` Read the proof instance; flip the order.
3. `[0.0.0_AB_MSTR]` Carry tag `market-overview-v1.11.8`.
