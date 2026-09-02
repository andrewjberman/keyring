# ANDREW-DIRECT 2026-09-02 ~20:0xZ -- `/open-calls` x5 at the COO terminal: the project tree RULED (calls 1-4), the custodian call becomes an INVESTIGATION (call 5)

**Received by:** `2.0.0_SA_COO`, at the COO terminal, in reply to `/open-calls` (5 cards).
**Recorded durably. NOT broadcast** -- Andrew ruled the XXX.md same-turn broadcast "not a viable
solution" this session; the record is the carrier, and the routing below is the delivery.

---

## 1. THE WORD, VERBATIM AND UNNARROWED

> "All recs approved. In the case of Call 5, it was supposed to be just the Schwab Book but it would
> appear there may be new additions outside of that, which we will need to investigate to pin down
> exactly what (i.e. investigating into any fields that might give it away, e.g. if there are
> custodian fields or codes that would show something like "Fidelity" or "Pershing Square" etc,
> because it appears maybe there is another custodian being phased in there but that would need to
> be confirmed)."

**NEVER A PARAPHRASE. THE PHRASING IS THE RULING.**

---

## 2. CALLS 1-4 -- "All recs approved" -> the (a) on every card

Spec: `SPEC_PROJECT_TREE_DIRECTIVE_MACRO_PROJECT_20260902.md` (@`31463f1286`, s.3a @`ea49c6dec0`).

| call | RULED | effect on the spec |
|---|---|---|
| 1 | **KEEP the macro layer; ratify it as a per-directive enum** (Rule 24 record + census) | s.5 stands; the tree is THREE levels `D{n}/{MACRO}/{PROJECT}/`; s.8 prerequisite 1 is live |
| 2 | **`project.json` MOVES into the project folder; `org/projects/` becomes a GENERATED INDEX** | s.2 choice B stands; the index generator (s.8 prereq 3) is the first build |
| 3 | **`deliverables/{serial}/` sub-folders** -- the path carries the owner; the gate stays a path gate | s.6 option (ii); no new resolver in the commit hook |
| 4 | **`task-orders` (hyphen), tree only, prospective** -- the 34+ existing `task_orders/` dirs untouched; the gate reads BOTH roots in the dual-register period | s.7 spelling decision closed; the gate glob change is ONE line, CTO's |

⛔ **SCOPE, so nobody reads "All recs approved" wider than four cards:** it approves the FOUR
recommendations as rendered on the cards. It does NOT approve the spec wholesale as law, does NOT
lift the L1-L5 water-test bound, and does NOT make any of it retroactive -- his 19:3xZ word
("prospective work ... ETFS_GUARDRAIL NFRA_CLDGRPH NFRA_COMPEFFICACY") stands untouched.

---

## 3. CALL 5 -- NOT a scope ruling. A DIRECTED INVESTIGATION.

**What he ruled, decomposed without widening:**

1. **INTENT, stated:** *"it was supposed to be just the Schwab Book."* That is the design intent of the
   49F SmartX feed. **It is NOT a ruling that the feed IS Schwab-only today** -- he immediately qualifies
   it.
2. **OBSERVATION, his:** *"it would appear there may be new additions outside of that."* Consistent with
   the measurement on the card (13 nine-digit keys, FMT CO/FMTC grammar, 18 rows, $12,293,768.23).
3. **THE ACT HE ASKS FOR:** *"investigate to pin down exactly what"* -- specifically **"any fields that
   might give it away, e.g. if there are custodian fields or codes"** that would show a custodian name.
4. **THE HYPOTHESIS TO CONFIRM OR KILL:** *"maybe there is another custodian being phased in there but
   that would need to be confirmed."*

>> **SO THE REMEDY FORK ON THE CARD IS NOT CHOSEN. It is DEFERRED behind a measurement he named:
   read the feed's own custodian fields/codes and report what they carry. "Fidelity" and "Pershing
   Square" are his EXAMPLES of what a custodian code might say, not claims that either is present.** <<

