# Canonical normalized upload bridge review

Reviewer: `3.0.0_SA_CVO~Y`, September 22, 2026.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Exact source: `c2a01fb3f8ae179a38c55a695894390ad9442c97`.

Bounded result: **46 supplied tests plus 7 subtests PASS; 11 independent controls
PASS**. No new candidate defect found within these controls. All 14 integrated
criteria remain **0 PASS / 0 FAIL / 14 NOT_EVALUATED**.

The new `ycharts/generate/normalized_input.py` is a pure bridge. It verifies
the frozen document hash/input identity, prepares declared canonical identifiers
and positive dollar strings, and checks an upload checkpoint against those exact
identities and values. It does not implement authorization, vendor identity
discovery, mutation intent, checkpoint provenance, storage retrieval or a worker.
Those remain caller obligations; there is no installed runtime proof here.

## Execution and evidence

`probe_normalized_bridge.py` archives the exact intake and generate trees into
the ignored seat runtime directory, records SHA-256 for every archived file,
and imports the actual parser, local normalizer, bridge, recipe and transport
serializer. Local identity and price responses are explicit fixtures. Socket
connections are forbidden in both the independent process and supplied test
subprocess. OfflineTransport records actual multipart bytes and returns fixed
synthetic responses; no vendor or cloud operation occurs.

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_normalized_bridge.py --pin c2a01fb3f8 --output org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/NORMALIZED_BRIDGE_c2a01fb3f8.json
```

Supplied suite: `test_normalized_input.py`, `test_recipe_decimal.py`, and
`intake/tests/test_portfolio.py`: **46 tests, 7 subtests PASS**. The bridge's
15 supplied controls are contained in the 46, not an additional count.
`NORMALIZED_BRIDGE_c2a01fb3f8.json` retains the actual pytest output, source
hashes, exact create payloads, and all independent outcomes.

| Independent control | Result |
|---|---|
| Duplicate AAPL values plus explicit cash through parser -> freeze -> upload -> JSON checkpoint -> bind -> actual create serialization | AAPL `9007199254740993.11`, cash `1`, total `9007199254740994.11`; exact JSON number and weight text, local key absent from upload bytes |
| Returned binding isolation | Later mutations of checkpoint rows and preparation rows leave the returned binding unchanged |
| Changed frozen holding without updated hash | `FROZEN_INPUT_CHANGED` |
| Changed frozen input ID | `FROZEN_INPUT_CHANGED` |
| Coherent successful upload for different symbols with equal amounts | Refused; matching amounts do not establish identity |
| Vendor echo with inferred `S:` prefix | Refused even when display/amounts could suggest a match |
| One-cent checkpoint change while success/reconciled flags remain true | Refused by exact comparison |
| Unrelated vendor display labels with unchanged exact security IDs | Binding remains to exact echoed IDs; labels pass through and do not act as a crosswalk |
| Upstream `1e-24` positive value | Refused by normalizer bounds before bridge preparation |
| Declared CUSIP `001234567`, USD `0.01` | Leading zeros and exact cents survive upload/checkpoint/bind/create; local key remains separate evidence |
| Frozen two-share position with USD12.35 dated price | Binds USD24.70 and original content hash without re-resolving the price |

Probe corrections are disclosed: the initial CUSIP case used `1e-24`, which the
normalizer already refuses. That refusal became its own control; the positive
CUSIP case uses USD0.01. The first complete run also exposed a test setup error:
changing the first sorted holding to `1` selected cash already equal to `1`.
That was a no-op, not a candidate integrity defect. The negative control now
selects AAPL explicitly and asserts its old value differs before changing it.
The final complete run passed all 11 controls; repeated runs are not added to
the counts. No implementation source was changed.

## Limits and next evidence

This branch accepts only exact canonical-symbol echo. A vendor returning a
different internal security ID requires a separately evidenced mapping contract;
prefixes, display names, order and equal amounts are insufficient. The reviewed
bridge refuses that case. A successful offline echo does not establish how the
actual vendor resolves the identifiers.

The bridge consumes an already authorized, verified frozen object and a caller's
checkpoint. We did not establish current-access ports, source-manifest integrity,
artifact retrieval authorization, retention, mutation-fence enforcement,
checkpoint-to-attempt provenance or worker recovery by invoking these pure
functions. M's actual source/manifest/loader handoff and the assembled worker
must supply those checks. Display label correctness is likewise not proved by
the identity binding check.

Flat-package composition, actual vendor upload/readback/create, browser routes,
durable job/status/report flow and full acceptance remain pending. No live,
deployment, policy activation or push was performed. Push state LOCAL.

-- 3.0.0_SA_CVO~Y
