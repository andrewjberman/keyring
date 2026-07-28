# A-2 SERVING-ORIGIN RULING + THE SILENT SENTINEL — `1.0.0_SA_CTO`, 2026-07-28 ~2005–2035Z

**archetype:** MIXED (DIAGNOSE + COORDINATE)
**Session:** fresh CTO context (predecessor PID 28724 died ~2000Z). Handoff `20260728_1957Z` + amendment `1958Z`.
**Peers:** `2.0.0_SA_COO` (primary counterpart), `3.0.0_SA_CVO`, `0.2.0_DT`, `0.7.0_AE_CloudOps~C`, `0.4.0_DS`.
**Trigger:** Andrew-direct `DEPRECATE LEGACY` (171003Z, recorded by DS @`bf986d81a`) was unfolded into sequencing.

---

## 1. THE SOVEREIGN RULING AND ITS FOLD

> **"we dont care what legacy does, we want to move full force into the REVAMP canonical structure and deprecate legacy"** — Andrew-direct, 2026-07-28T171003Z, at DS's terminal

**RULED: this is a DISINVESTMENT order, not a DEMOLITION order.** Two clauses doing different work — *"we dont
care what legacy does"* = stop spending on legacy; *"move full force into REVAMP"* = redirect the spend.
Neither says *remove the legacy emit today*, and the destructive reading strands the serve: **legacy is
currently the only producer ever wired to it.** Grounding is the standing law — **a known-wrong frozen number
is strictly safer than an unheld pipeline.**

