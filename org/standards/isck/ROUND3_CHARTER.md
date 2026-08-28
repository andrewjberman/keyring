# ISCK ADVERSARIAL PASS — ROUND-3 CHARTER (bounded: provenance, publication, suppression, refutation specificity, bundle identity)

**Cut by:** `1.0.0_SA_CTO~X` · **2026-08-28 ~02:4xZ** · **Authority:** `3.0.0_SA_CVO~X`'s C3 verdict
(self-drive D11 tick 7, 20260828T020732Z, ledger row 5) on the GPT memorandum's §7 (pinned at
`org/tier1_exec/1.0.0_SA_CTO/deliverables/D11_GPT_ISCK_STATUS_ASSESSMENT_20260828/`), sequenced AFTER
the R2-2 landing — which exists: **@bf6fbe53d9**. Andrew has NOT opened this round by name; it opens
on the delegated adjudication the loop runs under (his 2026-08-24/27 self-drive words), and he may
close it with one word.

**ATTACKED INPUT (frozen for the round):** `bf6fbe53d9` — the R2-2 landing tip. Gates at that tip
(atomic extract, this seat): six of six exit 0 | 8 open candidates (ARM1 8 disposed by record,
ARM3 0, ARM4 0 of 21). Any finding cites `file:line @ bf6fbe53d9` or a constructed instance run
against a git-archive extract of it; a working-tree number is not a citation (DT-R2-3).

---

## 1. OBJECTIVE (one sentence)

Prove that the contract can represent ONE coherent consumed state (`source_frontier`), ONE
immutable produced state (`surface_version`), ONE admissible publication path, and ONE reproducible
evaluation target — while REJECTING contradictory or suppressive alternatives — and that the
package can name ITSELF immutably.

## 2. IN SCOPE (the memo's five, with CVO~X's precision)

1. **`source_frontier`** — coordinate identity, uniqueness, completeness, locality, time ordering.
   ARM 1 is structurally blind here (no discriminant): every finding needs a constructed instance.
2. **`surface_version`** — links to frontier, materializer version, run, logical surface, physical
   instance, authority publication. Same blindness.
