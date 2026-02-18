# Test Strategy (v0.1)

## Purpose

Define the minimum test strategy required to pass the `v0.1` gate.

## Test Objectives

- Verify embodied control stability on early hardware.
- Verify bio-inspired perception preprocessing outputs.
- Verify safety and fault-handling behavior.
- Ensure requirement-level traceability.

## Test Levels

- L1 Module tests:
- message schema validation
- preprocessing transform correctness
- watchdog logic and threshold logic
- L2 Integration tests:
- sensor-to-control-to-actuator loop behavior
- calibration workflow and startup transitions
- L3 System demonstrations:
- orient-to-sound behavior
- visual fixation/tracking behavior
- repeatable calibration and telemetry output

## Validation Target Mapping

| Validation Target | Required Tests | Pass Condition |
|---|---|---|
| VT1 Stable closed-loop control (3-4 DoF) | IT-01, ST-01 | No unstable oscillation in baseline tracking scenarios; loop timing and command outputs remain within configured bounds |
| VT2 Orient-to-sound | IT-02, ST-02 | Directional cue estimate drives consistent orienting response in repeated trials |
| VT3 Visual fixation/tracking | IT-03, ST-03 | Reduced-resolution vision pipeline supports consistent target fixation/tracking behavior |
| VT4 Repeatable startup calibration | IT-04, ST-04 | Consecutive startup runs complete calibration successfully and produce comparable calibration metrics |

## Requirement Traceability Matrix

| Requirement | Test IDs |
|---|---|
| R1 | IT-01, IT-02, IT-03 |
| R2 | MT-01, IT-01 |
| R3 | IT-01, ST-01 |
| R4 | MT-02, IT-03 |
| R5 | MT-03, IT-02 |
| R6 | MT-04, IT-01 |
| R7 | MT-05, ST-04 |
| S1 | MT-06, IT-05 |
| S2 | MT-07, IT-05 |
| S3 | MT-08, IT-05 |
| S4 | IT-04, ST-04 |
| N1 | IT-01, ST-01 |
| N2 | IT-05 |
| N3 | MT-09 |
| N4 | This document + `docs/requirements.md` consistency review |

## Test Case List

- MT-01 Message contract conformance:
- inject representative messages on each channel
- verify schema, version, timestamp, and sequence validation
- MT-02 Vision preprocess correctness:
- verify expected format and range of contrast/foveated outputs from test frames
- MT-03 Audio preprocess correctness:
- verify banded outputs and directional cue outputs from synthetic and recorded audio
- MT-04 Virtual-muscle interface behavior:
- verify effort/tension commands map correctly to actuator-level intents
- MT-05 Telemetry integrity:
- verify required fields, monotonic timestamps, and event ordering
- MT-06 Range limit enforcement:
- verify out-of-range commands are clamped/rejected safely
- MT-07 Current/thermal guard behavior:
- simulate threshold breach and verify mitigation behavior
- MT-08 Watchdog behavior:
- simulate module timeout and verify safe-mode transition
- MT-09 Configuration externalization:
- verify runtime reads parameter sets from external config and records version metadata
- IT-01 Closed-loop baseline tracking:
- run 3-4 DoF tracking scenario under nominal conditions
- IT-02 Orient-to-sound integration:
- present controlled directional audio inputs and verify orienting outputs
- IT-03 Visual tracking integration:
- present moving target input and verify fixation/tracking control outputs
- IT-04 Startup and calibration flow:
- verify startup state machine phases and calibration completion criteria
- IT-05 Fault injection and graceful degradation:
- inject communication loss, invalid sensor frames, and guard threshold triggers
- ST-01 System demo: stable embodied control.
- ST-02 System demo: orient-to-sound.
- ST-03 System demo: visual fixation/tracking.
- ST-04 System demo: repeatable calibration and telemetry package.

## Test Data and Artifacts

- Synthetic test vectors for vision/audio preprocess.
- Recorded sensor datasets for repeatable integration runs.
- Telemetry logs per run with configuration hash/version.
- Test report template with pass/fail, metrics, and anomalies.

## Exit Criteria for v0.1 Test Gate

- All validation targets VT1-VT4 pass.
- No unresolved critical safety defects.
- Requirement traceability matrix is complete and current.
- Reproducible test evidence is stored with run metadata.
