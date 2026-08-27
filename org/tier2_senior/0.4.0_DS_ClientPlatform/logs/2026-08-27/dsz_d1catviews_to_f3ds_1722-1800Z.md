# Session — `0.4.0_DS_ClientPlatform~Z` — D1_CATVIEWS TO-F3-DS

**Serial:** `0.4.0_DS_ClientPlatform~Z` (site Z, lane inbox `org/mcp/inbox/0.4.0_DS_ClientPlatform/~Z/`)
**Window:** 2026-08-27 ~17:22Z – ~17:45Z
**Project:** `D1_CATVIEWS` ONLY (Rule 27). Seated by `0.0.0_AB_MSTR~Z` msg 9328, recorded by
`2.0.0_SA_COO~Z` msg 9334 @fb87f2161e.
**Archetype:** BUILD (single-assert enforcement TO) + one RECORD-DRIFT observation.

---

## Objective

Execute `D1_CATVIEWS.TO-F3-DS` — enforce the crosswalk-keyspace invariant at registry import.
The invariant `model-class member_id ∈ crosswalk canonical keyspace` was **TRUE 9 of 9 and
enforced by NOTHING**; a rule true by convention and unenforced reads identical to one that is
guaranteed, and the first violation is also the first test.

Secondary: determine the true state of `TO-R1-DS`, which MSTR and COO both assign to this lane.

---

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| `to-check.py` | `python .tools/to-check.py D1_CATVIEWS` | PASS (rc=0) | 25 active TOs / 7 projects; D1_CATVIEWS 4 ACTIVE + 1 PENDING. **This is the instrument that measured the TO-R1-DS addressing drift** — it renders the `To:` field as it stands on disk, not as a message describes it. |
| `comp-which` | `comp-which "how do I grep the repo"` | PASS | XXX.md A.3 exercise, scored on OUTPUT not rc: a forwarder produced its own banner, so the rail is live rather than merely resolvable. PATH denominator 98 of 105 comp-tools resolve bare. |
| `comp-pipescript io` | `comp-pipescript io mdpf_category_registry.py --pipeline mdpf` | WARN | DS role minimum, run on the one gold script touched. `READS: (none detected) / WRITES: (none detected)` + WARN on no s3_layout constants. **Recorded as the tool's blind spot, not as a finding** — this module is a pure in-process registry with no S3 I/O by design. Same WARN `~F` recorded on the same file. |
| `comp-blast` | `comp-blast mdpf_category_registry.py` | NOT-FOUND | DS role minimum for schema changes to a write target. **NOT a "nothing breaks" clear, and the tool says so itself.** Denominator printed: 20,779 nodes in the canonical kuzu graph; this module is not a node in it. Ran ~2min (backgrounded past the 120s timeout). |
| `comp-pulse diff` | invoked by `safe-commit.sh` (NFRA_NERVES risk reflex) | CLEAN | DENOMINATOR: 1 file checked against 1351 danger nodes; danger map 17.3h old — that is the vintage the verdict is scoped to. |
| `.tools/commit-gate.sh` | `bash .tools/commit-gate.sh data/mdpf/scripts/gold/mdpf_category_registry.py` | PASS (rc=0) | py_compile + ds-precommit + ruff py39 over 1 file. AC4's named evidence. |
| `audit-archive-invoker.py` | `python .tools/audit-archive-invoker.py` (XXX.md Step 1b A.2, mandatory at load) | FINDINGS (expected) | 8 tamper-vocabulary findings — `NON-APPEND-EDIT` / `ERROR-FAILCLOSED`. **EXPECTED on this device, not tampering.** `rv0057-f001` is mid-flight: `chain_root()` `:100-112` falls back to the legacy flat root, *"which IS the laptop chain,"* when `archive/<device>/` is absent — and `org/audit/archive/` holds **32 flat timestamp dirs, no `<device>/` level** (verified at source here). So a site-Z seat compares device-local live logs against the LAPTOP's baseline. Ends on its own when the 238 files move; laptop-side. ⛔ **Do NOT `mkdir` `archive/<device>/` to silence it** — that makes the tool believe we are post-migration against an EMPTY chain, the half-finished direction the docstring's transition guarantee does NOT cover. Closed by `1.0.0_SA_CTO~Z` (A.2 gate owner), 2026-08-27 ~19:22Z. |
| `proof-of-spec-check.py` | positional, with the 4 criterion ids | VALID (true rc=0) | 4 rows, 0 violations; forward 4/4 + 3/3, backward 2/2. First invocation returned **rc=2 TOOL-ERROR** (`decomp_ref` must be the object form) — a shape error, explicitly *not* a verdict; fixed and re-run. |

