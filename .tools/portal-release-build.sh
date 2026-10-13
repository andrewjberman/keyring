#!/usr/bin/env bash
# portal-release-build.sh -- the chosen-set release builder (NFRA_DEVPLN C-PROMOTE, FWD-5).
#
# A promote ships a LIST of approved feature branches. This script merges only those into a release
# branch cut from PROD (never live DEV), and checks the release's first-parent line for unapproved
# commits. It never pushes, never rebases, and offers no force option. Any refusal refuses the whole
# release and nothing is left behind.
#
#   bash .tools/portal-release-build.sh --features <b1,b2,...> [--repo <path>] [--prod-ref <ref>]
#   bash .tools/portal-release-build.sh --check <release-branch> [--repo <path>] [--prod-ref <ref>]
#   bash .tools/portal-release-build.sh --selftest
#
# The approval reader is `python .tools/open-calls.py approval-status --branch <b>` unless
# OPAL_APPROVAL_STATUS_CMD names another command (the selftest uses a fixture). Its one line is pinned:
#   APPROVAL branch= state= valid= row= by= head_sha= commits= class= box= pages=
# Refusal tokens of the pinned list: branch-not-found not-approved declined approver-not-valid
# stale-head commits-differ status-unreadable conflict unapproved-commits.
# Setup and argument refusals outside that list: bad-args no-workspace no-repo prod-ref-missing
# worktree-failed no-runtmp.

SELF_DIR="$(cd "$(dirname "$0")" && pwd)"
SELF="$SELF_DIR/$(basename "$0")"

MODE=""
FEATURES=""
CHECK_REL=""
REPO_ARG="portal"
PROD_REF="origin/PROD"

WS=""
REPO=""
WT=""
REL=""
REL_CREATED=0
PROD_SHA=""
R_REL=""
R_HEAD=""
REL_REF=""
REL_TIP=""
STAMP=""
CF=0
HEAD_SHA=""
ST_LINE=""
RC_F=0
RC_T=0
RC_U=0
STATUS_ARGV=()
FEAT_LIST=()
F_REF=()
F_SHA=()
F_CLASS=()
F_BY=()
F_ROW=()
F_PAGES=()

bad_args() {
  echo "ERROR: $1"
  echo "RELEASE result=REFUSED reason=bad-args branch=- base=- head=-"
  exit 2
}

# cleanup removes the ephemeral worktree the build made, on every path (EXIT trap). Git removes it
# when it is clean; a directory git will not remove (Windows long paths) is removed by path, and the
# worktree record is pruned either way.
cleanup() {
  if [ -n "$WT" ]; then
    git -C "$REPO" worktree remove "$WT" >/dev/null
    if [ -e "$WT" ]; then rm -rf "$WT"; fi
    git -C "$REPO" worktree prune >/dev/null
    WT=""
  fi
}

# refuse $1=reason $2=branch that names the refusal (optional). Prints the refusal and the RELEASE
# line, removes a release branch this run created, and exits 1.
refuse() {
  if [ -n "${2:-}" ]; then echo "REFUSE branch=$2 reason=$1"; fi
  if [ "$REL_CREATED" = 1 ]; then
    cleanup
    git -C "$REPO" update-ref -d "refs/heads/$REL" >/dev/null
    REL_CREATED=0
  fi
  echo "RELEASE result=REFUSED reason=$1 branch=${R_REL:--} base=${PROD_SHA:--} head=${R_HEAD:--}"
  exit 1
}

# fld LINE KEY NEXTKEY -- the value of KEY in a pinned APPROVAL line. A value may hold spaces (a FAST
# lease writes `by=FAST lease <file>`), so it runs up to the next pinned key, not to the next space.
fld() {
  local l=" $1" k="$2" n="$3" r
  case "$l" in *" $k="*) ;; *) return 1 ;; esac
  r="${l#*" $k="}"
  if [ -n "$n" ]; then
    case "$r" in *" $n="*) r="${r%%" $n="*}" ;; esac
  fi
  printf '%s' "$r"
}

# read_status BRANCH -- runs the approval reader; sets ST_LINE. Fails when the reader exits non-zero
# or prints no APPROVAL line.
read_status() {
  local out rc ln
  out=$("${STATUS_ARGV[@]}" --branch "$1")
  rc=$?
  if [ "$rc" -ne 0 ]; then return 1; fi
  ST_LINE=""
  while IFS= read -r ln; do
    ln="${ln%$'\r'}"
    case "$ln" in
      "APPROVAL "*) ST_LINE="$ln"; break ;;
    esac
  done <<< "$out"
  [ -n "$ST_LINE" ]
}

