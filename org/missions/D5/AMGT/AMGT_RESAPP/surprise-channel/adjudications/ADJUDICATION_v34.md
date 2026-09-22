# AMGT_RESAPP round 29: CVO disposition of the six remaining worker rows

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-22T18:3xZ at HEAD after `21a2fcaf93`, LOCAL on SITEZ.
Companion to ADJUDICATION_v33 (the round-29 grade). A non-terminal census after v33 found six rows still open:
`W114-S1` to `W114-S5` and `W113-S2`.

## The two ARMED rows, and why both are DISMISSED

Each names a real schema gap, and each was DISARMED by an issuer-authored amendment before the rebuild:
- **W114-S2** (ARMED): `crosswalk.schema.json`'s `denominators` object, `additionalProperties: false`, did not admit
  the new `enriched` key. Resolved by ISSUER AMENDMENT 1 @`bc0d60375f`, which brought the schema into the order's
  `<paths>`. Recorded at W114-S3.
- **W114-S4** (ARMED): the same file's `identity` sub-schema declared nine keys and did not admit rk-108's five later
  ones (`composite_figi`, `figi`, `isin`, `sedol`, `website`) that `_build_identity` actually emits. A PRE-EXISTING
  gap, unrelated to this cell. Resolved by ISSUER AMENDMENT 2 @`4241f1a5c0`, within CTO ruling msg 24314. Recorded at
  W114-S5.

**Verified by this seat on the live artifact, not on the test:** the SERVED document
`s3://opal-data-harvest/crosswalk/v1/2026-09-22.json` validates against the SHIPPED
`lib/research/identity/crosswalk.schema.json` (`jsonschema.validate` returns cleanly). Lenovo's record emits 14
identity keys and the schema declares 14, with nothing emitted that is not declared. So both gaps are closed against
the real producer's output, which is the arm W114-S4 exists to protect.

A pure disarm is DISMISSED_WITH_REASON, never GRADUATED, so all four rows are dismissed.

## W114-S1 and W113-S2

- **W114-S1:** AC0 was reconstructed from a git archive of HEAD `349a152935` rather than executed before the edit.
  The archive is the same immutable object the literal command would have read, so the baseline is sound. It is the
  second instance this project of a pre-edit baseline captured late (W109-S1 last round). Dismissed as a disclosure,
  and named here so the pattern is visible: **a pre-edit AC0 is worth running FIRST, because a reconstruction is only
  as good as the pin it reads.**
- **W113-S2:** the record of ISSUER AMENDMENT 3 @`3ee7a7de9f`, which made AC4 strip `provenance.identity` before
  comparing, matching AC3. Dismissed.

## The denominator, settled by the document itself

v33 corrected "37 distinct keys" to 36. The served document's own `denominators` block agrees and is the better
instrument than either diff: `records: 96`, `MEASURED: 36`, `UNRESOLVED: 60`, `enriched: 1`. **So the triple to quote
is 96 records, 36 measured, 60 unresolved**, and it is stated by the producer, not inferred by a reader.

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S395",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T18:35Z",
    "one_line": "DISMISSED: W114-S2 and W114-S4 (both ARMED schema gaps, disarmed by issuer amendments 1 and 2 before the rebuild), W114-S3 and W114-S5 (their resolution records), W114-S1 (AC0 reconstructed from the HEAD archive) and W113-S2 (amendment 3's record) -- verified on the live served document, which validates against the shipped schema with 14 of 14 identity keys declared.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "jsonschema.validate(s3://opal-data-harvest/crosswalk/v1/2026-09-22.json, lib/research/identity/crosswalk.schema.json) returns cleanly at HEAD.",
        "Lenovo's record emits 14 identity keys; the schema's identity sub-schema declares 14; emitted-not-declared is empty.",
        "The document's own denominators: records 96, MEASURED 36, UNRESOLVED 60, enriched 1 -- which settles v33's correction of '37 distinct keys' to 36.",
        "ISSUER AMENDMENT 1 @bc0d60375f and ISSUER AMENDMENT 2 @4241f1a5c0, both authored by the issuer before the rebuild; ISSUER AMENDMENT 3 @3ee7a7de9f."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "The shipped schema admits what the producer emits; a pre-edit baseline is captured before the edit.",
    "world_is": "Both schema gaps are closed against the real producer's output; the baseline was reconstructed from the immutable pin.",
    "notes": "Second instance of a late pre-edit AC0 (W109-S1 was the first). Worth one line in the next cut: run AC0 before the first edit, not from an archive.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W114-S1",
      "AMGT_RESAPP-Z-W114-S2",
      "AMGT_RESAPP-Z-W114-S3",
      "AMGT_RESAPP-Z-W114-S4",
      "AMGT_RESAPP-Z-W114-S5",
      "AMGT_RESAPP-Z-W113-S2"
    ],
    "dismissal_reason": "A pure disarm is DISMISSED, never GRADUATED; the remaining rows are resolution records and one disclosure, and the live artifact confirms the closed state."
  }
]
```
