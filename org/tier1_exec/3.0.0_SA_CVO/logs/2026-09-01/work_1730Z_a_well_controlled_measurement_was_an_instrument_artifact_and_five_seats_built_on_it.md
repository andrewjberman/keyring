# CVO delta 2026-09-01 12:05Z - 17:30Z -- a well-controlled measurement turned out to be an instrument artifact, a seat owned a production regression on someone else's error, and Andrew named the tool that caught it twenty minutes early

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE

Delta since `work_1205Z_two_sets_nobody_had_counted...md` @`4e20c99083` (ON origin, is-ancestor with a
fabricated-sha negative control). Zero commits by this seat until this log; the work was adjudication,
source and artifact verification, one root-cause find, and **four retractions of my own**.

---

## 1. ⛔⛔ THE SESSION'S LARGEST REVERSAL: A FALSE DENY THAT FIVE SEATS BUILT ON

```
  raw `aws simulate-principal-policy`, no context
     s3:ListBucket on opal-data-49financial  ->  implicitDeny
  comp-iam simulate, SAME role/action/ARN
     decision=implicitDeny
     missingContextValues=['ec2:ResourceTag/ManagedBy','cloudwatch:namespace','s3:prefix']
     VERDICT: CONDITIONED-UNEVALUATED -- "This is NOT a deny verdict"
  ... --context s3:prefix=string:gold/advi/     ->  decision=allowed
```
**Verified at this seat on both arms.** ⛔ **The role could always list. There was never a permission
gap** -- and on that false premise a grant remedy was scoped, and **`0.4.0_DS_ClientPlatform~G` owned a
PRODUCTION REGRESSION within minutes, unsoftened.**
>> **THREE BANKED RULES FIRED AT ONCE.** A positive control bounds UNDER-firing, never OVER-firing --
two controls fired and were cited as conclusive, and were **structurally incapable** of catching a
conditioned false-deny. A self-attribution is the least-audited claim in the fabric -- **nobody was
going to audit it BECAUSE it cost that seat something.** And Rule 21 routes raw-`aws` INSPECTION to the
comp rail; **the hook did not fire and the rule binds by reading.** <<
⭐ **ANDREW-DIRECT ~14:3xZ, VERBATIM: *"remember comp-iam when checking these things."*** Recorded
@`bfa3660361`. **It named the instrument that caught this, twenty minutes before it was caught.** The
wrapper adds exactly one thing over the raw call: it reads `missingContextValues` and refuses to render
a conditioned-unevaluated result as a deny. **The difference is not the answer -- it is whether the
answer knows what it did not evaluate.**

---

## 2. ⛔ MY OWN FOUR RETRACTIONS, AND THEY SHARE ONE SHAPE

```
  91801  "THAT IS THE 6-TO-0"          an 11:06Z PUBLISH of 7 keys is not a CHAIN run of 11 families
  91879  "the prediction is FALSIFIED" the run was the LAPTOP -- C:\Users\AndrewBerman traceback in
                                       rows[].error. The principal caveat I NAMED was the operative fact
  91817  "the coverage question is     I marked the evidence RELAYED and still drew a MEASURED
          CLOSED"                      conclusion from it
  92011  "not reachable from this      true of the MANIFEST, wider than my search, which covered only
          seat"                        local filesystem paths
```
>> **STATING A CAVEAT IS NOT RESPECTING IT. Twice the bound I wrote down was the exact fact that undid
the headline** -- and you name the bound because some part of you already knows it is load-bearing. <<
⛔ **AND THE DEEPER ONE: I PICKED THE WRONG BRANCH FROM THE RIGHT EVIDENCE.** Three families built
pre-fix despite the "denial"; I concluded *"a second factor is in play"* and **never named "the
measurement is wrong."** There was no first factor. **The estate spent an hour reconciling a tension my
framing kept alive.** Banked at
`feedback_when_evidence_contradicts_a_measurement_the_measurement_is_a_live_branch.md`.

---

## 3. ⭐ THE ROOT CAUSE I DID FIND, FROM AN ARTIFACT ALREADY WRITTEN

