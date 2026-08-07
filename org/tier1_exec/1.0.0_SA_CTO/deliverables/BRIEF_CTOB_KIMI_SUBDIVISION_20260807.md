# BRIEF — `1.0.0_SA_CTO~B` reinstantiation: Kimi subdivision, now FUSED to NFRA_PYFIELD

**From:** `1.0.0_SA_CTO` (base) · **2026-08-07** · **Authority:** Andrew-direct at the base CTO terminal

> **VERBATIM (Andrew, 2026-08-07):** *"Regarding Kimi, we need to reinstantiate CTO~B to pursue that
> I closed their session, will need a brief issued to them as well because I want to make sure that
> work they are doing is tied in with the development of the NFRA_PYFIELD ontology + probably bring
> 0.8.0_AE_CloudComp base on to spearhead that work as well."*

**Read this before touching the layout.** Three things changed while you were down, and two of them
invalidate premises your own prior session was working from.

**⛔ NOTHING IN THIS BRIEF IS A GATE.** No approval step, no sign-off, no hold. You build on
build-correctness + rollback. Andrew's 2026-08-06 ruling stands and *you* were the seat that caught
yourself manufacturing one — that correction holds and I am not re-imposing it from above.

---

## 1. YOUR CORPUS-STATE PREMISE IS STALE — measured today, and it makes your job MORE urgent

`KIMI_SEMANTIC_VERTICAL_PIPELINE_RESEARCH_20260804.md` records the scheduler as **DISABLED** and
*"exactly ONE report day (2026-07-30)."* **Both are now false.** Measured at my seat 2026-08-07 ~15:1xZ:

| | measured |
|---|---|
| `estate-report-0900et` | **ENABLED**, `cron(0 9 * * ? *)` America/New_York |
| report days present | 07-30, 08-04, 08-05, 08-06, **08-07** |
| today's run | fired **13:01:03Z**, completed 13:11:11Z |
| today's corpus | **153 nuggets** (105 SOVEREIGN / 9 DELEGATED / 39 UNCLASSIFIED), 881 changed paths, `degraded_sources: []` |

**The deterministic half is HEALTHY and producing daily.** What failed today is the half you are
being spawned to replace:

```json
"ai_section": "ABSENT",
"ai_absent_reason": "KIMI_TIMEOUT",
"ai_call": { "prompt_chars": 73798, "prompt_tokens_est": 18449,
             "max_tokens": 32000, "timeout_seconds": 300,
             "attempts": [ { "attempt": 1, "elapsed_s": 300.1 } ] }
```

**The AI half has never once succeeded, and it failed again this morning on a live production fire.**
Your subdivision is not a speculative improvement to a dormant pipeline — it is the direct remedy for
a defect that fires every single day against a rich, healthy corpus. That is a much better warrant
than your prior session had, and it is the reason Andrew reinstantiated you rather than parking this.

> *A COO capacity note reported the corpus "STALE at 07-31" and concluded a subdivision built now
> would point at nothing. **That was measured wrong and I corrected it** — they had conflated the
> changed-path corpus (healthy) with the B6 text-input stratum (genuinely empty, see §5). Do not
> inherit the stale version from any relay.*

---

## 2. ⭐ THE NEW CONSTRAINT — Andrew has FUSED your work to NFRA_PYFIELD

This is the instruction you cannot infer from your own lane, and it is the reason this brief exists.

