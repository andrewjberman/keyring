# GATE-2 DETERMINATION #5 -- PRE-READ RE-ANCHOR at `327db12ea`

**agent:** `3.0.0_SA_CVO~B` (Andrew-direct dedicated AoR validation lane, LD-0277) · **date:** 2026-07-15 ~23:0xZ
**scope:** COLD PRE-READ ONLY (CTO 223623Z via MSTR 223756Z). **NO hold motion of any kind rides this spawn.**
**supersedes:** nothing -- this RE-ANCHORS determination #4 (`8e4789fb7`, CLEARED at `59d70b95e`, later
RE-SCOPED: structural arms hold, fold-ON claims not live-verified on the then-empty basis).

> # >> NOTHING IN THIS FILE AUTHORIZES ANYTHING. V4 = WITHHELD -- NOT RUN -- AN EXPLICIT GAP. <<
> V4 verifies the FIRST NIGHTLY *AFTER* the switch flips, on the SERVED artifact, never a fixture.
> That is a definition, not a schedule. No fixture green in anything below closes it.

---

## 0. State of the world at determination time (read LIVE, 23:03Z)

- **`INF_AOR_FOLD_ACTIVE=1` is LIVE on `inf-gold-trigger`** -- the flip is ARMED (post-Andrew-GO, his
  "GO NOW" 22:42Z, recorded verbatim by DS~B and broadcast). This moves my det-#4 line "Switch OFF."
- **The chokepoint still HOLDS** (`INF_GOLD_DISPATCH_HOLD` present, `INF_GOLD_DISPATCH_RELEASE` absent).
  Nothing has dispatched. Nothing new is served (spine still the 07-10 artifact, phantom still on it).
- The release window is EXECUTING tonight. My pre-read is therefore on the critical path, and the
  "wide window" CTO offered at 223623Z closed six minutes after he wrote it. Reported, not complained.

## 1. MY INSTRUMENTS ARE INTACT -- verified at git, not assumed

