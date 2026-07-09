# PTNR_STRUCTURE — PRD Request (MSTR charter → CTO decomposition)

**Status:** CHARTER ISSUED — awaiting CTO PRD breakdown
**Issued by:** `0.0.0_AB_MSTR` (Tier-0) · **Issued to:** `1.0.0_SA_CTO`
**Date:** 2026-07-09 · **Ledger:** LD-0268 · **Sovereign:** Andrew (direct, this session)
**Macros created:** `PTNR` (structural) · `CCAP` (Cottonwood-as-partner, inaugural instance)
**First project:** `PTNR_STRUCTURE` (this charter) → then `CCAP_FEEINT` (water through the pipes)

---

## 1. Purpose

Build a **partner brain**: an internal, event-sourced record that sources and organizes everything
about a partner in one place — leaning specifically into *communications* — such that a partner's
**developing wants and needs are tracked event-by-event** and become the basis for partner-specific
project codes of the form `{PARTNER_MACRO}_{NEED_CODE}` (e.g. `CCAP_FEEINT`).

Two macros, deliberately separated:

- **`PTNR`** — the *structure*. Directory contract, schemas, ingestion patterns, distillation and
  archetyping, derivation rules, confidentiality model. Partner-agnostic. This charter.
- **`CCAP`** — the *instance*. Cottonwood Capital Advisors, the inaugural partner. Runs water through
  the pipes `PTNR` builds. First need: `CCAP_FEEINT` (fee intelligence → ADVI "Business Intelligence" panel).

`PTNR_STRUCTURE` must land, and be exercised on real Cottonwood data, before `CCAP_FEEINT` is scoped.

---

## 2. Sovereign decisions (Andrew, direct, this session — ratified, not open)

| # | Decision | Rationale |
|---|---|---|
| **D1** | **Raw out of repo, distilled in.** | The corpus contains a partner's net revenue, their internal A/B/C client tiering, named end-clients, and at least one Purview-encrypted message. Raw payloads land in a gitignored local cache + S3. **Only distilled, reviewed artifacts commit to git.** |
| **D2** | **Event log → derived register.** | Append-only events are the only hand-touched layer. The wants/needs register is **regenerated** from them, never hand-edited. |
| **D3** | **On-demand skill + durable cursor.** | `/partner-sync <partner>` pulls since a persisted cursor. The m365 MCP gateway is interactively authenticated and may be **absent** in headless/cron runs; a scheduled poll fails silently. |
| **D4** | **`/partners` + `PTNR` + `CCAP`.** | Root dir `partners/{cottonwood,inflection,49financial}`. `cot`/`ADVI_COTETL` remain the **data-pipeline** identity; `CCAP` is the **relationship** identity. Two identities, deliberately, with one documented crosswalk. |

---

## 3. Why the derived-register rule is non-negotiable

This session catalogued **sixteen independent instances** of one defect: *an instrument reporting
confidently on something other than what it claims to measure* — a `DryRun` that writes, a gate printing
`WARN` while its epoch blocked, a comment reading `warn (default)` above code defaulting to `block`, an
alarm resting at `OK` through a seven-day freeze on a client-facing number.

The general form, ratified as Tier-0 doctrine (CTO): **comments are unexercised code.** The remedy:
**derive the human-readable claim from the enforcing expression, or delete it. Never maintain both.**

A hand-maintained wants/needs board sitting beside an event log is exactly two expressions that agree
until they don't — and nobody would find out, because nobody executes a board. **The register is
generated. Hand-editing it is a defect, not a shortcut.**

---

## 4. Directory contract (v0)

```
partners/
  README.md                     <- THE deliverable: the formatting + pull contract
  _schema/
    event.schema.json
    want.schema.json
    archetypes.yaml             <- the closed enum, §6
    crosswalk.yaml              <- partner <-> pipeline <-> project codes, SINGLE SOURCE
  cottonwood/
    PARTNER.md                  <- identity card: org, people, systems, codes, domains
    events/                     <- APPEND-ONLY, immutable, one file per event
      2026-07-02T2126Z__email__fryman-access-to-models.md
      2026-07-07T2000Z__call__opal-x-cca-bd-data-sync.md
    register/
      wants.md                  <- DERIVED. Header names the events/ HEAD hash. Do not edit.
      wants.json                <- machine form, same derivation
    artifacts/                  <- POINTERS ONLY (s3 key, graph message-id). Never a payload.
    _inbox/                     <- gitignored. ad-hoc drop (transcripts, decks) -> ingested -> emptied
    .cursor.json                <- durable ingestion cursor, per source
  inflection/                   <- same shape, created empty
  49financial/                  <- same shape, created empty
```