# release_check REPO PROD_SHA REF -- walks PROD..REF on the first-parent line (the release's own merge
# commits; a feature's commits sit under its second parent). Sets RC_F, RC_T, RC_U and prints the line.
release_check() {
  local sha msg walk
  RC_F=0
  RC_T=0
  RC_U=0
  walk=$(git -C "$1" rev-list --first-parent "$2..$3") || return 1
  for sha in $walk; do
    RC_T=$((RC_T + 1))
    msg=$(git -C "$1" log -1 --format=%B "$sha")
    if printf '%s\n' "$msg" | grep -q '^Feature: '; then RC_F=$((RC_F + 1)); fi
    if ! printf '%s\n' "$msg" | grep -q '^Approved-By: '; then RC_U=$((RC_U + 1)); fi
  done
  echo "RELEASE-CHECK features=$RC_F first_parent_commits=$RC_T unapproved=$RC_U"
}

# setup_repo -- the workspace root (derived, never typed), the portal repo, and the approval reader.
setup_repo() {
  WS=$(git rev-parse --show-toplevel) || refuse no-workspace
  cd "$WS" || refuse no-workspace
  if [ -d "$REPO_ARG" ]; then REPO=$(cd "$REPO_ARG" && pwd); else refuse no-repo; fi
  if [ ! -e "$REPO/.git" ]; then refuse no-repo; fi
  if [ -n "${OPAL_APPROVAL_STATUS_CMD:-}" ]; then
    read -r -a STATUS_ARGV <<< "$OPAL_APPROVAL_STATUS_CMD"
  else
    STATUS_ARGV=(python .tools/open-calls.py approval-status)
  fi
}

main_check() {
  setup_repo
  if git -C "$REPO" rev-parse --verify -q "refs/heads/$CHECK_REL^{commit}" >/dev/null; then
    REL_REF="refs/heads/$CHECK_REL"
  elif git -C "$REPO" rev-parse --verify -q "refs/remotes/origin/$CHECK_REL^{commit}" >/dev/null; then
    REL_REF="refs/remotes/origin/$CHECK_REL"
  else
    refuse branch-not-found "$CHECK_REL"
  fi
  PROD_SHA=$(git -C "$REPO" rev-parse --verify -q "$PROD_REF^{commit}") || refuse prod-ref-missing
  REL_TIP=$(git -C "$REPO" rev-parse "$REL_REF^{commit}") || refuse branch-not-found "$CHECK_REL"
  R_REL="$CHECK_REL"
  R_HEAD="$REL_TIP"
  release_check "$REPO" "$PROD_SHA" "$REL_REF" || refuse status-unreadable
  if [ "$RC_U" -gt 0 ]; then refuse unapproved-commits; fi
  echo "RELEASE result=READY reason=- branch=$CHECK_REL base=$PROD_SHA head=$REL_TIP"
  exit 0
}

