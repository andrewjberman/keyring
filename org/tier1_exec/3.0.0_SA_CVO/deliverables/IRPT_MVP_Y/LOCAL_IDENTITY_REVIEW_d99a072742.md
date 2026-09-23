# Independent local security identity review

Reviewer `3.0.0_SA_CVO~Y`, September 22, 2026.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` v1.2.
Candidate `d99a0727422165b688fb93de3841ee7020ae5d8d`.

The bounded local identity branch passes **40 targeted supplied tests plus18
subtests**, and **10/10 independent controls** through actual retained uploads.
No new defect found in these controls. Actual M security/price source, vendor
resolution/readback and browser/runtime integration remain outstanding.

## Reproduction

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_upload_consumer.py --pin d99a072742 --output org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/UPLOAD_CONSUMER_d99a072742.json
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_local_identity.py --source-evidence org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/UPLOAD_CONSUMER_d99a072742.json --output org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/LOCAL_IDENTITY_d99a072742.json
```

The source evidence contains exact-pin file hashes, verified before import by
the independent probe. Complete portfolio.py and its supplied tests were read.
The targeted suite covers portfolio12, upload17 and retained-upload11 tests;
the earlier snapshot command's17 upload tests overlap and are not added again.
Producer-reported shared-schema tests were not rerun here, so the producer's48
count is not represented as this review's independent supplied-suite result.

Independent controls use the actual CSV parser, UploadService, normalizer and
P retained repositories with storage/clock/ACTIVE-policy doubles. Local resolver
fixtures return exactly security_key, canonical_identifier,
canonical_identifier_namespace and resolution_revision. They are not evidence
that M's actual source resolves the same securities. Network connections are
forbidden and canonical policy was not activated.

## Observed controls

| Control | Result |
|---|---|
| Large-cent dollars, repeated AAPL rows and explicit cash | Four source rows preserved, two canonical holdings; exact total9007199254740994.31 survives retained write/read |
| Unchanged local retry with resolver forbidden | Same full result, zero additional blob puts, no current resolver call |
| Two source aliases mapped by fixture to the same canonical key/identity | One holding totaling0.30; both original source identifiers preserved |
| Local-key shares with exact-date USD price12.35 | Two shares become24.70; price evidence carries the same local key and revision |
| Local weights25%/75% with reference notional100.01 | Exact total100.0100; basis remains REFERENCE_NOTIONAL |
| One canonical alias maps to different keys | Whole input NEEDS_CORRECTION / AMBIGUOUS_SECURITY_RESOLUTION |
| One key maps to different canonical identities | Whole input NEEDS_CORRECTION / AMBIGUOUS_SECURITY_RESOLUTION |
| Local and legacy vendor identities mixed across rows | Whole input NEEDS_CORRECTION / MIXED_SECURITY_IDENTITY |
| CASH namespace with noncanonical cash token | Whole input NEEDS_CORRECTION / CANONICAL_CASH_INVALID |
| Price quote identifies a different local key | Whole input NEEDS_CORRECTION / PRICE_INCOMPATIBLE |

Every negative leaves zero INPUT rows and only the retained original CSV blob;
no partial normalized portfolio is published. Positive local source and holding
rows have no security_id, and holdings declare CANONICAL_SECURITY. The local
normalizer does not manufacture a vendor identity. Canonical cash is explicit
in the resolver fixture; actual M cash resolution remains a source obligation.

The supplied legacy S-prefixed resolver tests provide compatibility checks only.
They must not be used as a runtime mapping from local security keys to vendor
IDs. Actual vendor upload/echo/readback is separately required before create.
Persisted local identity and frozen retry do not prove that vendor boundary.

## Interface dependency and limits

Separate CVO~P notice232035Z reports reviewfb0f801529 on backend5add22ca9f /
portalcb62721c60:24 supplied PASS,10 independent PASS/1 FAIL. R-P09 P2 permits
both browser input_id fields to change together while content/artifact hash
still identifies the original portfolio. This is peer-attributed, not rerun
here, and belongs to the browser response parser; it does not turn these local
normalizer controls into a producer or retained-runtime failure. COO~P was
notified. Route-unavailable/zero-transport limits remain. Y-S01 closure stands.

All fourteen integrated criteria remain NOT_EVALUATED. No full Y2/S2/S3/S7,
actual M source, vendor/session, maintained runtime, server concurrency or
browser claim is made. Review evidence is LOCAL; implementation code unchanged.

-- 3.0.0_SA_CVO~Y
