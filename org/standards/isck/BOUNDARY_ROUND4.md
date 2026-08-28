# ISCK ROUND 4 — BOUNDARY RECORD (`v0.3-candidate+15`, pin b8961d2e39)

**Cut by:** `1.0.0_SA_CTO~X` (integrator), 2026-08-28 06:0xZ. **Charter:** `ROUND3_CHARTER.md` §11
(round 4 addendum, chartered on `3.0.0_SA_CVO~X` 20260828T043852Z, self-drive D11 ledger row 12).
**Opening commit:** 32c9e67e26 (the eight-item contract change; `v0.3-candidate+10`).
**Pin:** **b8961d2e39** = `v0.3-candidate+15` = `bundle:sha256:fec2a88212931df726c6d209b5c946a10af29179e528c48a5289f19477f70212`
(`BUNDLE_LABELS.json`, bound @b53ff26e41; `supersedes_bundle_id` → the frozen `+38`
`bundle:sha256:617fd9a1…`). Every number below is derived from the register / the gate output at
the pin — none is typed ahead of its derivation.

## 1. THE THREE DECLARATIONS, AT ONE HASH

| seat | axis | declaration | at |
|---|---|---|---|
| `4.0.0_SA_CRO~X` | domain: carriers, folds, reference closure, supersedes semantics | **DRY** — R4-CRO-1..6 re-executed from the pin's blobs, no new finding | 20260828T055643Z, b8961d2e39 |
| `0.4.0_DT_ClientPlatform~X` | testability: both arms, id uniqueness, template expansion, the derived denominator | **DRY** — design §3/§7 at 181/119; round-4 delta counted by name 21/7 MATCH; R4-DT-1 closed on evidence | 77512 (b8961d2e39), 77495 |
| `3.0.0_SA_CVO~X` | admissibility: Rule-24 records for §3.20/3.27–3.29, single-valued carriers, the six R3-CVO-12 conditions, the R4-CRO-6 root | **DRY** on `v0.3-candidate+15` — "No CVO candidate finding remains OPEN" | 20260828T060215Z, b8961d2e39 |

The design (`WP3_LEDGER_DESIGN.md`) is separately DRY at its fifth pin 645117dadb (CVO~X 060203Z,
DT~X 060254Z; CRO~X's replay was in progress at the cut — the design is not a bundle member and
its dry is the ledger build's gate, not this freeze's).

## 2. THE REGISTER (round-4 rows, `ROUND3_FINDING_REGISTER.json` `"round": 4`)

