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
#     bash .tools/agentbus-sqs.sh watch             # on every box: it targets THIS box's own queue
#     bash .tools/agentbus-sqs.sh watch <this-device>   # the same, named; refused if it is not this box
# WITHOUT A WATCHER ON A DEVICE, MAIL TO THAT DEVICE IS NOT DELIVERED -- it accumulates. `send`
# returning a MessageId means STORED, never DELIVERED. Verified live 2026-07-29: site-Z watcher
# armed and exercised end-to-end; laptop side pending Andrew's word.
#
#   <device> is a box the device register lists (`agentbus-sqs.sh devices` prints the set, org/devices/DEVICES.json
#   holds it). `send <box>` puts a message on the queue THAT box drains; `recv <box>` drains the queue addressed TO that box.
#
# ACK DISCIPLINE (CLAUDE.md Rule 22b -- SENT IS NOT READ). A successful send returns a
# MessageId. THAT IS NOT DELIVERY. It is not delivered until the receiving agent emits
# an ACK naming that MessageId. `recv` prints the MessageId of everything it hands you
# precisely so you can ack it; a transport-side signal (SendMessage 200, a CloudWatch
# count, a queue depth of 0) is NEVER delivery evidence. A depth of 0 is equally
# consistent with "read" and "drained by something that discarded it".

set -euo pipefail

# A NON-ASCII BYTE IN A PEER'S MESSAGE MUST NOT BE ABLE TO TAKE DOWN THE CHANNEL.
# (measured 2026-08-13, root cause of two deafness windows in one session)
#
# Every path in this file that prints a message body does it through a python
# stdout -- the exec'd agentbus-consumer.py on the `watch` path, and the AWS CLI
# (itself python) on `recv` and the aws-CLI fallback loop. On Windows that stdout
# defaults to cp1252, so ONE U+26A0 in a body raised UnicodeEncodeError and killed
# the reader. On `recv` it surfaced as the loud, misleading
#   "aws sqs receive-message FAILED (rc=255) -- this is NOT an empty queue"
# with the real cause ('charmap' codec can't encode ...) buried in the dump; on
# `watch` it was SILENT -- the consumer died and the Monitor wrapper kept
# reporting running.
#
# EXPORTED, NOT SET PER-CALL, DELIBERATELY: it must reach the exec'd consumer, the
# CLI, and anything either of them spawns. One missed call site reopens the class.
# Senders must still keep bodies ASCII (CLAUDE.md: "No emojis (no non-ASCII) ...
# breaks CloudWatch/charmap") -- but that rule cannot be the control, because it
# depends on every peer remembering. This is the control.
export PYTHONIOENCODING=utf-8

ACCOUNT=313476888478
REGION=us-east-1
QUEUE_BASE="https://sqs.${REGION}.amazonaws.com/${ACCOUNT}"

# THE DEVICE REGISTER (NFRA_CTLPLN FWD-2, C-REGISTRY): every box -- its name, aliases and inbound
# queue -- is read from org/devices/DEVICES.json through its one reader, lib/devices.py. A box is
# added there once; nothing in this file lists boxes. Fail-closed: no python or an unreadable
# register refuses loudly (rc 3), never a built-in list.
_devices() {
    local _root _p
    _root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." 2>/dev/null && pwd)"
    for _p in python python3; do
        if command -v "$_p" >/dev/null 2>&1; then
            "$_p" "$_root/lib/devices.py" "$@" | tr -d '\r'
            return "${PIPESTATUS[0]}"
        fi
    done
    echo "agentbus-sqs: no python to read the device register (lib/devices.py) -- refusing" >&2
    return 3
}

queue_for() {
    local q
    q="$(_devices queue "$1")" || {
        echo "agentbus-sqs: unknown device '$1' (register holds: $(_devices names | tr '\n' ' '))" >&2; exit 2; }
    echo "${QUEUE_BASE}/${q}"   # the box's INBOUND queue: the queue it drains
}

