# NFRA_TORECORD — PURPOSE-LEVEL PRD v1

**Project:** `NFRA_TORECORD` (registered 2026-08-26 ~22:2xZ, Rule 27 step 1)
**Directive:** D0 · **Placement:** LAPTOP · **COO lane:** `2.0.0_SA_COO`
**Author:** `2.0.0_SA_COO` · **2026-08-26 ~22:4xZ**
**Certifier:** `3.0.0_SA_CVO` · **alternate base:** `1.0.0_SA_CTO` · **NOT this seat** (author)

---

## 1. THE PROBLEM, RESTATABLE BY A NON-AUTHOR

**A task order reports its own state through several surfaces. A dispatcher reads exactly one of
them. The others are PRODUCTS of doing the work; the one that is read is a SEPARATE ACT OF WRITING
that nothing enforces.**

So the surfaces disagree — **always in the same direction** — and the record routes work using the
field that is wrong. **This is structural, not a discipline problem:** every seat that produced a
divergence tonight was doing its own job correctly against the artifact in front of it.

⛔ **THE CONSEQUENCE IS NOT UNTIDINESS. IT IS RE-ISSUED WORK.** Five near-misses were measured on
2026-08-26; **two reached fresh seats**, and both were stopped by an executing seat declining to
believe a status field — **never by an instrument.**

---

## 2. THE DOMAIN — SIX MEASURED DEFECTS, WITH DENOMINATORS

| # | defect | measured | owner-at-registration |
|---|---|---|---|
| 1 | the `<status>` face nothing enforces — cert + proof land, face still reads open | **5 near-misses; 2 reached fresh seats** | the LINT (authorized) |
| 2 | `<status>` is FREE PROSE | **429 distinct values / 1,991 TOs / 40 leading tokens** | enum act, post-rollout |
| 3 | no declared CERT → TO link; found only by prose grep | **182 CERT-shaped files, substring-matched** | `3.0.0_SA_CVO` |
| 4 | the assignee scan discards the `SEATED:` PROSE notation, not the tilde | **`total=0` over 2,115 files for a lane doing real work** | `1.0.0_SA_CTO` (folded in) |
| 5 | declared instance paths that do not resolve | **67 of 166** | UNASSIGNED |
| 6 | no instance status value can express a criterion the issuer RULED closed | **0 of 1,067 rows carry `CLOSED`** | enum act, post-rollout |

**Denominator note, and it is load-bearing:** the lint that motivated this project **can fully
examine 99 of 2,067 task orders — about 4.8%.** 1,991 carry a `<status>`; 166 declare an
`instance_path`; **99 resolve.** ⛔ **A report of "0 findings" across 2,067 TOs while structurally
blind to 1,968 of them IS the silent no-op**, so coverage is a first-class output of anything built
here, never a footnote.

---

## 3. ⛔ WHY THIS IS ONE PROJECT — THE COMPOSITION IS THE FINDING

Each defect independently returns a **confident wrong answer** to the same reader, about the same
object, in the same direction. **They also compose, and the composition defeats piecemeal repair:**

> **The obvious remedy for #4 — re-file the TO into the live lane's directory — produces a file that
> LOOKS correctly seated and is STILL invisible to the assignee scan, because the discarded field is
> the `SEATED:` prose and not the path.** A repair that removes the only visible symptom and leaves
> the defect. **Fixing #4 alone makes the estate worse.**

And **#2 and #6 are the same enumeration act one layer apart** — a status vocabulary over 1,991 TOs
and a criterion-status vocabulary over 1,067 rows. **Minting them separately, by two seats, on two
nights, is how one record surface ends up with two incompatible vocabularies.**

**Six correct local decisions add up to nobody owning the surface.** That is what this project exists
to stop, and it is the reason the six are registered together rather than fixed apart.

---

## 4. INVARIANTS — binding on every cell the decomp will cut

· **`TR-inv-1` — NOTHING BUILT HERE BLOCKS WORK.** Every mechanism is a **lint on the RECORD**, never
  a gate on a lane. Andrew authorized the lead item as a consistency *check*; **a gate is outside the
  authorization and outside this project.**
· **`TR-inv-2` — ⛔ NO MECHANISM MAY WRITE A STATE NOBODY OBSERVED.** No auto-flip, no synthesized
  `cell_status`, no inferred completion. **AUTO-FLIP IS THE OBVIOUS FEATURE AND IT IS FORBIDDEN TWICE
  OVER:** it asserts an unmeasured state, **and it destroys the evidence of the defect it was built to
  detect** — the disagreement vanishes silently and the unenforced obligation becomes permanently
  invisible.
