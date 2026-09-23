# Accepted holdings publication candidate — 2026-09-22

Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`, M4/M5. This is a local code candidate, not deployed or a full M4/M7 PASS.

`holdings_snapshot.land` writes actual Gold Parquet, bounded canonical Platinum JSON and an immutable manifest through `holdings/publication.py`. Canonical `opal_naming.address` resolves original private firm homes. The family is `holdings` (`holdings_qa` in QA), partition `date=<business-date>`, with the complete snapshot content SHA256 as revision. Same-day changed content receives a separate history key. Neither X10 product placement nor a public path is used.

Each artifact write uses `IfNoneMatch=*`, requires a non-null S3 version, and is read back by VersionId and SHA256 before acceptance. Identical retries may reuse the same verified object. The manifest pins Gold/Platinum bucket, key, version, hash and byte length, plus source revisions and clocks. Gold is parsed as Parquet and its complete node JSON is compared to Platinum before writing. Bounds are 64 MiB Gold, 4 MiB Platinum/manifest and 1 MiB index.

The runner captures the current publication index before source construction. The only discoverability mutation is a conditional `IfMatch`/`IfNoneMatch` write of `platinum/holdings/current/manifest.json` after artifact verification. The index retains accepted revisions by business date; backdated publication cannot move latest backward. Concurrent stale publishers refuse. Validation, reconciliation or artifact-readback failure leaves the old accepted index unchanged. Orphan immutable artifacts after a failed attempt are not discoverable through the index; no cleanup is implemented or authorized.

The actual holdings Entry now gives its verified canonical tenant to the accepted reader. The reader checks index identity, dates, canonical reference location, exact version, length and hash before parsing. It rejects missing, corrupt, cross-firm and legacy mutable publications. It appends the accepted content revision to served source revisions. Existing exact retained selection, fresh grants and post-read revocation checks still apply. Storage references remain internal; served output carries the revision and original clocks.

## Verification

- `python -m pytest infra/aws/lambda/investor-reporting/holdings/tests -q`: **80 passed**.
- `python -m pytest data/assets/scripts/gold/investor_reporting/tests -q`: **85 passed**.
- Nineteen publication/transport tests include real Parquet and actual land -> accepted reader -> guarded Entry. Checks cover selected totals/revision, invalid refresh preserving the accepted old date/revision, corrupt manifest refusal, revocation during read, same-day history, conditional-writer conflict, malformed/different Gold, exact version/hash readback, unversioned refusal and size limits.
- These use an in-memory versioned S3 transport double and synthetic custody rows. No AWS write, vendor call, provisioning, deployment, schedule or push occurred.

## Integration requirements and limits

P owns packaging and IAM composition. Include `holdings/publication.py` and canonical `opal_naming.py`, registry files and naming schema at its supported runtime layout. The reader needs `s3:GetObject` on the canonical index and `s3:GetObjectVersion` on pinned Platinum snapshots/manifests. The runner additionally needs conditional object writes and Gold version reads. Pyarrow is publisher-only and not imported by the reader.

Versioning and write-policy enforcement have not been measured in a deployed environment. A timeout on the final index PUT has an ambiguous transport outcome; reconcile the accepted index instead of claiming rollback. Suspension of versioning during that final write is an operational control gap: returned `null` is refused but the completed write cannot be undone by this code. This candidate does not assert bucket policy enforcement or full crash consistency under a changing storage configuration.

Source builders still identify inputs primarily by dated labels; exact upstream object versions, independent full custody census/freshness, historical provider ownership and Y's accepted security/price/normalization adapter remain open. An accepted output manifest is not proof that these source capabilities exist. Fresh source-to-publication-to-browser proof for all three firms remains required. Browser header proof is separately in `BROWSER_SELECTION_EVIDENCE.md`.
