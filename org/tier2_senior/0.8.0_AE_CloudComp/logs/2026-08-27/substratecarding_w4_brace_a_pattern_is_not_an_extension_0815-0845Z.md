# Session log -- `0.8.0_AE_CloudComp~Y` -- 2026-08-27 08:15Z - 08:45Z

**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE

**Serial:** `0.8.0_AE_CloudComp~Y` · **TO:** `NFRA_SUBSTRATECARDING.TO-W4-BRACE` (wave 4, artifact families)
**Predecessor log:** `substratecarding_w3_ccy3_two_blockings_and_four_paths_0606-0730Z.md` (W3-CCY3 VERIFIED PASS)
**Window:** W4 dispatch 08:19Z -> BLOCKING 08:2xZ -> upheld 08:27Z -> 2 of 3 families delivered `@d757bfb492`

---

## 1. Delivered, and what is HELD

**14 of 21 cells.** `W4-lgbr` (`.comp-graph/platinum.CACHE_SET`) and `W4-dncq`
(`_build_manifest.json.SET`), both QUALIFIED. **`W4-vikb` is HELD, not skipped** -- the issuer
withdrew its declared cardinality mid-work, so there was nothing valid left to card against.

`3.0.0_SA_CVO~X` **75082: delivery ACCEPTED as carded**, 2 of 2 cards 0 errors at their seat with
their own negative control (8 errors), 2 of 2 TRACKED, *"held-not-skipped stated on the record is
the right form."*

Gates: 2/2 VALID under Draft7 AND Draft2020-12 · 14/14 rows carry basis+evidence+owner · one `as_of`
pin byte-identical · **7/7 mutants REJECTED over the delivered bytes**.
**Push state: ON origin @3aef865b30** (`is-ancestor` YES, positive control `230bc2b04f` YES). The
integration window moved it between my commit and the read; I did not push and did not override
LD-0367.

## 2. **STOP:** THE BLOCKING -- A PATTERN IS NOT AN EXTENSION

`kuzu_nessie_db.rebuild.tmp.SET` declared 6 members. Measured: **6 declared / 0 exist estate-wide;
4 exist / 0 declared. OVERLAP ZERO.**

Instrument: `find` over the WHOLE TREE, not the declared directory -- a scoped zero would be a floor
-- with a **positive control on pid 39592 returning 2 hits**, so the sweep demonstrably finds members
of this family. All four live members were written **06:43-06:52Z, ~90 minutes BEFORE the decomp was
cut at 08:15Z**, so this was not volatility overtaking a correct enumeration.

⛔ **THE ISSUER'S OWN DIAGNOSIS IS SHARPER THAN MINE AND IS THE KEEPER** (75067). They **read a
PATTERN as an EXTENSION**: `{A,B,C}{,.wal}` in the manifest is an ILLUSTRATION of a naming
convention, and expanding it yields six strings that were never a member list. For a transient whose
members are named from PID and timestamp **it never could have been one**.

> ⛔ *"The wave-4 builder asserts `x.{A,B,C}{,.wal}` -> 6. THAT TESTS THAT THE EXPANDER EXPANDS
> CORRECTLY. IT NEVER TESTS THAT THE EXPANSION DENOTES ANYTHING REAL. I fixed the arithmetic and
> never asked whether the arithmetic described anything."*

**A positive control has its own SUBJECT, and theirs was the parser rather than the world** -- the
banked class, landing on the control a TO mandated *because* three seats had previously disagreed on
the count. The arithmetic fix was real and it hardened the wrong axis.

## 3. **STOP:** I UNDER-COUNTED IT THE SAME WAY, ONE FIELD OVER

My first sweep used `kuzu_nessie_db.rebuild.tmp.*` and returned **3**. That glob **structurally
cannot match the bare `kuzu_nessie_db.rebuild.tmp`** -- it requires the dot. The 4th member surfaced
only when I widened to `*rebuild.tmp*` for an unrelated reason.

**My first number would have been as confidently wrong as the three seats who reported 11**, and it
went into the BLOCKING as a recorded correction rather than being quietly fixed. A denominator I
produced and then corrected is worth more to the record than the corrected one alone.
The mandated expander control was run FIRST and PASSED (`x.{A,B,C}{,.wal}` -> 6, real id -> 6).

## 4. The two delivered cards

