# Project Outline: Lucy Manifesto Revitalization (GA144)

## Mission

Revitalize the original Lucy android program by preserving the author's core thesis:

- intelligence must be embodied
- sensors and actuators must be biologically meaningful
- intelligence should emerge from distributed interacting modules, not a single scripted controller

Implement this with a modern architecture centered on `GA144` manycore chips for low-power, massively parallel, real-time sensorimotor processing.

## What We Preserve From The Author

From `source.pdf`, we keep these design commitments:

- Body-first AI: build in hardware, not only simulation.
- Realistic sensorimotor loops: vision, hearing, proprioception, and muscle-like control.
- Bottom-up composition: many small processing units configured as functional building blocks.
- Developmental learning: avoid hard-coded symbolic behavior and let capability emerge through interaction.

## Why GA144 For The Revitalization

- High parallelism supports many simultaneous low-latency loops.
- Excellent power profile for always-on embedded cognition.
- Natural fit for distributed "microcircuit" style architecture aligned with Lucy's original philosophy.

Note: the source text emphasizes distributed microcontrollers (PIC-era design) rather than GA144 specifically; this project upgrades that architecture to GA144-class manycore implementation.

## System Vision (Lucy v2)

Lucy v2 is a torso/head/arms developmental android platform with:

- compliant, muscle-like actuation abstractions over practical motors
- biologically-inspired sensing pipelines (retina-like vision transforms, cochlea-like audio maps)
- layered learning loops from reflex to adaptive behavior
- distributed compute fabric on GA144 chips with explicit inter-core messaging

## Technical Architecture

### 1. Compute Fabric

- GA144 node clusters partitioned by function: sensor front-end, motor control, integration/reflex, learning/plasticity, and safety/supervisory.
- Deterministic message-passing protocol between clusters.
- Real-time telemetry and debug bridge to host workstation.

### 2. Embodiment Layer

- Upper-body kinematic platform (head, eyes, jaw, arms, hands-lite).
- Series-elastic or virtual-muscle control model to emulate antagonist muscle pairs.
- Joint sensing for position, velocity, effort estimate, and calibration state.
- Quiet-mechanics priority to avoid self-noise contaminating audio learning.

### 3. Sensor Layer

- Vision: low/medium-resolution monocular first, binocular second.
- Vision: foveated remapping and contrast-dominant preprocessing.
- Vision: edge/temporal-change channels for active vision experiments.
- Audio: microphone pair with phase/time-difference localization pipeline.
- Audio: cochlea-like band decomposition into tonotopic representation.
- Audio: directional attention map for "cocktail party" style source selection.
- Proprioception/touch: joint-angle and tension-derived body-state maps.
- Proprioception/touch: phased introduction of tactile patches for contact-rich learning.

### 4. Learning and Behavior Stack

- Level 0: reflexes (stabilization, gaze orienting, basic protective responses)
- Level 1: sensorimotor calibration (self-model alignment, limb calibration)
- Level 2: adaptive control (tracking, reaching, auditory orienting)
- Level 3: developmental behaviors (babbling, imitation, guided interaction)
- Level 4: symbolic interfaces (optional, only after robust embodied competence)

### 5. Safety and Reliability

- hard limits on joint range, current, and thermal load
- watchdog and fault-containment per cluster
- graceful degradation under node or sensor failure
- repeatable bring-up and calibration scripts

## Program Plan

### Phase A: Source-to-Spec (2-3 weeks)

- Extract requirements from `source.pdf` into testable engineering statements.
- Define Lucy v2 capability matrix (must/should/could).
- Write GA144 hardware/software architecture spec v0.1.

Deliverables:

- `docs/requirements.md`
- `docs/architecture-ga144.md`
- `docs/test-strategy.md`

### Phase B: Core Platform Bring-Up (4-6 weeks)

- GA144 dev stack, boot flow, messaging primitives.
- Minimal body rig and actuator control loop.
- Sensor ingest prototypes (camera + dual mic + joint sensors).

Deliverables:

- running distributed runtime on GA144
- closed-loop control of at least 3-4 DoF
- recorded sensor telemetry pipeline

### Phase C: Bio-Inspired Pipelines (6-8 weeks)

- vision preprocessing (foveation, contrast pathways)
- cochlea-like audio transform and source-direction map
- virtual-muscle abstraction with antagonistic control semantics

Deliverables:

- demonstrable orient-to-sound behavior
- visual fixation and simple tracking behavior
- reproducible calibration routine

### Phase D: Developmental Learning (8-12 weeks)

- motor babbling and self-calibration learning
- guided reaching and imitation primitives
- sensorimotor contingency learning experiments

Deliverables:

- benchmark suite for emergent behavior
- milestone demo: guided interaction session

### Phase E: Integration and Manifesto v1 (3-4 weeks)

- consolidate findings into revised Lucy Manifesto v1.0
- compare original assumptions vs. GA144-era outcomes
- publish architecture, experiments, and open challenges

Deliverables:

- `docs/manifesto-v1.md`
- `docs/results-and-gaps.md`

## Success Criteria

- Lucy v2 demonstrates stable embodied control in real hardware.
- At least two non-trivial behaviors emerge from learning, not scripted logic.
- Distributed GA144 architecture sustains real-time operation within power budget.
- Project produces a defensible, test-backed manifesto update.

## Immediate Next Actions (This Week)

- Create requirements extraction document from `source.txt`.
- Draft GA144 node allocation and interconnect map.
- Define v0 hardware BOM for torso/head/arms prototype.
- Stand up baseline simulation harness for sensorimotor loops before hardware integration.