# --- THE DECLARED DEVICE SET (RV-0058 F-004) ------------------------------------------------------
# WHY THIS EXISTS, and it is a governance need rather than a transport one: /mstr-review's READER
# GUARD (RV-0057 F-001 item 1) must print WHICH DECLARED DEVICES it did not walk, and refuse a
# fabric-wide count when it walked fewer than all of them. Until this accessor, the device set was
# enumerated ONLY inside this transport tool -- three times (queue_for's labels above, the
# AGENTBUS_DEVICE validation in this_device, and the workspace-path patterns) -- and NOTHING a
# governance instrument could read. So a reviewer had to HAND-COPY "[laptop, sitez]" into the review.
#
# THAT IS THE HAND-COPIED-LIST CLASS org/XXX.md A.3 RECORDS TWICE (its remedy line named three tools
# and went stale the same day; its counts froze and drifted within one day). A guard whose DENOMINATOR
# is hand-copied under-reports exactly the gap it exists to surface: add a third device and the guard
# still prints a complete-looking two-device set, silently. That is the guard's own failure mode one
# level up, which is why the fix is derivation and not a fourth copy of the list.
#
# READ FROM THE DEVICE REGISTER (NFRA_CTLPLN FWD-2): the same register queue_for reads, through
# lib/devices.py, so the declared set and the queue map cannot disagree, and a box added to
# org/devices/DEVICES.json is picked up here with no edit to this file.
declared_devices() {
    _devices names
}

# --- THE TAILNET STAMP (NFRA_CTLPLN FWD-3, C-BUS; CTO msg 105932 on Andrew's word "the tailnet name is the
# real identifier") ---------------------------------------------------------------------------------------
# Every message carries the sender's and the recipient's TAILNET NAME (register field `tailnet_name`, the
# MagicDNS name), as SQS message attributes AND in the body envelope beside the serial. The names are read
# from the device register through lib/devices.py (OPAL_DEVICE_REGISTER honoured) and never typed here.
#   _tailnet of <label>   -> the tailnet name of the box a name or alias resolves to (rc 2 unknown/none)
#   _tailnet all          -> every tailnet name the register holds (boxes, then sender-only `senders`), one per line
# Fail-closed like _devices: no python or an unreadable register is rc 3, never a built-in list.
_tailnet() {
    local _root _p
    _root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." 2>/dev/null && pwd)"
    for _p in python python3; do
        if command -v "$_p" >/dev/null 2>&1; then
            "$_p" -c '
import sys
sys.path.insert(0, sys.argv[1] + "/lib")
import devices
mode = sys.argv[2]
try:
    reg = devices.load()
except devices.RegisterError as exc:
    print(str(exc), file=sys.stderr)
    sys.exit(3)
if mode == "all":
    print("\n".join(devices.held_tailnet_names(reg)))
    sys.exit(0)
canon = devices.resolve(sys.argv[3], reg)
for d in devices.devices(reg):
    if d["name"] == canon and d.get("tailnet_name"):
        print(d["tailnet_name"])
        sys.exit(0)
sys.exit(2)
' "$_root" "$@" | tr -d '\r'
            return "${PIPESTATUS[0]}"
        fi
    done
    echo "agentbus-sqs: no python to read the device register (lib/devices.py) -- refusing" >&2
    return 3
}

