#!/bin/sh
# fabric-activity-post-commit.sh -- after every commit, this box writes one record of what it changed to the shared
# activity store, so any box can ask "who else is working on this?" (.tools/fabric-activity.py; Andrew-direct
# 2026-10-08 ~16:5xZ, 4.0.0_SA_CRO). NON-BLOCKING by construction: backgrounded, a hard 60 s ceiling, every failure
# spools locally and exits 0. It ends itself: one put, then exit; nothing stays resident.
_ws="$(git rev-parse --show-toplevel 2>/dev/null)" || exit 0
[ -n "$_ws" ] || exit 0
[ -f "$_ws/.tools/fabric-activity.py" ] || exit 0
_sha="$(git -C "$_ws" rev-parse HEAD 2>/dev/null)" || exit 0
if command -v timeout >/dev/null 2>&1; then
  ( cd "$_ws" && timeout 60 python "$_ws/.tools/fabric-activity.py" emit --commit "$_sha" >/dev/null 2>&1 ) &
else
  ( cd "$_ws" && python "$_ws/.tools/fabric-activity.py" emit --commit "$_sha" >/dev/null 2>&1 ) &
fi
exit 0
