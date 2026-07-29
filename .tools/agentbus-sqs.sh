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
# TRANSPORT NOTE: SQS *IS* Port 2's ratified transport. eff96f5079 is the commit that CHANGED
# it from the 07-17 DynamoDB draft ("THE RATIFIED DESIGN IS NOT THE DRAFTED ONE ... Ratified
# shape = SQS FIFO queue-pair"), and NFRA_AGENTBUS_PRD.md Amendment B (@0e546bd1d, LD-0347)
# corrected the stale DynamoDB cell to match. These queues are the design, not a substitution.
#
# THIS PARAGRAPH PREVIOUSLY SAID THE OPPOSITE -- "a sovereign substitution, not a PRD amendment
# -- the PRD has not been amended" -- and it survived ~90 minutes AFTER Amendment B landed,
# inside the very tool the amendment is about. Caught by 1.0.0_SA_CTO (base), not by me. It is
# the third instance in one day of the same class: LD-0306's decision_summary outliving its own
# ratification, the PRD's A.0/O-4 cells reading "awaiting ratification" for ~6h after the yes,
# and now this header. THE LESSON IS NOT "READ MORE CAREFULLY" -- it is that a claim about a
# document's state, written into a DIFFERENT artifact, has no mechanism keeping it true. Prefer
# citing the governing record over restating its content; when you must restate it, expect to
# be the one who goes stale.
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

# WHICH DEVICE AM I? -- MEASURED, never assumed, and it is the load-bearing question here.
#
# Arming a consumer for the WRONG device is not a harmless mistake: it drains the OTHER
# machine's mail into a session that is not its recipient. That is the orphan-thief pattern
# (org/mcp/inbox-watch.sh, LD-0271) with a queue in place of an inbox -- the victim's queue goes
# to depth 0, every producer-side probe reads healthy, and the mail is simply gone. `watch` and
# `recv` therefore DEFAULT to the measured device and refuse the other one without an explicit,
# stated override.
#
# The discriminator is the workspace path's user component, because the two checkouts live under
# different Windows profiles. Deliberately NOT the agent serial: a ~Z suffix is an attribution
# convention, not a device fact, and base-serial agents run on site Z too (1.0.0_SA_CTO~Z is a
# lane, but nothing stops a bare serial from being launched here).
this_device() {
    if [ -n "${AGENTBUS_DEVICE:-}" ]; then
        case "$AGENTBUS_DEVICE" in
            laptop|sitez) echo "$AGENTBUS_DEVICE"; return 0 ;;
            *) echo "agentbus-sqs: AGENTBUS_DEVICE='$AGENTBUS_DEVICE' is not laptop|sitez" >&2; exit 2 ;;
        esac
    fi
    root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." 2>/dev/null && pwd)"
    case "$root" in
        *Opal?Bloomberg*|*OPALBL~1*) echo sitez ;;
        *AndrewBerman*|*ANDREW~1*)   echo laptop ;;
        *) echo "UNKNOWN" ;;
    esac
}

