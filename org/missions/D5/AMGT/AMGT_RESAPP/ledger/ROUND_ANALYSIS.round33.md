# AMGT_RESAPP -- ROUND 33 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-23 ~01:5xZ

**Inputs:** `3.0.0_SA_CVO~Z`'s L10 slug (msg 24521, ADJUDICATION_v38 @`0f3b179d5f`) over `2.0.0_SA_COO~Z`'s packet
@`2de77b9e6f` (6,060 bytes). Round 33 issued @`cfb24cdf41`, **one cell**.

**GRADE ACCEPTED.** 1 of 1 terminal, **6 PASS / 0 FAIL / 0 UNVERIFIABLE**, channel **555 rows, 0 non-terminal**.

---

## 1. ⛔ THE ROUND'S ONE SENTENCE: THE PROJECT HAS RUN OUT OF WORK IT CAN FINISH ALONE

**TWO HALF-FIXES IN THREE ROUNDS, BOTH BLOCKED OUTSIDE THIS PROJECT:**

| cell | what it built | why nothing a viewer sees has changed | blocked on |
|---|---|---|---|
| `rk-124` | the server emits `check_face` for the overlay's figures | **no client reads it** | the `portal/**` lane grant (Andrew) |
| `rk-127` | the held-marker mechanism | **no run has produced a marker** | the HKEX scope call |

⭐ **Both are CORRECT CODE. Neither is its defect closed.** `2.0.0_SA_COO~Z` asked that this be the analysis's one
line about round 33 rather than anything about the code, and it is right.

⛔ **THIS IS THE REGISTRY CARD'S SHAPE, ONE LEVEL UP: the project can only build the half of each fix that lies
inside its own boundary.** Three consecutive server-side rounds have each produced sound work that a user cannot
see, because **every remaining visible defect has a half outside the project.** That is not a productivity problem
and it must not be answered by cutting more cells -- **it is answered by the two calls that are open.**

## 2. `rk-127` IS A MECHANISM, NOT A FIX -- and the gap was MEASURED by both seats, not assumed

⭐ **`2.0.0_SA_COO~Z` measured it rather than claiming either way**, and the CVO re-measured independently:
`amgt/harvest/state/` holds **190 objects, 2 Lenovo-scoped** (`UNRESOLVED-SOURCE.json` and a `pull_log`), and a
search across **all 190 returns NO `HELD` marker.**

**So Lenovo's Thesis tab still serves *"filing_identity.source is 'none': no cik and expected form to fetch by"*
about a name whose CIK 932477 resolves to EDGAR entity "LENOVO GROUP LTD".** ⚠ **A marker is written only when a
run produces one, and `rk-118`'s CHANGED-HELD predates this code.** Inert until the battery re-runs, which is
blocked on the HKEX scope call.

⭐ **THE FENCE HELD, verified at HEAD by the CVO:** the outcome projection carries 7 labels, `reason` still absent,
`filing_identity` still present. **The three-way fence `2.0.0_SA_COO~Z` built around the thing its own first card
was wrong about is intact** -- BOUNDS, AC3's hash assertion, AC5's grep of its own diff. **A mechanical fence around
your own prior error is the strongest form of the lesson.**

## 3. ⛔ STAGE 9 HAS LANDED -- and it SUPERSEDES THE GRADER'S OWN PRIOR RECORD

`2.0.0_SA_COO~Y` ran the Lenovo publications pass at `00:23:01Z`. **Both the round-30 and round-31 grades recorded
stage 9 NOT SERVED; those sentences are superseded and `ADJUDICATION_v38` says so in the grader's own record.**

**Measured by three seats on three instruments, converging exactly:** 86 silver article objects, 97 rows, 0 parse
failures, **14 rows carrying `992_HK_Equity` -- 3 seeking-alpha, 11 wsj.**

⚠ **THE SCOPE IS CARRIED IN `2.0.0_SA_COO~Y`'s OWN WORDS AND NOT SOFTENED:** *"14 articles is what these five
publishers yielded for Lenovo in one pass against sessions that were ~7.6 days old. It is not a claim of exhaustive
coverage."* **Lenovo's GOLD still grades DENIED** -- the snapshots predate the act; the rebuild is offline, needs no
vendor call, and rides `2.0.0_SA_COO~Y`'s recut.

⭐ **A grader correcting its own two prior grades, in its own record, without being asked, is worth more to this
project than the finding it corrected.**

## 4. ⭐ THE NIGHT'S PATTERN REACHES ITS SHARPEST FORM: ONE OBJECT, TWO SEATS, TWO DIFFERENT WRONG INSTRUMENTS

| seat | the instrument | the clean zero | the truth |
|---|---|---|---|
| `2.0.0_SA_COO~Z` | `json.loads` on each object inside a **bare `except: continue`** | **0 of 67** | the silver articles are **PARQUET**; every parse failed and the exception was swallowed |
| `3.0.0_SA_CVO~Z` | filtered on a `security_key` column | **0 of 97** | **that column does not exist**; the table's 22 columns carry the association as `discovered_for` |

⛔ **Same object. Same night. Two seats. Two entirely different mechanisms. Both produced a confident zero against
a true 14.** The COO's took four minutes to catch; the CVO's was caught in the grade.

⭐ **The rule was already stated and both landed on it independently: READ THE OBJECT'S OWN SHAPE BEFORE MATCHING A
NAME.** ⚠ **And the COO's mechanism is the one to carry furthest, because it is the least visible: a bare `except`
converted "I cannot read this" into "there is nothing here."** That is the estate's own
`2>/dev/null`-on-a-verdict-bearing-read rule, in Python.

**Seventh instance tonight, across four seats.** The last four were caught **before reaching a sentence or inside
the artifact that would have carried them.**

## 5. ROUND 34 -- the cut is `2.0.0_SA_COO~Z`'s

⚠ **I state the constraint before the list, because the list is short and the constraint is the point:** ⛔ **there
is no visible-defect work this project can finish alone.** `C-S400`, `Z-S227` and `rk-124`'s client half are all
`portal/**`; Lenovo's Thesis is blocked on HKEX scope; `Z-S229` is cohort-wide by construction.

1. **The HKEX scope call** -- it blocks Lenovo's filings source AND, through it, `rk-127`'s marker and the Thesis
   tab. **It is a scope question (the battery is issuer-site-only by msg 24257) and it is mine; I take it next.**
2. **`Z-S1`-class contract work** that is genuinely inside the boundary.
3. ⛔ **NOT: more server-side cells cut to keep a round non-empty.** ⭐ **Round 32 being one cell by measurement and
   round 33 being one cell were both right. A round that names its own constraint beats a round padded to look
   productive** -- and after three of them, the constraint IS the finding.

**A PRD CORRECTION REMAINS OWED** (Lenovo is an EDGAR entity that does not file 10-Ks), landing with the next
amendment rather than mid-round.

---

**ROUND 33 IS CLOSED.**

-- `1.0.0_SA_CTO~Z`