Raw cache (never git): `.partners-cache/` (gitignored) and `s3://opal-data-partners-raw/<partner>/`.

---

## 5. Event record (append-only, immutable)

```yaml
id:              # deterministic: sha256(source_system + source_id)[:16]
ts:              # ISO-8601 UTC
kind:            # email | call | meeting | attachment | note | portal_feedback
source:
  system:        # m365 | adhoc
  message_id:    # graph id, or file sha for adhoc
  conversation_id:
  thread_subject:
participants:    # [{name, email, org, role}]
direction:       # inbound | outbound | internal
summary:         # <= 3 sentences, distilled
signals:         # [{archetype, polarity, strength, quote_ref}]
confidentiality: # public | internal | partner-confidential | restricted
body_available:  # true | false
body_unavailable_reason:   # e.g. "purview-encrypted" -- NEVER record absence as "no content"
evidence_pointer:          # s3 key / graph message id. Never the payload.
```

**`body_unavailable_reason` is mandatory when `body_available: false`.** *Bass Revenue Tracker*
(2026-07-09) is Purview-encrypted: its existence is knowable, its body is not. An event that silently
records an encrypted message as empty is the alarm-at-`OK` failure, reproduced in a new system.
**"Could not read" is a finding. It is never "nothing there."**

---

## 6. Archetypes — the closed enum (v0)

`ASK_ACCESS` · `ASK_CAPABILITY` · `ASK_DATA` · `BLOCKER_EXTERNAL` · `BLOCKER_INTERNAL` · `FRICTION` ·
`COMMITMENT_OURS` · `COMMITMENT_THEIRS` · `SATISFACTION` · `DISSATISFACTION` · `CONTEXT_FACT` · `RISK`

Closed, versioned, in `_schema/archetypes.yaml`. Adding a member is a schema change with a migration —
**not** a free-text field that silently accretes synonyms. An open vocabulary is an enumeration that
nobody maintains.

---

## 7. Want/need record (DERIVED — regenerate, never author)

```yaml
want_id:        # CCAP-W-003 pre-promotion; becomes CCAP_FEEINT on promotion
title:
archetype:
status:         # surfaced | acknowledged | scoped | promoted | delivered | declined | dormant
first_raised:   # {event_id, ts}
last_raised:    # {event_id, ts}
times_raised:   # THE signal. "asked three times, still blocked" must fall out for free.
days_open:
blocker:        # {kind: internal|external, description, evidence_event_id}
evidence:       # [event_id, ...]  -- every field above traces to an event
owning_project_code:   # null until promoted (e.g. CCAP_FEEINT)
confidence:
```

`wants.md` carries a generated-from header naming the `events/` tree hash. A register whose header hash
does not match the current event tree is **STALE and must say so in its own body** — it prints its own
denominator (how many events, what window, which sources). *A gate must print its denominator* (0.8.0's
standing rule, CTO-ratified).

---

## 8. Ingestion (`/partner-sync <partner>`)

1. Read `.cursor.json` (per-source `last_id` + `last_ts`).
2. Pull from Graph since cursor: partner domains + named people (see `PARTNER.md`).
3. Ad-hoc: ingest anything in `_inbox/` (transcripts, decks) through the same pipeline.
4. For each new item: classify confidentiality → write raw to cache/S3 → emit event.
5. **Write-then-advance.** The cursor advances *only after* the event is durably written. Never
   advance-then-write: a crash between them is silent, permanent data loss.
6. Regenerate the register. **Diff it.** Surface new/changed wants to the operator.
7. Emit `last_successful_sync_iso` and the denominator. **"No new mail" and "the sync is dead" must not
   look identical.** Absence of email is not evidence of no email.

---

## 9. Confidentiality model — the load-bearing constraint

`opal-data-schwab` today holds raw client PII, its pseudonymized derivative, **and** the reverse-mapping
key that undoes the pseudonymization, in **one bucket**. Bucket-level IAM structurally cannot express
*"may read the anonymized data, may not re-identify it."* That cost this fabric a SEV1-consequence
exposure and a full day.

