# Session log -- `0.8.0_AE_CloudComp~Y` -- 2026-08-27 06:06Z - 07:30Z

**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE

**Serial:** `0.8.0_AE_CloudComp~Y` · **TO:** `NFRA_SUBSTRATECARDING.TO-W3-CCY3` (wave 3, materializers)
**Predecessor:** respawn by MSTR after this seat's prior session died 05:31Z; TO dispatched 05:46Z, AFTER that death
**Window:** respawn 06:06Z -> two BLOCKINGs filed 06:20Z -> re-decomp @e48a7466ba -> 4 cards committed @fbb8a94c17

---

## 1. What this window was

Dispatched 2 subjects / 14 cells. **Delivered 4 subjects / 28 cells**, because both my subjects
turned out to have two write paths and the issuer re-cut CCY3 on my BLOCKING. Startup was clean:
`/watcher` armed (banner `parent-tied: pid 586101`, so protected, not orphan-capable), `/cloud-ops`
loaded, `org/XXX.md` walked, zero crons armed.

**Delivered `@fbb8a94c17`** -- 4 cards + a proof-of-spec instance. Gates: 4/4 VALID under both
Draft7 and Draft2020-12; 28/28 rows carry basis+evidence+owner; `proof-of-spec-check` VALID with
0 violations and 28/28 alignment both directions; 7/7 mutants rejected; determinism STABLE.
**PUSH STATE: LOCAL @fbb8a94c17** (ls-remote read; origin/CLOUD tip 21d1d672e6; `fbb8a94c17` NOT
an ancestor; positive control `230bc2b04f` IS -- instrument fires). Push blocked by the LD-0367
integrator-only rail; not overridden.

## 2. The two BLOCKINGs, both upheld and executed same-turn

**BLOCKING 1 -- the decomp's `write_evidence` named an artifact my subject does not write.**
It read *"writes fedobs_coevolution_snap"* for `cse_emit_frontend_coevolution.py`. That file
contains ZERO references to the token; the real writer is `emit_fedobs_snap.py:50` with the
schema entry at `snap_store.py:128`. Root, confirmed by the issuer: the subject IMPORTS
`NFRA_FEDOBS_frontend_coevolution_producer` at `:78`, so **the FEDOBS stem is in the file while
the artifact is not** -- a name resolved from a shared stem rather than from a read.

⛔ **THE INSTRUMENT IS WHY IT LANDED IMMEDIATELY.** An estate sweep that NAMES the positive
members, not a scoped grep whose zero could be a floor: my subject is ABSENT from the set of
files carrying the token while the two true writers are present. `2.0.0_SA_COO~X` said that
distinction is what let them act without re-measuring.

It was BLOCKING rather than OBSERVATION because **`writer_class: UNCLASSIFIED` rested on that
string** -- the class was not merely unmeasured, its stated basis pointed at another file's output.

**BLOCKING 2 -- both subjects had 2 write paths**, both carrying `write_paths_measured: null`.
Each pair differs in mechanism, bound AND authority. CCY3 re-cut 2/14 -> 4/28.

## 3. **STOP:** THE HALF I DID NOT SPLIT IS THE ONE THE ISSUER CALLED DECISIVE

`lambda_function.py:501` (overwrite) and `:504` (delete) are **exclusive BRANCHES of one atomic
commit envelope** -- same table, same bound at `:434`, same authority, and the docstring at
`:412-424` states the single-envelope design outright. I declined to call them two paths.

> `2.0.0_SA_COO~X`: *"A grain instruction that only ever produces MORE rows is not being applied,
> it is being obeyed. You are the first lane to return a bounded answer to it, and that is what
> makes the other three splits credible rather than a lane maximising against a criterion."*

**Worth keeping because the incentive ran the other way.** I had just been rewarded for splitting;
the cheap move was to split again. The (FILE, WRITE PATH) grain names three discriminators and
none of them differs across `:501`/`:504`.

## 4. What the four cards carry

- **W3-uuxp -- A PROTECTION RULED BLOCKING HAS NEVER EXECUTED.** `_provenance.py:271-303`
  `_archive_superseded` preserves the destructively-overwritten branch-head marker; CTO ruled it
  BLOCKING (`:279-280`) because the object is non-versioned and without the archive a criterion
  comparing against a prior marker degrades FAIL -> UN-EVALUABLE. **Three planes, each able to
  answer the other way:** it is called only from `_stamp_cas`, never `_stamp_unconditional`
  (parsed from the DEPLOYED vendored copy); the live Lambda has no `GLOBGRPH_MARKER_CAS`, so
  `_cas_enabled` reads its `off` default; `_branch_head.history/` holds zero objects and is absent
  from a delimiter listing that returned ten real siblings. **Bound stated:** an empty prefix on a
  non-versioned bucket cannot alone separate never-written from written-and-deleted -- the CODE
  plane closes it.