⚠ **WHAT IS ALREADY MEASURED, so the investigation does not re-run it** (`0.4.0_DS_ClientPlatform~N`,
2026-08-30 18:12Z, msg "the FMTC label TRACED before it reaches management"): the literal strings in
the data are **`FMT CO` -> 11 rows** and **`FMTC` -> 4 rows** (15 of the 18 nine-digit rows). **The
abbreviation IS in the data; the "Fidelity" expansion is NOT** -- that seat measured it and said so.
⛔ **THEREFORE THIS RECORD DOES NOT SAY "FIDELITY."** Andrew said it as an example of a custodian
name; the data says `FMT CO`. Expanding one into the other is exactly the inference DS~N refused to
make, and the investigation's first job is to find the field that WOULD settle it.

**Routed as an investigation ask -- NOT a TO.** No TO can be cut: `D3_MODELOVERLAY` declares no
`fabric` (L3 refuses), RC7 is open, and Andrew's L1-L5 bound holds. The natural owner is the DS lane
holding the D3 context (`~N` traced the label; `~E` completed TO-D3.1b @`e4a4f3cbee`). Delivered by
message; the ask names its acceptance (s.4) so the answer arrives in a form the remedy fork can be
ruled on.

---

## 4. WHAT DS~N ALREADY MEASURED (2026-08-30 18:12Z) -- so the ask is the RESIDUAL, not a re-run

Read in full before routing. `0.4.0_DS_ClientPlatform~N`, one vintage, denominators printed:

```
  CARRIER      column `account_name` in
               s3://opal-data-assets/smartx/platform/silver/fact_allocation_account_map/date=2026-08-28/data.parquet
  ⛔ INVISIBLE  to the 49F chain -- a06 reads only 3 of the map's 9 columns (allocation_id,
               account_id, account_number). The registration text sits one column outside every
               read this fabric makes of that table.
  "FMTC"       4 rows   "FMT CO"  11 rows   either: 15 of 18 nine-digit, 0 of 7,341 eight-digit
  "FIDELITY"   0 rows in the entire map (7,359)
  registration "FMTC CUSTODIAN - ROTH IRA & FBO <person>" / "FMT CO CUST IRA & FBO <person>"
  the other 3  bare personal registrations; non-IRA accounts carry no trustee line;
               655417051 pairs with 655417044 on the same person -- CONSISTENT-WITH, not proven
  $12,293,768.23  reproduced to the cent from the object, 13 distinct keys, 18 rows
```

>> **SO ONE FIELD HAS BEEN READ, AT ONE DATE, FOR ONE NAME.** Andrew asked for "any fields", for
   whether a custodian is being "phased in", and named more than one custodian. Three residuals: <<

## 5. THE RESIDUAL -- the investigation ask, with its acceptance

1. **ALL NINE COLUMNS, not one.** DS~N read `account_name`. The map has 9 columns and the chain reads 3.
   Enumerate the other 5 unread columns by name and, for each, whether it carries anything that could
   identify a custodian (a code, an id, a routing prefix, a firm string). `<column>: <n distinct> over
   <N rows>`; for the 18 nine-digit rows, the value of every such column verbatim; for a control of
   eight-digit rows, the same columns.
2. **ACROSS DATES -- the "phased in" test.** One vintage cannot show a phase-in. Read the nine-digit
   population (count of keys, count of rows, sum of `aum_value`) at every `date=` partition the map
   carries. **If the population is GROWING, that is the phase-in; if it is flat, it is a standing
   inclusion.** Print the date range as the denominator.
3. **OTHER CUSTODIAN NAMES, not just "FIDELITY".** Andrew named "Pershing Square" as a second
   example. Census the registration text and every column from (1) for custodian-shaped tokens
   generally -- `CUST`, `CUSTODIAN`, `TTEE`, `TRUSTEE`, `FBO`, and any firm-shaped string -- and
   report every DISTINCT custodian designation found, with its row count. Zero hits for a name is a
   result with the census as its denominator, never silence.
4. **Explicitly NOT asked:** a remedy, and NOT the expansion of `FMT CO` into a firm name. DS~N was
   right to refuse that inference and this ask does not reopen it.

**The acceptance in Andrew's own terms:** after (1)-(3), can the estate say from ITS OWN DATA whether
a custodian other than Schwab is present, WHICH designation(s), and whether its footprint is growing
-- each as a measured sentence, or as a stated non-finding with its denominator.
