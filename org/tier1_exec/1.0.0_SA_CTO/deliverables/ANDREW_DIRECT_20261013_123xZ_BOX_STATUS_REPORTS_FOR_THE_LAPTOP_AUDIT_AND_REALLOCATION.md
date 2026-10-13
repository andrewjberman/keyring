# Andrew-direct 2026-10-13 ~12:3xZ (laptop, 1.0.0_SA_CTO terminal) -- a structured status report from every box, written by each box's CRO, for the laptop audit and this week's reallocation

VERBATIM: "I need a request to go out to each box via MSTR that they need to write a structured status report which you will
design ahead of the broadcast. The premise is that we want to know what projects they are working on, the likes of which are
touching what repo (ajb_workspace, portal, opal_ai). We want to know the current status of these projects, what the dependencies
and blockers are, what needs to be accomplished next, the desired outcome of these projects, whether or not these projects are
client-facing, and any other details you think might be relevant to include in the form. The reason we want these, is because we
want to run an audit on the laptop box and establish how we will reallocate, because I think there are a lot of projects that
are less of a priority and it makes more sense for us to really pare down and establish what is necessary for the drive this
week. Please design the form as requested, then get it issued via MSTR, and have 4.0.0_SA_CRO on each box (including the laptop
4.0.0_SA_CRO) be the one that does the research and puts the file together. Ping me when all four are done and on this box for
review."

## Applied

| term | value |
|---|---|
| the form | `org/tier1_exec/1.0.0_SA_CTO/deliverables/BOX_STATUS_REPORT_FORM_20261013.md` (this seat designed it before the broadcast) |
| the validator | `python .tools/box-status-report-check.py <file>` (required keys, denominators, one YAML block per project) |
| the author on each box | that box's `4.0.0_SA_CRO` lane (laptop: `4.0.0_SA_CRO` base; site Z: `4.0.0_SA_CRO~Z`; dell1 and dell2: the box's CRO lane, spawned by the box manager in the MP-20261010 format if none is live) |
| the file each writes | `org/tier1_exec/4.0.0_SA_CRO/deliverables/BOX_STATUS_REPORT_<box>_20261013.md`, box in {laptop, sitez, dell1, dell2}; committed on the box's branch; it reaches the laptop through CLOUD |
| the route | `0.0.0_AB_MSTR` broadcasts the ask to `~Z`, `~DELL1`, `~DELL2` (each delivers to its CRO); this seat asks the laptop CRO directly |
| due | 2026-10-13 16:00Z (the ask names the clock; a later file is still taken) |
| the ping | this seat pushes Andrew one line when all four files are on the laptop and pass the validator |
| what the reports feed | the laptop audit and this week's reallocation; the CRO's own KEEP / PARK / CLOSE / MERGE recommendation per project is part of the form, Andrew decides |
