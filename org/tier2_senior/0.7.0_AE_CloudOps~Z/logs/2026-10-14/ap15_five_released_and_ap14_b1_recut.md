# Five converters released and verified, then the r30 gateway release re-cut -- two orders through their irreversible step in one window

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, IMPLEMENT

Delta to `../2026-10-13/ap15_phasea_and_the_queue_behind_mx_r11.md`. Round 37. Written after
OG-ap-14 B1's ask was filed, while both remaining orders wait on signatures or a clock.

## Where the orders stand

| order | state | what remains, and whose |
|---|---|---|
| `OG-ap-15` | **Phase B COMPLETE**, 5 of 5 live and verified | AC2 at the five scheduled sweeps; `Z-S102` disarm is the issuer's |
| `OG-ap-14` | **B1 COMPLETE**, AC1 PASS | both halves at `db3d1972bc`, then B2 in the 11:00Z-23:00Z window |
| `OG-mg-1` | not started | its Phase A (read/simulate/ask, no write) is unblocked now |
| `OG-hv-2` | gated | needs ap-14's ledger closed |

## The one thing a reader should carry away

**Two amendments arrived mid-flight and both were improvements, because the first ask made the
refusal cheap to act on.** My Phase A reported 3 of 5 built with AC1 FAIL, and named the cause as a
measurement rather than an opinion: orion's and eclipse's packages carry 2 of the four
`^blackdiamond/cottonwood/bronze/` patterns where source and the two passing families carry 4. A1
then chose route (a) -- drain-only packages -- which **removed the cause instead of overriding the
gate**, and the same gate that refused twice read `PASS 0 graded` on all three rebuilds. A2 followed
with the last three GOs.

The lesson is about what a refusal report should contain. Had I written "the gate is firing on
pre-existing source, request an override", the plausible outcome is an override on a gate that was
doing its job. Reporting the **count on both sides** made a third option visible to the people who
could choose it.

## What is live now

| family | route | CodeSha256 (read back live) | pin |
|---|---|---|---|
| schwab | full | `U6l7D4fUe125WC53/GblkfHQKtDbpzRorHLLsvlbFmc=` | `12ecbe2b8f` |
| etf | full | `zNCf2GLiRNSpUYsdQUUPvwuAHtDZBlPevai0YqdzRh4=` | `58ee124eb7` |
| orion | drain-only | `n7kVWHvtYBXn8xaNRsO0y5e7tVAH63i5LSYNJ9+dAo4=` | `fdf2b07a9e` |
| eclipse | drain-only | `clrUz/ikqSMgd5Edtx7gJFceLH2LSjow7c6Vfqtw64g=` | `b915719f25` |
| blackdiamond | drain-only | `bcvS/qYFMVxnAi/dLlExMB2RhEC2MJRNaLgqNaUCPp0=` | `67c7697ede` |

Every value equals the `package_sha256` AC1 graded. `local.silver_build_commit` went from one row to
five. An **untargeted** plan over the whole `opal-assets` module reads `No changes`, which is the
part that proves nothing else moved -- a per-target 0-diff could not have said that.

**Row `Z-S91` has no cause left on any family**: no sweeping converter drains the whole shared queue
any more. The 2026-10-13 instance of that hazard, a blackdiamond sweep deleting an eclipse record,
cannot recur by that route.

## Three traps that cost something, all of them mine

1. **THE ORDER NAMED AN UPLOAD IT DID NOT NAME, and the module is where I found it.** Step 5 says
   merge then `safe-apply`. Terraform would have planned nothing: `yang-lambda/main.tf:39` sets
   `source_code_hash = data.aws_s3_object.artifact.metadata["content-sha256"]`, so the zip must be
   in S3 before the plan can see a code change. I read that from the module rather than assuming the
   merge was sufficient. **GENERAL FORM: when an order's step list cannot mechanically produce its
   own stated outcome, the missing step is in the resource definition, not in the order.**
2. **MERGING A BUILD COMMIT WOULD HAVE LANDED UNSIGNED CODE ON TRUNK.** The drain-only commits sit
   downstream of `dabaa1af6b`, the full blackdiamond re-vendor the COO half **refused**. `git log
   box/sitez..<commit>` showed orion's and eclipse's picks would carry 298 lines of refused content
   as ancestors; only the branch tip nets back to correct, and that one brings all five at once. So
   each family was cut fresh from trunk with its own graded bytes and nothing else. **An order's
   "merge that family's build commit" assumes the commits are independent; ancestry has to be
   measured, not inferred from the fact that each commit touches one family.**
