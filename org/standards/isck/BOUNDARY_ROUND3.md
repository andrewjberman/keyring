# ISCK ADVERSARIAL PASS — ROUND-3 BOUNDARY RECORD

**Cut by:** `1.0.0_SA_CTO~X` · **2026-08-28 04:0xZ** · **On the word of both attackers:** `4.0.0_SA_CRO~X`
DRY across the visible package at 74671f0911 (20260828T033757Z) and re-affirmed at the candidate
a1207ef56f (20260828T035353Z); `3.0.0_SA_CVO~X` DRY at ea64a64850 after its finder replay
(20260828T040032Z). **What this record IS:** the close of the third ATTACK ROUND, chartered at
`ROUND3_CHARTER.md` @51e789ddfb on the GPT memorandum's §7 and `3.0.0_SA_CVO~X`'s C3 verdict.
**What it is NOT:** operational certification — the WP-3 ledger and the live vertical slice are
unbuilt (charter §8, memo §10); this record makes the contract **eligible for candidate freeze**
and nothing more.

---

## 1. VERSION IDENTITY PINS (derived; `bundle_identity.py dcbe214a44 --check` = OK)

```
  ATTACKED INPUT (round-2 landing + R2-2, frozen)   bf6fbe53d9     v0.2-candidate+8   bundle:sha256:2d2a2d9e…
  ROUND-3 CHARTER                                   51e789ddfb
  BOUNDARY PIN (package tip at cut)                 dcbe214a44     v0.2-candidate+38  bundle:sha256:617fd9a18df2…
                                                    (38 post-boundary amendments on the package path since ece1ac0f41,
                                                     enumerated by rev-list -- 25 CTO~X, 7 DT~X, 1 CVO~X, 1 COO~X, +4
                                                     boundary/register commits; the count is derived, not typed)
  LABEL REGISTRY                                    BUNDLE_LABELS.json: +8 and +38 bound; a rebinding REFUSES (exercised rc 1)
  SCHEMA $id                                        still opal:standards:isck:contract:v0.1 -- the label/bundle split is
                                                    deliberate (sec 7); candidate_id is the injective handle (R3-CRO-12)
  PUSH STATE AT CUT                                 LOCAL -- origin/CLOUD @3fbb493cda (ls-remote); 72+ commits ahead; the
                                                    integrator (0.0.0_AB_MSTR) has not run a window this session
```

**Gates at the boundary pin, ATOMIC EXTRACT of dcbe214a44 (`run_gates.sh`, this seat, 04:01Z):**
validate 4/4 axes + 22/22 positive + 100/100 reason-asserted mutants + 22/22 semantic + meta ·
container controls 3/3 · ablation OK · collisions 6 of 6 allowed · isolation 96 of 100 (the four
NON-ISOLATING are the LAW-2 coupling family, INFO) · labels 23 of 23 with the census line (26 headers
= 23 PARSED + 3 NON-RECORD + 0 UNPARSED) · probes ARM1 8 gaps (7 adjudicated, 1 deferred, 0 NEW) ·
ARM3 107 of 107, 0 open · ARM4 22 (22 adjudicated, 0 NEW) · 56 self-controls, none failed ·
**RUN_GATES overall exit 0 | 1 open candidate = the class-D deferred `entity_binding.status=disputed`
(ARM1_ADJUDICATION.md row 3; it is a projection under R2-2 and closes at WP-3).**
Corroborated on the same runner by `2.0.0_SA_COO~X`, `0.4.0_DT_ClientPlatform~X` and `4.0.0_SA_CRO~X`
at ea64a64850 / 74671f0911 (runner corroboration — the RECORD's closure is the attackers' replays).

## 2. TALLY — from the register, derived (`ROUND3_FINDING_REGISTER.json`, 30 rows, `render_round2_register.py --round 3`)

| | count |
|---|---|
| rows (one id per finding, ids unique, assigned from the first message) | **30** |
| FIXED (schema / validator / probes / runner / bundle tool) | 21 |
| AMENDED-RECORD (carriers, counts, attributions, the charter) | 7 |
| REFUTED (by a named rule, both) | **2** — R3-DT-2 (the runner never reads a missing consume line as zero) and **R3-CTO-2 (the planted claim, §4)** |
| OPEN at cut | **0** |
| by seat | CRO~X 16 · DT~X 6 · CVO~X 5 · CTO~X 2 · COO~X 1 |
| verification | every FIXED row carries a second-seat citation at a pin; R3-DT-6's is CRO~X's targeted replay at ea64a64850 |

**Refutation rate, quotable from the register only:** 2 of 30 filed claims refuted; both by a
named rule; one of them deliberately false (§4). Round 2's "0 of ~40" was never a rate; this is.

