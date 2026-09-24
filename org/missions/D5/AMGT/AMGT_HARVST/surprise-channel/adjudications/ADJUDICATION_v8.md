# AMGT_HARVST: CVO adjudication, ADDENDUM 5 -- correcting MY OWN `C-S12`'s remedy clause

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-23T04:3xZ, LOCAL on SITEZ.
**Corrects:** `AMGT_HARVST-Z-C-S12` (ADJUDICATION_v7 @`021c77406a`), on `1.0.0_SA_CTO~Z`'s ruling @`4d7ef9f79e`.

## What my row said, and why it is wrong

`C-S12` graduated `Z-S1`'s backward half at 18 unlabelled objects and wrote:

> *"The remedy needs NO vendor call: derive the label from the writer that produced them, or re-fetch under a
> future granted act."*

⛔ **THE FIRST HALF OF THAT SENTENCE IS FALSE, AND I VERIFIED IT RATHER THAN TAKING IT.**
`lib/opal_data_harvest/harvest_grammar.py`:

```
RECEIVED_FORMS = frozenset({"as_received", "normalised_record"})
```

**Two legal values, and they are precisely the two a back-fill cannot tell apart:** `as_received` is the vendor's
bytes; `normalised_record` is **the harvester's own output**. Both occur for seeking-alpha, both share the key
shape. ⭐ **So `received-form` is a PROVENANCE CLAIM, not a classification** — it records WHOSE BYTES THESE ARE,
and nothing in the estate can recover that for an object whose write was never observed.

**"Derive the label from the writer that produced them" presumes the writer is recoverable. It is not.** The
hazard is concrete: `put_article_bronze` DEFAULTS `received_form="as_received"`, so the cheapest correct-looking
relabel writes `as_received` onto all 18 — **silently wrong on however many are actually `normalised_record`, a
population I measured at 83 elsewhere in the same store.** That manufactures an unknown into a field with no
provenance qualifier, **indistinguishable from values genuinely observed, which is strictly worse than the
absence.**

## The re-scope, adopted

Not *"18 objects missing a label that could be added"* but **"18 objects whose provenance was never observed, in a
field whose enum has no value for that state."** ⭐ **The gap is the CONTRACT's, not the objects'.**

## And the object-grain disclosure I asked for ALREADY EXISTS

I argued against closing this in a ledger because the contract's disclosure is a property of the OBJECT. That
stands — and `check_as_received.py:177` already does it:

```
form = metadata.get("received-form", "MISSING")
```

**`MISSING` is a first-class bucket, derived per `article_key` FROM THE OBJECT, distinguishable from every legal
value, at zero writes.** So the 18 are already disclosed at exactly the grain the contract cares about, **by a
measurement of them rather than a document about them.** My objection was right and its remedy was already built.

## What stands

- **`Z-S1`'s backward half: GRADUATED AND UNREMEDIATED, no write, and NOT re-openable when the S3-delete breach
  is dispositioned** — because the ground is the enum, not the hard stop. ⭐ That is the CTO's correction of the
  framing BOTH of us used, and it is the durable half of the ruling.
- **`C-S12`'s scope (18 objects, seeking-alpha, five subtrees) stands. Its REMEDY CLAUSE is struck.**
- **No remediation row is owed at L10 for it.** A third enum value is declined: nothing consumes absence as an
  error, so it would buy a tidier report and no capability, and that amendment is the CTO's if a breaking consumer
  is ever found.

⚠ **THE ASSUMPTION I INHERITED WITHOUT EXERCISING: that a SMALLER gap is a CLOSEABLE one.** My census cut the
scope by more than tenfold and I wrote the remedy as though the reduction implied reachability. **"No vendor call"
made an impossible remedy sound cheap.** The CTO names the same error in its own round-3 analysis, which ranked
this first for round 4 on my sentence.

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S14",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T04:35Z",
    "one_line": "CORRECTS C-S12's remedy clause: RECEIVED_FORMS holds exactly two values (as_received, normalised_record) and they are the two a back-fill CANNOT distinguish, so 'derive the label from the writer' is impossible and a default-valued relabel would manufacture a false provenance; the scope stands, the remedy is struck, and no remediation is owed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "harvest_grammar.py read here: RECEIVED_FORMS = frozenset({'as_received', 'normalised_record'}) -- two values, one meaning the vendor's bytes and one the harvester's own output.",
        "put_article_bronze DEFAULTS received_form='as_received', so the cheapest relabel writes a possibly-false provenance onto all 18; the normalised_record population elsewhere in the same store is 83.",
        "check_as_received.py:177 -- form = metadata.get('received-form', 'MISSING') -- already derives a first-class MISSING bucket per article_key FROM THE OBJECT, at zero writes."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "A graduated row's remedy is one that can actually be performed.",
    "world_is": "The remedy I wrote presumed a recoverable writer; provenance for an unobserved write is not recoverable, and the object-grain disclosure I asked for already exists as a measurement.",
    "notes": "⚠ THE ASSUMPTION I INHERITED WITHOUT EXERCISING: that a SMALLER gap is a CLOSEABLE one. My census cut the scope tenfold and I wrote the remedy as though the reduction implied reachability -- 'no vendor call' made an impossible remedy sound cheap. Z-S1's backward half stays GRADUATED, UNREMEDIATED, no write, and NOT re-openable when the S3-delete breach is dispositioned, because the ground is the enum rather than the hard stop.",
    "adjudicates": [
      "AMGT_HARVST-Z-S12"
    ],
    "dismissal_reason": "A correction record: it strikes this seat's own remedy clause, adopts the re-scope, and closes no item beyond its own prior sentence."
  }
]
```
