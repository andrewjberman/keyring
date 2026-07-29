# INFRASTRUCTURE.TOOLS.O2 — the output contract, made decidable

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, IMPLEMENT
**author:** 3.0.0_SA_CVO · 2026-07-29 ~0200Z
**status of O2 at start:** `decided: NO` · `built: PARTIAL` · `serving: NO`
**why this document exists:** O2 could not move off `decided: NO` because the contract as written
(C1–C4) had never been tested against a real tool. This tests it. One clause turns out to be
**unsatisfiable by construction** for a whole class of tools, and the estate already contains a
ratified reference implementation for another.

---

## 0. The one-line finding

> **`comp-grep` — the tool CLAUDE.md Rule 21 mandates as every agent's first reflex when a raw grep
> is gated — tells the agent that a retrieval-failure zero is a real result.** Its sibling on the
> same rail, `comp-glob`, says the exact opposite and is correct. The defect is one line.

**And the second finding is about my own instrument.** A regex census suggested 19 tools shared this
defect. **Inspection of 13 found ZERO.** The estate's convention (declare the true count) is already
correct across `comp-glob`, `comp-arity`, `comp-secrets`, `comp-fedobs`, `comp-kuzu`; my census was
searching for the wrong idiom and scored its absence as a violation. **comp-grep is an OUTLIER, not
a representative — and the fix is to propagate a convention the estate already holds.** (§4)

---

## 1. What was measured (exercised, not read)

All cells run live against the working tree at `507c16864f`. Query token `import`, pathspec `.tools`.

### 1a. C3 — is an empty result distinguishable from a failed retrieval? **NO, and worse.**

| cell | pathspec | true matches available | comp-grep output | rc |
|---|---|---|---|---|
| A | `.tools` (valid) | 0 for a nonsense token | `0 match(es) in 0 file(s); scanned 260 file(s)` | 0 |
| B | `.tools/NO_SUCH_DIR_9137` | 0 for a nonsense token | `0 match(es) in 0 file(s); scanned 0 file(s)` | 0 |
| **C** | **`.tools/NO_SUCH_DIR_9137`** | **894 matches exist under `.tools`** | **`0 match(es) in 0 file(s); scanned 0 file(s)`** | **0** |

**All three additionally print, unconditionally:**

```
  0 matches is a real result here -- the .gitignore-aware working set was searched, not a stale index.
```

**Cell C is the defect.** A typo'd, renamed, or stale pathspec — over a token with 894 real hits —
returns `rc=0`, zero matches, and an explicit sentence instructing the reader to trust the zero.

**grounding: SOURCE-CONFIRMED** `.tools/comp-grep:172-173` @ `507c16864f`:

```python
if not matches:
    print("  0 matches is a real result here -- the .gitignore-aware working set was searched, not a stale index.")
```

The guard is `not matches` alone. It has **no reference to `scanned`**, so it fires identically
whether 260 files were searched or zero.

> **THE DISCRIMINATOR EXISTS AND IS CORRECT.** `scanned 0` vs `scanned 260` distinguishes cells A
> and C perfectly. A prose reassurance printed on the next line tells the reader to disregard it.
> **This is not a missing declaration. It is an affirmative false assurance printed next to a
> working instrument.**

This is the class CLAUDE.md already legislates against — *"put the control on the RETRIEVAL, not the
pattern"*; *"a zero from a time-windowed query needs a positive control"*; *"a wrong number is more
dangerous than a zero."* Here the **sanctioned on-rails answer** manufactures the false zero and
then vouches for it.

### 1b. C1 — is the denominator declared in-band? **NO — and C1 is unsatisfiable as written.**

Same query, past the cap:

| | comp-grep reported | TRUE |
|---|---|---|
| matches | 200 | **894** |
| files with hits | 22 | **115** |
| files scanned | `scanned 54 file(s)` | **260 in scope** |

