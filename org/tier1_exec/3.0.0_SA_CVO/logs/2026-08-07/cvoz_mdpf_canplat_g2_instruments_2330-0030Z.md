# CVO~Z session log — MDPF_CANPLAT.G2 instruments built, exercised, on the record

**archetype:** VALIDATE
**Seat:** `3.0.0_SA_CVO~Z` (fresh reset, Andrew-direct) · **Window:** 2026-08-06 23:30Z – 2026-08-07 00:30Z
**TO:** `MDPF_CANPLAT.G2.regression-comparator-and-acceptance` @f123fbf6e (GO 23:58:44Z, ACKed)
**Governing:** PRD @24d3eb2f8 §5.5 · CONTRACT @a3106d585 §B/§E · PRD §0 verbatim in force (shape project, no error-hunting)

## What shipped (deliverables/MDPF_CANPLAT_G2/, commit @411e8e8a3 + this session's follow-on)

1. **§B closed field-path list** (`sectionB_field_paths.json`) — machine-consumed; only named `exemptions`
   excuse a diff; `decision_pending`/`path_pending` excuse NOTHING; W-2 coverage exemption is
   `null_to_nonzero_value_only` so the Guard-3 `else None`→`else 0` one-token class fails by construction.
2. **Baseline pinned**: `baseline_manifest_20260807T000753Z.json` — 14/14 keys (12 canonical + 2 R12
   extras), explicit VersionId + ETag + sha256, stamped pin instant 2026-08-07T00:07:53Z, ~9.7h before
   the next 09:50 ET publisher cycle. Re-pins are new manifests.
3. **R7 comparator** (`r7_comparator.py`) — all five limbs; PASS-NOT-CITABLE stamped mechanically until a
   mutation record exists; structural walk localises container transitions to one path.
4. **R1/R2/R12 instruments** (`g2_instruments.py`) — R1 wording is EXISTENCE-only by construction; R2
   writes complete JSON run records; R12 checks both standalone extras.
5. **Records**: `MUTATION_EXERCISE_20260807.md` (M1 business-value: FAIL+LOCALISE at `total.aum`, 1/117
   paths; M2 Guard-3 `null→0`: FAIL as distinct NULL→ZERO at `non_model_aua[0]`, NOT absorbed by the
   coverage exemption; M3 positive control `null→123.45`: EXCUSED-ONLY — the exemption boundary sits
   exactly at zero, proven both directions), `THREE_STATE_20260807.md` (absent/null/zero → distinct
   verdicts; `2` vs `2.0` no-diff proves rule 3), `R1_R2_R12_first_run_20260807.md`.
6. **First citable full-surface run**: `runs/R7_20260807T002510Z.json` — live vs pin, 12/12 TIE,
   47,119 paths compared, 0 regressions, CITABLE.

## Measured, routed, not chased (PRD §0 discipline)

- **SURPRISE 002451Z → COO~Z**: pinned global account-distribution carries `basis`/`source` ABSENT (not
  null as PRD W-3 / CONTRACT B1 today-columns state). COO~Z triaged 002550Z → CTO~Z one-cell §B1
  amendment ask; my list stays as-extracted (fail-closed) until the amendment lands.
- R2 pre-build FAIL (229/43/29 divergent per type) is the instrument's negative control, recorded as
  such — the divergent set contains exactly the CONTRACT's measured rows (W-1 at cottonwood, the five
  global-only fields, `inflection_non_model_aua`), and nothing was routed as a defect.

## Error of my own, on the record

Mid-session I read a run of "No such file or directory" results as *the shared tree wiped my uncommitted
deliverables* and wrote that narrative into the README (later excised). Ground truth: my shell CWD was
still parked inside the deliverables directory, so every `org/...`-relative path resolved against the
wrong base — the retrieval failed, returned a value, and I read the value as world-state without
printing its frame. The surviving 00:07:53Z manifest falsified the narrative before anything external
shipped; the near-miss was a false-loss report to MSTR~Z, drafted and not sent. Same class as the
`git show <bad-ref> | grep -c` zero: the control belongs on the retrieval (pwd beside every relative
read), not on the pattern.

## Compiler Tools

| Tool | Call | Result |
|---|---|---|
| comp-which | "how do I enumerate served platinum keys with versions" (Phase 1 mandate) | routed to comp-keys (score 0.47); comp-platinum top hit not fitting (component trace) |
| comp-keys | `prefix s3://opal-data-portal-v2/platinum/mdpf/` | live listing incl. the 21:42Z archive sweep; NO VersionIds — gap for pin purposes, TO-sanctioned s3api fallback used (boto3 `list_object_versions` inside the committed instrument, denominator printed) |
| comp-validate | not run | no validate config exists for org-lane instrument artifacts; controls were the M1–M3 mutants + three-state fixtures (negative + positive, isolated invocations) |

Gap worth one line: comp-keys carries LastModified but not VersionId; a `--versions` mode would make the
pin's enumeration rail-native.

## Blockers

None at me. The §B1 amendment sits with CTO~Z (routed by COO~Z; my re-derive is mechanical when it lands).

## Next steps

1. **[3.0.0_SA_CVO~Z]** On CONTRACT §B amendment: re-derive `sectionB_field_paths.json`, new commit, cited.
2. **[3.0.0_SA_CVO~Z]** On P1-1 candidate artifacts landing: same-data-day R7 run per the vintage
   discipline; diffs land as regression reports to COO~Z.
3. **[3.0.0_SA_CVO~Z]** W-6 fold paths: when the CONTRACT names them, move `path_pending` → `exemptions`
   under the amendment protocol.

— 3.0.0_SA_CVO
