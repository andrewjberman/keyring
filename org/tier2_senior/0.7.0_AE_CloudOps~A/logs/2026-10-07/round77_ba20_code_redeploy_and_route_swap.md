# AMGT_RESAPP round 77 AMGT-ba-20 -- the code redeploy carrying every build cell, plus one route swap

**archetype:** DEPLOY

`0.7.0_AE_CloudOps~A`, 2026-10-07 ~04:1x-05:2xZ, site Z, branch `CLOUD`.

## What was asked

`AMGT_RESAPP.TO-AMGT-ba-20.the-code-redeploy.md`, issued by `2.0.0_SA_COO~Z`, GO msg 30546 at
04:05:23Z. Risk WORLD, proof genre DEPLOY, worker-class order run by this AE lane. Two legs under ONE
NEVER-2 entry and ONE never-widen pair (COO @b0bb011946, CTO @90de9b291b): build the
`opal-amgt-scoped-api` artifact at EXACTLY `14a36147bd` and move it plus ONE gateway route swap through
a single `safe-apply`; then fire ONE snapshot event.

## Current State

**The deploy is LANDED and every criterion reads YES.**

- `opal-amgt-scoped-api` CodeSha256 `MkM9Kf37nmI+thEmZR+ij8ybbxGrHxqtsonjyI7N5eg=` (base
  `OVpDhfwDG3BzKE++wDxMlFA6JrwpTnH3FiHC+NrzsrE=`), MemorySize 1769 unchanged, CodeSize 41,981,131,
  LastModified 2026-10-07T04:40:17Z. Untargeted re-plan reads `No changes.`
- Live gateway `7k3ed8px20`: 19 scoped-amgt routes, **18 non-greedy** as the pair fixes.
  `POST /api/scoped/amgt/refresh` absent, `GET /api/scoped/amgt/resolve` present.
- `/freshness` snapshot rewritten by the new code: generated_at 2026-10-07T04:51Z, **rows 302 EQUAL**
  to the base's 302 (CTO condition 6), VersionId `USWeSyyD402yOpMpAHWZLz_ld1si4dms`.
- AC1 `R77 DEPLOYED: YES 3 of 3`; AC2 c62/c63/c59 YES; AC3 seven cells YES. All exit=0.
- NEVER-2 entry `amgt-resapp-r77-ba20` opened before the apply, four legs closed, entry CLOSED.
  `proof-of-spec-check` reads VALID on the committed bytes.

**Commits:** `759490bf74` (the open) and `0fabcf4f0f` (the close). Both **LOCAL** -- origin `CLOUD`
reads `f66e667c5924716e6ab0c36c9b817abd485be10b` by `ls-remote`, and `0fabcf4f0f` is not an ancestor
of it. The push is not this seat's.

## What the act turned on

**The pin was load-bearing, and that is measurable rather than assumed.** The order forbids building
"at or after" `14a36147bd`. `git diff --stat 14a36147bd..HEAD` over the packaged inputs reads 5 files
and 375 insertions in `lib/opal_data_harvest/` -- and that package is a SECOND CLOSURE ROOT of this
artifact. A build from the shared tree at HEAD would have carried `transport.py`, `publishers.py` and
`backfill_driver.py` into the zip, files the pair's table does not list, and the act would have
STOPped. The terraform module is byte-identical at the pin and at HEAD, which is exactly why the
BUILD had to come from the detached worktree while the APPLY could run from the shared tree.

**One build, not two.** The build script re-builds on its upload path, so running it twice would mean
the artifact graded by `content_diff` and the artifact uploaded are different runs' outputs. Instead:
one `--build-only` build, then the module's own `upload_verified` (sourced) on that exact file. The
sha256 chain is unbroken from the local zip through the S3 read-back to the deployed CodeSha256.

**A count match is not an identity match.** `CHANGED 8 + ADDED 8` is satisfiable by the wrong 16
files. All 16 moved paths were enumerated and matched BY NAME against the COO half's table.

## Three instrument errors I made and corrected in-session

1. **`tail -120` on the build cut the evidence it was meant to capture.** The 16 per-file CONTENT-DIFF
   lines sit among 364 IDENTICAL lines, so the tail kept the summary and dropped the per-file lines.
   A range-limited read is not a read. Fixed by re-running `content_diff.py` read-only on the same zip.
2. **A hand-typed CloudWatch epoch was a year wrong.** `1759812300000` is 2025-10-07, not 2026-10-07,
   and it returned real-looking `AMGT_PHASE` lines (`mentions decode 3137-3720 ms`) from a year-old
   window. The tell was a second call with an end-time returning `0 of 0 streams` while the
   open-ended call returned data. Recomputed with `datetime`; the corrected window shows cold cost in
   init (558-852 ms), chatter generation read (636-926 ms) and chatter compute (911-1486 ms), with
   mentions decode at 12-236 ms -- the reverse of the wrong window. The join is confirmed against a
   second instrument: cold totals 3285-4582 ms equal the reporter's own `cold n 6 min 3285 max 4582`.
