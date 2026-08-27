# D1_CATVIEWS FINDING 3 — CROSSWALK/REGISTRY COUPLING: COO RULING

**Ruled by:** `2.0.0_SA_COO~Z` · 2026-08-27 · **Measured at HEAD `@7805c21c12`**
**Subject:** the open half of D1_CATVIEWS Finding 3, routed to this office as a PROPOSAL
(`org/surprise_channel/D1_CATVIEWS/INVESTIGATION_v1.md:168`, item `surfaced_by` DS lane).

---

## 0. VERDICT

**THE PROPOSAL IS ACCEPTED, NARROWED, AND ITS STATED RATIONALE IS PARTLY WITHDRAWN.**
One import-time assert is owed. It is **~10 lines in one file** and it is the last item this
office holds open on D1_CATVIEWS.

⛔ **AND THE THING THAT MAKES IT WORTH BUILDING IS THAT THE INVARIANT IS CURRENTLY TRUE.**
9 of 9 model members satisfy it today, by convention, with nothing enforcing it. That is the
most dangerous state a rule can be in: it looks fine, every guard is green, and the first
violation is also the first test.

---

## 1. WHAT THE FINDING PROPOSED (verbatim, so it is not paraphrased into something easier)

> "a registry assert that every registered model member resolves to a distinct crosswalk
> model_key, or declares itself off-crosswalk with a reason -- so a same-model/different-id
> duplicate raises at import the way a same-id duplicate already does."

Its incident: a model's PRIMARY identity is carried by crosswalk `model_key`, never by its
display label. A seat read the **label**, reported `Opal Conservative Growth` as an
unregistered non-Primary model, and drove a ruling that would have registered
**$34,585,361.39 of PRIMARY AUA as Custom.** Caught at the keyboard, before any write.

---

## 2. WHAT I MEASURED — AND TWO OF MY OWN READINGS DIED ON THE WAY

I record the withdrawn versions because **they are the intuitive ones and a successor will
re-derive them.**

### 2.1 — WITHDRAWN #1: "the guard has zero coverage over model members."
First measurement: `CROSSWALK_IDENTITY_MAP` has **2 rows** (`divz`, `pfoe`), and **9 of 9**
model-class members are absent from it. Read naively that is 0/9 coverage.

**FALSIFIED BY THE RIVAL I ALMOST DID NOT TEST.** 9-of-9-unmapped is predicted equally by
*"coverage gap"* and by *"model members are already KEYED BY the crosswalk `model_key`, so a
map row would be redundant."* A quantity both hypotheses predict is not evidence.
`mdpf_category_registry.py:278` sets `member_id=e.model_key`. **The second hypothesis is
correct.** The map exists only for the two SMA members whose registry id genuinely differs
from their crosswalk key. **The design is coherent and I nearly filed it as broken.**

### 2.2 — WITHDRAWN #2: "two model members are orphans."
Reading a 6-item sample of `CANONICAL_MODELS`, `opal_fixed_income` and
`opal_global_all_equity_total_return` appeared to be in no crosswalk key tuple. **A SAMPLE IS
NOT A POPULATION.** `CANONICAL_MODELS` carries **11** keys; both are in it.

**MEASURED, denominator printed, negative control run:**

```
CANONICAL_MODELS model_keys      : 11
crosswalk KEYSPACE (union)       : 11
model-class registry members     :  9   <- DENOMINATOR
RESOLVES in a crosswalk family   :  9 of 9
NEITHER family (ORPHAN)          :  0 of 9
negative control 'bogus_model_xyz' in keyspace : False   <- the test CAN discriminate
```

**So limb 1 of the proposal — "resolves to a distinct crosswalk model_key" — HOLDS AT HEAD,
by construction, for every model member.** Combined with the id-uniqueness raise at `:376`,
distinctness is structural, not incidental.

---

## 3. THE RESIDUAL, AND IT IS REAL — *NOTHING ENFORCES THE INVARIANT THAT CURRENTLY HOLDS*

`member_id ∈ crosswalk keyspace` is true 9/9 **by convention**. No code asserts it. So a new
registration under an id that is NOT a crosswalk key passes **every existing guard.**

**EXERCISED against the original incident's own specimen** (the label a seat actually
misread), not a hypothetical:

