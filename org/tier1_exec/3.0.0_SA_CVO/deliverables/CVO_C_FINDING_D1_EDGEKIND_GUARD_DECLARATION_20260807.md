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

## SWEEP — IS IT A CLASS OR A ONE-OFF? **ONE-OFF. And the bank comes out STRONGER.**

CTO~D left this open and neither of us should have. **The class is fully enumerable: the rule bank
contains exactly THREE `LIVE: N` population claims** (`grep -c 'LIVE: *[0-9]'` = 3, all in
`edgekind_semantic`). I tested all three against the census, not just the one that was found.

| # | claim | count | mechanism | verdict |
|---|---|---|---|---|
| 1 | `passthrough` — *"rename=false. LIVE: 337/961."* | **337 EXACT** | `rename == False` on **337/337 (100%)** | **HOLDS** |
| 2 | `rename` — *"rename=true. LIVE: 142/961 (== the rename-flag count — cross-checks)."* | **142 EXACT** | `rename == True` on **142/142 (100%)** | **HOLDS** |
| 3 | `recompute_guarded` — *"props.condition carries the guard. LIVE: 482/961."* | **482 EXACT** | `condition` on **23/482 (4.8%)** | **FAILS** |

**All three counts exact. Two of three mechanisms hold at 100% — and claim 2's own ADVERTISED
cross-check passes** (estate-wide `rename`-flag TRUE = 142 = the `kind=='rename'` count).

**And the bank's honest FORWARD declaration is also TRUE.** `:646` says *"EdgeKind not yet emitted on
PROP_PASSES -> forward (a producer step, not an ontology gap)."* Census of all **1382/1382**
PROP_PASSES: edges carrying a `kind` = **0**. Correctly declared.

> **VERDICT: the defect is ISOLATED, not systemic.** The bank is precise — it publishes exact counts,
> advertises a cross-check that actually passes, and declares an unpopulated element `forward` when it
> is unpopulated. **This raises confidence in the rail rather than lowering it, and narrows the remedy
> to a single line.** Verification should be able to CLEAR things, not only condemn them, and here it
> clears 3 of 4.

### THE DISCRIMINATOR — a generalizable property, extracted from the incident

**The two mechanisms that hold describe a MANDATORY field (`rename`, a boolean, always present). The
one that fails describes an OPTIONAL field (`condition`, nullable).**

> **A declaration that names a MANDATORY field as "carrying" something holds trivially. A declaration
> that names an OPTIONAL field as "carrying" something is the shape that can silently go unpopulated
> while its count stays true.** That is the class to check — not "rail declarations" in general.

## ⚠ SWEEP BY-CATCH — A MATERIAL CORRECTION TO THE SETTLED "LOCUS AT 961/961" FIGURE

Both CRO and CTO~D independently measured `via` (the file:line locus) at **961/961 on FLOWS_TO** and
concluded the locus is already universally present. **That is true of FLOWS_TO and false of the
population.**

**PROP_PASSES census, all 1382 — the complete props key population:**

```
attr        1382 (100%)
resolution  1382 (100%)
value       1382 (100%)
             ^^ NO `via`. NO locus. AT ALL.       negative control 'zzznotakey': 0
```

The rule bank itself binds **both** edge types to the same relation — `:139`
`derives-from: { binds_up: [FLOWS_TO, PROP_PASSES], carries: EdgeKind(...) }` — so both are
field-grain value flow.

| edge type | n | carries a locus? |
|---|---|---|
| FLOWS_TO | 961 | **yes, 100%** |
| PROP_PASSES | **1382** | **NO, 0%** |
| **field-flow total** | **2343** | **961 = 41%** |

> **961/961 is a PER-EDGE-TYPE figure being read as a POPULATION figure — and the edge type WITHOUT the
> locus is the LARGER one (1.4×).** Of 2,343 field-flow edges in the estate, **41% carry a locus.**
>
> **This does NOT revive the S-layer** — a missing locus on a producer is a population gap, not a
> missing ontology rung, and that conclusion is unchanged. **But it materially resizes the gap**, and
> it lands on a number that was about to go into a disposition as "already solved at 100%."
> `resolution` (the observer) *is* at 100% on both, so the observer half genuinely is universal; it is
> specifically the **locus** half that is not.

*(This is also the same denominator-scope error the estate's own doctrine names: a figure that is
complete over ONE edge type is not complete over the population, and the two are byte-identical when
the scope noun is dropped.)*

## FINAL PASS — the predicate applied, and a SECOND stale figure, drifting the OTHER way

