# Drive log 2026-10-15 12Z-19Z, 2.0.0_SA_COO~C (NFRA_CTLPLN, rounds 18 to 22)

Substantive ticks only. All pins are commits on `box/laptop`, LOCAL.

- **~11:20Z, round 18 drained:** `CT-ah-1` merged `3f4730b5d3`; packet `c34d3f13fe`.
- **~12:08Z, round 19 issued** (`afebfdc81a`, six cells, outcome first) after the CTO's coverage correction (2 of 28 FWDs realized; rounds 13-18 were hygiene). FWD-3 and FWD-24 driven by crossbox calls; FWD-14 and FWD-17 filed for Andrew. Drained ~13:30Z (merges `192e5b2e31` to `f6a6ed1e6e`), packet `d359d2bd70`.
- **~14:08Z, round 20 issued** (`9cfc5f5fd8`, four cells). Drained ~15:00Z, packet `58a0c48950`. FWD-3 matrix read 12 of 12; site Z refused a download; fetch records carry a device key.
- **~16:08Z, round 21 issued** (`57922ec762`, three cells plus `CT-ak-4` by amendment `4d79c7c58c` after the CloudOps seat's lane refusal, row `S9130`). FWD-5 positive arm: one signed change, comment-only (`461e3f64ee`, the script fails ruff at HEAD), deployed exactly one S3 key by the integrator's box-sync (PINNED-DEPLOY 18:01:57Z; LD-0367 lets only the integrator push `box/laptop`, row `S9132`). Packet `445bca4969`. Cross-box reads: FWD-21 audit lines quoted into a committed record, FWD-14 box records from the MacBook on four boxes, FWD-11 dell1 restart time.
- **~19:08Z, round 22 issued** (`54e8947a06`, three cells): the duckdb journey's fetch and checks 1-7 (cp314, dell1's CTO), `crossbox-call.py ack` refuses a non-manager, one hygiene batch. Issuer reads: the Windows laptop's outbound remote-desktop client log shows attempts to dell1 (10-13 13:17Z, 13:18Z) and dell2 (10-10 13:55Z, 10-13 13:18Z), none to site Z, and the targets' event 1149 lists (already read) hold no connection from the laptop's address `100.96.167.100`: the Windows-laptop arm of FWD-14 is NOT on record.
- **Andrew's word (via the CTO, `c89b56abba`):** `7841` closed (he restarted dell1 at 15:46Z), `c9a4` open (remote desktop tonight), `318f` open (the duckdb record), `715c` executed.
- **Open:** calls `c9a4`, `318f`. Workers `~119`, `~120`, `~121` running.
