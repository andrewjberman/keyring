#!/usr/bin/env bash
# .tools/wk-provision.sh -- provision (and remove) a portal-cell worker worktree.
# Git Bash 3.6.7-safe: default utilities only (git, sed, awk, grep, cut, ls, wc, mktemp, mklink via cmd.exe).
# See AMGT-rk-60 task order for the ruling this script implements.
set -uo pipefail

SELF="$(basename "$0")"

log_err() {
  echo "ERROR: $*" >&2
}

die() {
  local rc="$1"; shift
  log_err "$*"
  exit "$rc"
}

refuse() {
  local rc="$1"; shift
  echo "REFUSED: $*" >&2
  exit "$rc"
}

usage() {
  cat >&2 <<'EOF'
usage:
  wk-provision.sh provision <CODE> <n> --path <abs-path> [--portal-ref <commit-ish>] [--node-modules link|none|install]
                                        [--nested <path>=<ref> ...] [--order <task-order-file> ...]
                                        [--sparse-add <folder> ...] [--full "<reason>"]

provision is a SPARSE checkout by default: the base set is .tools/, lib/ and the project folder
org/missions/D*/*/<CODE> (plus the root files). --order adds every folder its <paths> block names (a file
contributes its parent folder; a path absent at HEAD is printed as SKIPPED). --sparse-add adds a folder.
--full "<reason>" is a full checkout; the reason is required (an empty reason is refused, rc 2, nothing created).
  wk-provision.sh portal <worktree-path> [--portal-ref <commit-ish>] [--node-modules link|none|install]
  wk-provision.sh remove <worktree-path> [--portal-only]
  wk-provision.sh --self-test

--node-modules: the DEFAULT is link. install is REFUSED (rc 2, before anything is created) unless a registry redirect to a
non-public host is present in the environment (BUN_CONFIG_REGISTRY / NPM_CONFIG_REGISTRY / npm_config_registry) or in the
portal's bunfig.toml: bun install contacts the package registry, and no request may leave this machine.

--nested <path>=<ref> (repeatable): provision a nested worktree for ANY path .gitmodules
maps, the same way portal's own nested worktree is provisioned (branch
<super-branch>-<path with / as ->, off <ref> resolved in the MAIN tree's copy of the
nested repo). node_modules handling stays portal-only. Refuses rc 2, before anything is
created, when the main tree's copy of the named submodule is uninitialised.
EOF
}

main_worktree() {
  git worktree list --porcelain | head -1 | sed 's/^worktree //'
}

# registry_redirect_ok <dir-with-bunfig> -- rc 0 only when at least one registry redirect is present (BUN_CONFIG_REGISTRY,
# NPM_CONFIG_REGISTRY, npm_config_registry, or a registry = "..." line in <dir>/bunfig.toml) AND EVERY one present names a
# non-public host (localhost, loopback, or a private range). Anything else, including no redirect at all, is rc 1.
registry_redirect_ok() {
  local dir="${1:-}" url host seen=0 bad=0 urls=()
  [ -n "${BUN_CONFIG_REGISTRY:-}" ] && urls+=("$BUN_CONFIG_REGISTRY")
  [ -n "${NPM_CONFIG_REGISTRY:-}" ] && urls+=("$NPM_CONFIG_REGISTRY")
  [ -n "${npm_config_registry:-}" ] && urls+=("$npm_config_registry")
  if [ -n "$dir" ] && [ -f "$dir/bunfig.toml" ]; then
    url="$(sed -n 's/^[[:space:]]*registry[[:space:]]*=[[:space:]]*"\([^"]*\)".*/\1/p' "$dir/bunfig.toml" | head -1)"
    [ -n "$url" ] && urls+=("$url")
  fi
  for url in "${urls[@]+"${urls[@]}"}"; do
    seen=$((seen + 1))
    host="${url#*://}"; host="${host%%/*}"; host="${host##*@}"
    case "$host" in
      \[*) host="${host%%]*}]" ;;
      *) host="${host%%:*}" ;;
    esac
    case "$host" in
      localhost|127.*|"[::1]"|10.*|192.168.*|172.1[6-9].*|172.2[0-9].*|172.3[0-1].*) ;;
      *) bad=$((bad + 1)) ;;
    esac
  done
  [ "$seen" -gt 0 ] && [ "$bad" -eq 0 ]
}

# guard_install_mode <mode> <dir-with-bunfig> -- refuses rc 2 for the install mode unless registry_redirect_ok.
guard_install_mode() {
  [ "$1" = "install" ] || return 0
  registry_redirect_ok "${2:-}" && return 0
  refuse 2 "--node-modules install runs bun install, which contacts the package registry, and no request may leave this machine; use --node-modules link (the default) or --node-modules none"
}

require_nested_repo() {
  local nested="$1"
  if [ ! -e "$nested/.git" ]; then
    refuse 2 "nested repository .git absent at $nested"
  fi
}

