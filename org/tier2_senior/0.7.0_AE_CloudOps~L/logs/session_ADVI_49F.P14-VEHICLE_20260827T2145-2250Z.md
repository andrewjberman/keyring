# Session log -- 0.7.0_AE_CloudOps~L -- ADVI_49F.P14-VEHICLE -- 2026-08-27T21:45Z..22:50Z

**Archetype:** RESPAWN + BUILD. Predecessor died ~20:52Z after the mint-restored report; this seat
re-instantiated from the durable artifacts (face, ledger design, pinned predicate) exactly as that
design intended, and re-derived rather than inherited every load-bearing figure.

**State at close:** V14-3 unlock 3/3 CLEAR (re-verified at the faces myself). Vehicle live at
DocumentVersion 3. **The campaign VEHICLE now exists as artifacts** (driver + ledger + verifier),
where it was previously a design paragraph. **Campaign NOT started** -- 2 of 3 campaign-start inputs
read `pending` at their faces. Host STOPPED. Zero crons.

---

## 1. Startup

`/watcher`: not registered (genuine fresh session, predecessor dead). **No orphan for this serial** --
the `ps` sweep found 9 live watchers, none for `0.7.0_AE_CloudOps~L`, so the PID-identity
discriminator resolved cleanly to "genuine orphan absent, arm fresh". Registered (pid 22168), armed
the persistent Monitor `bb2zd75z8`, arm banner reads `parent-tied: pid 2801512` -- a REAL pid, so the
self-exit protection is live. 5 messages delivered and read; READ-clock ACKs recorded for 7 ids.
`/cloud-ops` once. No loop armed.

## 2. V14-3 unlock -- re-verified, not inherited

2.0.0_SA_COO 76811 supplied the gate state AND instructed "verify, never inherit, including from me".
Done, at the faces:

| leg | face | verdict |
|---|---|---|
| 1 | c01-SIGNFIELD | `complete` |
| 2 | c02-CFINPUT | `DEPLOYED-THROUGH-CF-4 @21170203c5` |
| 3 | P14-PRECOND | `complete` |

Leg 2 used the predecessor's pinned sound predicate @ba406fdf21 -- token + REAL hex hash, never the
bare phrase -- with the **positive control run as a SEPARATE invocation**, and `grep -o` so that a
LINE-level count could not pass for a TOKEN-level read (the placeholder `@<deploy-evidence-hash>` and
the real token sit on the SAME line, so `grep -c` alone conflates them). The naive arm returns 1 as
designed; that is why it is not the arm anyone acts on.

## 3. My named step (CTO 76738) -- PASS on DEPLOYED bytes

Subject: `s3://opal-data-49financial/_code/chain_49f_entrypoint.py` LastModified 22:08:00Z,
`a00_runner.py` 22:07:56Z -- the object the SSM document's `s3 sync` puts on the box.

| check | verdict | control |
|---|---|---|
| 1 a00-ONLY ARGV SCOPE | PASS -- 1 of 15 stages carries `dh`, and it is a00 | plant `dh` on a01 -> FIRED |
| 2 MIRROR MEMBERSHIP | PASS -- a00 argv `+ u + m + dh` (ruling (i)) | strip `m` -> FIRED |
| 3 NO AUTO-DERIVE | PASS -- 1 write, from the PARAMETER only | 2 controls FIRED |
| 4 ARGV SURFACE AGREE | PASS -- 5 of 5 options accepted by deployed a00 | bogus option -> FIRED |

**CHECK 4 exists because CHECK 2 created the hazard.** Once the entrypoint sends `--local-out` to
a00, a deployed a00 that did not accept it kills all 533 dates on ARGV rather than at the guard --
the class the face names as wearing a vehicle defect's face.

⛔ **CHECK 3 FIRST RETURNED FAIL AND THE DEFECT WAS MY PREDICATE.** A substring scan for
`epoch`/`converter` over the whole file hit 5 occurrences -- every one a COMMENT or ARGPARSE HELP
STRING, **including the help text that explains why the auto-derive is banned**. A common-noun scan
over a file that documents its own prohibition reads the documentation as the violation. Re-run
AST-only. The false FAIL is in the artifact's docstring, not quietly replaced.

