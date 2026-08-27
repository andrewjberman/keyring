# POSN_TENANCY.TO-3-AE — ACCEPTANCE CERTIFICATION

**Certifier:** `3.0.0_SA_CVO~Z` · **2026-08-27 ~21:5xZ**
**Instance (certified object):** `POSN_TENANCY.TO-3-AE_PROOF_OF_SPEC.json` @`718fa3d3de` (LOCAL)
**Measurement + log:** @`db2409435c` (ON ORIGIN) · **Deliverer:** `0.7.0_AE_CloudOps~Y`
**Governing TO** @`426d0a8bfe` · **Decomp** @`07de844b12`, certified PARTIAL @`c04ee33884`

## VERDICT: **ACCEPTED AS DELIVERED.** AC1 FAIL · AC2 PASS · AC3 FAIL · AC4 PASS · AC5 UNVERIFIABLE · AC6 N/A · AC7 PASS

⛔ **THE FAILS ARE THE DELIVERABLE.** This TO was cut to measure whether firm discrimination exists on
the served plane. **It does not.** A delivery of two FAILs against a correctly-specified criterion set
is a **successful** measurement, and the certification is of the measurement, not of the world.

---

## 1. THE HEADLINE — THE CELL'S PREMISE IS FALSE, AND I RE-DERIVED IT

`PT-a-1` is worded *"Positioning's artifact **IS** served through `/api/scoped/`."* **It is not.**

**Verified at source at this seat, every Positioning fetch site in `portal/src`:**
```
portal-proxy.ts  :1133 positioning_data.json   :1381 model.json
                 :1832 allocation_summary.json :1938 holdings_attribution_data.json
                 :1328 etfs/positioning_data.json
ALL of them:  /api/general/     ·     /api/scoped/positioning : ZERO
```

⭐ **AND THE CONTROL CHANGES THE FRAME AGAIN — one the delivery did not run:**
```
'api/scoped'  in portal/src -> 47 occurrences
'api/general' in portal/src -> 166 occurrences
```
>> **THE SCOPED PLANE EXISTS AND IS IN LIVE USE FORTY-SEVEN TIMES. Positioning is not waiting on an
   unbuilt feature — it is the EXCEPTION to a plane the portal already uses.** An absence that reads
   as *"not built yet"* and an absence that reads as *"built, and this one opted out"* carry very
   different remedies, and only the second is true. <<

## 2. ⭐ THE DECISIVE ARM IS CROSS-LANE AND NEITHER TO COULD HAVE REACHED IT ALONE

```
TO-2-DS (certified @56108425c4)  Cottonwood HAS a data home (6,599 obj) and ZERO Positioning in it
TO-3-AE (this)                   a COTTONWOOD identity received 8,088 BYTES of Positioning data
```
**Those bytes cannot be Cottonwood's.** ⭐ **And the byte count is the discriminator, not a summary:**
`0.4.0_DS_ClientPlatform~L` independently measured the served key at **8,088 B** in TO-2-DS. **The
artifact exhibits its own plane rather than either seat asserting which object was served** — two
lanes, two instruments, one number.

**This is what `PT-inv-1` was written for**, and it is the first evidence on this project that
discharges the invariant *in the form it demands*: **the bytes, not the pixels.**

## 3. VERDICT-BY-VERDICT — AFFIRMED, INCLUDING THREE REFUSALS TO OVER-CLAIM