cmd_portal() {
  if [ $# -lt 1 ]; then
    die 2 "portal: <worktree-path> required"
  fi
  local worktree="$1"; shift
  local portal_ref=""
  local node_modules_mode=""

  while [ $# -gt 0 ]; do
    case "$1" in
      --portal-ref)
        shift
        [ $# -gt 0 ] || die 2 "portal: --portal-ref requires a value"
        portal_ref="$1"
        ;;
      --node-modules)
        shift
        [ $# -gt 0 ] || die 2 "portal: --node-modules requires a value"
        node_modules_mode="$1"
        ;;
      *)
        die 2 "portal: unknown argument: $1"
        ;;
    esac
    shift
  done

  [ -e "$worktree/.git" ] || refuse 2 "$worktree is not a git worktree (.git absent)"

  local main nested
  main="$(main_worktree)"
  nested="$main/portal"
  require_nested_repo "$nested"
  guard_install_mode "$node_modules_mode" "$nested"

  local gitlink_line gitlink_sha
  gitlink_line="$(git -C "$worktree" ls-tree HEAD portal)"
  gitlink_sha="$(printf '%s' "$gitlink_line" | awk '{print $3}')"
  [ -n "$gitlink_sha" ] || refuse 2 "gitlink sha unresolved for $worktree"

  if [ -z "$portal_ref" ]; then
    portal_ref="$(git -C "$nested" rev-parse --abbrev-ref HEAD)"
  fi

  local resolved_sha
  if ! resolved_sha="$(git -C "$nested" rev-parse --verify -q "${portal_ref}^{commit}" 2>/dev/null)"; then
    refuse 2 "--portal-ref $portal_ref does not resolve in $nested"
  fi
  echo "PORTAL_REF: $portal_ref -> $resolved_sha"

  local behind_ref
  behind_ref="$(git -C "$nested" rev-list --count "$gitlink_sha".."$resolved_sha" 2>/dev/null)"
  [ -n "$behind_ref" ] || behind_ref="?"
  echo "GITLINK: $gitlink_sha behind_ref=$behind_ref"

  local portal_dir="$worktree/portal"
  if [ -d "$portal_dir" ]; then
    local entry_count
    entry_count="$(ls -A "$portal_dir" 2>/dev/null | wc -l)"
    if [ "$entry_count" -ne 0 ]; then
      refuse 2 "$portal_dir is not empty; refusing to overwrite"
    fi
  fi

  local super_branch portal_branch
  super_branch="$(git -C "$worktree" rev-parse --abbrev-ref HEAD)"
  portal_branch="${super_branch}-portal"

  git -C "$nested" worktree add -b "$portal_branch" "$portal_dir" "$resolved_sha" \
    || die 1 "git worktree add failed for $portal_dir"
  echo "PORTAL: $portal_dir branch=$portal_branch"

  if [ -z "$node_modules_mode" ]; then
    # DEFAULT MODE: link (none only where the main tree holds no node_modules to link to).
    if [ -d "$nested/node_modules" ]; then
      node_modules_mode="link"
    else
      node_modules_mode="none"
    fi
  fi

  case "$node_modules_mode" in
    link)
      if command -v cmd.exe >/dev/null 2>&1; then
        local win_target win_link
        win_target="$(cygpath -w "$nested/node_modules")"
        win_link="$(cygpath -w "$portal_dir/node_modules")"
        # //J (doubled slash): MSYS's argv path-conversion rewrites a bare "/J" into "J:/" before
        # cmd.exe ever sees it (measured: cmd.exe //c echo /J <path> prints "J:/ <path>"); the same
        # doubled-slash escape already used for //c on this invocation keeps /J literal.
        cmd.exe //c mklink //J "$win_link" "$win_target" >/dev/null \
          || die 1 "mklink /J failed for $win_link -> $win_target"
      else
        ln -s "$nested/node_modules" "$portal_dir/node_modules" \
          || die 1 "ln -s failed for $portal_dir/node_modules"
      fi
      echo "NODE_MODULES: link -> $nested/node_modules"
      ;;
    install)
      guard_install_mode install "$portal_dir"
      command -v bun >/dev/null 2>&1 || refuse 2 "bun not found on PATH; --node-modules install requires PATH-resolved bun"
      ( cd "$portal_dir" && bun install --frozen-lockfile ) || die 1 "bun install failed in $portal_dir"
      echo "NODE_MODULES: install"
      ;;
    none)
      echo "NODE_MODULES: none"
      ;;
    *)
      die 2 "portal: unknown --node-modules mode: $node_modules_mode"
      ;;
  esac

  if [ -x "$portal_dir/node_modules/.bin/tsc" ]; then
    local tsc_out
    tsc_out="$("$portal_dir/node_modules/.bin/tsc" --version 2>&1)"
    echo "TSC: $tsc_out"
  else
    echo "TSC: ABSENT"
  fi
}

