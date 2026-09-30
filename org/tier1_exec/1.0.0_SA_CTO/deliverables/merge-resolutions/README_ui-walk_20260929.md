# CLOUD merge -- `.claude/skills/ui-walk/walk.mjs` -- resolution ruled by `1.0.0_SA_CTO~Z` (DSGN_AMGTV1 owner), 2026-09-29 ~21:0xZ

**For:** `0.0.0_AB_MSTR~Z`'s CLOUD push under Andrew's call 1
(`deliverables/ANDREW_DIRECT_20260929_204xZ_OPEN_CALLS_ALL_FINE_SEEKING_ALPHA_RENEWS.md`). That push is held on 5
merge-tree conflicts (MSTR~Z msg 20260929T205253Z). This file settles ONE of the 5. The other four are
`4.0.0_SA_CRO/RECON_REGISTER.md` and three `2.0.0_SA_COO~D/drive_log_20260929T{10,11,19}Z.md`; they are not this seat's.

**Inputs:** merge-base `5b69865bc7`; ours = site-Z `CLOUD` @`7668249a78`; theirs = `origin/CLOUD` @`0c955d5493` (fetched ~21:0xZ).

## RULING: KEEP BOTH SIDES. The additions are independent.

| side | what it adds | why it must stay |
|---|---|---|
| ours (site Z) | `login: true` / `--no-login`, the sign-in WALK VOID guard (`signin_detect.mjs`), `securities` / `--security`, `walkSecurityAnalysis` (DSGN_AMGTV1 AV-w-1, `e051ec096d` / drain `2a9ad75324`) | CVO~Z graded it on its own signed-out control (`ADJUDICATION_v6`, row `Z-S3` GRADUATED). Dropping it re-opens a walk that reports 0 findings on a sign-in page. |
| theirs (laptop CRO) | `--settle-extra-ms` / `settleExtraMs`, `--periods-per-account` / `periodsPerAccount()` (`15fb2b1e6a`, `976f671613`, `8bec660380`) | Independent instrument options, off by default. |

Hunk by hunk:
1. The `opt` literal becomes the union of both field sets.
2. The argv branches: both sides' `else if` lines are kept.
3. Two separate functions sit at the same insertion point. `walkSecurityAnalysis` comes first and is closed by its own
   braces, then `periodsPerAccount`, which the shared trailing braces close.

## Checks on `ui-walk.walk.mjs.RESOLVED.txt` (sha256 prefix `0ac82699e7902a70`)

- 0 conflict markers; `node --check` passes.
- Token preservation, counted as (ours / theirs / resolved):
  - `securities` 3 / 0 / 3
  - `login` 15 / 9 / 15
  - `settleExtraMs` 0 / 4 / 4
  - `periodsPerAccount` 0 / 4 / 4
  - `walkSecurityAnalysis` 2 / 0 / 2
  - `signin` 1 / 0 / 1
- **Not run:** a live walk on the merged file. The first DSGN_AMGTV1 round-5 walk starts with the signed-out control, so it
  exercises the guard on the merged tree.

**Use:** during the CLOUD merge, `cp` this file over `.claude/skills/ui-walk/walk.mjs` and stage it.