## 3. THE CHARTER'S FIVE TARGETS — what landed against each (`ROUND3_CHARTER.md` §2/§4)

1. **`source_frontier`** — R3-CRO-5/6/7/8 + R3-CVO-4: `normalization_version` + `canonical_key`
   (non-canonical shapes and same-key-two-versions reject; the normalizer itself is WP-3, §6 limit 12) ·
   entry `referent_scope` with the fabric/device arms (the validator's dead `fabric_id` key retired) ·
   `completeness` + `expected_count` + entry `availability` with `absence_evidence`, constrained in
   BOTH directions (a partial frontier must have something missing; no frontier exceeds its
   denominator) · batch temporal check (no observation after the consuming run's start).
2. **`surface_version`** — R3-CRO-9/10 + R3-CVO-5: batch run↔surface membership and frontier
   identity · `publication_state` with the publication receipt (only a SUCCEEDED run's output, never
   before it completed; `unpublished` REQUIRES the null carrier).
3. **The consume gate as a suppression mechanism** — R3-CVO-2 / R3-DT-3 / R3-DT-4 / R3-CRO-15 /
   R3-DT-6: every sidecar entry now carries `record_ref` + `ruled_at` + `arm_digest`, RESOLVED against
   the trusted repo's OBJECT DATABASE (`ISCK_REPO_ROOT`, exported by the runner; `git show
   <ruled_at>:<path>`; never a working-tree file; declared path, never a basename); orphan → NEW +
   WARN, stale digest → LAPSE, no root → UNRESOLVED named; cache keyed by root; controls (a)–(e) fire
   INSIDE the canonical atomic gate. Two intermediate states are on the record: 8a9ad0644e (resolver
   made the gate a NO-OP — exit 1, 32 open) and 82efe0bb27 (green by reading the working tree —
   a contamination path). R3-DT-2 REFUTED: the runner renders UNREAD, never zero.
4. **Refutation specificity** — §4 below.
5. **Bundle identity** — R3-CRO-12/13/14: injective `candidate_id` + label registry; the ARM-1
   sidecar a member; ABSENT-at-commit part of the identity; "+15" corrected to +17 at its commit.
   Also: `latest_authority` must resolve to a concrete head (R3-CRO-11).

Instrument-class findings that came out of the round's own machinery: R3-COO-1 (runner's raw ARM-1
figure), R3-CTO-1 (labels gate blind to `[]` — fixed by its owner with a subsection census that fails
by name), R3-CRO-16 (`semantic_errors(dict)` returned a clean `[]` — fails fast now).

## 4. THE SEALED CLAIM — REVEALED (charter §7, as amended on R3-DT-5)

**The plant:** `ROUND3_FINDING_REGISTER.json` row **R3-CTO-2** — *"an observed_absent
state_observation whose evidence_refs contains ONLY its own observation_id VALIDATES through both
the schema and the validator's semantic arm at bf6fbe53d9."* Deliberately false: the schema half is
true, the semantic half is not.

**The answer key (held in the integrator's scratchpad until now):** *"validate_isck.py
`semantic_errors()`: the CVR2-1 syntactic self-citation check — `self_tokens` includes the record's
primary id via `_PRIMARY_ID['state_observation'] = 'observation_id'`; an evidence_refs list that is
ENTIRELY self-citation raises `[i] state_observation: evidence_refs is ENTIRELY self-citation …`
(sec 6 limit 2, mechanical subcase), rc=1. The claim is false because the schema half is not the
gate; schema + semantic is the gate (COO-SR1's own lesson, round 2)."*

**Proof it was pre-declared — byte-exact (COO~X 77360 / CVO~X's C4 condition: the prose above is
not a recomputable key):** the key's EXACT bytes are `ROUND3_ANSWER_KEY.txt` (LF-only, no trailing
newline); the composition is `sha256(utf8(register row R3-CTO-2 "claim") + b"|" +
bytes(ROUND3_ANSWER_KEY.txt))`; `python org/standards/isck/verify_seal.py [--commit <sha>]`
recomputes it from the object database and prints MATCH/MISMATCH. `sha256(row.claim + "|" + answer_key)` =
`402da6e06c5d813b1350e9a1c4a01fd860945e11b8dfa84fb0cf065217f839af` — the seal carried in
`ROUND3_CHARTER.md` §7 since the opening commit 51e789ddfb. Recomputed at the cut over the register
row's text; any seat can repeat it.

**Result — SPECIFICITY MEASURED, and the margin recorded (both facts, as `0.4.0_DT_ClientPlatform~X`
and `3.0.0_SA_CVO~X` asked):**
- Refuted by the EXPECTED rule by TWO attackers independently — `4.0.0_SA_CRO~X` (constructed
  instance at bf6fbe53d9: schema 0 / semantic 1, CVR2-1 named) and `0.4.0_DT_ClientPlatform~X`
  (same rule, same construction, unread of the other).
- **DT~X's first pass returned UPHELD** for an instrument reason: `semantic_errors(selfcite)` called
  with a dict iterated the dict's keys and returned a clean `[]`; schema-0 beside semantic-`[]` was one
  sentence from filing UPHELD. Caught by a source read (a declared self-cite mutant sat impossibly
  beside the `[]`), not by the instrument. That misuse is now R3-CRO-16, FIXED at 393c248a09
  (`semantic_errors` fails fast on a non-list; a non-dict member is an error entry).
- **How the control became fireable at all:** as written at the opening commit it could NOT fire —
  the claim text lived only in the scratchpad, so no attacker could refute it (R3-DT-5, UPHELD). It
  was placed in the register as an ordinary row ~40 minutes before the cut; both refutations followed
  within 25 minutes. Future rounds place the claim at the opening commit and seal only the key.

**Next-charter attacker guidance (adopted from COO~X/DT~X):** for anything scored on an EMPTY
result, run the known-bad control through the SAME call first — a wrong-shape call returns the shape
the caller expects.

## 5. WHAT WAS NOT ATTACKED (named, so silence is not coverage)

- The frontier NORMALIZER itself (canonicalization beyond the mechanical shape checks) — WP-3.
- Cross-batch provenance (frontier↔run↔surface beyond one validated batch) — ledger scope, §6 limit 12.
- `identity_relation.retirement` semantics beyond the evidence requirement; the `contest_event`
  fold (open/resolve pairing across batches) — §6 limit 11.
- The vocab registries (`vocab/*.json`, warn-only) — no attack in any round.
- The build-time anchoring class (every attacker read the charter) — disclosed, not cured.

## 6. INDEPENDENCE LEDGER (the honest entries)

- R3-CVO-2 ↔ R3-DT-4: **PARALLEL, independent** — CVO~X forged through `_dispose`, DT~X censused its
  own module; ~2 minutes apart, neither an echo. COO~X read the module at the commit as a third route.
- R3-CTO-2's two refutations: **independent** (DT~X unread of CRO~X's; same rule by the same
  construction is what a specific rule should produce).
- R3-DT-5 ↔ CRO~X's §9 read: **convergent by different limbs** (session-death clause vs no public
  carrier named). Only the integrator could settle it, and did, against itself.
- `f2281ce7cb` / `6286d725e8`: two mis-attributed GOOD acts in opposite directions, corrected on the
  record, never rewritten. The round rule **one writer per file at a time** came out of them.
- Runner corroborations (COO~X, DT~X, CRO~X at the same hash) are seat-axis only — the runner
  reproduces; the record's closure is the attackers' replays.

## 7. EXIT-GATE STATE (`ROUND3_CHARTER.md` §8), per criterion

| criterion | state |
|---|---|
| unique ids + auditable dispositions in the register | **MET** — 30 rows, 0 OPEN, 0 enum violations (COO~X audits at 130e3afb1b / 9b27b8c41e) |
| required mutants + counterexamples pass from a clean extract of the pinned commit | **MET** — §1, atomic extract of dcbe214a44 |
| immutable candidate identity + digest manifest | **MET** — `BUNDLE_IDENTITY.json` v0.2-candidate+38, registry-bound |
| no new open candidate blocks WP-3 semantics | **MET** — the one open candidate is the class-D `disputed` projection, which WP-3 itself closes |
| the sealed claim refuted for its expected reason | **MET** — §4; with the margin stated |

**What this boundary therefore certifies:** the contract at dcbe214a44 is **`v0.2-candidate+38`,
ELIGIBLE FOR CANDIDATE FREEZE** under the memo's §10 "candidate freeze" column (clean-clone gates ·
round-2 register/candidate closure · round 3 closed · pinned identity bundle). **NOT certified:**
operational use — the WP-3 ledger, the live vertical slice and historical replay are the remaining
gates, and they are the next block of work. The first production record is not written under this
contract until they pass.

## 8. WHAT THE ROUND TAUGHT THAT THE PACKAGE NOW CARRIES

- **A control that cannot fire in the state it exists to detect** appeared three times (the sealed
  claim; ARM 3 agreeing with itself; a link guard that proved shape, not provenance) and was caught
  each time by a seat asking "could this arm have returned the other answer?"
- **A disposition typed ahead of the verdict** (mine, R3-CRO-15) and **a derived count quoted as
  "HEAD"** (mine, R3-CRO-14) — both now rules: cite the commit, wait for the seat.
- **The unit of commit is the file; the unit of work is the hunk** — one writer per file at a time.
- **An instrument that returns the caller's expected shape on misuse is worse than one that
  crashes** — fail fast, and run the known-bad control through the same call.
