# AMGT EXPERIENCE: current runtime interfaces

## B08 corpus observation in the thesis bundle

Producer: `4599b057952ce221c2cfccc14260969666a9d454`, integrated onto the merged runtime base at `94f186168d`. Runtime calls the real `read_report_input` for the route's already-resolved security identity. The existing `/security/{key}/thesis` response gains `corpus`; no new route or authority context is introduced. The connection uses the existing `_pool_client()` seam, so `AMGT_POOL_ROOT` remains hermetic in tests and normal operation uses the existing S3 client.

The whole producer response is retained beneath `corpus`:

| Field | Meaning |
|---|---|
| `interface_version` | `amgt-corpus-report-input/1` |
| `security_key` | Existing resolved route identity; never the display alias |
| `observed_at` | Read timestamp, not source vintage |
| `state` | `CURRENT`, `STALE`, `ABSENT`, or `FAILED` |
| `reason`, optional `error_type` | Named state/failure; no raw transport details |
| `substrate`, `prior_reports`, `documents` | Producer-owned input payloads; FAILED has no partial substrate |
| `member_states`, `member_hashes` | Derived-member freshness and identity |
| `input_manifest`, `input_manifest_sha256` | Referenced input bytes and stable binding, excluding observation time |

Exercised examples (field excerpts; complete producer shape is not abbreviated by the runtime):

- Current fixture: `state=CURRENT`, `security_key=ACME_US_Equity`, one prior report, nonempty continuation content hash and 64-character manifest hash.
- Changed fixture: `state=STALE`, prior continuation document retained, changed manifest hash.
- Missing retained extraction: `state=FAILED`, `substrate=null`, `input_manifest=[]`; the previous returned observation remains unchanged.
- Unresolved identity: `state=FAILED`, `error_type=InvalidIdentity`, `security_key=null`; no pool client is created.
- Empty local pool: `state=ABSENT`, empty prior reports, named reason; no live S3 client is created.

This endpoint is a read: unchanged prior Python observations are demonstrated, not revision-store publication preservation. The typed portal client/display, durable revision acceptance boundary, dependency-complete Linux package and authenticated browser acceptance remain unfinished. The measured producer read fanout (IMB: 142 GET / 9 LIST) must be accounted for in the separate B08 package and live latency proof. Corpus/harvest/naming/PyArrow dependencies cannot be silently omitted from that package.

## No-span repair stays separately pinned

`NEVERWIDEN_COO_HALF.md` at `5b455971f8` binds only candidate ZIP SHA256 `0c44108821fe52850c77b119490039453b082c3639fae6dbf58de054b1397a55`. This B08 source integration does not change that artifact, extend its signature, or authorize a deploy.

## Price generation handback

Y candidate `1b6cd9d4e0`, independently reviewed at `2865a9c26e`, is integrated at `30102a6905`. Price now makes an explicit generation-state determination for the shared writer. Retained scored crossed rows produce COMPLETE; missing crossed rows produce FAILED with `pointer=null` and `reason_code=NO_RETAINED_MEMBERS`, never an inferred EMPTY. The compute path may determine EMPTY with its explicit exclusion reason. A failed writer clears the draft pointer, returns the failure reason/receipt and leaves the prior stored pointer and vintage unchanged. Both CLI modes report failures with a nonzero exit and tolerate nullable pointers.

Five independent in-memory controls demonstrate these boundaries; 200 candidate tests pass. This is local compatibility acceptance, not H live-journey, NO_COVERAGE migration, Linux package or deployment acceptance. Shared H module ownership remains with Y; all further Price work belongs to this seat.
