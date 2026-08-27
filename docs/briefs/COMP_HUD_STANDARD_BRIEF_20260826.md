# THE AGENT HUD — a display/pagination/disclosure standard for the comp-* tools

**Brief · minted 2026-08-26 · author `2.0.0_SA_COO~X` · Andrew-commissioned**
**Status: BRIEF — a proposal to return to. NOT law, NOT a gate, NOT authorization to retrofit anything.**

**Commissioned verbatim (Andrew, 2026-08-26 ~18:5xZ):**
> *"whatever the default mechanism is, with associated disclosures should be consistent across tools. It seems
> to me that comp-find is the best equipped in this manner so it would make sense to have it serve as the
> default with regard to display, or what i refer to as 'HUD' for the agents (heads up display). That should be
> notated in a briefing somewhere that we can return to."*

---

## 1. THE EDICT EXISTS — AND ITS OWN PREMISE WAS FALSE

Andrew asked whether there had been an edict *"at one point"* and wondered if it *"wasn't equally applied."*
**It exists. It is his, and it is verbatim** (2026-08-05 ~2015Z, at the `3.0.0_SA_CVO~B` terminal; carried in
`.tools/comp-find:7` and `org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_SCRIPTGEN_AND_AGENT_NAVIGATION_SPEC.md:17`):

> *"replace comp-grep/glob with comp-find (no SLM rerank required, just have it **structure paginated results
> like all the other comp-tools do**)."*

⛔ **BUT THE DIAGNOSIS IS NOT "UNEQUALLY APPLIED." IT IS SHARPER AND IT IS WHY THIS RECURS.**

The edict's operative clause is a **comparison to an existing norm** — *"like all the other comp-tools do."*
**That norm did not exist when the sentence was written, and does not exist now.** Measured below: **1 of 105
comp-tools carries the full HUD, and it is `comp-find` — the tool the edict was spoken ABOUT.**

So the edict was **applied exactly once, to the one tool it named**, and the comparison class it invoked was
already empty. **It was not under-enforced; it was self-referential.** `comp-find` did not inherit a house
style — **it INVENTED one, and the instruction that produced it described the result as if it were the
precedent.**

⛔ **THE TRANSFERABLE FORM, because it will happen again: an instruction phrased as "do it like the others do"
carries NO specification. It is only as strong as the norm it points at, and if that norm is a
misremembering, the instruction lands on one tool and stops.** A standard has to be **written down as a
contract**, not invoked as a comparison. **That is the entire reason this brief exists rather than a second
edict.**

---

## 2. WHY THIS SURFACED NOW — TWO LIVE TRAPS, ONE FAMILY

Both found 2026-08-26 during D11 census work, both by Tier-2 lanes, both **near-misses on published false
absences**:

| | `comp-find` | `comp-keys prefix` |
|---|---|---|
| **the defect** | a content pattern **and** `--name` in one call scans **ZERO files** | truncates to **40 of N** by default |
| **default posture** | you must *actively* mis-call it | ⛔ **truncation IS the default — you must opt OUT with `--all`** |
| **the total** | printed in the header, **before** the rows | ⛔ printed **AFTER** the rows |
| **failure direction** | clean `0` over `0 scanned` | ⛔ **hides keys only → FALSE ABSENCES, never false presences** |
| **who caught it** | `0.4.0_DT_ClientPlatform~X` isolated; 3 seats reproduced | `0.4.0_DT_ClientPlatform~X`, by `head-object` |
| **near-miss** | a lane concluded a reference artifact absent | **the hidden key was `kuzu_nessie_db`, 51MB — the store D11 exists to find**, and the sentence calling it absent was already written |

⛔ **BOTH TOOLS WERE HONEST. BOTH READERS WERE FAST.** `comp-find` prints `0 hit(s) across 0 file(s) scanned`;
`comp-keys` prints `-- 129 key(s); showing 40`. **The true denominator was on the page both times.**

**That is the finding that shapes the whole standard: the defect is not missing information, it is
INFORMATION PLACED WHERE A FAST READER WILL NOT MEET IT.** A total printed after the rows is invisible to
anyone who greps, pipes, or reads top-down and stops when they have an answer — **which is every agent, on
every call.**

---

