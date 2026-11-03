from pathlib import Path

import mujoco


MODEL_PATH = Path(__file__).parent.parent / "models" / "one_joint_arm.xml"

TARGET_ANGLE_RAD = 0.0
INITIAL_ANGLE_RAD = 0.8

KP = 30.0
KD = 5.0
SIMULATION_SECONDS = 2.0


def compute_pd_torque(
    target_angle: float,
    current_angle: float,
    current_velocity: float,
) -> float:
    """Use PD control to calculate the joint motor torque."""
    angle_error = target_angle - current_angle
    return KP * angle_error - KD * current_velocity


def main() -> None:
    model = mujoco.MjModel.from_xml_path(str(MODEL_PATH))
    data = mujoco.MjData(model)

    data.qpos[0] = INITIAL_ANGLE_RAD
    mujoco.mj_forward(model, data)

    total_steps = int(SIMULATION_SECONDS / model.opt.timestep)

    print(f"Initial angle: {data.qpos[0]:.3f} rad")
    print(f"Target angle: {TARGET_ANGLE_RAD:.3f} rad")

    for _ in range(total_steps):
        torque = compute_pd_torque(
            TARGET_ANGLE_RAD,
            data.qpos[0],
            data.qvel[0],
        )
        data.ctrl[0] = torque
        mujoco.mj_step(model, data)

    print(f"Final angle: {data.qpos[0]:.3f} rad")
    print(f"Final velocity: {data.qvel[0]:.3f} rad/s")


if __name__ == "__main__":
    main()