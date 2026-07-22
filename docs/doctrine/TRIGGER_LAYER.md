# TRIGGER LAYER — a structural finding lands as a GATE or an OWNED BLOCKING ITEM, never as a note

**Status:** doctrine (binds future behaviour). **Authored:** 2026-07-22, `1.0.0_SA_CTO~Z`, under the
Andrew-direct postmortem handover @`7cc6376e5`. **Mechanism + gate design:**
`docs/architecture/NFRA_PSTMRT_PRD.md` §4. **The incident record:**
`docs/references/MDPF_POSTMORTEM_20260722.md`.

---

## The rule

**A structural finding — a defect of a CLASS, not an instance — lands as a GATE or an OWNED BLOCKING
ITEM. Never as a note. A finding that cannot fail a gate is a diary entry.**

An instance defect ("this partition is stale") can live in a report: someone is looking at it now. A
STRUCTURAL finding ("this enumeration cannot notice its own missing member") is a claim about every
future change — and future changes do not read old reports. The only carriers that reach the future
are (a) a gate that fires at the moment of violation, and (b) a tracked item with a named owner whose
absence of progress is itself visible.

## Why prose findings die (the mechanism, so the rule is obeyable)

- **A note has no failure mode.** It cannot fire, so no moment of work ever stops on it. The 05-08
  `comp-constants` note named the exact firm-set defect that later cost a quarter — verbatim, in the
  right file, eleven weeks early — and could stop nobody (`comp-constants.config.yaml:615`).
- **An honest flag nobody owns is halfway to no flag.** The 207h-stale danger map flew an accurate
  staleness flag with zero actors attached. Honesty without an owner is telemetry, not a control.
- **An inexpressive gate dies of noise, which is the same death from the other side.** A gate that
  cannot express "known, accepted, by whom, until when" re-reports ratified conditions forever, trains
  its readers to skim, and a skimmed gate is a dead gate that still looks alive (BL-1,
  `comp-constants.config.yaml` header). Expressiveness — structured severity, ownership, auditable
  exemption with loud expiry — is what keeps a gate alive, and is therefore PART of this doctrine,
  not a nicety.
- **Progress claims decay fastest and nothing expires them** (LD-0334). An owned item with a
  `review_by` is the expiry mechanism a note structurally lacks.

## What this binds

1. **Any agent recording a structural finding** files it where it can fail — a gate condition, or a
   tracked item `{owner, severity, review_by}` — in the same pass as discovering it. The prose
   description may accompany the filing; it may not BE the filing.
2. **Any comp-tool whose output includes structural findings** carries them as machine-checkable
   fields (`severity: blocking|advisory`, owner, expiry), never solely as free text. The lint is on
   the STRUCTURED FIELD, never a text-match over prose (matchers that fire on mentions are the wrong
   mechanism — LD-0274 boundary).
3. **Any reviewer accepting a deliverable** that contains a structural finding recorded only as prose
   sends it back: the finding is unfiled.
4. **Exemptions are first-class:** `{firm/site, by, date, why, expires}` — an exemption the gate
   honours without recording its authority is a hole with better manners.

## The boundary (what this does NOT license)

- It does not license new detectors. The estate's gap is the trigger layer, not the lens count
  (postmortem: 89 comp-tools, the failure was never missing instruments).
- It does not license bulk-converting historical notes into findings — that manufactures a hundred
  unowned items and kills the gate on day one. Conversion is at touch time, with an owner attached.
- It does not make every observation a blocking item. INSTANCE findings route as normal work;
  ADVISORY structural findings are legal — but they carry an owner and an expiry, or they are
  diary entries and this doctrine says so out loud.

**Related:** `CONTROLS_OVER_CARE.md` (care is not a control — this file is the trigger-side corollary:
a finding is not a control either, until it can fail) · `INSTRUMENTS_AND_AXES.md` 7a-7f ·
`NFRA_PSTMRT_PRD.md` §4 (the comp-findings gate that enforces clause 2).
