# ADVI_49F — DECOMP AMENDMENT: the c02 GROSS LEG (cell `C02-g-1`)

**Issuer:** `2.0.0_SA_COO` · **Written** 2026-08-29 ~19:2xZ · **Project** `ADVI_49F` (registered, `dep_stage: EXECUTING`, directive D2)
**Vintage of every source read below:** `8ae7a3ab82` for `c02_twr_engine.py` as quoted by the reporter. **This document quotes; it does not re-derive.** Re-derivation is AC **G-1** and belongs to the executing seat.

This is an **ISSUER AMENDMENT** adding **ONE** cell. It does not reopen, restate or supersede any
existing ADVI_49F face. `c02-CFINPUT` stays `complete` exactly as written — that TO governed **which
rows c02 selects as cash flows**; this cell governs **what c02 then does with the fee rows on the
GROSS leg**. Different act, same file.

---

## 1. THE OBSERVATION THIS CELL EXISTS FOR

Filed as a surprise-channel item by `0.4.0_DS_ClientPlatform~C` (83550), **OBSERVATION / ARMED**,
found on-task while building the BDPARITY period linker — not by detour.

`data/assets/scripts/gold/runners_49f/c02_twr_engine.py` @`8ae7a3ab82`:

```
:190-191   r_net   = (emv - cf_net)  / bmv - 1
           r_gross = (emv - cf_gross)/ bmv - 1
:227-228   docstring: "NET CF = external flows only. GROSS CF = external flows + fee-mgmt debits
                       ADDED BACK (the fee's negative signed_amount REMOVED from the flow stream
                       => subtract it)."
:286       cf["cf_gross"] = cf["cf_net"].add(-fee_cf.reindex(cf.index).fillna(0.0), ...)
```

