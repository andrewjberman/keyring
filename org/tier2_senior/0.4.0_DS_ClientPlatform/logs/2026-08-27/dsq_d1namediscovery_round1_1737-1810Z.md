# Session log -- `0.4.0_DS_ClientPlatform~Q` -- D1_NAMEDISCOVERY round 1 (TO-1, TO-2, TO-3)

**Serial:** `0.4.0_DS_ClientPlatform~Q` (lane seated 2026-08-27 ~17:37Z by `0.0.0_AB_MSTR~Z`, msg 9351)
**Window:** 2026-08-27 ~17:37Z - ~18:10Z
**Archetype:** BUILD (Rule 27 step 4 -- execute ON SPEC)
**Scope:** D1_NAMEDISCOVERY ONLY (Rule 27, one project per instance). TO-1, TO-2, TO-3.
**Build commit:** `fd15cd5cf3` (LOCAL -- `0.0.0_AB_MSTR~Z` is the integrator and pushes)

---

## 1. What was asked

MSTR-DIRECT msg 9351 (read and ACKed, READ clock): D1_NAMEDISCOVERY ONLY, TO-1/TO-2/TO-3,
cut `@2162f50620` against CVO's certified text. TO-2 carries CVO F2 (the fuzzy matcher and the
registry-absence trap); TO-3 carries CVO F3 (provenance SET, UNKNOWN vs NO-MATCH).

## 2. Startup

`/watcher`: registration was NOT REGISTERED (fresh lane) -> registered PID 35044. No `~Q` watcher
process existed, so nothing to reap -- the orphan rule's kill branch did not apply, and the PID
question was answered before any kill was considered. Monitor armed task `b9atqgprh`, arm banner
`parent-tied: pid 977912` (ARMED, not orphan-capable), watching the CANONICAL nested lane path
`org/mcp/inbox/0.4.0_DS_ClientPlatform/~Q`, not the dead flat form. Confirmed live end-to-end by the
Monitor consuming and emitting the one queued message.

`org/XXX.md`: A.1 session serial file written; A.2 audit-archive-invoker ran (findings noted in
section 6); A.3 PATH `98 of 105` comp-tools resolve bare AND the mandatory EXERCISE line ran a
forwarder (resolution is not execution); D owned-paths hook already wired; E `.comp-graph`
context set; `comp-to D1_NAMEDISCOVERY.TO-1`. **F: zero crons armed.**

## 3. Vintage -- measured, not assumed

The TOs mandate building against DECOMP `@669e04f27b`; the working-tree decomp is `@2162f50620`.
`git diff 669e04f27b 2162f50620` over the decomp touches **only** the section-3 criteria-count
line -- the round-1 amendment TO-3 section 9 required of whoever cut round 1. **Every cell
specification is byte-identical to the mandated vintage.** So TO-3 section 9's contingency ("if the
amendment is missing from the decomp, this TO is the evidence of the omission") **does not fire**:
`1.0.0_SA_CTO~Z` discharged it at the cut.

## 4. What was built

| file | role |
|---|---|
| `data/mdpf/scripts/gold/mdpf_name_discovery_declared.json` | THE DECLARED ARTIFACT -- sole home of the 6 tokens, 5 form classes, cottonwood's 5 surfaces, the output-state axis and the ND-e-2 enforcement policy with its reasons |
| `data/mdpf/scripts/gold/mdpf_name_discovery.py` | matcher + provenance + sweep. Contains NO token, form or surface literal |
| `data/mdpf/scripts/gold/tests/test_mdpf_name_discovery.py` | 15 criterion tests, all PASS |

Placement follows the D1 sibling: `mdpf_category_registry.py` lives in the same directory
(`3e88e10511`), and `data/*/scripts/gold/*.py` is the DS lane by Rule 13.

**Rule 5 pre-authoring check:** `comp-which` returned NO CURATED RULE for the surface question
(its own verdict, which is what licenses a direct search under Rule 21); `comp-find --name
'*name_discovery*'` returned 1 hit over 29039 files -- Andrew's ruling record, not a machine-readable
artifact. **Scope did NOT collapse to verify+rerun; this authored.**

## 5. The defect this build found in itself

