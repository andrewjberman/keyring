# Ledger irpt-resident-st12-20261002, the before-read (packet section 3 step 2). READ ONLY: no write, no restart, no vendor
# call. Sent through Systems Manager by host_read.py. A job in flight holds its generation message in flight, so the
# queue at 0/0 and the provider operation lease with no holder together say no job or operation is running.
set -u
UNIT=irpt-analysis-resident.service
R=/opt/irpt-resident
echo "before-read $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "unit $(systemctl is-active $UNIT) since $(systemctl show $UNIT -p ActiveEnterTimestamp --value)"
echo "running root $(systemctl show $UNIT -p ExecStart | grep -o "$R/[0-9a-z-]*" | head -1)"
echo "roots on host: $(ls -1 $R | tr '\n' ' ')"
for Q in irpt-generation irpt-generation-dlq; do
  echo "queue $Q $(aws sqs get-queue-attributes --queue-url https://sqs.us-east-1.amazonaws.com/313476888478/$Q --attribute-names ApproximateNumberOfMessages ApproximateNumberOfMessagesNotVisible --region us-east-1 --query 'Attributes.[ApproximateNumberOfMessages,ApproximateNumberOfMessagesNotVisible]' --output text 2>&1 | tr -s ' \t' '/')"
done
KEY=$(python3 -c "import hashlib; print('PROVIDER_OPERATION#' + hashlib.sha256(b'ycharts\\x001276035').hexdigest())")  # operation_lease.py:54, provider NUL account
aws dynamodb get-item --table-name irpt-jobs --key "{\"tenant\":{\"S\":\"_opal\"},\"job\":{\"S\":\"$KEY\"}}" --consistent-read --region us-east-1 --query 'Item.operation_row.S' --output text 2>&1 | python3 -c "
import json, sys, time
raw = sys.stdin.read().strip()
try:
    row = json.loads(raw)
    print('provider lease: holder %r session_fence %s state %s expires_in %.0f s' % (row.get('holder'), row.get('session_fence'), row.get('state'), (row.get('expires_at') or 0) - time.time()))
except ValueError:
    print('provider lease row: unreadable or absent (%s)' % raw[:80])
"
echo "journal, last 15 min, job lines: $(journalctl -u $UNIT --since '-15 min' --no-pager -o cat | grep -c -E 'IRPT_RESIDENT_(JOB|STEP|VENDOR)|READ_BACK|generate')"
