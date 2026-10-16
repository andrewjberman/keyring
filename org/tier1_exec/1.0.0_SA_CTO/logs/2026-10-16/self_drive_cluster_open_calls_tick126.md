# self-drive cluster open calls -- ticks 125-126 (2026-10-16 ~21:3xZ to ~22:0xZ), 1.0.0_SA_CTO laptop

state: ARMED   cadence: 30m   cron: 9d30d669   ticks covered: 125-126 (125 was quiet, appended to `org/mcp/drive_ticks/1.0.0_SA_CTO.md`)
arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261011_032xZ_CTO_LEADS_CLUSTER_OPEN_CALLS_LOOP_60M.md`

## Measurements (tick 126, ~22:02Z)

- 4 boxes read. 10 open (2 fork, 7 act), 304 closed. By box: laptop 1, sitez 5, dell1 0, dell2 4.
- Open cross-adjudications: 0 (52 in total). Inbox: 0 unread. Msgs 109757 and 109760 were acked.
- Dell2 closed `6d61` on its own.

## Driver acts since tick 124

- **COMM_ASSIST CA-n-2 (the deploy of the 446a fix): CTO half SIGNED @314121c000,** on the COO half @f6d80f2b0b, PIN `1aa63bde67`.
  - The act: one targeted apply of `module.ldo_001`, code only, Branch A `0/2/0`, by `~COMM1`.
  - The three foreign registry files are accepted on the COO half's 17-of-17 address probes.
  - Condition 9 added: if the replies route is refused beyond the pinned thread, that is a defect and CA-n-3 is held.
  - The CVO half is still owed.
- **`XA-20261016T213506Z-8db5` (`dell2 9794`), @651de9c2e4.** Ruling: YES.
  - `~D2` resolves the two account ids by a read-only staff read and sends them to `~C2` by broker message only.
  - The ids go in no committed file. The trace records booleans, dates and counts only, under a label. Each firm's id is read
    against its own series only.
- **dell1 relay (MSTR msg 109760), from Andrew-direct ~21:40Z at the dell1 C1 terminal:** "request this to be done from the laptop, as
  its in the downloads there, have the laptop CTO figure out how to upload".
  - The key is X15's: `s3://opal-data-cottonwood/commonwealth/cottonwood/bronze/crm/date=2026-06-23/CRM_CottonwoodCapitalAdvisors.zip`.
  - Read live: all three `DenyRestricted*` statements are in the bucket policy. The only writer is
    `cloudops-cot-restricted-breakglass-role`, whose trust admits only `Andrew_Berman_Console`. The `commonwealth/` prefix is empty.
  - So the landing is **Andrew's console act**, by design (X15 condition 1).
  - The inner zip was extracted to `Downloads\CRM_CottonwoodCapitalAdvisors.zip`: 26,485,027 bytes, sha256 `daad5946...768d`.
  - Andrew has the CloudShell steps. There must be NO console "Create folder", because X15 allows ONE object.
  - Ask 2 answered PARTLY: only the `pipe()` reader and the HHID map in `matcher.py` are reusable; there is no silver builder. An
    agent identity cannot read the restricted prefix.
  - Relayed to `2.0.0_SA_COO~C1` and the dell1 CTO through MSTR. After his upload: this seat's refused read from an agent identity,
    then the landed key goes to C1.

## Calls this tick

- No open calls for this seat.
- `dell2 9794` is ruled and awaits dell2's close.
- New `dell2 3c22` (opened 21:51Z): the PRICE pages of the Opal-built report, and whether C-V1 is lifted for the Analysis Request
  variants. It goes to dell2's CTO first; it is not escalated here.

## Acts only Andrew can do (each with its citation)

- **NEW:** land the CRM zip under the restricted prefix as `Andrew_Berman_Console` through the break-glass role. This is X15
  condition 1: no agent may write there.
- `sitez 8ed7` and `sitez f0d2`; `sitez bd68` (REC: narrow); `sitez 5b35`.
- `laptop b87f`.
- NFRA_CTLPLN FWD-2, FWD-6 and FWD-27.
- The TCKT_MTADTA audit-log check with IT.
- Postponed: `sitez def4`, `dell2 c02c`.

## Completion test

NOT DONE. The scope ends only on his stand-down.

## Compiler Tools

- `open-calls.py list --all --cloud`: OK.
- `xadj.py show/rule/list`: OK.
- `.tools/aws` reads: s3api get-bucket-policy, iam get-role, list-objects-v2 (prefix `commonwealth/`). OK.
