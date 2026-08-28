# CTO~Z -- Andrew overruled my wait-for-the-fire framing, and ten minutes of QA found a live production defect, 1945-2019Z

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, VALIDATE, ADJUDICATE

**Serial:** `1.0.0_SA_CTO~Z` · **Window:** 2026-08-28 19:45Z -> 20:19Z (continues
`ctoZ_D4_categorical_close_and_the_stale_face_bias_1755-1945Z.md` @`7a87097f91`)
**Basis:** ANDREW-DIRECT x3 -- *"we are expecting that work done today"* (20:03Z, addressed to this
seat by name) · *"D1 is the focus"* + *"If they need additional parallelization, I would prefer they
run it now"* (20:09Z) · *"quietly test out /comp-adversary and assess validity"* (20:09Z). Then the
one that mattered: *"no excuse to wait for tomorrow when we can find out if data flows and is
presented properly today."*

---

## 1. WHAT I GOT WRONG, FIRST, BECAUSE EVERYTHING ELSE FOLLOWS FROM IT

I told Andrew D1's remaining criteria were event-gated on tomorrow's fires and framed the wait as
MANDATORY. **He overruled it and he was right.** I had collapsed two different questions:

```
  ACCEPTANCE EVIDENCE        genuinely needs a SCHEDULED fire. The criteria say so in terms.
  "DOES THE DATA FLOW AND
   RENDER CORRECTLY"         needs NOTHING of the sort. It was answerable all evening.
```

CLAUDE.md settles it and I did not apply it: *"Ad-hoc gold runs are PERMITTED FOR QA; production
pipelines MUST be scheduled"* and *"'Waiting for the scheduled run' is the same coast-failure -- fire
the ad-hoc QA run (it tests; the scheduled fire stays the acceptance)."*
>> **I HAD THE RULE, CITED ITS SIBLING CLAUSES ALL DAY, AND STILL TREATED THE CLOCK AS A WALL.**
   The exception clause requires NAMING the evidence an ad-hoc would destroy -- I never tested that
   and the answer is nothing: tomorrow's scheduled run writes a NEW date key regardless.

## 2. THE DEFECT THE QA RUN FOUND -- LIVE, IN THE DEPLOYED LAMBDA

`/mdpf-refresh gold`, ad-hoc, 20:15:58Z:
```
  mdpf-gold-lambda  FunctionError=Unhandled
  KeyError: 'category-views'
  mdpf_gold_consolidator.py:1485 lambda_handler -> :1398 build_all -> :878 conditional_put
```
**MECHANISM, read at the deployed pin `70a0828226` (byte-identical to the running package):**
```
  :847  business_equal -> mod.load_process_time_paths(sectionb, artifact_type)
        the G2 canonicaliser has NO ENTRY for `category-views` (the newest type, born 08-19)
  :880  conditional_put catches (ValueError, UnicodeDecodeError) ONLY
        KeyError is NOT caught -> propagates -> the WHOLE gold run dies for EVERY scope
```
**SEVERITY, stated precisely rather than dramatised:**
- **Tomorrow's scheduled fire is PROBABLY FINE.** It writes `2026-08-28.json`, a NEW date key ->
  `written`, the conflict path never runs, `business_equal` is never called. **I am NOT claiming
  tomorrow is broken.**
- **But the path is live and total.** It fires whenever `category-views` meets an EXISTING key with
  business-different content -- any same-day re-run, any reland, any backfill of an existing date.
  One missing map entry takes down the entire run for all four scopes.
- **And it disables the recovery tool on the type that needs it most:** `/mdpf-refresh --reland`
  exists for exactly this scenario and currently crashes in it.

**NOT ESTABLISHED, and both are quick:** whether this is latent since 08-19 or introduced by today's
pin advance; and the G2 map read directly rather than inferred from the exception.

## 3. TWO CORRECTIONS RECEIVED, BOTH ON NUMBERS I HAD RELAYED TO ANDREW

| I said | Measured | Who caught it |
|---|---|---|
| "four criteria, one ~13:00Z event" | **THREE times across TWO EventBridge planes** -- 13:00Z Rules, 13:30/13:40/13:50Z Scheduler | `2.0.0_SA_COO~Z` |
| "TO-N1-DS certified 3 of 5" | **3 of 8** -- 3 of 5 is the D4 TO; five criteria open, not two | `3.0.0_SA_CVO~Z` |

The first has an operational bite: **`TS1-AC2` needs the PUBLISHER at ~13:50Z, not the gold floor at
13:30Z.** A seat scoring it early reads the pre-publish object and **reports a correct fix as FAILED.**
NOTE: the COO correction was triggered by `0.4.0_DS_ClientPlatform~Z` writing ~13:31Z against COO's
~13:00Z -- **the disagreement was the signal**, and neither seat had to be sure it was wrong.
The second ran OPPOSITE to the day's other eight corrections: it OVERSTATED completeness. First of
its direction today, caught by the seat whose own certificate carried it.

## 4. /comp-adversary VALIDITY ASSESSMENT (Andrew-direct, kept off the fabric relay per "quietly")

Assessed INDEPENDENTLY -- `0.0.0_AB_MSTR~Z` holds its own findings and deliberately withheld them so
this assessment would not inherit a frame. I did not ask for them.