```
candidate member_id       : 'opal_conservative_growth'
already in registry index : False   <- :376 id-unique assert PASSES
in CROSSWALK_IDENTITY_MAP : False   <- _build_identity_map iterates MAP ROWS; never sees it
in crosswalk keyspace     : False   <- ⛔ NOTHING CHECKS THIS
duplicates the real model : opal_long_term_conservative  (display 'Long Term', served=True)
```

**Every structural guard is green and the model is now registered twice under two ids.**
Direction of harm is the quiet one: AUA moves **out of Primary, into Custom** — a served,
client-facing number moving **down**, with no raise, `self_test` still `rc=0`.

⛔ **WHY THE EXISTING ASSERTS STRUCTURALLY CANNOT CATCH IT:** all three raises in
`_build_identity_map()` (`:557`, `:562`, `:568`) iterate `for row in CROSSWALK_IDENTITY_MAP`.
**Their domain is the map's rows. The hazard is a member that is ABSENT from the map.** A loop
over present rows cannot see an absent one. This is the add-a-row direction: an undercount
announces itself, an **overcount never does.**

---

## 4. THE RULING — what is owed, and what is explicitly NOT

**BUILD (accepted, narrowed to limb 1's enforcement):** an import-time assert in
`mdpf_category_registry.py`, beside `_build_identity_map()`, over the **model-class members**:

> every model-class `member_id` MUST be a key in the crosswalk's canonical keyspace
> (`CANONICAL_MODELS` model_keys), **or** carry an explicit off-crosswalk declaration with a
> reason. Violation → `RegistryError` **at import**, naming the id and both families.

**DO NOT BUILD (limb 2, deferred — and the reason is a rule, not a preference):**
a general `off_crosswalk` **field** on `CategoryMember`. `off-crosswalk` is **2 hits
estate-wide, both DOC band, 0 in code** (comp-find, 27,204 files scanned) — it has no carrier
today and **needs none yet, because the exemption set is currently EMPTY (0 of 9).** Adding a
field is a **Rule 24 schema act** (authoring a value axis) and would arrive owing a
four-postulate record. **Build the assert with NO exemption path; the first genuine
off-crosswalk model is the event that commissions the field, with its record.**
A field authored before its first member is an axis nobody can test.

**NOT A GATE.** This refuses a *malformed registration at import*. It does not gate a deploy,
a build, or a ship. Nobody needs approval from this office to land it.

---

## 5. WHAT THIS DOES **NOT** DO — the ship question stays shut

⛔ **THIS RULING DOES NOT LIFT THE D1_CATVIEWS NO-SHIP AND MUST NOT BE READ AS DOING SO.**
`build_package.py` states the NO-SHIP lifts only *"BY NAME (a COO/Andrew ship ruling, cited
here)."* **This is not that ruling.** See the separate finding on the interlock's stale
residual clause; the ship decision is a distinct act on a distinct record.

**A DISARM CONDITION BEING MET IS NOT A SHIP DECISION** — the same sentence my predecessor
wrote about Finding 2, now binding on Finding 3.

---

## 6. LANE + EVIDENCE

**Lane:** `data/mdpf/scripts/gold/*.py` is **DS-class under Rule 13** — not this office's to
commit. Cut as `D1_CATVIEWS.TO-F3-DS`. Seating is `0.0.0_AB_MSTR~Z`'s act; both prior
D1_CATVIEWS DS lanes closed out and are gone (**that was ASKED, not inferred from silence**).

**Acceptance is NOT the author's own measurement.** The control is a second seat's, per the
`:992` precedent: a positive arm (the `opal_conservative_growth` specimen above MUST raise)
and a negative arm (all 9 current members MUST still import clean). **Pin the specimen to an
immutable commit-ish** — a control whose member list comes from a mutable file is one peer
edit from becoming untestable, and nothing about it looks wrong when it silently passes.

| Claim | Evidence | Grain |
|---|---|---|
| limb 1 holds 9/9 | executed against `_INDEX` + `CANONICAL_MODELS` @`7805c21c12`, denominator + negative control printed | EXERCISED |
| invariant unenforced | `_build_identity_map` `:552-577` iterates map rows only; no keyspace check exists | source, read |
| specimen passes all guards | executed, the incident's own label | EXERCISED |
| `off-crosswalk` has no carrier | `comp-find -i "off-crosswalk"` → 2 hits, both DOC, 0 code, 27,204 files scanned | measured |

— `2.0.0_SA_COO~Z`, 2026-08-27
