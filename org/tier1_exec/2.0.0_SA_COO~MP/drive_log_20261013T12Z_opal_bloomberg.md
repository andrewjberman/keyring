# Drive log -- 2.0.0_SA_COO~MP -- 2026-10-13 09:0xZ to 12:1xZ (re-seat; NFRA_MCPORTAL, lease FULL)

**archetype:** COORDINATE

| tick | limb | act fired | evidence |
|---|---|---|---|
| 1 (~10:2xZ) | L6 GW round 1 | ONE issuance: FWD-20 (the gateway breakdown, Andrew's first MCPORTAL outcome) plus the deep-link cell (row Z-S41). 6 orders over decomposition v7; 3 workers spawned; z-4 GO to the applier | issue @37192ad0fc, merged @233e78932a; 10 checks dry-run FAIL at base as expected; SSM f25b53c5 confirmed /control-plane, /open-calls, /gateway = 404 live |
| 2 (~12:1xZ) | L7 drain | 3 of 3 build cells drained; two amendments to MP-z-3; the applier cells re-cut to a fresh lane | z-2 @bcddb3e6b0 (mcportal 6fbd25e pinned `nfra-mcportal-gw-z2`); z-1 @fda2ca67a3; z-3 @7218b1e3ae; co-run 70/70 |

## Decisions closed

1. **MP-z-3 AMENDMENT 1 (@d82d936b38).** The worker's GET-only catch-all made `POST /mcp` a 405. The live code redirects
   it 307 to `/mcp/`, and every client is registered at `https://mcp.opalinvest.dev/mcp`. As built, it would have broken
   every MCP client. The criterion I cut bounded GET only, so the defect was the issuer's. Fixed; re-resolved by the issuer.
2. **MP-z-3 AMENDMENT 2 (@9229e8be3c).** The test file's teardown popped `app.*` modules and broke every suite that ran
   after it: 7 failed with the file first, 0 with it last. The release's step 1 runs that order, so this would have
   stopped the release. Fixed in the test file only.
3. **Row Z-W13-S1, ruled in the drain commit.** GW.3 named the email rosters as tier holders; `tier.resolve_tier` reads
   the PRINCIPAL rosters. The worker added those as candidates and stated the basis. Accepted.
4. **MP-z-4 and MP-z-5 re-addressed to `0.7.0_AE_CloudOps~MQ` (@f67671f35c).** `~MP` reads HUNG (MSTR msg 33605); my GO
   msg 33596 is OFFER-EXHAUSTED. `~MP` cannot be killed: it guards the C17 rollback trees. A fresh lane was spawned and
   registered after about 70 s; the GO was delivered at 12:09Z.
5. **C17 round 2.** E1 waits on `4.0.0_SA_CRO~Z`'s written consent (asked 09:36Z). E2 is held so both ride one issuance.

## Waiting on

- `0.7.0_AE_CloudOps~MQ`: the z-4 ASK. Then I sign the COO half and `1.0.0_SA_CTO~Z` signs the CTO half.
- G-REL3 (z-5): z-4 applied, plus the pair on the release ASK, plus the gateway queue free.
- `4.0.0_SA_CRO~Z`: E1 consent.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| comp-iam role / stats | 222 roles; opal-gateway-role has no Scan on the access-state table | preflight line for z-4 |
| to-pipeline-gate (via safe-commit) | refused 4 times, then PASS | 3 sparse-cone gaps (org/projects, org/devices, org/standards); 1 real: comp-iam needed RUN with a denominator |
| proof-of-spec-check | VALID x3 | one INVALID read from the wrong tree (main), VALID in the worker's own tree |
| safe-merge | 5 merges; 1 row-gate refusal | my union of two appended JSON blocks left one malformed; re-resolved as whole blocks on the branch |

**Gap found:** a criterion that names an HTTP route's behaviour must name its METHODS. A GET-only fixture is silent on
every other method, and Starlette turns a GET-only match into a 405 for all of them.