- **W3-dljc -- A 259,918-BYTE VALID BATCH ONE PREFIX FROM ITS CONSUMER FOR 50 DAYS, EVERY
  INSTRUMENT GREEN.** `cse_producers_nightly.py:75` binds `warehouse/cse_ingest/pending/` and
  `:178` paginates that and no other (read from the CONSTANT, not the docstring). The subject's
  only output is at `warehouse/cse_ingest_staging/`. This morning's receipt: leg `sweep`
  `batches=0, failed_legs=[]`. **A clean green, because an empty prefix and nothing-to-do are the
  same event.** Intent UNMEASURED and not inferred; file NOT moved -- the seam is UNOWNED.
- **W3-thav -- 6 of 14, and the asymmetry is the defect.** `arn_to_class` maps 14 services;
  `bounded_derive_node` implements 6. The other 8 fall through to `:334 logger.debug`, which
  `:34`'s INFO level **suppresses**, while `:256` logs an UNKNOWN class at WARNING. **The
  better-recognized failure is the quieter one**, and `ec2` is in the silent set.
- **W3-bzgw -- the watermark that makes the producer incremental has never existed.** 404, and
  the whole prefix absent. Traced through code: no marker -> `_read_watermark` None -> `:250`
  watermark None -> `:170` filter never applies -> **every emit has been a FULL BACKFILL wearing
  an incremental producer's documentation.**

## 5. **STOP:** CodeSha256 MATCHED PERFECTLY AND THE PACKAGE WAS STILL STALE

Deployed hash == local zip byte-for-byte; `lambda_function.py` sha-identical to source. But the
vendored `_provenance.py` is **27,072 bytes vs 34,270** on disk.

⛔ **I CONTROLLED FOR CRLF BEFORE CALLING IT DRIFT** (the banked memory fired correctly): zip 0
CRLF, tree 641 -> **641 bytes line-ending inflation, 6,557 bytes REAL** divergence, normalised
shas unequal.

⛔ **THEN I BOUNDED IT, AND IT WENT THE REASSURING WAY.** Lines 1-391 byte-identical after
normalisation (`c58dddea55d8` both sides); first difference at `:405`; drift confined to the
dev-box header-READ surface the write path never calls. **Every symbol my cards cite sits in the
identical region at the same line number in both copies.** So the citations describe running code.

**I did not file an alarm, because the measurement did not support one.** The tempting move was
to report "the deployed Lambda is a week stale" -- true of the package, false of the write path,
and the cards would have inherited a false hazard. `git log` also corroborates: `_provenance.py`
was committed 2026-07-22, seven days after the zip was built.

## 6. The AC5 trap fired exactly as written

The scheduler plane DOES hold `globgrph-cse-producer-nightly`, ENABLED, `cron(30 3 * * ? *)`.
**A name-based read concludes my subject is triggered nightly.** Its `Target.Arn` is
`arn:aws:ecs:...:cluster/opal-globgrph` -- **a CLUSTER**. Task definition `globgrph-cse-producer:1`
runs `["python","/app/cse_producers_nightly.py"]` -- **still not my subject**. That module's
`:21-25` names `frontend_coevolution` as a LOCAL-source producer it deliberately does NOT run,
because a Fargate task cannot see the portal git submodule.

**Three hops, each READ.** The result is stronger than a bare absence: the subject is
architecturally un-triggerable from AWS by design. This independently re-derives
`1.0.0_SA_CTO~X`'s *"NO live trigger on either plane"* with a different instrument and supplies
the mechanism -- **corroboration, not repetition** (Rule 22).

Both planes swept with denominators: **137 events rules / 18 scheduler schedules.**

## 7. The contract caught two real defects of mine, and I fixed them the honest way

- **FLOOR RULE.** W3-bzgw shipped `persistence.basis: measured` over `form` and
  `mutation_policy` marked `inferred` (I have never seen the object that path writes).
  ⛔ **I DEMOTED THE SCALAR, NOT INFLATED THE SUB-CLAIMS.** Upgrading two claims to clear a
  validator is the exact inversion of what the floor rule exists to catch, and it would have been
  one keystroke.
- **id pattern.** `W3-dljc` carried a `composes` id of `portal (git submodule)`; the contract
  forbids prose in an id. Moved to the note.

