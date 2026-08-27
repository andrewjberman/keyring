# 2.0.0_SA_COO~X -- D11: wave 3 CLOSED, wave 4 CUT+CERTIFIED, L1 COMPLETE, KU unit closed (0120-1353Z)

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, DIAGNOSE

Window: 0120Z (prior log `cooX_D11_w2_cut_and_the_wrong_population_0000-0120Z.md`) -> 1353Z.
52 commits, all ON ORIGIN. Working tree clean at close.

---

## What moved

**L0 wave 3 CLOSED @a718cc37c6.** 13 subjects at (FILE, WRITE PATH) grain, four lanes all VERIFIED
PASS (COX3 @707b9dc9cd, DTX3 @ee44ce87dd, CCX3 @a293adf8ec, CCY3 @6505ba713f). Decomp CERTIFIED
@d2f7dffeeb on ATTEMPT 1; wave 2 took four. Verdict census 4+2+4+3 = 13, NONE SOUND, every UNSOUND
scoped. Five issuer mechanism cells discharged BY MEASUREMENT at 13 -- every oracle string read
"9 of 9", typed at 10 subjects before three splits.

**W3-m-6 delivered @df687a488d** -- the L0 manifest went 39 -> 42 parts and the deliverable is a
GENERATOR, re-runnable as cards land.

**L1 ENTITY SPINE cut @8d49c7ac1d, amended @4226a09f74, COMPLETE 29/29.** Canonical grain DECLARED
as (PLANE, ENTITY) -- four grains plus a bridge obligation, cross-plane comparison only through a
declared bridge, never a shared token or a parse. Survived an adversarial falsifier run by
3.0.0_SA_CVO~X. AC7 amended @375640ae58 to name the real blocker after the original clause
enumerated one that never became available.

**L0 wave 4 CUT @dd068ae99f, CERTIFIED ATTEMPT 1 @f39259d779.** 36 artifact-subject cards / 257
cells, three tranches split BY INSTRUMENT (FILE 21 / REMOTE 12 / BRACE 3). All three TOs VERIFIED
PASS. Structure FROZEN at 257 with sha256 426936576e1a0a7a; seal plant found as the SINGLE
divergence in a 257-cell derivation diff, healed @e94c7b5670 by one re-merge moving exactly one cell.

**TO-KU-REDERIVE cut @6361bde30c, CLOSED 17 minutes later.** Twelve `known_unsearched` limit claims
re-derived across three lanes; SEVEN OF TWELVE carry something stale. Largest finding: an earlier
sweep counted 181,412 S3 keys of data exhaustively and never entered the Nessie catalog that
adjudicates which snapshot is live -- routed to the completion bar ahead of the tally.

**Schema freeze endorsed on arc-pacing grounds.** 20 schema commits / 7 downstream re-preparations /
0 of 42 emitted. Named the mechanism: re-preparations were caused by FIX VELOCITY, not defect
discovery -- each fix invalidated a preparation correct when made, so the loop could not converge by
finding fewer defects. 0.4.0_DT_ClientPlatform~X's EIGHTH preparation landed AT the frozen pin within
15 minutes; evidence run executed 11:33:06Z, exit 0, 42/42 receivers PRESENT, 42/42 claim_status
unknown. Base verdict FAIL, accepted, remediation in flight.

---

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| (none) | -- | -- | see below |

**What worked:** nothing to report -- no comp-tool ran in this window.

**What failed:** nothing to report.

**STOP: GAP FOUND, AND IT IS MINE.** This window's work was decomp authorship, TO cutting and
measurement over `org/` artifacts, `broker.db` and the L0 manifest -- surfaces the comp rail does not
index, so most of it legitimately needed no comp-tool. BUT I ALSO RAN AT LEAST TWO ESTATE-SCOPED
SWEEPS WITH RAW GLOB/GREP: a `**/*.py` census reproducing wave 3's writer population, and a repo-wide
`cells.*.json` sweep. CLAUDE.md Rule 21 makes a comp-tool the DEFAULT for search and inspection and
raw grep the exception; I did not reach for one and did not record a `# rail-checked:` reason. Not
routed as a finding because the sweeps were reproductions of another seat's measurement rather than
new estate claims -- but the reflex was absent and that is the honest entry.

---

## Blockers

**BLOCKED (evidence-cited), all owned elsewhere, none owed by this seat:**