## 3. HOW `comp-find`'s HUD ACTUALLY WORKS — the anatomy worth copying

Source: `.tools/comp-find` @`fe269171f2`, render block `:255-300`. **Eleven elements, in emission order.**

```
comp-find [content] 'nerves_resolve'                                        <- 1  MODE + QUERY echoed
  DENOMINATOR: 2 hit(s) across 28794 file(s) scanned in scope               <- 2  DENOMINATOR, IN THE HEADER
               | 14 UNREADABLE, NOT searched | 1952 BINARY, NOT searched    <- 3  CARVE-OUTS, NAMED
  BANDS (true totals, not this page): HEAD=1 DOC=1                          <- 4  TRUE TOTALS vs PAGE, stated
  PAGE 1 of 1  (showing 2 of 2)                                             <- 5  POSITION IN THE POPULATION

  [HEAD] -- the query is in the FILE NAME -- usually what you meant         <- 6  BAND + WHAT IT MEANS
    .tools/comp-find:7: ...                                                 <- 7  THE ROWS

  MORE: 13 hit(s) not shown. Next: --page 2   (or --all, or --band <B>)     <- 8  THE EXACT NEXT COMMAND
```

**And on an empty result — the element with the highest value per character in the whole estate:**
```
  NO HITS. This is a MEASURED zero over 26841 scanned file(s) in scope --   <- 9  ZERO IS QUALIFIED
           not a claim the term is absent from the estate.
  ^ AND 14 in-scope file(s) were UNREADABLE and never searched.             <- 10 the zero's OWN carve-outs
    Your zero does NOT cover them.
  Widen with a pathspec, or -i, or check the pattern.                       <- 11 THE RECOVERY MOVE
```

### 3.1 The nine properties that make it work

| # | property | why it is load-bearing |
|---|---|---|
| **P1** | **The denominator is in the HEADER, before the rows** | The `comp-keys` trap is *entirely* a placement defect. A footer total is invisible to a piped or top-down reader. **Placement is the control.** |
| **P2** | **Truncation is DISCLOSED at the point of truncation** | `MORE: N not shown` sits where the rows stop, so the reader meets it exactly when they would otherwise conclude. |
| **P3** | **The disclosure carries the EXACT NEXT COMMAND** | `Next: --page 2 (or --all, or --band <B>)`. A disclosure that does not tell you how to widen is a warning, not a control. |
| **P4** | **True totals are labelled as distinct from the page** | `BANDS (true totals, not this page)` — the parenthetical does the work. It pre-empts the read it is most likely to receive. |
| **P5** | **A ZERO IS QUALIFIED IN PROSE, ON ITS OWN LINE** | *"a MEASURED zero over N scanned — not a claim the term is absent."* ⛔ **This one line is what makes the `comp-find` trap self-refuting**: `0 over 0 scanned` reads as absurd on its face. **`comp-keys` has no equivalent, which is why its trap draws blood.** |
| **P6** | **What was NOT searched is carved out and named** | UNREADABLE and BINARY files are excluded from the denominator *and stated*. A denominator that silently includes unsearched files is a lie with a number on it. |
| **P7** | **Grading is DETERMINISTIC and re-derivable** | No SLM, no learned rerank — by Andrew's word and for a harder reason stated in the source: *"a ranking an agent cannot re-derive is not auditable, and a non-deterministic rail cannot be a control."* |
| **P8** | **Every row is graded; grading is UNCAPPED even when display is capped** | Band counts are true over the whole result set, not over the page. **Truncating the DISPLAY must never truncate the MEASUREMENT.** |
| **P9** | **Bands carry their own meaning inline** | `[DOC] -- prose -- DESCRIBES the code and may be STALE; confirm against source`. The tool tells you how much to trust the row *at the row*. |

⛔ **P1 AND P5 ARE THE TWO THAT WOULD HAVE PREVENTED BOTH OF TODAY'S NEAR-MISSES.** Everything else is
quality-of-life. **If the standard is ever reduced for cost, reduce to P1 + P5 and keep them absolutely.**

---

## 4. THE MEASURED STATE — 105 TOOLS

**Instrument: regex over the source of every executable `.tools/comp-*` (105 files), 2026-08-26.**
⚠ **This is a PROXY and its limits are stated in §7. It detects the ELEMENTS, not the behaviour.**

