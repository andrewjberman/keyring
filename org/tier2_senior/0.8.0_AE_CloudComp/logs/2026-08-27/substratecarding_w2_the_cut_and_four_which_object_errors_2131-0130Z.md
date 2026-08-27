# Session log -- `0.8.0_AE_CloudComp~X` -- 2026-08-26 21:31Z - 2026-08-27 01:30Z

**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE

**Serial:** `0.8.0_AE_CloudComp~X` · **TO:** `NFRA_SUBSTRATECARDING.TO-W2-CCX2` (wave 2, CUT SHORT)
**Predecessor log:** `logs/2026-08-26/substratecarding_c0_c1_c2_cards_1728-1900Z.md` (+ annotations s.12, s.13)
**Window:** wave-2 GO (73743) -> Andrew-direct cut (74234) -> wave close (74310)

---

## 1. What this window was

Wave 2 of D11: 11 subjects / 77 cells, "the definitions as they stand currently". **Cut short by
Andrew at the delivered boundary after I had written 6.** The 6 are committed and stand; 5 subjects /
35 cells are **SCOPE-SUPERSEDED, never abandoned** -- one word apart, opposite wave-3 actions.

⛔ **The durable output of this window is NOT the cards. It is four which-object errors, three of them
mine, and the one I did not make.**

## 2. Delivered

**`1c2359c931`** -- 6 cards, all VALID against `SUBSTRATE_CARD.v2.schema.json`, all QUALIFIED:
`#relations` · `#roles` · `#node_bindings` · `#non_relation_edges` · `#relation_composites` ·
`#c1_frontend_adapter`. Card-level battery green at CVO~X's close. **No proof-of-spec instance --
ruled NONE-OWED (74275): an instance over the original 77 cells would assert criteria over 35 cells
that no longer exist. A false claim, not a paperwork gap.**

## 3. **STOP:** THE THREE WHICH-OBJECT ERRORS I COMMITTED

**Every one produced a well-formed, confident, internally-consistent claim about the wrong object.
No instrument at any seat detects this class** -- `3.0.0_SA_CVO~X` stated it against their own
re-check (74156): a narrow delta-check verifies the delta was as DECLARED and **structurally cannot
verify the TRUTH of an added claim.**

| # | error | how it was caught |
|---|---|---|
| 1 | **C1: block KEYS vs block CONTENTS.** Said 31 of 53 edge_types bound by no declared block. Truth: **0**. Each relation carries `binds_up: [...]` -- 47 physical names -- and I read only the keys. | carding `#relations` in wave 2 |
| 2 | **C2: one script vs two.** Said `MOTIF_c2c3_materialize_spec.py` produces "the two" class-spec JSONs. It writes ONE (`:44`); the canonical 13 come from `NFRA_MOTIF_P1_canonical_ab_catalog.py:58`. **THREE materializers.** | carding that script |
| 3 | **C2 again -- in the FIX for #2.** The script I named writes only the **DEVIATION subset**, which the rule bank's own law says must *"NEVER be presented as the C2/C3 layer itself."* I presented it as exactly that **while correcting a different error in the same card.** | carding, one step further |

⛔ **#1 IS THE ONE THAT SHOULD NOT HAVE HAPPENED: I had already caught the identical error in the
SIBLING card and written it up.** C0's `key` row records it in my own words -- *"that comparison was
against the wrong object"* -- and I committed it again in C1 **in the same session**, because for C1
I *did* open two of the four blocks. **Partial contact with the right object is what made the wrong
object invisible.**

## 4. **STOP:** THE FOURTH ONE I DID NOT MAKE, AND WHY IT MATTERS MOST

Measured: the entire globgrph module makes boto3 clients for **three services** (s3 37, sns 1, sqs 1).
No ec2, no lambda, no iam. Yet the graph carries LAMBDA 198 / IAM_ROLE 206 / EVENT_RULE 137 /
EC2_INSTANCE 32. **My wave-1 C0/C1 cards say the estate composes from "CloudTrail management events +
service describe scans."**

The evidence pointed hard at *my card is wrong*, it was the fourth instance of a class I had been
wrong about three times that night, and **filing the correction would have felt like the disciplined
act.**

