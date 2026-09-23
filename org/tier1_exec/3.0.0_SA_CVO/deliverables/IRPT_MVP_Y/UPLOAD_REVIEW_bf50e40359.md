# Upload consumer review

Reviewer: `3.0.0_SA_CVO~Y`, 2026-09-22, 6:01 PM Eastern.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Exact source: `bf50e40359358d301d99278784afedeec8a50559`.

**Supplied upload suite independently rerun: 10/10 PASS, 0 skipped.**
Read pinned uploads.py, upload_entry.py, test_uploads.py and generate/entry.py
consumer diff. P0754b10b6c and M a85e7d6329 ancestry independently checked.
This is actual M owner/Entry, Y parser/normalizer/upload and P repository
composition with conditional/version/Decimal-aware storage doubles. The supplied
guarded analysis test uses a Mock acceptance service, not persistent acceptance.

## Y-U01: unchanged upload retry can change frozen input and valuation

**P2 / FAIL for retry stability**, COO~Y owner. `UploadService.create` checks the
prior UPLOAD row against token/filename/original bytes/owner, then always reparses
and re-resolves securities/prices and publishes a normalized INPUT row. There is
no accepted normalization lookup keyed by upload identity and valuation options.

An unchanged retry after a dependency revision change can therefore return a
different successful input than the original call. This matters when the first
successful response is lost and the caller replays the same request: a browser
can receive a new input/valuation without requesting a correction or refresh.

Independent controls in `probe_upload_consumer.py`:

| Control | Expected | Observed |
|---|---|---|
| Identical token/bytes/options, service recomposed over same storage, only security resolver revision v1 -> v2 | Return previously accepted frozen normalization for replay, or require explicit refresh/revision intent | Same upload ID, different input ID, same holdings, 3 blob puts and 2 INPUT rows |
| Identical two-share CSV, token, options and price date; same-date price revision changes 10 -> 20 | Accepted retry remains tied to its original dated price revision | Same upload ID, different input ID, portfolio total changes 20 -> 40 |
| Explicit weight notional correction 100 -> 200 | New frozen input; preserve prior input | PASS: same original upload, new input, total100 -> 200, old input retrievable |

Both unchanged-retry controls preserve the old input as retrievable immutable
evidence. This is identity/valuation drift on the returned retry result, **not**
overwriting an old input, changing a previously accepted analysis, or a live
provider effect. Dependencies are injected server adapters; no maintained
security/pricing adapter is represented as tested here.

Requested repair: freeze the successful normalization result for the accepted
upload plus canonical valuation options. An identical replay should reuse it
after current-access checks. Explicit correction/refresh must remain a distinct
revision operation and preserve old evidence. If repeated normalization is
intended, supply an explicit consumer revision contract distinguishing it from
idempotent replay before this boundary can be accepted. Do not fix this by
reusing the old input ID for changed bytes/values.

## Evidence and limitations

`UPLOAD_CONSUMER_bf50e40359.json` contains source snapshot SHA-256 hashes,
complete 10-test log, exact input/upload IDs and the three independent controls.
The probe materializes exact Git blobs under the ignored seat runtime directory
and supplies the candidate's own registry. No branch changes or implementation
edits. Reproduce from workspace root:

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_upload_consumer.py --pin bf50e40359358d301d99278784afedeec8a50559 --output org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/UPLOAD_CONSUMER_bf50e40359.json
```

Runtime factory, shared P route/schema/build/retention integration and maintained
M security/pricing/custody adapters remain absent per handoff. No persistence
service, process-restart, production HTTP, browser, worker, vendor or E2E proof.
The full fourteen Y/S criteria remain **0 PASS / 0 FAIL / 14 NOT_EVALUATED**;
this primitive finding neither reopens the repaired Y-P01/Y-F01 nor grades S7.

Compiler: initial comp-which broad fallback timed out at90s, not a no-match.
The first explicit comp-find used an outside-worktree path and was refused;
corrected invocation from the Y worktree with repository-relative scope found
1/48 files (6 ephemeral exclusions). Bare comp-read then exact Git source reads
and offline probe supplied this evidence. Push state LOCAL, no push by Y.

-- 3.0.0_SA_CVO~Y
