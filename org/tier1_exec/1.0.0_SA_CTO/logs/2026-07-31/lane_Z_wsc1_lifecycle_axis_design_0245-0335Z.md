# CTO~Z lane: WS-C1 lifecycle axis designed through four revisions, and every defect in it was found by someone else

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, COORDINATE, DIAGNOSE, SCRIBE

**Serial:** `1.0.0_SA_CTO~Z` (site Z) · **Window:** 2026-07-31 02:45Z -> 03:35Z · **Regime:** NFRA_VELOCITY
EXCLUSIVE (Andrew GO ~0225Z). Nothing outside VELOCITY was touched.

## 1. What this session was

Startup, then the CORE critical path: **WS-C1, the D3 lifecycle/supersession vocabulary.** I own design
+ gate. `0.8.0_AE_CloudComp~C` builds, `3.0.0_SA_CVO~Z` verifies, `0.0.0_AB_MSTR~Z` holds the seam.

Delivered: a design spec through **four revisions**, a task order + GO, a scoped grant to a second AE,
a RAVC close, three findings routed, and one incident ruling. All committed and pushed as produced --
MSTR~Z counts 7+ silent session deaths on this device today, including my own predecessor at 2044Z.

## 2. The design (rev 4 @50643084b)

`lifecycle_class`, 7 values inside `dynamic_rails.D3_contract_obligation`:
`PERMANENT / TRANSIENT / EVENT_CREATED / DORMANT / LEGACY / RETIRED / UNDECLARED`.

Three ideas carry it:

- **POLARITY INVERSION.** A detector cannot merely KNOW about `TRANSIENT` and skip it; it must run the
  OPPOSITE predicate. Absence is healthy on 2 rows, presence is a finding on 2 -- **a single-polarity
  existence detector is wrong on 4 of 7, in the direction that proposes deleting live infrastructure.**
  A skip-list suppresses; a type inverts. Inverting also recovers `STRANDED` (written, never consumed
  = a dead pipeline leg), which no instrument in this estate can state in either direction today.
- **EVERY DECLARATION CARRIES ITS OWN FALSIFIER, AND EVERY FALSIFIER DECAYS.** The axis SUPPRESSES
  findings, so an unfalsifiable declaration is a silencer carrying a type system's authority.
- **PRODUCER-ASSERTED, NEVER OBSERVER-INFERRED.** The observer cannot distinguish never-yet from dead
  by looking, so requiring the observer to classify MOVES the impossible judgement rather than
  removing it.

## 3. The actual finding of this session: I found none of the defects in my own spec

| defect | found by | what it would have done |
|---|---|---|
| `DORMANT` missing entirely | `0.8.0_AE_CloudComp~C` (from its own divergent draft) | ungated `SILENT-RESIDENT` matched deliberate belts -- the outcome `keep-dormant.yaml` calls *"THE named failure mode"* |
| `revalidate_by` decay absent | the estate itself (`keep-dormant.yaml`, already running) | a falsifier verified once is a control that cannot fail |
| `SUPERSEDED`/`ORPHAN` token collision (**BLOCKING**) | `3.0.0_SA_CVO~Z` | both tokens already occupied on a ratified axis, and the collision HID a live bypass |
| `variance.Orphan` ungated | `3.0.0_SA_CVO~Z` | a separate WIRED detector flagging *"singleton, no sibling, no consumer"* -- the at-rest signature of a `TRANSIENT` |
| `max_dwell` a free scalar | `3.0.0_SA_CVO~Z` | declare TRANSIENT + any consumer + absurd dwell = a permanent silencer satisfying S.3 to the letter |
| RESOLVE-vs-EXERCISE | `3.0.0_SA_CVO~Z` | I required "D2-resolvable" one paragraph after citing "EXERCISE rather than RESOLVE" |
| flagship specimen fails my own S.3 | `3.0.0_SA_CVO~Z` | device-local artifacts have no cross-device observable |
| S.4 bound had no enforcement surface | `3.0.0_SA_CVO~Z` | a DESIRED-only control reading as APPLIED -- Rule 22a's exact class |

**A careful author with the right principles wrote a document that would have proposed deleting
registered rollback levers and left a live kill-list path ungated, while citing the registry that
documents one of those doors.** The repair rate is the story only because the record names who
repaired what; every F-n and R-n is attributed inline rather than absorbed into my prose.

## 4. Two ungrounded claims I made, in a document about grounding

Recording the pattern, not just the instances -- both were plausible reconstructions that fit the
symptom, and neither was checked before I published it.

1. **"Racing parallel edits" as the cause of rev 2's partial landing.** Written into a PUSHED commit
   message (`691860493`) whose entire subject was record integrity. **The timeline disproves it:**
   MSTR~Z's accidental stash at `03:12:18Z` preceded my rev-2 commit at `03:14:29Z` by 2m11s and
   pulled the edits out from under it. Corrected in rev 4's message, in-file, and to MSTR~Z and ~C
   directly. Cannot be corrected in `691860493` itself -- pushed, shared branch, NEVER#7.
