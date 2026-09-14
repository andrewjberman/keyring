# /self-drive AMGT_RESAPP & POSN_ASTTAX -- tick 105 (covers ticks 103-105) -- A LAW EDIT, A CITING AMENDMENT, AND AN INSTRUMENT DEFECT FOUND IN A DOCUMENT THIS SEAT CO-OWNS

**seat:** `1.0.0_SA_CTO~Z` · **state:** ARMED · **device:** sitez · **2026-09-14T08:12Z**
Tick 102's log is `@5a6bbf11b6`. Delta-driven, not the floor: the floor would not have fallen until tick 108.

> **THE BLOCK'S SHAPE:** two committed acts of this seat's own, one CLAUDE.md law edit with its three
> surfaces, one merge window held and answered, one defect found in a reader that had existed on this
> device for six minutes -- and **three corrections to things this seat published, one of which I
> caught myself and two of which I did not.**

---

## 1. `Z-S79`: CONFIRMED, THEN WIDENED, THEN CARRIED ON THE RIGHT CARRIER

`2.0.0_SA_COO~ZZZ` filed `AMGT_RESAPP-Z-S79` with this seat as **disarm owner**: `get_agent_status`
is lane-aware on one limb and lane-blind on two. **Confirmed here on a separate instrument** -- 28
files in the base folder, `pending` 6, lane tally `{3.0.0_SA_CVO~Y: 6}`. Total contamination, not
partial.

⛔ **AND IT LANDED ON A CLAIM OF MINE.** After retiring `bridge-state.json` I named "the broker
summary" as a sound instrument, as if the call returned one thing. **The limb I actually relied on is
the lane-aware one** -- so the verdict held by luck, and *a verdict resting on the sound limb of a
mixed instrument is indistinguishable, from the inside, from one resting on a blind limb.*

### The second sign, and it is worse than the first

| sign | mechanism | direction |
|---|---|---|
| TOO BIG | filter is `<status>`; `<issued_to>` never consulted | foreign lanes' work counted |
| TOO SMALL | `<status>` is FREE TEXT and the match is EXACT | real open work hidden |

**The discriminating test nobody had run.** `3.0.0_SA_CVO`'s folder holds **0** prose-`pending`, so it
cannot tell exact-match from prefix-match. `0.7.0_AE_CloudOps` holds both:
```
my parse, 402 files ...... EXACT 'pending' 3  |  PROSE-'pending' 2
the broker, same breath .. "## Pending task orders (3)"     -> EXACT-MATCH, PROVEN
```
The two hidden orders are `OPAL_ADVIPOINTERS.P4-PUBIAM-49F` (*"GATE CLEARED 2026-09-01"*) and
`P5-TEARDOWN-49F` (*"HELD ON THE FRAMEWORK P5 GATE"*). **Both GO'd. Neither terminal. Neither visible.**

**Right-domain census**, over the population the section actually reads (per-seat `task_orders/`):
```
88 folders | DENOMINATOR 2278 orders | exact 1483 | PROSE 679 | no <status> tag 116
55 of 88 folders carry prose | 31 orders GENUINELY OPEN AND INVISIBLE
```
⭐ **Two of those 31 carry the remedy inside their own status text** -- *"THE LEADING TOKEN WAS
`pending` AND THE BOARD REND..."*, *"THE BARE TOKEN `active` NOW LEADS THIS FIELD."* **This fabric has
met this defect before, fixed it one file at a time, and never fixed it at the reader.**
Corroboration from outside the thread entirely.

## 2. THE THREE CORRECTIONS

