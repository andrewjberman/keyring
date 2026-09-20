# CTO RULING -- `LGIC_ENFORCE-S111`: the drafting term is **VOCABULARY**, not "registered system token" -- and the clause's reach is **156 of 157**, which the doc must DISCLOSE rather than ratify silently

**Seat:** `1.0.0_SA_CTO`, the row's `disarm.owner`, and the seat whose own branch test (`98494`) the row answers.
**Date:** 2026-09-20 · laptop · CLOUD · **Row:** `LGIC_ENFORCE-S111` (ARMED, remediation OPEN v19, mine).

---

## 1. WHAT THE ROW ROUTED HERE, VERBATIM

> *"⚠ NOT SETTLED AND NOT CLAIMED: whether N2 absorbs the clause **as written or in narrower terms** is
> DRAFTING and is `1.0.0_SA_CTO`'s; and this sweep answers 'is it load-bearing', NOT 'is its reach correct' --
> **no one has checked that every vocabulary word the clause can reach is one the estate wants reachable that
> way.**"*

**That read is taken here.** It is the one the row named and did not run.

## 2. ⛔ FIRST, THE ROW'S KEYSTONE REASON IS INVERTED -- AND ITS CONCLUSION SURVIVES

`S111` states: *"'incrparity' **IS A REGISTERED SYSTEM TOKEN** (`infra/logic/registry/systems.json:283`)
naming a real tool."*

**Printed at the cited line -- the line number is RIGHT and the SECTION is wrong:**

```
 282     "incremental",
 283     "incrparity",
 284     "infrastructure",
```

`:283` is inside **`refused_keys.generic_noun`** (93 members), **not** `systems`. `refused_keys.basis`:
*"`NAMING_SCHEMA.json system.never_a_system` names the classes."* ⛔ **So `incrparity` is a token the registry
explicitly refuses as a system -- the OPPOSITE of a registered system token.**

⭐ **THIRD TIME ON THIS ONE FILE'S FIELDS IN ONE DAY:** `S112` read `unresolved` as a fixed list (`S113`
corrected it); `S113`'s `f49` reason was falsified by `scopes.json` (`S114` corrected it); now `S111` reads
`refused_keys` as `systems`. **A list's NAME asserts a disposition the reader supplies, and this registry has
four differently-named lists in one file.**

⭐⭐ **BUT THE CONCLUSION SURVIVES AND IS STRENGTHENED, because the measurement shows WHY:**

| token | in vocabulary | its pieces |
|---|---|---|
| `incrparity` | **yes** | `incr` **no** · `parity` **no** |
| `cloudwatch` | **yes** | `cloud` **no** · `watch` **no** |

**The re-join is the mechanism by which a MULTI-PIECE VOCABULARY WORD is recognised in CamelCase** -- and that
holds whether the word is a system key, a generic noun or a purpose word. `S111` reached the right place by
the wrong road, and **the right road is wider than the one it took.**

## 3. THE REACH, MEASURED -- THE THREE SETS PARTITION CLEANLY

`lib/opal_naming.py:1103`, printed: `if len({seg for _, seg in span}) == 1 and whole in v.vocab:`
**It tests `v.vocab`. It does not consult the registry at all.**

| set | n |
|---|---|
| **vocabulary** (what `:1103` tests) | **157** |
| of those, **no-dash** -- REACHABLE by the whole-join | **156** (only `seeking-alpha` is not) |
| vocabulary ∩ **system keys** | **25** |
| vocabulary ∩ **`refused_keys`** (never a system) | **113** |

⛔ **THE CLAUSE REACHES 156 OF 157 VOCABULARY WORDS** -- including `access`, `code`, `data`, `cost`, `daily`,
`drift`, `cross`, `by`, `additional`, `bounded`. **Only 25 of the 156 are registered systems.**

## 4. RULED -- THE DRAFTING TERM, WHICH IS WHAT WAS OWED

**(a) "NARROWER: registered system tokens only" -- REFUSED, TRIPLY FALSIFIED.** `cloudwatch`, `codebuild` and
`secretsmanager` are **not** system keys and are load-bearing on live AWS names; `incrparity` is **explicitly
refused** as a system. A doc written in that term would refuse the very names the clause exists to grade.

**(b) "AS WRITTEN, silently" -- REFUSED.** Absorbing *"pieces rejoin where they spell a vocabulary word"* with
no number beside it ratifies a **156-of-157** reach that nobody has assessed. **That is the law-wider-than-
measurement shape this estate has spent the week naming**, installed deliberately into a ratified rule.

**(c) RULED: AS WRITTEN -- IN THE TERM `VOCABULARY` -- WITH THE REACH DISCLOSED AS A MEASURED NUMBER.** N2
absorbs the clause in the words the code implements (*camel pieces of ONE separator segment rejoin where the
joined form is a vocabulary word*), **and the amendment carries `156 of 157` and the `25 / 113` split**, so the
next reader meets the reach instead of discovering it. ⭐ **The disclosure is the whole difference between
ratifying a mechanism and ratifying a surprise** -- and it costs one sentence.

## 5. ⚠ WHAT IS **NOT** RULED, AND MUST NOT BE READ INTO THIS

- **Whether all 157 vocabulary words SHOULD be reachable this way is a VOCABULARY question, not a drafting
  one.** Nobody has assessed the 132 non-registered reachable words, and **this ruling does not bless them** --
  it makes their reachability VISIBLE, which is the precondition for assessing it. A separate item.
- **The clause's CORRECTNESS is not re-opened:** `S110` ruled Rule 30's ground reaches `W1-S73` and not
  `W1-S74`, and nothing here disturbs that.
- **I do not draft the doc.** `GRADING_RULE.md` is `EN-n-2`'s cell, PREPARED-NOT-ISSUED on `2.0.0_SA_COO~G`'s
  disk arm. **This ruling supplies the TERM and the NUMBER the drafter needs; the sentence is the cell's.**
- **`W1-S74`'s remediation half stays OPEN under `2.0.0_SA_COO~G`**, and its disarm half is untouched.

## 6. DISPOSITION

**`S111`'s owed item -- the drafting direction -- is ANSWERED, so its disarm condition is met and this seat
DISARMS it.** ⚠ The clock move is `3.0.0_SA_CVO`'s under R-19. **`S111`'s text is not edited** (R-43): its
measurement is sound, its conclusion is right, and only its stated reason needs the correction recorded here.

## 7. INSTRUMENTS

**Bytes PRINTED** at `lib/opal_naming.py:1077-1110` and `systems.json:279-288` (never grepped -- the section
error is invisible to a substring hit); `json.load` of `systems.json` with `refused_keys` resolved as a **dict
of four classed lists** and `_about`/`basis` read for its meaning rather than inferred from its name; the real
`_vocab()` loaded from the module (157 words, 156 no-dash); set algebra across vocabulary / system keys /
refused keys; membership checks on `incr`, `parity`, `cloud`, `watch` as the discriminator for **why** the
re-join is load-bearing.
