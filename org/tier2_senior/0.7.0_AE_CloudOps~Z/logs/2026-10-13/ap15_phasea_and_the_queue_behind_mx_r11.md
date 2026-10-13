# OG-ap-15 Phase A: 3 of 5 built, the naming gate refused 2, and the rest of the queue is behind one sibling lane's ledger

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE

Delta to `ap10_b2_ap11_rollback_ap12_grant_ap13_narrow.md` (same date, earlier session). Round 37, a
fresh session after the ~17:51Z site-Z reboot. Three orders were delivered; one was worked to its
phase boundary and two were measured as blocked.

## Where the three orders stand

| order | state | what remains, and whose |
|---|---|---|
| `OG-ap-15` | **Phase A done, AC1 FAIL as measured** (3 of 5 built) | Phase B on the issuer's GO naming signed halves |
| `OG-ap-14` | **B1 not started -- precondition unmet** | `0.7.0_AE_CloudOps~MI` closing MX-r-11's ledger |
| `OG-hv-2` | **Phase A gate unmet** | ap-14's ledger, which is behind the same MX-r-11 |

## The one thing a reader should carry away

**The LGIC naming gate refused orion and eclipse, and it was RIGHT -- which is only knowable by
counting, not by reading the refusal.** The reflex read is "a re-vendor copies pre-existing source
text, so the gate is firing on a line I did not author" -- and the first half of that is true: the
three refused lines are pre-existing in `data/assets/scripts/silver/mirror_conversion.py` at trunk,
and the source commit that last touched that file (`b2538131ea`, OG-fd-2, today) passed the same
gate because it added only the fd-2 hunks.

But the gate grades ADDED lines, and the count is what settles it:

| | `^blackdiamond/cottonwood/bronze/` patterns in the package copy |
|---|---|
| source | 4 |
| etf, blackdiamond | 4 -- so their re-vendor added 0 matching lines and PASSED |
| orion, eclipse | **2** -- so their re-vendor ADDS two, and was REFUSED |

So for orion and eclipse the rebuild genuinely widens those packages' hardcoded-address surface.
Had I stopped at "pre-existing source, therefore noise" I would have asked for an override on a
refusal that is doing its job. **The discriminating read was the one that measured BOTH sides, and
the two families that passed are what made the two that failed interpretable** -- same shape as a
positive control, arrived at for free because the order happened to cover four families.

## What was actually built

Three packages, off trunk on `rel-nfra-oplgtw-fd2` at base `b0af6527a3`, nothing uploaded:

| family | build commit | package sha256 (base64) | non-drain drift |
|---|---|---|---|
| schwab | `12ecbe2b8f` | `U6l7D4fUe125WC53/GblkfHQKtDbpzRorHLLsvlbFmc=` | 0 |
| etf | `58ee124eb7` | `zNCf2GLiRNSpUYsdQUUPvwuAHtDZBlPevai0YqdzRh4=` | 19 |
| blackdiamond | `e05a80e0d9` | `hi/bL8SV9CKs0FNpo6ftPn4OTdEuF24wOqQ5C0aZln0=` | 298 |

**The sha256 encoding was a decision, not a transcription.** AC2 compares `live_code_sha256` to
`package_sha256`, and the live value is Lambda's `CodeSha256`, which is BASE64. A hex digest would
have satisfied AC1 (which only tests truthiness) and then failed AC2 at the grade, after a deploy.
`build-and-upload.sh` already emits base64 (`openssl dgst -sha256 -binary | base64`, :674), so the
right value was free -- but only if you read AC2 before writing the record rather than after.

## Three traps, all of them worth the cost

1. **The drift instrument was validated against a known answer BEFORE it was used.** The order's
   table (etf 19, orion 282, eclipse 398, blackdiamond 298) is FD2_DRIFT's
   `drift_lines_without_drain_code`, and my first implementation reproduced the OTHER column
   (101/359/475) because I measured against the pre-fd-2 pin `4c7e933975`, which already carries
   the fd-1 drain. Re-pinning to `12a92ffa49^` (the commit before OG-fd-1) reproduced all four
   numbers exactly. Then blackdiamond still read 280 against the order's 298: FD2 counts a
   never-vendored module's lines as `len(split("\n"))` = 91, where I had counted non-empty lines =
   73. **An instrument that reproduces a published number on four of five families and misses the
   fifth by exactly the blank-line count is telling you about its convention, not about the world.**
   Both columns are now recorded, so neither reading can be mistaken for the other.
2. **`ap15.AC1.sh` CRASHES on `build_commit: null`** -- `c + "^{commit}"` raises
   `TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'`, so the grader dies instead
   of reporting the family as unbuilt. Its own `.get(k, "")` default anticipates EMPTY, not null, so
   I recorded `""` with an explicit `build_commit_absent_reason` and AC1 then printed its intended
   verdict: "3 of 5 ... orion: build_commit not a commit". **A null I chose turned a FAIL into an
   instrument crash; the encoding the instrument's own default implies is the one to write.** Named
   to the issuer, which owns the check.
