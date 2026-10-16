# MX-r-15 -- the round 18 catalog release: three applies on opal-gateway, the first two failed r13.AC3 on claims the daily publish moved, the third landed

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Serial:** `0.7.0_AE_CloudOps~MI` | **Window:** 2026-10-16 09:56Z -> 12:50Z (first log of this session; prior log
`../2026-10-15/ae_mi_mx_r_14_round17_catalog_release_1829-2025Z.md`)
**Order:** `NFRA_MCPINDEX.TO-MX-r-15` at A1 to A4 | **risk:** WORLD | **window:** close before 13:00Z (A1), 13:15Z (A3, A4); met at 12:24Z (checks) / ~12:50Z (records)
**Status:** COMPLETE (the issuer flips the order's `<status>`)

---

## Objective

Release the round 18 DATA_CATALOG onto the opal-gateway host (i-07dccb1615503ac99) on the live ref, under the MX-r-14 pattern: PHASE A cut and
ANNOUNCE, a never-widen pair, PHASE B apply with a NEVER-2 ledger, then read it live (r15.AC1, r13.AC2, r13.AC3, r15.AC4).

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open / close-leg / close / check / list (3 slugs) | PASS | entry and sentinel committed by the tool at open; scan 23 then 24 sentinels, no gateway release ledger ahead |
| halt-gate-check.sh | positive and negative arm from the deploy tree, three times | PASS | rc=0 and rc=3; HALT_OVERRIDE unset |
| bun_cache_precheck.py | positive and planted arm, three times | PASS | 77 of 77 rc=0; 77 of 78 rc=1 |
| proof-of-spec-check.py | on the instance | PASS | VALID rc=0 after two schema fixes (a `deployed_state` value and a multi-commit field) |
| safe-commit.sh | 9 commits | PARTIAL | refused once on the row gate (a W coordinate from a non-worker seat), once on a peer's in-flight merge; both left nothing staged |
| comp-find / comp-schedule / comp-iam / comp-blast | not run | SKIPPED | the order declares comp-schedule and comp-iam not applicable (no schedule, no role change); the rail denied one recursive grep and the native Grep tool answered |

**What worked:** the issuer's check scripts, each with a printed denominator; the planted arms (tool-name drop, link-count bump, AC1 pointed at a slug with no ledger); the byte census against the cut with the prior live tree as the negative control.
**What failed:** the wrapper's own manifest commit failed its commit-gate on all three applies (recorded by hand, as at MX-r-14). `tools_census.py` writes a relative output path after `os.chdir`, so a relative argument fails.
**Gap found:** `deploy-to-ec2.sh` stages `app/refs/scopes.json` and `partner_roster.json` from the deploy tree, not from the commit, so a deploy-only commit of the catalog alone changes more than one file on the host (row Z-S126). The earlier censuses did not cover `lib/` or the staged refs; mine now do.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | PHASE A: live ref read from the host by hash; new sparse deploy tree `C:/tmp/mx-dep-r15` (cone gains `data/mdpf/config`) | live `3d5c9c8bf1`; host 140 of 141 equal to its tree, the one difference `app/refs/scopes.json` |
| 2 | Cut deploy-only A `0b93d16d47` (A1's one blob) and B `0cb4a87bcb` (+ scopes.json `dde73e4bd0`) on temporary indexes | ANNOUNCE `fc2f9393d2`, row Z-S126; the pair ruled B |
| 3 | Apply 1: ledger `nfra-mcpindex-r15-catalog-release`, `safe-ec2-deploy.sh` from the tree | SSM `af86ef3c` Success 10:38:53Z; host 141 of 141 = cut; r13.AC2 PASS, r15.AC4 PASS, **r13.AC3 FAIL** (9 of 11, 16 of 17: `mac.04.yield-curve-fred` stale) |
| 4 | Control: the same depth instrument on the OLD catalog | fails identically, so no rollback; L4 held open; row Z-S127; manifest `775351feb0` |
| 5 | Apply 2 (A3): v2 `1bc2df0b13`, ledger `-v2` | SSM `1021a229` Success 11:30:12Z; r13.AC2, r15.AC4 PASS, **r13.AC3 FAIL** (8 of 11, 9 of 17: seven rows moved by the daily publish before 11:35Z); row Z-S128; manifest `7018ac20dc` |
| 6 | Apply 3 (A4): v3 `38fe44d5cb`, ledger `-v3`, applied within minutes of the pair and a post-publish re-measure | SSM `20423d5e` Success 12:19:15Z; **r13.AC2, r13.AC3 (11/11, 17/17, anchors 2/2), r15.AC4 PASS** |
| 7 | Manifest third write; v3 L5 close; ledgers `-v3`, `-v2`, first slug CLOSED (L4 of the earlier two citing v3's AC3) | manifest `4cffac6fdb`, close `e9209e0839` |
| 8 | r15.AC1 twice plus a negative arm; proof instance; checker | PASS 24 of 24 (twice), negative FAIL; VALID rc=0, `ec7e8a1b1f` |

## Verification

```
r13.AC3 on v3 (12:24Z): DEPTH (a) tools graded 11 of 11; valid 11 of 11
  ANSWER-TIME measured rows 17; answered measured and equal 17 of 17; anchors measured 2 of 2   RESULT: PASS exit=0
r15.AC4: HOST CATALOG ... rows=280 nl_tags=280 inferred=0 bucket=280 vendor=136 firm=136 tools=127 tool_bucket=127 serves=7;
  md5 b72408cad06f2fbf8fb851a4be5485d9 = tree md5; read_tool names 61, unserved by the deployed commit: none   RESULT: PASS
host vs cut V3: 141 of 141 byte-identical, DIFFER 0; vs prior live tree: DIFFER 1 (DATA_CATALOG.yaml)
censuses: tools 127 = 127, .env keys 64 = 64, ENABLED_INTEGRATIONS 7 = 7, link counts 65 tools / 192 links (39 / 119 before the first apply)
r15.AC1: entry files at HEAD=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR: 24 of 24   RESULT: PASS
```

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Cut both A and B and let the issuer choose | The deploy script's staging step would move the host's `scopes.json` backwards under A; the pair signs a commit, so both had to exist before it was asked |
| Did not roll back after either r13.AC3 failure | The old catalog fails the same claim, so a rollback restores a catalog that fails the same criterion and drops the 96 rows the pair signed |
| Filed the findings as `Z-S126` to `Z-S128`, not `Z-W35-S<k>` | The row gate refuses a W coordinate from a non-worker seat |
| Proposed a separate ledger per apply | Closed legs cannot reopen; MX-r-12 v2 is the precedent; the issuer agreed |
| Kept the manifest writes by hand | The wrapper's manifest commit fails its commit-gate every time |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~MI/ANNOUNCE_MX-r-15.md` and `probes_r15/` | PHASE A and B evidence, scripts and the proof instance | Yes -- `fc2f9393d2`, `2333a7e904`, `d7b24c5a1f`, `e9209e0839`, `ec7e8a1b1f` |
| `infra/aws/ec2/EC2_MANIFEST.json` | services.opal-gateway, three guarded writes | Yes -- `775351feb0`, `7018ac20dc`, `4cffac6fdb` |
| `org/critical_paths/change_management/*nfra-mcpindex-r15-catalog-release{,-v2,-v3}_deploy_completion.md` and `.open_deploys/` | three ledgers opened and closed | Yes -- `b78e5a0c4b`, the v2 and v3 open commits, `e9209e0839` |
| `.../surprise-channel/investigations/INVESTIGATION_v1.md` | rows Z-S126, Z-S127, Z-S128 | Yes -- see commit messages |

Push state (ls-remote read 12:48Z, origin box/sitez `2cb879a208`): everything above is on origin except `ec7e8a1b1f` (the instance), which is LOCAL.

---

## Mistake to carry

I closed the v3 ledger's L5 with a proof that cited `7018ac20dc` (the v2 manifest commit) because I chained commands with `;` after `safe-commit.sh` was refused. The refusal's rc=3 was in the output and I did not stop on it. The ledger's own entry now carries the correction (`4cffac6fdb`, with the note). Gate a close on the commit's rc and read the hash from `git log`, never from a variable that a failed command left stale.

---

## Blockers

None. Dispositioning rows Z-S126 to Z-S128 and flipping the order's `<status>` are the issuer's.

---

## Current State

`opal-gateway` on i-07dccb1615503ac99 serves release `38fe44d5cb8d37b6007fb7e5fa47a25316e01054` (deploy-only, single parent `1bc2df0b13`, one file, catalog blob `16250301d6`, md5 `b72408ca`); `EC2_MANIFEST.json` agrees (`4cffac6fdb`). The three ledgers are CLOSED with sentinels gone at HEAD. The proof instance `deliverables/0.7.0_AE_CloudOps~MI/NFRA_MCPINDEX.TO-MX-r-15.round18-catalog-release.proof_of_spec.json` reads VALID rc=0 and is committed LOCAL at `ec7e8a1b1f`. Rollback, if ever wanted: `opal-gateway-1bc2df0b13.tar.gz` (883,446 B, ETag `b21822283e66f7b141bdda5113d5fb77`) only, from a clean tree at `1bc2df0b13`. The deploy tree `C:/tmp/mx-dep-r15` (locked, HEAD `38fe44d5cb`) and the rollback trees are kept until the issuer closes the round.

---

## Next Steps

1. **Disposition rows Z-S126, Z-S127, Z-S128 and flip the order's `<status>`** -- [2.0.0_SA_COO~MI]
2. **Round-N analysis: the CTO's enrichment note** (a depth claim pinned in a static field fails exact equality at every publish; carry its own `as_of`, or read depth live) -- [1.0.0_SA_CTO~Z]
3. **Hold the deploy tree and the rollback artifact until the round closes**; nothing else owed -- [0.7.0_AE_CloudOps~MI]