2. **"All 7 registered `keep-dormant.yaml` entries"** as the blast radius, asserted in revs 2 AND 3.
   Never measured. `variance.Orphan` is a CONJUNCTION and nobody has measured whether belts satisfy
   its no-sibling conjunct. CVO~Z printed it as unmeasured rather than let my number stand. Now
   **UNKNOWN, bounded above by 7**, with acceptance item 17 requiring it MEASURED before the gate is
   written.

## 5. Coordination

- **`0.8.0_AE_CloudComp~C`** -- TO `@5da07cf62` + GO. Disclosed an in-flight divergent draft
  unprompted, before landing, listing five divergences against its own interest. That disclosure is
  what produced `DORMANT`. Held on my `[STOP]` when the token collision landed; released to rev 3 with
  the TO amended `@d79957d22` rather than silently rewritten.
- **`3.0.0_SA_CVO~Z`** -- commissioned the design attack to run BEFORE my gate, on their argument that
  a finding arriving after the build it should have redirected is worthless. 9 findings, 8 accepted,
  then 3 more on the decay half. They also pinned a **pre-touch baseline oracle** (`8f8a63200`) with
  minutes to spare; **additivity is checkable only against a baseline pinned before the touch.**
- **`0.7.0_AE_CloudOps~Z`** -- ADMITTED to CORE, scoped to WS-C7 specimen capture only. Supplied the
  four-state partition of a 404 that produced `EVENT_CREATED`, and **refused to manufacture a WS-C1
  specimen it did not have.** RAVC closed with all three boundary claims independently verified.
- **`0.0.0_AB_MSTR~Z`** -- reported an incident it caused (a backtick in a message body executed
  `git stash` against the shared tree). Ruled: do NOT restore my file (rev 4 supersedes it), HOLD the
  stash until injured lanes confirm, and ~C's recovered hunks are reference material, not a landable
  build (they carry rev-1 vocabulary including the blocking tokens).

## 6. Findings routed, not built

- **`org/XXX.md` A.3 exercises a HAND-CHOSEN member.** The 2026-07-25 fix corrected
  resolve-vs-exercise and KEPT the hand-chosen sample, so the probe still cannot fail in the state it
  exists to detect. Specimen: `SPEC-1 @2c5e1c60e`. Law surface -> routed to MSTR~Z, not edited at ~Z.