**I stopped at "I have not located the producer."** My search for it returned **0 hits over 27,028
files on a pattern I invented** -- and a zero over a guessed predicate is a FLOOR, not an absence.
Marked the claim **UNVERIFIED, not falsified.**

⛔ **THE CLAIM WAS TRUE.** `1.0.0_SA_CTO~X` located both producers within the hour:
```
FULL         comp_aws_cli.py (org/modules/graph/, 158KB, 79 describe sites)  <- reached by sys.path insertion
INCREMENTAL  infra/aws/lambda/globgrph/incremental_updater                   <- CloudTrail events -> live describe per ARN
```
**"CloudTrail management events + service describe scans" names BOTH mechanisms correctly.**

> ⛔ **A FALSE CORRECTION IS HARDER TO REVERSE THAN A FALSE CLAIM.** A claim invites challenge; a
> self-retraction CLOSES the question, and nobody re-litigates a withdrawal. **Filing it would have
> withdrawn a true claim permanently.**

**And my module census was confirmed correct by CTO~X: *"correct, and blind -- the file is in another
tree."*** The measurement stood; the tree was wrong.

## 5. The reopen test, run before escalating

At 00:0xZ -- ninety minutes after the subject set was FROZEN -- I found what looked like an uncarded
materializer. **The available move was to file BLOCKING.** The freeze (73965) defines reopening as *a
head the resolution map does not account for -- a measurement any seat can run*. **I ran it:** both
objects IN MAP, the third materializer already another lane's subject, frozen set COMPLETE.

**So it was a defect in my card, not a gap in the wave's scope**, and I reported it as a correction
with that distinction explicit. `2.0.0_SA_COO~X`: *"a BLOCKING there would have cost the freeze ...
reopening it on a finding the measurement already accounts for would have retired the only thing
making the set trustworthy."* **First exercise of that criterion; it held.**

## 6. The finding the six cards carry

**The two rule-bank copies diverge on exactly the frontend adapter's 11 determinations -- SET-EQUAL,
zero residue both directions.** So the deliverables copy is the rule bank *before* that fold, which is
also why it lacks the adapter block entirely.
⚠ **The set equality is MEASURED; "the copy predates the act" is the READING.** No `git log -S` was
run, and a hypothesis-shaped result that comes out exact is the one nobody hedges.

Per block, with denominators: `#relations` mapping COMPLETE 53/53 but `governs`/`denies` ZERO live ·
`#roles` all 14 derive rules are **prose nothing evaluates**, 4 of 14 unbound · `#node_bindings`
PARTIAL BOTH DIRECTIONS (48/58 live bound, 11/59 named not live) and the bucket set **mixes roles with
handling policies** · `#non_relation_edges` 8/8 live, the healthiest · `#relation_composites` 1 of 3
declared-and-never-exercised · `#c1_frontend_adapter` its declared 3,912 reads 3,911 today, **reported
as a delta WITHOUT a drift verdict** because the two populations are not established identical.

## 7. v2 exercised -- the fix caught me on its first card

`basis_by_field` populated wherever provenance is mixed. ⛔ **The FLOOR RULE demoted four of my rows
from `measured` to `inferred`** -- v2 refused a `measured` scalar over an inferred `key_is_stable`, on
card 1 and three more after. **That is the fix catching a real over-claim by me, on the corpus it was
sized from.** `joinable_ref {id, note}` used throughout -- the fix this lane supplied the two-kuzu test
case for.

## 8. Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-kuzu` | node/edge censuses, provenance header read every call | PASS -- confirmed my read sat AT the wave pin; supplied every live denominator |
| `comp-find` | ~8 calls, each with **exactly one** of {content pattern, `--name`} | PASS -- 0 trap-shape calls; band grading load-bearing on the mapping hunt |
| `jsonschema` (v2) | 6 cards + negative control | PASS -- 6/6 VALID, control rejects a trust-removed card; **caught my `schema_version: 1` and the floor violation** |
| `.tools/safe-commit.sh` | 3 commits, `-F`, non-shell-written message files | PASS -- and see s.9 |
| `git ls-files` / `git log -1` | tracked status, per-file vintages | PASS -- turned the duplicate-copy question into measured binary facts |
| `aws events` + `aws scheduler` | both trigger planes | PASS -- carried from wave 1; scheduler plane confirmed no graph producer |

