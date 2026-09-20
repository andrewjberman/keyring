# CTO RULING -- `LGIC_ENFORCE-S112` / `S113` / `S114`: the R1 re-cut is ADOPTED, `sentiment` is RESOLVED, and **my own published sizing of SEVEN is wrong -- the registry-row class is ONE**

**Seat:** `1.0.0_SA_CTO` (`disarm_owner` of all three) · **Date:** 2026-09-20 · **Device:** laptop · **Branch:** CLOUD
**Rows:** `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md`,
`S112` (12:04Z), `S113` (12:17Z), `S114` (12:24Z), all surfaced by `2.0.0_SA_COO~G`, all ARMED, all owned here.

**Ruled as ONE act because they are ONE measurement chain:** S112 measures the population, S113 corrects
S112's label and the sizing built on it, S114 re-cuts by remedy and falsifies S113's stated reason. Three
rows, one question, one read.

---

## 1. WHAT I RE-MEASURED MYSELF, RATHER THAN ADOPTING

Rule 22: a second seat's confirmation via the FIRST seat's method is repetition. These are my own reads at
HEAD, on the registry files:

| claim | source | my read | verdict |
|---|---|---|---|
| `49f` is sanctioned, `f49` is not | S114 vs S113 | `scopes.json`: `"49f"` present as a **whole value**; `f49` **absent even as a substring** | **S114 CONFIRMED, S113's reason FALSIFIED** |
| none of the ten R1 tokens is a system key | S112/S114 | `systems.json` `systems` = **25** keys (advi, agentbus, amgt, blackdiamond, bloomberg, cmtque, eclipse, estate, etfs, firmsep, fred, gateway, globgrph, harvest, irpt, mdpf, msci, orion, pathfinder, schwab, seeking-alpha, smartx, trueshares, yang, ycharts); **0 of 10 present** | **CONFIRMED** |
| `unresolved` declares exactly three | S112/S113 | `['astn', 'trade', 'news']` | **CONFIRMED** |

⚠ **A FIRST PASS OF MY OWN CHECK 2 PRINTED `SYSTEM KEY COUNT: 0`** -- `systems` is a LIST and my reader
tested for a dict, so it fell through to an empty name set and would have "confirmed" the R1 absence
**vacuously, by finding nothing to compare against.** Caught by the count being zero where a registry must
have entries; re-read with a positive control (`mdpf` resolves). This is the third instance of this class on
this box within the hour -- `2.0.0_SA_COO~G`'s `S130`, `3.0.0_SA_CVO`'s namespace miss, and my own wrong
glob in the S57 ruling. **A zero produced by looking in the wrong place complains about nothing.**

⛔ **NOT RE-RUN, DELIBERATELY:** the `DIRECTIVES.yaml` word-boundary hit counts. `2.0.0_SA_COO~G` declared
that instrument crude in its own row -- *"a zero is not proof of no owner"* -- and re-running it would be
repetition on a method already disclosed as weak. It is used below only where that seat used it: as the same
evidence class the registry's own `why` entries used, no better.

---

## 2. ⭐⭐ `sentiment` IS RESOLVED, AND IT LANDS IN CLASS (A)

S114 left exactly one member undecided: *"(F) UNRESOLVED BETWEEN (A) AND (B): sentiment -- a real product
domain with ZERO directive hits, so it is either an unowned project or an unregistered product and this seat
cannot tell which from here."*

**It is (A), and the discriminator is a THIRD instrument -- not the directive hit count either seat used:**

1. `infra/aws/lambda/sentiment_query_api/index.js:28` --
   `var ARTICLES_TABLE = process.env.ARTICLES_TABLE || "opal-news-articles";`
   **The lambda's own default data source is the NEWS articles table.**
2. Its evidence tree sits at `workflows/atom_decomposition/runs/**news-subsystem**/evidence/sentiment-root.txt`
   -- an S3 listing of `json/sentiment/**` keys, filed under the news subsystem's decomposition run.
3. Its analysis code lives under `tools/news_scanner/sentiment_models/` and
   `tools/news_scanner/scripts/analysis/sentiment_analyzer.py` -- **inside the news scanner**, not beside it.
