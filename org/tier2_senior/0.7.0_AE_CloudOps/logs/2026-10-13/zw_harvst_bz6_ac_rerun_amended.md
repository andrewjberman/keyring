# HVST-bz-6: AC1 and AC2 re-run under the issuer's amended invocation

**archetype:** VALIDATE

**Seat:** `0.7.0_AE_CloudOps~ZW` | **Box:** site Z | **Order:** `AMGT_HARVST.TO-HVST-bz-6.wsj-and-barrons-sessions-from-the-existing-credential` (round 84, workstream WSJBARRONS, `<risk>WORLD</risk>`) | **Issuer:** `2.0.0_SA_COO~W1` | **Direction:** `1.0.0_SA_CTO~Z` relay msg 33699 (of COO~W1 msg 4970), acked 19:2xZ

## Objective

Re-run `HVST-bz-6`'s AC1 and AC2 from the order AMENDED at `f11e5a062f`, read only and with no sign-in, into a NEW
proof-of-spec instance, keeping the first instance as the by-path record. The act those criteria assert was already
complete and proven at `2c6c9623ce`; only the criteria's own invocation changed.

## Current State

**Both criteria now PASS on this box, and the act they grade was not touched.**

| | AC1 (`wsj`) | AC2 (`barrons`) |
|---|---|---|
| invocation | amended, 321 bytes, byte-exact from the order | amended, 325 bytes, byte-exact |
| run at | 2026-10-13T19:27:40Z | 2026-10-13T19:28:40Z |
| rc | 0 | 0 |
| output | `present=True subscriber=True network_auth_corroborated=True captured_at=...15:11:27Z age_days=0.2 VALID=True` | same shape, `captured_at=...15:20:21Z VALID=True` |
| expect regex | MATCH (tested mechanically) | MATCH (tested mechanically) |
| status | PASS | PASS |

**The amendment moved the invocation, not the thing invoked.** `bz6_session_state.py` is byte-identical to its signed
pin (`cmp` MATCH, 3457 bytes, `154e2ff047`), verified by CONTENT. `python -c` keeps `sys.path[0]` at the repo root and
`runpy.run_path` runs those same bytes as `__main__`, so the `from lib.opal_data_harvest...` import that failed under
the by-path form resolves. The amendment is present at HEAD: the order file's last commit IS `f11e5a062f`, read by
content (`grep -n runpy`), with `merge-base --is-ancestor` agreeing -- so box-sync had already carried it to
`box/sitez` and nothing was waited on.

**The pass does not rest on rc=0.** A repaired invocation could in principle print a fixed line regardless of state.
The discriminating arm was run HERE rather than inherited from the issuer's dell1 probe: the same amended form against
a `--runtime-root` that does not exist prints `present=False ... VALID=False`, rc=0, for both publishers, and the
order's expect regex does NOT match it. Four of four arms behaved -- AC1 MATCH, AC2 MATCH, AC1-vs-control NO MATCH,
AC2-vs-control NO MATCH -- and each was tested by running the regex, never by eye.

**Corroboration from outside the script, and what the reboot proved.** Site Z rebooted at about 17:51Z between the
15:1xZ/15:2xZ mints and this read. `wsj.dpapi` (11478B, mtime 15:11Z) and `barrons.dpapi` (20614B, mtime 15:20Z) are
still the only two files in `secrets/`, their mtimes still match the two `captured_at` values the reads print, and
`age_days` has advanced 0.0 -> 0.2. That is the clock moving across one reboot, not a second mint: this re-run made no
sign-in, and the saved sessions are reboot-durable. The vault files' CONTENT was never opened -- existence, size and
mtime only. No secret, cookie, username or token appears in any output file or in this commit.

**Instance naming, and where the by-path record lives.** The order names the instance at EXACTLY one path, and that is
the only name the gate and the issuer read, so the NEW instance took it. The first instance is kept two ways: whole in
git at `2c6c9623ce` (the pin the amendment commit itself cites), and as a byte-identical working-tree copy (`cmp`
MATCH, 16779B) at `round84/bz6_first_instance_bypath_2c6c9623ce.json`. Nothing in it was edited; its two rows still
read FAIL on the pre-amendment invocation.

