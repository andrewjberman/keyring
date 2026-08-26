# CVO~X — D11 wave-1 verification rubric (consolidated, pre-staged)

**Seat:** 3.0.0_SA_CVO~X · **Scope:** D11 / NFRA_SUBSTRATECARDING wave 1, proof-of-spec verification
**Sources:** CTO~X 72796 (acceptance nuance) + COO~X 72929 (verifier packet), both READ-acked.
Grounding of packet claims: DECOMP.md exists at
`workflows/atom_decomposition/runs/nfra-substratecarding/20260826T172918Z/DECOMP.md` (@aae317509b per
packet); all 4 TO files read on disk 2026-08-26 ~18:1xZ, criterion ids + issued_to + UNCERTIFIED
disclosure verified against the packet (instrument: direct file read — differs from COO~X's
harvest-regex).

## The four TOs (criterion sets verified on-face)

| TO id | lane | criteria (verified) | TO file home |
|---|---|---|---|
| NFRA_SUBSTRATECARDING.TO-W1-CCX.c0-c1-c2-cards | 0.8.0_AE_CloudComp~X | CCX-AC1..AC7 | base folder 0.8.0_AE_CloudComp/task_orders/ |
| NFRA_SUBSTRATECARDING.TO-W1-CCY.d1-d2-d3-cards | 0.8.0_AE_CloudComp~Y | CCY-AC1..AC7 | same base folder |
| NFRA_SUBSTRATECARDING.TO-W1-COX.c3i-compsimilar-cards | 0.7.0_AE_CloudOps~X | COX-AC1..AC7 | 0.7.0_AE_CloudOps/task_orders/ |
| NFRA_SUBSTRATECARDING.TO-W1-DTX.graph-object-manifest | 0.4.0_DT_ClientPlatform~X | DTX-AC1..AC6 | 0.4.0_DT_ClientPlatform/task_orders/ |

27 criteria total. Row legend: -1 methodology · -2 cadence · -3 persistence · -4 location ·
-5 coverage · -6 key · -7 failure_mode. Surfaces: a=C0 b=C1 c=C2 d=C3.i e=D1 f=D2 g=D3
h=comp-similar m=mechanism.

## Wave as_of (a proof-of-spec AXIS)

```
commit_ish    fe269171f2        <- WAVE ANCHOR, not the evidence vintage
graph_vintage kuzu_nessie_db@2902399899597701830 (edges snapshot 6557038275462806297)
              built 2026-08-26T14:07:59Z · 27,035 nodes / 58,224 edges · PROJECTION plane
```

- Mixed `as_of` across cards in one wave = REWORK, no exceptions.
- Evidence citations carrying their OWN commits != anchor is CORRECT (repo moved; lanes read at
  different HEADs). The REWORK is the opposite: evidence back-dated TO the anchor = false vintage.
- `graph_vintage` is the PROJECTION plane (27,035/58,224). CTO~X's warehouse read (27,061/60,858)
  is a DIFFERENT plane, not a conflict. A warehouse figure beside the projection as_of is
  conforming IF the evidence names its plane.

## Verification procedure per completion

1. `python .tools/proof-of-spec-check.py <instance.json> <criterion_ids>` — coverage before
   quality; decomp_ref pipeline gate resolves the governing TO. Exit 0 necessary, NOT sufficient.
2. Schema pass on each card against `org/standards/SUBSTRATE_CARD.schema.json` — necessary, NOT
   sufficient (three measured holes, next section).
3. The three AC criteria that close the schema holes (COO~X-measured, F-ids theirs):
   - **F-1** schema permits `coverage.denominator: null` → check `*-AC3`: non-null "N of M", both named.
   - **F-2** schema permits `determinism: inferential` with no `inference_detail` → check `*-AC4`:
     populated incl. `failure_is_loud`. Bites hardest on comp-similar (cost figure, Andrew-priced).
   - **F-3** schema permits `verdict: SOUND` with unworked rows → check `*-AC5`: INCOMPLETE iff >=1
     row genuinely unworked.
4. Judgment axes the schema structurally cannot carry:
   - `basis: absent` WITH evidence = WORKED row, PASS. Blank/guessed/unfilled = REWORK. Entirely
     verifier judgment.
   - Good-empty vs bad-empty (CCY-AC7 / DTX-AC2): evidence must name WHERE the lane looked and the
     search's DENOMINATOR. Unevidenced "nothing persists it" is indistinguishable from "did not look".
   - **Census-instrument trap check on every ABSENCE row** (two traps measured in-wave, 2026-08-26):
     (a) comp-find with a content pattern AND `--name` in one call scans 0 files — a 0-hits/0-scanned
     evidence line is a sweep that never ran, not an absence (DT~X 72991 4-arm + COO~X 73004 5-arm;
     `--files`/`--band`/`--limit` alongside `--name` are fine, COO~X 73050); (b) comp-keys prefix
     displays 40 rows by default with the true total printed BELOW them — an S3 absence needs `--all`
     or a full-pagination read (DT~X 73077: false-absence direction only, it can only hide keys).
     Verification form: the absence evidence must carry a scanned/total denominator consistent with
     the population it claims; a piped-rows count without the totals line is not a denominator.

## Expected passes (do NOT manufacture rework) — CTO~X 72796, adopted verbatim

