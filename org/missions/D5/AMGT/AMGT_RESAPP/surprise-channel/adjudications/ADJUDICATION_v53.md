# AMGT_RESAPP ROUND 43 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-26 ~02:3xZ
**Input:** `2.0.0_SA_COO~Z`'s `round43/DRAIN_END_PACKET.md` @`c6183d5ab8` (read to EOF, 5,527 B; blob
`87c5dff61d` confirmed in the pin's own tree), msgs 25960 + 25971.
**L7 state, RE-MEASURED not adopted:** `rr-1`, `rr-2`, `rr-3` all `complete` on their **LAST** `<status>`
tag; 8 acceptance criteria (2+4+2); **exactly 1 carrying `judgment="true"`** (rr-2 AC4). Matches the packet.

---

## 1. L8 -- THE CHANNEL COMPILE

⚠ **FIRST, A CORRECTION OF MY OWN INSTRUMENT.** My first pass read **333 non-terminal** because the terminal
set I used omitted `DISMISSED_WITH_REASON`. **307 of the project's 624 items carry that disposition**, so the
error inflated the open count more than twelvefold. Corrected: **624 items, 598 terminal, 26 NON-TERMINAL**,
66 files read, `unknown: []`, via `_latest_dispositions` (`.tools/surprise-row-gate.py:433`). Stated because
a wrong terminal set produces a number that looks measured and is off by an order of magnitude.

### ⛔ THE PACKET NAMES THREE ROWS. THE ROUND-43 WINDOW HOLDS SIX.

| row | surfaced | class / standing | in packet? | disposition here |
|---|---|---|---|---|
| `Z-S279` | 09-25T17:05Z | **BLOCKING / ARMED** | **NO** | **GRADUATED** -- the guard landed and is exercised (below) |
| `Z-S281` | 09-25T18:50Z | OBSERVATION / INERT | **NO** | **GRADUATED** -- `rr-2` fixed exactly this, verified three ways |
| `Z-S282` | 09-25T20:20Z | OBSERVATION / INERT | yes | **GRADUATED** -- the disarm-owner read; but its fold is a NO-OP (below) |
| `Z-S283` | 09-25T22:30Z | OBSERVATION / INERT | yes | **GRADUATED** -- cite Andrew-direct R-21 WITH `@b390c36444`; `RULINGS.jsonl` R-0021 is an unrelated coordination ruling |
| `Z-S284` | 09-25T23:40Z | OBSERVATION / INERT | **NO** | **GRADUATED** -- and the question it RESERVED to this seat is answered below |
| `Z-S285` | 09-25T23:58Z | OBSERVATION / INERT | yes | **GRADUATED** -- superseded by fact; it was already false when written |

⭐ **`Z-S284` IS THE OMISSION THAT MATTERS, AND IT IS NOT A CUTOFF ARTIFACT** -- the packet names `Z-S283`
(22:30Z) and `Z-S285` (23:58Z) and skips only the row BETWEEN them. A vintage cutoff drops a tail; this
dropped a middle. And `Z-S284` is the one row of the six that **holds another lane's ledger leg**.

### ⭐ FINDING 1: `adjudicates` ON A NON-TERMINAL ROW IS A NO-OP THAT READS AS A DISPOSITION

The packet's s.4 records `Z-S282` as *"adjudicates Z-S279"*, and `Z-S282` does carry
`adjudicates: ["AMGT_RESAPP-Z-S279"]`. **It closed nothing.** From the resolver's own bytes
(`.tools/surprise-row-gate.py`, the fold loop over investigation documents):

```
        for target in (r.get("adjudicates") or []):
            ...
            latest[target] = r.get("disposition")
```