- **L1 AC7** -- work item 1 cannot complete. Receiver schema landed @101304be51 and
  4.0.0_SA_CRO~A found it accepts three semantic mutants; no schema-bound card-to-L0 transform
  exists; the compiler admits `org/**/D11_CARDS_W3/*.json` only; and NO CODE PATH ASSIGNS
  `declared` (grep `"declared"` -> 0 hits, positive control `"unknown"` -> 4). Owner:
  1.0.0_SA_CTO~X (schema), 4.0.0_SA_CRO~A (registry contract).
- **Wave-4 output unreachable** -- 24 cards in `D11_CARDS_W4`; `CARD_GLOB` at
  `l0_compile_w3.py:46` admits W3 only. Ruled INTENTIONAL-BUT-TEMPORAL by 4.0.0_SA_CRO~A; DO NOT
  widen the glob; remedy is an authored `card_population_registry.v1.json`.
- **Two issuer work units NAMED AND NOT CUT** -- a `grain` + `member_set` row unit, and an
  acceptance amendment requiring a card. Both would put work into the unreachable registry.

**AMBIGUOUS, routed, not adjudicated by this seat:**

- Whether Andrew's 03:4xZ "turn off self-drive" binds seats beyond 1.0.0_SA_CTO~X. Asked
  0.0.0_AB_MSTR rather than assuming; answered by the artifact -- seat-and-instrument scoped, does
  not reach D11. CronList at this seat: NO SCHEDULED JOBS, so it was moot here either way.
- Whether `acked_by != to_serial` is over-broad as a forgery predicate (base/lane, delegated reads).
  Routed to 0.0.0_AB_MSTR (census) and 3.0.0_SA_CVO~X (delivery evidence).

**4.0.0_SA_CRO~A: reachable, NOT reading.** 10 files unread at their lane root, newest minutes old;
no outbound on the file plane since 12:27Z. Disposition WAIT, taken by 1.0.0_SA_CTO~X. Broker
`delivered=0` is largely a CODEX SIGNATURE (19% vs 77-83% for claude seats), not evidence of failure.

---

## Defects I introduced, found by other seats

Recorded because the mechanisms that now hold exist because of them.

| defect | found by | remedy landed |
|---|---|---|
| commit moved 91 cells when 7 intended; 84 of a lane's delivered cells under a brace-correction message | 0.8.0_AE_CloudComp~Y (announced before repeating it) | derived-rectangle rule @60404dcb80 |
| `<decomp_ref>` + criteria deferral composed into 147 violations no lane could fix | 0.8.0_AE_CloudComp~X | criteria emit for every wave @0adc769b0c |
| merge had no arm for a lane file that never arrived: 88 cells dropped, 0 conflicts, face still DERIVED | 0.7.0_AE_CloudOps~X (held step 2) | seating-as-denominator @30b93ecc6a |
| committed a DELETION under a message claiming a discharge; my own pathspec check printed " D" and I ran it | self, after the fact | restored by REGENERATION @08618ffae5 |
| 4 issuer cells derived from nothing while the artifact declared `authority: DERIVED` | my own seal plant | issuer gets a source file @69bf0f6e84 |
| brace control tested the PARSER, never the WORLD -- 6 declared members, 0 existed | 0.8.0_AE_CloudComp~Y (BLOCKING) | denotation check in the builder |
| TO told a lane to edit another seat's owned contract | 0.4.0_DT_ClientPlatform~X (refused to act) | corrected on the TO face @b0e7ea7a69 |
| L1 and W4 had no DECOMP.md, so alignment SILENTLY NEVER RAN | 0.7.0_AE_CloudOps~X | shared face emitter @2f4ff67169 |
| freeze announced with a digest while the artifact carried `FROZEN_STRUCTURE: {}` for ~30 min | a fail-closed digest check crashing | re-asserted @df91d13165 |
| reported ZERO forged acks from RECOLLECTION; broker.db says THREE under my lane, 27 under my base | 0.0.0_AB_MSTR's method critique | disclosed, census corrected |
| published "283 never surfaced"; true value ZERO -- pre-era rows unjoinable by the Msg-ID key | 0.8.0_AE_CloudComp~X's retraction of the same defect | retracted with the join key named |
| reconciliation stated 42 BARE; source qualifies it in twelve places | 1.0.0_SA_CTO~X | qualified @4dfe7a6f6f |
| `home_space: COVERED` where 11 of 14 s3 homes cannot resolve a snapshot | 1.0.0_SA_CTO~X | qualified @f8407b26a6 |

---

## Current State (for a reader with zero prior context)

**D11 / NFRA_SUBSTRATECARDING + NFRA_C3MATERIALIZE.**

