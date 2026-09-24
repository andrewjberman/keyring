#!/usr/bin/env bash
# memory-write-guard.sh -- PreToolUse (Write|Edit): seats do not write lessons to the auto-memory directory.
#
# Andrew-direct 2026-09-24 ~17:0xZ ("yes instead of the cap"), record
# org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260924_170xZ_MEMORY_PREFERENCES_ONLY_AND_THREE_HELD_ITEMS_YES.md:
# MEMORY.md holds his stable preferences only; a lesson that matters becomes a gate, field or skill fix by its owning
# seat, and an incident stays in git history. Refused: any Write or Edit to a file under a
# .claude/projects/<project>/memory/ directory other than MEMORY.md, and a MEMORY.md write that leaves it over 3 KB and
# larger than it was. FAST PATH: a payload that does not name a memory directory exits at once; a parse failure admits.
INPUT=$(cat 2>/dev/null || true)
case "$INPUT" in *memory*) ;; *) exit 0 ;; esac
printf '%s' "$INPUT" | python "$(cd "$(dirname "$0")" && pwd)/memory_write_guard.py" 2>/dev/null
exit 0