# require_nested_initialised <path> -- refuse rc 2, BEFORE anything is created, when the
# MAIN tree's own copy of the named submodule has no .git (never initialised there). The
# exact reason line an issuer's --nested caller relies on (OA-w-1 AC3).
require_nested_initialised() {
  local npath="$1" main
  main="$(main_worktree)"
  if [ ! -e "$main/$npath/.git" ]; then
    refuse 2 "$npath is uninitialised in the main tree (git submodule update --init $npath)"
  fi
}

# provision_nested <worktree> <path> <ref> -- generalises cmd_portal's own nested-worktree
# provisioning (branch naming, ref resolution, non-empty-dir refusal, `worktree add` off the
# MAIN tree's copy) to ANY path .gitmodules maps. No node_modules handling -- that stays
# portal-only (cmd_portal, unchanged).
provision_nested() {
  local worktree="$1" npath="$2" nref="$3"
  local main nested
  main="$(main_worktree)"
  nested="$main/$npath"
  require_nested_initialised "$npath"

  local gitlink_line gitlink_sha
  gitlink_line="$(git -C "$worktree" ls-tree HEAD -- "$npath")"
  gitlink_sha="$(printf '%s' "$gitlink_line" | awk '{print $3}')"
  [ -n "$gitlink_sha" ] || refuse 2 "gitlink sha unresolved for $npath in $worktree"

  local resolved_sha
  if ! resolved_sha="$(git -C "$nested" rev-parse --verify -q "${nref}^{commit}" 2>/dev/null)"; then
    refuse 2 "--nested $npath=$nref does not resolve in $nested"
  fi
  echo "NESTED_REF: $npath $nref -> $resolved_sha"

  local behind_ref
  behind_ref="$(git -C "$nested" rev-list --count "$gitlink_sha".."$resolved_sha" 2>/dev/null)"
  [ -n "$behind_ref" ] || behind_ref="?"
  echo "NESTED_GITLINK: $npath $gitlink_sha behind_ref=$behind_ref"

  local target_dir="$worktree/$npath"
  if [ -d "$target_dir" ]; then
    local entry_count
    entry_count="$(ls -A "$target_dir" 2>/dev/null | wc -l)"
    if [ "$entry_count" -ne 0 ]; then
      refuse 2 "$target_dir is not empty; refusing to overwrite"
    fi
  fi

  local super_branch nested_branch
  super_branch="$(git -C "$worktree" rev-parse --abbrev-ref HEAD)"
  nested_branch="${super_branch}-${npath//\//-}"

  git -C "$nested" worktree add -b "$nested_branch" "$target_dir" "$resolved_sha" \
    || die 1 "git worktree add failed for $target_dir"
  echo "NESTED: $npath -> $target_dir branch=$nested_branch"
}

# order_folders <task-order-file> -- one line per folder the order's <paths> block needs: "F <folder>" for a path present
# at HEAD (a file contributes its parent folder, a folder contributes itself); a path absent at HEAD prints a SKIPPED line.
order_folders() {
  local file="$1" p t d
  tr -d '\r' < "$file" | awk '/^<paths>/{f=1; next} /^<\/paths>/{f=0} f && NF {print}' \
  | while IFS= read -r p; do
      p="$(printf '%s' "$p" | sed 's/^[[:space:]]*//; s/[[:space:]]*$//')"
      p="${p%/}"
      [ -n "$p" ] || continue
      if ! git cat-file -e "HEAD:$p" 2>/dev/null; then
        echo "SKIPPED: <paths> $p is absent at HEAD (not added to the sparse set)"
        continue
      fi
      t="$(git cat-file -t "HEAD:$p")"
      if [ "$t" = "tree" ]; then
        echo "F $p"
      else
        d="$(dirname "$p")"
        [ "$d" = "." ] || echo "F $d"
      fi
    done
}

# FOLDERS: the sparse set for the current provision (global; add_folder de-duplicates).
FOLDERS=()
add_folder() {
  local f="${1%/}" x
  [ -n "$f" ] || return 0
  for x in "${FOLDERS[@]+"${FOLDERS[@]}"}"; do
    [ "$x" = "$f" ] && return 0
  done
  FOLDERS+=("$f")
}

# checked_out_stats <worktree> -- prints "<files> <bytes>": the tracked blobs PRESENT in the worktree (ls-files H
# entries), sized from HEAD's blob sizes (ls-tree -l), never from the disk's cluster size. A gitlink is not a file.
checked_out_stats() {
  local wt="$1" tl tt out
  tl="$(mktemp)" || return 1
  tt="$(mktemp)" || { rm -f "$tl"; return 1; }
  git -C "$wt" ls-files -t | awk '$1=="H"{print substr($0,3)}' > "$tl"
  git -C "$wt" ls-tree -r -l HEAD > "$tt"
  out="$(awk -F'\t' 'FILENAME==ARGV[1]{want[$0]=1; next} { split($1,a," "); if (a[2]=="blob" && ($2 in want)) { n++; b+=a[4] } } END { printf "%d %d", n+0, b+0 }' "$tl" "$tt")"
  rm -f "$tl" "$tt"
  printf '%s' "$out"
}

