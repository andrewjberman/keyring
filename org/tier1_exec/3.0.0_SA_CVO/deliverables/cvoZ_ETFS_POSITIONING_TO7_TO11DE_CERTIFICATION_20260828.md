# `ETFS_POSITIONING.TO-7` — CERTIFIED 7/7 · `ETFS_POSITIONING.TO-11-DE` — CERTIFIED 6/6

**Author:** `3.0.0_SA_CVO~Z` · **2026-08-28T05:1xZ** · Both filed by `0.4.0_DE_ClientPlatform~C`.

---

## VERDICTS

```
ETFS_POSITIONING.TO-7      rc=0 VALID  rows=7  violations=0   STEP ZERO 7-for-7, set-for-set
                           AC4 + AC5 moved UNVERIFIABLE-BY-INSTRUMENT -> PASS
                           alignment ANNOUNCE (no <decomp_ref>; pre-pipeline, CTO ruling 66492)
ETFS_POSITIONING.TO-11-DE  rc=0 VALID  rows=6  violations=0   STEP ZERO 6-for-6, set-for-set
                           6 PASS
```

⭐ **`TO-7` was UPDATED IN PLACE — no second instance.** The DS half's rows were right when filed
(`UNVERIFIABLE-BY-INSTRUMENT` is the honest value for an instrument that structurally cannot verify a
portal render); the DE lane then did the work that makes them verifiable and **moved the existing rows
instead of minting a rival record.** Two carriers of one obligation is the divergence surface this
estate has paid for repeatedly.

---

## ⭐ `POS-TO7-AC5` — MY **VACATED** RULING DISCHARGED, AND DISCHARGED THE RIGHT WAY

I ruled `AC5` VACATED @`ff29d0d85c`: it named the `isEtfs ? null : dataAsOf` ternary, which an unrelated
lane had refactored away at `7ebe38b0`, so **a zero-hit grep would have scored as a PASS for a reason
unrelated to Models being untouched.** The row addresses that head-on:

> *"THE CITED TERNARY WAS NOT USED AS THE SUBJECT. This row is NOT filed off a zero-hit grep …
> Verified against the successor construct instead: `REGISTERS_YANG_AS_OF.models === true` **IS** the
> Models branch."*

**That is re-grounding, not weakening** — precisely the remedy I named, on a subject that is *stronger*
than the ternary because it is mode-TOTAL.

**And three further things this row does that most do not:**
1. ⭐ **THE CONTROL RAN FIRST.** `PER_BOOK_AS_OF.models` flipped to `true` → `sha256 1e84042df9f22e4c
   / 92818 B`, **differs**. *"The comparison was shown able to fail before its pass was cited."* An
   instrument proven failable before its clean result is quoted.
2. ⭐ **BYTE-IDENTITY BY CONSTRUCTION, NOT BY CARE.** The models arm emits the existing `className`
   string character-for-character — *"the false path is not a re-derivation of today's markup, it IS
   today's markup."*
3. ⛔ **THE BASE-MOVED CAVEAT, MEASURED AND SELF-REPORTED.** A first render pair was captured at portal
   `8c2ba9bb`; another seat then landed `5a4349a5` into this **shared checkout** — 166 lines of
   `Positioning.tsx`, 71 of `HoldingsTab.tsx`, both on the Models render path, **and `ui-smoke.mjs`
   itself.** Every original render *predates* that commit, so they were unconfounded — **and stale the
   same instant, because a byte-identical claim is a claim about a diff against a BASE, and the base
   moved.** They re-ran with both sides at one base and **reported the re-run rather than the lucky
   outcome**: *"the hash is identical at both bases, so nothing was lost."*

---

## ⭐ `T11DE-AC1` — THE STORAGE DISCRIMINATOR WAS BUILT INTO THE CRITERION AND THEN EXERCISED

The criterion carries the clause: *"A FIRST-VISIT VIEWER WITH NO STORED SELECTION LANDS ON INT.
Verified on a CLEARED profile … and the report STATES the profile state."*

```
PROFILE STATE   CLEARED -- ui-smoke launches with no userDataDir and no storageState,
                so localStorage is empty BY CONSTRUCTION
POST-CHANGE     Portfolio Composition selector shows INT active (green)
PRE-CHANGE      same width, same cleared state -> UST active (orange)
=> DISCRIMINATING rather than merely consistent
```

⭐ **"Empty BY CONSTRUCTION" is stronger than "we remembered to clear it"** — it is a property of the
harness, so a successor cannot run this test in the warm state by accident. **The need-bound principle
applied to a fixture.**
**And the mirror hazard is recorded in the artifact, not just in the messages that produced it:** *"a
viewer whose storage already holds INT sees INT whether or not the fix landed, and that FALSE PASS is
silent. A warm browser cannot fail this test, so it cannot pass it either."*

---

## ⛔ ONE DEVICE-LEVEL HAZARD THAT HIT TWO SEATS IN ONE HOUR — INCLUDING ME

**The shared checkout confounded two independent measurements within minutes of each other:**

```
0.4.0_DE_ClientPlatform~C   byte-identity pair captured against a base another seat then moved
                            -> CAUGHT IT, re-ran, reported the re-run
3.0.0_SA_CVO~Z (me)         "13 proxy keys" census counted a peer's UNCOMMITTED, since-reverted edit
                            -> DID NOT CATCH IT. The true count is 12, and the catch-all line number
                               moved :232 -> :203 between our two reads for the same reason
```

>> **This is one device property, not two incidents. A census or a diff-based claim on this box names
its ref, or it is measuring a moment.** I stated `:232` as a source citation and it was true of a tree
that no longer exists. **My conclusion survived; the citation did not.**

---

## SCOPE

- **BRANCH STATE, NOT SERVED.** Portal `46f3863e` and `2858e7f5` are on DEV; **there is no DEV site**
  and only the PROD workflow publishes. Neither TO reaches a rung Andrew can open.
- **Neither is a D1 or D4 closure.** `TO-11-DE` is `ETFS_POSITIONING`, arising from Andrew's
  page-wide INT ruling rather than from the Satellites items.
- ⚠ **`0.4.0_DE_ClientPlatform~C` carries an UNDISCHARGED `comp-system` override** — one gate ordered a
  regen, a second forbids a DE lane from committing it. **They named it as structurally undischargeable
  by their lane rather than routing around it, and logged the audited override.** That is the correct
  handling and the residue is not theirs to close. **Not a defect in either certification.**

---

— `3.0.0_SA_CVO~Z`
