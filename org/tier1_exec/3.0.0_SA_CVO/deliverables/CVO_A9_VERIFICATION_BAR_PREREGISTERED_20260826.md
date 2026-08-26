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
| **A5a** Client - Opal Supervised | **~$1,476,313.07** (unallocated-weight portion) | his ruling + the itemisation already held |
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

## 6. NOT IN SCOPE OF THIS READ

The **SERVE decision** on the corrected ~$44.6M split is **Andrew's** and is open at him. **A green
A9 is the day's acceptance and is not authorization to serve.** I will not treat a pass as a release
signal and will say so in the verdict itself.
