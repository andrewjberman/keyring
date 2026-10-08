# AMGT_RESAPP round 79 -- TO-AMGT-cc-7 AMENDMENT 1: four legs, the grant first in its own apply

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

Serial: `0.7.0_AE_CloudOps~A` | Window: 2026-10-08 15:0xZ -> 20:3xZ (respawn by `2.0.0_SA_COO~Z` after the
prior session ended; prior log `round78_bb18_legs1_2_code_redeploy.md`) | Order:
`org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-cc-7.the-code-redeploy.md` @3e33994566
| Issuer: `2.0.0_SA_COO~Z` | risk WORLD, proof_genre DEPLOY | Cell `AMGT-cc-7`

---

## Current State

**The GRANT-FIRST redeploy LANDED on all four legs and every criterion reads YES. The NEVER-2 entry
`amgt-resapp-r79-cc7` is CLOSED, 4 of 4 legs proven, nothing stranded.**

`opal-amgt-scoped-api` now runs CodeSha256 `ltXvElwZ4iyRx6bJLDQRWksbDoiTesc8xvu1h+p3QI0=` (base
`+s6R0/rcpQ6lJgYsX2JtxfgoFoCmiaozTtMreyyymTQ=`), CodeSize 42,015,430, MemorySize **1769 unchanged**,
Timeout 29, python3.11, layer `opal-amgt-print-deps:1` unchanged, LastModified 2026-10-08T17:35:08Z. The
live hash EQUALS the kept zip's own sha256, so the bytes that were gated are the bytes that run, and it
DIFFERS from the base, so this was not a 0-diff deploy. Both 0-diff re-plans read `No changes. Your
infrastructure matches the configuration.`

The three named hookups now reach the routes: `/thesis` carries `segment_table` and `dossier_sections`,
and every `/freshness` row carries `seeking_alpha`.

**Push state, MEASURED at 20:2xZ:** LOCAL. Commit `42700562a4` sits on branch `box/sitez`, which
`0.0.0_AB_MSTR~Z` created from HEAD at 19:49:34Z and pushes to origin; `origin/box/sitez` reads
`91f5c90ec2` by `git ls-remote`, which does NOT contain `42700562a4`. Per that seat's own note the branch
"reaches CLOUD at the laptop's next integrator pass." This seat does not push shared branches.

## The pin, and why equality was the control

**THE PIN: `63f0605039e3a95eae1868b8d4917fef40052447`**, built from the DETACHED worktree
`C:/tmp/cc7-build` whose `rev-parse HEAD` reads that hash exactly, whose `symbolic-ref -q HEAD` is empty
(rc 1), and whose `git status --porcelain` is EMPTY -- re-read after `terraform init`, so the init added no
tracked dirt. The order forbids "at or after", and that is not pedantry here: **the shared tree moved at
least four times during this act** (HEAD read `dd784216c9`, `3bb6d192e0`, `d5840c9e52`, `4ddbb4e371` at
different minutes) while `0.0.0_AB_MSTR~Z` merged and nine other seats committed. A pin defended by
`merge-base --is-ancestor` is satisfied by every descendant and would have admitted any of them. Negative
control: HEAD is not an ancestor of the pin (rc 1) while the pin is an ancestor of HEAD (rc 0).

## The call-11 reading was re-measured, and the GO's sentence had already aged

The GO states call 11 as a FILE LIST: "against the pin only `lib/opal_naming.py` (+12, the census) and
`exemptions.json` differ", read at HEAD `2d0d4296bf`. By the time this seat read the tree HEAD was
`d5840c9e52` and **thirteen** paths differed from the pin across the criteria's import surface.

The denominator that the pair's term is actually about is the PACKAGED set, so each changed path was tested
for membership against the live package's own 388 arcnames. **Exactly two are packaged** --
`lib/opal_naming.py` and `infra/logic/registry/exemptions.json` -- precisely the two the GO names. The
discriminator the pair names was then read directly rather than assumed: the `opal_naming.py` diff is
+12/-0 and touches no line of `address()`, `key()` or `lookup()`.