| HUD element | tools carrying it | share |
|---|---|---|
| `DENOMINATOR` printed | 11 of 105 | 10% |
| `PAGE n of m` / `showing x of y` | **1 of 105** | <1% |
| `MORE:` / explicit next command | **1 of 105** | <1% |
| Qualified-zero block | 2 of 105 | 2% |
| Caps output somehow | 26 of 105 | 24% |
| Offers `--all` | 10 of 105 | 9% |

> ### ⛔ **CARRY ALL FOUR CORE ELEMENTS: 1 of 105 — `comp-find`.**

**And the two numbers that matter operationally:**

| | count | why it bites |
|---|---|---|
| **Tools that TRUNCATE with NO `--all` opt-out** | **21** | The reader cannot widen even knowing they should. |
| **Tools that TRUNCATE and print NO total at all** | **13** | ⛔ **Silent truncation. The reader has no signal that a population exists beyond the rows.** |

**The 13 silent truncators:** `comp-axes` · `comp-cochange` · `comp-deadgrant.py` · `comp-denytest.py` ·
`comp-firmsep-sweep.py` · `comp-freshness` · `comp-imgread` · **`comp-keys`** · `comp-kit-striplist-gate` ·
`comp-routable-check` · `comp-secrets` · **`comp-similar`** · `comp-tagauthz.py`

⚠ **Two names on that list deserve a second look and neither is a coincidence:** **`comp-keys`** is today's
trap, found by accident. **`comp-similar`** is a **live D11 subject** — its determinism is already suspect,
and it now also appears to truncate silently. **A tool whose output cannot be trusted for completeness AND
cannot be trusted for discrimination is two independent problems, and a card must not conflate them.**

---

## 5. THE PROPOSED STANDARD — THE HUD CONTRACT

**`comp-find` is the reference implementation. The contract is written out below rather than by reference,
because §1 is what happens when a standard is invoked by comparison instead of specified.**

### 5.1 TIER 1 — BINDING ON ANY TOOL THAT CAN RETURN MORE THAN IT DISPLAYS

**Five requirements. A tool that lists, counts, sweeps, or enumerates is in scope.**

1. **THE DENOMINATOR PRINTS IN THE HEADER, BEFORE THE FIRST ROW.** Never only in a footer.
   *Form:* `DENOMINATOR: <shown> of <total> <units> across <scanned> <scope>`
2. **A ZERO IS QUALIFIED IN PROSE.** *"a MEASURED zero over N scanned — not a claim of absence."*
   **A bare `0` is not a conforming output.**
3. **TRUNCATION IS DISCLOSED WHERE THE ROWS STOP, WITH THE EXACT NEXT COMMAND.**
   *Form:* `MORE: N not shown. Next: <verbatim command>`
4. **WHAT WAS NOT EXAMINED IS CARVED OUT AND NAMED** — unreadable, binary, skipped, out-of-scope.
5. **CAPPING THE DISPLAY NEVER CAPS THE MEASUREMENT.** Totals are computed over the full set.

### 5.2 TIER 2 — RECOMMENDED WHERE THE SHAPE FITS

6. `PAGE n of m (showing x of y)` · 7. `--all` opt-out · 8. deterministic, re-derivable ordering ·
9. inline band/trust annotation · 10. the recovery move on an empty result.

### 5.3 ⛔ ONE OPEN DESIGN QUESTION — DEFAULT-CAP vs DEFAULT-FULL

**`comp-find` caps at 25 and `comp-keys` at 40, and neither number is derived from anything.** The standard
above makes truncation *safe*; it does not settle whether it should be the *default*.

**My recommendation: keep a default cap and make the disclosure mandatory** — an uncapped default floods
agent context, which is a real correctness cost, not just a speed one. **But the cap should be ONE number
across the estate, stated in the contract, not per-tool folklore.** ⛔ **This is Andrew's call and I am not
taking it.** Naming it because a standard that leaves its central constant unspecified will drift back into
per-tool defaults within a month.

### 5.4 ⛔ WHAT THIS BRIEF DELIBERATELY DOES NOT DO

