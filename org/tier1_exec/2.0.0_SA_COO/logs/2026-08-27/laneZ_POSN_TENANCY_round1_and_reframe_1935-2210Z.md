# 2.0.0_SA_COO~Z — POSN_TENANCY ROUND 1 + THE ~21:52Z REFRAME, 1935–2210Z

**archetype:** COORDINATE · **secondary:** VALIDATE, DIAGNOSE
**Predecessors this session:** `laneZ_D1_D4_execution_1657-1815Z.md`, `laneZ_D1_D4_delta_1815-1935Z.md`
**Written for a ZERO-CONTEXT successor.** Read §1 and §2 before touching anything.

---

## 1. ⛔ THE ONE THING A SUCCESSOR MUST NOT MISS

**ANDREW-DIRECT ~21:52Z, VERBATIM:**
> *"all of Positioning is general, it was always meant to be a general page, but we are making an
> exception in the case of cottonwood here for the purpose of their "Satellites" portfolios."*

**This REFRAMED and SHRANK `POSN_TENANCY` after round 1 was cut.** My decomp's section (a)
specified re-plumbing the WHOLE Positioning artifact onto `/api/scoped/`. **He wants ONE FIRM'S
EXCEPTION on a page that is general BY DESIGN.**

⛔ **`PT-a-1`'s premise was FALSE WHEN WRITTEN, not overtaken.** Positioning was never on
`/api/scoped/` — 5 of 5 fetch sites are `/api/general/`, `public-data-router` holds 0 firm
references across 71 lines, and a 4,125-key sweep (terminal `IsTruncated: None`) found 0 firm
segments. **The decomp specified a change to an architecture it never measured.** Section (a)
re-scoped `@969e6b34eb`; **`PT-a-1`/`PT-a-3` RE-CERTIFICATION REQUIRED before any round-2 cut.**

⭐ **AND THE EXPOSURE IS SCHEDULED, NOT HYPOTHETICAL.** The served artifact is **OPAL-COMMON**
(`portfolios` = INT/LT/ST/ULT/UST, 0 firm tokens across 73,424 decompressed bytes, positive control
`portfolio`=19). So today it is a **design gap, not an incident** — but **the serving plane has no
firm discrimination at all, and he has now NAMED the firm-specific content that will enter it:
Cottonwood's Satellites.** ⛔ **The discrimination must exist BEFORE that content lands. That
ordering is the project.**

---

## 2. STATE AT HANDOFF

| TO | seat | state |
|---|---|---|
| `POSN_TENANCY.TO-2-DS` | `DS~L` | **ACCEPTED 4/4** `@e4b264c7c4`, certified `@56108425c4` |
| `POSN_TENANCY.TO-3-AE` | `AE~Y` | **COMPLETE AS A MEASUREMENT** `@8554814869`, certified `@2efba0f665` — ⛔ **CELLS NOT DISCHARGED** |
| `POSN_TENANCY.TO-1-DE` | — | **BLOCKED** — my Rule 27 mis-seat; needs a fresh DE lane |
| `D1_CATVIEWS.TO-L2-DS` | `DS~Z` | ACTIVE — AC1/2/4/5 certified, AC3/AC6 done, **AC7 outstanding** |

⛔⛔ **STRUCK ~22:5xZ — THIS LINE WAS A MALFORMED QUESTION AND I CARRIED IT ALL SESSION.**
~~AT ANDREW: the satellite membership maintainer (`REGISTRY_MAINTAINER = None`) — NOT covered by
"yes approve all recs"; that card carried NO REC.~~

**ANDREW-DIRECT ~22:5xZ, VERBATIM** (`@efa437d8ef`):
> *"This shouldnt be handdrawn at all, it should simply be 'Does it say "Opal Satellite" in the name?
> Add it and track henceforth if so. If an Opal Satellite disappears from daily pulls, now it is no
> longer tracked.'"*

>> ⛔ **MEMBERSHIP IS A PREDICATE OVER THE DAILY PULLS. `REGISTRY_MAINTAINER` IS NOT "STILL None" — IT
   IS DISSOLVED. A DERIVED SET HAS NOTHING TO MAINTAIN; THE PREDICATE IS THE MAINTAINER.** <<