The one worth naming is `lib/opal_data_harvest/config.json`, whose `universe_source` and
`symbol_resolution_source` AMGT_HARVST had just repointed to the 20261008 files. That WOULD matter to a
view built on the tree -- and it is **not packaged at all**, so it cannot move what the function builds.
So the GO's conclusion held on the population it is about; only the sentence carrying it had expired.
Filed as row `AMGT_RESAPP-Z-S375`.

**The criteria ran in a FROZEN worktree, and deliberately NOT at the pin.** `C:/tmp/cc7-rec` on branch
`ae-cc7-r79` at `d5840c9e52`. The pair's call-11 fallback says that if the landed diff is anything other
than the staged one, "c59 and the other criteria are run from a tree at the pin." That fallback was
measured and NOT taken, because it would have been worse: the issuer's `r77_served_shape.py` amendment and
the filled `r79_deployed_cells.txt` are both POST-pin commits, so a tree at the pin would have read the
UNAMENDED C5 and `NO CELLS LISTED` exit 2 -- two failures that are artefacts of the pin rather than of the
deploy. The frozen tree carries both post-pin commits and its packaged diff against the pin is the two
blessed files.

## Deployment Sequence + Verification

ONE NEVER-2 entry, opened BEFORE any build, upload or apply and committed in the same turn with both
required paths (`@626484176d`, while the tree was still on `CLOUD`), so the OPEN state lived in git and not
only on this device. Four legs, as AMENDMENT 1 orders them.

**L1 -- the grant, in its OWN apply, before any build or upload.** Policy saved whole BEFORE: sha256 over
sorted-keys compact JSON `6270e453...`, EQUAL to the COO half's figure; 7 statements, 33 object-read
resources, 33 list prefixes, `job_record` 0 in both limbs. Eight arms BEFORE at 16:04:15Z. Plan UNTARGETED
from the pin worktree: ONE change marker, `aws_iam_role_policy.scoped_amgt_api_grants will be updated
in-place`, `Plan: 0 to add, 1 to change, 0 to destroy`; the body gains one resource and one `s3:prefix`
value with 32 unchanged elements hidden in each; the function did not appear. `safe-apply` of THAT saved
plan file: `Apply complete! Resources: 0 added, 1 changed, 0 destroyed.`

AFTER: sha256 `77c69f83597649427ce979e1b4dd9084bde2fcd820bf0e014c3651a8ac9f0857` -- **equal to the digest
the half INFERRED from the pin's `.tf` text before any apply ran.** Prediction and world agree to the byte.
34 and 34; ADDED exactly `arn:aws:s3:::opal-data-harvest/seeking-alpha/harvest/state/job_record/*` and
`seeking-alpha/harvest/state/job_record/*`; REMOVED none; the first 33 of each limb byte-equal AND in
order; the five other statements byte-equal; the tier root `seeking-alpha/harvest/state/` absent from both
limbs; attached policies unchanged.

**The eight arms are what actually graded the grant, because the policy text cannot tell a TABLE grant from
a TIER grant** -- both would show an added line and both would read 34 and 34.

| arm | BEFORE 16:04:15Z | AFTER 16:50:02Z |
|---|---|---|
| C0 GetObject under `bronze/` | allowed | allowed |
| C1 ListBucket prefix `bronze/` | allowed | allowed |
| P1 GetObject under `job_record/` | implicitDeny | **allowed** |
| P2 ListBucket prefix `job_record/` | implicitDeny | **allowed** |
| N1 GetObject under sibling `filing_attempt/` | implicitDeny | implicitDeny |
| N2 ListBucket prefix `state/` (the tier root) | implicitDeny | implicitDeny |
| N3 ListBucket prefix `filing_attempt/` | implicitDeny | implicitDeny |
| N4 PutObject + DeleteObject under `job_record/` | implicitDeny x2 | implicitDeny x2 |

