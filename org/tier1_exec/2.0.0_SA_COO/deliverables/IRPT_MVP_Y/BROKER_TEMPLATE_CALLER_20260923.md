# Broker template caller -- concrete first-hop addition

Y source84c6e63806 on upload ebf8d33985. Three-file integration unit:
- intake/resolution_broker.py
- ycharts/generate/transport.py
- ycharts/session/tests/test_resolution_broker.py
All relative to infra/aws/lambda/investor-reporting/.

## Installed call chain

UploadService(resolve_template=UploadTemplateResolver(resolver), **existing_ports)
uses SecurityResolver(provider_check=BrokerSecurityCheck(...), identity=the
maintained identity reader, cache=the approved cache or None, clock=epoch_clock,
account_id=str(enrolled_user_id), source_revision=the deployed lookup code pin).
The BrokerSecurityCheck takes acquire_transport, same account/revision/clock.
Its acquire_transport must return a newly acquired actual
SessionBroker.operation_transport(raw, lease=shared_operation_lease,
holder=unique_operation_id, ttl=..., invoke=total_deadline_invoke,
clock=epoch_clock, wait=bounded_wait, request_budget=...).

It requests precisely /securities/securities_info?securities=URLENCODED_IDS,
matching CRO d7d044ba7a. Final response route, complete read,200,JSON MIME,
no login/WAF, byte count/1MiB cap and strict JSON must all pass before an envelope
can attest completeness. classify_batch still validates every returned row and
entitlement before omission becomes NOT_FOUND. Raw transports cannot be used.
Enrolled account mismatch/session change refuses. A timed-out or late operation
stays quarantined under the shared lease. A successful or rejected completed
read releases ownership. Caller failures become UNAVAILABLE, never negative.
The transport now records final_url_path/body_complete after response.read()
returns; ReplayTransport carries matching explicit fixture metadata. No query,
credentials, raw response or cookie value added to transport evidence.

## Executable proof

Set existing IRPT_FIRM_DESTINATION_POLICY pinned path; run:
python -m pytest infra/aws/lambda/investor-reporting/ycharts/session/tests -q
Result85 PASS (20 new controls including actual guarded UploadService -> broker
-> OperationLease -> ReplayTransport -> actual P ArtifactRepository and retained
input). CSV AAPL10.01/VNQ2.02 freezes12.03; reopen and same-token retry preserve
it with one provider invocation and two artifact writes.
Generation suite with the established exact P/M dependency roots:236 PASS plus
32subtests. Initial session run omitted the policy env and failed two existing
checks; rerun with the exact existing policy passed, no source weakening.

Provider bodies and AWS stores in these tests are offline fixtures. Actual
process-enforced transport deadline, durable operation store installation,
resident consumer/sign-in, public schemas and runtime package remain unproved.
This source does not turn raw Transport's socket timeout into a total deadline;
the resident invoke implementation must interrupt within the reserved budget.
No live call was made. Source compatibility is not installed runtime evidence.

## Review and next action

CTO76480a2a35 closes the preceding fe0 causal-recovery finding. Keep broker.py,
recipe.py,job.py and test_broker_recovery_evidence.py from fe0 together when
integrating. Current addition is separate and ready for direct review/P package
queue with ebf8 template upload requirements. Y continues resident installer,
deadline invocation, worker/frozen recipe/certifier assembly under approved
Andrew6fc3/CTOf1add. P installs shared resources, route/schema/IAM/package batch.
