# `0.4.0_DS_ClientPlatform~Z` -- 2026-08-29, 0330-0600Z

INC3-A measurement, increment-3 leg B/B', TO-N1-DS served scoring, and the repair of three
proof-of-spec instances. Written because `D1_CATVIEWS.TO-A3-DS_PROOF_OF_SPEC.json` cites this
directory as its `session_log` and the citation did not resolve until this file existed.

> **CITATION CONVENTION, and it is a limitation not a style choice.** Every bare `NNNNN`
> below is a broker Msg-ID **as delivered to `0.4.0_DS_ClientPlatform~Z`**. Measured
> 2026-08-29: one send writes ONE FILE PER RECIPIENT with a DIFFERENT id and a
> byte-identical body (one send -> 4 copies, ids 15849-15852, body md5 x1; a second ->
> 6 copies, ids 15934-15939, md5 x1). **So these ids resolve in THIS seat's inbox and
> nowhere else** -- another seat's copy carries a different number, and that number
> exists there pointing at an unrelated message, so the mismatch is SILENT. Each
> citation names its SENDER's serial, which is the half that survives delivery; to
> locate the exact message use the sender + the quoted content, or the stable
> `YYYYMMDDTHHMMSSZ_<sender>` filename prefix, which is identical in every copy.

---

## 1. `D1_CATVIEWS.TO-A3-DS` -- INC3-A. CLOSED 4/4 @`b68b9d7168`

**The assigned question:** measure the Tax SMA account population and its declared discriminator.

NOTE: **THE DISCRIMINATOR IS NOT WHERE THREE SEATS PLACED IT.** `1.0.0_SA_CTO~Z` (15849),
`2.0.0_SA_COO~Z` (15853) and the TO amendment all located the membership rule in
`build_fact_taxsma_report.py:47`'s *"Scope: Chiles-only for now"* docstring.
```
  THAT IS A SCOPE NOTE DATED 2026-07-17 AND IT IS STALE.
  The SAME docstring's next sentence is the operative one:
      "this module processes EVERY ACCOUNT PRESENT IN THE BRONZE PARTITION"
  -> the silver producer applies NO membership filter at all.
  THE RULE, in code:  taxsma_registry.py:144-149 @7d97a8bed2  list_active() -> status=="active"
                      lambda_function.py:252-273              discover_accounts()
                      s3://opal-data-assets/blackdiamond/49f/_ops/taxsma_roster.json
```
**A docstring is not a discriminator; `status` is, and it is a field a consumer can reject on.**

**The population:** 5 enrolled -- Chiles, Bump, Macy, Nixon, Tracey. Andrew ruled 5 independently;
the roster carries 5. **Two instruments, one number, so the population is `held` AND `measured`.**

CRITICAL: **AND THE INSTRUMENT THE ISSUERS NAMED UNDER-REPORTS.** 15877/15863 directed that progress be read
as *"which of the 5 resolve through `dim_account_xref`"*:
```
  xref-resolved  1 of 5        roster-active  3 of 5        DISAGREEMENT
```
Nixon and Tracey are ACTIVE with resolved BD ids and are absent from the xref by every id form --
they resolved **tier-3 (account-api)**, and tier-3 results land in the ROSTER. The xref is the
tier-1 surface. **A seat following that instruction publishes "1 of 5" with a printed denominator
and marks two fully-resolved accounts unresolved.**

### Two errors of mine on this face, both caught by controls
1. **A false zero from a grain-mismatched key.** I zero-padded to 10 digits; BD carries Chiles as
   `27265115` unpadded. The Chiles POSITIVE CONTROL failing is what caught it. Re-keyed -- and the
   zero PERSISTED, which is how the padding fault and the wrong-frame fault below were told apart.
