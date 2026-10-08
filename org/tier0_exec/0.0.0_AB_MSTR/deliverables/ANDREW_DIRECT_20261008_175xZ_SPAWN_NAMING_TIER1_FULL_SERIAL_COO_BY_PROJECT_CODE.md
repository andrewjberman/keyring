# Andrew-direct 2026-10-08 ~17:5xZ at the dell1 0.0.0_AB_MSTR~DELL1 terminal -- spawn naming

**Verbatim:** "Another thing that i need from you and from the DELL2 box is that when you are spawning agents, you need to be
spawning them with the following pattern. CTO/CVO/CRO spawned with full serial, e.g. 1.0.0_SA_CTO~DELL2. For COOs, they
need to be spawned as the project code they are working on, which should always just be one project code, e.g. NFRA_TRNSPT."

**Addendum, same terminal, minutes later, verbatim:** "Also, if there is a tier2 agent being launched, they should also be
launched with their full serial listed in the tab. If you want guidance for you and DELL2 on  how to do this, ask MSTR on the
laptop box, as they do it with every session launch, as does SITEZ". Asked of the laptop 0.0.0_AB_MSTR over the bus
(fe00d74b); its answer is relayed to 0.0.0_AB_MSTR~DELL2.

**Settled, same terminal ~19:0xZ, verbatim:** "Yes, this is just the tab in Powershell, not its actual registration. The
registration is always the full serial, as that is necessary for commits/mcp/etc". It answers the dell1 card "(a) what you see
vs (b) what the seat is called" with (a), and the later dell2 word (record 1ccced2e59: "FOR COOs they should not be using SERIAL
at all ... e.g. DSGN_IRPTV2") is read the same way: a COO's TAB shows its one project code, alone; it registers, commits and
receives mail as its full serial. Mechanism: `.tools/spawn-agent.ps1 <serial> -Tab <PROJECT_CODE>` (the tab title, passed to
`ajb.ps1` as `OPAL_TAB_TITLE`); every other seat's tab is its full serial. A title only holds where Windows Terminal has
`profiles.defaults.suppressApplicationTitle: true` (set on dell1 ~19:0xZ). Re-seating seats spawned earlier: not answered.

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