cmd_provision() {
  if [ $# -lt 2 ]; then
    die 2 "provision: <CODE> <n> required"
  fi
  local code="$1"; shift
  local n="$1"; shift
  local path="" portal_ref="" node_modules_mode="" full="false" full_reason=""
  local nested_specs=() order_files=() sparse_adds=()

  while [ $# -gt 0 ]; do
    case "$1" in
      --path)
        shift; [ $# -gt 0 ] || die 2 "provision: --path requires a value"; path="$1" ;;
      --portal-ref)
        shift; [ $# -gt 0 ] || die 2 "provision: --portal-ref requires a value"; portal_ref="$1" ;;
      --node-modules)
        shift; [ $# -gt 0 ] || die 2 "provision: --node-modules requires a value"; node_modules_mode="$1" ;;
      --nested)
        shift; [ $# -gt 0 ] || die 2 "provision: --nested requires a value (path=ref)"
        nested_specs+=("$1") ;;
      --order)
        shift; [ $# -gt 0 ] || die 2 "provision: --order requires a value (a task-order file)"
        order_files+=("$1") ;;
      --sparse-add)
        shift; [ $# -gt 0 ] || die 2 "provision: --sparse-add requires a value (a folder)"
        sparse_adds+=("$1") ;;
      --full)
        shift; [ $# -gt 0 ] || die 2 "provision: --full requires a reason"
        full="true"; full_reason="$1" ;;
      *)
        die 2 "provision: unknown argument: $1" ;;
    esac
    shift
  done

  [ -n "$path" ] || die 2 "provision: --path <abs-path> is required"
  if [ "$full" = "true" ]; then
    [ -n "$(printf '%s' "$full_reason" | tr -d '[:space:]')" ] \
      || refuse 2 "--full needs a non-empty reason (a full checkout is recorded with its reason); nothing created"
  fi
  local o
  for o in "${order_files[@]+"${order_files[@]}"}"; do
    [ -f "$o" ] || refuse 2 "--order $o is not a file; nothing created"
  done
  guard_install_mode "$node_modules_mode" "$(main_worktree)/portal"

  # The project folder: exactly one org/missions/D*/*/<CODE> directory at HEAD. Checked BEFORE anything is created.
  local pf_hits pf_count
  pf_hits="$(git ls-tree -r -d --name-only HEAD -- org/missions | grep -E "^org/missions/D[^/]*/[^/]+/${code}\$" || true)"
  pf_count="$(printf '%s\n' "$pf_hits" | grep -c . || true)"
  [ "$pf_count" -le 1 ] || refuse 2 "org/missions/D*/*/$code names $pf_count directories at HEAD (one expected); nothing created"

  FOLDERS=()
  if [ "$full" = "false" ]; then
    add_folder ".tools"
    add_folder "lib"
    if [ "$pf_count" -eq 1 ]; then
      add_folder "$pf_hits"
    else
      echo "WARN: no org/missions/D*/*/$code directory at HEAD; the project folder is not in the sparse set"
    fi
    local line sa sa_c
    for o in "${order_files[@]+"${order_files[@]}"}"; do
      while IFS= read -r line; do
        case "$line" in
          "F "*) add_folder "${line#F }" ;;
          *) echo "$line" ;;
        esac
      done < <(order_folders "$o")
    done
    for sa in "${sparse_adds[@]+"${sparse_adds[@]}"}"; do
      sa_c="${sa%/}"
      if git cat-file -e "HEAD:$sa_c" 2>/dev/null; then
        add_folder "$sa_c"
      else
        echo "SKIPPED: --sparse-add $sa is absent at HEAD (not added to the sparse set)"
      fi
    done
  elif [ "${#order_files[@]}" -gt 0 ] || [ "${#sparse_adds[@]}" -gt 0 ]; then
    echo "NOTE: --order and --sparse-add are ignored in full mode"
  fi

  # Validate EVERY --nested spec against the MAIN tree BEFORE anything is created (super
  # worktree included) -- OA-w-1 AC3: the refusal names the path and creates nothing.
  local spec npath nref
  if [ "${#nested_specs[@]}" -gt 0 ]; then
    for spec in "${nested_specs[@]}"; do
      npath="${spec%%=*}"
      nref="${spec#*=}"
      [ -n "$npath" ] && [ "$npath" != "$spec" ] || die 2 "provision: --nested requires path=ref (got: $spec)"
      require_nested_initialised "$npath"
    done
  fi

  local branch="wk-${code}-${n}"
  local base_sha
  base_sha="$(git rev-parse HEAD)"
  if [ "$full" = "true" ]; then
    git worktree add -b "$branch" "$path" HEAD || die 1 "git worktree add failed for $path"
  else
    git worktree add --no-checkout -b "$branch" "$path" HEAD || die 1 "git worktree add failed for $path"
    git -C "$path" sparse-checkout init --cone || die 1 "sparse-checkout init --cone failed for $path"
    git -C "$path" sparse-checkout set "${FOLDERS[@]}" || die 1 "sparse-checkout set failed for $path"
    git -C "$path" checkout -q HEAD || die 1 "checkout of HEAD failed in $path"
  fi
  echo "WORKTREE: $path branch=$branch base=$base_sha"
  local stats files bytes
  stats="$(checked_out_stats "$path")"
  files="${stats% *}"
  bytes="${stats#* }"
  if [ "$full" = "true" ]; then
    echo "PROVISIONED $path branch=$branch mode=full reason=$full_reason files=$files bytes=$bytes"
  else
    echo "PROVISIONED $path branch=$branch mode=sparse folders=${#FOLDERS[@]} files=$files bytes=$bytes"
  fi

  local portal_args=("$path")
  [ -n "$portal_ref" ] && portal_args+=(--portal-ref "$portal_ref")
  [ -n "$node_modules_mode" ] && portal_args+=(--node-modules "$node_modules_mode")
  cmd_portal "${portal_args[@]}"

  if [ "${#nested_specs[@]}" -gt 0 ]; then
    for spec in "${nested_specs[@]}"; do
      npath="${spec%%=*}"
      nref="${spec#*=}"
      provision_nested "$path" "$npath" "$nref"
    done
  fi
}

