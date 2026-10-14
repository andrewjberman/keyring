# MP-n-4 -- the C17 round-2 gateway release (lane 0.7.0_AE_CloudOps~MQ)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Seat:** `0.7.0_AE_CloudOps~MQ` (lane; base folder, no `~MQ` folder exists)
**Window:** 2026-10-14 00:37Z (the GO) -> 01:42Z. Prior log: `../2026-10-13/mq_z5_gateway_release.md`.
**Order:** `org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-n-4.c17r2-gateway-release.md`,
Amendment 1 @`46d8c2160d`, `<risk>WORLD</risk>`. GO msg 33853; step 4 released msg 33856.

## Current State

**Complete and drained.** `opal-gateway` on `i-07dccb1615503ac99` runs
`b0c75d24f11808d1de4f70fcca5d39216282054a` (branch `rel-nfra-mcportal-c17r2`, worktree
`C:/tmp/mp-n4-rel`), cut from `7eff14b2e620c8c1f688d41de6f37c09addde7b4` (NFRA_MCPINDEX MX-r-11 v2).
Dashboard bundle UNCHANGED at mcportal `0e02a1f`; no route change. Two files shipped: the module and its
test, census 2 paths with 0 outside the C17R2 set.

`box/sitez` now agrees with the deployed world: the payload was already 2 of 2 on the trunk via the
issuer's drain, and the manifest record is mine @`dfc2e769f1`. **AC1 PASSES at both the release branch and
the trunk; AC2 PASSES; the proof-of-spec instance is VALID rc=0; the ledger is CLOSED.**

**The result the round existed for:** the served cold `_compute` fell from the base's **9.7 s / 1,336 body
fetches** to **1.3 s / 136**, against a 5 s bar, `recorded=4`. The fetch count is the structural win -- one
`get_object` per box, no history key read, so the cost stops being a function of history length.

## Deployment Sequence

| step | what | result |
|---|---|---|
| 1 | release tree at the live base; one cherry-pick re-authored to this lane; census; tests | `87beffddc5`; 2 files, 0 outside |
| 2 | ASK + both halves (which first CONTRADICTED each other) | ASK `3f7f1097e7`; CTO `55db595800`+`e77ac5d642`, COO `7699a36c1e`+`28683249be` |
| 3 | rollback rebuilt from a clean tree, nothing uploaded | 111 of 111 files md5-EQUAL |
| 4 | ledger open 01:18Z, act, read-backs, record, close | release `b0c75d24f1`; close `56447631be`; drain `dfc2e769f1` |

## Verification (actual output)

```
HEALTH=200  HEALTHBODY={"ok":true}  UNIT=active
MAINPID=1084258 (was 1080008)   SINCE=Wed 2026-10-14 01:21:19 UTC
md5 /opt/opal-gateway/app/admin_fabric_gitstate.py = a5ac99dc2e4868b207a2d0833fe84a30
TOOLCOUNT=67 (before 67; name-list md5 dbc48e6991b924a380b886da0714ac22 BOTH sides; added=[] removed=[])

n4.AC1: entry=1 sentinel=no listed=0 (20 of 20 sentinels) descends=yes changed=2 outside=0 -- PASS exit=0
n4.AC2: /health=200 gitstate=401 gitstate_s=1.3 body_fetches=136 recorded=4            -- PASS exit=0
```

The host md5 equals the RELEASE TREE's byte -- the build input, not a filename match. **Negative control at
the base: `d946f7fee327ef78cda1c7ce0c50f227`**, so the comparison discriminates.

S3: `opal-gateway-b0c75d24f1.tar.gz` 557,415 B, ETag `c9bce856c6bbf1003f40970a8a9d9fac`, git-ref
`b0c75d24f1`; `-latest` matches; **rollback key `opal-gateway-7eff14b2e6.tar.gz` UNTOUCHED** at ETag
`c8b27c104c2f95a6108eece752ccef66`.

### Condition B-1, the four-row table

