# /self-drive ~O fabric -- ticks 106-107 (1.0.0_SA_CTO~O, 2026-09-28 07:45Z-08:47Z)

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d.

- **MX-s-10** (port the scheduled asset-dim run to REST): AE~I PHASE A (@284cf7d702) ported the SSM document; step 2
  was REFUSED with its measurement: the scripts are published but their imports (`lib/`, the naming registry and
  schema) are absent from the whole opal-data-bd bucket. COO~O held step 2 in amendment A1 (@7b98791aeb) and routed it
  as row Z-S43.
- **Z-S43 RULED** by this seat (@e4b19b9898):
  - Firm-neutral lib code ships by the path `lib/etf_classifier.py` already took into opal-data-bd.
  - The registry resolves at BUILD time: an opal_naming `TARGET_REGISTRY_KEYS` target renders a GENERATED 49F pin
    (the `perfrp_firm_pin.py` precedent). The multi-firm registry never travels.
  - This seat commits the one-line `lib/opal_naming.py` entry (BASE_EXEC) when the worker has the pin.
  - Proof: regenerating gives identical bytes; `--help` runs on the instance with opal_naming absent.
  - COO~O told (inbox file 20260928T083421Z).
- Owed by this seat next: the `TARGET_REGISTRY_KEYS` entry; the MX-s-10 CTO never-widen half once PHASE A matches the
  current dim.

**Inbox:** 1 message in the span (COO~O 083013Z, Z-S43), acted. 0 unread at 08:47Z.

**Open calls in scope:** 0 new. **Cards at Andrew:**
- (1) URGENT: rotate the BD password.
- (2) The history-scrub scope.
- (3) The census as a commit gate.
- (4) The switchover sitting.

**Completion test:** NOT DONE. 0 of 4 projects are complete.

state: ARMED