# RECEIVE-SIDE REFUSAL (AMENDMENT 2, rows W3-S2/W3-S3). Input: the receive-message JSON in $1, the queue URL in $q.
# Sets DELIVER_JSON to the same JSON holding only the messages to deliver, and REFUSED_N to the count refused.
#   - sender tailnet name (attribute from_tailnet) HELD by the register  -> delivered.
#   - NO from_tailnet stamp (a box still running the old script)         -> delivered, with one line
#       WARN agentbus unstamped sender=<serial>      (until every box sends stamped; strict refusal is a later flip)
#   - a stamped name the register does NOT hold                          -> REFUSED: the whole message (body and
#       attributes) is written to ${AGENTBUS_REFUSED_DIR:-org/mcp/inbox/_agentbus_refused}/<UTC stamp>_<message id>.json,
#       one line  REFUSED agentbus sender_tailnet=<name> reason=<why> record=<path>  is printed, and only THEN is the
#       message DELETED from the queue so it can never block the one-group FIFO. Recorded, never silently dropped:
#       a record that cannot be written leaves the message on the queue.
# The consumer (agentbus-consumer.py) applies the same rule and reads the register the same way (lib/devices.py).
# Fail closed: without a resolvable jq, or with an unreadable register, the check cannot be made, so EVERY message is
# withheld (not delivered, and NOT deleted -- there is nothing to record a judgement on).
partition_by_sender() {
    local json="$1" held rdir stamp
    DELIVER_JSON=""; REFUSED_N=0
    if [ -z "$JQ" ]; then
        REFUSED_N="$(printf '%s' "$json" | grep -o '"MessageId"' | wc -l | tr -d ' ')"
        echo "[agentbus] WITHHELD ${REFUSED_N} message(s): no jq resolvable, so the sender tailnet name cannot be checked against the register -- NOT delivered, NOT deleted; they remain on the queue."
        return 0
    fi
    held="$(_tailnet all | "$JQ" -R . | "$JQ" -s -c .)" || {
        echo "[agentbus] WITHHELD ALL: the device register's tailnet names could not be read -- NOT delivered, NOT deleted." >&2
        REFUSED_N="$(printf '%s' "$json" | "$JQ" '.Messages | length' | tr -d '')"; return 0; }
    rdir="${AGENTBUS_REFUSED_DIR:-${_jq_self_dir}/../org/mcp/inbox/_agentbus_refused}"
    # unstamped mail: delivered with a WARN naming the serial
    printf '%s' "$json" | "$JQ" -r '.Messages[] | select((.MessageAttributes.from_tailnet.StringValue // "") == "")
         | "WARN agentbus unstamped sender=" + (.MessageAttributes.from.StringValue // "unknown")' | tr -d ''
    REFUSED_N="$(printf '%s' "$json" | "$JQ" --argjson held "$held"         '[.Messages[] | (.MessageAttributes.from_tailnet.StringValue // "") as $t | select($t != "" and (($held | index($t)) == null))] | length' | tr -d '')"
    if [ "$REFUSED_N" -gt 0 ]; then
        mkdir -p "$rdir"
        stamp="$(date -u +%Y%m%dT%H%M%SZ)"
        printf '%s' "$json" | "$JQ" -c --argjson held "$held"             '.Messages[] | (.MessageAttributes.from_tailnet.StringValue // "") as $t | select($t != "" and (($held | index($t)) == null))'             | tr -d '' | while read -r m; do
            local mid tn rh rec
            mid="$(printf '%s' "$m" | "$JQ" -r .MessageId | tr -d '')"
            tn="$(printf '%s' "$m" | "$JQ" -r '.MessageAttributes.from_tailnet.StringValue' | tr -d '')"
            rh="$(printf '%s' "$m" | "$JQ" -r '.ReceiptHandle // ""' | tr -d '')"
            rec="${rdir}/${stamp}_${mid}.json"
            if printf '%s' "$m" | "$JQ" --arg at "$stamp" --arg tn "$tn"                 '{refused_at: $at, sender_tailnet: $tn, reason: "sender tailnet name not held by the device register", message: .}' > "$rec"; then
                echo "REFUSED agentbus sender_tailnet=${tn} reason=not-held-by-the-device-register record=${rec}"
                aws sqs delete-message --region "$REGION" --queue-url "$q" --receipt-handle "$rh" >/dev/null 2>&1                     || echo "[agentbus] WARN: the refused message ${mid} was recorded but its delete FAILED; it will redeliver and be refused again."
            else
                echo "[agentbus] REFUSED [id ${mid}] sender tailnet name [${tn}] but the record could not be written to ${rec} -- NOT deleted; it remains on the queue."
            fi
        done
    fi
    DELIVER_JSON="$(printf '%s' "$json" | "$JQ" -c --argjson held "$held"         '.Messages |= map(select(((.MessageAttributes.from_tailnet.StringValue // "") as $t | ($t == "" or (($held | index($t)) != null)))))')"
}

# --- JQ RESOLUTION (NFRA_TOOLARCH.PATHFIX) --------------------------------------------------------
# RESOLVE THE TRACKED BINARY, NEVER THE BARE NAME. `command -v jq` FAILS IN EVERY HARNESS SHELL --
# they are non-interactive, source no profile, and so never put .tools on PATH. That made the
# jq-absent fallback below not a rare degraded path but THE LIVE PATH on this device, which is how a
# text-parsing fallback nobody expected to run got to destroy real mail.
#
# `.tools/jq.exe` is TRACKED and present (jq-1.7.1). Deriving it from this script's own location is
# the same rule already applied to the comp-* tools, and it is strictly better than hardening the
# fallback because it means the fallback NEVER EXECUTES.
#
# Measured 2026-07-29 by 1.0.0_SA_CTO~B, reproducing 0.0.0_AB_MSTR's report rather than trusting it:
#   command -v jq            -> NOT FOUND (this harness shell)
#   .tools/jq.exe --version  -> jq-1.7.1
JQ=""
_jq_self_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ -x "${_jq_self_dir}/jq.exe" ]; then
    JQ="${_jq_self_dir}/jq.exe"
elif [ -x "${_jq_self_dir}/jq" ]; then
    JQ="${_jq_self_dir}/jq"
elif command -v jq >/dev/null 2>&1; then
    JQ="$(command -v jq)"
fi