`NFRA_PYFIELD` is **AUTHORIZED and REGISTERED** (Andrew-direct: *"Yeah i want the python data
tracing"*). PRD v1.0 at `docs/architecture/NFRA_PYFIELD_PRD.md`. It builds a Python field-grain
extractor emitting D1-conformant `FLOWS_TO` edges for `data/*/scripts/{gold,silver}/**`. **TO-0 is
already CLOSED** — the column denominator landed in 43 minutes: **2,744 of 4,406 name-based subscripts
are columns, 62.3% [95% CI 56.8–68.3]**, vintage stamped, systematic sampling. TO-1 (the recognizer)
is authored and its receiver is `0.8.0_AE_CloudComp` base.

**THE CONTRACT — three terms, and `2.0.0_SA_COO` ruled the shape correctly: these are TWO workstreams
with a written contract, NOT one workstream with two seats.** The instrument is Rule 24 postulate (iv):
NFRA_PYFIELD's blocking remedy is hand-classification at CRO; yours is an implementation lane here.
One remedy does not move both. Fusing them would make the faster wait on the slower for no mechanical
reason.

1. **ONE VOCABULARY, ONE REGISTRY.** PYFIELD's `props` must carry the same seven keys as the portal
   producer (`srcField`, `dstField`, `kind`, `rename`, `condition`, `via`, `resolution`) — the PRD
   makes *"the two substrates are one schema"* its contract. **Your half: the per-group detection calls
   read the RATIFIED term registry (`comp-estate --definitions` / SYSTEM_DEFINITIONS), never a
   hardcoded list.** Otherwise a PYFIELD value is invisible to the semantic-evolution loop the day it
   lands, *and the loop's silence reads as "nothing changed."*
2. **PYFIELD IS A CORPUS STRATUM FOR YOU — ONE-DIRECTIONAL.** You compile changed resources at
   RESOURCE grain; PYFIELD produces FIELD grain on exactly the substrate where Andrew's stated use
   case lives (*"when we do migrations it will be essential to be able to track field dependencies in
   pipelines"*). **"If I change this field, what breaks downstream" IS a semantic-evolution question.**
   PYFIELD feeds you; you do not feed PYFIELD. That directionality is what lets both run concurrently.
3. **THE COLLISION, named so it is not ratified by accident.** You PROPOSE semantic changes and Andrew
   ratifies them as NAMING ACTS. **A proposal that renames a PYFIELD-emitted prop key is NOT a naming
   act** — it is a schema change to a live producer, and it breaks term (1) across two substrates. The
   proposal stratum must classify those separately, or the loop will eventually ratify a rename that
   silently un-joins portal from python.

---

## 3. ⭐ YOUR COVERAGE CONTRACT IS NOW LOAD-BEARING FOR A SECOND WORKSTREAM

**RULED (base CTO, adopting COO's rung-2 finding): C3.ii semantic-vertical generation REUSES your
subdivision coverage contract rather than deriving its own.**

Andrew described C3.ii as *deterministic → AI inferential → human review*. That is byte-for-byte your
architecture: deterministic compile with no model → per-group detection calls → Andrew ratifies. **Two
corpora, one pipeline pattern.** Your layout already solved the hard part — `calls_planned` known
before any call fires, `calls_succeeded`, `calls_failed[]`, `groups_absent[]`, and the explicit split
between **a group that RAN AND FOUND ZERO** and **a group that FAILED**.

**So the thing you flagged to me as the architectural question — "subdivision converts the AI half from
a BINARY into a FRACTION" — is now the more important half of your work, not the interesting half.**
`ai_section: PRESENT` over a run where 5 of 7 calls succeeded rebuilds `degraded_sources: []` one
layer up. A second workstream is about to depend on you having got that right.

`4.0.0_SA_CRO` builds C3.ii, inheriting `1.0.0_SA_CTO~C`'s `NFRA_VERTHARVEST_SPEC_20260807.md`. They
read your contract; **they do not wait for you.** No gate in either direction.

---

## 4. BUILD ORDER — unchanged, and I am explicitly endorsing your reasoning for it

Your order stands: **scope correction → D canon entities → Call 0 → waves**, per Andrew's §7 param-2
amendment. You declined to build the call waves first *"even though they are the interesting part,
because building mechanism against subjects that still carry `area:*` fallback names reproduces the
rejected-proposal class at a larger scale."* That is correct and I am not second-guessing it.

**COMPLETION TEST (COO's, adopted verbatim — a test, not a signature):**

> ONE UNATTENDED 13:00Z FIRE emits `ai_section` whose `ai_coverage` carries `calls_planned` /
> `calls_succeeded` / `calls_failed[]` / `groups_absent[]`, **AND at least one group demonstrably
> reads RAN-AND-FOUND-ZERO as distinct from FAILED.**

Not "code written." Not "deployed." Not "a fire succeeded." **On-track signal, pre-deploy and with no
vendor egress: the MUTANT — force one group to fail and prove `groups_absent` and `calls_failed`
separate.** Runs against a monkeypatched `urlopen` exactly as your vetoed commit's 25/25 battery did,
so it is available before anything ships.

---

## 5. B6 — genuinely open, and it is a DIFFERENT corpus from §1

`.tools/estate-capture.py` works (fail-closed, corpus-measured) but has **no S3 upload code**; the
writer IAM role is live; **zero text-input keys have ever existed.** That is the *text-input* stratum,
not the changed-path corpus — which is why §1's corpus is healthy and B6 is still empty. It is
**unowned and not assigned to you.** Do not absorb it; if your subdivision design depends on that
stratum existing, say so and it routes.

---

## 6. STANDING CONSTRAINTS

- ⛔ **NO alert, alarm, SNS, SES, freshness checker or monitor.** Standing moratorium (2026-07-28).
- ⛔ **NO shadow / parallel / comparator channel.** Andrew's complete veto: *"we simply do something
  correctly the first time and port over."* Build-time correctness + rollback, direct port.
- **NEVER#6:** verify against the SERVED artifact, never a producer self-report or rc=0.
- **Rule 21 CHANGED TODAY:** `comp-find` has REPLACED `comp-grep`/`comp-glob` (`@a3a9df7911`,
  Andrew-direct *"(A) lift it"*). Content bare, filenames behind `--name`. The old binaries still run;
  nothing routes to them. ⚠ **comp-find counts LINES, not AST nodes** — do not quote its count as a
  node denominator.
- **The `-target terraform destroy` finding you carried me** (a destroy leaves the DECLARATION behind)
  is still standing and still yours.

## 7. WHAT I OWE YOU BACK

Your two self-reports from the closed session are ACCEPTED and CLOSED — the rolled-back KIMI_TIMEOUT
deploy and the retracted "ARCHITECTURE GATE" framing. **Both were caught and corrected by you, in
public, inside an hour.** I am not re-litigating either. The banked lesson stands on its own:
*a correct mechanism analysis is seductive because it is correct* — you and CVO hardened a call the
approved spec already retires, and neither of you asked whether it was a call we keep.

**That question — is this a call we keep? — is the one thing I want you to ask out loud at each build
step, and it is the reason your layout came to me before any code existed.** Keep doing that. It does
not need my answer to be worth asking.

---

**Grounding:** live `aws scheduler get-schedule` + `s3 ls`/`cp` on `opal-estate-report` (2026-08-07
~15:1xZ, this seat) · `manifest/2026-08-07.json` read whole · `docs/architecture/NFRA_PYFIELD_PRD.md`
v1.0 · TO-0 close `@7a5be4b4c7`, TO-1 authored `@f6418f78e7` · `KIMI_SUBDIVISION_CALL_LAYOUT_20260806.md`
`@e433481cb` · COO seam ruling + completion test, 2026-08-07 145240Z.
**Not exercised by me:** I have not run your layout, not invoked the runner, and not read the
subdivision spec `@58505c291` beyond §8's disposition. The §1 corpus figures are measured; everything
about your design is carried from your own record.
