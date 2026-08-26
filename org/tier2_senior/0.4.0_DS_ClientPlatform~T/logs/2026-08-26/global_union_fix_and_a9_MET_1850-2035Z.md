# 0.4.0_DS_ClientPlatform~T -- the global-union fix, the STOP that caught a false green, and A9 MET (1850-2035Z)

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT (primary) · VALIDATE · DIAGNOSE

Continues `cotpair_d8_repair_recuts_and_a9_grade_1649-1850Z.md` @`9262072602`. Window: the global
composition fix seated by `1.0.0_SA_CTO` 73148, through the authorized real chain run, to **A9 MET**
(ratified `2.0.0_SA_COO` 73562).

---

## SUMMARY

The cottonwood repair recovered a NEW `by_model` key, `opal_fixed_income`. Those dollars reached
global's `model_aua` but not its `by_model` cohort sum, because `GLOBAL_MODEL_KEYS` is a **FIXED TUPLE
that discovers nothing**. Registered the key across the union, exercised it on real artifacts, and
graded A9.

**A9 = MET.** 12/12, `errors=none`, **0 FATAL lines**, identity delta `0.0100` present and the pre-fix
`43676557.1200` absent, global composition gate PASS across 462 dates.

**The load-bearing act of this window was a STOP, not a fix:** my first post-edit run printed
`global composition gate PASS -- clean across 462 dates`, and it was **a pass over the wrong input**.

---

## FINDINGS

### F7 -- I nearly reported a green that was about a world where the fix did not exist

Post-edit run: `opal_fixed_income` **None on all 462 dates**, yet the composition gate PASSED.
MEASURED WHY: the fold reads `gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries.json`, last written
**2026-08-25T19:45:31Z** -- a day before the pair fix -- carrying 5 keys with the key ABSENT. With the
key absent from the leg, the fold takes the *"firm does not carry this model: not a gap"* branch and
**passes by SKIPPING the thing under test.**

⛔ **RULE 22's ORDER FAILURE IN ITS EXACT FORM: DISCRIMINATION PASSING INSIDE A WRONG STATE.** A green
gate, a clean 462-date census and a correct-looking identity -- all true, all about the wrong world.
Caught only because gate (ii) pre-registered a SPECIFIC number and the observed value was `None`
instead of `$8,442,396.92`.

**THE SEQUENCING FACT BEHIND IT:** `qa_local` writes **ZERO S3 by design**, so the delta is
unobservable on ANY qa_local run, before or after any bundle rebuild. Exercising it required a slice
**regenerated AND written**. That fact -- not the edit -- was what actually changed the night's plan.

### F8 -- I flagged the gate as possibly mis-dated; I was reading a different frame

I measured that the dim carries **no Fixed Income row in PARTITION `date=2026-08-25`** (it appears in
`date=2026-08-26`, 2 accts, `$8,442,396.91`) and asked whether gate (ii) was pointed at the wrong date.
**`1.0.0_SA_CTO` reconciled it (73253 s.1): the slice is VALUE_DATE-keyed.** The row lives in partition
08-26 carrying value_date 08-25, so regeneration places those dollars **at the 08-25 cell** -- which the
regenerated slice then confirmed by exercise (`[('2026-08-25', 8442396.91)]`, 1 non-null cell).
**Two frames of the one word "date".** The gate was NOT re-pointed. **I did not amend a bar I am graded
against** -- that is the back-fitting the discipline exists to prevent, and the bar was right as written.

### F9 -- A fourth wrong-denominator instance, inside a SOVEREIGN CONDITIONAL

The 18:10Z conditional-YES quoted `Client - Opal Supervised ~$1.48M`. **The served field carries
`$2,256,694.98`** -- a `$780,381.91` gap, being a third account's sleeve dollars. Surfaced pre-serve;
`1.0.0_SA_CTO` ruled (a): the artifact is right, the headline was the subset grain, and the serve
figure was corrected on the record. **Andrew's 20:15Z ratified set carries the full-segment figure.**
Fourth time this one number travelled with a wrong population attached in a single thread.

### F10 -- The owned-paths gate refused me and was RIGHT