**Binding consequences:**
- Legacy keeps running, unfixed and undiagnosed. (This is what answered DS's offered SmartX new-vs-legacy dig: no.)
- **Both `explicitDeny` holds STAY.** Removing them is not deprecation — it is un-protecting the serve. Any lane proposing it is a STOP.
- Deprecation teardown is the **LAST** step of the cutover, not the first.
- ⚠ The Denies are **PRINCIPAL-scoped**: >=6 other principals can still write those keys. *"Nobody writes that prefix"* is a convention, not a control.

**ALSO RULED — the publisher carries its OWN `ScheduleExpression`; `cycle-complete.json` is an ACCELERATOR
only.** Event-only triggering would be (a) the CLAUDE.md-named defect whose measured instance is *this
product* (`mdpf-daily-refresh-trigger`, `ScheduleExpression: None`, froze the client-facing product for six
days with fresh inputs unused), and (b) **born dead** — `cycle-complete.json` has never been written once in
the product's history, so the publisher would never fire while presenting as healthy. **This de-couples the
publisher from Stage 6: it is NOT sequenced behind cottonwood or behind AE's grant.**

---

## 2. A-2 RULED: THE SEPARATE EGRESS PRINCIPAL (option 1)

**The decision rests on Andrew's own generalization constraint, not on cost and not on my prior:**
> `{product}` is REAL — `advi` follows identically. **Anything that cannot absorb `advi` without a rewrite is wrong.** (1834Z/1906Z)

**Option C** (serve MDPF directly from `opal-data-assets`) is **9 EXACT-PATH behaviors + a bucket policy
enumerating 9 exact keys.** Adding `advi`, a scope, or an artifact-type means hand-writing more
infrastructure each time. **That is the hand-enumeration defect at the infrastructure layer — the fifth
altitude of the same class found in one day** (hand-listed key set 4→5→8→23 · hand-modelled type list ·
data-derived roster · restated roster copies · Option C).

**Option 1 generalizes:** an egress principal writing `platinum/{product}/{scope}/{artifact-type}.json`
makes `advi` **data entries and zero infrastructure** — the property DS already demonstrated on the accrual
side.

**AND IT RESOLVES THE FENCE ARGUMENT WITHOUT OVERTURNING IT.** COO+CVO correctly established that
`DenyAnyS3MutationOutsideMonolith` (`NotResource: [opal-data-assets, opal-data-assets/*]`, 12 roles) fences
the publisher INTO the monolith by construction, and CVO's reframe is adopted verbatim: **"this is not a
broken permission, it is the fence working exactly as designed."**
>> **BUT THE FENCE GOVERNS *WRITES* AND CLOUDFRONT GOVERNS *READS* — ORTHOGONAL PLANES. The fence tells us a
>> FENCED role cannot write to `portal-v2`. It says nothing about where the portal should READ from. A
>> write-side constraint gets a write-side answer.** <<
**A NEW, NON-FENCED egress principal widens NOTHING** — all 12 members keep their one-way property untouched.
CVO's warning (*"framing it as a permissions gap would invite widening a deliberate one-way fence on 12 roles
to unblock one trigger"*) is correct and names the shape this would otherwise have taken; **it argues against
adding an Allow or removing a role from the fence, neither of which is option 1.** 11 of 12 members are
ingest roles; the publisher is egress. **That remains a misclassification, not a carve-out.**

### 2a. ⚠ LANDMINE — OPTION C IS STAGED MACHINERY, A THIRD STATE (CTO item)
```
cloudfront-distribution.tf
 :115-126  OAC "opal-data-assets-mdpf-oac" -- "MDPF_REVAMP.S5, Option C"; bucket policy grants
           THIS distribution GetObject on the 9 exact keys
 :248-253  origin domain_name "opal-data-assets.s3.us-east-1.amazonaws.com"  origin_id "S3-opal-data-assets"
 :654-666  "7b. MDPF_REVAMP.S5 Option-C -- 9 exact-path direct behaviors -> opal-data-assets"
APPLIED (dist EVTSA9VEHNZVH): 7 origins, S3-opal-data-assets ABSENT; behaviors targeting it = 0
```
**Not dead, not live — STAGED.** Declared, reviewed, never applied; behaviors currently generate nothing.
**A latent origin for the bucket we are consolidating INTO, sitting unapplied in a tree FROZEN to targeted
applies.** Someone will find it and enable it as *"the fix that's already written."* **Must be explicitly
RETIRED or explicitly marked SUPERSEDED-BY-`{product}`-GENERALIZATION in the PRD, with the reason. Not left
silent.**

---

## 3. THE GOLD-DDB VALUE-STALL: ROOT-CAUSED, AND THE CONTROL SAYS PASS

### 3a. THE LINEAGES ARE SEPARATE BY DESIGN (COO measured, dispatch `:355`/`:415`/`:607`)
```
LEGACY  Stage 3 / WS-A  gold/mdpf_aggregate_aua.py      -> platinum/mdpf/*      -> daily-emitter -> GOLD DDB
REVAMP  Stage 6         dim_mdpf_aggregate_aua_...py    -> gold/mdpf_revamp/*   -> (no publisher)
```
**The gold DDB is fed ENTIRELY by the legacy lineage.** `:607` states the split outright. **Therefore no
revamp-side fix can ever reach it** — not DS's 3-leg fix, not AE~C's grant, not the `:524`/`:525` cottonwood
emitters. **AE~C's grant is structurally incapable of affecting the DDB stall** (its work remains correct and
worth landing on its own terms).

### 3b. THE MECHANISM — a purpose-built ERROR-level control that certifies the failure
Independently re-derived: `data/mdpf/scripts/gold/mdpf_aggregate_aua.py`, 71,863 B / 1,385 lines,
`cottonwood` **0** tokens, `blackdiamond` **0**.
```python
:492  def expected_partners_for(date):                       # ROSTER COPY #1
:497      base = {"49financial"}
:498      if date >= INFLECTION_PARTNER_ONBOARD_DATE: base.add("inflection")   # "2026-05-18"
:736  # MDPF_ASSETS.019 SENTINEL 2 -- expected partners present   <- built after a 5/19 partial-emission miss
:744  missing_partners = sorted(expected - present_firms)
:750  s2_status = "ERROR"                                     # if any expected partner missing
:757  s2_detail = "all expected partners present: [...]"      <- WHAT IT EMITS TODAY
:1132 expected_partners = {"49financial","inflection"}        # ROSTER COPY #2, different function
:1199 "feeders_missing": sorted(expected_partners - present)  # -> [] in the served artifact
```
**Five independent self-certifications PASS on the 16:46:39Z artifact**, one of which I re-derived to the cent:
```
status "current" · lag_vs_as_of_days 0 · rolled_forward_partners {} · meta.feeders_missing []
reconciliation identity_1 PASS residual 0.0
  model 1,553,315,028.29 + sma 23,416,527.61 + non_model 267,853,609.57 = 1,844,585,165.47 == partner_aua_subtotal
  partner_aua_subtotal - cohort_2b 61,179,431.77             = 1,783,405,733.70 == opal_aggregate_aua
```
>> **THE CONTROL IS TRUTHFUL AND SILENT: its expectation set and the data share the same enrollment omission.
>> ENROLLED-THEN-FAILED throws `ERROR`; NEVER-ENROLLED certifies healthy. Its sensitivity is ANTI-CORRELATED
>> with the severity of the failure.** << Doctrine filed as `CONTROLS_OVER_CARE.md` §III-e.

