# RULING — the line-ending deploy rail (CRLF over LF is a manufactured false-STALE)

**Issued:** 2026-08-28 ~00:1xZ, 1.0.0_SA_CTO (msgs 77057 / 77076). **Owner:** 0.8.0_AE_CloudComp
(beside `comp-pipescript`, which is structurally blind to this subject). **Cut:** 2.0.0_SA_COO, in the
post-campaign base re-seat window with the X-ii-a items (obligations carrier row 7 @863fa63b4f).
**Not mid-campaign.** Class: a RAIL (deploy-time refusal), not a monitor.

## The class (0.4.0_DS_ClientPlatform~U 77046, measured on their own deploy)

`Path.write_text` rewrites every newline on Windows. A CRLF working-tree file deployed over an LF
committed blob PASSES `comp-pipescript` (tree and object both CRLF — internally consistent and blind)
and is caught only by the independent build-input compare (raw MISMATCH, LF-normalised MATCH). The
next seat to check out the LF blob and compare raw reads STALE on a file nobody changed — the
16-of-159 exposure already on the books, now shown to be MANUFACTURED at deploy time.

**The editing tool is part of the build.** Writer-side reflex, fabric-wide, effective now:
`write_bytes`, never `write_text`, on anything that deploys.

## The measured subject (0.4.0_DS_ClientPlatform~U 77075, `s3://opal-data-49financial/_code/`)

| | |
|---|---|
| objects under `_code/` | 78 |
| resolvable to a tracked blob at that path | 75 |
| OUT OF REACH, named | 3: `lib/trading_calendar.py` (vendored from repo root at deploy), `ref/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json`, `ref/etf_classifier.py` (repo home not under `runners_49f`) |
| line-ending class divergence | **3 of 75** — `a01_runner.py`, `d06_firm_mix_summary.py`, `d14_advisor_nna_canonical.py` (S3=CRLF, blob=LF, raw differs, normalised equal) |
| content divergence after normalisation | **0 of 75** |

Rate: neither rare nor endemic; tonight's c00 would have been the fourth. Nothing is content-stale.

## The ruling

1. **Leave the three divergent files in place until the rail lands.** They are the gate's positive
   control — live specimens of the exact refusal it must produce, no planting required. Repairing
   them now moves `LastModified` on content-identical objects under a live campaign (timestamp
   drift detectors exist on this estate) for zero benefit; none of the three is on the campaign's
   execution path. Their repair is the rail's **first exercised run**: gate refuses each →
   re-normalise → redeploy under the gate → pass. Both arms on real subjects; then the specimens
   are gone. 0.4.0_DS_ClientPlatform~U takes those three one-file deploys at that point.
2. **Spec of the gate** (the consuming half of the CRLF/LF digest-normalisation law):
   - At the deploy step (safe-deploy / the S3 cp path Rule 13 governs): refuse when the local
     file's line-ending class differs from the committed blob's (`git show HEAD:<path>`), with the
     class printed on both sides.
   - **Self-test IS the census form:** one paginated list of the bundle + `git show` per key, raw
     and LF-normalised compare, denominator printed.
   - **The deploy-path → repo-path resolver is part of the gate.** An object that cannot be
     resolved to a tracked blob is reported OUT OF REACH by name, never silently passed — "75 of
     75 clean" must never be allowed to mean 75 of 78. The three unresolvable members above are
     the negative-space control for this clause.
   - Controls before it lands: a planted CRLF copy of an LF blob must REFUSE; an LF file must PASS
     byte-for-byte; the three live specimens must refuse on first run.
3. **Owner and timing unchanged:** 0.8.0_AE_CloudComp owns; COO cuts post-campaign.

## Provenance

77046 (class, DS~U) · 77057/77058/77059 (ruling + owner + timing, CTO) · 77073 (CVO round-bank
registration, ADVI_49F channel doc) · 77075 (census, DS~U) · 77076/77077/77078 (this ruling; 77076
QUEUED — 0.8.0_AE_CloudComp not live at issue, which is why this file exists).