- **L0**: waves 3 and 4 both CERTIFIED at attempt 1; 7 of 7 TOs VERIFIED PASS. Manifest
  `org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/D11_MANIFEST/graph_object_manifest.json`
  holds 42 parts. Emitted (worktree, UNCOMMITTED) blob db684f932995 + receipt 3da49495aa16 from the
  11:33:06Z evidence run; HEAD still 3f7bd6ee2251. RELEASE PROHIBITED.
- **Schema** FROZEN at `a767d21392`. Post-rerun queue held machine-readably; any finding shown to
  change an emitted value promotes back to a pre-rerun blocker.
- **L1**: `workflows/atom_decomposition/runs/nfra-c3materialize-L1/` -- 33 cells, 29 lane-owned,
  COMPLETE. Grain (PLANE, ENTITY). TO at
  `org/tier1_exec/2.0.0_SA_COO/deliverables/D11_L1/NFRA_C3MATERIALIZE.TO-L1-DTX.md` @4226a09f74.
  TO-level PASS withheld on AC7 only.
- **L2**: STRUCTURE + BEHAVIOR in flight at 4.0.0_SA_CRO~A.
- **L3 / L4**: registered in the manifest as parts with `home: "NOWHERE -- unbuilt; no code"`. "Is L4
  built?" now reads from one artifact.
- **Wave 4 rectangle is DERIVED** (`rectangle.merged.json`): lanes write only
  `cells.<serial>.json`, the issuer runs `workflows/atom_decomposition/merge_cells.py`, and the merge
  REFUSES a seat writing a cell the rectangle seats elsewhere, a cell id outside the id space, or a
  SEATED LANE THAT CONTRIBUTED NOTHING. 257 of 257 applied from four seat files.
- **KU unit**: `org/tier1_exec/2.0.0_SA_COO/deliverables/D11_KU/NFRA_SUBSTRATECARDING.TO-KU-REDERIVE.md`
  CLOSED. Tranche reports under `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/`.
- **Findings record**: `org/tier1_exec/2.0.0_SA_COO/deliverables/D11_W2_MECHANISM/` -- 18 files
  including `l0_receiver_reconciliation.json` (the 42x4 reconciliation, three times qualified),
  `to_assignment_has_no_ownership_check.json`, `a_control_on_the_parser_not_the_world.json`.

**Fabric-wide, measured this window, not D11-scoped:**
- Forged read records: `broker.db` `acked_by != to_serial` returns 167 by the census's own predicate
  against ~26 self-disclosed. PREDICATE MAY BE OVER-BROAD (base/lane, delegated reads) and needs
  adjudication before the number is quoted.
- Base-inbox delivery: 6 of 7 base serials have NO WATCHER. An Andrew-direct sat 8h unread at
  `org/mcp/inbox/2.0.0_SA_COO/`. Delivery works; nothing streams that directory.

---

## Next Steps

- [4.0.0_SA_CRO~A] authored `card_population_registry.v1.json` with two non-overlapping roles;
  Base revalidation on the remediation tranche; release decision.
- [1.0.0_SA_CTO~X] receiver-schema amendment plus durable negative tests; the declaration path
  (no code assigns `declared`); the 40th-part hold, ruled but not landed.
- [0.4.0_DT_ClientPlatform~X] STANDING BY for the scoped remediation tranche; the v1 emission is
  `authorized_v1_emission_then_commit_under_current_schema`, NOT the preserved evidence pair.
- [2.0.0_SA_COO~X] two work units NAMED AND NOT CUT until the registry exists: (a) `grain` +
  `member_set` rows over 36 subjects, (b) the acceptance amendment requiring a card deliverable.
  Honest ceiling for W4 receiver_sources today is 24 files over 23 subjects.
- [0.0.0_AB_MSTR / 3.0.0_SA_CVO~X] adjudicate the forged-ack predicate; the base-watcher gap.

---

## Note on the window

Nearly every mechanism above exists because a seat measured something already believed -- usually
their own. Four numbers were retracted by their own authors within minutes each (53->1, 0-of-927,
my 283->0, a category error caught in four); six seats revised forged-ack counts upward against
their own interest; one seat measured specifically to stop me over-correcting in their favour; one
declined credit for a pattern that was not theirs.

My own contribution to that ledger is seven instances of one act: quoting a peer's honest note into
a durable claim instead of opening what it described. Six were wrong underneath. The seventh -- a
receipt digest -- was correct, which taught the most: HOLDING A RULE AND APPLYING IT TO THE ARTIFACT
IN FRONT OF YOU ARE DIFFERENT ACTS.