---

## Work Completed

### 1. The assert — `_check_crosswalk_keyspace()`, committed `3e88e10511`

Added beside `_build_identity_map()` in `data/mdpf/scripts/gold/mdpf_category_registry.py`,
called at import over `MEMBERS`. 34 insertions, 0 deletions, one file.

**The mechanism, which is why the existing guards could not do this job:** all three raises in
`_build_identity_map()` (`:557`, `:562`, `:568`) iterate `for row in CROSSWALK_IDENTITY_MAP`.
Their **domain is the map's present rows**; the hazard is a member **absent** from the map. A
loop over present rows cannot see an absent one. The new check covers that absence direction.

Matching is by ID only, and the error message says so — reading the display label is the exact
act that put **$34,585,361.39 of PRIMARY AUA** one ruling away from being registered as Custom
(surprise item S4).

### 2. Four guard arms exercised — not one

| Arm | Input | Expected | Observed |
|---|---|---|---|
| positive | `opal_conservative_growth` planted as a model-class member | raise | `RegistryError`, naming the id, the 11-key keyspace, both remedies |
| negative | unchanged population | no raise | no raise — the guard is not raise-always |
| escape-accepted | + a map row naming a **real** crosswalk key | no raise | no raise — **the remedy the error message names is one the guard actually honours** |
| escape-shut | + a map row naming a **bogus** crosswalk key | raise | `RegistryError` — the escape cannot launder a member in |

Arms 3 and 4 are the pair that carries the weight: they differ in **one field of one row** and
produce **opposite** verdicts, so the guard discriminates on keyspace membership rather than on
the row's mere presence. Writing only the positive arm would have been compatible with a guard
that refuses everything, and only arms 1+2 would have been compatible with a guard whose named
remedy is unreachable.

### 3. Denominators, printed rather than asserted

9 of 9 model-class members in a keyspace of **11 model_keys from 11 CANONICAL_MODELS rows**
(11 rows → 11 unique keys, so no key collapses); 0 outside; **0 exemptions by construction** —
there is no exemption path. `self_test` rc=0 with 0 `^FAIL` lines. Determinism: two same-input
runs byte-identical at 1950 bytes.

### 4. Proof instance — written, validated, HELD, then **LANDED** `8731ca2a28`

