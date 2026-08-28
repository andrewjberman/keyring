# CERTIFICATION — `ETFS_SATELLITES.TO-7-AE` (the scoped satellites route)

**Certifier of record:** `3.0.0_SA_CVO~Z` · **Issued:** 2026-08-28T02:5xZ
**Executor:** `0.7.0_AE_CloudOps~S` · **Issuer:** `2.0.0_SA_COO~Z` · **Report:** msg 12286
**Instance (certified object):** `org/tier2_senior/0.7.0_AE_CloudOps~S/deliverables/ETFS_SATELLITES.TO-7-AE_PROOF_OF_SPEC.json` @`2795da3de9`

---

## VERDICT: **CERTIFIED. 7 of 7 PASS, and the coverage the checker could not assert is verified here.**

---

## 1. ⛔ THE CHECKER HANDED ME TWO THINGS IT EXPLICITLY CANNOT ASSERT, AND BOTH ARE THE CERT'S JOB

Run at this seat, `VALID`, 7 acceptance rows, **0 violations**. But it printed its own limits, unprompted:

> *"no `expected_criterion_ids` given — **COVERAGE UNCHECKED** (row quality only; **an omitted criterion is invisible to this run**). The cert consumer runs step-zero."*

> *"this closes the TO against ITSELF and against the decomp's id space. Whether the TO's declared set
> IS the decomp's complete criterion-bearing set is **a CVO cert judgment (enforcement layer 5), NOT
> asserted here**."*

**A tool that names the question it is not answering is worth more than one that returns a bare PASS** —
and the coverage limb is precisely where a certification goes hollow if nobody runs it.

### STEP-ZERO, RUN AT THIS SEAT
```
TO declares      T7AE-AC0 · AC0b · AC1 · AC2 · AC3 · AC4 · AC5     = 7
Instance files   T7AE-AC0 · AC0b · AC1 · AC2 · AC3 · AC4 · AC5     = 7, all PASS
                 IDS IDENTICAL, SET-FOR-SET. No omitted criterion.
```
**COVERAGE COMPLETE.**

### AND THE "2 OF 27" IS BY DESIGN, NOT A GAP
`alignment-forward-2` resolved **2/2** distinct cell_refs against a decomp id space of **27**. That is
correct: the TO's `<decomp_ref>` declares exactly **`SAT-a-4`** and **`SAT-c-2`** and states **"NO new
cell."** Its `<certification>` records that this seat's own lineage certified the decomp and that
`SAT-a-4` was **left explicitly open for the issuer to close** — which this TO does. Two of
twenty-seven is the declared scope, and I checked that rather than reading a low ratio as a shortfall.

## 2. ⚠ ONE PRECISION CORRECTION TO THE REPORT — the coverage holds, the citation did not

msg 12286 §1 states *"`expected_criteria` is 7; filed rows are 7."* **The instance's `expected_criteria`
field reads `None`** — which is exactly why the checker printed COVERAGE UNCHECKED.

The **claim is true** (the TO does declare 7) and the **citation is wrong** (it is not backed by the
field named). I verified the denominator from the TO itself, so nothing rests on the mis-citation.
⭐ Recording it because a true conclusion resting on a field that does not exist is the shape that
survives review — nobody re-checks a number that turned out right.

## 3. WHAT THE EXECUTION DID THAT I AM CERTIFYING AS METHOD

- **AC3's row is another seat's measurement and SAYS SO.** The APPLIED half is the executor's; the
  EXERCISED half is `0.4.0_DE_ClientPlatform~S`'s @`80f42be356`. **They did not re-run it** — *"re-running
  a peer's command is repetition, not corroboration, and the criterion is discharged by the measurement
  rather than by who typed it."* Rule 22 applied to **attribution**, which is the direction it is
  usually forgotten in.
- **AC4/AC5 argued by STRUCTURAL IMPOSSIBILITY, not by behaviour.** The router constructs statuses
  `['204','400','401','403','404']` — **no 200** — and contains no `books` / `as_of` / `schema_version`
  at all, so it *cannot* synthesise an empty set from a refusal nor strip an `as_of`. **Positive
  control:** the same probe finds `statusDescription` / `status` / `error` / `Not Found` / `401`, so the
  ABSENCE is a finding rather than a dead probe. A structural argument beats a passing test.
- **Two stale sentences corrected by AMENDMENT, not silent edit.** The ledger header and one evidence
  line said AC3's authenticated half was outstanding — true when written, false now. *"A ledger that
  silently rewrites its own history is worse than one that shows the correction."*
- **The other seat's finding carried AS THEIRS, with its bound verbatim:** the `opal-capital` 400 is
  **not evidence about the cottonwood path in either direction**. A measurement on one path is not
  evidence about a sibling path, and saying so in *both* directions is what keeps it honest.

## 3a. ⭐ ADDENDUM 02:54Z — `T7AE-AC2`'s EXHIBIT LIMB IS NOW DISCHARGED, AND IT TESTS WHAT THE FORGED CLAIM COULD NOT

`0.4.0_DE_ClientPlatform~S` took the free half my 12277 §5 ruled for, using the **committed
`49financial`** credential — **real, and issued by the live auth layer**, so it exercises **ISSUANCE AND
RESOLUTION TOGETHER**, forging nothing:

```
NEGATIVE  49financial -> /api/scoped/satellites/registry.json
          403 {"error":"artifact_forbidden","firmId":"49financial", ...}
POSITIVE  same bearer -> its OWN advisor-intelligence route
          200, 1919 B
```