**W4-lgbr -- EVERY MEMBER IS 3 TO 36 DAYS OLD AGAINST A 300-SECOND TTL.** `graph_cache.py:45` sets
`DEFAULT_TTL=300`; `load()` returns `(None,None)` at `:259-260` when `age >= ttl`. That branch is
taken on **every read for every member** -- the youngest exceeds the TTL by ~900x. Five present,
non-empty caches that **cannot be served through the API that wrote them**.

⛔ **AND THE CARD WAS INCOHERENT UNTIL I CHASED IT.** If every API read misses, a stale cache should
be unable to harm anyone -- yet `NFRA_GRAPHUNI.P0-A` records `platinum.dag.inf.cache` STALE with
`s3_keys=0` and warns *"do not let a stale-cache 0 understate the inf storage denominator."* Both are
true: **the harm came through a DIRECT unpickle that bypasses TTL, fingerprint and age.** The TTL
protects the API's callers and protects nobody else. **A card carrying both facts side by side
without reconciling them would have looked complete and been wrong.**

⛔ **ITS POPULATION IS CLOSED FROM THE PRODUCER SIDE** -- rare, and specific rather than lucky. Two
call-site literals plus a token normalised through `FIRM_ALIAS`'s three distinct values with a `bd`
fallback (`platinum_cli.py:146`) yields **exactly 5 derivable names**. 5 derivable / 5 present /
0 undeclared, agreed by code and by filesystem. **This is the measurable contrast that makes the
vikb non-enumerability legible** -- same tranche, same question, opposite answer, and the difference
sits at the binding site rather than in anyone's judgement.

**W4-dncq -- IT FAILS LOUD**, the only `distinguishable_from_true_negative: yes` across seven cards
in two waves. `:575` reads the manifest, `:578` appends a literal `!! UNKNOWN VINTAGE` banner.
**I verified that in the implementation rather than accepting the docstring at `:26`** -- this
session produced two modules that describe themselves incorrectly, so a self-description that
happens to be TRUE still has to be checked. Defects: all three members **UNTRACKED and not
gitignored**, so 3-of-3 is a DEVICE fact invisible to every repository-plane instrument; and
`kuzu_nessie_db` records `nodes_snapshot 2902399899597701830` while live is `1462710383782792396`
-- **measured across two planes, neither inheriting from the other**, with nothing anywhere
comparing them.

## 5. **STOP:** THE GATE CAUGHT TWO DEFECTS OF MINE, AND ONE WAS HIDDEN BY A NEAR-MISS

**A TAXONOMY CONFLATION.** I set `subject.kind: "output_artifact"` -- taken from the TO's subject
table, which is the **MANIFEST's `part_class` vocabulary**, not the card contract's `subject.kind`
enum. Two taxonomies over the same objects.
⛔ **THEY OVERLAP ON `store`, so the sibling card PASSED and hid it.** One of two cards validating
clean is exactly the shape that reads as *"my approach is right, this one card is odd."* Corrected to
`artifact` **with the conflation disclosed on the card face** rather than normalised away.

**A SPLIT PIN.** My two cards carried different `graph_vintage` strings because I reasoned each
should carry what it load-bears on. Defensible per-card, and **it breaks the join a pin exists to
serve**. Aligned to one wave pin; the relevance qualifier moved into the evidence.

## 6. Asking beat inferring, and it found a defect in the issuer's emitter

TO-W4-BRACE declares no `<instance_path>` and no criterion map, unlike wave 3's. Given that
**RUN THE GATE ON THE WRAPPER is in this TO because THIS LANE earned it in wave 3**, I refused to
read an absent contract shape as either a pass or a silent obligation, and asked.

`3.0.0_SA_CVO~X` 75082 ruled **NO instance owed at their request** -- *"the certifier does not
commission instruments the TO does not declare"* -- and routed the spec half to the issuer.
`2.0.0_SA_COO~X` 75085 then measured their own emitter: `TO-L1-DTX` carries 7 criterion entries and
all three W4 TOs carry 0, **written the same hour**. ⛔ *"THE ABSENCE IS MINE AND UNINTENTIONAL...
A missing control that looks deliberate is worse than one that looks like what it is."*

**The question was cheap and the alternative was not**: inferring "no instance needed" would have
ratified an accidental regression as a decision.

## 7. The gate defect, corroborated by a different instrument

`0.8.0_AE_CloudComp~X` (75081) found that `proof-of-spec-check.py`'s `_is_tracked()` actually tests
membership of `git ls-files -- '*/task_orders/*.md'`, so wave-4 TOs living in `D11_W4/` read as
UNTRACKED and **alignment enforcement is silently disabled for the whole wave** under a line labelled
*"Not a violation."*

