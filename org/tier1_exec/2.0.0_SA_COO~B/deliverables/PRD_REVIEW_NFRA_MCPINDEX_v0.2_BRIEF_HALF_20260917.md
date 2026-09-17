# L4-R REVIEW -- NFRA_MCPINDEX PRD v0.2, BRIEF half -- REFUSE, additive, brief-half-only

**Reviewer:** `2.0.0_SA_COO~B`, in `4.0.0_SA_CRO`'s stead. Routing re-read by this seat at review time, not taken from
the delivery: `prd-signoff.py status NFRA_MCPINDEX` -> brief "OWED BY 2.0.0_SA_COO~B (no live CRO session; COO in its
stead)". (One earlier read, taken while this lane's heartbeat had lapsed past 120 s, routed the half to the CRO base
instead; the routing follows liveness and flipped back on the next heartbeat.) This lane does not hold NFRA_MCPINDEX's round.
**Delivered as:** msgs 97689 and 97691 from `1.0.0_SA_CTO`, 2026-09-17T22:53Z / 22:55Z.
**Reviewed object:** `org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md` @`59f6f001b1`, by `git show` at that pin
(224 lines), read in full. `half_hash` as delivered: `c1d819248340`.
**Against:** `docs/briefs/opal-mcp-tool-index-brief-20260917.md` @`826ac6925a`, by `git show` at that pin (216 lines), read in full.
**Instrument:** both documents read whole by this seat; then a fixed-string census of 30 brief terms over the PRD text.
`2.0.0_SA_COO~G`'s v0.1 review read the named writer's own bytes; this review reads the COVERAGE claim against the PRD's
bytes, so the two do not repeat each other.

## Verdict

**REFUSE.** What v0.2 set out to fix, it fixed: C1 now states the single-writer contract as an obligation with a census
bar, Scope no longer asserts a writer, and the ten outcomes are carried as cards. None of that is reopened here. The
refusal is on the section this half exists to check. BRIEF COVERAGE (`:194-199`) is one six-line paragraph. It has no
heading denominator and no per-heading disposition, it makes one claim the bytes contradict, and four brief items that
each decide a cell are in the PRD nowhere. Every correction below lands in the brief half (BRIEF COVERAGE, Scope and
evidence boundary, SURFACE MANIFEST, Ground truth, Acceptance matrix, Canonical handoff); none needs ENDPOINT or CONTRACTS.

## 0. The denominator is absent

The brief carries **20 headings** at `826ac6925a`, every line matching `^#`: **1 H1 + 9 H2 + 10 H3** (the ten outcomes
O1-O10). Census: `heading` 0 hits in the PRD. The paragraph accounts for three groups (ten outcomes, nine preconditions,
six non-claims) and is silent on ANDREW'S WORDS, PART II, PART III, PART IV's nine findings, PART VI and REFS. NFRA_SPMOVE
v0.2/v0.3 (@`55fc495feb`, same author, same day) is the working shape: one row per heading, CARRIED / CARRIED-AS-OPEN /
NOT CARRIED with the reason, then the PART V and PART VII maps item by item.

## 1. "Its six non-claims are carried into the evidence boundary" (`:199`) -- measured 2 of 6

The evidence boundary (`:66-69`) carries VII.1 (no AWS state, sizes and timings unmeasured) and VII.2 (common questions
not enumerated). The other four:

| brief | the non-claim | PRD census | what it decides |
|---|---|---|---|
| VII.4 `:196` | Bloomberg on-demand is the SITEZ standing read; NOT claimed reachable from the laptop fabric | `SITEZ` 0, `laptop fabric` 0 | **FWD-8's market-data half, S10 and A8 on a project whose fabric is `laptop`.** A8 asks for "one market-data answer". If that read lives on the other fabric, the outcome is not provable by an act a laptop seat can take on demand, which is the Rule 27 defect the CTO re-cut LGIC_CANON FWD-5 for today (record @`57a15b2bbe`). L5 cannot see the question from this PRD. |
| VII.5 `:197` | citations are the research passes' reads, not re-verified line by line | `re-verified` 0 | Every PART IV file:line the PRD repeats is CLAIMED, not MEASURED. This is the exact class v0.1 was refused on (a header's claim inherited as fact), so it is the non-claim most worth carrying. |
| VII.6 `:198-199` | the scoping record recommended D6 and business-first names; Andrew overruled both; the record is research, not direction | `scoping` 0, `business-first` 0, `overruled` 0, `2a7fc3339f` 0 | The research record is the brief's stated foundation (`:6-7`) and so is on L5's reading list. Without this line a decomposer can take overruled direction from it. The record's path and pin are not in the PRD at all. |
| VII.3 `:194-195` | the tool-naming rule is the CRO seat's READING of his answer | half-carried | C3 carries "the schema does not grade tool names" and then RULES the rule binding. The CTO may rule; what is missing is the label that the rule is inferred from "Refer to LGIC naming", not spoken by him. |