`ND-a-3` requires the Opal-side discriminator (`CA Tax-Free Bond` is not an Opal name-form; the Opal
muni *"would literally say Muni"*) to sit where the `Tax`/`Muni` catchers are defined. It did --
inside `tokens[Tax]`/`tokens[Muni]`, cited in the module docstring, **and completely inert.**
`matches_word_boundary` normalised the NAME but not the PHRASE, so once `CA Tax-Free Bond` had
become `CA Tax Free Bond` the compiled pattern still carried the hyphen and could never match.

**My own AC3 test passed over it**, because it asserted the discriminator was PRESENT in the
artifact rather than that it FIRED on an input. A presence check cannot tell a live predicate from
a dead one. Fixed at the predicate (both sides through one normaliser) and the test now names the
input that must make it fire AND the input that must not (`Opal Tax SMA` -> no marker), so the
marker discriminates instead of decorating every row. Re-exercised as planted mutant M4.

## 6. Surprise channel (OBSERVATION / INERT -- surfaced, no action taken)

- **`python .tools/audit-archive-invoker.py` (XXX.md step A.2) integrity findings on this device.**
  ⛔ **CORRECTED ~19:2xZ, AND THE ERROR WAS MINE: this bullet first read "11 findings ... 7
  NON-APPEND-EDIT and 4 ERROR-FAILCLOSED". THE TRUE CENSUS IS 13 -- 8 and 5.** I ran the invoker
  under `tail -12` and counted the visible lines as the census; the output is 19 lines. **A
  truncated read reported as a denominator** -- the exact class this estate has banked twice over
  (*never head OR tail a search whose count carries a verdict*; *a denominator is an artifact, not
  a summary*). Re-run untruncated: rc=1, 19 lines, `grep -c 'INTEGRITY/'` = **13**, split 8/5.
  Nothing downstream read the number -- it lives in a surprises array, not in any acceptance row,
  denominator or verdict -- but a wrong number in a certified record is a wrong number, so it is
  corrected in all three instances rather than left standing.

  **SUBSTANCE: CLOSED, and not by me.** `0.0.0_AB_MSTR~Z` established the mechanism at source
  (`@e4f3b36f41`): `chain_root()` returns `archive/<device>/` only if that dir exists and otherwise
  falls back to the legacy flat root, which its own docstring says **is the laptop chain** -- so a
  site-Z seat compares device-local live logs against the LAPTOP's baseline. `1.0.0_SA_CTO~Z` then
  closed it as the named A.2 gate: it is `rv0057-f001`, a migration mid-flight with a named
  terminus, **not an artifact and not a tamper**, and no further reports are needed.
  **I verified both halves here rather than relaying them.** The named discriminator is
  **DIRECTION, not magnitude**: over all 8 sized rows, **shrank=8, grew=0, unchanged=0**
  (1.46x-23.81x). A wide spread is what the device-axis reading *predicts*; a tamper reading
  predicts mixed directions with some logs UNCHANGED, and 0 of 8 are unchanged. That
  independently reproduces `0.4.0_DS_ClientPlatform~L`'s 8/8 from a different seat and run.
  Resolution condition unmet: **0 device-level subdirs** under `org/audit/archive/`.
  ⛔ **I did NOT create that directory** -- `1.0.0_SA_CTO~Z` names one `mkdir` as the trap (it would
  make the tool believe we are post-migration while all 238 files remain flat, comparing live logs
  against an EMPTY chain). I only listed it read-only.
  **The invariant is the ZERO, not the total:** I read 29 subdirs, CTO read 32 minutes later. The
  total grows as archives are minted and is wrong the moment it is written; `0 device-level` is what
  the fallback actually keys on. Banking the perishable total would have manufactured a false
  disagreement between two correct reads.
- **CVO F2 named three resolution surfaces over this name space; there are FIVE.** The two it did
  not name are `data/mdpf/scripts/gold/mdpf_model_registry.json:1 @e88c54e238` (whose declared
  absence policy, *"emits model_key=null + model_key_unmapped -- surfaced, never silently dropped"*,
  is the ONE estate surface that already matches ND-c-3) and
  `data/assets/scripts/gold/build_cottonwood_mdpf_slice.py:151,243-257 @2d5f8a7f74` (`canonical_key()`
  RAISES -- this is ND-g-2's named forward hazard, recorded and NOT remediated, since it is a
  producer this project does not own). Both are recorded in `RESOLUTION_SURFACES` in the module.
  This WIDENS F2 rather than contradicting it, and it changes nothing about the discharge.

## 6a. Mid-session: the TOs were re-seated underneath the build (msg 9467, ACKed)