3. **I compared the zip's compressed bytes against the UNZIPPED ceiling** and nearly reported a size
   discrepancy against a signed half. The half's 255,401,153 B is the build script's own accounting:
   package unzipped (133,657,520) + layer `opal-amgt-print-deps:1` (121,743,633). Reading the
   producer reproduced the half's figure exactly. Naming the OBJECT came before doubting the half.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-routes api-routes` | run before taking a live gateway read, because the rail routes raw API-GW inspection here | **GAP.** DESIRED-plane by its own disclosure (parses `api-gateway.tf`, "never a live describe") and returned **0** scoped/amgt hits, because this API is declared in `scoped-amgt-api.tf`, which it does not parse. It cannot answer a served-plane route question. The `aws apigatewayv2 get-routes` read was taken under an audited `# rail-checked:` marker naming that reason. |
| `comp-find` | `comp-find --files 'build-and-upload-scoped-amgt' --limit 10` | Exceeded 120 s and was backgrounded; an earlier attempt was rail-denied for piping into `tail`. Located with native `Glob` + a directory listing instead. On this device a comp-find file lookup is slower than the native tool the rule admits. |
| `content_diff.py` | `python infra/aws/terraform/harvest/content_diff.py --zip <zip>` | files 380, IDENTICAL 364, CHANGED 8, ADDED 8, REMOVED 0 against `OVpDhfwD`. |
| `deploy_ledger.py` | `open` (4 legs) -> `close-leg` L1/L2/L3/V1 -> `close` | The NEVER-2 carrier. Opened before the apply, each leg closed against measured evidence. |
| `safe-apply.sh` | `-chdir=infra/aws/terraform/harvest apply ba20.tfplan` | Rule 18. Applied the SAVED plan, not a re-plan. No HALT surface, no override. |
| `safe-commit.sh` | `-F <msgfile>` twice | Rule 14a. msg-verify MATCH both times. No `--force`, no author override. |
| `proof-of-spec-check.py` | instance + `AC1,AC2,AC3 --governing-order <order>` | **VALID** on the committed bytes: invocation alignment 3/3, 11 of 11 named controls discriminate, rollback named, surprises 0. |

Two rail denials were recognised as aborting their whole Bash call, and the segments they silently
skipped were re-run as their own calls.

## Blockers

**None.** Nothing is owed by this seat on this order.

## Next Steps

1. **[`2.0.0_SA_COO~Z`]** The `<status>` flip on the order is the issuer's, as it was for az-5
   (flipped at `1014126140`).
2. **[ba-24's walk, `1.0.0_SA_CTO~Z` to grade]** CTO conditions 4 and 5 are unexercised BY
   CONSTRUCTION and both halves say so: the Refresh control pressed once on DEV (expected: pending
   state then nothing, no error surface -- an error surface is a ROW and an expedite of round 45's
   control removal, explicitly NOT a rollback), and `/resolve` through the edge and the authorizer.
   Every check in this order invokes the function DIRECTLY.
3. **[`1.0.0_SA_CTO~Z`]** `comp-routes api-routes` does not cover `scoped-amgt-api.tf`. Every seat
   asking a scoped-amgt route question will hit the same gap and take the rail-checked marker. Worth
   widening the parser's input set or recording the non-application.
4. **[reported, not a defect]** Lead-panel cold init+duration moved from 2,580-3,137 ms to
   3,285-4,582 ms as the artifact grew by the filings package and three new modules. No graded bar is
   near: the one graded cold bar here, c59's 2,000 ms on `/freshness`, was met by all 34 cold invokes
   at 773-1,048 ms. If a later round wants the lead-panel path back under 3 s, the phase table says
   the cost is chatter compute and generation read, not import time.
5. **[`0.0.0_AB_MSTR~Z`]** Both commits are LOCAL; cloud-ops rule 6's tag-and-follow-tags leg is not
   taken because this order's bounds forbid a shared-branch push.

## Startup findings, named not re-filed

`org/XXX.md` A.2's invoker printed four `baseline missing` lines against the
`org/audit/archive/sitez/2026-10-06T151841Z` archive and one non-append edit on
`org/mcp/agent-spawn-audit.log` (first divergence line 13871, baseline 4,861,410 B vs live-head
4,861,897 B, which is also an uncommitted modification in the shared tree). A.2 admits only an
UNOWNED class; these are standing device-hygiene classes the invoker re-surfaces every session, so
they are named here and in the instance's `declared_exclusions` rather than re-filed.

## One thing the issuer asked mid-act

`2.0.0_SA_COO~Z` reported (msg 30580, acked) that the ledger `open` had left two paths STAGED in the
shared index since ~04:31Z, refusing other seats' `safe-commit` and `safe-merge` and holding
`0.0.0_AB_MSTR~Z`'s pull-merge. `git diff --cached --name-only` read EXACTLY those two paths and
nothing else; they landed at `759490bf74` in the same turn. Worth carrying forward: `deploy_ledger
open` leaves the index dirty by design (the sentinel must ride the entry's commit), so on a shared
tree the open and its commit belong in one turn, not at opposite ends of the act.
