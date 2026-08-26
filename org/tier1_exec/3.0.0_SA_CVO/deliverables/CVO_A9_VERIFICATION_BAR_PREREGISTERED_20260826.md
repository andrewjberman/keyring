# CVO A9 VERIFICATION BAR — PRE-REGISTERED BEFORE THE A-PRIME APPLY

**Author:** `3.0.0_SA_CVO` · **Written:** 2026-08-26 ~17:45Z
**Subject:** `MDPF_COTREMEDIATION` — the CVO read of A9 after `0.6.2_AE_PartnerETL~A`'s A-Prime apply
and `0.4.0_DS_ClientPlatform~T`'s re-fire.

**STATE AT WRITING, so this cannot be back-dated:** `mdpf-gold-lambda` LastModified
**2026-08-26T15:29:34.000+0000**, CodeSha256 **`3/897ecG2Xzal+0Xl+Ygoshsqccd6smAcMwygv8KjZQ=`** —
i.e. the pre-A-Prime bundle. **The apply has NOT landed.** Everything below is written blind of the
result.

---

## WHY THIS EXISTS

`2.0.0_SA_COO` committed A1–A9 at `8d87d4784c` **before** the edit, so a pass is a prediction met
rather than a number tuned to. **The same hazard applies one level up:** a verifier who writes their
acceptance read *after* seeing the executing lane's report grades against that report's framing.
This is the verifier's own discipline applied to the verifier. It costs one artifact.

**This does not gate anything.** It is not an approval step, not a hold, and not a new criterion —
A9's definition is COO's at `8d87d4784c` and unchanged. This records only what I will check and,
more importantly, **what would make me refuse a green.**

---

## 1. WHAT A9 IS (COO's, not mine — restated only so the bar is unambiguous)

`a4_objects_built` **6/12 → 12/12**, `errors{}` **empty**, on ad-hoc `{"qa_local": true}` against
`mdpf-gold-lambda`.

## 1a. ⛔ THE `12` IS PIN-COUPLED — WRITTEN DOWN HERE BECAUSE IT WAS RECORDED NOWHERE

**`a4_expected` IS DERIVED, NOT A LITERAL.** Verified at source, not taken on relay:
`mdpf_gold_consolidator.py:207 a4_expected_frame()`, deriving from `ARTIFACT_TYPE_SCOPE_SET` /
`SCOPES` (`:92`, 4 members) × `ARTIFACT_TYPES` (`:164`) = **4 × 3 = 12** at the DEPLOYED BUNDLE's pin.

>> **THIS BAR'S `12` IS CORRECT ONLY AGAINST THE CURRENT PIN. @`ba2a91d980` MOVES `a4_expected`
12 → 15** (the D1_CATVIEWS fourth artifact type). **If the pin ever advances past that commit, a
CORRECT run emits 15 and this bar reads it as a FAILURE.** <<

**Tonight it does not bind** — A-Prime's pin is `48c473caa1` + `bae0a826d3`'s pair file, which does not
cross it, so **12 is right for this grade.** Recorded because the coupling existed in nobody's notes:
`0.7.0_AE_CloudOps~K` went looking for it during the bundle census and could not find it, and
`2.0.0_SA_COO` routed it here at 72948 rather than authoring in this file.

**A bar whose correctness silently depends on a pin nobody mentions is a false-RED generator the first
time someone does the right thing** — it fires on the pin advance, i.e. on the fix. Same class as the
`efec3ca8b5`/`cd357d6319` ~8h-window fact, which is now placed at `build_package.py:277`.

**EXPIRY:** this clause lapses when the bundle pin crosses `ba2a91d980`. **At that point the correct
count is 15 and any bar still asserting 12 is wrong** — including this one.

## 2. WHAT I WILL CHECK, AND THE ORDER IS THE MECHANISM

Rule 22's order — `GRAIN` / `COVERAGE` / `STATE` before `DISCRIMINATION`. A green A9 read inside a
wrong `STATE` is the failure mode this whole thread produced once already
(`comp-pipescript MATCH` true and silent about the lambda).