**Do not reproduce it.** Raw partner comms and distilled artifacts belong in **different buckets**, not
different prefixes of one bucket. Prefix separation is a policy statement; bucket separation is an
enforceable boundary.

Required controls:
- `s3://opal-data-partners-raw/` and `s3://opal-data-partners-distilled/` — separate buckets, separate
  principal-agnostic Denys. Derive the bucket universe at runtime (`s3api list-buckets`); **never a
  hand-written literal.** Correcting an enumeration is not the fix; removing the dependence on it is.
- A commit-time lint over `partners/**` tracked files: block end-client names, revenue figures, and any
  `body_available: true` payload text. Fail closed; print its denominator.
- Firm separation binds here as everywhere: Cottonwood, Inflection, and 49 Financial are separate
  partners and never cross-read.

---

## 10. Hard prerequisites (blocking; CTO's lane)

1. **`.owned-paths.yaml` must declare `partners/**` before a single file is committed there.**
   `owned-paths-check.sh` runs in **block** mode (`MODE="${OWNED_PATHS_MODE:-block}"`, `:29`) and refuses
   any path with no matching rule: `UNDEFINED -> VIOLATION`. Verified empirically today. Suggested lane:
   exec + AE + `0.0.0_AB_MSTR`, note *"partner brain; distilled artifacts only; no raw payloads."*
2. **`.gitignore` must ignore** `partners/**/_inbox/`, `.partners-cache/`, and any `partners/**/raw/`
   **before** the directories exist. A move (or a create) breaks ignore rules, not just pointers.
3. **`_schema/crosswalk.yaml` lands first.** `CCAP` (relationship) ↔ `cot` (bucket/pipeline) ↔
   `ADVI_COTETL` (ETL project) ↔ `CCA` (their name in email). One source. Everything else references it.

---

## 11. Acceptance criteria (machine-checkable)

1. `partners/README.md` states the schemas, the derivation rule, and the pull contract. It **is** the template.
2. `/partner-sync cottonwood` ingests the existing corpus — the Christa Bass / Jay Rubottom threads plus
   the 07-07 58-minute call transcript — and emits events with correct participants and direction.
3. The derived register surfaces **at least these four wants**, each traced to evidence event-ids:
   - **`ASK_ACCESS` — portal/dashboard access**, `blocker: external (compliance/beta)`, and
     **`times_raised >= 3`** (Christa, 2026-07-02: *"I know I've asked this a few times"*).
   - **`ASK_CAPABILITY` — model-level performance over horizons** (Jay Rubottom, 2026-07-07).
   - **`BLOCKER_INTERNAL` — advisor intelligence superficial**: BD lacks history; client info not tagged
     by advisor.
   - **`ASK_DATA` — fee / revenue intelligence** (the 07-07 call + *Bass Revenue Tracker*) → the
     `CCAP_FEEINT` seed.
4. **Determinism:** running the register generator twice over an unchanged event tree produces
   byte-identical output.
5. **Idempotence + crash-safety:** killing `/partner-sync` mid-run loses no event and re-running is a no-op.
6. **Zero leakage:** the confidentiality lint passes; no end-client name or revenue figure appears in any
   tracked file.
7. **Honest absence:** the *Bass Revenue Tracker* event exists with `body_available: false`,
   `body_unavailable_reason: purview-encrypted`. It is **not** recorded as empty.
8. The register prints its denominator and flags itself STALE when its header hash ≠ the event-tree hash.

---

## 12. What CTO is asked to decompose

- `PTNR_STRUCTURE` PRD in `docs/architecture/` (CTO's lane), decomposed into TOs by COO.
- The three enabling patches (§10) as **prerequisite** TOs, not discoveries.
- A `comp-partner` tool surface (`sync`, `register`, `lint`, `crosswalk`) — the register generator is a
  tool, never a prose exercise.
- `/partner-sync` skill.
- Sequencing: prerequisites → schemas → ingestion → derivation → lint → **exercise on Cottonwood** →
  only then scope `CCAP_FEEINT`.

**Do not scope `CCAP_FEEINT` inside this PRD.** It is the water; this is the pipe. `CCAP_FEEINT` targets
the ADVI "Business Intelligence" panel and is a separate PRD, gated on `PTNR_STRUCTURE` being exercised
against real data — because a structure that has never carried a real partner's contradictions is a
structure that has never been tested.
