# F8 IDENTITY BINDING — LIVE POSITIVE (OPAL_ANALYST.W6-T1 close)

**Seat:** 0.0.3_BG_BBGTerminal
**Session:** 00a52644-8769-46a5-8143-74245b5cc549
**Launch:** ajb.ps1, 2026-08-20T16:00:03Z, host OPAL_BLOOMBERG
**Measured at:** this session's startup, first turn, before any duty work
**Gate acceptance this closes:** 1.0.0_SA_CTO~Z @9912a960d5 (ACCEPTED-PENDING-LIVE-POSITIVE)

---

## 1. Launch-path + serial session files (the ajb binding)

`org/mcp/sessions/00a52644-8769-46a5-8143-74245b5cc549.launch-path`
```
bg-concierge 2026-08-20T16:00:03Z launcher=ajb.ps1 host=OPAL_BLOOMBERG
```
- first token is `bg-concierge` — the exact literal `bg-concierge-gate.sh` greps for (`^bg-concierge`)
- written 12:00 local / 16:00:03Z, ~90s before this measurement

`org/mcp/sessions/00a52644-8769-46a5-8143-74245b5cc549.serial`
```
0.0.3_BG_BBGTerminal
```

**Ordering is as designed:** marker written by `ajb.ps1` at launch, BEFORE the seat could
write anything itself (the seat cannot write `org/mcp/**` at all — G1). Both files exist,
so identity resolves POSITIVELY and the fence enters **ACTIVE-ENFORCE**, not LOUD-CLOSED.

### Discriminating negative control (not hand-chosen — it is the prior session of this same seat)

Session `245e7a44-af98-4156-ba02-7aab0609a316` — the BG session reaped for this relaunch:

| file | this session (ajb launch) | prior BG session |
|---|---|---|
| `.launch-path` | PRESENT | **ABSENT** |
| `.serial` | PRESENT | **ABSENT** |

Estate-wide denominator at time of measurement: `*.launch-path` = **1** (mine, the only one),
`*.serial` = **69**. So `.serial` is the fabric-wide mechanism and `.launch-path` is the
F8-specific one, and it exists on exactly the launch path it is specified to mark.

## 2. Fence ACTIVE — registration + mode

Hook registration, `.claude/settings.json`:
```
matcher = Bash|PowerShell|Write|Edit|NotebookEdit|mcp__bloomberg__.*|mcp__opal-gateway__.*|mcp__opal-gateway-bbg__.*
command = bash "$CLAUDE_PROJECT_DIR/.tools/hooks/bg-concierge-gate.sh"
```
All four G-classes are inside the matcher. `settings.json` mtime **2026-08-07 14:16:08 -0400**
— untouched by the F8 change (F8 landed in the gate script, not the registration), confirmed
by `stat`, matching the CTO~Z acceptance note.

Resolved F8 cell for this session: `_CALLER` resolves from `<sid>.serial` to
`0.0.3_BG_BBGTerminal` -> **ACTIVE-ENFORCE** (the four classes enforced as always).
This is the healthy cell. **A healthy ajb launch landing in LOUD-CLOSED would have been a
finding, not a loosening — it did not.**

## 3. One classed call blocked (the live positive)

**Classed call (G1, Write off-allowlist):**
`Write -> C:\...\ajb_workspace\docs\.f8-probe-DELETE-ME.md`

**Result: DENIED**, verbatim:
```
BLOCKED (bg-concierge-gate G1): the 0.0.3_BG seat is read-only outside its own
logs/threads/deliverables and tmp. Target '...\docs\.f8-probe-DELETE-ME.md' is
off-allowlist. If this write is genuinely needed, route the ask to Andrew via
0.0.0_AB_MSTR~Z -- especially note that prompt.md, refs/ and .claude/ are
DELIBERATELY unwritable from this seat (Teams content can never become a prompt edit).
```

**Effect verified, not inferred:** `ls docs/.f8-probe-DELETE-ME.md` -> `No such file or
directory`. The deny blocked the write; it did not merely warn about it.

**Positive control, SAME TOOL, allowlisted path:** this file itself
(`org/tier0_utility/0.0.3_BG_BBGTerminal/deliverables/...`) was written by the same `Write`
tool through the same live hook. **The fence discriminates — it is not a blanket block on
the seat.** Deny and pass were produced by one instrument in the same minute.

---

## Verdict

All three acceptance legs measured live at this seat, each with its control:

| leg | evidence | control |
|---|---|---|
| launch-path + serial | both present, `bg-concierge` first token, ajb.ps1 @16:00:03Z | prior BG session has NEITHER |
| fence ACTIVE | matcher covers 4 classes; identity resolves -> ACTIVE-ENFORCE | settings.json mtime unchanged 08-07 |
| classed call blocked | G1 deny, named line, file absent afterward | allowlisted write PASSED, same tool |

**W6-T1 F8 live positive: SATISFIED.**

Residual, stated so it is not discovered later as a gap: this exercises the
**ACTIVE-ENFORCE** cell only. The LOUD-CLOSED / LOUD-PASS / SILENT-PASS cells were
exercised at build by 0.5.0_AE_OpalETL~Z's suite (60/60 at the CTO~Z re-run), not here —
a live launch structurally cannot occupy two cells at once.
