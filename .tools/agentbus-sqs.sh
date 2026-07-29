#!/usr/bin/env bash
# agentbus-sqs.sh -- cross-device agent messaging over SQS (OPAL_SQSCHAT).
#
# WHY THIS EXISTS. opal-agent-comms is a LOCALHOST broker (port 7800) and
# org/mcp/liveness.json is gitignored, so both are DEVICE-LOCAL: an agent on site Z
# cannot see, address, or be addressed by the fabric on Andrew's laptop over MCP.
# Measured 2026-07-29: get_live_agents() on site Z returned 1 (itself) while
# 1.0.0_SA_CTO / 3.0.0_SA_CVO / 0.2.0_DT / 0.4.0_DE were provably alive on the laptop
# (11 pushes in the preceding hour). Before this, the ONLY working cross-device channel
# was the git trunk -- a HISTORY tier: no ack, no ordering, no backlog signal, and it
# needs a pull to move. This is the DELIVERY tier.
#
# TRANSPORT NOTE, read before extending: NFRA_AGENTBUS_PRD.md:105-108 designs the
# cross-DEVICE case (Port 2) on DynamoDB and reserves SQS for the cross-COLLEAGUE case
# (Port 1). This tool applies the Port-1 TRANSPORT to the Port-2 USE CASE on Andrew's
# explicit direction 2026-07-29 ("just frontrun the SQS creation"). That is a sovereign
# substitution, not a PRD amendment -- the PRD has not been amended. See OPAL_SQSCHAT.json.
#
# SECURITY MODEL: Port 2 deliberately carries NO cross-distrust controls (PRD A.2) --
# the same principal owns both machines, so there is no colleague boundary to partition.
# Do NOT route cross-principal traffic through these queues; that is Port 1's problem.
#
# USAGE
#   agentbus-sqs.sh send  <to-device> <from-serial> <body...>
#   agentbus-sqs.sh recv  <this-device> [--keep] [--max N]   # one-shot drain
#   agentbus-sqs.sh watch <this-device>                      # THE CONSUMER -- run under Monitor
#   agentbus-sqs.sh peek  <device>          # depth only, consumes nothing
#
# TO MAKE THIS DEVICE REACHABLE, arm the consumer once per session, under the Monitor tool
# (persistent: true, timeout_ms: 3600000):
#     bash .tools/agentbus-sqs.sh watch laptop      # on the laptop
#     bash .tools/agentbus-sqs.sh watch sitez       # on site Z
# WITHOUT A WATCHER ON A DEVICE, MAIL TO THAT DEVICE IS NOT DELIVERED -- it accumulates. `send`
# returning a MessageId means STORED, never DELIVERED. Verified live 2026-07-29: site-Z watcher
# armed and exercised end-to-end; laptop side pending Andrew's word.
#
#   <device> is `laptop` or `sitez`. `send laptop` puts a message on the queue the
#   LAPTOP drains; `recv sitez` drains the queue addressed TO site Z.
#
# ACK DISCIPLINE (CLAUDE.md Rule 22b -- SENT IS NOT READ). A successful send returns a
# MessageId. THAT IS NOT DELIVERY. It is not delivered until the receiving agent emits
# an ACK naming that MessageId. `recv` prints the MessageId of everything it hands you
# precisely so you can ack it; a transport-side signal (SendMessage 200, a CloudWatch
# count, a queue depth of 0) is NEVER delivery evidence. A depth of 0 is equally
# consistent with "read" and "drained by something that discarded it".

set -euo pipefail

ACCOUNT=313476888478
REGION=us-east-1
PREFIX="https://sqs.${REGION}.amazonaws.com/${ACCOUNT}/agentbus-ajbdev"

queue_for() {
    case "$1" in
        laptop) echo "${PREFIX}-sitez-to-laptop.fifo" ;;   # site Z sends, laptop drains
        sitez)  echo "${PREFIX}-laptop-to-sitez.fifo" ;;   # laptop sends, site Z drains
        *) echo "agentbus-sqs: unknown device '$1' (expected: laptop | sitez)" >&2; exit 2 ;;
    esac
}

cmd="${1:-}"; shift || true

