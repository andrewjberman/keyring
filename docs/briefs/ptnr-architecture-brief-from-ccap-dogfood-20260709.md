# PTNR / CCAP — Architecture Brief from the Cottonwood Dogfood

**Status:** MSTR → CTO. Supplements the `PTNR_STRUCTURE` PRD request (`docs/briefs/ptnr-structure-prd-request-20260709.md`, LD-0268).
**From:** `0.0.0_AB_MSTR` · **To:** `1.0.0_SA_CTO` · **Date:** 2026-07-09
**One line:** We ran a real partner's fee-intelligence corpus (Christa Bass / Cottonwood) through a proto-`PTNR` structure *before* the PRD is built. The dogfood validated the schema, produced the acceptance-test fixture, and surfaced a set of requirements no design session would have found. This is that record.

---

## 0. Why this exists

`PTNR_STRUCTURE` was chartered as *pipe-first, water-second* (LD-0268): build the structure, then run a partner through it. Andrew reversed the order for one partner in-session — he fed the Cottonwood corpus in live, and we distilled it against a hand-built proto-structure. **The proto-structure held.** Every schema decision in LD-0268 now has a worked example, and the failures we hit are the PRD's real acceptance criteria.

**Treat this brief as the empirical half of the PRD.** LD-0268 is what we intended; this is what a real partner's data actually did to it.

---

## 1. The two-store architecture (validated)

The load-bearing decision (LD-0268 **D1**): **raw out of repo, distilled in.** It now has a concrete shape.

```
RAW  (never git)                                  DISTILLED  (git, macro PTNR)
Desktop/partners/                                 ajb_workspace/partners/
  README.md            <- the raw-store contract    README.md          <- schema + pull contract
  <partner>/                                        _schema/           <- event/want/archetype/crosswalk
    PARTNER.md          identity card                <partner>/
    .manifest.jsonl     THE BRIDGE                     PARTNER.md       identity (distilled)
    attachments/        xlsx pdf csv png               events/          append-only, immutable
    calls/              audio vtt docx                 register/        wants.md + wants.json (DERIVED)
    csv/                machine-readable extracts       artifacts/       POINTERS ONLY (raw_id, s3 key)
    unlocked/           decrypted working copies        .cursor.json     durable ingestion cursor
    annotations/        per-artifact analysis + notes
    _inbox/             gitignored drop zone
                                                    ALSO out of git:
                                                    s3://opal-data-partners-raw/<partner>/
                                                    s3://opal-data-partners-distilled/<partner>/
```

**The split is a storage boundary, not a folder convention.** Client names, revenue figures, and end-client PII live ONLY on the raw side and in `opal-data-partners-raw`. The repo holds events, the derived register, and **pointers** (`raw_id` + `sha256`) — never a payload.

**Live example (Cottonwood, tonight):** 27 raw-side artifacts, 0 bytes of client data in the repo. The `partners/` directory does **not** exist in the repo yet — correctly, because `.owned-paths.yaml` has no `partners/**` rule and the gate would block it (§7).

### 1.1 The manifest is the bridge, and it is the whole trick

`.manifest.jsonl` — one JSON line per raw artifact — is what lets a repo event *reference* a raw file without *containing* it:

```json
{"raw_id":"39f1b84105d87530","sha256":"<64hex>","partner":"cottonwood","kind":"attachment",
 "path":"cottonwood/attachments/Revenue since inception_ Bass 72026.xlsx","bytes":121856,
 "source":{"system":"adhoc","origin":"Downloads"},"confidentiality":"partner-confidential",
 "body_available":false,"body_unavailable_reason":"irm-or-password-encrypted-ooxml (OLE2 CFB with Encrypted stream)",
 "derived_from_raw_id":null,"ingested_at":"2026-07-09T17:33:00Z"}
```

- A distilled event cites the **`raw_id`**. The `sha256` makes the citation *verifiable*: every derived number traces to the exact bytes it came from, and a raw file that changes under a claim is detectable.
- `derived_from_raw_id` chains a CSV or annotation back to its source artifact. Tonight: every one of the 7 derived CSVs and 9 annotations chains back to the single encrypted workbook `39f1b84105d87530`.
- **Integrity is checkable in four lines** (re-hash every manifested path; compare to `sha256`). Tonight's store: 27 rows, **0 hash drift, 0 unmanifested files, 0 ghosts.**