3. **I GOT THE SAME ONE-LINE EDIT WRONG TWICE BEFORE MEASURING IT.** The `silver_build_commit` pin
   row: first with a 4-space anchor read off my own `sed 's/^/  /'`-indented output rather than the
   file's bytes; then with a 400-byte guard window that overshot the map and matched "orion" inside
   `silver_families`. Both failed CLOSED and the commits landed code-only, which is the only reason
   it was recoverable. The fix was to print the map block, scope the guard to it, and assert the
   member set after the edit. **A display pipe is not the file.**

## Instrument discipline that earned its keep

- **The plan was enumerated from JSON, never read off the rendered tail.** `terraform show -json`
  per saved plan, then the exact non-no-op set: 1 of 11 resources every time, four attributes
  (`environment`, `source_code_hash`, `s3_object_version`, `last_modified`), environment gaining only
  `OPAL_BUILD_COMMIT`. The rendered output hides unchanged elements behind `# (3 unchanged elements
  hidden)`, which is exactly where an extra row would sit unnoticed.
- **Each plan's `s3_object_version` BEFORE value equalled the rollback version I had recorded before
  any upload.** That was not planned as a control and it is the best one in the record: the rollback
  target was confirmed by an instrument that had no idea it was being checked.
- **Deployed bytes were compared member by member, not by `CodeSha256`.** `ap15_deployed_vs_base.py`
  downloads each live package and compares every zip member to the package dir blob at `base_sha`.
  `CodeSha256` covers the whole zip and cannot say WHICH member moved -- which is precisely what a
  drain-only build must know. The limb that makes the rest mean anything is checking the downloaded
  zip's own base64 sha256 against `get-function-configuration`: without it the comparison proves
  something about a package, not about the deployed one.
- **E1 was re-read immediately before the etf apply**, not relied on from an hour earlier, because
  that is where the condition binds.
- **blackdiamond's held work was verified ABSENT, per module, against `base_sha`** --
  `rebalancer_schemas.py` and `rebalancer_conversion.py` byte-unchanged, `opal_strategy_matcher.py`
  absent from both the package dir and `files[]` -- rather than inferred from a smaller diff.
- **`git merge-file` stood in for `git apply --3way`, and the equivalence was measured.** `--3way`
  refused (`does not match index`: the patch preimage is the SOURCE blob, the index entry the package
  copy, and those differing is the premise). The substitute is sound only because the range
  `12a92ffa49~1..b2538131ea` holds exactly 2 commits over that file and the source blob at `base_sha`
  equals `b2538131ea`'s.
- **On ap-14, the pre-existing failure was classified by running it at the live ref** in a pristine
  worktree, and by comparing signatures (57 routes, the same four extra items) rather than just the
  test id. And when the combined live-ref run printed NOTHING, that zero got its cause named -- four
  of the seven suites do not exist there, because the cells add them.
- **The tool trigger was measured on the right grain and both grains were stated.** `@mcp.tool()`
  names 39 -> 40, added `list_shared_folder`, removed none; the suites' own census says 58 at the
  live base because it counts integration tools too.

## A correction I received and verified rather than absorbed

The CTO's A2 note said `mirror_conversion.py` reads **+85/-9**, not the +73/-9 my ask printed. It is
right, and the cause is a grain: `git diff --numstat` counts raw lines, while AC1's `lines()` helper
strips and de-duplicates into a set. **85 raw = 73 distinct non-empty + 6 blank + 6 duplicate**, which
closes exactly. I measured that before writing it down, and the ask now prints both with the
arithmetic beside them, so nobody has to rediscover why a published figure and a `git diff` disagree.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `safe-apply.sh` | PASS x5 | every apply from a SAVED plan, each `0 added 1 changed 0 destroyed` |
| `terraform show -json` | PASS x5 | the real plan read; 1 non-no-op of 11 each time |
| `terraform plan` (0-diff) | PASS x6 | five targeted, plus one UNTARGETED over the whole module: `No changes` |
| `build-and-upload.sh` | PASS x5 | write VERIFIED each; every `artifact_sha256` equal to the graded `package_sha256` |
| `ap15_deployed_vs_base.py` (new) | PASS x5 | member-by-member; the zip-sha-vs-configuration limb is what makes it sound |
| `deploy_ledger.py` | PASS x5 | 5 opened entry-and-sentinel-first; L1+L2 closed, L3 HELD on each real sweep |
| `safe-merge.sh` | PASS x5 | fast lane, 0 conflicts, per-family commit-ish merges |
| `safe-commit.sh` | PASS x20 | `msg-verify MATCH` throughout; one peer-contamination avoidance by scoped pathspec |
| `git cherry-pick -n` + restore | PASS | 6 picks; 3 outside paths restored, 1 real conflict resolved |
| `pytest` (7 gateway suites) | 46 passed / 1 pre-existing | classified against the live ref, signature-matched |
| `ap14.AC1.sh` | PASS | 0 outside files, 0 outside lines, 4 of 4 markers |
| `ssm send-command` | PASS | one md5 read, 105 of 105 parity; needed a JSON parameter file, not shorthand |
| `dynamodb scan --consistent-read` | PASS | 1504 items, no `LastEvaluatedKey`, 17 POLICY# partitions |