main_build() {
  local i b ref tip actual msg HEAD_SHA
  setup_repo
  if [ -z "$FEATURES" ]; then bad_args "empty --features"; fi
  IFS=',' read -r -a FEAT_LIST <<< "$FEATURES"
  if [ "${#FEAT_LIST[@]}" -eq 0 ]; then bad_args "empty --features"; fi

  # 1. every branch exists (read as origin/<b>, else local). Nothing is created before this passes.
  for b in "${FEAT_LIST[@]}"; do
    if [ -z "$b" ]; then bad_args "empty branch name in --features"; fi
    if ! git check-ref-format --branch "$b" >/dev/null; then refuse bad-args "$b"; fi
    if git -C "$REPO" rev-parse --verify -q "refs/remotes/origin/$b^{commit}" >/dev/null; then
      F_REF+=("refs/remotes/origin/$b")
    elif git -C "$REPO" rev-parse --verify -q "refs/heads/$b^{commit}" >/dev/null; then
      F_REF+=("refs/heads/$b")
    else
      refuse branch-not-found "$b"
    fi
  done

  PROD_SHA=$(git -C "$REPO" rev-parse --verify -q "$PROD_REF^{commit}") || refuse prod-ref-missing

  # 2. every row approves its branch at this head and this commit count.
  for i in "${!FEAT_LIST[@]}"; do
    b="${FEAT_LIST[$i]}"
    ref="${F_REF[$i]}"
    tip=$(git -C "$REPO" rev-parse "$ref^{commit}") || refuse status-unreadable "$b"
    actual=$(git -C "$REPO" rev-list --count "$PROD_SHA..$ref") || refuse status-unreadable "$b"
    read_status "$b" || refuse status-unreadable "$b"
    P_BRANCH=$(fld "$ST_LINE" branch state)
    P_STATE=$(fld "$ST_LINE" state valid)
    P_VALID=$(fld "$ST_LINE" valid row)
    P_ROW=$(fld "$ST_LINE" row by)
    P_BY=$(fld "$ST_LINE" by head_sha)
    P_SHA=$(fld "$ST_LINE" head_sha commits)
    P_COMMITS=$(fld "$ST_LINE" commits class)
    P_CLASS=$(fld "$ST_LINE" class box)
    P_PAGES=$(fld "$ST_LINE" pages "")
    if [ "$P_BRANCH" != "$b" ]; then refuse status-unreadable "$b"; fi
    case "$P_STATE" in
      APPROVED) ;;
      DECLINED) refuse declined "$b" ;;
      ABSENT|OPEN) refuse not-approved "$b" ;;
      *) refuse status-unreadable "$b" ;;
    esac
    if [ "$P_VALID" != "yes" ]; then refuse approver-not-valid "$b"; fi
    if [ "$P_SHA" != "$tip" ]; then refuse stale-head "$b"; fi
    if [ "$P_COMMITS" != "$actual" ]; then refuse commits-differ "$b"; fi
    if [ "$P_ROW" = "-" ] || [ "$P_BY" = "-" ]; then refuse status-unreadable "$b"; fi
    F_SHA+=("$tip")
    F_CLASS+=("$P_CLASS")
    F_BY+=("$P_BY")
    F_ROW+=("$P_ROW")
    F_PAGES+=("$P_PAGES")
  done

  # 3. the ephemeral worktree cut from PROD, and the release branch it carries.
  STAMP=$(date -u +%Y%m%dT%H%M%SZ)
  REL="release/$STAMP"
  while git -C "$REPO" rev-parse --verify -q "refs/heads/$REL" >/dev/null || [ -e "$WS/.runtmp/portal-release-$STAMP" ]; do
    sleep 1
    STAMP=$(date -u +%Y%m%dT%H%M%SZ)
    REL="release/$STAMP"
  done
  mkdir -p "$WS/.runtmp" || refuse no-runtmp
  WT="$WS/.runtmp/portal-release-$STAMP"
  trap cleanup EXIT
  trap 'exit 130' INT TERM
  if git -C "$REPO" worktree add -q --no-track -b "$REL" "$WT" "$PROD_SHA" >/dev/null; then
    REL_CREATED=1
  else
    refuse worktree-failed
  fi
  if [ -z "$(git -C "$WT" config user.email)" ]; then
    export GIT_AUTHOR_NAME="${OPAL_AGENT_SERIAL:-portal-release-build}"
    export GIT_AUTHOR_EMAIL="${OPAL_AGENT_SERIAL:-portal-release-build}@opal.agent"
    export GIT_COMMITTER_NAME="${OPAL_AGENT_SERIAL:-portal-release-build}"
    export GIT_COMMITTER_EMAIL="${OPAL_AGENT_SERIAL:-portal-release-build}@opal.agent"
  fi

  # 4. one --no-ff merge per feature, trailers on the merge commit.
  for i in "${!FEAT_LIST[@]}"; do
    b="${FEAT_LIST[$i]}"
    msg=$(printf 'merge feature %s into %s\n\nFeature: %s\nApproved-By: %s @%s\n' "$b" "$REL" "$b" "${F_BY[$i]}" "${F_ROW[$i]}")
    if ! git -C "$WT" merge --no-ff -q -m "$msg" "${F_SHA[$i]}" >/dev/null; then
      git -C "$WT" merge --abort >/dev/null 2>&1
      refuse conflict "$b"
    fi
  done

  # 5. the check on the release's first-parent line, then the promote list.
  release_check "$REPO" "$PROD_SHA" "refs/heads/$REL" || refuse status-unreadable
  if [ "$RC_U" -gt 0 ]; then
    R_REL=""
    refuse unapproved-commits
  fi
  CF=0
  for i in "${!FEAT_LIST[@]}"; do
    echo "PROMOTE-LIST branch=${FEAT_LIST[$i]} class=${F_CLASS[$i]} by=${F_BY[$i]} row=${F_ROW[$i]} pages=${F_PAGES[$i]}"
    if [ "${F_CLASS[$i]}" = "client-facing" ]; then CF=$((CF + 1)); fi
  done
  echo "PROMOTE-CLIENT-FACING count=$CF"
  HEAD_SHA=$(git -C "$REPO" rev-parse "refs/heads/$REL")
  echo "RELEASE result=READY reason=- branch=$REL base=$PROD_SHA head=$HEAD_SHA"
  exit 0
}