**This is the design's answer to the session's through-line** (§5). A manifest that prints its own denominator — how many rows, what's readable, what's missing — is an enumerator that cannot silently lie about coverage.

---

## 2. Schema

### 2.1 `PTNR` (structural macro) vs `CCAP` (instance)

- **`PTNR`** = the partner-agnostic structure: directory contract, schemas, archetype enum, ingestion pattern, derivation rule, confidentiality model. Partner-neutral.
- **`CCAP`** = Cottonwood Capital Advisors, the inaugural partner. First need: `CCAP_FEEINT` (fee intelligence → ADVI "Business Intelligence" panel).
- Partner needs are `{PARTNER_MACRO}_{NEED}` → `CCAP_FEEINT`.

### 2.2 Crosswalk — one entity, four identities (validated as necessary)

Cottonwood proved the crosswalk is not optional. It exists in this estate under **four** codes:

| identity | code | where |
|---|---|---|
| Relationship (partner brain) | `CCAP` | this workstream |
| Data pipeline / bucket | `cot` | `opal-data-cot` |
| ETL project | `ADVI_COTETL` | `org/projects/` |
| Their own shorthand | `CCA` | their email / meeting titles |

`_schema/crosswalk.yaml` is the single source. `cot`/`ADVI_COTETL` stay the **data** identity; `CCAP` is the **relationship** identity. **Do not merge.**

### 2.3 Event record (append-only, immutable)

```yaml
id:              # sha256(source_system + source_id)[:16]
ts:              # ISO-8601 UTC
kind:            # email | call | meeting | attachment | note | portal_feedback
source: {system, message_id, conversation_id, thread_subject}
participants:    # [{name, email, org, role}]
direction:       # inbound | outbound | internal
summary:         # <= 3 sentences
signals:         # [{archetype, polarity, strength, quote_ref}]
confidentiality: # public | internal | partner-confidential | restricted
body_available:  # true | false
body_unavailable_reason:   # MANDATORY when body_available:false
evidence_pointer:          # raw_id / s3 key. Never the payload.
```

### 2.4 Archetype enum (closed, versioned)

`ASK_ACCESS · ASK_CAPABILITY · ASK_DATA · BLOCKER_EXTERNAL · BLOCKER_INTERNAL · FRICTION · COMMITMENT_OURS · COMMITMENT_THEIRS · SATISFACTION · DISSATISFACTION · CONTEXT_FACT · RISK`

Closed set in `_schema/archetypes.yaml`. Adding a member is a schema change with a migration — **not** a free-text field that silently accretes synonyms. (An open vocabulary is an enumeration nobody maintains — §5.)

### 2.5 Want/need record — **DERIVED, never authored**

```yaml
want_id:  first_raised:  last_raised:  times_raised:   # times_raised IS the signal
archetype: status:  days_open:  blocker: {kind, description, evidence_event_id}
evidence: [event_id...]   owning_project_code:   confidence:
```

`wants.md` is generated from `events/`, carries the event-tree hash, and **declares itself STALE when the hash diverges.** Hand-editing the register is a defect, not a shortcut. **Why this is non-negotiable:** a hand-maintained board beside an event log is two expressions of one truth, and nobody executes a board — it drifts silently. The Cottonwood corpus *contains a live instance of exactly this failure* (§4.4).

---

## 3. The ingestion + verification pipeline (as exercised)

Every artifact tonight went through the same path, and each stage earned its place:

1. **Ingest raw** → copy to `attachments/`/`calls/`, or paste into `_inbox/`. Originals never moved.
2. **Classify readability at the door.** Compute magic bytes / CFB streams. `body_available` + reason. (§4.1)
3. **Extract to machine-readable** (CSV), one artifact per source sheet.
4. **VERIFY the extract against the source's own internal totals** before trusting it. (§3.1)
5. **Annotate** — a first-class artifact per sheet: what it is, its scope, its traps, its open questions.
6. **Manifest** every output with `sha256` + `derived_from_raw_id` + verification verdict + known anomalies.
7. **Cross-reference** artifacts against each other; record disagreements, never silently merge. (§4.5)

### 3.1 The verification discipline — "prove the alignment, don't assume it"

