# ANDREW-DIRECT 2026-09-12 ~17:4xZ -- the five key tensions and the grid restatement: "These work i like it"

**archetype:** SCRIBE (record)
**Channel:** the `4.0.0_SA_CRO~D` terminal, direct to this seat. **Recorded by:** `4.0.0_SA_CRO~D`.
**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Status:** LAW-SHAPED DIRECTION RULED. ⛔ **NOTHING MOVES. NOT A MIGRATION AUTHORIZATION.** The
~16:1xZ pause is UNCHANGED. Method authority: his ~17:2xZ instruction (`b65a7225a2` s.3) that key
tensions settle with the CRO before the brief, each as a RULE or an acceptable RANGE.

---

## 1. THE WORDS, VERBATIM AND COMPLETE

> **"These work i like it"**

⛔ **THAT IS THE WHOLE OF WHAT HE SAID**, answering the tension set this seat put to him in-terminal
minutes earlier: one wording defect in the ratified grid, five tensions (two proposed as RANGES, three
as RULES), and a list of already-ruled items named so neither party re-opens them.

## 2. HOW "THESE" IS READ, STATED SO IT CAN BE NARROWED

*"These"* is read as **the set, as proposed** -- every item below carries the resolution this seat
put forward, unaltered. Each item is enumerated separately so that **any one is revertible on his
word without disturbing the others.** This seat did not widen any proposal between putting it and
recording it; the text below is the text he read.

---

## 3. WHAT IT RULES, ITEM BY ITEM

### 3.0 THE GRID RESTATEMENT (a defect in this seat's own card 2 of ~17:0xZ, found by `1.0.0_SA_CTO`, 96216)

**WAS:** client-confidential + derived -> *"ALL FOUR TIERS, IN THE FIRM BUCKET. MANDATORY."*
**NOW:** client-confidential + derived -> **bronze and silver in `opal-data-assets`, unchanged; gold
and platinum in the firm bucket. MANDATORY.**

The literal "all four" contradicted his 2026-08-25 ~17:55Z word, Rule 17b at `dd9b33de65`, and this
seat's own closure that client silver home is settled. The CTO's reason for insisting it be fixed in
the grid rather than glossed: *"a canon whose correct reading requires three other documents is not
yet a canon."* The 2x2 as ratified at `ed3f6b32e4` s.2 is read with this restatement from now on.

### 3.1 T1 -- TENANCY vs PIPELINE SHAPE: a RANGE keyed on ATTRIBUTABILITY

**The tension:** his ~13:0xZ word *"there should be some layer where they are accrued in
opal-data-mdpf. that is effectively the gold layer"* and his ~17:0xZ grid (client-confidential -> firm
bucket) named different homes for the same bytes. Measured: 13 per-firm MDPF platinum objects
written 2026-09-12 into the shared bucket (`d35653da5e` s.2). `1.0.0_SA_CTO` (96216) named the same
axis from the gold end: IRPT's Holdings tab, three firms' slices, one view.

**RULED -- the RANGE:**
- A slice **ATTRIBUTABLE to one firm**, at ANY grain (account, relationship, or firm-level aggregate),
  is that firm's data: **firm bucket, gold AND platinum, MANDATORY.**
- A **CROSS-FIRM COMPOSITE not attributable to any one firm** (a "global" row, a de-identified
  aggregate): **product bucket gold, `opal-data-portal-v2` platinum, PERMITTED** -- with the
  de-identification basis written as an entry in the exception register.
- The product pipeline's **CODE** lives in the product bucket regardless (Rule 17b); a product
  pipeline therefore writes to N+1 homes (its own, plus one per attributable firm slice).

**Consequence stated, not acted on:** the 13 objects at `platinum/mdpf/{49financial,cottonwood,
inflection}/` are firm-attributable and therefore classified VIOLATION for the ledger. `1.0.0_SA_CTO`'s
IRPT accrual spec (`SPEC_IRPT_GOLD_ACCRUAL_MDPF_20260912.md` @`ac3915c7eb`) is, by its author's own
read, indifferent to this answer except for its home and its `firm_id=` partition. **Nothing moves.**

