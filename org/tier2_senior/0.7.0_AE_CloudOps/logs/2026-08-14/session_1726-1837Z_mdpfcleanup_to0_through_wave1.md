# Session 1726-1837Z — OPAL_MDPFCLEANUP TO-0 → wave-1 close (+4 CRO gate-applies interleaved)

**archetype:** MIXED (VALIDATE / DEPLOY / DIAGNOSE)

## Headline
Andrew's debt-cleanup project ran TO-0 (pin+exercise) through the wave-1 kill close in one evening:
21 AWS resources destroyed across 3 gated applies, 2 ratified kill rows REVERSED to KEEP on
falsifying evidence (the pre-agreed rule working), 1 new kill row discovered that the PRD census
missed, and 3 instrument corrections self-caught and filed. Zero reserved acts; zero unratified acts.

## TO-0 (proof rev 3 @95bc510e77, COO-validated 7/7 at rev 1)
- wsb/wsd feeders pinned at deployed bytes -> K3-COUPLED not K2 (feeds read daily by the KEEP
  smartx Lambda's account_distribution job); wsb is NOT the canonical fact_model_aum_daily producer.
- NEW KILL ROW (census gap): smartx-account-distribution-daily (cron 30 11Z) -> the
  {"job":"account_distribution"} leg — the daily 11:30:39Z json/mdpf writer, pinned via 6-day
  version history + rule-by-cron + deployed bytes. Route repointed platinum at CANPLAT (deployed
  router:6 read whole, 332B); FE reads platinum (aum.ts:490 verbatim).
- Publisher R12 legacy emission: ALREADY RETIRED in deployed bytes ("json/mdpf/* is never
  touched"); stale memory attribution corrected in MEMORY.md.
- freshness-checker ABSENT (named-error + 0/197 materialized; a 50-per-page trap read discarded).
- Trees swept with denominators; guarded-set both-spellings clean (444 underscore keys == archive).

## TO-1 (ratified) / TO-2 (collapsed to verification)
- Card @4f007d31af -> Andrew "all recs approved" @874b52729c; proof_TO-1 @c7a4573084 with referents.
- TO-2's content-vs-wiring fork had a third answer: the dim re-home ALREADY EXISTS (consolidator
  :712 at the executing pin mints the dim; today's untouched 13:30:39Z scheduled floor wrote it).
  Value tie: canonical vs legacy same-day dim = identical structure, deltas ONLY value_date+dollars
  (the vintage roll, self-attributed in-artifact). proof_TO-2 @809b948ef4. CTO (b): acceptance
  stamps after tomorrow's cycle under pin 84c1fc08fd (today's sample exercised pre-repin bytes).

## Wave-1 (TO-3, proof @95bc510e77; ledger CLOSED)
- Apply 1 (v0.9.1): account-distribution trigger set, 3 destroys. Starts TO-4's >=7d access-log clock.
- Apply 2 (v0.7.5): cot-session-complete set, 3 destroys (1x/7d vs daily chain = the exercise).
- Apply 3 STOPPED PRE-EDIT: bd runners FALSIFIED-LIVE (InvokeRunner grant session-chain.tf:121
  exercised; fees-runner 22:21Z last night, runner 00:09Z today) -> rows KEEP per the ratified
  disputed-row rule; last-invocation instrument now a STANDING PRD requirement @4708e35800.
- Apply 4 (v0.9.2): smartx K1 sets + 2 validate-found scheduler-role companions, 15 destroys;
  full-root plan REJECTED dirty (2 unrelated KEEP-Lambda staged-artifact updates surfaced to COO,
  not applied); 0-diff stated with its denominator (residual == exactly those 2 rows).

## The day's instrument class, third and fourth sightings (all self-caught)
- TO-0's "ABSENT both namespaces" on smartx-model-monthly-pull queried the BASE name; the real
  scheduler carried -daily (CloudTrail DeleteSchedule NONE proved it existed). Corrected rev 3.
- TO-0's trigger-state dormancy could not see the bd runners' second entry point; the
  consumers-first sweep was the working control. Both gaps named, both now closed by standing rule.

## Interleaved: 4 CRO re-pin gate-applies (mdpf-gold-lambda)
GATE-GO #1-#4 executed (v2.1.2-v2.1.5): expected-rows-only plans, safe-apply, 0-diff, four-way sha
identity each (built==uploaded==downloaded==executing). The EVR/point_class/W-7 bytes carry production.

## Open at session end
- Tomorrow ~13:30-14:00Z ONE PASS, THREE CLOSURES: TRGALN B2-slot adjudication; CLEANUP TO-2
  acceptance sample (pin 84c1fc08fd unattended); TO-5 cycle read. Then K3 wave on CTO's stamp.
- TO-4 reserved kills: access-log window running from apply-1; conditions durable in the TO file.
- Residuals at owners: smartx staged-artifacts classification (COO); account_distribution dead-code
  rider (CTO); 8 local tags riding MSTR's integration window.

## Compiler Tools
| Tool | Invocation | Result |
|---|---|---|
| comp-trigger / comp-find / comp-routes | TO-0 sweeps + trace + edge-versions | census, writer pin, route repoint (DESIRED) -- then CLOSED at deployed edge bytes |
| comp-blast | (earlier session) | radii; kuzu warm |
| terraform | state list/show x4 roots, validate, targeted plans x7, safe-apply x7 | all applies expected-rows-only; every 0-diff carries its denominator |
| live primitives | get-function downloads x5, version-history reads, CloudTrail lookup, log last-event reads, simulate battery (earlier) | every kill claim desired/applied/exercised |
| python | matched-row value diffs, block excision, proof writers | the day's decisive instruments |

What worked: consumers-first sweeps + found-controls caught two would-be incidents pre-mutation.
What failed: three of my own absence/dormancy reads used wrong-domain instruments — each
self-caught within the session and corrected on the record. Gap filed: kill-claim invocation-history
now standing (CTO @4708e35800).
