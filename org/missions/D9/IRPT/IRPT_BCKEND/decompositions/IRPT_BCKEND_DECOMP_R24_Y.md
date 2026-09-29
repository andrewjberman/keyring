# IRPT_BCKEND round 24 -- workstream ~Y (Analysis) decomposition

Issuer `2.0.0_SA_COO~Y`, 2026-09-29 ~20:4xZ. Trigger: `1.0.0_SA_CTO` decision 103026, which placed the manual walk-2
backend and ruled three items to this lane -- *"~Y: W2-04/05 names from the model catalog + etf-classifications, no
external lookup; W2-06 correction words on the status wire; W2-07 is S206/S218."* Source: ~D's state table
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/walk-v2-state-table-20260929.md` @f80d019a6c (W2-01..22
against PROD `ba8e971f` / DEV `5068973b`).

## The rectangle, and what is NOT cut

| item | ~Y's half | this round |
|---|---|---|
| **W2-06** | the correction words on the status wire (`job_detail` -> words) | **CUT: `IB-yr-241`** |
| **W2-04 / W2-05** | one resolve/catalog read served to the page (Opal model catalog + etf-classifications ticker -> name) | **NOT CUT -- unmet dependency, named below** |
| **W2-07** | the cause of the needs-attention state | **NOT CUT -- already covered, named below** |

**W2-07 is already in flight and is not re-cut.** The CTO maps it to S206/S218. `IRPT_BCKEND-S206` is CONFIRMED on the
current build (`IRPT_BCKEND-S215` @b902e33b15), and S218's observation step is round 23's `IB-yr-231`, which is
complete, graded 4 passed and awaiting drain. Cutting it again would be cutting for coverage.

**W2-04/W2-05 are NOT cut this tick, and the reason is now MEASURED, not merely unknown.** The item needs two
sources joined. The Opal model catalog half is in hand and verified by this lane at 16:4xZ:
`generate/templates.json` `comparison_catalog.entries`, 4 entries, CRLF-normalized sha256 `54656584`, each carrying
`key`, `label` and `security_id`, three of four `live_proven: true`.

The **etf-classifications half exists but is the wrong instrument for a ticker -> name lookup**, and the numbers say
so. From `2.0.0_SA_COO~M`'s census `deliverables/IRPT_MVP_M/ETF_CLASSIFICATIONS_COVERAGE_20260928.json`, over the
`gold/canonical/holdings/2026-09-25.parquet` partitions:

| source | items | cot tickers covered | bd tickers covered |
|---|---|---|---|
| `etf_classifications` | **285** | 179 of 847 = **21.1%** (39.7% of MV) | 228 of 1449 = **15.7%** (68.1% of MV) |
| `bd_securities` | **10,837** | 817 of 847 = **96.5%** (77.8% of MV) | 1,383 of 1,449 = **95.4%** (73.7% of MV) |

`etf_classifications` is a CLASSIFICATION table, and it knows roughly one ticker in five. A comparison row named from
it would be unnamed for about four holdings in five -- which is the very defect W2-04 exists to fix. `bd_securities`
covers about 95% of the same tickers.

**This is a CTO decision, not an issuer amendment,** because 103026 named the source: *"names from the model catalog
+ etf-classifications"*. Asking before cutting is cheaper than cutting a cell that cannot serve its outcome. Sent
with the numbers above. `IB-yr-242` is cut on that answer, and if the answer is to proceed with what exists, the
cell states its own coverage ceiling on the face so no one later reads an unnamed row as a bug.

## The cell

| cell | item | outcome served | risk | worker | depends on | checks (base dry-run at CLOUD HEAD) |
|---|---|---|---|---|---|---|
| `IB-yr-241` | **the status wire carries WORDS, not only a code.** A non-terminal or attention-bearing Analysis request serves, alongside `state` and `public_reason_code`, a short human correction sentence derived from the SERVER's own `job_detail` / finding -- so `ProspectJobStatus` has something to show and `OwnedRequestHistory` need not print "Open it to see what to change" on every row. The words are SERVER-derived and enumerated; no free text, no vendor material, and no new state | FWD-4 (a user who is told to correct something is told WHAT) | WORLD (the served status envelope gains a field; no existing field changes) | `~85` | none -- `job_detail` already carries the code, proven live in W24 | `R24_CHECKS/test_r24_y1_correction_words.py`: `serves_words_for_a_known_code` FAIL, `unknown_code_degrades_safely` FAIL, `existing_envelope_unchanged` PASS (control) |

**Why this cell and not a page mapping.** The state table offers two seats for W2-06: the words on the wire
(IRPT_BCKEND) or a page mapping (DSGN_IRPTV1). The CTO chose the wire, and the evidence from today supports it: W24's
two jobs ended `SESSION_REFRESH_ALREADY_USED`, a code a user can do nothing with, and W22/W24's three normalization
stops ended `RESOLVE_RETRY_EXHAUSTED` whose only stated remedy is `REPLACE_FILE` -- which rows `IRPT_BCKEND-S206` and
`IRPT_BCKEND-S215` show is the WRONG remedy for that code. A page mapping would hard-code that wrong advice into the
front end. The server knows which it is; the page does not.

**What it must NOT do.** No new row state, no change to `state` or `public_reason_code`, no free-text passthrough of
an exception body, and no vendor identifier, cookie or URL -- the `refusal_line()` discipline and the closed-token
lesson from `IB-yr-231`'s `named_line()` both hold. An unknown code degrades to the existing behaviour rather than
inventing advice.

Edges: none; `IB-yr-241` is a single independent cell. **fanout: 1 of 1 chains, cap 8.** Slot: measured per S197 at
this write.


## Amendment 1 (2026-09-29 ~21:2xZ) -- W2-04/05 is UNBLOCKED and cut as `IB-yr-242`; the rectangle is now 2 cells

Two CTO decisions closed the two open questions this round carried. Both are recorded here because an inbox is not a
record.

**Decision 103035 -- no substitution, and the degrade path is ruled.** The ticker -> name half stays on
etf-classifications: *"Andrew is retiring bd-securities, so a new reader of it is the fork he named."* That is a
reason this lane did not have, and it overrides the coverage argument -- a 95%-coverage source is worthless if
reading it creates a fork Andrew has forbidden. The gap is instead `MDPF_SECCLASS`'s first need, backfilled through
the FWD-7 scheduled path with bd-securities as reviewed INPUT only. **The rule for this cell:** a ticker
etf-classifications lacks **shows its ticker verbatim with no name, never "Comparison N"**.

**Decision 103038 -- shape B, on this lane's recommendation.** `_contracts/ResolvedScope.schema.json` is
`additionalProperties: false` with 12 properties and 9 required, and the composer documents the gap itself
(`GenerateComposer.tsx:20-25`: ResolvedScope v1 *"carries no catalogue of selectable comparisons"*), so the catalogue
could not be added quietly. Of the two homes -- (A) a v1->v2 contract change on a ratified schema, or (B) a sibling
scoped GET -- **B is ruled**, because the catalogue is page PREFILL rather than scope or entitlement, it moves no
ratified contract, and A would re-open the L4-R halves.

**`IB-yr-242` conditions, verbatim from 103038:** the route sits under the existing
`/api/scoped/investor-reporting/` family **behind the same authz guard and tenant check**; it gets **its own new
`_contracts` schema (v1, `additionalProperties: false`)** and the portal validates against it; **any new resource name
is builder output (rule 30)**; and **a named entry is only one whose name comes from the model catalogue or
etf-classifications -- any other ticker shows verbatim.**

| cell | item | outcome served | risk | worker | depends on | checks (base dry-run at CLOUD HEAD) |
|---|---|---|---|---|---|---|
| `IB-yr-242` | a sibling scoped GET serves the comparison catalogue -- the model catalogue's 4 entries joined to etf-classifications for ticker -> name -- behind the existing authz guard and tenant check, against its own new v1 `_contracts` schema; an entry with no name from either source carries its TICKER VERBATIM and never a positional label | FWD-4 (W2-04/05: the page can resolve and NAME a comparison before Add, and refuse at Add) | WORLD (a new served route) | to be measured per S197 at the cut | none -- 103038 settled the shape, 103035 the source | `R24_CHECKS/test_r24_y2_catalogue_read.py` -- to be written and dry-run at the cut |

**Rectangle now: 2 cells, `IB-yr-241` and `IB-yr-242`. fanout: 2 of 2 chains, cap 8.** W2-07 remains not cut and
already covered (S206 confirmed at S215; S218's observation is round 23's `IB-yr-231`, complete and graded).

**L6 is the next act for both cells** -- battery, base dry-run, order, spawn. Round 23 is why they are not rushed
into this tick: its first battery failed all four criteria on a harness error, and only exercising the control
revealed that the two red criteria were measured absences rather than a broken fixture. A cell cut against an
unexercised battery is a cell cut blind.


## Amendment 2 (2026-09-29 ~22:1xZ) -- `IB-yr-241` needs NO new field and NO contract change; it rides `actions[]`

**Issuer amendment, on a measured contract read, before the order was cut.** Cell `IB-yr-241` as first written said the
status wire "serves, alongside `state` and `public_reason_code`, a short human correction sentence", which implies a
NEW FIELD. That would have been wrong twice over, and the contracts say so:

1. `_contracts/StatusEnvelope.schema.json` is **`additionalProperties: false`** with 7 properties, and
   `PublicStatusEnvelope` likewise with 6. A new field is a contract change.
2. `public_reason_code` is documented from the PRD CONTRACTS table @62301f71e0, required-meaning **item 5 of 6**, as
   *"a code, never a message"*. Putting words there is forbidden by the contract's own text, and adding a 7th meaning
   would be a PRD change, not a cell.

**But the envelope already has the right home.** `actions[]` items are `{action, safe, description}`, all three
REQUIRED, `additionalProperties: false`, and:

- `action` is an **enum that already contains `CORRECT`** -- `["RETRY", "RESUME", "RESYNC", "CORRECT", "WAIT", "NONE"]`;
- `description` is a required string, documented as *"what the action does"*;
- `safe` is `const: true` -- *"only SAFE actions are offered; an unsafe one is omitted rather than flagged"*.

And it is already used for prose on the live wire: W22's Y1 K5 response carried
`"actions": [{"action": "WAIT", "safe": true, "description": "accepted work is queued for processing"}]`.

**So the cell is: when a request needs correcting, the envelope offers `{"action": "CORRECT", "safe": true,
"description": "<the words>"}`, the words derived from the server's own `job_detail` / finding.** No new field, no
contract change, no PRD change, and no new enum value -- the CTO's *"correction words on the status wire"* is served by
the wire as it already stands. This is strictly more conservative than the first wording and it is the issuer's to
rule (the cell's shape inside its own decomposition), so it needs no further decision.

**Consequence for the battery:** the criteria assert on `actions[]`, not on a new key, and one of them is a control
that the envelope's 7 properties are unchanged and still validate against `StatusEnvelope.schema.json`. A cell that
changed the contract would fail its own control.

**Also carried into the cell from `IB-yr-231`:** the words are chosen from an ENUMERATED server-side mapping, never
free text and never an exception body -- `RESOLVE_RETRY_EXHAUSTED` in particular must NOT say "replace the file",
because rows `IRPT_BCKEND-S206` and `IRPT_BCKEND-S215` measured that as the wrong remedy.