cmd_remove() {
  if [ $# -lt 1 ]; then
    die 2 "remove: <worktree-path> required"
  fi
  local worktree="$1"; shift
  local portal_only="false"

  while [ $# -gt 0 ]; do
    case "$1" in
      --portal-only) portal_only="true" ;;
      *) die 2 "remove: unknown argument: $1" ;;
    esac
    shift
  done

  local main nested portal_dir
  main="$(main_worktree)"
  nested="$main/portal"
  portal_dir="$worktree/portal"

  if [ -d "$portal_dir" ] && [ -e "$portal_dir/.git" ]; then
    # The node_modules link (a junction or a symlink) is UNTRACKED, so `git worktree remove` -- which
    # only clears the worktree's tracked/admin content -- leaves it on disk as an orphan and never
    # recurses into it (measured: the linked target's file count is unchanged by either step). Unlink
    # it explicitly, first, so the directory `git worktree remove` clears is left fully empty.
    if [ -L "$portal_dir/node_modules" ]; then
      rm "$portal_dir/node_modules" 2>&1 || echo "WARN: could not unlink $portal_dir/node_modules" >&2
    fi
    git -C "$nested" worktree remove --force "$portal_dir" \
      || echo "WARN: git worktree remove reported an issue for $portal_dir" >&2
  fi
  # ISSUER REPAIR (row W60-S3): recreate the empty gitlink placeholder so the superproject's own
  # status reads clean (never "D portal"), and NEVER run `worktree prune` here -- a prune clears
  # every unrelated pre-existing prunable entry in the nested repository's worktree list, which
  # AC5 forbids; `git worktree remove` above already drops this call's own entry on its own.
  mkdir -p "$portal_dir"
  echo "REMOVED: $portal_dir"

  # GENERALISED (OA-w-1): tear down every OTHER provisioned nested worktree the SAME way
  # (placeholder recreated empty, no `worktree prune` -- the W60-S3 repair above, generalised).
  # portal is excluded here (handled by name above, unchanged); node_modules unlink stays
  # portal-only because only cmd_portal ever links one.
  local gm="$worktree/.gitmodules"
  if [ -s "$gm" ]; then
    local npath ndir ntarget
    while IFS= read -r npath; do
      [ -z "$npath" ] && continue
      [ "$npath" = "portal" ] && continue
      ndir="$main/$npath"
      ntarget="$worktree/$npath"
      if [ -d "$ntarget" ] && [ -e "$ntarget/.git" ]; then
        git -C "$ndir" worktree remove --force "$ntarget" \
          || echo "WARN: git worktree remove reported an issue for $ntarget" >&2
        mkdir -p "$ntarget"
        echo "REMOVED: $ntarget"
      fi
    done < <(git config -f "$gm" --get-regexp '\.path$' 2>/dev/null | awk '{print $2}')
  fi

  if [ "$portal_only" = "false" ]; then
    git worktree remove --force "$worktree" || die 1 "git worktree remove failed for $worktree"
    echo "REMOVED: $worktree"
  fi

  local listing listing_count total
  listing="$(git -C "$nested" worktree list)"
  listing_count="$(printf '%s\n' "$listing" | grep -F -c "$portal_dir" || true)"
  total="$(printf '%s\n' "$listing" | grep -c . || true)"
  echo "PORTAL_WORKTREES_LISTING_PATH: $listing_count of $total"
}

