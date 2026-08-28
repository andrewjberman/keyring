# ISCK Round 2 closure, Codex log skill, and reboot handoff - 4.0.0_SA_CRO~X

**archetype:** MIXED
**Date:** 2026-08-28
**Task Order:** ISCK.ROUND2 / D11.CRO-A-COVERAGE / CODEX.LOG-SKILL
**Status:** IN PROGRESS

---

## Objective

Continue the exact `4.0.0_SA_CRO~X` seat after the prior ISCK review log: attack the actual ISCK
contract and Round 2 landings, cover responsibilities transferred from CRO~A, make the Claude-style
`/log` workflow available as a repository-owned Codex skill, and leave a zero-context recovery
record before Andrew's device reboot.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| ISCK atomic gate runner | `bash org/standards/isck/run_gates.sh 9760630ae7` | PASS | Six of six gates exited 0 at the boundary package tip; 11 open candidates remained: ARM1 9, ARM3 0, ARM4 2 of 20 undisposed. |
| ISCK atomic gate runner | `bash org/standards/isck/run_gates.sh bb7444a08e` | PASS | Six of six gates exited 0 after the consumption-time entry guard; committed sidecar read 18 adjudicated, 2 deferred, 0 NEW; self-controls passed. |
| Independent ARM4 harness | exact `bb7444a08e` blobs executed in memory | PASS | Duplicate-key, renamed-class-D, widened-payload, and exact-match positive-control behavior were asserted independently without mutating the working tree. |
| Git object/DAG checks | `rev-parse`, `rev-list`, `merge-base --is-ancestor`, blob SHA-256 | PASS | Exposed three boundary identity errors and confirmed their amended values. |
| Codex seat tests | `org.mcp.tests.test_codex_seat_load` plus installer projection checks | PASS | Canonical `load` and `log` skills projected byte-exactly and launcher integration checks passed before commit `c736acd81b`. |
| comp-find all-corpus census | `python .tools/comp-find -i verification_standing --corpus all --files --all` | FAIL | Started at worktree `27f3d192c6` but returned no denominator before the reboot stand-down; no all-corpus claim may be made from it. |

**What worked:** Atomic Git extraction prevented the dirty shared worktree from affecting ISCK gate
results. Object identity and ancestry checks caught errors that prose review and several partial
re-verifications missed. The in-memory ARM4 harness exercised the real loader and disposition path
without rewriting the sidecar.

**What failed:** `comp-find` was absent from `PATH` and absent from the callable-tool catalog even
though its repository implementation exists at `.tools/comp-find`. Direct Python invocation of its
new `--corpus all` mode did not return a denominator within the available 30-second window.

**Gap found:** The delivered superseded-consumer census is package-bounded and lacks an exact
invocation hash. The out-of-package population remains unmeasured at shutdown. The Codex launcher
also does not currently expose the repository's `comp-find` command on `PATH`.

---

## Work Completed

### 1. ISCK Round 2 attacked through its actual contract and gates

- Read the ISCK contract, schema, validator, proposal/design artifacts, ARM records, and Round 2
  boundary rather than treating the boundary prose as the contract.
- Independently verified the boundary package at `9760630ae7`: schema blob
  `b2e3c3683e15`, stored-byte SHA-256
  `586bf52cf3171cdf361d6ed3fdb37e0c0cfa7f0b91d23bb3b4f1d48146360859`, contract blob
  `d1506ca0944e`, validator blob `418ad2b96d7c`, R2-2 design blob `41cacec709b8`, and six green
  atomic gates.
- Confirmed the substantive Round 2 state: exit condition 1 MET; condition 2 ultimately MET and
  EXERCISED after a post-fetch rerun at an on-origin hash; condition 3 NOT RUN and NOT BUILT. The
  contract remains `v0.2-candidate`, attacked but not frozen or cleared for operational use.
- Verified the main schema repairs and carried work: R2-1 and R2-8 accepted; DT-R2-6 removed the
  uninhabitable contradicted/adjudicator coupling; ARM3 reached 95/95 inhabitable values; ARM4 left
  two class-D reversals and ARM1 left nine candidates; R2-2 append-only/derived-status design is
  attacked-dry but its WP-3 landing remains carried.

### 2. Found and closed the ARM4 consumption-integrity defect

- At exact `6245dc0a3d`, attacked three vectors. Duplicate JSON keys failed open correctly and a
  renamed class-D key remained NEW/non-suppressed. A widened
  `values_at_adjudication` payload under an exact live key was nevertheless accepted and
  suppressed: key identity was checked while the second representation of the value set was not.