3. **The ARM-4 CONSUME GATE as a possible SUPPRESSION mechanism** (`isck_coverage_probes.py`
   `_dispose` + `ARM4_ADJUDICATION.json`): can a ruling hide a live arm? A missing consume line
   must render UNREAD, never zero (COO-R2-1's remedy under attack).
4. **REFUTATION SPECIFICITY — a PREDECLARED deliberately-false claim.** CVO~X's charter precision,
   verbatim: *"predeclare at least one deliberately false claim and require its correct refutation
   by the expected evidence/rule; do not use the memo's ambiguous phrase 'false acceptance'."* The
   integrator files the planted claim SEALED (a sha256 of its text + expected refutation rule in
   this file's §7 before the round opens; the text revealed at the boundary). An attacker who
   upholds it has measured the round's specificity, not sensitivity.
5. **IMMUTABLE CONTRACT-BUNDLE IDENTITY** — memo Appendix C: `contract_bundle_id`,
   `semantic_version`, `status: candidate | frozen | retired`, doctrine/schema/validator/gate-suite
   commits + digests, vocabulary digests, round boundary commits, post-boundary amendments,
   receipts, `supersedes_bundle_id`. Attack: one label mapping to two byte-distinct bundles must be
   REJECTED or forced to distinct candidate ids. The record is authored by `1.0.0_SA_CTO~X` as
   `BUNDLE_IDENTITY.json` + its Rule-24 record; the attackers refute it.

## 3. EXPLICITLY OUT OF SCOPE (a finding here is routed to the surprise channel, not the round)

- Reopening opaque minted serials vs hash-derived identity (Andrew's ISCK ruling @d869c9ffe0).
- Reopening the binding/fingerprint split.
- Designing the fusion algorithm, DEC-02..05 thresholds, or filling the 56 L3 bridge cells (HELD).
- Adding a new GENERAL governance mechanism — memo §11's operating principle, adopted: *"No new
  general governance mechanism unless the vertical slice exposes a defect that the current
  machinery cannot express."* A round-3 defect that needs new machinery is a FINDING against the
  machinery, filed, not built.
- WP-3's persistence engine / API form (open by design; memo §12).

## 4. REQUIRED ATTACK MATRIX (memo §7, verbatim targets; each row is a constructed instance)

| target | attack | expected result |
|---|---|---|
| source_frontier | same semantic coordinate twice with conflicting `source_version` | REJECT as contradictory |
| source_frontier | same source through syntactically different but equivalent coordinates | normalize or HOLD; never silently double-count |
| source_frontier | a device-local source omits owning fabric/device | REJECT or mark frontier incomplete |
| source_frontier | observation timestamp later than the run that claims to consume it | REJECT temporal impossibility |
| source_frontier | completeness claimed without a declared expected-source denominator | REJECT unsupported completeness |
| source_frontier | unavailable source OMITTED rather than represented | REJECT or downgrade provenance; no silent disappearance |
| surface_version | references a nonexistent frontier / materializer version / run | REJECT at ledger scope (schema: declare limit 3) |
| surface_version | failed run output becomes current authority without an explicit admissible promotion | REJECT publication |
| surface_version | publication timestamp precedes run completion | REJECT temporal impossibility |
| surface_version | physical Kuzu instance claims a logical source version it was not built from | DETECT integrity/provenance mismatch |
| coherence target | `latest_authority` lacks the concrete authority head resolved at evaluation | REJECT non-reproducible evaluation |
| consume gate | a missing or suppressed line is read as zero candidates | UNREAD, never zero |
| adversarial process | the sealed deliberately-false claim (§7) | REFUTED with evidence; refutation recorded in the register |
| bundle identity | one semantic version label maps to two byte-distinct bundles | REJECT or distinct candidate ids |

Each row lands as a finding id (`R3-<seat>-<n>`) in `ROUND3_FINDING_REGISTER.json` (same schema
as round 2's; the renderer is reused) — **the register is built DURING the round, not after it**
(round 2's owed-denominator lesson, CRO-BV4).

## 5. SEATS AND INDEPENDENCE

| seat | role | independence note |
|---|---|---|
| `4.0.0_SA_CRO~X` | attacker: frontier + surface + bundle identity; carries the ARM-3 half of any re-verify | not an author of any round-3 artifact |
| `3.0.0_SA_CVO~X` | attacker: consume-gate suppression + refutation-specificity adjudicator (rules whether the planted claim was refuted FOR THE RIGHT REASON); Rule-24 certification of new records | author of record on `f2281ce7cb` (ARM-3 fix) — does NOT re-verify ARM 3 |
| `0.4.0_DT_ClientPlatform~X` | attacker: instrument-side (probes/gates/consume gate); owner's run of ARM 1-4 at every cited tip | owns the probe module — its gate findings are corroborated by CRO~X's run, never by its own re-run |
| `2.0.0_SA_COO~X` | gates (labels/collisions/ablation/isolation) + the register's denominator audit + decomp cells if a finding needs a seat | — |
| `1.0.0_SA_CTO~X` | integrator: dispositions, landings at cited commits, the sealed claim, the bundle-identity record | author; issues NO refutation of its own findings |

Build-time anchoring (round 1/2's unresolved class) is DISCLOSED again, not cured: every attacker
reads this charter.

## 6. RULES BINDING THE ROUND (round-2's, kept; two added)

- **No moving target:** every landing is ONE commit at a cited hash; attackers re-attack at the new
  citation, never the tree. Gates run via `run_gates.sh <commit>` (atomic extract).
- **Every patch match-asserted; every "landed" a grep count at the commit** (round-2 RE-1).
- **Both-direction controls:** a mutant per then-arm AND positive coverage per accepting branch;
  a verifier's report carries its own denominator (CVO~X's re-verify rule).
- **Unique finding ids from the first message** (NEW): a finding without an `R3-` id is not filed.
- **A refutation names the rule or evidence that refutes** (NEW, CVO~X): "does not reproduce" is
  not a refutation; the refuting arm/citation is.
- Attack-dry declarations by BOTH attackers close the round; the integrator cuts the boundary.

## 7. THE SEALED CLAIM (refutation-specificity control)

⛔ **AMENDED 2026-08-28 ~03:4xZ on R3-DT-5 (`0.4.0_DT_ClientPlatform~X`): as first written, this
control could NOT fire.** The claim's TEXT lived only in the integrator's scratchpad and was never
placed in any artifact an attacker reads — so "no attacker refuted it" would have read as attacker
effort when the accurate statement was "no attacker could have" (the watcher-status / ARM-3 class:
a control that cannot fire in the state it exists to detect). **Corrected shape, applied before the
boundary:** the CLAIM is PLACED in a landed artifact at the moment of sealing — in this round,
`ROUND3_FINDING_REGISTER.json` row **R3-CTO-2**, filed as an ordinary claim to adjudicate; only the
ANSWER KEY (claim text + expected refuting rule, whose sha256 is the seal below) stays private. A
session death then costs the key, not the claim, and the boundary sentence is either "refuted by
the expected rule" (specificity MEASURED), "upheld / refuted by a different rule" (a specificity
FINDING), or "planted, un-found by N attackers" — never "unmeasurable". Future rounds seal this way
from the opening commit.

`sha256(claim_text + "|" + expected_refuting_rule)` = **`402da6e06c5d813b1350e9a1c4a01fd860945e11b8dfa84fb0cf065217f839af`** (computed 2026-08-28 at the opening commit; the sealed text is held ONLY in the integrator's session scratchpad -- a session death before the boundary loses it, and the boundary then states specificity UNMEASURED rather than reconstructing a claim; the successor may seal a fresh one in a new commit) **``** — filled by the
integrator in the OPENING commit of the round (this charter's commit carries the seal; the claim
text is revealed in `BOUNDARY_ROUND3.md`). The seal is computed by the integrator alone; no
attacker sees the text. If NO attacker refutes it by the boundary, the round's sensitivity is
measured and its specificity is NOT, and the boundary says so.

## 8. EXIT CRITERIA (memo §7, adopted verbatim with the register requirement)

- All round-3 findings have unique ids and auditable dispositions in `ROUND3_FINDING_REGISTER.json`.
- Required mutants and counterexamples pass from a clean extract of the pinned candidate commit.
- The contract bundle has an immutable candidate identity and digest manifest (`BUNDLE_IDENTITY.json`).
- No new open candidate blocks WP-3 semantics.
- The sealed claim was refuted for its expected reason (or the boundary states specificity UNMEASURED).

**On exit:** contract FREEZE becomes eligible (memo §10 "candidate freeze" column: clean-clone gates
+ round-2 register/candidate closure + round 3 closed + pinned identity bundle); operational
certification (WP-3 ledger + live vertical slice + historical replay) remains a SEPARATE gate. The
first production record is not written under a contract that cannot prove its own bundle identity.

## 10. CLOSED — `BOUNDARY_ROUND3.md`, pin dcbe214a44 (2026-08-28 04:0xZ)

Both attackers DRY; 30 rows, 0 OPEN; the sealed claim revealed and proven pre-declared (seal
recomputed over the register row + key); exit criteria §8 all MET. Candidate freeze ELIGIBLE;
operational certification NOT — see the boundary record.

## 9. OPENING STATE

Seats live at cut (broker read 02:3xZ): CRO~X, CVO~X, DT~X, COO~X — 4 of 4. Round OPENS on this
charter's commit; first attacks cite `bf6fbe53d9`. The integrator's first act after the cut: the
bundle-identity record + the sealed claim (same turn, next commit).

## 11. ADDENDUM — ROUND 4: `v0.3-candidate` (chartered 2026-08-28 04:5xZ on `3.0.0_SA_CVO~X` 20260828T043852Z, self-drive D11 ledger row 12)

**Why a round 4 exists.** The WP-3 design attack (`WP3_LEDGER_DESIGN.md` §2b) found that the FROZEN
`v0.2-candidate+38` cannot carry five facts append-only and leaves two reference fields untyped. Per
C5's last sentence and §2b's ruling, those land as a NEW candidate — never a mutation of `+38`.

**Scope — seven items, closed (a finding outside them routes to the surprise channel):**

| # | item | carrier / change |
|---|---|---|
| 1 | assertion supersession | `supersedes` (backward) on `identity_relation` + `bridge_assertion`; `superseded_by` becomes derived (refused on write) |
| 2 | binding open/close | `binding_event {opened \| closed}` with `binding_id`, `occurred_at`, `actor`, `evidence_refs` |
| 3 | materializer decommission | `lifecycle_event materializer_decommissioned` |
| 4 | materializer process supersession | `lifecycle_event materializer_superseded` with `superseding_version_id`; `superseded_by_version` becomes derived (refused on write); ONE per materializer |
| 5 | mint-authority epochs | `authority_epoch_event {opened \| closed}` with `authority_id`; overlap rejected, reopening legal |
| 6 | `contest_event.consequence_refs[]` | typed: record-id union (`rel:` \| `bind:` \| `ctev:` \| the binding_event id) |
| 7 | `migration_receipt.migrated_record_ref` | typed: record-id union over the catalog |

Each item lands with its schema conditionals, fixtures, mutants (both arms per then-arm) and the
fold it feeds in `WP3_LEDGER_DESIGN.md` §4. **Out of scope:** anything in `+38` the design did not
route; the ledger engine; the battery runner.

**Identity.** The family rule in `bundle_identity.py` (amended on ledger row 12): a bundle whose
schema blob differs from the frozen `+38` schema derives a NATIVE label `v0.3-candidate+N` (N =
package-path commits since the round-3 boundary) with `supersedes_bundle_id` = the `+38` bundle id;
a bundle id already bound in the registry keeps its label (no second alias, ever). `+38` stays
immutable; `BOUNDARY_ROUND4.md` cites the pin; `--write` then `--freeze --boundary` operate on the
native v0.3 label.

**Seats and axes — unchanged from §5:** `4.0.0_SA_CRO~X` domain (carrier semantics, folds,
reference closure), `3.0.0_SA_CVO~X` admissibility (a carrier that can return two answers; Rule-24
on every new enum), `0.4.0_DT_ClientPlatform~X` testability (both arms, gates at the atomic
extract), `2.0.0_SA_COO~X` gates + register audit, `1.0.0_SA_CTO~X` author of the bounded change and
integrator; issues no refutation of its own findings.

**Rules — §6 in full, plus:** finding ids `R4-<seat>-<n>` from the first message; rows land in
`ROUND3_FINDING_REGISTER.json` with `"round": 4` (one register, one renderer, the denominator
audit unchanged); **declarations are PINNED** — a dry is a measurement at a named hash and never
carries forward (DT~X 77413); the round is dry when all three declarations coincide at ONE pin,
and the integrator names a QUIET PIN and holds the attacked surface still there until they do
(COO~X 77407 / CVO~X 044801Z / DT~X 77413, adopted). The sealed-claim control (§7, corrected shape)
is placed in the register at the opening commit of the round.

**Exit:** §8 verbatim, with `BOUNDARY_ROUND4.md` and the v0.3 label frozen schema-only. **Then and
only then** ledger code (ledger row 12: "held until the amended design and v0.3 candidate are each
attacked-dry/frozen").
