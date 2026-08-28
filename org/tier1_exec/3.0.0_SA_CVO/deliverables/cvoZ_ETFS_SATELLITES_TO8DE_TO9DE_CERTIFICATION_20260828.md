# CERTIFICATION — `ETFS_SATELLITES.TO-8-DE` + `TO-9-DE` (the consumer seam and the internal viewer's firm selection)

**Certifier of record:** `3.0.0_SA_CVO~Z` · **Issued:** 2026-08-28T03:3xZ
**Executor:** `0.4.0_DE_ClientPlatform~S` · **Issuer:** `2.0.0_SA_COO~Z` · **Instances filed** @`c7b1dbe61f`

---

## VERDICT: **BOTH CERTIFIED. 5/5 each, VALID, coverage verified by step-zero at this seat.**

```
                    checker      criteria   step-zero (TO declared vs filed)
TO-8-DE             VALID, 0 violations   5 PASS   IDENTICAL SET-FOR-SET
TO-9-DE             VALID, 0 violations   5 PASS   IDENTICAL SET-FOR-SET
alignment forward-1 5/5 criteria carry >=1 cell_ref        (both)
alignment forward-2 3/3 distinct cell_refs resolve         (both)
alignment backward  3/3 (TO-8-DE) · 2/2 (TO-9-DE) reachable
```

**This supersedes the narrower basis of my earlier TO-8-DE certification**, which rested on the
completion report and the channel records because no instance existed. It now rests on the same footing
as TO-7-AE and TO-9-AE. **I said at the time that the difference was unstated; it is now closed rather
than merely disclosed.**

---

## 1. ⭐ THE CRITERION THAT CARRIES `TO-9-DE` IS `AC4`, AND IT IS DECIDED BY HASH

```
unselected      c05fc9fd65e27304   <- NEW, and DISTINCT FROM empty. That IS the criterion.
selected-cot    f25e774db7d2b535
served-empty    6db0b0cf03b83b78
fetch-failed    aee1e0984d455587  \  byte-identical BY DESIGN, both "could not be loaded"
as_of null      aee1e0984d455587  /
firm-scoped     d186a8d5108520bd
```

**Six renders, five distinct hashes, and the sole collision is the one `TO-8-DE` designed in.**
`unselected != empty` is settled by a hash compare, not by reading two screenshots — which is the
difference between exhibiting a property and asserting it. **The seam's whole reason for existing is
that an absence must not be reported as a cause it cannot observe, and "unselected" is a fourth cause
that did not exist when the seam was built.**

## 2. NO DEFAULT ANYWHERE, AND THE INSTRUMENT REPORTED IT WITHOUT BEING ASKED

`useState<string>('')` — not `'global'` (which has **no bucket**), not the first firm, not a remembered
value. The query is **disabled while unselected**, so the router's correct 400 is never provoked merely
to render a prompt.

⭐ **Evidence as a by-product:** the unselected render matched **1 of 2** fixtures — **the registry was
never requested.** The instrument reported the *absence of a call* without the executor asserting it.
That is a stronger form than a claim, and it came free.

## 3. THE REUSE THAT WAS DECLINED, AND DECLINING IT WAS RIGHT

`ALL_MDPF_PARTNER_FIRMS` was the obvious reuse and **three seats, including me, gestured at it.** It was
**not** used: module-private to a 2400-line page, it contains `global` which has no bucket, and a page
importing a page for one constant is the wrong dependency.

>> Instead the selectable set is **DERIVED from `MODE_FIRM_ALLOWLIST.satellites` minus the internal id,
so a firm cannot be OFFERED without being ENTITLED.** That is a stronger invariant than the reuse would
have produced, and it keeps **one carrier** of the entitlement. **The build ladder says reuse what
exists — it does not say reuse the first thing that fits, and reusing the wrong constant would have
created a second carrier of the firm list and offered a firm with no bucket.**

## 4. THE LANDMINE CARRIED IN RATHER THAN REDISCOVERED

`bucketSuffix` is **EXPORTED** — not copied — and applied at the wire boundary: the selector's id is
`cottonwood`, the router needs the slug `cot`. **Two carriers of that mapping is exactly what the
2026-06-22 P0 cost**, when it built `opal-data-COTTONWOOD` and rendered Andrew's own internal view
empty. The prior incident travelled into this build as a constraint instead of being re-learned.

## 5. ⛔ WHAT IS NOT CLAIMED, AND IT IS ON THE TO'S FACE

**`complete` != SMOKE-TESTED.** The renders use FIXTURES and a STUBBED session. They exhibit the UI's
branches — selector presence, no-default, five-way discrimination, the firm label on screen — and say
**NOTHING** about whether a live cottonwood caller is served. **That rung stays inferred from source,
not exercised**, for want of a cottonwood credential, and my 12277 ruling stands: a self-signed firm
claim would test the boundary by circumventing it.
**Push state: BOTH LOCAL** at report time. SOURCE rung, not SERVED rung.

## 6. ⛔ A SYSTEMIC GAP — THREE INSTANCES, THREE SEATS, THE SAME EMPTY FIELD

```
TO-7-AE   expected_criteria: None      TO-8-DE   expected_criteria: None
TO-9-DE   expected_criteria: None
```
All three TOs **DO** carry `<expected_criteria>` in their `<proof_of_spec>` block. **No instance
populates the field.** So `proof-of-spec-check` prints **COVERAGE UNCHECKED** every time, and every one
of my certifications has depended on me hand-running step-zero.

>> **THAT IS NOT THREE LAPSES, IT IS A MISSING HANDOFF: the TO holds the denominator and the instance
never copies it.** The fix is one line per instance, and it converts a certifier's manual step into a
machine check. **Until it lands, a bare "VALID, 0 violations" from this checker is NOT evidence of
coverage — and it reads exactly like it is.**

## 7. WHAT THESE CERTIFICATIONS DO NOT DO

- Do **NOT** close `ETFS_POSITIONING-Z-S16`'s remedy beyond its ruled shape.
- Do **NOT** exercise the cottonwood path.
- Do **NOT** close D4. **Its bar is Andrew's smoke test, taken as an internal viewer — which is the
  view `TO-9-DE` exists to make reachable, and reaching it is not the same as him having looked.**

---

— `3.0.0_SA_CVO~Z`
