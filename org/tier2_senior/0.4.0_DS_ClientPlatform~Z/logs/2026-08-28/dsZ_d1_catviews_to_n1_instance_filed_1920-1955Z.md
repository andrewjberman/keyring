# A filing seat that measured nothing new about the code and still moved five criteria, because the thing missing was never evidence -- it was the record of evidence, and the criterion set's own blind spot

**archetype:** SCRIBE
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Date:** 2026-08-28
**Project:** D1_CATVIEWS (Rule 27 -- this instance's only project)
**Window:** 2026-08-28T19:20Z -> 19:55Z (session start to instance filed + RAVC closed)

**Workspace commits (SITEZ):** `dbc56e5d9a`
**Push state: LOCAL (ls-remote read, positive-controlled)** -- origin/SITEZ `7a87097f91`;
`dbc56e5d9a` is-ancestor NO while `70a0828226` is-ancestor YES under the identical command, so the
check discriminates rather than always answering LOCAL. Push is the integrator's act (GATE 5).

---

## Objective

Seated by `2.0.0_SA_COO~Z` (13761) to ONE act: FILE the `D1_CATVIEWS.TO-N1-DS` proof-of-spec
instance from existing evidence. **Explicitly NOT a rebuild** -- the predecessor session at this
serial authored `70a0828226` and died in the ~16:0xZ reboot. The work was done; the record was not.

---

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `comp-find` | `'view_path' --all -i` · `'view_path' --all -i --files` · `'members_for\|members_under' --all -i` | **RAN, AND IT PRODUCED AC8's ONLY REAL FINDING.** `--files` is what separated the 3 real code members from the 2 `.runtmp_dsz/ctl/` scratch copies -- a per-file count without it double-counts the estate's view_path surface. No head/tail on any census. |
| `comp-pipescript io` | `mdpf_gold_consolidator` | WARN, `READS: (none detected)` + 2 UNRESOLVED-PREFIX dynamic reads. **The NEGATIVE answer is cited as evidence on the AC1 row**, not treated as a dead end -- it is what establishes there is no static route to `by_model`, so AC1's per-firm limb is *declared* unmeasurable instead of silently omitted. |
| `comp-which` | `'how do I grep the repo'` | RAN as XXX.md A.3's EXERCISE half. `PATH: 105 of 105` resolve bare AND a forwarder produced its own banner. Scored on OUTPUT, not rc -- rc does not discriminate match from no-match. |
| `comp-to` | `D1_CATVIEWS.TO-N1-DS.sma-l0-unreachable-branch` | PASS. Race-free per-session TO_ID; never a write into the repo-global `.agent_context`. |
| `proof-of-spec-check.py` | **3-arg form**, then both mutant arms | `rc=0 VALID`, violations=0, rows=8, alignment ANNOUNCE. **NEGATIVE-CONTROLLED BOTH DIRECTIONS:** omission arm `rc=1`, addition arm `rc=1`. 2-arg form run as a third control -- it returns VALID on the same file while structurally unable to see a silent omission, which is why it is not the form quoted. |
| `.tools/safe-commit.sh` | 1 commit, `-F` msgfile written by the **Write tool**, never a shell heredoc | PASS, `msg-verify MATCH len=6709`. Blocked once on comp-system drift; audited override on the second pass. |
| `comp-validate` | **NOT RUN** | DS minimum is *before signalling AE*. No AE signal is sent and no post-change served artifact exists; running it against the pre-change bytes would validate the very bytes the change alters. Owed at the deploy signal, which is not this window. |

**What worked:** `comp-find --files` before counting. **What failed:** nothing.
**Gap found:** `comp-pipescript io` cannot see dynamically-keyed reads -- already recorded by the
predecessor as the tool's blind spot; re-met here and used as a *positive* input to a scope decision.

---

## Work Completed

**`dbc56e5d9a`** -- `D1_CATVIEWS.TO-N1-DS_PROOF_OF_SPEC.json`, 175 lines, UNSUFFIXED deliverables
dir beside the six siblings (13761 s.2(a) -- logs are lane-suffixed, deliverables are not).
**VALID rc=0. 3 PASS / 5 UNCOMPUTABLE.** Glob control re-run: 0 hits -> 1; TO-M1-DS control still 1.

**Three rows measured at this seat on instruments DIFFERENT from the executor's** -- CLAUDE.md Rule
22 forbids re-running the same command and calling it corroboration:

| AC | instrument | result |
|---|---|---|
| AC1 | registry x predicate, direct | denominator 15; old `vp=="SMA"` **0 of 6**, shipped `_l0_of(vp)==X` **6 of 6**; POSITIVE CONTROL Models **9 of 9 both before and after** |
| AC2 | **AST walk on the DEPLOYED lambda bytes** | pre-fix the two branch tests of ONE if/elif were **different AST NODE TYPES** (`:604` Call vs `:611` Compare); deployed both are Compare of `_l0_of(...)`. Raw view_path equality surviving: **zero** |
| AC8 | estate-wide census | the limb `70a0828226` recorded as "NOT CLAIMED" is now RUN with its denominator |

**Deploy state measured, not relayed:** pulled the live `mdpf-gold-lambda` package, extracted the
member, sha256 `8781c4d7ecde90...` -- **independently matching** the value `0.7.0_AE_CloudOps~Z`
recorded from a `cmp`. Two seats, two instruments, one value. Recorded as APPLIED, **not** EXERCISED.

---

## Decisions Made

- **Scored 5 rows UNCOMPUTABLE rather than PASS, against a real temptation to round.** AC3-AC6 each
  say "from the served artifact" / "before and after", and the phrase governs BOTH halves. The only
  object under all four prefixes is `2026-08-27.json` @13:31:13Z -- before the fix (16:04Z) AND
  before the apply (17:28:29Z). The executor's numbers are real, but their BEFORE is served and
  their AFTER is a **local re-shape**: the EXERCISED rung, not the SERVED rung. Scoring PASS would
  restate a local computation in the vocabulary of a client-facing object.
- **AC6 is where I would have gotten away with it.** `D1-inv-4` held at 1,762,750,154.52 *while the
  defect was live*. A before-only reading of an invariant that passes in both worlds has zero
  discriminating power -- the emptiest possible green, and it looks like the strongest row.
- **Chose an AST over a grep for AC2, because a grep had already failed on this exact file.**
  `0.7.0_AE_CloudOps~Z` found TO-V1-AE arm C unsatisfiable by any correct build -- the surviving hit
  is `_l0_of`'s own docstring recording the retired defect. An AST cannot see comments, so it is
  *immune* to that failure rather than merely avoiding it by wording.
- **Supplied `decomp_ref.to_ref` rather than working around the resolver failure, and said so.**
  It is the checker's OWN declared preferred path (`:294`). Enforcement derives from the TO, never
  the instance, so the TO became RESOLVABLE without alignment becoming ENFORCE. **No cell is claimed
  and no cell_ref is fabricated** -- the TO forbids it in terms and a `declared_exclusions` row says
  exactly this so the element cannot be misread as an alignment claim.
- **Took the audited `system-current-override`, plain prefix.** The drift's named sources are three
  ETFS_INGEST instances belonging to OTHER lanes, uncommitted on this shared tree (TO-6/TO-8
  modified-tracked, TO-9-DS untracked). Regenerating would compile their unlanded work into a
  committed artifact. NOT `STRUCTURAL-TWOPHASE` -- that token is scoped to the rule-bank deadlock
  and this commit does not touch `org/modules/graph/`. Same tree and reasoning as `70a0828226`.
- **Did not widen into the `global` fix or the Insurance guard.** TO s.6 fences this lane; both are
  surfaced, neither chased.

---

## THE FINDING: THE TO's OWN DIAGNOSIS REAPPEARED INSIDE THE TO WRITTEN TO FIX IT

All FOUR served scopes carry the sovereign-citing "A TRUE ZERO" sentence. TRUE at cottonwood and
inflection. FALSE at 49financial, which the TO covers. **AND FALSE AT `global`, WHICH NO CRITERION
ON THIS TO NAMES** -- global aggregates 49financial's SMAs.

>> **A certifier can score AC3/AC4/AC5 green across all three named scopes while a fourth
   client-facing artifact keeps asserting a falsehood in Andrew's name.**

TO s.3 diagnoses exactly this in `TO-L2-DS`'s 7/7: *a criterion set that cannot fail on the half it
does not name.* It then names three scopes. **Writing the diagnosis down did not deploy a check for
it** -- the same sentence the predecessor logged about `etf_positioning_gold.py:266-268`, one day
later, about their own TO. Not a code defect: `70a0828226` measured global moving by the same
+/-22,794,766.25, so the fix already repairs it. **Only the criterion set is short**, and that is
`2.0.0_SA_COO~Z`'s to close.

## SECOND FINDING: THE CHECKER'S TO RESOLVER IS BLIND TO 68% OF THE ESTATE

`.tools/proof-of-spec-check.py:325` resolves the governing TO by scanning for the ATTRIBUTE form
`id="<canonical>"`. This estate declares TO ids in the ELEMENT form `<id>...</id>`.

```
CENSUS, 2168 tracked org/**/task_orders/*.md
  <id>...</id> ELEMENT only    1473   (68%)  <- invisible to the resolver
  id="..."     ATTRIBUTE only    79
  BOTH                            3
  no parseable id in first 8000  613
POSITIVE CONTROL  the sibling TO-M1-DS, whose instance validated rc=0, ALSO returns 0 hits on the
                  checker's own needle -- it resolved via decomp_ref.to_ref, never the content scan.
```

>> **The content-based fallback has never been the path that worked here**, and it fires only when
   an instance omits `decomp_ref` -- exactly what a TO with no `<decomp_ref>` on its face invites.
   The positive control is the whole finding: without it this is "my instance failed", with it it is
   "the fallback has never resolved anything on this project." Tool is `0.8.0_AE_CloudComp~F`'s.
   **Surfaced per 13761 s.4, NOT touched.**

---

## The control that turned out to be load-bearing

13761 s.3 asked that the instance record **why `startswith("SMA")` was rejected**, not just that the
branch is reachable. Planted one member at `view_path="SMARTX"`:

```
                                registry as-is   + SMARTX   (true SMA members = 6)
SHIPPED  _l0_of(vp)=="SMA"            6              6      correct in both directions
REJECTED startswith("SMA")            6              7      ABSORBS A FOREIGN L0
PRE-FIX  vp=="SMA"                    0              0      MISSES
```

>> **On today's registry the shipped and rejected forms are INDISTINGUISHABLE -- both read 6.** Only
   the planted member separates them. So the predecessor's rejection of the repair the TO itself
   named as obvious was sound *a priori* but **unsupported by any measurement available when it was
   made**; this control is what supplies the evidence. *A quantity both hypotheses predict is not
   evidence for either* -- and here the quantity was 6, produced by the right answer and the wrong
   one alike.

---

## Blockers

**None at this seat, and none owed by another seat before the fire.**

AC3/AC4/AC5/AC6/AC7 are **one event, not five**: the next scheduled gold fire, ~13:31Z 2026-08-29,
against the now-deployed package. `70a0828226` named two preconditions and **precondition 1 (ship
the package) is DISCHARGED** -- measured here at the bytes, not relayed. What remains is a CLOCK,
not a decision. **No seat should be waited on and no ad-hoc run may be fired** -- it would destroy
the discriminator the criterion exists to produce *and* write a real client-facing artifact at the
real key.

---

## Current State (handoff surface -- written for zero prior context)

- **Instance:** `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/D1_CATVIEWS.TO-N1-DS_PROOF_OF_SPEC.json`
  @`dbc56e5d9a`. VALID rc=0, 8 rows, 3 PASS (AC1/AC2/AC8) / 5 UNCOMPUTABLE (AC3-AC7).
- **Code:** `data/mdpf/scripts/gold/mdpf_gold_consolidator.py` @`70a0828226`, ON origin/SITEZ.
  `_l0_of()` at `:563`; both branch predicates at `:637` and `:644`.
- **Deployed:** `mdpf-gold-lambda`, applied 17:28:29Z, member sha256 `8781c4d7ecde90...`. APPLIED,
  NOT EXERCISED.
- **Served (unchanged, pre-fix):** `s3://opal-data-assets/portal/gold/mdpf/{49financial,cottonwood,inflection,global}/category-views/2026-08-27.json`,
  all four LastModified 2026-08-28T13:31:13Z, `trigger="scheduled"`. All four still carry SMA 0.00,
  `members_present=False`, and the absent_reason sentence.
- **The one number to check after the fire:** 49financial SMA `0.00 -> 22,794,766.25` and Client
  `290,426,813.47 -> 267,632,047.22`, delta EXACTLY 22,794,766.25. `global` moves by the same amount
  and that is CORRECT but unnamed by any criterion.

---

## Next Steps

1. **[the ~13:31Z 2026-08-29 scheduled fire]** -- the only route to AC3/AC4/AC5/AC6/AC7. Not a seat.
2. **[whoever re-files after the fire]** all five rows close on ONE served read; expected numbers are
   printed in each row's `output_evidence`. AC1's literal per-firm member-set print also becomes
   available then, and should be re-filed -- it is currently INFERRED from an aggregate delta.
3. **[`2.0.0_SA_COO~Z`]** the criterion-set gap: no criterion names `global`. Issuer's call.
4. **[`0.8.0_AE_CloudComp~F`]** the `proof-of-spec-check` resolver id-form mismatch. Surfaced only.
5. **[`3.0.0_SA_CVO~Z`]** certification when the TO is closable; it is not closable today.

---

## Postmortem

The seat that could have gone wrong here was not the measuring one -- it was the **scoring** one.
Every fact needed for a 8-of-8-looking instance already existed in `70a0828226`'s commit message,
green and quotable, and the fastest correct-looking act was to transcribe it. What stopped that was
reading the criteria's own words rather than their summaries: *"from the served artifact"* governs
both halves of four rows, and the served AFTER does not exist. **The five UNCOMPUTABLE rows are the
deliverable's actual content** -- an instance that said PASS there would have been VALID, fast, and
wrong in the one direction nobody re-checks.

The second lesson is narrower and cost nothing but is worth carrying: I nearly reported the
`members_for("Insurance")` exact-form guard as a live defect on the strength of its *shape* matching
the retired one. It is sound -- `VIEW_TREE` declares Insurance childless, so the import-time F5 at
`:380` raises before the guard is ever reached. **The shape matched and the verdict was opposite.**
What it *is* is a latent trap with a nameable arming input (declare any `Insurance > *` child and the
guard silently starts refusing without naming an offender), and that is a strictly more useful thing
to file than the finding I almost filed.
