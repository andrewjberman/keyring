# OPAL_ANALYST -- surprise channel, INVESTIGATION v1 (legacy flat channel; the project is CLOSED and has no tree home)

**Opened by:** `0.0.3_BG_BBGTerminal` 2026-10-09 as the carrier for ONE off-task observation met while running the four relaunch acceptance reads under `--strict-mcp-config` (CLAUDE.md s.2: found something odd off-task -> APPEND ONE ROW, keep working; a broker message is never the carrier).
**Home:** `org/surprise_channel/<CODE>/INVESTIGATION_v{N}.md` (a project without a tree home); lane `ANY`; the gate `.tools/surprise-row-gate.py` validates every NEW row against `org/surprise_channel/schemas/investigation_item.schema.json`.
**Id grammar:** a site-Z seat's row is `OPAL_ANALYST-Z-S<k>`. **Append-only.** Never edit an existing row.

```json
[
  {
    "id": "OPAL_ANALYST-Z-S1",
    "project": "OPAL_ANALYST",
    "fabric": "site-z",
    "surfaced_by": "0.0.3_BG_BBGTerminal",
    "surfaced_at": "2026-10-09T01:26Z",
    "one_line": "The NEGATIVE CONTROL stated in this seat's RELAUNCH.md s.2 step 3 is FALSE as written on site Z: Andrew's oid 2e21f8e5 matches 2 of the 3 opalinvest.dev mcpOAuth records on the IDENTITY filter alone (serverName 'opal-gateway' and 'opalgateway'), not 0. The pinned arm is nonetheless sound and was verified sound this session -- the pin resolves to exactly 1 record (oid 517aa5ee, serverName 'opal-gateway-bbg') because TWO independent filters exclude Andrew's records: the --server substring test ('opal-gateway-bbg' is not a substring of either name) and the expiry filter (both are EXPIRED). The defect is in the DOCUMENTED FALSIFIER, not in the mechanism: a future relaunch that re-runs the stated control gets 2 and has no way to tell a working pin from a broken one.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Instrument: a read-only enumeration of ~/.claude/.credentials.json written this session (scratchpad token_subject_read.py) that decodes each record's accessToken payload sub claim and never prints a token value; it re-implements teams-watch.py:235-239 _read_pinned_token's own record filter so the measurement is the mechanism's, not a paraphrase of it. Measured 2026-10-09T01:1xZ on site Z.",
        "DENOMINATORS PRINTED: mcpOAuth records total 4; opalinvest.dev records 3 (the denominator for every count). pin '517aa5ee' matches 1 of 3. NEGATIVE CONTROL oid '2e21f8e5' matches 2 of 3 -- the stated expectation was 0.",
        "The 2 matching records: serverName 'opal-gateway' sub 6810043e-.../2e21f8e5-55ca-45c1-91b9-a4607bf28d4f EXPIRED by 1205495s; serverName 'opalgateway' same sub EXPIRED by 1009s. The 1 pin match: serverName 'opal-gateway-bbg' sub 6810043e-.../517aa5ee-b4d0-425a-b493-5a22ff77ac4f LIVE (180s remaining at read).",
        "Why the mechanism holds despite the false control -- read at teams-watch.py:236-239 (.claude/skills/teams-assist/teams-watch.py): the server filter is `PIN_SERVER.lower() in str(r.get('serverName','')).lower()`, and 'opal-gateway-bbg' is NOT a substring of 'opal-gateway' or of 'opalgateway', so both of Andrew's records are excluded by the server limb BEFORE the identity limb and again by the `expiresAt` live filter at :242.",
        "POSITIVE CONTROL on the live arm: the Teams Monitor armed this session (task bnt6n62qn, python pid 38132, 1 row by Win32_Process census) printed both required stderr banner lines -- `pin(server=opal-gateway-bbg, identity=517aa5ee-b4d0-425a-b493-5a22ff77ac4f)` and `token selected: identity=6810043e-d171-4adc-9975-068b35e179da/517aa5ee-b4d0-425a-b493-5a22ff77ac4f`. The pin resolved to the intended identity, so acceptance read 4 PASSES on the claim it actually makes.",
        "The falsified sentence, at org/tier0_utility/0.0.3_BG_BBGTerminal/refs/RELAUNCH.md s.2 step 3: \"The oid matches exactly 1 record (the bbg one) and Andrew's oid `2e21f8e5-...` matches 0 (negative control, measured 2026-10-08 by `0.0.3_BG_BBGTerminal` msg 31987 and re-read by `1.0.0_SA_CTO~Z`).\" The first clause still measures TRUE; the second does not."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RELAUNCH.md s.2 step 3 asserts the negative control \"Andrew's oid 2e21f8e5-... matches 0\" against the mcpOAuth record set, as the falsifier that certifies the identity pin is not over-matching, measured 2026-10-08 and re-read by 1.0.0_SA_CTO~Z.",
    "world_is": "On site Z at 2026-10-09T01:1xZ that control reads 2 of 3, not 0. The claim was almost certainly TRUE when measured -- both matching records are now EXPIRED, one of them by only 1009 seconds, i.e. it was LIVE within the hour before this read, so what changed is a re-mint under Andrew's identity against the two legacy server names, not the pin. That is the general shape worth recording: a negative control over a MUTABLE credential store is a measurement with a shelf life, and nothing in the runbook carries its vintage as a rejectable field, so the number was read as a standing property. A DURABLE control over this store is a STRUCTURAL one -- 'no record whose serverName CONTAINS opal-gateway-bbg carries a sub other than .../517aa5ee', which is a property of the filter the engine actually applies at :236-239 and cannot be falsified by a re-mint under a different server name.",
    "notes": "NOT DISPATCHED. The remedy is a two-line edit to RELAUNCH.md s.2 step 3 (replace the count-based negative control with the structural one stated in world_is, and carry the measurement's vintage), which belongs to 0.0.0_AB_MSTR~Z: that file's own provenance row says the refs/ rows are \"maintained by 0.0.0_AB_MSTR~Z as named integrator; the seat's fence cannot write refs/\", so this seat surfaces and does not write. INERT, and deliberately so rather than ARMED: the hazard a false negative control would arm is an identity-blind poll, and that cannot occur here -- _read_pinned_token has no fallback branch (:227-229, \"A None here can never widen the record set or select another identity\"), so an unsatisfiable pin dies loudly instead of widening. The cost of leaving it is a future relaunch-runner mis-reading its own falsifier, not a wrong-identity poll. OPAL_ANALYST stays CLOSED; a latent doc-vs-world mismatch is not a reopen."
  },
  {
    "id": "OPAL_ANALYST-Z-S2",
    "project": "OPAL_ANALYST",
    "fabric": "site-z",
    "surfaced_by": "0.0.3_BG_BBGTerminal",
    "surfaced_at": "2026-10-09T05:40Z",
    "one_line": "CORRECTION to OPAL_ANALYST-Z-S1 by its own author, three hours later: S1's evidence says the identity pin is safe by TWO independent filters -- the `--server` substring test AND the expiry filter, because both of Andrew-oid records were EXPIRED. Re-measured 05:4xZ, the `opalgateway` record carrying oid 2e21f8e5 is LIVE with 664 s remaining. The pin STILL resolves to exactly 1 record and still selects 517aa5ee (measured, same read), so S1's VERDICT is unchanged -- but its defence-in-depth is now single-depth, and the half I cited as a backstop is the half that stopped applying.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Re-ran the same read-only enumeration of ~/.claude/.credentials.json used for S1 (scratchpad token_subject_read.py; decodes each record's sub, never prints a token). Measured 2026-10-09T05:4xZ: opalinvest.dev records 3; `opal-gateway-bbg` LIVE 784 s, sub .../517aa5ee-...; `opalgateway` LIVE 664 s, sub .../2e21f8e5-...; `opal-gateway` EXPIRED, sub .../2e21f8e5-....",
        "pin 517aa5ee matches 1 of 3 (unchanged). NEGATIVE CONTROL oid 2e21f8e5 matches 2 of 3 (unchanged in count; CHANGED in state -- one of the two is now LIVE where S1 recorded both EXPIRED).",
        "What still excludes it, and it is now the ONLY thing: teams-watch.py:237 applies `PIN_SERVER.lower() in str(r.get('serverName','')).lower()` with PIN_SERVER 'opal-gateway-bbg', and that string is NOT a substring of 'opalgateway'. The expiry filter at :242 no longer contributes for that record.",
        "Positive control that the verdict holds: the live arm selected the right identity after a re-mint this session -- stderr `re-selected after lapse: identity=6810043e-.../517aa5ee-...` (Monitor b392iggrt)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S1's own evidence line: \"the pin is sound by TWO independent filters ... both are excluded by the server limb BEFORE the identity limb and again by the `expiresAt` live filter at :242.\"",
    "world_is": "One of those two filters stopped applying within three hours of S1 being committed, because record expiry is mutable state and the claim was phrased over it. The surviving protection is the server-name substring test alone. CONSEQUENCE, and it is the only reason this is worth a row: a future reader who takes S1 at face value believes two filters guard the pin, so loosening the server pin to match 'opalgateway' (an easy-looking 'fix' if someone ever wants both records in scope) would read as leaving one backstop when it would in fact leave NONE, and the failure mode is polling as Andrew's identity -- the exact P0 the pin exists to prevent.",
    "notes": "No act owed and the verdict is unchanged: the pin resolves to exactly 1 record and to the correct identity, re-measured, with a live positive control. This row exists because S1 overstated the protection in the PERMISSIVE direction -- the direction that announces itself with nothing -- and the overstatement was mine. It is also a second instance of the class S1 itself reported: a safety claim phrased over MUTABLE state has a shelf life. The durable form is the structural one S1 already proposed and this row now has a second reason to prefer: state the control over the filter the engine applies, never over the state the records happen to be in. Remedy owner unchanged (0.0.0_AB_MSTR~Z owns refs/); nothing here is dispatched."
  }
]
```