The truncation token **is** emitted (`[TRUNCATED at --max 200; refine the pattern/pathspec]`) — **C2
is satisfied.** But the reader cannot tell 200-of-201 from 200-of-894, which are different
decisions. And `scanned 54 file(s)` carries no denominator, so it reads as a completed scan when it
is the count of files reached *before* the cap broke the loop.

**grounding: SOURCE-CONFIRMED** `.tools/comp-grep:137,143-145,149,165-166` — `scanned += 1` per file
opened; `truncated = True; break` at the cap; outer `if truncated: break`; footer prints `scanned`
bare. The same truncated numbers are written to the rail log at `:186`.

> **THE STRUCTURAL RESULT: C1 demands "M measured BEFORE bounding." An early-exit tool cannot know M
> — it stopped looking. Computing M would require abandoning the early exit, i.e. paying the full
> scan the cap exists to avoid.** C1 as written is not merely unmet here; it is **unaffordable for
> the entire early-exit class**, and a contract clause no tool can satisfy will be quietly ignored
> rather than met. **This is the clause that was blocking `decided: YES`.**

### 1c. The in-estate reference implementation — `comp-glob`

`comp-glob`, the sibling primitive on the same rail, on the identical question:

```
NO MATCH: comp-glob -- 0 file(s) for pattern=*.py pathspec=.tools/NO_SUCH_DIR_9137
  This is NOT a confirmation the file is absent -- it is 0 hits in the
  .gitignore-aware working set. Next: widen the pattern (`*.py*`), search content
  instead (`comp-grep <text>`), or check whether the path is gitignored
  (`git check-ignore -v <path>`) -- 16 of the .tools/comp-* files are.
```

It **refuses to assert absence**, names the population it actually searched, and routes the reader
onward. It is still C3-**partial** — it does not distinguish a valid empty directory from a
nonexistent one — but it **never claims to**, so it cannot mislead. That is the register's own
principle satisfied: *bounding is not the problem, undeclared bounding is.*

**Therefore the comp-grep fix is PROPAGATION, not invention.** The correct wording already exists,
on the same rail, and needs no new doctrine to justify.

---

## 2. The contract, v2 — decidable

C2, C3, C4 stand as written. **C1 is amended.** Additions marked ➕.

| id | clause | decidable test |
|---|---|---|
| **C1′** | **Declare the SCOPE DENOMINATOR in-band. Where the true population is knowable, report `N of M`. Where the tool exits early and M is unknowable, report a LOWER BOUND with explicit semantics (`N of >=N`) AND the scope actually examined (`54 of 260 files`). An unqualified bare count is the violation.** | Run past the cap; assert output contains either an `M` or an explicit `>=` / examined-of-scope pair. |
| C2 | truncation is a VISIBLE TOKEN, never an absence | Run past the cap; assert a token appears. |
| C3 | an EMPTY result must be distinguishable from a FAILED retrieval | Run the A/C cell pair; assert outputs differ **and** that neither asserts absence. |
| ➕ **C3a** | **A tool MUST NOT assert that a zero is real unless it can establish that it searched a non-empty population.** | Assert no unconditional absence-claim string exists in the zero path. |
| C4 | the contract is the TOOL'S, not the caller's | The tool emits its own denominator without caller flags. |

**Why C1′ rather than C1:** the honest denominator for an early-exit tool is a *lower bound plus the
examined scope*, which costs nothing — both numbers are already in hand at the break. C1 asked for a
number the tool structurally does not have; C1′ asks for the two it does.

**Why C3a is separate from C3:** C3 is about *distinguishability* — a property of two outputs
compared. C3a is about *a claim made in one output*. comp-grep satisfies neither, but a tool could
satisfy C3 (outputs differ) while still printing an absence-claim, and that would still be the
dangerous cell. comp-glob is the inverse: fails C3, passes C3a, and is safe **because of C3a**.
**C3a is the load-bearing one, and it was not in the original contract.**

---

## 3. The proposed comp-grep change (NOT LANDED — held)

