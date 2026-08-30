# 49 Financial — 13 accounts we cannot attribute to a custodian

**Prepared for:** Opal Capital management · **Date:** 2026-08-30 · **Prepared by:** Opal data platform
**Status:** Findings are measured and independently reproduced. One question is open and requires 49F.

---

## The short version

Thirteen client accounts, holding **$12.29 million**, appear in the SmartX allocation data we receive for
49 Financial. They are **not present in either of the two 49F Schwab books** we hold. **Eleven of the thirteen** carry
account registrations naming a custodian abbreviated **"FMTC" / "FMT CO"**, which is not Schwab. The
remaining two carry only a person's name, with no custodian designation at all.

We cannot determine from our own data which institution that is. Everything inside our estate that could
answer it is either empty or covers only Schwab accounts. **The one action needed is to ask 49 Financial
who custodies these thirteen accounts.**

Nothing is broken, no data is missing, and no client reporting is wrong today. These accounts are simply
outside the custody books we receive, and we would rather name that plainly than quietly drop them.

---

## What these accounts appear to be

The registration text on **eleven of the thirteen** describes **retirement and trust arrangements** — the
strings carry "CUST" / "CUSTODIAN" and "FBO" ("for benefit of"), and reference IRA, Rollover IRA, Roth IRA
and SIMPLE registrations.
This is ordinary custodial nomenclature for retirement assets held at a trust company rather than at a
brokerage.

That is a coherent and unremarkable business picture: **a client's retirement assets custodied away from
the main brokerage relationship, while the investment models applied to them are still managed through
SmartX** — which is exactly why they reach us through the allocation data and not through the Schwab
custody feed.

They are also structurally distinguishable from every other account we receive:

| | count |
|---|---|
| Accounts in the SmartX allocation map | 5,804 |
| — with eight-digit account numbers (the Schwab pattern) | 5,791 |
| — **with nine-digit account numbers (this population)** | **13** |

The thirteen are the *only* nine-digit accounts in the file, and the custodian designation is exclusive to
them — it appears on **none** of the 7,341 eight-digit rows.

**Two of the thirteen are a slightly different question, and should be asked about separately.** Stated in
both units, because they are easy to confuse:

| | rows | distinct accounts |
|---|---|---|
| Carry an "FMTC" / "FMT CO" registration | 15 of 18 | **11 of 13** |
| Carry no custodian designation, only a name | 3 of 18 | **2 of 13** |

The two without a designation are **645624489** and **655417051**. They are nine-digit and absent from both
Schwab books exactly like the other eleven, so they belong to the same population — but our data says
nothing about who holds them. Describing all thirteen as "the FMTC accounts" would assert something we
have measured for eleven.

---

## What we measured, and how confident we are

**They are not in the 49F Schwab books — either of them.**

| book | master account | rows | our 13 accounts found |
|---|---|---|---|
| 49 FINANCIAL | 0008335338 ("0833") | 7,371 | **0 of 13** |
| 49 WEALTH MANAGEMENT LLC | 0008242234 ("0824") | 7,291 | **0 of 13** |

Each book was checked against its own authoritative account record, using that record's own custodian
field — every one of which reads "SCHWAB". Two independent teams ran the comparison separately and
reached identical results, including reproducing four unrelated unexplained absences by exact account
number.

**Why this "zero" can be trusted.** A zero is the easiest result in the world to produce by accident, so
it was tested rather than assumed:

- **The test can find things.** Of the 5,791 known eight-digit accounts, 5,787 were located in the Schwab
  book — through the identical matching logic the thirteen were put through.
- **The test can reject things.** A fabricated account number was correctly returned as absent.
- **A near-miss was caught and corrected.** The first attempt compared account numbers in a different
  format from the one the book stores, which produces "0 of 13" for a purely cosmetic reason — an answer
  indistinguishable from a real absence. It was caught before it was reported, and the verification was
  rebuilt so the successful control runs through the same formatting path as the thirteen.
- **Four accounts remain unexplained** (four of the 5,791 eight-digit accounts are also absent from the
  book). They are unrelated to this question and are recorded rather than swept aside.

---

## What we cannot answer, and will not guess

**Who custodies these accounts is not answerable from our data.**