**ARM 2 IS WHAT MAKES ARM 1 MEAN ANYTHING.** A 403 from a dead, expired or malformed bearer proves
nothing about a boundary; the *same* bearer returning 200 where the firm IS entitled shows the token is
live and accepted, so the 403 is a **real refusal of a real, authenticated, non-entitled caller**. And
cottonwood's bytes were compared **by sha256**, not inferred from the status code.

⛔ **AND THIS IS THE BETTER TEST OF THE BOUNDARY THAN THE COTTONWOOD CALL WOULD HAVE BEEN — I priced my
own §5 too low.** A firm boundary's job is to **REFUSE THE WRONG FIRM**, not to serve the right one. A
cottonwood success would exercise the happy path; this exercises the property the boundary exists to
provide. The "free half" was not a consolation for the rung I declined — **it was the load-bearing arm,
and the expensive option would have tested the less important direction.**

⚠ It does **NOT** establish that a cottonwood caller succeeds. That rung stays OPEN and honestly
labelled. Two different claims; one measured.

## 3b. ⛔ A BOUND ON THIS CERTIFICATION, STATED BECAUSE THE ADDENDUM EXPOSED IT

**My §1 verdict verified SCHEMA VALIDITY and COVERAGE. It did NOT audit each row's evidence quality.**
I checked that seven declared criteria were seven filed criteria with identical ids, and that the
checker's own unasserted limbs were closed. **I did not re-derive what any individual row's evidence
actually shows.**

That is a legitimate certification scope and it is the one the checker's step-zero note describes — but
it is narrower than "7/7 PASS" reads, and this addendum is the proof: `AC2`'s exhibit limb was
strengthened *after* I certified it, by a measurement I had not seen. **A reader must not take this
certificate as an audit of every row's substance.**

## 3c. ⛔ ADDENDUM 03:03Z — `T7AE-AC1`'s DENOMINATOR IS BLIND TO IN-PLACE CHANGE. VERDICT UNCHANGED; THE QUALIFIER LIVES HERE.

`0.7.0_AE_CloudOps~Y` verified the apply with the **same instrument and argv** as their pre-apply read
— which is what makes the two comparable — and found:

> *"'Exactly one added' and 'four re-pointed' were BOTH TRUE OF THE SAME APPLY. The counting control
> could not have seen the re-point."*

`AC1`'s denominator reads **27 behaviors post-apply vs 26 pre = exactly 1 added of 1 intended.** True
about **ADDITIONS**, and **structurally blind to an in-place change**: four existing behaviors moved
`:24 -> :25` and a cardinality check cannot see it. **A reader could take "exactly one added" as
"nothing else changed." It does not say that, and it cannot — a cardinality check answers HOW MANY,
never WHICH ONES.**

### THE VERDICT DOES NOT CHANGE, AND I AM NOT RE-OPENING THE INSTANCE
`AC1` is PASS **on its own subject** — the route exists, is scoped, and the MODELS/ETFS payloads did
not move. Nothing is mis-scored, the denominator was never wrong, and the four re-points were
**disclosed PROSPECTIVELY** in the deploy ledger, which states the apply *"ADDS the behavior **and
re-pins existing behaviors to the new qualified_arn**"* and pre-explains the `lambda_arn "...:24" ->
null` lines so nobody reads them as unwiring. The prediction was written before the act and the
verification confirms it exactly. **Re-opening a certified artifact to widen a denominator that was
never wrong is churn against a live "pure execution" instruction.**

### ⛔ BUT THE QUALIFIER DOES NOT BELONG IN A BROKER MESSAGE, AND THAT IS MY CORRECTION TO THE DISPOSITION
`0.7.0_AE_CloudOps~S` proposed *"this message is the carrier for the qualifier."* **A broker message is
the weakest durable carrier this estate has, and tonight's whole catalogue is stale carriers.** The
disclosure lives in the ledger; the blind denominator lives in the certified instance; **the two are
different documents and the shorter one is what gets quoted.**
>> **SO THE QUALIFIER GOES HERE, IN THE CERTIFICATE** — the artifact a later reader consults for the
verdict. Amending my own record costs nothing, reaches the right reader, and requires the executor to
re-open nothing. **The asymmetry is the point: the certifier can carry a bound the executor would have
to churn to carry.**

### ⭐ AND THE SIBLING ARM IS THE STRONGER EVIDENCE, AND IT IS NOT MINE
`shared-advisor-router-response` **gained the association and HELD AT `:5`** — it did not republish.
That is the positive control on *"only the changed artifact republishes."* The executor's own evidence
showed the satellites router moved, **which is consistent with EVERYTHING republishing**; this shows a
sibling that did **not**. Without that arm, "Terraform deploys the artifact, not the source" is an
argument; with it, it is a measurement.

### ⚠ AND MY OWN FRAMING PROPAGATED AN ERROR
I called the cottonwood call *"the last unexercised rung of Andrew's item 2."* What was actually
unexercised was **the HAPPY PATH**, with the security-relevant direction already measured — and
`0.7.0_AE_CloudOps~S` reports inheriting that framing and repeating it into their own record.
**A certifier's phrasing is adopted downstream faster than a certifier's caveats**, which is the
second time tonight this seat has watched a headline outrun its qualifier.

## 4. WHAT THIS CERTIFICATION DOES NOT DO

- Does **NOT** close `ETFS_POSITIONING-Z-S16` — staff still see a pill that 400s. The remedy fork spans
  the router and the mode allowlist and is the issuer's.
- Does **NOT** close the **cottonwood rung**, which remains INFERRED FROM SOURCE ONLY. My 12277 ruling
  stands: a self-signed firm claim would test the boundary by circumventing it.
- Does **NOT** touch `TO-6-AE`, whose AC3 fires 07:00Z on its own trigger.
- Does **NOT** close D4. Its bar is Andrew's smoke test.

---

— `3.0.0_SA_CVO~Z`
