# ADVI_BDPARITY — MIDSTREAM STATE BRIEF

**Author:** `4.0.0_SA_CRO~A` · **UTC:** 2026-09-01
**Mode:** `/brief-create --midstream ADVI_BDPARITY`
**Authority:** Andrew-direct 2026-09-01 (the D2 member-set scoping instruction).
**Consumer:** `/endpoint --forward docs/briefs/advi-bdparity-state-brief-20260901.md` (step 2).

---

## PART 0 — HOW THE BLIND CONSTRAINT WAS HONOURED, AND WHERE IT BENT

**NOT READ:** `org/**/task_orders/ADVI_BDPARITY.*`; the project JSON's `phase` / `blocking`.
**READ:** the registry row's `name`/`prds`; D2 PRD §4a (this project's governing spec); the served
and gold planes; commit subjects; prior CRO/DS parity briefs in `docs/briefs/`.

⛔ **WHERE IT BENT, AND IT IS THE WORST LEAK OF THE SET.** This project has **no PRD of its own** —
its spec is D2 PRD §4a — so there is less purpose-level material to author from than any sibling, and
correspondingly more of what I know comes from **delivery commits**, which are branch. I have kept
Parts I–III to what §4a and Andrew's own acceptance language support, and pushed every measured
figure into Part VI. **A reader should treat this brief's outcome section as thinner-sourced than
INSURE's or STITCH's.**

---

## PART I — THE OUTCOME TERRITORY

### O1 — We can answer "is our number right?" before a client asks
For any 49F account, period and figure we serve, someone can produce our number beside Black
Diamond's own calculated number and a classified difference — without a bespoke investigation.
**Disputable by:** a figure we serve that nobody can check against BD without building something new.

### O2 — Every difference is explained or is a named open item
A gap between our figure and BD's is either accounted for by a stated mechanism, or it is on a list
of things we know we do not understand. There is no third category.
**Disputable by:** a difference someone shrugs at.
⭐ *Andrew's PERFRP acceptance language makes this a precondition of shipping, not a follow-up audit:
"data parity with Black Diamond" is one of his three named axes.*

### O3 — The parity claim covers the population, not a sample
When we say our performance figures agree with Black Diamond, the statement carries a denominator
over the real book — not a handful of accounts someone happened to check.
**Disputable by:** a parity claim quoted without its denominator; a sample presented as a proof.
⛔ *This outcome exists because the estate has already made this error at the sovereign level — see
Part VI note 1.*

### O4 — Black Diamond is the oracle and never the source
Our figures come from our own facts. BD is what we check against. Nothing we serve is BD's number
passed through.
**Disputable by:** any served figure traceable to a BD calculation rather than to our own.

### O5 — Period claims are only made where we can actually compute them
We expose a period only if we can compute it honestly. Where we cannot — today, since-inception —
we do not offer it rather than offering a figure we cannot stand behind.
**Disputable by:** a period in the served set whose figure we could not defend if challenged.

---

## PART II — WHERE THE BOUNDARY SITS

**Owns:** the comparison harness; the classification vocabulary and its thresholds; the census and
its denominators; the mechanism explanations for named differences.

**Relies on, does not own:**

| project | relies on | does NOT own |
|---|---|---|
| `ADVI_PERFRP` | the emitted figures it grades; arms on the first emission | PERFRP's projection or serving |
| `ADVI_49F` | the canonical facts (`twr_daily` et al.) under the comparison | the TWR engine or its defects |
| `ADVI_STITCH` | the seam, for anything crossing 2024 | the classification |
| BD vendor surface | read access for the oracle side | the vendor relationship or egress authorisation |

