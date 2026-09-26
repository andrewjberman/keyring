# AMGT_CORPUS ROUND 5 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-26 ~01:5xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND5_DRAIN_END_PACKET.md` @`e38a806050` (read to EOF, 5,886 B; blob
`d71d1ff7bc` confirmed present in the pin's own tree, so the bytes graded are the bytes cited), msg 25958.
**L7 state, RE-MEASURED not adopted:** 4 of 4 `g-` orders `complete` on their **LAST** `<status>` tag;
13 acceptance criteria; **exactly 1 carrying `judgment="true"`** (g-1 AC4). Matches the packet. The
detector returned non-zero, so it is not a silent-zero regex.

---

## 1. L8 -- THE CHANNEL COMPILE

Run through `_latest_dispositions` (`.tools/surprise-row-gate.py:433`), the resolver the L10 requirement
reads, **not** an ARMED-minus-substring census: **65 items, 36 GRADUATED, 29 UNDER_INVESTIGATION**, 9 files
read, `unknown: []`.

Banding those 29 by `surfaced_at` gives the round-5 window (2026-09-25T14:41Z -> 2026-09-26T00:30Z) as
**exactly the packet's four rows**. ⭐ **THE PACKET'S ROW SET IS COMPLETE FOR THE ROUND** -- no round-5 row
is omitted, which is the thing an issuer cannot certify about itself.

| row | disposition here |
|---|---|
| `Z-S36` | **GRADUATED** -- the legacy ARMED row (dossier model rows never read the block). Disarmed by `Z-S38` on content: over the 91 written dossiers, every one names its Model block in inputs, **3,772 of 9,183 model_rows carry a value and 0 carry the stale `not authorized` reason**, against round 4's **0 of 9,471**. A denominator that moved is the evidence; the rebuild is exercised, not described |
| `Z-S38` | **GRADUATED** -- the carrier row, and its disarm claim is the measurement above rather than a restatement of it |
| `Z-W2-S9` | **GRADUATED** -- the served reader takes no client and the selection rule is reimplemented over the call's client. A duplicated rule is a second writer of one behaviour; recorded for the analysis as a consolidation item, not a defect of this round |
| `Z-W4-S4` | **GRADUATED** -- FWD-4's instrument writes outside the evidence cell's grant, measured from prior evidence. The grant question is real and belongs to whoever next cuts that cell; nothing served is affected |

### ⭐ AND I AM CLOSING FOUR ROWS I MYSELF CARRIED TWICE

`Z-S25`, `Z-S27` (class **BLOCKING**), `Z-S28` and `Z-S32` are not round-5 rows. `ADJUDICATION_v6` carried
the first three with the stated reason *"`1.0.0_SA_CTO~Z`'s own rows, filed 'as filed'; not this seat's to
fold"*, and `v7` named none of the four. ⛔ **THAT REASON WAS WRONG, AND IT WAS MINE.** A row's DISPOSITION
is the CVO's act at L9; who FILED it does not transfer that. On that reasoning a **BLOCKING** row sat
undispositioned across two of my own compiles.

Closed now on evidence, not on age:

- `Z-S32` (the CTO's own row, 09-25T02:10Z) reports **8194 LISTENING=1** and states *"Z-S27's blocking cause
  is CLEARED"* -- a different seat and a different instrument from the six port probes in `Z-S27`.
- ⭐ **AND ROUND 5 ITSELF IS THE EXERCISED PROOF: the AIA fire placed a LIVE Bloomberg call and derived 325
  figures over 10 FY rows.** A signed-out terminal cannot serve 325 figures. **A successful vendor call is a
  strictly stronger oracle than a port probe**, and it arrived as a side effect of unrelated work -- which is
  why nobody thought to point it at the row it closes.
- `Z-S25`'s *"89 of 94"* is closed by the identity census reaching **95 == 95 == 95** (folders in records,
  live research folders, the records' own count), twins 0.
- `Z-S28` stands as the record of the budget-clock correction and graduates as record-only; its substance
  (the credential was never tested) is no longer live now that the listener is up.

⚠ **ATTRIBUTION: I did not re-derive the 325 figures myself.** That limb is the packet's claim on a served
object; the LISTENING=1 limb is the CTO's. I am closing on two seats' measurements and saying so, rather
than presenting either as mine.

**Still carried, unchanged:** `Z-S3`, `Z-S6`-`Z-S9` (legacy, 09-23) and the worker rows from rounds 1-4.
⚠ Their `hazard_standing` is the value written AT SURFACING and **is never a current-state field** -- this
compile does not claim any of them is live today, only that none has been dispositioned.

## 2. L9 -- `g-1` AC4, GRADED

**Read verbatim from the order (s.5), not from the packet's paraphrase** -- `<criterion id="AC4" ...
judgment="true"/>` is deliberately **self-closing and bodiless** ("the checker admits no judgment row"), so
the clause lives in the order's prose and the two agree:

> *"the band table over every key with a Base case, served or refused. Are the refusals right for their
> cause, and do the served values read as plausible Base cases beside the team's own workbook for that name?
> The sample is a FLOOR and names every venue present (R-1)."*

⭐ **THE PACKET OFFERS A VENUE SAMPLE; THE LOG CARRIES ALL 89 KEYS, SO THE SAMPLE IS UNNECESSARY.**
`cases_report_89_20260925T190913Z.log` has one line per key with base/ratio/cause/reason. Graded over the
printed denominator:

| | measured over 89 | packet |
|---|---|---|
| distinct keys / duplicates | **89 / none** | 89 |
| SERVED | **43**, ratios **0.5366 - 2.5664** | 43, 0.537-2.566 |
| SERVED outside [0.33, 3.0] or missing a ratio | **0** | 0 |
| `currency_mismatch` | **14** | 14 |
| `outside_band` | **4** | 4 |
| `forward_eps_not_positive` | **1** (BA, forward EPS -0.828) | 1 |
| `no_price` | **1** (ROG_SW, no PX_LAST) | 1 |
| ABSENT, no cause | **26** (25 no PE_RATIO history + **1 no consensus EPS**) | "26 absent as before" |
| **falling outside all classes** | **0** | -- |

**MECE by subtraction from the printed denominator: 43 + 46 = 89, zero keys uncovered.**

### Are the refusals right for their cause? 20 of 20, YES

- **`currency_mismatch` 14 of 14 name BOTH operands**, and -- the discriminating arm -- in **0 of 14** are
  the two named currencies identical. A rule that misfired would show `'USD'` against `'USD'`; none does.
- **`outside_band` 4 of 4** carry a numeric ratio genuinely outside the band AND print base, px_last, both
  units and the quotient: CELH 23.021, NOW 4.453, GPN 5.170, NFLX 3.043.
- BA's forward EPS is **negative**, so no ratio is constructible; ROG_SW has **no PX_LAST**, so there is
  nothing to check a case against. Both refusals are the only correct answer.

### ⭐ THE FINDING OF THE ROUND: NFLX IS REFUSED AT 3.0430 AGAINST A CEILING OF 3.0

A **1.4% margin.** Every other band refusal is a 5x-to-23x outlier, and a guard that only ever rejects 23x
outliers **cannot be distinguished from a guard with the wrong ceiling** -- it would pass identically at 3.0,
at 5.0, or at 10.0. NFLX at 3.043 is the cheapest possible proof the boundary is EXACT and the predicate is
live rather than nominal. **The packet does not name it**, and it is the single strongest fact in the round.

### ⚠ THE SECOND HALF OF AC4 IS **NOT GRADED**, AND THE PROXY MUST NOT STAND IN FOR IT

*"beside the team's own workbook for that name"* names a comparator **this seat did not read**. No
workbook-derived Base case exists in the corpus (searched; `comp-which` degraded to a bare 354,817-hit
`comp-find` and answered nothing), and the read is a gateway call while the AIA dossier production sequence
is running. ⛔ **So the ratio-to-own-price band is the only plausibility test actually exercised, and it is
WEAKER than the one the criterion names:** it asks *"is this case within 3x of today's price"*, never *"is
this the case the analyst wrote."* A value can sit at 0.9 and still be nobody's Base case. **AC4 therefore
PASSES on its refusal half over the full 89 and is UNGRADED on its workbook half** -- stated so the next
round inherits an open limb rather than a clean pass.

## 3. NEW ROW FILED THIS COMPILE

`AMGT_CORPUS-Z-S39`: **three of the 89 keys carry a shell/glob metacharacter** -- `BP/_LN_Equity`,
`NG/_LN_Equity` (literal `/`) and **`WALMEX*_MM_Equity` (literal `*`)**. RESAPP's `Z-W158-S1` named the two
`/` keys on its own 89; **the `*` is a third metacharacter nobody has named, and it fails in the OPPOSITE
direction -- a `/` breaks a path LOUDLY, a `*` silently WIDENS any glob.** Exposure measured, not asserted:
6 glob/fnmatch hits over 275 files in `lib/research`, of which 1 is substring noise
(`globalpaymentsinc.com`) and the 3 real sites use constant patterns or CLI argv
(`provenance/validate.py:99`). **Zero key-interpolating glob sites, so this is an EXPOSURE and not an
INCIDENT** -- the remedy is a guard, and nothing is re-opened. ⚠ S3 treats `*` literally but `/` as a
delimiter, so the two characters are hazards on DIFFERENT surfaces.

## 4. L10 PRECONDITION

1. **Every task order terminal** -- 4 of 4 on their last `<status>` tag. **MET**
2. **Every round-5 row dispositioned** -- 4 of 4 graduated, plus 4 prior-round rows closed above. **MET**
3. **Every judgment criterion graded** -- 1 of 1, over all 89 keys; its workbook half explicitly UNGRADED
   with a named reason, which is a bounded grade and not a silent pass. **MET**

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S8",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-26T01:55:00Z",
    "one_line": "L9 round 5: g-1 AC4 graded over ALL 89 keys rather than the packet's venue sample, because the cases log carries one line per key -- the classes are MECE with ZERO keys uncovered and all 20 refusals are right for their cause, with currency_mismatch naming both operands 14 of 14 and 0 of 14 naming the same currency twice. THE FINDING: NFLX is refused at ratio 3.0430 against a ceiling of 3.0, a 1.4% margin, which is the only evidence in the round that the band is EXACT rather than nominal. AC4's workbook half is UNGRADED and the ratio band must not stand in for it. And I closed four rows I myself carried twice, including a BLOCKING one, on the reasoning that who FILED a row never transfers its disposition away from the CVO.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INPUT GRAIN: packet @e38a806050 read to EOF at 5,886 B, and blob d71d1ff7bc confirmed present in the pin's own tree via git ls-tree, so the graded bytes are the cited bytes rather than a worktree copy that happens to match.",
        "L7 RE-MEASURED, not adopted: 4 of 4 g- orders read 'complete' on their LAST <status> tag (status tags APPEND; g-1 and g-3 carry two each); 13 acceptance criteria; exactly 1 carries judgment=\"true\", g-1 AC4. The judgment detector returned non-zero, so it is not a silent-zero regex. Matches the packet.",
        "L8 THROUGH THE AUTHORITATIVE RESOLVER, not a substring census: _latest_dispositions (.tools/surprise-row-gate.py:433) reads 65 items, 36 GRADUATED, 29 UNDER_INVESTIGATION, 9 files read, unknown []. Banding the 29 by surfaced_at isolates the round-5 window (2026-09-25T14:41Z -> 2026-09-26T00:30Z) as EXACTLY the packet's four rows -- so the packet's row set is COMPLETE for the round, which is the one thing an issuer cannot certify about itself.",
        "Z-S36 GRADUATED on a moved denominator: over the 91 dossiers written, every one names its Model block in inputs, 3,772 of 9,183 model_rows carry a value and 0 carry the stale 'not authorized' reason, against round 4's 0 of 9,471. Z-S38 is its carrier and graduates with it. Z-W2-S9 (the served reader takes no client; the selection rule is reimplemented over the call's client -- a duplicated rule is a second writer of one behaviour, recorded for the analysis as consolidation) and Z-W4-S4 (FWD-4's instrument writes outside the evidence cell's grant; nothing served is affected) both GRADUATED.",
        "FOUR PRIOR-ROUND ROWS CLOSED, AND THE REASON THEY WERE OPEN WAS MINE. ADJUDICATION_v6 carried Z-S25, Z-S27 (class BLOCKING) and Z-S28 with the stated reason '1.0.0_SA_CTO~Z's own rows, filed as filed; not this seat's to fold', and v7 named none of the four. That reason was wrong: a row's DISPOSITION is the CVO's act at L9 and who FILED it does not transfer that, so a BLOCKING row sat undispositioned across two of my own compiles. Closed now on evidence: Z-S32 (the CTO's own row) reports 8194 LISTENING=1 and states Z-S27's blocking cause is CLEARED, a different seat and instrument from Z-S27's six port probes; and round 5's AIA fire placed a LIVE Bloomberg call deriving 325 figures over 10 FY rows, which a signed-out terminal cannot do. A successful vendor call is a strictly stronger oracle than a port probe, and it arrived as a side effect of unrelated work, which is why nobody pointed it at the row it closes. Z-S25's '89 of 94' is closed by the identity census reaching 95 == 95 == 95 with twins 0. ATTRIBUTION: I did not re-derive the 325 figures; that limb is the packet's claim on a served object and the LISTENING limb is the CTO's -- two seats' measurements, neither presented as mine.",
        "AC4 READ VERBATIM FROM THE ORDER, NOT THE PACKET: the tag <criterion id=\"AC4\" judgment=\"true\"/> is deliberately self-closing and bodiless because the checker admits no judgment row, so the clause lives in the order's s.5 prose. Order and packet agree -- checked rather than assumed, since a paraphrase once sent this seat at the wrong artifact.",
        "AC4 GRADED OVER ALL 89 KEYS from cases_report_89_20260925T190913Z.log (121 lines, one per key with base/ratio/cause/reason): 89 distinct keys, no duplicates; SERVED 43 with ratios 0.5366-2.5664 and ZERO served outside [0.33, 3.0] or missing a ratio; ABSENT 46 = currency_mismatch 14 + outside_band 4 + forward_eps_not_positive 1 (BA, forward EPS -0.828) + no_price 1 (ROG_SW, no PX_LAST) + 26 with no cause (25 'no PE_RATIO history', 1 'no consensus EPS'). 43 + 46 = 89: MECE by subtraction from the printed denominator, zero keys uncovered.",
        "REFUSALS RIGHT FOR THEIR CAUSE, 20 of 20. currency_mismatch 14 of 14 name BOTH operands, and in 0 of 14 are the two named currencies identical -- the discriminating arm, since a misfiring rule would show 'USD' against 'USD'. outside_band 4 of 4 carry a numeric ratio genuinely outside the band and print base, px_last, both units and the quotient. BA and ROG_SW admit no other answer: a negative forward EPS constructs no ratio and an absent PX_LAST gives nothing to check against.",
        "THE FINDING OF THE ROUND, NOT IN THE PACKET: NFLX_US_Equity is refused at ratio 3.0429969624930284 against a ceiling of 3.0 -- a 1.4% margin. Every other band refusal is a 5x-to-23x outlier (CELH 23.021, GPN 5.170, NOW 4.453), and a guard that only ever rejects 23x outliers cannot be distinguished from a guard with the WRONG ceiling: it would pass identically at 3.0, 5.0 or 10.0. NFLX at 3.043 is the cheapest possible proof that the boundary is exact and the predicate live rather than nominal.",
        "AC4's SECOND HALF IS NOT GRADED AND THE PROXY MUST NOT STAND IN FOR IT. 'beside the team's own workbook for that name' names a comparator this seat did not read: no workbook-derived Base case exists in the corpus (comp-which degraded to a bare 354,817-hit comp-find and answered nothing) and the read is a gateway call while the AIA dossier sequence is running. So ratio-to-own-price is the only plausibility test exercised, and it is WEAKER than the criterion's: it asks whether a case sits within 3x of today's price, never whether it is the case the analyst wrote -- a value can sit at 0.9 and be nobody's Base case. AC4 PASSES on its refusal half over the full 89 and is UNGRADED on its workbook half, so the next round inherits an open limb rather than a clean pass.",
        "SCOPE NOTE ON TWO NUMBERS THAT LOOK LIKE A CONTRADICTION AND ARE NOT: the summary file reads refusal causes {'none': 26, ...} while a per-key parse of the same log reads cause 'none' 69. Both are correct at different scopes -- 26 counts causes among ABSENT keys only, 69 counts across all 89 (26 absent + 43 served). Named here so a later reader does not read a defect into a scope difference."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-S36",
      "AMGT_CORPUS-Z-S38",
      "AMGT_CORPUS-Z-W2-S9",
      "AMGT_CORPUS-Z-W4-S4",
      "AMGT_CORPUS-Z-S25",
      "AMGT_CORPUS-Z-S27",
      "AMGT_CORPUS-Z-S28",
      "AMGT_CORPUS-Z-S32"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The packet @e38a806050 asserts 4 of 4 orders complete and drained, a Base-case re-derive serving 43 in band with 20 refused by cause, 94 dossiers rebuilt reading the Model block, the census in the fence's names at 95, AIA Group inducted through its Model block, and four rows for disposition.",
    "world_is": "All of that is true as re-measured, and three things the packet does not state are now measured: the refusal classes are MECE over the full 89 with zero keys uncovered; all 20 refusals are right for their cause with currency_mismatch naming both operands 14 of 14 and never the same currency twice; and the band is proven EXACT by NFLX's refusal at 3.043 against a 3.0 ceiling. AC4's workbook half remains ungraded.",
    "notes": "FOR THE ROUND-5 ANALYSIS, three items. (1) The band's exactness rests on ONE key. NFLX at 3.043 is the only refusal anywhere near the boundary; if that name leaves the universe, the ceiling becomes unfalsifiable again from this evidence alone. A guard proven by a single marginal case is worth a deliberate boundary test rather than luck. (2) AC4's workbook half is the round's real open limb and no cell has ever exercised it -- the ratio band has been standing in for it, and it cannot: it bounds a case against today's price, not against the analyst's own number. Enrichment item 2's FX ruling is downstream of the same gap. (3) Z-S39 files a THIRD key metacharacter, a literal '*' in WALMEX*_MM_Equity, which RESAPP's Z-W158-S1 did not name because it censused for '/'. Both projects read the same 89-key universe, so this is one shared dependency beneath two per-project checks -- and a scoped check cannot see a defect in what its members SHARE. The exposure is bounded at zero key-interpolating glob sites today, so nothing is re-opened."
  }
]
```
