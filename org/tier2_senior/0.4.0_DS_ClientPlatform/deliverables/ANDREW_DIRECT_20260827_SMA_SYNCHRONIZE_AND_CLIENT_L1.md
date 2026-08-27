# ANDREW-DIRECT 2026-08-27 — SMA/Models/Client SYNCHRONIZATION + the Client L1 set

**Received by:** `0.4.0_DS_ClientPlatform~Z` (D1_CATVIEWS DS lane, Rule 27)
**Channel:** Andrew directly at this seat's terminal
**Time:** 2026-08-27 ~19:5xZ
**Context:** immediately following this seat's `/draw` of the `category-views` L0/L1/L2
structure, which reported the Models/Client vs SMA asymmetry as a measured finding.

> ⛔ **VERBATIM. THE PHRASING IS THE RULING — do not paraphrase this block.**

> *"I do not like that SMAs have a different path with no dollars, that is not right we need to
> synchronize these things. Also, Client should technically just be Opal Supervised and Opal
> Unsupervised. Eventually we can get into the fees and the client-supervised as opposed to
> opal-supervised derivations and etc., but im not sure yet how that will take shape so its not a
> priority at this stage."*

---

## RULING 1 — SMAs MUST BE SYNCHRONIZED WITH MODELS/CLIENT

**This SETTLES the fork `2.0.0_SA_COO~Z` put to him.** That fork was: *render SMA L1 without
dollars and say so on the surface, OR the emitter gains the field.* **He has rejected the
no-dollars branch in terms** — *"a different path with no dollars, that is not right."*
**Option 1 is dead; nobody should still be waiting on that fork.**

### ⛔ SCOPE IS NOT ADJUDICATED HERE — his sentence names TWO defects, not one

| | reading | what it changes |
|---|---|---|
| **A (narrow)** | `MdpfCategorySmaL1Node` gains `aum` | fixes *"no dollars"*. `l1_nodes` stays a positional array — the **path** stays different. |
| **B (wide)** | SMA adopts `children: Record<label, MdpfCategoryChildNode>` like Models and Client | fixes *"different path"* **and** *"no dollars"*. One mechanism across all three cards. |

**His sentence names the DIFFERENT PATH first and the missing dollars second, and asks to
"synchronize these things" — which reads toward B.** But that is an inference about scope, and
the receiving seat does not adjudicate scope (`org/XXX.md`). **Surfaced to `1.0.0_SA_CTO~Z`
(schema gate) and `2.0.0_SA_COO~Z` (decomp/seating) to rule.**

### WHAT IS INVARIANT ACROSS BOTH READINGS — and it is DS-class

Both readings require the same producer change, so it is not blocked on the scope ruling:

```
mdpf_gold_consolidator.py:566-578
    for key, entry in by_model.items():
        value  = _last((entry or {}).get("model_value"))
        member = registry.resolve_any(key)          # crosswalk id -> registry id
        elif member.view_path == "SMA":  sma_aum += value      # <- :577
```

**The per-strategy figure is ALREADY COMPUTED, per member, and discarded into a scalar at `:577`.**
Both A and B need it kept. `resolve_any()` already performs the crosswalk->registry identity
translation (49F's `by_model` keys SMAs as `opal_div_sma`/`opal_growth_sma`), so no new derivation
and no new source is required — this is **KEEP-vs-DISCARD**.

⚠ **The CONTRACT half is a schema act either way** — `1.0.0_SA_CTO~Z`'s gate, and it arrives at
`3.0.0_SA_CVO~Z` as a **Rule 24 authoring act** with a declared domain and a word-boundary token
census. **Cheaper to build is not smaller to certify** (`3.0.0_SA_CVO~Z`, 9863).

---

## RULING 2 — CLIENT L1 IS OPAL SUPERVISED + OPAL UNSUPERVISED

### ⭐ MEASURED AT SOURCE: THIS IS ALREADY TRUE IN THE EMITTED DATA. NO PRODUCER CHANGE IS IMPLIED.

`mdpf_category_registry.py`, the Client emit block:

```python
drawn = display_l1_nodes("Client")     # -> ['Client > Opal Supervised', 'Client > Opal Unsupervised']
...
for node_path in drawn:                # <- children are built ONLY from `drawn`
    kids[display_label(node_path)] = {"aum": ..., "view_path": node_path}
```

Measured this turn:

```
display_l1_nodes('Client')      -> ['Client > Opal Supervised', 'Client > Opal Unsupervised']
CLIENT children keys EMITTED    -> built from `drawn` only; Advised/Residual NEVER emitted as children
VIEW_TREE Client > *            -> Opal Supervised, Opal Unsupervised, Advised, Residual
```

**`Advised`/`Residual` exist only in the DECLARED node space (`VIEW_TREE`) and as the HELD advisory
axis, emitted under its own key for audit and explicitly NOT renderable as an L1 peer.** So his
word **confirms the shipped shape rather than changing it.**

### THE ONE QUESTION HIS WORD DOES NOT SETTLE — surfaced, not decided

Whether `Advised`/`Residual` should now be **removed from `VIEW_TREE` and the held-axis record
entirely**, or **remain held for audit**. Removing them would touch the **08-19 taxonomy gate**
(`D1_TAXONOMY_GATE_RULING_20260819.md`), which is `1.0.0_SA_CTO~Z`'s.

**This seat's read, offered as a read and not as a closure:** he said the fee and
client-supervised-vs-opal-supervised derivations are *"not a priority at this stage"* and that he is
*"not sure yet how that will take shape."* **A deferral is not a repeal**, and the held axis is
exactly the mechanism that keeps a deferred question auditable without rendering it. So the
default should be HOLD, not DELETE — but that is `1.0.0_SA_CTO~Z`'s call, not this lane's.

⛔ **DO NOT read "not a priority at this stage" as authorising removal of the held record.** The
double-count that `D1-inv-4` forbids is prevented by the axis being DATA on the node; deleting the
held axis to "simplify" would remove the mechanism, not the complexity.

---

## WHAT THIS DOES NOT CHANGE

**`D1_CATVIEWS` remains NO-SHIP** (`2.0.0_SA_COO~Z` `@0d08954d4c`). Nothing in this directive
addresses the ruling's actual basis — that the projection has never produced served output, so the
missing evidence is a RUN, not a READ. **A synchronized SMA path on an unpublished artifact is
still an unpublished artifact.**

`category-views` is still withheld from the consolidator's `ARTIFACT_TYPE_SCOPE_SET`, so the
accessor currently observes `unavailable` by design.

---

## STATUS AT THIS LANE

**Recorded and broadcast the same turn**, per `org/XXX.md` ("ANY AGENT RECEIVING AN ANDREW-DIRECT
INSTRUCTION RECORDS IT DURABLY AND BROADCASTS IT — SAME TURN"). Broadcast to `2.0.0_SA_COO~Z`,
`1.0.0_SA_CTO~Z`, `0.0.0_AB_MSTR~Z`, `3.0.0_SA_CVO~Z`.

**NOT self-assigned.** This lane holds `TO-F3-DS` (complete + accepted) and is otherwise idle; the
producer half is squarely DS-class and this seat can start it on a seat from `2.0.0_SA_COO~Z`, but
seating is theirs and the schema half is gated at `1.0.0_SA_CTO~Z`.
