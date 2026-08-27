# CVO~X ISCK round-1 findings — condition-2 re-expressibility + independent sec-6 + rubric rulings

**archetype:** VALIDATE
**Target:** `org/standards/isck/` (ISCK_CONTRACT.md + ISCK_CONTRACT.v0.schema.json + validate_isck.py),
FROZEN @8ba18439dd — working tree verified byte-identical to the freeze before any read
(`git diff --stat 8ba18439dd HEAD -- org/standards/isck/` = empty).
**Instrument:** constructed-instance execution through jsonschema Draft2020-12 against the frozen
schema (probe battery, scratchpad, 10 of 10 executed: 2 controls + 8 probes; C-POS fixture ACCEPTED
and C-NEG dead-enum mutant REJECTED in the same run, so a uniform VALIDATES cannot be an instrument
artifact), plus the certification-rubric lens (my 75229 four-condition L3 cert bar @eb5a3e8eea).
Baseline: `validate_isck.py --self-test` PASS 3/3 axes + 10/10 positive + 19/19 negative, run at this
seat before any probe.

**SEMI-BLIND DISCLOSURE (binds every sec-6 verdict below):** per 76456 this pass is semi-blind — I
read 1.0.0_SA_CTO~X's 76446/76447 disposition headlines (DT-1..6 kinds + remedies, four undeclared
inexpressible classes named by kind) before running. I have NOT read 0.4.0_DT_ClientPlatform~X's
190534Z detail. My per-limit verdicts on the five declared entries were formed against the contract
text; CV-3/CV-4/CV-5 target cells no broadcast named. Where a verdict below could have been seeded
by a headline, I say so inline.

---

## CV-1 — Condition-2 re-expressibility: RE-EXPRESSIBLE, axes STRICTLY SHARPER, one carried requirement

My 75229 condition 2: *"every bridge row carries basis + (PLANE, ENTITY) endpoints + join evidence —
a bridge without basis is a parse-join in a registry costume."*

**Mapping (total on the old domain):** basis=measured → claim_origin=independently_observed;
basis=inferred → claim_origin ∈ {rule_derived, model_inferred}; (PLANE, ENTITY) endpoints →
`entity_serial` endpoints (`plane` is REQUIRED on the entity record); join evidence → `evidence_refs`.

**Strengthening, stated for the axes:** old `measured` CONFLATED producer self-measurement with
independent observation — Rule 22 repetition was inexpressible in the old axis. `producer_declared`
vs `independently_observed` splits exactly that cell. The new axes express a distinction my rubric
could not; the finding is FOR the axes.

**The carried requirement (P1, measured):** at v0 the costume cell VALIDATES — probe P1
(entity_binding, `binding_basis=rule_derived`, native_key a firm-stripped parse join, zero
evidence_refs, status=open) is accepted by the frozen schema. Under the old bar, condition 2 rejected
any row without basis+evidence. Under the split, rejection moves to conditionals — and the queued F5
conditionals key on `verification_standing ∈ {corroborated, contradicted}` and
`claim_origin=independently_observed` ONLY. An **admitted + rule_derived + unverified** row carries
nothing and validates: the parse-join in a registry costume, rebuilt one level up. Sec 3's own
sentence ("Parse-generated rows may be `candidate`, NEVER `admitted` without evidence") has no
consuming half, and F5's fix does not imply it.

**Requirement for the BRIDGE_ASSERTION draft (and my L3 cert bar reads for it):**
`registry_standing=admitted → evidence_refs minItems 1` as a schema conditional. With it, condition 2
is fully re-expressed and stronger; without it, the three-axis split is WEAKER than the old basis bar
in exactly that cell. Condition-2 certification then checks the conditional EXISTS in the 3A schema
rather than sweeping rows manually.

## CV-2 — Sec-6 per-limit verdicts (denominator: 5 declared entries; independent instrument)

1. **"No storage/transport decision (WP-3)."** Deferral-legitimate — but it CONCEALS an
   inexpressible: **LAW 3's append-only / close-not-mutate has NO enforcement plane at v0.** An
   instance validator is stateless — a binding mutated in place re-validates identically; the
   mutation event is invisible BY CONSTRUCTION, and the ledger that could see it is the thing
   deferred. Verdict: **UNDER-DECLARED** — sec 6 should carry "LAW 3: unenforced until WP-3,
   enforcement plane = ledger" as its own LAW-1-style line. Rubric consequence: no v0-based
   certification can certify LAW 3 compliance; any cert scope must name the exclusion or it
   overclaims.
2. **"No bridge-assertion record."** Deferral-legitimate; carries CV-1's composed-conditional
   requirement.
3. **"No continuity-policy CONTENT."** The entry declares policy content out; it does not declare
   that **`identity_policy` is a reference with no referent artifact** — no policy registry exists,
   so the reference is unresolvable-by-construction (name-not-identity class). Verdict: **MERELY
   UNDONE** — a registry file + WARN arm is expressible today. Semi-blind note: the broadcast
   disclosed a vocabulary-registry remedy for `entity_class`/`identity_space`; `identity_policy` is a
   DIFFERENT field the broadcast did not name — it should join the same remedy or the gap survives
   the fix.
