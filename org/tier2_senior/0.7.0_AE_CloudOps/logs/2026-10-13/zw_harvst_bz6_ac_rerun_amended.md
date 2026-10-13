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

**Corroboration from outside the script, and what the reboot proved.** This box booted at 18:57:31Z
(`LastBootUpTime`, measured), between the 15:1xZ/15:2xZ mints and this 19:2xZ read. The reboot was ANNOUNCED for about
17:51Z and did not happen then; a sibling read of mine at 18:25Z had already measured no boot, so the announced time
is not the measured one and this log uses the measured one. `wsj.dpapi` (11478B, mtime 15:11Z) and `barrons.dpapi` (20614B, mtime 15:20Z) are
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

---

## Addendum, 2026-10-13T19:55Z -- HVST-bz-7's two records arrived, and neither is a pass

**archetype:** DIAGNOSE

Next Step 2 above said bz-7 was on an organic wait with both publishers printing `NONE`. That is now stale, and the
record it was waiting for says something more interesting than a pass or a fail.

Both publishers have ended a cycle since the windowless cut, and **both ended `STOPPED=sign_in_refused`** -- after
bz-6 gave each of them a saved session that still reads `VALID=True`. bz-7's AC1 does NOT match. Per that order's
step 3 this is a RECORDED RESULT and not a pass: row **`AMGT_HARVST-Z-S119`** filed (BLOCKING / INERT, `disarm_owner`
`2.0.0_SA_COO~W1`), the order STAYS OPEN, and nothing was driven to move a line.

**One `STOPPED=` token, two different behaviours.** The detail string is identical for both
(`SignInRefused: 401 under --no-sign-in: no refresh`), which is exactly why the records were opened rather than the
line graded:

| | wsj `20261013T173708Z` | barrons `20261013T184606Z` |
|---|---|---|
| ran | 17:37:08Z -> 18:46:05Z (**69 min**) | 18:46:06Z -> 18:46:27Z (**21 s**) |
| collected / pairs done | **35 / 35** (`no_new_articles` x35), uploads 1 | **0 / 0** |
| never started | 206 | 241 |
| failed on | `security-d7660d8c73fc8217`, after 35 good pairs | `security-b0fe721e1f2a0d8b`, its FIRST key |

**The negative arm is measured, not assumed.** Each publisher's three cycles BEFORE bz-6 (2026-10-12 07:18Z, 07:48Z,
19:16Z) each lasted ONE SECOND with `collected=0`, `pairs_done=0`, `never_started=241`. So bz-6's session measurably
changed wsj (1 s / 0 pairs -> 69 min / 35 pairs) and measurably did not change barrons' pair count. "Both still
`sign_in_refused`" is true and is the least informative true sentence available about these two records.

**What it is not.** Not the operator and not the reboot: both run summaries read `interrupted=false` and
`stopped_by_operator=false`, and both cycles ENDED before the box booted at 18:57:31Z. Not a two-vault mismatch: the
registered task's `--runtime-root` and live PID 8792's `--runtime-root` are both exactly the path bz-6 minted into and
AC1/AC2 read. The runner auto-restarted 17 s after boot and is cycling bbg now, so the pass order is intact.

**The coexistence is the finding.** barrons was refused at 18:46Z and still read `VALID=True` at 19:28:40Z, 42 minutes
LATER, off the same unchanged vault file. `VALID=True` is a LOCAL predicate -- present + subscriber +
network_auth_corroborated + age -- and carries no claim about what the vendor will accept. A session that is valid at
mint and 401s 69 minutes later is a REFRESH problem wearing a sign-in refusal's name; whether bz-6's endpoint can be
met by a saved session at all while the runner forbids refresh is the issuer's call, and the row asks it.

**Also corrected here:** this log and the bz-6 instance first said site Z "rebooted at about 17:51Z". That was the
ANNOUNCED time. `LastBootUpTime` reads **18:57:31Z**, and a sibling read of mine at 18:25Z had already measured no
boot. Both carriers now use the measured time. The substance is unchanged -- a boot did fall between the mints and the
re-run, and both saved sessions survived it.

bz-7's step 2 is done for both publishers: each `.cycle.json` copied byte for byte with its SHA-256 and length beside
the source's (`round84/bz7_wsj_cycle_record.json`, `round84/bz7_barrons_cycle_record.json`), and the read appended to
`round84/bz7_read.out` as a third section.
