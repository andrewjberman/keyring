import { expect, test } from 'bun:test'
import { readSubmissionRequest } from './src/pages/InvestorReporting/contracts/submission-request'
import { LiveClient } from './src/api/endpoints/investor-reporting'
import fixture from './actual-composition.json'

test('fresh actual retained prospect fixture is admitted and deeply detached', () => {
  const raw = structuredClone(fixture.browser)
  const parsed = readSubmissionRequest(raw)
  expect(parsed).toEqual(raw)
  raw.comparison_keys.push('later-source-change')
  raw.prepared_for = 'later label'
  expect(parsed).toEqual(fixture.browser)
})

for (const label of ['A', 'é', 'e\u0301', '🌍'.repeat(200), '  <>&" recipient  ']) {
  test(`exact Unicode recipient survives client serialization ${JSON.stringify(label).slice(0, 35)}`, async () => {
    const body = { ...fixture.browser, prepared_for: label }
    let captured: unknown
    const api = new LiveClient({ transport: { async request<T>(_url: string, init: { body?: string }): Promise<T> {
      captured = JSON.parse(init.body!)
      throw new Error('offline transport sentinel')
    } }, telemetrySink: () => undefined })
    await api.submitAnalysisRequest(body).catch(() => undefined)
    expect(captured).toEqual(body)
  })
}

const invalid = [
  { prepared_for: null }, { prepared_for: ' ' }, { prepared_for: '\u0000' },
  { prepared_for: '\u0080' }, { prepared_for: '\udfff' }, { prepared_for: '🌍'.repeat(201) },
  { owner: {} }, { resolved: {} }, { source_descriptors: {} }, { principal_id: 'other' },
  { account_ids: ['injected'] }, { snapshot_id: 'injected' }, { client_id: 'injected' },
  { input_id: `portfolio_${'A'.repeat(64)}` }, { comparison_keys: ['unknown'], variant: 'overview' },
  { comparison_keys: ['duplicate', 'duplicate'], variant: 'multicomp' },
]
for (const [index, patch] of invalid.entries()) {
  test(`invalid boundary refuses before transport ${index}`, () => {
    let calls = 0
    const api = new LiveClient({ transport: { async request<T>(): Promise<T> {
      calls++
      throw new Error('must not send')
    } }, telemetrySink: () => undefined })
    expect(() => api.submitAnalysisRequest({ ...fixture.browser, ...patch } as any)).toThrow()
    expect(calls).toBe(0)
  })
}

test('missing required recipient refuses; title cannot substitute', () => {
  const { prepared_for: ignored, ...old } = fixture.browser
  expect(ignored).toBeTruthy()
  expect(() => readSubmissionRequest(old)).toThrow()
})

test('valid custody keeps title recipient and selected identities separate', () => {
  const { input_id: ignored, ...rest } = fixture.browser
  expect(ignored).toBeTruthy()
  const custody = { ...rest, client_id: 'c', snapshot_id: 's', account_ids: ['acc-a'],
    prepared_for: 'display-only', report_title: 'distinct-title', comparison_keys: ['b', 'a'], variant: 'multicomp' }
  expect(readSubmissionRequest(custody)).toEqual(custody)
})
