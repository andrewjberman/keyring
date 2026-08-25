# Z-S48 ACCEPTANCE ORACLE -- AMENDED BY ITS DISARM OWNER, 2026-08-25 ~08:0xZ

**Owner:** `2.0.0_SA_COO~Z` (the `disarm_owner` named on the row itself)
**Row:** `ETFS_INGEST-Z-S48`, `org/surprise_channel/ETFS_INGEST/INVESTIGATION_v1.Z.md:1273`
**Status of the row:** **UNCHANGED -- `UNDER_INVESTIGATION` / `ARMED`. Tonight's act does NOT disarm it.**
**Push state:** landed LOCAL, rides integration (LD-0367).

---

## 1. WHY THIS FILE EXISTS -- A CORRECT FIX WAS ABOUT TO FAIL A STALE ORACLE

Z-S48 published an acceptance oracle **with its values fixed in advance** (msgs 8457-8461), and that
was the right thing to do -- it is unpassable by merely *changing something*:

> *"exactly FOUR names change -- JPM to JPMorgan Chase & Co., MRVL to Marvell Technology Inc,
> VZ to Verizon Communications Inc, SALXX to a proper-cased fund name -- and the other 162 stay
> BYTE-IDENTICAL."*

**Tonight's Andrew-direct remedy changes TWO names (SALXX, FXFXX), and one of them is not in that
oracle at all.** Left standing, the oracle **fails a correct fix**, and because it was deliberately
built to be strict it fails *loudly* -- presenting as a real defect at exactly the moment somebody
is verifying a sovereign-ordered change.

> **A control pinned to a constant that the sanctioned fix will move stops being a control and
> becomes a manufactured finding.** The oracle was right when written. The scope moved under it.

## 2. THE AMENDMENT (binds tonight's act ONLY)

```
TONIGHT'S ORACLE:  exactly TWO names change -- SALXX, FXFXX.
                   The other 167 served names stay BYTE-IDENTICAL.
                   (denominator: 169 distinct tickers, platinum/etfs/positioning_data.json @04:53:51Z)
```

**The 4-name oracle is SUSPENDED, NOT DELETED.** It remains the acceptance oracle for the
*case-normalisation* defect, which is **not** tonight's work and is not authorised tonight.

## 3. THE DISTINCTION THAT JUSTIFIES THE NARROWING -- TWO DEFECTS, NOT ONE

The row treated "all-caps" as one class. It is two, and they take different authority:

| | instances | what is wrong | authority |
|---|---|---|---|
| **UNREADABLE VENDOR STRING** | `SALXX` "STATE STREET INST U.S. GOVERNMENT MMKT ADMN CLASS" · `FXFXX` "First American Treasury Obligations Fund 01/01/2040" | vendor **cruft** in a client-facing name (share-class tokens, a maturity date) | **ANDREW REPORTED THIS.** In scope tonight. |
| **MERELY UPPERCASE** | `JPM` · `MRVL` · `VZ` | the name is **correct**, the **case** is not | a different defect. **Out of fence tonight.** |
| **LEGITIMATELY UPPERCASE** | `BP` · `GSK` · `MPLX` | nothing -- the capitals **are** the name | open product fork, Andrew's call. Untouched. |

`0.4.0_DS_ClientPlatform~Z` proposed the 2-ticker scope and **flagged its own divergence from the
published oracle rather than silently narrowing it.** That is why this amendment happened before the
remedy rather than after it failed.

## 4. THE OBSERVATION THAT OUTLIVES TONIGHT -- Z-S48's DETECTOR UNDER-COVERS ITS OWN CLASS

**`FXFXX` is not all-caps.** Z-S48's predicate (`all alphabetic characters uppercase`) **never saw
it**, and FXFXX is the same defect as the one the row was opened for.

The row already records that its detector cannot separate *correctly*-uppercase from *wrongly*-
uppercase -- a failure on the **inside** of its match set. **This is the mirror failure, on the
outside: a member of the true class that the predicate cannot match at all.**

> The real class is **"a vendor string that is not a display name."** All-caps was a **PROXY** for
> it. The proxy over-matches (BP/GSK/MPLX) *and* under-matches (FXFXX) simultaneously.
> **So Z-S48's count of 7 is neither a floor nor a ceiling, and must not be quoted as either.**

This is why the remedy is a **curated map**, not a transform: no string function maps
`STATE STREET INST U.S. GOVERNMENT MMKT ADMN CLASS` to `State Street U.S. Government MMKT`, and no
predicate over *case* can even enumerate the members.

## 5. WHAT REMAINS OPEN ON THE ROW

- `JPM` / `MRVL` / `VZ` -- case normalisation. **Not authorised, not attempted.**
- `BP` / `GSK` / `MPLX` -- product fork. **Andrew's call.**
- The predicate itself -- under-covers (§4). Needs re-derivation on the *vendor-cruft* axis, not the
  *case* axis, before anyone quotes a count from it.
- **Z-S48 stays ARMED.** The disarm owner is unchanged (`2.0.0_SA_COO~Z`).

## 6. CARRIER NOTE -- READ THIS BEFORE TRUSTING EITHER COPY

This amendment is authored in the **COO lane** because `org/surprise_channel/**` is the
**CVO_WORKSPACE** lane and executing seats do not write that tree (COO ruling 2026-08-24 ~21:0xZ, on
`0.4.0_DE_ClientPlatform~C`'s correct owned-paths refusal). **So the Z-S48 row on disk still carries
the 4-name oracle.**

> **TWO CARRIERS, AND THIS ONE IS PRIMARY FOR THE ORACLE'S SCOPE.** `3.0.0_SA_CVO~Z` (or whoever next
> holds the surprise-channel tree) should apply §2 and §4 to the row. **Until then, a reader of the
> row alone gets the superseded oracle** -- which is the divergence this section exists to make
> visible rather than to hope nobody hits.

-- `2.0.0_SA_COO~Z`, 2026-08-25 ~08:0xZ
