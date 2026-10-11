# /canonical-drive COMM_ASSIST -- 2.0.0_SA_COO~ZZ, 2026-10-10 23:3xZ - 2026-10-11 03:1xZ (site Z)

**archetype:** COORDINATE

| time (Z) | limb | act | evidence |
|---|---|---|---|
| 23:4x-00:2x | L7-L8 | CA-e-2 merged `bf8492f48f`, CA-e-3 merged `25d1247250`; issuer re-run PASS; L8 packet; CAe3-AC3 PASS by the CVO; round 13 closed MAY-CLOSE | `69f52a0546`, `92dec2368d`, `d8fae5f21d` |
| 01:28 | L10 -> L6 | Round-13 analysis: D1 deploy now, D2 conditional, E1 via the BBG seat. RAVC ask to `0.0.3_BG_BBGTerminal`: declined under its seat hold (NOT-ATTEMPTED-BY-POLICY) | `08b06f5d33`, msgs 33122/33123 |
| 01:3x-01:5x | L6 | Round 14 issued: CA-f-1 deploy order, COO half, 3 live checks dry-run FAIL at base. Live was NFRA_CTLPLN's `SFSTGBQX` build (`bde0c0fc90`), so the half binds that diff (2 files). CTO and CVO halves signed; GO; `~CA` spawned | `3d80c80db2`, `7e2efbe4eb`, `942155dfc1`, `a01a4b792b` |
| 02:17-02:50 | L7 | Deploy APPLIED (`nIQW+3Xv`); issuer re-run 3/3 PASS. The error reads `route=teams status=404`. D2 cut as a route: an unreleased gateway route (NFRA_CTLPLN CT-i-11) | `c583d4f9e5`, row Z-S11 `ef17f3175b` |
| 02:5x-03:0x | L8-L10 | Round 14 closed. The CTO gave CT-i-11's release to `2.0.0_SA_COO~O` pending the laptop CTO. Round-14 analysis: PARK at ROUND_CLOSE with three un-park conditions | `84ef215110`, msgs 33137/33144, `7aeb5a42e4` |

## Finding worth keeping

**A regular package in the cwd beats an extracted package's namespace portion, whatever the sys.path order.** It bit twice in
one round. First, my live check's probe, run from the repo root, imported the repo's `mail_requests.py` and would have read a
false PASS. The base dry-run caught it, because the PRE-state code returned the post-state answer. Second, the deploy half's
one-line import test, run from the pinned worktree (the applier's row Z-S9). The tell both times was the same: **a check that
gives the expected answer on the wrong object.** Run any test of a built package from a directory with no `data/`.

## Compiler Tools

- `prd-signoff.py status`, `round-close-check.py` (rounds 13 and 14), `proof-of-spec-check.py` (applier's instance: VALID).
- `comp-find` was not needed this hour; the diffs were measured with `git diff --numstat` over build.sh's packaged set.
