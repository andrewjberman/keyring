# Test Lambda Deletion Runbook (DEBT_1STRUN.005)

**Status:** Documented, NOT executed. Awaiting Andrew approval.

## Candidates

| Function | Runtime | Last Modified | Role |
|---|---|---|---|
| `test-yfinance-simple` | python3.11 | 2026-02-13 | lambda-execution-role |
| `yfinance-aapl-test` | null (broken) | 2026-02-13 | lambda-execution-role |

Both were flagged in DEBT_1STRUN.002 as test functions not worth registering in `lambda-source-map.json`. `yfinance-aapl-test` has `runtime=None` (cannot execute). Neither is wired to EventBridge, Step Functions, or API Gateway.

## Pre-delete checks (run before execution)

```bash
# Confirm no event source mappings
aws lambda list-event-source-mappings --function-name test-yfinance-simple
aws lambda list-event-source-mappings --function-name yfinance-aapl-test

# Confirm no EventBridge targets reference them
aws events list-rule-names-by-target --target-arn arn:aws:lambda:us-east-1:313476888478:function:test-yfinance-simple
aws events list-rule-names-by-target --target-arn arn:aws:lambda:us-east-1:313476888478:function:yfinance-aapl-test

# Confirm no invocations in last 30 days
aws logs filter-log-events --log-group-name /aws/lambda/test-yfinance-simple --start-time $(date -d '30 days ago' +%s)000 --max-items 1
aws logs filter-log-events --log-group-name /aws/lambda/yfinance-aapl-test --start-time $(date -d '30 days ago' +%s)000 --max-items 1
```

## Deletion commands

```bash
aws lambda delete-function --function-name test-yfinance-simple
aws lambda delete-function --function-name yfinance-aapl-test

# Optional: delete the log groups
aws logs delete-log-group --log-group-name /aws/lambda/test-yfinance-simple
aws logs delete-log-group --log-group-name /aws/lambda/yfinance-aapl-test
```

## Post-delete

- Remove any stale entries from `infra/aws/lambda/ci/lambda-source-map.json` (both were intentionally NOT registered in .002, so likely nothing to remove).
- Commit author: `0.5.0_AE_OpalETL <0.5.0_AE_OpalETL@opal.agent>`
- Tag: none required (test-lambda cleanup, not a pipeline deploy).