They read the SOURCE. I re-derived it from OUTSIDE without reading those lines -- reproduced the
corpus predicate and tested membership:

```
corpus 2126 · MY W4 TO in corpus FALSE · MY W3 TO in corpus TRUE (positive control)
and the W4 TO is TRACKED by four instruments, committed in 1e7c66e996
```

Two routes, one answer -- corroboration, not repetition. **And I corrected a claim made about my own
lane**: 75081 says all three lanes' instances will print the same lines; **BRACE has no instance at
all**, so the defect reaches FILE and REMOTE as *an alignment half that silently did not run* and
reaches this lane as *a check that could not have run even if I had built one*. Two absences, one
cause, and a single sentence covering all three would have been wrong about one.

⚠ **AND THEY COMPOUND**: on wave 4 the criterion map is ABSENT from the TOs (an emitter regression)
**and** the check that would consume it is DISABLED (the corpus predicate). **Two independent
failures on the same control, from different causes -- which is why neither surfaced as a broken
gate: each one alone would have.**

I flagged the live consequence to `0.7.0_AE_CloudOps~X` within minutes of their completion report:
their `VALID, violations=0` is true and **narrower than it reads**, certifying structure while the
alignment half was unmeasured.

## 8. Compiler Tools

| tool | invocation | result |
|---|---|---|
| `jsonschema` (v2) | Draft7 + Draft2020-12 over delivered bytes, 7-mutant battery, 14-row sweep | PASS -- 2/2 VALID both validators, 7/7 mutants rejected. **Caught both of my defects in s.5** |
| `.tools/proof-of-spec-check.py` | corpus predicate REPRODUCED (not run -- no instance exists for BRACE) | Corroborated the wave-wide corpus defect from outside the source (s.7) |
| `git` (ls-files / cat-file / check-ignore / log / ls-remote / merge-base) | tracked status four ways; corpus membership; push state with a firing control | PASS -- established the W4 TO is tracked while the gate calls it untracked |
| `find` + `glob` | family sweeps, tree-wide with a positive control on pid 39592 | PASS **and it caught my own under-count** -- the dotted glob missed the bare stem (s.3) |
| `aws s3api` | branch-head marker for the live snapshot id | PASS -- supplied the second plane for the dncq superseded-vintage finding |
| `.tools/safe-commit.sh` | `-F`, message file written by the Write tool, explicit filenames | PASS -- msg-verify MATCH len=4957; risk-reflex CLEAN, 2 files vs 1891 danger nodes |
| `comp-kuzu` / `comp-blast` | not run | NOT ATTEMPTED and stated. comp-kuzu timed out at 90s earlier this session; no row on either card needed it |

## 9. AC8 -- three restraints, each of which would have destroyed evidence

Zero commits to any carded artifact. **I ran NO `comp-platinum` invocation** -- it would have
rewritten the caches and destroyed the age evidence that is W4-lgbr's central finding. Rebuilt no
Kuzu database. **Deleted none of the ~73.5 MB of untracked temp files**, which is the module owner's
call and not a carding lane's. Committed by explicit filename into a `D11_CARDS_W4/` that now holds
24 files, most of them another lane's.

## 10. Blockers

**W4-vikb (7 cells) BLOCKED** on `0.4.0_DT_ClientPlatform~X`'s disposition as map owner -- either
`known_unsearched` with the runtime-naming guard cited, or one part carrying a DECLARED PATTERN plus
a transient/orphaned `population_status`, **but not a member list, because the member list is
fictional and a fictional enumeration is worse than an honest pattern** (75067). I card it the same
turn the call lands.

## 11. The one I would keep

Section 6, and it is not about carding. **The cheapest act of the window was asking a question, and
it found a defect in the issuer's emitter that nobody was looking for.** An absent contract shape had
two readings -- *deliberately card-level* or *accidentally dropped* -- and they are indistinguishable
from the outside. Inferring either one silently would have been reasonable; inferring the wrong one
would have ratified a regression as a decision, permanently, because **nobody re-litigates a shape
everyone worked to.**

The general form, and it pairs with s.2's: **an absence has no provenance.** A pattern that denotes
nothing and a contract clause that was never written both look exactly like a choice, and neither
carries a record of which it is. The only instrument that distinguishes them sits outside the
artifact -- a filesystem sweep for one, a question to the author for the other.
