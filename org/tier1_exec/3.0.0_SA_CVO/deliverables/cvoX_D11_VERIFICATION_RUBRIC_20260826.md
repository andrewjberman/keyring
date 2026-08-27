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
   - **The EMPTY-ARRAY inverse hazard (74172/74184, survived two gates and my PASS):** an empty
     `projection_of: []` is a POSITIVE claim ("derives from nothing") that certifies there is no
     source so nobody ever asks again — and no instrument distinguishes a measured-empty array from
     a never-populated one. Verification form: an empty lineage array on any subject with a
     plausible generator draws the same where-looked/denominator question as an absence row; an
     unevidenced [] on a generated-looking artifact is a flag, not a pass.

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
  **RESTATED 73258: the KEY form is v1-schema-REJECTED (additionalProperties:false, exercised by
  CloudComp~X with fired control) — the wave-1 operative form is IN-EVIDENCE prose on
  process.methodology.evidence. No lane fails for the in-evidence form; nobody amends the schema
  mid-wave; a real v2 field is routed to the schema owner for the wave boundary.**
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
- **COO~X 73227 — TO-W1-DTX AMENDED (sovereign-input spec amendment, issuer's act):** DTX-AC1 is
  SUPERSEDED by conformance to `org/standards/L0_GRAPH_SUBSTRATE_MANIFEST.schema.json` (exercised at
  my seat: Draft 2020-12 check_schema PASS, empty manifest rejected with 5 errors; required =
  schema_version/as_of/compiled_by/denominator/parts). AC2/AC4/AC5/AC6 stand; the schema's
  `denominator.known_unsearched` IS AC6 as a rejectable field. SCOPE IS BOUNDED: census reach +
  card `projection_of`/`co_resident_stores` lineage + known_unsearched PRINTED — a manifest stating
  its limits is conforming; implied completeness is not; Andrew's "EVERY SINGLE" is the artifact's
  ambition, not the wave-1 bar. `temporal_claim` is newly minted with NO x-rule24 record (routed to
  CTO~X): the manifest must state it adopted the field without a record; DT~X must NOT author the
  record themselves. DTX-AC5 (zero commits touching manifested stores/generators) unchanged.
  UPDATE (CTO~X 73242): the temporal_claim x-rule24 record LANDED @54b9d6f37d — DT~X's limits note is
  DISCHARGED (drop it, or keep with the @54b9d6f37d citation; either conforms). Verifier watch-item
  from the record's own state-coherence clause: a claim DOWNGRADED to make a claim-vs-vintage
  violation disappear is laundering, not remedy — check that any temporal_claim downgrade in the
  manifest carries its reason.
- **AC4-class scoring split (COO~X 73253.3):** `determinism: deterministic` established by the
  two-arm control (same-input identical AND different-input different — the second arm is what makes
  it a measurement) satisfies *-AC4 NEGATIVELY and legitimately (trigger {inferential,hybrid} unmet,
  null inference_detail correct). Distinct from CCX's vacuous-true (`unknown`, trigger never armed):
  one says "measured, not inferential", the other "not established" — never scored the same.
- **Wave state at 19:30Z:** 8/8 cards delivered; SC-m-2 MEASURED by COO~X's exercise (8/8 on-pin,
  planted-wrong-commit control fired); carded_utc clusters 3/3/2 by lane batch (ruled not-a-defect;
  decomp wording aligns at boundary); non-ASCII in 5 of 8 cards routed to schema owner as
  OBSERVATION (outside the ASCII rule's stated scope; no lane changes anything).

## Wave-close checklist (this seat's obligations, discharged by MEASUREMENT never declaration)

- **SC-m-5 (mine):** zero commits by a carding lane touching a subject's own generator during the
  wave — measure over the wave's commit set (each lane's completion commits already read clean at
  verification; the wave-close pass sweeps the full window).
- **Live estate hazard to flag in the wave-close record (COO~X 73307 ask):** D3's contract validator
  returns rc=0 from BOTH arms (real PASS and planted-mutant REJECT) — anything gating on its exit
  code is not gating. Named owner on the D3 card; hazard is estate-wide beyond the card.
- **Absence claims built on `composes`/`projection_of` arrays inherit the spelling-collision defect**
  (COO~X 73295: 51 raw vs 43 distinct, 6 subjects with multiple spellings; the dedup key is a stated
  heuristic, not an identity function). "X is not in any projection_of" may be reading a different
  spelling of X. v2 joinable_ref {id, note} fix landed @efd36a8169, wave-boundary only; L0 manifest
  arrays deliberately untouched mid-wave.
- **AC4 three-way outcome (COO~X 73307, verbatim adopted):** CCX vacuous-true (not established) ·
  CCY vacuous-defensible-static · COX negatively-satisfied (the only reproducibility MEASUREMENT).
  Never flattened to "AC4 passed" ×3.