# WHICH DEVICE AM I? -- MEASURED, never assumed, and it is the load-bearing question here.
#
# Arming a consumer for the WRONG device is not a harmless mistake: it drains the OTHER
# machine's mail into a session that is not its recipient. That is the orphan-thief pattern
# (org/mcp/inbox-watch.sh, LD-0271) with a queue in place of an inbox -- the victim's queue goes
# to depth 0, every producer-side probe reads healthy, and the mail is simply gone. `watch` and
# `recv` therefore DEFAULT to the measured device and refuse the other one without an explicit,
# stated override.
#
# The discriminator is the box's own setting, AGENTBUS_DEVICE, made once at bring-up as a user
# environment variable and resolved through the device register (NFRA_CTLPLN C-REGISTRY). Never the
# workspace path (LD-0405; the path fallback was dropped on 1.0.0_SA_CTO msg 105622 once both boxes
# read the setting back) and never the agent serial (a ~Z suffix is attribution, not a device fact).
# A process started BEFORE the setting was made lacks it in its environment, so the persisted user
# setting (HKCU\Environment) is read next; it is the same setting, not a derivation. Neither present
# -> UNKNOWN plus a loud line on stderr; every caller refuses on UNKNOWN.
device_setting() {
    if [ -n "${AGENTBUS_DEVICE:-}" ]; then
        echo "${AGENTBUS_DEVICE}"; echo "AGENTBUS_DEVICE (process environment)" >&3; return 0
    fi
    local key="${AGENTBUS_REG_KEY:-HKCU\\Environment}" out
    if command -v reg >/dev/null 2>&1; then
        out="$(MSYS_NO_PATHCONV=1 reg query "$key" /v AGENTBUS_DEVICE 2>&1 | tr -d '\r')"
        out="$(echo "$out" | awk '$1=="AGENTBUS_DEVICE" && $2 ~ /^REG_(EXPAND_)?SZ$/ {print $3}')"
        if [ -n "$out" ]; then
            echo "$out"; echo "AGENTBUS_DEVICE (persisted user setting, $key)" >&3; return 0
        fi
    fi
    return 1
}

this_device() {
    local claim canon
    if ! claim="$(device_setting 3>/dev/null)"; then
        echo "agentbus-sqs: AGENTBUS_DEVICE is not set (process environment or persisted user setting) --" \
             "set it once at bring-up to a device in org/devices/DEVICES.json; refusing to derive it from a path" >&2
        echo "UNKNOWN"; return 0
    fi
    if canon="$(_devices resolve "$claim")"; then echo "$canon"; return 0; fi
    echo "agentbus-sqs: AGENTBUS_DEVICE='$claim' is not in the device register ($(_devices names | tr '\n' ' '))" >&2
    exit 2
}

