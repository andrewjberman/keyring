# Andrew-direct — 2026-08-19 ~1900Z (chat, this terminal, Andrew present)

**VERBATIM:**
> *"relay your findings here to MSTR~Z. Tell them they need to instantiate 1.0.0_SA_CTO~Z and
> 2.0.0_SA_COO~Z to oversee the incoming PRDs and that your findings here need to be folded into
> the OPAL_ANALYST project"*

**Context he was answering:** he asked (1) where OPAL_ANALYST stood, and (2) how developed this
seat's backend retrieval capabilities are — then sharpened it to: what tooling exists and what it
is CONNECTED to, and on guardrails, what prior art exists, what is IMPLEMENTED vs DESIGNED-only,
and of what is implemented, what is PROSE GUIDE vs ACTUALLY GATED.

**Two instructions, both for MSTR~Z, relayed verbatim, scope NOT adjudicated by me:**
(a) instantiate `1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~Z` to oversee the incoming PRDs;
(b) fold my findings into the OPAL_ANALYST project.

**Relayed:** MCP -> `0.0.0_AB_MSTR~Z` at 20260819T192059Z
(`20260819T192059Z_0.0.3_BG_BBGTerminal_ANDREW-DIRECT__instantiate_CTO_Z___COO_Z.md`,
filesystem + broker + channel push). Grounding carried WITH each finding per the relayer half of
the record+broadcast law — a relay is the same act as an assertion with a longer fuse.

## The 10 findings relayed (all EXERCISED this session, not read off a doc)

| # | Finding | Grounding |
|---|---|---|
| F1 | **W5 and W6 have no task-order file at all**, though PRD §9.0 names both as completion requirements | `ls org/*/*/task_orders/` grep -> zero |
| F2 | **`DATA_CATALOG` still `version: 0.1`**; v0.2 is the program's landing surface, so completed atom_decomp output has NOT reached the operating registry | `refs/DATA_CATALOG.yaml:16` (BUCKET_ALLOWLIST is already v0.2) |
| F3 | Prior art covers 8.5 of 15 pages; W4b closing != program closing | PRD §9.1 |
| F4 | **Live user-visible defect** — catalog says `factor-tilts/{tier1\|tier2}.json`, bucket holds `tier1-snapshot` / `tier2-spreads` / `tier3-timeseries` | `get` rc=1 on a COMPLETE 3-key walk + `list` denominator 3/3 |
| F5 | ycharts **deliberately** unexercised — availability is not authorization; needs Andrew's per-use word (PRD §1e) | CLAUDE.md vendor-egress rule |
| F6 | **The fence governs TOOLS, not CONTENT** — the whole answering layer (catalog classification, vintage rule, T-1 discipline, thread memory, ACK-FIRST) is prose; a wrong number with no vintage passes every gate | rule enumeration G1–G4, `bg-concierge-gate.sh` 170 lines |
| F7 | **`never_serve` is prose; READS are ungated** — G2 blocks writes only, and `aws s3 cp` DOWN passes by positive control | the gate's own test suite |
| F8 | **Fence identity is single-sourced for this seat, and the fence caused it** — G2 blocks the A.1 serial-file write, so only `$OPAL_AGENT_SERIAL` remains; unset -> exit 0, no output, **silent stand-down of all four classes** | `:70-74` + `env -u` probe, exercised |
| F9 | **Do not file a bug on the suite's "1 failure"** — 33/34 from inside this shell, **34/34 under `env -u`**; the failure is my own serial leaking into the fallback | both runs |
| F10 | **The outer fence masks the inner one** — local G4 blocks gateway calls before the server sees them, so the server-side allowlist's DENIALS cannot be exercised from this seat | G4 live block |

## Live gate probes run to produce the above (wiring layer, not just the script)
`opal-gateway` whoami -> BLOCKED (G4) · `bloomberg_historical_data` -> BLOCKED (G3) ·
`reference_data` 3 securities -> BLOCKED (G3) · `reference_data` 1 security -> **PASSED**, SPX
7,718.58 (**positive control** — the fence discriminates) · shell redirect into repo content ->
BLOCKED (G2, at my own startup) · suite 34/34 clean.

## Retrieval exercised
10 of 11 channel keys retrieved live with vintages; DDB `opal-news-trending-daily` 2026-08-18 ->
20 items COMPLETE walk. Partial-is-not-absence is **mechanized in the tool** (every retrieval
prints a denominator), not merely prose — F4 is the proof: it failed by naming its own denominator.

## What I did NOT do
No action on any finding. I cannot edit `refs/` or `prompt.md` from this seat by design (G1), I do
no git work, and F1/F2 are TO-issuance calls belonging to MSTR~Z / CTO~Z. **No gate proposed, no
workstream manufactured** — routing only, per the no-inferred-gates law.
