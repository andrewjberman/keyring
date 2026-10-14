# IRPT_ANLREQ -- decomposition, round 36A: THE ORDINARY-VIEWER AUTHORIZER OF THE UPLOAD DOOR, workstream ZA round 36 (issuer 2.0.0_SA_COO~Y2)

**Input:** row `IRPT_ANLREQ-D2-S93` (BLOCKING), from the release-28 sitting (`SITTING_RESULT.txt`: D1 to D4 refused NOT_AUTHORIZED before the file was read): the door composes `ports["ordinary_authorizer"]` as None (`reports/generate_installed.py :336`), so no non-Opal viewer can upload; FWD-1 needs a partner-firm advisor to upload its holdings. The CTO's rulings (msgs 7502 and 7505): build the producer; admit a non-Opal viewer only when the firm comes from the verified token, equals the request's firm and is in the viewer's `allowedFirmIds`, and the viewer has an active users row and a partner row for that firm; everything else refused as today; the same rule as the approved locked-firm portal route (open call 7773); a new never-widen pair stating who gains upload; then D1 to D4 re-run as the synthetic advisor.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-306` | the new module `_scope/ordinary_viewer.py` (a factory over INJECTED readers returning the `(request, principal, owner) -> bool` callable), its wiring in `reports/generate_installed.py` over readers the Lambda already holds (fail-closed otherwise), at least 14 tests on fakes, the record `r36/ORDINARY_AUTHORIZER.json` with the rule, the principal shape, the Lambda role's rights on the two tables, and the one-paragraph authorization change | the investor-reporting source tree (three paths) and the worker's record folder | WORLD (an infrastructure path) |

## Edges and chains

- One chain. Not in this round: the release (the package that carries the module is `irpt-ycharts-generate`, and an IAM change if the role cannot read the partner-row table: both are the release pair's), the pair itself, the partner-advisor drive.

fanout: 1 of 1 chains, cap 8, reason: one authorizer module with its wiring and tests; the rule is one function.