## 2. PART V -- two of nine land on nothing

- **V.4 (`:168-169`)**: "Every new tool classified in `destructive_ops` and `data_entitlement`; the pinned tool-count tests
  move with each tool." Census: `destructive_ops` 0, `data_entitlement` 0, `tool-count` 0, `pinned` 0. C2 and A11 say
  "a safety classification" and name neither registry, and nothing tells a worker that adding a tool breaks pinned count
  tests. That is a guard a consuming cell needs on its face.
- **V.8 (`:173`)**: the coverage paragraph lists "the standing integration checklist" as where V.8 lands, which is the
  precondition naming itself. `NFRA_INTEGRATIONS_STANDARD` 0 hits; no contract, surface or acceptance row holds
  s.6 / 8.1. It needs a home (S4/S5/S10 each add an integration) or an explicit NOT CARRIED with the reason.

## 3. PART IV -- two findings that decide S3 and C7 are absent

- **Finding 6, second sentence (`:151-152`)**: "Served advisor intelligence for Inflection and Cottonwood lives in firm
  buckets, not the portal bucket." Census: `Inflection` 0, `Cottonwood` 0, `firm bucket` 0. C5 has a portal-backed tool
  read "the same precomputed table the portal reads", and C7 fences read roles "to exact silver prefixes". For advisor
  intelligence those two do not meet: the table is not silver and not in the portal bucket. A role that reads a FIRM
  bucket is a different grant with a different control on it. Measured by this seat today on one such bucket and offered
  as evidence, not as this PRD's claim: `opal-data-49financial`'s bucket policy `DenyForeignFirmPrincipals` denies `s3:*`
  to `role/cot-*`, `role/inf-*`, `role/mdpf-*` and `role/opal-assets-mdpf-*`
  (`infra/aws/terraform/mdpf-pipeline/iam.tf:598-603`); the Inflection and Cottonwood buckets' policies were NOT read.
- **Finding 5 (`:147-149`)**: the precomputed sources by name (`platinum/mdpf`, `platinum/etfs`, `platinum/advi`,
  `json/*`) and silver's shape (one parquet per table per scope per business day). Census: `platinum` 0, `json/` 0. S3 is
  "per-surface readers over the portal's precomputed tables" and names no table family, so A2's "per portal surface" has
  no denominator to be counted against.

## 4. PART III -- the beta bar is dropped

`:119-120`: "each admitted person's first week produces a list of questions the index could not route -- that list is
the next round's analysis input." Census: `first week` 0, `unrouted` 0. It is the mechanism by which VII.2 ever closes
and the input S8 runs on after the first property; S11 and A9 cover admission and removal only.

## Checked and NOT refused on

- The ten outcomes map one-to-one to FWD-1..FWD-10, and the PART II boundary is restated in Scope, including all six
  "explicitly not" items.
- PART IV findings 1, 3, 7, 8 and 9 are in Ground truth. Finding 3's "transactions and the `fact_*` tables are not yet
  exposed" is carried only as "three `dim_*` tables only" (`fact_` 0 hits); FWD-3 promises transactions, so one clause
  naming the unexposed tables is worth adding in the same bump.
- Finding 2's `catalog_gate.py` (0 hits): the serve/deny gate already exists behind one route; S2 should say whether it
  reuses it. The author's judgment.
- V.5's dependency is carried in Canonical handoff (`:222-224`), not "at FWD-3" as the paragraph says. A pointer fix.
- C1's re-cut is sound as a brief-half matter; whether it is right AS A CONTRACT is the ratified-text half's read.

## Push state

Stated in the message that reports this stamp, as a measured value.