**The fold writes the FOLDING row's disposition onto its target.** `Z-S282`'s own disposition is
`UNDER_INVESTIGATION`, so folding `Z-S279` wrote `UNDER_INVESTIGATION` onto a **BLOCKING, ARMED** row -- it
RE-ASSERTED it open. ⛔ **The tool is not defective**: the sibling branch says so in a comment (*"a second
carrier that is open keeps the item open"*). **The defect is the belief that filing `adjudicates` disposes
of a row.** Only a TERMINAL row's fold closes a target, and at L9 that is the CVO's `GRADUATED` row -- which
is what this file is. A BLOCKING row read as adjudicated for six hours while mechanically open.

### ⭐ FINDING 2: AIA GROUP HAS A CANONICAL IDENTITY, AND `Z-S285` WAS ALREADY FALSE WHEN WRITTEN

`lib/research/identity/registrations.json` carries, at **`registered_at 2026-09-25T23:48Z`**:

```
folder "AIA Group" | bloomberg "1299 HK" | resolution MEASURED | security_key 1299_HK_Equity
identity: LEI ZP5ILWVSYE4LJGMMVD57, CIK 1522877, FIGI BBG0016XR1Q8, ISIN HK0000069689, SEDOL B4TX8S1
```

| row | written | the claim | true when written? |
|---|---|---|---|
| `Z-S284` | **23:40Z** | AIA has no minted identity | **YES** -- 8 minutes before the mint |
| `Z-S285` | **23:58Z** | *"AIA Group joined the live library mid-round with no identity"* | **NO** -- 10 minutes after it |

⭐ **NEITHER SEAT WAS CARELESS. The fact changed underneath both inside a twenty-minute window**, because
two projects read ONE universe through separate acts with no shared clock: `AMGT_CORPUS` round 5 minted the
identity on Andrew's *"go ahead with AIA"* while `AMGT_RESAPP` round 43 was measuring its absence.

**THIS ANSWERS THE QUESTION `Z-S284` RESERVED TO THIS SEAT AND RELEASES THE HELD LEG.** That row states its
shape (a) -- *"mint a canonical identity for 'AIA Group' ... reserved on the picks question to
`3.0.0_SA_CVO~Z`"* -- and records that the lane *"held ledger leg L2 on gate (a)"*. **Shape (a) is already
DONE**, by another project, on Andrew's own word. The leg is released; no picks decision is owed from here.
`rr-3`'s `CAPTURE_FAILED 1` was correct at its run time and is now stale, and amendment 1's pin to the 94 at
the cut remains the right call for the criterion.

## 2. L9 -- `rr-2` AC4, GRADED ON THE RENDER

**AC4 asks** that a SERVED case's VALUE appear on both surfaces and that deleting the line was not the fix.
Graded against `rr-2.AC4.output.txt` **beside both PNGs** -- ⛔ **a JSON pass without the render read by a
person is care, not a control.**

**PASS, on both arms:**

- **SERVED (RKT).** Page footer and export text carry the same sentence: `Base case: SERVED -- 7386.63633
  (consensus EPS (FY1) x trailing-median P/E)`. **APPLIED, not merely desired**: `render_pack.py:729`
  `_model_cases_markdown` passes the NESTED per-case object (`cases.get(str(name).lower())`) and its own
  docstring names `Z-S281` as the bug it fixes.
- **ABSENT (BA), the arm that matters.** `Base case: ABSENT -- forward EPS (FY1 BEST_EPS) is
  -0.8280000000000001, not positive` renders **as a present line with its own reason**. Upside and downside
  carry the methodology reason. **Deleting the line was not the fix**, confirmed on the render.
- ⭐ **CROSS-INSTRUMENT CORROBORATION: `7386.63633 / 4923.00 = 1.5004`**, against `AMGT_CORPUS`'s
  independently measured RKT Base ratio of **1.500**. Two projects, two instruments, four significant
  figures. **The VALUE is right.**

### ⚠ TWO PRESENTATION DEFECTS VISIBLE ONLY ON THE RENDER, ON BOTH ARMS

1. ⛔ **THE CASE VALUE CARRIES NO CURRENCY, ON A PAGE THAT LABELS ITS PRICE.** The same render reads
   `Price GBp 4923.00` (RKT) and `Price USD 196.80` (BA) in the header tile, then prints the base case as a
   bare `7386.63633`. **The page demonstrably knows the unit and drops it exactly where the number is a
   valuation a person would act on.** On a **GBp** name this re-presents the precise ambiguity behind
   `Z-S265` (the 100x class) and `Z-S279` (seven implausible bases) -- both currency-scale defects. **This is
   not cosmetic; it is the same failure mode, one layer up, in the presentation instead of the arithmetic.**
2. **Raw float repr reaches the reader**: `7386.63633` is five decimal places on a price, and
   `-0.8280000000000001` is sixteen significant figures of IEEE-754 noise shown to an analyst.

**Neither is AC4's subject, so AC4 PASSES.** Both are recorded for the round-43 analysis, and the first is
the one worth a cell.

## 3. BOUNDS, ADOPTED FROM THE PACKET AND CHECKED

- **The page change is on portal DEV only.** A user on the live site still sees the old case line. The
  promote is carried item 4 and nothing here changes that.
- **The RKT run renders RKT's payloads under BA's route keys** because `ui-contract-check.mjs` navigates to
  BA only. The render's own header reads `RKT LN` / `Reckitt Benckiser Group PLC`, so the provenance is as
  the packet states -- checked, not assumed.
- **The 95th name is outside the grade**, correctly, and Finding 2 changes its status rather than the grade.
- Deployed `982nlz5T...mYvo=`; population pinned at 94, `read_at 2026-09-25T18:42:56Z`.

## 4. L10 PRECONDITION

1. **Every task order terminal** -- 3 of 3 on their last `<status>` tag. **MET**
2. **Every round-43 row dispositioned** -- **6 of 6**, including the three the packet did not name. **MET**
3. **Every judgment criterion graded** -- 1 of 1, on the render and both arms. **MET**

---

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S421",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-26T02:35:00Z",
    "one_line": "L9 round 43: rr-2 AC4 PASSES on BOTH arms graded on the RENDER, with the served value corroborated across two projects (7386.63633/4923.00 = 1.5004 against AMGT_CORPUS's 1.500). THREE FINDINGS: the packet named 3 of the round's 6 rows and the omitted one holds another lane's ledger leg; 'adjudicates' on a NON-TERMINAL row is a no-op that re-asserts its target open, which left a BLOCKING ARMED row reading as adjudicated for six hours; and AIA Group HAS had a canonical identity since 23:48Z, so Z-S285 was already false when written at 23:58Z and the question Z-S284 reserved to this seat is answered by an act another project had already taken.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INPUT GRAIN: packet @c6183d5ab8 read to EOF at 5,527 B, blob 87c5dff61d confirmed present in the pin's own tree, so the graded bytes are the cited bytes.",
        "L7 RE-MEASURED, not adopted: rr-1, rr-2, rr-3 all read 'complete' on their LAST <status> tag; 8 acceptance criteria across the three; exactly 1 carries judgment=\"true\" (rr-2 AC4). Matches the packet.",
        "MY OWN INSTRUMENT CORRECTED IN THE RECORD: a first pass read 333 non-terminal because the terminal set omitted DISMISSED_WITH_REASON, which 307 of the project's 624 items carry -- an error that inflated the open count more than twelvefold and would have read as measured. Corrected: 624 items, 598 terminal, 26 NON-TERMINAL, 66 files read, unknown [].",
        "THE PACKET NAMES 3 ROWS; THE ROUND-43 WINDOW HOLDS 6. Unnamed: Z-S279 (BLOCKING, ARMED, 17:05Z), Z-S281 (the CTO's, 18:50Z) and Z-S284 (the AE's, 23:40Z). Z-S284 is not a cutoff artifact: the packet names Z-S283 at 22:30Z and Z-S285 at 23:58Z and skips only the row BETWEEN them. A vintage cutoff drops a tail, not a middle.",
        "FINDING 1, VERIFIED FROM THE RESOLVER'S OWN BYTES: the fold loop over investigation documents executes 'latest[target] = r.get(\"disposition\")', so an adjudicates entry writes the FOLDING row's disposition onto its target. Z-S282's own disposition is UNDER_INVESTIGATION, so folding Z-S279 wrote UNDER_INVESTIGATION onto a BLOCKING ARMED row and RE-ASSERTED it open. The tool is NOT defective -- its sibling branch carries the comment 'a second carrier that is open keeps the item open'. The defect is the belief that filing adjudicates disposes of a row: only a TERMINAL row's fold closes a target, and at L9 that is the CVO's GRADUATED row. A BLOCKING row read as adjudicated for roughly six hours while mechanically open.",
        "FINDING 2: AIA GROUP HAS A CANONICAL IDENTITY. lib/research/identity/registrations.json carries folder 'AIA Group', bloomberg '1299 HK', security_key 1299_HK_Equity, resolution MEASURED, registered_at 2026-09-25T23:48Z, with LEI ZP5ILWVSYE4LJGMMVD57, CIK 1522877, FIGI BBG0016XR1Q8, ISIN HK0000069689, SEDOL B4TX8S1. Z-S284 (23:40Z) claimed no identity and was TRUE, 8 minutes before the mint. Z-S285 (23:58Z) claimed no identity and was ALREADY FALSE, 10 minutes after it. NEITHER SEAT WAS CARELESS: two projects read ONE universe through separate acts with no shared clock, and AMGT_CORPUS round 5 minted the identity on Andrew's 'go ahead with AIA' while AMGT_RESAPP round 43 was measuring its absence.",
        "FINDING 2's CONSEQUENCE: Z-S284 states shape (a) -- 'mint a canonical identity for AIA Group ... reserved on the picks question to 3.0.0_SA_CVO~Z' -- and records that the lane 'held ledger leg L2 on gate (a)'. Shape (a) is ALREADY DONE by another project on Andrew's own word, so the leg is RELEASED and no picks decision is owed from this seat. rr-3's CAPTURE_FAILED 1 was correct at its run time and is now stale; amendment 1's pin to the 94 at the cut remains right for the criterion.",
        "AC4 GRADED ON THE RENDER, BOTH ARMS, not on the JSON. SERVED (RKT): page footer and export text carry the identical sentence 'Base case: SERVED -- 7386.63633 (consensus EPS (FY1) x trailing-median P/E)'. APPLIED not merely desired -- render_pack.py:729 _model_cases_markdown passes the NESTED per-case object via cases.get(str(name).lower()) and its docstring names Z-S281 as the bug it fixes. ABSENT (BA): 'Base case: ABSENT -- forward EPS (FY1 BEST_EPS) is -0.8280000000000001, not positive' renders as a PRESENT line with its own reason, and upside/downside carry the methodology reason -- so deleting the line was not the fix, confirmed on the render rather than inferred.",
        "CROSS-INSTRUMENT CORROBORATION OF THE SERVED VALUE: 7386.63633 / 4923.00 = 1.5004, against AMGT_CORPUS's independently measured RKT Base ratio of 1.500 from cases_report_89_20260925T190913Z.log. Two projects, two instruments, agreement to four significant figures. The VALUE is right, which is what makes the presentation defects below worth separating from it.",
        "TWO PRESENTATION DEFECTS VISIBLE ONLY ON THE RENDER, ON BOTH ARMS, NEITHER AC4's SUBJECT. (1) THE CASE VALUE CARRIES NO CURRENCY ON A PAGE THAT LABELS ITS PRICE: the same render reads 'Price GBp 4923.00' for RKT and 'Price USD 196.80' for BA in the header tile, then prints the base case as a bare 7386.63633. The page demonstrably knows the unit and drops it exactly where the number is a valuation a person acts on, and on a GBp name that re-presents the precise ambiguity behind Z-S265 (the 100x class) and Z-S279 (seven implausible bases), both currency-scale defects -- the same failure mode one layer up, in the presentation rather than the arithmetic. (2) Raw float repr reaches the reader: 7386.63633 is five decimal places on a price and -0.8280000000000001 is sixteen significant figures of IEEE-754 noise.",
        "BOUNDS CHECKED, NOT ADOPTED: the RKT run renders RKT's payloads under BA's route keys because ui-contract-check.mjs navigates to BA only, and the render's own header reads 'RKT LN' / 'Reckitt Benckiser Group PLC', so the fixture provenance is as the packet states. The page change is on portal DEV only, so a user on the live site still sees the old case line. Deployed 982nlz5T...mYvo=, population pinned at 94, read_at 2026-09-25T18:42:56Z."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-S279",
      "AMGT_RESAPP-Z-S281",
      "AMGT_RESAPP-Z-S282",
      "AMGT_RESAPP-Z-S283",
      "AMGT_RESAPP-Z-S284",
      "AMGT_RESAPP-Z-S285"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The packet @c6183d5ab8 asserts three orders terminal and VALID, FWD-30 met on the served plane at 94 of 94 with the cases axis at 282 of 282 against a population pinned at the cut, the Model Cases rendering on page and export, and three rows for disposition.",
    "world_is": "All of that is true as re-measured, and three things the packet does not state are now measured: the round's channel holds SIX rows and not three, with the omitted middle one holding another lane's ledger leg; the adjudicates field on a non-terminal row re-asserts its target OPEN rather than closing it, so a BLOCKING ARMED row was never disposed; and AIA Group has carried a canonical identity since 23:48Z, which makes Z-S285 false as written and answers the question Z-S284 reserved to this seat.",
    "notes": "FOR THE ROUND-43 ANALYSIS, four items. (1) THE CURRENCY-LESS CASE VALUE IS THE ONE THAT DESERVES A CELL. The arithmetic defect class this project has chased for three rounds -- Z-S265, Z-S279 -- is currency scale, and the fix now serves a correct number with its unit stripped, on a page that labels the price tile two inches above it. A reader cannot tell 7386.63633 GBp from GBP, and that is the exact discrimination the 100x bug turned on. (2) THE adjudicates NO-OP IS A FABRIC ITEM, NOT A PROJECT ONE: any seat filing adjudicates on an open row believes it has disposed of the target and has not. The cheap remedy is for the gate to REFUSE adjudicates on a row whose own disposition is non-terminal, since that combination can never mean what its author intends. (3) AIA needs no picks decision from this seat and its Model block is already derived under the CTO's extended pair, so enrichment item 1 reduces to confirming RESAPP reads the same registration the corpus wrote. (4) Z-S284's own instrument lesson is worth keeping verbatim: a LIVE population is not a fixed denominator, and the tell was that the sweep printed a denominator (95) disagreeing with the one the order recorded (94) -- visible only because the sweep prints its population and read time on its first line."
  }
]
```
