# ANDREW-DIRECT 2026-08-28 ~14:0xZ — TWO RULINGS FROM ONE DASHBOARD LOOK

**Recorded by `2.0.0_SA_COO~Z` (issuer, `D1_CATVIEWS`). Both relayed verbatim by `1.0.0_SA_CTO~Z`
(msgs 13174, 13177), which received them at its terminal. Both arrived within ~10 minutes of the
13:50:50Z publisher write — i.e. from HIS OWN FIRST LOOK at the served cards.**

⛔ **THIS RECORD CAPTURES TWO CUTS THIS SEAT OWES. NEITHER IS DISPATCHED.** There is no live DS or DE
lane; seating is Andrew's call, not this seat's to assume. Recording them here so the rulings survive
the session that received them — a broker message is not a carrier.

---

## RULING 1 — `Alternatives` is out of L0 (CONFIRMS his 08-27 ruling, from his own eye)

> ⛔ **VERBATIM. Typos are his and are preserved.**
> *"Just checked the dashboard, we actually dont even need Alternatives either. It's really just Models
> SMAs and Client."*

**L0 = `Models` / `SMA` / `Client`.** `Alternatives` OUT. `Insurance` stays out.

⚠ **HE REACHED THIS INDEPENDENTLY, ~7 MINUTES AFTER THE ARMED ITEM WAS FILED, WITHOUT HAVING SEEN IT**
— *"just checked the dashboard"*. **The empty $0 card was visible enough to draw sovereign comment on
first look.** That is the cost of the seam, measured: it reached his eye before it reached a fix.

⛔ **HIS SENTENCE CONFIRMS THE DECISION, NOT THE TREATMENT.** It does not re-specify the mechanism and
must not be read as widening or narrowing the 08-27 scope.

### THE TREATMENT IS THE 08-27 RECORD'S, AND IT IS **NOT** THE INSURANCE PATTERN
`org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/ANDREW_DIRECT_20260827_REMOVE_ALTERNATIVES_FROM_L0.md`
```
registry / VIEW_TREE  "Alternatives LEAVES THE DECLARED L0 NODE SET"
                      DS-class -- data/mdpf/scripts/gold/mdpf_category_registry.py
emitted block         view_plane.peers stops carrying it     FOLLOWS the registry
renderer              NO CHANGE
smoke fixture         NODE + peer entry removed              DE lane, DONE @77d1bbce
```
>> **TWO EXCLUSIONS, TWO MECHANISMS, BOTH HIS. DO NOT COLLAPSE THEM.**
```
Insurance      STAYS in the node set; DISPLAY-ONLY; node, members and gold partition share UNCHANGED.
Alternatives   LEAVES the declared L0 node set AT THE REGISTRY. peers stopping is a CONSEQUENCE.
```
⚠ **`2.0.0_SA_COO~Z` GOT THIS WRONG ONCE ALREADY** — specified the Insurance pattern one paragraph
after quoting the table above. Corrected @`f82463700c`. **Data cost is nil either way today
(`aum 0.0, members 0` on all four scopes), which is exactly why nothing in the numbers would have
caught the substitution.**

### OWED CUT 1 — DS-class, `mdpf_category_registry.py`. Never cut. **That is this seat's failure.**
The 08-27 record NAMED the owner. `0.4.0_DE_ClientPlatform~Z` did its half and correctly flagged the
other as not its own. **The issuer did not cut the DS half.** Not a gap in the map — a gap between the
map and the issuer.

---

## RULING 2 — L1/L2 named constituents render ONLY if AUM is associated

> ⛔ **VERBATIM. Typos are his and are preserved.**
> *"Also sometng Iwould recommend is that named constituents at L1 and L2 only appear if there is AUM
> associated. if I am a client that does not have any Opal Fixed Income, i should not even se Opal
> Fixed Income in Custom Models."*

⚠ *"I would recommend"* is his idiom for a **product ruling**, not a musing.

**EXTENDS a principle L0 already implements** — the component's own *true zero → no card, never an
empty one* — down to L1 and L2. Same instinct as Ruling 1 ten minutes earlier: **he does not want to
look at categories that are not his.**

### ⛔ THE LIMB A NAIVE IMPLEMENTATION GETS WRONG (`1.0.0_SA_CTO~Z` ruling, 13177 §3)
>> **SUPPRESS ON *MEASURED ZERO*. NEVER ON *FALSY*.** Three states reach this predicate; one is his:
```
aum MEASURED and == 0            -> SUPPRESS.  His rule.
aum ABSENT / null / UNKNOWN      -> RENDER, in the `predicate === 'unavailable'` treatment. NOT his rule.
member absent from client data   -> nothing to suppress; it was never a node.
```
⛔ **`if (!node.aum)` COLLAPSES ALL THREE.** A null AUM is not a zero AUM, and suppressing on falsy
makes **a data defect and a legitimate empty look identical to the client** — the page renders
correctly while silently hiding the broken thing. The component **already has** an `unavailable`
treatment; the rule must route TO it, not around it.
⭐ **THE MECHANICAL TEST: SUPPRESSING A TRUE ZERO IS SUM-PRESERVING; SUPPRESSING AN UNKNOWN IS NOT.**
If the parent total stops reconciling after suppression, something that was not a zero was suppressed.
The existing `sums` block supports this check — `gold_plane` / `view_plane` / `total_aua` reconcile
today at **481,690,858.04** for cottonwood.

### OWED CUT 2 — `D1_CATVIEWS`, plane UNDETERMINED
⚠ **WHICH PLANE IS AN OPEN QUESTION AND IT IS NOT ANSWERED HERE.** L0 exclusions run PRODUCER-side
(`view_plane.excluded`), but a **per-client zero is a render-time fact about that client's holdings**.
⛔ **Do not assume it mirrors the Alternatives fix.** The decomp owes that call.
⛔ **SCOPE BOUND: he said L1 and L2. He did NOT reopen L0**, which he settled ten minutes earlier.
Relay verbatim; do not widen.

---

## TIMING — state this before anyone promises him sooner

⛔ **The producer writes ONCE DAILY at 13:50:50Z.** Anything landing today is visible to him
**TOMORROW at the earliest**, and only if it is producer-side. ⛔ **NO AD-HOC PRODUCER RUN** — it
writes a real artifact at the real key and destroys the scheduled-vs-adhoc discriminator
`TP1AE-AC1` exists to produce.

## STATE

| item | owner | status |
|---|---|---|
| Ruling 1 treatment | DS-class, `mdpf_category_registry.py` | **CUT OWED by `2.0.0_SA_COO~Z`. Not dispatched — no live DS lane.** |
| Ruling 2 | `D1_CATVIEWS`, plane undetermined | **CUT OWED by `2.0.0_SA_COO~Z`. Decomp owes the plane call.** |
| Seating | `0.0.0_AB_MSTR~Z` | **Andrew's call.** `3.0.0_SA_CVO~Z` and every Tier-2 lane are closed by his own act. |
