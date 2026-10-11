# AMGT-kk-1: the name list carries its folder count again, behind a guard that refuses the regression -- 0.7.0_AE_CloudOps~AMG

**archetype:** DEPLOY

**Date:** 2026-10-09
**Task Order:** `AMGT_RESAPP.TO-AMGT-kk-1.republish-the-name-list-with-research-folders` (round 86, `<risk>WORLD</risk>`)
**Status:** COMPLETE -- AC1, AC2, AC3 all PASS; proof instance VALID; deploy ledger CLOSED; drained

---

## Objective

Re-publish `s3://opal-data-harvest/crosswalk/v1/2026-10-09.json` from the one box whose research
library reads, so `research_universe` carries its live folder count instead of the `absent` it got when
jj-4 ran on library-less dell1 -- and first land a guard so that regression cannot recur.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| commit-gate.sh | `.tools/commit-gate.sh lib/research/identity/crosswalk.py <test>` | PASS | `clean for 2 of 2 file(s)` |
| pytest | `py -3.12 -m pytest lib/research/identity/tests/ lib/research/corpus/tests/test_library.py -q` | PASS | 276 passed -- the regression arm |
| comp-find | `comp-find '_research_folders_for_disclosure' . --limit 30` | PASS | found the ONE caller + the ONE 2-tuple patcher; this decided the design |
| deploy_ledger.py | `open` (5 legs) -> `close-leg` x5 -> `close` | PASS | opened before the act, CLOSED with every leg proven |
| proof-of-spec-check | `<instance> AC1,AC2,AC3 --governing-order <order>` | PASS | `VALID (rc=0)` |
| aws s3api | `head-object` / `list-object-versions` before and after the put | PASS | s3api, not `aws s3 ls` -- UTC, per rule 22a |
| crosswalk --disclosure | `python -m lib.research.identity.crosswalk --as-of 2026-10-09 --disclosure` | PASS | the order's named free pre-check |
| sequence-check | `--project AMGT_RESAPP` | PASS | PLACED, EXECUTING, active |
| to-check | `--all --assignee 0.7.0_AE_CloudOps~AMG` | PASS | `total=0` of `scanned=5335` at seating |
| crossbox-call.py | `ack` x4, `open --kind CALL` | PARTIAL | acks fine; the envelope commit is barred to this seat (see below) |
| comp-pipescript / comp-iam / comp-blast | not run | SKIPPED | AE minimums bind to gold-run triggers, `iam.tf` changes and infra changes; this act had none (the order's own preflight declares comp-iam already run and comp-schedule not applicable) |

**What worked:** `comp-find` was load-bearing, not ceremonial -- it found that
`_research_folders_for_disclosure` has exactly one code caller AND one test that patches it as a
**2-tuple**, which is why the guard got a separate `_library_absent_reason` probe instead of a widened
return. Widening it would have broken `test_crosswalk_served_union.py` and `round85_prep`'s check.
`--path` on the round-85 check let me grade the candidate **before** the put and catch a blocker while
it was still free to catch.

**What failed:** nothing crashed. Three self-inflicted misses worth recording, because each one looked
like a finding until it was checked:
1. `python -I` ignores `PYTHONPATH`, so my first library read raised `ModuleNotFoundError: No module
   named 'lib.research'` -- a FALSE absence that reads exactly like a missing module. `-I` is for
   untrusted downloaded files, not this repo's own code.
2. My first attempt to exercise the guard set `OPAL_RESEARCH_LIBRARY_ROOT` to a bogus path, which did
   NOT make the library absent -- `library_root()` silently fell through to the next candidate. The run
   proved my setup wrong, not the guard. That became row S3.
3. My first surprise rows used `AMGT_RESAPP-AMG-S1`; the gate's `ID_RE` admits a coordinate of ONE
   capital plus digits, and `DEVICES.json` says the laptop's `row_coordinate` is `""` -- "the laptop
   bare". Reverted and re-minted as `AMGT_RESAPP-S1`. `surfaced_at` also has to be a real timestamp,
   not a masked `16:1xZ`.

**Gap found:** row S4 -- the mass-deletion audit log is written in the invoking tree.

---

## Work Completed

### 1. AC3 first: a guard so the regression cannot recur (`f2dbac84a4`)

`build_crosswalk` writes `research_universe = {"absent": ...}` whenever its caller passes no folders
(`crosswalk.py:975-990`), and `_research_folders_for_disclosure` swallows EVERY read failure. On
`--write-pool` that silently replaces a served folder count with an absence -- exactly how today's key
lost the 97 folders 2026-10-07 carried.

`main` now refuses that put: nonzero exit (2), a reason on stderr naming the served count, placed
BEFORE `build_crosswalk` and before any put. Scoped to fire on an ABSENT library over a served count
and nothing else. `--out`, `--dry-run`, `--disclosure` and a first publish with no served
`research_universe` are unchanged -- none of them can overwrite a count.

The trigger needs the error the existing helper discards, so it comes from a separate
`_library_absent_reason()` probe, called ONLY after the folders came back `None` (so a readable library
is never listed twice -- asserted in a test). **The helper's `(folders, root)` arity is untouched on
purpose:** `test_crosswalk_served_union.py:183` patches it as a 2-tuple and `round85_prep`'s check
reads it.

10 arms in `test_crosswalk_refuses_absent_library.py`, including a negative arm (a readable library
still publishes over a served count) so an unconditional refusal could not pass, and four grading the
probe directly against the real `LibraryAbsentError`.

**The arms BIND, by a planted mutant:** deleting the refusal's `return 2` flips the mutant to
`OK: uploaded s3://opal-data-harvest/crosswalk/v1/2026-10-09.json` and fails 2 of 10; restored, 10
pass. The mutant ran only against a mocked `write_pool`, so no S3 object was ever at risk.

### 2. The pre-publish diff caught a blocker while it was still free (row `AMGT_RESAPP-S1`)

The order requires the widened diff printed BEFORE the put. Graded against the `--out` candidate, C1-C4
passed and **C5 failed on exactly one leaf**: `research_universe.source`.

`2026-10-07.json` was built on **site Z** -- its source names the `Opal Bloomberg` user profile -- not
on the laptop. AMENDMENT 2's GO said "2026-10-07.json was built there" of the laptop, and
`GROUP_REPUBLISH_NOTES.md` section 1 quotes that same site-Z path while calling the box "the laptop".
So a correct republish from here necessarily moves that leaf, `--admit` did not name it, and the field
MUST name the device that did the read -- writing site Z's path would be a false disclosure.

**I held the put** and sent one ask. The order's own gate says every field must be equal or *admitted*,
and admission is the issuer's; proceeding would have been me adjudicating it, and if the issuer had
instead re-cut to site Z my publish would have needed a rollback. Everything that did not depend on
the answer was finished first: the guard landed and tested, AC2 run, the diff printed in full, the
prior VersionId recorded, the candidate built, rollback bytes held locally.

The issuer ruled in AMENDMENT 4: admit it, and corrected its own GO ("2026-10-07.json was built on
SITE Z, not the laptop"). Resolving row `AMGT_RESAPP-D1-S17`.

### 3. AMENDMENT 3's STOP condition fired, and was cleared as prescribed

Three client-data removal commits had to be ancestors of HEAD before a served write. At
`f2dbac84a4`: `20e0b6408b rc=1`, `cb16f8b2f9 rc=1`, `d2eb7316f2 rc=1`, `96a82dda90 rc=0` -- the
positive control read 0, so the three were real. The laptop's box-sync was paused for the incident.

Remedied as directed: merged `origin/CLOUD @dbf224fbf1` (`80c910315f`). Re-printed at `778e99abd8`:
all four `rc=0`. Graph only -- no `git show`, no `git log -p`, no checkout of those commits or their
paths. A second merge (`d1db275360`, CLOUD `@d1d1f17871`) took the issuer's AMENDMENT 4 edit to AC1's
embedded `<invocation>`, WITHOUT which the instance's recorded invocation would have diverged from the
order and been refused for what was only a stale local copy.

Both merges carried upstream deletions (93 and 86) and the mass-deletion gate required attribution;
the trailers name the CTO fold and `ADVI_COTBKF.TO-CB-az-1` respectively. Those deletions are not this
seat's act.

### 4. The act

| | |
|---|---|
| **PRIOR VersionId** | `CHWQWAM0oNxOpU_5Hs8_fy5RUZ_Sgl20` -- 850056 bytes, sha256 `a03c8cac74f9ac43...` |
| **NEW VersionId** | `d3y5Cbs6ygTMvKj28fSvbR4ciDsyPv.9` -- 850198 bytes, sha256 `0229681e6db25ab5...`, 17:20:53Z |
| versions on the key | **2**, prior `IsLatest=false` -- no delete, rollback intact |
| records / issuer.cik | 243 kept (243 of 243 prior present) / 204 of 243 measured, 0 bad |
| `research_universe.folders` | **102** (`read_at` 2026-10-09T17:20:50Z), from `C:\Users\AndrewBerman\OneDrive - Opal Capital\Shared - Documents\Asset Management\Research` |

AC1 live `R85 CROSSWALK AC1: YES` exit=0. AC2 `R84 LISTING AC1: YES` exit=0 -- **a bound**: it passed
at base too, so it proves the republish broke nothing, never that it worked. AC3 10 passed exit=0,
before and after.

### 5. The guard, exercised against the live count it now protects

The unit arms cannot reach this. With the real `LibraryAbsentError` raised from `library_root` (the
dell1 condition) and `write_pool` replaced by a mock so a guard failure could not touch the key:
`main(--write-pool)` -> `rc=2`, `write_pool called=False`, printing `REFUSED: ... the served latest
list carries research_universe.folders=102 ... NO put was attempted` -- the count read live from the
key this act had just published. Negative arm in the same run: `--out` rc=0, no put, 850056 bytes.

Worth stating: the guard was correctly **INERT for this very publish**, because the served latest WAS
today's key carrying `absent`, so `served_folders` was `None`. The republish is what armed it.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Hold the put on one issuer call rather than publish and ask later | The order's own pre-publish gate says equal-or-admitted; admission is the issuer's. Waiting cost minutes; publishing wrong would have cost a rollback of a served artifact 243 records and downstream readers consume. Everything not depending on the answer was done first. |
| A separate `_library_absent_reason` probe, not a widened helper return | `comp-find` showed one test patches the helper as a 2-tuple and the round-85 check reads it; widening would break both. The probe runs only on the failure path, so a readable library is never listed twice. |
| Instance genre BUILD, not DEPLOY | Section 5's prose says DEPLOY but the order carries no line-anchored `<proof_genre>DEPLOY</proof_genre>` (grep 0 against a positive control). The schema: DEPLOY "is a CLAIM the checker grades against the governing order's issuer mark" and "the graded party cannot confer it on itself". So the mutant block, with a real mutant. |
| Instance to `~AMG/deliverables/`, not the `~RA1` path section 5 still names | `<paths>` and `<slot>` both read `~AMG`, and the complete-flip gate searches the assignee's own dir (the `~TRL` precedent at `31ee4440a2`). Line 69 is a leftover from before the re-address; surfaced to the issuer. |
| `determinism: N/A-WITH-REASON`, not STABLE | Two `--out` builds matched in length and in every graded denominator but are NOT byte-identical by design -- `research_universe.read_at` is a fresh live timestamp. STABLE would overclaim. |
| AC3's `expect` rendered as `10 passed...exit=0` | My first rendering of the order's prose used the literal `0 failed`, which `pytest -q` NEVER prints when green (with failures it prints `2 failed, 8 passed`). The evidence is unchanged; the regex now matches what the order's own named invocation actually emits. |
| Used the audited author override for the two `lib/` paths; did NOT for `org/devices/crossbox/` | The order's `<paths>` explicitly grants the two `lib/` files, and the TO-is-the-grant clause is hard-keyed to `0.9.0_WK_*` so an AE seat can never match it -- the validator's own comment records the override as the route taken at v3's first drain (row S2). `DEVICES_CROSSBOX` is the opposite case: its text says the folder is for each BOX MANAGER's records, so overriding would be taking that role. Asked `0.0.0_AB_MSTR` instead. |
| Reverted and re-minted the row ids rather than force them through | `ID_RE`'s coordinate is one capital plus digits, and `DEVICES.json` says the laptop's is `""`. Confirmed the dirty delta was only my two rows before reverting. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `lib/research/identity/crosswalk.py` | the guard + `_library_absent_reason` | Yes -- `f2dbac84a4` (audited override, lane BASE_EXEC) |
| `lib/research/identity/tests/test_crosswalk_refuses_absent_library.py` | 10 arms (new) | Yes -- `f2dbac84a4` |
| `.../deliverables/0.7.0_AE_CloudOps~AMG/...proof_of_spec.json` | the instance, VALID | Yes -- `fe30d75c0d` |
| `org/critical_paths/change_management/20261009T1714Z_amgt-resapp-r86-kk1-...md` | ledger, CLOSED | Yes -- `fe30d75c0d` |
| `.../surprise-channel/investigations/INVESTIGATION_v1.md` | rows S1-S4 | Yes -- `3a50c93247`, `76f6aa9189`, `a0223eb6af` |
| `.../deliverables/0.7.0_AE_CloudOps~AMG/XB_KK1_REPORT_TO_R1.md` | the final report | Yes -- `8a36cd64ee` |
| `s3://opal-data-harvest/crosswalk/v1/2026-10-09.json` | **the act** | n/a -- VersionId `d3y5Cbs6ygTMvKj28fSvbR4ciDsyPv.9` |
| `org/devices/crossbox/*.json` (5) | 4 acks + 1 CALL envelope | **No** -- barred to this seat; asked `0.0.0_AB_MSTR` |

Drain: `14191e0e45`, **on origin** `box/laptop` (`ls-remote` read). Worktree `C:/tmp/amg-kk1`
force-removed and branch `wk-amgt-kk1-r86` deleted after confirming containment.

---

## Blockers

None for this order -- it is done. One item is parked on another seat:

- `0.0.0_AB_MSTR` owes the `org/devices/crossbox/` commit + the bus line so `2.0.0_SA_COO~R1` on dell1
  is notified. The report BODY is already committed at `8a36cd64ee` and reaches CLOUD by box-sync, so
  the substance is not gated on that -- only the notification is.
- Rows `S2` (owner `0.0.0_AB_MSTR`), `S3` (owner `2.0.0_SA_COO~R1`), `S4` (owner `1.0.0_SA_CTO`) are
  open by design. S2 and S3 are cited by the proof instance, so they gate the issuer's `complete` flip
  until dispositioned -- correctly.

---

## Current State

`AMGT_RESAPP.TO-AMGT-kk-1` is executed and drained. `s3://opal-data-harvest/crosswalk/v1/2026-10-09.json`
now serves `research_universe.folders = 102` at VersionId `d3y5Cbs6ygTMvKj28fSvbR4ciDsyPv.9`, with the
prior version `CHWQWAM0oNxOpU_5Hs8_fy5RUZ_Sgl20` retained for a versioned-re-put rollback and no delete
made. AC1/AC2/AC3 all PASS, the proof instance reads `VALID (rc=0)` against the governing order, and
the deploy ledger is CLOSED with all 5 legs proven and no sentinel left. A guard in
`lib/research/identity/crosswalk.py` now refuses any future `--write-pool` that would write `absent`
over a served count -- proven armed end to end against the live 102 with the put made impossible. Four
surprise rows are filed, one of them already resolved by the issuer. `<status>` was not touched: the
order file is not in this order's `<paths>` and the terminal statuses are the issuer's.

---

## Next Steps

1. **`[2.0.0_SA_COO~R1]` Flip `<status>` to `complete`** -- every criterion PASSES and the instance is
   VALID at `~AMG/deliverables/`. Two issuer-side items named in the report: section 5 line 69 still
   points the proof path at `~RA1`, and the order carries no `<proof_genre>DEPLOY</proof_genre>` if the
   DEPLOY genre was intended.
2. **`[0.0.0_AB_MSTR]`** Commit `org/devices/crossbox/` (5 kk-1 records) and put
   `XB-20261009T181651Z-b4e2` on the bus to dell1.
3. **`[1.0.0_SA_CTO]`** Row S4: resolve the mass-deletion audit log's path via
   `git rev-parse --git-common-dir` so worktree rows survive the mandated force-remove.
4. **`[0.7.0_AE_CloudOps~AMG]`** Event-driven hold. Act on the next `[INBOX]` event the same turn and
   re-arm the Monitor on each `[WATCHER-EXPIRED]` line, one call, same turn, no skill load.