`_manifests//4b36d4f5743c.json` -- **note the DOUBLE SLASH:**
```
  "asof": ""      -> eligible = [d for d in dates if d <= ""]  is ALWAYS EMPTY
  emitter_tail: "REFUSED: fact_uln has no partition at or before  (its 541 span 2024-07-08..2026-08-31)"
                                                              ^^ nothing between "before" and "(its"
```
**541 healthy partitions, named in the refusal, and every family refused.** ⛔ **`required=True` on
`--asof` FORBIDS OMISSION AND ACCEPTS `""`** (`0.4.0_DS_ClientPlatform~G`, `:506`) -- **a presence gate,
not a validity gate** -- and `:614` mints the manifest key from the same empty value, so **the double
slash is DERIVED, not a curiosity.** ⭐ **I read the ARTIFACT; that seat read THE CODE THAT MINTS IT.**
⛔ **And it explains the PUBLISH path only. The chain's 6-to-0 remains uncaused** -- the chain LOGS and
PASSES one binding (`:494` print, `:365` argv, `:540` call site), so it passed a real date.

---

## 4. THE REASONS WERE NEVER EMPTY -- THREE CARRIERS, NO CONSUMER READS ALL THREE

```
  the chain log's `reason` field    renders  -           <- a ruling was taken on THIS
  the manifest's `emitter_tail`     the full REFUSED text
  the manifest's `error`            a raw Python traceback (and it names the HOST filesystem)
```
⛔ **`1.0.0_SA_CTO` ruled UNMET-PRECONDITION on eleven blank `reason` fields and withdrew it: *"I read
ONE FIELD of ONE CARRIER and concluded ABSENCE."*** ⭐ **And `error` doubles as a BOX DISCRIMINATOR** --
`C:\Users\...` = laptop, POSIX = EC2 -- **which is how the 07:27Z run was identified as laptop-run and
my falsification collapsed.**

---

## 5. ⭐ TICK 110 CALL 1 REACHED EIGHT INSTANCES, AND ONE IS THE WORST YET

`chain_49f_entrypoint.py:406` -- **any non-zero rc becomes `emitter_refused`, and `emitter_refused` is
EXCLUDED from `hard_fail`.**
>> **ELEVEN BY-DESIGN REFUSALS AND A TOTAL FAILURE OF ALL ELEVEN PRODUCE BYTE-IDENTICAL STAGE OUTPUT
(`STAGE OK rc=0 hard_fail=0`), and the reassuring prose is printed UNCONDITIONALLY.** *"A line that
cannot be false is not evidence, and this one was doing active harm."* <<
**That is why the regression was undetectable from any single run and surfaced only by comparing ACROSS
DAYS.** Four seats had that log open.

---

## 6. ADJUDICATIONS AND CENSUSES DELIVERED

| item | verdict |
|---|---|
| tick 117 CALL 1 (AC11 ride-or-detach) | **RIDE** -- `PRF-inv-3` claims rollup CORRECTNESS, verified at source; CTO's own flip condition fails |
| tick 117 CALL 2 (serve-release intent) | **ADJUDICABLE** -- Andrew's verbatim is about CREATING GATES from a stop-word; nothing here relays a word. **Limb (a) bounds the REMEDY: rule the semantics, propose the gate** |
| the `canon-json-v1` ruling | **PASS.** Carrier 6 verified at source: 2026-08-11, **nineteen days before the ruling that got it wrong** |
| V-4 on c02-VINTAGEDIGEST | **MET**, amendment verified additive (0 status/criterion/id lines touched) |
| the PENDING-EXPIRY second condition | **~4 flip of 139**, not 139 -- 109 of 113 stay ANNOUNCE regardless |
| the artifact-resolution arm | **104 of 282 STANDS** -- ungated, no second condition |

⭐ **And a scheduler-plane census resolved two "missing" resources**: `advi-49f-gold-floor`
`cron(45 12)` ENABLED **is** the 12:45Z fire, and `advi-49f-publisher` **exists** and is DISABLED --
**so AC4's instrument needed no re-point and an issuer act left the queue.**

---

## 7. Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| `comp-iam simulate` | 2 | **PASS** | the Andrew-named instrument; caught what raw simulate cannot |
| `aws s3 cp` manifest reads | 6 | **PASS** | the cheapest instrument in the session -- root cause from an artifact already written |
| `aws scheduler` | 3 | PASS | the plane a Rules census cannot see |
| `python ast` equality | 1 | PASS | comment-only verified with a discriminating control |
| `sed`/`grep` source reads | 14 | PARTIAL | one **line-range** check was the WRONG INSTRUMENT -- a function body is not linear with its caller |
| `find` for chain artifacts | 1 | PASS | bounded negative, `/tmp`-cleanup confound named |

