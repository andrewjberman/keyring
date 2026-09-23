# Analysis resident publication - current integration delta

Source `2874e37647` over `bfe6469b1e` and `4ebe6948d9`, in
`C:/Users/AndrewBerman/Desktop/irpt-mvp-y-20260922`.
Seat `2.0.0_SA_COO~Y`, September 23, 2026, 17:52 Eastern.
LOCAL; origin CLOUD `b475b96309c0034b513f19393138984d05716d0e`.

## Behavior and exact installer delta

The resident worker, post-download recovery and certified publisher now use the
accepted job's concrete tenant for storage, while passing the unchanged actual
actor to all current authorization checks. Global or selected firm is a view,
not a replacement storage owner. Retention promotion derives both the accepted
submitter and original input owner from the retained, hash-verified composition;
it preserves refresh ancestry and rejects unrelated ownership. READY redelivery
reopens the same certified report with current access and the concrete partition.

P integrates exactly these four Y files below
`infra/aws/lambda/investor-reporting/ycharts/generate/`:
`resident_worker.py`, `publication_worker.py`, `publisher.py`,
`tests/test_resident_worker.py`. No new factory argument, resource, route or
queue message field. Use existing P `37526d36ae` or compatible accepted storage:
artifact/report get and retention require_live/promote accept `data_firm=...`;
puts/persist retain the actual owner and current actor. The consumer supplies
that keyword only for cross-firm reads, preserving same-firm compatibility.
P's principal_for(record) must resolve the accepted submitter's current actual
authority, not synthesize a principal from queue tenant or immutable input owner.

Also consume `bfe6469b1e`'s resident_session.py and worker/test delta. CTO closed
the exact bootstrap finding at `3d9f451`: only ResourceNotFound bootstraps;
denied/throttled/service/unknown reads are sanitized unavailable, and invalid
configuration cannot consume login/refresh intent. Existing factory and literal
installer/rollback in RESIDENT_ASSEMBLY_HANDOFF_20260923.md remain the interface.

## Focused evidence

18 tests PASS in 13.68s: ten adapter-to-worker missing/error boundaries, plus
eight connected Opal publication cases covering partner and other-Opal creators,
certified READY/reopen, revoked authority, changed original retention owner and
retained-PDF crash recovery without vendor reacquisition. The same-firm connected
case separately passed; three existing publisher source/revocation controls pass
in 4.75s, including refresh ancestry. Ruff and commit gates pass. No broad suite.

Reproduce the combined focused cases from the Y worktree:

```powershell
$env:IRPT_DUAL_OWNER_TEST_ROOT='.runtime/dual-owner'
$env:IRPT_INTERACTIVE_ACCESS_TEST_ROOT='.runtime/interactive-access-9a3ec2a11f'
python -m pytest infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_resident_worker.py -q -k 'opal_cross_firm or secret_read_failure or missing_session_bootstraps'
```

The fixtures verify exact P375 storage/admission and M485 maintained-source hashes;
the extraction recipe is in DUAL_OWNER_HANDOFF_20260923.md. Real acceptance,
repository, retained bytes, frozen recipe, certification and publication code run
against offline AWS/vendor fixtures. These checks do not prove deployed policy,
host installation, actual vendor report contents, browser or all-firm live journeys.

## Next proof and owner

P owns the current shared repositories/authority factory, package and sole-consumer
cutover receipt on approved always-on `i-0167fd745ad906a66`. Y consumes the concrete
installed boundary and proves AAPL 10.01 + VNQ 2.02 Dollars Overview through real
login, queue, vendor PDF, retained certified Analysis report, screen and reload.
CTO review `2dd385ed59` accepts exact `2874e37647` as bounded source PASS:
eight cross-firm cases PASS3.69s and four existing controls PASS2.22s in an isolated
exact-pin tree. The same commit grants publisher.py integration to P; the other
three paths were already covered. Bootstrap closure remains accepted at3d9f451.
The next missing installed MODULE:build_resident_runtime interface and readbacks
are recorded in current INTERFACES.md; no new factory signature is requested.
All Y1-Y7/S1-S7 remaining firm/input/unit/variant/recovery/export cases remain open.
