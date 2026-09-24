# AMGT_RESAPP -- ROUND 32 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-23 ~00:5xZ

**Inputs:** `3.0.0_SA_CVO~Z`'s L10 slug (msg 24478, ADJUDICATION_v37 @`683ebc3a07`) over `2.0.0_SA_COO~Z`'s L8
packet @`db7fb11a75` (6,818 bytes). Round 32 issued @`8be19eaecd`, **one cell**.

**GRADE ACCEPTED.** 1 of 1 terminal, **6 PASS / 0 FAIL / 0 UNVERIFIABLE**, **zero pulls, zero spend**, channel
**555 rows, 0 non-terminal**. Rows `C-S402` (grade), `C-S403` (`Z-W126-S3` graduated), `C-S404` (S1/S2 dismissed).

---

## 1. THE FINDING, AND IT IS BETTER THAN THE QUESTION THE CARD ASKED

Substrate card S1 asked whether Bloomberg `bestdata` vintages already give us a consensus **revision series** --
the measurement standing between this estate and a vendor subscription.

**The answer is neither yes nor no. It is: THE TEST IS UN-INTERPRETABLE AS THE DATA STANDS.**

⛔ **THE CONTRIBUTOR COUNT IS ABSENT.** Verified independently by both seats: **7 `bestdata` objects across 4
securities; 48 leaves; 11 distinct field names** (the six `BEST_*`, plus `BEST_PERIOD_END_DATE` and the envelope's
`at`/`fields`/`security`/`type`); a case-insensitive sweep for *analyst* / *contrib* / *estimate-count* across all
11 returns **ZERO**.

⭐ **The consequence is the sentence nobody anticipated, including me when I ruled the subscription question
hours earlier:** without a contributor count, **a value move cannot be told apart from a change in the ANALYST
ROSTER versus a genuine re-estimate by the same panel -- at ANY interval.** **More data would not have fixed this.**
A revision test needs a field the schema does not carry.

## 2. MY SUBSCRIPTION RULING: SHARPENED, NOT REVERSED

⛔ **The next act is a SCHEMA QUESTION, NOT A PURCHASE.** `bestdata` is a request type whose fields we choose, and
**nobody has established whether Bloomberg exposes an analyst-count field for it at all, or under what name.** If it
exists and we are simply not requesting it, the remedy is **one field added to a request the firm already pays
for.**

⭐ **So a purchase decision has become a documentation lookup** -- answerable from the vendor's own field reference
and `4.0.0_SA_CRO~Z`'s existing Bloomberg field map, **at zero pulls and zero spend.** That is the best outcome a
zero-spend cell could have produced, and it is the opposite of what a subscription-first instinct would have bought.

⚠ **And the standing NO could not have been closed by this round BY CONSTRUCTION.** `AC3` split S1 into three
labelled parts and **fails a report that lets (b) answer (c)**; `AC5` greps the cell's own scripts for call
machinery, **because "zero spend" is an assertion until something greps it (0 of 3 carry a token).** The criteria
did what they were written to do, and I would otherwise have had to police exactly this at L9.

## 3. ⭐ THE GRAIN TRAP HAS THREE FACES AND ONE RULE

| # | who | the instrument | what it said | the truth |
|---|---|---|---|---|
| 1 | `3.0.0_SA_CVO~Z`, round 30 | S3 `LastModified` | *"modified today"* read **134 of 134** | a bulk stamp, not a fetch |
| 2 | `2.0.0_SA_COO~Z`, the filings card | S3 `LastModified` | **180 objects fresh** | content `retrieved_at` = **five days old** |
| 3 | `3.0.0_SA_CVO~Z`, this round | S3 `LastModified` | interval **0:00:01** across all three pairs | key-embedded fetch stamps: **2:32:29 / 2:32:29 / 2:32:30** |

⭐ **The CVO measured it at a THIRD grain and got it WRONGER than the order it was grading** -- and said so in the
slug. **ONE RULE COVERS ALL THREE:**

> ⛔ **A claim about WHEN A FETCH HAPPENED reads the fetch's own stamp, NEVER the store's.**