The only field in our estate that carries a custodian's *name* comes from a SmartX platform table that is
effectively empty: of its 47 daily files, 46 contain zero rows. The single populated file dates from
2026-07-14, contains 91 records, lists every one as "Schwab", and contains **none** of these thirteen
accounts. It cannot answer the question even in principle.

**On "FMTC":** the abbreviation is genuinely present in the data — it is not something we inferred and
then repeated back to ourselves. But the expansion is not. The word "Fidelity" appears **zero times** in
the entire allocation file. FMTC is widely used for Fidelity Management Trust Company, and that is a
reasonable reading, but **it is a reading, not a measurement.**

The distinction matters for the conversation with 49F: *"these accounts are custodied somewhere that is
not Schwab"* is something our own data proves. *"These accounts are at Fidelity"* would be us telling a
partner something we have not verified. We recommend asking, not asserting.

---

## Why this matters to our work

**It does not affect current reporting.** Client-facing performance and advisor reporting are built from
the Schwab custody books. These thirteen accounts are not in those books and therefore are not, and never
were, part of those numbers. Nothing shown to a client is wrong.

**It does affect scope, in one specific way we have already handled.** The account universe for the
SmartX-driven work is being defined on the 5,791 eight-digit accounts, with these thirteen **named and
explicitly excluded** rather than silently dropped. An account that vanishes without explanation is a
future data-quality incident; an account excluded by name with a documented reason is a decision.

**It leaves $12.29 million of client assets outside our account-level analytics.** These accounts hold
allocations we can see but cannot join to a custody record, so they cannot appear in account-level
performance, fee, or advisor analysis. Whether that matters depends on the answer to the custody
question — which is why the question is worth asking.

**One related item, for completeness.** The two 49F master accounts are registered to **different legal
entities** on the custodian's own records: 0824 is "49 WEALTH MANAGEMENT LLC" and 0833 is
"49 FINANCIAL". Our internal documentation describes their roles (0824 for model portfolios, 0833 for
advisor intelligence) consistent with prior guidance, but the entity distinction had not previously been
recorded on our side and may be relevant to how these relationships are described.

---

## What we recommend

1. **Ask 49 Financial to confirm the custodian for these thirteen accounts.** They are the only party who
   can answer; our estate provably cannot. The account numbers are listed below.
2. **Ask whether these accounts are intended to be in scope** for the reporting and analytics we produce.
   If they are, we will need a custody data feed that covers them; if they are not, the current exclusion
   is already the correct handling and we will document it as intentional.
3. **No system change is recommended at this time.** Building anything before the custody question is
   answered would mean designing for a guess.

**The thirteen accounts:**

```
346482072   628629323   628629325   638330272   638357130
638357389   638379681   638380768   638421860   638451957
645624489   655417044   655417051
```

*Client names and registration details are deliberately omitted from this document. They are available
from the source record if needed for the conversation with 49F.*

---

## Appendix — grounding

| item | value |
|---|---|
| Source of the thirteen | SmartX platform allocation map, dated 2026-08-28 |
| Rows in that file | 7,359 (5,804 distinct accounts) |
| The thirteen | 13 distinct accounts across 18 rows |
| Without any custodian designation | 3 rows = 2 accounts (645624489, 655417051) |
| Combined value | $12,293,768.23 (sum of the 18 rows) |
| Share of accounts | 13 of 5,804 = 0.22% by count; **share by value not computed** |
| Custodian label carrier | the account registration field in that same file |
| "FMTC" / "FMT CO" | 15 of 18 rows = 11 of 13 accounts; 0 of 7,341 eight-digit rows |
| "FIDELITY" | 0 occurrences in the entire file |
| Schwab books checked | 0008335338 (7,371 rows) and 0008242234 (7,291 rows), both dated 2026-08-28 |
| Verification | performed twice, independently, by separate teams; all figures reproduced |
| Open question | custodian identity — not answerable in-estate |

**A note on the SmartX data itself:** the SmartX platform data is held separately from both Schwab custody
books in our storage. An earlier internal description placed this feed under the 0833 Schwab book; that
description was incorrect and has been corrected. It does not change any finding above — all measurements
were taken against the actual locations, not the description.
