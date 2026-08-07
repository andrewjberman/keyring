# ATOM_DECOMP — STATE OF THE PROJECT + NEXT STEPS (2026-08-07, as of 21:30Z)

**Author:** `4.0.0_SA_CRO~A` (ATOM_DECOMP corpus audit lane)
**archetype:** SCRIBE · **secondary:** VALIDATE
**Window:** 18:25Z → 21:30Z. **Prior log:** `cro_lane_a_atom_decomp_pass1_audit_1645-1825Z.md`.

> ⚠ **CORRECTION TO MY OWN PRIOR LOG'S FILENAME:** it is named `1645-1825Z`, but that session did not
> end at 1825Z — it ran to the last commit at **21:23Z**. The name understates the window by ~3h.
> **Not renamed deliberately** (it is cited in this file and in commit messages; renaming would
> manufacture dangling citations to save a digit — the exact trade `07` records). **The window in the
> name is wrong; this line is the correction.**

---

## 1. WHAT THIS PROJECT IS

`projects/ATOM_DECOMP/` is a **method package**: a specification, a portable skill, fill-in templates,
and a worked case study, describing how to take a large system apart and rebuild it safely — before a
migration, standardization, consolidation or decommission. It was **authored by GPT**, is **Andrew's
folder**, and its named method owner is `1.0.0_SA_CTO~A` (`00:4`).

**72 tracked files** — 68 GPT-authored (at import @`66d83132d5`) + 4 authored by `4.0.0_SA_CRO` base
on 2026-08-07.

## 2. WHAT HAPPENED TODAY

A dedicated lane (`~A`, this seat) was spawned to audit it because it is GPT-authored and Andrew
wanted it examined. **Audit-only first pass**, then — on his ruling — **repair**.

**Andrew-direct ~1915Z:** *"Recs are approved go ahead"* (@`fbf4a18120`) — mechanical refinement +
one audit-only read of the held-out case files.
**Andrew-direct ~1940Z at base's terminal:** *"Approved acrtoss the board"* (@`784e17bb66`) —
ratifying base's proceed-condition. **The unwind contingency is discharged, not exercised.**

**19 commits. 15 findings. 9 corpus files repaired. 72/72 files audited at some depth** (21 read in
full; all 51 case-study files sized + content-hashed, trigger pair read substantively).

---

## 3. WHAT IS TRUE NOW — verified, and verified at WHICH LAYER

**All four repairs are CONFIG-LEVEL and were checked with firing controls.**

| finding | state | how it was verified |
|---|---|---|
| **F-1** charter template was invalid YAML | **FIXED** | parser run both directions: original @`66d83132d5` → `ScannerError` line 14; fixed → 14 keys. Control: `.owned-paths.yaml` parses. |
| **F-12** `00` §7 index dangled 3 of 5 paths | **FIXED** | 8 of 8 entries resolve (was 5 of 8) |
| **F-4** 11 ledgers mandated, 7 shipped | **FIXED** | 12 of 12 mapped; 6 templates added, LF-verified with `file(1)` |
| **F-3** opening instruction gate-denied; `comp-pipescript` withheld against XXX.md mandate | **STRUCK** (CTO ruling) | both strings 0 now, 1 each at prior vintage @`f9d1d2e73f` |

## 4. ⛔ WHAT IS **NOT** TRUE — and this is the load-bearing section

**THE METHOD IS NOT DEMONSTRATED TO WORK. IT HAS NEVER BEEN RUN — not once, not on anything.**

Everything in §3 is *"the file is well-formed."* **None of it is a behavioral claim** (Rule 22a: a
config read cannot ground a "works"). Specifically:

- **Gates G0–G7 have never been exercised.** No run has passed or failed one.
- **The six templates I added are headers I derived from the spec's own field lists.** Reasonable,
  traceable to text the method already carries — and **never filled in by anyone.** A header nobody
  has filled is a hypothesis about what the work needs.
- **`02:5` prescribes the cure and it is still undone:** *"Use the packaged skill manually on one
  read-only system audit."* **That is the corpus's own stage 1 and it has not happened.**
- **F-2 IS STILL LIVE IN THE CORPUS.** Two contradictory normative rule-lists remain. An agent
  picking the package up today can obey either and be non-compliant with the other **without seeing
  the conflict.** Not fixed deliberately — fixing it means choosing, and that is a naming act.

**Accurate one-line status: it no longer fails BEFORE you start. That is not the same as working.**

---

## 5. NEXT STEPS — ordered, each with owner and what unblocks it

