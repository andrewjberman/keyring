# AMGT_RESAPP round 78 -- TO-AMGT-bb-18 LEGS 1 and 2: the code redeploy at the pin, and the snapshot event

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

Serial: `0.7.0_AE_CloudOps~A` | Window: 2026-10-08 06:38Z -> 07:5xZ (session start; prior log
`../2026-10-07/round78_bb23_leg0_vendor_from_deployed.md`) | Order:
`org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-bb-18.the-code-redeploy.md` @672ff10378
| Issuer: `2.0.0_SA_COO~Z` | risk WORLD, proof_genre DEPLOY | Cells `AMGT-bb-18` (legs 1-2) and
`AMGT-bb-23` (LEG 0, landed 2026-10-07)

---

## Current State

**The redeploy LANDED and every criterion reads YES. The NEVER-2 entry `amgt-resapp-r78-bb18` is
CLOSED, 6 of 6 legs proven, nothing stranded.**

`opal-amgt-scoped-api` now runs CodeSha256 `+s6R0/rcpQ6lJgYsX2JtxfgoFoCmiaozTtMreyyymTQ=` (base
`MkM9Kf37nmI+thEmZR+ij8ybbxGrHxqtsonjyI7N5eg=`), CodeSize 42,001,525, MemorySize **1769 unchanged**,
python3.11, layer `opal-amgt-print-deps:1` unchanged, LastModified 2026-10-08T07:19:32Z. The live hash
EQUALS the kept zip's own sha256 in base64, so the bytes that were gated are the bytes that run, and it
DIFFERS from the base, so this was not a 0-diff deploy. The 0-diff re-plan reads `No changes. Your
infrastructure matches the configuration.`

The GO for legs 1 and 2 arrived on the order itself at 2026-10-08T06:34:55Z -- not as a broker message --
about four minutes before this session registered. LEG 0 was already on CLOUD at `9e42b6cdb7`.

**What the act carries.** The round-78 adapter's six hookups (coverage marker, country case, the /thesis
statement of inputs, officer rank, source names, the peer price-listing refusal), the Peers V
below-three sentence, the rot signal's one home, the six dispersion field names, and -- the big one --
the dossier reader from method 5 to **method 7**, which makes this apply the act that moves the page: 51
section values in 35 names plus the 5 method-7 trims of 55 characters. **Six values are served
known-truncated by the CTO's ruling and are named here: LLY, NU (two), QXO, UNH, and SHOP management.**
Seven files from other projects ride the artifact; the one with a new served branch is
`lib/trading_calendar.py`, whose fallback now RAISES for a year outside 2010-2027 where the deployed copy
answered by weekday.

**Push state, MEASURED at 07:5xZ:** LOCAL. `origin CLOUD @f7e80ffdf2` by `git ls-remote`; this seat does
not push shared branches.

## The pin, and why equality was the control

**THE PIN: `fbb643923e9ab3db14aa8d8062fa9015a6722690`**, built from a DETACHED worktree
`C:/tmp/bb18-build` whose `rev-parse HEAD` reads that hash exactly and whose `symbolic-ref -q HEAD` is
empty. The order forbids "at or after", and that is not pedantry: the COO half measured that a build at
the merged trunk `f6cff376d1` would list 21 CHANGED, two of them off the half's table, which the order
makes a STOP. Shared HEAD was `c5cf46cc55` when this session started and `834beaddab` by its close --
peers committed six times during the act -- and neither was built. `dossier.py` line 145 at the pin reads
`METHOD_VERSION = "amgt-corpus-dossier/7"`.

## Deployment Sequence + Verification (AE role addition)

ONE NEVER-2 entry, opened BEFORE the build and **committed in the same turn with both required paths**
(`@98d018e6bf`), so the OPEN state lived in git and not only on this device. Six legs, closed in order.