`infra/aws/lambda/.../mdpf_revamp_model_crosswalk.py` is lane `CLOUD_OPS_OR_ETL` ("any AE agent"); this
seat is DS. **I did not `--force` and did not self-authorize `GIT_COMMIT_AUTHOR_OVERRIDE` to reach into
a lane I do not own** -- the same refusal `2.0.0_SA_COO` took minutes earlier and called right.
Committed the 3 DS files, measured and published the divergence blast radius (`build_package.py:141`
takes the data/mdpf copy, so tonight's fold was unaffected; the infra copy feeds
`opal-assets-daily-emitter`), and routed the re-vendor to AE. **CLOSED at 20:31Z: the re-vendor landed
ON ORIGIN, both homes byte-identical, and my working tree is clean on that path.**

### F11 -- My gate (i) control re-implemented its own subject

My gate (i) test evaluated the fold's predicate MYSELF rather than observing the fold's branch --
**a control that re-implements its subject tests the copy.** I reported 18 candidates AND the caveat,
and asked a non-author to take the settling read rather than clear my own control.
`1.0.0_SA_CTO` did: the 18 DO take `gap = True` (my re-implementation was faithful), **but `gap` is
local to one (key,date) cell** and `:1890-1893` treats a per-key `None` as a NON-CONTRIBUTION, not a
poison. **Gate (i) CLEAN.**
⛔ **AND THE RECORD CORRECTION MATTERS MORE THAN THE VERDICT:** `2.0.0_SA_COO` 73430 caught that the
closing limb (`:1890-1893`) has **ONE reader**; `3.0.0_SA_CVO` corroborated only the `gap`-fires limb,
which is a REPETITION of the same trace. **Gate (i) is CLEAN SINGLE-SOURCED.** I carried that
correction into my own grade rather than letting "two senior seats agreed" ride.

---

## ACCEPTANCE -- A9 = MET

Fired 20:27:07Z, after `0.6.2_AE_PartnerETL~A`'s apply at 20:21:10Z.

| arm | result |
|---|---|
| PRECONDITION vintage, BOTH instruments | `18:21:12Z -> 20:21:10Z`; `LdShsMmF... -> 57V6D/ZN...` **MOVED** |
| ARM 1 `FATAL:` lines, counted DIRECTLY | **0** (never the 5-of-7 summary counter -- known defect, COO 73506) |
| ARM 2 PRIMARY -- identity delta | `0.0100` PRESENT; `43676557.1200` **0 occurrences** |
| ARM 3 -- global composition gate | **PASS**, clean across 462 dates |
| ARM 4 SECONDARY -- objects | **12/12**, `errors=none` |

Also 0 occurrences of `SCOPE FAILED` / `refusing to emit` / `SystemExit` across 717 log lines.

**GATE (ii), the pre-registered one:** `opal_fixed_income @2026-08-25 = 8,442,396.91`;
`sum(by_model cohort=model) 1,802,566,138.35` vs `model_aua 1,802,566,138.36`, delta **0.01**;
movement **+8,442,396.91** vs pre-registered **+8,442,396.92**. **MET (1c float).**
>> `model_aua` now reads **1,802,566,138.36** -- byte-for-byte the figure in the original FATAL. Both
>> sides of that failed identity agree, and the side that moved is the one the fix targets. <<

**NOT VERIFIED, stated rather than assumed:** I could NOT find a `by_model{10}` line in the lambda's
stream, so I did **not** report "global emitted 10 keys" as measured from this run. `GLOBAL_MODEL_KEYS`
9->10 was proven by `0.6.2_AE_PartnerETL~A` on the RE-DOWNLOADED RUNNING BYTES -- stronger evidence,
and that seat's. **Cited, not re-derived.**

---

## COMPILER TOOLS

| tool | result | note |
|---|---|---|
| `commit-gate.sh` | PASS | 4 files, then 3 |
| `safe-commit.sh` | **REFUSED then PASS** | owned-paths refused the AE-lane path (F10) -- the gate working |
| `safe-deploy.sh` | PASS x2 | 3 gold scripts, `comp-pipescript` MATCH each |
| crosswalk `_self_test` | **PASS UNCHANGED** | "11 models: 7 served, 5 core, 2 sma, 2 blend" -- the `== 2` assert passing WITHOUT being edited IS the control that the tightened predicate says what it means |

**GAP CARRIED FORWARD (restated from the prior log, now doubled):** `comp-pipescript deployed` returns
MATCH while certifying only the S3 code tree -- **silent about the lambda bundle**. Second independent
way that instrument reads green on stale running bytes, distinct from the CRLF false-STALE class and
pointing the opposite direction.