cmd_self_test() {
  local repo_root scratch_base tmp_base
  repo_root="$(git rev-parse --show-toplevel)"
  scratch_base="$repo_root/.scratch"
  mkdir -p "$scratch_base"
  tmp_base="$(mktemp -d "$scratch_base/wkprov-selftest.XXXXXX")"

  local main nested
  main="$(main_worktree)"
  nested="$main/portal"

  local fail=0
  local total=8

  local wt1="$tmp_base/wt1"
  local wt2="$tmp_base/wt2"
  local wt3="$tmp_base/wt3"
  local wt4="$tmp_base/wt4"
  local orphan_portal="$tmp_base/orphan-portal"

  echo "== ARM 1: portal provisions at the nested repository's HEAD =="
  # --no-checkout: a stand-in superproject worktree needs no full working-tree checkout (the
  # superproject's own checkout cost is unrelated to what this arm tests); "git checkout HEAD --
  # portal" alone then populates just the gitlink placeholder THROUGH GIT'S OWN CHECKOUT MACHINERY
  # -- a plain "mkdir -p" produces a directory that LOOKS the same but leaves the worktree's index
  # unreconciled, so "git status" reports it "D portal" forever after (measured: a real full
  # checkout reads clean immediately; --no-checkout + mkdir reads "D portal" both before AND after
  # the gitlink is touched). ARM5 checks status, so it needs the real placeholder, not the look-alike.
  git worktree add --no-checkout -b wk-selftest-rk60-1 "$wt1" HEAD >/dev/null 2>&1
  git -C "$wt1" checkout HEAD -- portal
  local arm1_out arm1_rc
  arm1_out="$(bash "$0" portal "$wt1" 2>&1)"; arm1_rc=$?
  echo "$arm1_out"
  local arm1_ok="true"
  [ "$arm1_rc" -eq 0 ] || arm1_ok="false"
  [ -f "$wt1/portal/package.json" ] || arm1_ok="false"
  local expected_sha actual_sha actual_branch
  expected_sha="$(git -C "$nested" rev-parse HEAD)"
  actual_sha="$(git -C "$wt1/portal" rev-parse HEAD 2>/dev/null || echo "")"
  [ "$actual_sha" = "$expected_sha" ] || arm1_ok="false"
  actual_branch="$(git -C "$wt1/portal" rev-parse --abbrev-ref HEAD 2>/dev/null || echo "")"
  [ "$actual_branch" = "wk-selftest-rk60-1-portal" ] || arm1_ok="false"
  if [ "$arm1_ok" = "true" ]; then echo "ARM1: PASS"; else echo "ARM1: FAIL"; fail=$((fail + 1)); fi

  echo "== ARM 2: a bad --portal-ref refuses rc 2, creates nothing =="
  git worktree add --no-checkout -b wk-selftest-rk60-2 "$wt2" HEAD >/dev/null 2>&1
  git -C "$wt2" checkout HEAD -- portal
  local arm2_out arm2_rc
  arm2_out="$(bash "$0" portal "$wt2" --portal-ref no-such-ref-rk60 2>&1)"; arm2_rc=$?
  echo "$arm2_out"
  local arm2_ok="true"
  [ "$arm2_rc" -eq 2 ] || arm2_ok="false"
  local wt2_portal_count
  wt2_portal_count="$(ls -A "$wt2/portal" 2>/dev/null | wc -l)"
  [ "$wt2_portal_count" -eq 0 ] || arm2_ok="false"
  if [ "$arm2_ok" = "true" ]; then echo "ARM2: PASS"; else echo "ARM2: FAIL"; fail=$((fail + 1)); fi

  echo "== ARM 3: a non-empty portal/ refuses rc 2 =="
  git worktree add --no-checkout -b wk-selftest-rk60-3 "$wt3" HEAD >/dev/null 2>&1
  git -C "$wt3" checkout HEAD -- portal
  echo "placeholder" > "$wt3/portal/dummy.txt"
  local arm3_out arm3_rc
  arm3_out="$(bash "$0" portal "$wt3" 2>&1)"; arm3_rc=$?
  echo "$arm3_out"
  local arm3_ok="true"
  [ "$arm3_rc" -eq 2 ] || arm3_ok="false"
  if [ "$arm3_ok" = "true" ]; then echo "ARM3: PASS"; else echo "ARM3: FAIL"; fail=$((fail + 1)); fi
  rm -f "$wt3/portal/dummy.txt"

  echo "== ARM 4: link mode resolves ./node_modules/.bin/tsc --version =="
  local arm4_ok="true"
  if [ -x "$wt1/portal/node_modules/.bin/tsc" ]; then
    local tsc_out tsc_rc
    tsc_out="$("$wt1/portal/node_modules/.bin/tsc" --version 2>&1)"; tsc_rc=$?
    echo "$tsc_out"
    [ "$tsc_rc" -eq 0 ] || arm4_ok="false"
  else
    echo "tsc binary absent at $wt1/portal/node_modules/.bin/tsc"
    arm4_ok="false"
  fi
  if [ "$arm4_ok" = "true" ]; then echo "ARM4: PASS"; else echo "ARM4: FAIL"; fail=$((fail + 1)); fi

  echo "== ARM 5: remove --portal-only leaves the nested worktree list without the path, and recreates the empty placeholder =="
  local arm5_out arm5_rc
  arm5_out="$(bash "$0" remove "$wt1" --portal-only 2>&1)"; arm5_rc=$?
  echo "$arm5_out"
  local arm5_ok="true"
  [ "$arm5_rc" -eq 0 ] || arm5_ok="false"
  if git -C "$nested" worktree list | grep -F -q "$wt1/portal"; then arm5_ok="false"; fi
  [ -d "$wt1/portal" ] || arm5_ok="false"
  local wt1_portal_count
  wt1_portal_count="$(ls -A "$wt1/portal" 2>/dev/null | wc -l)"
  [ "$wt1_portal_count" -eq 0 ] || arm5_ok="false"
  local wt1_status
  wt1_status="$(git -C "$wt1" status --short -- portal 2>&1)"
  [ -z "$wt1_status" ] || arm5_ok="false"
  if [ "$arm5_ok" = "true" ]; then echo "ARM5: PASS"; else echo "ARM5: FAIL"; fail=$((fail + 1)); fi

  echo "== ARM 6: no worktree prune runs -- an unrelated pre-existing prunable entry survives =="
  git worktree add --no-checkout -b wk-selftest-rk60-4 "$wt4" HEAD >/dev/null 2>&1
  git -C "$wt4" checkout HEAD -- portal
  bash "$0" portal "$wt4" >/dev/null 2>&1
  # Manufacture an UNRELATED prunable entry in the nested repository's own worktree list: add a
  # worktree, then delete its directory OUTSIDE git so git itself marks it "prunable" on next list.
  git -C "$nested" worktree add --no-checkout -b wk-selftest-rk60-orphan-portal "$orphan_portal" HEAD >/dev/null 2>&1
  rm -rf "$orphan_portal"
  local arm6_ok="true"
  if ! git -C "$nested" worktree list | grep -F "$orphan_portal" | grep -q "prunable"; then
    echo "WARN: could not manufacture the orphan prunable entry; arm6 cannot discriminate"
    arm6_ok="false"
  fi
  local arm6_out arm6_rc
  arm6_out="$(bash "$0" remove "$wt4" --portal-only 2>&1)"; arm6_rc=$?
  echo "$arm6_out"
  [ "$arm6_rc" -eq 0 ] || arm6_ok="false"
  # The orphan entry must STILL be listed (prunable or not) -- if `remove` ever ran `worktree
  # prune`, this entry would be gone.
  if ! git -C "$nested" worktree list | grep -F -q "$orphan_portal"; then arm6_ok="false"; fi
  [ -d "$wt4/portal" ] || arm6_ok="false"
  local wt4_portal_count
  wt4_portal_count="$(ls -A "$wt4/portal" 2>/dev/null | wc -l)"
  [ "$wt4_portal_count" -eq 0 ] || arm6_ok="false"
  # Scope the check to cmd_remove's OWN body (the self-test's cleanup, further down in this same
  # file, legitimately calls "worktree prune" on itself -- a whole-file grep would match that and
  # fail ARM6 unconditionally regardless of what cmd_remove does). Comment lines are stripped too:
  # cmd_remove's own repair comment says "NEVER run `worktree prune` here", which contains the
  # literal phrase without calling it.
  if sed -n '/^cmd_remove()/,/^}/p' "$0" | grep -v '^[[:space:]]*#' | grep -q "worktree prune"; then
    echo "ERROR: cmd_remove's own body still calls \"worktree prune\""
    arm6_ok="false"
  fi
  if [ "$arm6_ok" = "true" ]; then echo "ARM6: PASS"; else echo "ARM6: FAIL"; fail=$((fail + 1)); fi

  echo "== ARM 7: full cleanup -- every branch and worktree the self-test created is gone =="
  git worktree remove --force "$wt1" >/dev/null 2>&1
  git worktree remove --force "$wt2" >/dev/null 2>&1
  git worktree remove --force "$wt3" >/dev/null 2>&1
  git worktree remove --force "$wt4" >/dev/null 2>&1
  # NEVER a repo-wide "git worktree prune" here (superproject): the leftovers check below (the
  # tmp_base / branch --list greps) is what catches a failed explicit removal above -- a
  # repo-wide prune would silently erase the evidence of that failure, and it would also erase
  # every OTHER seat's own prunable worktree registrations in this same repository.
  local arm7_ok="true"
  # Swept by PATTERN, not by one hardcoded name per arm: a hardcoded list silently misses any
  # branch a later arm creates (measured -- "wk-selftest-rk60-4-portal", created by ARM6's own
  # provision call, was never in this list and survived every prior version of this cleanup).
  # This is the self-test's OWN cleanup of ITS manufactured orphan entry (ARM6), never the
  # `remove` verb's behavior under test (which is proven by ARM6 to never prune). A repo-wide
  # "git -C $nested worktree prune" would clear ARM6's own orphan so the orphan's own branch
  # (wk-selftest-rk60-orphan-portal) can be deleted by the branch-delete loop below -- but it
  # would ALSO clear every OTHER prunable entry in the nested repository, which is exactly the
  # W60-S3-class hazard this arm exists to close. So locate and remove ONLY the ONE admin entry
  # that is ARM6's own orphan: read every
  # "$(git -C "$nested" rev-parse --absolute-git-dir)/worktrees/*/gitdir" file (the gitdir file
  # names "<worktree path>/.git") and select the entry whose target, normalized, equals
  # $orphan_portal normalized -- this box's git prints "C:/..." forward-slash paths while
  # $orphan_portal may carry the same path in the MSYS "/c/..." form, so both sides are run
  # through "cygpath -m" before comparing. This runs BEFORE the branch-delete loop below: a
  # branch still referenced by a prunable-but-unpruned worktree admin entry is still "used by
  # worktree" as far as `branch -D` is concerned, so removing the orphan's own admin entry first
  # is what lets its branch delete succeed. If the match is not exactly one, this is an ARM7
  # FAIL naming the count -- never a fallback to a repo-wide prune.
  local nested_git_dir orphan_norm match_count match_admin_dir gitdir_file entry_target entry_norm
  nested_git_dir="$(git -C "$nested" rev-parse --absolute-git-dir)"
  orphan_norm="$(cygpath -m "$orphan_portal" 2>/dev/null || echo "$orphan_portal")"
  match_count=0
  match_admin_dir=""
  if [ -d "$nested_git_dir/worktrees" ]; then
    for gitdir_file in "$nested_git_dir"/worktrees/*/gitdir; do
      [ -e "$gitdir_file" ] || continue
      entry_target="$(cat "$gitdir_file" 2>/dev/null)"
      entry_target="${entry_target%/.git}"
      entry_norm="$(cygpath -m "$entry_target" 2>/dev/null || echo "$entry_target")"
      if [ "$entry_norm" = "$orphan_norm" ]; then
        match_count=$((match_count + 1))
        match_admin_dir="$(dirname "$gitdir_file")"
      fi
    done
  fi
  echo "ORPHAN_ADMIN_MATCH: count=$match_count dir=$match_admin_dir orphan_norm=$orphan_norm"
  if [ "$match_count" -eq 1 ]; then
    rm -rf "$match_admin_dir"
  else
    echo "ERROR: expected exactly 1 admin entry matching the orphan, found $match_count"
    arm7_ok="false"
  fi
  local b
  for b in $(git branch --list 'wk-selftest-rk60-*' | awk '{print $NF}'); do
    git branch -D "$b" >/dev/null 2>&1
  done
  for b in $(git -C "$nested" branch --list 'wk-selftest-rk60-*' | awk '{print $NF}'); do
    git -C "$nested" branch -D "$b" >/dev/null 2>&1
  done
  rm -rf "$tmp_base"

  if git worktree list | grep -F -q "$tmp_base"; then arm7_ok="false"; fi
  if git -C "$nested" worktree list | grep -F -q "$tmp_base"; then arm7_ok="false"; fi
  if git branch --list 'wk-selftest-rk60-*' | grep -q .; then arm7_ok="false"; fi
  if git -C "$nested" branch --list 'wk-selftest-rk60-*-portal' | grep -q .; then arm7_ok="false"; fi
  if [ "$arm7_ok" = "true" ]; then echo "ARM7: PASS"; else echo "ARM7: FAIL"; fail=$((fail + 1)); fi

  echo "== ARM 8: cmd_self_test's own body invokes no git worktree prune =="
  local arm8_ok="true"
  local self_test_prune_invocations
  self_test_prune_invocations="$(sed -n '/^cmd_self_test()/,/^}/p' "$0" | grep -v '^[[:space:]]*#' | grep -cE '^[[:space:]]*git( -C [^ ]+)? worktree prune')"
  if [ "$self_test_prune_invocations" -ne 0 ]; then
    echo "ERROR: cmd_self_test's own body still invokes \"worktree prune\" ($self_test_prune_invocations time(s))"
    arm8_ok="false"
  fi
  if [ "$arm8_ok" = "true" ]; then echo "ARM8: PASS"; else echo "ARM8: FAIL"; fail=$((fail + 1)); fi

  echo "RESULT: $fail arm(s) failed of $total"
  [ "$fail" -eq 0 ]
}

main() {
  local verb="${1:-}"
  case "$verb" in
    provision) shift; cmd_provision "$@" ;;
    portal) shift; cmd_portal "$@" ;;
    remove) shift; cmd_remove "$@" ;;
    --self-test) cmd_self_test ;;
    *) usage; die 2 "unknown verb: $verb" ;;
  esac
}

main "$@"
