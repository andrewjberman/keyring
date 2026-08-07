# S-LAYER AXIS FIELD TEST 01 — the five axes against real code

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Recon ID:** RCN-0006 — registered in [`RECON_REGISTER.md`](../RECON_REGISTER.md)
**Date:** 2026-08-07
**Companion to:** `SCRIPT_IO_ONTOLOGY_SPEC_20260806.md` REV 2 @785ed481f
**Status:** FINDINGS. **NOT a spec amendment, and deliberately not folded into the spec** — that
artifact is under live review by `3.0.0_SA_CVO~C` and amending it underneath a reviewer is thrash.

---

## Why this exists

`3.0.0_SA_CVO~C` is testing whether the five axes are **logically** independent — all ten pairs.
That is the right test and it is theirs. **Nobody was testing whether the axes fit REAL CODE.** A
schema can be perfectly orthogonal and still have no bucket for the third line of an actual script.

So: one real file, read line by line, every site classified by hand against the five axes, and every
place the classification failed written down. **The failures are the output.** The sites that
classified cleanly are reported as a count and are not the interesting part.

**Subject:** `data/etfs/scripts/gold/avgcap_monthly_average.py`, lines 1–120.
**Chosen because it is NOT in the held-out set** (ETFS, not ADVI_PERFORMANCE, not MDPF_GLOBAL) and
because it is ordinary — a real gold script with real S3 I/O, not a specimen chosen to flatter the
schema. **This is a hand-classified sample of ONE FILE. It is a stress test, not a census.**

**Denominator: 8 distinct site shapes examined. 4 classified cleanly. 4 did not.**

---

## What classified cleanly (reported, not dwelt on)

| site | direction | grain | resolution | condition |
|---|---|---|---|---|
| `:85` `paginator.paginate(Bucket=…, Prefix=…)` | `ingress` | partition | **`partial`** — bucket folded, prefix carries a runtime `partner` → `s3://opal-data-etfs/daily/{?}/` | `iterated` |
| `:107` `s3.get_object(Bucket=…, Key=key)` | `ingress` | partition | `partial` | `unconditional` |
| `:88`/`:95` `key.endswith(".json")` + `to_date(stem)` in try/except | **`guard`** | — | — | `handled` |
| `:100` `print(f"SKIP: …")` | `egress` | artifact | `literal` | `guarded` |

Two things worth banking from the clean column: **Axis 3 `partial` earned its place immediately** —
the very first real site has a folded bucket and a dynamic path segment, exactly the shape it exists
for. And **`guard` earned its place on the first file**, which I had flagged in §9.3 as a value I was
unsure belonged on the direction axis at all. That is weak evidence for keeping it, not strong: one
file.

---

## F1 — CONSTRUCTOR / HANDLE-ACQUISITION SITES HAVE NO DIRECTION VALUE

```python
:72   s3 = boto3.client("s3", region_name="us-east-1")
:81   paginator = s3.get_paginator("list_objects_v2")
```

Neither is `ingress`, `egress`, `derive`, `roundtrip`, `control`, or `guard`. They carry no payload,
cross no boundary, and gate nothing. **Under Axis 1 as specified, these sites do not exist.**

Excluding them looks obviously correct — *a constructor makes no API call.* **CLAUDE.md Rule 22a
already records what happens when you act on that instinct**, in this exact shape:

> *"`boto3.resource(svc)` → `.Table(name)` → `table.put_item(...)` is NEVER traced —
> opal-data-refresh-api executes 5 real DynamoDB operations and comp-iam's output contains
> 'dynamodb' ZERO times … The constructor tokens are CORRECTLY excluded from the K-line (they make
> no API call), **which also removes the only textual tell of the uncovered shape — a correct
> exclusion can delete the marker of a blindness.**"*

`boto3.resource(` appears in **60 files** under `infra/aws/lambda`. This is not hypothetical and the
estate has already paid for it once.

> **THE FINDING: the S-layer is about to re-derive comp-iam's exact blindness, from the same correct
> instinct, one layer down.** A binding whose target is only knowable by following a handle is
> precisely the case where silence reads as absence.

**Not proposing the fix here** — a sixth direction value, a separate handle/alias axis, and "sites
carry a `handle_binding` field" are all plausible and they are not equivalent. Flagged for the
reviewers as a **P0 structural gap**, because whatever is chosen must be chosen before extraction is
built, not after.

---

## F2 — GRAIN TRANSITION HAS NO REPRESENTATION