- Routed the measured failure to `0.4.0_DT_ClientPlatform~X` and `1.0.0_SA_CTO~X`. CTO pre-granted
  the seventh audited override for `isck_coverage_probes.py` only.
- DT landed the entry guard at `bb7444a08e`. It validates four-part key shape, permitted class,
  sorted duplicate-free payloads, and exact equality between key values and payload values; any
  mismatch emits WARN and suppresses nothing.
- Independently accepted `bb7444a08e`: duplicate key -> WARN/NEW/zero suppressed; renamed class-D
  -> NEW/non-suppressed; widened payload -> `DISAGREES` plus WARN/NEW/zero suppressed; exact
  key/payload -> exactly one adjudicated. Six atomic gates remained green.

### 3. Re-verified and repaired the Round 2 boundary record

- Cut record: `ece1ac0f41`; package tip: `9760630ae7`; on-origin integration head observed:
  `3fbb493cdafd584209a10c6353794667e5507b98`.
- Found four record-level defects:
  1. The ISCK-path span was 37 commits, not 35; 35 was the count only through `9fb81b743a`.
  2. `6245dc0a3d` is an ancestor of `9760630ae7`, so it is post-dry/outside-dry but inside the
     pinned boundary output. `bb7444a08e` is the true first post-boundary amendment.
  3. ARM4 prose blob `f85d4b24a6e6` belongs to `05086d045c`; `5892013077d3` is the amended blob at
     `9760630ae7`. The first record conflated those vintages.
  4. The roughly 40 tally mixed findings, inputs, accepts, censuses, fixes, and owed work, so
     `0 refuted` had no auditable denominator and could not be quoted as a rate.
- CTO upheld all four and amended the boundary at `8bce3fa495`; the record now says roughly 40
  listed contributions and makes a deduplicated finding register owed before a refutation rate is
  stated. `7c776ccc5d` amended condition 2 to MET after the on-origin read. `f6269a9a82` recorded the
  post-fetch gate execution and the completed CRO acceptance of `bb7444a08e`.
- CVO corrected its own whole-record re-verification claim to a nine-cell measured denominator and
  independently confirmed the four missed cells. The reusable boundary rule is now: every
  re-verifier states measured cells over asserted cells or disclaims the remainder.

### 4. CRO~A coverage and D11 L0 governance

- Accepted the COO/CRO Base transfer to cover responsibilities assigned to `4.0.0_SA_CRO~A`.
- Landed `1a5624ae2a`: named the CRO family as the D11 L0 v1 emission authorizer and added the
  consumer gate in the layer contract, schema, and validator under
  `org/tier1_exec/4.0.0_SA_CRO~A/deliverables/SUBSTRATE_COHERENCE_V3_PROPOSAL/`.
- The commit changed 107 lines across the contract JSON, its schema, and
  `validate_layer_contracts.py`; it is authored by exact seat `4.0.0_SA_CRO~X`.

### 5. Canonical Codex `/log` skill

- Created `org/mcp/codex-skills/log/` as the repository authority, mirroring the Claude session-log
  workflow while preserving exact Codex seat identity and launcher-owned runtime boundaries.
- Generalized `org/mcp/install-codex-load-skill.py` to install both canonical `load` and `log`
  projections byte-exactly, without changing the compatibility filename or the public single-skill
  installer default.
- Updated `org/mcp/start-codex-seat.ps1` and `.tools/ajb2.ps1` so both skills are installed before
  the app-server starts, and expanded `org/mcp/tests/test_codex_seat_load.py` for idempotent,
  byte-exact dual projection.
- Installed the projection at `C:/Users/AndrewBerman/.codex/skills/log`, validated it, and committed
  the six repository paths as `c736acd81b7e800de3205eaabdb7b01013f10b12` under the exact seat
  author. No unrelated staged or dirty paths were absorbed.

### 6. Superseded-consumer census intake

- COO delivered a package census with a 17-file denominator and eight consumers: six tied to the
  reducing `verification_standing` domain and two `materializer.current_status` consumers that must
  survive untouched.
- The silent-narrowing trap is `identity_relation.allOf[4]`: removing `superseded` shrinks an enum
  membership arm without deleting the arm, so the schema can still parse and the existing gates can
  remain green while coverage narrows.
- The delivery did not name the exact commit/tree used. A pin request was sent to
  `2.0.0_SA_COO~X`. The all-corpus follow-up was started but did not produce evidence before Andrew's
  reboot order.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Do not equate a green schema/gate suite with operational readiness. | The charter's vertical-slice battery is a separate end-to-end build and remains unbuilt. |
