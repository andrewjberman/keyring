# 0.7.0_AE_CloudOps~P -- ETFS_POSITIONING.TO-5: the proof-of-spec instance EXISTS, filed from evidence that already existed

**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE

**Window:** 2026-08-28T19:00Z -> 20:00Z. Fresh seat (`~P` lane, first session).
**Commit:** `f32d343133` -- **LOCAL @f32d343133 (ls-remote read; `origin/SITEZ` at `a951b1bd21`)**. Push is
the integrator's act, not mine.
**Ledger:** NONE OPENED, deliberately -- filing an instance touches no deployed surface. Nothing applied,
nothing re-planned, nothing invoked.

---

## What the assignment was, and what it was not

`3.0.0_SA_CVO~Z` refused TO-5 pending an **executor act**: no proof-of-spec instance had ever been filed,
so there was nothing to certify and, in the face's own words, *"NO AMOUNT OF CERTIFIER TIME MOVES THIS."*
`2.0.0_SA_COO~Z` (13726) scoped it precisely: the schedule underneath is LIVE and ENABLED, so the work is
to **file the instance from existing evidence and re-apply nothing.**

That scoping held all the way through. Every one of the six criteria was dischargeable from artifacts that
already existed -- committed Terraform, two CLOSED deploy ledgers, CloudWatch invocation records and live
S3 objects. **No criterion turned out to need a deploy**, so the escalation the issuer asked for on that
condition ("if a criterion looks like it needs a deploy, stop and tell me -- that would mean the criterion
is wrong, not the world") was never triggered. The one criterion that *is* wrong is wrong in a different
way, below.

## The verdict

`proof-of-spec-check.py` **rc=0 VALID**, scored on the RC and not on the output string, per the face's own
instruction. 6/6 acceptance rows, 0 violations, coverage closed against `<expected_criteria>`
(AC1,2,3,4,5,7 -- there is deliberately no AC6). Alignment ENFORCE: 6/6 criteria carry `cell_refs`, 2/2
resolve into the decomp's 23-id space, 1/1 declared cell reachable.

⭐ **`ETFS_POSITIONING` is NOT exposed to the systemic alignment defect COO reported at 13733.** That
defect is `ETFS_INGEST`-specific: `CELL_ID_RE` requires a lowercase surface segment and `INGEST-T3-6` is
uppercase. TO-5's cells are `ETFS-d-1` / `ETFS-e-2` -- the form the regex can see. I checked this *before*
filing rather than discovering it in the verdict, and it means my clean alignment result is **not**
evidence that the `ETFS_INGEST` problem is fixed. Two different projects.

## ⛔ The one thing a certifier must not skim: AC4

**`ETFS-TO5-AC4`'s literal clause is FALSE, and I scored the row PASS anyway. Both halves of that are
deliberate.**

The criterion reads *"the as-of the run stamps **matches** `lib/trading_calendar.expected_last_trading_day`
-- never wall-clock. DS built the guard; this proves it survives deployment."*

```
MEASURED, 4 of 4 scheduled fires:  expected_frontier=D   as_of=D-1   trading_days_behind=1
```

It is not a near-miss and it is not a data problem. It is **unsatisfiable by any correct build at a
`cron(0 13)` fire**: `lib/trading_calendar.py:101-105` returns *"today if today is a trading day"*, so at
13:00Z the frontier is the fire's own date, while both inputs' newest partition is D-1 (silver netassets
fires 22:00Z on D; the 11:00Z local bbg pull writes `bbg/D-1/`). as_of is T-1 **by construction, forever.**

And equality would not merely be unreachable -- it would be **wrong**. The producer's own docstring
(`etf_positioning_gold.py:486-493`) states the design intent: `expected` comes from the CALENDAR and
`as_of` from the DATA, deliberately two independent sources, because *"a guard whose two sides are the same
expression over the same clock has no input that makes it fire."* **A criterion demanding equality is
demanding the degenerate guard.** CLAUDE.md NEVER#4 agrees the norm is T-1.

So the row is PASS **on the operative clause** -- never wall-clock, guard survives deployment, both proven
on the exercised plane -- with the falsification written inside the row where it cannot be read green
without being seen.

>> **The reasoning, stated because the choice was not obvious.** FAIL would report a correct, working,
>> calendar-driven guard as broken -- a false statement about the world. A silent PASS would hide a
>> falsified clause from the certifier -- a false statement about the evidence. The row has to carry both
>> facts, so it does. **What I did NOT do: edit the face, rename a cell, retrofit a `cell_ref`, or soften
>> the criterion.** The re-cut is the issuer's act and it is routed to them.

## What the evidence actually shows

| id | what carried it | the part that makes it evidence rather than assertion |
|---|---|---|
| AC1 | `comp-trigger` | `cron(0 13 * * ? *)` verbatim, ENABLED, correct target -- at **140 events-rules + 18 schedules**, i.e. BOTH EventBridge planes, since `list-rules` structurally cannot see a Scheduler entry. **Mutant on the same instrument** (nonexistent function name) -> NO MATCH at the same denominator. |
| AC2 | live config + source map | 512 MB / 120 s, and **the sizing is vindicated, not asserted**: the first scheduled fire reports **Max Memory Used 264 MB**, above the 256 MB default -- the default would have OOM'd. Source-map entry present at a 202-entry denominator. |
| AC3 | invocation record + `s3api` | A real fire's own record runs the whole chain to `PUBLISHED ... (126,788 B, listing-verified)`. Live object present; **bogus key under the SAME prefix 404s**, so the probe discriminates the key rather than the prefix. |
| AC5 | `comp-find -i` | **All 8 blocks in the root enumerated by name** -- zero alarm/SNS/SES/freshness/monitor. The 3 pattern hits are 3 comments. **Positive control**: same pattern over `globgrph` -> 214 hits / 26 files, so the zero is measured. |
| AC7 | log streams + per-run manifest | See below -- the row with the most ways to go wrong. |

## AC7, and the two traps in it

**Identifying "the FIRST scheduled fire" is where this row could have quietly gone wrong.** I enumerated
all **13** log streams in the group rather than querying the date I expected -- so a wrong assumption
would have surfaced as a missing or extra stream instead of confirming itself. Exactly four begin at
13:00:42Z (08-25/26/27/28); the earliest is **2026-08-25T13:00:42Z**, the first 13:00Z boundary after the
08-24T23:00Z deploy.

- **Invocation record:** `run_class=scheduled`, RequestId `dd66bc26-...`, START/END/REPORT, no
  `FunctionError`. **Exactly one stream at that boundary = ONE invocation, no async retries** -- which
  discharges the prediction my predecessor left open (*"expect ONE invocation and ONE manifest; if I see
  three, the marshal fix did not take"*). It is one. The marshal fix held **on the scheduled path**, which
  the synchronous ad-hoc invokes structurally could not have tested.
- **Artifact:** the criterion demands the *artifact* carry `run_class: scheduled`, not just the log. The
  per-run manifest does, as an **event-derived** field rather than a configured one.
- **The agreement is proven on a discriminating quantity.** Record: `built 126788 B, sha256 973f3e559a92f556...`;
  manifest: `body_bytes 126788`, `body_sha256 973f3e559a92f556...`. ⚠ **A byte count alone would not have
  been evidence** -- this exact producer has already been observed republishing a live key at an
  *identical size* with a different ETag. The sha256 is what makes it mean something.
- The amendment's **PASS-WITH-FINDING** branch is therefore **not taken**, and I recorded that explicitly:
  a silent omission would read as though the branch had never been evaluated.

## Surfaced, not chased

- **The served key is ONE key that is OVERWRITTEN.** Anyone verifying AC7 against
  `platinum/etfs/positioning_data.json` reads the *latest* fire (2026-08-28T13:01:26Z, 146,944 B) and finds
  no trace of the 08-25 fire the criterion is about. **The per-fire record is the manifest**, keyed by
  `run_id`. Written into the instance's `surprises` because it is a trap laid for the next reader, not for me.
- **AC2's vintage stated rather than glossed.** The live function now carries CodeSha256
  `qQk9ohLihOInJnvj...` at LastModified `2026-08-28T18:49:14Z` -- that is **`ETFS_INGEST.TO-10-AE`'s
  apply, a different project** (COO 13733), landed ~10 min before this seat was registered. Memory,
  timeout, handler and both layers are unchanged from the TO-5 deploy, so AC2 is unaffected; I cite
  those fields and deliberately **do not** cite CodeSha256 as acceptance, because code currency is not
  what AC2 asks about.
- **`aws` shim path-rewrite, measured here:** `s3api get-object` with an **absolute POSIX destination**
  returned a well-formed JSON envelope with **rc=0 and wrote no file**. Re-run from inside the target dir
  with a relative destination it wrote correctly (828 B, confirmed by `ls` before reading). Known site-Z
  class; recorded because *rc=0 plus a plausible response* is precisely the shape that gets trusted.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-which` | `comp-which "where is the ETFS_POSITIONING TO-5 task order face and where do proof-of-spec instances live"` | **NO CURATED RULE MATCHED** | Ran first per Rule 21 and the 08-28 Andrew-direct bulletin. The honest answer -- all 80 candidates below the vetted band. Recorded as a **coverage gap**; I took its own printed fallback (`comp-find --name`) rather than picking the top-ranked fuzzy guess, which the tool explicitly warns against. |
| `comp-find` | `--name 'ETFS_POSITIONING' --all`; `-i '<alarm/sns/ses/freshness/monitor>' --path .../etfs-positioning --all`; same pattern `--path .../globgrph` (**positive control**); `-i '^resource \|^module ' --path .../etfs-positioning --all` | PASS | Two load-bearing uses. (1) The name census (**41 files**) established the TO-5 **absence against a positive control** -- 7 sibling instances exist *including TO-2 in this seat's own deliverables dir*, so directory and naming pattern both resolve and the zero was a true absence. (2) Carried AC5 by enumerating all 8 blocks **and** proving the absence pattern could fire (214 vs 3). `-i` was necessary, not decorative: the only in-root matches are SHOUTED comment lines. |
| `comp-trigger` | `etf-positioning-producer`; `etf-positioning-producer-zzzNoSuch9999` (**mutant, separate invocation**) | PASS | Carried AC1 whole. The face names it precisely because it censuses **both** EventBridge planes with a printed denominator. The mutant is what makes the positive result discriminating rather than an artefact of a tool that always matches something. |
| `proof-of-spec-check.py` | positional, 6 ids, **rc captured before anything could clobber it** | rc=1 -> **rc=0 VALID** | First run: 2 violations, **both mine** (`kind: "artifact"` not in the enum; both are S3 objects -> `s3_object`). Second run clean. ⚠ Note for the certifier: **a passing rc attests structure and coverage, NOT that a row's evidence is real** -- this checker is known to pass a placeholder row -- so the AC4 judgement is not disposed of by rc=0. |
| live AWS primitives | `lambda get-function-configuration`; `logs describe-log-groups / describe-log-streams / get-log-events`; `s3api head-object` (target **+ negative control**); `s3api get-object` | PASS | Everything comp-* could not reach. `describe-log-streams` is what identified the first scheduled fire **by enumeration**. `s3api` used deliberately over `aws s3 ls` (LOCAL time, no marker) because every timestamp in the instance is a UTC claim. `get-object` on the manifest is what moved AC7 from a log-only observation to an **artifact** observation, which is what the criterion actually demands. |

**What worked.** Enumerating before selecting -- on the log streams and on the TF blocks. Both were places
where querying the answer I expected would have confirmed itself.

**What failed.** My own two schema violations, caught by the gate rather than by me. And `comp-which`
returned nothing usable for a file-location question -- a real catalog gap, recorded rather than papered over.

**Gap found.** `commit-gate` reported `checked 0 of 1 file(s) -- NOTHING WAS CHECKED` for a `.json`
deliverable and says so loudly, which is correct behaviour. The language-appropriate instrument here is
`proof-of-spec-check.py`, which I ran; **the gate's WARN is not cited as validation.**

## Blockers

**None at this seat.** The instance is filed, VALID, and committed.

**Owned elsewhere, listed so they are not read as mine:**
- [`2.0.0_SA_COO~Z`] **`ETFS-TO5-AC4`'s wording** -- unsatisfiable by any correct build at a 13:00Z fire.
  Issuer's re-cut; the face is unedited.
- [`2.0.0_SA_COO~Z` / `1.0.0_SA_CTO~Z`] The `ETFS_INGEST` cell-id convention (13733) -- **not** cleared by
  my clean alignment result; different project.
- [`0.0.0_AB_MSTR~Z`] `f32d343133` needs an integrator push; `origin/SITEZ` is at `a951b1bd21`.
- [`3.0.0_SA_CVO~Z`] TO-5 is now certifiable. **Nothing here stamps TO-5 or D4 closed** -- that is
  Andrew's, through his channel with CVO.

## Current State

`ETFS_POSITIONING.TO-5_PROOF_OF_SPEC.json` exists at the path its own face declares, passes the mechanical
gate at rc=0, and the executor act CVO refused the TO for is discharged. The schedule it attests to has
fired cleanly 4 of 4 times.

## Next Steps

- RAVC to `2.0.0_SA_COO~Z` -- filed + VALID + the AC4 wording defect, once.

---

## DELTA 19:22-19:30Z -- the issuer re-cut AC4, and the instance was re-filed against it

**Commit:** `1ff7f9fa60` -- **LOCAL (ls-remote read; `origin/SITEZ` at `a951b1bd21`)**.

`2.0.0_SA_COO~Z` **RE-CUT `ETFS-TO5-AC4` on the face @`b0f6b4f937`** (13766), striking the original in
place rather than deleting it, and ratified the handling: *"a build that PASSED my criterion would have
shipped a guard that can never fire."* **AS IT NOW BINDS:** the run derives `as_of` from the DATA and
reconciles it against the calendar, computing and stamping `trading_days_behind` as a small
non-negative integer, never wall-clock. Only the false equality is gone.

**The consequence that landed on my artifact, and why I did not fix it immediately.** The re-cut made my
`criterion_verbatim` quote superseded text. Two things had to be measured before acting:

```
  IS IT A MECHANICAL FAILURE?   NO. `criterion_verbatim` is in PROOF_OF_SPEC.schema.json and NOWHERE
                                in proof-of-spec-check.py -- no rc can ever detect this. The CERTIFIER
                                is the only reader who would meet it. So: raise before certification.
  CAN I RE-FILE YET?            NO. The re-cut face was UNCOMMITTED (` M`). Filing then would have
                                pinned vintage_commit 2566025e4d to text that vintage does not contain
                                -- A CITATION WHOSE OWN VINTAGE DISPROVES IT.
```

So I surfaced it as an A-or-B call with a rec and named the face landing as my own trigger, rather than
either churning against a working tree or sitting on it. The face landed at `b0f6b4f937` (verified: tree
clean, `git show` positive-controlled at 358 lines); `2.0.0_SA_COO~Z` ruled **option A** at 13779.

**What changed: three text/vintage fields and one surprise disposition. `1 file changed, 6 insertions,
6 deletions.`**

| field | change |
|---|---|
| `criterion_verbatim` | original equality wording -> the criterion as it now binds |
| `spec_ref.vintage_commit` | `2566025e4d` -> `b0f6b4f937` (the vintage that CONTAINS the quote) |
| `status_reason` | reframed -- the defect lives on the face now, so the row stops re-deriving it |
| `surprises[0]` | `OBSERVATION x ARMED` -> **DISARMED AND REMEDIATED**, disposition recorded |

⛔ **status PASS, denominator and every line of measured evidence are byte-identical to the original
filing.** No re-measurement was performed and none was needed -- the re-cut describes what the deployed
run already does on all five limbs. **A re-file that moved a number would have been a different act than
the one authorised**, and the 6/6 line diff is the evidence that none moved. Re-validated: rc=0 VALID,
6/6, alignment 6/6 forward / 2/2 resolve / 1/1 backward.

⚠ **VINTAGE ON MY OWN VERDICT, per 13779 s.3:** this rc=0 is true at **LOCAL HEAD**. The checker fix
`87c5761e9e`/`d4da9da939` is not on origin, so a seat re-running against `origin/SITEZ` may read
differently -- **an unpushed checker, not a bad instance**. `ETFS_POSITIONING` alignment was clean
independently of that fix, so the caveat is about reproducibility of the run, not a dependency.

## Also this window

- **Corrected a peer's claim about my own artifact.** `0.4.0_DS_ClientPlatform~P` (13763) warned my
  filing would hit the comp-system gate and stated my file was one of three counted in the 247->250
  drift. It was not, and it could not be: `safe-commit.sh:612`'s pre-check is a **hardcoded three-entry
  path enumeration** naming `0.4.0_DS_ClientPlatform/deliverables/` and not mine, and `comp-system`
  itself returns *"no comp-system `_SOURCE` in the changeset -- gate n/a, open"* for my exact path
  (positive control: the DS path fires **BLOCKED-ON-PEER-LANDING**). Two instruments agreeing.
  **I therefore did NOT write a `system-current-override:` line** -- for a gate that never evaluated the
  commit that would be a false correctness signal in the audit log. That seat re-derived the correction
  at source and carried it to `2.0.0_SA_COO~Z` themselves, where the wrong set-size was heading into the
  `STRUCTURAL-TWOPHASE/proof-of-spec` adjudication.
- **The generalisable half, surfaced not adjudicated:** the gate's trigger surface names ONE seat's
  deliverables dir, so two proof-of-spec instances of the same kind filed the same hour meet different
  gates. The "a guard is only as wide as its enumeration" shape. It also means that deadlock is
  **seat-scoped, not fabric-wide**.

## Blockers (delta)

**None. Seat IDLE.** Nothing half-landed, no ledger open, no override written, nothing outstanding to
any seat. Both commits await the integrator's push.

## CERTIFIED 19:28Z

`3.0.0_SA_CVO~Z` certified **TO-5 rc=0 VALID, 6 rows, 0 violations, coverage 6/6** at cert
`@b5b9f8ae6e` (13787), with its own **negative control** -- the same instance plus one bogus id
returns rc=1, so the check discriminates -- and the 3-arg form throughout, since the 2-arg form
returns a clean rc=0 that says COVERAGE UNCHECKED. **`ETFS-TO5-AC4` was certified on the RE-CUT, not
the original.** The certifier independently reached the same reading of the original defect: *"a build
that PASSED it would have shipped a guard that can never fire."* `ETFS-TO5-AC6`'s absence was checked
rather than assumed and survives because the face declares it.

⚠ **ONE CITATION HAZARD I INTRODUCED AND HAVE ROUTED.** The cert names the instance at `f32d343133`;
the instance is now `1ff7f9fa60` (the AC4 re-file, ~1 minute earlier). **The certification's substance
is unaffected** -- the delta is `criterion_verbatim`, `spec_ref.vintage_commit`, `status_reason` and
one surprise disposition, with status, denominator and every measurement byte-identical. But a later
reader diffing the cert's cited hash against the instance at HEAD would meet a divergence, which is the
same class I raised to the issuer an hour earlier about my own `criterion_verbatim`. Surfaced to
`3.0.0_SA_CVO~Z` to re-point or ratify; **not my call to edit a certificate.**

⛔ Certification does NOT close `ETFS_POSITIONING` or D4 -- Andrew ruled *"D4 is done"* a READ, and the
register act travels through his channel.
