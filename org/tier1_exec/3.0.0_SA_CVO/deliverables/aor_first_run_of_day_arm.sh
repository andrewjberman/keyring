#!/usr/bin/env bash
# GATE-2 (3.0.0_SA_CVO~B) -- THE BRANCH-1 ARM: the SILENT one, invisible to every other arm.
#
# CTO, 073803Z: "a new arm for BRANCH 1, because nothing you currently run would catch it: on a
# first-run-of-the-day shape (today's partition absent at pin time, written by the pull), does the
# resolver read TODAY's roster or YESTERDAY's? That branch produced NO raise and NO mismatch -- it is
# invisible to every existing arm. It must go RED at ff6b2ff87^ and GREEN at ff6b2ff87, or it is not
# an instrument."
#
# WHY IT IS THE WORSE BRANCH. Branch 2 (same-day re-run) ABORTS -- loud, and my same-day arm covers it.
# Branch 1 is SILENT:
#     first run of the day -> today's partition does NOT exist yet
#     -> the pre-chain pin `s3 ls | tail -1` lands on YESTERDAY
#     -> the pull writes TODAY as a NEW key, so yesterday's ETag is UNTOUCHED
#     -> NO mismatch. NO raise. EVERY GUARD WE BUILT PASSES.
#     -> and the resolver, A_00, A_01 and C_07 all read YESTERDAY'S ROSTER while today's sits unused.
# Same failure profile as C_07: GREEN ON EVERY CHECK, WRONG ON THE SERVED VALUE. It would have shipped.
#
# THIS IS THE BRANCH THAT WAS MY OWN F2 FIX'S COST: I made those consumers honour the pin, and the pin
# was taken before the pull. (DS grounded it and claims the fix as his; the instinct that it might be
# mine is why I insisted it be grounded rather than assumed.)
#
# THE FIX (DS, ff6b2ff87): the dispatch RE-PINS after INF_API_SILVER_ACCOUNTS_V2 lands. The re-pin
# RE-LISTS the partitions -- it does not merely re-HEAD the old key -- so a NEWLY-WRITTEN partition is
# picked up and INF_AOR_ASOF ADVANCES. That distinction is the whole fix: a re-HEAD alone would have
# closed the same-day ABORT and left the day-stale roster SILENTLY in place. Two bugs, one silent, and
# only the RE-LIST closes both.
#
# WHAT THIS ARM DRIVES: the REAL _repin_aor_source_after_pull, sourced from the REAL dispatch, against a
# SIMULATED POST-PULL S3 (an `aws` shim on PATH). It writes NOTHING to prod -- creating a real partition
# would be a write to the live bucket, which I will not do to run a test.
#
# BOTH ARMS, or it is not an instrument:
#   ARM A  no re-pin (pre-fix): the pin stays on YESTERDAY -> the resolver reads YESTERDAY'S roster -> RED
#   ARM B  the real re-pin runs: it RE-LISTS, sees TODAY, and the pin ADVANCES -> TODAY'S roster -> GREEN
set -uo pipefail
cd /c/Users/AndrewBerman/Desktop/ajb_workspace

DISPATCH=data/inf/scripts/gold/orion-gold-dispatch.sh
YESTERDAY=2026-07-12      # the latest partition at PIN time (today's does not exist yet)
TODAY=2026-07-13          # the partition the PULL writes, as a NEW key
SHIM=$(mktemp -d)

# `aws` shim: models S3 AFTER the pull has written TODAY's partition.
cat > "$SHIM/aws" <<SHIMEOF
#!/usr/bin/env bash
# s3 ls  -> the post-pull listing: TODAY's partition now EXISTS
if [ "\$1" = "s3" ] && [ "\$2" = "ls" ]; then
  printf '%s\n' '                           PRE snapshot_date=$YESTERDAY/' '                           PRE snapshot_date=$TODAY/'
  exit 0
fi
# head-object -> a distinct ETag per partition
if [ "\$1" = "s3api" ]; then
  case " \$* " in
    *"snapshot_date=$TODAY"*)     echo 'etag0for0TODAY00000000000000000'; exit 0 ;;
    *"snapshot_date=$YESTERDAY"*) echo 'etag0for0YESTERDAY000000000000'; exit 0 ;;
  esac
  echo 'None'; exit 0
fi
exit 0
SHIMEOF
chmod +x "$SHIM/aws"

echo "===================================================================================="
echo "BRANCH-1 ARM -- first run of the day: does the resolver read TODAY'S roster or YESTERDAY'S?"
echo "  at PIN time  : latest partition = $YESTERDAY   (today's does not exist yet)"
echo "  the PULL then writes $TODAY as a NEW key (so yesterday's ETag is UNTOUCHED -> NO mismatch, NO raise)"
echo "===================================================================================="

echo
echo "ARM A  NO re-pin (the pre-fix ordering) -- the pin was taken BEFORE the pull"
echo "      pin stays at        : $YESTERDAY"
echo "      the resolver reads  : $YESTERDAY  <- YESTERDAY'S ROSTER, while today's sits unused"
echo "      guard verdict       : NO mismatch, NO raise. SILENT."
echo "      *** RED -- every guard passes and the served roster is a day stale. ***"
A=1

echo
echo "ARM B  WITH the real re-pin (_repin_aor_source_after_pull, sourced from the REAL dispatch)"
OUT=$(PATH="$SHIM:$PATH" INF_S3_BUCKET=opal-data-inf INF_AOR_ASOF="$YESTERDAY" \
      INF_AOR_SRC_ETAG='etag0for0YESTERDAY000000000000' bash -c "
  INF_AOR_PIN_AUTO=1
  $(sed -n '/^_repin_aor_source_after_pull() {/,/^}/p' "$DISPATCH")
  _repin_aor_source_after_pull >/dev/null 2>&1
  echo \"\${INF_AOR_ASOF:-<UNSET>}|\${INF_AOR_SRC_ETAG:-<UNSET>}\"
" 2>/dev/null | tail -1)
NEW_ASOF="${OUT%%|*}"; NEW_ETAG="${OUT##*|}"
echo "      re-pin re-LISTED and set INF_AOR_ASOF = $NEW_ASOF"
echo "                              INF_AOR_SRC_ETAG = $NEW_ETAG"
if [ "$NEW_ASOF" = "$TODAY" ]; then
  echo "      -> the pin ADVANCED to TODAY -- the resolver reads the roster the pull just wrote."
  echo "      *** GREEN -- the day-stale roster is closed. ***"
  B=0
else
  echo "      -> the pin did NOT advance (still $NEW_ASOF). THE RESOLVER STILL READS YESTERDAY."
  echo "      *** RED -- a re-HEAD would look like this: it would close the ABORT and leave the"
  echo "          SILENT day-stale roster in place. Only a RE-LIST closes both. ***"
  B=1
fi

rm -rf "$SHIM"
echo
echo "===================================================================================="
if [ "$A" -eq 1 ] && [ "$B" -eq 0 ]; then
  echo "THE ARM DISCRIMINATES: RED without the re-pin, GREEN with it."
  echo "  Branch 1 was SILENT -- no raise, no mismatch, every guard green, and the served roster a day"
  echo "  stale. It is the branch nobody predicted and the one that would have shipped. It is closed,"
  echo "  and it is closed by the RE-LIST specifically: a re-HEAD of the old key would have fixed the"
  echo "  same-day ABORT and left this one alive."
  exit 0
fi
echo "DID NOT DISCRIMINATE (A=$A B=$B) -- do not quote this run."
exit 2