3. **A `grep -c locked` read 0 against four locks that had all landed.** I locked four release/
   rollback worktrees against GC, and my verification -- `git worktree list --porcelain | grep -A1
   -E "<names>" | grep -c locked` -- printed 0 because `locked` is not within one line of the
   `worktree` line. A per-tree parse showed 4 of 4 locked. `LD`-class lesson I already hold ("never
   read a gate's verdict from a positional slice") and still re-learned on a cheap read.

## Instrument discipline that earned its keep

- **The build base moved under me and I measured the consequence instead of assuming it.**
  `box/sitez` advanced 30 commits between my read and the worktree creation (peers plus a CLOUD
  box-sync), so the branch is based at `b0af6527a3`, not the `2bbce5d267` I had read. `git log
  --name-only b0af6527a3..box/sitez` over the four build surfaces returned ZERO files, so the base
  is source-equivalent to trunk for this build. Recorded as a basis line, not a hope.
- **N = 3 writers of `dlq_drain`, measured on two planes.** Four named files gave 3 assignment
  sites; `comp-find '\["dlq_drain"\]'` over 199,856 files gave SURFACED=3 and TEST=3, the same
  three. The corpus-wide DEF band reads 2, which is not a contradiction: etf calls
  `mc.dlq_drain_record`, so there are two function DEFINITIONS and three assignment sites. **Two
  numbers at different grains, both true, and the ask states which grain it means.**
- **Both branches of the expected outcome, read from each producer's own rule.** The three writers
  do NOT share a rule (mirror unconditional, etf unconditional per tree, schwab guarded by `if dlq
  is not None`). schwab's guard cannot fail in production because `run_sweep` sets `dlq` to the
  drain result or a fallback dict, never `None`. The only branch where the key is absent is a sweep
  that writes no status section at all (`NOT_WRITTEN (no silver partitions)`). **An empty DLQ still
  writes the key carrying `drained: 0`, so AC2 is robust to a quiet queue** -- which matters,
  because a quiet queue is the normal case and would otherwise have looked like a failed deploy.
- **A gate's named Action is not a gate override.** `build-and-upload.sh` refused blackdiamond until
  `opal_strategy_matcher.py` was registered in `lambda-source-map.json` `files[]`. I did exactly
  what the refusal's Action line said and did NOT set `BAU_PARITY_SKIP`. The edit was surgical
  rather than a `json` round-trip, because reserialising a 2,700-line shared map would have put a
  reformat diff across every other function: anchored inside that function's own `files[]`,
  occurrence count asserted to rise by exactly one, `json.loads` before the write was kept, and
  `git diff` read `1 file changed, 1 insertion`.
- **The sentinel census was read across EVERY worktree, and the stale copies are the trap.**
  MP-z-5's sentinel is gone from the shared tree's HEAD but still sits at HEAD in six older
  worktrees. Those are branch state, not open deploys -- NEVER-2's warning running in the opposite
  direction from the usual one. The shared tree carries the CLOSED entry, so MP-z-5 is genuinely
  done; MX-r-11's sentinel, by contrast, is present in the shared tree and its entry reads OPEN.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `vendor-manifest.sh` (copy + `--check`) | PASS x5 | `--check` before and after each family; schwab 11 of 11 parity, exactly 1 file moved |
| `build-and-upload.sh BUILD_ONLY=1` | PASS x3, REFUSE x1 then PASS | blackdiamond refused on ADHC_DRIFTD.002 until the source-map row; import-closure OK on all three |
| `ap15_drift.py` (new) | PASS | reproduces FD2_DRIFT's BOTH columns on all five families; two pins, missing-module lines counted FD2's way |
| `safe-commit.sh` | PASS x6, REFUSE x2 | the two refusals are the naming limb on orion and eclipse; `msg-verify MATCH` on every commit |
| `commit-gate.sh` | FAIL once, then PASS x3 | caught a heredoc-mangled comment (see below) before it reached a commit |
| `surprise-row-gate.py` | PASS | row Z-S102, 1 new row of 522 checked |
| `ap15.AC1.sh` | CRASH, then FAIL (intended) | see trap 2 |
| `comp-find` | PASS x2 | one corpus census and one assignment-site enumeration, denominators printed |
| `aws lambda get-function-configuration` | PASS x5 | all four unpinned values equal the fd-2 ask's 17:2xZ read |
| `aws s3api list-object-versions` | PASS x5 | exact-key filtered; control printed 41 versions over 7 family keys |
| `deploy_ledger` state | READ ONLY | no ledger opened by this seat this session; nothing deployed |

**What worked:** validating the drift instrument against a published answer before trusting it;
reading AC2 before writing the record that AC2 consumes; measuring both sides of the naming-gate
refusal instead of arguing from authorship. **What failed:** a heredoc ate a `\\` and broke a python
comment mid-string (the commit gate caught it, and this device's memory already holds that lesson);
a `grep -c` verdict read 0 against four successful locks; I chose a JSON null that crashed a
grader. **Gap found:** `ap15.AC1.sh` has no guard for an absent `build_commit` -- named to the
issuer, which owns the check.

## Blockers

**None owned by this seat.** Every open item belongs to someone else, and each is a named act
rather than a wait:

- `[2.0.0_SA_COO~O]` and `[1.0.0_SA_CTO~Z]` -- sign or refuse schwab, etf and blackdiamond, each
  alone, and rule on orion/eclipse's route. Row `Z-S102` names the three routes: elect the fd-2
  ask's option (b) drain-only package; let `mirror_conversion.py` reach LGIC conformance under its
  own migration (rule 30 R19); or an R20 register entry.
- `[0.7.0_AE_CloudOps~MI]` -- close MX-r-11's ledger `nfra-mcpindex-r10-catalog-release` (opened
  22:34:48Z, 8h window). ap-14 B1 and, behind it, hv-2 Phase A both start from that close.

## Current State (handoff -- zero prior context assumed)

**Nothing was deployed this session. No ledger was opened by this seat. The world is unchanged**
except for six commits on a build branch and three on `box/sitez`.

- **Build branch `rel-nfra-oplgtw-fd2`** at `C:/tmp/og-rel-fd2`, base `b0af6527a3`. Carries the
  three built families, the source-map row, and -- UNCOMMITTED in the working tree -- the vendored
  orion and eclipse copies, deliberately left in place so no re-vendor is needed once a route is
  chosen. The re-vendored package dirs are NOT on `box/sitez`, per the order's step 1.
- **On `box/sitez`:** `292b2a01b3` (row Z-S102), `f917adf37c` (the build record, the drift
  instrument, its output, and the five-family ask). Push state: **LOCAL @f917adf37c**, measured --
  `git ls-remote` reads origin `box/sitez` at `ddcb9ed5f5`, 2 behind. Push is never this seat's act.
- **Live, unchanged:** schwab runs `YeLmNn/Tkz+HYVVrCS/PeE+mISSAnH/8ilUUxPEnCmk=` with
  `OPAL_BUILD_COMMIT a11240c01c`; etf, orion, eclipse and blackdiamond run their 2026-09-27 builds
  UNPINNED; the gateway runs `64b3e54658`.
- **PARTIAL ROLL-OUT STILL STANDS.** Only schwab drains per-family. etf, blackdiamond, orion and
  eclipse keep draining the WHOLE shared queue until their own releases land, so row `Z-S91` stays
  open for all four -- and the 2026-10-13 instance of that hazard (a blackdiamond sweep deleting an
  eclipse record) can recur at any 13:00Z or 16:00Z sweep.
- **Four worktrees locked** against GC with a reason (`mp-n1-rb`, `mp-n1-rb2`, `og-rel-cti11`,
  `og-rel-pptx`): each is a release or rollback pin on a live gateway ref, flagged by the GC hook as
  "unlanded work" because a deploy-only cut never merges to trunk. Locking is the correct
  disposition -- `worktree_gc` has deleted a live pin before.

**What the next act needs, concretely:**

1. **On the issuer's GO for a signed family** -- open ledger `nfra-oplgtw-fd2-<family>-drain` (entry
   AND sentinel first), merge that family's build commit into `box/sitez` with `safe-merge.sh`
   carrying the package dir and its one `silver_build_commit` row, `safe-apply` with
   `-target='module.silver_converter["<family>"]'`, and STOP on any plan row beyond that one
   function's code fields plus the one environment value. Apply only OUTSIDE `[09:15,11:35)`,
   `[12:00,13:35)`, `[15:45,16:35)` and `[21:15,23:59)` Z -- the converters' own sweep and pull
   windows. Then grade at that family's NEXT SCHEDULED sweep (schwab `cron(15 12)`, blackdiamond
   `cron(0 13)`, etf `cron(30 23)`): no ad-hoc invoke.
2. **If a graded sweep writes no status section at all**, the key is absent for an input-state
   reason and the honest act is to re-read at the next scheduled sweep, NOT to roll back working
   code. ap-12's AC2 is the precedent: a criterion no deployment could satisfy was graded FAIL and
   the code deliberately left in place.
3. **When MX-r-11's ledger closes** -- ap-14 B1: re-read `EC2_MANIFEST.json`
   `services.opal-gateway.deployed_commit` at HEAD, confirm it with ONE SSM md5 read of the host,
   re-confirm ONE gateway release in flight across every worktree with the per-tree denominator
   printed, then cherry-pick the six commits in order into `C:/tmp/og-rel-r30`. ap-14's B2 window is
   11:00Z-23:00Z, so its deploy is a next-day act regardless.
