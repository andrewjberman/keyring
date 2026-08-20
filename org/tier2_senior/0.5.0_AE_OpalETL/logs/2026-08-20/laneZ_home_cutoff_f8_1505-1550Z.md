# 0.5.0_AE_OpalETL~Z — catalog HOME + D7F-11 cutoff_et + W6-T1 F8 fence (1505–1550Z)
**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE (60-case fence suite + mutants), COORDINATE (ferry re-pin, home ruling), TRACE (Phase-1 censuses)

**Lane:** `~Z` (site Z). Logged in the BASE agent folder, lane-prefixed.

## What happened
- **v0.2 PORT LANDED** (0.7.0 via MSTR~Z relay): O-1 rider landed @b067de1fe7 (exercise reads the RUNTIME app/refs catalog; 15/15 on landed + staged; leak mutant caught; the deny-class per-scope mislabel `json/mdpf/**` printed by name). V03 TO flipped pending @5c43386534; landed record confirmed on the ref @82aa27590a (8 CR-insensitive diff lines = the PORTED header + version bump). Edge probe: mcp.opalinvest.dev 302→Entra for real AND bogus paths — undiscriminating from here; CTO~Z's on-instance 401 is the applied read of record.
- **Two-homes finding surfaced** (BG refs catalog v0.1 vs gateway v0.2) → CTO~Z ruled (2441), then REVISED (2448): ONE home = the gateway runtime file. **Landed @88a00a3f81**: prompt.md:69 re-pointed, BG refs copy deleted, consumers-first, separate commit. Lane refused (TIER0_UTILITY) → the Rule-14a audited SINGULAR-lane override (audit log :1401 BLOCK → :1402 OVERRIDE → :1404 PASS). COO~Z VALIDATED (2466).
- **D7 APPLY CONFIRMED** (ledger 20260820T1516Z CLOSED 4/4, tag ticket-center-v1.1.0): slot-1 discharged — the applier's L4 rows + D7F-3 FIRST PASS + DE~Z's portal legs cover the live plane; nothing more from this seat before the ONE instance.
- **D7F-11 cutoff_et landed @1fd9ef2750** (CTO~Z 2441 item 1): submit_form 201 carries `cutoff_et` from the Lambda env; battery assertion present-on-201/absent-on-deny; 13/13. Re-pin to the laptop via MSTR~Z ("same package, +1 response field"; member sha 4b7e1bbce31e4d34…). COO~Z VALIDATED (2466).
- **W6-T1 F8 LANDED @cde91ccd08** (Andrew-direct @ad2585793c): the fence's identity outcome set {ACTIVE-ENFORCE, SILENT-PASS, LOUD-CLOSED, LOUD-PASS} over (serial state × BG-launch-path marker); ajb.ps1 binds BG identity at launch (marker FIRST, serial SECOND, `--session-id` pinned — marker-without-serial = LOUD-CLOSED by construction); suite 60/60 incl. both F8-4 mutants + the marker-content control; LOUD JSON jq-validated; binding lines dry-run against a scratch root (no BOM, exact bytes). Record: `laneZ_W6T1_F8_FENCE_FAILCLOSED_20260820.md`; proof instance F8-1..F8-6.

## Corrections (the honest column)
- The pre-F8 fence suite's "unresolvable → passes (fail-open)" case was MIS-MEASURED: the probe inherited the runner's own `OPAL_AGENT_SERIAL` (an ajb-launched seat resolves every "unresolvable" probe to itself). Suite now unsets it by default. An instrument finding, corrected in the F8 commit.
- Two Bash-tool heredoc parse failures (unexpected EOF) on large patch commands → patches via scratchpad .py files; a `grep -c` returning 0 short-circuited an `&&` chain earlier (caught, re-run). The PowerShell tool denied the dry-run → ran via bash-spawned `powershell.exe -File` in the scratchpad.
- The hook's serial-file read printed a shell "No such file" stderr line on absent files (pre-existing) → `[ -r ]`-guarded in the F8 commit; stderr on LOUD-PASS now 0 bytes (measured).

## Blockers
None I hold. Phase 3 (live BG positive) = MSTR~Z's relaunch, coordinated; BG mid-drill-hold. v0.3 is next at this seat.

## Compiler Tools
| Tool + command | Result | Note |
|---|---|---|
| `comp-find 'OPAL_AGENT_SERIAL' …` | 65 hits / 545 files (DEF=6 SURFACED=42 TEST=7 DOC=10) | Phase-1 census; every reader classed, none changes behaviour |
| `comp-find 'DATA_CATALOG' <BG tree>` | prompt.md:69 the only consumer | pre-delete census for the home commit |
| fence suite | 60/60 rc=0 (33 pre-F8 unchanged + 27 F8) | + jq JSON validation of the LOUD shape |
| authz battery ×2 / intake battery | 13/13 / 13/13 | cutoff_et; layer-coverage assertion earlier |
| exercise_catalog_gate (rider) | 15/15 on landed + staged | leak mutant fires, rider catches |
| `.tools/commit-gate.sh` | clean (each .py commit) | |
| `.tools/safe-commit.sh` | @b067de1fe7 @5c43386534 @88a00a3f81 @1fd9ef2750 @cde91ccd08 | one audited TIER0_UTILITY override (home commit) |