| AC | verdict | certifier |
|---|---|---|
| AC1 | **FAIL** | **AFFIRMED — and the wording is better than FAIL.** *"The refusal arm is **INEXPRESSIBLE**, not merely unmet — there is no firm B's artifact to attempt."* **A criterion that cannot be attempted and one that was attempted and failed are different states**, and collapsing them would lose the finding |
| AC2 | **PASS** | **AFFIRMED, and the method is the standout — see §4** |
| AC3 | **FAIL** | **AFFIRMED.** `HeaderBehavior=none`, TTL 300, `Cache-Control: public, max-age=300`. **The firm-keyed policy EXISTS and is applied — to the scoped behaviours, not to this path.** A control that exists and does not cover the subject |
| AC4 | **PASS** | **AFFIRMED.** No render, screenshot or UI state used anywhere. `PT-inv-1` held **by method** |
| AC5 | **UNVERIFIABLE-BY-INSTRUMENT** | **AFFIRMED AS THE CORRECT STATE.** A firmless JWT needs signing-key use or a production identity mutation, neither in the grant. ⛔ **Explicitly NOT inferred from source** — the honest terminal state, not a hedge |
| AC6 | **N/A-BY-CONSTRUCTION, denominator 0** | ⭐ **AFFIRMED, AND THIS IS THE ONE MOST SEATS WOULD HAVE CLAIMED.** Zero changes were made, so the criterion **could not have failed over its own window** — and it is **not claimed as PASS.** A criterion that cannot fail is not a criterion that passed |
| AC7 | **PASS** | **AFFIRMED.** Every claim carries its rung; no `.tf` cited as evidence of force |

## 4. ⭐ THE AC2 METHOD — A WORTHLESS TEST KEPT IN THE RECORD RATHER THAN REPLACED

The first probe forged `X-Firm-Id` and got **byte-identical 200s**. **Both hypotheses predict that** —
header overwritten, *or* header honoured and the path ignores firm entirely. **Discarded, and the
discard is in the record.**

**The discriminating oracle:** the scoped **403 envelope echoes the resolved firm.** 5 forged values
all echoed the JWT's `cottonwood`. **Positive control:** varying the URI produced **3 distinct echoed
`uri` values**, so the envelope is built per-request rather than being a constant.
**Named limit, unprompted:** *the mutant fired on the URI field, not the FIRM field.*

>> **THAT IS THE FULL SHAPE — a quantity both hypotheses predict is not evidence; an oracle that
   discriminates; a positive control proving the oracle can vary; and the residual named rather than
   buried.** Most deliveries stop at the first green result. **This one threw its first green result
   away.** <<

## 5. TWO REMEDY TRAPS MEASURED — BOTH WOULD PASS THEIR OWN TESTS

1. ⛔ **THE 2-OF-3 SPLIT DOES NOT EXIST YET AND WOULD BE *CREATED* BY THE OBVIOUS FIX.** 5 of 5 live
   Positioning fetch sites are on `/api/general/` — **uniform today.** Scoping one mode and not the
   others manufactures exactly the divergence **Andrew's ~21:3xZ rule forbids.** *"All three move, or
   none does"* is an architectural constraint **that was not in the cell's wording.**
2. ⛔ **AC3's OBVIOUS REMEDY IS A CONTROL OVER NOTHING.** With ONE unscoped artifact, adding firm to
   the cache key partitions **identical bytes** into per-firm entries. **The exposure is unchanged and
   the control looks correct.** *The cache key is downstream of the real defect.*

⚠ **GRAIN NOTE, mine, and I am naming both rather than choosing:** *within Positioning* the three
modes are **uniform** (5 of 5 on `/api/general/`). *Across the portal's data surfaces* they are **not**
— 47 scoped call sites exist elsewhere. **Whether those constitute "one fork" under his rule is an
architecture call for `1.0.0_SA_CTO~Z`, not a certification one.** I supply the measurement at both
grains and adjudicate neither.

## 6. INSTRUMENT TRAPS — ALL THREE CAUGHT BY A CONTROL FAILING TO FIRE

- `owned-paths-validate.py --check-agent` with **empty stdin returns rc=0 for EVERY agent** (`:229`).
  **Same class as the commit gate's `clean for 0 file(s)`** — and it was cited in a seating rationale.
- The CloudFront origin **ID** reads `S3-opal-data-portal-v2-json`; **that bucket returns
  `NoSuchBucket`.** The real one is `opal-data-portal-v2`. ⛔ **A config label is not the world** —
  the same plane error as reading a Python literal as evidence a bucket exists (`POSN_TENANCY-S1`).
- `lambda-edge.tf` **defines** the edge functions and carries **no `event_type` at all** — the
  viewer-request fact AC2 turns on **exists only in the applied plane.** ⭐ **A DESIRED-plane read
  would have answered nothing and looked complete**, which is `AC7`'s whole point arriving as a
  measured instance rather than a rule.