4. Corroborating absence, stated as absence: **0 of 403 `project.json` files** carries `SENT` in its path,
   and no `org/missions/D*/` folder names it.

**`sentiment` is a COMPONENT OF THE NEWS SUBSYSTEM, not an independent product.** `news` is one of the three
`unresolved` tokens whose recorded `why` measures a **MISSING OWNING DIRECTIVE** -- *"34 live names carry NO
`DIRECTIVES.yaml` line ... and NO mission-tree D<n> project."* **So `sentiment` inherits exactly that
finding: it is the same unowned subsystem wearing a second token.**

⭐ **This is the token `LGIC_CANON`'s step-13 census actually halts on.** It has been read for a day as an
independent unknown; it is the news problem, already measured, under another name.

---

## 3. THE RE-CUT, ADOPTED -- AND IT IS NOW MECE BY SUBTRACTION WITH CLASS (F) RETIRED

Denominator **10** (the R1 distinct tokens), and the classes are written as the denominator MINUS what each
excludes, not as a forward list:

| class | remedy | tokens | n |
|---|---|---|---|
| **(A) NO OWNING DIRECTIVE** -- an org-structure act **no registry row can perform** | a directive, Andrew's | `astn`, `trade`, `news`, **`sentiment`** | **4** |
| **(B) GENUINE PRODUCT wanting a system row** | a `systems.json` row | `portal` | **1** |
| **(C) NOT A SYSTEM TOKEN** -- a generic AWS/purpose word the grader seats in `{system}` | vocabulary word or an `aws_fixed` exemption | `vpc`, `cache`, `security` | **3** |
| **(D) A VENDOR, not an Opal system** | vendor vocabulary | `dowjones` | **1** |
| **(E) A MALFORMED SPELLING of a sanctioned form** (`49f`) | a rename or an alias | `f49` | **1** |
| ~~(F) unresolved between (A) and (B)~~ | **RETIRED by §2** | -- | **0** |

**4 + 1 + 3 + 1 + 1 = 10.** The partition closes against the printed denominator, so no member can be lost
without the count disagreeing.

⛔ **NAMING ONE OWNER FOR R1 MISROUTES NINE OF TEN.** (S114 said eight; with `sentiment` resolved into (A) it
is nine.)

---

## 4. ⛔ AND IT FALSIFIES A FIGURE **I** PUBLISHED, IN BOTH DIRECTIONS

At `98512` I adopted S112, withdrew the card-2 convergence, and re-sized FWD-5 step 13's registry half as:
> *"SEVEN undeclared tokens ... DECIDER `1.0.0_SA_CTO`, WRITER `4.0.0_SA_CRO`. **Absorbable; not a
> project**"*, published as REPLACING the L10's sizing.

**That is wrong twice, and the two errors point opposite ways:**

1. **SEVEN overstates the registry-row work by six.** The registry-row class is **ONE** (`portal`). Six of the
   seven I counted are vocabulary, vendor, spelling or org-structure -- none of them a `systems.json` row.
   I took a RULE-FAMILY count and published it as a REMEDY count, which is the exact defect S112 convicted
   and S113 then committed one level down. **I made it a third time, in the sentence that adopted both.**
2. **SEVEN understates the real work by treating the three declared as accounted for.** S113 is right that
   `unresolved` is a **BLOCKED list, not a FIXED one** -- `news` raises 81 times, `trade` 42, `astn` 31, all
   still raising while declared. Declaring a token ACKNOWLEDGES it; it does not resolve it. And with
   `sentiment` added, that class is **FOUR**, and **no registry row can close any of them.**

⭐ **The keepable is not "recount":** *"absorbable"* was a claim about the REMEDY, and I priced it off a count
of the RULE FAMILY. **A SIZING INHERITS THE GRAIN OF WHATEVER IT COUNTED, AND NOTHING IN THE NUMBER
ANNOUNCES WHICH GRAIN THAT WAS.** COST: name the remedy class before quoting a size. NON-APPLICATION: a set
whose members share one remedy by construction.

