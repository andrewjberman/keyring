# CVO~Z session log -- 2026-08-29 0210Z-0250Z: a criterion that COULD NOT PASS, and a floor run that COULD NOT LAND

**archetype:** VALIDATE
**secondary_archetypes:** MIXED (COORDINATE)

**Serial:** `3.0.0_SA_CVO~Z` (site-Z lane, Tier-1 CVO)
**Window:** since the 2125-2300Z log (`9381ec6c71`) -> ~02:50Z
**Authority:** Andrew-direct singular session priority -- *"finished pipeline, finished frontend
display, and new promote with all of it live, this session"*; *"everything must be done tonight."*

---

## 1. THE HEADLINE -- TWO THINGS STOPPED BEFORE THEY COST ANYTHING

```
  1  THE 2c ACCEPTANCE ORACLE COULD NOT PASS.  `git hash-object` (SHA-1 over a
     `blob <len>\0` header) can never equal `hashlib.sha256(raw)` -- 40 hex vs 64.
     It was minutes from gating a RESERVED-CATEGORY DELETE. WITHDRAWN by 2.0.0_SA_COO~Z;
     1.0.0_SA_CTO~Z adopted my replacement and ran it: 22 modules, 3 DRIFTED.
  2  THE FLOOR RUN COULD NOT LAND ITEM 1, and it was derivable BEFORE the run.
     Same trading day -> same as_of -> the SAME EXISTING KEYS -> conditional_put
     returns "conflict" and does not write.  MEASURED OUTCOME: conflicts=16, 16 of 16.
```

>> **THE DELETE IS THE ONLY THING THAT CAN LAND TONIGHT'S WORK, AND IT REQUIRES ANDREW'S EXPLICIT
   IN-SESSION WORD.** `0.7.0_AE_CloudOps~Z` refused to self-grant it and was right to. <<

```
  d213a1a3b2  ratifier: refuse a NEGATIVE fee-line value (the row c3 cannot be)
  936981e452  ratifier: score the item-1 Client L1 split; fix an over-broad NA branch
```

## 2. THE CRITERION THAT COULD NOT PASS -- AND WHY THAT IS THE DANGEROUS DIRECTION

`15325 s.4` proposed verifying the rebuilt package by matching `BUILD_MANIFEST`'s per-file sha256
against `git hash-object`. Measured on `mdpf_gold_consolidator.py` @`9dcc87dd5b`:

```
  BUILDER  build_package.py:418  hashlib.sha256(RAW bytes)   3c5e62f0...  len 64
  PROPOSED git hash-object       SHA-1 over "blob <len>\0"   825f2f97...  len 40
  POS CONTROL 88,960 bytes read . NEG CONTROL a different module differs
```

**They cannot match on any file, ever.** STOP: **THE HAZARD IS NOT THE RED -- IT IS THAT AN
INEXPLICABLE RED GETS RELAXED UNDER TIME PRESSURE, AND THE RELAXED FORM PASSES THE STALE PACKAGE.**
`1.0.0_SA_CTO~Z` reached the same conclusion independently and put my framing on the record.

**AND A SECOND, DEEPER LEG:** the manifest agrees with the source at the pin IT NAMES for **every
package the builder has ever produced** (`:413` -> `:418` -> `:434`, all one pin). `1.0.0_SA_CTO~Z`
then MEASURED it: **22 of 22 agree on the STALE package that caused the hold.** It certifies
COHERENCE, never CURRENCY. The leg that carries the predicate is `source_vintage.pin`, added on
this challenge.

WARN: **I ALSO OVERSTATED ONE BOUND.** I said `modules len == 22` cannot bound completeness -- true --
but the residual is smaller than I implied: `enforce_import_closure:173` is FAIL-CLOSED at `:210`
and `:225` with **no skip flag by design** (`:195`), so a package missing a required module
**cannot be built**. Scope: that fires at BUILD, so on a downloaded artifact the verdict is
INHERITED, not re-measured.

## 3. THE FLOOR RUN, PREDICTED THEN CONFIRMED

Predicted at 02:4xZ from `mdpf_gold_consolidator :946-1004`, before the result existed:

```
  the manifest path NAMES its own as_of:  _manifests/2026-08-27/20260828T221739Z.json
  a run at 22:17 local FRIDAY produced as_of 2026-08-27 (T-1) -> the next run, same
  trading day, same frontier, SAME DATED KEYS -> existing is not None -> business_equal
  -> item 1 flips Client from predicate 'unavailable'/children {} to 'available'/2 children
  -> NOT a process-time path -> "conflict", RECORDED, NOT OVERWRITTEN
```

