# SIGN-OFF (1.0.0_SA_CTO half) -- UI walk window 26: Andrew's three-variant automated-submission proof

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W26_20260930.md` @`d052be1db4`, blob prefix `0b209ba6`
(2.0.0_SA_COO~Y msg 103174). The blob prefix was printed here from `git hash-object` on the file. **Signed:** 1.0.0_SA_CTO, 2026-09-30 ~05:5xZ.
The 4.0.0_SA_CRO half is asked separately.

## Read at signing
- **Per-use word:** the packet quotes Andrew-direct 2026-09-30 ~04:4xZ verbatim: "I think we need to do a test to actually prove an automated ycharts submission for each of the
  three variants right now ad hoc and see if we even get a generated export." The vendor calls are the three bodies of this one window and nothing wider. I read the quote in the packet, not the record file.
- **The act:** one login, three serialized bodies (Overview, Comparison, Multi) for cottonwood on the same W15 CSV, cap 150 minutes (arithmetic shown: about 110 plus margin), no retry of any body.
- **Both branches:** an arm that fails leaves its REQ as evidence and files a BLOCKING row the same tick, and the remaining arms still run; a misbehaving resident closes the window and retains the principal.
  Every arm is a write the principal owns plus reads; no code, IAM, schedule, deploy or resident restart.
- **The one change (W26-3):** K1 is deleted only when all three jobs are terminal, because deleting it over a live job is what made REQ-86f1ce70 unrunnable (S231). A retained K1 has no credential, so it cannot log in.

## Conditions (each a stop)
1. **Second-seat credoff, agreed before opening.** `0.0.0_AB_MSTR` is to run `walk_principal.py --kind=uiwalk credoff <epoch>` and read back `ParameterNotFound` before K4. MSTR's acceptance of that act is
   recorded in the ledger before the window opens; if MSTR has not accepted, the window does not open. It must not fall back to the walker doing both halves.
2. **Pins re-read at create** (resident root and worker sha, unit active, the Lambda version, queue, DLQ baseline 1) and written in the ledger. Any difference means the window does not open.
3. **Serialized on the `irpt-jobs` terminal**, not on the K5 acceptance: `irpt-generation` read 0/0 and no non-principal job live immediately before each K5.
4. **DLQ read before and after.** Growth over the baseline of 1 is a BLOCKING row the same tick.
5. **No replay:** a challenged vendor mutation is never replayed, no fourth arm, no second login. The window closes at 150 minutes.
6. **A retained K1** (cap arrives with a job non-terminal) is recorded as CAP-TRUNCATED with the job id; K1-CRED must read as gone; K1 is deleted later under its own ledger note once its jobs are terminal.
7. **Censuses:** the users census and `walk_window_census.py` before and after, printed.
8. **Reporting discipline:** each arm's result is its named terminal `irpt-jobs` state and, for READY, the original vendor PDF object and certified report. Conclusions about the vendor or the body shape are limited to
   what the three results show; three results of one shape do not settle a fourth variant.

## Not covered
A retry, a restart of the resident, a code or IAM change, a new vendor account, REQ-86f1ce70 revived or deleted, and any use of Andrew's word beyond this window.

## RE-AFFIRMED on amendment 1 (1.0.0_SA_CTO, 2026-09-30 ~06:0xZ)

Packet blob is now `1c88bb49` (@`628d7e7602`; was `0b209ba6`). The blob prefix was printed here from `git hash-object` and matches the ask. I read the diff (`d052be1db4..628d7e7602`): a NARROWING that replaces "queue 0/0"
with the W26-5 SOLO GATE and names two stranded jobs (`REQ-86f1ce70...`, `REQ-3a1b73a8...`); no arm, login, retry or reach is added. Conditions 1-8 above stand, condition 3 read as the SOLO GATE. One addition:
9. **The gate's state list comes from the job state machine, not from the amendment's text.** The amendment names QUEUED, CLAIMED, SUBMITTING and SUBMITTED; earlier packets also name RESOLVING. Before the window, derive the full non-terminal
   set from the source of the job states, print the enumeration beside the gate, and treat any non-terminal state as blocking. The two stranded ids are excluded by exact id only.
