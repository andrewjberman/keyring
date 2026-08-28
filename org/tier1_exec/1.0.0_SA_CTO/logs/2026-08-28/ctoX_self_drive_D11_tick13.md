# 1.0.0_SA_CTO~X — `/self-drive D11` ticks 12–13 (04:0xZ–04:4xZ): the frozen contract, the WP-3 design under attack, the v0.3 block opened

**archetype:** COORDINATE
**secondary_archetypes:** IMPLEMENT, VALIDATE, SCRIBE

**Ticks covered:** 12, 13 (+ the continuous inbox-driven work between them). **State: ARMED** (cron
`e17cfef7`; paired `/drive D11` at `2.0.0_SA_COO~X` ticked 13 @8125662166 — ledger rows 9–10 consumed
as bookkeeping, WP-3 start + L3 cells HELD on the dry condition). Scope: D11 → `NFRA_SUBSTRATECARDING`
active/EXECUTING, 2 open TOs, 1 claim of 341 JSONs scanned (= the member), device LAPTOP.
**Completion test: NOT DONE — 0 of 1; REACHABLE 1 / UNREACHABLE 0.** Calls pitched: 2 (tick 13) + 2
(tick 12); verdicts: 4; RESERVED: 0 (the all-reserved tell did not fire). Ledger: 12 rows.

## VERDICTS (operative sentences verbatim in the ledger; ids and acts here)

- **Row 9 C4** (CVO~X 040820Z): freeze YES as a REGISTRY fact → `v0.2-candidate+38` FROZEN schema-only
  @91d24d7e79 (`bundle_identity.py --freeze`, second-seat-verified by CRO~X + COO~X, two instruments).
- **Row 10 C5** (same message): design before code → `WP3_LEDGER_DESIGN.md` @91d24d7e79, attacked since.
- **Row 11** (CVO~X 043852Z, pitched 043706Z): `state_observation.producer_serial` **STAYS EXTERNAL**
  in v0.3 (a producer may be a probe, a validator run, a seat; `mat_serial` would make every observer
  a registered materializer). Act: §2d's "typing filed to v0.3" clause for that field struck.
- **Row 12** (same message): the v0.3-candidate round shape **APPROVED** — CTO~X authors the bounded
  contract change; CRO/CVO/DT keep their axes; `ROUND3_CHARTER.md` addendum, `R4-<seat>-<n>` ids,
  `round: 4` rows in the continued register, `BOUNDARY_ROUND4.md`. **Condition:** incorporate the
  043700Z replay first — met in this commit. **Family rule AMENDED:** a native `v0.3-candidate+N`
  label with `supersedes_bundle_id` → the frozen +38, never a second alias on a `v0.2-candidate+N`
  record. Ledger code stays HELD until the amended design AND the v0.3 candidate are each
  attacked-dry/frozen; contract authoring is my own lane and opens now.

## THE DESIGN ATTACK, BY THE NUMBERS (register 53 rows, 0 OPEN at my read)

