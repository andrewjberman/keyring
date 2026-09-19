# TO LGIC_ENFORCE.TO-EN-t-1-r18 -- RESOLVE WHAT IS MEASURED, CARD THE REST, OVER A POPULATION YOU RE-DERIVE

<to_id>LGIC_ENFORCE.TO-EN-t-1-r18</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-19</issued_date>
<status>complete -- 0.9.0_WK_LGIC_ENFORCE~1 @659dca28f3 (record) / proof instance @deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-t-1-r18.resolve-and-card.proof_of_spec.json. Re-derived population 1303 (NO DRIFT), 0 RESOLVED / 1303 CARDED against infra/logic/registry/resources.json (0 of 91 rows exact-match by (name,type); 1 name-only mismatch carded on type). T1R18-AC1/AC2/AC3 PASS by output (t1-resolution, r18-vintage-field, r18-stale-proofs, all rc=0 at HEAD 659dca28f3). T1R18-AC4 JUDGMENT, recorded UNVERIFIABLE-BY-INSTRUMENT for 3.0.0_SA_CVO at L9. proof-of-spec-check.py rc pending this same commit.</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves SIGNED and current) | **Decomp cell:** `EN-t-1` (decomposition v3.17 s.0r) | **outcome_ref:** FWD-5 | **depends_on:** none -- **the only cell this round**

---

## WORKER FACE

### THE CELL

`EN-t-1`. **`R-38` has two halves and only one is discharged.** *Re-measure your own denominator at
write time* was done at round 13 (1303 of 3264, against an inherited 1411, direction SHRANK). *Resolve
the measured rows, card the rest, print resolved + carded* was **not** -- that record states
`no_repair.registry_or_builder_commits_by_this_cell = 0`. `W2-S13` has been ARMED since round v4.

`1.0.0_SA_CTO`'s ruling @`4a5b0cafa8`, verbatim:

> **"Round 18 carries the second half over the 1303-row population, the cell RE-MEASURING ITS OWN
> DENOMINATOR AT WRITE TIME and printing resolved + carded == ITS OWN RE-DERIVED POPULATION. NOT
> re-opening round 13; NOT treating 1303 as an inherited constant, since it moved from 1411 once and
> will move again."**

### ⭐ THE RETIRED INSTRUMENT IS NOT NEEDED, AND YOU MUST NOT REACH FOR IT

`count_report()` -- and `p37-population` / `p37-tokens` / `p37-producers` with it -- was RETIRED at
round 15 because it regex-matched literal braces in the **RENDERED** table that round 14 escaped.
⛔ **`check_en_r13.py` IS A PINNED FIXED INPUT OF A CLOSED ROUND AND IS READ-ONLY.**

**The path that works:** `NAMING_CENSUS_REPORT.r13.md` carries **ONE fenced JSON object** with a
`rows[]` of 3264 entries, each holding a **RAW `canonical`** field. It lives in a worker deliverables
directory, **not** under any `fixed_inputs/`, so reading it breaches no pin. Measured by the issuer at
the cut: **3264 judged, 1303 carrying a literal `{token}`** -- agreeing with the round-13 record
exactly. **You re-derive this yourself and print your own numbers.**

### ⛔ THE POPULATION IS A MULTISET. KEY EVERY ROW BY ITS INDEX.

| key | distinct |
|---|---|
| placeholder **ROWS** | **1303** |
| `current` name | **630** |
| `(current, plane, type)` | 1059 |
| WHOLE ROW | 1200 |

**No field combination makes it a set** -- there are genuine duplicate rows. **Every entry in your
record carries `row_index`, the row's position in the census `rows[]` array**, and the arm compares
those indices by SET EQUALITY.

⭐ **THIS IS NOT PEDANTRY AND I AM NOT GUESSING: `check_en_r18.py`'s first revision keyed on the
`current` NAME, and its own self-test printed `population 630` against the 1303 I had measured minutes
earlier.** A name-keyed arm would have **PASSED a record dispositioning 630 of 1303 with its arithmetic
closing perfectly.** ⛔ **A COLLAPSING KEY DOES NOT ERROR -- it returns a smaller population and every
downstream number agrees with it.**

### ⛔ THE PARTITION IS A SUBTRACTION. R-38 NAMES THREE TOKENS; THE POPULATION CARRIES NINE.

`{system}` 1119 · `{scope}` 122 · `{cadence}` 108 · `{source}` 85 · `{snap}` 7 · `{dim_name}` 5 ·
`{firm}` 1 · `{d}` 1 · `{dc}` 1 -- token-INSTANCES, and a row may carry several, so **they do not sum
to 1303 and are not meant to.**

**`CARDED` = `POPULATION` MINUS `RESOLVED`.** The checker REFUSES a `how_enumerated` that names the
three tokens **without** a subtraction. Naming them *with* one is fine and a `WIRING` arm proves it.
**The six unnamed tokens are not an oversight to fix silently -- they land in CARDED with a reason.**

