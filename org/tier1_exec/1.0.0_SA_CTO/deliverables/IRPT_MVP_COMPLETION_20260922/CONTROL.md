# Investor Reporting - CTO control sheet

Current 2026-09-23 23:25 UTC (Claude CTO session, successor to the Codex session closed 22:42Z).
All three products INCOMPLETE. CTO reviews directly; no independent CVO queue. Contract v1.4 and
exact path grants govern implementation. Evidence for this sheet's live figures:
DIRECT_REVIEW_2020_20260923/CLAUDE_TAKEOVER_LIVE_READBACK_20260923.json.

| Product / owner | Measured current evidence | Next executable result |
|---|---|---|
| Holdings / COO~M | Deployed reader repaired: irpt-holdings CodeSha l/GQrFcE...DDU= at 23:00:52Z, CTO-downloaded zip == approved 97f190ac (33 members, no parents[4]); ledger closed 5c8d6f8e34. COT expanded publication live: index grwnbLkeu (23:00:30Z) -> revision 93f930c265, 18 objects, 841 accounts / 13,793 positions / USD 548,412,662.59 reconciled, both Anna accounts present; prior index retained. Last real login: FAIL NOT_READY (22:17Z) against the OLD reader and the d486-only publication. | M: deployed reader matrix (0698 / d486 / combined; default + 2026-09-22 READ_OK, 2026-09-23 refused) against the live Lambda, then Andrew's signed-in Anna selection + reload on localhost:5174. Then 49F (Schwab 0833 + SmartX + Tax workbook) and INF (Orion + Eclipse where retained) candidates and the snapshot model overlay (Andrew 22:4xZ). P: defined-code NOT_READY reason contract (still open). |
| Reporting / COO~P | Native Linux replay PASS (2fb5422b04). Storage bucket live and verified. Callable/atomic one-use 068e9ccd85 and retained pointer f04d1e71bd NOT yet CTO source-reviewed. retained.tf naming gate now PASSES under LD-0609 (CTO-accepted). X10 PENDING_ENFORCEMENT. | P: merge CLOUD into the backend branch (never rebase), commit retained.tf; return 068e/f04d for CTO review with the 8 affected tests (reviewer export must include data/firm_registry.json); callable installation + least-privilege roles + native layer + enforcement matrix. Andrew-directed goal: Performance for 49F/INF/COT, /loop 20m. |
| Analysis / COO~Y | 2874e37647 cross-firm source accepted; P holds the 31-path integration grant (b02c9ad5af + f89fac6686). Current-authority source ADJUDICATED (RULINGS IRPT-ANALYSIS-CURRENT-AUTHORITY-20260923): P implements profile fields + IAM, Y consumes at job start/release. Host i-0167fd745ad906a66 is STOPPED by ec2-auto-shutdown-enforcer at 21:21Z (no AutoShutdown=disabled tag). | P: profile reader fields + exact IAM plan; AutoShutdown=disabled tag on the host via Terraform (plan to CTO, Andrew may veto); resident factory install + sole-consumer cutover receipt. Y: consume the authority decision; run the real-login 12.03 Overview journey once P's receipt lands. Andrew-directed goal: Analysis E2E, /loop 20m. |

## Ownership and immediate dependencies

P is sole shared auth/header/schema/routes/IAM/build/storage/export writer, with exact reviewed Y/M
integration grants. Y and M retain semantic implementation and full-tab exercise responsibility. P
performs bounded ready integration batches while advancing Reporting. No broad branch grant or
second queue/session consumer.

CTO review queue, in order: (1) M deployed reader matrix receipt, then Andrew's screen; (2) P
068e9ccd85 + f04d1e71bd source; (3) P authority-port + IAM plan and host-tag plan; (4) M
c354c33a92 Tax runner/Silver candidate and TAX_ONE_SHOT_RUNTIME_PLAN (after the Holdings thread
reaches the screen; no Tax runtime GO yet); (5) X10 enforcement matrix acceptance (CTO owner, M
registry writer).

M Tax dependency unchanged: d3a8c3e7e3 store accepted; c354c33a92 runner/Silver seam candidate
awaits CTO review; runtime capability/permissions still require concrete review; no research-envelope
conversion, full Tax restart or fourth COO.

## Decisions retained

- Opal has every function across all firms, clients and accounts; Global defaults. Firm viewers
  remain limited by current server-verified grants. Worker authority replays auth-handler refresh()
  on opal-users-v2; OPAL_GLOBAL iff firmId opal-capital or userType Dev; own-firm otherwise; admin
  descendants parked (P) until a journey needs them. Retained owner fields are locators, never grants.
- Holdings categories: Models / SMAs / Client(plug). Actual signed custody values, original dates,
  full census and reconciliation; no missing-as-zero or inferred USD. Snapshot model overlay only
  (client -> models -> assets), no model time series (Andrew 22:4xZ at COO~M).
- Andrew confirms all COT report amounts USD (6f45e8fbc9). Other firm currency remains evidence-bound.
  COT all-four-null no-position rows may be excluded with counts; partial-null rows refuse.
- Andrew Tax B d70decd6b2: 49F Traded=YES under SMAs/ALT Strategies/Tax, canonical dated membership
  and b00 net_mv_plus_cash. Workbook AUM/leverage do not set custody values.
- Y dedicated always-on host i-0167fd745ad906a66 approved 6fc3f5f785; the enforcer reaps it at +3h
  idle without the AutoShutdown=disabled tag, so the tag is a prerequisite of "always on".
- SmartX account PTD and allocation monthly results differ. No synthetic custom windows or set returns
  from sleeve averaging; unknown method/fees stay unknown.
- MSTR alone pushes shared branches and handles seat recovery and the Codex runtime retirement.
  All three COO lanes are Claude sessions with Andrew-directed /goal + /loop 20m; P's Codex driver
  PID 3520 retirement is MSTR's act.
- LD-0609 naming-gate lookup context ACCEPTED on CTO arms; no waiver, no bypass.
- Recorder 0b8784 accepted; preserve prior source-map/audit forensic residue.

## Review and completion rules

Each owner keeps concise STATUS with exact pins, current files, first failing hop, next proof,
dependency owner and limits. Messages only interface/blocker/handoff; no ACK chain. Use fast
affected checks and reuse pinned evidence; no test quota. All current review artifacts are in
DIRECT_REVIEW_2020_20260923. Source acceptance and infrastructure deployment do not prove an
authenticated user journey.

Done requires real backend/data/login, correct selected economics and authority, retained immutable
output, reopen/recovery and required export across every named firm/unit/variant. A first live
account is a milestone, never substituted for scope.