**L1 -- the build.** 07:07:18Z to 07:07:39Z, `--build-only C:/tmp/bb18-r78-fbb643923e.zip`, under
`AMGT_DEPLOYED_ZIP=C:/tmp/ba20-r77-14a36147bd.zip`, `PIP_NO_INDEX=1`,
`PIP_FIND_LINKS=C:/tmp/bb18-wheels`, `PIP_LOG=C:/tmp/bb18-pip.log`. No variable was unset to get past
anything. The script's own lines: `DEPLOYED: live CodeSha256 MkM9Kf37...` (it reads the live hash itself,
every run), `OK: 147 file(s) copied` out of the deployed zip, `CLOSURE: 114 entr(ies) at the fixed point
after 5 pass(es) -- 41 seeded, 73 added by closure`, 18 data members,
`VENDORED-FROM-DEPLOYED: 147 file(s) -- pyarrow/ 132, pyarrow-16.1.0.dist-info/ 6, rpds/ 4,
rpds_py-2026.6.3.dist-info/ 5`, `SIZE: package 133718098 B unzipped over 388 entries + layer 121743633 B
= 255461731 B against the 262144000-byte ceiling (97.5% used, 6682269 B spare)`, `zipped: ... 42001525
bytes 388 entries (114 code, 18 data, 256 vendored)`, `VERIFY: 104 module(s) required, 104 packaged,
missing []` with `VERIFY-SCOPE` empty at module AND function scope, `VERIFY-DATA: 18 of 18 ... 8 of 8 ...
native extension ['rpds/rpds.cpython-311-x86_64-linux-gnu.so']`, and `ISOLATED: OK ... 3 of 3 arms`.
`collector_record.py` appears in neither the closure nor the diff, which the half makes a STOP if present.

**bb-23's edited Python block had never run before this build.** It ran clean on its first real exercise.

**L2 -- the three pre-upload gates.**
1. `r78_bb23.py --compare-zip`: `PASS Z1 the four folders ... equal the deployed zip's byte for byte 147
   of 147 equal; mismatched 0, missing 0, extra 0 []` -> `R78 BB23 COMPARE-ZIP EQUAL: YES`, exit 0.
2. The build's own `CONTENT-DIFF SUMMARY: files 388, IDENTICAL 358, CHANGED 22, ADDED 8, REMOVED 0,
   against MkM9Kf37...` -- exactly ADDENDUM 2's expectation. Matched **by identity, not by count**: the 22
   CHANGED lines were read by name and are the half's 19 repo files plus precisely the three
   `dist-info/RECORD` paths the addendum names, with no fourth vendored line; the 8 ADDED are one-for-one
   the half's 8 round-78 cells; REMOVED 0. A count-only read would have been strictly weaker here, because
   the addendum had just widened the expected total from 19 to 22.
3. The three RECORD files proven sorted-line equal to the deployed zip's: 43 and 43 lines, 19 and 19, 5
   and 5 -- the counts the addendum predicted -- `SORTED-LINES-EQUAL True` 3 of 3, each `bytes_equal
   False`, which is what put them on the CHANGED list. Negative control: `jsonschema/__init__.py`, a
   vendored file outside the three, reads `bytes_equal True`.

**C3, the no-fetch term, measured on the PIP_LOG with a positive control.** 0 hits each for `Starting new
HTTPS connection`, `Starting new HTTP connection`, `files.pythonhosted.org`, `GET /simple`, `Downloading
http` and `urllib3`; positive controls `Ignoring indexes` 2 and `Local files found` 6, which prove the
file parsed. Both pip steps resolved from `C:/tmp/bb18-wheels` and each ends in a `Successfully
downloaded` line. The 6 wheels were hashed before the build: 6 of 6 equal to
`round78/BB18_WHEEL_FOLDER_SHA256_20261008.txt`.

**L3 -- the upload.** The module's own `upload_verified` on **the kept zip**, not a rebuild:
`s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip` VersionId
`5EzlvQKaRhlENyrD6osK7pRdpfUkDTxi`, content-sha256 `+s6R0/rcpQ6...`, ContentLength 42,001,525, read back
and matching on both fields. The prior version `VHwcuot4i70V2evVL44EBgQc0BcAtScd` is still stored.

**L4 -- one plan, one apply.** `terraform plan` with **no `-target`**: one address,
`module.scoped_amgt_api.aws_lambda_function.this`, `will be updated in-place`, moving exactly
`last_modified`, `s3_object_version` and `source_code_hash`, with 28 unchanged attributes and 4 unchanged
blocks hidden; `Plan: 0 to add, 1 to change, 0 to destroy`. No other resource carries a `~`. The harvest
root is byte-identical between the pin and shared HEAD and its working tree was clean, so that plan is the
pin's configuration. `.tools/safe-apply.sh -chdir=infra/aws/terraform/harvest apply` (Rule 18, never bare
`terraform apply`): `Apply complete! Resources: 0 added, 1 changed, 0 destroyed.`

**L5 -- the snapshot event.** ONE invoke with exactly
`{"amgt_scheduled_action": "refresh_freshness_snapshot"}`: StatusCode 200, FunctionError null, stamp
`generated_at 2026-10-08T07:23Z, rows 302, etag "1a6f6d51e1ca72658249989dc500e074"`. The producer's
self-report was JOINED to the object: before VersionId `GyD7kjRk9hcHp4npg3vtTFiEOpz8QHGL` 3,894,841 B,
after VersionId `aF3aeCvDoQOXbiA.yB_fQNgf5Jm5F5Z2` 4,418,656 B at 07:24:00Z -- a new version at the **same
key**, which is the half's NEVER-1 read on `lib.opal_naming.address()` holding under a changed
`opal_naming.py`.

**Also run, reported and NOT graded.** `leadpanel_cold_warm.py --label after` at 07:22:10Z, 3 minutes
after the apply and before the snapshot event: 9 routes, every status `[200]`, 6 cold invokes at 3,521 to
4,434 ms on chatter days=30 and warm 511 to 699 ms across the three windows. The cold `AMGT_PHASE` lines,
read from CloudWatch over a window **computed** from the apply timestamp rather than typed: generation
read 687 to 1,109 ms, mentions decode 18 to 113 ms, compute 1,056 to 1,089 ms, names 0 to 1 ms,
classification 6 to 10 ms.

**L6 -- the criteria, run TWICE and agreeing.** Once in a wrapper shape (07:25:34Z to 07:32:15Z), then
again as the order's **literal `<invocation>` strings** (07:33:33Z to 07:40:13Z), the second being the
record's evidence because the proof instance's recorded invocation has to be the order's own string.

```
AC1  R78 DEPLOYED: YES 3 of 3                                    exit=0
       line 1  r78_bb17.py --crit AC1 --where deployed  PASS  H6 rows read 60, wrong 0 []
       line 2  r78_bb5.py  --crit AC1 --where deployed  PASS  R78 BB5 AC1 READ: YES
       line 3  r78_bb6.py  --crit AC1 --where deployed  PASS  R78 BB6 AC1 READ: YES