The `NET REV SINCE INCEPTION` sheet arrived as a ragged whitespace-delimited paste (clients who joined mid-history have leading blanks). A one-column mis-shift was the obvious silent failure. **So the parser was made self-verifying:**

- **Check 1:** per-column sum of the 72 client rows must reproduce the `Total AUM Net Revenue` row. **PASS, all 29 columns, to $0.00.**
- **Check 2:** `AUM + Consulting + Insurance` must reproduce `GRAND TOTAL`. **PASS.**

That is not a nicety. It is the difference between a parse we *believe* and a parse we can *prove*. When the unlocked Sheet-5 export arrived later, MSTR re-verified the transcription against it: **0 diffs across 63 client rows × 15 columns.** The hand-transcription was exact — but we only know that because we checked, not because we asserted it.

**PRD requirement:** every extract must reconcile against a source-internal invariant before any downstream artifact consumes it. `could-not-reconcile` is a finding, not a silent pass.

---

## 4. Findings — the requirements a design session would have missed

These are why the dogfood mattered. Each is an empirical requirement, discovered by running real data.

### 4.1 Unreadable is not empty (the encryption finding)

The workbook is **IRM/RMS rights-managed** (`EncryptedPackage` + `DRMEncryptedDataSpace`, no `EncryptionInfo`). Graph's Workbook API returns `501 WorkbookNotSupported`; the rights bind to Andrew's identity, so only his Excel can open it.

**And our own M365 MCP gateway failed the exact way the product must not:** on the same file, `read_workbook` returned an honest `501`, but `read_document` returned `byte_size:0` and **`read_file` returned `content:"", truncated:false`** — an unreadable file reported as an empty one. Any agent calling `read_file` would conclude the revenue tracker is blank. **Routed to CTO + OPLMCP owner as a gateway defect.**

**PRD requirement:** `body_available:false` + a mandatory reason. An ingestion that files an unreadable artifact as empty is the same defect class as a CloudWatch alarm resting at `OK` through a freeze. *"Could not read" is a finding.*

### 4.2 Scope changes mid-workbook (the 7× error)

Sheets 1 & 2 are **Christa's book only**; Sheet 3 is **firmwide** with a Bass carve-out. For 2025, **Bass = 13.6% of firm revenue, 9.4% of firm AUM.** Reading Sheet 1 as firmwide would have been wrong by **~7×** — and would have looked completely plausible.

**PRD requirement:** every derived artifact carries its scope (denominator) in its own body. A number that does not state its denominator invites the reader to supply one, and the reader supplies "the firm."

### 4.3 Two derivations downstream of the source (the provenance chain)

The real source is **Commonwealth's pivot table** (custodian, clean). What we received was: **Commonwealth pivot → Christa's hand-maintained tracker → Copilot's summary.** Each step lost fidelity; the last one **fabricated a quarter** (§4.6). Andrew independently articulated the general law tonight, on a separate Orion thread: *"partner pipelines get clean data from the custodian, and something breaks in the hand-off to Black Diamond/Orion."*

**PRD requirement:** `CCAP_FEEINT` sources from the **custodian extract**, not the tracker. The tracker becomes a thing to reconcile *against*, not rebuild *from*. The manifest's `source` + `derived_from_raw_id` fields make the derivation depth explicit and auditable.

### 4.4 Two hand-maintained records of one book disagree (the product thesis)

Sheet 1 and Sheet 3's Bass block both describe Christa's 2025 revenue. **They disagree in 6 of 12 months**, from three structurally distinct causes: an insurance in/out definitional difference (December), a recurring `~$506.48` item classified inconsistently (Jan–May), and unexplained AUM-level deltas (Aug `+$1,036`, Sep `-$530`). **Verified not a parse artifact** — no column offset reconciles them, and the 72 client rows corroborate Sheet 1 to $0.00 (§4.5).

**This is the argument for `CCAP_FEEINT`**, stronger than the one we started with: the product is not a prettier chart of numbers she has — it is a **single derived source where components reconcile by construction**, so "which spreadsheet is right?" stops being a question. It is our own doctrine (derive the reported value from the source; never maintain two expressions) sold as a partner deliverable.

### 4.5 Never silently merge (the entity crosswalk)

