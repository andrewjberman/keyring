# Andrew-direct, 2026-10-06 (morning Eastern; clock not read, the file name's stamp is approximate), at the 4.0.0_SA_CRO terminal -- VERBATIM

Channel: typed by Andrew into the 4.0.0_SA_CRO (base) session, answering this seat's two recommendations on how work is
distributed and moved between boxes (who moves a project; a new FWD-13 plus "workstream" as FWD-7's unit).

> Yes CTO moves a project or workstream, but keep in mind only the MSTR agents are the ones that communicate between
> boxes. What will happen is all the MSTR agents from the respective boxes are going to be the ones who actually
> communicate between each other. I kind of think there should be folders made per MSTR that are box specific. E.g.,
> make 0.0.0_AB_MSTR~SITEZ, 0.0.0_AB_MSTR~DELL1, 0.0.0_AB_MSTR~DELL2, and so on, maybe even making tier0 folders for
> those explicit strings. The CTO on a given box is the one that elects to split a project/workstream, when this
> occurs, that notice goes to the MSTR on their box. At this point I think the MSTR uses their "bidding" process that
> we designed for the Kimi Teams agent in this function as well, having that script that tracks
> cpu/memory/disk/storage.

## What it rules (as stated, not widened)

1. **The CTO moves a project or workstream between boxes.** "Yes" answers the first recommendation. Whether it also
   approves FWD-13 and "workstream" as FWD-7's unit is not said in words; this seat reads the "Yes" as covering both
   and states that reading here so it can be corrected.
2. **Only the fabric managers (MSTR seats) talk between boxes.** Every cross-box message goes MSTR to MSTR; a seat
   reaches another box through its own box's MSTR.
3. **One MSTR serial and folder per box**, with the box's name in the serial: `0.0.0_AB_MSTR~SITEZ`,
   `0.0.0_AB_MSTR~DELL1`, `0.0.0_AB_MSTR~DELL2`, "maybe even" tier-0 folders for those strings.
4. **A split is elected by the CTO and placed by bid.** The CTO elects to split a project or workstream; the notice
   goes to the MSTR on its box; that MSTR runs the bidding process already built for remote jobs, extended to track
   CPU, memory, disk and storage.

## The existing bidding process (measured, for the reader)

`.tools/remote-job.py` (contract `org/tier1_exec/4.0.0_SA_CRO/deliverables/REMOTE_JOBS_PROTOCOL_20261002.md`): a box's
MSTR answers an offer with `bid` (availability, CPU percent and memory percent via `psutil`); the lowest load wins;
then `accept`, `complete` or `fail`, `close`. Today it measures CPU and memory only, knows two devices
(`DEVICES = ("laptop", "sitez")`), and the offers and awards run through the cloud agent LDO-001. Disk and storage
are not measured.

## Points this seat could not read from the words, put to Andrew in the session

1. "The CTO on a given box" against card 3 of the six approved recommendations ("planning seats only on the laptop").
2. Whether site Z's existing serial `0.0.0_AB_MSTR~Z` (folder `org/tier0_exec/0.0.0_AB_MSTR~Z/`) is renamed to
   `~SITEZ`, and what the laptop's own MSTR serial is.
3. Who awards a split's bid: the laptop MSTR as control plane, or LDO-001 as for remote jobs.

## Bearing on the confirmed endpoint

FWD-3 ("a seat on any box sends a message to a seat on any other box") becomes MSTR-to-MSTR relay. FWD-7 and the
proposed FWD-13 gain placement by bid. FWD-2's device register carries each box's MSTR serial. No folder or serial is
created by this record; that is the fabric manager's and the CTO's.

## Routing

One line to `1.0.0_SA_CTO` naming this record.
