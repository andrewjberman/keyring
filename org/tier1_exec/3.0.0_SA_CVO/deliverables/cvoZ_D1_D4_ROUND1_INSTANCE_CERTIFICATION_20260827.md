# CERTIFICATION — `D1_NAMEDISCOVERY` + `ETFS_SATELLITES` ROUND-1 PROOF INSTANCES

**Certifier:** `3.0.0_SA_CVO~Z` · 2026-08-27 ~18:3xZ
**Instances (certified objects):**
`ETFS_SATELLITES.TO-1` / `TO-2` @`7f44de8371` (`0.4.0_DS_ClientPlatform~W`)
`D1_NAMEDISCOVERY.TO-1` / `TO-2` / `TO-3` @`39fb2289bb` (`0.4.0_DS_ClientPlatform~Q`)
**Cert commit:** resolve with `git log --diff-filter=A -- <this file>`
⛔ **The hash on a certification's face names the object certified, never the certificate.**

---

## VERDICT: **BOTH SETS CERTIFIED.** 24 criteria, 0 violations, every control fired.

---

## 1. THE CHECK THAT MATTERED MOST TODAY, AND IT PASSES

Both decomps were **corrected mid-flight** this afternoon — `SAT-inv-2`'s falsified wording was
amended on its normative line, and D1's `R-n1`/`ND-d-1` were repaired after my F1. **The live risk was
that a build team had already read the pre-correction text.** Measured:

| instance set | `decomp_ref.vintage_commit` | what that commit IS |
|---|---|---|
| `ETFS_SATELLITES` TO-1/TO-2 | `936b9ae1e9` | **the SAT-inv-2 amendment ON the normative line** |
| `D1_NAMEDISCOVERY` TO-1/2/3 | `669e04f27b` | **the D1 F1/F4 repair (`ND-d-1` = SET, not scalar)** |

Both resolve, both are ancestors of HEAD; a fabricated hash does not resolve (negative control).
⛔ **Neither team built against a falsified artifact.** The correction reached the builders before the
build did — which is the entire point of amending the normative line rather than appending to a
review section.

⭐ **And `0.4.0_DS_ClientPlatform~W` built the maintainer slot exactly to the ruling**:
`MAINTAINER_STATUS` carries *"not a build gate"*, and the test **ASSERTS THE STATE without enforcing a
gate.** That is the distinction between recording an open sovereign call and manufacturing friction,
and it was the easiest thing in this whole chain to get wrong.

## 2. INDEPENDENT INSTRUMENT RUN, WITH ITS CONTROLS

Re-run at this seat — **not accepted from the instances** — positional form, rc captured before any
pipe:

```
ETFS_SATELLITES.TO-1   rc=0  rows=4  violations=0  VALID
ETFS_SATELLITES.TO-2   rc=0  rows=5  violations=0  VALID
D1_NAMEDISCOVERY.TO-1  rc=0  rows=5  violations=0  VALID
D1_NAMEDISCOVERY.TO-2  rc=0  rows=4  violations=0  VALID
D1_NAMEDISCOVERY.TO-3  rc=0  rows=6  violations=0  VALID
                             ---- 24 criteria, 0 violations ----

CONTROL  bogus criterion id   -> rc=1, violations=5, INVALID      (the zero discriminates)
CONTROL  2-arg form           -> rc=0 printing COVERAGE UNCHECKED (a MEANINGLESS zero)
```

⛔ **The second control is the one that matters here.** This estate has banked that
`proof-of-spec-check` passes a placeholder row and that the 2-arg form returns `rc=0` while checking
no coverage at all. **Every rc=0 above came from the full positional form**, and both build seats
stated the same distinction unprompted in their own reports.

**Structural completeness, per instance:** all 24 rows carry a non-empty `criterion_verbatim`,
`invocation`, `output_evidence` **and `denominator`**. Zero empty fields across the set.

## 3. MY FINDINGS ARE DISCHARGED — **EXERCISED**, NOT MERELY ROUTED

D1 `F2` and `F3` were LIVE at certification and routed into the round-1 cut. They are now **in the
acceptance evidence**, which is a stronger state than "carried in a TO":

```
TO-2 evidence   crosswalk (1) · modelPortfolioColors (1)   <- F2's resolution surfaces, named
TO-3 evidence   843d875b (6) · Pathfinder (4)              <- F3's specimen, exercised
```

**`D1 F2` and `D1 F3`: DISCHARGED.** F1 and F4 were discharged earlier at `669e04f27b`.
**All four D1 findings are now closed.**

⭐ And `0.4.0_DS_ClientPlatform~W` independently hit F2's failure mode on the D4 side:
`CANONICAL_MODEL_NAME` is keyed **without** the `Opal ` prefix that every constituent name carries,
and `resolveCanonicalModelName` returns an unknown string **verbatim by design** — so the join yields
a plausible non-book key, **no error**, and an empty result reading as *"no weights"* rather than
*"the key did not match."* **I raised F2 as a letter-vs-principle argument with no instance two hours
earlier; they found the instance on a different project without working D1.**

## 4. ONE OBSERVATION, NOT A FINDING — **METHOD MONOCULTURE**

```
ETFS_SATELLITES   9 of 9 rows   method = test_suite
D1_NAMEDISCOVERY 15 of 15 rows  method = command
```

Within each set **every criterion rests on one instrument class**, so a defect in the harness itself
would fail all rows of that set together and the `violations=0` would not move. **This is not a
defect and it does not qualify the verdict** — each TO carries 2 declared controls, the two sets use
*different* instrument classes from each other, and criteria of one kind legitimately share a runner.
**Recorded because "24 of 24 PASS" reads as 24 independent confirmations and it is closer to two.**

## 5. WHAT I AM NOT ASSERTING

- **No served-artifact claim.** I certified the instances and their alignment, not that anything
  renders or serves. `ETFS_SATELLITES` remains a portal-only build not yet shipped.
- **I did not re-execute the builds.** Re-running certified producer work is a rewind, not a
  verification.
- **The `denominator` fields were checked for PRESENCE and non-emptiness, not re-derived.** Naming
  that as a scope limit rather than implying I re-measured 24 denominators.

## 6. ⛔ AN INSTRUMENT ERROR OF MINE, DISCLOSED BECAUSE IT NEARLY BECAME AN ACCUSATION

My first reader over these instances reported **"9 of 9 rows: evidence length 0, no cell refs,
THIN/PLACEHOLDER."** That was **entirely an artifact of my own guessed field names** — the schema uses
`criterion_verbatim` / `invocation` / `output_evidence` / `denominator`, and I had looked for
`evidence` / `cell_refs`.

>> **Had I reported it, I would have accused a seat of filing nine placeholder rows when they had
   filed 1,500-character evidence blocks.** What caught it was dumping one row verbatim instead of
   trusting my own reader. **Third time today an instrument of mine was the defect** — the others
   being a line-anchored grep that read 0-of-27 as a true absence, and a carrier-lag pattern whose
   strict form missed a known positive. <<

**The transferable half:** a reader that finds *nothing* in a structured artifact should be suspected
before the artifact is. **An empty result from a wrong field name and an empty result from an empty
field are byte-identical**, and only the first is common.

— `3.0.0_SA_CVO~Z`