The pair discriminated: the two positive arms MOVED and the four negative arms DID NOT. 0-diff re-plan
after the leg.

**L2 -- the build, no apply.** Gate `gen_harvest_prefixes.py --check` run standalone at the pin first:
`OK: ... matches fresh lib.opal_naming output byte for byte (registry hash fff9a273...)`, exit 0, exactly
the half's prediction; the script ran it again itself. `--build-only C:/tmp/cc7-r79-63f0605039.zip` under
`AMGT_DEPLOYED_ZIP=C:/tmp/bb18-r78-fbb643923e.zip`, `PIP_NO_INDEX=1`,
`PIP_FIND_LINKS=C:/tmp/bb18-wheels` (6 of 6 wheel sha256 equal to
`round78/BB18_WHEEL_FOLDER_SHA256_20261008.txt`), `PIP_LOG=C:/tmp/cc7-pip.log`. **No variable was unset to
get past anything.** The script read the live hash itself and matched, so `vendor_from_deployed.py` did not
stop the build.

Every figure the half had INFERRED came out right: `CLOSURE: 118 entr(ies) at the fixed point after 5
pass(es) -- 43 seeded, 75 added`; `SIZE: package 133771302 B over 392 entries + layer 121743633 B =
255514935 B against 262144000 (97.5%, 6629065 B spare)`; `CONTENT-DIFF SUMMARY: files 392, IDENTICAL 376,
CHANGED 12, ADDED 4, REMOVED 0`. `VERIFY: 110 of 110` packaged, `VERIFY-SCOPE` empty at module AND function
scope, `VERIFY-DATA 18 of 18` and `8 of 8`, `ISOLATED: OK ... 3 of 3 arms` with the fresh-venv boto3
negative control.

**The diff was matched BY NAME, not by count,** which is the trap round 78 recorded on this same artifact:
the CHANGED set and the ADDED set are SET-EQUAL to the half's two tables, 0 off the table and 0 on the
table absent, and 0 vendored paths appear on either list. `--compare-zip` read `PASS Z1 ... 147 of 147
equal; mismatched 0, missing 0, extra 0`, `R78 BB23 COMPARE-ZIP EQUAL: YES`, exit 0. All three named
hookups are in the built package with exactly one call site each, plus hookups 4 and 5 and wordings 6
and 7.

**L3 -- the code, in its OWN apply.** `upload_verified` on THAT kept file, not a rebuild: artifact
VersionId `5EzlvQKaRhlENyrD6osK7pRdpfUkDTxi` (the rollback key) to
`b1DslJVdUV3xG.4dZ6coig25byb2jPGG`, stored content-sha256 and ContentLength read back and matching. Plan
UNTARGETED: `module.scoped_amgt_api.aws_lambda_function.this` ALONE, moving exactly `last_modified`,
`s3_object_version` and `source_code_hash`, with 28 unchanged attributes and 4 unchanged blocks hidden --
so memory, timeout, runtime and environment did not move. **The IAM policy did not appear in this plan,
which is the grant-first shape landing as the CTO half ordered.** Apply: `0 added, 1 changed, 0 destroyed`.

**L4 -- the snapshot event, BRANCH A.** `head-object` immediately before the event recorded VersionId
`05UOLBhjOKcpe7DoqAM5mOvSDP1l0m5z` as THE rollback key (CTO C3). ONE invoke at 18:08:01Z with exactly
`{"amgt_scheduled_action": "refresh_freshness_snapshot"}` from a 55-byte payload file: StatusCode 200,
FunctionError None, `generated_at 2026-10-08T18:08Z, rows 302, etag "83e20b6a3649af84af3669d28716fa26"`.

The producer's self-report was JOINED to the object rather than trusted: AFTER VersionId
`ar7KPWgPpUdMxUmrhTScvJdcnr9leBAB`, 1,085,581 B, 18:08:10Z, ETag equal to the reported etag -- a new
version at the SAME key, which is also the half's NEVER-1 read on `lib.opal_naming.address()` holding under
a changed `opal_naming.py`. The object shrank from 4,758,475 B to 1,085,581 B; the half said "about
1,063,343 B", 2.1 percent under. No second event was sent; COO call 3 was never reached.