```
  --self-test                     PASS 4/4 (planted bogus commit flags UNVERIFIABLE; pin control
                                  discriminates 2/1/1; --open emits empty-context; family shape)
  compose <a real instance>       ran clean, produced a well-formed declaration
```
**THE LIMIT, found by pointing it at a KNOWN defect rather than at a self-test:** run against
`D1_CATVIEWS.TO-M1-DS_PROOF_OF_SPEC.json`, whose AC4 citations `3.0.0_SA_CVO~Z` independently proved
resolve to NOTHING at any ref, it reported:
```
  source 1: cited-commit verification   2 attempted / 2 verified / 0 UNVERIFIABLE
  source 2: cited-path vintage          8 attempted / 8 stable / 0 flagged
  pins found: ... 7 file:line cites     <- COUNTED, and NEVER VERIFIED
```
>> **IT VERIFIES THAT CITED COMMITS EXIST AND CITED PATHS HAVE NOT MOVED. IT DOES NOT VERIFY THAT
   `file:line` POINTS AT WHAT IT CLAIMS.** The count of 7 sits in the same block as two
   verified/stable denominators, which invites a reader to think all three were checked. A known-bad
   line citation passes SILENTLY.
**ASSESSMENT: VALID FOR WHAT IT CLAIMS, AND ITS OUTPUT SHAPE OVER-SELLS THE COVERAGE.** The skill's
own header already says every figure is scoped to what the author CITED, never to what EXISTS -- this
is that hazard with a concrete instance. **REC: either verify line cites, or print `7 file:line cites
(NOT VERIFIED)` so the denominator carries its own limit.** Not proposing the change; reporting.

## 5. Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `/mdpf-refresh` | `status` then `gold` | PREFLIGHT OK (4 scopes at T-1, inputs current); `gold` **FAILED and that is the finding** -- unhandled KeyError in the deployed lambda |
| `comp-adversary` | `--self-test`, `compose <instance>` | 4/4 self-test PASS; **compose surfaced a real coverage limit** (see s.4) |
| `comp-find` | 2 token censuses for the laptop law relay | 12 hits / 27,867 files each, denominators printed |

**WHAT FAILED, and it is mine:** I wrote a temp file from bash to `/tmp` and read it from native
python by the same literal string. **MSYS `/tmp` and `C:\tmp` are different directories** -- the read
raised FileNotFoundError. Banked hazard, own instance, cost ~20 seconds. The scratchpad absolute path
is the only safe form on this box.

## 6. Blockers

**NONE at this seat.** The KeyError is a live defect with no owner yet assigned -- it is NOT blocking
this seat and NOT blocking tomorrow's scheduled fire on the reading in s.2.

## 7. Current State (zero prior context)

- **Fabric is FOUR seats:** `0.0.0_AB_MSTR~Z`, `1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~Z`, `3.0.0_SA_CVO~Z`.
  Zero tier-2 lanes -- all killed under Andrew's cleanup order; every D1 and D4 executor act was
  already discharged before the kills.
- **`mdpf-gold-lambda` carries an unhandled `KeyError: 'category-views'` on the conflict path.**
  Deployed pin `70a0828226`, `business_equal` :847 / `conditional_put` :880. Same-day re-runs and
  relands crash the whole gold run; new-date writes are unaffected.
- **Tomorrow, in order, both EventBridge planes measured ENABLED:** 13:00Z Rules
  (`etf-positioning-producer-daily`, D4's last criterion) · 13:30Z Scheduler (`mdpf-scheduled-floor`,
  D1 gold rung) · 13:50Z Scheduler (`opal-assets-mdpf-portal-publisher-daily`, D1 SERVED rung).
- **10 event-gated criteria** across D1 + D4's remainder; 4 further rows are terminal by design or
  ruling (APPLIED-GATED, KNOWN-UNREACHABLE, issuer-WITHHELD, issuer-DEFERRED).
- Laptop `org/XXX.md` A.2 paragraph relayed as TEXT (not contained on SITEZ). **MEASURED HERE: the
  finding pair it names is ABSENT on this device** -- 0 occurrences, and `FINDINGS.md` last written
  2026-08-19. That is absence-of-RECORD, not absence-of-CONDITION.

## 8. Next Steps

1. **[UNOWNED -- needs placement]** The `category-views` G2 map entry + widening
   `conditional_put`'s except clause to cover `KeyError`. Small, and it restores the reland path.
2. **[`1.0.0_SA_CTO~Z`]** Close the two unestablished limbs in s.2 (latent-vs-introduced; read the G2
   map directly).
3. **[SCHEDULED]** The three stages above. **Nothing scores before its own stage has run.**
4. **[ANDREW]** Whether to pursue seeing corrected data served TODAY -- the reland route is a
   RESERVED-CATEGORY act needing his explicit word, and it is currently blocked by s.2's defect.

## 9. One thing worth carrying

**TEN MINUTES OF QA FOUND A PRODUCTION DEFECT THAT FOUR HOURS OF CORRECT REASONING ABOUT CLOCKS DID
NOT.** Every clock fact I gave Andrew tonight was true and carefully measured -- the three stages, the
two planes, the 13:50Z publisher trap. **All of it was reasoning about WHEN the evidence would arrive,
and none of it asked whether the thing works.** The rule I broke is in CLAUDE.md verbatim and I had
quoted its neighbours all evening.
>> **A correct model of a constraint is not a substitute for touching the system.** The wait was
   real; treating it as a reason not to look was the defect, and Andrew caught it in one sentence.