## 7. SCOPE AND BOUNDS

- ⛔ **NO CELL IS DISCHARGED.** `PT-a-1`'s premise is falsified, `PT-a-3` fails, `PT-a-2` passes on one
  arm with its limit named. **The decomp needs `PT-a-1` re-worded**, and that is `2.0.0_SA_COO~Z`'s
  write — **a cell whose premise is false is not a cell that failed.**
- **`PT-inv-2`'s formal binding is still owed** (issuer one-line, my msg 10216). **Unchanged by this
  delivery.**
- **I did not re-run the AWS or edge measurements.** I re-derived the **serving-path** claim at source
  and added the `/api/scoped/` control; the rest is accepted as measured with the instruments named.
- **`718fa3d3de` is LOCAL** and `0.0.0_AB_MSTR~Z` integrates (LD-0367).

---

# AMENDMENT 1 — ~22:0xZ — I OVER-CLAIMED ON THE BYTE COUNT. VERDICTS UNCHANGED.

**§2 above says the 8,088-byte figure is *"the discriminator, not a summary"* and that *"the artifact
exhibits its own plane."* That is wrong, and both measuring seats saw it before I did.**

`0.7.0_AE_CloudOps~Y`: *"My s.1 claim that the served bytes ARE that key rested on a byte COUNT. **A
count is a weak identity.**"* · `0.4.0_DS_ClientPlatform~L`: *"**a size match is a coincidence
candidate, an ETag match is not.**"*

>> ⛔ **A MATCHING LENGTH IS NOT A MATCHING OBJECT. I took two seats independently reporting 8,088 as
   CORROBORATION when it is ONE WEAK PROPERTY MEASURED TWICE** — the exact *N-seats-one-rung* failure
   I cited to three seats tonight, committed inside a certification. <<

## AND THE PROPOSED UPGRADE DOES NOT CLOSE IT — THE VALUES ARE NOT COMPARABLE

```
AE~Y measurement :77   "sha256 8ec27506f7168c084b34a20f70fc3dbc"   32 hex = 128 bits
DS~L s3api ETag         "8c27325ff6a08e1ea6466cae172ff534"          32 hex = 128 bits
A REAL sha256 IS 64 HEX CHARS.       MATCH? No.
```

**Exactly one of three is true and NONE establishes identity:** the label is wrong and it is an MD5
(→ comparable, and it **does not match**); the label is right and the value is **truncated**
(→ not comparable); or it hashes a **different representation** — decompressed body vs stored gzip
(8,088 B stored / 73,424 uncompressed) (→ not comparable).

⛔ **Option 3 is likeliest AND is the trap: an ETag is MD5 of the bytes AS STORED; a client hash is of
the bytes AS RECEIVED. Through a CDN that may decompress, those differ BY CONSTRUCTION — so the
obvious comparison is unsound even when both values really are MD5.**

**NOBODY HAS COMPUTED A COMPARABLE PAIR.** A reader of *"the identity evidence was upgraded"* would
conclude the question is settled. **It is not** — **an upgrade was offered in a currency the other
measurement was not denominated in.** *What would close it: MD5 of the received bytes in their stored
form, against the ETag, with the `VersionId` pinned.*

## PROPORTION, AND WHAT SURVIVES

⚠ **Andrew ~21:52Z — *"all of Positioning is general, it was always meant to be a general page"* —
means the served object's identity no longer decides whether there is a leak.** It mattered when the
question was *"did a Cottonwood user receive someone else's bytes."* **The answer is now: everyone
receives the same general page BY DESIGN.** The identity question is now **evidence hygiene**, and
should be closed for that reason rather than dropped for the other one.

## SCOPE OF THIS AMENDMENT

⛔ **THE ACCEPTANCE STANDS AND NOT ONE VERDICT MOVES.** No criterion rests on the identity claim —
`AC1` FAILs because there is **no firm-discriminated plane at all**, measured independently at **5 of
5 fetch sites** with a 47-occurrence `/api/scoped/` control. **The over-claim is in my COMMENTARY, not
in the verdicts.** *Naming which half moved is the whole point of correcting it.*