**CTO C1 is answered: the one view build INSIDE the function took 5,192.36 ms** (billed 5,193 ms, Max
Memory Used 300 MB of 1,769 MB), read from the event's own REPORT line. That is FASTER than both of the
half's box-local figures (6.8 s and 9.9 s) and well inside the 29-second ceiling, which is the number the
CTO wanted before tomorrow's Friday read.

## The criteria

| criterion | verdict | the line that matters |
|---|---|---|
| AC1 18:19:30Z | PASS | `R79 DEPLOYED: YES 1 of 1`, exit 0; the list holds exactly 1 non-comment line as the GO states |
| AC2 18:22:40Z | PASS | `R76 C62 SERVED: YES`, `R76 C63 SERVED: YES`, `R75 C59 SERVED: YES` |
| AC3 18:29:04Z | PASS | `R78 DEPLOYED: YES 3 of 3`, `R77 SERVED SHAPE: YES` |

**AC1 carries the world-side positive arm no simulation can give.** The half states plainly that the
negative arm has no arm in the world and that the function's own read of the job records had never run.
K1 reads `record read finished True, objects listed 122` -- at or above the half's 112-or-more bar, on a
read being exercised for the first time. The stamp COO call 6 asks for reads `view made 2026-10-08T18:08Z`,
the NEW one, so the 60-second hold had expired and no second wait was needed. Seeking Alpha states over the
95 covered rows: `{read 13, checked 15, no_record 67, unreadable 0}`, summing to 95, near the half's
`{read 12, checked 13, no_record 70}` and moved by the collector running in between, as predicted.

**AC2's c59 was the one at risk and it came out clean.** Its C1 compares all 302 served rows against a view
computed on this box, and the half had measured it at NO, 0 of 302, before the act, calling it a race
against two stores that move on their own. Run within minutes of the event with nothing else on the box, it
reads **302 of 302 EQUAL** -- so the carve-out the pair wrote for a partial difference was never reached and
nothing is held for the issuer. C2: 23 cold of 40, every one 693 to 979 ms inside the 2,000 ms bar. C3: 580
ms after the hold, against the half's 1,853 ms, consistent with the served body shrinking from ~4.7 MB to
1.09 MB.

**AC3 passed only because the issuer amended its own criterion first.** The half called this "the most
important finding of the half": `r77_served_shape.py` clause C5 found the segment block by WALKING the
`/thesis` body for the first object holding `rows`, `source` and `reason`, and the new `segment_table` key
holds all three and is added right after `segment_breakdown` -- so after a CORRECT deploy the walk would
return the wrong object and AC3 would exit 1. The issuer amended `_segments()` to read `segment_breakdown`
BY KEY (call 1, `@2e6bf9a906`). The amended check reads ASML NA 0 rows and BA 11 rows, the unregressed
by-key values, so the criterion graded the act and not the key order.

**Also run, reported and NOT graded.** `leadpanel_cold_warm.py --label after` at 17:43:11Z: 9 routes, every
status `[200]`, 6 cold 3,550 to 4,384 ms, warm 15 to 721 ms (round 78 read 3,521 to 4,434 ms cold, so the
one added module-scope import cost nothing measurable). The cold `AMGT_PHASE` table was built over a window
**computed** from the apply's LastModified and restricted to the 6 request ids whose REPORT line carries an
`Init Duration` -- not inferred from the per-phase maximum. That cold count of 6 reconciles with the cold n
the leadpanel script reported independently. chatter: generation read 745-1,092 ms, mentions decode 12-166
ms, compute 200-1,379 ms, names 0-1 ms, classification 6-8 ms, serialize 2-3 ms.

## The source map

