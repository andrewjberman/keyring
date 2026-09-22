import { expect, test } from 'bun:test'
import { LiveClient, NotYetExercisable, IR_ROUTE_TABLE, irBuildRequest } from './src/api/endpoints/investor-reporting'
import { parseIrEnvelope, EnvelopeMismatch } from './src/pages/InvestorReporting/contracts/envelope'
import actual from './actual-upload.json'
import routes from './docs/contracts/investor-reporting/v1/routes.json'

const fresh = () => structuredClone(actual.normalized.response)

test('independently regenerated guarded producer success and correction parse unchanged', () => {
  for (const sample of [actual.normalized, actual.correction]) {
    expect(parseIrEnvelope('analysis-input-upload', sample.response).data).toEqual(sample.response.data)
  }
})

test('complete route status, verb and path denominator equals pinned backend', () => {
  expect(IR_ROUTE_TABLE.map(r => [r.method + ' ' + r.pathTemplate, r.status]).sort())
    .toEqual(routes.routes.map(r => [r.route_key, r.status]).sort())
})

test('bound hash must identify both top-level and nested input, not merely agree with artifact hash', () => {
  const body = fresh()
  body.data.input_id = body.data.input_ref.input_id = 'portfolio_' + '0'.repeat(64)
  expect(body.data.input_ref.content_sha256).not.toBe('0'.repeat(64))
  expect(() => parseIrEnvelope('analysis-input-upload', body)).toThrow(EnvelopeMismatch)
})

test.each(['family', 'mutable', 'version', 'length', 'source'])('malformed receipt %s refuses', mode => {
  const body: any = fresh()
  const artifact = body.data.input_ref.artifact_ref
  if (mode === 'family') artifact.family = 'ORIGINAL_CSV'
  if (mode === 'mutable') artifact.immutable = false
  if (mode === 'version') artifact.version_id = 'null'
  if (mode === 'length') artifact.byte_length = 1.5
  if (mode === 'source') body.data.portfolio.source.upload_id = 'UP-' + 'f'.repeat(64)
  expect(() => parseIrEnvelope('analysis-input-upload', body)).toThrow(EnvelopeMismatch)
})

test('correction cannot carry an accepted input reference or document', () => {
  for (const property of ['input_ref', 'portfolio']) {
    const body: any = structuredClone(actual.correction.response)
    body.data[property] = (fresh().data as any)[property]
    expect(() => parseIrEnvelope('analysis-input-upload', body)).toThrow(EnvelopeMismatch)
  }
})

test('hidden retry serializes identical body and explicit lineage is preserved', () => {
  const request = { ...actual.normalized.request, supersedes_input_id: fresh().data.input_id }
  const first = irBuildRequest('analysis-input-upload', { body: request })
  const second = irBuildRequest('analysis-input-upload', { body: structuredClone(request) })
  expect(second).toEqual(first)
  expect(JSON.parse(first.body!)).toEqual(request)
})

test('unavailable route refuses repeated attempts with zero transport calls', async () => {
  let calls = 0
  const api = new LiveClient({ transport: { async request<T>() { calls++; return {} as T } } })
  for (let i = 0; i < 2; i++) {
    await expect(api.uploadAnalysisInput(actual.normalized.request)).rejects.toBeInstanceOf(NotYetExercisable)
  }
  expect(calls).toBe(0)
})
