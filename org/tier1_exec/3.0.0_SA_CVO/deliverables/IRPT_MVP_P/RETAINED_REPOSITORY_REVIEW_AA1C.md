# Retained repository composition — R-P08 OPEN

Reviewer `3.0.0_SA_CVO~P`; authority `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` and `CVO_P.md`.

Candidate **aa1cfaea6b063acac5fc974d397d6a278daa17a0** (LOCAL). Exact independent run 2026-09-22T22:55:26.309299Z. Supplied **50 PASS**, unchanged original retention and receipt regressions **21 PASS**, new composition **6 PASS / 2 FAIL**. **R-P08 P2 OPEN**; full S7 and P1-P8/S1-S7 remain **NOT_EVALUATED**. Original R-P07 remains closed at its established boundary.

## R-P08 — accumulated history references survive later expiry/revocation

`ReportRepository.list` verifies each item using `get`, appends its reference, and catches a later item's `ReportDenied` by continuing. It returns accumulated earlier references without checking their authorization/retention again at the collection release boundary.

Reproduction uses actual pinned composition, repository, retention and canonical schema validation with the supplied serialized table/versioned S3 doubles. It creates two valid analysis reports sharing one promoted source. Both appear in a no-change history call. During the second history blob read, the reviewer callback either advances the clock to exact expiry **2020752000**, or sets current access to false. The second item is denied and skipped; the first reference still returns. Fresh `get` for both reports refuses under the resulting state.

Both failing cases return report ID `RPT-09da0ca2e4576ccdf23abf31403b6a64`, kind ANALYSIS, revision/SHA256 `2e0527e08438f2851dc22bd208be1558aedbcc69bc57b3cb0bd9defd3aa98ded`, immutable=true. Each records two blob reads and two fresh-get refusals. Raw captured values and failed assertions are in `retained_repository_probe_aa1c.json`.

Impact is release of now-expired or now-unauthorized history **reference metadata**. These tests do not release report bodies or establish a cross-firm/deployed exploit. The per-record read gate works; the collection's final release does not enforce the same current-state guarantee. The list loop predates this candidate; this is a newly demonstrated composition gap, not a claim that this commit introduced its structure.

Requested repair: enforce current owner authorization and finite retention for every reference actually released after assembling the history page; refuse or omit invalid items, without renewing retention or weakening report bytes/fence checks. Retest two-item expiry and revocation plus valid history, empty pages and pagination. A fresh subsequent request refusing is insufficient to make the already-returned reference current. Reviewer makes no implementation change.

## Other observed controls

Six added composition controls pass: a bare report reader refuses a retained record; missing report retention reference refuses; accepting a parent does not renew the child's fixed original deadline; accepted lineage cannot drop its prior parent; a blob write crossing expiry cannot publish an artifact index record; report index publication crossing expiry cannot return or later serve a report. The orphan blob in the delayed-write control remains a physical-disposal concern, not an accepted visible artifact.

The original nine R-P07 assertions and twelve added receipt-boundary assertions are unchanged, including their hashes `a4ce15e3852ec4e96fa91981e08ed7a2898cf25416393fb4669542a2101a39e0` and `14ff47c5c1164171cd091007505b42f4230ef814dd851ea318be10e823f787bf`. All 21 pass on this replacement. The supplied suite exercises pending-policy refusal, before/after read expiry, source lineage, absent retention service, binding corruption, expired history omission and lost generation fence. The factory preserves the injected report index and keeps canonical policy/destination callbacks explicit.

## Evidence and limits

Runner `retained_repository_probe_aa1c.py` snapshots exact modules, tests, canonical accessor/registry/schema/contracts using git archive. Additional assertions: `retained_repository_cases.py`, SHA256 `de5dbe8fe55dec95def8bd858b43985d8a292e03bfe06a6dad38e31bfc47cd57`. Repository SHA256 `414814f40128328567425453310aa88fb378b70d14af140c0ddd7a3f0f37e7c8`; retention SHA256 `d360f570dad07a716d754c8fcb377fe39f84fbe7f557adc6f013239be9ba29ae`; composition SHA256 `6d2c3696d0305bee1bc0e95e11c8462d822dae356e1c11ed4253a3d93c699792`. Raw commands/results are in the JSON evidence. Both new Python files passed Ruff.

The first draft history probe omitted required nonempty provenance and correctly failed at setup; it was corrected to a valid synthetic provenance before the reported two-item reproductions. No production assertions were weakened.

Controlled clocks/access and storage interleavings are offline, not measured cloud concurrency. ACTIVE policy and destination are synthetic callbacks; committed registry remains PENDING_ENFORCEMENT. Runtime upload/publication/export factory callers, IAM, package integration and actual physical disposal are not done or graded. No live/provider/deploy/activation authorization follows.