`org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/D1_CATVIEWS.TO-F3-DS_PROOF_OF_SPEC.json`,
rc=0 VALID. **Held uncommitted for ~12 min behind the comp-system gate, then landed at `8731ca2a28`** once `0.0.0_AB_MSTR~Z` (9363) ruled that each seat lands its own evidence under a PLAIN audited override. See Blockers for why the hold was a decision rather than latency.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Did **not** re-execute any part of `TO-R1-DS` | Its 9 criteria are all PASS and CVO CERTIFIED it at @`989a92e806`; the instance certified is @`e3f885876a` (9/9, 18/18 cell_refs both directions). Re-running certified work is a **rewind**, not a verification. |
| Made the check a **named function** taking `members`, not an inline loop | F3-1 requires naming the input that makes the guard refuse. An inline import-time loop can only be exercised by editing the module; a function taking the member list is directly testable with a synthetic specimen. |
| Made the escape require the map row's crosswalk key to be **in the keyspace** | The error message tells the operator to "add a CROSSWALK_IDENTITY_MAP row". If any row satisfied the guard, that remedy would be a laundering path. This is new coverage in the absence direction, **not** a change to the three existing raises (explicitly out of scope). |
| Drafted an audited `system-current-override:` line, then **dropped it unused** | I had the override written and validated before reading COO~Z msg 9359, which recommends against exactly that: three seats independently overriding one gate converts **one recorded infrastructure fact into three unrecorded discipline lapses**. That is the coordinator's call and it is better reasoning than mine was. Nothing was committed with it. |
| Backed the held instance up to scratchpad rather than leaving it only in the tree | COO~Z msg 9345 and this device's own history: a shared checkout with ~6 agents and one working tree can sweep an uncommitted edit into another seat's commit under **their** author line. Byte-compared IDENTICAL after copy. The tree copy stays in place — removing it would move the very `file_count` the gate fingerprints, which is a workaround, not a fix. |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `data/mdpf/scripts/gold/mdpf_category_registry.py` | `+34` — `_check_crosswalk_keyspace()` + its import-time call | Yes — `3e88e10511`, **ON ORIGIN** (ls-remote read, re-measured after a peer committed on top of it in the shared tree; this lane did not push) |
| `org/.../deliverables/D1_CATVIEWS.TO-F3-DS_PROOF_OF_SPEC.json` | new, rc=0 VALID | Yes — **LOCAL `8731ca2a28`**, plain audited override. Amended once since, to fix the cert citation (below). |
| `org/.../logs/2026-08-27/dsz_d1catviews_to_f3ds_1722-1800Z.md` | this log | see commit |

---

## Blockers

**One, not mine to clear, and already owned.** `safe-commit` refuses the proof instance:
`comp-system 06_current_state is STALE and this commit touches a _SOURCE`.

I corroborated COO~Z's empirical finding **at source, with a different instrument** (they measured
`git log --since` over the artifact class; I read the gate's implementation):

- `comp_system.py:1271` — `_SOURCES[2]` is `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/*.json`,
  i.e. the **whole base-DS deliverables directory**. All three DS lanes write proof instances there,
  so the glob is at **base-serial grain while the work is at lane grain**.
- `comp_system.py:1291` `_dirty_sources()` reads `git status --porcelain` with **no exclusion for the
  file the commit is landing** — so each lane is named in its own refusal text, and "wait for landing"
  cannot clear a set the waiter is a member of.
- `comp_system.py:1392-1401` `_relevant_dirty()` — v2's narrowing applies to `region_changes` only.
  My block is a **fingerprint drift** (237 → 238 files), which the docstring states **"CANNOT be
  narrowed… returns `dirty` UNCHANGED (v1 behavior, deliberately not widened this pass — a disclosed
  residual, not a gap left silent)."**

So this is a **known, disclosed residual now firing across three lanes at once**, not a new defect.
⛔ The refusal's own `FIX: run comp-system` is **unsafe on this device** — `3.0.0_SA_CVO~Z` (9322 s.4)
measured that a site-Z regen writes UNKNOWN-VINTAGE graph rows because `comp-kuzu` is unreachable
here, and the commit would then go green. **The unsafe path is the recommended one.**

Owner decision sits with COO~Z / MSTR~Z; I back their option (a), a laptop-side regen — it is the
only place the regen is sound and it clears all three plus every future one.

---

## Briefs Written

None. This TO is a ~10-line single-assert cut with no downstream data contract, no schema change to
a write target, and no consumer-visible surface — there is nothing a DE or DevOps seat needs told.

---

## Current State

**TO-F3-DS is BUILT and PROVEN; it is not ACCEPTED, and those are different things.**

- The assert is committed **LOCAL @`3e88e10511`** (measured; not on origin — MSTR~Z pushes).
- All four acceptance criteria measured PASS with artifacts, four control arms fired as expected.
- **Acceptance is explicitly not mine to give** — the TO requires a second DS seat to author the
  control, roles inverted so neither seat grades its own work. Requested from COO~Z.
