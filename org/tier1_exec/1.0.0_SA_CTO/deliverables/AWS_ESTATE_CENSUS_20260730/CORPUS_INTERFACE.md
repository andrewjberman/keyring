# CORPUS INTERFACE — the contract for consumers of RULINGS_LEDGER + SEMANTIC_NOTES

**Why this file exists:** Andrew's ruling 6 (2026-07-30, via CVO) made the estate-report pipeline's
corpus **user input / tribal knowledge**, not git activity — and named two examples that are both
this program's capture (the ETFS-canonicality confusion with its in-conversation resource
enumeration; the `opal-data-mdpf` decommission intent), described as *"literally quotes from me and
cto conversation summarized."*

**Consequence: these files stopped being my notes and became an INTERFACE.** `0.7.0_AE_CloudOps~B`
is building against them. This document declares what they may rely on — and, honestly, what they
may not.

## 1. What the corpus is

| Artifact | Content | Grain |
|---|---|---|
| `20_rulings/RULINGS_LEDGER.jsonl` | one JSON object per line, append-only | one ruling / finding / execution |
| `20_rulings/SEMANTIC_NOTES/s3_buckets.md` | Andrew's verbatim + normalized fields + instrument delta | one resource |
| `20_rulings/SEMANTIC_NOTES/ddb_tables.md` | same | one resource |
| `00_framework/ONTOLOGY_CLASSES.md` | the recurring knowledge-kinds | one class |

**The high-signal payload is `ruling` (verbatim-carrying) and `basis` (who said it, when, where).**
A consumer wanting *"what did Andrew actually say"* reads those two.

## 2. Guaranteed fields — present on 116/116 rows as of 2026-07-31

`ts` · `id` · `type` · `ruling` · `business_function` · `basis` · `instrument_delta_class` · `executed`

- `ruling` — free text, often carrying **Andrew verbatim in quotes**. The primary payload.
- `basis` — provenance. **Distinguishes SOVEREIGN VERBATIM from DELEGATED CTO annotation** (C-17).
  A consumer must not treat a delegated annotation as something Andrew said. The string
  `Andrew-verbatim` / `Andrew-direct` marks the former; `Andrew-DELEGATED` marks the latter.
- `instrument_delta_class` — the ontology payload; **null on 39/116 rows** (legitimately: not every
  row carries a delta). Non-null on 77.
- `executed` — null when nothing was done; otherwise the evidence string.

## 3. DECLARED INSTABILITY — read this before building

**(a) `sits_at` and `scope` are on 97/116 rows, NOT all.** They were added mid-session (2026-07-30
~19:0xZ) when canon alignment landed. The 19 earlier rows lack them. **Consumers must treat both as
optional.** I will not backfill: backfilling would restamp rows whose authorship moment did not
include those fields, which is the frozen-map/mtime-lie class this program exists to name.

**(b) `type` is an OPEN VOCABULARY and it grew organically — 36 distinct values across 116 rows**,
including compound forms (`semantic-note+ruling`, `intake+verdict`, `ruling+finding`,
`finding-correction`). **Do not switch on `type` exhaustively.** Match on substring or treat unknown
values as generic. A consumer that enumerates types will break on the next append.

**(c) Append-only, never rewritten.** Corrections arrive as NEW rows that retract earlier ones (see
the retraction rows). **A consumer must not assume the latest row about an `id` is the only one** —
read all rows for an id and honour the most recent. This is deliberate: the retraction trail is
itself evidence.

**(d) `id` is human-authored and NOT a stable key.** It is descriptive, sometimes long, occasionally
carrying a resource ARN or a parenthetical. Do not use it as a join key; match on substring.

## 4. SEMANTIC_NOTES structure

Per resource: a `## <n>/<total> <resource-name> — <headline>` heading, then `**Verbatim:**` (Andrew's
exact words), then `**Normalized:**` (business_function / target_state / action), then optionally
`**Delta:**` or `**Instrument delta:**`. Batches are separated by `# Batch N` headings.

**The verbatim block is the tribal-knowledge payload.** It is the thing Andrew's ruling 6 is asking
for and it is the field a consumer should extract first.

## 5. CADENCE, and the load-bearing weakness

**The canonical repo is `C:\Users\AndrewBerman\Desktop\OPAL_WORLD_MODEL\` and IT HAS NO REMOTE.**
The fabric reads a mirror at
`ajb_workspace/org/tier1_exec/1.0.0_SA_CTO/deliverables/AWS_ESTATE_CENSUS_20260730/`, refreshed by a
**manual CTO copy step**.

> **Therefore MIRROR CADENCE = CORPUS FRESHNESS, and the mirror is refreshed by a person.**
> A daily automated pipeline whose primary feed is behind a hand-run copy has a person in its
> critical path. That is a person-shaped control — *care, not a control* — and it is now
> load-bearing rather than merely inelegant.
>
> **The fix is a remote on the canonical repo. OPEN AT ANDREW, raised four times, now blocking a
> daily pipeline rather than an agent's read.** Until it lands, a consumer must check the mirror's
> commit date and treat it as the corpus vintage — never assume same-day.

## 6. Change protocol

Consumers of record: `0.7.0_AE_CloudOps~B` (estate-report pipeline), `0.7.0_AE_CloudOps~*` (TAP
lanes, T6 join). **CTO notifies both before any change to guaranteed fields (§2), the notes
structure (§4), or append semantics (§3c).** Additive fields need no notice; removals and renames do.
