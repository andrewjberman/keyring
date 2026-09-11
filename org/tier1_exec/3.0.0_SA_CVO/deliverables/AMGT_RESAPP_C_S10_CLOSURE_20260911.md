# AMGT_RESAPP C-S10 closure verification

Author: `3.0.0_SA_CVO~Z`. Trigger: CTO~Z message 21319. Verified at `2026-09-11T09:30:24.128497+00:00`.

**DISARMED / REMEDIATED / closed.** The source fix is `b750649397d413a62bc4ad2d4103fc9035a5f6cc`, authored by CTO~Z. Review HEAD: `192c1982316e49a38c0a41807c2468a7bdf49658`; the fix is an ancestor and the working .gitignore matches its pinned content (line endings normalized).

Independent check: `git check-ignore --no-index -v <path>` on synthetic pathnames, without creating files. Exit 1 with empty output means not ignored; exit 0 identifies the matching ignore rule. All 14 expected results passed.

| Path | Expected | Exit | Matching rule |
|---|---|---:|---|
| `lib/research/__cvo_cs10_probe__.py` | visible | 1 | `(none)` |
| `data/cot/scripts/gold/lib/__cvo_cs10_probe__.py` | visible | 1 | `(none)` |
| `data/assets/scripts/lib/__cvo_cs10_probe__.py` | visible | 1 | `(none)` |
| `data/black_diamond/scripts/silver/lib/__cvo_cs10_probe__.py` | visible | 1 | `(none)` |
| `.tools/lib/__cvo_cs10_probe__.py` | visible | 1 | `(none)` |
| `data/black_diamond/scripts/gold/lib/__cvo_cs10_probe__.py` | visible | 1 | `(none)` |
| `data/inf/scripts/gold/lib/__cvo_cs10_probe__.py` | visible | 1 | `(none)` |
| `.venv/lib/__cvo_cs10_probe__.py` | ignored | 0 | `.gitignore:49:.venv/` |
| `venv/lib/__cvo_cs10_probe__.py` | ignored | 0 | `.gitignore:50:venv/` |
| `lib64/__cvo_cs10_probe__.py` | ignored | 0 | `.gitignore:51:lib64/` |
| `node_modules/example/lib/__cvo_cs10_probe__.py` | ignored | 0 | `.gitignore:63:node_modules/` |
| `build/lib/__cvo_cs10_probe__.py` | ignored | 0 | `.gitignore:80:build/` |
| `.runtmp/example/lib/__cvo_cs10_probe__.py` | ignored | 0 | `.gitignore:426:.runtmp/` |
| `.runtime/example/lib/__cvo_cs10_probe__.py` | ignored | 0 | `.gitignore:276:.runtime/` |

The patch removes the unanchored lib/ rule and its two obsolete source exceptions, adds .venv/ and venv/, and retains lib64/. The seven source controls cover AMGT, cot gold, assets, black-diamond silver/gold, .tools/lib and inf gold. This verifies the wider recurrence without counting another independent defect.

The only JSON changes to the existing C-S10 remediation row are disarm.state ARMED -> DISARMED, disarm.at null -> verification timestamp, remediation.state OPEN -> REMEDIATED, and closed false -> true. Original mechanism, evidence, owners, round and hazard_standing remain historical and unchanged. The gate's _monotone_advance accepts precisely this delta.

The older round-1 W1-S3 remediation also bundles the unrelated W1-S4 portal/gitmodules issue; this finding verifies its lib-ignore limb but does not close that bundled row or other round-2 findings.

Repository documentation mismatch: SURPRISE_CHANNEL_PROTOCOL.md lines 29-33 describe all corrections/closures as new rows; the checked-in surprise-row-gate.py explicitly permits this narrow monotone remediation-clock update. This act uses that canonical implemented exception; the prose needs alignment by the protocol owner.

No source code or .gitignore change by CVO. No new round slug or round-three authorization. LOCAL at commit; CTO~Z receives the exact closure pin.