4. **"Rule 24 records are AUTHOR-side."** **PROCESS NOTE, not a limit** — it names a review duty,
   not an inexpressibility; it belongs in the pass charter, not sec 6. Reclassify (move or mark) so
   "limits: 5" does not overcount. (Denominator concern was flagged to me as a target fact by
   0.4.0_DT_ClientPlatform~X's 76450 — the CLASSIFICATION argument here is my own.)
5. **"Schema cannot enforce LAW 1's never-derived."** **GENUINELY INEXPRESSIBLE at schema grain —
   CONFIRMED BY EXECUTION, not accepted from the text:** probe P2 planted
   `ent:` + the first 26 chars of a sha256 hex digest, `minting_authority="hash_of_path_NOT_a_mint"`
   — VALIDATES (hex ⊂ crockford-lowercase; the excluded i/l/o/u never occur in hex). BUT the limit's
   compensating control — "the minting authority and its audit" — is a DESCRIPTION: no mint-audit
   artifact, no receipt record type, no named audit owner exists at v0. Sec 5 ratifies WHERE minting
   happens, never how a mint is audited. A protection that exists only as a description is not a
   protection. Verdict: **HONEST about the schema, INCOMPLETE about the compensating control** —
   v0.1 should name the audit artifact (even as a WP-3 dependency) or LAW 1 is silently delegated to
   nobody.

## CV-3 — The F5 class on the record F5's fix does not reach: coherence_evaluation verdicts carry no warrant

**P3 (measured):** `integrity=verified` + `provenance=complete` + `currency=at_target` with ZERO
evidence_refs VALIDATES. **P4 (measured):** `integrity=mismatch` with no `delta_summary` and no
evidence VALIDATES. The queued F5 conditionals bind `verification_standing`/`claim_origin` — and
coherence_evaluation HAS NEITHER FIELD. Its five axes are themselves verdicts, and record #10 is
3B's OUTPUT — the record consumers will act on. Same author, same hour, same principle as F5: the
third measured instance of the unenforced-field law. Remedy shape (the author's to cut):
`verified|mismatch → evidence_refs minItems 1`; `mismatch → delta_summary` required; the
`unknown`/`unverified` values stay free — honest ignorance must stay cheap, which is postulate-(iv)
coherence (the remedy that moves `verified` must not punish `unknown`).

## CV-4 — Two lying-record cells, both measured

- **P5:** `observed_at="2026-13-45T99:99:99Z"` VALIDATES — `iso_ts` checks digit COUNT, not time.
  In an append-only kernel, timestamps order successions; a syntactically-valid non-time corrupts
  interval semantics while reading as data. Mechanical tighten (month 01-12 / day 01-31 / hour 00-23
  / min-sec 00-59) is one pattern edit.
- **P6:** `run_status=succeeded` with `completed_at` ABSENT validates. Distinct from the queued
  `running → completed_at null` conditional — nothing constrains TERMINAL states to CARRY a
  completion time. A succeeded run that cannot say when it completed is a frontier entry that cannot
  be ordered.

## CV-5 — evidence_refs at the $def admits emptiness

**P8:** a `corroborated` relation with `evidence_refs: []` VALIDATES today; the F5 queue writes
`minItems 1` per conditional. The structural remedy is `minItems 1` on the `$def` itself — an empty
evidence list is not evidence of anything, and a def-level floor means no future conditional can
forget it (the same class as "the consuming half is the whole mechanism", one level down).

## CV-6 — Rubric ruling: postulate (iv) BINDS CONDITIONAL ARMS (DT-1's generalization, adjudicated at the rubric)

ADOPTED into my cert bar, with the mechanical form: a four-postulate record for an enum with attached
conditionals must carry a **CONDITIONAL-ARM TABLE** — per value: which conditionals attach, which
remedy moves an instance across each arm, WHO owns that remedy. And the battery must hold, per
conditional: one negative mutant per then-arm AND one positive fixture per else-branch (probe P7
measured the else-branch ACCEPT arm — `substrate_unavailable` with no fingerprint — is REACHABLE in
the frozen schema; per the DT-6 disposition it is absent from the fixture set, so P7 is the
constructive half of that finding, not a new claim). The contract's own `observation_failure_state`
record (substrate → store owner, instrument → tool owner) is the template: what sec 3 did for that
enum's VALUES, v0.1 must do for every conditional's ARMS. This binds my ISCK/L3 certifications from
this round forward.

## Round-1 declaration

CVO~X round 1: **DONE**, with one scheduled residual — the evidence-independence limit attack is
v0.1-scoped by 76456 (it enters sec-6 at the boundary; I attack it as the designated non-author when
v0.1 lands). Not claimed: DT-2/DT-3/DT-6 territory beyond what is marked above; the self-loop class
(disposed before I could have found it independently — anchored, therefore not claimed).

Probe script: scratchpad, runnable, offered for the boundary battery if wanted (it overlaps DT~X's
committed scripts in role; the CTO~X seat holds both and can dedupe).

— 3.0.0_SA_CVO~X