| # | Axis | The check | Refuse the green if |
|---|---|---|---|
| 1 | **STATE** | `get-function-configuration` LastModified **and CodeSha256** both MOVED off the baseline above | either is unchanged — then the re-fire ran the OLD bundle and a 12/12 would be about a different artifact |
| 2 | **GRAIN** | the graded run post-dates the apply | the run timestamp precedes LastModified |
| 3 | **COVERAGE** | `errors{}` genuinely empty, not merely `cottonwood`/`global` cleared | any residual key is unlisted rather than absent |
| 4 | **DISCRIMINATION** | the identity delta reads **0.0100** vs tolerance 0.02, not the pre-fix **43676557.1200** | the pre-fix delta appears anywhere in the run's own log |

## 3. ⛔ THE ARM THAT MATTERS MOST, AND IT IS THE ONE A GREEN CANNOT SUPPLY

**A 12/12 is consistent with two different worlds:** the fix ran, *or* something else changed and the
count moved for an unrelated reason. **The discriminating evidence is that the identity gate flipped
`FAIL → PASS` on the SAME comparison that failed at `43,676,557.12`.** I check the delta, not the
count. A 12/12 without the delta moving is **not** a pass, and I will say so.

**Corollary I am binding myself to now:** if A9 comes back green and I cannot independently confirm
the bundle vintage moved, my verdict is **`COULD-NOT-VERIFY`, not PASS.** Could-not-verify is a
finding, not a failure.

## 4. WHAT I WILL NOT RE-DERIVE, AND WHY

**A1–A8.** `0.4.0_DS_ClientPlatform~T` exercised them twice against a pre-registered bar with a
PRE-FIX CONTROL that reproduces production to the cent. Re-running that seat's own build with that
seat's own method would be a **REPETITION** — one measurement reported twice, wearing the authority
of two — which Rule 22 names explicitly. **I already contributed the limb that seat could not: the
served-label check, executed against the running registry rather than cited from the PRD**
(`display_label('Client > Opal Supervised')` → `'Client - Opal Supervised'`, byte-identical; the
node/label arm failed correctly with `UnknownMemberError`).

**The 16-member bundle census.** Dispatched to `0.7.0_AE_CloudOps~K` by COO at 72791. It originated
as my measurement (72705 s.5) and is now that seat's work. Duplicating it is the four-seats-md5-one-file
waste this estate has already banked.

## 5. THE FALL-BACK, IF THE APPLY DOES NOT LAND TONIGHT

Then A9 is **NOT REACHED** — not failed. Tomorrow's 13:30Z fire runs the `15:29:34Z` bundle at its
**exercised signature: 6/12, `cottonwood`+`global` erroring.** ⛔ **NOT "same as today"** — today's
fire predates that bundle, so a divergent log points at the **scheduled-vs-ad-hoc path**, not at the
fix. Adopted into the fall-back's text by CTO at 72757.

---

## AMENDMENT 1 — 2026-08-26 ~17:52Z, WRITTEN BEFORE THE APPLY, BEFORE ANY RESULT

**Trigger:** Andrew-direct 17:42/17:45Z (@`9261c99991`, relayed `1.0.0_SA_CTO` 72809). He looked at
the Anna accounts himself, withdrew his own ~$22M bet — *"your estimate of 2.87m checks out"* — and
ruled the **DIVZ sleeve is an OPAL SMA**: it buckets to SMAs(L0)/DIVZ(L1), **not** to
Client - Opal Supervised. `2.0.0_SA_COO` sequenced **(i)**: hold the apply, fold a second re-cut into
the same pin, apply once.

**STATE AT AMENDMENT:** `mdpf-gold-lambda` still LastModified **2026-08-26T15:29:34.000+0000**,
CodeSha256 unchanged. **The apply has still NOT landed. This amendment precedes the result, which is
the only condition under which an added criterion is a criterion at all.**

### A5 splits three ways and the split is the point

| id | expected | source |
|---|---|---|
| ~~**A5a** Client - Opal Supervised~~ | ~~**~$1,476,313.07** (unallocated-weight portion)~~ | ~~his ruling + the itemisation already held~~ **— MIS-GRAINED, see AMENDMENT 3** |
| **A5b** SMAs / DIVZ | **$1,393,065.98** (the DIVZ sleeve) | same |
| **A5 total** (unchanged) | **$2,869,379.04** | sovereign-confirmed at account level |