`0.7.0_AE_CloudOps~Z` measured: **`conflicts=16`, all 16 dated gold keys conflict-held, the 16
objects built and none landed.** The publisher then re-projected the OLD gold, so platinum could not
carry item 1 either.

>> NOTE: **NOTHING MALFUNCTIONED. THE 16 CONFLICTS ARE A CONTROL WORKING** -- `conditional_put` refused
   to silently overwrite dated-immutable gold and recorded both sha256s per key. A pipeline that had
   overwritten them without a word would have looked smoother and been worse. <<

**AND THE FORK PUT TO ANDREW HAS TWO COHERENT LIMBS, which is why I supplied the second:** a NO
does not leave a defect in place -- **Monday's scheduled run has as_of 2026-08-28, a key that does
not exist, so `existing is None` and item 1 lands CLEANLY with zero deletes.** The cost of NO is a
weekend of old numbers on the card, not a broken pipeline. That is Andrew's trade to make.

## 4. THE ARMED HAZARD I FOUND WHILE LOOKING AT SOMETHING ELSE

```
  CLIENT_L1_RULE  3 keys   CLIENT_L1_HELD  1 key: ['cottonwood']   <- the ENTIRE hold set
  :787  global_client_l1_blockers() = the intersection -> ['cottonwood'] -> [] if lifted
  :800  client_l1_split(global, ...) then RAISES UnknownMemberError, no fallback
```

**Cottonwood is the ONLY blocker, therefore the LAST one. Removing the stale hold entry -- the
obvious, correct-looking, one-line remediation that `0.4.0_DS_ClientPlatform~Z` had just correctly
reported as DISCHARGED -- takes down the global scope.** The code says why in its own words:
*"never reachable while a constituent was held, so it was deliberately not built speculatively."*
Filed BLOCKING+ARMED, disarmed same-turn: do not lift tonight; when lifted it is
**implement-then-remove**, never the removal alone. Confirmed by `1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~Z`.

## 5. WHERE I WAS WRONG, AND WHERE A CONTROL SAVED ME

- STOP: **MY OWN DENOMINATOR WAS THE WRONG POPULATION.** I offered `account_count_by_model_key`
  (110/228/15/11/114/2) as cottonwood's Client-account denominator. `0.4.0_DE_ClientPlatform~Z`
  challenged the unstated premise and **was right**: the file itself says summing it overcounts the
  firm population ~1.51x (`:28-30`), and 321 is the DISTINCT **opal-assigned** count. Neither is a
  Client denominator. **And the question is DISSOLVED, not answered:** `:381` excludes zero-residual
  accounts, so a small count is predicted by BOTH hypotheses. The discriminating fields were on the
  artifact all along and all three of us walked past them -- `itemisation_breaks` (`:373`) and
  `negative_residual_accounts` (`:375`).
- STOP: **A TWO-LINE COMMENT GAVE ME A FALSE ABSENCE.** Verifying the `scope_note` fix, my line-based
  grep returned 0 at BOTH the old and new pins -- an answer that reads "already fixed everywhere",
  including on a lambda where it provably is not. **The phrase wraps across two lines in a comment
  quoting it.** NOTE: **MY NEGATIVE CONTROL IS THE ONLY REASON I CAUGHT IT** -- the old pin was supposed
  to return >0. Re-run POSITIVELY (`"all-scope: every scope"` PRESENT): **0 at `7604f2b4bd`, 1 at
  `9dcc87dd5b`, 1 at `73c2dea263`.** A positive formulation needs no control and no comment can fool it.
- STOP: **AND I NEARLY RE-STALED THE LAMBDA MYSELF.** I was about to commit my deferred
  `r7_comparator.py:284` fix before checking that **my own file is packaged member 22-of-22**. Held
  deliberately, and stated as a decision rather than left as an oversight. Verified after the fact
  that my two commits touch NO packaged member (control: `r7_comparator` reads True).

## 6. THE RULE NOBODY HAD STATED, WHICH BOUND FOUR SEATS TONIGHT

>> **ANY COMMIT TO ANY OF THE 22 PACKAGED MEMBERS RE-STALES THE LAMBDA. "COMMIT IS THE DEPLOY" IS
   TRUE OF THE S3 CODE PLANE AND FALSE OF THE ZIP -- AND THE FLOOR RUNS THE ZIP.** <<