AC2  R76 C62 SERVED: YES | R76 C63 SERVED: YES | R75 C59 SERVED: YES        exit=0
       c59: snapshot generated_at 07:23Z, rows EQUAL 302 of 302; burst of 40 -> 13 cold,
            all 200 and inside the 2000 ms bar (819..1158); after 65 s idle 1983 ms
AC3  R77 SERVED SHAPE: YES, C1..C6 all PASS                      exit=0
       page view 200, 66,341 B, 95 rows, 3 stale; plain /freshness still 302 rows
AC4  R78 BB23 AC1 SERVED: YES  (LEG 0, 2026-10-07, not re-run -- see below)  exit=0
AC5  R78 BB23 AC2 SERVED: YES  (LEG 0)                                       exit=0
AC6  R78 BB23 AC3 SERVED: YES  (LEG 0)                                       exit=0
```

**AC1's line 1 is the round's discriminating read**: it read NO, 0 of 6 clauses against the base, with H6
at 2 wrong of 60 peer rows, and reads YES, 6 of 6 now, H6 at 0 wrong of 60. **No criterion read NO, so the
rollback was named and NOT taken.**

**AC4 to AC6 were not re-run after the apply, by the GO's own words** -- "the helper will refuse the old
zip, which is the ruling working". That refusal was **exercised rather than assumed**: handed
`ba20-r77-14a36147bd.zip` against the NEW live hash the helper exits **rc=1**, `ERROR: sha256 mismatch ...
nothing was copied`, and creates no dest folder; the positive control, the new kept zip against the same
hash, exits **rc=0** and copies 147 files. So the ruling holds and `bb18-r78-fbb643923e.zip` is round 79's
`AMGT_DEPLOYED_ZIP`. **Both zips are kept on disk**, per COO half term 6.

Proof instance:
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-bb-18.the-code-redeploy.proof_of_spec.json`
-- `proof-of-spec-check` with the governing order bound reads **VALID (rc=0)**: coverage AC1 to AC6,
invocation-alignment **6 of 6 matching, 0 diverging**, DEPLOY GENRE limb satisfied with **10 of 10 named
controls discriminating** and the rollback named, surprises 1 entry resolving to a channel row.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-tool PATH rail | `org/XXX.md` A.3 census + forwarder exercise | PASS | 104 of 104 resolve bare; the `comp-which` forwarder RAN |
| comp-blast | `comp-blast opal-amgt-scoped-api` | PASS, with a vintage caveat | 3 DynamoDB tables, 7 IAM policies, 3 roles, 1 KMS key, 2 Lambdas, 2 layers, 3 buckets; 24 of 24 traversal. **The served graph was built 06:15:41Z, BEFORE this apply** -- sound here only because 0 `.tf` files differ between the round-77 build commit and the pin, so no edge moved. It would NOT be sound for an act that changed a route or a grant. This closes the gap LEG 0's log deferred to leg 1. |
| comp-find | `--name 'leadpanel_cold_warm.py' --limit 20`; `'NOT YET UPLOADED' <channel> --limit 10` | PASS | The second is the denominator behind row S370: **0 hits across 119 files** scanned in the channel, a MEASURED zero, which is why S370 is a new row and not a duplicate |
| deploy_ledger.py | `open` (6 legs) -> `close-leg` L1..L6 -> `close` | PASS | Opened before the build, committed the same turn, CLOSED 20261008T075402Z, sentinel removed |
| proof-of-spec-check | `<instance> AC1..AC6 --governing-order <order>` | **VALID rc=0** | First run was INVALID with 4 named schema defects (an `acceptance.cell_refs` key the schema forbids, two `artifacts_produced.kind` values outside the enum, and a `surprises` entry written as an object where the schema wants a row-id-prefixed string). Fixed and re-run. |
| commit-gate | ridden by `safe-commit.sh` | **NOT EVIDENCE OF A PASS** | On the ledger-open commit it printed `checked 0 of 2 file(s) -- NOTHING WAS CHECKED` and the risk reflex read `NOT-DECIDABLE: danger map STALE ... could not check is NOT checked clean`. Recorded as what it is: that commit held a `.json` sentinel and a `.md` ledger, neither in the gate's graded set. An absence of coverage, not a clean gate. |
| naming-gate / to-pipeline-gate / surprise-row-gate | ridden by `safe-commit.sh` | PASS | naming-gate 0 graded over a domain of 0 paths; to-pipeline-gate OK no `task_orders/*.md`; surprise-row-gate graded the appended row |
| audit-archive-invoker | `python .tools/audit-archive-invoker.py` | WARN | 13 findings, all pre-existing owned classes; not re-filed per `org/XXX.md` |

