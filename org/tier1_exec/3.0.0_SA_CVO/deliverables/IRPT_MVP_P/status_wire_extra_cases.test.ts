// Appended after immutable original pairing assertions, with the same imports.
for (const [kind, pair] of Object.entries(outer.cases)) {
  test('public parser refuses injected server correlation for ' + kind, () => {
    const injected = structuredClone(pair.refusal) as any
    injected.status.internal_correlation_id = 'corr-must-stay-internal'
    expect(() => parseIrEnvelope(pair.refusal.operation, injected)).toThrow()
    expect(parseIrEnvelope(pair.refusal.operation, pair.refusal).refused).toBe(true)
  })
}
