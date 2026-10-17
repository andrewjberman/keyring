# Andrew-direct, 2026-10-17 ~02:5xZ, at the 1.0.0_SA_CTO~DELL2 terminal

**Verbatim:**
1. "let's just use the match sheet from DELL1 for now"
2. "have MSTR reach out to DELL1 to get /tdrop of the folder. there is a lot of data on this"

**Context:** they came minutes after `~D2` reported that Cottonwood has no advisor ownership map. Without one, Cottonwood advisor and client
viewers see nothing; Global staff are unaffected (`_scope/resolve.py:445-469`).

**This seat's reading, open to dell1's correction:** the match sheet is dell1's Cottonwood advisor-to-client (or account) match. It serves "for
now" as the source of the Cottonwood ownership map.

**Acts:**
- `0.0.0_AB_MSTR~DELL2` asks dell1, through its MSTR, for a `/tdrop` of the folder.
- **Handling:** the folder holds client data, so it lands OUTSIDE the repository (the containment ruling of 2026-10-09). Only counts and
  hashes are ever committed, and nothing is pushed.
- `~D2` then builds the Cottonwood ownership map from it, in its own cell.

-- `1.0.0_SA_CTO~DELL2`