| # | what I published | what is true | who found it |
|---|---|---|---|
| 1 | the 28-vs-24 gap was "most likely different admission rules -- my census admitted one `**group` artifact, which is not an order" | **0 of 28 lack a `<status>`; all 28 are orders.** The `**group` entry is a real order whose VALUE is prose | `2.0.0_SA_COO~ZZZ` |
| 2 | "pushing now that the window is shut" (22541) | push on shared `SITEZ` is the integrator's act; **nothing was pushed**, as every other commit tonight | **me**, before anyone had to |
| 3 | the widening test = "a non-CVO **LANE**" (22515) | **a LANE is not a POPULATION** -- the under-specified test let a clean wrong-domain read look like an answer | its consequence, via `2.0.0_SA_COO~Z` |

⭐ **#1 IS THE ONE TO KEEP, AND IT IS SUBTLE.** 22513 made a point of **printing** the 28-vs-24
discrepancy rather than smoothing it away -- and then closed it with a hypothesis in the next clause.
⛔ **A PRINTED DISCREPANCY CARRYING A LIKELY EXPLANATION IS CLOSED IN THE READER'S MIND EXACTLY AS
FIRMLY AS A MEASURED ONE, AND IT IS WORSE THAN LEAVING IT OPEN:** the word *unreconciled* recruits the
next reader; *most likely X* dismisses them. **All 28 files were open in the same call. Listing which
four differed was one line.** I did the cheap half and dressed it as the expensive half.

⚠ **AND MY OWN PARSER HAD THE ANSWER AND I MISREAD IT.** My census bucketed on FIRST TOKEN and printed
`complete 17 | pending 6 | ... | '**group' 1`. Exact `complete` is **8**, not 17. **A value that
obviously was not an enum, sitting in a column I had labelled as one, was the loudest possible tell
that the field is prose -- and I filed it as evidence of a non-order file.** The anomaly was the
finding; I used it as the excuse.

## 3. ⭐ THE CLEAN READ THAT COULD NOT HAVE FAILED -- RULE 24'S GREEN, MEASURED

`2.0.0_SA_COO~Z` took the widening test I named and measured POSN_ASTTAX: **19 of 19 single-token, 0
prose**, offered -- reasonably -- as *an argument AGAINST widening*. **Its instruments were the right
ones and deliberately chosen** (`ls-tree` with separated argv, no `2>/dev/null`, whole-value census).

⛔ **But it read `org/missions/D4/POSN/POSN_ASTTAX/task-orders` -- the PROJECT TREE folder, hyphen --
which the broker never reads; and that folder holds 15 `complete`, 4 `staged` and ZERO `pending`, so
it could not have discriminated exact-vs-prefix in either direction.**
>> **A CLEAN RESULT FROM A POPULATION THAT CANNOT EXPRESS THE DEFECT IS NOT EVIDENCE OF ABSENCE.** And
   the failure mode is the one Rule 24 names by name: **THE GREEN.** A wrong-domain read returning
   non-empty gets argued with; returning EMPTY it gets ACTED ON. **That green would have closed a live
   fabric-wide defect.** The under-specified test was mine. <<

## 4. THE RULING, AND WHY THE REC WAS DECLINED

`2.0.0_SA_COO~ZZZ` (22529) found the mechanical gap: `Z-S79`'s committed `notes` carry the NARROW
condition **as an `OR`**, so scoping to `<issued_to>` alone disarms it on its face while the free-text
defect runs. Three options offered; **REC was (c), record the widening in this seat's tick log.**

⛔ **DECLINED, because (c) has the exact defect it identifies.** 22529's own argument is that *a
disarming seat reads the ROW, not the log.* Putting the constraint in a log is **the same error as
siting a round-5 precondition in the round-3 ledger** -- which this seat committed once tonight on
POSN_ASTTAX and does not need to commit twice.
⭐ **AND A CITING ROW IS NOT A SECOND CARRIER.** A second carrier is an INDEPENDENT row asserting the
same condition with its own disarm path. `Z-S80` is **INERT by construction**, creates no path, and
only rewrites the condition on `Z-S79`, which **REMAINS ARMED**. Append-plus-cite is the channel's own
amendment mechanism -- the same shape a disarm row uses.
**The filer offered to author it; declined with thanks.** The ruling is this seat's and the provenance
should say so.

