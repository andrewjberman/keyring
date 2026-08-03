# Deploy completion — C2-sibling: frontier-counts catch discriminates absent vs corrupted

**Deployer:** 0.2.0_DS_PortfolioAnalytics (Rule-13 DS gold lane) · **Opened/closed:** 2026-08-03 22:29–22:32Z (single-leg, in-session)
**What:** `s3://opal-data-mdpf/code/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py` → repo HEAD @72cd1a7860. One hunk in `load_account_dist_frontier_counts` (the `:621-625`-class sibling swallow found by C2's outward trace).
**Authority:** CTO ruling + one-hunk grant 20260803T222834Z — C2-treatment: "honest-None is a claim about ABSENCE; a parse failure is not absence." Absent → declared honest-None + WARN (preserved); any other failure → contextual `RuntimeError` (`from e`).

## Discriminating mutant-pair evidence (the CTO's added bar: absence-only would pass unfixed)

| Case | Pre-fix (control) | Post-fix |
|---|---|---|
| ABSENT key (REAL S3, forced firm `zzz-c2sib-absent`) | WARN + `{}` | WARN + `{}` — **UNCHANGED** (declared behavior preserved; real `NoSuchKey` exercised the narrow branch) |
| CORRUPTED body (stubbed reader returning unparseable bytes; zero S3 writes) | **silent `{}` with the WARN saying "absent"** — the defect: a parse failure wearing the absence label | **raises** `RuntimeError: C2-SIBLING FAIL-LOUD: staged account_dist 49financial UNPARSEABLE ... (JSONDecodeError...)`, `__cause__: JSONDecodeError` |
| SUCCESS (real `49financial` staged read) | sha256 `44136fa355b3...` | sha256 **IDENTICAL** |

**Raise path — traced FRESH for THIS call site (C2b acceptance: not inherited from C2):** the three call sites (`:884` build_49f_artifact, `:1109` build_inflection_artifact, `:1927` build_global_artifact @72cd1a7860) sit in functions containing **zero** try/except statements (scanned spans `:794-1080`, `:1072-1180`, `:1741-2000`); `main` has no enclosing try (C2 trace, same structure) → rc≠0 → dispatch `|| return 1` → `STAGE6-REVAMP status=error`. All three sites reach the per-stage surface.

**TO reconciliation:** this work executed 22:29–22:32Z on CTO's direct ruling (222834Z to this seat) and CROSSED with the formal `MDPF_GLOBAL.C2b` TO @1d62ca44db (COO GO 22:31:37Z, citing the CTO→COO grant record 222901Z). Same ruling, two message IDs — commit @72cd1a7860 cites 222834Z; this ledger carries both. TO flipped pending; every C2b acceptance item is satisfied by the work above including the discriminating pair with the corruption leg shown failing on pre-fix code.

## Verification

commit-gate clean · `comp-pipescript deployed --pipeline mdpf` → **MATCH** · same-session ledger (this file).
**Cycle-attribution addendum:** this deploy also lands before tonight's cycle; a loud `C2-SIBLING FAIL-LOUD` tonight would mean a CORRUPTED staged account_dist (not absence) — new information either way.
