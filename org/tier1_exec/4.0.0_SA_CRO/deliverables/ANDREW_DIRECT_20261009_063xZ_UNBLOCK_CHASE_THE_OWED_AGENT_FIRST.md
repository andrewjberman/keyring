# ANDREW-DIRECT 2026-10-09 ~06:3xZ -- /unblock: first chase whoever was supposed to do the work, until an ack

**Channel:** Andrew at the 4.0.0_SA_CRO terminal, laptop, 2026-10-09 ~06:30Z (02:30 ET), after this seat's /unblock dated-wait
fix (@d2012292b9).

## Verbatim

> Yeah something that should be worked into the unblock is one of the first things that should be checked is if some other agent was supposed to do something, and didnt. need to assess if that agent is actually live first of all, which means if its same box, run /unstick peek. if another box, have the mstr on your box write the mstr on the other box and they run /unstick peek and see whats going on with the agent in question. If they are not present, they need to be spawned, if they are present but just busy I recommend the following strategy, which requires a screenshot of the duration of their query and the amount of tokens spent. If that number is 10:1, e.g. 10min and 1k tokens, that agent is hung, and most likely their whole box is hung. This happens with bad surprise rows and etc, its always a gitops failure issue, often times happens at sitez they are the worst with this, but it can happen elsewhere. If that is the case and it is possible to get that information, then the work needs to be relocated to another box, preferably the same box where the request originated. If that can't be done, e.g. it has to be done on sitez because it needs some local bbg files, then it is just noted that it has to be handled when sitez clears up. This is a very specific case, and usually it is enough to just tell the agent to follow the trail of "who was supposed to be working on this" and chase it down. The main thing is that it cannot be allowed to slide. The agent has to chase down whoever was supposed to do that work, nudge them, push until they get an ack. If they can't get an ack, like the example i gave, they need to figure out the workaround from there and document it.

## Placement (no scope adjudicated)

- Owner of `/unblock` and `.tools/unblock.py`: `4.0.0_SA_CRO~B`, not live; built by `4.0.0_SA_CRO` (this seat).
- The chase is the FIRST check of the `/unblock` flow, ahead of writing to the CRO. Its result is carried in the case file, so
  it cannot slide silently.
- `/unstick --peek` is operator-initiated by its own skill text (it steals focus). This record is Andrew's word for its use in
  the chase.
- Changes other seats' work (every COO driving a project; each box's MSTR for the cross-box peek and the spawn): one line to
  `1.0.0_SA_CTO` naming this record.