**AND MY OWN SCAN OVER-REPORTED.** My proactive id-pattern sweep then flagged 4 more violations,
all on `subject.id` -- **false positives: the pattern binds `composes`/`invents` ids, and my
walker applied it to every key named `id`.** A control whose SUBJECT was the wrong field. Resolved
against the validator itself; two of those four cards had already validated with that exact
subject-id form. **Had I trusted my scan I would have mangled four correct ids.**

## 8. Delivered-artifact finding on a peer, raised pre-cert

`proof-of-spec-check` on `NFRA_SUBSTRATECARDING.TO-W3-CCX3_PROOF_OF_SPEC.json` -> **11 violations,
INVALID.** **My own CCY3 instance returned the same 11 first**, which is why I could hand over the
exact fix rather than just the verdict: `method` is a closed enum; `controls` admits only
`mutant` + `determinism` and `determinism` is required; `decomp_ref` admits no `pin_note`.

⛔ **POSITIVE CONTROL, so this is not a broken-checker claim:** the same checker returns VALID on
my lane's already-certified W1-CCY instance. Two wave-3 lanes drifted the same three ways
independently.

⛔ **AND THE ALIGNMENT FIGURES SURVIVE THE FAILURE.** On an INVALID instance the checker still
prints `8/8`, `21/21`, `21/21` -- and warns, in its own output, that those figures are NOT
evidence of validity. **The numbers a completion report most naturally quotes are exactly the ones
that outlive the verdict.** I nearly quoted my own 28/28 that way before scrolling down.

⛔ **`$?` THROUGH A PIPE READS `tail`, NOT THE CHECKER.** My first run printed INVALID and reported
`EXIT=0`. Read the VERDICT LINE, never rc -- same shape as the `comp-validate` rc trap.

## 9. Compiler Tools

| tool | invocation | result |
|---|---|---|
| `jsonschema` (v2 contract) | Draft7 + Draft2020-12 over delivered bytes, 7-mutant battery, 28-row sweep | PASS -- 4/4 VALID both validators, 7/7 mutants rejected. **Caught two real defects of mine pre-delivery** (s.7) |
| `.tools/proof-of-spec-check.py` | my instance + CCX3 + W1-CCY as control | PASS -- mine VALID 0 violations after fix; surfaced CCX3's 11 (s.8) |
| `comp-kuzu` | `MATCH (n) RETURN count(n)` for the as_of vintage | **FAILED** -- timeout 90s, rc=143, no header. Recorded as attempted-and-failed; vintage sourced from the live branch-head marker instead and the substitution disclosed on the face |
| `comp-rail` (Rule 21) | fired twice, unrequested, on Bash greps under `infra/` | PASS -- **the gate improved the work**: the refused sweep re-run under ripgrep returned a NAMED positive-member set, which is what made BLOCKING-1 sound rather than a floor. One later `.tf` lookup carried an explicit `# rail-checked:` marker |
| `aws` (lambda/events/scheduler/ecs/s3api) | ESM, reverse-lookup, both planes, taskdef, head-object, list-objects-v2 ±delimiter | PASS -- every live denominator + the 3-hop trigger resolution. `s3api` chosen over `aws s3 ls` deliberately (UTC vs LOCAL) |
| `git` (ls-files/log/diff/rev-parse/cat-file) | tracked w/ firing negative control; vintages; `d2cf839c79..HEAD` diff; ls-remote ancestry | PASS -- diff EMPTY is what licenses pinning to `049ff4ca4a` though HEAD moved 3x mid-session |
| `.tools/safe-commit.sh` | `-F`, message file written by the Write tool, explicit filenames | PASS -- msg-verify MATCH len=5192; risk-reflex CLEAN, 5 files vs 1891 danger nodes |
| `comp-blast` | not run | NOT ATTEMPTED and stated. `~X` recorded it timing out on a globgrph module this same session; the consumer question was answered by reading `_provenance.py`'s consumer path instead |

## 10. AC8 -- three restraints, each of which would have destroyed evidence

Zero commits touching any carded module. The Class-3 remedy (`choices=`, already at
`snap_store.py:415`) NAMED, NOT APPLIED. Beyond that: I did NOT run the producer; I did NOT write
the W3-bzgw marker key -- **that PUT would have manufactured the very object whose absence is the
card's central measurement**; and I did NOT re-stage the 259,918-byte batch, though one copy would
"fix" s.4's finding. It is not this lane's call and the seam is UNOWNED.

## 11. Shared-directory hazard, handled

`D11_CARDS_W3/` holds 7 cards: **`~X` 3, `~Y` 4**, measured by `carded_by`, never by path.
Committed by **explicit filename**, never by directory pathspec -- `safe-commit`'s contamination
guard is structurally blind to files INSIDE a declared pathspec, so a directory pathspec would
sweep a peer's cards under this lane's author line.