# Guard: refuse to act on a device that is not this one unless the caller says so out loud.
assert_own_device() {
    want="$1"; me="$(this_device)"
    if [ "$me" = "UNKNOWN" ]; then
        echo "agentbus-sqs: CANNOT RESOLVE THIS DEVICE from the workspace path." >&2
        echo "  Set AGENTBUS_DEVICE=laptop|sitez explicitly. Refusing to guess -- guessing wrong" >&2
        echo "  drains the other machine's mail (the orphan-thief pattern)." >&2
        exit 2
    fi
    if [ "$want" != "$me" ]; then
        echo "agentbus-sqs: REFUSING -- you asked to consume '${want}' mail but this device is '${me}'." >&2
        echo "  Draining another device's queue makes its mail vanish while every producer-side" >&2
        echo "  probe still reads healthy. If you genuinely mean it (e.g. recovering a dead peer)," >&2
        echo "  re-run with AGENTBUS_DEVICE=${want} and say why in your log." >&2
        exit 2
    fi
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
    # Device arg is OPTIONAL and defaults to this machine. Only consume $1 if it actually names
    # a device -- otherwise `recv --keep` would read "--keep" as the device.
    case "${1:-}" in
        laptop|sitez) dev="$1"; shift ;;
        *)            dev="$(this_device)" ;;
    esac
    assert_own_device "$dev"
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
    dev="${1:-$(this_device)}"        # defaults to THIS device -- you should not have to know
    assert_own_device "$dev"
    q="$(queue_for "$dev")"

    # SINGLE-CONSUMER GUARD (added 2026-07-29 on 1.0.0_SA_CTO~Z's finding; PRD B.4a).
    #
    # SQS DELIVERS EXACTLY-ONCE, SO A SECOND CONSUMER ON THIS QUEUE DOES NOT DUPLICATE MAIL --
    # IT STEALS IT. Each message goes to whichever receiver wins the race, arbitrarily, and the
    # losing session sees NOTHING: no error, no gap, no trace. That is strictly worse than the
    # /watcher double-arm race it resembles, because a race duplicates while this one silently
    # partitions an agent's inbox between two sessions.
    #
    # This was a live near-miss, not a hypothetical: /agentbus's own usage line invites every
    # agent to arm a consumer at session start, and CTO~Z read that, recognised the trap, and
    # deliberately did NOT run the skill -- which is the only reason site Z still has one
    # consumer lineage. A skill that depends on its reader spotting a flaw in its own
    # instructions is not a control. So the refusal lives HERE, where it fires at violation
    # time, instead of in prose that taxes every reader forever.
    #
    # A LOCKFILE, DELIBERATELY NOT `ps` PARSING. CTO~Z produced two bogus orphan verdicts today
    # parsing `ps -ef` by field position, because this box's UID column is "Opal Bloomberg" --
    # WITH A SPACE -- so $2/$3 silently yields "pid=Blo". A PID file plus `kill -0` asks the
    # kernel a question with one right answer and no field positions to get wrong. Stale locks
    # self-clear: if the recorded PID is dead, we take the lock.
    LOCK="/tmp/agentbus-consumer-${dev}.lock"
    if [ -f "$LOCK" ]; then
        other=$(cat "$LOCK" 2>/dev/null || echo "")
        if [ -n "$other" ] && kill -0 "$other" 2>/dev/null; then
            echo "agentbus-sqs: REFUSING -- a consumer for '${dev}' is ALREADY RUNNING (pid ${other})." >&2
            echo "  SQS is exactly-once: a second consumer would STEAL this device's mail at random," >&2
            echo "  with no trace on the losing side. This is not a duplicate-delivery race." >&2
            echo "  If that consumer is dead, its lock self-clears -- re-run and you will take it." >&2
            echo "  To hand over deliberately: stop the other Monitor first, then re-run." >&2
            exit 3
        fi
        echo "agentbus-sqs: stale lock for pid ${other:-?} (process gone) -- taking it." >&2
    fi
    echo $$ > "$LOCK"
    # Release on any exit path so a clean stop never leaves a lock that blocks the next session.
    trap 'rm -f "$LOCK" 2>/dev/null || true' EXIT INT TERM
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
            # EMIT THE MessageId WITH THE BODY. The first version emitted the body alone, and
            # that is not cosmetic: Rule 22b's ONLY delivery oracle is an ack NAMING the
            # MessageId, so a consumer that hides the id STRUCTURALLY PREVENTS THE DISCIPLINE
            # THIS TOOL PREACHES. Caught live -- 1.0.0_SA_CTO~Z could not close verification
            # leg (b) because it held no id for a message my consumer had genuinely delivered.
            # The tool enforced an ack rule while withholding the one field an ack requires.
            #
            # Paired via jq, not two greps: grep -o over Body and MessageId separately yields two
            # INDEPENDENT lists, and pairing them by position is an assumption about AWS's field
            # ordering that would mis-attribute ids to bodies on any multi-message receive --
            # silently, and worst exactly when traffic is heaviest. jq keeps each pair together
            # because it parses the structure instead of the text.
            if command -v jq >/dev/null 2>&1; then
                printf '%s' "$out" | jq -r '.Messages[] | "[AGENTBUS -> '"${dev}"'] [id \(.MessageId)] \(.Body)"'
            else
                # Fail LOUD rather than silently degrading to an id-less emit -- an emit without
                # an id looks like a delivery and cannot be acked, which is worse than no emit.
                echo "[agentbus] ERROR: jq absent -- cannot emit MessageId with body. Ack discipline (Rule 22b) is unsatisfiable without it. Install jq or run 'recv --keep' by hand."
            fi
            printf '%s' "$out" | grep -o '"ReceiptHandle": "[^"]*"' | cut -d'"' -f4 | while read -r rh; do
                aws sqs delete-message --region "$REGION" --queue-url "$q" --receipt-handle "$rh" >/dev/null 2>&1 || true
            done
        fi
    done
    ;;

  device)
    # Answers "which machine am I?" so a caller never has to guess. Prints the resolution basis
    # too -- a bare answer with no basis is the kind of unfalsifiable output this estate keeps
    # getting burned by.
    me="$(this_device)"
    echo "device: ${me}"
    echo "  basis: $([ -n "${AGENTBUS_DEVICE:-}" ] && echo "AGENTBUS_DEVICE override" || echo "workspace path")"
    echo "  root:  $(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
    if [ "$me" = "UNKNOWN" ]; then
        echo "  -> UNRESOLVED. Set AGENTBUS_DEVICE=laptop|sitez. Refusing to guess is deliberate." >&2
        exit 2
    fi
    echo "  my inbound queue: $(queue_for "$me")"
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