- `aor_gate2_runner.py` + `aor_gate2_fix_bar.py`: **untouched since the det-#4 commit** (`git diff --stat
  8e4789fb7 HEAD` over my deliverables shows only my own later-07-13 additions).
- The bar's ONLY change since its pre-registration (`294965d79`) is **my own** det-#4 §5 property-rewrite
  (author `3.0.0_SA_CVO~B`, commit `8e4789fb7`). No foreign touch. The staged claim "runner + bar intact"
  is **VERIFIED**, not accepted.
- Housekeeping: `aor_timelock_bar_v2_account_grain.py` (mine, 07-13) had sat **untracked** -- an instrument
  not pinned at any hash is a record defect by my own rules. Committed with this file.

## 2. THE STAGED ROUND-8.2 SET -- what a cold read VERIFIES vs what it can only ATTEST

| staged claim | my verification | status |
|---|---|---|
| runner at repo parity, imports on deployed bytes | **INDEPENDENTLY RE-VERIFIED**: my own fresh `comp-pipescript deployed` sweep 23:0xZ -- `INF_A_0.aor_resolver` + `INF_D_11` MATCH (were MISSING pre-bundle), all 8 previously-STALE bundle scripts MATCH incl. `INF_C_01`/`INF_C_07`/`INF_D_00f`; `INF_D_00d` re-checked by download after a tool TIMEOUT -- md5 tie `94c149e3` | **VERIFIED on the censused set** -- but see §3 for the census boundary |
| pin guard both directions | **VERIFIED AT SOURCE**: `aor_resolution.py:184-187` UNSET -> REFUSE ("refuse to skip the content check rather than fabricate one"); `:219` mismatch -> REFUSE; dispatch RE-PINS after the accounts_v2 pull (`orion-gold-dispatch.sh:1490-1494`), closing the pre-pull-pin-names-the-superseded-partition trap | **VERIFIED (mechanism)**; the 0/9,510 fold-OFF baseline number is DS-attested (G3 close log) |
| suites 155/155 incl. my conformance arms both switch states | **census VERIFIED**: 5 suites = exactly 155 test functions (resolution 64 + timelock 38 + fold_derivation 22 + conformance 21 + c01_wiring 10); the conformance 6-way table **forces** the switch state per-control, never ambient (`test_advisor_of_record_conformance.py:164-182`) -- both states by construction; my gate-2 arms are embedded (R8-F1 serving-path firebreaks `test_aor_resolution.py:177`, T2 `test_advisor_timelock.py:218`, the [STOP]-confirmed classes `:316,:371`) | **census VERIFIED; the RUN is DS-attested** (155 passed, 1.58s, step-1 log). My own re-run rides my battery fire at the in-order moment |
| reproduce_aor_fold_gate PASS, native cross-check, 164 exact, neg controls | **mechanism READ-VERIFIED at HEAD**: real assertion teeth -- raises on any native-vs-reproduced mismatch (two derivations of one fact), F6 asserts per-account on the SERVED after-state not the net-set, and a swap-control that cannot be constructed is **NOT a pass** (`swap_caught=None` != ok) | **mechanism VERIFIED; result DS-attested** (`6db926cd1`: 164 exact, 0 mismatch, targets 135.24/29.19/24.13/12.42M, firm conserved) |

**Discriminated honestly:** `test_r82_f2b_c_HELD_the_phantom...` (`test_aor_resolution.py:1832`) **returns a
str -- a test that structurally cannot fail**, counted inside the 155. DS disclosed it themselves (step-1
log "smell noted"). It is a held-decision RECORD deliberately parked in the suite, so: **154 assertions + 1
scribe-record.** Not a defect in the staging's honesty; a defect in the count's granularity. The fix rides
battery staging per DS; I will not count it as an assertion in anything I sign.

## 3. >> THE ONE NEW FINDING: THE CENSUS BOUNDARY. Three serve-path consumers are deployed PRE-round-8. <<

**Routed URGENT to CTO 232031Z (gate owner), CC MSTR+COO. Explicitly NOT a hold motion.**

Evidence chain, all my own instruments:
1. Fresh sweep: `INF_D_02c.client_directory` / `INF_D_04.client_portal_summary` /
   `INF_09.generate_partner_analytics` = **STALE** (everything else in inf-gold MATCH).
2. **md5 vintage-tie:** deployed `INF_D_04` == repo @ `5581c0de1^` **EXACTLY** (`88e6fb3e...`); deployed
   `INF_09` == `5581c0de1^` **EXACTLY** (`80734cdd...`); deployed `INF_D_02c` (`ca5337ab...`) matches no
   vintage I tested -- older still. `5581c0de1` is round-8 c2: **"consumer migration -- fold census 10->1,
   household 4->1, all views inherit the canonical resolution."** The deployed bytes of these three predate
   the moment consumers stopped deriving attribution themselves.
3. All three **still carry the DEPLOY-SERVE-HELD sentinel in repo**, are **absent from the G3 bundle
   manifest** (silent -- not an excluded-by-design record), and are **dispatch-invoked with `--upload`**
   (`orion-gold-dispatch.sh:268,270,271`).
4. `INF_C_07` itself -- the round-8.2 un-fold override (`dbd10d7aa`) -- **IS deployed-fixed (MATCH).** The
   finding is one layer out: pre-migration consumers with their own inline fold-era household derivations.

**Materiality (mechanism-argued, NOT exercised -- labeled per Rule 22):** a CHAIN-WIDE run under
`INF_AOR_FOLD_ACTIVE=1` executes these three at pre-canonical bytes while the rest of the chain serves
canonical resolution -- the **"partial, silent, inconsistent fold"** class named in `dbd10d7aa`, surfacing
on client_portal_summary / client_directory / partner_analytics. **IF tonight's supervised run is scoped to
the NNA spine, this is sequenced-not-blocking.** Run scope is the gate owner's call, not mine. I request
nothing of the chain.

**The class, named for the record:** "runner at FULL repo parity" was TRUE on its census (the AoR catalog =
the bundle set), and the census boundary excluded three dispatch-invoked serve-path files. Same shape as
DS~B's own CATCH-2 tonight (*"a deploy manifest censuses the IMPORT CLOSURE, not the file list"*) -- one
ring further: **a release-parity census must cover the DISPATCH-INVOKED closure, not the sentinel list.**
Verification law #6/#10: state the denominator; my sweep's denominator was the dispatch table, and that is
why it saw what the sentinel-set census could not.

## 4. RE-ANCHOR VERDICT

- **Det-#4's structural clearance CARRIES at `327db12ea`.** The full delta since my anchor (28 commits,
  +4,412/-77 on `data/inf/`) is enumerated and read: every commit either strengthens a class I named
  (stamp-aware fold `5c33ca56f`, single-source derivation `53098d018`, fold-then-lock refusal `48904598a` --
  my own [STOP], confirmed at source -- collapse detector `ff0653ff3`, C_07 override deletion `dbd10d7aa`,
  scratch-prefix dry-run capability `f99d67524`) or executes a ruling (`fd7764ce3`, `877cdfc82`). **Nothing
  in the delta weakens any property my battery asserts.**
- **The re-scope's outstanding condition** (fold-ON claims fed on a REAL basis) **is MET-BY-EVIDENCE-I-READ**
  (native `advisor_of_record_raw` 837/874 on the 07-15 scheduled row, fold_map=164 byte-stable across two
  consecutive scheduled rows, reproduce-gate PASS on live silver) **and NOT YET MET-BY-MY-OWN-RUN.** A cold
  pre-read attests; it does not render. **My battery re-fire at `327db12ea` is the confirming act of this
  re-anchor** -- commissioned by the gate owner at its in-order moment (it is chain-neutral: fixtures + live
  READS, no writes, no dispatch) -- and it grades against §5 below, pre-registered NOW so the result cannot
  be goalpost-moved by me later.
- **V4 = WITHHELD -- NOT RUN -- EXPLICIT GAP.** Unchanged. It fires on the first nightly AFTER the flip, on
  the SERVED artifact, against §6. Never before. "Lift the hold so CVO can run V4" remains the control-defeat
  vector and remains REFUSED in advance.

## 5. PRE-REGISTERED battery expectations at `327db12ea` (written BEFORE the battery re-fires)

| arm | expected | why |
|---|---|---|
| `aor_gate2_final_matrix` / `aor_f4_and_inherit_census` / `aor_f2_pin_does_not_bind_a00` / `aor_r2_null_stamp` / `aor_gate2_fix_bar` (5/5) / `aor_off_is_a_noop_guard` | **GREEN** | structural properties; the delta only strengthened their mechanisms; the fold-OFF 0/9,510 baseline corroborates the no-op guard |
| `aor_round8_battery` (35 arms) | GREEN **or declared refusals** | round-8.2 moved premises under some arms (the reproduce-gate precedent: the harness premise, not the property, goes stale); a refusal-to-render is honest, a confident stale verdict is not -- triage per arm |
| `aor_served_view_under_on` | **GREEN** | the property `dbd10d7aa` hardened; its proven-RED control (`69219a7db`) must still catch |
| `aor_phantom_advisor_arm` | **RED until the first post-flip artifact serves, then MUST flip GREEN** | the phantom ($52,604.80) is still on the served 07-10 spine; its disappearance IS V4's headline |
| `aor_phantom_switch_arm` | **EXPECTED TO CHANGE STATE -- and that is the arm WORKING** | its det-#4 green was DATA-DEPENDENT (the 3 phantom accounts were roster-absent on the 07-12 basis; I named switch-dependence REACHABLE in det-#4 §3). On the real basis the release pre-registration asserts the switch moves the phantom bucket to patrick (+$1.03M incl. $52,604.80) -- the fold doing its job under Andrew's backfill ruling, not a regression. A CHANGED verdict here confirms det-#4 §3's warning, and I record that NOW so nobody (including me) reads it as a break |

**[FIRED 23:3xZ, CTO-commissioned 232947Z -- and my phantom_switch prediction was WRONG; the annotation
stands, the prediction does not get rewritten.]** Battery at `327db12ea`: **exit 0 -- 9 GREEN + 1 expected
RED (phantom_advisor), every arm at its det-#4 expectation** (evidence:
`CVO_B_GATE2_BATTERY_FIRE_327db12ea_20260715.txt`; denominator: 10 live arms / 10 declared exclusions --
the four 07-13-PM time-lock-chapter arms declared EXCLUDED with reasons before firing). `phantom_switch_arm`
did **NOT** change state, and it is RIGHT: **my §5 row above mis-attributed the phantom-move mechanism.**
The release delta's "phantom GONE / patrick UP incl. $52,604.80" rides the **SILVER-RESCUE leg (G4)** --
real `rep_id`s at silver, so the accounts never floor to the phantom -- **not the AoR fold**; the arm
correctly measures the fold in isolation (its PC1-PC3 controls all catch). Residual I closed myself: the
arm's "TODAY ... grounded live, 873 rows" line is a **hardcoded 07-13 label** (the arm is hermetic -- its
own §15 class). Re-grounded LIVE on `silver/api_dims/accounts_v2/snapshot_date=2026-07-15` (874 rows, ties
DS's census): **560/703/1225 ALL still roster-ABSENT** (positive control: 42 PRESENT); the +1 account since
07-12 is `4364`, not one of the three. Switch-independence of the phantom HOLDS on the live basis, freshly
grounded. **V4 precision this adds to §6.2: the "phantom GONE" cell binds to the RESCUE leg having executed
in the release run -- if the executed run carried no rescue, a still-present phantom is a rescue-sequencing
fact, not a fold failure; grade it mechanism-discriminated.**

## 6. WHAT V4 NEEDS AT ITS MOMENT (pre-registered, so the served check has a bar it did not write)

1. The SERVED artifact of the **first post-flip nightly** (`platinum/firm/advisor_nna_canonical.json` +
   the per-advisor prefixes), not any preview, not any fixture.
2. Graded against the **banked pre-registered delta**: firm total UNCHANGED **$133,107,667.64**; phantom
   **GONE** (key absent, not zeroed); joe DOWN ~$2.1M; peter UP ~$1.6M; patrick UP ~$1.03M **incl. the
   $52,604.80**; `noel_soderblom` platinum surfaces APPEAR.
3. **Byte-identity between the run I clear and the run that executed**: the (source_digest, fold_mode,
   code_digest) pin stamps on the artifact vs the dispatch's pinned values.
4. Dry-run-before-stamp evidence honored (the `--out-prefix` scratch capability `f99d67524` exists for
   exactly this; the stamp-order law -- FOLD with real data, verify, THEN LOCK -- is absolute).
5. Cross-surface consistency **including the §3 three** as resolved by the gate owner's scope call --
   a spine that folds while client_portal_summary serves pre-fold keys is a V4 FAIL on consistency
   grounds even if the spine numbers tie.
   **[RULED 23:28Z, after this file landed -- CTO 232824Z @ `194d3d674`]:** the three `--upload` legs are
   HELD this window (named stage-B precondition; DS~B to ground the runtime exclusion mechanism at source);
   exclusion oracle = the three surfaces' listings (key+ETag+LastModified) UNCHANGED across the window,
   ledger-recorded. **At V4 I verify that oracle independently** -- the three surfaces UNCHANGED against
   the ledger's record, with an instrument the ledger does not own -- alongside the spine checks above.
   Serve-lift at migrated vintages is a later deliberate bundle; I re-verify those three at their new
   vintages then, outside V4.

---
-- `3.0.0_SA_CVO~B`
