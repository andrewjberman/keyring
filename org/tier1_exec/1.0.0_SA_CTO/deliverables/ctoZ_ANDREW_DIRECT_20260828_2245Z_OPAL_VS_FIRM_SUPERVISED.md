# ANDREW-DIRECT 2026-08-28 ~22:45-22:47Z -- OPAL SUPERVISED vs FIRM SUPERVISED, AND THE 49F SCOPE

**Recorded by:** `1.0.0_SA_CTO~Z` · **Broadcast same turn:** msg 14441 + 14446 (5 seats each,
5 DELIVERED / 0 QUEUED / 0 REFUSED both times) · **Surface:** `D1_CATVIEWS` increment 2, item 1.

Four rulings inside ~3 minutes. Recorded VERBATIM because the distinction they draw is not
recoverable from a paraphrase -- the whole content is *which of two same-named quantities is meant*.

---

## 1. THE RULINGS, VERBATIM

**(a) 49F SCOPE + the $138.8M open call**
> *"No for 49F Model Porfolios just conts the 0824 account and that whole thing is supervised. We are
> not looking at the Unsupervised group from 0833 or otherwise, maybe we do that later."*

**(b) THE DISTINCTION**
> *"There is a very important key here that cannot get conflated, there is a differnece between Opal
> Supervised versus Firm Supervised, those two concepts are not the same"*

**(c) THE PROHIBITION**
> *"they cannot be flattened"*

**(d) THE DISPLAY LENS**
> *"What we are showing is always through the lens of Opal Supervised/Unsupervised"*

---

## 2. WHAT THEY MEAN OPERATIONALLY

```
  OPAL SUPERVISED   the residual of accounts holding OPAL MODELS         <- what the NODE means
  FIRM SUPERVISED   the FIRM's own flag -- Cottonwood's Black Diamond
                    `account_supervised`, the whole 458,053,742.19       <- a DIFFERENT quantity
```
- **(b)+(c):** the two may never be collapsed into one node, one label, or one axis. Binds the
  SCHEMA and the RENDERER, not only the ETL.
- **(d):** this view is **SINGLE-LENS** -- everything displayed is the Opal lens. No firm-lens node,
  no dual axis, no perspective toggle.
- **(b)/(c) and (d) COMPOSE, they do not conflict.** The non-flattening rule is what MAKES the single
  lens safe: you cannot honestly show one lens if the two are collapsed, because then "Supervised"
  means whichever source last wrote it.
- **NOT a retirement.** Firm-Supervised is not ruled worthless — only *not what this view shows*.
  Nobody deletes `supervised_split.json` or "cleans up" `account_supervised`. Classification is never
  a deletion warrant (NEVER#3).

## 3. RULING (a) CLOSES AN OPEN CALL, AND CORRECTS ME

`org/tier1_exec/2.0.0_SA_COO/deliverables/OPEN_CALL_49F_UNSUPERVISED_138M_20260825.md` — held by
`2.0.0_SA_COO`, open since 2026-08-25, asking IN or OUT on **$138,839,619.90 / 538 accounts**.
**ANSWER: OUT, DEFERRED.** 49F Model Portfolios scope = the **0824** account, entirely supervised;
the **0833** unsupervised group is not in scope. *"maybe we do that later"* — deferred, not dead.
⛔ **AND IT REVERSES A SUSPECTED DEFECT OF MINE.** I flagged 49financial's served
`Client - Opal Unsupervised = 0.0` as likely wrong, because the registry says *"NEVER Unsupervised
= 0"*. **Under (a) that 0.0 is CORRECT.** It stayed a question instead of becoming a filed finding
only because it went to Andrew rather than into the record.
⚠ **UNVERIFIED, stated at its real strength:** `comp-find` puts `0824`/`0833` on Schwab surfaces
(`schwab-0824-silver-rollforward`, `canonical-schwab-si2/migrate-0833-to-canonical.py`), so they read
as Schwab account/rep codes. **Nobody has confirmed those are the same identifiers Andrew means.**
The ruling is authoritative; the identifier mapping is a LEAD.

## 4. ⛔ WHY NO VALUE-BASED CRITERION CAN CATCH A VIOLATION (`3.0.0_SA_CVO~Z`, msg 14452)

Any AC of the form *"`Client - Opal Supervised` == \<figure\>"* or *"the Client children sum to
`Client.aum`"* **cannot distinguish the two concepts.** Both are plausible dollar amounts, in the same
slot, under the same parent, summing correctly.
>> **THE NUMBER RECONCILES EITHER WAY. ONLY ITS DERIVATION DISCRIMINATES.**

**THE CRITERION MUST ASSERT THE SOURCE, NEGATIVELY, WHERE A GREP CAN SETTLE IT:**
- **AC-DERIVATION (negative):** the code path producing the node reads **neither**
  `D_05.supervised_split.py` / `supervised_split.json` **nor** any `account_supervised` firm flag.
  **POSITIVE CONTROL:** the same probe must FIND those tokens where they legitimately live, so a zero
  is an absence and not a broken search.
- **AC-CONCEPT (positive):** the node derives from the OPAL-MODELS residual.
- **AC-NON-FLATTENING:** schema + render, per (c).

## 5. THE THING WORTH CARRYING

`supervised_split.json` is **clean, MECE, three-valued, and asserts its own totals per date.** Wired
into the wrong node it would reconcile, render, and pass every control it carries — while being the
wrong concept.
>> **EVERY QUALITY THAT MAKES IT A GOOD ARTIFACT IS WHAT MAKES IT DANGEROUS HERE.** Tonight produced
   eight instances of an instrument that was correct about the wrong thing; this is the first where
   the misleading object is a **well-built dataset** rather than a check. A high-quality artifact in
   the wrong slot defeats more controls than a broken one, because a broken one fails something.
