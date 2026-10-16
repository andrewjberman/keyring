# Andrew-direct 2026-10-16 ~23:40Z, at the 2.0.0_SA_COO~S1 terminal (dell1)

VERBATIM, one message:

> we need to have a mechanism with the globgrph lambda where it can do a print out to the desktop on this machine.

**Recorded by:** 2.0.0_SA_COO~S1, 2026-10-16T23:40:39Z (terminal, no broker channel).

**Reading taken (the issuer's, not Andrew's, and stated to him in the reply):** a way for a group member to ask the door `globgrph-trino-access-lambda` (SOC2_MSLOGS) for a result and have it land as a
file on this machine's Desktop. The door runs in AWS and cannot push to a laptop; the file is written by the CALLER'S client after it invokes the member alias, so the mechanism is the read client (`data/m365_metadata/scripts/silver/read_timeline.py`
and the later C-READS reads) gaining an output-to-Desktop option. The file holds the door's answer only, the Desktop folder is derived from the user profile (never typed), and nothing is sent anywhere.

**Status:** not built. Round 1's issuance is closed to new orders (ONE ISSUER PER ROUND), so this joins the round-N enrichment list for the CTO. Usable today without code: `python read_timeline.py ... > "%USERPROFILE%\Desktop\<name>.txt"`.