## 9. **STOP:** A COMMIT THAT TIMED OUT AND HAD ALREADY LANDED

`safe-commit.sh` hit SIGTERM at 2 minutes. **The commit had already landed** (`439764512d`); the
timeout was in a post-commit step. Index clean, no `index.lock`, nothing staged. **A blind retry would
have produced a duplicate or fought a lock.** I hand-ran the msg-verify the wrapper never reached:
3,137 intended vs 3,138 landed bytes, zero backticks, anchored subject match 1, exactly 3 files.
⛔ **A TIMEOUT IS NOT EVIDENCE THE ACT FAILED** -- same shape as the cross-fabric ledger rule, where an
unclosed entry is evidence *this device did not observe completion*, not that the work is unfinished.

## 10. Two other instrument errors of mine, caught before they cost anything

- **`grep -rl '64.4'` matched `_id 616484651842`** -- unescaped `.` is regex any-char. It reported my
  withdrawn figure inside **another lane's finished card**, and I nearly reported cross-lane
  contamination that did not exist. ⛔ **A predicate is not a neutral instrument when its output is an
  allegation about someone else's work.** Caught by checking WHAT the pattern matched, not the file list.
- **A substring filter on my own serial** matched a peer's subject record whose *spelling string* cited
  me, briefly looking like a 10-vs-11 assignment mismatch. Exact-match resolved it: 9+5+10+11 = 35.

## 11. Shared-directory hazard, surfaced

`~X` and `~Y` write into the SAME `D11_CARDS_W2/`. A commit declaring the DIRECTORY as its pathspec
sweeps the peer's in-flight cards under the committing lane's author line -- ⛔ **and `safe-commit`'s
contamination guard is structurally blind to it**, because the guard fires on files OUTSIDE the
declared pathspec and these are inside. I verified that before sending, and committed by explicit
filename. **The damage lands on the other lane: a card committed, attributed to a seat that did not
write it. The false-attribution shape arriving through a pathspec instead of a pronoun.**

## 12. Blockers

**NONE.** Stopped on instruction, not on a block.

## 13. The wave's own lesson, and it is not mine

The cut happened because **the population was wrong** -- wave-1 `composes`/`projection_of`/
`co_resident_stores` hold artifact references AND prose descriptions, **one field two grains, Rule
24(ii) at the SOURCE** -- so a faithful harvest returned a mixed-grain set and 10 of 44 subjects
resolved to no openable artifact. Every instrument agreed: 44 subjects, 313 cells, alignment closed,
decomp CERTIFIED.

> ⛔ **A CERTIFICATION IS A STATEMENT ABOUT INTERNAL COHERENCE, AND INTERNAL COHERENCE IS EXACTLY WHAT
> A WRONG POPULATION PRESERVES.**

And the sentence I would keep over any of my own, from `2.0.0_SA_COO~X` after they laboured
SCOPE-SUPERSEDED-vs-abandoned at length and then blended VERIFIED with DELIVERED-UNVERIFIED **in the
same commit**:

> ⛔ **"Knowing the class does not make it fire at the site."**

## 14. State at close

D11 wave 2 CLOSED (74310). This lane: **6 DELIVERED + committed `@1c2359c931`**, 5 subjects / 35 cells
SCOPE-SUPERSEDED, no instance owed, **no deprecation verdicts on any card** (per `W2-m-3`: the tag is a
second pass AFTER carding, because a lane that decides a subject is doomed while carding it cards it
differently). Wave-1 C0/C1/C2 stand, amended three times under authorization, each amendment across
**three artifacts** -- card, proof instance, log annotation.
**Push state, measured with a firing control:** `1afca94ab8` ON origin; `1c2359c931`, `439764512d` and
this log LOCAL, riding integration.
**Next is MATERIALIZERS, and no decomp is cut until Andrew and `1.0.0_SA_CTO~X` settle the scope.**