CTO~D re-aimed the open item using the discriminator above — *"the sweep worth running is not 'all
rails' but every declaration naming a nullable field"* — a much smaller and better-aimed denominator
than a rail-wide audit. Applied:

**The whole at-risk set is THREE declarations** (`grep -c 'props\.'` = 2, plus `:303`'s named-field
population claim). All three measured against the 961 census:

| line | declaration | measured | verdict |
|---|---|---|---|
| `:322` | *"the graph SERIALIZES `props.kind` as `recompute/guarded` (slash)"* | live values are exactly `passthrough`/`rename`/`recompute/guarded` | **HOLDS** |
| `:303` | *"884/961 FLOWS_TO carry a non-null `dstField`"* | **961/961** | **STALE — the gap CLOSED** |
| `:321` | *"`props.condition` carries the guard. LIVE: 482/961."* | 23/482 (4.8%) | **FAILS** |

**I audited my own predicate before claiming a ratified figure had moved**, because here I was the
likely source of error: `dstField` key absent **0**, `None` **0**, empty string **0**, literal `"null"`
**0**, whitespace-only **0** — **961 real values across 386 distinct strings**. And the control: **the
same predicate on `condition` returns 23**, so it is not a predicate that always passes. The bank is
internally consistent at its own vintage — `884 + 77 = 961`.

### F-5 — A DECLARED COVERAGE GAP HAS SILENTLY CLOSED, AND THE RECORD STILL SHOWS IT OPEN

`:330` `coverage_boundary` — *"**77/961 FLOWS_TO carry no dstField** — coarser-than-field flow; grain
read as artifact."* **Measured today: 0/961. The 77-edge gap is CLOSED.**

**This is a different failure from `:321`, and the direction is what makes it matter.** `:321`
**overstates** capability. `:330` **understates** it — **a reader planning work off the bank today
would scope a 77-edge field-grain remediation that no longer exists.** That is the second time in this
engagement a stale figure would have driven unnecessary build work; the first was the S-layer itself.

### THE SHARPER DISCRIMINATOR — **STAMPED vs UNSTAMPED**, and it beats mandatory-vs-optional

| block | vintage-stamped? | outcome |
|---|---|---|
| `:301` `edge_grain_binding` | **YES** — `# denominators printed (comp-kuzu 2026-07-23)` | `:303` is stale **but HONEST** — it tells you when it was true. **Not a defect.** |
| `:326` `coverage_boundary` | **NO** | `:330` has gone **FALSE** and says nothing about when it was measured |
| `:318` `edgekind_semantic` | **NO** | `:321` **FAILS**; `:319`/`:320` happen to still hold |

> **BOTH errors live in the two UNSTAMPED blocks. The one STAMPED block ages honestly.**
>
> **A published figure with a measurement vintage degrades into a dated fact. The same figure without
> one degrades into a false statement — in whichever direction the estate happens to move.** Stamping
> does not keep a number true; it keeps a number *honest about being old*, which is the only property
> a hand-copied denominator can actually hold.

**This is CLAUDE.md's own frozen-not-live class**, one rail over — the same reason that file refuses to
print a comp-tool count and defers to the gate that maintains it.

**Refinement to the gate candidate CTO~D is taking to Andrew** (theirs to propose, not mine to build):
key it on **an unstamped population figure**, not only on a nullable-field mechanism claim. The two
predicates catch different things and both are cheap — *nullable-field* catches a claim that was
**never** true; *unstamped* catches a figure that has **stopped being** true. `:321` is the first,
`:330` is the second, and only the union catches both.

**And credit where the bank earns it: none of this would be checkable if it did not print its
denominators in the first place.** The practice that exposed three drifted figures is the same
practice that makes the rail auditable at all, and the stamping convention works exactly where it is
applied. **The remedy is to extend an existing good habit to two blocks that lack it — not to install
a new one.**

## SCOPE BOUND — stated so it is not over-quoted

**Edge types swept: `FLOWS_TO` (961, census) and `PROP_PASSES` (1382, census).** Both complete, not
sampled. **95.2% is a FLOWS_TO figure; 41% is a FLOWS_TO+PROP_PASSES figure.** Neither is an estate
figure over *all* edge types — `RENDERS` (2447), `READS_FIELD` (2110), `HAS_FIELD` (4269) and the rest
are **unswept**, and I make no claim about them.

*Fence note, continuing my disclosure: 5 of the 14 files carrying a populated guard are
AdvisorIntelligence surfaces. I recorded only counts and paths, used no ADVI content as a vocabulary
example, and this finding is about a rail declaration rather than rail authorship. Disclosed because an
undeclared corpus is indistinguishable from a breached one.*

— 3.0.0_SA_CVO~C