- **Currency vocabulary, final operative form (73307):** UNVERIFIED = generator exists, currency
  unestablished · NOT_APPLICABLE = absence MEASURED · neither = unworked row.
- **P1 CLASS for the wave-close record (COO~X 73406, operative ask on this seat):** one enum over a
  mixed-provenance unit — 3 measured instances in 2 contracts (generator_currency key-rejected;
  L0 basis on kuzu.s3; card basis on 4 of 21 ACCEPTED CCX rows carrying HELD sub-claims in prose).
  **The wave-close record MUST state: a PASS on a row with `basis: measured` means DOMINANT
  provenance measured with held parts disclosed in prose — the enum cannot deliver per-part truth
  in v1.** Cards not at fault (honest disclosure throughout); contract had nowhere to put it. v2
  candidate routed: scalar basis stays and MUST BE THE FLOOR (weakest claim across fields — CTO~X
  73403), optional basis_by_field map.
  **Class denominator (COO~X compiled 73438, CORRECTED UP by CCX author-adjudication 73458): AT
  LEAST 15 of 56 — CCX's true count is 7/21 (their held-language detector missed 3 rows phrased
  `<peer> MEASURED <figure>`, the BEST disclosure form and the one a hedging-vocabulary detector is
  blindest to); CCY 3/21 and COX 5/14 are likely under-counted by the same mechanism and only their
  authors can adjudicate. A FLOOR OF FLOORS, never a rate.** Durable detector lesson banked: key on
  ATTRIBUTION (another actor named as source), then author-adjudicate ruling-cites vs fact-cites —
  no regex separates them. **Wave-close figure form (CTO~X 73462): AUTHOR-ADJUDICATED where
  available, DETECTOR-DERIVED otherwise, never summed as one instrument** (the defect is what the
  author DID, not what the text SAYS — every text detector measures a proxy). **Root cause on the
  record: pre-measurements handed down in the decomp brief WITHOUT a provenance slot become
  laundered claims one layer down through no fault of any receiving seat; v2's basis_by_field +
  FLOOR closes it mechanically @6cb34bc2ca.** Row-summing is valid here (rows partition cleanly by lane) where part-summing was not —
  same fabric, opposite arithmetic, different grains. ⛔ **THE CONFOUND, verbatim into the wave-close
  record: every detector keys on DISCLOSURE language, so the rate measures honesty, not hygiene —
  COX's 36% is the most transparent card set, not the worst; a silently-holding lane scores 0% and
  is strictly worse. Never score lanes comparatively on it; the undetectable silently-held
  population is unmeasurable from the artifacts.** CCY's three-way provenance split
  (measured-by-me / measured-by-peer-cited / held) is v2 shape evidence, CTO~X's.
- **DTX part-count bar (COO~X 73328, SC-m-4 closed BOUNDED):** the manifest must NOT adopt 37/39/43
  or any lane sum as a part count — the identity is not in the strings (a key strict enough to catch
  false splits merges `kuzu_nessie_db` with its S3 twin; measured, both directions). DT~X's part_id
  is where identities get MINTED, not consumed; UNRESOLVED markers + known_unsearched are the
  conforming answers where resolution fails. A precise part count in the manifest without minted
  identities behind it is the over-count-as-thoroughness failure.

## WAVE 2 — verification bar (Andrew-ruled 2026-08-26 ~20:5xZ at the CTO~X terminal, via 73663)

- **Scope: ALL 43 candidates, Andrew's word verbatim** ("Let's go through these anyway... all the
  definitions of these things as they stand currently"). My 73651 scope adjudication is SUPERSEDED
  and not operative — his word governs. The 33/10 measurement survives as decomp PRIORITISATION only.
- **The dedup amendment SURVIVES on its own basis** (scope-independent — it is a fact about the
  candidate list): the two spellings of c2_individuate.py are ONE subject; COO~X accepted it as
  binding on any wave-2 decomp (73658 s.1) before the scope ruling and nothing in the ruling
  touches it. Cert check when the decomp routes.
- **Contract: SUBSTRATE_CARD.v2.schema.json** — four constraints v1 lacked: joinable_ref {id,note};
  basis_by_field + FLOOR (scalar = weakest claim across fields); materializer_standing (field, not
  prose); forward_disposition.
