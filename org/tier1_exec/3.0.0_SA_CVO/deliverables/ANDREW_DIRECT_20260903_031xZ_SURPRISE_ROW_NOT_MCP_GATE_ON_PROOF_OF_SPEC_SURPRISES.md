# ANDREW-DIRECT 2026-09-03 ~03:06Z at the 3.0.0_SA_CVO terminal -- surprises are ROWS, not MCP; a gate on the proof-of-spec `surprises` field, NOW

**Channel:** Andrew, typed directly at the `3.0.0_SA_CVO` terminal (laptop, PID 14124), after a fork he ran at this
terminal ("Surprise channel shouldnt need to come over mcp, ...") reported twice into this session. Relayed by MCP the
same minute: `1.0.0_SA_CTO` 92976, `2.0.0_SA_COO` 92977, `0.0.0_AB_MSTR` 92978 (3 DELIVERED / 0 QUEUED / 0 REFUSED).

**Verbatim, entire, his spelling kept:**

> WRite an MCP to CTO that we need this fixed, claude.md should not have that rule to do this over mcp + any gate with proof of spec surprises field to prevent this should be implemented now, have CTO get on tha tnow

## What it binds (relayed as written; this seat adjudicates neither wider nor narrower)

1. **`1.0.0_SA_CTO` fixes it NOW.** Two acts, both in that seat's lanes (CLAUDE.md = BASE_EXEC; gates = LOOP_MECHANISM).
2. **CLAUDE.md must not carry the rule that a surprise goes over MCP.** The line at issue, CLAUDE.md s.2 (worktree HEAD
   03eb9e3dba): *"FOUND SOMETHING ODD OFF-TASK? Do NOT halt-and-investigate -- one line to `3.0.0_SA_CVO` (cc issuer),
   KEEP WORKING."* It names the broker as the carrier and never mentions the row. The surfacing act is the ROW at the
   project's channel, which `.tools/surprise-row-gate.py` validates at commit and `org/surprise_channel/surprise-watch.sh`
   delivers to this seat with the exact path. `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` s.4 ("CVO assembles; any seat
   surfaces") and `docs/doctrine/THE_SURPRISE_CHANNEL.md` ("one line to the coordinator") carry the same wording. A law
   edit has three surfaces: commit + same-turn broadcast + push state stated.
3. **A gate on the proof-of-spec `surprises` field, implemented NOW.** `org/standards/PROOF_OF_SPEC.schema.json`
   `surprises` is today an array of free strings ("one line each, observed outside mandate, NO action taken"). His
   word: *any* gate on that field that prevents a surprise existing only as a broker message. The design (where it
   refuses; whether the entry becomes a row id or carries one) is `1.0.0_SA_CTO`'s under Rule 24.

## The specimen this answers (measured at this seat)

- `0.8.0_AE_CloudComp`'s surprise reached `3.0.0_SA_CVO` ONLY as broker message 92943 (02:55:51Z). Both channel roots
  were empty for NFRA_COMPEFFICACY; no `NFRA_COMPEFFICACY-S` id anywhere under `org/`.
- `3.0.0_SA_CVO` assembled row S1 @03eb9e3dba (03:00:58Z). The notifier (task b6cli05zq) fired on it within one poll:
  `NEW ROW NFRA_COMPEFFICACY-S1 project=NFRA_COMPEFFICACY fabric=laptop class=OBSERVATION hazard=ARMED -> <path>`.
- The row path was deterministic end to end. The MCP hop was the only non-deterministic part and it cost three broker
  messages (92943, 92960, 92970), an issuer reply and a CVO assembly in place of one file append. A notifier watching
  files is structurally blind to a surprise that only ever reaches an inbox.

## Input carried with the relay (a fork's reading at his terminal, marked as such -- NOT a ruling)

- Doctrine clause -> "append the row at the project's channel, keep working"; no MCP send; the notifier is the CVO's only
  intake; assembly, where any is needed, happens in the file.
- Gate -> every `surprises` entry resolves to a row id in the project's channel; a TO cannot flip to `complete` while an
  entry does not; a worker commit under a tree TO whose message cites a surprise with no row staged is refused.
- Trap named: a gate cannot read the broker plane; it binds only artifacts it can see.

## Not adjudicated here

Whether the TO template's SURPRISE GATE line ("one row to the surprise channel, cc `2.0.0_SA_COO`") changes with it is
`2.0.0_SA_COO`'s L6 text. Whether this seat's `NFRA_COMPEFFICACY-S1` assembly stands as the pattern or the exception is
answered by his word above: the worker writes the row.

-- 3.0.0_SA_CVO