62 entities match exactly across Sheets 1↔2; 10 are Sheet-1-only, 4 Sheet-2-only. The tempting inference — *"revenue ends early in Sheet 1 ⇒ churned"* — is **falsified**: `ASKINS, JACK & MARILYN` ends 9 columns early yet appears in Sheet 2 at $2,009.84. And `ALEMAYEHU, ASHLEY & BK` (S1) vs `ALEMAYEHU, ASHLEY` (S2) is almost certainly one household — **not merged.** "Almost certainly" is how a fuzzy match becomes a fabricated join.

**PRD requirement:** entity resolution proposes candidates; a human confirms. Auto-merge on name similarity is banned. `WMCA` (Commonwealth) vs `WMCF` (Sheet 3) — one letter apart — is the canonical trap; they are **not** established as the same thing.

### 4.6 The Copilot audit — five failures, five gates

Sheet 5 is Copilot-generated and author-disclaimed (*"I'm assuming this isn't accurate"*). Audited against the source, it is **Sheet 1 to the cent, 35/36 quarters within $0.50, with exactly one fabricated cell**: Advisory Q1 2024 = `$59,536`, true value `-$90` — the quarter *before the book existed*. That one cell overstates FY2024 by ~$59,626 and reports growth as **+19.9% when the truth is ~+56%.** The sheet even **refutes itself**: its own client detail sums to `$0` for the quarter its summary values at `$61,780`.

The five failures map 1:1 onto five gates `CCAP_FEEINT` must carry:

| Sheet-5 failure | Gate |
|---|---|
| Invented a pre-inception quarter | **Inception mask** — a period before the book exists is `null`, never `0`; YoY against it refuses to render |
| Client detail ≠ firm summary | **Cross-foot by construction** — the rollup is derived from the detail; no two independent aggregates |
| Projection ignored its own stated method | **Stated method = executed method** — derive the printed assumption from the code that applies it |
| FY-total ≠ sum of components | **Totals computed, never typed** |
| Three FY24 figures, undocumented `0.89` factor | **Every figure names its source + transform** — gross/net is a labelled axis |

### 4.7 Anchoring a series by triangulation, with provenance

Sheet 1 arrived with **no header row**. Rather than guess months from the sheet name, `period_label` was left empty and the calendar was *derived*: Sheet 3's `Bass WMCF` series matches Sheet 1's `Consulting` exactly for Jun–Dec 2025 (7/7), fixing `p01 = 2024-01`. **Independently confirmed twice more** — Sheet 5's Copilot column map (`2026: Z…AD, actual data ends May 2026`) and Commonwealth's own description of the report layout (*"year at the top, months 1-12"*). Three independent sources, none aware of the others. The labels ship with `label_provenance: "derived:anchor p13=2025-01 via sheet3 Bass series"`. **Provenance travels with the derived value.**

### 4.8 The upstream lead (`S58`) — routes around the standing blocker

Commonwealth's extract lists *"households under the **S58 ID**."* If `S58` is Christa's rep code, **the advisor→household mapping that Black Diamond lacks already exists at the custodian** — the exact `BLOCKER_INTERNAL` Andrew named ("client info not tagged by advisor"). This is the single most promising lead for generalizing `CCAP_FEEINT` from one advisor to all Cottonwood advisors, **without** waiting on BD advisor-tagging. `INFERRED, not confirmed` — an ASK in the drafted reply, not an assumption.

---

## 5. How this maps to the session's through-line

Every finding above is one defect class, the same one that ran through the whole 2026-07-09 session: **an instrument reporting confidently on something other than what it claims to measure**, and its sibling, **an enumerator that finds nothing being indistinguishable from one that cannot see.** CTO's formulation — *comments are unexercised code* — and DS~B's — *an enumerator that finds nothing and one that cannot see are the same output* — are the governing principles.

The partner-data instances:
- `read_file` returns `""` on an unreadable file → **existence ≠ content** (§4.1)
- A number with no scope reads as firmwide → **value ≠ denominator** (§4.2)
- Copilot's "quarterly summary" fabricates a quarter and reports it as data → **rendered ≠ measured** (§4.6)
- A hand-maintained board drifts from its event log → **reported ≠ derived** (§4.4)
- `delivered` on a dead channel; four charters stranded in an unwatched dir → **sent ≠ reached** (LD-0269; the same night, the same class)

