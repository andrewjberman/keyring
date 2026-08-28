# CTO~Z — both clocks fired, Andrew looked, and he overruled me twice, 0600-1455Z

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, DIAGNOSE, COORDINATE, SCRIBE

**Serial:** `1.0.0_SA_CTO~Z` · **Window:** 2026-08-28 06:00Z -> 14:55Z (continues
`ctoZ_portal_prod_promote_v2_1_170_0435-0600Z.md`)
**Basis:** the 07:00Z / 13:00Z / 13:50Z scheduled fires, then five ANDREW-DIRECT messages from his own
look at the rendered dashboard.

---

## 1. WHAT LANDED

| Clock | Result |
|---|---|
| **07:00:19Z** | `ETFS_SATELLITES.TO-6-AE` **AC3 PASS**. Registry written by the SCHEDULED path, first time ever. |
| **11:06:33Z** | `ETFS_INGEST` rung 1 — the vendor RETURNS `GICS_INDUSTRY_GROUP_NAME`. |
| **13:01:26Z** | ETFs producer: `industry_group` on **189 of 189** holdings (baseline 0). |
| **13:50:50Z** | **Andrew's asset-category cards, 4 of 4 firm scopes.** `TP1AE-AC1` discharges. |

**ANDREW'S VERDICT ON D4:** *"the blended number is definitely the product, i would say thats done"*
— build complete, product question CLOSED. ⛔ **3 certifications outstanding; nobody writes a closure.**

## 2. THE FALSIFIABLE PREDICTION HELD TO THE TICKER

Stated **before** the 13:00Z fire, on `2.0.0_SA_COO~Z`'s corrected denominator:
```
PREDICTED  absent-from-source = EXACTLY 1, and it is ABT
ACTUAL     absent-from-source = 1   book DIVZ, ticker ABT, asset_class Equity
PREDICTED  not-applicable-non-equity = the run's OWN FI count (never a literal)
ACTUAL     8 = CASH x4, FXFXX x2, SALXX x2
```
⭐ **`SECURITY_NOT_IN_CHARACTERISTICS` = 0**, which is why I declined to put a number on that split —
**my unstated estimate would have been wrong.**

## 3. WHAT I GOT WRONG (9 — the honest count)

| Claim | Truth | Caught by |
|---|---|---|
| suppress on MEASURED ZERO; route nulls to "unavailable" | **ANDREW OVERRULED.** A null is a 0 to the end user | Andrew |
| segregation ⇒ suppression must be PRODUCER-SIDE | **ANDREW OVERRULED.** Render-side; "the architecturally simple decision" | Andrew |
| "Andrew will see an EMPTY `Alternatives` card at $0" | **No card renders.** L0 zero-suppression already works | his own screenshots |
| `Alternatives` remedy = "EXACTLY AS INSURANCE IS DONE" | wrong mechanism — it LEAVES the declared L0 node set | myself, 6 min later, without noticing I contradicted myself |
| exact prediction built on `data_as_of 2026-08-26` | the run resolves **08-27**. Right numbers, wrong day | `2.0.0_SA_COO~Z` |
| `classify()` decides ABT's asset class | **`infer_is_cash()` does** — and I had `:1193` in my own output | `2.0.0_SA_COO~Z` |
| "7 blanks ⇒ non-zero ABSENT_FROM_SOURCE" | wrong by 6 — non-equity is tested FIRST | myself, on the corrected denominator |
| "7c71701789 is not on origin; a pull won't get it" | landed between my read and my send | `2.0.0_SA_COO~Z` |
| negative control on `4477e6d8a1` | **it had also been pushed** — a control I assumed, not measured | myself |

⛔ **THE TWO OVERRULES SHARE A SURFACE, AND THAT IS THE FINDING.** Both determined **what a user sees**.
**Every ruling I made about how we MEASURE, RECORD or VERIFY stood unquestioned** — the baseline rule,
name-the-writer, `HOLDING_KEYS` is a validator, observation-vs-verdict, peel the tag.
>> **PRACTICE ADOPTED: mark a ruling `SOVEREIGN-PROVISIONAL` when it determines what a user sees.**
Same authority, conditional DURABILITY. Only the ISSUER can label the two apart — `2.0.0_SA_COO~Z`
sealed two of mine into durable text within minutes and had to strike both. **The fix is my label, not
their speed.**

## 4. FINDINGS THAT CAME FROM READING THE ARTIFACT, NOT THE REPORT

- ⛔ **`ContentLength` is 2196 BEFORE AND AFTER the 07:00Z write.** A size comparison files a FALSE FAIL
  on a fire that plainly happened — and an earlier version moved 2182→2196, so the instrument *looks*
  reliable. **A fixed-shape daily artifact is exactly where length is blind.**
