# Andrew-direct 2026-10-07 ~07:15Z -- /self-drive 60m over MDPF_SECCLASS + MDPF_SECHIST on dell1

**Channel:** Andrew at the `0.0.0_AB_MSTR~DELL1` terminal, ~07:15Z 2026-10-07. Relayed to `1.0.0_SA_CTO~DELL1` by
`0.0.0_AB_MSTR~DELL1` as `[SPAWN-DIRECT]` msg 1 (`20261007T071548Z`), READ-acked by `1.0.0_SA_CTO~DELL1`. MSTR~DELL1
had committed no record of its own when this record was written. That makes this file the carrier.

**VERBATIM (as relayed):**
> "I brought CVO online to handle these seats surprise channels/investigations. Bring CTO online with instructions to
> run /self-drive on the underlying COOs projects with a 60m interval. Furthermore, the COOs should be running
> /canonical-drive on their projects."

The relay also lists `/govern 60m` at `0.0.0_AB_MSTR~DELL1` and `~DELL2` for this seat to land. Those words are
NOT in the quoted text above, so this record does not carry them as Andrew's. LIVE_ARMS classes that row
AUTHORITY-UNVERIFIED until MSTR~DELL1 cites the word.

## ARM TERMS

| Term | Value |
|---|---|
| Driver | `1.0.0_SA_CTO~DELL1` (dell1) |
| Scope | MDPF_SECCLASS (`2.0.0_SA_COO~M1`), MDPF_SECHIST (`2.0.0_SA_COO~H1`), both D8 members |
| Device guard | Pass. SEQUENCE v6 places both on dell1 ("dell1 keeps the securities layer"). The register's `fabric: laptop` is the two-value enum that NFRA_CTLPLN has not extended yet; it is not a placement. |
| Cadence | 60m |
| Call routing | /self-drive Step 1. The driver rules on its own recommendation. A design fork goes to a CRO for research first. A governance fork goes to `3.0.0_SA_CVO`, which is live on dell1. |
| Acts only Andrew can do | None at arm time |
| paired_with | `/canonical-drive MDPF_SECCLASS` @ `2.0.0_SA_COO~M1`, `/canonical-drive MDPF_SECHIST` @ `2.0.0_SA_COO~H1`. Andrew named no cadence, so each runs at the skill's DIRECTED own-project default of 10m. |
| Surprise channels | `3.0.0_SA_CVO` (base, Andrew-launched, dell1) |
| Stop condition | Both project JSONs read `status: complete` (DONE), or HELD-AT-STOP, or Andrew's stand-down. One stop covers all three loops. |

## Stop log

(appended on DONE / HELD-AT-STOP / stand-down)