2. CRITICAL: **A real absence in ONE FRAME read as unavailability in the estate.** I filed the omission size
   BLOCKED because `fact_bd_allocation` contains none of the five. That measurement was correct and
   **the conclusion was too wide** -- that feed is 0824-scoped and the accounts are 0833.
   `1.0.0_SA_CTO~Z` (15898) found them in `schwab/08335338/silver/dim_balance`, and I reproduced
   **6,445,461.07 to the cent** independently. **The TO's own title said "at Schwab 0824" and I
   inherited that frame instead of testing it.** `dim_account_xref` carries an `in_0833_universe`
   column flagging Chiles True -- the discriminator was in an artifact already open on my desk.

**Contribution back:** the two measures decompose exactly on 5 of 5 --
`net_mv_positions = mkt_value_long + mkt_value_short` and
`net_mv_plus_cash = net_mv_positions + cash_balance_settled_only`. The books are genuinely
long/short (1.43-1.49x long, 0.43-0.49x short), so **`mkt_value_long` overstates by 2,926,110.90
(45%)** while reading as the obvious "market value" column.

---

## 2. Increment-3 leg B/B' -- `source_basis` @`b6e97e9685`

Andrew: *"this is an SMA, so our logic on models + smas simply has to change, the plug doesnt work
with this in mind."*

```
  client_aum = non_model - sma_carve_out_aum      (was: - sma_aum)
  total_aua  = total + sma_additive_aum           (was: total)
```
CRITICAL: **THE OLD GUARD COULD NOT FAIL.** Client is DEFINED as the complement, so `SMA + Client ==
non_model` held for every value of SMA, correct or not. **The premise was invisible because every
identity was built from it.**

**Acceptance is `CLIENT DOES NOT MOVE`, never "SMA went up"** -- the broken version also increases
SMA, by taking the money out of Client. Exercised two-sided: Client held at 300.0 while SMA grew by
exactly the additive amount; the **refused** shape on the same fixture reports 240.0.

**Provable no-op today** -- no `by_model` entry resolves to an additive member, so the additive sum
is 0.00 and both changed expressions are identical to their old form. The arithmetic goes live
before the dollars do.

WARN: **The unverified three (`muni`/`idvz`/`pfde`) are DECLARED, not defaulted, and the direction is
argued:** a wrong `carve_out` understates CLIENT (the number Andrew watches, and the one that caught
this bug); a wrong `additive` inflates the FIRM TOTAL by double-counting, which nothing watches.
Recorded as a safe-direction CHOICE so nobody later cites it as a measurement.

CRITICAL: **Rule 24 census found a real collision:** `additive` already means *"a column added to a vendor
schema"* here (1176 word-boundary hits, including inside `data/mdpf/scripts/gold`). `carve_out` is
clean (1). Named and accepted rather than unilaterally renamed -- four seats were already using the
vocabulary. `source_basis` must never be shortened to a bare `basis`.

---

## 3. Leg C -- BLOCKED, and the block is the finding

```
  mdpf-gold-lambda-role, ALL 17 resource entries enumerated:
     schwab/08242234/silver/*   GRANTED        schwab/08335338  ABSENT
  simulate-principal-policy, BOTH principals x BOTH masters:
     gold-lambda-role    0833 implicitDeny  |  0824 allowed
     daily-runner-role   0833 implicitDeny  |  0824 allowed   (AE found the 2nd principal;
                                                               my first denominator was 1 of 2)
```
CRITICAL: **AND THE ACCEPTANCE DESIGNED TO CATCH PROBLEMS IS BLIND TO THIS ONE.** `qa_local` runs under
**operator** credentials; the lambda runs as its role. **qa_local would have gone GREEN, the reserved
delete would have fired on that green, and the rebuild would have AccessDenied -- 16 keys deleted and
not rebuildable.** Banked as memory `a-control-in-a-different-principal-cannot-see-permissions`.

OK: It is `implicitDeny`, **not** `explicitDeny` -- nothing denies it, the grant is simply absent. So
the remedy is purely additive. **That is the SHAPE of the remedy, not an argument for it:** the grant
IS the sovereign scope decision (`2.0.0_SA_COO~Z` 16146), and `1.0.0_SA_CTO~Z` withdrew their own IAM
remedy on the same ground.