## 5. THREE ACTS COMMITTED

```
Z-S80         @e1a4e917f2  the citing amendment -- disarm condition WIDENED to TWO SIGNS, both required
Rule 22a      @854dc8ae4e  CLAUDE.md gains ROSTER: three limbs, two base-scoped and exact-matching prose
(relay)       msg 22541    sequence-check --project silently passes a typo -- to the laptop CTO
```
**`Z-S80` guards:** anchored insert at the file's unique closing structure, wrong-file guard (both
`Z-S79` and the project key asserted), id-collision refusal, edit-scoped ASCII guard, and a post-edit
**JSON re-parse asserting rows 144 -> 145 with the fence count unchanged**; `Z-S79` verified still
ARMED after the write. Gate: `1 new row of 145 total checked (144 pre-existing, NOT re-graded)`.
**Rule 22a guards:** unique anchor inside 22a, already-present refusal, ASCII guard, and **POSITIONAL
asserts that the clause lands AFTER the 22a header and BEFORE rule 28** -- the property the siting
depends on. Rule 28 verified intact.
**Three surfaces honoured:** commit + same-turn broadcast to the **five LIVE seats read from the
roster this breath** + push state stated **as LOCAL** in the broadcast itself.

## 6. THE MERGE WINDOW, AND THE FOREIGN-STAGE THAT WAS NOT ONE

`0.0.0_AB_MSTR~Z` opened a window (22517) and asked for commits to hold. **Held.** Rather than take the
offered silence-as-clear, I measured and answered -- and the measurement found **two files STAGED
under my own `deliverables/`**, which is exactly the shape `safe-merge.sh` refuses on.
```
git rev-parse -q --verify MERGE_HEAD ... 56608aadd4 == origin/CLOUD tip, EXACTLY
ls-tree (separate argv):  SEQUENCE_DOCUMENT_APPROVED.md  CLOUD 1 | SITEZ 0  -> arrives with the leg (A)
                          ROUND_ANALYSIS_IRPT_FNTEND...  CLOUD 1 | SITEZ 1  -> updated by the leg (M)
                          org/XXX.md (CONTROL, same shape)             1 | 1
```
**The integrator's own merge, in flight.** Nothing reset, aborted or stashed. ⭐ The discriminator that
settles it is `MERGE_HEAD`, **not the file list** -- and three seats independently reached that same
discriminator on the same window.

## 7. ⛔ THE DEFECT IN A DOCUMENT THIS SEAT CO-OWNS, FOUND ON THE FIRST READ

The leg made `org/missions/SEQUENCE.yaml` readable here. `/self-drive` Step 0.7 makes
`sequence-check --project <CODE>` **mandatory before starting work on a project.** Four arms:
```
A  --project LGIC_NAMING  (placed)     projects: 1 + the row, prd ADMITTED   rc=0   <- positive control
B  --project AMGT_RESAPP  (unplaced)   projects: 0  FLAGS: none              rc=0
C  --project ZZZZ_NOSUCH  (impossible) projects: 0  FLAGS: none              rc=0
D  --project LGIC_NAMNIG  (TYPO of A)  projects: 0  FLAGS: none              rc=0
```
**B, C AND D ARE BYTE-IDENTICAL, AND THE OUTPUT NEVER NAMES THE PROJECT IT WAS ASKED ABOUT.** So a
seat that types `ADVI_FIRMBKTS` with one character wrong is told `FLAGS: none`, `rc=0` and **steps
over the one HOLD the document exists to enforce**.
>> **THE DIRECTION IS THE REASSURING ONE AGAIN.** A wrong code returning an ERROR is fixed in five
   seconds; a wrong code returning a CLEAN PASS is acted on. **`enforcement: TRACK` does not soften
   this** -- TRACK means the reader flags and the CTO raises, so a reader that cannot flag IS the
   mechanism, not a warning layer above it. <<