⛔ **AND THE FAILURE IS MINE AS MUCH AS ANY SEAT'S. I reported this as the single open item at Andrew
in EVERY report tonight — eight or nine times — and I NEVER ONCE ASKED WHETHER A MAINTAINER SHOULD
EXIST AT ALL.** I refused to name one by inference (**correct** — `SAT-inv-2` is exactly what that
refusal avoids) and routed it as sovereign (**also correct**), and both correct acts left the
malformation untouched.
⭐ **`1.0.0_SA_CTO~Z`'s formulation, adopted:** *"A WELL-FORMED REFUSAL TO ANSWER A MALFORMED QUESTION
STILL LEAVES THE MALFORMATION IN PLACE… RESERVING A QUESTION PROTECTS ME FROM ANSWERING IT WRONGLY
AND ALSO FROM NOTICING IT IS THE WRONG QUESTION."*
⚠ **Andrew supplied the premise correction. No seat did, across five hours and four carriers.**
**BLOCKED, NOT DEFERRED:** round 2 on `PT-a-1`/`PT-a-3` (CVO re-cert) · `TO-1-DE` (DE lane) ·
`PT-inv-3` (a CREDENTIAL grant, not code).

⛔ **`PT-inv-3` — null firm fails closed — HAS NEVER BEEN EXERCISED**, carried into the decomp
`@6a07d17cbb` **because `TO-3-AE` is closed and a closed record is where an open item goes to die.**

---

## 3. WHAT I GOT WRONG — SEVEN, AND SIX ARE ONE CLASS

1. **Rule 27 mis-seat.** Seated a 2nd project on `DE~Y`, which held 2 open `ETFS_SATELLITES` TOs.
   `gate2` refused in ANNOUNCE mode; the commit landed anyway. **I read the seat's SUMMARY ("IDLE")
   as its HOLDINGS.** ⭐ **And I had just run a PID probe and felt covered — that probe answers "is
   this seat ALIVE", Rule 27 asks "is this seat FREE". A PROBE THAT FIRES CORRECTLY IS THE MOST
   EFFECTIVE WAY TO STOP LOOKING.**
2. **`PT-inv-7` grounds invalid** — sent CVO an urgent correction about a cell **absent from the pin
   they were certifying.** I conflated my working file with the pinned object.
3. **TWO items parked "OPEN AT ANDREW" he had already ruled AND ASSIGNED TO ME** — the AE re-scope
   (CALL 3) and the SMA-dollars question, whose answer sat verbatim in
   `mdpf_gold_consolidator.py:573`, unread. **Both rulings arrived inside answers I wanted for a
   different limb, and satisfaction ended the read.**
4. **Markdown backticks in `<decomp_ref>`** → a compliant executor's proof instance read **INVALID**.
5. **`AC7` named FIVE sites; there are SEVEN.**
6. **`<instance_path>` pointed at `~Z/deliverables/` — a directory that DOES NOT EXIST.** ⭐ Caught
   BEFORE filing. (4/5/6 are one class: **prose written fluently into fields a PARSER reads.**)
7. **Asserted the render "deliberately withholds a bar" from COMMENTS.** The code is data-driven and
   correct (`hasAmounts` computed from rows). ⛔ **`comp-find` printed `[DOC] — may be STALE` on the
   very lines I quoted.**

> ⛔ **THE UNIFYING SHAPE: I MEASURE ARTIFACTS WELL AND MY OWN SENTENCES BADLY** — and a wrong
> CRITERION is worse than a thin one, because **an incomplete criterion leaves work undone; a
> MISDESCRIBING one causes work to be done wrong.**

**AND ANDREW CORRECTED THE COMP-FIND HABIT A 4TH TIME.** The real pattern: **I use `comp-find` to
LOCATE, then drop to grep to INSPECT.** The rail holds while I don't know where something is and
evaporates the instant I do. **Cost: a grep chained against a format I never read returned a CLEAN
ZERO.** When run properly, `comp-find "SMA_MEMBERS"` returned **`DEF=1`** — one definition site —
**and THAT was the verification, because MECE over a WRONG domain passes vacuously.**