**What worked.** Reading both halves whole (537 + 137 lines) before touching anything, and then
**extracting each criterion's `invocation` and `expect` out of the order programmatically** instead of
retyping them. The invocation-alignment limb compares the recorded string against the order's byte for
byte modulo declared placeholders; a retyped flag or path would have been an INVALID with nothing wrong
with the work. It read 6 of 6 first try.

**What failed, and was caught.** Three wrong-object reads, each re-measured rather than reported:

1. **`git worktree list --porcelain | awk '{print $2}'` silently dropped 5 of 76 worktrees** -- exactly
   the ones whose path contains `Opal Bloomberg`. It reported "answered 72, errored 5" with a real-looking
   denominator. Re-parsed with `sed -n 's/^worktree //p'`: 76 of 76 answered, 0 errors, 68 distinct entry
   files. A space in the workspace path is a banked site-Z trap and it still caught me.
2. **A `grep -c` over a pattern including `https://pypi` returned 2 against the pip log** -- and those two
   hits were pip's `Ignoring indexes: https://pypi.org/simple` lines, which it writes precisely when it is
   NOT using the index. Reporting 2 as the request count would have inverted the finding. Re-measured with
   six request-shaped predicates and two positive controls.
3. **`helper ... | head -3; echo "rc=$?"` printed `rc=0` for a helper that had exited 1** -- the value
   belonged to `head`. Re-measured without a pipe: rc=1 on the refusal, rc=0 on the positive control.

Two rail denials: a bare `find`, and a `comp-find` piped into `tail`. Each was re-run as the rail directs
rather than overridden. The first also confirms the banked lesson that a denial aborts the whole Bash call.

**Gap named, not papered over.** The size line reads 255,461,731 B / 97.5% against the COO half's INFERRED
255,458,488 B / 97.4% -- 3,243 B apart. The half labelled its figure INFERRED and the build's own
accounting is the measured one, so there is no contradiction to resolve; but round 79 has under 6.7 MB of
unzipped headroom and the build stops itself over the ceiling. Surfaced in the proof's forward notes.

## Surprise rows

**ONE filed: `AMGT_RESAPP-Z-S370`** (OBSERVATION, hazard **INERT**, `disarm_owner` `2.0.0_SA_COO~Z`,
`surfaced_at` 2026-10-08T07:40:54Z). The Lambda source map's entry for this function still carries
`_artifact_note: "NOT YET UPLOADED. No artifact exists at the key above and no terraform apply has been
run"`, while the artifact has now been uploaded and applied twice -- round 77 and this act. Both clauses
are false of the world and have been since round 77 closed at `0fabcf4f0f`.