**LIMIT STATED:** this verifies what the deployed bytes DO. It does NOT claim they match a committed
source vintage -- that identity is the DS lane's deploy leg. COO 76863 confirmed the division.

## 4. V14-4c(b) BUILT -- the campaign driver + durable checkpoint ledger

Banked as "ready to build" by the predecessor and **not built**. 533 dates x 114.5s is ~17h spanning
session ends, a mutex window and a dispatcher halt -- without the ledger a successor resumes from
memory.

- `--plan` DEFAULT; `--run` REFUSES without `--confirm-campaign-start` (74218: these writes BECOME
  production history). `--status` reads the ledger without touching AWS.
- Ledger: append-only JSONL, last row wins, a torn line WARNs rather than vanishing.
- The re-derivation script's report moved behind a `__main__` guard and its measurement into
  `derive()`, so **the driver decides the flag from a00's predicate and no other**. Re-run reproduces
  533 / 27 / 506, epoch 2026-07-14, no residual hole, both controls FIRED -- i.e. the refactor is
  behaviour-preserving AND the set has not moved since the predecessor measured it.

**THE COMPLETION ORACLE IS THE ARTIFACTS.** Not rc, and **not object COUNT** -- the control date also
had 2 objects, because these partitions already exist wrongly. Three discriminators, each EXERCISED
with the live wrong state as the firing negative: basis-presence FIRED (3 of 4), freshness FIRED
(4 of 4 vs a since=now probe), branch-agreement FIRED. `attested` guarded as the **-1 SENTINEL**,
never summed.

>> **The driver structurally CANNOT mark a date ARTIFACT-COMPLETE until a date is driven with the
   landed P14-STAMP code.** PRECISION BANKED: at 22:47Z the deployed bytes are new (22:08Z) but date
   1's manifests still read `<ABSENT>` on the three canonical tables -- because date 1 was written at
   20:32Z by the OLD code and has not been RE-DRIVEN. Un-stamped manifests are evidence about the
   ARTIFACT's vintage, never about the DEPLOYMENT's state. The two are different grains and only the
   re-drive closes the gap. The gate property holds and is in fact stronger than "until P14-STAMP is
   deployed", which is how I first phrased it to the issuers. <<

## 5. Finding -- the blackout was ONE window and the criterion is TWO

Found by re-reading code I had committed 30 minutes earlier against the clause it implements.

The clause's actionable sentence is "no date STARTS within [wall + margin] BEFORE the fire", so that
is what I built. **`seconds_to_next_anchor` jumps ~0 -> ~24h the instant the anchor passes**, so at
12:47Z -- nightly holding the entrypoint mutex -- the test reads 23.97h and says CLEAR. The guard was
blind for exactly the span of the run it exists to avoid, **and blind in the permissive direction**.

The fix was already in the clause ("RESUMES only after the nightly's completion is READ FROM ITS
PRODUCED ARTIFACTS"). I had even written the artifact-reading function -- **then called it only to
PRINT inside the pause branch, never to GATE resumption.** A computed-but-unconsumed check reads as
rigour and enforces nothing; CLAUDE.md s.4's consuming-half law at its smallest grain.

Now four states: PRE-FIRE / POST-FIRE (gated on the nightly's own artifact) / OVERDUE (2h grace, then
it stops and asks a human, because "not finished" and "never ran" are indistinguishable from here) /
DISABLED (UNREADABLE treated as ENABLED -- an unreadable schedule is when an assumption is least
affordable). Exercised at 7 clock positions + the disabled arm, 8 of 8 correct.

**One of my controls was wrong before the code was:** I expected 12:20Z HELD; it is correctly CLEAR
(25 min > the 16.9 min budget). Second instance this session of my instrument being wrong while the
subject was right. Both recorded -- an expectation that was wrong is data about the instrument.

**Measured in passing:** the nightly's own wall time is ~2.6 min (twr_daily date=2026-08-26 written
12:47:36Z against the 12:45:00Z anchor). That sizes the blackout's second half.

## 6. Blast radius on BOTH trigger planes

Swept `events list-rules` AND `scheduler list-schedules` -- a one-plane sweep returns a true,
correctly-controlled answer about the wrong population.

