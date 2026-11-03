from pathlib import Path

import mujoco


MODEL_PATH = Path(__file__).parent.parent / "models" / "one_joint_arm.xml"
INITIAL_ANGLE_RAD = 0.8
SIMULATION_STEPS = 500


def main() -> None:
    model = mujoco.MjModel.from_xml_path(str(MODEL_PATH))
    data = mujoco.MjData(model)

    data.qpos[0] = INITIAL_ANGLE_RAD
    mujoco.mj_forward(model, data)

    print(f"Initial angle: {data.qpos[0]:.3f} rad")
    print(f"Initial velocity: {data.qvel[0]:.3f} rad/s")

    for _ in range(SIMULATION_STEPS):
        mujoco.mj_step(model, data)

    print(f"Simulation time: {data.time:.3f} s")
    print(f"Final angle: {data.qpos[0]:.3f} rad")
    print(f"Final velocity: {data.qvel[0]:.3f} rad/s")


if __name__ == "__main__":
    main()