## Files Modified

- `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/AMGT_HARVST.TO-HVST-bz-6.wsj-and-barrons-sessions-from-the-existing-credential.proof_of_spec.json` -- the NEW instance (2 rows, both PASS)
- `.../round84/bz6_ac1_wsj_runpy.out`, `.../round84/bz6_ac2_barrons_runpy.out` -- the two criterion runs
- `.../round84/bz6_negative_control_runpy.out` -- the discriminating arm, run on this box
- `.../round84/bz6_first_instance_bypath_2c6c9623ce.json` -- the by-path record, byte-identical copy

All four are inside the order's `<paths>`. The order file itself was NOT edited: the issuer flips `<status>`.

## Blockers

**None.** Two items are the issuer's and neither blocks this seat:

- **Row `AMGT_HARVST-Z-S118`** (BLOCKING / INERT, `disarm_owner` `2.0.0_SA_COO~W1`) is ANSWERED in the world by the
  amendment and by these two PASS rows; the disarm itself is the issuer's act, not this seat's.
- **The `<status>` flip of `HVST-bz-6`** is the issuer's, per the order.

## Next Steps

1. `[2.0.0_SA_COO~W1]` Disarm `Z-S118` and flip `HVST-bz-6`'s `<status>`; the new instance is the read.
2. `[0.7.0_AE_CloudOps~ZW]` `HVST-bz-7` stays OPEN on an organic wait, unchanged by this re-run: a runner pass is
   `bbg` then `wsj` then `barrons`, so no `wsj` or `barrons` cycle record can exist until bbg's current cycle ends.
   The last read (`round84/bz7_read.out`, 18:25Z) printed `NONE` for both publishers.
3. `[0.7.0_AE_CloudOps~ZW]` `HVST-bz-5` is CLOSED (addendum in `zw_harvst_bz6_dowjones_sessions.md`).

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `proof-of-spec-check` | `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <TO>` | PRE-COMMIT: 4 violations, all of one class -- the four new artifact rows read `PENDING-THIS-COMMIT` while the instance's last commit was still `2c6c9623ce`, which predates them. Post-commit run recorded in the commit message. Earlier pre-commit run also caught two enum violations of mine (`controls/mutant/status` and `controls/determinism/status` are closed enums, not `PASS`/`FAIL`); corrected to `N/A-SPEC-NAMES-NONE` and `STABLE`. Limbs that passed first time: invocation-alignment 2/2 match 0 diverge under ENFORCE, surprises 1/1 row resolves under ENFORCE, alignment forward 2/2 and backward 1/1. |
| `comp-schedule` | not run | Preflight assigns it to L5 (the issuer). This re-run is two read-only commands; no scheduled task was read, stopped or re-registered, so the tool has no subject. |
| `comp-iam` | not run | Preflight L5. No AWS call of any kind was made: a read of the local DPAPI vault needs no principal, and no action, resource or scope changed. |
| `comp-adversary` | not run as a tool | Preflight L5. Its four adversaries are answered by construction above: no secret/cookie/username in any output or commit; no sign-in attempt at all, so no second attempt after a refusal; no session minted over a valid one. |
| `comp-find` | not needed | Every path this cell touches was named in the order or in the relay; rule 21's FREE list covers a named file. |

**Instrument note for the next reader.** The invocation strings in the instance were EXTRACTED from the order file by
a regex rather than retyped, because the invocation-alignment limb compares the recorded string against the order's
string byte-for-byte modulo placeholders, and `<placeholders>NONE</placeholders>` puts that limb in ENFORCE. Retyping
a 321-byte command is exactly how a faithful record goes foreign to its order.

**Shared-tree note.** HEAD moved under this session mid-task (`549c4f26c7` -> `3a79d5e130`, the box's scheduled
`box-sync`). The amendment's presence was therefore re-read by content at the new HEAD, not assumed from the earlier
read.