selftest() {
  local ok_count=0 n=0 out rc rel9 plain tree before after wt c ok p0 tipv cntv
  T=$(mktemp -d) || { echo "ERROR: mktemp -d failed"; echo "RELEASE-SELFTEST cases=0/0 ok=False"; exit 1; }
  trap 'chmod -R u+w "$T" >/dev/null 2>&1; rm -rf "$T"' EXIT
  export GIT_AUTHOR_NAME=selftest GIT_AUTHOR_EMAIL=selftest@opal.agent
  export GIT_COMMITTER_NAME=selftest GIT_COMMITTER_EMAIL=selftest@opal.agent
  export FIX_DIR="$T/fix"
  mkdir -p "$FIX_DIR" "$T/ws"

  cat > "$T/fixture.sh" <<'FIXEOF'
#!/usr/bin/env bash
# selftest fixture: prints the APPROVAL line written for --branch <b>; exits with <b>.rc when present
b=""
while [ $# -gt 0 ]; do
  case "$1" in
    --branch) b="$2"; shift 2 ;;
    *) shift ;;
  esac
done
f="$FIX_DIR/${b//\//__}"
if [ -f "$f" ]; then
  cat "$f"
  rc=0
  if [ -f "$f.rc" ]; then rc=$(cat "$f.rc"); fi
  exit "$rc"
