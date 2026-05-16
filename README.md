# AI-Powered Vehicle Face-ID Immobilizer

This open-source module provides a biometric authentication system designed for commercial fleet management, advanced driver-assistance systems (ADAS), and Driver Status Monitoring (DSM) integration. 

The system prevents unauthorized vehicle operation by verifying the driver's identity via an in-cabin camera before enabling the ignition system.

## Key Features
* **Biometric Driver Verification:** Utilizes convolutional neural networks (CNN) to match the real-time driver video stream with the authorized Driver ID database.
* **Hardware Immobilization Control:** Interfaces with vehicle ignition relays to safely lock/unlock the starter motor.
* **Fail-Safe Architecture:** The software operates strictly during the *pre-ignition phase*. It cannot interrupt engine power while the vehicle is in motion, ensuring compliance with automotive safety standards.

## System Architecture & Workflow
1. **Driver Entry:** The system activates when the vehicle cabin door opens or the accessory power (ACC) turns on.
2. **Face Detection:** The in-cabin camera captures the driver's face.
3. **Identity Matching:** The Edge AI module processes the image and extracts facial vectors, comparing them against the local encrypted database.
4. **Action:** * **Match Found:** The system triggers the relay to unlock the ignition.
   * **No Match / Unknown Person:** The vehicle remains immobilized, and a security log (with a snapshot) is prepared for fleet dispatch transmission.
  
```mermaid
graph TD
    A[Vehicle ACC ON / Door Opened] --> B[Activate In-Cabin Camera]
    B --> C{Face Detected?}
    C -->|Yes| D[Extract Facial Vectors via Edge AI]
    C -->|No| B
    D --> E{Match with Local Database?}
    E -->|Authorized| F[Trigger Relay: UNLOCK Ignition]
    F --> G[Engine Start Permitted]
    E -->|Unauthorized| H[Trigger Relay: LOCK Ignition]
    H --> I[Security Alert & Fleet Dispatch 

  * **No Match / Unknown Person:** The vehicle remains immobilized, and a security log (with a snapshot) is prepared for fleet dispatch transmission.

```mermaid
graph TD
    A[Vehicle ACC ON / Door Opened] --> B[Activate In-Cabin Camera]
    B --> C{Face Detected?}
    C -->|Yes| D[Extract Facial Vectors via Edge AI]
    C -->|No| B
    D --> E{Match with Local Database?}
    E -->|Authorized| F[Trigger Relay: UNLOCK Ignition]
    F --> G[Engine Start Permitted]
    E -->|Unauthorized| H[Trigger Relay: LOCK Ignition]
    H --> I[Security Alert & Fleet Dispatch Log]