**Filed, NOT fixed:** `infra/aws/lambda/ci/lambda-source-map.json` is outside this order's `<paths>`, so
owned-paths would refuse the edit. INERT because nothing machine-reads that field -- the entry's six
machine-read keys are correct, `comp-iam` reads `source` and the deploy workflow reads `source_dir`. The
cost is to a human asking whether this function has ever been deployed and being told no. Found while
checking Deployment Rule 4 (every Lambda carries an entry), which it does.

**One row is NOT mine to move, and is surfaced rather than adjudicated.** `AMGT_RESAPP-Z-S368` is ARMED
with `disarm_owner` `2.0.0_SA_COO~Z` and its own notes say "ARMED until the round-78 redeploy (order
AMGT-bb-18, legs 1-2) carries bb-8 and bb-17 ... its deployed list carries `r78_bb17.py --crit AC1 --where
deployed`, whose H6 then reads 0 wrong." **That condition is now met**: H6 reads `rows read 60, wrong 0 []`
on the deployed function. The evidence is in AC1's output; the disposition is the owner's act.

## MCP traffic

4 messages. Inbound 0 new -- `get_delivery_state` read 30 of 30 rows READ with an ACKABLE DENOMINATOR of
30 of 30, and both the lane inbox and the base inbox read empty, so nothing was owed on arrival. The GO
itself came on the order file, not through the broker, which is why an empty inbox was not an idle
session. Outbound 1: the completion report to `2.0.0_SA_COO~Z`. The CTO was not copied -- Rule 31 reserves
that for decisions, and this is a report. 3 heartbeats with the summary moved as the act moved.

## Files Modified

| File | Change |
|---|---|
| `org/critical_paths/change_management/20261008T0702Z_amgt-resapp-r78-bb18_deploy_completion.md` | NEW then CLOSED: the NEVER-2 entry, 6 legs each carrying its proof |
| `org/critical_paths/.open_deploys/amgt-resapp-r78-bb18.json` | NEW then REMOVED by the close (the sentinel) |
| `.../deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-bb-18.the-code-redeploy.proof_of_spec.json` | NEW, VALID |
| `.../deliverables/0.7.0_AE_CloudOps~A/round78-bb18/` | NEW: the build log, the PIP_LOG C3 asks be attached, the plan, the apply, the 0-diff re-plan, the leadpanel read and both criteria runs |
| `.../surprise-channel/investigations/INVESTIGATION_v1.md` | +24 lines, 0 deletions: row S370 appended. Shared append-only file, so committed in the shared tree per Rule 14b's inversion. 953 rows parse; the one non-ASCII character in the file is pre-existing at line 18, far from the new row |

**No source file changed.** This act builds, uploads and applies; it edits no `.py`, no `.tf`, nothing
under `lib/`.

## Blockers

**None. Nothing is owed by this seat on this order.**

## Next Steps

1. **[`2.0.0_SA_COO~Z`] The four hand reads the GO reserves** -- one invoke of the route behind
   `scoped_amgt.py:1567` with an as-of date in 2009 (CTO half C4), `/thesis` officers for
   `BP/_LN_Equity`, and `/resolve?q=apple` and `?q=microsoft` (C5). The function is live and serving;
   these are not this seat's.
2. **[`2.0.0_SA_COO~Z`] Dispose `AMGT_RESAPP-Z-S368`** -- its disarm condition is met, evidence in AC1.
   And flip the order's `<status>`; that is the issuer's act, as it was for ba-20 and az-5.
3. **[`2.0.0_SA_COO~Z`] Row `S370`** -- a one-line edit of the source map's `_artifact_note` by a seat
   holding `infra/aws/lambda/`. INERT, so it gates nothing.
4. **[`1.0.0_SA_CTO~Z`] CTO half C1 now binds**: the live code is BEHIND CLOUD HEAD on the 5 packaged
   files the trunk merge `f6cff376d1` moved, two of them off this half's CHANGED list. The next
   redeploy's half measures them. Also C4's dated item -- on 2028-01-01 the trading-calendar frontier
   leaves its own fallback range and every staleness read on this function raises; this act put the
   raising copy into production, so that clock is now running on live code.
5. **[`3.0.0_SA_CVO~Z` / `2.0.0_SA_COO~X`] `amgt-corpus-r40-ap10d` stays OPEN** across this act by the
   COO half's own words -- its Lv leg reads the live route AFTER this deploy, and the page has now moved
   to method 7. Not this executor's to close.