**⚠ LABEL THE BASIS — two quantities, not a gap.** `opal_aggregate_aua` 1,783,405,733.70 vs the SERVE
1,951,676,164.42, delta ~$168.3mm. Per the standing 0824/0833 law these are a **2-firm number and a 3-firm
number**. **The defect is not the value — it is that a 2-firm number carries a firm-wide name and asserts
completeness.**

**THE FIX IS CHEAP:** single-source the roster to the authoritative scope list, have `:492` and `:1132` both
read it, enroll cottonwood with an onboard date exactly as inflection was on 2026-05-18. **The enrollment
mechanism exists and works — it was simply never walked.**

**OPEN AT ANDREW (routed by COO, sovereign not wiring):** *should the Model Portfolios headline AUA include
Cottonwood?* The phased-enrollment mechanism means absence is either a DEFECT or a PENDING ENROLLMENT and the
code cannot distinguish them. **Either way the LABEL is wrong; only the ROSTER fix is contingent.**

**NOT ESTABLISHED (honest residuals):** feeder discovery on the read path unexamined; 0 tokens is strong, not
exhaustive (a cottonwood feeder under a neutral key would not appear); the 4 `etf_ownership_timeseries/`
objects and the bare 448,246 B product-level file remain UNTRACED — **the emitter re-point licenses clearing
nothing.**

---

## 4. THE PLATINUM NAMESPACE — inverted twice, ending cheaper than it started

I read "start-forward, no backfill" as *start clean*. **`platinum/` = 446 objects**, `{scope}` level holding
four different KINDS of thing (real scopes · an artifact-type · ticker-keyed ETF data · 07-12 fixtures · a
bare product-level file). I flagged the 434-object date-keyed `aggregate_aua/` series as non-conformant
residue occupying the target namespace.

**COO inverted it from the emitter's own run log:** `opal-assets-daily-emitter`, `cron(15 17 * * ? *)`, ran
17:15:19Z, reads that series, writes the gold DDB. **It is not residue — it is an ACCRUAL TIER inside the
SERVING bucket, on a schedule, feeding a live table.** And DS's P1 accrual already landed 11 objects at the
canonical home. **The finding is: THE EMITTER READS THE WRONG TIER; the `{scope}`-level occupancy is a
symptom.**

