#!/usr/bin/env bash
# Sign-in option C (CTO rulings batch 131 item 2) on the st12 resident -- leg S (ONE operator sign-in, no probe first),
# then leg J (ONE job attempt) only if S authenticates. The hop-8 runner's legs S and J with this window's folder, root,
# base and ledger; leg P is NOT run (batch 127: no probe precedes a job; the session read EVICTED at 06:26Z).
#
#   bash signin_c_run.sh --plan   # the running root, the solo gate and what each leg would run; no vendor call
#   bash signin_c_run.sh --leg-s  # ONE run of the canonical sign-in wrapper in the resident's context
#   bash signin_c_run.sh --leg-j  # ONE upload and ONE Overview; refuses unless S reads AUTHENTICATED >= 600 s ago
#
# Packet: ../SIGNIN_C/WINDOW_PACKET_SIGNIN_C_20261002.md. Each leg once; a leg whose output exists refuses. A CAPTCHA is
# a clean refusal: no retry, and no second leg S inside 24 hours (batch 131 item 2).
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
export HOP8_OUT="$HERE/../SIGNIN_C"
export HOP8_ROOT="/opt/irpt-resident/cf3ae52aee-st12"
export HOP8_BASE="SC_overview_cottonwood"
export HOP8_AUTHORITY="sign-in C leg J; CTO batch 131 item 2 and batch 130; Andrew-direct 2026-09-27 124xZ; ledger irpt-signin-c-20261002"
P_OUT="$HOP8_OUT/LEG_P_OUTPUT_20261001.txt"   # the hop-8 runner's file name for leg P's verdict
mkdir -p "$HOP8_OUT"
case "${1:-}" in
  --plan)
    exec bash "$HERE/hop8_run.sh" --plan
    ;;
  --leg-s)
    # The hop-8 runner admits leg S only after a NOT_LIVE probe. No probe is made in this window, so the stand-in
    # names its source instead of a reading: the resident's own eviction verdict of 06:26:09Z and the refused
    # refresh of 06:26:18Z (HOP3_PROOF/OUTCOME_HOP3_PROOF_20261002.md).
    [ -e "$P_OUT" ] || printf '%s\n' "NO PROBE MADE (CTO batch 127). The session's last reading: EVICTED 2026-10-02T06:26:09Z, refresh refused CHALLENGE_CAPTCHA_UNSUPPORTED 06:26:18Z (HOP3_PROOF/OUTCOME_HOP3_PROOF_20261002.md)." "PROBE_VERDICT=NOT_LIVE:EVICTED_0626Z_NOT_PROBED" > "$P_OUT"
    exec bash "$HERE/hop8_run.sh" --leg-s
    ;;
  --leg-j)
    exec bash "$HERE/hop8_run.sh" --leg-j
    ;;
  *)
    echo "usage: signin_c_run.sh --plan | --leg-s | --leg-j" >&2
    exit 2
    ;;
esac