· **`TR-inv-3` — COVERAGE IS AN OUTPUT, NOT A FOOTNOTE.** Every run prints what it could and could not
  examine, with the denominator. **A confident zero over a population it cannot see is the failure
  mode this project is about, and it must not be reproduced by its own remedy.**
· **`TR-inv-4` — A VALUE CARRIES ITS CLAIM.** Anything this project emits distinguishes
  `measured` / `inferred` / `absent` in a field a consumer can branch on — **and the consuming half is
  the mechanism: without a consumer that REFUSES an unmarked value, the field is decoration.**

---

## 5. THE REQUIRED FAILURE MODE (Rule 28 q7)

**THREE outcomes, never two: `CONSISTENT` / `INCONSISTENT` / `UNREADABLE`.**

⛔ **`UNREADABLE` IS COUNTED AND PRINTED AND NEVER FOLDED INTO A PASS.** A record-lint that silently
no-ops emits output **byte-identical to a clean estate**, and its failure is **anti-correlated with
its own visibility: the more completely it is broken, the cleaner it reads.**

**A two-value schema here is the same defect as #6 one layer up** — the case where the mechanism
cannot answer collapsing into the clean negative.

---

## 6. EXPLICITLY OUT OF SCOPE

· **Any gate, approval step, hold or sign-off.** Not from prudence, symmetry or precedent.
· **Auto-remediation of any kind** — see `TR-inv-2`.
· **The enum mints (#2, #6) as a late-session edit.** They are Rule 24 acts over live populations and
  belong inside this project with printed denominators.
· **Whether the same face-vs-artifact divergence exists on PRDs, project JSONs or registry entries.**
  Not measured; **not assumed either way**; a separate ask if wanted.
· **Adjudicating the 11 TOs that fire the strengthened predicate today.** They are evidence the SHAPE
  recurs at scale, **NOT a defect count** — none was individually adjudicated and some may be
  legitimately open.

---

## 7. ⛔ THE EMBARGO BOUNDARY — ruled by `1.0.0_SA_CTO`, on the record so the scope survives the week

Under Andrew's ~20:32Z products-first word:
· **THE FACE-FLIP LINT BUILDS when the COO schedules it** — Andrew authorized that mechanism **BY
  NAME** (~21:07Z, `@862b6bf35c`), so it is **outside the embargo by sovereign word**.
· **THE OTHER FIVE ARE RECORDED WITH OWNERS AND BUILD IN THE POST-ROLLOUT PLATFORM DRIVE** — unless
  one **demonstrably blocks a product from shipping correct data during the week**, which is the
  embargo's own exception and **gets said loudly at the time**, not assumed quietly.
· **The enum mints are exactly the deliberate-pass work the post-rollout drive exists for.**

---

## 8. WHAT "DONE" WOULD MEAN (purpose-level only)

**A dispatcher reading the TO record gets an answer that is either RIGHT or VISIBLY UNKNOWN — never
confidently wrong.** Concretely: a completed-and-certified TO cannot present as open to the one field
a dispatcher reads; a lane's real holdings are discoverable by the sanctioned scan; a criterion the
issuer ruled closed has a value that can say so; and every instrument states the population it could
not see.

⚠ **NOT in scope of "done": that no TO is ever mis-dispatched again.** The remedy is a record that
**does not lie**, not a record that **cannot be misread**.

---

## 9. PROVENANCE + A DATED CAVEAT

Six defects measured 2026-08-26 by **five seats** — `0.8.0_AE_CloudComp~F` (#1, first, unprompted, on
its own surface), `0.4.0_DS_ClientPlatform~V` (#1 root cause + #2/#3/#5 census), `0.4.0_DS_ClientPlatform~R`
(#6, 0 of 1,067), `0.7.0_AE_CloudOps~L` (#4 mechanism), `0.4.0_DS_ClientPlatform~S` (#1 instance).
**First artifact: the face-flip check spec `@9a2a020870`.**

⛔ **THE COUNTS IN §2 ARE A VINTAGE.** They were measured across one evening on a live, moving
population; **`0.4.0_DS_ClientPlatform~R` watched its own census move from 1,061 to 1,067 rows inside
fifteen minutes.** ⚠ **The decomp re-runs every denominator at its own hand and does not inherit these
— the SHAPE is the finding, the DIGITS age.** One project over tonight, a certified decomp went stale
under a sovereign word four hours later and stayed stale 21 hours while work was delivered against it.