**The design principle that falls out, and it is the PTNR invariant:** *every artifact in the partner brain states its own denominator, its own provenance, and its own readability — and the register is derived, never asserted.* A partner brain built any other way reproduces, in a new surface, every failure this session catalogued.

---

## 6. Confidentiality model (the incident this is built to not repeat)

`opal-data-schwab` holds raw client PII, its pseudonymized derivative, **and** the reverse-mapping key that undoes the pseudonymization — **in one bucket.** Bucket-level IAM structurally cannot express *"may read the anonymized data, may not re-identify it."* That was tonight's SEV1-consequence PII exposure.

**PTNR does not reproduce it:**
- `opal-data-partners-raw` and `opal-data-partners-distilled` are **separate buckets**, separate principal-agnostic Denys. **A prefix is a policy statement; a bucket is an enforceable boundary.**
- Bucket universe derived at runtime (`s3api list-buckets`), never a hand-written literal.
- A commit-time confidentiality lint over `partners/**` — blocks end-client names, revenue figures, any `body_available:true` payload text. Fails closed, prints its denominator.
- Firm separation binds: Cottonwood / Inflection / 49 Financial never cross-read.

---

## 7. Prerequisites — CTO's lane, blocking (unchanged from LD-0268, now with evidence)

1. **`.owned-paths.yaml` must declare `partners/**`** before a single file commits there. `owned-paths-check.sh` runs `MODE=block` and refuses undeclared paths — **verified empirically tonight** when an unrelated `archive/**` move was blocked for exactly this reason. Suggested lane: exec + AE + `0.0.0_AB_MSTR`, note *"partner brain; distilled artifacts only; no raw payloads."*
2. **`.gitignore` must precede the directories** (`partners/**/_inbox/`, `.partners-cache/`, `partners/**/raw/`). A create/move breaks ignore rules, not just pointers — **also verified tonight** (a `models/` archive move would have silently added 300 gitignored artifacts).
3. **`_schema/crosswalk.yaml` lands first**, as one source: `CCAP ↔ cot ↔ ADVI_COTETL ↔ CCA`.

---

## 8. What I'm asking CTO to do

1. **Fold this brief into the `PTNR_STRUCTURE` PRD as its empirical half.** LD-0268 is the intent; this is the validated shape + the discovered requirements.
2. **Use the Cottonwood store as the acceptance-test fixture.** The derived register generator must reproduce, from the events, the four legible wants (portal access `times_raised≥3`, model-perf, advisor-intel-superficial, fee-intel→CCAP_FEEINT) — and must reproduce Christa's 66 relationships and `$168,035.70` exactly, or it is not ready. *It must reproduce what a human can already see.*
3. **Ratify the 5 output gates (§4.6) as the `CCAP_FEEINT` correctness contract** — inception mask, cross-foot-by-construction, stated=executed, totals-computed, source+transform-labelled.
4. **Route the two live tool defects** the dogfood surfaced: (a) M365 gateway `read_file`/`read_document` returning empty on an unreadable file (§4.1); (b) confirm the confidentiality lint (§6) as a commit-gate build.
5. **Decompose via COO** once the PRD is written. Sequencing: prerequisites → schemas → ingestion → derivation → lint → **exercise on the Cottonwood fixture** → only then scope `CCAP_FEEINT`.

**Do not scope `CCAP_FEEINT` in `PTNR_STRUCTURE`.** It is the water; this is the pipe. And the pilot is deliberately **advisor-scoped** (Andrew: *"for now it's just Christa… a mechanism to prototype for all Cottonwood advisors"*) — the entity grain is advisor→relationship, never firm→relationship, and generalization is gated on the `S58` upstream tag, not assumed.

---

## Appendix — the Cottonwood store as it stands (raw side, `Desktop/partners/cottonwood/`)

27 manifest rows, 0 hash drift, 0 unmanifested: 1 encrypted attachment (`body_available:false`), 1 screenshot, 1 call transcript (993 cues), 4 raw pastes, 7 derived CSVs (reconciliation-verified), 1 unlocked export (transcription-verified 0-diff), 9 annotations (one per sheet + reconciliation + Commonwealth thread + 2 email drafts), 3 store docs (`README`, `PARTNER.md`, `OPEN_QUESTIONS.md`). Repo side: **empty, by design** — awaiting the §7 prerequisites. Nothing client-facing has been asserted to the partner; an unlocked source file has been requested.
