# MDPF_SECCLASS -- 17-FWD board, round 24 L8 packet: SKELETON (2.0.0_SA_COO~M1, 2026-10-13 ~19Z)

STATUS OF THIS FILE: a skeleton, not the board. Direction: cluster packet O7 (relay msg 5010; CTO msg 5026): a FULL 17-FWD board prints in the round-24 L8
packet; every other FWD stays uncut until it exists. Every "last stated grade" below is a quotation of a CTO round analysis (read by grep on 2026-10-13), not a
measurement; "MEASURED NOW" is EMPTY for every row and is filled at round close from live reads, each with its denominator. The CVO grades; this seat states evidence.

Population: the PRD's FWD-1..FWD-17 (`org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` lines 24-204, DONE WHEN lines read in full).
Last-grade sources: CTO round analyses R8 (`..._ROUND_8_20261007.md` table lines 14-21), R9 (lines 14-18), R10 (line 12), R19 (lines 27, 82).

| FWD | outcome (short) | DONE WHEN (class) | last stated grade (source) | read needed at close | MEASURED NOW |
|---|---|---|---|---|---|
| 1 | BD advisor sees class/sub-class from the one shared list | one live BD chain run, traced list -> page | NOT REALIZED (R19: served BD mix held 23 securities the list can place; R19 line 82: re-read after e91 leg G) | `r24_legg_read.py e97` + e91 read after the 23:00Z chain; the trace of one client | EMPTY |
| 2 | one answer for a security's class on every screen | a set of securities across every screen | NOT REALIZED on BD (R9: SC-e-22 enum never issued) | the chosen handful across the seven surfaces named in ACCEPT | EMPTY |
| 3 | a correction in one place shows everywhere after its next run | one real correction read on every screen | no stated grade found in R8/R9/R10/R19 (grep) | not read | EMPTY |
| 4 | the repeatable "no second definition" check | check run on demand, read at each round's close | no stated grade found in R8/R9/R10/R19 (grep) | the FWD-4 check (count of places looked at, list, planted-copy control) | EMPTY |
| 5 | old BD list deleted, nothing needed it | deletion on Andrew's confirmation after the check reads zero users | NOT REALIZED (R8: 5 readers; R9: first reader switch built, E_18 not switched) | readers list + FWD-4 check; Andrew's act, never mine | EMPTY |
| 6 | exceptions written down, owner and reason | a reader looks up securities on exception screens | no stated grade found (grep) | not read | EMPTY |
| 7 | new security in any firm's daily holdings gets its entry on a schedule | scheduled classification fired on demand, then the ordinary run | no stated grade found (grep) | scheduled-run telemetry + the entry for a new ticker | EMPTY |
| 8 | fund vs individual stock on the list; holdings table orders stocks after funds | one real client's holdings read on the page | no stated grade found (grep) | page read, one real client | EMPTY |
| 9 | every Rival Funds stock has its entry and one year of history | whole Rival Funds list read against the shared list | NOT REALIZED (R8: history half unfilled, 7 stocks no Bloomberg id); PRD: TO-SC-e18 filled three years | list-vs-list read with a denominator | EMPTY |
| 10 | new ETF-trading stocks get entry + three-year history by a routine | routine fired on demand, then the ordinary run | no stated grade found (grep) | routine telemetry | EMPTY |
| 11 | unplaceable security gets an AI-classified entry; AI-made list exists | classifier run on one security, entry and the AI list read | NOT REALIZED (R9: served act built e48/e49, held for its half) | the AI-made index read | EMPTY |
| 12 | sector + industry group on the list; Positioning ETF view shows them | ETF view opened, holdings' sectors read vs the list | NOT REALIZED (R9: sector writer not applied) | the ETF view for one Opal ETF | EMPTY |
| 13 | Investor Reporting Holdings tab shows the list's class everywhere | one Cottonwood client's tab read against the list | NOT REALIZED on BD (R9; the enum restore SC-e-100 landed 2026-10-13, not deployed) | the tab read, one client | EMPTY |
| 14 | properly written names wherever holdings are listed | Andrew has opened a Holdings tab and read the names | NOT REALIZED (R8: 2,624 unnamed rows; R9: served act built, held) | name read; Andrew's own act | EMPTY |
| 15 | per-firm list of held securities with no entry, reaches zero | list pulled for each of three firms, read at zero | NOT REALIZED (R8: 1,046 held with no old row; R9: held) | three counts with denominators | EMPTY |
| 16 | each screen's group mapping from the six classes is stated | a reader looked up the mapping per screen | NOT REALIZED (R8: 3 screen disagreements) | the mapping table | EMPTY |
| 17 | every old-list security has an entry under the six classes | count of old-list securities with no entry read at zero | NOT REALIZED (R8: population and held definition open; R9: held) | the count, with the old-list denominator | EMPTY |

Rows whose last stated grade is only "not found by grep" are NOT claimed ungraded: a grep over four analyses is not a census of every CVO grade
(`ADJUDICATION_v1..v22` and the L10 stamps are the grading record and are read at close before any such row is filled).

Not in this file: the sync cell (C-DEMQUE-SECCLASS-SYNC, CTO PRD addendum @4dda49c7e3), which is cut at the round-25 recut, not mid-round.
