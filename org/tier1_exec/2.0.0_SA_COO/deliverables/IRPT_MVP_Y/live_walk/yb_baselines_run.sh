#!/usr/bin/env bash
# Fold-in Y-B (CTO batch 178, CTO_FOLD_IN_IRPT_THREE_BRIEFS_20261002.md section 2): the typo file and Case D each reach
# NEEDS_CORRECTION on TODAY's code, recorded before the two intake gates change. ONE upload per leg, no submission
# (WALK_K4_ONLY=1: live_chain.py makes exactly one K4 POST and never a K5), one leg at a time behind hop7_run.sh's solo gate.
#
#   bash yb_baselines_run.sh --plan  <file.xlsx>    # solo gate + the K4 body; no secret read, no POST
#   bash yb_baselines_run.sh --typo  <file.xlsx>    # ONE upload of the typo file (AAPL as APPL, sha256 87afdc7db1c58b38..)
#   bash yb_baselines_run.sh --case-d <file.xlsx>   # ONE upload of Case D (20 rows, sha256 f0d344fa967504bd..)
#
# The caller passes a NEUTRALLY NAMED copy (the server stores the filename; a person's name must not reach a record). The
# file's sha256 prefix is checked against the case before anything fires. AUTHORITY: Andrew-direct 2026-10-02 ~18:1xZ
# ("Yes one at a time with queue empty"; record addendum 3 @7f197bcde6) and CTO msg 104351. Evidence: ../YB_BASELINES/.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
export HOP7_OUT="$HERE/../YB_BASELINES"
AUTH="fold-in Y-B; CTO batch 178 and msg 104351; Andrew-direct 2026-10-02 181xZ addendum 3 @7f197bcde6"
mode="${1:-}"; file="${2:-}"
[ -f "$file" ] || { echo "usage: yb_baselines_run.sh --plan|--typo|--case-d <file.xlsx>" >&2; exit 2; }
sha=$(sha256sum "$file" | cut -c1-16)
case "$mode" in
  --typo)   want=87afdc7db1c58b38; base=YB_typo_cottonwood ;;
  --case-d) want=f0d344fa967504bd; base=YB_case_d_cottonwood ;;
  --plan)   want="$sha"; base=YB_plan ;;
  *) echo "usage: yb_baselines_run.sh --plan|--typo|--case-d <file.xlsx>" >&2; exit 2 ;;
esac
[ "$sha" = "$want" ] || { echo "REFUSED: $file sha256 $sha is not the case's $want" >&2; exit 3; }
export HOP7_BASE="$base" HOP7_AUTHORITY="$base; $AUTH" WALK_UPLOAD_FILE="$file" WALK_FILE_TYPE=xlsx WALK_K4_ONLY=1
echo "  case file : $(basename "$file") sha256 $sha"
if [ "$mode" = "--plan" ]; then exec bash "$HERE/hop7_run.sh" --plan; fi
exec bash "$HERE/hop7_run.sh"