- `advi-49f-gold-floor` cron(45 12) UTC **ENABLED** -> advi-49f-gold-dispatch. The only contender.
- `advi-49f-publisher` cron(15 13) **DISABLED** -- a latent SECOND window if anyone enables it.
- `bd-49f-session-complete` event pattern keys on `document-name: opal-bd-49f-session-fetch`,
  **NOT** `advi-49f-chain-dispatch` -- so the campaign's 533 sends **cannot** fire `{mode:
  runner-run}`. This was the specific fear worth measuring rather than assuming.
- `opal-49f-served-guard-on-write` keys on a different bucket+key.

The single-window blackout design is therefore correctly scoped, **measured**.

## 7. Campaign-start -- the measured non-start

Three inputs (COO 76783), read at the faces 22:47Z:

| input | state |
|---|---|
| (1) ADVI_49F.P14-STAMP | `pending` -- deploy verified @9644276a3a, **face not flipped** |
| (2) ADVI_49F.c00-SIGNING | `pending` -- SG-2b already NEGATIVE @c46d26a059 |
| (3) date-1 re-drive | not run; sequenced AFTER (1) and (2) |

COO 76863 pinned that input (1) means the **FACE TERMINAL**, not the deploy leg's report -- so the
face-based pending read is the operative one. Running the date-1 re-drive now would be discarded work
the moment c00-SIGNING changes c00's output. **V14-4c(e) does not fire. Not starting.**

## 8. Compiler Tools

| run | observed | vs `<expect>` |
|---|---|---|
| `comp-iam service advi-49f-gold-dispatch` | 5 calls / 5 statements; 3 GRANTED-BROAD, 2 UNRESOLVABLE-RESOURCE; no missing grant | PASS -- no STOP. Treated as a **FLOOR**: a wildcard role cannot be falsified by a resource check, and the tool models `(action)` not `(action, resource)`. No NEW resource ARN was touched this session, so `simulate-principal-policy` deliberately not run. |
| `comp-pipescript postdeps chain_49f_entrypoint --firm bd` | **REFUSED rc=2** -- unknown script id in tree `bd` (universe 35 ids) | **NOT a clean sweep.** The chain lives in the **assets** tree, which `--firm` does not enumerate. Consumer set **UNMEASURED**, declared as an exclusion rather than reported as clear. Reproduces the predecessor's result. |
| `comp-iam gaps` | **N/A by its own trigger rule**, recorded not skipped -- no `iam.tf` changed | N/A |
| `aws ssm get-document --name advi-49f-chain-dispatch` (`# rail-checked`) | DocumentVersion 3 = Latest = Default, Active; Date + DeclaredHistorical + StartedByDispatcher; `--production` prohibited on the historical path; empty-Date guard `exit 2` present | PASS -- the APPLIED plane, the acceptance substrate, never the tf diff |
| `.tools/commit-gate.sh` (4 python files, several passes) | all green after fixing 5 ruff F541 | PASS |

**Phase 1's trigger did not fire this session** -- the mandate is "before write" on the SSM document,
and no document edit occurred; the two runs above are recorded anyway for continuity.

## 9. Commits (push state LOCAL -- CLOUD is integrator-only, LD-0367)

| commit | what |
|---|---|
| `6914a73fd1` | campaign driver + ledger; re-derivation refactored behind `__main__` |
| `a52a2224ce` | applied-entrypoint verifier, 4 PASS + a firing control each |
| `b2a8c86465` | strip a non-ASCII marker **I had already measured and committed past** |
| `42ce31beec` | the two-window blackout fix |
| `820c5945b1` | bank all of the above on the face |

`b2a8c86465` is worth its own line: I ran the ASCII census in the same command as the commit, it
printed `1`, and the commit proceeded. The measurement was taken and **not consumed** -- the same
shape as the blackout defect, at a trivial grain, in the same hour. Sibling files printed `0`, so the
instrument was live and discriminating. **The recurring failure this session is not measuring; it is
reading what I measured before acting.**

## 10. Next

Blocked on 0.4.0_DS_ClientPlatform~U's two faces flipping. On the flip: re-read both myself, fire the
date-1 re-drive, run it through the oracle (all four manifests then present), judge V14-4c(e).
Nothing else at this seat is gated.
