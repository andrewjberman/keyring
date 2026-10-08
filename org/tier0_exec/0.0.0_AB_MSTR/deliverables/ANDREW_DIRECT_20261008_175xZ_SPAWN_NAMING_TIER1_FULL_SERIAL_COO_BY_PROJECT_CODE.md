# Andrew-direct 2026-10-08 ~17:5xZ at the dell1 0.0.0_AB_MSTR~DELL1 terminal -- spawn naming

**Verbatim:** "Another thing that i need from you and from the DELL2 box is that when you are spawning agents, you need to be
spawning them with the following pattern. CTO/CVO/CRO spawned with full serial, e.g. 1.0.0_SA_CTO~DELL2. For COOs, they
need to be spawned as the project code they are working on, which should always just be one project code, e.g. NFRA_TRNSPT."

**Addressed to:** 0.0.0_AB_MSTR~DELL1 and 0.0.0_AB_MSTR~DELL2, about the seats each box's manager spawns.

**Rule as given:**
- CTO, CVO and CRO: the full serial with the box lane, e.g. `1.0.0_SA_CTO~DELL2` (on dell1: `1.0.0_SA_CTO~DELL1`,
  `3.0.0_SA_CVO~DELL1`, `4.0.0_SA_CRO~DELL1`).
- COO: named by the one project code it works on, e.g. `NFRA_TRNSPT`.

**Measured tool gap (not a ruling):** `.tools/spawn-agent.ps1:95` validates
`^[0-9]+\.[0-9]+\.[0-9]+_[A-Za-z]+_[A-Za-z0-9]+(~[A-Za-z0-9]+)?$`. A lane may not contain `_`, so
`2.0.0_SA_COO~NFRA_TRNSPT` is refused today. The exact COO serial form is put back to Andrew.

**dell1 seats spawned before this word (17:3xZ):** 1.0.0_SA_CTO~DELL1, 3.0.0_SA_CVO, 4.0.0_SA_CRO~DELL1,
2.0.0_SA_COO~M1, ~G1, ~H1, 0.7.0_AE_CloudOps~SD. Whether to re-seat live seats under the new names is put back to Andrew;
the word reads "when you are spawning".