⛔ **AND IT BIT THE ISSUER THE SAME HOUR:** `2.0.0_SA_COO~X`'s "0 tracked" flag keyed on the shared
directory and moved CCY3's gap onto CCX3's name -- *in the same turn they acknowledged the message
warning them about that exact glob* (74892). **A shared directory cannot attribute work.** My
commit closes the real row: `~Y` 5 of 5 tracked at HEAD (`git cat-file -e`, negative control fires).

## 12. Blockers

**NONE.** Two BLOCKING surprises filed, both upheld, both disarmed same-turn by the issuer's
re-decomp. Nothing owed by this lane on either.

## 13. State at close

CCY3 **COMPLETE** -- 4 cards / 28 cells, 8/8 AC PASS, TO `<status>` flipped pending -> complete.
Routed to `3.0.0_SA_CVO~X` for cert (74899), cc issuer (74900). CCX3 instance finding to
`0.8.0_AE_CloudComp~X` cc CVO (74904/74905).
**Push state, measured with a firing control:** `fbb8a94c17` LOCAL, riding the integration window;
push is integrator-only per LD-0367 and was NOT overridden.

## 14. The one I would keep

Section 5. **I measured a real 6,557-byte divergence in a deployed package and the correct output
was "this does not reach my subject."** Every incentive pointed at filing it -- it was novel, it
was in a module my cards lean on, and "deployed Lambda is a week stale" is a better-sounding
finding than "I bounded it and it is fine." **The bound was three commands past the alarm**, and
the alarm would have put a false hazard on four cards and into a wave record.

`2.0.0_SA_COO~X`'s line from this window is the general form, and it cuts both ways:
**"Deriving a value does not make it right. It makes it consistently whatever the source says."**
A correctly-measured number can still be an answer to the wrong question -- and the fix is not
more measurement, it is naming the question the number is supposed to answer before quoting it.

## 15. ANNOTATION (07:2xZ) -- s.8 WENT STALE ABOUT A PEER WITHIN FOUR MINUTES, AND THAT IS THE ACCUSING DIRECTION

**Section 8 states CCX3's instance is INVALID with 11 violations. It is not, and by the time I
committed the log it already was not.**

```
0.8.0_AE_CloudComp~X fix committed   06935043aa   07:13:53Z
my 74904 composed                                 07:17:33Z
CCX3 gate re-read (their seat + CVO)              violations=0, VALID
```

**A 3m40s window the sender cannot see.** `0.8.0_AE_CloudComp~X` (74906) declined to call it a
stale-reader error: *"a cross-vintage read manufactures a discrepancy that exists only in the
reader."* `3.0.0_SA_CVO~X` (74907) recorded the same -- the hand-off *"crossed the CCX3 rework in
flight."* Third crossing this wave.

⛔ **THIS IS THE HARDER HALF OF THE BANKED RULE.** The usual form is *my own artifact goes stale
against the ruling that corrected it.* This is the inverse: **my artifact went stale about SOMEONE
ELSE, in the accusing direction, and a committed log is exactly where such a claim survives
uncontested.** The fix is not more care before sending -- I could not have seen the 4-minute
window -- **it is re-reading my own file on the trigger "a correction landed."** That trigger
fired at 74906 and I acted on it here.

**WHAT SURVIVES, AND IT IS THE PART THAT MATTERED:** the diagnosis was correct and independently
reached; `0.8.0_AE_CloudComp~X` confirms the remedies match on all three causes. The durable
finding was never "CCX3 is invalid" -- it is that **two lanes drifted from the same contract in
the same three ways, independently, and each found it only when an external party ran the gate.**
CVO is riding that to the contract owner as **schema ergonomics, not lane defect**, and my
positive control (the certified W1 instance passing) is what makes that reading available rather
than "two careless lanes." A finding whose value sat in the pattern, not the verdict.

## 16. CLOSE -- VERDICT RECEIVED

`3.0.0_SA_CVO~X` **74907: VERIFIED PASS @6505ba713f**, battery re-run at that seat with its own
instruments rather than accepted from my delivery report: gate VALID with 28/28 alignment both
directions; 4/4 cards 0 errors against v2 validated independently of my dual-draft runs; 5/5
tracked with an empty untracked scan; containment at `@049ff4ca4a`. **QUALIFIED x4**, with the
floor rule noted as *"exercised in the direction it exists for."* The verdict names the AC8
restraints as the wave's strongest -- three refusals each of which would have destroyed the
evidence it "fixed."

**ALL FOUR WAVE-3 LANES VERIFIED PASS.** 13 subjects, none SOUND, every UNSOUND scoped and every
floor declared. **The close is the issuer's act; nothing at this seat blocks it.**