A card that finds defects is a PASSING card (card verdict != resource verdict). Specifically:
1. ~~D3 (SC-g-*) cards EMPTY by ruling — persistence none / location null IS the finding.~~
   **RETIRED 18:35Z per COO~X 73050: the expected-empty prior is FALSIFIED by measurement**
   (CloudComp~Y found `org/modules/graph/estate-contracts/`, 14 records / 2 of 2 files, linter's own
   predicate + independent atom_layer0 corroboration, both control arms exercised from different
   truths). A non-empty D3 row is the CORRECT result, not scope drift; an empty one now needs its
   where-looked evidence like any other. General form banked: an expected-empty prior makes a lane
   argue against the spec to report content — report the measurement, the TO is what bends.
2. C3.i (SC-d-*) cards UNSOUND by expectation — it is the baseline the replacement must beat.
   KNOWLEDGE-side zeros on C3.i are structural, already measured; reproducing them is not a finding.
3. `basis: absent` + evidence = complete row.
4. `determinism: unknown` with evidence of what was tried = honest. (Failure mode is the confident
   `deterministic` with no exercise.)
5. `UNOWNED` legal and loud. Rework a BLANK owner and a GUESSED owner (guess is worse than none).
6. Empty arrays are claims (`composes: []` asserts composes-nothing); a MISSING key is the gap.
7. INCOMPLETE is about the CARD — read why; worked-to-absent rows under an honest INCOMPLETE: accept.
8. `failure_mode.distinguishable_from_true_negative: no` = the project's highest-value finding class.

## Hard reworks — CTO~X 72796 + COO~X 72929, adopted

- Mixed as_of within the wave (see above).
- `coverage.denominator` null without explicit stated reason.
- `basis: measured` whose evidence is not a grounding (`file:line @ commit-ish` or an exercised
  command with output; line citation without vintage is not a citation; docstring is not exercise).
- ANY remediation by the carding lane — qualify-do-not-fix; a fix is out-of-spec regardless of
  card quality.

## Andrew-direct 1907Z operative rows (DT~X 73174 relay, first-hand at their terminal) — bind cards
delivered AFTER 19:07Z; CCX (delivered 19:06Z) judged against the prior bar

- A historical materializer's OUTPUT is not evidence of a CURRENT layer — such artifacts take
  `authority_role: evidence`, never source. (A card that holds the rebuilt-graph surface and the
  static-output surface APART, naming both, satisfies this without an enum flip — CCX ruling 2.)
- Generator tags carry a qualified currency: `generator: <path>` + `generator_currency: UNVERIFIED`
  unless currency was actually measured. An omitted row and an unqualified row are opposite facts
  that look identical.
- The suspicion axis is SEMANTIC, not vintage: "deprecated opinionation, filtering, questionable
  definitions" — age/mtime/snapshot instruments are blind to it. A methodology row resting on "the
  generator ran recently" is non-responsive to this axis.
- SC-d-* (C3.i): Andrew states NO stable C3 layer exists — the ABSENCE is the finding; a card
  presenting a C3-shaped one-off materialization as "the C3 layer" is wrong on its face.
- Canonical-materializer intent is POST-wave-1, trigger "after reviewing all substrate cards" —
  authorizes nothing now; any lane building one mid-wave is out of spec.

## Wave-1 ruling log (issued with verdicts + issuer rulings adopted)

- **AC-F3 binds mechanically** (CCX verdict ruling 1): `basis: absent` on any row → standing must be
  INCOMPLETE; INCOMPLETE over worked-to-absent rows = healthy PASS; genuinely unworked rows = rework
  regardless of verdict. TO-prose alignment is the issuer's wave-boundary act.
- **COO~X 73209 R1 — generator_currency authorized, sequenced:** `generator: <path>` +
  `generator_currency: UNVERIFIED` (default, not fallback — claiming currency requires measuring it).
  Applied as a DECLARED DELTA after my pass returns on a card; I re-check the delta NARROWLY, not the
  whole card. CCX verdict scoped to the delivered vintage and is not invalidated by the delta.
- **COO~X 73209 R2 — the semantic axis is an estate-wide UNMEASURED:** every card either carries its
  semantic finding or states explicitly that the axis was NOT SYSTEMATICALLY EXAMINED. Per-card
  silence must not read as clean. One sentence, not new measurement.
- **COO~X 73209 R3 (DT~X 73207.3 adopted) — on the semantic axis, silence is the weaker evidence:**
  a card with no semantic finding does not outrank one with a finding; exactly one forcing function
  has been measured across eight subjects. C2's UNSOUND is currently the most informative card.
- **authority_role on C2: closed, do not flip** — two surfaces, two values (rows rebuilt-by-derive =
  projection; static envelopes behave like evidence). No competing reading exists.

## Standing context

- nerves_resolve is the worked REFERENCE card (CTO~X's, pre-wave vintage): not a wave member, not
  held to wave as_of, not the mandatory shape. A lane re-card under the wave stamp supersedes it.
- DECOMP state: **UNCERTIFIED, disclosed on every TO face** (verified 4/4). Sealed mutant not yet
  planted at packet time; COO~X routes the cert request separately. Wave-wide cell coverage 59 of
  61; 2 residuals (SC-m-1 freeze, SC-m-4 wave-2 derivation) ISSUER-executed, named.
- This seat is a VERIFICATION lane, not an approval gate (stated in 72792, agreed by CTO~X 72796).
  Nothing waits on this seat except where TASK_ORDER_PROTOCOL already binds the complete flip.

— 3.0.0_SA_CVO
