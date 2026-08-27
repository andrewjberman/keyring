# CVO~X proof-of-spec verdict — NFRA_SUBSTRATECARDING.TO-W1-CCX · **PASS**

**Verifier:** 3.0.0_SA_CVO~X · **Verified at:** 2026-08-26 ~19:1xZ · **Lane:** 0.8.0_AE_CloudComp~X (73163)
**Artifacts verified:** commits `7bb29e2514` + `7d5ef9f3ab` — **both re-measured ON origin/CLOUD at my
seat** (fetch + `merge-base --is-ancestor`, bogus-hash positive control fired). Files held stable by the
lane during this pass (their 73194) — verified vintage = delivered vintage.

## Battery (all my own invocations, none cited from the lane)

| check | result |
|---|---|
| `proof-of-spec-check.py` with `CCX-AC1..AC7` | **VALID rc=0** · rows=7 violations=0 · alignment ENFORCE · fwd-1 7/7 · fwd-2 23/23 · backward 23/23 · vintage c8aa46b1a5 RESOLVES |
| v1 schema over C0/C1/C2 | **0 errors, 3 of 3 cards** |
| basis+evidence+owner per row | **21 of 21 rows carry all three; zero blank, zero guessed-owner** |
| AC3 / F-1 (denominators) | **PASS, exemplary** — every coverage row is N-of-M with sums closing exactly (C0 48/58 types + volume split; C1 22/53 + volume; C2 19+6,207=6,226 no residue) |
| AC4 / F-2 (inference_detail) | **VACUOUS-TRUE as disclosed** — all three `determinism: unknown` (the honest value), no inferential/hybrid, trigger never armed. Each card names the instrument that would settle it |
| AC5 / F-3 (INCOMPLETE iff absent) | **PASS** — 0 rows carry `basis: absent`; QUALIFIED/QUALIFIED/UNSOUND coherent |
| wave as_of | **byte-identical across 3 cards**, commit_ish `fe269171f2` = anchor, graph_vintage = the pinned projection snapshot |
| evidence back-dating | **CLEAN** — exactly 1 occurrence of the anchor hash per card, and it is the `as_of` field itself |
| spot-read C2 key row / C0 key row | grounded (`file @ commit` vintages); C0's self-caught wrong-object comparison kept on the record — the right conduct |
| census-trap audit | comp-find 4/4 clean by the lane's printed denominators; comp-keys 0 pre-73102 calls, then `--all` used to UPGRADE a held row to measured via a second instrument |

**Verdicts accepted as delivered: C0 QUALIFIED · C1 QUALIFIED · C2 UNSOUND (blocking: 12 declared
families vs 13 served canon classes, zero shared names, `declared_mapping: null` after a hunt —
owner named, not remediated).** Per the governing principle: a card that finds defects is a passing
card; C2 UNSOUND is the card working.

## Rulings issued with this verdict

1. **AC-F3 vs CCX-AC5 phrasing divergence (their obs 1):** the certified decomp's AC-F3 mechanical
   form binds — any row carrying `basis: absent` requires `standing: INCOMPLETE`; an INCOMPLETE over
   worked-to-absent rows is a healthy PASS (CTO~X 72796 cases 3+7); a genuinely UNWORKED row is
   rework regardless of verdict. The TO prose's "genuinely unworked" clause selects which INCOMPLETEs
   are acceptable, not when INCOMPLETE is required. No outcome conflict; moot for CCX (0 absent rows).
   Issuer may align the TO prose at the wave boundary — OBSERVATION, not an interrupt.
2. **`authority_role` flip (their 73194):** NOT required for wave-1 verification. The delivered C2
   card already holds the two surfaces apart (graph rows rebuilt-by-derive = `projection`; untracked
   JSON envelopes behaving like `evidence`), which satisfies the Andrew-direct's operative concern
   without a unilateral enum flip. The schema-semantics call belongs to the issuer/schema owner at
   the wave boundary.
3. **Proposed amendment (73194 items 1–3):** verification-compatible — it changes no verdict and no
   denominator and strengthens rows 1/4 for the named downstream consumer. Acceptance is the
   ISSUER's call, not mine. **Files are released from verification hold as of this verdict**; if the
   amendment lands, I re-run the mechanical battery on the amended vintage (cheap, deterministic).

## P2 observations (no action required)

- `as_of.carded_utc` is identical to the second across all three cards (18:17:02Z) while file
  mtimes span ~30 min — one clock read reused, not per-card. No vintage incoherence results (it
  strengthens wave identity); noted because the decomp's s.3.1 says per-card.
- Declared exclusion carried forward for the record: all three cards measured mapping COVERAGE,
  never mapping CORRECTNESS (their own disclosure #3).

---

## ADDENDUM 2026-08-26 ~21:5xZ — C1 coverage claim WITHDRAWN by the lane (73801); PASS scope clarified

The lane's wave-2 carding of `NFRA_ONTOLOGY_RULE_BANK.yaml#relations` falsified C1's central
coverage claim: "31 of 53 edge_types bound by no declared block / 64.4%" is FALSE — the wave-1 read
built its declared universe from the relations block's KEYS and never opened `binds_up` members;
the true figure is **53 of 53 / 100% declared**. Affected rows: coverage.denominator,
coverage.explicitly_out, key.declared_mapping, verdict.why defect (1). C1 stays QUALIFIED (its
other defects rest on untouched rows); anyone who consumed the 64.4% or the 31-unbound list treats
both as withdrawn. Amendment sequenced by the issuer per the declared-delta pattern; narrow
re-check at this seat when it lands.

**Scope statement for future readers of this PASS:** the battery verified schema conformance, row
completeness, alignment, vintage discipline, and evidence FORM. It does not and structurally
cannot verify that a lane's instrument was pointed at the right OBJECT — a well-formed, printed-
denominator, positively-controlled number over the wrong object passes every check the verifier
holds. The cross-check that catches this class is what caught it: independently re-reading the
definition at source in a later wave. A PASS here is a form-and-process verdict, never a truth
warrant on every figure.

— 3.0.0_SA_CVO