⛔ **NOT PATCHED BY THIS SEAT.** `.tools/**` is lane ANY so the grant exists, **but a measured grant is
not a mandate**: this session is scope-bound, and a silent one-sided edit to a cross-fabric reader six
minutes old is how two copies of an intent begin. Raised with the reproduction for its author.
**First read as co-owner:** neither scoped project is placed, and the document **discloses** that
(`pending_placement: "the rest of both registers"`) rather than omitting it. **Placing nothing and
asking nothing placed today** -- placement is a co-owner's act on Andrew's word per the file's own
`change_log` rule, and neither project has an ordering constraint anyone has identified.

## 8. STATE AND COMPLETION

```
AMGT_RESAPP  ROUND_CLOSE  47 of 47 COMPLETE, 0 OPEN    round 9 at L9 with a bound adjudicator
POSN_ASTTAX  EXECUTING    15 COMPLETE / 4 ACTIVE of 19 round 4 at L9
             denominator 2618 tree+flat orders · ZZZZ_NOSUCH control = 0
next slug    REMEDIATION_v9 ABSENT · _v4 ABSENT · ROUND_ANALYSIS.round4 ABSENT -- correctly;
             prior-round controls (_v8, _v3, round3) all PRESENT, so ABSENT means absent
portal       gitlink e85f6eb84f == MERGED INDEX == origin/CLOUD == submodule checkout -- four planes;
             negative control fires (is-ancestor rg-2 -> gitlink = FALSE). Freeze intact.
OPEN CALLS   0 adjudicable · 2 RESERVED · NO PITCH  (all-reserved tell does not fire: 0 adjudicable)
  1of2 LIMB 6 widening -- 2.0.0_SA_COO~Z landed the joint close @dd6d2fce82, no longer mail-only
  2of2 list owner -- ANSWERED but NOT DONE; FWD-14 unrealized, Z-S78 unmet
COMPLETION   NOT DONE -- 0 of 2 (denominator: 2 projects, 2 of 14 live directives)
             REACHABLE 2 · UNREACHABLE 0 · HELD-AT-STOP NOT REACHED
```
**Push state:** local HEAD `854dc8ae4e`, `origin/SITEZ 750bbf82fe` (ls-remote), **5 ahead -- LOCAL**;
push on shared SITEZ is the integrator's act. **No TO cut, no dispatch, no apply, no promote, no
gitlink move.**

## Compiler Tools

`git rev-parse -q --verify MERGE_HEAD` as the foreign-stage discriminator, chosen over the file list
(and over `test -f .git/MERGE_HEAD`, which is vacuous in a linked worktree) · `git ls-tree <ref>
--name-only -- <path>` with **separated argv** for every existence check, never `cat-file -e`'s fused
`<ref>:<path>`, each with a **same-shape** present control · a `ZZZZ_NOSUCH` zero control on the order
census and an `org/NO_SUCH_CONTROL.md` zero control on the sequence-file check · prior-round
`REMEDIATION`/`ROUND_ANALYSIS` files as PRESENT controls so an ABSENT verdict discriminates · a
**FALSE-capable** negative control on the gitlink (`is-ancestor rg-2 -> gitlink` = FALSE), per
`2.0.0_SA_COO~Z`'s rule that an all-TRUE control set is uncertified · the exact-vs-prefix test
deliberately run on a seat holding BOTH kinds, because the folder in front of me could not
discriminate · `to-check.py` on `status_class` (**there is no `status` key**) · `ls-remote` for every
push-state claim · the **validator EXERCISED** rather than `.owned-paths.yaml` read as prose, after
that file's own warning that 18 notes describe a phantom gap · `safe-commit.sh -F` with message files
written by a non-shell writer · **and the heredoc that broke on apostrophes, rewritten to the
scratchpad rather than re-tried with more escaping.**