**Disposition: re-point, never delete** — the prefix then drains by disuse rather than by a served-output move
needing never-widen sign-off. **Scope it as BOTH the layering fix AND a detectability upgrade** — the platinum
source has cottonwood **ABSENT and self-certifying complete** (undetectable); the canonical tier has it
**PRESENT but 3–5 trading days stale** (detectable). **It converts an unfalsifiable defect into a falsifiable
one. It does NOT fix the stall, and must not be scoped as if it does** (COO's warning, adopted).

---

## 5. CORRECTIONS AGAINST ME

1. **I ruled option 2 "dead, killed three ways." The Terraform refutes me** — Option C's OAC, origin, scoped
   bucket policy and 9 behaviors already existed. **Wrong in the confident direction**, and COO+CVO were
   pointed at something real I did not know existed.
2. **I parked the critical-path gate.** I parked AE item ③ (the egress principal) as *"design-heavy"* 13
   minutes after ruling the publisher critical path, while holding a handoff that named ③ as its gate.
   **Parking by CATEGORY instead of by POSITION IN THE CHAIN.**
3. **I nearly filed two instrument defects against a tool that was right.** *"comp-routes 25 vs live 24 =
   drift"* — comp-routes counts the default behavior, CloudFront's `Quantity` excludes it: 24+1=25, exact
   agreement. And a queued hypothesis that comp-routes hid the 9 behaviors in an unexpanded `dynamic` block —
   it reported 0, live is 0, consistent. **Both errors were the same error: comparing two numbers without
   establishing what each was OF** — the rule I had spent the hour applying to someone else's numbers.
4. **My cottonwood causal chain was FALSIFIED** by COO's cheaper discriminator (one grep, available all
   along, no grant required). `build_global_artifact` has **three** legs at HEAD, was deployed 14:08Z, and the
   ~15:00Z run performed a 3-firm build — yet the 16:46Z artifact still has zero cottonwood. **Wrong branch
   entirely.** I retracted the acceptance criterion I had drafted for AE~C **before it reached them**, and
   told them explicitly that a persisting stall is not their work failing.
5. **My own doctrine submission was incomplete and would have certified the violating file as compliant.**
   *"Roster declared, types derived"* — endorsed by COO, held one commit short of landing, corrected only by
   reading the body after the location was already agreed. **The roster IS declared. Twice.**

---

## 6. Compiler Tools

| tool | result |
|---|---|
| `comp-routes behaviors` | 25 DESIRED behaviors, 0 targeting `opal-data-assets`. **Accurate on both counts** — I wrongly suspected it of hiding `dynamic`-block behaviors. Its own COVERAGE header correctly discloses DESIRED-plane-only, which is why I grounded on the live primitive per Rule 22a. |
| `comp-grep` | located `build_global_artifact` across 3 files / 24,103 scanned — **denominator printed**. Produced the 3-leg signature that falsified my chain. |
| `comp-freshness` | **GAP: returned only help text** on a bare invocation; did not answer the vintage question. Fell through to stage-2 raw verification. Worth a look — it is the designated freshness instrument. |
| live `s3api head-object` / `s3 ls` / `cloudfront get-distribution-config` | stage-2 verification per the standing two-stage rule. **`head-object` returns explicit GMT; `s3 ls` returns LOCAL** — both appear in this record and the distinction is load-bearing (memory entry 11). |
| Gate-1 rail | 4 `# rail-checked:` overrides, each with a stated reason (bucket-prefix grammar · in-file partner roster · CF origin declaration-existence · applied-plane CF truth). None answerable by a comp-tool. |

---

## 7. OPEN AT WINDOW END

**MINE:** Option C staged-machinery disposition (retire or mark superseded) · §17.2's 9-row consumer table
reconciled against DT's derived 23-key/6-namespace union @`ef18a5fac` (**put the DERIVATION + residual in the
PRD, never the number — it has been wrong four times**) · the `|| return 1` sweep · `account-units` consumer
trace · A2 remainder (ETF objects + bare product-level file, untraced).
**AE~C:** INFRA.TOOLS findings landed, then the Stage 6 grant under an explicit NEVER#6 commitment.
**AE-base successor:** the legacy-lineage stall — **visibly UNOWNED, BLOCKED ON CAPACITY.** COO declined to
false-assign it (correct: *"it has an owner" is the kind of thing that stops being re-examined*); spawn
requested at MSTR 183123Z.
**DS:** read-preference removal, held on AE ① + a demonstrably fresh cottonwood artifact. **Production before
consumption, not reversible.**
**DE:** AGG weighting, designed against C1–C4.
**AT ANDREW:** the cottonwood-enrollment product question (routed by COO). Nothing else blocking.

**Serve state: `5f758b47` / 254,419 B / 2026-07-28T13:41:05Z GMT — unchanged across this window.**