---

## 4. WHAT THE FABRIC PRODUCED THAT I DID NOT

- **`DS~L`: a GRAIN trap that would have INVERTED a criterion** — token `position` matches **922 of
  6,599** objects in Cottonwood's home = the *canonical positions* pipeline, a different grain. A
  naive census reports PRESENT; the true answer is ABSENT.
- **`DS~Z`: "the restructure and the emit contract are ONE ACT"** — two TOs would have built the same
  surface twice. Also the `:245` **PREMISE/REASONING split** — the reasoning (*"$0 would say 'this
  firm holds none of it' about a firm holding millions"*) **outlived its premise by 40 minutes and
  Andrew then ratified it.**
- **`CVO`: `D1-h-r3` carries FOUR claims, not two** — both CTO and I quoted to *"his four, verbatim"*,
  **stopping exactly where the cell switched from DESCRIBING to PRESCRIBING.**
- **`AE~Y`: discarded their own AC2 arm** — forged `X-Firm-Id` → byte-identical 200s, **which BOTH
  hypotheses predict.** Replaced with the 403-envelope echo + a positive control.
- **`AE~Y`: the cache-key trap** — with one common artifact, adding firm to the cache key partitions
  **IDENTICAL BYTES**: a green-looking control measured against the wrong era.

---

## 5. FABRIC FINDINGS (routed, not built — moratorium)

⛔ **`DELIVERED` READS AS `[ACTIVE]`.** `to-check.py:51` `COMPLETE_WORDS` omits *"delivered"*;
`_classify_status` defaults unknown → `return "ACTIVE"`. **2 open TOs affected.** ⭐ **SECOND enum
tonight missing a value, BOTH defaulting toward MANUFACTURING WORK** (proof-of-spec has no
"correctly blocked"). Measured cost of that direction: `TO-R1-DS`'s stale ACTIVE **recruited two
seats onto finished work.** `1.0.0_SA_CTO~Z` has since ruled against adding the value; the finding
stands.

⚠ **5 OPEN TOs ON SEATS THAT ENDED TONIGHT** — `~P`(2) `~W`(2) `~Y`(1); `~Q` died holding 0.
**Nothing wrote a line for any of the four deaths.** ⛔ **BOUND: 13 of 15 TO-holding seats are not
live HERE, but the broker is LOCALHOST-ONLY and TO files are shared with the laptop fabric — "not
live here" is NOT "dead."** Only the four watched ending on this box are claimed.

⚠ **`ADVI_STITCH.TO-A1-DS` is addressed to the literal placeholder `0.4.0_DS_ClientPlatform~<letter>`**
— issued by this office's base lane, status DELIVERED (so it reads ACTIVE), executed by `~Q` (dead).
**Three defects on one row.**

---

## 6. METHOD NOTES A SUCCESSOR CAN USE

- **Seating requires BOTH axes:** ALIVE (PID probe, with controls) **and** FREE (`to-check`) —
  **never the seat's own summary**, which answers neither.
- **`comp-find` on the CITATION, not the topic.** `D1-h-r3` → `SURFACED=2` directly; `"SMA L1"` → 16
  candidates needing classification. **Sweep what CITES a thing to find its dependents.**
- **A blank field in a per-file loop is a FINDING.** Two blank rows were `portal/` files — the parent
  repo cannot date a submodule's files, and those two were the most important in the set.
- **An artifact certifies its own plane:** `ContentLength 8088` matched the served response — but
  ⚠ **a size match is a COINCIDENCE CANDIDATE; the ETag is the identity check** (`DS~L`'s correction
  to my evidence).
- **Ten zeros beside a parse error is the instrument broken, not the world empty.** The Positioning
  artifact is **gzipped**; my first token scan grepped compressed bytes and returned a clean,
  wrong answer that agreed with what I expected.

— `2.0.0_SA_COO~Z`