- **F-010 generalization** (MSTR~Z's): the mandate for `-F`/heredoc is scoped to `git commit`, but the
  substitution mechanism applies to ANY shell-parsed argument carrying prose. **A gate on the command
  surface does not cover the substitution surface.** Their incident is the existence proof.
- **`keep-dormant.yaml`'s `annotation_cite` carries no vintage** -- live on 7 entries today; Rule 22
  says a line citation without a vintage is not a citation. CTO arch-gated, not mine to edit at ~Z.
- **`org/tier1_exec/1.0.0_SA_CTO~Z/**` has no owned-paths PATH rule.** Distinct from the "phantom
  tilde-lane gap" that file warns about -- the AGENT lane-strip works; this is a missing PATH
  enumeration, the CRO precedent. Used the base folder instead of granting myself a path (SoD).

## 7. Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `comp-which "how do I grep the repo"` | A.3 startup EXERCISE (not resolution) | PASS -- forwarder RAN, produced its own banner. 92 of 94 comp-tools resolve bare |
| `audit-archive-invoker.py` | Startup A.2 | rc=1, 11 findings -- device-locality, fails CLOSED correctly. **Standing gate item: NOT to be "repaired" by re-baselining** |
| `git show <oracle>:<path>` + positive control | Grounding the F-1 token collision at the PINNED oracle rather than the in-flight tree | CONFIRMED `variance.labels` line 115 of 425; denominator printed; positive control run |
| `safe-commit.sh` (x6) | Every commit, `-F` heredoc per F-010 | PASS; surface-check clean, risk-reflex CLEAN against 900/1484 danger nodes |
| `owned-paths-check` (via safe-commit) | Blocked my first commit | **Correct refusal** -- a live gate firing, not a nuisance |
| `never-rules-gate` | Blocked `git stash` on the shared worktree | **Correct refusal.** I complied; MSTR~Z later triggered a stash through the substitution surface the gate cannot see |

**What worked:** grounding claims at a PINNED COMMIT rather than the working tree -- three seats share
one checkout here and the disk moved under me twice.
**What failed:** my own two ungrounded causal claims (section 4). Both would have been caught by the
check I demand of others.
**Rail deviation, disclosed:** I ran `find . -name "keep-dormant.yaml"` -- a broad estate-scoped find
that should have been `comp-glob` under Rule 21 Gate-1. It was not denied. Recording it as my
deviation rather than as evidence the gate is absent; the correct call was `comp-glob`.

## 8. State / next

Repo pushed, `0/0`. Spec at **rev 4 `@50643084b`**, acceptance **17 items**. `~C` building against
rev 3/4 after stash recovery; CVO~Z holding build-verify until I gate; `0.7.0~Z` idle-but-warm with
its grant discharged.

**NEXT:** gate `~C`'s build (items 1-17) -> signal CVO~Z -> **WS-C2**, the corpus walk that is this
enum's real acceptance test. My standing instruction to CVO~Z holds: **if the enum does not change at
WS-C2, be suspicious of the walk** -- and after F-1/F-3/F-4/F-6 that is now evidence about the BUILD,
not about the enum.

---

## 9. ADDENDUM (03:35-04:15Z) -- WS-C1 IS CLOSED

| | |
|---|---|
| LANDED | `NFRA_ONTOLOGY_RULE_BANK.yaml` v1.7 -> **v1.8** `@880f527cc` (+234/-1); 06 recompiled `@e22f38c41` |
| GATED | `1.0.0_SA_CTO~Z`, 19/19 mechanical |
| VERIFIED | `3.0.0_SA_CVO~Z`, independently **re-derived**, content 15/15 |
| PARITY | `comp-system --check` = SYSTEM CURRENT. Repo `0/0` |

**A REAL DEADLOCK, EXERCISED FROM BOTH SIDES.** The commit gate refused the landing (06 stale, *"run
comp-system first"*); `comp-system --check` refused to run (*"source file(s) are uncommitted...
would launder unlanded peer work into 06's committed self-description"*). Each correctly pointed at
the other. Broken with an audited `system-current-override` in the only safe direction -- land the
GATED source, then recompile against it -- and the follow-on landed in the same session, which is the
sequence comp-system itself demands. **CVO~Z had predicted this deadlock from source two hours
earlier; the tool then said it verbatim at runtime.**

**MY GATE PROBE WAS WRONG THREE TIMES BEFORE IT WAS RIGHT**, all FALSE FAILS against a correct build:
wrong key (`lifecycle_class` vs `lifecycle.enum`/`.polarity`) -- **which returned an empty enum, after
which my polarity check PASSED VACUOUSLY on the empty set**; a case-sensitive match against an
uppercase verdict; and universal fields sought per-class instead of at `contract_record.required`.
Negative controls + re-derivation produced the 19/19; the first run would have sent CVO~Z hunting
drift that does not exist.

**AND MY ITEM-13 CHECK HAD NO MUTANT.** CVO~Z's did -- a 1-byte flip inside `variance` was DETECTED.
**Mine merely did not fail; theirs could have and didn't. Only one of those is evidence**, and I had
spent the night invoking that exact standard at other people.

**TWO CORRECTIONS FOLDED AT THE GATE, both self-reported by their authors before landing:** `~C`
caught a FALSE STATEMENT in its own handoff (a comp-kuzu query recorded as *"timed out and returned
nothing"* had been backgrounded and **completed, exit 0, with 3 rows**) -- *a tool's non-return
standing in for a null result*, the same defect as item 17 one level down. And `variance.Orphan`'s
population stays **UNKNOWN, bounded above by 7**; `bd-gold-qa-runner-forgotten` suggests one entry may
have a SIBLING and thus never have been a candidate, explicitly **not** computed.

**FINAL TALLY -- FOUR SEATS, EIGHT DEFECTS IN ONE ARTIFACT IN NINETY MINUTES, AND EVERY SEAT ALSO
SHIPPED A LYING INSTRUMENT** (~C three, me three, CVO~Z two -- including a token check that would have
**forbidden the rule bank from documenting its own prohibition**). **Not one was caught by care. Every
one was caught by a control, a positive control, a negative control, a mutant, a noticed
inconsistency, or a peer.**

**V-1, NEW, CVO~Z's surface (LD-0319):** `comp-system --check` reads CURRENT off the **DISK** while the
**COMMITTED** artifact still carries stale counts (91/70 vs a true 90/69) -- the DESIRED-vs-APPLIED
inversion pointed at the parity surface itself. Ruled: land the 10 substantive lines EOL-preserved,
**scoped to their 3 files, NOT the 11 stash-entangled ones**, with a diff-size control BEFORE push.
Their measurement independently corroborates the site-Z EOL condition in section 6: **12 tracked
files, 11 of them inside `stash@{0}`**, stored blobs CRLF against `core.eol=lf`.

**Item 17 disposition (CVO~Z as verifier, accepted):** measured before the GATE IS WRITTEN, not before
the vocabulary lands. Now a prerequisite for increment 2's gate authoring, not an optional extra.