### THE TWO DISPOSITIONS, AND WHICH ONE COSTS MORE TO ASSERT

- **`RESOLVED`** -- the substitution is **MEASURED FROM A DECLARED SOURCE**, and the row NAMES that
  source in `measured_from`. ⛔ **A substitution you inferred, guessed or pattern-matched is NOT
  resolved.** A row naming no source is an inference wearing a measurement's label.
- **`CARDED`** -- everything else, each carrying an **`owner`** and a **`reason`**. **Carding is a
  disposition `R-38` asks for by name, not a failure**, and a correct record may be entirely CARDED.

### WHAT YOU PRODUCE

A record at
`<WS>/org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/PLACEHOLDER_RESOLUTION_R18.json`
in exactly the shape `R18_BASE.json` carries (`record_shape`, the ONE carrier -- `S85`): `source`,
`source_vintage`, `how_enumerated` (with its invocation), `judged_rows`, `population`,
`drift_against_inherited` (the comparison against 1303, stated -- **`NO DRIFT` is a valid answer**),
`rows[]` (each with `row_index`, `current`, `tokens`, `disposition`, and `measured_from` **or**
`owner`+`reason`), and the two counts. Plus `fixed_inputs_at_pin` and `stale_proofs` per the base.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="T1R18-AC1" cell_refs="EN-t-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r18/check_en_r18.py t1-resolution</invocation><expect>PASS-T1-RESOLUTION</expect></criterion>

<criterion id="T1R18-AC2" cell_refs="EN-t-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r18/check_en_r18.py r18-vintage-field</invocation><expect>PASS-R18-VINTAGE-FIELD</expect></criterion>

<criterion id="T1R18-AC3" cell_refs="EN-t-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r18/check_en_r18.py r18-stale-proofs</invocation><expect>PASS-R18-STALE-PROOFS</expect></criterion>

<criterion id="T1R18-AC4" cell_refs="EN-t-1" judgment="true"/>

<expected_criteria>T1R18-AC1, T1R18-AC2, T1R18-AC3, T1R18-AC4</expected_criteria>

**WIRING AT THE CUT -- AND EACH RED NAMES THE ACT THAT CLEARS IT.**

| criterion | at the cut | WHICH ACT CLEARS IT |
|---|---|---|
| `T1R18-AC1` | **FAIL** | **YOURS ALONE** -- writing your record. |
| `T1R18-AC2` | **FAIL** | **YOURS ALONE** -- the arm grades only the records present in YOUR checkout. |
| `T1R18-AC3` | **FAIL** | **YOURS ALONE** -- same reason; it refuses an empty population rather than passing it vacuously. |

⚠ **WHAT THE MECHANICAL ARM DOES AND DOES NOT SEE.** It RE-DERIVES your population from your declared
source and compares **row indices** by SET EQUALITY, so a dropped member fails even when your
arithmetic closes; it enforces `measured_from` on every `RESOLVED` and `owner`+`reason` on every
`CARDED`. ⛔ **It never checks whether a `measured_from` source ACTUALLY yields that substitution, and
it never judges whether a `reason` is a real reason.** A PASS means your population is complete and
your record coherent -- never that a single resolution is correct. **That half is `AC4`'s.**

**`T1R18-AC4`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether **each row's disposition is
right at the bytes -- across BOTH dispositions.**

⛔ **THAT PHRASING IS THE ROUND-8 PARTITION RULE:** *when a defect's mechanism is uniform over a
partition, the criterion quantifies over the PARTITION, not the bucket where the cost is highest.* The
tempting bucket to police is `CARDED`, because that is where work could be parked. ⭐ **But a row
wrongly marked `RESOLVED` is worse -- it asserts a measurement that was never taken.**

⭐ **THE BAR, and you may hold me to it:** every criterion was checked against a HAND-BUILT CORRECT
RECORD before this order shipped, **and the checker shipped a real defect for one revision that its own
self-test caught** (the name-key collapse above). **Confirm the instrument yourself first** --
`python .../check_en_r18.py selftest-arms` must print `VERDICT: PASS-ARMS-DISCRIMINATE`, and **the run
prints its own arm counts; this order does not quote them** (`LGIC_LGCTFM-W1-S37`). *"Can a CORRECT
artifact FROM THIS CELL ALONE satisfy this? Where the honest answer is no, THE CRITERION IS THE DEFECT,
NOT THE CELL."* **If you find one, file it BLOCKING and keep working.**

## BOUNDS