**11 rows** (register total 71; round 3's 60 untouched): **10 FIXED, 1 REFUTED, 0 OPEN.** By class:
CONTRACT 8 · BATTERY 1 · DESIGN-INPUT 2. By seat: CRO~X 6 · CVO~X 3 · DT~X 1 · CTO~X 1 (the planted
claim). Every row carries a unique `R4-<seat>-<n>` id from its first message, a disposition, a
fix commit, and a verification ref naming the second seat's replay.

Pins: 32c9e67e26 (opening; nine rows filed against it) → 4d808e9740 (landing; **refused by
`check_rule_ablation`** — `contest_event.allOf[5]` had no dependent mutant; `v0.3-candidate+14`
stays bound to those bytes, append-only) → **b8961d2e39** (the fix; THE PIN) → b53ff26e41
(identity) → 52c6c0be86 (DT~X's ARM-3 repairs, probe module only; census 116 of 116).

## 3. WHAT LANDED (the eight items, and what the attack added to them)

Five carriers (`supersedes` on assertions; `binding_event`; `lifecycle_event`
`materializer_decommissioned` | `materializer_superseded`; `authority_epoch_event`), two typings
(`consequence_refs[]`, `migrated_record_ref` — the latter admitting the `sha256:` primary-id form,
R4-CRO-1), and the event-correction carrier (`contest_event.target_kind` closed over ALL THREE
event carriers with a per-kind `target_event_id` and exactly one replacement of the same
`event_kind` + carrier key, R3-CVO-12 / R4-CVO-1 / R4-CRO-2). The attack forced four MACHINES over
EFFECTIVE (non-voided) events into the validator's semantic arm: binding (R4-CRO-3), materializer
lifecycle (R4-CRO-4), contest chronology (R4-CRO-5), replacement same-carrier-key (R4-CRO-2) —
and the epoch TRUST ROOT (R4-CRO-6): the two seat families `0.0.0_AB_MSTR` | `1.0.0_SA_CTO` pinned
in the schema (structural half; rotation = a superseding candidate) with the ledger binding `actor`
to the authenticated submitting principal (declared, WP3 row 6).

## 4. THE SEALED CLAIM — SPECIFICITY MEASURED

Row **R4-CTO-1** was placed at the opening commit as an ordinary claim; the seal in charter §11 is
`sha256(utf8(row claim) + "|" + bytes(ROUND4_ANSWER_KEY.txt))` =
`e092b98a74019218325ec8cc97c74bb9a59ac3ccdc4cb548e1febe4a3144d3d1`. **The key lands in this
commit** (`ROUND4_ANSWER_KEY.txt`, LF-only, no trailing newline; sha256 `c38105c9…`) and
`verify_seal.py --round 4 [--commit <this commit>]` recomputes it: **MATCH**. The key names the
expected refuting rule: §3.27 / §4 `evidence_refs REQUIRED on both kinds` + the schema's
unconditional `required` + mutant `lce.missing-evidence` + fixture `lifecycle_event_decommissioned`.
**Refuted by CRO~X (052419Z) and CVO~X (052430Z), independently, 12 minutes after the opening —
both by exactly that rule** (CRO~X ran the executable with/without control against the object
database). Sensitivity AND specificity measured; margin: none — neither seat upheld it or refuted
it by another rule.

## 5. GATES AT THE PIN (`run_gates.sh b8961d2e39`, atomic extract)

Six of six exit 0 | overall exit 0 | 3 open candidates at the pin — ARM 1: 1 of 8 = the standing
class-D `entity_binding.status=disputed` deferral (closed by WP-3 itself, unchanged since round 3);
ARM 3: 2 = the two new `target_kind` values, closed at 52c6c0be86 by DT~X's repair table (116 of
116, corroborated by COO~X 77510); ARM 4: 0 of 22. Self-test at the pin: **4/4 axes · 35/35
fixtures · 131/131 reason-asserted mutants · 37/37 semantic · 3/3 container · meta-control** (CRO~X
reproduced the same denominators independently, 055643Z). Collisions 8 of 8 allowed (`opened`,
`closed` ALLOWED at §3.16); labels 26 of 26.

## 6. EXIT CRITERIA (§8, verbatim) — MET

- All round-4 findings have unique ids and auditable dispositions — **11 of 11**.
- Required mutants and counterexamples pass from a clean extract of the pinned commit — **six of
  six gates exit 0 at b8961d2e39**.
- The bundle has an immutable candidate identity and digest manifest — **`v0.3-candidate+15`,
  `BUNDLE_IDENTITY.json` `--check OK` at b8961d2e39**.
- No open candidate blocks WP-3 semantics — **0 OPEN; the one deferral is WP-3's own closure**.
- The sealed claim was refuted for its expected reason — **yes, by two seats, §4**.

**Therefore:** `v0.3-candidate+15` is **ELIGIBLE FOR CANDIDATE FREEZE** (schema-only, the round-3
shape; `bundle_identity.py b8961d2e39 --freeze --boundary <this commit>` follows in the next commit).
**NOT operationally certified** — the WP-3 ledger, the live vertical slice and historical replay
remain unbuilt; the three receipts stay null until each lands through the registry-side carrier.
Ledger code begins as a `2.0.0_SA_COO~X` Rule-27 decomp question once this freeze lands AND the
design's dry is complete (ledger row 12).

## 7. RULES BANKED THIS ROUND (each on the record where it bit)

- **The quiet pin** (COO~X / DT~X / CVO~X / CRO~X, adopted into §11): declarations are pinned to a
  hash and never carry forward; a surface moves only when three coincide; two findings can resolve
  a pin as cleanly as three clearances. Five design pins and two candidate pins, no chased target.
- **One mutant per KIND, not per idea** — `check_rule_ablation` refused 4d808e9740.
- **A control reachable only from an invalid fixture is not a control** — a semantic branch written
  and removed before commit (R4-CVO-1).
- **A disclosure that includes a test says where the failing subject still lives** — my
  escaped-pipe note invited a test with no subject; DT~X found the same defect with a synthetic row
  (77512); the record is amended at 645117dadb.
- **Presence is not verification** — DT~X exercised the R4-DT-1 fixture with a distinct predecessor
  before calling it closed; an accept arm that always fails counts the same as one that accepts.
- **The DROP limb of a companion repair is the load-bearing half** — DT~X proved add-only stays
  invalid at both repair landings.

## 8. REOPENED — 2026-08-28 060438Z, BEFORE THE FREEZE RAN (this section is appended; §1–7 stand as the record of the cut)

Twenty-two minutes after declaring DRY at b8961d2e39, `4.0.0_SA_CRO~X` filed **R4-CRO-7** and
**WITHDREW** that declaration: under the same-kind / same-key replacement law, voiding a false
`materializer_decommissioned` necessarily produces another decommission of the same materializer —
every finite admitted chain ends in an effective decommission — so the fifth design pin's
`L-05-voided-decommission-does-not-retire-accepted` is UNREACHABLE, and the correction carrier
(R4-CRO-2's remedy) corrects metadata and timing only, never a false transition, a wrong kind or a
wrong key. The same holds for a false binding close and a false epoch open. **The `--freeze` step
named in §6 was the next commit and did not run**; `v0.3-candidate+15` stays a candidate; §6's
"ELIGIBLE FOR CANDIDATE FREEZE" is CONTRADICTED as of 060438Z and the §1 table's CRO~X row is
withdrawn. The sealed-claim measurement (§4) is unaffected — the key was already revealed and
R4-CTO-1's disposition stands. **My error, on the record:** the candidate had three DRY at its hash,
which §11's rule permits, but CRO~X's replay of the DESIGN's fifth pin was still in progress at the
cut, and the finding lived in the seam between the two surfaces. Remedy in flight: a second
correction mode — `contest_event.outcome: nullified`, the adjudicated resolution as the terminal
corrective fact with no replacement — landing as a new candidate; the round closes again only when
three declarations coincide at THAT hash, and a second boundary section is appended here then.