- **forward_disposition rules (the word "after" is the design):** born UNDECIDED · OPTIONAL at top
  level — ABSENT on a wave-2 card is CONFORMING, not a gap · **a CARDING lane that FILLS it is OUT
  OF SPEC** (set_by must not be the carding lane; dispositioning is a second pass with a separate
  owner, whose identity is Andrew's to say) · undecided never defaults to keep because a thing
  currently runs.
- Naming hygiene noted: `forward_disposition` not `disposition` (that token already means residue
  classification in the phase-B reconcile — census run before minting, 0 collisions).
- **WAVE 2 DISPATCHED (COO~X 73747 @d700d7913d): 4 TOs, 35 subjects, 245 cells + 5 mechanism =
  250.** Decomp `runs/nfra-substratecarding-w2/20260826T210050Z/` @9e0394fedf, UNCERTIFIED, cert
  pending this seat (expect a seal-bearing request — each attempt takes a FRESH sealed plant).
  Criterion sets {CCX2,CCY2,COX2,DTX2}-AC1..AC7 = 28. **Wave-2 anchor `100e7ea130`** (a wave-1
  anchor on a wave-2 card is a WAVE defect); graph_vintage unchanged BY MEASUREMENT (projection not
  rebuilt, re-read 21:19Z). **W2-m-3: ZERO deprecation verdicts at first delivery** — a lane that
  decides a subject is doomed cards it differently, so the tag must not leak backward; any fate
  language in a wave-2 card is a rework. **declared_opinions: the card-schema slot now EXISTS
  (CTO~X @9660f526d8, ADDITIVE-OPTIONAL — landed ~2 min after dispatch, invalidates nothing in
  flight). THREE conforming forms: field populated · field explicit NULL (loud = opinions buried,
  subject unreviewable — a finding, not a blank) · field ABSENT with the prose-in-methodology.how
  form (the original TO-face instruction; the evidence note check applies to this form only).
  Which form the wave standardizes on is the ISSUER's call; absence is never read as a gap.** Harvest over the W2 face = 251
  CONFIRMED at my seat: the extra is wave-1's SC-m-4 inside the input filename, cited by no
  criterion — never a 251st cell. Subjects arrive as prose strings: identity resolved by reading
  the thing, not the string.
- **Frozen-vintage battery additions (from the amendment cycle):** cert holds until COO~X declares
  the subject set FROZEN + the face is regenerated from the frozen rectangle (attempt records
  @79dea5e112 + @6b8292a1e2 accumulate; 2 seal reveals owed). At the one battery: (i) face-vs-
  rectangle harvest equality (the withhold condition); (ii) the 68-heads → subjects DEDUP check —
  CTO~X's closure test (73948) fixes the head population at 68 via the 3 x-names-parts fields
  (invents adds ZERO stores — its 21 heads are opinions/concepts, marker removed @e789861948,
  measured; a parts-read of invents would mint 21 phantom subjects, CARRIER-3 at 21x); heads are
  pre-dedup, subjects post-dedup, and the dedup reconciliation (subjects + collapses ≡ 68 heads at
  their grain) is UNVERIFIED and is the certifier's check; (iii) the cross-artifact executor join
  (attempt-3's instrument, now standing); (iv) W2-m-2's two-denominator oracle + the 43-closure
  self-test arm. Bonus banked: 21 declared_opinions already harvested in wave-1 invents fields.

## For the wave-2 close record (banked as the threads settle)

- **The which-object class, the wave's most repeated finding, now measured in four seats' work:**
  a control validates the INSTRUMENT, never the CHOICE OF SUBJECT — every discriminator is
  downstream of "which object am I measuring", so all of them agree, and the agreement is what
  makes the answer feel finished (Rule 22's ordering clause, live). The remedy that worked twice:
  NAME THE OBJECT AT SOURCE AND READ IT — never re-read your own sentence. No instrument exists
  for the class; the demonstrated detector is the next wave reading the thing itself.
- **The reopen test exercised once and it HELD** (74154/74160): a scary find at 00:0xZ was tested
  against the map before escalation — both objects IN MAP, correction not BLOCKING, freeze intact.
  The criterion exists so midnight finds get tested rather than escalated.
- **The law-vs-card join gap, UPGRADED (CTO~X 74169, measured):** the violated prohibition exists in
  ONLY ONE of the two rule banks (live :693; July copy ZERO, control firing) — a seat working from
  the July copy did not miss the law, IT STRUCTURALLY DOES NOT EXIST for them. The join is
  CONDITIONAL ON WHICH FILE YOU OPENED and nothing in either file says it is one of two. Direction
  ratified, wave-boundary; **prerequisite named: the estate must DECLARE WHICH RULE BANK IS
  CANONICAL before any join is built** — a joiner over an undeclared two-copy source is the
  derived-identity class again. Subject #44 is thereby the MECHANISM of tonight's law violation,
  not bookkeeping.
- **Typed-beside-generated at EIGHT instances, all issuer's, plus the L0 parts_registered (CTO's
  8th):** every one a hand-maintained assertion beside a machine-derived truth, machine right every
  time; remedy = derive, never also type. Containment check: direction ratified, wave-boundary.
- Pending narrow re-check: the three-materializer C2 correction (authorized 74160; three strings +
  instance + log annotation) when CloudComp~X lands it; the baked_static_spec_layers two-row fix
  (authorized 74184) when CloudOps~X lands it.
- **CERT SCOPE, in the issuer's own words after the Andrew-direct 00:15Z assessment (74211):** "a
  certification is a statement about INTERNAL COHERENCE, and internal coherence is exactly what a
  wrong population preserves." The attempt-4 PASS certified the packet coherent — it could not and
  did not certify that the 44-subject population was the population Andrew asked for. Root cause of
  the population mix is Rule 24(ii) AT THE SOURCE FIELDS (v1's composes held artifacts AND prose —
  one field, two grains — inherited by any faithful harvest); v2's joinable_ref is the fix and it
  landed after the population was derived. Assessment: 32/44 openable, 12 fragments (UPPER BOUND,
  2 likely over-called), 8 of 12 concentrated in the lane that raised it. Scope decision is
  Andrew's/CTO~X's; no lane halted (the sovereign MAY was not hardened into a stop).

## Late wave-2 close-bank additions (2026-08-27 ~01:2xZ)

- **The live-claim-vs-record distinction has FIELD grain, not artifact grain** (authored by
  0.7.0_AE_CloudOps~X, confirmed 74330): one proof-of-spec instance held BOTH — a
  decomp_ref.vintage_commit asserting a false vintage (LIVE CLAIM, correctly repinned) beside a
  criterion_verbatim quoting a true one that has since moved (RECORD, correctly left untouched).
  An artifact-bin rule could not have produced that call. My verification treats correct/leave
  decisions per FIELD.
- **A correction has a SUBJECT and can be right-that-wrong while locating it in the wrong artifact**
  (74330, on my own contest): I contested a mis-set credit suspecting the durable record; the
  record was already clean and the defect was in the multi-recipient message describing it. The
  contest was right, its subject one layer off — the reader's available surface IS the record from
  where they sit.

- **known_unsearched CAN ONLY NAME THE GAPS YOU HAVE IMAGINED** (DT~X 74295): wave-1's residue was
  fully predicted by the declared-limits block; the graph-producer-outside-the-graph-module was not
  predicted at all — the difference is imagination, not diligence. A declared-limits block is a
  measurement of the author's model of the world, not of the world. Verified @006d00376f: both
  load-bearing table rows now name the incremental_updater Lambda; the consumer un-named as
  producer (my re-check).
- **A FALSE CORRECTION IS HARDER TO REVERSE THAN A FALSE CLAIM** (CCX2 74290): a claim invites
  challenge; a self-retraction closes the question. The UNVERIFIED-not-falsified hold on a
  guessed-pattern zero preserved a TRUE claim that the producer find then CORROBORATED. The close
  carries no doubt marker on the C0/C1 composes rows.
- **Three instruments, three blind spots, one object, each individually correct about its own
  tree** — the producer invisibility diagnosis: only a different PLANE catches it, no better
  single instrument does. Wave-3 design input.
- **Battery statement amendment (74286, standing): every card-level battery result carries each
  subject's COMMIT STATE (hash or UNTRACKED)** — a sound measurement of an unretrievable subject
  reads identically to a durable green and is not one.

## Standing battery amendment (2026-08-26 ~23:5xZ, after the twice-missed pin)

- **PIN CONTAINMENT is a standing battery step on every proof-of-spec verification:** `git show
  <decomp_ref.vintage_commit>:<DECOMP path>` must CONTAIN the instance's cell ids (first + last
  suffices with a firing control). The gate checks pin-RESOLVES only and DECLARES containment a
  non-goal on every run — my battery read past that disclaimer twice in one hour (COX2 by
  inheritance, DTX2 minutes after writing the correction). The check the tool declares out of
  scope is the check this battery owns.

## Standing context

- nerves_resolve is the worked REFERENCE card (CTO~X's, pre-wave vintage): not a wave member, not
  held to wave as_of, not the mandatory shape. A lane re-card under the wave stamp supersedes it.
- DECOMP state: **UNCERTIFIED, disclosed on every TO face** (verified 4/4). Sealed mutant not yet
  planted at packet time; COO~X routes the cert request separately. Wave-wide cell coverage 59 of
  61; 2 residuals (SC-m-1 freeze, SC-m-4 wave-2 derivation) ISSUER-executed, named.
- This seat is a VERIFICATION lane, not an approval gate (stated in 72792, agreed by CTO~X 72796).
  Nothing waits on this seat except where TASK_ORDER_PROTOCOL already binds the complete flip.

— 3.0.0_SA_CVO
