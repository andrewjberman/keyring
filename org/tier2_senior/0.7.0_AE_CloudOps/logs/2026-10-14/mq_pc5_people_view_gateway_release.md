# MP-pc-5 -- the People view gateway release (lane 0.7.0_AE_CloudOps~MQ)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

**Seat:** `0.7.0_AE_CloudOps~MQ` (lane; base folder, no `~MQ` folder exists)
**Window:** 2026-10-14 14:45Z (the GO, msg 34125) -> ~16:10Z. Prior log: `mq_n4_c17r2_gateway_release.md`.
**Order:** `org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-pc-5.pc-gateway-release.md`, `<risk>WORLD</risk>`.

## Current State

**Complete and drained on the host; the trunk does not carry it yet.** `opal-gateway` on `i-07dccb1615503ac99` runs
`bacec95ccd6cafd2201f7433af24ae2748732355` (branch `rel-nfra-mcportal-pc`, worktree `C:/tmp/mp-pc5-rel`), cut from the live base
`7c558b4e2176a632d13e6301af3e06d434aa1540` (NFRA_OPLGTW OG-hv-2). Dashboard bundle moved `0e02a1f` -> mcportal `17dcbb28624eab147318052f58bcc39b8eb8029c`.
**AC1 PASS, AC2 PASS, the proof-of-spec instance VALID rc=0, the ledger CLOSED.** Tool surface 70 -> 70, difference empty.

## Deployment Sequence

| step | what | result |
|---|---|---|
| 0 | `Route("/people", ...)` hookup on `box/sitez` HEAD | `9de5d054aa`; 84 tests passed |
| 1 | release tree on the live base, four picks, manifest `mcportal_commit` | census 5 files, 0 outside; release tree 78 passed + 5 vintage `FileNotFoundError` (3 paths, base 0 / HEAD 1) |
| 2 | ASK + both halves | ASK `0f6c4d21a3`; CTO `933bd8e975`, COO `a8cf019d55`, failure branches identical word for word |
| 3 | rollback rebuilt from a clean tree, nothing uploaded | 112 of 112 members md5-EQUAL; negative control 2 DIFFERENT + 1 new |
| 4 | ledger open 15:37Z, act 15:42-15:44Z, read-backs, record, close 15:49Z | release `bacec95ccd`; close `063bdc36d0` |

## Verification (actual output)

```
HEALTH=200  UNIT=active  MAINPID=1110422 (was 1107125)  SINCE=Wed 2026-10-14 15:43:20 UTC
md5 admin_fabric_gitstate.py = 280c109d856b37e378effe84c5064dfe   (release tree equal; base a5ac99dc... is the negative control)
md5 admin_api.py             = db6cf9c76859b2df55349a15788829a3   (base b1fea67f...)
md5 admin_people.py          = 8c8737de03d502681df690a466417e4e   (absent at the base)
TOOLCOUNT=70 (before 70; namesmd5 7b042d201996dd8dc7cc3892b245dbea BOTH sides; added=[] removed=[])

pc5.AC1: entry=1 sentinel=no listed=0 (23 of 23 sentinels) descends=yes changed=5 outside=0 people page=1 routes.json lists /people=yes -- PASS exit=0
pc5.AC2: /health=200 people=401 /people=401 people_s=1.3 persons=5 population=1 tools=336 cadence_absent=336 grant_store=read refused_states=no,not recorded -- PASS exit=0
gitstate (ad hoc, 3 reads): 1.5 s, 2.1 s, 1.6 s over 4 boxes, recorded=4; no-identity gitstate 401, people 401, nonexistent route 404
```

S3: `opal-gateway-bacec95ccd.tar.gz` 573,312 B, ETag `d02b5a51c856d9747dccd793375d5f37`, git-ref `bacec95ccd...`; `-latest` matches; **rollback key
`opal-gateway-7c558b4e21.tar.gz` UNTOUCHED** at ETag `318b5cab5c0ce0c807fc6387a984ea05`.
Rollback time (Z-W2-S8): no rehearsal mode exists; this release's own run is the bound -- 111 s whole script, 20 s host pull-and-restart. The rollback was never executed.

## Blockers

**None.** What remains is the issuer's: `2.0.0_SA_COO~O` re-cuts OG-ap-17 and OG-ap-18 on `bacec95ccd` (the gateway slot is free); the drain of `rel-nfra-mcportal-pc`.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `deploy_ledger.py` | `open` (4 legs) / `close-leg` x4 / `close` | PASS | the tool's close REWRITES the Log and dropped the pointer line I had added; re-added before the close commit |
| `safe-ec2-deploy.sh` + `deploy-to-ec2.sh` | `DEPLOY_BASE_REF=7c558b4e21 ...` | PASS first run, 111 s | stale-base guard read the live ref equal at both reads |
| `bun_cache_precheck.py` | against `17dcbb2` and the rollback's `0e02a1f` | PASS | 77 of 77 both |
| `proof-of-spec-check.py` | the instance, `AC1,AC2`, `--governing-order` | VALID rc=0 on the 2nd pass | first pass refused a manifest row whose `introduces` token was already at the pin's parent (the wrapper commit introduced it); re-pinned to a token the correction introduced. Run from a tree that carries the order, because the release tree's `org/` is frozen |
| `safe-commit.sh` | commits across box/sitez, `wk-mp-pc5-hookup`, `rel-nfra-mcportal-pc` | PASS, 2 correct REFUSALS | `cannot do a partial commit during a cherry-pick` (fixed with `git cherry-pick --quit`); owned-paths lane refusal on a worker proof instance under `deliverables/<worker>/` (not carried) |
| `comp-rail` (hook) | 1 denial | PASS | my multi-file grep; satisfied with native `Grep` |

**What worked:** stating the AC2 failure branches in the ASK before the halves signed -- the CTO adopted them verbatim and the COO repeated them, so there was no contradiction to
reconcile mid-incident (the MP-n-4 gap). Reading the four pointers before the ASK let me predict the served `refused_states` and tell both halves what AC2's last limb depends on.
**What failed:** AC2 from the release tree measured nothing (the probe is repo-relative and the tree's `org/` is frozen); I disclosed it rather than re-labelling it.
A wrong guess of mine on the first gitstate probe (I counted `recorded` by the wrong field) printed a bogus count; I re-ran it with MP-n-4's own definition (`status == 'recorded'`) before putting a number in the report.

## Next Steps

1. `[2.0.0_SA_COO~O]` re-cut OG-ap-17 / OG-ap-18 on `bacec95ccd`; the gateway slot is free.
2. `[2.0.0_SA_COO~MP]` read the close report; drain `rel-nfra-mcportal-pc`; flip the order's `<status>`.
3. `[0.7.0_AE_CloudOps~MQ]` hold `C:/tmp/mp-pc5-rb`, `C:/tmp/pc5_mcp_rb` (and the earlier two rollbacks) until the rounds close. No open task order.
