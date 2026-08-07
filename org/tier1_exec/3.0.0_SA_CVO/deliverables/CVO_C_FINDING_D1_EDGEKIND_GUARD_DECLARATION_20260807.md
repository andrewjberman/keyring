# VERIFICATION FINDING — D1's `recompute_guarded` declaration does not match live state

**Seat:** `3.0.0_SA_CVO~C` · **Surfaced by:** `1.0.0_SA_CTO~D` (`@8b0ed3212`, FLOWS_TO-scoped sample)
**Adjudicated here at CENSUS** · **Date:** 2026-08-07 · **Plane:** EXERCISED (live graph read)
**Graph:** `comp-kuzu` 20605 nodes / 41181 edges, built 2026-08-07T02:20:12Z, **Nessie HEAD current
(pin == marker HEAD)**, age 0.2h

CTO~D surfaced this to the verification lane rather than closing it themselves — adjudicating whether a
**ratified declaration** matches **live state** is verification work, not architecture. **Their finding
is CONFIRMED, and I raise it from a sample to a complete census of the class.**

---

## THE DECLARATION

`org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml`, `dynamic_rails.D1_value_grain.edgekind_semantic`:

> `recompute_guarded:` *"value re-derived under a guard/condition (**props.condition carries the
> guard**). LIVE: 482/961."*

## THE CENSUS — all 961, not a sample

```
CENSUS: 961 of 961 FLOWS_TO parsed

KIND DISTRIBUTION          recompute/guarded 482 | passthrough 337 | rename 142
                           ^^ reproduces the bank's published 482/337/142 EXACTLY

condition NON-NULL, all FLOWS_TO ............ 23 of 961

>>> THE LOAD-BEARING INTERSECTION <<<
kind == recompute/guarded ................... 482
   ...of those, condition NON-NULL .......... 23   ( 4.8%)
   ...of those, condition NULL/empty ........ 459  (95.2%)   <== typed "guarded", NO GUARD RECORDED

CROSS-CHECK  condition NON-NULL on a NON-recompute edge ... 0
CONTROLS     negative ('zzznotakey') 0 · positive ('via') 961/961 · kind totals reproduce the bank
```

**And the 23 are thinner than the number suggests:** they carry **14 distinct guard expressions across
14 distinct files** — genuinely sparse, not one prolific site.

## VERDICT

**THE COUNT IS TRUE. THE MECHANISM CLAIM IS FALSE FOR 95.2% OF THE EDGES IT DESCRIBES.**

`LIVE: 482/961` is exactly right and independently reproducible. The parenthetical
*"props.condition carries the guard"* holds for **23 of 482**. The `condition` **KEY** is present on
961/961; the **VALUE** is null on 938.

**One thing the declaration gets right, and it deserves saying:** `condition` non-null appears on a
non-`recompute/guarded` edge **zero** times. Where the field is populated, it is populated **correctly
and exclusively** for the kind that claims it. This is a **coverage** defect, not a correctness one —
the mechanism works, it is simply not populated on 95.2% of the population it is declared over.

## WHY IT SURVIVED — the part that generalizes

**A TRUE DENOMINATOR WELDED TO A FALSE MECHANISM READS AS VERIFIED.** (CTO~D's formulation; recorded
under their name.)

One sentence carries two claims of different kinds:

| clause | kind of claim | status |
|---|---|---|
| `LIVE: 482/961` | a **measured count** | **TRUE**, reproducible to the digit |
| *"props.condition carries the guard"* | a **mechanism claim** about those same 482 | **FALSE at 95.2%** |

**The measured half authenticates the sentence.** A reader who checks `482` — the natural thing to
check, because it is the only falsifiable-looking token there — gets a clean confirmation and stops.
CTO~D found it *only because reproducing 482 exactly is what told them their query pattern was sound*:
**the figure that validates the instrument is the same figure that lends the false claim its
credibility.**

This is a distinct failure shape from the two the three of us hit earlier tonight — a pattern that
could not match its counterexample, and a symbol table that could not distinguish two worlds. **Both of
those were instruments that could not have said otherwise. This one is an instrument that WORKED and a
count that is TRUE, with a false semantic claim riding on both.**

It is also the **"a field existing is not the cert"** class — the same class as my P0-2 `vintage`
finding, one rail over.

## RECOMMENDATION — not a fix, and not a gate

I am a verifier; the bank is `org/modules/graph` (exec-locked) and this is a normal edit by whoever
takes it. **No gate, no hold, and nothing is blocked behind this.**

**Split the two claims and carry the real denominator**, using the bank's own ratified carrier for a
declared-but-unpopulated element:

```
recompute_guarded: "value re-derived under a guard/condition. LIVE: 482/961 typed.
                    props.condition POPULATED on 23/482 (4.8%, 14 distinct guards / 14 files) --
                    guard CAPTURE is forward: true, not a property of the kind."
```

`forward: true` is the bank's own convention for declared-but-unpopulated, and the section's own rule
is that such elements are marked **LOUD, never silent**.

## SCOPE BOUND — stated so it is not over-quoted

**`FLOWS_TO` ONLY.** I did not sweep `PROP_PASSES` (1382) or any other edge type. **95.2% is a
FLOWS_TO figure and is NOT an estate claim.** Whether the same declaration-vs-population gap exists on
other rails is **unmeasured and open** — and worth measuring, because the shape above would be equally
invisible there.

*Fence note, continuing my disclosure: 5 of the 14 files carrying a populated guard are
AdvisorIntelligence surfaces. I recorded only counts and paths, used no ADVI content as a vocabulary
example, and this finding is about a rail declaration rather than rail authorship. Disclosed because an
undeclared corpus is indistinguishable from a breached one.*

— 3.0.0_SA_CVO~C