### 3.2 T2 -- WHAT "RECOMMENDED" PERMITS FOR GENERAL PIPELINES: a RULE with one free axis

**The tension:** `opal-data-etfs` carries silver/gold/platinum in its own bucket (476/60/38 objects,
all live), not in assets. Under *"bronze and silver in assets every single time"* that is a violation;
under *"rule of thumb"* it is fine. A sweep cannot tell which.

**RULED:** for GENERAL data the **tier law holds wherever a tier exists** (raw bronze; parquet silver
and gold; JSON only at platinum; one JSON producer per served key), **and bronze still lands in
`opal-data-assets`** so the estate keeps one ingest spine -- **but everything above bronze may live
in the product bucket, with a declared reason in the exception register.** The alternative ("bucket
axis fully free for general data") was offered and not taken.

**Consequence stated, not acted on:** `opal-data-etfs/silver/` and `/gold/` and `/platinum/` are
CONFORMANT under this rule once their reason is declared; its bronze home is a ledger question (its
bronze planes were not found outside assets in the census, so likely already conformant -- UNVERIFIED).

### 3.3 T3 -- ONE SOURCE FEEDING BOTH CELLS: a RULE

**The tension:** a source served raw (Pathfinder holdings, his word) that a derived product also
consumes; the grid is per-USE and one source can sit in two cells.

**RULED:** the tier obligation is set by the **MOST DERIVED CONSUMER**. The raw serve is a separate,
declared route from bronze; it does **not** exempt the derived path from silver -> gold -> platinum.

### 3.4 T4 -- WHERE BRONZE AND SILVER CODE LIVES: a RULE (this was a gap, not a collision)

**The gap:** Rule 17b homes gold code with gold; nothing homed ingest and silver code. Measured:
`code/bronze/` and `code/silver/` planes in `opal-data-bd`, `-cot`, `-inf`, `-mdpf`; one `code/bronze/`
in assets.

**RULED: ONE CODE HOME PER PIPELINE**, in the product or firm bucket beside the gold code. Reason
carried from the 2026-08-25 incident (three seats hand-deriving "which copy of this code runs"): a
pipeline's code split across two buckets re-creates it. The alternative (code beside its data under
`assets/code/{vendor}/{scope}/`) was offered and not taken.

### 3.5 T5 -- BACKUPS, SCRATCH AND PROBES INSIDE TIER PLANES: a RULE

**Measured:** ~15,000 objects -- `opal-data-inf/backup/gold_canonical_PRE_REDERIVE_20260713T1012Z/`
(8,805), `opal-data-inf/_pre_rebuild_backup/20260630T234458Z/silver/` (6,060), eleven `_probe/*`
planes in assets, tool scratch.

**RULED: NEVER inside a tier plane.** A `_backup/` root outside the grammar (or a separate bucket);
every entry dated, with an expiry.

---

## 4. ALREADY RULED -- named in the same set so neither party re-opens them

No dual-write (his complete veto; MDPF_CANON *"the move and the re-shape are ONE act"*). Gold is
parquet. Silver in assets. A vendor MASTER is a valid scope (0824/0833). Firm spellings resolve
through the identity spine (outcome O4). D10-3 deferred until a heavy case. **Unchanged by this
record; listed for coverage.**

---

## 5. WHAT THIS DOES NOT RULE

1. **NO MIGRATION.** Every "consequence stated" above is a LEDGER CLASSIFICATION, not a move. NEVER#3
   unchanged. The pause is unchanged.
2. **D14's title** -- still open between "ontology" and "canon" (`b65a7225a2` s.2a, as corrected).
3. **The six-outcome set and the one-project-with-migrations-separate structure** -- not yet ratified;
   they were redirected behind the tensions, which are now settled. The brief is next.
4. **Per-scope D10-1 ticks** -- still return to him via the tick-list (outcome O2).

## 6. WHAT HAPPENS NEXT

With the tensions settled, `/brief-create` runs at this seat (Rule 27: L1 is `4.0.0_SA_CRO` only). The
brief carries every ruling above as RATIFIED LAW cited to this record, `ed3f6b32e4`, `e29a895ce3`
and `b65a7225a2`, and its Part IV names the tensions as FINDINGS with their measured basis so the PRD
does not re-buy them.
