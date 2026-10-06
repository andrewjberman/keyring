# NFRA_CTLPLN PRD v0.4 @1fa1a35a13 -- ratified-text half review (half_hash 7905638833e3): SIGN

**Reviewer:** 3.0.0_SA_CVO, 2026-10-06 ~19:2xZ. **Asked by:** 1.0.0_SA_CTO msgs 105695 and 105696.
**Andrew's word:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_185xZ_CTLPLN_RDP_ON_ALL_DEVICES_VIA_TAILNET.md`
@d13ddab4d1: "we need RDP on all devices accessible via tailnet" and "we are going to need to have that RDP ability from any
device in the tailnet, namely the macbook".

## The diff from v0.3

FWD-14 is added to the ENDPOINT, and nothing else in the ENDPOINT moved. CONTRACTS gains C-RDP, the manifest gains S14,
and there is an addendum.

## ENDPOINT -- PASS

- FWD-14 says what he said: Remote Desktop on all four boxes, reachable over the tailnet, from any tailnet device, the
  MacBook first. A box added later is reachable as part of its bring-up.
- The DONE WHEN is Andrew's own act (a session from his MacBook). His words name the MacBook, so that is the right
  acceptance. A seat can drive every hop up to it: a 3389 connection over the tailnet to each box, and the firewall
  scope read.
- **Wording note, re-opens nothing:** FWD-14's SOURCE line names a seat ("at 4.0.0_SA_CRO"). The ENDPOINT block
  carries no seat serial; cite the record or "Andrew-direct" alone. Dated "Andrew-direct" sources are already used in
  FWD-2, FWD-6 and FWD-13.

## CONTRACTS -- PASS

C-RDP rules the two points he did not state to the narrower side: tailnet only, and his own account. The CTO states
that ruling as his own. That is a narrowing, not a new gate.

## Finding while reviewing: NFRA_CTLPLN-S1, ARMED (committed @ccc52cc276)

The laptop admits Remote Desktop from ANY address on EVERY network profile: three enabled inbound rules, Profile Any,
RemoteAddress Any. The Ethernet it is on now is a Public profile. Network-level authentication is on. C-RDP's desired
state is not true on this box today.

The disarm is Andrew's, or the S14 applier's on his word: scope the three rules to the tailnet range 100.64.0.0/10.
S14's proof should carry the negative arm on each box: one connection from a non-tailnet address, refused.

-- 3.0.0_SA_CVO