### ⬛ STEP 1 — **AT ANDREW: rule which rule-list is operative** *(the only thing gating nothing else, and the cheapest)*
**Owner: Andrew. Ready now — the delta table is built and sitting in the audit report.**
Two lists disagree: `00` §5's 8 "non-negotiable laws" vs `SKILL.md:10-21`'s 9 "Rules". Neither
contains the other — **5 of 8 laws have a Rule; 5 of 9 Rules have a law.**
**CTO ruled `SKILL.md` operative, then AMENDED itself: that is *necessary and not sufficient* — a
ratification must EXPLICITLY carry laws 3/4/5 forward or retire them BY NAME. "Silence on them is not
adoption, it is loss."**
⚠ **Law 3 is the single best-evidenced law in the corpus** (proven on live AWS: 154→155 triggers
concealing −4/+5 and 13 stale registry rows) **and it is one of the three at risk.**
**Cheap to rule once with the table in front of him; expensive to unpick if guessed.**

### ⬛ STEP 2 — **THE REAL TEST: run the method once, read-only, on one contained system**
**Owner: UNASSIGNED. Not started, not staffed, needs Andrew's word that it is worth the cycles.**
**This is the only thing that converts "no longer broken" into "works."** It is `02`'s own stage 1,
it is cheap, and it is the acceptance event for every repair in §3 — the templates get filled, the
gates get exercised, and the method either produces something useful or collapses.
**Needs: (a) a subject system, contained and read-only; (b) an owner; (c) a decision it is worth
doing.** **Recommendation: yes, and small** — a method whose first real use is a live migration is
being tested in the worst possible place.

### ⬛ STEP 3 — base CRO's six own-file findings *(F-8/9/10/11/13/14)*
**Owner: `4.0.0_SA_CRO` base. AUTHORIZED by Andrew ~1940Z. Base's lane, explicitly not mine.**
Internal contradictions and version-record defects in base's own four files. Real, second-order, and
nothing depends on them.

### ⬛ STEP 4 — F-15: 11 of 51 case-study files are duplicate copies
**Owner: unassigned. NOT fixed. Low urgency, non-zero risk.**
5 documents stored at 2–3 paths each — **45 distinct documents in 51 files.** All byte-identical
**today**, which is why it is worth naming: **they acquire a contradiction on the first edit to any
single copy, silently.** 4 of the 6 files in the case study's own "Durable ADVI source set" are among
them. **Decision needed: dedupe, or declare one canonical path per document.**

### ⬛ STEP 5 — BANKED, not scheduled
- **Full tool-decoupling of the method.** CTO banked this as a **method-design question, not a
  defect** — my F-3 edit deepened an existing estate-coupling (bounded by naming the category before
  the instance). A separate, larger edit; nobody's tonight.
- **`.owned-paths.yaml:425` "89 tracked files"** → routed to CTO by base. Text fix only; the grant
  itself is sound.

---

## 6. ⚠ ONE OBSERVATION I NOTICED AND NEVER FILED — recorded rather than quietly dropped

**`02` §3's evaluation suite lists NINE scoring dimensions** (denominator closure, edge recall,
contradiction detection, claim reproducibility, consumer-contract preservation, work-package
atomicity, rollback quality, cleanup completeness, false absence assertions) — **with no scale, no
threshold, and no pass bar.** *"Score X"* without a bar is unfalsifiable, and it sits directly beside
§4's acceptance targets, which ARE crisp.

**I read this at ~17:0xZ, judged it lower-severity than the mechanical defects, and never gave it a
finding number.** It is not in the audit report's 15. **If there is a second pass it should be
F-16**; I am naming it here rather than letting an unfiled observation evaporate, because "I noticed
it and did not file it" is invisible to every instrument.

---

## 7. COMPILER TOOLS

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-state --self-test` | gate before trusting drift | **PASS 3/3** | instrument discriminates |
| `comp-state` | drift sweep | ~800 BEHIND, **noise-dominated** | `REGROW REGISTRY` rows whose evidence commits are about C3.ii — lexical false positives, triaged not actioned |
| `get_live_agents` | fabric roster | 11 LIVE | used for the exec-sum, not for this state doc |
| `python yaml.safe_load` | F-1 repair verification | **FIXED parses / ORIGINAL fails** | via stdin — a `/cygdrive/c` path is invisible to native-Windows Python |
| `file(1)` | line-ending checks | 9 of 72 CRLF | adopted after `grep $'\r'` failed its own positive control |
| `git ls-tree` / `cat-file -e` | denominators + pin validation | 72/72, 5/5 pins | the 89 refutation |
| `md5sum` | case-study duplicate census | 11 of 51 | F-15 |
| `safe-commit.sh` | 19 commits, all `-F` | PASS | one correctly REFUSED — I had written a message for edits I had not made |

**What worked:** printing the denominator before every count — it caught the 89 before it became my
coverage figure. **What failed:** six instrument failures of my own, all caught by controls and none
by care. **Gap found:** none in the tooling.

## 8. BLOCKERS

**None at me. This lane has no addressable work left.**
- **At Andrew:** STEP 1 (which rule-list) and STEP 2 (authorize the first real run).
- **At base CRO:** STEP 3, its own six findings — authorized, its lane.
- **Unowned:** STEP 4 (duplicates) needs someone assigned or a decision to accept them.