**What worked:** reading artifacts that already exist. Three seats were preparing to spend chain runs on
a cause legible in a manifest.
**What failed:** four of my own claims (s.2), each a conclusion wider than its stated bound.
**Gap found:** `comp-iam`'s population is LAMBDA entry points -- **the EC2/SSM gold chain is outside it
entirely**, so a permission defect from a code change is invisible to the sweep built for exactly that.
⭐ `comp-iam gaps` **would** have caught this the moment the fix landed. Routed to `1.0.0_SA_CTO`.

---

## 8. Current State

- **The chain's 6-to-0 has NO surviving cause.** The fix, the invocation, the empty asof, the staging
  flags, and the IAM denial are all dead. `2.0.0_SA_COO` ruled **no new causal story until a measurement
  of what the chain run actually did.**
- ⛔ **"The 09:46Z run" NAMES TEN SSM INVOCATIONS IN SEVENTEEN SECONDS** with at least three distinct
  outcomes (7 live-lock refusals, one a00 abort at 1.7s, at least one reaching `perfrp_projection`).
  **Every claim of that form now needs an invocation id.**
- **The IAM grant is REVOKED and must not be re-evidenced** -- three seats confirmed from three directions.
- ⭐ **The chain's stdout IS reachable off-box via SSM RunCommand retention** (`0.7.0_AE_CloudOps~M`),
  host stopped -- but it carries the CHAIN's stdout, not the emitter subprocess's, so it does not close
  the 6-to-0.
- **`2.0.0_SA_COO` is LIVE** (my "still down" at 13:1xZ was a re-assertion without a re-read).

## 8a. LATE ADDENDUM (17:3x-17:4xZ) -- A SIXTH HYPOTHESIS LIVED AND DIED INSIDE FIFTEEN MINUTES

**Andrew, verbatim, relayed by `1.0.0_SA_CTO`: *"8/28 is Friday, it is the last day we have data" /
"because its the last trading day" / "prior to today."*** ⛔ **This is CLAUDE.md's trading-calendar
NEVER — *FRIDAY IS MONDAY'S ANSWER* — and five seats ran an afternoon without invoking it.**
**Then it died as an explanation, correctly:**
```
  09:46:26Z  invocation e74c9108  fact_acc: have 08-26,27,28  -> ABORT stage 1 of 17, 1.7s
                                   perfrp NEVER RAN in this invocation
  09:46:39Z  THIRTEEN SECONDS LATER  fact_acc date=2026-08-31: 7,379 rows READ
```
**The 08-26/27/28 enumeration is a PREMATURE-RUN SNAPSHOT, not a standing boundary — the partition
landed in the intervening thirteen seconds.** ⭐ **Andrew's FACT stands and has a VINTAGE; the
inference drawn from a later abort line does not.** `1.0.0_SA_CTO` scoped that retraction correctly.
⛔ **AND I HAD THE DIRECT REFUTATION IN MY OWN 92011 s.3** — `canonical_valuation` and `flow_ledger`
both listed `date=2026-08-31` in my own output — **and argued from the resolver's date policy instead.
Third seat in one afternoon whose refuting line was in a message it had already written**, and the
remedy for it is the one I banked at 13:0xZ and did not run.

## 9. Blockers

**No CVO-owned blocker.**
- the 6-to-0 measurement -> needs the chain's LOCAL manifest; the host is **stopped**, and an instance
  start is a state change nobody has authorized.
- `comp-iam` population scope -> `1.0.0_SA_CTO`.
- **AT ANDREW, unchanged:** per-date flow-ingestion scoping · D3-vs-D8 ordering · `--enumerate`
  certification · **and the PERFRP two-carrier question reserved at 91668.**

## 10. Next Steps

1. **[whoever takes the read]** the invocation id that reached `perfrp_projection` -- s.8 makes the
   timestamp ambiguous.
2. **[1.0.0_SA_CTO]** CALL 1's disposition, now at eight instances including the `hard_fail` exclusion.
3. **[3.0.0_SA_CVO]** adjudicate ticks; do not offer a causal story under the standing ruling.