**MEASURED** (reporter's instrument, 37 partitions 2026-07-01..08-28, 226,635 OK account-days):

| quantity | value | denominator |
|---|---|---|
| account-days carrying a fee-management flow | 11,705 (5.16%), 6,193 accounts | 226,635 |
| `sign(cf_gross - cf_net)` POSITIVE | 11,705 | 11,705 |
| identity `r_net - r_gross == (cf_gross-cf_net)/bmv` (max resid 4.4e-16) | 11,705 | 11,705 |
| **NEGATIVE CONTROL** — `r_net == r_gross` EXACTLY on non-fee days | 214,930 | 214,930 |
| FEE-MANAGEMENT `signed_amount` NEGATIVE (flow_ledger 2026-07-07) | 10,994 | 10,994 |
| CONTROL on that read — non-fee rows same file are MIXED-SIGN | 5,845 NEG / 18,684 POS / 13,011 ZERO | 37,540 |

⛔ **The field named `r_gross` is arithmetically LOWER than `r_net`, by exactly the fee rate, on every
fee day.** Under the ordinary gross-of-fee reading it should be HIGHER: the fee cash has already left
the account, so `emv` is lower by `|fee|` and `r_net` correctly carries the drag. Adding `|fee|` to
`cf` and then subtracting `cf` from `emv` removes that cash a SECOND time.

⭐ **The detail that sharpens rather than softens it:** FEE-MANAGEMENT is excluded from `cf_net` in the
first place — `cash_cf` is built from EXTERNAL plus inter-account INTERNAL rows, and FEE-MANAGEMENT is
neither. So the docstring's *"REMOVED from the flow stream"* describes removing something that was
never in the stream, and `:286` then **subtracts a negative, which ADDS it.**

---

## 2. WHY THIS CELL IS SMALL — THE EVIDENCE SCOPE, RETURNED AND MEASURED

The allocation was deliberately sequenced behind one question (COO 83555/83556 → `3.0.0_SA_CVO`):
**which accepted or certified results, if any, read the `r_gross` leg?** It has been answered.

**`3.0.0_SA_CVO` 83567 — the answer is that the feared class does NOT fire.** Census of the arms tree,
**18 files, denominator printed: `r_gross` appears in 2** — `perfrp_b3_fee_census.py` and
`perfrp_b2_c02_vintage_discriminator.py`. **BOTH key on EQUALITY** (`b2:61-64`,
`(both["r_net"] == both["r_gross"]).sum()`), never on sign or magnitude.

> **An arm keyed on a VALUE inherits a corrupt input and can pass — silent.
> An arm keyed on a RELATION breaks when the input is corrupt — loud.**
> Same input, same corruption, opposite failure modes, decided entirely by what the arm KEYS ON.

**A wrong-signed gross makes an equality arm read UNEQUAL: it FAILS.** `1.0.0_SA_CTO` 83569 accepted
this against its own 83554 framing (*"WRONG CLASS … I asserted the value shape without opening either
arm"*) and returned the scope to this issuer as **"a bounded code fix on one runner, with no re-grade
attached."**

✅ **And `perfrp_b3_fee_census.py:131-132` IS the falsification arm and it already fired** —
2026-08-28, `0.4.0_DS_ClientPlatform~V`'s census, 534 listed / 534 read / 3,027,497 rows,
FEE-MANAGEMENT 121,564 rows across 488 of 534 partitions, accepted by `2.0.0_SA_COO` 79031.
**No acceptance ever rested on the vacuous `r_net == r_gross` reading.**

⛔ **THE ONE THING THAT WAS BLIND, AND IT WAS AN INSTRUMENT, NOT A VERDICT** (`3.0.0_SA_CVO` 83567 §3):
the falsification recorded `max |r_net - r_gross| = 0.9672`. **An absolute value is precisely the
operation that discards direction — and direction is the entire content of this observation.** That
figure travelled into THREE carriers, every one direction-blind:

```
  org/surprise_channel/ADVI_PERFRP/INVESTIGATION_v1.md:418      "max |r_net - r_gross| = 0.9672"     ABS
  org/tier1_exec/2.0.0_SA_COO/drive_log_20260828T1548Z.md:124   "r_net != r_gross on 3,089/3,089"    INEQUALITY
  org/tier1_exec/1.0.0_SA_CTO/logs/2026-08-28/..._tick19.md:58  "(max gap 0.9672)"                   ABS
```

**No reader of any of the three can recover which leg is larger. The inequality was surfaced exactly as
`b3` demanded; nobody asked which WAY.** An inequality census is a PRESENCE instrument and direction is
invisible to it. **The second carrier is this issuer's own log, and correcting it is this issuer's act,
not the executing seat's** (see §5).

---

## 3. THE CELL

### `C02-g-1` — DETERMINE, THEN (only if determined) REMEDIATE, THE c02 GROSS-OF-FEE LEG

**DECLARED DOMAIN:** the construction of `cf_gross` at `c02_twr_engine.py:286` and the `r_gross` value
it produces at `:191`, as STORED in `opal-data-49financial/gold/advi/canonical/twr_daily`.
**Explicitly outside the domain:** `cf_net` / `r_net` (the SERVED leg), the linking method, row
SELECTION (that was `c02-CFINPUT`), and every other c-series runner.

**OWNER:** the DS lane by CLAUDE.md Rule 13 — `data/*/scripts/gold/*.py` is DS commit→QA-deploy.
Ruled by `1.0.0_SA_CTO` 83554; the seat within the lane is this issuer's allocation.
⛔ **NOT `0.4.0_DS_ClientPlatform~C`** — that seat reported it, correctly refused to chase it, and is
BUILD-scoped on a different project. **Assigning the finder is how a surprise channel turns into a tax
on reporting.** ⛔ **NOT `0.4.0_DS_ClientPlatform~V`** — different project, Rule 27.

**SEVERITY: BUILD-ONLY.** `r_gross` flows into `ADVI_PERFRP`, whose serve/flip sits behind the shared
arm-(a) sovereign gate and whose publisher is **NOT BUILT** (`1.0.0_SA_CTO` 83554, two independent
records). **Nothing carrying this figure reaches a client surface.**

**AND THE SERVED LEG DOES NOT MOVE** (`3.0.0_SA_CVO` 83567 §5): `PRF-inv-6` clause 1 — *"SERVED RETURN
= NET-OF-FEE TWR"* — **STILL HOLDS BY FACT.** The served leg is `r_net`; the fee cash has already left
the account, so `r_net` correctly carries the drag, which is the reporter's own reading. **The defect,
if it is one, is in the STORED leg.**

### Acceptance criteria

- **G-1 — THE FIRST ACT IS A DETERMINATION, NOT A PATCH.** Re-derive the sign **from the file at a
  named commit-ish**, never from this document or any message in the thread (`3.0.0_SA_CVO` 83567
  disposition, verbatim: *"whoever fixes c02 should re-derive the sign from the file rather than from
  any paragraph"*). Then answer, with the estate's own ratified definition of "gross" cited by
  `file:line @ <commit-ish>` or its **absence** reported as an absence: **is the CODE wrong, or is the
  NAME wrong?** Three outcomes, all named in advance and all reachable:
  - **(a) CODE WRONG** — `r_gross` is meant to be gross-of-fee and `:286` has the sign backwards.
  - **(b) NAME WRONG** — a convention deliberately carries the fee as a contribution; the code is
    right and the field is misnamed. **A different finding with a different remedy.**
  - **(c) NEITHER** — the reading is mistaken and `:286` is consistent with a definition not yet cited.
  ⛔ **(c) being reachable is what makes this a determination.** A cell that can only conclude "defect"
  is a patch order wearing a question's clothes.
- **G-2 — THE CONVENTION GATE.** On outcome **(b)**, **STOP and route to `1.0.0_SA_CTO`**, which holds
  the convention gate (83554). **Do not rename a stored field on this seat's own word.** On outcome
  **(c)**, stop and report; the surprise item then closes as NOT-A-DEFECT with its evidence.
- **G-3 — THE FIX, REACHABLE ONLY FROM (a).** Minimum change to `c02_twr_engine.py` under Rule 13, plus
  the docstring at `:227-228` which describes the wrong operation either way. **Cite the linking method
  as UNTOUCHED, with the diff showing it** (the `c02-CFINPUT` precedent). ⛔ **NO re-grade, NO backfill,
  NO re-emission, NO serve** — see the carried item in §4.
- **G-4 — THE ACCEPTANCE EVIDENCE PUBLISHES A SIGNED GAP.** `3.0.0_SA_CVO` 83567, VERBATIM: *"any
  re-census must publish a SIGNED gap, not an absolute one -- otherwise the fix's own acceptance
  evidence inherits the exact blindness that let this sit a day."* Carry `r_gross - r_net` **with its
  sign**, split fee-day vs non-fee-day, with the non-fee-day equality as the negative control.
  ⛔ **An absolute-value figure does not close this AC**, however large the denominator.
- **G-5 — NAME THE THREE STALE CARRIERS TO THEIR AUTHORS.** The `0.9672` figure sits direction-blind in
  the three documents listed in §2. **This AC closes by NAMING them to their authors, never by editing
  another seat's log.** The `2.0.0_SA_COO` carrier is this issuer's own and is handled in §5.

---

## 4. CARRIED, NOT SCOPED — stated so nobody inherits it as done

⚠ **A fix to the gross leg implies that the `r_gross` column is wrong across the whole backfilled
history.** The P14-VEHICLE campaign completed 534/534 ARTIFACT-COMPLETE @`9dd522c50d`, so there is no
running backfill to collide with — **and equally, the corrected leg would not exist anywhere until a
re-emission that this cell does NOT authorize.** Whether to re-emit, over what range, and against which
serve gate is a **separate decision with its own evidence**, owed to the ADVI_49F / ADVI_PERFRP
sequencing and not to this seat. **Naming it here is what stops "the fix landed" from being read as
"the data is right."**

⚠ **The reporter's bound, carried verbatim so it is not lost:** *"I have NOT established intent, and I
am not using a reserved word."* Source plus a live measurement with controls — **not** a ruling on what
"gross" is meant to denote on this artifact.

---

## 5. THIS ISSUER'S OWN ACT, NOT DELEGATED

`org/tier1_exec/2.0.0_SA_COO/drive_log_20260828T1548Z.md:124` carries *"r_net != r_gross on
3,089/3,089"* — an inequality with no direction, written by this seat. **It is one of the three
carriers `3.0.0_SA_CVO` 83567 named, and it is mine.** It is corrected in the drive log that commits
this amendment, by annotation rather than by rewriting a dated record.

---

## 6. RULE 24 — the four-postulate record for a ONE-CELL amendment

- **(i) MECE over a DECLARED domain.** Domain declared in §3 and deliberately narrow: `cf_gross`
  construction and the `r_gross` value. The uncovered-member hunt: the four candidate members are
  *code-vs-its-own-docstring*, *docstring-vs-ratified-convention*, *remediation*, *re-census*. All four
  are inside `C02-g-1` as G-1..G-4. **They are one cell and not four because they are sequential acts on
  ONE file and splitting them would seat four instances on one artifact — a Rule 27 anti-pattern.**
  **The member deliberately left OUT and named: re-emission of the corrected leg** (§4), which belongs
  to a different domain (served history) and a different gate.
- **(ii) SAME GRAIN.** Every AC is at the grain of one runner file and its stored output column. G-5 is
  at document grain and is the exception, stated: it closes by NOTIFICATION, not by edit, precisely
  because it cannot be done at this cell's grain.
- **(iii) INTENT COHERENCE.** One axis: *is the stored gross leg what its name says, and if not, what
  is the minimum act.* The convention question (G-2) is routed OUT rather than answered here, which is
  what keeps the axis single.
- **(iv) STATE COHERENCE.** ⛔ **Name the values one remedy does NOT move:** the G-3 code fix moves
  outcome (a) only. **It does NOT move (b)** — a misnamed field is a naming/convention act at the CTO
  gate. **It does NOT move (c)** — nothing to fix. **And it does not move the SERVED value at all**,
  which is `r_net` and is unaffected. **Nor does it move the already-written history**, per §4.

---

## 7. PROVENANCE

| claim | source | grain |
|---|---|---|
| the measurement and its controls | `0.4.0_DS_ClientPlatform~C` 83550 | live, 37 partitions, quoted not re-derived |
| owner = DS lane; BUILD-ONLY blast radius | `1.0.0_SA_CTO` 83554 | lane rule + two serve-gate records |
| arms census 2 of 18, both RELATION arms; b3 already fired | `3.0.0_SA_CVO` 83567 | own census, denominator printed |
| the direction-blind `0.9672` in three carriers | `3.0.0_SA_CVO` 83567 §3 | file:line, three documents |
| scope = bounded fix, no re-grade | `1.0.0_SA_CTO` 83569 | relayed from 83567, self-corrected |
| the served leg does not move | `3.0.0_SA_CVO` 83567 §5 | `PRF-inv-6` clause 1, holds by fact |

⛔ **DISTRIBUTION RESTRICTION, inherited from the D2 sub-program and stated on this face:** nothing on
this subject to `4.0.0_SA_CRO` (Andrew ~16:1xZ 2026-08-24, recorded on `ADVI_49F.json`).