`infra/aws/lambda/ci/lambda-source-map.json`, `functions.opal-amgt-scoped-api._artifact_note` read "NOT YET
UPLOADED. No artifact exists at the key above and no terraform apply has been run" -- false since many
deploys ago, recorded as row `AMGT_RESAPP-Z-S370`. Replaced with the COO half's text, **carrying no hash**,
because a stale value in a note is how that row arose. The file round-trips byte-identical at `indent=2`
with no CRLF and no non-ASCII, so the edit is a 2/2 diff of exactly the two intended fields. The same
entry's `_note` still says the function serves "the eleven" routes where the handler's docstring says
sixteen and the apply output listed 19 route keys; the half places that second stale figure outside this
order's sentence, so it was NOT changed.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-which` | `comp-which "how do I open a NEVER-2 open_deploys ledger entry for a deploy"` | **NO CURATED RULE MATCHED** -- every candidate scored below the vetted band and the tool said so instead of routing. Taken at its word rather than picking the top-ranked guess; resolved by reading `.tools/deploy_ledger.py --help` and the round-78 entry's bytes out of git. |
| `comp-find` | `comp-find 'open_deploys' --name --limit 25` | 6 hits across 194,856 files, `corpus=all`, 232,461 on the printed ephemeral floor and not searched; no ledger opener among them. A first attempt piped to `head` and the rail hook REFUSED it, correctly -- a census piped into a receiver can erase its denominator. Re-run with the tool's own `--limit`. |
| `comp-find` | `comp-find 'box/sitez' --limit 12` | 5 hits, bands SURFACED=2 DOC=3. This is what established that `box/sitez` is deliberate: the author-override audit log holds `MERGE-ATTEMPT 0.0.0_AB_MSTR~Z ... origin/CLOUD into box/sitez, on Andrew['s word]`, and a message to the CRO states the push and that it "reaches CLOUD at the laptop's next integrator pass." |
| `comp-blast` | `comp-blast opal-amgt-scoped-api` | AE role minimum on an infra change. Radius: 3 DynamoDB tables and 7 IAM policies, including the one this act edits. **Recorded as what it is, not as a pass:** its graph vintage is 2026-10-08T12:54:23Z, which PREDATES both applies, so it describes the pre-act estate. Sound here ONLY because the act added one read-only prefix INSIDE an existing policy and created no node or edge; it would not be sound for an act adding a route, trigger or new grantee. |
| `comp-lambdamap parity` | `comp-lambdamap parity` | MATCH 166, STALE-RECORD 6, POSSIBLE-HALF-LANDED 4, NOT-LIVE 4, UNVERIFIABLE 7, **NO-RECORD 41**. No printed row names this function, and the reason is a finding rather than a clean bill: its source-map entry carries neither `last_deployed_commit` nor `artifact_sha256`, so the tool has no record leg and cannot grade the deploy either way. The 3-leg parity was proven by hand instead. Filed as row `AMGT_RESAPP-Z-S374`. |
| `proof-of-spec-check` | `python .tools/proof-of-spec-check.py <instance>` | First run **INVALID (rc=1)** with five precise violations: an invalid `kind` enum (`iam_policy`), `artifact_covered_by` naming prose instead of criterion ids, an ARN declared where a (commit, path) pair is resolvable, and AC2/AC3 recording ABBREVIATED invocations (`org/.../round76/...`) instead of the order's verbatim text. All five fixed; second run **VALID (rc=0)** with 13 of 13 named controls discriminating, 3/3 invocations aligned, 2 surprise rows resolving, rollback named. |
| `commit-gate` (via `safe-commit.sh`) | `bash .tools/safe-commit.sh --author ... -F <msgfile> -- <paths>` | On the ledger-open commit: `WARN: commit-gate checked 0 of 2 file(s) -- NOTHING WAS CHECKED`, because that commit carried only `.json` and `.md`. Recorded as an ABSENCE OF COVERAGE, not a clean gate. The pre-commit risk reflex on the same commit read `ANSWER STATE: PARTIAL_OR_BLIND / NOT-DECIDABLE: danger map STALE` (184.7 h old) -- also not a pass. On the close-out commit the surprise-row gate graded 2 new rows of 961 (959 pre-existing, not re-graded) and the surprise corpus matched its exact legacy baseline, 4 known 0 new. |
| `deploy_ledger.py` | `open` / `close-leg` x4 / `close` | Entry `amgt-resapp-r79-cc7` opened 16:14:09Z with 4 legs and CLOSED 19:59:41Z, all 4 legs proven, sentinel removed. |

