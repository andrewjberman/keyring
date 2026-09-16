# K.2 reconstruction attestation, signed BEFORE seal-open: nfra-oplgtw__20260914T1919Z, attempt 01

- **Certifier:** `3.0.0_SA_CVO`. The phase-1 work was performed by a worker fork of the base session, under the same serial.
- **Author:** `1.0.0_SA_CTO~A`.
- **Packet:** `workflows/atom_decomposition/runs/nfra-oplgtw/20260914T1919Z/` @ `e0171ca5851d04b5a82d46658b0fb76560833d0f`.
- **Author seal commitment:** `MUTANT_SEALED.md`, sha256 `283c323ac5448973301289310fbd6600d6ad84f6050d5562d3708bfd83054ca6`, sealed 2026-09-14T21:50:51Z.
- **State at signing:** the seal is NOT open. This seat holds no seal bytes, no coordinates, no nonce, no dry rectangle and no plant patch.

**Law:** `docs/architecture/OPAL_ANALYST_PRD.md:1232-1260` @03062fcea1 (K.2(c) and (e)); `:1265-1268` (M-C); `:2444-2448` (a route is recorded as AVAILABLE-AND-DECLINED, with its mechanism, never as a bare "no"); `projects/ATOM_DECOMP/skill/atomic-decomposition/SKILL.md:30-31` @03062fcea1.

## The declaration

**This seat did not derive, and did not attempt to derive, the plant's location by any non-assessment route (diff, replay or positional inference).**

**The nomination** in the signed assessment (`SIGNED_ASSESSMENT.md`, this directory) comes from assessing cells against their cited sources:
- **Instrument 1** is `check_c.py`. It re-derives 50 facts from pinned artifacts and source ASTs and compares them to the cell values. It printed 2 MISMATCH lines, both at `S3-data.recorded_observation`, footer `08242234/dim_balance`.
- **Instrument 2** was written fresh for this attempt. It walks `observed-metadata.json` @39a8c5eeca directly and reads `PROVENANCE_COLS` from `schwab_schemas.py` @c9a44aa896 by a regex, not an AST.
- Both instruments agree: the artifact records 39 columns (39 distinct names), and 39 = 34 vendor + 5 provenance. The cell says 40.

## Routes, one by one

| # | Route | Status | Mechanism and effect |
|---|---|---|---|
| R1 | **Prior full read of original c1, and replay of the original fill patches** (this seat's round @619dec559f) | **PRESENT IN CONTEXT; not taken as a locating route** | This fork inherits the base session's context, which contains `VERIFY_ROUND.md`@619dec559f. That file states c1's S3 column equalities ("30=25+5, 39=34+5, 29=24+5"), so c1's value for this coordinate was knowable before any assessment ran. It was not consulted to choose where to look. The nomination rests on the two source instruments above, and the source value (39) and the c1 value coincide. **An auditor should weigh that this knowledge was present.** |
| R2 | **`check_c.py`, the instrument that read 50/50 OK on c1** | **USED, as assessment; declared because of its dual character** | The script was written in the prior round against c1's cell structure. Its expected values come from pinned sources, not from c1. For a coordinate it covers, it flags a disagreement with source, not a change from c1: a correction that agrees with source passes silently. Because it was green on c1, a red on final at a covered coordinate also implies that the value differs from c1. That inference was not needed and is not relied on. It covers 50 facts across 7 of 18 cells. |
| R3 | **Deterministic replay** of `rectangle.c0.json` + `patches/*.patch.json` (the pre-dry patches in the packet) through `ssot_validate.py patch`, then a diff of the result against `rectangle.final.json` | **AVAILABLE-NOT-TAKEN** | All inputs are packet members at @e0171ca585, and the validator is at `references/ssot_validate.py`. K.2 records that this "names the plant" (`OPAL_ANALYST_PRD.md:1234-1235`). No replay was run and no diff was made. |
| R4 | **Direct diff** of the packet's `rectangle.c1.json` (the replayed predecessor) against `rectangle.final.json` | **AVAILABLE-NOT-TAKEN** | Such a diff shows the cycle 2-7 corrections plus the plant. It was not run. Only line 8 of each rectangle was read, for the D3 check. |
| R5 | **Git history:** a content diff of the run directory from @4498e665cc / @619dec559f to @e0171ca585 | **AVAILABLE-NOT-TAKEN (commit enumeration only)** | `git log 619dec559f..HEAD -- <run dir>` was run. It lists one commit (e0171ca585) and shows no content. No `git diff` or `git show` of a rectangle was run at any commit other than @e0171ca585. |
| R6 | **Positional inference** from the correction and dry patch rows (`c2-domain`, `c2-git-record-pins`, `c3`-`c7`) | **AVAILABLE-NOT-TAKEN** | Those files' contents were not opened. For the patch SCHEMA, only `data.fill.patch.json`'s `patch_meta` and its first row's key names were read; that is an original fill patch, already read in the prior round. **ENCOUNTERED:** `run.json`, a mandatory packet read, carries `notes.cycle_2_counting` ("S6 boundary evidence received both domain and pin correction") and `notes.review_lenses` (cycles 3 and 5 changed 1 cell each, cells not named). The cells' own `reviewed_at` stamps and "cycle-3 / cycle-5" instrument text were read during the full cell read that the assessment requires. Both name cells that a correction touched. Neither is the nominated cell, whose `reviewed_at` is 2026-09-14T19:32:37Z, the original fill time. |
| R7 | **Shared-user access** to the author's session scratchpad, codex thread or conversation history | **AVAILABLE-NOT-TAKEN** | The Windows user and filesystem are shared, and the boundary is not isolation (`PACKET_README.md`). No path outside the repository belonging to `1.0.0_SA_CTO~A` was listed or read. |
| R8 | **Author routed commentary** (M-I) | **USED, as required** | Read: the handoff message (inbox `20260914T220038Z_1.0.0_SA_CTO_A_...`), `PACKET_README.md`, `run.json` notes, `seed_metadata_correction.json` and `d4-pin-grain-check.json`, the last two for D3 and D4. None names a planted cell. Not read: `auth-findings.md`, `data-findings.md`, `auth-prd-review.md`, `compiler-probes.txt`, `comp-*.txt` and `validation_context_declaration.md`. |
| R9 | **Memory and records** | **USED, for D1-D4 closure only** | Used: this seat's `VERIFY_ROUND.md`@619dec559f (see R1). The auto-memory index is loaded in context and holds nothing about this run. |
| R10 | **Packet allowlist, FAIL-CLOSED** | **APPLIED; nothing declined** | The run directory holds 29 files at @e0171ca585, at HEAD and on disk. The allowlist holds 29. Differences: 0 in either direction. 0 untracked, 0 modified, 0 commits since. **Order, honestly:** the enumeration ran in the same parallel tool batch as the first reads of `PACKET_README.md`, `packet-allowlist.json`, `run.json` and `verifier_packet.json`, not strictly before them. All four are allowlisted, and no unexpected file existed, so no unexpected file was read. |

## Limit (K.2(e), restated so it is not overread)

This is a self-report. It binds through the cost of a false statement, and it is falsifiable only while the closure packet stays auditor-inspectable: this directory, the base session's transcript and the author's dry and plant trail.

Signed: `3.0.0_SA_CVO`, 2026-09-14, before seal-open.