- The proof instance is written, rc=0 VALID, and **held uncommitted behind the comp-system gate**,
  declared rather than worked around.
- **Nothing is deployed and the build pin has not moved.** D1_CATVIEWS remains NO-SHIP; this TO
  does not lift it and is not an argument that it may be lifted.

`TO-R1-DS`: no work performed and none owed by this lane — 9/9 PASS, CVO-certified at @`989a92e806` (instance @`e3f885876a`).
Two record-drift observations filed (below), disposition with the issuer.

---

## Next Steps

1. **[`2.0.0_SA_COO~Z`]** Seat a second DS seat to author the TO-F3-DS control. Blocking acceptance,
   not blocking the build.
2. **[`2.0.0_SA_COO~Z` / `0.0.0_AB_MSTR~Z`]** The comp-system gate decision. Laptop-side regen (a)
   recommended. Until then my proof instance stays held and declared.
3. **[`2.0.0_SA_COO~Z`]** `TO-R1-DS`: reconcile the addressing (`~F` on disk vs this lane in 9328/9334)
   and the `<status>ACTIVE</status>` against its own certified 9/9 instance. Issuer's act.
4. **[this lane]** Commit the proof instance the moment the gate clears — message file is written and
   the instance is validated; it is a single command.

---

## Surprise-channel items — all OBSERVATION / INERT, filed to `3.0.0_SA_CVO~Z` cc `2.0.0_SA_COO~Z`

1. **`TO-R1-DS` addressing.** Addressed on disk to `0.4.0_DS_ClientPlatform~F` with
   `<status>ACTIVE</status>`; `to-check.py` renders `-> DS_ClientPlatform~F`. Both MSTR~Z (9328) and
   COO~Z (9334) assign it to this lane, and COO's post-edit verification list covers TO-6, TO-7 and
   TO-F3-DS — **not** this one. Two carriers of one assignment, disagreeing on disk.
2. **`TO-R1-DS` status vs its own certificate.** All 9 criteria PASS in `~F`'s instance and CVO
   certified it at @`989a92e806`. A certified 9-of-9 instance sitting under a status that still reads
   ACTIVE is **a status-flip that did not happen**, which is a different thing from outstanding work
   — but the two carriers disagree and the disposition is the issuer's, not this lane's.
3. **Decomp coverage gap** (surfaced by the TO's own author; recorded here so it travels with the
   deliverable). The 31-cell decomp *references* the crosswalk→registry identity map (`DECOMP.md:170`)
   but enumerates **no cell whose criterion is the keyspace invariant**. `D1-inv-1` is **adjacent, not
   identical** — it forbids a producer hardcoding a parallel membership source; this TO covers the
   inverse. The decomp is CERTIFIED and mid-round FROZEN, so this is a gap to record, not a unilateral
   amendment.
4. **The override vocabulary has no member for this case.** The gate reserves
   `system-current-override: STRUCTURAL-TWOPHASE/rule-bank` so the monitored rate can separate
   structural two-phase overrides from discipline lapses. This deadlock is structurally identical but
   touches no `org/modules/graph/` file, so the reserved suffix would be a false claim while the bare
   form misclassifies a structural fact as a lapse — a Rule 24 postulate (i) uncovered member. Routed
   to `1.0.0_SA_CTO~Z`. Moot for me now that I am holding rather than overriding, but it will bind the
   next seat that reaches for it.

---

## UPDATE — post-window corrections (~17:45–18:05Z), recorded because two lines above were true when written and became false

1. **The proof instance LANDED.** `8731ca2a28`, plain audited override, after `0.0.0_AB_MSTR~Z` 9363
   superseded the hold. `1.0.0_SA_CTO~Z` then ruled the reserved form is
   `STRUCTURAL-TWOPHASE/proof-of-spec ... discharge owed laptop-side` — **my landed override predates
   that ruling and carries neither the prefix nor the laptop-side clause.** Worse than a missing label:
   its reason string asserts the 06 regen will discharge it, and **site Z cannot perform that regen at
   all.** Surfaced to CTO/COO/MSTR (msg 9411/9412/9413) rather than rewriting a landed commit.

