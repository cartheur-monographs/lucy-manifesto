# GA144 Architecture Spec (v0.1)

## Goal

Define the `v0.1` runtime and module architecture for a GA144-based Lucy platform.

## Design Principles

- Distributed execution over centralized monolith.
- Deterministic module interfaces and timing.
- Embodied control loops first, higher cognition later.
- Safety constraints applied at runtime boundaries, not only in application logic.

## System Context

- On-device compute: GA144 node fabric for real-time control/perception paths.
- Host-side support: development tools, telemetry capture, analysis, and optional supervisory tasks.
- Mechatronics: head/arm joints with sensor feedback and actuator control.
- Perception: monocular camera and dual microphones in `v0.1`.

## Logical Module Partition

- M1 Sensor Ingest:
- camera ingest and downsampling
- microphone ingest and framing
- joint state and health sensor ingest
- M2 Perception Preprocess:
- vision contrast/foveation transforms
- audio band decomposition and directional estimation
- M3 Integration/Reflex:
- orienting reflexes
- baseline tracking coordination
- calibration state machine
- M4 Motor Interface:
- virtual-muscle command translation
- low-level actuator command output
- limit enforcement hooks
- M5 Safety Supervisor:
- watchdogs
- range/current/thermal checks
- safe-mode transitions
- M6 Telemetry:
- timestamped event/trace output
- run metadata and configuration capture

## Inter-Module Messaging

- Transport model: deterministic message passing.
- Contract style: fixed message schemas per channel.
- Required channel classes:
- sensor frames
- state estimates
- control intents
- actuator commands
- safety events
- telemetry events
- All control-relevant messages include:
- monotonic timestamp
- module source id
- sequence counter
- payload version

## Timing Model (v0.1 Targets)

- Vision preprocess loop: best-effort real-time at reduced resolution.
- Audio directional loop: fixed-period frame processing.
- Motor control loop: fixed-period control cycle with jitter monitoring.
- Safety loop: independent watchdog and threshold checks at equal or faster cadence than motor loop.

## Calibration and Startup

- Startup phases:
- P1 hardware/interface check
- P2 sensor sanity check
- P3 joint calibration routine
- P4 closed-loop readiness confirmation
- Calibration outputs are persisted as versioned parameter sets and included in telemetry header.

## Failure Handling

- Failure classes:
- recoverable transient
- degraded operation
- fatal/safe-stop
- On module timeout or invalid data:
- raise safety event
- transition affected path to degraded or safe mode
- continue telemetry for root-cause analysis

## Implementation Constraints (v0.1)

- Prefer simple, explicit state machines over opaque adaptive logic in safety-critical paths.
- Keep perception preprocessing bounded and inspectable.
- Maintain host-independent minimal runtime behavior for core control loops.

## Deliverables for Architecture Gate

- Module graph with channel definitions.
- Initial message schema definitions.
- Runtime state machine definition for startup/calibration/safe-mode.
- Configuration parameter registry and versioning rules.