⛔ **A5a + A5b MUST SUM TO A5.** That is the arm: the re-bucketing MOVES money between two Opal
buckets and must not create or destroy any. **If the two parts do not sum to $2,869,379.04, the
re-cut has done something other than re-route** — and that is a refusal, not a rounding note.
⛔ **CONFIRMED BY MEASUREMENT, NOT ASSUMED** (72809's own words). I grade the OBSERVED split, not the
expected one restated.

### The key-spelling arm — the one most likely to pass wrongly

Measured on the served plane this turn:
`s3://opal-data-portal-v2/platinum/mdpf/global/aggregate-aua-timeseries.json` carries
**`opal_div_sma` (2 occurrences)**; **`DIVZ` uppercase: 0**; **`Client - Opal Supervised`: 0**.

⛔ **A re-cut emitting `DIVZ` would MINT A NEW KEY BESIDE AN EXISTING ONE rather than route into it** —
a fresh canonical-key question wearing the appearance of bucket reuse. **I check the emitted key
against the served union's spelling, not against the ruling's taxonomy prose.** The ruling is written
in taxonomy terms; the served key is `opal_div_sma`; those are different name spaces and the ruling
does not relax the served-union canonical-key guard.

### What the second zero means, and it is good news worth stating

`Client - Opal Supervised` is **absent from the served artifact today**. So **nothing client-facing
currently carries the mis-bucketed $1.39M — the correction lands before the segment ever serves.**
This is not a repair of something public, and my verdict will say so rather than let a reader infer
a live defect.

### Binding, unchanged in spirit

If the apply lands before a further amendment is warranted, I grade against **this** bar. If A5a/A5b
arrive ungraded or unmeasured, I report them **UNGRADED — not MET and not FAILED.** I will not
back-fit a criterion to a result.

---

## 6. ~~NOT IN SCOPE OF THIS READ~~ — **SUPERSEDED, see AMENDMENT 2**

~~The **SERVE decision** on the corrected ~$44.6M split is **Andrew's** and is open at him. **A green
A9 is the day's acceptance and is not authorization to serve.** I will not treat a pass as a release
signal and will say so in the verdict itself.~~

**Struck 2026-08-26 ~18:12Z. Andrew's 18:10Z conditional-YES reverses it — see below. Preserved
struck rather than deleted, because a reader who saw the original must be able to tell it was
overturned rather than never written.**

---

## AMENDMENT 2 — 2026-08-26 ~18:12Z: THE STAKES CHANGED, THE ARMS DO NOT LOOSEN

**Trigger:** Andrew-direct 18:10Z @`666fe25b0c`, relayed `1.0.0_SA_CTO` 72923. **SERVE is
CONDITIONAL-YES:** if tonight's apply + grade read GREEN on the pre-registered protocol, the
**08-27 13:30Z fire SERVES the corrected split** — Models +$43.68M incl. Fixed Income, SMAs/DIVZ
$1.39M in `meta.sma_l0`, Client - Opal Supervised ~$1.48M. **Not green → nothing serves and the fork
returns to him.**

**STATE AT AMENDMENT:** lambda still `15:29:34Z` / `3/897ecG...`. Apply still not landed. Written
before the result, as both prior versions were.

### ⛔ WHAT THIS DOES TO THIS BAR

**§6 said a green A9 is not a release signal. That is now FALSE: a green grade IS the serve trigger.**
My verdict moves from *the day's acceptance* to **the gate on a client-facing $43.68M re-attribution
that serves tomorrow.**

This is Rule 22's *"SIZE BY THE CLAIM YOUR WORK FEEDS, not only the act in front of you — a cheap act
can feed an expensive claim."* The act is unchanged; the error-eater moved from **me/the record** to
**the world**. So DISCRIMINATION now binds at full strength, and it already did in this bar's design.

### THE ARMS ARE UNCHANGED — AND THAT IS THE POINT, NOT AN OVERSIGHT

I am **not** adding criteria because the stakes rose. Andrew's own stated condition —
*vintage moves both instruments; delta `0.0100` present + `43676557.1200` absent PRIMARY; 12/12
secondary; both A5 grains placed and sized* — **is the protocol already written here and in
`0.4.0_DS_ClientPlatform~T`'s 72813.** The bar was sized correctly when it was cheap; a bar that
needs tightening once it matters was never a bar.
⛔ **Adding an arm now would also be un-pre-registerable** — invented after the sovereign attached
consequences to the outcome, which is the same defect as tuning to a result, one step removed.

### WHAT I RE-CHECKED RATHER THAN ASSUMED, AND IT CAME BACK BENIGN

A serving run means the artifacts reach consumers, so I asked what is **NEW on the served plane**:
- `meta.sma_l0` is a new meta key → **additive**; unknown-key addition is not the estate's portal
  failure mode (`MISSING = runtime undefined` is, and that is the opposite direction).
- `Client - Opal Supervised` — **measured 0 occurrences in the served artifact today.** The segment
  is NEW, not changed. **So the $1.39M re-bucket cannot move a number any consumer is displaying,
  because nothing is displaying it yet.**
>> **NO EXISTING SERVED VALUE IS OVERWRITTEN BY THIS CHANGE. Both affected structures are new to the
served plane.** That is why the raised stakes do not require a new consumer-side arm — checked, not
assumed. <<

---

## AMENDMENT 3 — 2026-08-26 ~18:15Z: **THE DEFECT WAS IN MY OWN BAR.** A5a named the SEGMENT and carried a COMPONENT's value

**STATE:** lambda still `15:29:34Z`. Apply still not landed. Written before the result.

**Trigger:** `0.4.0_DS_ClientPlatform~T`'s 72932 caught a **$780,381.91** gap between the serve
conditional's `~$1.48M` and the field that actually ships; `1.0.0_SA_CTO` ruled **(a)** at 72938 —
the artifact is right, the headline was the subset grain, and Andrew's definition says **ANY** account
containing Opal Models, with no parent-type qualifier.

### ⛔ AND THE SAME DEFECT IS IN AMENDMENT 1, WHICH IS MINE

My A5a row read **`Client - Opal Supervised | ~$1,476,313.07`**. That row **names the SERVED SEGMENT
and gives the value of ONE COMPONENT of it** — the unallocated-weight portion of the non-Opal-parent
2-account subset. The parenthetical said "unallocated-weight portion," so it was not unlabelled; it
was **mis-attached**, which is worse, because a qualifier in parentheses reads as a description of
the segment rather than as a different population.

**CORRECTED — both grains, each carrying its denominator ON THE SAME LINE as the number:**

| id | population | expected |
|---|---|---|
| **A5a** Client - Opal Supervised — **THE SERVED FIELD** | **3 accounts**, full segment | **$2,256,694.98** |
| **A5a′** non-Opal-parent subset | **2 accounts** (Anna \*9237, \*9238) | **$1,476,313.07** |
| **A5b** SMAs → `opal_div_sma` | **1 account** (Anna \*9237) | **$1,393,065.98** |

Itemisation of A5a: sleeve **$780,381.91** + unattributed-leg **$0.00** + unallocated **$1,476,313.07**
= **$2,256,694.98**. Re-derived independently at exact decimal; reconstructs to the cent.
**The `$0.00` unattributed-leg limb IS the DIVZ leg leaving** — a check arm that exists only because
the residual was itemised rather than left as a remainder.

**I GRADE THE SERVED FIELD AT A5a (full, 3 accounts) and report A5a′ beside it.** Grading only the
subset would score a serving figure against a population that is not what ships.

### THE COUNT, AND WHY I AM PUTTING IT IN MY OWN RECORD

**This is the FIFTH instance tonight of one correct number travelling with a wrong population** —
$38.1M/129-accounts · "$2,869,379.04 across all 129" · A5b's 1-vs-2 · the serve conditional's 2-vs-3 ·
**and this row, in the verifier's own pre-registered bar.** I filed the boundary-precision note on
someone else's claim at 72826 and carried the identical defect in an artifact I had committed twice.
**The axis does not spare the seat that polices it.** Nothing here changes an arm; it changes which
number an arm is pointed at, which is the whole failure mode.

### BINDING, UNCHANGED AND NOW LOAD-BEARING

`COULD-NOT-VERIFY` if the vintage does not move on **both** instruments. **Under a conditional-YES,
COULD-NOT-VERIFY is NOT-GREEN, and not-green means nothing serves.** I will state that consequence
explicitly in the verdict so no reader has to derive it — and I will not soften a could-not-verify
into a pass because a serve is waiting on it. **That is precisely the pressure this clause was
written, at zero stakes, to survive.**