**CRLF:** `build_cottonwood_mdpf_slice.py` is CRLF (1044 CRLF / 0 bare LF). My LF-anchored edit failed
LOUD (the good direction); git warned it will normalise to LF on next touch, which I named to
`0.6.2_AE_PartnerETL~A` so a CRLF-only delta would not be misread as a content change in its diff arm.

---

## COMMITS + WRITES

| ref | what |
|---|---|
| `2d5f8a7f74` | the 3 DS-lane files, flagged DESIRED-NOT-EXERCISED (flag superseded by 73331 once exercised) |
| deploys | `mdpf_revamp_model_crosswalk.py`, `dim_mdpf_aggregate_aua_timeseries.py`, `build_cottonwood_mdpf_slice.py` -> `code/scripts/{gold,assets_gold}/` |
| S3 writes | pair `--upload` (3 objects) + slice `--upload` (95,098B). **GOLD plane only, DS lane Rule 13. No served/platinum object touched.** |

**ROLLBACK, captured BEFORE any write** (`opal-data-assets` versioning = Enabled):
`aggregate_aua_timeseries.json` `0F00n.QOTPRgiWGd1NbS0TYqS7rClS.o` ·
`account_distribution.json` `s.zJ2MVHfidiRRNdaTdElVbW46dp64dW` ·
`aum_metrics.json` `_goNvzkQl3O06lWig8D3NA0WoEe5MGk5` ·
`account_units.json` `unJ7.iZf8oHv9biwr3llirQutqtC_HKo`

---

## BLOCKERS

**None.** A9 MET and ratified. Nothing owed by this lane on D8.

---

## CURRENT STATE

`mdpf-gold-lambda` runs pin `1b96f70ad3` (applied 20:21:10Z, `CodeSha256
57V6D/ZNiAGSKBe2UkJ33aevjHDCLj0HNRphN//+iKg=`), `GLOBAL_MODEL_KEYS` 10 keys incl. `opal_fixed_income`,
crosswalk 11 models. Full chain green: 12/12, errors none.

**SERVE IS ARMED.** Andrew 20:15Z `@7a843d25da`, VERBATIM: *"Agreed completely we should def be
serving."* Each scope serves at the 2026-08-27 13:30Z fire **IFF its own pre-registered gates pass**;
anything not green refuses loudly and stays stale. Ratified served set:
Models **+$43,676,557.12** (incl. Fixed Income $8,442,396.91) · SMAs/DIVZ **$1,393,065.98** in
`meta.sma_l0` · Client - Opal Supervised **$2,256,694.98 / 3 accounts**.
**Tonight's greens are DECISION evidence; the scheduled fire remains the ACCEPTANCE.**

---

## RESIDUALS CARRIED (none blocking)

1. **Gate (i) CLEAN but SINGLE-SOURCED** on `1.0.0_SA_CTO`'s `:1890-1893` read. If doubled, it needs a
   DIFFERENT instrument, not the same trace -- and not by me: I wrote the change.
2. **`gap=True` is a MISLABEL** on a not-yet-existing model's pre-existence dates ("contributing firm,
   missing measurement" vs the honest "outside its existence window"). Identical output, zero
   arithmetic consequence, but it will confuse the next reader who greps gap counts.
3. **The run-internal asymmetry** (my 73331 s.4): at 18:24Z `model_aua` already carried the Fixed
   Income dollars while `by_model` did not, within ONE run reading ONE firm. Narrowed tonight, **never
   explained.** Both sides agree now, so it gates nothing -- **it must NOT be recorded as "resolved by
   the fix".**
4. The 5-of-7 summary counter defect (CVO's), which is why ARM 1 counts `FATAL:` lines directly.

---

## NEXT STEPS

1. **[`3.0.0_SA_CVO`]** last word against its own pre-registered bar `@e4b4966fc3`; its
   COULD-NOT-VERIFY precondition demonstrably does not fire (both vintage instruments moved).
2. **[`3.0.0_SA_CVO`]** reads tomorrow's 13:30Z fire on a SERVING run.
3. **[unassigned]** residuals 1-3 above, at the next deliberate touch of the fold.

---

## DO NOT

- **Do not read a green composition gate as evidence the fix works without checking WHICH SLICE the
  fold read.** That exact green was available tonight and was false.
- **Do not grade this chain off `a4_objects_built` or the 5-of-7 summary.** Count `FATAL:` lines.
- **Do not record gate (i) as double-read.** One reader on the closing limb.
- **Do not treat tonight's ad-hoc greens as production evidence.** The scheduled fire is the acceptance.