- ⛔ **`platinum/mdpf/` is written by the 13:50Z PUBLISHER, not the 13:30Z gold floor** — 13:50:50Z to
  the second, six consecutive days. The whole fabric had been saying 13:30Z. ⚠ **`head-object` alone
  would have said 16:28Z**, because the newest version on that key is an ad-hoc. **The version LIST
  exposes cadence; the head is one sample, and there the newest sample is least representative.**
- ⛔ **The ETFs chain is ONE stage (13:01:2xZ, 85s after cron) and mdpf is FOUR.** That asymmetry is why
  the conflation was easy: **a correct model from the neighbouring pipeline, transferred to one with a
  different shape. A pipeline's stage count is not inferable from its sibling's.**
- ⛔ **`GICS_INDUSTRY_GROUP_NAME` IS TRUNCATED AT 30 CHARS, MID-WORD**, in the vendor file. Diagnosed
  **without spending the vendor call**: `_scalarize` returns non-dates unchanged, `_el_to_py` is a
  straight `el.getValue()`, and the only slices in the whole path are a date and a log list.
  **The cap is Bloomberg's. The FIX call is HELD at Andrew.**
- ⛔ **An 888-char engineer-facing diagnostic is IN THE SERVED JSON** at `.nodes.Client.predicate_reason`
  — source paths, routing codes, and a named client's $46,436,739.80. **1 of 4 scopes (cottonwood),
  and it is that firm's own data in its own file — NOT cross-firm.** Audience: **Opal staff and
  advisors only** (Andrew). **No portal change can reach it; producer-side.**

## 5. Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `to-check.py` | `--all` | **PASS** — 94 TOs / 40 projects, and it DISCLOSED `unresolved_serials=98` rather than reporting a silent zero |
| `deploy_ledger.py` | `close-leg` x5, `close`, `check --red` | **PASS** — closed the promote 5/5 and surfaced 2 unrelated stranded entries |

**No `comp-*` tool ran this window and that is correct, not a lapse:** every question was *"what does
LIVE STATE say"* — answered by `s3api`, `lambda get-function`, `cloudfront`, `scheduler`, `git
ls-remote`/`merge-base`, and source reads inside a DOWNLOADED Lambda package. **A comp-tool indexes the
repo; the repo was not the subject.** ⚠ **I used native `Grep`/`Read` heavily (nudge-and-proceed), and
under the Rule 21 amendment I authored this window that is the EXCEPTION path — declared, not hidden.**

## 6. Blockers

**NONE at this seat. ZERO open calls at Andrew** — all six from the 14:3xZ card set answered.

## 7. Current State (zero prior context)

- **PROD** `portal-v2.1.170` @`d4a048fd`, served-verified. **Satellites live and its producer proven on
  the scheduled path.**
- **`industry_group` flowing end-to-end**: vendor → gold → publisher → adapter → page. 180 `observed` /
  8 `not-applicable` / 1 `absent-from-source`. ⚠ **values truncated at 30 chars, vendor-side.**
- **Andrew's cards SERVED**, 4 scopes, `as_of 2026-08-27`, sums reconcile at 481,690,858.04.
  ⛔ **Every L2 under `Models` renders `--` — the values are not mapped.**
- **CLAUDE.md Rule 21 AMENDED @`7c71701789`, ON ORIGIN.** Limb 1: only the `infra/*.tf` limb actually
  denies; raw-`aws` INSPECTION does not fire. Limb 2: never `head` ANY census, raw grep included.
- **`3.0.0_SA_CVO~Z` REOPENED** on Andrew's word (he reversed his own closure). ⛔ **Queue is 12; 3 are
  INVISIBLE to `to-check`** (`ETFS_SATELLITES` TO-6-AE/TO-8-DE/TO-9-DE) — **work the list, not the board.**

## 8. Next Steps

1. **[`3.0.0_SA_CVO~Z`]** The 3 Satellites certs first — they are the last gate on a project Andrew
   called done, and they are the 3 the register cannot see.
2. **[`2.0.0_SA_COO~Z`]** 4 held cuts. ⛔ **MAP THE L2 VALUES BEFORE THE SUPPRESSION RULE SHIPS** — every
   L2 is `--` today, so suppression-first empties the layer. Plus `predicate_reason` and `Alternatives`.
3. **[ANDREW]** One held call: authorize a Bloomberg query to test a field-width override / alternate
   mnemonic. **Diagnosis is complete; only the remedy needs the word.**
4. **[`0.0.0_AB_MSTR~Z`]** Integrator pushes; `D1_CATVIEWS.TO-P1-AE`'s face is world-done and stale.

## 9. One thing worth carrying

**Andrew opened the page and found in ten minutes what the fabric had not found in fourteen hours** —
an empty category he had already ruled out, and L2 rows with no values. ⭐ **Every lane verified its own
surface correctly all night.** The defects he saw lived in the seams: **a ruling applied to the fixture
but never cut for the producer, and a smoke test that passed because it ran against the fixture that
HAD the ruling.** ⛔ **The instrument that found them was a human looking at the product** — and no
measurement I ran, however controlled, was pointed at that question.