---

## 4. `D1_CATVIEWS.TO-N1-DS` -- four served rows scored @`75f61912e1`

4 PASS / 0 FAIL. AC3's limb D was **scoreable, not `N/A-BY-DATE`** -- the reland rebuilt the same
dated key, so `as_of` stayed 2026-08-27 and the date-scoped literals were scored and both hit.

CRITICAL: **A FOURTH SCOPE MOVED AND NO CRITERION NAMES IT.** `global`: SMA 0.00 -> 22,794,766.25, Client
290,426,813.47 -> 267,632,047.22, sentence PRESENT -> ABSENT. AC4 names cottonwood and inflection only;
AC5 names 49financial and "where it is TRUE". **The movement is CORRECT** (it mirrors 49financial to
the cent, which basis B predicts) -- the finding is COVERAGE. The before-image had ALREADY annotated
it *"FALSE, AND NOT NAMED BY ANY CRITERION ON THIS TO"* hours earlier and nothing acted on it,
**because a note inside an evidence blob is not a work item.**

WARN: My scorer's first version printed that global was "exactly as the before-image recorded it" --
**FALSE; global had moved and my own output asserted it had not.** Caught by reading the emitted
value against the before-image rather than against my summary of it.

---

## 5. Proof-of-spec repairs @`f57304010d`, `2a80cf9b11`

`3.0.0_SA_CVO~Z` (16253) reported TO-N1-DS INVALID on 5 additive fields. **I checked the sibling and
the CLOSED face was worse: TO-A3-DS carried 15**, including five *missing required* fields.

CRITICAL: **A TOOL CRASH WAS HIDING BEHIND MY FIRST FIX.** My `controls` was a STRING;
`proof-of-spec-check.py:61` does `controls.mutant.get(...)` -> AttributeError -> **rc=2, which the tool
labels NOT-A-VERDICT.** An instance that crashes the checker has not been judged at all. **rc=2 and
rc=1 are different states.**

**Final:** TO-N1-DS VALID rc=0. TO-A3-DS 15 -> 1, and the 1 is unfixable from the instance --
`INC3-A` cannot match `CELL_ID_RE` (`PREFIX-<lowercase>-<digits>` or `PREFIX-m-<name>`), so the
decomp id space parses as ZERO. **`cell_refs` live on the TO FACE and are schema-FORBIDDEN on an
acceptance row**, so remedy "step 3 -> the instance" was withdrawn (16294): doing it would re-break
the artifact it was meant to fix. **The instance was never in the blast radius; the remedy is 2 files.**

WARN: Corrected my own record at `2a80cf9b11`: I had written the decomp has *"NO `cells` array at all"* --
true of the KEY, but it reinforces the absence reading, and the five cells ARE declared. **The cell is
not missing; its ID FORM is not admitted.** Fixed because the wording propagated the wrong diagnosis,
not because it was factually wrong about anything I did.

---

## 6. State at close

```
  leg C            ANDREW's 0833 scope word. Both routes need it.
  TO-N1-DS AC7     the ~13:30Z SCHEDULED fire (+ TO-M1-DS TM1-AC1, TO-P1-AE).
  INC3 rename      1.0.0_SA_CTO~Z picks the id form; MY SHARE IS NOTHING.
  lambda           STALE by exactly b6e97e9685, a value no-op. Rebuild correctly held.
  commits          11, all ON ORIGIN (integrator swept @223539e8e1).
  overrides        5 STRUCTURAL-TWOPHASE taken, 5 discharged in-session.
```
CRITICAL: **NO STAND-DOWN TAKEN.** Every open item is gated on someone else's act and each gate is named.
Per `1.0.0_SA_CTO~Z` 16314: an idle fabric with every item correctly blocked is a success state, and
pre-writing leg C against a guessed answer would make the YES cheap and the NO expensive -- pressure
on a decision that is Andrew's to make freely.
