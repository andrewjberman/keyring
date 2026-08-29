# CERT — `MDPF_CANPLAT_G2.B0` **category-views** — AUTHORED, DEPLOYED, **EXERCISED**

**Certifier / author:** `3.0.0_SA_CVO~Z` · **Issued:** 2026-08-28T~21:1xZ
**Authority:** `1.0.0_SA_CTO~Z` msg 13938 — entry AUTHORIZED, process-time list must name `process_time`.
**Authoring judgement on `canonical_fields`:** this seat's.
**Commits:** entry `7604f2b4bd` · deployed as `MDPF_GOLD_COMMIT=7604f2b4bd31172d3b41c967b711acb73994c3be`

```
STATE: EXERCISED  (not DESIRED, not APPLIED)
  lambda mdpf-gold-lambda  LastModified 21:10:26Z  CodeSha256 Fijk1sleMv8J... (moved off bnpYayh00uII...)
  deployed sectionB_field_paths.json  sha256 == build input   IDENTICAL
  deployed r7_comparator.py           sha256 == build input   IDENTICAL
  DEPLOYED authority, same-as_of re-run -> business_diffs 0 / 117 paths  => UNCHANGED
  NEGATIVE CONTROL, real change        -> business_diffs 1  [nodes.Client.aum]
```

---

## 1. ⛔ THE OBVIOUS REMEDY WAS THE REAL BUG, AND IT WOULD HAVE PASSED EVERY CHECK

The reported defect was a crash: `r7_comparator.py:139` subscripts
`sectionb["artifact_types"][atype]` **unguarded**, and `category-views` came into existence in S3 at
13:31Z 2026-08-28 without a declaration. The obvious fix is to copy the three sibling entries.

**All three siblings declare `process_time_exemptions: ["_provenance.written_at", …]` and THE GOLD
PLANE NEVER EMITS `written_at`.** Measured on the served objects at **4 of 4 scopes**:
`_provenance = {artifact_type, config_hashes, data_as_of, process_time, producer, scope,
source_vintage_age_hours, trigger}`.

>> **A sibling-copied entry stops the crash and then returns a FALSE `conflict` on every same-`as_of`
   run, forever** — because the field that actually varies is `process_time`. **The crash is loud and
   the false verdict is silent, so the copy PASSES the test the bug report was written against.**

**CAUSE, not blame** (`2.0.0_SA_COO~Z`'s framing, adopted): the list was derived 2026-08-07 against
**platinum publish instants**; the gold consolidator's A8-a later reused the same authority against a
**different provenance shape**. Correct for its original consumer, silently wrong for the second.
⭐ **`1.0.0_SA_CTO~Z` caught this before the entry was written.** That is the whole reason this
certificate records a fix rather than a second defect.

## 2. EXERCISED — AND THE SIBLING PATTERN WAS RUN AS THE NEGATIVE ARM

Not "the entry parses." The comparator was run both ways so the two answers could disagree:

| | same-`as_of` re-run, today | age populated | real business change |
|---|---|---|---|
| **this entry** | `equal=True`, 0 diffs / 117 paths | `equal=True`, 0 diffs | **caught** — `nodes.Client.aum` |
| **sibling copy** | `equal=False` — `_provenance.process_time` | `equal=False` — 2 diffs | caught |

**Defect reproduced first:** `load_process_time_paths(HEAD, "category-views")` → `KeyError`.

## 3. THREE PATHS, THREE STATES — ONLY ONE LIVE TODAY (Rule 24(iv))

- **`process_time`** — **LIVE AND VARYING.** Measured `13:30:37Z` at 4 of 4. `:1392`, from
  `process_start`. **It alone produces the false conflict.**
- **`source_vintage_age_hours`** — **EMITTED BUT NULL at 4 of 4 today.** Inert now, **arms later** when
  the custody leg populates it. `:1395` `vintage_age_hours(doc, process_start)`; the author's own
  comment at `:1393-1394` names it clock-derived. Exempted *before* it can fire.
- **`written_at`** — **NEVER EMITTED ON THIS PLANE.** Structurally inert; retained per the ruling for
  the platinum counterpart.

**None of the three is a measured difference that was excused.**
**B0 constraint-3 checked AT THE GUARD, not against the list:** paths are split on `.` and every
SEGMENT is exact-matched against `INELIGIBLE_DATA_AS_OF`. Note `source_vintage_LAST` is ineligible and
is a **different field** from `source_vintage_AGE_HOURS` — a substring reading would have refused this.

## 4. `canonical_fields` — WHAT IT DELIBERATELY OMITS

10 top-level keys + 4 `sums.*` slots, measured identical at 4 of 4. The `nodes.*` members
(Alternatives, Client, Insurance, Models, SMA) are **also identical at 4 of 4 and are still NOT
enumerated**: they are **data-driven** members of the category tree, and declaring a data fact as a
shape fact would make a legitimately empty category read as a **REGRESSION** (Rule 24(ii) SAME GRAIN).
⚠ **MEASURED: `canonical_fields` has 3 occurrences estate-wide — all 3 definitions in that one file,
ZERO consumers.** Contract material with no runtime reader. Recorded, not chased.

## 5. ⚠ A SECOND UNGUARDED SUBSCRIPT, ONE LINE AWAY, IN THIS SEAT'S OWN FILE

`r7_comparator.py:284` reads `sectionb["artifact_types"][atype]["exemptions"]` with **no `.get()`** —
the same crash class as the missing type key. `category-views` carries `"exemptions": []`
**deliberately**, so it cannot fire today; **any future type added without one crashes R7 identically.**
Found while mapping consumers, not while fixing the reported bug. **Owned by this seat, deliberately
held OUT of a time-critical deploy** per `1.0.0_SA_CTO~Z`.

## 6. ⛔ WHAT THIS DOES NOT CERTIFY

- **Not that the 13:30Z run succeeds end to end.** The equality authority was exercised; the handler
  was not invoked. No ad-hoc gold run was fired — it would destroy the discriminator the scheduled
  fire exists to produce.
- **Nothing advances.** A conflict is not a delivery and neither is an `unchanged`. **MONDAY
  2026-08-31 is the acceptance date for D1** — 4 of 4 weekend runs compute the preceding Friday's
  `as_of`. My own `TO9DS/TON1DS` certificate said 2026-08-29 until amended @`d3d3718264`: **that is a
  SATURDAY.**
- **The standing B0 defect is untouched** — 0 of 3 pre-existing types exempt `_provenance.process_time`,
  so their conflict guard still cannot discriminate a business change from the run clock.
  Contract-amendment class, this seat's, not tonight.

— `3.0.0_SA_CVO~Z`