Option (B) lands in `mdpf_category_registry.py`, **a packaged member**, so a delete fired before
rebuild #3 would be spent on code lacking the global fix -- and buying that back costs a SECOND
reserved-category ask. **Andrew's attention at 02:4xZ is the scarce resource, not the delete.**
`2.0.0_SA_COO~Z` was caught by this third referent three times and banked it; stated once as a
standing rule rather than re-derived a fourth time.

## 7. COMPILER TOOLS

| Tool | Run | Result | Note |
|---|---|---|---|
| `ratify_sma_live.py` | 3 runs, un-piped, rc before any pipe | PASS | 24 -> **86 scored assertions** |
| refuse fixture (inline) | the negative-value row, both directions | PASS | refuses -$2.25M, accepts (A); **c3 PASSES the same shape** |
| `sha256sum` vs `git hash-object` | the 2c oracle | **FAIL the oracle** | 64 vs 40 hex; neg control differs |
| `git show <pin>` x3 | scope_note across 3 pins | PASS | 0/1/1 -- discriminating, bytes printed |
| `.tools/safe-commit.sh` | 2 commits | PASS | `-F` msgfile by the Write tool; msg-verify MATCH |
| PACKAGE membership parse | 22 entries measured | PASS | comment at `:131` says 20 -- **stale by two** |

**What worked:** predicting the floor outcome from source *before* the run, and negative controls --
two separate false conclusions of mine died on them tonight.
**What failed:** a line-based grep against a wrapped comment; and an overstated completeness bound
(s.2) that I corrected in the same thread.
**Gap found:** `build_package.py:131`'s comment describes 20 members; the list holds 22. The one
human-readable carrier for the `len == 22` predicate disagrees with the code.

## 8. BLOCKERS

**NONE AT THIS SEAT.** The re-ratification is **GATED, with a named owner**: it cannot run until the
served bodies change, and they cannot change without the reserved-category delete, which requires
**Andrew's explicit in-session word** (`mdpf_refresh.py:265-266, 326-327`). `0.7.0_AE_CloudOps~Z`
holds that ask. Deferred with a stated reason: `r7_comparator.py:284` (packaged member -- would
re-stale the lambda mid-sequence).

## 9. CURRENT STATE

- **`ratify_sma_live.py` @`d213a1a3b2`** -- 86 scored assertions across 2 planes x 4 scopes.
  **The item-1 row FAILS on both planes today**, so it discriminates landed from not-landed. Latest
  run: PASS 68 / FAIL 18, rc=1, `VERDICT: NOT RATIFIED` -- **16 of the 18 are the stale served
  `scope_note`, 2 are item 1.** Both clear when the delete lands.
- **PUSH STATE: LOCAL** for both my commits (`ls-remote` NOT read this window -- stated as unread,
  not defaulted).
- **`cvoZ_FINAL_RATIFICATION_20260828.md` IS VINTAGE-PINNED** to the `2026-08-27` objects and goes
  stale the moment the reland rewrites them. **Re-issue is owed, and gated on the same delete.**
- The scope_note fix is **already committed and already in both rebuild pins** -- no separate text
  fix, commit, sweep or 2c is needed for it.

## 10. NEXT STEPS

- [`3.0.0_SA_CVO~Z`] **On L4: run the ratifier with `--post-reland`, un-piped, and re-issue the
  ratification** with attempt count and any criterion change disclosed in the verdict itself.
- [`3.0.0_SA_CVO~Z`] After the reland closes: land `r7_comparator.py:284`'s guard.
- [`0.7.0_AE_CloudOps~Z`] The Andrew ask -- **with both limbs**, and sequenced so the word is spent
  after rebuild #3 rather than before.
- [`1.0.0_SA_CTO~Z`] Whether `build_package.py:131`'s "20" comment is worth one line. Not a gate.

## 11. SURPRISE CHANNEL

- **BLOCKING, ARMED -> DISARMED same-turn** -- the `CLIENT_L1_HELD` lift taking down global (s.4).
  Owner `1.0.0_SA_CTO~Z`; confirmed by two seats.
- **OBSERVATION, INERT** -- `supervised_basis` reaches the artifact and is consumed by **0 portal
  files** (positive controls `presentAum` 2, `absent_reason` 1; negative control 0). On screen the
  0.76% arrives with no basis, and the label `Client - Opal Supervised` invites the exact misreading
  I made twice. `0.4.0_DE_ClientPlatform~Z` has adopted CARRY-vs-RENDER; this is its fixture.

-- `3.0.0_SA_CVO~Z`
