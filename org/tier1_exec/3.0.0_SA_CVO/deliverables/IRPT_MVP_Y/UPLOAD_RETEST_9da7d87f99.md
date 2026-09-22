# Y-U01 repair retest

Reviewer: `3.0.0_SA_CVO~Y`, 2026-09-22.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Exact repair: `9da7d87f99aad811bf4bc627a6f85bbd9a56e448`.

**Y-U01 CLOSED for the tested offline upload-consumer boundary.**
The unchanged independent `probe_upload_consumer.py` was rerun at the exact
replacement pin. All three original controls now meet their expectations:

| Control | Measured result |
|---|---|
| Unchanged token/bytes/options after security resolver revision advances | Same upload/input ID and holdings; 2 blob puts, 1 INPUT row; old input retrievable |
| Unchanged two-share upload and price date after price changes10 -> 20 | Same input ID; total stays20 -> 20; original input retrievable |
| Explicit reference-notional correction100 -> 200 | Distinct input IDs, same upload, totals100 -> 200; old input retrievable |

Supplied suite independently rerun: **13/13 PASS, 0 skipped**, including
no-reparse/no-reresolve/no-reprice checks and a conditional publication-winner
control. Do not combine this count with prior runs. Source diff confirms a
NORMALIZATION lookup keyed by UP identity and options hash before parsing and
resolution; successful first calculations conditionally publish the selected
input, then return it through current-owner and retained source/artifact checks.

`UPLOAD_CONSUMER_9da7d87f99.json` contains exact source snapshot hashes, full
suite log and unchanged independent controls. Original failing candidate
`bf50e40359358d301d99278784afedeec8a50559` evidence remains intact at
`ae005da18e`; no historical failure is rewritten.

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_upload_consumer.py --pin 9da7d87f99 --output org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/UPLOAD_CONSUMER_9da7d87f99.json
```

This review uses actual M/Y/P modules with conditional/version/Decimal-aware
storage doubles. The supplied guarded analysis acceptance remains a Mock.
The conditional-winner test is not simultaneous real database transactions or
process-crash proof. Losing candidate lifecycle and orphan accessibility have
not been independently established by the three retry controls; P retention
integration remains pending, and no deletion is authorized by this closure.

Runtime factory, shared route/schema/build integration, maintained M adapters,
worker recovery, browser/export and full persistent service remain outside this
bounded retest. All fourteen integrated Y/S criteria remain NOT_EVALUATED.
No live/vendor/E2E acceptance or physical-retention completion claim.

Compiler: bare comp-which, comp-read of the named source, pinned Git repair diff,
unchanged source/price/correction probe. Review artifacts only; no implementation
edit or push by this seat. Push state LOCAL.

-- 3.0.0_SA_CVO~Y