- **It authorizes NO retrofit.** 21 + 13 tools are named as a measurement, not a work order.
- **It creates NO gate.** No approval step, no commit check, no CI rule. *(CLAUDE.md: never implement a gate
  without Andrew's explicit word — and a HUD lint would be exactly that.)*
- **It mints NO taxonomy.** The Tier-1/Tier-2 split is a **priority ordering, not a classification axis**, so
  Rule 24 is not triggered. **If anyone converts it into an enum on a tool registry, that IS a
  schema-enumeration act and ships its four-postulate record.**
- **It does not touch `comp-similar` or `comp-keys`.** Both are live D11 subjects under qualify-do-not-fix.

---

## 6. IF THIS IS EVER ADOPTED — THE SEQUENCE THAT WOULD ACTUALLY WORK

**Not authorized. Recorded so the shape survives.**

1. **Write the contract into a place tools are read FROM**, not a doc they are compared to. §1 is the proof
   that comparison does not propagate.
2. **A shared renderer, not 105 hand-rolls.** One `_comprail`-level `hud_header()` / `hud_more()` /
   `hud_zero()`. **The estate already has `_comprail` as the shared substrate `comp-find` imports** — the HUD
   belongs beside it. *(Build-ladder: the infrastructure exists; a per-tool reimplementation is the duplicate
   this would create.)*
3. **Convert on touch, not in a sweep.** A tool gets the HUD when someone edits it for another reason.
   **A 105-tool retrofit is exactly the kind of unrequested scope that becomes permanent debt.**
4. **The 13 silent truncators are the only population with a case for going first** — they are the ones that
   can produce a false absence with no signal at all.

---

## 7. COST, AND WHEN THIS DOES NOT APPLY

*(CLAUDE.md requires any new verification rule to state both. A rule without a non-application clause is
incomplete and does not land.)*

**COST:** for a tool author, roughly ten lines against a shared renderer — a header line, a `MORE:` line, a
zero block. **For a reader: zero.** The HUD *reduces* reader cost; that is its entire purpose.

⛔ **IT DOES NOT APPLY TO:**
- **A tool that cannot return more than it displays.** A single-value probe, a boolean gate, a `--self-test`.
  **Adding a denominator to a one-row answer is noise, and noise is what trains readers to skip headers —
  which would attack P1, the property that matters most.**
- **`--json` / machine-readable modes.** The consumer is a parser; the totals belong in the structure.
- **A tool whose output IS the population by construction** (e.g. `comp-which` routing a single question).
- **Pass-through wrappers** around a tool that already carries the HUD — double-printing is worse than none.

⛔ **AND THE HONEST LIMIT OF §4's NUMBERS:** the survey is **regex over source**. It detects the PRESENCE OF
ELEMENTS, not correct behaviour. **A tool could paginate perfectly and score `.` on my table by wording its
output differently; another could print `DENOMINATOR` over a wrong population and score `YES`.** I exercised
only two tools directly (`comp-find`, `comp-similar`). **Treat the 105-row table as a RANKED PLACE TO LOOK,
never as a verdict on any single tool** — which is the same caveat `comp-find`'s own `DENOMINATOR` line
carries: it certifies the sweep, not the question.

---

## 8. PROVENANCE

| | |
|---|---|
| Andrew's original edict | 2026-08-05 ~2015Z, `3.0.0_SA_CVO~B` terminal — `.tools/comp-find:7` |
| Andrew's HUD commission | 2026-08-26 ~18:5xZ, this seat |
| Reference implementation | `.tools/comp-find` @`fe269171f2`, render `:255-300` |
| `comp-find` trap | `0.4.0_DT_ClientPlatform~X` msg 72990; reproduced by `2.0.0_SA_COO~X` + `0.7.0_AE_CloudOps~X` (73024) |
| `comp-keys` trap | `0.4.0_DT_ClientPlatform~X` msg 73076; reproduced by `2.0.0_SA_COO~X` |
| Survey | 105 executable `.tools/comp-*`, 2026-08-26, regex-over-source (limits: §7) |

⛔ **THE ONE LINE TO CARRY IF NOTHING ELSE SURVIVES:**
> **THE DENOMINATOR IS ON THE PAGE — PUT IT WHERE A FAST READER MEETS IT.**
> Both of today's near-misses were tools telling the truth in a place nobody read.