fi
echo "APPROVAL branch=$b state=ABSENT valid=- row=- by=- head_sha=- commits=- class=- box=- pages=-"
exit 0
FIXEOF
  export OPAL_APPROVAL_STATUS_CMD="bash $T/fixture.sh"

  # the origin, the seed that builds it, and the portal clone inside the test workspace
  git init -q "$T/ws"
  git init -q --bare "$T/origin.git"
  git -C "$T/origin.git" symbolic-ref HEAD refs/heads/PROD
  git init -q "$T/seed"
  git -C "$T/seed" symbolic-ref HEAD refs/heads/PROD
  addc() { printf '%s\n' "$3" > "$1/$2" && git -C "$1" add -- "$2" && git -C "$1" commit -q -m "$3"; }
  addc "$T/seed" base.txt "prod base"
  git -C "$T/seed" branch -q DEV
  git -C "$T/seed" checkout -q DEV
  addc "$T/seed" dev1.txt "dev change one"
  addc "$T/seed" dev-only.txt "dev only change, not approved"
  git -C "$T/seed" checkout -q PROD
  for f in feat-a feat-b feat-open feat-declined feat-unread; do
    git -C "$T/seed" checkout -q -b "$f" PROD
    addc "$T/seed" "$f.txt" "$f work"
    git -C "$T/seed" checkout -q PROD
  done
  git -C "$T/seed" checkout -q -b feat-dev DEV
  addc "$T/seed" dev-feat.txt "feat-dev work on top of DEV"
  git -C "$T/seed" checkout -q PROD
  git -C "$T/seed" push -q "$T/origin.git" --all
  git clone -q "$T/origin.git" "$T/ws/portal"
  PORTAL="$T/ws/portal"

  tipof() { git -C "$PORTAL" rev-parse "refs/remotes/origin/$1^{commit}"; }
  cntof() { git -C "$PORTAL" rev-list --count "refs/remotes/origin/PROD..refs/remotes/origin/$1"; }
  reset_fix() { rm -f "$FIX_DIR"/*; }
  st() { # $1 branch $2 state $3 valid $4 head_sha $5 commits $6 class
    local f="$FIX_DIR/${1//\//__}"
    printf 'APPROVAL branch=%s state=%s valid=%s row=row-%s by=andrew head_sha=%s commits=%s class=%s box=laptop pages=p1,p2\n' \
      "$1" "$2" "$3" "${1//\//-}" "$4" "$5" "$6" > "$f"
  }
  stu() { # $1 branch: the reader fails (rc 2) and prints an UNREADABLE line
    local f="$FIX_DIR/${1//\//__}"
    printf 'APPROVAL branch=%s state=UNREADABLE valid=- row=- by=- head_sha=- commits=- class=- box=- pages=-\n' "$1" > "$f"
    printf '2\n' > "$f.rc"
  }
  run() { (cd "$T/ws" && bash "$SELF" "$@"); }
  refused_with() { printf '%s\n' "$1" | grep -qx "REFUSE branch=$2 reason=$3"; }
  wtcount() { git -C "$PORTAL" worktree list --porcelain | grep -c '^worktree '; }
  relcount() { git -C "$PORTAL" for-each-ref --format='%(refname)' refs/heads/release/ | grep -c .; }
  record() { # $1 name $2 cond (0|1)
    n=$((n + 1))
    if [ "$2" = 1 ]; then
      ok_count=$((ok_count + 1)); echo "CASE $n $1 ok=True"
    else
      echo "CASE $n $1 ok=False"
    fi
  }

  # 1. two approved features build a release with unapproved=0
  reset_fix
  st feat-a APPROVED yes "$(tipof feat-a)" "$(cntof feat-a)" client-facing
  st feat-b APPROVED yes "$(tipof feat-b)" "$(cntof feat-b)" opal-internal
  out=$(run --features feat-a,feat-b); rc=$?
  rel1=$(printf '%s\n' "$out" | sed -n 's/^RELEASE result=READY .* branch=\([^ ]*\) .*/\1/p')
  c=0
  if [ "$rc" -eq 0 ] && [ -n "$rel1" ] \
     && printf '%s\n' "$out" | grep -qx 'RELEASE-CHECK features=2 first_parent_commits=2 unapproved=0' \
     && printf '%s\n' "$out" | grep -qx 'PROMOTE-CLIENT-FACING count=1' \
     && git -C "$PORTAL" cat-file -e "$rel1:feat-b.txt" \
     && [ "$(wtcount)" -eq 1 ]; then c=1; fi
  record "two-approved-release-unapproved-0" "$c"

  # 2. one OPEN feature among two refuses the whole release and creates no branch
  reset_fix
  st feat-a APPROVED yes "$(tipof feat-a)" "$(cntof feat-a)" client-facing
  st feat-open OPEN - - - opal-internal
  before=$(relcount)
  out=$(run --features feat-a,feat-open); rc=$?
  after=$(relcount)
  c=0
  if [ "$rc" -ne 0 ] && refused_with "$out" feat-open not-approved \
     && printf '%s\n' "$out" | grep -q '^RELEASE result=REFUSED reason=not-approved ' \
     && [ "$before" = "$after" ] && [ "$(wtcount)" -eq 1 ]; then c=1; fi
  record "one-open-refuses-whole-release-no-branch" "$c"

  # 3. a stale head refuses
  reset_fix
  p0=$(git -C "$PORTAL" rev-parse "refs/remotes/origin/PROD^{commit}")
  st feat-a APPROVED yes "$p0" "$(cntof feat-a)" client-facing
  st feat-b APPROVED yes "$(tipof feat-b)" "$(cntof feat-b)" opal-internal
  out=$(run --features feat-a,feat-b); rc=$?
  c=0
  if [ "$rc" -ne 0 ] && refused_with "$out" feat-a stale-head; then c=1; fi
  record "stale-head-refuses" "$c"

  # 4. a valid=no row refuses
  reset_fix
  st feat-a APPROVED no "$(tipof feat-a)" "$(cntof feat-a)" client-facing
  out=$(run --features feat-a); rc=$?
  c=0
  if [ "$rc" -ne 0 ] && refused_with "$out" feat-a approver-not-valid; then c=1; fi
  record "valid-no-row-refuses" "$c"

  # 5. a row whose commit count differs from the branch refuses
  reset_fix
  st feat-a APPROVED yes "$(tipof feat-a)" 9 client-facing
  out=$(run --features feat-a); rc=$?
  c=0
  if [ "$rc" -ne 0 ] && refused_with "$out" feat-a commits-differ; then c=1; fi
  record "commits-differ-row-refuses" "$c"

  # 6. a feature cut from DEV carries DEV commits beneath it; the row (approved as one commit) refuses
  reset_fix
  st feat-dev APPROVED yes "$(tipof feat-dev)" 1 client-facing
  out=$(run --features feat-dev); rc=$?
  c=0
  if [ "$rc" -ne 0 ] && refused_with "$out" feat-dev commits-differ \
     && [ "$(cntof feat-dev)" -eq 3 ]; then c=1; fi
  record "feature-cut-from-DEV-refuses-commits-differ" "$c"

  # 7. a DECLINED row refuses
  reset_fix
  st feat-declined DECLINED - - - opal-internal
  out=$(run --features feat-declined); rc=$?
  c=0
  if [ "$rc" -ne 0 ] && refused_with "$out" feat-declined declined; then c=1; fi
  record "declined-refuses" "$c"

  # 8. a reader that fails (rc 2) refuses as status-unreadable
  reset_fix
  stu feat-unread
  out=$(run --features feat-unread); rc=$?
  c=0
  if [ "$rc" -ne 0 ] && refused_with "$out" feat-unread status-unreadable; then c=1; fi
  record "unreadable-reader-refuses" "$c"

  # 9. --check on a release with one extra plain untrailered commit on its first-parent line refuses
  reset_fix
  st feat-a APPROVED yes "$(tipof feat-a)" "$(cntof feat-a)" client-facing
  st feat-b APPROVED yes "$(tipof feat-b)" "$(cntof feat-b)" opal-internal
  out=$(run --features feat-a,feat-b)
  rel9=$(printf '%s\n' "$out" | sed -n 's/^RELEASE result=READY .* branch=\([^ ]*\) .*/\1/p')
  c=0
  if [ -n "$rel9" ]; then
    tree=$(git -C "$PORTAL" rev-parse "$rel9^{tree}")
    plain=$(git -C "$PORTAL" commit-tree "$tree" -p "$rel9" -m "plain change without trailer")
    git -C "$PORTAL" update-ref refs/heads/plain-check "$plain"
    out=$(run --check plain-check); rc=$?
    if [ "$rc" -ne 0 ] && printf '%s\n' "$out" | grep -qx 'RELEASE-CHECK features=2 first_parent_commits=3 unapproved=1' \
       && printf '%s\n' "$out" | grep -q '^RELEASE result=REFUSED reason=unapproved-commits '; then c=1; fi
  fi
  record "check-plain-untrailered-commit-refuses" "$c"

  # 10. an unapproved change left on the temporary DEV is NOT on the release (DEV positive control)
  c=0
  if [ -n "$rel1" ] && git -C "$PORTAL" cat-file -e "refs/remotes/origin/DEV:dev-only.txt" \
     && ! git -C "$PORTAL" cat-file -e "$rel1:dev-only.txt" \
     && ! git -C "$PORTAL" merge-base --is-ancestor "refs/remotes/origin/DEV" "$rel1"; then c=1; fi
  record "unapproved-DEV-change-not-on-release" "$c"

  ok=False
  if [ "$ok_count" -eq "$n" ]; then ok=True; fi
  echo "RELEASE-SELFTEST cases=$ok_count/$n ok=$ok"
  if [ "$ok" = True ]; then exit 0; fi
  exit 1
}

# ---- argument parse and dispatch ----
while [ $# -gt 0 ]; do
  case "$1" in
    --features)
      [ $# -ge 2 ] || bad_args "--features needs a value"
      MODE=build; FEATURES="$2"; shift 2 ;;
    --check)
      [ $# -ge 2 ] || bad_args "--check needs a branch"
      MODE=check; CHECK_REL="$2"; shift 2 ;;
    --repo)
      [ $# -ge 2 ] || bad_args "--repo needs a path"
      REPO_ARG="$2"; shift 2 ;;
    --prod-ref)
      [ $# -ge 2 ] || bad_args "--prod-ref needs a ref"
      PROD_REF="$2"; shift 2 ;;
    --selftest)
      MODE=selftest; shift ;;
    *)
      bad_args "unknown argument: $1" ;;
  esac
done

case "$MODE" in
  build) main_build ;;
  check) main_check ;;
  selftest) selftest ;;
  *) bad_args "give --features <list>, --check <branch> or --selftest" ;;
esac