Three design revisions since the freeze: bec797df5f (R3-DT-7: both arms per row), 2f1fdc4c18
(R3-CRO-18..20, R3-CVO-6..8: atomic batches, decision tables, `v0.3-candidate` routed),
39e7c981cb (R3-CRO-22..28, R3-CVO-9, R3-DT-8: schema-derived reference table of 29 rows,
`commit_seq` replay anchor, fork rejection + HEAD rules, responsibility 13, authored-stays-authored,
mint-fact equality, registry-side receipt carrier), and this commit (CVO~X's replay: a FOURTH
carrier `materializer_superseded`, chain-cycle rejects, duplicate-resolved/self-merge rejects,
same-batch tie broken by `surface_version_id`; R3-CVO-10 filed FIXED — and CRO~X's replay 044058Z
in the same window: R3-CRO-29 a version chain has ONE root and never crosses a lineage, R3-CRO-30 a
FIFTH carrier `authority_epoch_event` so row 6's epoch arms have a source of truth (ROUTED to v0.3),
R3-CRO-31 receipt values validated as resolvable commits BEFORE mutation (an empty string had been
accepted and would have poisoned the slot forever), R3-CRO-32 the R3-CRO-21 row's stale basis).

Replays received: R3-CVO-7 PASS · R3-CRO-28 8 of 8 on a scratch registry with a contamination
control (COO~X 77392) · the 136 vector reproduced 13 of 13 by DT~X (77399) and COO~X · sec 2d's
census corroborated from the schema by DT~X (77394; every delta traced to DT~X's own instrument,
not filed) · DT~X DRY on §3/§7 at 39e7c981cb — **a prior-revision fact again after this commit**
(§3 moved in rows 3/6/7/11/13; 149 arms by the same predicate), re-run asked, not assumed.
CRO~X's replay PASSED R3-CRO-22 (27 typed refs re-derived from the schema), the 136 vector and the
receipt arms, then filed R3-CRO-29..32 (above). Outstanding: CRO~X + CVO~X replays of this commit.

## MY OWN ERRORS THIS WINDOW, ON THE RECORD

The row-2 reference census written from memory (R3-CRO-22: short by four; replaced by a derivation
whose rule a second seat re-implemented from the text alone) · "derived becomes REQUIRED" was a
contract change dressed as a ledger rule (R3-CRO-26) · the typed 90 survived one commit past its own
correction at :126 (R3-DT-8; the class is retired: no typed total remains, both numbers checked by
DT~X) · the receipt carrier shipped with no value validation — CRO~X wrote an empty string into a
scratch slot and it took (R3-CRO-31; I exercised five arms on the carrier and none on the VALUE, the
wrapper-vs-object pattern again) · fix velocity: three revisions in 40 minutes moved DT~X's DRY
target twice — named to the attackers each time rather than counted as clearance.

## Compiler Tools

| tool | result | note |
|---|---|---|
| schema walk at dcbe214a44 (`$ref`/`pattern` census) | 27 pattern-typed refs; every other `$ref` non-record | the §2d derivation; DT~X re-derived: corroborates |
| `bundle_identity.py --receipt` on a SCRATCH registry | 5 arms (COO~X: 8) hold; bundle id unchanged; real `--check` OK | R3-CRO-28 |
| §3 arm parser (DT~X's predicate) | 136 @39e7c981cb (4 seats identical) → 149 this commit | never typed in the doc |
| `bundle_identity.py --receipt` VALUE arms on a scratch registry | empty / malformed / nonexistent REFUSED, sha unchanged; valid commit stored as full hash | R3-CRO-31 |
| `render_round2_register.py --round 3 --check` | OK, 49 rows | every count derived |
| `.tools/commit-gate.sh` on `bundle_identity.py` | clean | ruff py39 |
| `directives-check.py --json` | D11 LAPTOP, 1 member, 2 open TOs; 12 live | the scope denominator |
| `comp-find` | not needed this window (all reads at known paths or via the schema walk) | stated per the standard |

## Blockers

None in my lane. Ledger CODE is gated (CVO~X 043852Z) on two dry/frozen states; the v0.3 authoring
block is open at this seat now.

## Next Steps

1. **[1.0.0_SA_CTO~X]** `ROUND3_CHARTER.md` addendum (round 4: five carriers + two typings);
   `bundle_identity.py` family rule → native `v0.3-candidate+N` + `supersedes_bundle_id`; then the
   contract/schema/validator/fixture changes on the bounded scope; `--write`, boundary, `--freeze`.
2. **[4.0.0_SA_CRO~X · 3.0.0_SA_CVO~X · 0.4.0_DT_ClientPlatform~X]** replays at this commit; dry
   declarations on the design when they hold.
3. **[2.0.0_SA_COO~X]** rows 11–12 consumption (`unblocks: NONE`); the ledger build is a Rule-27
   decomp question only after both gates.
4. **[0.0.0_AB_MSTR]** integration window: ~83 local commits.

**state: ARMED** · push state of this log: LOCAL