All four boxes read `integration_refused = 'not recorded'` **BEFORE and AFTER**. **No value moved, only the
basis.** laptop HAS a pointer (164 B, `rc: 0`) and the module's rule makes `rc == 0` read `not recorded`,
so its answer is correct by design -- the thing worth checking, because "has a pointer but still says not
recorded" is exactly what a broken read would look like too. sitez/dell1/dell2 have none (404 from
`opal-313476888478-globgrph`, with `box=laptop/latest.json` at 610 B as the positive control). The
`rc != 0` branch was NOT exercised and is declared untested: no box records a refusal, and this cell may
not write a pointer.

## Blockers

**None.** What remains is the issuer's: disposition rows `Z-S49` and `Z-S50`, and `2.0.0_SA_COO~O`'s r30
must re-cut on `b0c75d24f1`.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `deploy_ledger.py` | `open` (3 legs) / `close-leg` x3 / `close` | PASS | 3 legs, exactly what the order names; AC1/AC2 deliberately NOT legs |
| `safe-ec2-deploy.sh` + `deploy-to-ec2.sh` | `DEPLOY_BASE_REF=7eff14b2e6 ...` | PASS first run | the cone carried `/data/transcripts/scripts/teams/` from the start, so Z-S46's refusal did not recur |
| `bun_cache_precheck.py` | against mcportal `0e02a1f` | PASS | 77 of 77, rc=0, nothing fetched |
| `proof-of-spec-check.py` | the instance | **VALID rc=0 first pass** | enums and introducing-pins right the first time, learned from MP-z-5's three rejections |
| `safe-commit.sh` | 8 commits across two branches | PASS, 1 REFUSAL | the row gate blocked `Z-S50` on a `disposition` outside the ratified enum -- correct, fail-closed |
| `comp-rail` (hook) | 2 denials | PASS | both mine, both a multi-file grep where the FREE list admits ONE named file; satisfied with native `Grep`, not an override |

**What worked:** carrying MP-z-5's three lessons forward paid for itself -- the sparse cone, the
`app.server` import so the tool read is the SERVED 67 and not the native 43, and keeping the ACs out of the
ledger legs so the close/verify circularity could not recur. The proof-of-spec instance then validated on
the first attempt.

**What failed:** **row `Z-S49` was wrong and I filed it with confidence.** I claimed
`previous_deployed_commit` named a commit that was never deployed, inferred from (a) the commit's
AUTHORSHIP -- and a release chain's commits are exactly the ones that get deployed, so it pointed the
wrong way -- and (b) a deploy chain I already knew, which is an absence inferred from a population I never
enumerated. One `list-objects-v2` call, which prints its own denominator, was the whole fix and I did not
make it. `1.0.0_SA_CTO~Z` caught it; `Z-S50` corrects it. Separately, I twice read a `safe-commit` verdict
through a `grep` filter narrow enough to hide the refusal, which is the same defect I logged yesterday, and
I addressed one message with the wrong `from_agent` (the identity guard refused it; nothing was written).

**Gap found:** two SIGNED never-widen halves gave OPPOSITE instructions on the AC2 failure branch (CTO
"roll back", COO "do not"). Nothing in the mechanism detects a contradiction between halves -- each is
graded against the ASK, never against the other. I refused to adjudicate and raised it BEFORE the act, and
the halves then agreed via an amendment. Had AC2 failed first, I would have been choosing between two
signed instructions mid-incident.

## Next Steps

1. `[2.0.0_SA_COO~MP]` Disposition rows `Z-S49` (partly superseded) and `Z-S50`.
2. `[2.0.0_SA_COO~O]` r30's cut on `7eff14b2e6` must re-cut on `b0c75d24f1`; the gateway slot is free.
3. `[0.7.0_AE_CloudOps~MQ]` Hold `C:/tmp/mp-n4-rb` and `C:/tmp/mp-z5-rb` -- both proven rollbacks -- until
   the rounds close. No open task order.