| Keep post-dry consumer findings outside the attacked-dry certification while pinning them as amendments. | Scope integrity requires distinguishing what was attacked from what merely exists in the pinned DAG. |
| Require key/payload equality at sidecar consumption. | The ruled value set was encoded twice; validating only the key allowed the human-auditable payload to lie. |
| Do not quote `0 refuted` as a rate before the finding register lands. | A mixed contribution table is not a deduplicated finding denominator. |
| Require re-verification denominators. | A partial read presented as whole silently inherits authority for skipped cells. |
| Preserve repository ownership of Codex skills and install projections byte-exactly. | Seat startup is repository-closed; personal skill copies must not become an independent authority. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier1_exec/4.0.0_SA_CRO~A/deliverables/SUBSTRATE_COHERENCE_V3_PROPOSAL/layer_contracts_and_checkpoints.v1.json` | Named CRO-family v1 emission authorization and consumer gate. | Yes - `1a5624ae2a` |
| `org/tier1_exec/4.0.0_SA_CRO~A/deliverables/SUBSTRATE_COHERENCE_V3_PROPOSAL/schemas/layer_contracts_and_checkpoints.v1.schema.json` | Enforced the governance fields. | Yes - `1a5624ae2a` |
| `org/tier1_exec/4.0.0_SA_CRO~A/deliverables/SUBSTRATE_COHERENCE_V3_PROPOSAL/validate_layer_contracts.py` | Added consumer-gate validation. | Yes - `1a5624ae2a` |
| `org/mcp/codex-skills/log/SKILL.md` and `agents/openai.yaml` | Added canonical Codex log skill and interface metadata. | Yes - `c736acd81b` |
| `org/mcp/install-codex-load-skill.py` | Generalized installation to canonical `load` and `log` projections. | Yes - `c736acd81b` |
| `org/mcp/start-codex-seat.ps1`, `.tools/ajb2.ps1` | Advertised and installed both canonical skills before startup. | Yes - `c736acd81b` |
| `org/mcp/tests/test_codex_seat_load.py` | Added byte-exact, idempotent dual-install tests. | Yes - `c736acd81b` |

---

## Blockers

- AMBIGUOUS: `2.0.0_SA_COO~X` delivered the R2-2 superseded-consumer census in message 77158 but
  did not name its invocation commit/tree. The package result is detailed, but it is not yet
  reproducible landing evidence. The all-corpus population also remains unmeasured.
- Andrew-direct reboot stand-down is an operator pause, not a project blocker and not a D11 scope
  stand-down.

---

## Current State

The ISCK Round 2 attack is closed at CTO~X. Boundary amendment 3 is `f6269a9a82`; its package pin
`9760630ae7` is on `origin/CLOUD` at observed head `3fbb493cdafd584209a10c6353794667e5507b98`,
with exit conditions 1 and 2 MET and condition 3 NOT RUN/NOT BUILT. Local amendments
`7c776ccc5d`, `8bce3fa495`, and `f6269a9a82`, plus DT's accepted entry guard `bb7444a08e`, must ride
an integration window if they are not already ancestors after reboot. CTO~X owns the deduplicated
finding register, ARM1's nine candidate dispositions, and the R2-2 landing with checklist
`bfcebc58c5`; COO~X's census needs an exact pin before it is cited as gate evidence. This seat's
finished source commits are D11 governance `1a5624ae2a` and canonical Codex log skill
`c736acd81b`; the shared worktree contains extensive unrelated changes that were deliberately
preserved. No operational ISCK use is authorized until the WP-3-backed vertical-slice sequence is
built and passes.

---

## Next Steps

1. **[4.0.0_SA_CRO~X] Resume the all-corpus `verification_standing` census at an explicitly pinned tree** - require the printed corpus denominator and classify every out-of-package hit before making an absence claim.
2. **[2.0.0_SA_COO~X] Supply the exact census invocation hash/tree** - message 77158's 17-file/eight-consumer result is otherwise not reproducible.
3. **[1.0.0_SA_CTO~X] Land the deduplicated finding register, dispose ARM1's nine, and complete the R2-2 checklist-gated landing** - these are the named Round 2 carries.
4. **[0.0.0_AB_MSTR] Integrate and report ancestry for the local Round 2 tail and `c736acd81b`** - preserve the amendment chain rather than squashing its corrections out of the record.
5. **[1.0.0_SA_CTO~X] Keep ISCK at `v0.2-candidate` until the vertical-slice battery exists and passes** - green contract gates are not the operational exit condition.

