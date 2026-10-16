# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, ticks 27-28 (2026-10-16 ~14:59Z to 15:57Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Rulings and acts

| input | act | record |
|---|---|---|
| MSTR~Z 35078, relaying ms: can the BBGTerminal seat read Teams screenshots and Excel? | Both tools exist: `read_chat_message_images` (`tools.py:1698`), and `read_teams_attachment` (`:1203`) handing off to `read_workbook`. Neither had been exercised by the seat. Asked `0.0.3_BG_BBGTerminal` to exercise both (35079, READ 15:11:36Z); an interim answer went to ms (bus b6b1df75) | msgs |
| BBGTerminal 35091: 7 chats plus 1 channel listed; both tools NOT PROVEN (no pasted image and no .xlsx in reach; a .har declined as client-data risk); asked Alyssa for test files | The answer went to ms via MSTR~Z: no "Opal-gateway-BBG" channel exists; Alyssa's 1:1 with the seat is the place; per-tool results follow | seat log `teams_homes_and_image_xlsx_tools_not_proven_no_safe_target.md` |
| MSTR~Z 35087: `bg-concierge-gate.sh` unwired since 09-17 (Andrew's "pull that off right now", LD-0580); `prompt.md` corrected @66b1c7d3e9 | RULED: it stays unwired, since re-wiring would reverse Andrew's own act. The `prompt.md` fix is accepted. Andrew told in one line | msg 35089 |
| MSTR~Z 35090: the 13-CUSIP pull (1 `reference_data` call, NAME and SECURITY_DES) | was on Andrew's 15:12:44Z word "Just pull it from BBG": an authorised exception. The quota is not chased (two fields on 13 securities) | -- |
| MSTR~Z 35096: law-edit relay, rule 34 (CloudOps one lane per MACRO per box) | Rule read at `CLAUDE.md:92`. Site Z NFRA moves to ONE lane, `~NFRA1`. In-flight orders finish where they are: OG-ap-28 at `~Z`, OG-ap-29 at `~ZS`. `~MI` and `~MQ` retire once cleared: `~MI` commits 1 file and releases its tree lock; COO~MP re-addresses or cancels MP-pd-7. COOs notify MSTR at the first new NFRA CloudOps cut | msgs 35104, 35108, 35113-35115 |

## Scope state

7 open on site Z (54 rows), all `act`, all only Andrew can do; 0 forks. COO lanes live: `~O`, `~MI` and `~MP`.

The batched gateway release (OG-ap-28 at `~Z`) carries:
- the `-live` routing, after OG-ap-29 Phase B at `~ZS`;
- `~MI`'s 49F rows;
- the OG-en-10 429 audit, E9 and MP-pf-11.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| Grep (tools.py, `CLAUDE.md:92`) | the Teams tools; rule 34's lane name | 2 tools; `~<MACRO><n>` |
| get_agent_status | BBGTerminal liveness | OFFLINE = idle heartbeat; MSTR measured it consuming |
| safe-commit.sh | this log | -- |

- **What failed:** I named `~Z` as the surviving lane (35104) before reading rule 34, which names the lane `~NFRA1`. I corrected it in 35108 within 2 minutes.
