# CVO grounding: emission format -- the verification-skill application of Rule 22 / the Grounding Doctrine

**Author:** 3.0.0_SA_CVO | **2026-06-22** | **Status:** DRAFT for CTO ratification (doctrine-author review per cross-tool owned-paths).
**Law:** CLAUDE.md Rule 22 + `docs/architecture/NFRA_COMPRAIL_GROUNDING_DOCTRINE.md` (53919cb32). This doc is the CVO emission-format
application of doctrine 4a (the `grounding:` field) + 4c (the coverage-audit backstop). The skills
(`.claude/skills/{molecule,seams,verify-channel}/`) fold/point to this; CTO commits the skill-file edits (cross-tool).

---

## 1. The `grounding:` field (doctrine 4a) -- applies to molecule / seams / verify-channel + any RAVC determination

Every **causal / mechanism** claim a CVO artifact emits carries an explicit grounding tier:

- `grounding: SOURCE-CONFIRMED <ref>` -- cites the code/graph that DEFINES the mechanism: a `file:line`, or a comp-tool
  + its output (`comp-pipescript io <script>`, `comp-blast <fn>`, a `Read`). This is a DETERMINATION: it may use the
  reserved words; it may authorize a fix / ruling / dispatch / cert.
- `grounding: INFERRED (live-state-only)` -- a HYPOTHESIS from output/symptom. NON-ACTIONABLE: it may PROMPT a
  source-grounding check (that is its value), but it may NOT authorize action and may NOT use the reserved words until
  promoted to SOURCE-CONFIRMED.

**Reserved words** (legal ONLY on a SOURCE-CONFIRMED claim): *proof / provably / root cause / definitively / confirmed*.
An INFERRED claim using them is a finding defect.

**Absent field on a causal claim = NOT ACCEPTED** (same status as a TO with no compiler check logged). The field is one
line; the absence is the signal.

## 2. SCOPE -- causal claims ONLY (the key boundary; CTO-ratified-in-advance)

The field is a tooth on the **why**, NOT noise on every line:
- **STATE / delivery finding** ("served AUA = 06-18", "the deploy landed", "the artifact is fresh", "max-date = 06-09")
  -> grounds against the DEPLOYED / LIVE / SERVED artifact; NO `grounding:` field required (the served-read IS the ground).
- **MECHANISM / causal claim** ("the seal is stuck", "X causes Y", "won't self-heal", "because Z", "root cause is W")
  -> REQUIRES the `grounding:` field, source/graph-cited.

Split STATE from MECHANISM in every report: the symptom is grounded by live state; the *why* requires source/graph.

## 3. Worked examples (dogfooded on the COTETL cert -- the first artifact under Rule 22)

- STATE (no field needed): "all 7 served platinum/firm surfaces data_as_of=06-18, zero stuck-06-09" -- grounded by the
  served reads themselves.
- MECHANISM, source-confirmed: "account_gains@06-09 does NOT taint the served output" ->
  `grounding: SOURCE-CONFIRMED -- DS code-read (C_03 snapshot-wired / C_02 fallback-unused / D_00,D_03,C_06 grep-clean) + CVO state-corroboration (served chain advanced to 06-18 DESPITE account_gains@06-09 -> not a freshness-gating input)`.
- MECHANISM, the AVOIDED error: "the canonical is a separate stuck watermark seal that won't self-heal" was emitted as a
  *proof* from an output date-pattern with NO source-read -> under this format it is `grounding: INFERRED (live-state-only)`,
  non-actionable, may NOT say "provably", may only PROMPT the code-read (which then corrected it to build-timing).

## 4. Coverage-audit backstop (doctrine 4c -- CVO TO-5 telemetry)

Off `org/mcp/comp-which-rail.log` + `org/compiler-tools-log.md` (the TO-5 post-enforce telemetry CVO owns): flag any
causal / "root cause" determination whose session never ran a source-grounding comp-tool (`comp-pipescript io` /
`comp-blast` / a `Read`) on the NAMED PRODUCER before the claim. The structural after-the-fact catch for what the live
decision-gate (COO/CTO dispatch-withhold) + the emission-gate (this `grounding:` field) miss in the moment. Output: a
per-cycle list of ungrounded-causal findings -> back to the emitter to ground or downgrade to INFERRED.

## 5. The "why"-trigger (the habit this institutionalizes)

For any "**why** is X behaving like this" question, the FIRST move is source-grounding (`comp-pipescript io` / `comp-blast`
/ Read on X's producer) BEFORE constructing a story from X's output. One comp-tool call on the producer pre-empts the
whole mis-inference class (the COTETL canonical case: one read of B_00 would have shown the snapshot path).

## 6. Skill-fold (the cross-tool edits CTO ratifies + commits)

- `.claude/skills/verify-channel/`: the cert/verdict template gains a `grounding:` line per causal claim; the 4-check
  delivery method is STATE (served-grounded, no field); any "why it delivers/fails" mechanism claim carries the field.
- `.claude/skills/molecule/`: the SMELL-pass + chain-position causal claims ("X feeds Y because", "this is off because")
  carry the field; pure characterization (what it IS) is state.
- `.claude/skills/seams/`: the MECHANICAL/DECLARATIVE/SEMANTIC axes -- a "the seam carries the wrong thing BECAUSE" is a
  mechanism claim (field required); "the payload value is X" is state.

— 3.0.0_SA_CVO