```python
if not matches:
    if scanned == 0:
        print("  WARNING: 0 files were scanned. This is a FAILED RETRIEVAL, not a real zero --")
        print("  the pathspec matched no tracked, non-ignored files. Verify it exists:")
        print("    git ls-files <pathspec> | head")
        # and a non-zero rc, so a caller reading only rc is not told 'clean'
    else:
        print("  0 hits in the .gitignore-aware working set actually searched (%d file(s))." % scanned)
        print("  This is NOT a confirmation of absence -- widen the pattern, or check "
              "`git check-ignore -v <path>`.")
```

plus, in the footer, `scanned %d of %d file(s)` and `>=` semantics on a truncated match count.

**HELD, NOT LANDED, and the reason is a live collision:** `comp-which` runs `comp-grep`/`comp-glob`
as its fallback path, and `0.8.0_AE_CloudComp` is at this moment capturing BEFORE-output for CTO's
**mandatory byte-identical routing-identity control** on the comp-which wiring. If that capture
includes comp-which's stdout bytes, a footer change of mine appears in their AFTER as a divergence
that has nothing to do with their diff. Flagged to them at 015851Z; land is gated on their answer
(routing DECISIONS → orthogonal, land freely; STDOUT BYTES → land after their capture closes).

---

## 4. The census — and what it cannot see

93 `comp-*` files on disk. **This is the DISK population, not "the toolkit"** (the count cascade:
93 disk / 89 classified / 89 homed / 69 in `tools_index` / 105 use-cases — every number correct for
a different population).

Regex census over `.tools/comp-*`: **24 bounded, 19 of those with "no truncation token" in source.**

> ### ⚠ THAT 19 IS WRONG, AND THE INSTRUMENT THAT PRODUCED IT WAS MINE
>
> **I inspected 13 of the 19 and found ZERO violators.** My `TOKEN` regex searched for the words
> *truncated / capped / more / of N*. **The estate's actual idiom is to DECLARE THE TRUE COUNT**,
> which my regex could not see. So the census reported as "no token" a set of tools that satisfy C1
> by a **better** mechanism than the one I was looking for.

Measured, from source at `507c16864f`:

| tool | what it actually does | verdict |
|---|---|---|
| `comp-arity` | `f"{len(unreadable)} file(s) UNREADABLE"` → shows 5 → `f"(+{len(unreadable)-5} more)"` | **C1 + C2 BOTH SATISFIED — gold standard** |
| `comp-secrets` | `f"'{ident}' is ambiguous ({len(matches)} matches)"` → then shows 10 | **C1 SATISFIED** (total declared *before* bounding) |
| `comp-fedobs` | shows `rows[:50]` → then prints `f"rows={n}"` with the true total | **C1 SATISFIED** |
| `comp-kuzu` | `--limit` defaults `None`; LIMIT appended only if passed (`kuzu_cli.py:83-84,145`) | **CLEAN — no silent bound** |
| `comp-axes` | `top3=fails[:3]` — the bound is *named in the field* | self-declaring |
| `comp-heat` | `res['sql'][:90]` — truncates a SQL string for display | **false positive** |
| `comp-routable-check` | `reason[:88]` — string display truncation | **false positive** |
| `comp-imgread` | PIL binary reader; register already rules it not an enumerator | **not an enumerator** |
| `comp-depth`, `comp-gitdrill`, `comp-iam-usage`, `comp-keys`, `comp-residue` | `--limit/--max/--top N` user-supplied flags (`comp-keys` also has `--all`) | caller-controlled, not silent |

**6 of 19 remain uninspected** — `comp-deadgrant.py`, `comp-firmsep-sweep.py`, `comp-freshness`,
`comp-kit-striplist-gate`, `comp-tagauthz.py`, `comp-whoread.py`. **Claimed as nothing.**

> ### THE HEADLINE INVERTS
>
> **`comp-grep` is not a representative of a 19-tool class. It is an OUTLIER on a rail whose
> siblings all do it correctly** — `comp-glob` refuses to assert absence, `comp-arity` declares
> total-and-remainder, `comp-secrets` declares the count before bounding, `comp-fedobs` prints the
> true row total. The estate's convention is already right. **One tool breaks it, and it happens to
> be the one Rule 21 makes mandatory.**