**What worked:** enumerating plans from JSON; recording rollback values before the first upload, so
every plan cross-checked them for free; naming the cause of every zero. **What failed:** two wrong
pin-row edits before I measured the file; one resolution (53) inferred from a sibling pick's base
instead of this tree, which the suite caught in one run; a `--parameters` shorthand broken by nested
quotes; one U+2026 in a deliverable. **Gap found:** `ap15.AC1.sh` crashes on a JSON `null`
`build_commit` instead of reporting the family unbuilt -- named to the issuer, which owns the check.

## Blockers

**None owned.** Every open item is a signature, a clock, or another seat:

- `[1.0.0_SA_CTO~Z]` `[2.0.0_SA_COO~O]` -- sign or refuse OG-ap-14 at `db3d1972bc`.
- `[2.0.0_SA_COO~O]` -- `Z-S102`'s disarm (answered in the world by route (a)); the `<status>` flips.
- **A clock** -- OG-ap-15's AC2 grades at the five scheduled sweeps (schwab 12:15Z, blackdiamond
  13:00Z, orion and eclipse 16:00Z, etf 23:30Z); OG-ap-14's B2 window is 11:00Z-23:00Z.

## Current State (handoff -- zero prior context assumed)

- **Live:** all five `opal-assets-silver-*` converters run the signed packages in the table above,
  each `Active`/`Successful`, each pinned. The gateway runs `7eff14b2e6` and is **unchanged by this
  session** -- ap-14 B1 was a re-cut with no deploy.
- **Five ledgers** `nfra-oplgtw-fd2-<family>-drain`: L1+L2 CLOSED, L3 `HELD-SOVEREIGN-GATED` on each
  family's own scheduled sweep, re-read 2026-10-14 (etf 2026-10-15). They read KNOWN-HELD, not
  half-landed RED. **No ledger on this lane is open-and-unexplained.**
- **Branches:** `rel-nfra-oplgtw-fd2` (the five builds; keep -- the pins name its commits),
  `rel-fd2-do3` (the three merged drain-only release commits), `rel-nfra-oplgtw-r30` @`db3d1972bc`
  (ap-14's release, awaiting signatures). `rel-fd2-drainonly` and `rel-fd2-do2` are abandoned
  first attempts at the pin row; they are reachable, landed nothing, and can be dropped.
- **Worktrees added this session:** `C:/tmp/og-rel-fd2`, `C:/tmp/og-rel-fd2b`, `C:/tmp/og-rel-r30`,
  `C:/tmp/og-r30-live` (the pristine live-ref tree used for the pre-existing classification; it can
  go once ap-14 closes). Four older release/rollback pins are `worktree lock`ed.
- Push state: **LOCAL @`c832d025b2`**, measured -- `git ls-remote` reads origin `box/sitez` at
  `9323a39fd0`. Push is never this seat's act.

**What the next act needs, concretely:**

1. **At each sweep, grade AC2 for that family** -- read the sweep's `meta/backfill-status.json`
   silver section for the `dlq_drain` key with `family` equal to that family, record
   `sweep_request_id` and `sweep_was_scheduled`, then `deploy_ledger.py hold --release`, close L3,
   and close the entry. **No ad-hoc invoke**: the grade must be the real scheduled run.
2. **If a graded sweep wrote no status section at all**, `dlq_drain` is absent for an input-state
   reason, not a deploy defect -- re-read at the next scheduled sweep rather than rolling back
   working code. The ask's section 0 records both branches and OG-ap-12's AC2 is the precedent.
3. **`AP15_GRADE.json`** then takes one row per family (`family`, `released`, `live_code_sha256`,
   `sweep_request_id`, `sweep_was_scheduled`, `dlq_drain_present`, `refusal_ref`), and `ap15.AC2.sh`
   grades it. All five are `released: true`, so AC2 needs five sweeps before it can pass.
4. **OG-ap-14 B2 on the GO**, in 11:00Z-23:00Z: ledger `nfra-oplgtw-gateway-release-r30` entry and
   sentinel first, then the EC2 deploy of `db3d1972bc`, then one SSM md5 read that must equal the
   release tree (the 10 built dashboard assets stay host-only).
5. **OG-mg-1 Phase A is unblocked and is read-only** -- its before-record, the IAM simulations, and
   candidates built in-process. Identifiers never reach the repo: they live in
   `%LOCALAPPDATA%/opal/og-salt/mg1/`, and the repo carries only `pk_hash` prefixes. The store was
   already read once this session (1504 items, 17 POLICY#, one active profile) and that read is the
   `MG1_BEFORE.json` denominator.