```python
:108   rows = json.loads(resp["Body"].read())
```

Axis 2 assigns **a** grain to a site. This site has **two**: `artifact` on the way in, `row` on the
way out. It is the exact point where an object becomes records.

REV 2 §5/R2 says *"S1 sites may be FINER-grained than the C1 edge they aggregate into."* That covers
a site being finer than its edge. **It does not cover a site that is finer than ITSELF.**

This matters more than it first reads. Grain-transition sites are where **provenance actually
breaks** — upstream of `json.loads` you can talk about objects, downstream you can talk about rows,
and nothing in the schema marks the seam. A layer whose whole purpose is field-level flow that
cannot represent artifact→row is not going to reach field grain by accident.

Note `row` is `forward: true` in D1 (declared, unpopulated). **So the S-layer may be about to need a
D1 grain that D1 does not populate** — which per REV 2 §5/R3 is a ratification-chain question, not a
local fix.

---

## F3 — "ENUMERATE THE KEY SPACE" AND "READ A PARTITION" COLLAPSE TO THE SAME TOKEN

```python
:85    paginator.paginate(Bucket=…, Prefix="daily/{partner}/")   # lists WHICH keys exist
:107   s3.get_object(Bucket=…, Key="daily/{partner}/{day}.json") # reads ONE key's CONTENT
```

Both classify as `ingress` at `partition` grain. **They are not the same act.**

- The lister depends on the **existence and naming** of keys. It breaks when a producer renames.
- The reader depends on the **content** of a key. It breaks when a producer changes schema.

The script itself proves the distinction is load-bearing: `:91-98` exists **only** because listing
returns non-contract names, and a mis-named object (`holdings_{date}.json`) is logged-and-skipped.
That is a real defect class living entirely in the gap between the two.

For blast radius — the thing §5 claims the layer licenses — conflating them is a wrong answer, not a
coarse one. *Candidate:* this may be a `derive`-style sub-kind on Axis 1, or a sixth axis
(**existence-dependency vs content-dependency**). **A sixth axis is a serious claim and I am not
making it on one file.**

---

## F4 — ARE LITERAL CONSTANTS S0 SITES? THE SPEC DOES NOT SAY

```python
:56-60   PARTNER_CLOCKS = {"inflection": date(2026, 5, 15), "49f": None, "cottonwood": date(2026, 6, 8)}
:70      CANONICAL_PARTNERS = ("49financial", "inflection", "cottonwood")
```

These are **hardcoded business policy** — onboarding clocks that bound a denominator, and an
allowlist whose own comment says the default glob *"would otherwise pick up staging/test prefixes …
DOUBLE-COUNTING 49F."*

§3.3 defines S0 as *"one S0 record per call/expression site that participates in any binding."*
**Ambiguous on constants.** If constants are not sites, a script's dependence on a hardcoded
business date is invisible to the layer — and that is exactly the class project coherence exists to
surface.

**The estate has already answered this for itself:** `comp_constants_cli.py` treats constant sites
as first-class and tracks env-backing. **A spec that excludes them contradicts a shipped tool** —
and `CANONICAL_PARTNERS` here is explicitly a mirror of a guard in a *different* file
(`etf_ownership_dashboard.py`), which is a cross-file constant coupling that only a constant-aware
layer could ever see.

---

## What this does and does not establish

- **It does NOT establish that the axes are wrong.** Four of eight shapes classified cleanly on the
  first real file, and two axis values I was unsure about earned their place.
- **It does NOT bound anything.** One file, 120 lines, hand-classified, Python only. **The React/TSX
  side has not been field-tested at all** and F1–F4 may look completely different there — prop flow
  has no constructors and no deserialization boundary, so I would expect *different* failures, not
  fewer.
- **It DOES establish that the axes have at least four gaps that real code hits within 120 lines**,
  and that one of them (F1) is a blindness the estate has already paid for once in `comp-iam`.
- **The classifier was me.** A hand-classification by the schema's own author is the weakest possible
  instrument on this question — I am motivated to find my axes sufficient, and I found gaps anyway,
  which is *some* evidence but not the kind that should settle anything. **An independent classifier
  on a file I did not choose is the test that would.**

## Recommended next

1. **React/TSX field test** — same method, a non-ADVI portal component. Mine, next tick.
2. **F1 is P0** and blocks extraction design; F2 is P0 for anything claiming field grain.
3. F3 and F4 are P1 — real, but they change the schema's *shape*, not its viability.
