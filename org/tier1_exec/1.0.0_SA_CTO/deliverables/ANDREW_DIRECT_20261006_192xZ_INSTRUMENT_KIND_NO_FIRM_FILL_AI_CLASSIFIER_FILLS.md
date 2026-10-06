# ANDREW-DIRECT 2026-10-06 ~19:2xZ -- a firm's own label never fills `instrument_kind`; the AI classifier does

**Channel:** typed at the `1.0.0_SA_CTO` terminal (laptop), answering this seat's `/open-calls` CALL 1 of 1.
**Recorded by:** `1.0.0_SA_CTO`, same turn.

## Verbatim

"Yes aghreed with the rec here"

## The call and the REC he agreed to

**Call:** may a firm's own label (for example Black Diamond's asset type) fill a security's blank `instrument_kind` in the shared
classification table (`etf-classifications`)? Routed to him by this seat (msg 103218, 2026-09-30); carried AWAITED in
`org/missions/D8/MDPF/MDPF_SECCLASS/STATUS.md` Dependencies.

**REC (agreed): No.** A per-firm value never fills `instrument_kind` on a table row. A blank `instrument_kind` is filled by the AI
classifier, which lands without human review and is listed in the AI-landed index (his 2026-10-05 ruling, MDPF_SECCLASS
C-AIINDEX). One source keeps the table canonical; firm labels differ by firm.

## Scope

MDPF_SECCLASS only; closes the Dependencies row. Changes no outcome text.

-- 1.0.0_SA_CTO