`2.0.0_SA_COO~Z` re-seated all three TO faces at `@9181534a61` **while this seat was building
them** -- the `<issued_to>` elements read `DS-class ... SEAT NOT ASSIGNED`, so `to-check.py`
rendered them unassigned or resolved a serial out of prose. *"A seating that exists only in a
message is not a seating."* Nothing about the work changed and nothing was blocked.

**I re-pinned `spec_ref.vintage_commit` to `9181534a61` rather than leaving it at the vintage I
happened to open** -- but I MEASURED the delta first instead of assuming it was cosmetic:
`git diff 2162f50620 9181534a61` over each TO changes 10 lines, and **0 of them are
criterion-bearing** (`ND-TO|<criterion|expected_criteria|Acceptance criteria|cell_refs`), with a
**positive control** that the same pattern matches **14** lines inside the file -- so those zeros
are measured absences rather than a broken pattern. Only `<issued_to>` and an added seating note
moved. No criterion was re-read and the build stands.

## 7. Compiler tools

| phase | tool | result |
|---|---|---|
| 1 | `comp-which` on the surface question | NO CURATED RULE MATCHED -- catalog does not cover it; licenses the direct search under Rule 21 |
| 1 | `comp-find --name '*name_discovery*'` | 1 hit / 29039 files -- no existing declared artifact. Rule 5: scope does not collapse |
| 1 | `comp-find -i` token census | `Tax` 25149 hits / 27217 files vs `Muni` 1801 -- the ND-c-1 substring evidence, measured on this estate |
| 2 | `.tools/commit-gate.sh` | rc=0 on both `.py` files |
| 2 | risk-reflex `comp-pulse diff` (in safe-commit) | REFLEX CLEAN, 3 files vs 1351 danger nodes |
| 3 | `proof-of-spec-check.py` x3 | see section 8 |

## 8. Proof of spec

Three instances authored under `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/`
(paths dictated by each TO's `<instance_path>`). `proof-of-spec-check.py` run POSITIONALLY, rc
captured with no pipe. **The instrument refused the first draft** (missing `controls`,
`declared_exclusions`, `surprises`, `session_log`, `compiler_tools`; `vintage_note` not permitted on
`decomp_ref`) -- recorded because a checker that accepted a malformed instance would have told me
nothing.

**Mutant controls -- four planted, four fired, tree restored to byte-identical:**

| mutant | change | result |
|---|---|---|
| M1 | `satisfied_forms` returns `out[:1]` (the scalar CVO F1 refuses) | `AssertionError: 1 != 4 : forms=['bare']` -- and `bare` is exactly the least-specific value F1 predicted |
| M2 | word-boundary predicate degraded to substring | FAILED -- the estate-vocabulary baits are caught |
| M3 | `annotate_registry` sets `NO_MATCH` on an un-noded token | `ND-c-3 VIOLATION: registry annotation changed the verdict 'CANDIDATE' -> 'NO-MATCH'` x3 |
| M4 | revert the normalise fix (section 5) | `'partner_tax_free_descriptor' not found in [] -- it is INERT` |

**Determinism:** two same-input runs, byte-identical (9553 bytes, 99 lines) once the wall-clock
timing line is normalised. rc=0 both.

**Final verdicts, rc captured with no pipe:** TO-1 `rc=0 VALID` (5 rows), TO-2 `rc=0 VALID`
(4 rows), TO-3 `rc=0 VALID` (6 rows). **NEGATIVE CONTROL on the instrument:** the same command
against TO-2 with one bogus id appended (`ND-TO2-AC99`) returns **`rc=1 INVALID`** -- the
bidirectional coverage diff still refuses, so the three zeros above are verdicts and not a
checker that passes everything.

## 9. State at close

- **TO-1, TO-2, TO-3: built, exercised, 15 of 15 criteria PASS.** Build at `fd15cd5cf3` **LOCAL**
  (push state read below); proof instances + this log in the follow-on commit.
- **Nothing blocked.** No gate created, no cron armed, no alert/monitor built, no served key
  written, no silver/bronze partition touched, no historical data reclassified.
- **Out of scope, honoured:** `ND-g-1` security grain, `ND-g-2` the `canonical_key('DIVZ SMA')`
  raise (recorded, not remediated -- not this project's producer), `ND-g-3` the classification act,
  `ND-g-4` partners beyond cottonwood.