**Two further limitations, both still live:**

1. **The census is BLIND to wrapper tools (false negatives — the dangerous direction).** `comp-kuzu`
   is 24 lines of bash delegating to `infra/aws/globgrph/kuzu_cli.py`. The census scanned
   `.tools/comp-*` only, so for every wrapper the bounding logic lives where it cannot look. **It
   therefore UNDER-reports bounding, and an under-reporting instrument reads as a clean bill** — the
   same silence-is-the-defect shape as comp-iam.
2. **A regex census is a hypothesis, and this one was falsified in the direction that flatters the
   author.** It manufactured 19 apparent defects. Had I reported that number without inspecting, I
   would have filed 13+ false findings against peers' tools — the exact false-divergence class I
   nearly hit against `0.8.0_AE_CloudComp`'s timings hours earlier. **The lesson is not "regexes are
   imprecise"; it is that I searched for MY expected idiom and scored its absence as a defect.**

---

## 5. State change proposed for the register (MSTR owns `state.yaml`; I do not edit it)

| field | from | to | basis |
|---|---|---|---|
| O2 `decided` | `NO` | **`YES` pending CTO ratification of C1′ + C3a** | the contract is now testable; C1 was the blocker and is amended |
| O2 `built` | `PARTIAL` | `PARTIAL` (unchanged) | still true — no tool has been changed. The patch is written and **held**, and held is not built |
| O2 `serving` | `NO` | `NO` (unchanged) | nothing landed |

**`built` deliberately does NOT move.** A written, exercised, unlanded patch is not a behaviour
change, and this document exists partly because the estate keeps scoring artifacts as outcomes.

---

## 6. What this does not cover

- **6 of 19 census candidates uninspected** (`comp-deadgrant.py`, `comp-firmsep-sweep.py`,
  `comp-freshness`, `comp-kit-striplist-gate`, `comp-tagauthz.py`, `comp-whoread.py`). Named, not
  claimed. Several are gates with side effects and were deliberately not run blind.
- **The wrapper-blind axis** — a whole class of tools whose bounding the census cannot see. Sizing
  it needs a different instrument (resolve each wrapper to its implementation, then scan that).
- **C4 is untested.** Every instance measured here is the tool's own bounding; the register notes
  every prior measured instance came from a *caller's* bounding, and I did not test that direction.
- **No claim that the four contract clauses are exhaustive.** The SIMULATE miss in the O1 classifier
  proved a missing category is silent; a fifth clause would fail identically.

---

## 7. Compiler Tools

| tool | result | note |
|---|---|---|
| `comp-grep` | **FINDING** | the subject; C1 + C3 + C3a violations, source-confirmed |
| `comp-glob` | PASS | C3-partial but honest; the reference implementation for the fix |
| `comp-kuzu` | PASS | verified negative — no silent default limit |
| `comp-arity` / `comp-secrets` / `comp-fedobs` | PASS | declare the true count; C1-satisfying by a mechanism my census could not see |
| `comp-heat` / `comp-routable-check` | n/a | census false positives, confirmed by inspection |
| `git grep` / `git ls-files` | control | independent true denominators (894 / 115 / 260) |

**What worked:** the A/C cell pair — same token, one variable (pathspec validity) — is a reusable
C3 probe for any search tool, and it is what turned a suspicion into cell C.

**What failed — mine, and it is the more instructive half:** my census's `TOKEN` regex encoded MY
expected idiom (*truncated / capped*) and scored its absence as a defect, producing **19 apparent
violators of which the 13 inspected are all compliant**. Reporting that number unexercised would
have filed 13+ false findings against peers' tools — the same false-divergence class I nearly hit
against `0.8.0_AE_CloudComp`'s timings hours earlier, and caught the same way: by checking my own
instrument before trusting its verdict.

**Gap found:** the census cannot see wrapper implementations (§4.1) — it under-reports bounding,
which is the direction that reads as clean.

— 3.0.0_SA_CVO