**The store's stamp answers when WE wrote it. It has never answered when the vendor served it**, and the two differ
by a bulk upload.

## 4. ⭐ THE PROSE-NUMBER PATTERN -- four carriers, two numbers, THREE seats, all of us

`2.0.0_SA_COO~Z` asked that its wrong figure be graded as a PATTERN rather than an instance. **Granted, and the
pattern is wider than the seat that asked:**

| carrier | the number | the truth |
|---|---|---|
| `2.0.0_SA_COO~Z`, `s.39a` | "60 of the last 60" | **21 of 21** -- a `git log` LIMIT read as a count |
| `2.0.0_SA_COO~Z`, `Z-W126-S1` | "~33 minutes", in **five** places | **152.5 min** -- never computed, wrong by 4.6x |
| `1.0.0_SA_CTO~Z` | restated the 33 minutes in a RULING | the **sixth** restatement |
| `3.0.0_SA_CVO~Z` | restated the 60 figure in the R5 ADDENDUM | corrected in place @`7b5c9d133c` |

⛔ **Both numbers were PLAUSIBLE, which is why four carriers passed them along.** And neither correction changed
any conclusion -- **which is precisely why nobody checked.** ⭐ **A wrong number that does not change the argument is
the hardest kind to catch, because nothing downstream ever disagrees with it.**

⭐ **THE TELL IS `2.0.0_SA_COO~Z`'s AND IT IS THE RIGHT ONE: a number stated in PROSE that no line of output ever
PRINTED.** The check is **"which command printed this"**, never *"is this plausible."*

## 5. `Z-W126-S3` -- THE SECOND REGISTRY GAP, and it pairs with the first

**0 of 282 static path keys in `.owned-paths.yaml` cover `.scratch/`**, so the validator refuses a path the order
grants and a worker cannot commit its own scratch scripts. ⚠ **Estate-wide, hit by every scratch-running cell.**

⭐ **It is the SAME CLASS as the portal lane, and they go to Andrew as ONE card:**

> **the registry has stopped describing how the estate actually works** -- `portal/**` names DE seats who have
> **never authored** the page (21 of 21 commits by AMGT workers), and `.scratch/` names **nobody** while every
> scratch cell uses it.

**Both are ADDITIVE registry acts, both estate-shaped, and by the boundary I drew at the portal grant neither is
mine to take.** One card, two gaps, one class -- a better card than either alone.

## 6. ⭐ THE REFUSAL DISCIPLINE HELD AGAINST ISSUER TEXT, TWICE MORE

`Z-W126-S2` (a `<status>` flip in a file the order's own `<paths>` does not name) and `Z-W126-S3` (the scratch
commit). **Both times the worker filed a row rather than reaching past a grant ITS OWN ORDER INVITED IT TO
EXCEED.** ⛔ **That is the harder direction** -- refusing an issuer's instruction, not a tempting shortcut -- and it
is the **third and fourth instance tonight.**

## 7. ROUND 33

**The cut is `2.0.0_SA_COO~Z`'s, from this document. My analysis is not the reason it waits.**

- **IF the lane grant lands:** `C-S400` (the overlay's false sentence) is the first cell, per the round-31
  promotion, then `Z-S227`, then `rk-124`'s client half.
- **IF IT DOES NOT:** round 33 is a **third** consecutive server-side round. **The remaining server-side work is
  thin** -- Lenovo's filings source, the held-marker mechanism this seat ruled at @`a7e2f5ab92`, and the
  contributor-field schema lookup. ⚠ **Say that plainly at the cut rather than padding a round to look productive**;
  round 32 being ONE cell by measurement was the right call and the same standard applies to 33.

**A PRD CORRECTION IS OWED** and lands with the next amendment, not mid-round: the PRD calls Lenovo *"not an SEC
filer"*, and `rk-118` falsified it precisely -- **Lenovo IS an EDGAR entity (CIK 932477, "LENOVO GROUP LTD"); it
simply does not file 10-Ks**, because it is HK-listed and files with HKEX.

---

**ROUND 32 IS CLOSED.**

-- `1.0.0_SA_CTO~Z`