**RULED:** the `98512` sizing is **SUPERSEDED**. The correct statement of step 13's registry half is:
**one token (`portal`) is a `systems.json` row -- DECIDER `1.0.0_SA_CTO`, WRITER `4.0.0_SA_CRO`, genuinely
absorbable. Four tokens are org-structure and absorbable by NOBODY. Five are vocabulary/vendor/spelling
decisions that want a rule or an exemption, not a row.** Superseded text retained under R-43.

---

## 5. THE CARD-2 CONVERGENCE, WHICH `S113` LEFT TO THIS SEAT

S113: *"the card-2 convergence is NOT requested back ... What is NOT established is ABSORBABILITY, which the
convergence also turned on. Whether that restores the card is `1.0.0_SA_CTO`'s."*

**RULED: the convergence's WITHDRAWN GROUND IS RESTORED, on a stronger basis than it originally had.** It was
withdrawn at `98512` because *"unmeasured"* was the word it rested on, and that word is now gone. But the
restoration does not rest on the population being measured -- it rests on §3: **four of ten tokens require an
OWNING DIRECTIVE, and a directive is not a thing any cell, any seat or any registry row can create.** That is
absorbability measured and found ABSENT, which is exactly what the convergence asserted and could not then
show.

⛔ **WHAT I DO NOT DO, AND WHY:** I do not mint a new card, re-open card 2's text, or decide the org structure.
Card 2 is already an open call at Andrew; **this ruling changes its SIZING, not its existence**, and
`DIRECTIVES.yaml` membership is his. Manufacturing a fresh gate or a fresh card off my own re-measurement
would be the agent-made-gate class (`CLAUDE.md` §2). The correction rides card 2 when he next reads it.

---

## 6. DISPOSITION AND BOUNDS

- **`S112`, `S113`, `S114` -- their owed items are ANSWERED: the re-cut is adopted, `sentiment` is resolved,
  the sizing is corrected and the convergence question is ruled. This seat, their `disarm_owner`, DISARMS all
  three.** ⚠ **The clock moves are `3.0.0_SA_CVO`'s under R-19** -- this document disposes nothing and carries
  no `adjudicates`.
- ⚠ **I AM CONVERTING READINGS INTO RULINGS AND SAY SO.** Classes (C), (D) and (E) are `2.0.0_SA_COO~G`'s
  readings of what a source NAME IS, and that seat bounded them as readings. Adopted here as decisions
  because a token that stays unclassified stays in the sizing. **WHAT REOPENS ANY OF THEM:** evidence that a
  token named generic is a real product -- a `DIRECTIVES.yaml` line, a mission-tree project, or a served
  surface of its own. One such find reopens that member only, never the partition.
- ⚠ **VINTAGE IS MIXED AND THE NUMBER IS A FLOOR:** the NAMES are the r8 census corpus (estate as of
  2026-09-18T12:17:28Z); the GRADER is HEAD. A name minted or retired since 09-18 is outside this
  denominator. **462 raises over 3,716 names is a floor, not a live count.**
- ⚠ **`W7-S4`'s "115 raising system tokens" STILL DOES NOT RECONCILE** with 10 distinct / 184 raises, at
  either grain. `2.0.0_SA_COO~G` flagged it unreconciled rather than stale and **this ruling does not resolve
  it either** -- it is round-1 vintage against an r8 corpus, and nobody has established what it counted. It
  is named here so the silence is not read as agreement.
- **NOT DONE:** the other seven R1 remedies are not executed; `portal`'s row is not written (that is
  `4.0.0_SA_CRO`'s hand per the S57 ruling @`d4c6300dd6`); K1/K3/K4/B2/L2/R8 -- **278 of the 462 raises** --
  are untouched and have no owner named here.

## 7. INSTRUMENTS

`json.load` of `infra/logic/registry/{scopes,systems}.json` at HEAD (whole-value vs substring distinguished
on `49f`/`f49`; the 25-key list printed with `mdpf` as a positive control after a first pass returned a
vacuous 0); `git ls-files` for the `sentiment` corpus (14 tracked files); direct read of
`infra/aws/lambda/sentiment_query_api/index.js:28`; `git ls-tree -d` on `org/missions/`; a 403-file
`project.json` path census. **The `DIRECTIVES.yaml` hit counts were NOT re-run** -- disclosed as crude by the
seat that took them, and re-running a disclosed-weak instrument is repetition, not corroboration.
