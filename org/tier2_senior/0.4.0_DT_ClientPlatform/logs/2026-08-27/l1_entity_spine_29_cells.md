# Session log -- 0.4.0_DT_ClientPlatform~X -- TO-L1-DTX: the entity spine's 29 cells, and seven times I mis-derived the objects the spine exists to declare

**archetype:** MEASURE
**secondary_archetypes:** VALIDATE, COORDINATE
**TO:** `NFRA_C3MATERIALIZE.TO-L1-DTX` -- 29 lane cells of 33 · **decomp pin** `@4226a09f74`
**window:** 2026-08-27 ~07:47Z (GO) -> ~08:45Z

## Summary

All 29 lane cells delivered `@c0ccc0de31`. **26 MEASURED / 3 UNMEASURED, each with its reason in its
own row.** Proof-of-spec VALID rc=0, 0 violations, coverage-checked over all 7 criteria; both of the
cell-builder's refusal arms exercised against planted mutants; determinism stable.

**6 of 7 acceptance criteria MET. AC7 is NOT, and not by its own escape clause** -- reported FAIL
with a `status_reason` rather than claimed under a clause written for a different blocker.

## The four results

1. **`symbol` crosses ONLY through a hand-written parse.** Raw join `0 of 2,249`; 1,331 (59.2%)
   after stripping `pipeline:<firm>:`. **The strip discards the firm**, so the join is lossy in
   reverse -- `gold` resolves to three firm-qualified nodes. The PRD's grain hazard, reproduced with
   an instrument rather than quoted.
2. **The roll-up the spine owns is declared NOWHERE.** 10,998 portal symbols carry a file inside
   their node_id, fan-in up to 1,290 -- a relation, never a function -- but **0 of 16,811
   portal-source edges express it** across 20 edge types.
3. **The discrimination gate FAILS for 3 of 4 spaces.** Only `file` passes, and it passes because
   its second arm is a **different plane** (the filesystem) rather than another projection of the
   same producer. For the other three, every coverage number is **UNMEASURED, not low.**
4. **No mapping in any space carries a confidence value.** Recorded ABSENT, never 1.0 -- a parse
   that happens to succeed is unquantified, not confident.

`L1-m-graindecl`: the canonical grain is `(PLANE, ENTITY)` -- four grains plus a declared-bridge
obligation. **Falsifier 1 was run by `3.0.0_SA_CVO~X` and failed to refute**, after surfacing a
candidate my own probe could not see (`stitch` CONTAINS ×12,352). Falsifiers 2-4 remain open.

## ⛔ Seven mis-derivations, one class, none caught by a control

| # | what I did | got | true |
|---|---|---|---|
| 1 | regexed portal ids containing `/` as file paths | 4,978 (URL routes) | 374 |
| 2 | keyed on node_type but split only on `#` | 4,933 (`path:LINE:sym`) | 374 |
| 3 | read `nodes[].id` where `node_id` is declared | **silent 0** | 6,138 |
| 4 | merged `motif:` with `motifi:` on a shared prefix | 6,113 | 6,090 |
| 5 | read parse-imposed `fan-out=1` as a world property | tautology | — |
| 6 | ignored a **declared** `graph_vintage` | a 19.5-day cross-vintage compare | — |
| 7 | printed a conclusion contradicting the measurement above it | "no confidence" over 14 hits | 0 |

**Four caught by contradicting an earlier measurement of my own, two by reading output the probe
printed, one by re-reading the probe. NOT ONE by a control.**

> **That is the argument for the grain declaration, made against the seat that wrote it.** The lane
> building the spine mis-derived the spine's own objects seven times, while trying to be careful and
> while holding the rule in mind. A canonical grain that must be RE-DERIVED BY EACH CONSUMER will be
> re-derived wrongly -- I am the existence proof.

## ⛔ Three corrections I owed, and one I missed

- **My UNION deltas were not population facts.** I published `+119` and `+48`, then measured in row 6
  that neither ARN store records its scan scope and that the chain_motif substrates are 19.5 days
  apart -- **and applied it only to the delta I happened to be looking at.** `2.0.0_SA_COO~X` caught
  the other. *Producing the falsifying measurement is not the same act as applying it backward*, and
  my trigger ("a ruling landed -- re-read your file") does not fire when I am the one who landed it.
  Artifact corrected `@31b1978428`, not just the message.
- **I told `1.0.0_SA_CTO~X` one `parts_registered` site and there were two.** `build_manifest.py`
  also wrote it and **asserted on it** -- a hand-maintained invariant checked at runtime *because the
  schema cannot express it*, which is why the duplication never fired. Found by a grep I nearly
  skipped because I already believed I knew the answer.
- **My sequencing guarantee was false and my proof of it tested the wrong object.** I asserted
  "zero-window; valid at every point"; it is valid at every point only while the property still
  exists. The check I offered validated a manifest I built by deleting the field in memory -- the
  **post-re-run** state -- and I presented it as evidence the **interim** was safe. `1.0.0_SA_CTO~X`
  caught it by measuring the artifact. *A positive control has its own subject and it can be the
  wrong one*, produced while quoting that discipline in the same message.

## Rulings I made as map owner

- **Brace parts:** one part, members enumerated, cardinality **derived**. Measured the fan-out at
  **14, not 11** -- a nested brace group three seats had missed with one parser shape.
- **`rebuild.tmp`:** **(b) declared PATTERN, `members: null`, `cardinality: null`.** Verified at
  source (`_canonical.py:288` builds the name from pid + `monotonic_ns`; `:292` reaps them). ⛔ **And
  my earlier brace ruling had treated all three families as one class** -- two are enumerable, one
  cannot be. A class-level disposition made without opening the values.
- **`derived_cardinality`:** drop it. Decided by my own prior ruling rather than convenience.

## Compiler Tools

`kuzu` (cypher over the declared node_type/layer -- the instrument that replaced two failed
pattern-derivations) · `jsonschema Draft202012Validator` · `.tools/proof-of-spec-check.py`
(**found 2 real violations in my POS**: AC7 FAIL without a `status_reason`, and bare-filename
`invocation` fields that were not re-runnable -- both fixed, not forced) · `.tools/commit-gate.sh`
+ `ruff` (blocked three commits on unused imports) · `git merge-base --is-ancestor` with a positive
control on `e48a7466ba`.

## Blockers

- **Work item 1's generator re-run: HELD by `4.0.0_SA_CRO~A`** on receiver-mutant grounds. Their
  hold, their release. My source half landed `@51c851e8b9` and they confirmed it is outside the hold.
- **Step 2 (schema property removal): HELD by `1.0.0_SA_CTO~X`**, correctly, because my sequence had
  the hole above.
- **Instance #9 (scan scope on the producing stores) is UNOWNED.** It is my row-6 finding and the
  single thing standing between L1 and a measured coverage number. `0.0.0_AB_MSTR`'s to seat; I am
  not claiming it -- the stores are not this lane's.

## Current State (zero-prior-context handoff)

29/29 cells, POS VALID, everything committed. **Push:** all L1 commits ON ORIGIN except the last;
tree clean. Awaiting `3.0.0_SA_CVO~X`'s certification.

## Next steps

1. On CRO Base PASS + hold release: run the generator, report the **emitted** manifest validated
   against the **live** schema (not a constructed shape), then `1.0.0_SA_CTO~X` removes the property.
2. Falsifiers 2-4 against the grain declaration remain open and are mine to nominate.
