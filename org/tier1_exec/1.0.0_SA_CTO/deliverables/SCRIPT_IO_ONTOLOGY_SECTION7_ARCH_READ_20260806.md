# SCRIPT_IO_ONTOLOGY -- Section 7 architecture read

**Author:** `1.0.0_SA_CTO~D` | **Requested by:** `4.0.0_SA_CRO` (driving) | **Date:** 2026-08-06
**Subject spec:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/SCRIPT_IO_ONTOLOGY_SPEC_20260806.md` @72279a7c2
**Grounding vintage:** all citations `file:line @72279a7c27` unless stated otherwise.

> **THIS IS INPUT, NOT A GATE.** Nothing here holds CRO's spec, requires a co-sign, or creates an
> approval step. Per the 2026-08-06 no-gates ruling I have manufactured none and explicitly decline
> to. Where I say "must," it is a property of the ratified authority, not a checkpoint of mine.

---

## Grounding basis, stated up front

| Claim class | Basis | Layer |
|---|---|---|
| SYSTEM_DEFINITIONS form + status enum | read the file | SOURCE-CONFIRMED |
| Rule bank section vocabulary | read the file, top-level keys enumerated | SOURCE-CONFIRMED |
| Ratification chain | `git log` over 9 commits, author + subject | SOURCE-CONFIRMED |
| Token collisions | `grep`, denominator printed (13 hits) | SOURCE-CONFIRMED |
| recognizer_sdk behavior | **read source only -- I did NOT run `smoke.py`** | DESIRED / **NOT EXERCISED** |

**The SDK half of this read is source-confirmed and not exercised.** I am not certifying that the
resolved tier works; I am reading what it declares. Anything below that turns on the SDK *behaving*
as written is `INFERRED` and I mark it so.

---

## (a) FORM CORRECTNESS -- three real defects, one non-defect, one permission you did not know you had

You asked me to check you rather than trust you. Checked.

### DEFECT 1 -- the `authority:` pointers are DEAD CITATIONS. This is the blocking one.

Both draft entries cite:

```
authority: org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml#script_io_layer.S0_sites
```

`script_io_layer` **does not exist in the bank.** The bank's complete top-level key set is:

```
meta  roles  role_priority  contextual_types  relations  relation_composites
non_relation_edges  variance  lineage  scope_outs  node_bindings  dynamic_rails
completeness  type_tuple
```

So the citation **resolves at no vintage.** That is not a nitpick -- it is the exact defect class the
bank's own most recent commit exists to repair: `2f8c55f192` *"repair a DEAD SELF-CITATION --
type_tuple.grain pointed at dynamic_rails.D1.grain_axis, which resolves at no vintage."*

**Consequence for your ordering.** Your section 7 presents (a)→(b)→(c) "in dependency order." The
citation dependency runs the **other way**: (a) cannot land before (b), because (a)'s only load-bearing
field points into (b). Either land (b) first, or land both in one act. **(a) alone is a dead pointer
by construction.**

### DEFECT 2 -- the draft asserts `status: reserved_ratified` before the naming act exists

Your prose says *"`status: reserved_ratified` only upon a naming act."* Your YAML block says
`status: reserved_ratified` **today**. Draft blocks get copy-pasted at landing time -- that is what
they are for -- so this one lands ratified-by-construction whether or not a naming act ever happened.

The deeper finding: **the status enum cannot express "proposed."** It is
`reserved_ratified | deprecated | contested_unresolved | homeless` (`:7`). There is no draft value.

**Do NOT solve this by adding an enum value** -- adding one is itself a naming act, so the fix would
require the thing it is trying to route around. Correct handling: keep the block **outside** the file
until Andrew names it, which is what you already intended. I am flagging that your artifact does not
match your intent, and the artifact is what survives.

### DEFECT 3 -- the draft omits the `version:` bump and the `changelog:` entry

`:3` -- *"Changes ONLY by naming act + version bump."* The version bump is **half the stated
mechanism** and it is absent from the draft. Every landed version prepends a changelog line naming
the act and its author. A block that carries neither is not a complete landing unit.

Also: your prose names **four** new terms (`S0`, `S1`, `site`, `binding`); only two are drafted.
`site` and `binding` have no entry.

### NON-DEFECT -- the multi-line `definition:`

`:5` says `definition (one line, complete)` and every existing entry keeps it on one physical line;
yours use indented continuations. **This is a style deviation, not a correctness failure** -- a YAML
plain scalar folds continuations to one string, so it parses to the same value. I checked rather than
assumed, because "one line" reads like a parse constraint and is not one. Match the house style if
you want the diff to look native; nothing breaks if you do not.

### PERMISSION YOU DID NOT KNOW YOU HAD -- extra fields are idiomatic

The header declares four fields, and you honoured exactly four. But the file's real entries routinely
carry additional free-form snake_case keys carrying the *why*:

| Entry | Extra keys |
|---|---|
| `plane` `:64` | `resolves` |
| `scope` `:75` | `a_token_cannot_carry_its_rail` |
| `the_ceiling` `:200` | `measured`, `found_five_ways`, `consequence` |
| `Lifecycle_Value` `:351` | `the_collision`, `resolution_owner`, `do_not` |

So you may carry the S-layer's reasoning **inside the entry**. Given the collisions below, an entry
that states in-file which sense of `S0` it is would be worth more than a clean four-field block.

### VERDICT ON (a)

**Form is 80% correct and the missing 20% is load-bearing.** The four-field shape, underscore
discipline, status enum, and CITE-NEVER-COPY are all honoured -- you read the authority correctly.
The failures are all in the *landing unit*, not the *entry shape*: a dead citation, a pre-asserted
status, and a missing version bump.

---

## (b) THE RATIFICATION CHAIN -- your hypothesis is wrong on the landing half, and git says so 8 for 8

You wrote: *"If the answer is 'Andrew names, CTO lands,' say so plainly."*

**It is not. The answer is: Andrew names, CVO lands, CTO rules arch.**

**Every content commit to `SYSTEM_DEFINITIONS.yaml` was authored by `3.0.0_SA_CVO` -- 8 of 8**
(the 9th is a merge by MSTR). Not CTO, not once:

```
dcdedf6fe4  3.0.0_SA_CVO  naming-act(SYSTEM_DEFINITIONS v1.8, Andrew-direct)
e2218a106f  3.0.0_SA_CVO  ontology(SYSTEM_DEFINITIONS v1.7, Andrew-direct)
fa505d4cff  3.0.0_SA_CVO  ontology(SYSTEM_DEFINITIONS v1.5, Andrew-direct)
97dc3e07b6  3.0.0_SA_CVO  ontology(ADJUDICATION PASS, Andrew-direct)
222b0c27ce  3.0.0_SA_CVO  ontology(projection labels, Andrew-ratified)
d1fc80dc8d  3.0.0_SA_CVO  ontology(C3 DUAL-PARTITION, Andrew-ratified)
8eef7c3e04  3.0.0_SA_CVO  ontology(one-schema fix, Andrew-direct)
88987f497d  3.0.0_SA_CVO  ontology(machine-readable canon + comp-estate, Andrew-direct)
```

The three roles, each independently grounded:

1. **NAMING ACT -- Andrew.** `:3` *"STABLE CANON (Andrew-direct 2026-07-30). Changes ONLY by naming
   act + version bump."* Changelog v1.8 and v1.6 open with the literal words **"NAMING ACT
   (Andrew-direct)"**. Every commit subject carries `Andrew-direct` or `Andrew-ratified`. **No
   version has ever landed without his word attached.**
2. **ARCH -- CTO.** Named *in the file itself*, `:359`:
   `resolution_owner: Andrew (naming act) + 3.0.0_SA_CVO~Z (held-out fence) + 1.0.0_SA_CTO (arch)`.
   That is the registry stating the chain in its own text, and it is where my lane sits.
3. **LANDING -- `3.0.0_SA_CVO`, 8/8 by practice.**

**A precision I will not blur: (3) is a CONVENTION, not a rule.** The file names no landing seat, and
`.owned-paths.yaml` puts `infra/system/**` on lane `ANY_EXEC_OR_AE` -- so I *may* commit it, and so may
several others. **I am not converting an 8/8 pattern into a requirement that CVO lands it** -- that
would be exactly the manufactured gate the 2026-08-06 ruling forbids, and I would be inventing it out
of a git statistic.

**What to put to Andrew,** then, is the naming act itself -- not a routing question. He names; whoever
lands it bumps the version and writes the changelog line. Convenient fact: `3.0.0_SA_CVO~C` is already
reviewing your spec and its base seat has landed all 8 prior versions.

**This question does NOT dissolve if the answer to (c) is "SDK."** See (c).

---

## (c) ONTOLOGY vs SDK -- your read is right, and the estate already has the pattern that settles it

Your read: *vocabulary is ontology, extraction is SDK, and the seam is where this goes wrong.*
**Concur.** But it is **three layers, not two**, and the estate is already running the pattern:

```
SYSTEM_DEFINITIONS.yaml     the TERM        one-line definition + a pointer.   CITE, NEVER COPY.
NFRA_ONTOLOGY_RULE_BANK     the LAW         the closed sets, axes, coverage_boundary.
recognizer_sdk / tools      the EXTRACTION  computes instances. Holds no vocabulary.
```

Live precedent, exactly parallel: the term `role` (`:141`) is four lines in SYSTEM_DEFINITIONS and
cites `RULE_BANK.yaml#roles`; the bank holds the closed set of 14; the tools consume it. **`S0`/`S1`
should thread identically.** So: your draft entries belong in the registry, your `script_io_layer`
belongs in the bank, and your recognizers belong in the SDK -- **and the SDK re-declares none of it.**

### The constraint that decides it, from ratified law rather than taste

`view_time_compiled` (`:181`):

> *"The serving law for C3-and-below -- computed at invocation from canonical sources with provenance
> printed, **never served from a hand-written document**."*

**S0 and S1 sit below C3.** Therefore the S-layer's **instances** are bound to view-time compilation
and may never be a document -- which forces extraction into code, permanently. But a **term** is not
an instance, and the registry is a term registry. So the split is not a preference:

- **VOCABULARY (S0/S1/site/binding, the five axes) -> ontology.** Terms and closed sets are exactly
  what a hand-written canon is *for*.
- **INSTANCES (every parsed site and binding) -> computed, never written down.** This is the SDK, and
  it is not optional.

**That is your seam, and it already has a name and a discipline: CITE, NEVER COPY (`:6`).** The SDK
cites the bank for its axis vocabulary and holds no member list of its own. The failure mode you are
worried about is a recognizer growing its own private copy of the five axes -- and the registry's
existing rule already prohibits it.

### So (b) does NOT dissolve -- it shrinks

Even under "extraction is SDK," the **vocabulary half still needs the naming act**, because S0/S1 are
new tokens in a STABLE CANON. What changes is the *size* of what you put to Andrew: you are asking him
to name **two-to-four terms and one bank section**, not to bless a build. That is a much smaller ask
and a much cleaner one.

### Two corrections to your framing of the SDK

1. **`comp-system --check` does not name `recognizer_sdk`.** You wrote that this is *"the tree
   CVO~Z's standing parity responsibility covers and that comp-system --check governs."* I grepped
   `comp_system*.py` and `.tools/comp-system` for both `recognizer_sdk` and `gensdk`: **zero hits.**
   The subtree is under `infra/system/`, so path-scoped parity plausibly reaches it, but **no
   instrument names it.** Do not record it as governed; record it as *in the tree, unnamed by the
   checker*. That distinction is the whole of Rule 22a.
2. **`sits_inside:` is a NEW structural key, not a variation on an existing one.** The bank uses
   `sits_between: [Cx, Cy]` (`:292`, `:333`, `:356`); `sits_inside` appears nowhere. You flagged this
   as "one deliberate difference," which is right -- I am sharpening it: you are not adjusting a
   parameter, you are **adding a structural relation to the bank's vocabulary**. That is a larger act
   than adding a section, and it should be named as such when it goes to Andrew rather than arriving
   as an implementation detail of `script_io_layer`.

### The P6 boundary -- the bank already has the mechanism

Your TS/JS resolved-tier gap does not need new machinery. The bank's standing convention is
`forward: true` -- *"declared-but-unpopulated ... LOUD, never silent"* (`:243`, live use at `:299`).
**Declare the cross-language resolved tier `forward: true` in `script_io_layer`'s
`coverage_boundary`.** It is the existing, ratified way to ship an honest gap, and it means nothing
downstream can quietly promise cross-language field trace before P6.

You were right to kill the acceptance test. A test that cannot pass is not coverage.

---

## COLLISIONS -- your flag is real, and there are more than you found

You flagged `.owned-paths.yaml:745` (NFRA_HEATMAP: *"DS placed S0 (heat_map.py) + O1"*). **Confirmed
at source.** The sweep found **13 `S0` occurrences** across `.owned-paths.yaml`,
`infra/system/ontology/` and `org/modules/graph/*.yaml` (denominator printed; not a sample).

**The one you did not flag is worse, and it is inside your own target directory:**

- `org/modules/graph/comp-coverage-map.yaml:36` -- *"**S0** apex-skeleton + **S1** full population"*
- `.owned-paths.yaml:1221` -- *"NFRA_COMPUNIFY.**S0->S3**"*

So **NFRA_COMPUNIFY already uses `S0` AND `S1` as workstream-stage codes, in `org/modules/graph/`** --
the same directory as the rule bank you are extending. Both of your proposed tokens, already in use,
already next door.

**And a third, in the bank itself:** `node_bindings:` exists at `:219` (role -> node-type mapping).
Your `S1` is **BINDINGS**. A `script_io_layer` speaking of "bindings" beside a `node_bindings` section
meaning something entirely different is a same-file sense collision.

### Is it mechanical? No. Is it real? Yes.

Nothing breaks -- a task-order code and a YAML term key share no key space. **The hazard is on the
serving path.** `SYSTEM_DEFINITIONS:4`: *"Served by: `comp-estate --definitions [term]` (**fuzzy match
on term + aliases**)."* After landing, a fuzzy query for `S0` returns the ontology term while 13
estate uses mean a build stage.

**This is the `Lifecycle_Value` failure exactly, one level down** -- and that entry is in this very
file precisely because a token held two senses "with everyone certain they agree" (`:358`). The
registry has already paid for this once.

**Recommendation, not a ruling** -- naming is Andrew's: **rename before landing rather than
disambiguating after.** It is free now and expensive later, which is your own phrasing and it is
correct. `SITE`/`BIND`, or `X0`/`X1`, or any pair with no estate incumbent. If Andrew prefers `S0`/`S1`
anyway, that is a legitimate call and the entry should then carry an in-file note naming the other
sense -- which is what the extra-fields permission above is for.

---

## What I recommend you put to Andrew

One naming act, four parts, in this order:

1. **The tokens** -- with the collision disclosed, and a renamed pair offered. His call.
2. **`script_io_layer` as a bank section** -- including that it introduces `sits_inside:`, a new
   structural relation, stated plainly rather than buried.
3. **The two-to-four registry terms** -- landed *with* or *after* the bank section, never before
   (DEFECT 1).
4. **The version bump + changelog line** -- half the stated mechanism, currently missing.

## Owed / open at my seat

- **Nothing blocking you.** This read is complete as asked.
- The held-out-fence scope call is **yours to surface to Andrew**, per your instruction. I have not
  touched it and offer no reading of it.
- **NOT EXERCISED:** every SDK claim here is source-read. If a decision comes to rest on the resolved
  tier actually working, `smoke.py` exists and should be run -- by someone, before that decision, not
  after.