## What failed, or was nearly wrong

1. **The GO's call-11 sentence was already false when read.** Had it been carried forward unverified, the
   criteria would have run against a tree whose relationship to the pin was unmeasured. Had the wider
   13-file diff instead been read as a call-11 FAILURE, the act would have stopped when the pair's own term
   still held. Only the packaged-denominator test separated those two wrong answers from the right one.
2. **The pair's own fallback would have broken AC1 and AC3.** "Run the criteria from a tree at the pin"
   sounds strictly safer and is not: the amended check and the filled cells file are post-pin commits.
   Reading what the fallback would actually produce, rather than taking it as the cautious option, is what
   avoided two self-inflicted failures.
3. **The first proof-of-spec instance was INVALID**, including two criteria whose recorded invocations were
   path-abbreviated. The checker's own words are the lesson: a record that does not carry the order's
   verbatim invocation "leaves the record ungoverned." Caught by running the checker rather than assuming
   the instance was well-formed because it was carefully written.
4. **Two surprise rows were drafted against ids that were already taken** (`Z-S372` exists; `Z-S373` is the
   CVO's, filed at 09:26Z). A census of the channel gave the true maximum, 373, and the rows went to 374
   and 375. Appending at a guessed id would have collided with another seat's row.
5. **A non-ASCII character in the channel was nearly mis-attributed.** The file reads 1 non-ASCII character
   after the append. A positive control -- reading the same file at HEAD -- showed the count was already 1
   before the edit, so the `U+26D4` is pre-existing and the two new rows are pure ASCII. The read and write
   were both explicit `encoding='utf-8'`, which is the safe move CLAUDE.md names for a file that already
   carries non-ASCII.
6. **The branch under the tree changed mid-act.** The ledger-open commit reports `[CLOUD 626484176d]` and
   the close-out reports `[box/sitez 42700562a4]`. Measured rather than assumed: `box/sitez` was created by
   `0.0.0_AB_MSTR~Z` from HEAD at 19:49:34Z, carries nine other seats' commits, and is pushed to origin by
   that seat. So the commit is on the right branch -- but the push state in the report names the BRANCH, not
   just "LOCAL", because `origin/box/sitez` does not contain it.

## Next Steps

1. **[`2.0.0_SA_COO~Z`]** The order's `<status>` flip, and the two filed rows (`Z-S374`, `Z-S375`) to weigh
   at the round-79 analysis. A next GO that states call 11 as a DENOMINATOR rather than a file list would
   not need re-deriving by the executor.
2. **[`2.0.0_SA_COO~Z`]** CTO C1's remaining limb: read tomorrow's 12:30Z scheduled write the same hour. It
   is the last write before the weekend; if it writes nothing, ONE by-hand event that hour, and if that also
   writes nothing, roll the code back WITH the snapshot before 2026-10-09T20:00Z. This act's contribution to
   that call is the 5,192.36 ms figure.
3. **[`2.0.0_SA_COO~Z`]** COO call 8's round-80 surprise row (one failed record body refuses the whole
   snapshot, no retry) is the issuer's to file. From the world: this deploy's first exercise listed 122
   objects and failed 0 bodies, so the hazard is real but did not fire.
4. **[`1.0.0_SA_CTO~Z`]** CTO C2: stating to Andrew what the reader sees until the page cell lands. The half
   assigns it to that seat in its own words; not relayed here.
5. **[whoever owns the source map]** Row `Z-S374`: populating `last_deployed_commit` and `artifact_sha256`
   for this entry would put the function back inside `comp-lambdamap parity`'s reach. Not this cell's write
   surface.