# Guard: refuse to act on a device that is not this one unless the caller says so out loud.
assert_own_device() {
    want="$1"; me="$(this_device)"
    if [ "$me" = "UNKNOWN" ]; then
        echo "agentbus-sqs: CANNOT RESOLVE THIS DEVICE: AGENTBUS_DEVICE is not set." >&2
        echo "  Set it to one of: $(_devices names | tr '\n' ' '). Refusing to guess -- guessing wrong" >&2
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
    to="${1:?usage: send <to-device> <from-serial> <body...>}"; shift
    from="${1:?usage: send <to-device> <from-serial> <body...>}"; shift
    body="$*"
    [ -n "$body" ] || { echo "agentbus-sqs: refusing to send an empty body" >&2; exit 2; }
    ts="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    # THE TAILNET STAMP (see _tailnet above): the sender's box is this device (AGENTBUS_DEVICE through the
    # register), the recipient's is the box named by <to>; both names come from the register's tailnet_name.
    me="$(this_device)"
    if [ -z "$me" ] || [ "$me" = "UNKNOWN" ]; then
        echo "agentbus-sqs: REFUSING to send -- this box is unresolved, so the sender's tailnet name cannot be stamped (set AGENTBUS_DEVICE)." >&2
        exit 2
    fi
    from_tn="$(_tailnet of "$me")" || { echo "agentbus-sqs: REFUSING to send -- the register holds no tailnet_name for sender box '${me}'." >&2; exit 2; }
    to_tn="$(_tailnet of "$to")" || { echo "agentbus-sqs: REFUSING to send -- the register holds no tailnet_name for recipient '${to}'." >&2; exit 2; }
    # MessageGroupId is REQUIRED on a FIFO queue. One group keeps global ordering across
    # the channel; switch to a per-conversation group if strict ordering per thread is
    # wanted and cross-thread head-of-line blocking becomes a problem.
    out=$(aws sqs send-message --region "$REGION" --queue-url "$(queue_for "$to")" \
        --message-group-id opal-sqschat \
        --message-attributes "from={StringValue=${from},DataType=String},sent_at={StringValue=${ts},DataType=String},from_tailnet={StringValue=${from_tn},DataType=String},to_tailnet={StringValue=${to_tn},DataType=String}" \
        --message-body "[${ts}] [from ${from}] [tailnet ${from_tn} -> ${to_tn}] ${body}")
    # THE TRUNCATION QUESTION, ANSWERED AND WRITTEN DOWN (0.0.0_AB_MSTR asked for the reason, not
    # just the change): an SQS MessageId is a UUID -- charset [0-9a-f-] -- so it CANNOT contain a
    # quote and the escaped-quote truncation that destroyed message BODIES cannot occur on THIS
    # field. That risk is genuinely nil here. Measured, not assumed.
    #
    # BUT A DIFFERENT AND REAL DEFECT LIVES ON THIS LINE, and it is the third instance of the same
    # class in this file: A FAILED EXTRACTION RENDERED AS A SUCCESSFUL SEND.
    #   extraction yields nothing  ->  mid=""  ->  "SENT to sitez: MessageId="   at rc=0
    # The send genuinely SUCCEEDED -- the message is on the queue -- so this is not a send failure,
    # it is a RECEIPT failure, and the two need different words. Rule 22b's entire ack discipline
    # hangs off that id: an empty one makes the message UNACKABLE, so the sender holds a receipt
    # they cannot use for a message that really was delivered. Empty must be distinguishable from
    # failed (contract C3), and silence is not an option the header contract allows.
    if [ -n "$JQ" ]; then
        mid=$(printf '%s' "$out" | "$JQ" -r '.MessageId // empty')
    else
        mid=$(printf '%s' "$out" | grep -o '"MessageId": "[^"]*"' | cut -d'"' -f4)
    fi
    if [ -z "$mid" ]; then
        echo "SENT to ${to} -- BUT THE MessageId COULD NOT BE READ FROM THE RESPONSE."
        echo "  THE MESSAGE WAS SENT. This is a RECEIPT failure, not a send failure -- do not resend"
        echo "  blindly or you will duplicate it. Rule 22b cannot be satisfied without the id, so"
        echo "  this send is UNACKABLE until the recipient reports what it received."
        echo "  Raw response follows so the id is recoverable by hand:"
        printf '%s\n' "$out" | sed 's/^/    /'
        exit 3
    fi
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
    # RECEIVE-SIDE REFUSAL (see partition_by_sender above): a message from a sender tailnet name the register
    # does not hold is recorded, reported and deleted; unstamped mail is delivered with a WARN.
    partition_by_sender "$out"
    REFUSED_N="${REFUSED_N//$'\r'/}"
    if [ -n "$DELIVER_JSON" ] && [ "$(printf '%s' "$DELIVER_JSON" | "$JQ" '.Messages | length' | tr -d '\r')" -gt 0 ]; then
        out="$DELIVER_JSON"
        printf '%s\n' "$out"
    else
        echo "(no deliverable messages: ${REFUSED_N} refused/withheld above)" >&2
        exit 4
    fi
    if [ "$keep" -eq 1 ]; then
        echo
        echo "--keep: messages NOT deleted; they return to the queue after the visibility timeout."
    else
        # Delete only what we actually received, one handle at a time.
        # STRUCTURAL extraction (see JQ= above): a body containing the literal text
        # '"ReceiptHandle": "..."' would hand a text-grep a phantom handle out of payload content.
        # NOTE this path does NOT share the watch-path truncation bug -- :205 prints the RAW JSON,
        # so nothing here was ever emitted lossily. Verified before changing it, not assumed.
        # With no jq resolvable we do NOT fall back to text-parsing the delete set: we decline to
        # delete and say so, because an unrecoverable operation is the wrong place to guess.
        if [ -n "$JQ" ]; then
            printf '%s' "$out" | "$JQ" -r '.Messages[] | .ReceiptHandle' | while read -r rh; do
                [ -n "$rh" ] || continue
                aws sqs delete-message --region "$REGION" --queue-url "$q" --receipt-handle "$rh" >/dev/null 2>&1 || true
            done
        else
            echo
            echo "WARN: no jq resolvable -- NOT deleting. The messages above were printed in full"
            echo "      (raw JSON), so nothing is lost; they redeliver after the visibility timeout."
            exit 0
        fi
        echo
        echo "Consumed (deleted from queue). ACK each MessageId above to the sender -- deletion is NOT an ack."
    fi
    if [ "$REFUSED_N" -gt 0 ]; then
        echo "agentbus-sqs: ${REFUSED_N} message(s) REFUSED (sender tailnet name not in the register), recorded and removed from the queue." >&2
        exit 4
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
    #
    # ATOMIC ACQUISITION (P1 process GC): the lock is CREATED with noclobber (O_EXCL), so of two simultaneous arms
    # exactly one creates it; the old check-then-write let both start. A stale lock (recorded pid dead) is renamed
    # aside -- a rename succeeds for one racer only -- and the create is retried; losing any step is the rc-3 refusal.
    # AGENTBUS_LOCK overrides the path (tests only).
    LOCK="${AGENTBUS_LOCK:-/tmp/agentbus-consumer-${dev}.lock}"
    _lock_take() { ( set -C; printf '%s\n' "$$" > "$LOCK" ) 2>/dev/null; }
    _lock_read() {   # an empty read may be a racer between create and write: read once more after 1 s
        local o; o="$(cat "$LOCK" 2>/dev/null || true)"
        if [ -z "$o" ] && [ -e "$LOCK" ]; then sleep 1; o="$(cat "$LOCK" 2>/dev/null || true)"; fi
        printf '%s' "$o"
    }
    _lock_refuse() {
        echo "agentbus-sqs: REFUSING -- a consumer for '${dev}' is ALREADY RUNNING (pid ${1:-?})." >&2
        echo "  SQS is exactly-once: a second consumer would STEAL this device's mail at random," >&2
        echo "  with no trace on the losing side. This is not a duplicate-delivery race." >&2
        echo "  If that consumer is dead, its lock self-clears -- re-run and you will take it." >&2
        echo "  To hand over deliberately: stop the other Monitor first, then re-run." >&2
        exit 3
    }
    if ! _lock_take; then
        other="$(_lock_read)"
        if [ -n "$other" ] && kill -0 "$other" 2>/dev/null; then
            _lock_refuse "$other"
        fi
        echo "agentbus-sqs: stale lock for pid ${other:-?} (process gone) -- taking it." >&2
        # ONE racer clears: mkdir is atomic. Under it, remove the lock only if it still holds the dead pid, then
        # take. A racer that cannot get the mutex stands down (rc 3). A mutex left by a crash ages out after 60 s.
        _took=1
        if mkdir "${LOCK}.clearing" 2>/dev/null; then
            if [ "$(_lock_read)" = "$other" ]; then rm -f "$LOCK"; fi
            if _lock_take; then _took=0; fi
            rmdir "${LOCK}.clearing" 2>/dev/null || true
        else
            _age=$(( $(date +%s) - $(stat -c %Y "${LOCK}.clearing" 2>/dev/null || date +%s) ))
            if [ "$_age" -gt 60 ]; then rmdir "${LOCK}.clearing" 2>/dev/null || true; fi
        fi
        [ "$_took" -eq 0 ] || _lock_refuse "$(_lock_read)"
    fi
    # Release on any exit path so a clean stop never leaves a lock that blocks the next session.
    trap 'rm -f "$LOCK" 2>/dev/null || true' EXIT INT TERM
    echo "agentbus-sqs: watching ${dev} inbound (long-poll 20s). Emits one line per message; silent otherwise." >&2
    # NO-SPAWN CONSUMER (Andrew cleanup 2026-07-30): the aws-CLI loop below launches a FULL
    # python interpreter per 20s long-poll (~4,320/day/device, ~1-2s CPU each + the heaviest
    # per-event EDR import scans on the box). One long-lived boto3 daemon holds the same
    # receive->emit-THEN-delete contract with zero per-poll spawns. exec (not spawn) so the
    # MSYS pid in the lockfile stays THIS process and `kill -0` liveness keeps resolving;
    # the python removes the lock on exit (the EXIT trap above does not survive exec, by
    # design). Guarded fallback (Rule 16 pattern): no python/boto3 -> the original aws-CLI
    # loop below runs unchanged. Emit format is CONTRACT in both paths -- acks key on it.
    _PYBIN=""
    for _p in python python3; do
        if command -v "$_p" >/dev/null 2>&1 && "$_p" -c "import boto3" >/dev/null 2>&1; then
            _PYBIN="$_p"; break
        fi
    done
    if [ -n "$_PYBIN" ] && [ -f "${_jq_self_dir}/agentbus-consumer.py" ]; then
        # OWNER TIE (P1 process GC): $PPID here is 1 -- the harness's top process (Git\bin\bash.exe) is not an MSYS
        # process -- so the owner is resolved on the WINDOWS chain from this process's winpid: the topmost bash.exe
        # above it (what the Monitor stop kills) and that process's parent (the session). The consumer exits when
        # either exits. Empty resolution = no --owner-winpid = the consumer's cap-only behaviour (fail open).
        _owner_args=()
        _selfwin="$(cat "/proc/$$/winpid" 2>/dev/null || true)"
        if [ -n "$_selfwin" ]; then
            for _o in $("$_PYBIN" "${_jq_self_dir}/agentbus-consumer.py" --resolve-owners "$_selfwin" | tr -d '\r' || true); do
                _owner_args+=(--owner-winpid "$_o")
            done
        fi
        exec "$_PYBIN" "${_jq_self_dir}/agentbus-consumer.py" \
            --queue-url "$q" --device "$dev" --region "$REGION" \
            --lock "$LOCK" --lock-pid "$$" "${_owner_args[@]}"
    fi
    echo "agentbus-sqs: python/boto3 unavailable -- falling back to the per-poll aws-CLI loop" >&2
    # BOUNDED like the python consumer (1700 s, AGENTBUS_MAX_SECONDS overrides, 0 disables): an unbounded loop
    # outlives its Monitor and holds the lock. $SECONDS is bash's own clock -- no extra process per pass.
    _max_s="${AGENTBUS_MAX_SECONDS:-1700}"
    SECONDS=0
    while [ "$_max_s" -eq 0 ] || [ "$SECONDS" -lt "$_max_s" ]; do
        set +e
        out=$(aws sqs receive-message --region "$REGION" --queue-url "$q" \
                --wait-time-seconds 20 --max-number-of-messages 10 \
                --message-attribute-names All 2>&1)
        rc=$?
        set -e
        if [ $rc -ne 0 ]; then
            # LOUD, and never silently retried into looking like an empty queue.
            echo "[agentbus] RECV ERROR rc=${rc} -- this is NOT an empty queue: $(printf '%s' "$out" | tr '\n' ' ' | cut -c1-160)"
            _left=60
            if [ "$_max_s" -gt 0 ] && [ $((_max_s - SECONDS)) -lt 60 ]; then _left=$((_max_s - SECONDS)); fi
            [ "$_left" -gt 0 ] && sleep "$_left"
            continue
        fi
        if printf '%s' "$out" | grep -q '"Messages"'; then
            # RECEIVE-SIDE REFUSAL (partition_by_sender): a message whose sender tailnet name the register
            # does not hold is recorded, reported and deleted (partition_by_sender). This loop is the aws-CLI fallback;
            # the boto3 consumer (agentbus-consumer.py) is the primary watch path.
            partition_by_sender "$out"
            REFUSED_N="${REFUSED_N//$'\r'/}"
            out="$DELIVER_JSON"
            if [ -z "$out" ] || [ "$(printf '%s' "$out" | "$JQ" '.Messages | length' | tr -d '\r')" -eq 0 ]; then
                sleep 5
                continue
            fi
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
            # DELETE IS GATED ON A SUCCESSFUL EMIT. NEVER UNCONDITIONAL.
            #
            # DATA-LOSS BUG, shipped in the id-emit build and caught by 0.0.0_AB_MSTR on the
            # laptop within minutes: the delete loop sat OUTSIDE this branch, so on a box with no
            # jq the consumer printed an ERROR *about* the message, emitted nothing, and DELETED
            # IT ANYWAY. At least one message addressed to the laptop was permanently lost.
            # The file's own stated invariant is "emit THEN delete ... always fail toward the
            # duplicate" -- I wrote that paragraph and then broke it in this function, because
            # the failure branch handled the FORMATTING failure and forgot it still held an
            # undelivered MESSAGE. A guard placed outside the branch it guards is not a guard.
            # SECOND DATA-LOSS BUG, in the FALLBACK that the first fix left standing. Reported by
            # 0.0.0_AB_MSTR 165356Z, independently reproduced here before touching anything:
            #
            #   grep -o '"Body": "[^"]*"'  STOPS AT THE FIRST ESCAPED QUOTE.
            #     body: Andrew said \"stop\" and more text after
            #     got:  Andrew said \                        <- rest silently gone, then DELETED
            #
            # It emitted a FRAGMENT, so emitted=1, so the message was deleted and the remainder was
            # unrecoverable. WORSE THAN THE BUG IT REPLACED, because a truncated line looks like a
            # delivery instead of an error. And the traffic on this bus is largely VERBATIM ANDREW
            # QUOTES -- which contain quote characters BY DEFINITION -- so it fired on close to
            # every message that matters most.
            #
            # Independent second defect, same block: `grep | cut | while` exits 0 even when the
            # while body runs ZERO times, so a total extraction failure also set emitted=1 and
            # deleted. The guard could not tell "emitted successfully" from "emitted nothing".
            #
            # THE FIX IS RESOLUTION, NOT HARDENING (see JQ= above): with the tracked jq resolved,
            # this fallback never runs. It is kept only for a box with no jq at all -- and it is
            # now structurally incapable of losing anything, because IT NEVER DELETES. A duplicate
            # is recoverable; a deletion is not. That is this file's own stated invariant, applied
            # to the branch that kept violating it.
            emitted=0
            if [ -n "$JQ" ]; then
                if printf '%s' "$out" | "$JQ" -r '.Messages[] | "[AGENTBUS -> '"${dev}"'] [id \(.MessageId)] \(.Body)"'; then
                    emitted=1
                fi
            else
                # DEGRADE, NEVER DROP -- and "never drop" now means never delete, not merely
                # "print something first". An id-less, possibly-truncated emit is a REDELIVERY
                # PROMPT, not a delivery.
                echo "[agentbus] WARN: no jq resolvable (tracked .tools/jq.exe absent AND no jq on PATH)."
                echo "[agentbus] Emitting BEST-EFFORT text extraction, which MAY TRUNCATE at an escaped quote."
                echo "[agentbus] NOTHING WILL BE DELETED on this path -- messages redeliver until a real jq is present."
                printf '%s' "$out" | grep -o '"Body": "[^"]*"' | cut -d'"' -f4 | while read -r b; do
                    echo "[AGENTBUS -> ${dev}] [id UNAVAILABLE] [POSSIBLY TRUNCATED] ${b}"
                done
                emitted=0
            fi
            if [ "$emitted" -eq 1 ]; then
                # ReceiptHandles are extracted STRUCTURALLY, for the same reason bodies are: a
                # message whose body contains the literal text '"ReceiptHandle": "..."' would hand
                # a text-grep a PHANTOM handle out of attacker-or-accident-controlled content.
                # Parsing the structure cannot be fooled by the payload.
                printf '%s' "$out" | "$JQ" -r '.Messages[] | .ReceiptHandle' | while read -r rh; do
                    [ -n "$rh" ] || continue
                    aws sqs delete-message --region "$REGION" --queue-url "$q" --receipt-handle "$rh" >/dev/null 2>&1 || true
                done
            else
                # Not deleted -> becomes visible again after the visibility timeout and is
                # redelivered. A duplicate is recoverable; a deletion is not.
                echo "[agentbus] NOT DELETED -- emit failed, message left on the queue for redelivery."
            fi
        fi
    done
    echo "[AGENTBUS-EXPIRED] aws-CLI fallback consumer for ${dev} ended after ${_max_s}s (Monitors die at 30 min). RE-ARM with ONE Monitor call: cd <workspace-root> && exec bash .tools/agentbus-sqs.sh watch"
    exit 0
    ;;

  device)
    # Answers "which machine am I?" so a caller never has to guess. Prints the resolution basis
    # too -- a bare answer with no basis is the kind of unfalsifiable output this estate keeps
    # getting burned by.
    me="$(this_device)"
    echo "device: ${me}"
    echo "  basis: $(device_setting 3>&1 >/dev/null || echo "none")"
    echo "  root:  $(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
    if [ "$me" = "UNKNOWN" ]; then
        echo "  -> UNRESOLVED. Set AGENTBUS_DEVICE to a device in org/devices/DEVICES.json ($(_devices names | tr '\n' ' ')). Refusing to guess is deliberate." >&2
        exit 2
    fi
    echo "  my inbound queue: $(queue_for "$me")"
    ;;

  devices)
    # THE DECLARED DEVICE SET, for /mstr-review's READER GUARD (RV-0058 F-004).
    # Prints the set AND EXERCISES each member through queue_for -- a device that cannot resolve a
    # queue is not a declared device, it is a typo. Printing a list without resolving it would be a
    # config-read standing in for a behavioural check (Rule 22a), which is the same substitution the
    # guard this feeds was built to stop.
    echo "declared devices (read from the device register org/devices/DEVICES.json -- single source of truth):"
    n=0
    for d in $(declared_devices); do
        printf "  %-8s -> %s\n" "$d" "$(queue_for "$d")"
        n=$((n+1))
    done
    echo "DECLARED_COUNT=${n}"
    echo "this device: $(this_device)"
    echo
    echo "READER-GUARD USE: a governance walk names walked/declared/UNWALKED from THIS output."
    echo "  Do NOT hand-copy the set into a review -- a hand-copied denominator cannot grow, and a"
    echo "  guard whose denominator cannot grow under-reports the exact gap it exists to surface."
    ;;

  peek)
    dev="${1:?usage: peek <device>}"
    aws sqs get-queue-attributes --region "$REGION" --queue-url "$(queue_for "$dev")" \
        --attribute-names ApproximateNumberOfMessages ApproximateNumberOfMessagesNotVisible
    echo "NOTE: depth is a PRODUCER-SIDE signal. It cannot distinguish read from discarded."
    ;;

  *)
    grep '^#' "$0" | sed 's/^# \{0,1\}//' | head -40
    exit 2
    ;;
esac
