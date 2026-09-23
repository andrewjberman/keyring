# Y-R01 unchanged repair retest

Reviewer: `3.0.0_SA_CVO~Y`, September 22, 2026 Eastern.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Repair pin: `745c02890e` (full resolved source hash in the companion JSON).
Original finding/evidence commit: `446aed5ba86415b0004014be6701482bee2a6ce3`.

**Y-R01 CLOSED for the pinned offline reader boundary.** All **12 original
independent controls PASS**, and the combined supplied suite is **49 PASS**.
The original failure JSON/report remain unchanged. All integrated criteria
remain **0 PASS / 0 FAIL / 14 NOT_EVALUATED**.

The repair requires actual strings before matching report_id, revision and
certification_sha256. The original numeric64-digit certification digest now
raises `RequestReadRefused: READY_REPORT_RECEIPT_REQUIRED`; the identical valid
string control still returns the full schema-valid fixture. The canonical READY
writer still rejects the numeric value. All original owner/job/index/current
authorization and both retention-chain controls retain their passing outcomes.

```powershell
git diff 446aed5ba8 -- org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_owned_report.py
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_owned_report.py --pin 745c02890e --output org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/OWNED_REPORT_745c02890e.json
```

The probe diff was empty. No independent scenario, assertion or helper was
changed for this retest. `OWNED_REPORT_745c02890e.json` records the exact full pin,
source hashes, supplied pytest output and all 12 results. The original probe
uses exact Git snapshots, actual readers/repositories and offline storage/clock/
ACTIVE-policy fixtures; socket connections remain forbidden.

The supplied49 consists of the current owned-report tests plus prior owned-
request and retained-upload suites. It includes the new three-field numeric
receipt regressions and preceding public-projection tests. Those passing supplied
projection tests are not an independent public-interface or HTTP acceptance
review. The unchanged probe still tests the full **internal** reader.

No real certifier/publication provenance, HTTP Entry, installed runtime,
browser/report flow, IAM or vendor action was established. The historical finding
was malformed persisted receipt validation, not demonstrated unauthorized access;
its closure does not broaden those claims. No implementation source changed or
push performed. Push state LOCAL.

-- 3.0.0_SA_CVO~Y
