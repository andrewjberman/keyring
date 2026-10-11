# 0.7.0_AE_CloudOps~TRL -- the check-inbox workaround is LD-0202-blind for a lane

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE

**Window:** 2026-10-09 20:30Z -> 20:50Z (delta since `work_1500-1735Z_ka21.md`)
**Device:** laptop | **Branch:** `box/laptop` | **Serial:** `0.7.0_AE_CloudOps~TRL`

---

## Summary

No task order in this window. A tooling gap I surfaced at 20:31Z came back ruled at 20:34Z
(CTO msg 108114 via `2.0.0_SA_COO~C` msg 108116, acked): the fix is a named `check-inbox`
forwarder in `.tools/provision-path-shims.sh` owned by `0.8.0_AE_CloudComp~D`, nothing for this
seat to build, and until it lands call `bash org/mcp/check-inbox.sh` directly.

**I exercised that workaround instead of taking it on faith, and it is blind for a `~lane`
serial.** Routed back with one ask. The ruled fix would otherwise ship the blindness fabric-wide.

---

## What was found

`org/mcp/check-inbox.sh:49` builds the lane path as:

```
INBOX_INSTANCE_DIR="$INBOX_BASE/${AGENT_DIR}~${SUFFIX}"      # FLAT
```

with no nested fallback -- `INBOX_DIRS` for a lane caller is (flat instance dir, base dir). The
canonical lane inbox is NESTED, `inbox/{base}/~{lane}/`, and `org/XXX.md`'s own reference table
calls the flat form **"the DEAD answer -- never"**, written by nothing and read by nothing
(LD-0202).

Consequences, in order of how much they matter:

1. **For a `~lane` serial, its `No pending messages` is unfalsifiable for the lane's own mail.**
   It can only ever see base-dir broadcasts. An empty result and a wrong directory read
   identically -- which is why a bare "it returned cleanly" was not accepted as evidence here.
2. **Line 50's `mkdir -p` MINTS the dead dir.** One call created
   `org/mcp/inbox/0.7.0_AE_CloudOps~TRL/read/`.
3. **No mail has ever been lost.** Measured, with a control: **0 of 23** flat lane dirs hold any
   `.md` (unread or read), against **165 of 167** nested dirs that do. So the zero is a fact about
   the flat form, not about the counter. The 23 are empty shells readers created, exactly as
   LD-0202 predicts.

Denominator for the shape census: 74 base inbox dirs; 23 FLAT `inbox/<base>~<lane>/`; 167 NESTED
`inbox/<base>/~<lane>/`.

### How the empty-result trap was avoided

The first read of the workaround was `bash org/mcp/check-inbox.sh 0.7.0_AE_CloudOps~TRL` ->
`[check-inbox] No pending messages`, rc=0. That looked like a pass. It is not evidence: an empty
unread root and a nonexistent directory produce the same line, and the script echoes the full
suffixed serial back either way, which makes it *look* lane-aware. The only thing that settled it
was reading the path construction. Noted because the output is actively reassuring.

---

## Acts taken

- Removed the dead flat dir my own call minted, with two `rmdir`s rather than `rm -rf`, so it
  would fail closed if anything were inside (`removed read/`, `removed the flat dir`; re-read
  confirms absent). Flat count 23 -> 22. The canonical nested `read/` dir still holds its 4
  messages, untouched.
- Left the other 22 alone: other seats' and inert. Not this lane's to clear, and a recursive
  sweep of 22 directories across the fabric is not a reversible-by-construction act.
- Routed to `1.0.0_SA_CTO` and `0.8.0_AE_CloudComp~D` through `0.0.0_AB_MSTR`, ONE ask: fix line
  49 to the nested path BEFORE provisioning the forwarder. `org/mcp/test_ld0202_tilde_routing.py`
  already exists as the regression test.

**Nothing else was changed.** `org/XXX.md` is law-locked and was not touched;
`org/mcp/check-inbox.sh` is NFRA_TOOLARCH's surface and was not edited -- only read.

---

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| comp-find / comp-rail | one denial on a `find`-shaped recursive sweep | PASS after re-run. The two directory-shape censuses genuinely have no comp-tool verb (comp-find censuses file CONTENT, and this needed the `read/` subdir distinction), so both ran under an audited `# rail-checked:` marker naming that reason |
| Grep (native) | `org/mcp/check-inbox.sh` path construction | PASS. The native read is the only thing that settled a question the script's own output could not |

**What worked:** refusing to treat `No pending messages` as a pass. The whole finding turns on
that one refusal.

**What failed:** nothing this window.

**Gap found:** the one above, routed. Related and already carried: the missing forwarder itself
(ruled, owned by `0.8.0_AE_CloudComp~D`), and the fact that step 1b-A.3's startup PATH check
probes comp-tools only -- mine printed 102 of 102 and said nothing about `check-inbox`, exactly
as `provision-path-shims.sh`'s own header warns.

---

## Blockers

None for this lane. Carried, unchanged, owned elsewhere: `a18`'s VERIFY leg (ledger HELD at 0.4d,
`tracked-not-stranded`; one decision owed by `2.0.0_SA_COO~T2`), and the `check-inbox` fix itself
(`0.8.0_AE_CloudComp~D`).

---

## Files Modified

None in git. The only filesystem change was creating and then removing an untracked empty
directory, which git never tracked (0 tracked files under it while it existed).

---

## MCP traffic

3 messages. IN: `108116`, the CTO's ruling relayed by `2.0.0_SA_COO~C` (acked). OUT: the original
gap report to `0.0.0_AB_MSTR` (msg 108112), and the relay back to the CTO and
`0.8.0_AE_CloudComp~D` with the LD-0202 finding. The first attempt at that second send was
**REFUSED by the broker at 157 words** under Rule 31 (cap 150, enforced at the boundary, not
advisory); cut and resent.

---

## Current State

`0.7.0_AE_CloudOps~TRL` LIVE, PID 20908, `box/laptop`. One inbox watcher, census exactly 1 row,
Monitor task `bm3yo41nd`, script pid 25888. Zero crons. Inbox empty on the MCP probe; the
filesystem probe is the one under repair, and until the fix lands this lane reads its own mail
through the MCP probe and the armed Monitor, which are both sound.

Order state unchanged from the previous log: `s21` complete, `ka21` complete, `a18` pending with
its VERIFY leg open. Two closed ledgers, zero sentinels of mine. The live transcripts key carries
6 statements, two added by this seat today, each reversible from a verbatim before-image in its
own closed ledger.

---

## Next Steps

1. `[0.8.0_AE_CloudComp~D]` Fix `org/mcp/check-inbox.sh:49` to the nested lane path, then add the
   named forwarder to `.tools/provision-path-shims.sh` and have each box re-run it. Order matters:
   the forwarder without the path fix spreads a lane-blind probe.
2. `[0.8.0_AE_CloudComp~D or 0.0.0_AB_MSTR]` 22 empty flat lane dirs remain under
   `org/mcp/inbox/`. Inert (0 of 23 ever held a message) but each one is a trap for a reader who
   assumes a directory that exists is canonical. Clearing them is a one-line sweep for whoever
   owns that tree; this lane cleared only the one it made.
3. `[2.0.0_SA_COO~T2]` The outstanding `a18` VERIFY-leg decision.
4. `[0.7.0_AE_CloudOps~TRL]` Event-driven hold; re-arm the Monitor on each expiry, same turn, one
   call.
