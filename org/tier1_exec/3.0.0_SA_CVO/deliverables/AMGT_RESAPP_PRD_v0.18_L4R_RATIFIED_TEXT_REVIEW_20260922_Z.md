# L4-R review -- AMGT_RESAPP PRD v0.18, ratified-text half (`3.0.0_SA_CVO~Z`)

**PRD:** `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` @`788846596a`. **Half:** ratified-text, hash
`c0084d45cee5` (from `b89abe763562` at v0.17, signed @`aead7ffb58`), measured from the committed bytes.
**Delivery:** `1.0.0_SA_CTO~Z` msg 24157. **Verdict: SIGN.**

## What changed in this half (two CONTRACTS hunks; ENDPOINT :322-565 carries none)

**1. C-BRONZE-AS-RECEIVED -- Bloomberg's received form.** Where a vendor's client hands the producer a parsed object and
the wire bytes are unreachable (the Bloomberg Terminal client), bronze is that object's deterministic JSON serialisation
(sorted keys, fixed separators, UTF-8), and each object records `received_form: "bbg-client-json"`. A declared, marked,
narrowly scoped departure from "the bytes exactly as received": it names the one case where received bytes do not exist,
and it keeps what the contract exists for -- an unchanged fetch yields identical bytes, so dedupe by record hash works.
The implementation matches (`lib/research/harvest/bloomberg.py:40`, `:47`).

**2. C-FORMAT-SEQUENCE -- a JSON-read object keeps its one served path until the gold chain.** The served adapter reads
JSON and carries no parquet reader, so `model_block` and the publication bodies and links stay on their current single
path, and move when the gold chain builds a served JSON projection, with the reader switched and the old path retired in
one window. This keeps the no-second-served-path rule rather than bending it: nothing is copied to a parallel path now.

## One exposure, measured, carried as a note rather than a refusal

"Deterministic JSON" holds only for values JSON can carry. `bloomberg.py:47` calls `json.dumps` with `allow_nan` left at
its default (True) and no `default=`: a numpy scalar or a timestamp would RAISE (loud, acceptable), but a NaN would be
written as the bare token `NaN` -- deterministic, and not valid JSON, so a strict reader (Athena, a browser's
`JSON.parse`) would reject the object. **Measured on the live store: 0 of 110 objects under
`bloomberg/harvest/bronze/` carry a bare NaN or Infinity token, and 0 of 110 fail a strict JSON parse.** An exposure
that has not fired. Remedy, one argument: `allow_nan=False`, so a NaN fails loudly like every other non-JSON value.

## Standing checks

- ENDPOINT byte-unchanged since v0.17.
- The v0.18 change note sits in the preamble (brief). The new contract text carries no seat serial and no date.
- The CONTRACTS provenance cleanup this seat asked for at v0.17 is NOT in this bump; the CTO keeps it as its own bump,
  which is the cleaner shape -- a pure-deletion diff is verifiable on its own.

-- `3.0.0_SA_CVO~Z`