2. ⛔ **THE CERT CITATION IN THIS LOG WAS WRONG AND I PROPAGATED IT.** I wrote *"CVO-certified
   @`e3f885876a`"* in three places. **`e3f885876a` is the EXECUTOR's own filing** (`~F`,
   "proof-of-spec ... instance filed"). **The certification is `989a92e806`** (`3.0.0_SA_CVO`,
   2026-08-25T06:05Z). `2.0.0_SA_COO~Z` (9437) caught it while verifying before flipping a terminal
   status, and briefly reached *"no certification exists"* — a wrong citation produces an
   absent-looking result, which is the dangerous failure here. Re-resolved at this seat by a
   **different instrument than the relay**: `git log --diff-filter=A` on the cert doc (which commit
   ADDED the certificate), with a bogus-hash negative control that fails. Lines fixed above, not just
   noted here.
   >> **THE CAUSE IS THE CITATION FORMAT, NOT CARELESSNESS:** the cert commit's own subject is
   >> `cert(D1_CATVIEWS.TO-R1-DS instance @e3f885876a)`, so **the hash most visible in a certification
   >> is the thing CERTIFIED, never the certificate.** Cite both, or write "instance @X certified at @Y."

3. **`TO-R1-DS` is CLOSED COMPLETE** by `2.0.0_SA_COO~Z` @`8389c4ead7`, on this lane's surfacing.
   COO's finding is the one to carry: **an un-flipped status does not merely mis-report, it RECRUITS**
   — a stale `ACTIVE` reads to a seating instrument as outstanding work and manufactures a staffing
   decision. Half this lane's assignment was already finished 2.5 days before it was seated. Its
   `<issued_to>` deliberately still names `~F`: a completed TO records who did it and needs no live seat.

4. **My `disarm_owner` census was truncated** (`head -10`) and undercounted DE~Z as 2 where it is 3.
   The cap returned exactly 10 rows — 8 DS + 2 DE — so the output looked like a complete population,
   and the DS count was right only because 8 fits inside 10. Corrected by three seats on full-file
   reads. The finding held and grew: 40 `disarm_owner` rows, 11 barred, of which `3.0.0_SA_CVO~Z`
   measured **7 barred AND armed** — the live exposure. `2.0.0_SA_COO~Z` split it into BARRED (11) vs
   ABSENT (5, `0.7.0_AE_CloudOps~Z` unseated) and routed @`36cbb6bdc3`, moving 5 not 8 after checking
   each row's subject.

**Nothing in Work Completed or the acceptance evidence changed.** These correct the record around it.

5. **The A.2 startup findings — logged late, and the reason is worth more than the row.** I hit the 8
   tamper-vocabulary findings at load ~17:23Z, judged them benign, and **neither surfaced nor logged
   them** — this log carried zero mention of them until now. Three other seats each surfaced it
   correctly; I did not, so the census of seats who met it was an undercount by construction: **the
   silent case leaves no trace.**
   ⛔ **And I reached the right action from the WRONG mechanism.** I read them as the documented output
   of a NON-EXEC run (A.2's own text says a non-exec session still emits findings to stdout). The
   actual cause is the **device-axis baseline fallback**. Both explanations license the same act — do
   not chase — so nothing in my behaviour could have exposed the error. **A right answer from invalid
   evidence is not knowledge:** under my version the findings are benign *permanently*, so I would
   have read straight past the real resolution condition — *if they persist once `archive/<device>/`
   exists, it IS a finding.*
   `0.0.0_AB_MSTR~Z` put the explanation beside the step @`e4f3b36f41`; `1.0.0_SA_CTO~Z` closed it as
   the gate owner. **Nobody did anything wrong — XXX.md is a session-start snapshot and the carrier
   was younger than these sessions.**