case "$cmd" in
  send)
    to="${1:?usage: send <laptop|sitez> <from-serial> <body...>}"; shift
    from="${1:?usage: send <laptop|sitez> <from-serial> <body...>}"; shift
    body="$*"
    [ -n "$body" ] || { echo "agentbus-sqs: refusing to send an empty body" >&2; exit 2; }
    ts="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    # MessageGroupId is REQUIRED on a FIFO queue. One group keeps global ordering across
    # the channel; switch to a per-conversation group if strict ordering per thread is
    # wanted and cross-thread head-of-line blocking becomes a problem.
    out=$(aws sqs send-message --region "$REGION" --queue-url "$(queue_for "$to")" \
        --message-group-id opal-sqschat \
        --message-attributes "from={StringValue=${from},DataType=String},sent_at={StringValue=${ts},DataType=String}" \
        --message-body "[${ts}] [from ${from}] ${body}")
    mid=$(printf '%s' "$out" | grep -o '"MessageId": "[^"]*"' | cut -d'"' -f4)
    echo "SENT to ${to}: MessageId=${mid}"
    echo "  NOT DELIVERED until an agent on '${to}' acks this MessageId (Rule 22b)."
    ;;

  recv)
    dev="${1:?usage: recv <laptop|sitez> [--keep] [--max N]}"; shift
    keep=0; max=10
    while [ $# -gt 0 ]; do
        case "$1" in
            --keep) keep=1; shift ;;
            --max)  max="${2:?--max needs a number}"; shift 2 ;;
            *) echo "agentbus-sqs: unknown flag '$1'" >&2; exit 2 ;;
        esac
    done
    q="$(queue_for "$dev")"
    # DO NOT 2>/dev/null THIS CALL. The first version of this script did, and it turned every
    # failure -- bad credentials, wrong region, no network, a typo'd queue name -- into the
    # string "(no messages addressed to X)", which is BYTE-IDENTICAL to a healthy empty queue.
    # A user then reads "it didn't work" as "nothing was sent". That is the same discarded-stderr
    # class CLAUDE.md names for `git show 2>/dev/null`: the error goes to stderr and the empty
    # stdout renders as a clean negative result. Capture stderr, branch on rc, and SAY WHICH.
    set +e
    out=$(aws sqs receive-message --region "$REGION" --queue-url "$q" \
            --wait-time-seconds 10 --max-number-of-messages "$max" \
            --message-attribute-names All 2>&1)
    rc=$?
    set -e
    if [ $rc -ne 0 ]; then
        echo "ERROR: aws sqs receive-message FAILED (rc=$rc) -- this is NOT an empty queue." >&2
        echo "  queue: $q" >&2
        echo "  aws said:" >&2
        printf '%s\n' "$out" | sed 's/^/    /' >&2
        echo >&2
        echo "  Common causes, in the order they actually happen:" >&2
        echo "    1. This device has not pulled the commit that added this script's queues." >&2
        echo "    2. No AWS credentials on this shell: run  aws sts get-caller-identity" >&2
        echo "    3. Wrong account -- the queues live in 313476888478 / us-east-1." >&2
        exit 1
    fi
    if ! printf '%s' "$out" | grep -q '"Messages"'; then
        echo "(no messages addressed to ${dev}) -- this is a REAL empty queue: the API call succeeded."
        exit 0
    fi
    printf '%s\n' "$out"
    if [ "$keep" -eq 1 ]; then
        echo
        echo "--keep: messages NOT deleted; they return to the queue after the visibility timeout."
    else
        # Delete only what we actually received, one handle at a time.
        printf '%s' "$out" | grep -o '"ReceiptHandle": "[^"]*"' | cut -d'"' -f4 | while read -r rh; do
            aws sqs delete-message --region "$REGION" --queue-url "$q" --receipt-handle "$rh" >/dev/null 2>&1 || true
        done
        echo
        echo "Consumed (deleted from queue). ACK each MessageId above to the sender -- deletion is NOT an ack."
    fi
    ;;

  watch)
    # THE CONSUMER. Without this running somewhere, the queue-pair is a DURABLE OUTBOX, not a
    # delivery tier -- measured 2026-07-29: two messages sat undrained for ~45min because nothing
    # on either device called ReceiveMessage. Every Port-2 property (ACK-as-oracle, breach
    # surfacing, and specifically the LATENCY case that carried the ratification) presupposes a
    # poller. The transport was never the critical path; this is.
    #
    # RUN IT UNDER THE MONITOR TOOL (persistent: true), never Bash run_in_background -- the Bash
    # tool only notifies on EXIT and this never exits, so you would go silent. Same rule, same
    # reason, as org/mcp/inbox-watch.sh stream mode.
    #
    # ORDERING IS LOAD-BEARING: emit THEN delete. inbox-watch.sh's orphan-thief bug is the
    # inverse (mv to read/ at :120 BEFORE echo at :124), so a dead consumer eats mail while every
    # probe reads healthy. Here, a death between emit and delete redelivers after the visibility
    # timeout -- a DUPLICATE, not a LOSS. Always fail toward the duplicate.
    #
    # SCOPE: this is session-bound wherever you run it. It dies with the session, exactly like the
    # inbox Monitor, and must be re-armed next session. A durable consumer is a separate decision
    # (a service/scheduled task on each device) and is NOT this.
    dev="${1:?usage: watch <laptop|sitez>   # the device you ARE, i.e. the queue addressed TO you}"
    q="$(queue_for "$dev")"
    echo "agentbus-sqs: watching ${dev} inbound (long-poll 20s). Emits one line per message; silent otherwise." >&2
    while true; do
        set +e
        out=$(aws sqs receive-message --region "$REGION" --queue-url "$q" \
                --wait-time-seconds 20 --max-number-of-messages 10 \
                --message-attribute-names All 2>&1)
        rc=$?
        set -e
        if [ $rc -ne 0 ]; then
            # LOUD, and never silently retried into looking like an empty queue.
            echo "[agentbus] RECV ERROR rc=${rc} -- this is NOT an empty queue: $(printf '%s' "$out" | tr '\n' ' ' | cut -c1-160)"
            sleep 60
            continue
        fi
        if printf '%s' "$out" | grep -q '"Messages"'; then
            printf '%s' "$out" | grep -o '"Body": "[^"]*"' | cut -d'"' -f4 | while read -r b; do
                echo "[AGENTBUS -> ${dev}] ${b}"
            done
            printf '%s' "$out" | grep -o '"ReceiptHandle": "[^"]*"' | cut -d'"' -f4 | while read -r rh; do
                aws sqs delete-message --region "$REGION" --queue-url "$q" --receipt-handle "$rh" >/dev/null 2>&1 || true
            done
        fi
    done
    ;;

  peek)
    dev="${1:?usage: peek <laptop|sitez>}"
    aws sqs get-queue-attributes --region "$REGION" --queue-url "$(queue_for "$dev")" \
        --attribute-names ApproximateNumberOfMessages ApproximateNumberOfMessagesNotVisible
    echo "NOTE: depth is a PRODUCER-SIDE signal. It cannot distinguish read from discarded."
    ;;

  *)
    grep '^#' "$0" | sed 's/^# \{0,1\}//' | head -40
    exit 2
    ;;
esac