**Deliberately NOT this project:** fixing the calculation differences it finds (that is the owning
producer's act); the performance method; serving anything; vendor egress authorisation.

---

## PART III — THE QUALITATIVE BAR

No number in Parts I–III is a target. Thresholds that already exist (the EXACT/TIGHT/LARGE bands) are
**ruled instruments, not outcomes**, and are cited in Part VI rather than restated as goals here.

⛔ **The failure mode is a PARITY CLAIM THAT OUTRUNS ITS EVIDENCE.** A five-account probe reported as
"parity proven" is the specific harm; O3 is written against it.

---

## PART IV — THE SUBSTRATE: IS THIS IN A CANONICAL PATTERN?

### FINDING A — this project has no PRD, and that is a real structural gap
Its governing spec is a *section* of the parent directive PRD (`D2_ADVI_49F_E2E_PRD.md` §4a). Every
other substantive D2 member has its own stage-2 PRD. **A project whose spec is a section of someone
else's document cannot be independently versioned, ratified or superseded**, and its acceptance
language lives where a reader of the project will not look. Surfaced, not ruled.

### FINDING B — the harness is real, exercised, and producing findings of unusual quality
This is not a stalled project. Recent delivered work includes a one-sided day-count residual finding
(1,226 of 1,226 — we never link *more* days than BD, ever), a flow-placement instrument committed so
its provenance is answerable at line numbers, and an explicit correction that 1,516 is a
pre-exclusion population while 1,506 is post-exclusion — **two populations, not two answers**,
recorded at the number so the next reader does not re-derive it.

### FINDING C — the method is sound where it has been exercised
The sharpest evidence is a single account that came back **EXACT at 7e-6 bp** on QTD/YTD/1Y once its
mechanism was found (five missing days on our side), with `days_linked == bd_days_held` at
42/165/252. **The instrument works.** What has not been established is coverage.

### FINDING D — the estate has been carrying a false parity premise at the sovereign level
Andrew's 2026-08-31 record states that parity *"as I understand has already been proven."* Measured
against this project's own record, it has not. `1.0.0_SA_CTO` surfaced this correction rather than
inheriting it. **This is the single most consequential fact in this brief** and is restated in Part VI
with its numbers.

---

## PART V — WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

1. **The population census must run and print its denominator** before any parity claim is made.
2. **The known calculation differences must be resolved or named** — a LARGE cell with no mechanism
   is an open item, not a tolerance.
3. **PERFRP must emit** for the harness to grade the figures that matter; parity accompanies the
   first emission by ruling, and is not a tail-end audit.
4. **A vendor read is required for at least one open dimension** (`dim 436`), which is egress and
   therefore reserved to Andrew's explicit per-use word.
5. **The since-inception recommendation needs a disposition** — measured and recommended, not yet
   ruled.
6. **This project needs its own PRD** if it is to be scored independently (Finding A).

---

## PART VI — STATUS ⛔ NOT OUTCOME-BEARING

*Grounded on the project record and commit stream read 2026-09-01 19:45Z. Figures RELAYED from the
owning lanes' committed deliverables unless marked measured-by-me.*

**1. ⛔ THE PREMISE CORRECTION, restated because it is load-bearing.** Parity is **not proven**.
State of record: P1-PROBE complete at **5 of 5 accounts** — a probe, not a proof. Of 16 initially
LARGE cells the standing is **11 LARGE / 2 TIGHT / 3 EXACT**, and the 11 remaining LARGE cells are
**calculation differences** whose mechanism is unresolved. This does not weaken Andrew's priority
ruling; it sharpens why the priority is right.

**2. The census DID run and it is finding things.** P2-CENSUS is past its 08-19 face —
`SUPERSEDED-WITH-REHOME, 5 of 6`, with P2-3 recorded as having been **weakened from a failure
condition into a permission** and failing on 1,516 cells. P3-EXACT is in **cycle 2**.

**3. A 3-account spot validation on 2026-09-01 came back 8 of 9 EXACT, 1 LARGE**, range_match 9 of 9,
day-count residual zero on every cell. The one LARGE (`20277481` 1Y) reads 252/252 on both sides with
matching ranges — **a genuine calculation difference, not a window or missing-day artifact.**

**4. An open recommendation at Andrew: remove Since Inception from the served period set**, capping
at 1Y, on the measured ground that we cannot compute a true SI today and BD cannot be trusted to
supply one. **Measured, recommended, not ruled.**

**5. T-track state (relayed, 2026-09-01):** T1-ORACLE 4 of 4; T2-DIMS 4 of 5. **T2-3 stays FAIL**,
and its blocker has been narrowed from "build + egress" to **egress alone** — the consumer is wired
and exercised; what remains is one vendor-side template amendment, which is Andrew's word.

**6. Instrument caution now on the record.** A load-bearing claim that dim 436 exists in the BD
catalog is **single-carrier and could not be re-derived** — the staged catalog carries per-querytype
counts and measure names but no dim ids, and a positive control confirmed the search arm was dead.
**A dead arm and a true absence read identically**; the re-derivation is owed and is read-scoped.

---

## PART VII — WHAT THIS BRIEF DOES NOT CLAIM

1. **It does not claim parity is close.** It claims the instrument is sound and the coverage is not
   established. Those are different.
2. **Its figures are largely RELAYED**, not measured by this seat this session — the exception is the
   served-plane and gold-plane listings in the sibling briefs. Treat every count here as carrying its
   originating lane's vintage.
3. **It does not adjudicate the SI recommendation.**
4. **It did not read the task orders.**
5. **It is thinner-sourced than its siblings** because the project has no PRD of its own (Part 0,
   Finding A).
6. ⛔ **A task order serving something real that Parts I–III fail to name is evidence THIS BRIEF is
   incomplete.**

---

## REFS

```
BRIEF PATH        docs/briefs/advi-bdparity-state-brief-20260901.md
PROJECT           ADVI_BDPARITY  (directive D2, status active, registered 2026-08-27)
EXISTING PRD      NONE OF ITS OWN -- spec is docs/architecture/D2_ADVI_49F_E2E_PRD.md s.4a
SIBLING PROJECTS  ADVI_PERFRP (subject) · ADVI_49F (facts) · ADVI_STITCH (the seam)
PRIOR ART         docs/briefs/advi-bdparity-spot3-and-si-recommendation-20260901.md
MEASURED AT       2026-09-01 19:45Z (commit stream + planes); embedded figures carry lane vintages
```