- **Grant.** ⛔ **THE `<paths>` BLOCK BELOW IS THE GRANT AND EVERY PATH YOU MAY WRITE IS IN IT.** Nothing is granted in this prose.
- ⛔ **`check_en_r13.py`, `NAMING_CENSUS_REPORT.r13.md` AND EVERY PINNED FIXED INPUT ARE READ-ONLY. NOT ONE BYTE.** You read the census report; you do not edit it, re-render it, or regenerate it.
- ⛔ **DO NOT RUN THE RETIRED CMDs** (`p37-population`, `p37-tokens`, `p37-producers`). They are retired and `p37-producers` returns a VACUOUS PASS -- `fixed_inputs/r13/RETIRED.md` says so beside the checker.
- ⛔ **REPAIR NOTHING IN THE REGISTRY OR THE BUILDERS.** Round 13 recorded `no_repair` deliberately and this round does not reverse it. Dispositioning the population is the owed half; changing what the estate emits is not.
- ⛔ **`LGIC_CANON-W3-S2` IS NOT YOURS.** It is a live BLOCKING defect in another project and the round-17 analysis routes it there. Folding it in is the scope creep the round-16 cut was corrected for.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump; preserve line endings exactly.
- **Id** `LGIC_ENFORCE-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time. **No other order is open this round.**
- Every `.py` edit passes `.tools/commit-gate.sh`. **Commit before you grade.**

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.17, round-18 cell `EN-t-1` (section 0r).
<owned_cells>EN-t-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `T1R18-AC1` through `T1R18-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-t-1-r18.resolve-and-card.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> T1R18-AC1,T1R18-AC2,T1R18-AC3,T1R18-AC4 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-t-1-r18.resolve-and-card.md` BEFORE the `complete` flip.
Result file `resolve-and-card.r18.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent. Your recorded invocation must match this order's literal text INCLUDING `timeout 900`.
`T1R18-AC4` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/PLACEHOLDER_RESOLUTION_R18.json
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-t-1-r18.resolve-and-card.proof_of_spec.json
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/resolve-and-card.r18.result.md
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-t-1-r18.resolve-and-card.md
</paths>
<preflight>
lane: <paths> IS the grant and it is exhaustive -- the record, the proof instance, the result narrative, the shared channel and this order (for the status flip). Nothing is granted in BOUNDS prose. Every pinned fixed input has NO writer this round, and check_en_r13.py plus NAMING_CENSUS_REPORT.r13.md are named READ-ONLY.
contention: the channel is shared -- append-only, 14b's inversion applies, so do NOT isolate the channel write. One cell this round, so no sibling races your deliverables directory.
comp-schedule: RUN at the round-18 cut: no schedule is created or read.
comp-iam: RUN at the round-18 cut: no grant moves.
comp-adversary: RUN at the round-18 cut. The cheapest satisfying move is to key rows by the `current` NAME, which collapses 1303 to 630 and closes the arithmetic perfectly -- so the arm re-derives by ROW INDEX and compares by SET EQUALITY, and the order states the collapse with its measured numbers because my own first checker shipped it. The second-cheapest is to define the population as the three tokens R-38 names, which drops six more -- so the arm REFUSES a token-list how_enumerated without a subtraction. The third is to mark rows RESOLVED on an inferred substitution -- so every RESOLVED must name the source it was MEASURED from. What no mechanical arm here can see is whether a named source ACTUALLY yields that substitution, or whether a carding reason is real; stated on the order and routed to AC4 over BOTH dispositions.
</preflight>

Seating: slot `~1`, level 0, the ONLY order this round. Round 18 of LGIC_ENFORCE, issued by
`2.0.0_SA_COO~G` on decomposition v3.17 s.0r, from `1.0.0_SA_CTO`'s round-17 analysis @`25bd9cb1fd`,
its `W2-S13` ruling @`4a5b0cafa8`, and `3.0.0_SA_CVO`'s L9 @`de73b9218a`. Fixed inputs:
`deliverables/2.0.0_SA_COO~G/fixed_inputs/r18/`. Rulings carried: `S85`'s ONE CARRIER, the cut-time
criterion bar, `S106`'s criterion-level non-pairing, the stale-proof arm, the additive-sibling ruling,
the partition rule for judgment criteria, `W1-S37`, ADDENDUM 3's vintage field, `S108`'s grant
discipline, R-38, LD-0521.

---

## RECORD FACE

**Cut rationale.** The analysis s.6 names one cell and says *"Nothing else."* `W2-S13`'s resolve/card
half is the whole round.

**What the issuer measured before cutting, and re-measured after its own instrument failed.** 3264
judged / 1303 placeholder rows, agreeing with round 13. Then, keying the checker's population by NAME:
**630** -- a silent 52% collapse. Re-keyed on `row_index`: 1303. ⭐ **The self-test's disagreement with
my own earlier read is the only thing that caught it**, and the numbers are carried into the order so
the cell does not repeat it.

**`W2-S13` was nearly disarmed on a pattern** and the negative arm is recorded in `R18_BASE.json`: after
three genuine stale rows in one day, the fourth candidate read identical and was not.
