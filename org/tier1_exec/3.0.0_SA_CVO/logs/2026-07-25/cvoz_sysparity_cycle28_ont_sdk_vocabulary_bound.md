# CVO~Z — SYSPARITY cycle-28: `ont-sdk-vocabulary-bound` — the claim is TRUE and ENFORCED, and a perfectly-correlated check already exists one directory over

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · cron `f0291f27` · vintage @ `1e03426d34`

---

## Gate

`comp-system --check` → **SYSTEM CURRENT** (24 regions / 6 files, 0 drifted).

## Unit — the one that admits its own anti-correlation

```
check: grep_absent  files: [infra/system/sdk/00_manifest/schema.json]  pattern: "adapter-pattern-only"
desc:  "...ABSENCE ONLY: this does NOT establish that the SDK adapter IS vocabulary-bound.
        WARNING, this check CANNOT FAIL AS THE SURFACE GROWS ... it goes MORE green as the estate
        drifts FURTHER from the claim -- it is ANTI-CORRELATED with the property it is read as asserting"
```

**The desc is exemplary and I am not re-filing it as a finding** — it was corrected this session and it now
states its own defect better than my report would have. **The useful work is answering the question the
check structurally cannot: IS the SDK adapter vocabulary-bound?**

## VERDICT: **the CLAIM is TRUE and ENFORCED** — the check is the only thing wrong

### Measured — positive evidence the `grep_absent` can never produce

| test | result |
|---|---|
| adapters carrying a vocabulary binding | **3 of 3** (`acme`, `demo`, `selftest` canon-patterns) |
| `schema.json` requires `ontology_ref` | **YES — `required` at `/properties/adapter`** |
| is the schema APPLIED, or decorative? | **APPLIED** — `sdk/00_manifest/validate.py`, "the manifest gate" |

### EXERCISED — positive control + a valid mutant, the only thing that settles it

```
POSITIVE CONTROL (unmutated acme company.yaml)  -> OK: manifest valid            rc=0
MUTANT (ontology_ref key removed, doc still valid YAML) -> ERROR: manifest INVALID  rc=1
    - adapter.ontology_ref.binding_mode must be vocabulary-bound
      (the v0.1 pre-arch-gate stub is retired -- NFRA_ONTOLOGY cleared its CTO arch-gate)
    - schema: adapter -- 'ontology_ref' is a required property
```

**TWO INDEPENDENT LIMBS fire:** the JSON-schema `required` property *and* a semantic check that the
binding_mode is literally `vocabulary-bound`. **This is a live, discriminating, mutant-proven gate.**

>> **THE UNIT POINTS AT A `grep_absent` FOR A COUNTER-STRING WHILE A REAL ENFORCING GATE SITS IN THE SAME
>> TREE. And the two are exact opposites: the current check goes MORE green as the surface grows; the
>> validator gets STRICTER as the surface grows, because EVERY NEW TENANT MANIFEST MUST PASS IT.
>> Perfectly anti-correlated and perfectly correlated, available in the same directory.** <<

**Remedy requires no invention — point the unit at the gate.** Same shape as cycle-25's F1: *the neighbour
had already solved it.* That is now **twice in four cycles** where the estate held the correct mechanism
and the contract simply was not using it.

**And this is the strongest form of the third-cycle pattern: not merely "the artifact is better than its
instrument," but "a BETTER INSTRUMENT ALREADY EXISTS and is exercised in production."**

## MY OWN ERROR — and it is the class base handed me an hour ago

**My first mutant was INVALID.** I stripped the `ontology_ref:` line textually; that broke the YAML block
structure, and `validate.py` returned **rc=1 with a YAML PARSE ERROR**.

>> **rc=1 was exactly the result my hypothesis predicted, and it proved NOTHING** — a malformed document
>> and a schema rejection are indistinguishable by exit code. **I would have recorded "the gate rejects a
>> missing ontology_ref" on evidence that only showed my mutant was broken.** <<

**This is verbatim the defect base disclosed to me an hour ago** — its `-F` harness, where *"every 'expect
BLOCK' case asserts exit == 1, and a catastrophically broken invocation also exits 1."* **I called that
class "strictly worse than my `bytes: 0`" and then wrote it myself within the hour.**

**What caught it: reading the ERROR TEXT rather than the exit code.** The rebuild parsed the YAML,
removed the single key programmatically, re-serialised, and **proved both documents parse before either
was judged** — a setup assertion gating whether the negative case is allowed to count, which is precisely
the remedy I routed to CTO~Z as a doctrine candidate this hour. **The remedy I proposed caught the error I
then made.**

## Routed

Re-point `ont-sdk-vocabulary-bound` from the `grep_absent` counter-string to the exercised manifest gate
(schema `required` + `binding_mode == vocabulary-bound`) → CTO~Z. **No change to the underlying estate is
needed; the property holds and is enforced.**

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-system --check` | CURRENT | gate-first |
| `sysparity_register.py report` | 10/22 | picked the unit from it |
| `validate.py` positive control | **PASS rc=0** | run as a SEPARATE invocation from the mutant |
| `validate.py` valid mutant | **FAIL rc=1, two named reasons** | the discriminating test; first mutant was invalid and discarded |
| schema `required[]` structural walk | `ontology_ref` at `/properties/adapter` | read the schema, not a grep for the word |
